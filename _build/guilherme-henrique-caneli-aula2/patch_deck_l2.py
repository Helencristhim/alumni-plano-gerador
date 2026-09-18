#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troca o deck IN CLASS da Aula 2 no arquivo do professor e espelha para o aluno.

Substitui, no arquivo standalone, tres blocos e so eles: a phase-bar, as
phase-labels e o slides-container. A casca (head, CSS, JS, nav, aba de menu)
fica byte a byte como estava, porque e ela que faz o slide-mode funcionar.

Depois roda o mirror_aluno.py do modelo, que e quem sabe produzir o espelho do
aluno (tira data-teacher, troca rotulos, aponta o EXIT para o hub do aluno).

USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/patch_deck_l2.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'guilherme-henrique-caneli-aula2.html')


def troca(s, abre_re, novo):
    """Troca o elemento que comeca em abre_re, fechando por BALANCO de <div>."""
    m = re.search(abre_re, s)
    assert m, 'bloco nao encontrado: %s' % abre_re
    depth = 0
    for t in re.finditer(r'<div\b|</div\s*>', s[m.start():]):
        depth += 1 if t.group(0).startswith('<div') else -1
        if depth == 0:
            fim = m.start() + t.end()
            return s[:m.start()] + novo + s[fim:]
    raise AssertionError('bloco nao fecha: %s' % abre_re)


def main():
    novo = open(os.path.join(HERE, 'slides.html'), encoding='utf-8').read()
    partes = re.search(r'(<div class="phase-bar".*?</div>)\s*(<div class="phase-labels".*?</div>)\s*'
                       r'(<div class="slides-container".*)', novo, re.S)
    assert partes, 'slides.html nao tem os tres blocos esperados'
    bar, labels, container = partes.group(1), partes.group(2), partes.group(3).rstrip()

    s = open(PROF, encoding='utf-8').read()
    antes_slides = len(re.findall(r'data-slide="\d', s))
    # O deck original ja nasce com +1 <div> (uma tag dentro de string de JS, que o
    # GATE 4 ignora porque pula script/style). A trava certa e o DELTA: o patch nao
    # pode piorar o balanco, e nao precisa consertar divida que nao e dele.
    def saldo(x):
        return len(re.findall(r'<div\b', x)) - len(re.findall(r'</div\s*>', x))
    antes_saldo = saldo(s)
    s = troca(s, r'<div class="phase-bar"[^>]*>', bar)
    s = troca(s, r'<div class="phase-labels"[^>]*>', labels)
    s = troca(s, r'<div class="slides-container"[^>]*>', container)

    # A navegacao do deck e HARDCODED no JS: totalSlides, o mapa slidePhases e o
    # texto inicial do contador. Trocar os slides sem trocar estes tres deixa o
    # deck preso no numero antigo -- o botao Next morre no slide 35 e a barra de
    # fases aponta para a fase errada. Nao ha gate que pegue isso: o JS compila.
    pares = re.findall(r'data-slide="(\d+)" data-phase="(\d+)"', container)
    total = len(pares)
    s = re.sub(r'var totalSlides = \d+;', 'var totalSlides = %d;' % total, s)
    s = re.sub(r'var slidePhases = \{[^}]*\};',
               'var slidePhases = {%s};' % ','.join('%s:%s' % (n, f) for n, f in pares), s)
    s = re.sub(r'(<span class="slide-counter" id="slideCounter">)[^<]*(</span>)',
               r'\g<1>01 / %02d\g<2>' % total, s)

    depois_slides = len(re.findall(r'data-slide="\d', s))
    assert depois_slides >= antes_slides, ('deck encolheu: %d -> %d slides (GATE 3 barra)'
                                           % (antes_slides, depois_slides))
    assert saldo(s) == antes_saldo, ('balanco de <div> mudou: %d -> %d' % (antes_saldo, saldo(s)))
    fns = set(re.findall(r'function ([a-zA-Z0-9_]+)\(', s))
    usados = set(re.findall(r'on\w+="([a-zA-Z0-9_]+)\(', container))
    assert usados <= fns, 'handler sem funcao no deck: %s' % sorted(usados - fns)
    open(PROF, 'w', encoding='utf-8').write(s)
    print('  + professor: %d -> %d slides' % (antes_slides, depois_slides))

    r = subprocess.run([sys.executable, os.path.join(ROOT, '_build', 'model', 'mirror_aluno.py'), PROF],
                       capture_output=True, text=True, cwd=ROOT)
    print((r.stdout or r.stderr).strip())
    assert r.returncode == 0, 'mirror_aluno falhou'


if __name__ == '__main__':
    main()
