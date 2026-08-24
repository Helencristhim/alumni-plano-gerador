#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrai do artefato os FRAGMENTOS de conteudo de cada aula — a entrada do builder.

O QUE ISTO PROVA
----------------
O builder monta uma aula a partir de fragmentos. Se os fragmentos sairem do proprio
artefato, o caminho fecha um circulo verificavel:

    artefato  ->  fragmentos  ->  builder  ->  material  ==  artefato

Se o material gerado nao voltar a ser o artefato (a menos da identidade do aluno), o
builder perdeu alguma coisa no caminho -- e o gate diz exatamente qual regiao. E a mesma
ideia do "prove o superset" do P2 §38, aplicada a geracao em vez da publicacao.

O QUE E UM FRAGMENTO
--------------------
As regioes que MUDAM por aula. O resto -- CSS, JS, chrome, abas, dialogo de confirmacao --
e shell, e nao entra aqui:

    aulaN/slides.html     as telas do deck daquela aula (data-lesson="N")
    aulaN/preclass.html   o bloco #pcN, com as seis atividades
    aulaN/postclass.html  o bloco #psN, com os cinco componentes
    aulaN/guide.json      os 14 campos do Teacher's Guide daquela aula
    aulaN/registro.json   a linha da aula no registro: tema, nav, stages, cod, framework

USO:
    python3 scripts/black/extrai_fragmentos.py [--destino _build/black/_do-artefato]
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-private-black.html")
DESTINO = os.path.join(RAIZ, "_build", "black", "_do-artefato")


def mascara_script_style(s):
    out = list(s)
    for m in re.finditer(r"<(script|style)\b[^>]*>(.*?)</\1\s*>", s, re.S):
        for k in range(m.start(2), m.end(2)):
            if out[k] != "\n":
                out[k] = "."
    return "".join(out)


def fecha_tag(s, i, tag="div"):
    d = 0
    for m in re.finditer(r"<" + tag + r"\b|</" + tag + r"\s*>", s[i:]):
        d += 1 if not m.group(0).startswith("</") else -1
        if d == 0:
            return i + m.end()
    raise SystemExit(f"<{tag}> aberta em {i} nao fecha")


def bloco_por_id(h, hm, ident, tag="div"):
    m = re.search(r"<" + tag + r'[^>]*id="' + re.escape(ident) + r'"[^>]*>', hm)
    if not m:
        return None
    return h[m.start():fecha_tag(hm, m.start(), tag)]


def slides_da_aula(h, hm, n):
    """Todas as telas com data-lesson="n", na ordem, sem tocar no que vem entre elas."""
    partes = []
    for m in re.finditer(r'<div class="slide[^"]*"[^>]*data-lesson="' + str(n) + r'"[^>]*>', hm):
        partes.append(h[m.start():fecha_tag(hm, m.start(), "div")])
    return "\n\n".join(partes)


def registro_da_aula(h, n):
    """A linha `n:{...}` do var LESSONS. Recortada por balanco de chaves, nao por regex de
    linha: os campos tem objetos dentro (stages) e virgulas dentro de string."""
    m = re.search(r"\n\s*" + str(n) + r":\{", h)
    if not m:
        return None
    i = h.index("{", m.start())
    prof, k = 0, i
    while k < len(h):
        if h[k] == "{":
            prof += 1
        elif h[k] == "}":
            prof -= 1
            if prof == 0:
                return h[i:k + 1]
        k += 1
    return None


def guide_da_aula(h, n):
    m = re.search(r"var GUIDE=\{", h)
    if not m:
        return None
    reg = re.search(r"\n\s*" + str(n) + r":\{", h[m.start():])
    if not reg:
        return None
    ini = m.start() + reg.start()
    i = h.index("{", ini)
    prof, k = 0, i
    while k < len(h):
        if h[k] == "{":
            prof += 1
        elif h[k] == "}":
            prof -= 1
            if prof == 0:
                return h[i:k + 1]
        k += 1
    return None


def main():
    destino = DESTINO
    if "--destino" in sys.argv:
        destino = os.path.join(RAIZ, sys.argv[sys.argv.index("--destino") + 1])
    h = open(ARTEFATO, encoding="utf-8").read()
    hm = mascara_script_style(h)

    aulas = sorted({int(x) for x in re.findall(r'data-lesson="(\d+)"', hm)})
    if not aulas:
        raise SystemExit("o artefato nao tem tela com data-lesson — mudou de forma")
    os.makedirs(destino, exist_ok=True)

    resumo = {}
    for n in aulas:
        pasta = os.path.join(destino, f"aula{n}")
        os.makedirs(pasta, exist_ok=True)
        pecas = {
            "slides.html": slides_da_aula(h, hm, n),
            "preclass.html": bloco_por_id(h, hm, f"pc{n}"),
            # `psb{n}` e o BOTAO que troca de aula; o bloco de conteudo e `ps{n}` -- mesmo
            # par do pre-class (`pcb{n}` botao, `pc{n}` bloco). Peguei o botao na primeira
            # tentativa e o extrator reprovou por conta propria, o que e o comportamento
            # certo: bloco que nao existe nao vira fragmento vazio.
            "postclass.html": bloco_por_id(h, hm, f"ps{n}"),
            "registro.js": registro_da_aula(h, n),
            "guide.js": guide_da_aula(h, n),
        }
        faltando = [k for k, v in pecas.items() if not v]
        if faltando:
            raise SystemExit(f"aula {n}: nao achei {faltando} no artefato")
        for arq, conteudo in pecas.items():
            with open(os.path.join(pasta, arq), "w", encoding="utf-8") as fh:
                fh.write(conteudo.strip() + "\n")
        resumo[n] = {k: len(v) for k, v in pecas.items()}
        resumo[n]["telas"] = len(re.findall(r'data-lesson="' + str(n) + r'"', pecas["slides.html"]))

    # as regioes que NAO sao por aula, mas sao do aluno: perfil e syllabus
    comuns = {
        "perfil.html": bloco_por_id(h, hm, "tab-planning"),
        "syllabus.html": bloco_por_id(h, hm, "tab-syllabus"),
    }
    for arq, conteudo in comuns.items():
        with open(os.path.join(destino, arq), "w", encoding="utf-8") as fh:
            fh.write(conteudo.strip() + "\n")

    print(f"=== fragmentos extraidos para {os.path.relpath(destino, RAIZ)}")
    for n, d in resumo.items():
        print(f"  aula {n}: {d['telas']} telas · slides {d['slides.html']}B · "
              f"pre-class {d['preclass.html']}B · post-class {d['postclass.html']}B · "
              f"guia {d['guide.js']}B")
    for arq, c in comuns.items():
        print(f"  {arq}: {len(c)}B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
