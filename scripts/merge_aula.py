#!/usr/bin/env python3
"""Mergeia UMA aula por vez, com o CI conferido de verdade (REGRA 32).

    python3 scripts/merge_aula.py 1669              # confere e mergeia
    python3 scripts/merge_aula.py 1669 1671         # em ordem, um por vez
    python3 scripts/merge_aula.py 1669 --dry-run    # so diz o que faria
    python3 scripts/merge_aula.py 1669 --wait       # espera o CI concluir

POR QUE ESTE SCRIPT EXISTE
--------------------------
O `main` NAO tem branch protection (a API devolve 404). Nenhum check e obrigatorio
do lado do GitHub, entao `gh pr merge` mergeia PR VERMELHO sem reclamar. A unica
trava possivel e esta aqui.

E "verde" nao e obvio. O rollup mistura DUAS formas:

  CheckRun      -> status (QUEUED/IN_PROGRESS/COMPLETED) + conclusion (SUCCESS/...)
  StatusContext -> state  (SUCCESS/PENDING/FAILURE/ERROR)

O deploy preview da Vercel entra como StatusContext e fica **PENDING por tempo
indeterminado**. Exigir "todos SUCCESS" trava o merge pra sempre; aceitar
"nao-falhou" mergeia com o gate ainda rodando — foi assim que um PR vermelho ja
passou. A regra correta esta em `avaliar()`:

  - QUALQUER check com conclusao de falha  -> BLOQUEIA, sempre.
  - O check `gates` (o gate de qualidade real, .github/workflows/validate-lessons.yml)
    TEM de estar COMPLETED + SUCCESS. Ausente ou rodando -> NAO mergeia.
  - Checks de DEPLOY PREVIEW pendentes nao bloqueiam: sao previa, nao correcao,
    e o deploy de producao acontece depois do merge de qualquer forma.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

# Conclusoes de CheckRun que contam como "nao passou".
FALHA = {"FAILURE", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED", "STARTUP_FAILURE", "STALE"}
# Conclusoes que contam como OK (skipped/neutral nao sao erro).
OK = {"SUCCESS", "NEUTRAL", "SKIPPED"}
# O gate de qualidade que NAO pode faltar.
GATE_OBRIGATORIO = "gates"
# Checks de preview de deploy: pendencia neles nao bloqueia.
PREVIEW = re.compile(r"vercel|preview|netlify", re.I)


def gh(*args, parse=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)}: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout) if parse else r.stdout


def avaliar(rollup):
    """-> (veredito, [motivos]). veredito in {'ok','falhou','esperando'}."""
    # `gates` pode aparecer VARIAS vezes no rollup — cada rerun (ou cada
    # fechar/reabrir do PR, que e como a gente destrava checkout pendurado) soma
    # uma entrada. Todas sao do MESMO head SHA, entao um SUCCESS ja prova que o
    # codigo passou; uma duplicata ainda rodando e redundante, nao um bloqueio.
    # Guardar so a ULTIMA vista fazia o PR verde ficar preso — travou a aula 4 da
    # ana-luiza-sellmann com dois SUCCESS no rollup.
    falhas, pendentes, gates = [], [], []
    for c in rollup:
        nome = c.get("name") or c.get("context") or "?"
        if c.get("__typename") == "CheckRun":
            concluido = c.get("status") == "COMPLETED"
            conclusao = (c.get("conclusion") or "").upper()
        else:  # StatusContext
            estado = (c.get("state") or "").upper()
            concluido = estado not in ("PENDING", "EXPECTED", "")
            conclusao = estado
        if concluido and conclusao in FALHA:
            falhas.append(f"{nome}: {conclusao}")
        elif not concluido:
            pendentes.append(nome)
        if nome == GATE_OBRIGATORIO:
            gates.append((concluido, conclusao))

    if falhas:
        return "falhou", falhas
    if not gates:
        return "falhou", [f"o check '{GATE_OBRIGATORIO}' nao existe neste PR — "
                          "sem ele nao da pra afirmar que a aula passou"]
    if any(c and x not in OK for c, x in gates):
        return "falhou", [f"'{GATE_OBRIGATORIO}': "
                          + ", ".join(x for c, x in gates if c and x not in OK)]
    if not any(c and x in OK for c, x in gates):
        return "esperando", [f"'{GATE_OBRIGATORIO}' ainda rodando"]
    # Gate verde. Pendencia sobrando so bloqueia se NAO for preview de deploy —
    # e o proprio `gates` sai da conta: o veredito dele ja foi dado acima, e uma
    # DUPLICATA ainda rodando (rerun/reopen) nao pode desfazer um SUCCESS do
    # mesmo SHA. Sem esta excecao a aula 4 da ana-luiza-sellmann ficava presa com
    # dois SUCCESS e um rerun em andamento.
    trava = [p for p in pendentes
             if not PREVIEW.search(p) and p != GATE_OBRIGATORIO]
    if trava:
        return "esperando", [f"pendente: {', '.join(trava)}"]
    return "ok", [f"'{GATE_OBRIGATORIO}' SUCCESS" +
                  (f"; preview ignorado: {', '.join(pendentes)}" if pendentes else "")]


def url_coberta_por_redirect(caminho):
    """A URL deste arquivo continua respondendo depois de ele sumir?

    Le os `redirects` do vercel.json NO MAIN. Se houver um source apontando para a
    URL publica do arquivo, apagar o arquivo nao mata o link — a borda responde 308 e
    leva ao destino. Sem isso, apagar = 404 silencioso no link que a aluna ja tem.
    """
    if not caminho.startswith("public/") or not caminho.endswith(".html"):
        return False
    url = caminho[len("public"):]                      # public/aluno/x.html -> /aluno/x.html
    try:
        raw = subprocess.run(["git", "show", "origin/main:vercel.json"],
                             capture_output=True, text=True, check=True).stdout
        for r in (json.loads(raw).get("redirects") or []):
            if r.get("source") == url:
                return True
    except Exception:
        return False
    return False


def slugs_do_pr(arquivos):
    """Slugs de aluno tocados pelo PR — o merge tem de ser de UM aluno so."""
    achados = set()
    for p in arquivos:
        for rx in (r"^public/(?:professor|aluno)/([a-z0-9-]+?)(?:-aula\d+)?\.html$",
                   r"^public/audio/([a-z0-9-]+)/",
                   r"^_build/([a-z0-9-]+)-aula\d+/"):
            m = re.match(rx, p)
            if m:
                achados.add(m.group(1))
                break
    return achados


def _supabase():
    """URL + chave publicavel, lidas do MESMO arquivo que o site usa.

    Duplicar a chave aqui criaria uma segunda fonte que envelhece sozinha."""
    cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "public", "lib", "supabase-config.js")
    with open(cfg, encoding="utf-8") as f:
        txt = f.read()
    url = re.search(r"SUPABASE_URL\s*=\s*'([^']+)'", txt)
    key = re.search(r"SUPABASE_ANON_KEY\s*=\s*'([^']+)'", txt)
    return (url.group(1), key.group(1)) if url and key else (None, None)


def promover_status(slug):
    """Aluno que APARECE NO DASHBOARD COM MATERIAL e ativo E aprovado.

    Ordem do Dan, 31/07/2026: "apareceu no dashboard COM MATERIAL e ativo/aprovado".
    Aula mergeada e material NO AR, numa URL real — os dois campos que a dashboard
    le tem de refletir isso:

      * `perfis.status`  — ordena e CONTA: rascunho/em_revisao caem em "Em criacao",
        aprovado/material_publicado em "Em andamento". Perfil com aula no ar marcado
        como Rascunho mente na tela e some da contagem (foi o caso do Leonardo
        Constantino e da Lucia Nishiyama, corrigidos a mao em 30/07).
      * `perfis.ativo`   — e o que efetivamente ENTREGA o material ao aluno. Ate
        30/07 este script nao o tocava de proposito, tratando a revisao pedagogica
        como portao. O Dan reverteu: material gerado ja entra ativo.

    UM campo continua intocado, e nao por esquecimento: **`deactivated`**. Ele e o
    soft-delete que a propria dashboard oferece e foi usado para esconder DUPLICATAS
    (Zilaudio, Daniela, Vanessa — 30/07). Perfil escondido de proposito que ganhasse
    `ativo=true` voltaria a aparecer na tela e desfaria aquele trabalho. Por isso o
    `ativo` so sobe para quem NAO esta deactivated.

    Idempotente: so faz PATCH do que esta fora do lugar. Falha aqui NUNCA derruba o
    merge — a aula ja esta em producao.
    """
    url, key = _supabase()
    if not (url and key):
        print("  (status: nao achei a config do Supabase — perfil nao promovido)")
        return
    h = {"apikey": key, "Authorization": f"Bearer {key}",
         "Content-Type": "application/json", "Prefer": "return=representation"}
    try:
        req = urllib.request.Request(
            f"{url}/rest/v1/perfis?id=eq.{slug}&select=id,status,ativo,deactivated",
            headers=h)
        atual = json.load(urllib.request.urlopen(req, timeout=20))
        if not atual:
            print(f"  (status: '{slug}' nao esta na tabela perfis — nada a promover)")
            return
        p = atual[0]
        patch = {}
        if p.get("status") in ("rascunho", "em_revisao"):
            patch["status"] = "aprovado"
        if not p.get("ativo"):
            if p.get("deactivated"):
                print(f"  (perfil '{slug}' esta deactivated — NAO reativado de proposito)")
            else:
                patch["ativo"] = True
        if not patch:
            return
        req = urllib.request.Request(
            f"{url}/rest/v1/perfis?id=eq.{slug}", headers=h, method="PATCH",
            data=json.dumps(patch).encode())
        novo = json.load(urllib.request.urlopen(req, timeout=20))[0]
        print(f"  perfil: status {p.get('status')} -> {novo['status']}, "
              f"ativo {p.get('ativo')} -> {novo['ativo']}")
    except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError) as e:
        print(f"  (status nao promovido: {type(e).__name__} — a aula esta mergeada mesmo assim)")


def reapontar_dependentes(head):
    """PR cuja BASE e a branch que estamos prestes a deletar tem de ser reapontado
    pro main ANTES do merge.

    O `--delete-branch` apaga a branch base do PR filho, e o GitHub **FECHA** o
    filho em vez de reapontar (e depois nao deixa reabrir: 'Cannot change the base
    branch of a closed pull request'). Aconteceu em 29/07/2026 com o #1671, que
    teve de ser recriado como #1672. O trabalho nao se perde — a branch head
    sobrevive —, mas o PR morre e o historico de revisao vai junto.
    """
    dependentes = gh("pr", "list", "--base", head, "--state", "open",
                     "--json", "number,headRefName")
    for d in dependentes:
        print(f"  reapontando PR dependente #{d['number']} ({d['headRefName']}) -> main")
        gh("pr", "edit", str(d["number"]), "--base", "main", parse=False)
    return [d["number"] for d in dependentes]


def conferir(pr, retrofit=False, apaga_ok=False):
    """`retrofit=True` relaxa UMA regra: a de um aluno so.

    `apaga_ok=True` relaxa OUTRA, e so ela: a de nao deletar arquivo — e ainda assim
    apenas para arquivos cuja URL o vercel.json ja serve por redirect. Arquivo sem
    cobertura barra do mesmo jeito, com ou sem a flag.

    Ela existe para PR de AULA — a geracao nao pode sprawlar por varios alunos (REGRA 32).
    Um retrofit autorizado pelo Dan (ex.: o Spot the Error, 708 arquivos em 30 alunos, PR
    #1731) e outra coisa: toca muitos alunos POR DEFINICAO, e quebrar em 30 PRs deixaria a
    revisao pior, nao melhor. Todo o resto continua valendo, inclusive a unica trava que
    realmente protege producao: `gates` COMPLETED+SUCCESS e nenhum check vermelho. Nao ha
    branch protection no main — se este script afrouxar, nao ha segunda linha.
    """
    d = gh("pr", "view", str(pr), "--json",
           "number,state,title,baseRefName,headRefName,files,statusCheckRollup")
    problemas = []

    if d["state"] != "OPEN":
        problemas.append(f"PR nao esta aberto (state={d['state']})")

    if d["baseRefName"] != "main":
        problemas.append(
            f"base e '{d['baseRefName']}', nao 'main' — mergear agora jogaria a aula "
            f"naquela branch, nao em producao. Mergeie a aula anterior primeiro "
            f"(o GitHub reaponta esta pro main ao deletar a branch base)")

    caminhos = [f["path"] for f in d["files"]]
    delecoes = [f["path"] for f in d["files"] if f.get("deletions", 0) and not f.get("additions", 0)]
    if delecoes:
        # Apagar pagina de aluno e o erro mais caro que este script pode deixar passar:
        # um link que a aluna tem no WhatsApp vira 404 sem aviso e sem ninguem saber.
        # Mas EXISTE um caso legitimo — a pagina virou ponte e o vercel.json passou a
        # servir aquela URL por redirect. Entao a licenca nao e "confie em mim": e
        # PROVAR que a URL continua respondendo. Quem nao estiver coberto, barra.
        orfaos = [c for c in delecoes if not url_coberta_por_redirect(c)]
        if orfaos or not apaga_ok:
            alvo = orfaos if orfaos else delecoes
            problemas.append(
                f"o PR DELETA arquivo(s): {alvo[:5]}"
                + ("\n      (nenhum redirect no vercel.json cobre essa(s) URL(s) — o link morreria)"
                   if orfaos else
                   "\n      (todas cobertas por redirect no vercel.json; --apaga-arquivo libera)"))

    slugs = slugs_do_pr(caminhos)
    if len(slugs) > 1 and not retrofit:
        problemas.append(
            f"PR toca mais de um aluno: {sorted(slugs)}"
            f"\n      (retrofit autorizado pelo Dan? --retrofit relaxa SO esta regra)")

    veredito, motivos = avaliar(d.get("statusCheckRollup") or [])
    return d, problemas, veredito, motivos, slugs


def main():
    ap = argparse.ArgumentParser(description="Mergeia uma aula por vez com o CI conferido (REGRA 32)")
    ap.add_argument("prs", nargs="+", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--wait", action="store_true", help="espera o gate concluir (ate 20 min por PR)")
    ap.add_argument("--apaga-arquivo", dest="apaga_arquivo", action="store_true",
                    help="permite APAGAR pagina — so se o vercel.json ja servir aquela URL por redirect")
    ap.add_argument("--retrofit", action="store_true",
                    help="PR de retrofit autorizado: relaxa SO a regra de um aluno so")
    a = ap.parse_args()

    saida = 0
    for pr in a.prs:
        print(f"\n=== PR #{pr}")
        prazo = time.time() + 20 * 60
        while True:
            d, problemas, veredito, motivos, slugs = conferir(pr, retrofit=a.retrofit, apaga_ok=a.apaga_arquivo)
            if veredito != "esperando" or not a.wait or time.time() > prazo:
                break
            print(f"  ... {motivos[0]} — reconferindo em 60s")
            time.sleep(60)

        print(f"  {d['title'][:78]}")
        print(f"  base={d['baseRefName']}  arquivos={len(d['files'])}  aluno={sorted(slugs) or '?'}")
        for m in motivos:
            print(f"  CI: {m}")

        if problemas:
            for p in problemas:
                print(f"  BLOQUEIO: {p}")
            saida = 1
            continue
        if veredito == "falhou":
            print("  BLOQUEIO: CI nao esta verde — NAO mergeia.")
            saida = 1
            continue
        if veredito == "esperando":
            print("  ESPERANDO: o gate ainda nao concluiu. Rode de novo (ou use --wait).")
            saida = 2
            continue

        if a.dry_run:
            print("  [dry-run] mergearia com squash + delete-branch")
            continue

        reapontar_dependentes(d["headRefName"])
        try:
            gh("pr", "merge", str(pr), "--squash", "--delete-branch", parse=False)
        except RuntimeError as e:
            # O `--delete-branch` tambem apaga a copia LOCAL, e o git recusa quando a
            # branch esta presa por uma worktree (que e como geramos aula). O merge
            # server-side JA aconteceu — tratar isso como falha reportaria "nao mergeou"
            # para uma aula que esta em producao, que e pior que o lixo da branch local.
            msg = str(e)
            if "Merge already in progress" in msg:
                # Corrida: o subagente do aluno tambem chamou o merge deste PR.
                # Nao e erro — o estado do PR abaixo diz quem ganhou.
                print("  (merge ja em andamento por outro processo — conferindo o estado)")
            elif "used by worktree" in msg or "failed to delete local branch" in msg:
                print("  (branch local presa pela worktree — nao deletada; irrelevante)")
            else:
                raise
        estado = gh("pr", "view", str(pr), "--json", "state")["state"]
        if estado != "MERGED":
            print(f"  ERRO: depois do merge o PR esta {estado}, nao MERGED")
            saida = 1
            continue
        print(f"  MERGEADO — a aula esta em producao (deploy automatico pela Vercel)")
        if len(slugs) == 1:
            promover_status(next(iter(slugs)))
        print(f"  LEMBRETE: a proxima aula deve sair do main atualizado "
              f"(git fetch && git rebase origin/main), nao desta branch.")

    return saida


if __name__ == "__main__":
    sys.exit(main())
