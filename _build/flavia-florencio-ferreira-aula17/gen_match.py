#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Certification", "an official document that proves something is true"),
    ("Designation", "an official name or title given to something"),
    ("Origin", "the place where something comes from"),
    ("Territory", "an area of land in one region or country"),
    ("Artisanal", "made by hand in the traditional way"),
    ("Denomination", "the official name that shows where a product is from"),
    ("Producer", "a person or company that makes a product"),
    ("Label", "a small paper on a product with information about it"),
    ("Role", "the job or part you have in a team or meeting"),
    ("To explain", "to make something clear and easy to understand"),
]
defs = [d for _, d in pairs]
rng = random.Random(1717)

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
