#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 54 — o material que se declara BILINGUE entrega o apoio inteiro.

DE ONDE ISTO VEIO
-----------------
A Vanessa e a primeira aluna REAL-BEGINNER do produto (A1 declarado, A0 real), e a producao
nunca tinha previsto esse ponto de partida. A revisao de 02/09/2026:

    "se a aluna nao tiver apoio para tudo o que esta escrito em ingles, pode ser um fator
     limitante para ela"

O pre-class e o unico momento em que ela esta SOZINHA com o material. Na aula ha um professor
que traduz, reformula e da a palavra; no pre-class nao ha ninguem. Uma alternativa em ingles
que ela nao le nao e exercicio -- e uma linha que ela pula, e o exercicio parece feito.

O QUE ISTO NAO E
----------------
Nao e uma regra para todo material. De A2 em diante vale a REGRA 13 (zero portugues na tela
do aluno), e ligar isto para todos seria trocar uma regra da chefe por uma conveniencia. O
modo e DECLARADO no config do aluno (`"apoio": {"bilingue": true}`) e o proprio caminho da
Vanessa e para sair dele.

Entao este gate nao pergunta "tem portugues?". Ele pergunta:

    o material que PROMETEU o apoio bilingue esta entregando ele por inteiro?

Promessa parcial e o pior dos dois mundos: metade dos exercicios acessivel, metade nao, e
nada na tela dizendo qual e qual.

O QUE ELE MEDE, no arquivo do ALUNO (que e onde a promessa e cobrada)
---------------------------------------------------------------------
  1. o rotulo do botao de conferir esta nas duas linguas ("Check / Checar");
  2. todo item de exercicio fechado do pre/post-class tem a sua traducao (`.item-pt`);
  3. a traducao nasce ESCONDIDA -- ela abre ao conferir. Visivel desde o inicio, o olho vai
     nela e o ingles ao lado vira decoracao (a mesma razao da REGRA 2.1 do imersivo, pelo
     avesso);
  4. a aba Feedback esta em portugues. E a unica superficie do aluno que nao e exercicio: e
     o professor falando com ele, e em ingles ela e uma caixa bonita que nunca vai ser lida.

O VOCABULARIO FICA DE FORA, e nao por esquecimento: no `par` as duas alternativas SAO a
traducao. Uma segunda traducao por baixo entregaria a resposta antes da escolha.

ESCOPO: o carimbo `alumni-anatomia=consultivo`, cruzado com o config que declara o modo.
Material que nao declara nao e medido -- nao ha promessa a cobrar.

USO:
    python3 scripts/consultivo/check_apoio_bilingue.py [arquivo.html ...]
    python3 scripts/consultivo/check_apoio_bilingue.py --selftest
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

ROTULO = "Check / Checar"
# As mecanicas de conferir de exercicio FECHADO. `ppCheck` (o `par`, vocabulario) fica fora.
CHECAGENS = ("mCheck", "selCheck", "czCheck")


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def bilingues():
    """Os slugs cujo config declara o modo. A promessa esta no config, nao no HTML."""
    fora = {}
    for cfg in glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json")):
        d = json.load(open(cfg, encoding="utf-8"))
        if (d.get("apoio") or {}).get("bilingue"):
            fora[d["slug"]] = d
    return fora


def regiao(c, ident):
    """O miolo de uma aba, do id ate o fim do proprio bloco (contagem de <div>)."""
    m = re.search(r'<div[^>]*id="' + re.escape(ident) + r'"[^>]*>', c)
    if not m:
        return ""
    i, prof = m.end(), 1
    for t in re.finditer(r"<(/?)div\b", c[m.end():]):
        prof += -1 if t.group(1) else 1
        if prof == 0:
            i = m.end() + t.start()
            break
    return c[m.end():i]


def exercicios(txt):
    """(id, mecanica) de cada exercicio fechado da regiao."""
    return [(m.group(2), m.group(1))
            for m in re.finditer(r"\b(" + "|".join(CHECAGENS) + r")\(this,'([^']+)'\)", txt)]


