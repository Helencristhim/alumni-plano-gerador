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


# O bloco tem marca de INICIO e de FIM porque o injetor precisa poder rodar de
# novo: sem elas, a segunda rodada ou duplicava a regra ou (com a guarda antiga,
# que so testava um seletor) silenciosamente NAO atualizava o resto do bloco.
CSS_INI = '/* === CPE aula 2: inicio (gerado por patch_deck_l2.py) === */'
CSS_FIM = '/* === CPE aula 2: fim === */'
CSS_ANTIGO = '/* === CPE: painel de gabarito (irmao do botao) === */'
CSS_ANTIGO_FIM = '.slide-dark .cpe-key { background:#fff;color:#1a1a2e; }'

CSS_KEY = CSS_INI + """
/* --- painel de gabarito (irmao do botao) --- */
.cpe-reveal { margin-top:1rem; }
.cpe-reveal .comp-q { margin-top:0; }
.cpe-key { display:none;border:1px solid var(--border);border-top:none;border-radius:0 0 10px 10px;background:var(--bg-elevated);padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7;color:var(--text); }
.comp-q.revealed + .cpe-key { display:block; }
.slide-dark .cpe-key { background:#fff;color:#1a1a2e; }

/* --- Part 6: as sete frases numa tela so, inteiras (pedido do professor) --- */
.cpe-sent-card { padding:1.1rem 1.3rem; }
.cpe-sents { display:flex;flex-direction:column;gap:.38rem; }
.cpe-sent { display:flex;gap:.6rem;align-items:flex-start;background:var(--bg-elevated);border:1px solid var(--border);border-radius:9px;padding:.42rem .75rem;font-size:.87rem;line-height:1.34;color:var(--text); }
.cpe-sent-k { flex:0 0 1.2rem;font-weight:700;color:var(--accent); }
.cpe-sent-foot { margin:.6rem 0 0;font-size:.8rem;line-height:1.4;color:var(--text-mid); }

/* --- Part 4: as duas tarefas e as dezesseis opcoes na MESMA tela --- */
.cpe-exam-intro { margin:0 0 .4rem;font-size:.82rem;line-height:1.42;color:var(--text-mid); }
.cpe-mini-row { display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center;margin-bottom:.45rem; }
.cpe-mini { display:flex;align-items:center;gap:.4rem;background:var(--bg-elevated);border:1px solid var(--border);border-radius:20px;padding:.22rem .7rem .22rem .25rem; }
.cpe-mini-btn { width:24px;height:24px;min-width:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;padding:0; }
.cpe-mini-lbl { font-size:.76rem;font-weight:600;color:var(--text);white-space:nowrap; }
.cpe-two { display:grid;grid-template-columns:1fr 1.32fr;gap:.7rem;align-items:start; }
.cpe-two .ic-card { margin-bottom:0;padding:.7rem .8rem; }
.cpe-two .ic-card-h3 { font-size:.92rem;margin-bottom:.25rem; }
.cpe-two .ic-match-hint { font-size:.72rem;margin-bottom:.15rem; }
.cpe-two .ic-match-score { font-size:.72rem;margin-bottom:.32rem; }
.cpe-two .ic-match { grid-template-columns:auto 1fr;gap:.6rem; }
.cpe-two .ic-match-col h4 { font-size:.66rem;margin-bottom:.28rem; }
.cpe-two .ic-chip { font-size:.72rem;line-height:1.24;padding:.24rem .42rem;margin-bottom:.19rem;border-radius:7px; }

/* --- Part 6: sete frases INTEIRAS numa lista de escolha, sem cortar --- */
.ic-card[data-dense] .ic-choices { gap:.35rem; }
.ic-card[data-dense] .ic-choice { font-size:.82rem;line-height:1.33;padding:.42rem .7rem;gap:.6rem;align-items:flex-start;border-radius:9px; }
.ic-card[data-dense] .ic-opt { margin-top:.05rem; }
""" + CSS_FIM


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
    if CSS_INI in s and CSS_FIM in s:
        a, b = s.index(CSS_INI), s.index(CSS_FIM) + len(CSS_FIM)
        s = s[:a] + CSS_KEY + s[b:]
    elif CSS_ANTIGO in s:
        # deck que ja recebeu a primeira versao do bloco, ainda sem marca
        a = s.index(CSS_ANTIGO)
        b = s.index(CSS_ANTIGO_FIM, a) + len(CSS_ANTIGO_FIM)
        s = s[:a] + CSS_KEY + s[b:]
    else:
        k = s.rindex('</style>')
        s = s[:k] + '\n' + CSS_KEY + '\n' + s[k:]
    assert s.count(CSS_INI) == 1, 'bloco de CSS duplicado'
    open(PROF, 'w', encoding='utf-8').write(s)
    print('  + professor: %d -> %d slides' % (antes_slides, depois_slides))

    r = subprocess.run([sys.executable, os.path.join(ROOT, '_build', 'model', 'mirror_aluno.py'), PROF],
                       capture_output=True, text=True, cwd=ROOT)
    print((r.stdout or r.stderr).strip())
    assert r.returncode == 0, 'mirror_aluno falhou'


if __name__ == '__main__':
    main()
