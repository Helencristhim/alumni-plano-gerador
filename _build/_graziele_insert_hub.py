#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere ADITIVAMENTE os snippets de UMA aula (gerados pelo build_from_model.py,
modo snippets) nos hubs monoliticos de graziele-dias (prof E aluno).

NAO toca aulas anteriores. So adiciona: card IN CLASS (so prof), accordion
Pre-class (prof+aluno), bloco Complementares (prof+aluno), entradas de audioMap
(prof+aluno) e ajusta var totalLessons {N-1}->{N}. NAO insere stamp (stamps 1-5
ja existem no hub; programa de 50 aulas usa so 5 stamps).

USO: python3 _build/_graziele_insert_hub.py N
"""
import os, re, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SNIP = open(os.path.join(HERE, f'graziele-dias-aula{N}', 'hub_snippets.html'), encoding='utf-8').read()

def between(s, a, b):
    i = s.index(a) + len(a)
    j = s.index(b, i)
    return s[i:j].strip()

card = between(SNIP, '-->\n', '<!-- 2. STAMP') if '<!-- 2. STAMP' in SNIP else between(SNIP, '(inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 3. ACCORDION')
# part 1 card: take the <a ...>...</a> block
m = re.search(r'(<a href="/professor/graziele-dias-aula%d\.html\?autostart=1".*?</a>)' % N, SNIP, re.S)
card_prof = m.group(1)
card_aluno = card_prof.replace('/professor/graziele-dias-aula%d.html' % N, '/aluno/graziele-dias-aula%d.html' % N)

accordion = between(SNIP, '(inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
complementary = between(SNIP, f'(inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
amap_inner = between(SNIP, '<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>', '</script>')
amap_block = '\n'.join(l for l in amap_inner.splitlines() if l.strip())

PREV = N - 1

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    edits = 0
    # 1. audioMap (prof+aluno)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); edits += 1
    # 2. accordion Pre-class (prof+aluno)
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises anchor'
    s = s.replace('</div><!-- /tab-exercises -->', '\n' + accordion + '\n\n</div><!-- /tab-exercises -->', 1); edits += 1
    # 3. complementares (prof+aluno)
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary anchor'
    s = s.replace('</div><!-- /tab-complementary -->', '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); edits += 1
    # 4. totalLessons {PREV}->{N}
    assert f'var totalLessons={PREV}' in s, f'{path}: totalLessons={PREV} nao encontrado'
    s = s.replace(f'var totalLessons={PREV}', f'var totalLessons={N}', 1); edits += 1
    # 5. menu card (so prof) — inserir apos o </a> da card da aula anterior
    if is_prof:
        anchor_href = f'/professor/graziele-dias-aula{PREV}.html?autostart=1'
        idx = s.index(anchor_href)
        close = s.index('</a>', idx) + len('</a>')
        s = s[:close] + '\n' + card_prof + s[close:]
        edits += 1
    else:
        # aluno hub: cards do menu IN CLASS nao existem (aba so prof). Nada a fazer.
        pass
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({edits} edicoes, +{(len(s)-len(orig))//1024} KB)')

patch(os.path.join(ROOT, 'public', 'professor', 'graziele-dias.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'graziele-dias.html'), False)
print(f'aula {N}: hubs atualizados (aditivo).')
