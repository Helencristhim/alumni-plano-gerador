#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 16 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-15 nem a anomalia do cronograma (ex-lesson 21-25). So:
  - insere o accordion real da aula 16 (Pre-class) ANTES do ex-lesson-21 (prof E aluno)
  - insere stamp16 logo apos stamp15 (prof E aluno)
  - insere o bloco de Complementares da aula 16 apos o bloco da aula 15 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 16 logo apos o card da aula 15 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 16)
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

# --- ancora: accordion da aula 16 entra ANTES do ex-lesson-21 (nao ha placeholder p/ 16) ---
LESSON21_ANCHOR = '<div class="lesson-card" id="ex-lesson-21">'

STAMP15 = ('<div class="stamp" id="stamp15" data-label="Museum" style="background-image:url(\''
           'https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=200&q=80\')"></div>')
STAMP16 = ('\n        <div class="stamp" id="stamp16" data-label="City Tour" style="background-image:url(\''
           'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 15 (anchor) + card da aula 16 (so prof) ---
CARD15 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula15.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 15</div>\n'
    '    <div class="ilc-title">A Day at the Museum</div>\n'
    '    <div class="ilc-desc">Buying tickets and talking about art in Paris &mdash; How much is / How much are + There is / There are &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD16 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula16.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 16</div>\n'
    '    <div class="ilc-title">Asking About the City</div>\n'
    '    <div class="ilc-desc">A guided tour in Paris and getting information &mdash; Can you tell me...? + Is there...? &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 15 (ultimo wrapper l15-youtube) ---
COMP15_ANCHOR_RE = r'(data-media="l15-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp16 logo apos stamp15
    assert s.count(STAMP15) == 1, f'{path}: ancora stamp15 nao unica'
    s = s.replace(STAMP15, STAMP15 + STAMP16, 1); n += 1

    # 3. accordion Pre-class: insere o conteudo real da aula 16 ANTES do ex-lesson-21
    assert s.count(LESSON21_ANCHOR) == 1, f'{path}: ancora ex-lesson-21 nao encontrada/unica'
    s = s.replace(LESSON21_ANCHOR, preclass + '\n' + LESSON21_ANCHOR, 1); n += 1

    # 4. complementares: append apos o bloco da aula 15 (ultimo wrapper l15-youtube)
    m_comp = re.search(COMP15_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l15-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l15-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 16 (so prof)
    if is_prof:
        assert s.count(CARD15) == 1, f'{path}: ancora card IN CLASS aula 15 nao unica'
        s = s.replace(CARD15, CARD15 + CARD16, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
