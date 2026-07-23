#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows embaralhadas (REGRA 24) e injeta no preclass.html."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

pairs = [
    ("Inquiry", "a formal question or request for information"),
    ("Moderator", "a person who leads a meeting and gives everyone a turn to speak"),
    ("Panel", "a small group of experts who answer questions in front of people"),
    ("Follow-up", "a second question that asks for more detail"),
    ("Response", "what you say back when someone asks you a question"),
    ("Feedback", "useful comments about someone's work or ideas"),
    ("To confirm", "to say that something is true or correct"),
    ("To wonder", "to want to know something in a soft, polite way"),
    ("Polite", "kind and respectful in the way you speak"),
    ("To facilitate", "to help a meeting run in an easy, smooth way"),
]
defs = [d for _, d in pairs]
rng = random.Random(1919)

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
