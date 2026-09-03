#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 57 — material A0 nao presume producao autonoma de frase como condicao de entrada.

A NORMA (CEFR Companion Volume, faixa Pre-A1; adotada em 03/09/2026)
--------------------------------------------------------------------
A0 / Real Beginner corresponde a Pre-A1: um estagio ANTERIOR a capacidade generativa. O
aluno depende de palavra isolada, expressao formulaica, contexto e apoio do interlocutor.

    "Nao se deve presumir producao autonoma de frases como condicao de entrada. Palavras
     isoladas e respostas formulaicas podem constituir desempenho valido; frases simples
     podem ser desenvolvidas progressivamente como objetivo em direcao a A1."

O QUE ESTE GATE MEDE, E POR QUE CADA COISA
-------------------------------------------
So no PRE-CLASS, e so em material cujo header declara A0. O pre-class e o unico momento em
que o aluno esta SOZINHO com o material -- no in-class ha professor mediando, e a norma
manda o apoio ser mais seletivo la.

  1. GAP-FILL COM BANCO. Digitar a palavra e recuperacao livre; escolher entre candidatas e
     reconhecimento. A faixa sustenta a segunda.
  2. PRODUCAO LIVRE COM MODELO. Prompt aberto sem modelo presume que a frase ja existe.
  3. ALVO DE FALA CURTO (<= 6 palavras). Nao proibe a frase: proibe a frase LONGA como
     porta de entrada. A frase simples e o objetivo, e chega construida.

O QUE ELE NAO MEDE: se a aula e boa, se o tema faz sentido, se o ingles esta certo. Ele
mede se o material que DECLAROU A0 entrega o apoio que a faixa exige -- a mesma pergunta do
GATE 54 do consultivo, e nao "tem portugues?".

A DIVIDA E ALVARA (REGRA 30)
-----------------------------
Material A0 escrito antes desta norma continua no ar e FUNCIONA. `pre_a1_baseline.json`
congela quantas telas de cada arquivo ainda estao assim. O gate NUNCA exige que o numero
caia; exige que nao SUBA. Arquivo fora do baseline comeca em zero: aula nova nasce conforme,
de graca. `--update` recongela depois de um conserto legitimo, e recusa recongelar para cima.

USO:
    python3 _build/model/check_pre_a1.py [arquivo.html ...]
    python3 _build/model/check_pre_a1.py --update
    python3 _build/model/check_pre_a1.py --selftest
