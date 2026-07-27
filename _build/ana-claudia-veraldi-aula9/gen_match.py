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
    ("To mumble", "to speak quietly and unclearly, so the words run together"),
    ("To catch", "to hear and understand something that was said"),
    ("The gist", "the general meaning of something, without every single word"),
    ("Word for word", "every single word, exactly as it was said"),
    ("To trail off", "to stop speaking gradually, so the end of the sentence disappears"),
    ("To keep up", "to follow something that is moving too fast for you"),
    ("Filler word", "a small sound people use while they think, like um or you know"),
    ("To zone out", "to stop paying attention without deciding to"),
    ("Slang", "very informal words used inside one group or one region"),
    ("To rephrase", "to say the same idea again in different words"),
    ("To speak up", "to talk more loudly so that people can hear you"),
    ("To drown out", "to be so loud that another sound cannot be heard"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(9090 + i)
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
