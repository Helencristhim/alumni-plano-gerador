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
    ("Renovation", "the work of repairing and improving an old building"),
    ("Beam", "a long, thick piece of wood that holds up a roof or a floor"),
    ("Plumbing", "the system of pipes that carries water through a building"),
    ("Wiring", "the system of electric cables inside the walls"),
    ("Leak", "a crack or a hole that lets water escape"),
    ("Damp", "slightly wet, in a way that damages walls and wood"),
    ("To sand down", "to rub a surface with rough paper until it is smooth"),
    ("To strip", "to remove the old paint or covering from a surface"),
    ("To salvage", "to save something old and useful before it is thrown away"),
    ("To knock down", "to destroy a wall or a building on purpose"),
    ("Rewarding", "giving a good feeling because the effort produced something real"),
    ("To be worth it", "good enough to justify the time, money and effort"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(7070 + i)
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
