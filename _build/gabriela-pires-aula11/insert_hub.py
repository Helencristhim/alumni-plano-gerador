#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 11 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-10 nem a anomalia 21-25. So:
  - substitui o CARD PLACEHOLDER da aula 11 (Pre-class) pelo accordion real (prof E aluno)
  - insere stamp11 logo apos stamp10 (prof E aluno)
  - insere o bloco de Complementares da aula 11 no fim da grade "Por Aula" (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 11 logo apos o card da aula 10 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 11)
Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/gabriela-pires/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_block = '\n'.join(l for l in m.group(1).splitlines() if l.strip())

# --- placeholder da aula 11 (Pre-class) a ser substituido pelo accordion real ---
PLACEHOLDER11 = (
    '<div class="lesson-card">\n'
    '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
    '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80\');opacity:0.35;"></div>\n'
    '    <div class="lesson-header-content">\n'
    '      <div class="lesson-number">Aula 11 — Pre-class</div>\n'
    '      <h3 style="opacity:0.7;">Let\'s Eat! — Food, Menus &amp; Ordering at a Restaurant</h3>\n'
    '      <div class="lesson-desc" style="font-style:italic;color:var(--text-dim);">Conteúdo será adicionado no próximo bloco.</div>\n'
    '    </div>\n'
    '    <div class="expand-icon">&#9660;</div>\n'
    '  </div>\n'
    '  <div class="lesson-body"><p style="text-align:center;padding:2rem;color:var(--text-dim);font-style:italic;">Conteúdo será adicionado no próximo bloco.</p></div>\n'
    '</div>'
)

STAMP10 = ('<div class="stamp" id="stamp10" data-label="Looks" style="background-image:url(\''
           'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=200&q=80\')"></div>')
STAMP11 = ('\n        <div class="stamp" id="stamp11" data-label="Food" style="background-image:url(\''
           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 10 (anchor) + card da aula 11 (so prof) ---
CARD10 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula10.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 10</div>\n'
    '    <div class="ilc-title">What Do You Look Like?</div>\n'
    '    <div class="ilc-desc">Describing people &mdash; descriptive adjectives + has/is &mdash; 60 min &mdash; 29 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD11 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula11.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 002-2V2"/><path d="M7 2v20M21 15V2a5 5 0 00-5 5v6c0 1.1.9 2 2 2h3z"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 11</div>\n'
    '    <div class="ilc-title">Let\'s Eat!</div>\n'
    '    <div class="ilc-desc">Food, menus &amp; ordering at a restaurant &mdash; would like + countable/uncountable &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp11 logo apos stamp10
    assert s.count(STAMP10) == 1, f'{path}: ancora stamp10 nao unica'
    s = s.replace(STAMP10, STAMP10 + STAMP11, 1); n += 1

    # 3. accordion Pre-class: substitui o placeholder da aula 11 pelo conteudo real
    assert s.count(PLACEHOLDER11) == 1, f'{path}: placeholder da aula 11 nao encontrado/unico'
    s = s.replace(PLACEHOLDER11, preclass, 1); n += 1

    # 4. complementares: append no fim da grade "Por Aula" (apos a ultima wrapper aula-10-3)
    m_comp = re.search(r'(data-media="aula-10-3".*?</div>\s*</div>\s*</div>)', s, re.S)
    assert m_comp, f'{path}: ancora aula-10-3 (Por Aula) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar aula-10-3 nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 11 (so prof)
    if is_prof:
        assert s.count(CARD10) == 1, f'{path}: ancora card IN CLASS aula 10 nao unica'
        s = s.replace(CARD10, CARD10 + CARD11, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
