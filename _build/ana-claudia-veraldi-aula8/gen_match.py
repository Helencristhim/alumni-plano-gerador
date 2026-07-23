#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras de revisao do Bloco 1 (aulas 1-7)
PAIRS = [
    ("Requirement", "something the software must do"),
    ("To deploy", "to put new code on a server so people can use it"),
    ("Milestone", "an important point or achievement in a project"),
    ("Challenge", "a difficult task that tests your skills"),
    ("Workflow", "the steps a task goes through from start to finish"),
    ("To prioritize", "to decide what is most important to do first"),
    ("Severity", "how serious a bug is"),
    ("Root cause", "the real reason a problem happens"),
    ("Blocker", "something that stops you from making progress"),
    ("To follow up", "to check on something again later"),
    ("To clarify", "to make something clearer or easier to understand"),
    ("Edge case", "an unusual situation at the limit of what is expected"),
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
