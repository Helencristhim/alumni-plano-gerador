#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Eloquent", "speaking in a clear, strong, and beautiful way"),
    ("Register", "the level of formal or casual language you choose"),
    ("Fluency", "the ability to speak smoothly, without stopping too much"),
    ("Credibility", "the quality of being trusted and believed by others"),
    ("Assertive", "confident and direct, in a calm and positive way"),
    ("Formal", "polite and professional, for serious situations"),
    ("Rapport", "a friendly, easy connection between two people"),
    ("Concise", "short and clear, with no extra words"),
    ("Spontaneous", "natural and not planned in advance"),
    ("Articulate", "able to express your ideas clearly in words"),
]
defs = [d for _, d in pairs]
rng = random.Random(2020)

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
