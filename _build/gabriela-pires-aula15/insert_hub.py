#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 15 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-14 nem a anomalia do cronograma. So:
  - substitui o CARD PLACEHOLDER da aula 15 (Pre-class) pelo accordion real (prof E aluno)
  - insere stamp15 logo apos stamp14 (prof E aluno)
  - insere o bloco de Complementares da aula 15 apos o bloco da aula 14 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 15 logo apos o card da aula 14 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 15)
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

# --- placeholder da aula 15 (Pre-class) a ser substituido pelo accordion real ---
PLACEHOLDER15 = (
    '<div class="lesson-card">\n'
    '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
    '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80\');opacity:0.35;"></div>\n'
    '    <div class="lesson-header-content">\n'
    '      <div class="lesson-number">Aula 15 — Pre-class</div>\n'
    '      <h3 style="opacity:0.7;">Have You Ever…? — Experiences &amp; Present Perfect</h3>\n'
    '      <div class="lesson-desc" style="font-style:italic;color:var(--text-dim);">Conteúdo será adicionado no próximo bloco.</div>\n'
    '    </div>\n'
    '    <div class="expand-icon">&#9660;</div>\n'
    '  </div>\n'
    '  <div class="lesson-body"><p style="text-align:center;padding:2rem;color:var(--text-dim);font-style:italic;">Conteúdo será adicionado no próximo bloco.</p></div>'
)

STAMP14 = ('<div class="stamp" id="stamp14" data-label="Restaurant" style="background-image:url(\''
           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>')
STAMP15 = ('\n        <div class="stamp" id="stamp15" data-label="Museum" style="background-image:url(\''
           'https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 14 (anchor) + card da aula 15 (so prof) ---
CARD14 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula14.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 2v7c0 1.1.9 2 2 2h0c1.1 0 2-.9 2-2V2"/><path d="M5 2v20"/><path d="M16 2v20"/><path d="M16 11c2.2 0 4-1.8 4-4s-1.8-5-4-5"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 14</div>\n'
    '    <div class="ilc-title">Eating Out Like a Local</div>\n'
    '    <div class="ilc-desc">Ordering a dinner at a restaurant in Paris &mdash; I would like / Could I have + Can you recommend &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD15 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula15.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 15</div>\n'
    '    <div class="ilc-title">A Day at the Museum</div>\n'
    '    <div class="ilc-desc">Buying tickets and talking about art in Paris &mdash; How much is / How much are + There is / There are &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 14 (ultimo wrapper l14-youtube) ---
COMP14_ANCHOR_RE = r'(data-media="l14-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp15 logo apos stamp14
    assert s.count(STAMP14) == 1, f'{path}: ancora stamp14 nao unica'
    s = s.replace(STAMP14, STAMP14 + STAMP15, 1); n += 1

    # 3. accordion Pre-class: substitui o placeholder da aula 15 pelo conteudo real
    assert s.count(PLACEHOLDER15) == 1, f'{path}: placeholder da aula 15 nao encontrado/unico'
    s = s.replace(PLACEHOLDER15, preclass, 1); n += 1

    # 4. complementares: append apos o bloco da aula 14 (ultimo wrapper l14-youtube)
    m_comp = re.search(COMP14_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l14-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l14-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 15 (so prof)
    if is_prof:
        assert s.count(CARD14) == 1, f'{path}: ancora card IN CLASS aula 14 nao unica'
        s = s.replace(CARD14, CARD14 + CARD15, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
