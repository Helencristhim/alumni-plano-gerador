#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 59 — classe usada no conteudo do consultivo existe no CSS do shell.

O DEFEITO, E POR QUE ELE E DIFICIL DE VER (03/09/2026)
-------------------------------------------------------
A professora reportou que as tres perguntas da tela 3 da Vanessa estavam "sem espaco" e
"pequenas demais". Nao era ajuste fino: elas usavam `comp-questions` / `comp-q`, classes do
molde IMERSIVO que o shell do CONSULTIVO **nao estiliza**. Saiam com o corpo padrao do
navegador — 16px, sem espacamento, sem filete — enquanto o componente da casa (`qlist` /
`q-item`) da 23px com respiro e barra de accent.

    O HTML e valido. O gate estatico passa. O navegador nao reclama. So a TELA mostra.

E o defeito se espalha por copia: quem escreve a aula seguinte olha a anterior. Medido em
03/09: **33 ocorrencias em 7 aulas de 5 alunos**.

O QUE ESTE GATE MEDE
--------------------
Toda classe usada num fragmento de conteudo do consultivo (`slides.html`, `preclass.html`,
`postclass.html`) tem de aparecer no CSS de um dos dois shells. Classe orfa = classe que o
autor achou que existia.

NAO mede o imersivo: la `comp-q` E estilizada, e a mesma classe e legitima.

A DIVIDA E ALVARA (REGRA 30)
-----------------------------
`classe_orfa_baseline.json` congela quantas ocorrencias cada arquivo ja tem. O gate NUNCA
exige que o numero caia — exige que nao SUBA. Arquivo fora do baseline comeca em zero: aula
nova nasce conforme, de graca. `--update` recongela e recusa recongelar para cima.

USO:
    python3 scripts/consultivo/check_classe_orfa.py
    python3 scripts/consultivo/check_classe_orfa.py --update
    python3 scripts/consultivo/check_classe_orfa.py --selftest
"""
import glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHELLS = [os.path.join(RAIZ, "_build", "model", "shells", n)
          for n in ("consultivo.html", "consultivo-aluno.html")]
FRAGMENTOS = os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                          "*.html")
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classe_orfa_baseline.json")
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"


def estilizadas():
    """Toda classe citada no CSS dos shells, mais as que o JS cria em runtime."""
    out = set()
    for s in SHELLS:
        if not os.path.exists(s):
            continue
        t = io.open(s, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r"<style[^>]*>(.*?)</style>", t, re.S):
            out |= {x.group(1) for x in re.finditer(r"\.([a-zA-Z][\w-]*)", m.group(1))}
        # classes que o JS adiciona/consulta: existem de fato, so nao no CSS
        out |= {x.group(1) for x in re.finditer(r"classList\.(?:add|toggle|remove)\('([\w-]+)'", t)}
        out |= {x.group(1) for x in re.finditer(r"querySelector(?:All)?\('\.([\w-]+)", t)}
    return out


def orfas_do_arquivo(caminho, ok):
    t = io.open(caminho, encoding="utf-8", errors="ignore").read()
    achadas = {}
    for m in re.finditer(r'class="([^"]+)"', t):
        for c in m.group(1).split():
            if c not in ok:
                achadas[c] = achadas.get(c, 0) + 1
    return achadas


def varre():
    ok = estilizadas()
    fora = {}
    for f in sorted(glob.glob(FRAGMENTOS)):
        a = orfas_do_arquivo(f, ok)
        if a:
            fora[os.path.relpath(f, RAIZ)] = a
    return fora


def carrega():
    return json.load(io.open(BASELINE, encoding="utf-8")) if os.path.exists(BASELINE) else {}


def main():
    if "--selftest" in sys.argv:
        return selftest()
    atualizar = "--update" in sys.argv
    base, fora = carrega(), varre()
    print("=== GATE 59 — classe do conteudo existe no CSS do shell (consultivo) ===")
    if atualizar:
        novo = {k: sum(v.values()) for k, v in fora.items()}
        for k, v in base.items():
            if novo.get(k, 0) > v:
                print(f"  {VERMELHO}RECUSADO{ZERA} {k}: {novo[k]} > {v} congelado. Baseline nao sobe.")
                return 1
        json.dump(dict(sorted(novo.items())), io.open(BASELINE, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"  baseline recongelado: {len(novo)} arquivo(s)")
        return 0
    falhou = False
    for arq, classes in fora.items():
        n = sum(classes.values())
        if n > base.get(arq, 0):
            falhou = True
            print(f"  {VERMELHO}FAIL{ZERA}  {arq}: {n} uso(s) de classe sem CSS "
                  f"(congelado {base.get(arq, 0)})")
            for c, q in sorted(classes.items(), key=lambda x: -x[1]):
                print(f"          .{c} x{q} — o shell nao estiliza; a tela sai sem formato")
    if falhou:
        print(f"\n{VERMELHO}GATE 59 — classe que o autor achou que existia.{ZERA} "
              f"Use o componente da casa (ex: qlist/q-item no lugar de comp-q).")
        return 1
    print(f"{VERDE}GATE 59 OK{ZERA} — {len(base)} arquivo(s) na divida congelada, nada novo.")
    return 0


def selftest():
    ok = estilizadas()
    assert "q-item" in ok, "o shell deveria estilizar .q-item"
    assert "comp-q" not in ok, "comp-q nao deveria estar estilizada no consultivo"
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write('<div class="qlist"><div class="q-item">ok</div></div>')
        limpo = fh.name
    assert orfas_do_arquivo(limpo, ok) == {}, "acusou arquivo limpo"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write('<div class="comp-questions"><div class="comp-q">x</div></div>')
        sujo = fh.name
    a = orfas_do_arquivo(sujo, ok)
    assert a.get("comp-q") == 1 and a.get("comp-questions") == 1, a
    os.unlink(limpo); os.unlink(sujo)
    print("GATE 59 selftest OK — aceita o componente da casa, morde a classe sem CSS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
