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
    ("A turning point", "the moment where an important change begins"),
    ("The last straw", "the final small problem that makes you act, after many others"),
    ("To snap", "to suddenly lose your patience after holding it for a long time"),
    ("Gridlocked", "so blocked by traffic that nothing moves at all"),
    ("To dawn on somebody", "to become clear to somebody for the very first time"),
    ("On a whim", "suddenly, with no planning at all behind it"),
    ("To talk somebody out of it", "to persuade somebody not to do what they were planning"),
    ("Reckless", "acting without thinking about the risk"),
    ("To hand in your notice", "to tell your employer formally that you are leaving"),
    ("To go through with", "to actually do the difficult thing you had decided to do"),
    ("To burn your bridges", "to destroy any chance of going back to what you left"),
    ("Second thoughts", "the doubts that arrive after you have already decided"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(6060 + i)
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
        f'<span class="match-word" style="flex:0 0 190px">{word}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{options}</select></div>')

block = '\n'.join(rows)
html = open(PC, encoding='utf-8').read()
assert '<!--MATCH-ROWS-->' in html, 'placeholder ja consumido?'
html = html.replace('<!--MATCH-ROWS-->', block)
open(PC, 'w', encoding='utf-8').write(html)
print(f'OK: {len(PAIRS)} match-rows embaralhadas injetadas em {PC}')
