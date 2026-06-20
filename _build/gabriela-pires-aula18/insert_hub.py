#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 18 (gerados pelo
build_from_model.py) nos hubs monoliticos da Gabriela Pires.

NAO toca aulas 1-17 nem a anomalia do cronograma (ex-lesson 21-25). So:
  - insere o accordion real da aula 18 (Pre-class) ANTES do ex-lesson-21 (prof E aluno);
    como a aula 17 ja vive imediatamente antes do ex-lesson-21, a 18 entra depois da 17
  - insere stamp18 logo apos stamp17 (prof E aluno)
  - insere o bloco de Complementares da aula 18 apos o bloco da aula 17 (prof E aluno)
  - mescla as entradas de audioMap (prof E aluno)
  - insere o card IN CLASS da aula 18 logo apos o card da aula 17 (SO prof)
  - NAO mexe em var totalLessons (=25, ja cobre a aula 18)
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

# --- ancora: accordion da aula 18 entra ANTES do ex-lesson-21 (a 17 ja esta antes do 21) ---
LESSON21_ANCHOR = '<div class="lesson-card" id="ex-lesson-21">'

STAMP17 = ('<div class="stamp" id="stamp17" data-label="Gift Shop" style="background-image:url(\''
           'https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=200&q=80\')"></div>')
STAMP18 = ('\n        <div class="stamp" id="stamp18" data-label="Postcard" style="background-image:url(\''
           'https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=200&q=80\')"></div>')

# --- card IN CLASS da aula 17 (anchor) + card da aula 18 (so prof) ---
CARD17 = (
    '<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula17.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 17</div>\n'
    '    <div class="ilc-title">Buying Gifts &amp; Making Choices</div>\n'
    '    <div class="ilc-desc">Shopping for gifts in a Paris gift shop &mdash; choosing with one / ones + Which one...? &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)
CARD18 = (
    '\n\n<a class="inclass-lesson-card" href="/professor/gabriela-pires-aula18.html#inclass" style="text-decoration:none;">\n'
    '  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="1"/><line x1="14" y1="5" x2="14" y2="19"/><circle cx="9" cy="10" r="2"/><path d="M5 16l3-3 2 2"/></svg></div>\n'
    '  <div class="ilc-info">\n'
    '    <div class="ilc-number">Lesson 18</div>\n'
    '    <div class="ilc-title">Sending a Postcard</div>\n'
    '    <div class="ilc-desc">At the post office in Paris &mdash; writing a short postcard and sending it with object pronouns (send it to her) &mdash; 60 min &mdash; 28 slides</div>\n'
    '  </div>\n'
    '  <div class="ilc-arrow">&rarr;</div>\n'
    '</a>'
)

# --- ancora do bloco de Complementares da aula 17 (ultimo wrapper l17-youtube) ---
COMP17_ANCHOR_RE = r'(data-media="l17-youtube".*?</div>\s*</div>\s*</div>)'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap (mescla as entradas no inicio do objeto)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp18 logo apos stamp17
    assert s.count(STAMP17) == 1, f'{path}: ancora stamp17 nao unica'
    s = s.replace(STAMP17, STAMP17 + STAMP18, 1); n += 1

    # 3. accordion Pre-class: insere o conteudo real da aula 18 ANTES do ex-lesson-21
    assert s.count(LESSON21_ANCHOR) == 1, f'{path}: ancora ex-lesson-21 nao encontrada/unica'
    s = s.replace(LESSON21_ANCHOR, preclass + '\n' + LESSON21_ANCHOR, 1); n += 1

    # 4. complementares: append apos o bloco da aula 17 (ultimo wrapper l17-youtube)
    m_comp = re.search(COMP17_ANCHOR_RE, s, re.S)
    assert m_comp, f'{path}: ancora l17-youtube (Complementares) nao encontrada'
    anchor = m_comp.group(1)
    assert s.count(anchor) == 1, f'{path}: ancora complementar l17-youtube nao unica'
    s = s.replace(anchor, anchor + '\n' + complementary, 1); n += 1

    # 5. card IN CLASS da aula 18 (so prof)
    if is_prof:
        assert s.count(CARD17) == 1, f'{path}: ancora card IN CLASS aula 17 nao unica'
        s = s.replace(CARD17, CARD17 + CARD18, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'gabriela-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'gabriela-pires.html'), False)
print('hubs atualizados (aditivo).')
