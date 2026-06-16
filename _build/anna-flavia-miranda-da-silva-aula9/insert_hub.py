#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 9 (gerados pelo
build_from_model.py) nos hubs monoliticos (inline) da Anna Flavia.

Nao toca aulas 1-8. So adiciona: card IN CLASS (so prof), stamp9, accordion
Pre-class, bloco de Complementares, entradas de audioMap (+ [order-l9]) e
ajusta var totalLessons=8 -> 9. Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/anna-flavia-miranda-da-silva/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l9] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l9]": "{AUDIO_BASE}pc9_order_sequence.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), no formato das cards existentes da Anna ---
CARD9 = (
    '  <a href="/professor/anna-flavia-miranda-da-silva-aula9.html?autostart=1" target="_blank" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '    <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>\n'
    '    <div><div style="font-weight:600;font-size:.95rem">Our Product: Sugar</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Adjectives &amp; describing our product -- 27 slides</div></div>\n'
    '  </a>')

STAMP8 = ('<div class="stamp" id="stamp8" data-label="Plans" style="background-image:url(\''
          'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=200&q=80\')"></div>')
STAMP9 = ('\n        <div class="stamp" id="stamp9" data-label="Product" style="background-image:url(\''
          'https://images.unsplash.com/photo-1581006852262-e4307cf6283a?w=200&q=80\')"></div>')

CARD08_TAIL = (
    '    <div><div style="font-weight:600;font-size:.95rem">Making Plans</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Going to (future) &amp; appointments -- 27 slides</div></div>\n'
    '  </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp9
    assert s.count(STAMP8) == 1, f'{path}: ancora stamp8 nao unica'
    s = s.replace(STAMP8, STAMP8 + STAMP9, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=8;' in s, f'{path}: totalLessons=8 nao encontrado'
    s = s.replace('var totalLessons=8;', 'var totalLessons=9;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD08_TAIL) == 1, f'{path}: ancora card 08 nao unica'
        s = s.replace(CARD08_TAIL, CARD08_TAIL + '\n' + CARD9, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'anna-flavia-miranda-da-silva.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'anna-flavia-miranda-da-silva.html'), False)
print('hubs atualizados (aditivo).')
