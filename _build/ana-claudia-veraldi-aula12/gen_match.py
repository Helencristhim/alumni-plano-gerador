#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 12 (first conditional / planning)
PAIRS = [
    ("A forecast", "a statement about what the weather is probably going to do"),
    ("A downpour", "a short period of very heavy rain"),
    ("To call off", "to cancel something that was already arranged"),
    ("To postpone", "to move an event to a later date"),
    ("A backup plan", "a second plan you keep ready in case the first one fails"),
    ("To fall through", "to fail before it happens, after it was already arranged"),
    ("To squeeze in", "to find time for something in a day that is already full"),
    ("On short notice", "with very little warning before something happens"),
    ("To count on", "to trust that something will happen or that somebody will help"),
    ("To run out of", "to use all of something so that none is left"),
    ("Chances are", "it is very likely that something will happen"),
    ("To be up to you", "to be your decision to make, and nobody can make it for you"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1220 + i)
    opts = defs[:]
    # embaralha ate que a definicao correta NAO caia na posicao i (REGRA 24)
    while True:
        rnd.shuffle(opts)
        if opts.index(answer) != i:
            break
    options = '<option value="">Select...</option>' + ''.join(
        f'<option value="{o}">{o}</option>' for o in opts)
    rows.append(
        f'        <div class="match-row" data-answer="{answer}">'
        f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{options}</select></div>')

block = '\n'.join(rows)
html = open(PC, encoding='utf-8').read()
assert '<!--MATCH-ROWS-->' in html, 'placeholder ja consumido?'
html = html.replace('<!--MATCH-ROWS-->', block)
open(PC, 'w', encoding='utf-8').write(html)
print(f'OK: {len(PAIRS)} match-rows embaralhadas injetadas em {PC}')
