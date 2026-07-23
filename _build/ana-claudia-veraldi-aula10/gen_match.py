#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 10 (reporting a problem)
PAIRS = [
    ("Impact", "how badly a problem affects users or the business"),
    ("Symptom", "a visible sign that something is wrong"),
    ("Frequency", "how often a problem happens"),
    ("To resolve", "to fix a problem and close it"),
    ("Regression", "when something that worked before breaks after a change"),
    ("Reproducible", "able to be made to happen again in the same way"),
    ("Patch", "a small update that fixes a specific problem"),
    ("Downtime", "a period when the system is not available to users"),
    ("To roll back", "to return the software to an earlier working version"),
    ("Evidence", "facts, like logs or screenshots, that show what happened"),
    ("Concise", "giving clear information in few words"),
    ("Vague", "not clear or not specific enough"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1010 + i)
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
