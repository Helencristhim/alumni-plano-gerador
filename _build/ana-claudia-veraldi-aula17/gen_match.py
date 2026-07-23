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
    ("To relay", "to pass a message from one person to another"),
    ("To convey", "to communicate an idea or feeling so others clearly understand it"),
    ("To reiterate", "to say something again to make it clear or to stress it"),
    ("To paraphrase", "to restate what someone said in your own words"),
    ("To notify", "to formally tell someone that something has happened"),
    ("To acknowledge", "to confirm that you have received or noticed something"),
    ("Recipient", "the person who receives a message or email"),
    ("Thread", "a connected series of messages or emails on one topic"),
    ("Chain of command", "the order in which people report to and answer to each other"),
    ("Discrepancy", "a difference between two accounts or numbers that should match"),
    ("Wording", "the specific choice of words used in a message"),
    ("Verbatim", "using exactly the same words; word for word"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1717 + i)
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
