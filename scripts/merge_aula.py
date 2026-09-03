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


def arquivos_removidos(pr, files):
    """Quais arquivos este PR REMOVE de fato — nao "quais so perderam linhas".

    `gh pr view --json files` nao traz o status por arquivo, entao a versao antiga
    inferia delecao de `deletions>0 and additions==0`. Isso confunde duas coisas
    diferentes: um PR que APAGA a pagina de uma aluna, e um PR que so RETIRA LINHAS
    dela (limpar HTML morto nao adiciona nada, entao cai na mesma heuristica). O
    segundo e trabalho legitimo e ficava impossivel de mergear — barrou a limpeza
    das 6 secoes vazias de Complementares da ana-claudia-veraldi (PR #1892), onde
    os dois arquivos seguiam vivos na branch.

    A REST API traz `status` por arquivo, e so diz `removed` quando o arquivo
    realmente sumiu. Se a chamada falhar, caimos na heuristica antiga DE PROPOSITO:
    barrar um PR legitimo custa uma mensagem de erro; deixar passar a delecao de uma
    pagina publicada vira 404 no link que a aluna ja tem no WhatsApp.
    """
    try:
        api = gh("api", f"repos/{{owner}}/{{repo}}/pulls/{pr}/files", "--paginate")
        return [f["filename"] for f in api if f.get("status") == "removed"]
    except Exception:
        return [f["path"] for f in files
                if f.get("deletions", 0) and not f.get("additions", 0)]


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


# Moldes nao sao alunos. Nao tem contrato, nao estao em `perfis`, nao aparecem na dashboard
# -- e o material deles carrega `<meta name="alumni-molde">` desde 27/08/2026. Um PR que
# gera aula de aluno e reconstroi o molde no caminho (porque o builder mudou) nao esta
# "tocando dois alunos": esta tocando um aluno e a ferramenta.
MOLDES = {"helen-mendes", "stephanie-vicente"}


def slugs_do_pr(arquivos):
    """Slugs de ALUNO tocados pelo PR — o merge tem de ser de um aluno so.

    Duas coisas que nao contam como "outro aluno", e as duas apareceram no primeiro PR de
    aluno real no consultivo (Luiz, 27/08/2026), que este guarda bloqueou por engano:

    - `{slug}-ciclo{N}` (e o antigo `{slug}-c{N}`) e o MESMO aluno. Enquanto ele tem aula no
      material antigo, o ciclo novo
      nasce ao lado em `{slug}-c1.html`; contar os dois como pessoas diferentes fazia o
      guarda ver dois alunos onde ha um.
    - o MOLDE nao e aluno.

    O que o guarda protege continua protegido: PR de um aluno que mexe no material de OUTRO
    segue bloqueado, que e o acidente que ele existe para impedir."""
    achados = set()
    for p in arquivos:
        for rx in (r"^public/(?:professor|aluno)/([a-z0-9-]+?)(?:-aula\d+|-c(?:iclo)?\d+)?\.html$",
                   r"^public/audio/([a-z0-9-]+)/",
                   r"^_build/([a-z0-9-]+)-aula\d+/",
                   r"^_build/consultivo/([a-z0-9-]+)/"):
            m = re.match(rx, p)
            if m:
                achados.add(m.group(1))
                break
    return achados - MOLDES


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


