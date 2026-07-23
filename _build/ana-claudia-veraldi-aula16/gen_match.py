#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 16 (postmortems / conditionals)
PAIRS = [
    ("Postmortem", "a review after an incident to learn from it"),
    ("Retrospective", "a meeting to look back on what went well and badly"),
    ("Hindsight", "understanding a situation only after it has happened"),
    ("Incident", "an unplanned event that disrupts a service"),
    ("Outage", "a period when a system is down and unavailable"),
    ("Blameless", "focused on causes, not on blaming people"),
    ("Preventable", "able to have been avoided"),
    ("Takeaway", "a key lesson or point to remember"),
    ("Oversight", "an unintentional failure to notice or do something"),
    ("Near miss", "an event that almost caused harm but did not"),
    ("Contributing factor", "one of several causes that led to a problem"),
    ("To backfire", "to have the opposite effect to what was intended"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1610 + i)
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
