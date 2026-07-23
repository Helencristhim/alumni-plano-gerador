#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 12 (second conditional / decisions)
PAIRS = [
    ("Trade-off", "a balance between two good things you cannot both fully have"),
    ("Hypothetical", "imagined, not real; used to think about a possible situation"),
    ("Contingency", "a plan for something that might go wrong"),
    ("To mitigate", "to make a risk or a problem less serious"),
    ("Downside", "the negative part or disadvantage of a choice"),
    ("To postpone", "to move something to a later time"),
    ("To justify", "to give a good reason for a decision"),
    ("To assess", "to judge how good, bad or risky something is"),
    ("Alternative", "another option you can choose instead"),
    ("Reasonable", "fair and sensible"),
    ("To reconsider", "to think again about a decision"),
    ("Cost-effective", "giving good value for the time or money spent"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1210 + i)
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
