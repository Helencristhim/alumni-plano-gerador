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
    ("Requirement", "something the system must do, agreed with the client"),
    ("To escalate", "to pass a serious issue to a higher level or team"),
    ("Root cause", "the real, underlying reason for a problem"),
    ("Blocker", "something that stops you from making progress on a task"),
    ("To follow up", "to check on something or continue it after a first contact"),
    ("Edge case", "an unusual situation at the limit of normal use"),
    ("To deploy", "to release software so that users can use it"),
    ("Outage", "a period when a system is down and unavailable"),
    ("Trade-off", "a balance between two good things you cannot both fully have"),
    ("To mitigate", "to make a risk or a problem less serious"),
    ("To reiterate", "to say something again to make it clear or to stress it"),
    ("To signpost", "to use small phrases that guide the listener through your answer"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1919 + i)
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
