#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 11 da Pricila nos hubs
monoliticos (inline) prof/aluno. Nao toca aulas 1-10. Adiciona: card IN CLASS (so
prof), stamp11, accordion Pre-class, bloco Complementares, entradas audioMap
(+ [order-l11]) e ajusta var totalLessons=10 -> 11.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/pricila-adamo/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l11] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l11]": "{AUDIO_BASE}pc11_order_smalltalk.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), formato identico aos cards existentes da Pricila (accent) ---
CARD11 = (
    '    <a href="/professor/pricila-adamo-aula11.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">11</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Small Talk</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Question forms &amp; tag questions -- 28 slides</div></div>\n'
    '    </a>')

STAMP10 = ('<div class="stamp" id="stamp10" data-label="Market" style="background-image:url(\''
           'https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=200&q=80\')"></div>')
STAMP11 = ('\n        <div class="stamp" id="stamp11" data-label="Small Talk" style="background-image:url(\''
           'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=200&q=80\')"></div>')

CARD10_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">Shopping Abroad</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Quantifiers, prices, too/enough -- 29 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp11
    assert s.count(STAMP10) == 1, f'{path}: ancora stamp10 nao unica'
    s = s.replace(STAMP10, STAMP10 + STAMP11, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=10;' in s, f'{path}: totalLessons=10 nao encontrado'
    s = s.replace('var totalLessons=10;', 'var totalLessons=11;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD10_TAIL) == 1, f'{path}: ancora card 10 nao unica'
        s = s.replace(CARD10_TAIL, CARD10_TAIL + '\n' + CARD11, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('hubs atualizados (aditivo).')
