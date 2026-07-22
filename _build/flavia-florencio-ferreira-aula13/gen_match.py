#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Opinion", "an idea or feeling you have about something"),
    ("Perspective", "a particular way of seeing a situation"),
    ("Argument", "the reasons you give to support your idea"),
    ("Evidence", "facts that show that something is true"),
    ("Position", "the opinion a person holds on a topic"),
    ("Counterpart", "a person with the same job in another company"),
    ("Point", "the main idea in what someone says"),
    ("To agree", "to have the same opinion as someone"),
    ("To disagree", "to have a different opinion from someone"),
    ("To assert", "to say your idea firmly and with confidence"),
]
defs = [d for _, d in pairs]
rng = random.Random(1313)

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
