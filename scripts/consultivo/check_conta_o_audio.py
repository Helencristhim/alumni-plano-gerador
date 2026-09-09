#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 70 — a tela nao CONTA o audio: diz o que cada um faz.

O INCIDENTE (09/09/2026, aula 20 da Gabriela Pires)
----------------------------------------------------
Uma tela do deck afirmava, sobre o dialogo que a aluna acabara de ouvir:

    "In the conversation you just heard, Maya asks twice and Chris asks once."

O `talk.json` diz outra coisa. Maya pede o motivo UMA vez (turno 2, "Really? Why do you say
that?"); Chris devolve a pergunta UMA vez, no fim (turno 7). O numero na tela estava errado,
e a professora leria isso em voz alta, na frente da aluna, com o audio tocado ha um minuto.

Nenhum gate viu. O texto e gramatical, o exercicio funciona, e o audio bate
com todos os exercicios -- so a frase em prosa mentia.

POR QUE ESTE GATE PROIBE EM VEZ DE CONFERIR
--------------------------------------------
A primeira versao deste gate CONTAVA: turnos do falante, e turnos com "?". Ela nao pegava o
defeito. Medido no proprio caso: contando turnos com interrogacao, Maya tem DOIS (o turno 0
comeca com "So?"), entao "Maya asks twice" passaria -- e continuaria errado, porque
"asks" ali queria dizer "pede o motivo", que e uma leitura de FUNCAO e nao de pontuacao.

Contar da o numero certo de uma coisa que nao e a que a frase afirma. Entao a regra nao e
"o numero tem de bater": e **nao ponha na tela um numero que ninguem consegue conferir**.

E a mesma escolha que o catalogo ja faz no PRO-008, que proibe "a terceira" em vez de
verificar qual e a terceira: a ordem muda, o rotulo nao. Aqui: a contagem depende de como
se le a fala, a descricao do movimento nao.

    ERRADO   "Maya asks twice and Chris asks once."
    CERTO    "Maya asks Chris to explain, and at the end Chris asks her the same thing back."

A segunda diz mais, e continua verdadeira se o dialogo ganhar uma linha.

O QUE ELE MEDE
--------------
So material com o carimbo `alumni-anatomia=consultivo` E com algum dialogo (`var TALKS`).
Na superficie que um humano LE -- texto visivel, nota de tela (`data-teacher`), guia e
cartoes --, procura uma afirmacao de FREQUENCIA sobre um nome do elenco:

    <nome do elenco>  ...  (asks|says|speaks|answers|pergunta|diz|fala|responde)  N vezes

nas duas ordens, em ingles e em portugues. `once more` / `mais uma vez` ficam de fora: sao
instrucao de repeticao, nao contagem de fala.

BASE ZERO, MEDIDA ANTES DE ENTRAR
----------------------------------
Os SETE materiais da anatomia em 09/09/2026: nenhuma ocorrencia. O gate nasce sem divida e
sem alvara -- e a unica frase que ele teria barrado ja foi reescrita.

ESCOPO: o carimbo `alumni-anatomia=consultivo`. Gate novo nasce escopado.

USO:
    python3 scripts/consultivo/check_conta_o_audio.py [arquivo.html ...]
    python3 scripts/consultivo/check_conta_o_audio.py --selftest
"""
import glob
import html as _html
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# A contagem. `once` so conta como frequencia quando NAO e "once more"/"once again" -- e a
# diferenca entre "ele diz uma vez" e "diga mais uma vez", que e instrucao e aparece em toda
# tela de retask.
_NUM = (r"(?:once(?!\s+(?:more|again|you|she|he|they|it|the|a\b))"
        r"|twice"
        r"|(?:two|three|four|five|six|\d+)\s+times"
        r"|(?:uma|duas|tr[eê]s|quatro|cinco|seis|\d+)\s+vez(?:es)?)")
_VERBO = (r"(?:asks?|asked|says?|said|speaks?|spoke|answers?|answered|repeats?|repeated"
          r"|pergunta|perguntou|diz|disse|fala|falou|responde|respondeu|repete|repetiu)")

# Nos dois sentidos: "Maya asks twice" e "twice, Maya asks". A janela e curta de proposito --
# 60 caracteres cabem uma oracao, e nao um paragrafo inteiro que so por acaso tem as duas
# pontas.
_JANELA = 60


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def elenco(c):
    return re.findall(r'\{n:"([^"]+)",g:"[fm]"\}', c)


def tem_dialogo(c):
    m = re.search(r"var TALKS=(\{.*?\});", c, re.S)
    return bool(m) and m.group(1).strip() not in ("{}", "{ }")


def superficie(c):
    """So o que um humano LE: texto visivel, notas de tela, guia e cartoes."""
    teacher = " ".join(_html.unescape(m) for m in re.findall(r'data-teacher="([^"]*)"', c))
    corpo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", c, flags=re.S)
    corpo = _html.unescape(re.sub(r"<[^>]+>", " ", corpo))
    js = " ".join(_html.unescape(x) for x in
                  re.findall(r"var (?:GUIDE|CARDS)\s*=\s*(\{.*?\n\})", c, re.S))
    return re.sub(r"\s+", " ", corpo + "\n" + teacher + "\n" + js)


def confere(caminho_ou_texto, cru=False):
    c = caminho_ou_texto if cru else open(caminho_ou_texto, encoding="utf-8",
                                          errors="replace").read()
    if carimbo(c) != ANATOMIA:
        return None
    nomes = elenco(c)
    if not nomes or not tem_dialogo(c):
        return []
    s = superficie(c)
    # Os tres padroes se sobrepoem de proposito, e a MESMA frase casa em mais de um
    # ("Maya asks twice and Chris asks once" casa duas vezes pelo Chris). Reportar o mesmo
    # trecho duas vezes faz o autor procurar dois defeitos onde ha um: a deduplicacao e por
    # POSICAO no texto, e nao pelo texto casado, que muda de padrao para padrao.
    fora, cobertos = [], []
    for nome in nomes:
        n = re.escape(nome)
        for rx in (rf"\b{n}\b.{{0,{_JANELA}}}?{_VERBO}\s+{_NUM}",
                   rf"{_VERBO}\s+{_NUM}.{{0,{_JANELA}}}?\b{n}\b",
                   # "Three times, Maya says..." — o numero na frente. So com os tres termos
                   # COLADOS: afrouxar aqui traz "the three questions ... Maya ... says".
                   rf"{_NUM},?\s+\b{n}\b\s+{_VERBO}"):
            for m in re.finditer(rx, s, re.I):
                a, b = m.span()
                if any(a < fim and ini < b for ini, fim in cobertos):
                    continue
                cobertos.append((a, b))
                fora.append((nome, re.sub(r"\s+", " ", m.group(0)).strip()))
    return fora


def main(argv):
    alvos = argv or sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                           glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html")))
    print(f"=== GATE 70 — a tela nao conta o audio (anatomia {ANATOMIA}) ===")
    total, vistos = 0, 0
    for f in alvos:
        r = confere(f)
        if r is None:
            continue
        vistos += 1
        rel = os.path.relpath(f, RAIZ)
        for nome, trecho in r:
            total += 1
            print(f"  {VERMELHO}FAIL{ZERA}  {rel}: a tela conta quantas vezes {nome!r} fala "
                  f"— “{trecho}”.\n        Diga o que cada um FAZ, nao quantas vezes: "
                  f"“{nome} pede o motivo, e no fim o outro devolve a pergunta.” "
                  f"O numero e uma afirmacao sobre o audio que ninguem confere, e ja foi "
                  f"escrito errado uma vez.")
        if not r:
            print(f"  {VERDE}ok{ZERA}    {rel}")
    if total:
        print(f"\n{VERMELHO}GATE 70 — {total} contagem(ns) de fala em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"\n{VERDE}GATE 70 OK{ZERA} — {vistos} arquivo(s) com dialogo, e nenhum conta o audio "
          f"na tela.")
    return 0


CABECA = ('<meta name="alumni-anatomia" content="consultivo">'
          '<script>var CAST=[{n:"Maya",g:"f"},{n:"Chris",g:"m"}];'
          'var TALKS={20:[{s:0,t:"Really? Why do you say that?"}]};</script>')


def selftest():
    casos = [
        ("a frase do incidente", True,
         '<p>In the conversation you just heard, Maya asks twice and Chris asks once.</p>'),
        ("a reescrita que a substituiu", False,
         '<p>Maya asks Chris to explain, and at the end Chris asks her the same thing back.</p>'),
        ("contagem em portugues na nota de tela", True,
         '<div data-teacher="Repare que Chris responde duas vezes antes de ceder."></div>'),
        ("contagem na ordem inversa", True,
         '<p>Three times, Maya says the same thing.</p>'),
        ("‘once more’ e instrucao, nao contagem", False,
         '<p>Listen to Maya once more, and then answer.</p>'),
        ("‘mais uma vez’ tambem nao", False,
         '<div data-teacher="Toque a fala de Chris mais uma vez, devagar."></div>'),
        ("numero longe do nome nao casa", False,
         '<p>Maya is the one who starts. The whole class listens, answers the three '
         'questions on the screen, and then everybody says twice as much as before.</p>'),
        ("nome fora do elenco nao e medido", False,
         '<p>Sam asks twice and Alex asks once.</p>'),
        ("material sem dialogo nao e medido", False, None),
    ]
    erros = 0
    for nome, deve, corpo in casos:
        if corpo is None:
            html = ('<meta name="alumni-anatomia" content="consultivo">'
                    '<script>var CAST=[{n:"Maya",g:"f"}];var TALKS={};</script>'
                    '<p>Maya asks twice.</p>')
        else:
            html = CABECA + corpo
        pegou = bool(confere(html, cru=True))
        if pegou != deve:
            erros += 1
        print(f"  {(VERDE + 'ok' + ZERA) if pegou == deve else (VERMELHO + 'ERRO' + ZERA)}  "
              f"{nome}: esperado {'FALHA' if deve else 'passa'}, deu "
              f"{'FALHA' if pegou else 'passa'}")
    print("selftest OK" if not erros else f"selftest com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
