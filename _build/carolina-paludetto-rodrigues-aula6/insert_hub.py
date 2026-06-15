#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 6 (gerados pelo
build_from_model.py) nos hubs OLD-mold (monoliticos inline) da Carolina.

Nao toca aulas 1-5. So adiciona: card IN CLASS (so prof), stamp6, accordion
Pre-class, bloco de Complementares, entradas de audioMap (+ [order-l6]) e
ajusta var totalLessons=6. Os fragmentos vem dos arquivos do builder.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/carolina-paludetto-rodrigues/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l6] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l6]": "{AUDIO_BASE}pc6_order_sequence.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (parte 1, so prof) com margin-top p/ uniformidade ---
mc = re.search(r'1\. CARD.*?\n(\s*<a href.*?</a>)', snip, re.S)
card = mc.group(1)
card = card.replace('color:inherit"', 'color:inherit;margin-top:.8rem"', 1)

STAMP5_TRAVEL = ('        <div class="stamp" id="stamp5" data-label="Travel" '
                 'style="background-image:url(\'https://images.unsplash.com/'
                 'photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>')
STAMP6 = ('\n        <div class="stamp" id="stamp6" data-label="Sports" '
          'style="background-image:url(\'https://images.unsplash.com/'
          'photo-1461896836934-bd45ba8bf8bd?w=200&q=80\')"></div>')

CARD04_TAIL = (
    '    <div><div style="font-weight:600;font-size:.95rem">Carolina\'s Favorite Things '
    '— My Hobbies and Passions</div><div style="font-size:.8rem;color:var(--text-dim)">'
    'Like/Love/Enjoy/Prefer + Gerund — 27 slides</div></div>\n  </div>\n</div>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp6
    assert s.count(STAMP5_TRAVEL) == 1, f'{path}: ancora stamp5 Travel nao unica'
    s = s.replace(STAMP5_TRAVEL, STAMP5_TRAVEL + STAMP6, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=5;' in s
    s = s.replace('var totalLessons=5;', 'var totalLessons=6;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD04_TAIL) == 1, f'{path}: ancora card 04 nao unica'
        new_tail = CARD04_TAIL[:-len('\n</div>')] + '\n' + card + '\n</div>'
        s = s.replace(CARD04_TAIL, new_tail, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'carolina-paludetto-rodrigues.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'carolina-paludetto-rodrigues.html'), False)
print('hubs atualizados (aditivo).')
