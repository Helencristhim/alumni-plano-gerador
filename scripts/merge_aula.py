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
import re
import subprocess
import sys
import time

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
    falhas, pendentes, gate = [], [], None
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
            gate = (concluido, conclusao)

    if falhas:
        return "falhou", falhas
    if gate is None:
        return "falhou", [f"o check '{GATE_OBRIGATORIO}' nao existe neste PR — "
                          "sem ele nao da pra afirmar que a aula passou"]
    concluido, conclusao = gate
    if not concluido:
        return "esperando", [f"'{GATE_OBRIGATORIO}' ainda rodando"]
    if conclusao not in OK:
        return "falhou", [f"'{GATE_OBRIGATORIO}': {conclusao}"]
    # Gate verde. Pendencia sobrando so bloqueia se NAO for preview de deploy.
    trava = [p for p in pendentes if not PREVIEW.search(p)]
    if trava:
        return "esperando", [f"pendente: {', '.join(trava)}"]
    return "ok", [f"'{GATE_OBRIGATORIO}' SUCCESS" +
                  (f"; preview ignorado: {', '.join(pendentes)}" if pendentes else "")]


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


def conferir(pr):
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
        problemas.append(f"o PR DELETA arquivo(s): {delecoes[:5]}")

    slugs = slugs_do_pr(caminhos)
    if len(slugs) > 1:
        problemas.append(f"PR toca mais de um aluno: {sorted(slugs)}")

    veredito, motivos = avaliar(d.get("statusCheckRollup") or [])
    return d, problemas, veredito, motivos, slugs


def main():
    ap = argparse.ArgumentParser(description="Mergeia uma aula por vez com o CI conferido (REGRA 32)")
    ap.add_argument("prs", nargs="+", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--wait", action="store_true", help="espera o gate concluir (ate 20 min por PR)")
    a = ap.parse_args()

    saida = 0
    for pr in a.prs:
        print(f"\n=== PR #{pr}")
        prazo = time.time() + 20 * 60
        while True:
            d, problemas, veredito, motivos, slugs = conferir(pr)
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
            if "used by worktree" not in str(e) and "failed to delete local branch" not in str(e):
                raise
            print(f"  (branch local presa pela worktree — nao deletada; irrelevante)")
        estado = gh("pr", "view", str(pr), "--json", "state")["state"]
        if estado != "MERGED":
            print(f"  ERRO: depois do merge o PR esta {estado}, nao MERGED")
            saida = 1
            continue
        print(f"  MERGEADO — a aula esta em producao (deploy automatico pela Vercel)")
        print(f"  LEMBRETE: a proxima aula deve sair do main atualizado "
              f"(git fetch && git rebase origin/main), nao desta branch.")

    return saida


if __name__ == "__main__":
    sys.exit(main())
