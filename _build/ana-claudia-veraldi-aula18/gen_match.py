#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as match-rows EMBARALHADAS (REGRA 24) e injeta no placeholder do preclass.html.
Cada linha recebe TODAS as 12 definicoes como <option>, em ordem embaralhada e
diferente da ordem das palavras. Deterministico (seed fixa)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PC = os.path.join(HERE, 'preclass.html')

# (palavra, definicao == data-answer) -- 12 palavras NOVAS da aula 18 (fluency strategies)
PAIRS = [
    ("To hold the floor", "to keep control of the conversation and your turn to speak"),
    ("To stall", "to slow down on purpose to buy time before you answer"),
    ("Train of thought", "the line of thinking you are following as you speak"),
    ("To backtrack", "to go back and correct or restate what you just said"),
    ("To digress", "to move away from the main topic while you are speaking"),
    ("Tangent", "a related but off-topic point you drift onto"),
    ("To elaborate", "to add more detail to what you have said"),
    ("To reword", "to say the same thing using different words"),
    ("To improvise", "to speak without preparation, thinking on your feet"),
    ("To signpost", "to use small phrases that guide the listener through your answer"),
    ("To trail off", "to gradually stop speaking without finishing your sentence"),
    ("To ramble", "to talk on and on in an aimless, unfocused way"),
]

defs = [d for _, d in PAIRS]
rows = []
for i, (word, answer) in enumerate(PAIRS):
    rnd = random.Random(1810 + i)
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
