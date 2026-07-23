#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Health", "the good state of your body and mind"),
    ("Exercise", "physical activity you do to stay strong and fit"),
    ("Sleep", "the rest you get when you close your eyes at night"),
    ("Meal", "the food you eat at one time, like breakfast or lunch"),
    ("Habit", "something you do often, almost without thinking"),
    ("Energy", "the power your body has to do things"),
    ("Stress", "a feeling of worry or pressure"),
    ("Balance", "a healthy mix between work and rest"),
    ("To relax", "to become calm and let go of worry"),
    ("To rest", "to stop and give your body a short break"),
]
defs = [d for _, d in pairs]
rng = random.Random(1010)

rows = []
for i, (word, ans) in enumerate(pairs):
    opts = defs[:]
    # embaralha ate a resposta correta NAO cair na mesma posicao do word (REGRA 24)
    while True:
        rng.shuffle(opts)
        if opts.index(ans) != i:
            break
    opt_html = '<option value="">Select...</option>'
    for o in opts:
        opt_html += f'<option value="{o}">{o}</option>'
    rows.append(
        f'        <div class="match-row" data-answer="{ans}">'
        f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>'
    )

block = '\n'.join(rows)
s = open(PC, encoding='utf-8').read()
assert '<!--MATCH-ROWS-->' in s, 'placeholder ja substituido?'
s = s.replace('<!--MATCH-ROWS-->', block)
open(PC, 'w', encoding='utf-8').write(s)
print(f'injetadas {len(rows)} match-rows embaralhadas')
