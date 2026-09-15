#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 76 — no deck, a atividade fechada tambem e DECLARADA.

POR QUE ISTO EXISTE (15/09/2026)
--------------------------------
O GATE 45 tirou o exercicio da mao de quem escreve no pre-class e no post-class: o autor
declara em `blocos.json`, o `render.py` emite, e o `data-ok`, as classes e a ordem dos
atributos deixam de ser teclados. O proprio GATE 45 avisa o que ficou de fora: "O DECK ainda
nao e declarado — o slides.html continua com HTML de exercicio escrito a mao".

As aulas 19 a 21 da Gabriela, que o Dan tomou como exemplo em 15/09/2026, ja declaram TODA
atividade fechada do deck (`escolha`, `classificar`, `par`, `ordenar`, com `nu: true`). E foi
nessas atividades declaradas que a revisao pode exigir o que nenhum HTML a mao sustenta: o
`porque` por item, o embaralhamento pelo emissor, e o `Expected` do guia citando item por
item (GATE 71, que so enxerga o que esta em `blocos.json`). No molde, ate esta data, eram ZERO
marcadores `<!--BLOCOS:` no deck — e o molde e o que a geracao seguinte copia.

A REGRA
-------
Numa aula com carimbo gen >= 1, o `slides.html` nao contem HTML de atividade fechada escrito
a mao: grade de classificar/completar, lista de marcar, par, ordenar, lacuna, cartao de acervo,
linha de frase — nem `data-ok`, que e o gabarito teclado.

Fica FORA, de proposito: a caixa de escrita do quadro de devolutiva (`fb-board`), que e
anotacao do professor e nao exercicio, e o player de escuta do deck. Nenhum dos dois tem
emissor hoje; cobrar declaracao deles seria cobrar uma forma que nao existe.

As marcas sao as do GATE 45 (lidas de la, uma lista so), menos essas duas.

ESCOPO: aulas com `geracao.json` gen >= 1 (scripts/consultivo/geracao.py).

USO:
    python3 scripts/consultivo/check_deck_declarado.py [pasta-do-aluno ...]
    python3 scripts/consultivo/check_deck_declarado.py --todas      # ignora o carimbo (sonda)
    python3 scripts/consultivo/check_deck_declarado.py --selftest
"""
import importlib.util
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import geracao  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "check_atividade_declarada", os.path.join(AQUI, "check_atividade_declarada.py"))
_g45 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_g45)

GEN = 1
FORA = {"escrita", "audio"}
MARCAS = [(p, o, k) for p, o, k in _g45.MARCAS if k not in FORA] + [
    (r'\sdata-ok="', "gabarito teclado (data-ok)", "o kind da atividade"),
]
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"


def confere_aula(pasta, todas=False):
    if not todas and geracao.gen(pasta) < GEN:
        return []
    sp = os.path.join(pasta, "slides.html")
    if not os.path.exists(sp):
        return []
    s = open(sp, encoding="utf-8").read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r'\sdata-teacher="[^"]*"', "", s)   # prosa do guia pode CITAR uma classe
    faltas = []
    for padrao, oque, kind in MARCAS:
        n = len(re.findall(padrao, s))
        if n:
            faltas.append(f"{geracao.chave(pasta)}: {n}x {oque} escrito a mao no deck — "
                          f"declare como `kind: {kind}` (com `nu: true`) no blocos.json e "
                          f"ponha <!--BLOCOS:chave--> na tela.")
    return faltas


def main(argv):
    todas = "--todas" in argv
    pastas = geracao.aulas([a for a in argv if not a.startswith("--")] or None)
    medidas = [p for p in pastas if todas or geracao.gen(p) >= GEN]
    faltas = []
    for p in pastas:
        faltas += confere_aula(p, todas)
    for f in faltas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if faltas:
        print(f"\n{VERMELHO}GATE 76 REPROVOU{ZERA} — atividade fechada escrita a mao no deck.")
        return 1
    print(f"{VERDE}GATE 76 OK{ZERA} — {len(medidas)} aula(s) medida(s) (gen >= {GEN}) de "
          f"{len(pastas)}; toda atividade fechada do deck vem do emissor.")
    return 0


def selftest():
    import json
    import tempfile

    def roda(slides, gen=1, nome="aluna-x/aula30"):
        with tempfile.TemporaryDirectory() as d:
            pasta = os.path.join(d, *nome.split("/"))
            os.makedirs(pasta)
            open(os.path.join(pasta, "slides.html"), "w", encoding="utf-8").write(slides)
            if gen is not None:
                json.dump({"gen": gen}, open(os.path.join(pasta, "geracao.json"), "w"))
            return bool(confere_aula(pasta))

    MOLDE = ('<div class="match-grid" id="ev1"><div class="match-row"><span class="match-word">'
             'x</span><select data-ok="B"><option value="A">a</option></select></div></div>')
    casos = [
        ("grade de classificar do molde (aula 1, tela 5)", MOLDE, 1, True),
        ("so o data-ok ja reprova", '<select data-ok="A"></select>', 1, True),
        ("lacuna a mao", '<input class="blank-input" placeholder="...">', 1, True),
        ("o marcador de bloco passa", '<div class="slide-inner"><!--BLOCOS:ev1--></div>', 1, False),
        ("o quadro de devolutiva (writebox) fica fora", '<textarea id="f" class="writebox">'
         '</textarea>', 1, False),
        ("o guia que CITA a classe nao e a classe", '<div class="slide" data-teacher="a '
         'match-grid"></div>', 1, False),
        ("aula anterior ao carimbo nao e medida", MOLDE, None, False),
    ]
    erros = 0
    for nome, s, gen, deve in casos:
        pegou = roda(s, gen, "gabriela-pires/aula19" if gen is None else "aluna-x/aula30")
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    # a carimbo ausente fora da lista congelada e material novo, e o builder recusa
    g, erro = geracao.le(os.path.join(tempfile.gettempdir(), "aluna-x", "aula99"))
    ok = bool(erro)
    erros += not ok
    print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  aula nova sem "
          f"geracao.json e recusada pelo carimbo: {'recusada' if erro else 'ACEITA'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(sys.argv[1:]))
