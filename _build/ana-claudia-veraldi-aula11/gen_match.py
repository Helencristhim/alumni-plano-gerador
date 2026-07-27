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
    ("To adjust", "to slowly change your habits so that a new situation feels normal"),
    ("Culture shock", "the confused feeling you get when everything around you works differently"),
    ("Overwhelming", "so strong or so much that you cannot deal with it easily"),
    ("Eerie", "strange and slightly frightening, in a very quiet way"),
    ("Homesick", "sad because you are far from the place you think of as home"),
    ("To crave", "to want something so badly that the feeling is almost physical"),
    ("Solitude", "time alone that you choose and enjoy"),
    ("Self-sufficient", "able to provide what you need without depending on other people"),
    ("To make do", "to manage with what you have, because nothing better is available"),
    ("To grow on you", "to become something you like, slowly, after not liking it at first"),
    ("A trade-off", "something good you give up in order to get something else"),
    ("Pitch-black", "completely dark, with no light at all"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(11100 + i)
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
