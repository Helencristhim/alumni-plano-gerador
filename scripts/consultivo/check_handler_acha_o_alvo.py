#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 68 — o handler acha o elemento que ele vai procurar.

O DEFEITO
---------
`czCheck(btn, id)` resolve o segundo parametro assim:

    var host = document.getElementById(id); if(!host) return;

Duas telas do MOLDE chamavam `czCheck(this)` -- **com um argumento so**. `id` chega
`undefined`, `getElementById(undefined)` devolve `null`, e a funcao RETORNA EM SILENCIO.
A aluna preenche as lacunas, clica em Check e nao acontece nada. Nao ha erro no console,
nao ha excecao, nao ha nada: o `if(!host)return` e uma guarda bem escrita fazendo
exatamente o que devia.

Achado em 09/09/2026, nas aulas 3 e 4 da stephanie-vicente -- o molde.

POR QUE O GATE 42 NAO PEGA
---------------------------
O 42 abre no chromium e CLICA, e a rede dele e o `pageerror`. Este defeito **nao estoura**:
o handler existe, compila, roda e sai. Clique que nao faz nada e clique que da certo sao
indistinguiveis para quem so escuta erro.

POR QUE NAO E UMA CHECAGEM DE ARIDADE
--------------------------------------
Medido antes de escrever a regra: **85** chamadas do consultivo passam menos argumentos do
que a funcao declara -- `playTalk`, `say`, `sayAs`. Todas certas: sao parametros opcionais
com valor padrao. Um gate de aridade seria 85 falsos positivos, e um gate com 100% de
falso positivo nao e rigor, e ruido que ensina a ignorar o CI.

O que sobra e a forma em que a falta E defeito por construcao: o parametro que a funcao
entrega a `getElementById`. Esse nao tem padrao -- ou vem, e existe, ou o handler morre
calado. A regra le o CORPO da funcao para descobrir QUAL parametro e esse; nao ha lista de
nomes de funcao escrita aqui.

DUAS PERGUNTAS
--------------
 1. O argumento que vira `getElementById` foi passado?
 2. Se e um literal, o id existe no documento?

ESCOPO: os arquivos publicados da anatomia consultivo, professor e aluno.

USO:
    python3 scripts/consultivo/check_handler_acha_o_alvo.py [arquivo ...]
    python3 scripts/consultivo/check_handler_acha_o_alvo.py --selftest
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

RX_HANDLER = re.compile(r'on\w+="([A-Za-z_$][\w$]*)\(([^"]*)\)[;"]')
RX_ID = re.compile(r'<[a-zA-Z][^>]*?\sid="([^"]+)"')
MARCA = 'name="alumni-anatomia" content="consultivo"'


def assinatura(html, nome):
    """(parametros, corpo) da funcao, ou (None, None). O corpo vai ate a chave que fecha."""
    m = re.search(r"function\s+" + re.escape(nome) + r"\s*\(([^)]*)\)\s*\{", html)
    if not m:
        return None, None
    params = [x.strip() for x in m.group(1).split(",") if x.strip()]
    i = m.end() - 1
    profundidade = 0
    for j in range(i, len(html)):
        if html[j] == "{":
            profundidade += 1
        elif html[j] == "}":
            profundidade -= 1
            if profundidade == 0:
                return params, html[i:j + 1]
    return params, html[i:]


def argumentos(texto):
    """Os argumentos do TOPO da chamada: virgula dentro de aspas ou de parenteses nao separa."""
    fora, nivel, atual, aspas = [], 0, "", None
    for ch in texto:
        if aspas:
            atual += ch
            if ch == aspas:
                aspas = None
            continue
        if ch in "'\"":
            aspas = ch
            atual += ch
            continue
        if ch in "([{":
            nivel += 1
        elif ch in ")]}":
            nivel -= 1
        if ch == "," and nivel == 0:
            fora.append(atual.strip())
            atual = ""
            continue
        atual += ch
    if atual.strip():
        fora.append(atual.strip())
    return fora


def posicoes_de_id(params, corpo):
    """Os indices dos parametros que a funcao entrega a `getElementById`."""
    return [i for i, p in enumerate(params)
            if re.search(r"getElementById\(\s*" + re.escape(p) + r"\s*\)", corpo or "")]


def confere_texto(html, rel):
    falhas = []
    ids = set(RX_ID.findall(html))
    cache = {}
    for m in RX_HANDLER.finditer(html):
        fn, crus = m.group(1), m.group(2)
        if fn not in cache:
            cache[fn] = assinatura(html, fn)
        params, corpo = cache[fn]
        if not params:
            continue
        alvos = posicoes_de_id(params, corpo)
        if not alvos:
            continue
        args = argumentos(crus)
        for i in alvos:
            if i >= len(args):
                falhas.append(
                    f"{rel}: {fn}(...) recebe {len(args)} argumento(s) e o {i + 1}º "
                    f"({params[i]!r}) e o que vai para getElementById. Sem ele o handler "
                    f"acha null e RETORNA EM SILENCIO — o clique nao faz nada, e nao da erro.")
                continue
            a = args[i]
            if len(a) > 1 and a[0] in "'\"" and a[-1] == a[0] and a[1:-1] not in ids:
                falhas.append(
                    f"{rel}: {fn}(...) procura o elemento {a} e nao ha nenhum com esse id.")
    return falhas


def materiais(alvos):
    if alvos:
        return alvos
    fora = []
    for sub in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", sub, "*.html"))):
            with open(p, encoding="utf-8", errors="replace") as fh:
                if MARCA in fh.read(4000):
                    fora.append(p)
    return fora


def main(argv):
    falhas, medidos = [], 0
    for p in materiais(argv):
        with open(p, encoding="utf-8", errors="replace") as fh:
            html = fh.read()
        medidos += 1
        falhas += confere_texto(html, os.path.relpath(p, RAIZ))
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 68 REPROVOU{ZERA} — {len(falhas)} handler(es) que nao "
              f"acham o elemento que vao procurar.")
        return 1
    print(f"{VERDE}GATE 68 OK{ZERA} — {medidos} arquivo(s): todo handler que resolve por id "
          f"recebe o id, e o id existe.")
    return 0


def selftest():
    JS = ("<script>function czCheck(btn,id){var h=document.getElementById(id);"
          "if(!h)return;}\nfunction say(t,r,v){var x=r||1;}</script>")
    casos = [
        ("id passado e existente", False,
         JS + '<div id="cz3"></div><button onclick="czCheck(this,\'cz3\')">C</button>'),
        ("id NAO passado — o handler morre calado", True,
         JS + '<div id="cz3"></div><button onclick="czCheck(this)">C</button>'),
        ("id passado e inexistente", True,
         JS + '<div id="cz3"></div><button onclick="czCheck(this,\'cz9\')">C</button>'),
        ("parametro opcional a menos — NAO e este defeito", False,
         JS + '<button onclick="say(\'hi\',0.9)">S</button>'),
        ("funcao que nao resolve por id", False,
         JS + '<button onclick="say(\'hi\')">S</button>'),
    ]
    erros = 0
    for nome, deve, html in casos:
        pegou = bool(confere_texto(html, "x.html"))
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
