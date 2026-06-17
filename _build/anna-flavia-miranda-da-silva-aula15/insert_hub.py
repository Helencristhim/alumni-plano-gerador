#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 15 (gerados pelo
build_from_model.py) nos hubs monoliticos (inline) da Anna Flavia.

Nao toca aulas 1-14. So adiciona: card IN CLASS (so prof), stamp15, accordion
Pre-class, bloco de Complementares, entradas de audioMap (+ [order-l15]) e
ajusta var totalLessons=14 -> 15. Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/anna-flavia-miranda-da-silva/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l15] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l15]": "{AUDIO_BASE}pc15_order_spday.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), no formato das cards existentes da Anna (accent-light) ---
CARD15 = (
    '  <a href="/professor/anna-flavia-miranda-da-silva-aula15.html?autostart=1" target="_blank" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '    <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">15</div>\n'
    '    <div><div style="font-weight:600;font-size:.95rem">Review -- SP Integration</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Full day at the SP office -- 27 slides</div></div>\n'
    '  </a>')

STAMP14 = ('<div class="stamp" id="stamp14" data-label="Lunch" style="background-image:url(\''
           'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>')
STAMP15 = ('\n        <div class="stamp" id="stamp15" data-label="Review" style="background-image:url(\''
           'https://images.unsplash.com/photo-1552664730-d307ca884978?w=200&q=80\')"></div>')

CARD14_TAIL = (
    '    <div><div style="font-weight:600;font-size:.95rem">Business Lunch</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Food vocabulary &amp; ordering -- 27 slides</div></div>\n'
    '  </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp15
    assert s.count(STAMP14) == 1, f'{path}: ancora stamp14 nao unica'
    s = s.replace(STAMP14, STAMP14 + STAMP15, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=14;' in s, f'{path}: totalLessons=14 nao encontrado'
    s = s.replace('var totalLessons=14;', 'var totalLessons=15;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD14_TAIL) == 1, f'{path}: ancora card 14 nao unica'
        s = s.replace(CARD14_TAIL, CARD14_TAIL + '\n' + CARD15, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'anna-flavia-miranda-da-silva.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'anna-flavia-miranda-da-silva.html'), False)
print('hubs atualizados (aditivo).')