def confere(caminho, slug_bilingue):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return None
    slug = re.sub(r"-c(?:iclo)?\d+$", "", re.sub(r"\.html$", "", os.path.basename(caminho)))
    if slug not in slug_bilingue:
        return None
    fora = []

    # ---- 1. o rotulo do botao, nas duas linguas
    for mec in CHECAGENS:
        for m in re.finditer(r'<button[^>]*onclick="' + mec + r"\(this[^\"]*\"[^>]*>"
                             r"([^<]*)</button>", c):
            if m.group(1).strip() != ROTULO:
                fora.append(f"botao de conferir com o rotulo {m.group(1).strip()!r}: em "
                            f"material bilingue ele vai nas duas linguas ({ROTULO!r}). "
                            f"`Check` e a primeira palavra em ingles de que o pre-class "
                            f"inteiro depende, e a aluna ainda nao a entende.")
                break

    # ---- 2 e 3. a traducao de cada item, e ela nasce escondida
    pre = regiao(c, "tab-preclass") + regiao(c, "tab-postclass")
    for ident, mec in exercicios(pre):
        bloco = regiao(c, ident)
        if not bloco:
            continue
        itens = len(re.findall(r'class="(?:match-row|quiz-option|blank-input)"', bloco)) or \
            len(re.findall(r'class="match-row', bloco)) + \
            len(re.findall(r'class="quiz-option"', bloco)) + \
            len(re.findall(r'class="blank-input"', bloco))
        traducoes = len(re.findall(r'class="item-why item-pt"|class="item-pt"', bloco))
        if traducoes < itens:
            fora.append(f"exercicio {ident!r}: {itens} item(ns) e {traducoes} traducao(oes). "
                        f"Item sem traducao sai perfeitamente formado — so nao da a aluna "
                        f"como saber o que a frase dizia.")
        if re.search(r'class="item-why item-pt"[^>]*style="[^"]*display\s*:\s*block', bloco):
            fora.append(f"exercicio {ident!r}: a traducao nasce VISIVEL. Ela abre ao "
                        f"conferir — antes da tentativa, o olho vai nela e o ingles ao "
                        f"lado vira decoracao.")

    # ---- 4. a aba Feedback em portugues
    fb = regiao(c, "tab-feedback")
    if fb:
        sobrou = [t for t in ("What worked", "Keep developing",
                              "Feedback will be available", "After each lesson")
                  if t in fb]
        if sobrou:
            fora.append(f"aba Feedback ainda em ingles: {sobrou}. E a unica superficie do "
                        f"aluno que nao e exercicio — e o professor falando com ele.")
    return fora


def main(argv):
    alvos = [a for a in argv if not a.startswith("--")]
    if not alvos:
        alvos = sorted(glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html")))
    decl = bilingues()
    print(f"=== GATE 54 — o apoio bilingue prometido (anatomia {ANATOMIA}) ===")
    if not decl:
        print(f"{VERDE}GATE 54 OK{ZERA} — nenhum material declara `apoio.bilingue`. "
              f"Nada a cobrar.")
        return 0
    total, vistos = 0, 0
    for f in alvos:
        r = confere(f, decl)
        if r is None:
            continue
        vistos += 1
        rel = os.path.relpath(f, RAIZ)
        if r:
            total += len(r)
            for e in r:
                print(f"  {VERMELHO}FAIL{ZERA}   {rel}: {e}")
        else:
            print(f"  {VERDE}ok{ZERA}     {rel}")
    if not vistos:
        print(f"{VERMELHO}GATE 54 — {sorted(decl)} declara(m) o modo e nenhum arquivo "
              f"publicado foi encontrado.{ZERA}")
        return 1
    if total:
        print(f"\n{VERMELHO}GATE 54 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"\n{VERDE}GATE 54 OK{ZERA} — {vistos} arquivo(s) entregam o apoio que prometem.")
    return 0


def selftest():
    falhas = []
    cab = '<meta name="alumni-anatomia" content="consultivo">'
    # o rotulo
    bom = f'<button class="verify-all-btn ghost" onclick="mCheck(this,\'m1\')">{ROTULO}</button>'
    mau = '<button class="verify-all-btn ghost" onclick="mCheck(this,\'m1\')">Check</button>'
    if re.search(r'<button[^>]*onclick="mCheck\(this[^"]*"[^>]*>([^<]*)</button>',
                 bom).group(1).strip() != ROTULO:
        falhas.append("nao leu o rotulo bom")
    if re.search(r'<button[^>]*onclick="mCheck\(this[^"]*"[^>]*>([^<]*)</button>',
                 mau).group(1).strip() == ROTULO:
        falhas.append("nao viu o rotulo so em ingles")
    # a regiao
    if regiao(f'{cab}<div id="x"><div>a</div>b</div>c', "x") != "<div>a</div>b":
        falhas.append("a regiao nao fecha no <div> certo")
    # a mecanica do vocabulario NAO entra
    if exercicios("<button onclick=\"ppCheck(this,'p1')\">x</button>"):
        falhas.append("o `par` (vocabulario) entrou na cobranca, e ele e a excecao")
    if exercicios("<button onclick=\"czCheck(this,'cz1')\">x</button>") != [("cz1", "czCheck")]:
        falhas.append("nao viu o gap-fill")
    if falhas:
        print(VERMELHO + "selftest FALHOU" + ZERA)
        for f in falhas:
            print("  -", f)
        return 1
    print(f"{VERDE}selftest OK{ZERA} — o gate le o rotulo, recorta a regiao pelo balanco de "
          f"<div>, ve o gap-fill e poupa o vocabulario.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv[1:]))
