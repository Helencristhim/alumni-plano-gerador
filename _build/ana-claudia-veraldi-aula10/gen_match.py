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
    ("A creature of habit", "someone who always does the same things in the same order"),
    ("An errand", "a short trip you make to do one small necessary job"),
    ("To be stuck in a rut", "to be trapped in a routine that never changes and never improves"),
    ("Hectic", "very busy and fast, in a way that feels out of control"),
    ("To juggle", "to handle two or more demanding things at the same time"),
    ("To dread", "to feel fear or heavy dislike about something before it happens"),
    ("To bump into", "to meet someone by chance, with no plan at all"),
    ("To swap", "to give one thing up and take another in its place"),
    ("Second nature", "something you do so automatically that it takes no thought"),
    ("To cut back on", "to reduce how much of something you do or use"),
    ("Restless", "unable to relax, sit still or stay in one place"),
    ("Nowadays", "in the present period of time, in contrast with the past"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(10100 + i)
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
