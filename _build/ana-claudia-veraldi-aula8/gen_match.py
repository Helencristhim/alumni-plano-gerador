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
    ("To settle in", "to slowly start to feel at home in a new place"),
    ("A fresh start", "a chance to begin again, leaving the old life behind"),
    ("To end up", "to reach a place or a situation you did not plan"),
    ("To take stock", "to stop and think carefully about where you are now"),
    ("To stick with", "to continue with something even when it gets hard or slow"),
    ("Steady", "regular and unhurried, without sudden changes"),
    ("To unwind", "to let go of stress and relax after a busy day"),
    ("To get by", "to manage with the little money or help you have"),
    ("Sense of purpose", "the feeling that what you do every day matters"),
    ("To look forward to", "to feel happy about something that is coming"),
    ("Worn out", "very tired, or old and damaged by long use"),
    ("On the whole", "when you consider everything together"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(8080 + i)
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
