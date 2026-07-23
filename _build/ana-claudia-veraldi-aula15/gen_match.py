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
    ("To suggest", "to hint that something is probably true, without stating it directly"),
    ("Tentative", "not final or certain; said or done with caution"),
    ("Apparently", "based on what seems true, though not fully confirmed"),
    ("Presumably", "most likely; used when you assume something is true"),
    ("To imply", "to communicate something indirectly, without saying it openly"),
    ("Cautious", "careful to avoid mistakes or risks; not rushing to conclusions"),
    ("Seemingly", "in a way that appears to be true, on the surface"),
    ("To downplay", "to make something seem less important or serious than it is"),
    ("Roughly", "approximately; not exactly"),
    ("To soften", "to make a message gentler or less direct"),
    ("Understated", "expressed in a calm, restrained way, without exaggeration"),
    ("To qualify", "to add a detail that limits a statement and makes it less absolute"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1515 + i)
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
