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
    ("Accent", "the way people from a country or region pronounce a language"),
    ("Intonation", "the way the voice rises and falls when we speak"),
    ("Word stress", "the part of a word we say with more force"),
    ("Pace", "the speed at which someone speaks"),
    ("To clarify", "to make something clearer or easier to understand"),
    ("To rephrase", "to say the same idea again using different words"),
    ("To catch", "to hear and understand what someone says"),
    ("Filler word", "a small sound or word, like um, used while thinking"),
    ("To mishear", "to hear something wrongly"),
    ("Context", "the situation around a word that helps you guess its meaning"),
    ("To confirm", "to check that something is true or correct"),
    ("Unclear", "hard to hear or understand"),
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
        f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{options}</select></div>')

block = '\n'.join(rows)
html = open(PC, encoding='utf-8').read()
assert '<!--MATCH-ROWS-->' in html, 'placeholder ja consumido?'
html = html.replace('<!--MATCH-ROWS-->', block)
open(PC, 'w', encoding='utf-8').write(html)
print(f'OK: {len(PAIRS)} match-rows embaralhadas injetadas em {PC}')
