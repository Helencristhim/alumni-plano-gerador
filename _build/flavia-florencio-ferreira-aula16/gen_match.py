#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Institution", "an organization created for a public purpose"),
    ("Representative", "a person who speaks or acts for an organization"),
    ("Portfolio", "the full range of programs or products an organization offers"),
    ("Bilateral", "between two countries, groups, or sides"),
    ("Protocol", "the formal rules and steps people follow"),
    ("Affiliation", "an official connection to an organization"),
    ("Delegation", "a group of people who represent a country or group"),
    ("Headquarters", "the main office of an organization"),
    ("Sector", "a part of the economy or area of business"),
    ("Reputation", "the opinion people have about someone or something"),
]
defs = [d for _, d in pairs]
rng = random.Random(1616)

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
