#!/usr/bin/env python3
"""GATE DE DEPLOY — producao so sai de um commit que esta no `main` do GitHub.

POR QUE ISTO EXISTE (03/08/2026)
--------------------------------
As 16:21, 16:25 e 16:52 UTC alguem rodou `vercel --prod` de um checkout LOCAL:

    source   : cli          <- nao veio do GitHub
    gitDirty : 1            <- arvore de trabalho suja
    commit   : f4f4b6f49    <- NUNCA existiu no GitHub (API responde 422)

O Vercel publica o CONTEUDO DO DISCO daquela maquina. O checkout era de **29/05** —
dois meses atrasado. Resultado: producao voltou para maio. O dashboard velho fazia
`select('id,data,...)` e estourava o statement timeout com 99 perfis, caindo no
fallback estatico de 8 alunos ("so aparecem 10 alunos"), e TODO material gerado de
junho em diante virou 404 (helen-mendes, thiago-negraes, catalogo...).

O `main` nunca regrediu. Nao houve push. So a PRODUCAO regrediu — e por isso nenhum
gate de CI viu: **nada disso passa pelo CI**. E a segunda vez (a REGRA 19 ja registra
o incidente de 11/06). Nao existe toggle na Vercel para proibir deploy por CLI —
conferido na API, no projeto e no time. Entao a trava tem de morar no BUILD, que e o
unico ponto por onde todo deploy passa, venha do git ou da CLI.

A REGRA
-------
Deploy de PRODUCAO exige um commit alcancavel a partir do `main` no GitHub.
- veio do git   -> o SHA esta no main (ou e um ancestral) -> PASSA
- veio da CLI de um checkout limpo e sincronizado -> PASSA
- veio da CLI de um checkout velho/sujo -> o SHA nao existe la, ou divergiu -> FALHA

Preview nao e tocado: quem esta testando branch precisa deployar a vontade.

FALHA-ABERTO NA DUVIDA, FALHA-FECHADO NA PROVA
----------------------------------------------
So barra com prova positiva (o GitHub respondeu e disse que o commit nao esta no
main). Rate limit, rede fora, repo inacessivel: deixa passar com aviso. Um gate que
derruba deploy legitimo por instabilidade de rede seria desligado na primeira
madrugada — e ai nao protege mais nada.
"""
import json
import os
import sys
import urllib.error
import urllib.request

OWNER = os.environ.get("VERCEL_GIT_REPO_OWNER") or "Helencristhim"
REPO = os.environ.get("VERCEL_GIT_REPO_SLUG") or "alumni-plano-gerador"
BASE = "main"
TIMEOUT = 15


def out(msg):
    print(f"[deploy-source] {msg}", flush=True)


def get(url):
    """(status, payload). status None = nao deu para perguntar (rede/timeout)."""
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "alumni-deploy-gate",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        out(f"nao consegui falar com o GitHub ({e.__class__.__name__})")
        return None, None


def main():
    env = os.environ.get("VERCEL_ENV", "")
    if env != "production":
        out(f"VERCEL_ENV={env or '(vazio)'} — nao e producao, seguindo.")
        return 0

    sha = (os.environ.get("VERCEL_GIT_COMMIT_SHA") or "").strip()
    if not sha:
        out("BLOQUEADO: deploy de producao sem commit do git.")
        out("Producao sai de PR mergeado no main (REGRA 19). Nunca de `vercel --prod`.")
        return 1

    # O repo tem de estar alcancavel, senao qualquer 404 abaixo seria ambiguo
    # (commit fora do main? ou repo privado/fora do ar?). Sem essa checagem o gate
    # derrubaria producao no dia em que o repo mudasse de visibilidade.
    status, _ = get(f"https://api.github.com/repos/{OWNER}/{REPO}")
    if status != 200:
        out(f"nao deu para verificar o repo (HTTP {status}) — seguindo sem barrar.")
        return 0

    status, data = get(
        f"https://api.github.com/repos/{OWNER}/{REPO}/compare/{BASE}...{sha}"
    )

    if status in (404, 422):
        out(f"BLOQUEADO: o commit {sha[:9]} nao existe no GitHub.")
        out("Isso e a assinatura de `vercel --prod` rodado de um checkout local:")
        out("o Vercel publica o disco daquela maquina, que pode estar meses atrasado.")
        out("Foi assim que a producao voltou para 29/05 em 03/08/2026.")
        out("Caminho certo: commit -> push -> PR -> merge no main (REGRA 19/32).")
        return 1

    if status != 200 or not isinstance(data, dict):
        out(f"nao deu para comparar com o {BASE} (HTTP {status}) — seguindo sem barrar.")
        return 0

    rel = data.get("status")
    # identical = e o proprio topo do main; behind = ancestral (deploy enfileirado
    # enquanto outro merge entrou na frente — legitimo e comum).
    if rel in ("identical", "behind"):
        out(f"ok: {sha[:9]} esta no {BASE} ({rel}).")
        return 0

    out(f"BLOQUEADO: {sha[:9]} nao esta no {BASE} (relacao: {rel}).")
    out(f"Commits a frente do {BASE}: {data.get('ahead_by')}. Producao so sai do {BASE}.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
