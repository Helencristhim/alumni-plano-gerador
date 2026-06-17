#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 13 (gerados pelo
build_from_model.py) nos hubs monoliticos (inline) da Anna Flavia.

Nao toca aulas 1-12. So adiciona: card IN CLASS (so prof), stamp13, accordion
Pre-class, bloco de Complementares, entradas de audioMap (+ [order-l13]) e
ajusta var totalLessons=12 -> 13. Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/anna-flavia-miranda-da-silva/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l13] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l13]": "{AUDIO_BASE}pc13_order_report.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), no formato das cards existentes da Anna (accent-light) ---
CARD13 = (
    '  <a href="/professor/anna-flavia-miranda-da-silva-aula13.html?autostart=1" target="_blank" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '    <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">13</div>\n'
    '    <div><div style="font-weight:600;font-size:.95rem">Presenting Numbers</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Comparatives &amp; financial words -- 27 slides</div></div>\n'
    '  </a>')

STAMP12 = ('<div class="stamp" id="stamp12" data-label="Meeting" style="background-image:url(\''
           'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80\')"></div>')
STAMP13 = ('\n        <div class="stamp" id="stamp13" data-label="Numbers" style="background-image:url(\''
           'https://images.unsplash.com/photo-1543286386-713bdd548da4?w=200&q=80\')"></div>')

CARD12_TAIL = (
    '    <div><div style="font-weight:600;font-size:.95rem">In a Meeting</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Giving opinions &amp; agreement -- 27 slides</div></div>\n'
    '  </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp13
    assert s.count(STAMP12) == 1, f'{path}: ancora stamp12 nao unica'
    s = s.replace(STAMP12, STAMP12 + STAMP13, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=12;' in s, f'{path}: totalLessons=12 nao encontrado'
    s = s.replace('var totalLessons=12;', 'var totalLessons=13;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD12_TAIL) == 1, f'{path}: ancora card 12 nao unica'
        s = s.replace(CARD12_TAIL, CARD12_TAIL + '\n' + CARD13, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'anna-flavia-miranda-da-silva.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'anna-flavia-miranda-da-silva.html'), False)
print('hubs atualizados (aditivo).')
