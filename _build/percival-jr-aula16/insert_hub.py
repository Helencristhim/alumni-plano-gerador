#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 16 (gerados pelo
build_from_model.py) nos hubs do Percival JR.

NAO toca aulas 1-15. So adiciona: card IN CLASS (so prof), stamp16, accordion
Pre-class, bloco de Complementares, entradas de audioMap (+ [order-l16]) e
ajusta var totalLessons 15->16. Fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/percival-jr/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l16] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l16]": "{AUDIO_BASE}pc16_order_l16.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (parte 1, so prof) com margin-top p/ uniformidade ---
mc = re.search(r'1\. CARD.*?\n(\s*<a href.*?</a>)', snip, re.S)
card = mc.group(1)
card = card.replace('color:inherit"', 'color:inherit;margin-top:1rem"', 1)

# --- stamp16 (parte 2) ---
ms = re.search(r'2\. STAMP.*?\n(<div class="stamp" id="stamp16".*?</div>)', snip, re.S)
stamp16 = ms.group(1)

STAMP15 = ('<div class="stamp" id="stamp15" data-label="Video Call" '
           "style=\"background-image:url('https://images.unsplash.com/"
           "photo-1587825140708-dfaf72ae4b04?w=200&q=80')\"></div>")

AULA15_HREF = 'percival-jr-aula15.html?autostart=1'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp16 (apos stamp15 Video Call)
    assert s.count(STAMP15) == 1, f'{path}: ancora stamp15 nao unica'
    s = s.replace(STAMP15, STAMP15 + '\n        ' + stamp16, 1); n += 1

    # 3. accordion Pre-class (antes do fim da tab-exercises)
    assert s.count('/tab-exercises -->') == 1, f'{path}: marker tab-exercises nao unico'
    s = re.sub(r'</div>\s*<!-- /tab-exercises -->',
               lambda mm: '\n' + preclass + '\n\n' + mm.group(0), s, count=1); n += 1

    # 4. complementares (antes do fim da tab-complementary)
    assert s.count('/tab-complementary -->') == 1, f'{path}: marker tab-complementary nao unico'
    s = re.sub(r'</div>\s*<!-- /tab-complementary -->',
               lambda mm: '\n' + complementary + '\n\n' + mm.group(0), s, count=1); n += 1

    # 5. totalLessons 15 -> 16
    assert len(re.findall(r'totalLessons=15(?![0-9])', s)) == 1, f'{path}: totalLessons=15 nao unico'
    s = re.sub(r'totalLessons=15(?![0-9])', 'totalLessons=16', s, count=1); n += 1

    # 6. card IN CLASS (so prof): inserir apos o </a> que fecha o card da aula 15
    if is_prof:
        i = s.index(AULA15_HREF)
        j = s.index('</a>', i) + len('</a>')
        s = s[:j] + '\n' + card + s[j:]; n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'percival-jr.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'percival-jr.html'), False)
print('hubs atualizados (aditivo).')
