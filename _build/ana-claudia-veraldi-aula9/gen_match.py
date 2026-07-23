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
    ("Specification", "a detailed written description of what the software must do"),
    ("Scope", "the boundaries of what a project includes and excludes"),
    ("Acceptance criteria", "the conditions a feature must meet to be accepted"),
    ("Use case", "how a user interacts with the system to reach a goal"),
    ("Assumption", "something you treat as true without checking it"),
    ("Constraint", "a limit or restriction you have to work within"),
    ("End user", "the real person who will actually use the software"),
    ("To gather", "to collect information from different people or sources"),
    ("To sign off", "to formally approve that something is correct or complete"),
    ("To double-check", "to check something again to be completely sure"),
    ("Ambiguous", "not clear because it has more than one meaning"),
    ("Feasible", "possible to do within the time and limits you have"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(9090 + i)
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
