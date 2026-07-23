#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Information", "facts and details that you ask for or give"),
    ("Registration", "the desk where you sign in when you arrive at an event"),
    ("Entrance", "the door where you go into a building"),
    ("Restroom", "a public toilet or bathroom"),
    ("Elevator", "the machine that takes you up and down between floors"),
    ("Floor", "one level of a building"),
    ("Badge", "a card with your name that you wear at an event"),
    ("Hall", "a big room where an event takes place"),
    ("Directions", "the words that tell you how to get to a place"),
    ("Sign", "a board with words that shows you where to go"),
]
defs = [d for _, d in pairs]
rng = random.Random(1111)

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