"""
import glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pre_a1_baseline.json")
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"
MAX_PALAVRAS_FALA = 6


def texto(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def e_a0(html):
    """O nivel vem do PRIMEIRO chip do header -- a mesma leitura do `nivel_cefr` do builder."""
    m = re.search(r'<div class="student-info">(.*?)</div>', html, re.S)
    if not m:
        return False
    primeiro = re.search(r"<span>(.*?)</span>", m.group(1), re.S)
    return bool(primeiro and re.search(r"\bA0\b", texto(primeiro.group(1))))


def regiao_preclass(html):
    m = re.search(r'id="tab-exercises".*?(?=<div class="slides-wrapper"|id="tab-inclass")',
                  html, re.S)
    return m.group(0) if m else ""


def achados(html):
    """Os defeitos Pre-A1 do pre-class deste arquivo. Lista de (tipo, detalhe)."""
    if not e_a0(html):
        return []
    pre = regiao_preclass(html)
    if not pre:
        return []
    out = []
    # 1. gap-fill sem banco de palavras
    for bloco in re.findall(r'<div class="lesson-body".*?(?=<div class="lesson-card"|\Z)', pre, re.S):
        if 'class="blank-input"' in bloco and "pc-bank" not in bloco:
            out.append(("gap-fill sem banco",
                        f'{len(re.findall(chr(99)+"lass=.blank-input", bloco))} lacuna(s) pedem a palavra digitada'))
    # 2. producao livre sem modelo
    for tc in re.findall(r'<div class="think-card".*?</div>\s*</div>', pre, re.S):
        if "pc-modelo" not in tc:
            q = texto(re.search(r'class="think-question">(.*?)</div>', tc, re.S).group(1))[:60] \
                if re.search(r'class="think-question">', tc) else "?"
            out.append(("producao livre sem modelo", q))
    # 3. alvo de fala longo demais
    for frase in re.findall(r'class="speech-card"[^>]*data-phrase="([^"]+)"', pre):
        n = len(texto(frase).split())
        if n > MAX_PALAVRAS_FALA:
            out.append(("alvo de fala longo", f"{n} palavras: {texto(frase)[:70]}"))
    return out


def carrega():
    if os.path.exists(BASELINE):
        return json.load(io.open(BASELINE, encoding="utf-8"))
    return {}


def alvos(argv):
    fs = [a for a in argv if a.endswith(".html")]
    if fs:
        return fs
    return sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")))


def main():
    if "--selftest" in sys.argv:
        return selftest()
    atualizar = "--update" in sys.argv
    base = carrega()
    novo, falhou = {}, False
    print("=== GATE 57 — material A0 nao exige producao autonoma de entrada ===")
    for f in alvos(sys.argv[1:]):
        try:
            html = io.open(f, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        ach = achados(html)
        rel = os.path.relpath(f, RAIZ)
        if ach:
            novo[rel] = len(ach)
        permitido = base.get(rel, 0)
        if len(ach) > permitido and not atualizar:
            falhou = True
            print(f"  {VERMELHO}FAIL{ZERA}  {rel}: {len(ach)} achado(s), congelado(s) {permitido}")
            for t, d in ach[:4]:
                print(f"          · {t}: {d}")
    if atualizar:
        for k, v in base.items():          # o congelado so pode CAIR
            if k in novo and novo[k] > v:
                print(f"  {VERMELHO}RECUSADO{ZERA} {k}: {novo[k]} > {v} congelado. Baseline nao sobe.")
                return 1
        json.dump(dict(sorted(novo.items())), io.open(BASELINE, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"  baseline recongelado: {len(novo)} arquivo(s)")
        return 0
    if falhou:
        print(f"\n{VERMELHO}GATE 57 — material A0 pedindo o que a faixa nao sustenta.{ZERA}")
        return 1
    print(f"GATE 57 OK — {len(base)} arquivo(s) na divida congelada, nenhum defeito novo.")
    return 0


def selftest():
    """Prova que o gate MORDE: um A0 sem apoio reprova, o mesmo com apoio passa, e um
    material que nao declara A0 nao e medido."""
    cabeca = '<div class="student-info"><span>%s</span></div>'
    corpo = ('<div class="tab-content" id="tab-exercises"><div class="lesson-body">'
             '<div class="fill-blank-item"><input class="blank-input" data-answer="don\'t"></div>'
             '<div class="think-card"><div class="think-question">Talk about your music.</div>'
             '<div class="speech-controls"></div></div>'
             '<div class="speech-card" data-phrase="My favorite band is from the eighties.">'
             '</div></div></div><div class="slides-wrapper">')
    ruim = (cabeca % "A0 &middot; Iniciante Absoluto") + corpo
    assert len(achados(ruim)) == 3, achados(ruim)
    bom = ruim.replace('<div class="fill-blank-item"',
                       '<div class="phrase-list pc-bank"></div><div class="fill-blank-item"') \
              .replace('<div class="speech-controls">',
                       '<div class="pc-modelo">I love rock.</div><div class="speech-controls">') \
              .replace("My favorite band is from the eighties.", "I love rock.")
    assert achados(bom) == [], achados(bom)
    outro = (cabeca % "B1 &middot; Intermediario") + corpo
    assert achados(outro) == [], "nao-A0 nao pode ser medido"
    print("GATE 57 selftest OK — morde o A0 sem apoio, aceita o com apoio, ignora quem nao e A0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
