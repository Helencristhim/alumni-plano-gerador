#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 13 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-12 nem a anomalia do cronograma. So:
  - substitui o CARD PLACEHOLDER da aula 13 (Pre-class) pelo accordion real (prof E aluno)
  - insere stamp13 logo apos stamp12 (prof E aluno)
  - insere o bloco de Complementares da aula 13 apos o bloco da aula 12 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 13 logo apos o card da aula 12 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 13)
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

# --- placeholder da aula 13 (Pre-class) a ser substituido pelo accordion real ---
PLACEHOLDER13 = (
    '<div class="lesson-card">\n'
    '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
    '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80\');opacity:0.35;"></div>\n'
    '    <div class="lesson-header-content">\n'
    '      <div class="lesson-number">Aula 13 — Pre-class</div>\n'
    '      <h3 style="opacity:0.7;">What Were You Doing? — Past Continuous &amp; Yesterday</h3>\n'
    '      <div class="lesson-desc" style="font-style:italic;color:var(--text-dim);">Conteúdo será adicionado no próximo bloco.</div>\n'
    '    </div>\n'
    '    <div class="expand-icon">&#9660;</div>\n'
    '  </div>\n'
    '  <div class="lesson-body"><p style="text-align:center;padding:2rem;color:var(--text-dim);font-style:italic;">Conteúdo será adicionado no próximo bloco.</p></div>'
)

STAMP12 = ('<div class="stamp" id="stamp12" data-label="Shopping" style="background-image:url(\''
           'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=200&q=80\')"></div>')
STAMP13 = ('\n        <div class="stamp" id="stamp13" data-label="Directions" style="background-image:url(\''
           'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 12 (anchor) + card da aula 13 (so prof) ---
CARD12 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula12.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.38 3.46L16 2a4 4 0 01-8 0L3.62 3.46a2 2 0 00-1.34 2.23l.58 3.47a1 1 0 00.99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 002-2V10h2.15a1 1 0 00.99-.84l.58-3.47a2 2 0 00-1.34-2.23z"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 12</div>\n'
    '    <div class="ilc-title">Shopping in the City</div>\n'
    '    <div class="ilc-desc">Shopping for clothes in Paris &mdash; how much / how many + comparative adjectives &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD13 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula13.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-1.447-.894L15 4m0 13V4m0 0L9 7"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 13</div>\n'
    '    <div class="ilc-title">Getting Around the City</div>\n'
    '    <div class="ilc-desc">Public transport and asking for directions in Paris &mdash; imperatives + Where is / How do I get to &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 12 (ultimo wrapper l12-youtube) ---
COMP12_ANCHOR_RE = r'(data-media="l12-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp13 logo apos stamp12
    assert s.count(STAMP12) == 1, f'{path}: ancora stamp12 nao unica'
    s = s.replace(STAMP12, STAMP12 + STAMP13, 1); n += 1

    # 3. accordion Pre-class: substitui o placeholder da aula 13 pelo conteudo real
    assert s.count(PLACEHOLDER13) == 1, f'{path}: placeholder da aula 13 nao encontrado/unico'
    s = s.replace(PLACEHOLDER13, preclass, 1); n += 1

    # 4. complementares: append apos o bloco da aula 12 (ultimo wrapper l12-youtube)
    m_comp = re.search(COMP12_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l12-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l12-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 13 (so prof)
    if is_prof:
        assert s.count(CARD12) == 1, f'{path}: ancora card IN CLASS aula 12 nao unica'
        s = s.replace(CARD12, CARD12 + CARD13, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
