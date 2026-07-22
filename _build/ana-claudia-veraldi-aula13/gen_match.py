#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer)
PAIRS = [
    ("Adaptation", "the process of changing to fit a new situation"),
    ("Transition", "a change from one situation, job, or state to another"),
    ("To adjust", "to change slightly to fit a new situation"),
    ("Mindset", "a person's usual way of thinking and attitude"),
    ("Comfort zone", "the familiar situation where you feel safe and relaxed"),
    ("To embrace", "to accept something new willingly and with enthusiasm"),
    ("Unfamiliar", "not known to you; new and a little strange"),
    ("Gradual", "happening slowly, in small steps"),
    ("To settle in", "to become comfortable in a new place or role"),
    ("Resilience", "the ability to recover quickly from difficulty"),
    ("Shift", "a change in position, focus, or direction"),
    ("To thrive", "to grow and do very well"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1313 + i)
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
