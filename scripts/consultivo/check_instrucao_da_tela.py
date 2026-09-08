#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 63 — no in-class, o enunciado e DA TELA, e esta na tela.

O CASO
------
Revisao da professora sobre a aula 1 da Vanessa (PR #2509):

    "Tela 5 e 6: enunciado na TELA, nao atras do botao de portugues."

O que havia: as duas telas injetavam um exercicio (`<!--BLOCOS:ev1-->`, `<!--BLOCOS:cl1-->`)
e o enunciado morava no `abertura` do proprio bloco, com o apoio em portugues no `pt`. Isso
tem duas consequencias, e as duas so aparecem na tela:

  1. o `pt` de um bloco vira o acordeao "Ver em portugues" -- fechado. No in-class o apoio e
     inline (`<span class="slide-pt">`, visivel ao lado do ingles), e e assim de proposito:
     ha professora conduzindo, e nada do que orienta a acao pode depender de um clique;
  2. o enunciado sai DEPOIS do documento, dentro da caixa do exercicio, em vez de acima
     dele. A aluna le o material antes de saber o que fazer com ele.

A correcao subiu a instrucao para `<p class="slide-question">` na tela, com o `.slide-pt`
inline, e ZEROU o `abertura`/`pt` dos dois blocos. Este gate e essa correcao virada regra.

Catalogo do auditor (04/09/2026): **PRO-011 Verbo sem acao correspondente** e **PRO-010
Instrucao redundante ou contraditoria** vizinham o caso; o que ele mede aqui e mais simples
e anterior aos dois -- a tela tem exercicio e NAO tem enunciado nenhum.

A05 (adendo de 05/09/2026, Linguagem Instrucional Pedagogica), §5.2: a instrucao publicada
deve "nomear uma acao que a interface ou a dinamica realmente oferece" e "conter contexto,
sequencia ou produto quando a atividade depender deles". Tela com exercicio e sem enunciado
nao chega a ter forma linguistica para avaliar.

AS DUAS REGRAS
--------------
(a) tela que injeta um exercicio TEM enunciado na propria tela (`.slide-question`,
    `.task-instr`, `.subprompt` ou `.slide-lead`);
(b) bloco injetado numa TELA nao carrega `abertura`/`instr`/`pt` proprios -- no in-class
    quem enuncia e a tela. (No pre-class e o contrario: ali o bloco E a unidade, e o
    `abertura` e o lugar certo. Por isso a regra so vale para as seccoes que o
    `slides.html` injeta.)

Nao ha aqui nenhuma regra sobre COMO a frase e escrita. Verbo, tom e naturalidade sao do
A05 e de leitura humana -- e o proprio A05 §10.2 manda a suite REPROVAR detector lexical
simplista. Este gate conta elemento, nao palavra.

PENDENTES (declarados, nao consertados aqui)
---------------------------------------------
Treze telas de tres alunos entram na regra (a): tem exercicio e nenhum elemento de
enunciado. Em varias delas a tarefa esta insinuada no `slide-heading` ("Two of these say
something back") ou so na nota do professor. Escrever o enunciado e conteudo -- e conteudo
de aluno que este PR nao foi pedido para mexer (REGRA 31). Ficam listadas abaixo com o caso,
como o Dan fixou em 03/09/2026 (excecao em codigo, com a razao). A lista so pode CAIR.

ESCOPO: os fragmentos autorais, `_build/consultivo/{slug}/aula{n}/`.

USO:
    python3 scripts/consultivo/check_instrucao_da_tela.py [dir ...]
    python3 scripts/consultivo/check_instrucao_da_tela.py --selftest
"""
import glob
import json
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, AMARELO, ZERA = "\033[32m", "\033[31m", "\033[33m", "\033[0m"

ENUNCIADO = ("slide-question", "task-instr", "subprompt", "slide-lead")
EXERCICIO = ("escolha", "par", "completar", "classificar", "lacuna", "gravar", "escrever")

PENDENTES = {
    # "{slug}/{aula} tela N": ja estava assim quando a regra nasceu
    "caio-de-souza-amante/aula1 tela 5", "caio-de-souza-amante/aula1 tela 6",
    "caio-de-souza-amante/aula2 tela 6", "caio-de-souza-amante/aula3 tela 4",
    "caio-de-souza-amante/aula4 tela 4", "caio-de-souza-amante/aula4 tela 5",
    "joice-lopes-leite/aula9 tela 6", "joice-lopes-leite/aula10 tela 6",
    "joice-lopes-leite/aula11 tela 4", "joice-lopes-leite/aula12 tela 5",
    "joice-lopes-leite/aula12 tela 6",
    "lucia-nishiyama-serra/aula4 tela 4", "lucia-nishiyama-serra/aula5 tela 4",
}
POR_QUE_PENDENTE = ("a tarefa aparece no slide-heading ou so na nota do professor; escrever "
                    "o enunciado e decisao de conteudo em material fora do escopo deste PR "
                    "(REGRA 31)")


def telas(html):
    for m in re.finditer(r'<div class="slide [^>]*data-slide="(\d+)"[^>]*>(.*?)'
                         r'(?=\n<div class="slide |\Z)', html, re.S):
        yield m.group(1), m.group(2)


def classes(corpo):
    return {c for lista in re.findall(r'class="([a-z0-9 \-]+)"', corpo)
            for c in lista.split()}


def confere(pasta):
    falhas = []
    sl = os.path.join(pasta, "slides.html")
    bl = os.path.join(pasta, "blocos.json")
    if not (os.path.exists(sl) and os.path.exists(bl)):
        return falhas
    with open(sl, encoding="utf-8") as fh:
        doc = fh.read()
    with open(bl, encoding="utf-8") as fh:
        blocos = json.load(fh)
    aula = "/".join(pasta.replace("\\", "/").rstrip("/").split("/")[-2:])
    for n, corpo in telas(doc):
        secs = re.findall(r"<!--BLOCOS:([a-z0-9]+)-->", corpo)
        exercicios = [b for s in secs for b in (blocos.get(s) or [])
                      if isinstance(b, dict) and b.get("kind") in EXERCICIO]
        if not exercicios:
            continue
        onde = f"{aula} tela {n}"
        if not (classes(corpo) & set(ENUNCIADO)):
            falhas.append((onde, f"{onde}: injeta {secs} e nao tem enunciado na tela. A "
                                 f"aluna ve o exercicio sem saber o que fazer com ele."))
        for b in exercicios:
            tem = [k for k in ("abertura", "instr", "pt") if b.get(k)]
            if tem:
                falhas.append((onde, f"{onde}: o bloco {b.get('id')} traz {tem} proprio. No "
                                     f"in-class quem enuncia e a TELA -- o `pt` do bloco "
                                     f"vira acordeao fechado, e o enunciado sai depois do "
                                     f"material em vez de antes."))
    return falhas


def aulas(alvos):
    if alvos:
        return [a.rstrip("/") for a in alvos]
    return sorted(os.path.dirname(p) for p in
                  glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                                         "slides.html")))


def main(argv):
    falhas, perdoados, medidas = [], [], 0
    for pasta in aulas(argv):
        if not os.path.isdir(pasta):
            continue
        medidas += 1
        for onde, msg in confere(pasta):
            (perdoados if onde in PENDENTES else falhas).append(msg)
    for m in perdoados:
        print(f"{AMARELO}PENDENTE{ZERA} {m}")
    for m in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {m}")
    if perdoados:
        print(f"\n{AMARELO}{len(perdoados)} pendente(s) declarado(s){ZERA} — "
              f"{POR_QUE_PENDENTE}.")
    if falhas:
        print(f"\n{VERMELHO}GATE 63 REPROVOU{ZERA} — {len(falhas)} tela(s) com exercicio e "
              f"sem enunciado proprio.")
        return 1
    print(f"{VERDE}GATE 63 OK{ZERA} — {medidas} aula(s): toda tela com exercicio enuncia a "
          f"tarefa nela mesma.")
    return 0


def selftest():
    cab = ('<div class="slide slide-dark" data-slide="6" data-stage="5" data-lesson="1" '
           'data-teacher="" data-snap="5">\n  <div class="slide-inner">\n'
           '    <span class="stage-pill">5 &middot; One word, or a sentence</span>\n'
           '    <h2 class="slide-heading">One word, <span class="accent">or a sentence?</span></h2>\n')
    instr = ('    <p class="slide-question">Mark the two whole sentences.'
             '<span class="slide-pt">Marque as duas frases inteiras.</span></p>\n')
    fim = "    <!--BLOCOS:cl1-->\n  </div>\n</div>\n"
    limpo = {"kind": "escolha", "id": "cl1", "itens": [{"t": "a", "ok": True}]}
    sujo = dict(limpo, abertura=["Two of these are whole sentences."],
                pt="Duas destas sao frases inteiras.")
    casos = [
        ("tela com exercicio e sem enunciado", True, cab + fim, limpo),
        ("tela com enunciado proprio", False, cab + instr + fim, limpo),
        ("enunciado dentro do bloco (o defeito da aula 1)", True, cab + instr + fim, sujo),
    ]
    erros = 0
    for nome, deve, slides, bloco in casos:
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "slides.html"), "w", encoding="utf-8") as fh:
                fh.write(slides)
            with open(os.path.join(d, "blocos.json"), "w", encoding="utf-8") as fh:
                json.dump({"cl1": [bloco]}, fh)
            pegou = bool(confere(d))
        if pegou != deve:
            erros += 1
        print(f"  {(VERDE + 'ok' + ZERA) if pegou == deve else (VERMELHO + 'ERRO' + ZERA)}  "
              f"{nome}: esperado {'FALHA' if deve else 'passa'}, deu "
              f"{'FALHA' if pegou else 'passa'}")
    print("selftest OK" if not erros else f"selftest com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
