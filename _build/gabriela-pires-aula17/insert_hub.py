#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 17 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-16 nem a anomalia do cronograma (ex-lesson 21-25). So:
  - insere o accordion real da aula 17 (Pre-class) ANTES do ex-lesson-21 (prof E aluno)
  - insere stamp17 logo apos stamp16 (prof E aluno)
  - insere o bloco de Complementares da aula 17 apos o bloco da aula 16 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 17 logo apos o card da aula 16 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 17)
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

# --- ancora: accordion da aula 17 entra ANTES do ex-lesson-21 (nao ha placeholder p/ 17) ---
LESSON21_ANCHOR = '<div class="lesson-card" id="ex-lesson-21">'

STAMP16 = ('<div class="stamp" id="stamp16" data-label="City Tour" style="background-image:url(\''
           'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80\')"></div>')
STAMP17 = ('\n        <div class="stamp" id="stamp17" data-label="Gift Shop" style="background-image:url(\''
           'https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 16 (anchor) + card da aula 17 (so prof) ---
CARD16 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula16.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 16</div>\n'
    '    <div class="ilc-title">Asking About the City</div>\n'
    '    <div class="ilc-desc">A guided tour in Paris and getting information &mdash; Can you tell me...? + Is there...? &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD17 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula17.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 17</div>\n'
    '    <div class="ilc-title">Buying Gifts &amp; Making Choices</div>\n'
    '    <div class="ilc-desc">Shopping for gifts in a Paris gift shop &mdash; choosing with one / ones + Which one...? &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 16 (ultimo wrapper l16-youtube) ---
COMP16_ANCHOR_RE = r'(data-media="l16-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp17 logo apos stamp16
    assert s.count(STAMP16) == 1, f'{path}: ancora stamp16 nao unica'
    s = s.replace(STAMP16, STAMP16 + STAMP17, 1); n += 1

    # 3. accordion Pre-class: insere o conteudo real da aula 17 ANTES do ex-lesson-21
    assert s.count(LESSON21_ANCHOR) == 1, f'{path}: ancora ex-lesson-21 nao encontrada/unica'
    s = s.replace(LESSON21_ANCHOR, preclass + '\n' + LESSON21_ANCHOR, 1); n += 1

    # 4. complementares: append apos o bloco da aula 16 (ultimo wrapper l16-youtube)
    m_comp = re.search(COMP16_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l16-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l16-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 17 (so prof)
    if is_prof:
        assert s.count(CARD16) == 1, f'{path}: ancora card IN CLASS aula 16 nao unica'
        s = s.replace(CARD16, CARD16 + CARD17, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
