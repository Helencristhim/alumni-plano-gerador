#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 20 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-19 nem a anomalia do cronograma (ex-lesson 21-25). So:
  - insere o accordion real da aula 20 (Pre-class) ANTES do ex-lesson-21 (prof E aluno)
  - insere stamp20 logo apos stamp19 (prof E aluno)
  - insere o bloco de Complementares da aula 20 apos o bloco da aula 19 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 20 logo apos o card da aula 19 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 20)
Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_block = '\n'.join(l for l in m.group(1).splitlines() if l.strip())

# --- ancora: accordion da aula 20 entra ANTES do ex-lesson-21 (nao ha placeholder p/ 20) ---
LESSON21_ANCHOR = '<div class="lesson-card" id="ex-lesson-21">'

STAMP19 = ('<div class="stamp" id="stamp19" data-label="Plans" style="background-image:url(\''
           'https://images.unsplash.com/photo-1543007630-9710e4a00a20?w=200&q=80\')"></div>')
STAMP20 = ('\n        <div class="stamp" id="stamp20" data-label="Trip Recap" style="background-image:url(\''
           'https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 19 (anchor) + card da aula 20 (so prof) ---
CARD19 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula19.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 19</div>\n'
    '    <div class="ilc-title">Making Plans with Friends</div>\n'
    '    <div class="ilc-desc">Arranging to meet up with friends in Paris &mdash; present continuous for future + Let\'s / Why don\'t we &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD20 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula20.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 20</div>\n'
    '    <div class="ilc-title">My Paris Trip So Far</div>\n'
    '    <div class="ilc-desc">Looking back at the whole trip &mdash; present perfect with already / yet / just / ever &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 19 (ultimo wrapper l19-youtube) ---
COMP19_ANCHOR_RE = r'(data-media="l19-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp20 logo apos stamp19
    assert s.count(STAMP19) == 1, f'{path}: ancora stamp19 nao unica'
    s = s.replace(STAMP19, STAMP19 + STAMP20, 1); n += 1

    # 3. accordion Pre-class: insere o conteudo real da aula 20 ANTES do ex-lesson-21
    assert s.count(LESSON21_ANCHOR) == 1, f'{path}: ancora ex-lesson-21 nao encontrada/unica'
    s = s.replace(LESSON21_ANCHOR, preclass + '\n' + LESSON21_ANCHOR, 1); n += 1

    # 4. complementares: append apos o bloco da aula 19 (ultimo wrapper l19-youtube)
    m_comp = re.search(COMP19_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l19-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l19-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 20 (so prof)
    if is_prof:
        assert s.count(CARD19) == 1, f'{path}: ancora card IN CLASS aula 19 nao unica'
        s = s.replace(CARD19, CARD19 + CARD20, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
