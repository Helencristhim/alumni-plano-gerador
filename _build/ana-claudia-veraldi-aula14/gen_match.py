#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 14 (advanced modals / recommendations)
PAIRS = [
    ("Preference", "a thing you like or want more than another"),
    ("To recommend", "to advise something as the best choice"),
    ("Advisable", "wise or sensible to do"),
    ("Worthwhile", "worth the time, money or effort"),
    ("To opt for", "to choose one option instead of others"),
    ("Viable", "realistic and able to work as a choice"),
    ("Upside", "the positive part or advantage of a choice"),
    ("Rationale", "the reasons behind a decision"),
    ("Reluctant", "not wanting to do something; hesitant"),
    ("To lean toward", "to prefer or be inclined to one option"),
    ("Prudent", "careful and sensible; avoiding risk"),
    ("Compelling", "strong enough to convince you"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1410 + i)
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