def _e_do_consultivo(slug):
    """O aluno tem material da anatomia consultivo? Le o carimbo, nunca uma lista a mao."""
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho = os.path.join(raiz, "public", "data", "anatomias.json")
    try:
        with open(caminho, encoding="utf-8") as fh:
            return slug in (json.load(fh).get("consultivo") or {})
    except Exception:
        return False


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

    NENHUM CAMINHO E SILENCIOSO (corrigido em 05/08/2026). Antes, o caso "nada a
    fazer" saia com um `return` mudo e era indistinguivel de sucesso: em 05/08 a Ana
    Paula e a Viviane ficaram `rascunho` depois do merge e ninguem viu, porque a
    funcao nao imprimiu NADA nas duas vezes. Quem le a saida do merge nao consegue
    diferenciar "ja estava certo" de "falhou calado" — e como a excecao aqui e
    engolida de proposito (a aula ja esta no ar), o silencio era a unica pista.
    Agora toda saida IMPRIME o que aconteceu, e o PATCH e RECONFERIDO na origem:
    dizer "promovi" sem reler e so repetir o que a gente pediu, nao o que ficou.
    """
    # MERGE DE AULA DO CONSULTIVO NAO MEXE NO `perfis.status`.
    #
    # `perfis.status` descreve o material IMERSIVO, que e o que esses alunos usam hoje e que
    # ja esta aprovado. O material do consultivo tem status PROPRIO, carimbado no head pelo
    # builder (`alumni-anatomia-status`) e lido pelo indice que a aba do dashboard consome --
    # e comeca em `rascunho`, porque esta em escrita.
    #
    # Promover aqui significaria mexer na etiqueta do imersivo por causa de uma aula do
    # consultivo: dois materiais, um campo, a informacao errada nos dois lugares. Foi o que
    # aconteceu em 01/09/2026, quando segurar o consultivo apagou o "Aprovado" do imersivo.
    #
    # A lista sai do carimbo no disco (`anatomias.json`) -- nao ha segunda lista para alguem
    # esquecer de atualizar. Para promover o material do consultivo, muda-se o `status` no
    # config e regera: a etiqueta e derivada do arquivo, como todo o resto da aba.
    if _e_do_consultivo(slug):
        print(f"  perfil: '{slug}' tem material do consultivo — `perfis.status` NAO tocado "
              f"(ele descreve o imersivo; o consultivo tem status proprio, no config)")
        return

    url, key = _supabase()
    if not (url and key):
        print("  (status: nao achei a config do Supabase — perfil NAO promovido)")
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
            print(f"  perfil: ja estava status={p.get('status')} ativo={p.get('ativo')} "
                  f"— nada a promover")
            return
        req = urllib.request.Request(
            f"{url}/rest/v1/perfis?id=eq.{slug}", headers=h, method="PATCH",
            data=json.dumps(patch).encode())
        json.load(urllib.request.urlopen(req, timeout=20))
        # RELE da origem: o retorno do PATCH e o que pedimos, nao prova do que ficou.
        req = urllib.request.Request(
            f"{url}/rest/v1/perfis?id=eq.{slug}&select=id,status,ativo", headers=h)
        novo = json.load(urllib.request.urlopen(req, timeout=20))[0]
        print(f"  perfil: status {p.get('status')} -> {novo['status']}, "
              f"ativo {p.get('ativo')} -> {novo['ativo']}")
        pendente = [k for k, v in patch.items() if novo.get(k) != v]
        if pendente:
            print(f"  !! ATENCAO: {', '.join(pendente)} NAO ficou como pedido "
                  f"(a aula esta no ar, mas o aluno pode nao aparecer na dashboard). "
                  f"Rode: python3 -c \"import sys;sys.path.insert(0,'scripts');"
                  f"import merge_aula;merge_aula.promover_status('{slug}')\"")
    except (urllib.error.URLError, OSError, ValueError, KeyError, IndexError) as e:
        print(f"  !! status NAO promovido ({type(e).__name__}: {e}) — a aula esta "
              f"mergeada mesmo assim, mas CONFIRA a dashboard e rode: python3 -c "
              f"\"import sys;sys.path.insert(0,'scripts');import merge_aula;"
              f"merge_aula.promover_status('{slug}')\"")


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
    # A TRAVA E SOBRE LINK QUE MORRE, ENTAO ELA OLHA O QUE VIRA LINK (03/09/2026).
    #
    # Ela dizia "apagar pagina de aluno e o erro mais caro" e media QUALQUER arquivo do
    # repo. Um JSON dentro de `scripts/` nao e servido pela Vercel, nao tem URL e nao tem
    # link no WhatsApp de ninguem — mas barrava o merge igual, e a saida sugerida
    # (`--apaga-arquivo`) tambem nao passa, porque ela exige um redirect no vercel.json
    # para uma URL que nunca existiu. O PR ficava sem caminho nenhum.
    #
    # Aconteceu ao apagar `scripts/consultivo/nome-da-tela-baseline.json` (PR #2518), o
    # alvara que o Dan mandou nao existir. Isto NAO afrouxa a protecao: tudo que a Vercel
    # serve continua barrado do mesmo jeito, com ou sem flag. O que muda e o gate deixar de
    # nomear uma regiao ("pagina") e medir outra ("arquivo").
    SERVIDO = ("public/",)
    delecoes = [c for c in arquivos_removidos(pr, d["files"]) if c.startswith(SERVIDO)]
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
