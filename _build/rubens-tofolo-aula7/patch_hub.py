#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""patch_hub.py — integra a aula 7 nos hubs existentes (prof + aluno) de forma ADITIVA.
Insere: stamp7, accordion Pre-class (ex-lesson-7), bloco Complementares (l7-),
entradas de audioMap (pc7_ + [order-l7]) e (no prof) o card do menu IN CLASS.
Bump de totalLessons 6 -> 7. Idempotente (pula se ex-lesson-7 ja existe)."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
N = 7
SLUG = 'rubens-tofolo'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# audioMap: todas as entradas pc7_ do snippet + a linha do [order-l7]
pc_lines = re.findall(r'^\s*("[^"]+": "/audio/rubens-tofolo/pc7_[^"]+"),\s*$', snip, flags=re.M)
order_line = '"[order-l7]": "/audio/rubens-tofolo/a7_order_restaurant.mp3"'
amap_block = '\n'.join('  ' + l + ',' for l in pc_lines) + '\n  ' + order_line + ','

STAMP7 = ('        <div class="stamp" id="stamp7" data-label="At the Restaurant" '
          'style="background-image:url(\'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>')

MENU_CARD = (
    '    <a href="/professor/rubens-tofolo-aula7.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">07</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">At the Restaurant</div><div style="font-size:.8rem;color:var(--text-dim)">Ordering food politely -- would like, could I have -- 28 slides</div></div>\n'
    '    </a>\n  </div>\n</div>')

STAMP6_LINE = ('        <div class="stamp" id="stamp6" data-label="Making Plans" '
               'style="background-image:url(\'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=200&q=80\')"></div>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-7"' in s:
        print(f'  = {os.path.relpath(path, ROOT)}: ja integrado, pulando')
        return
    n = 0
    # 1. stamp7 apos stamp6
    assert STAMP6_LINE in s, f'{path}: stamp6 nao encontrado'
    s = s.replace(STAMP6_LINE, STAMP6_LINE + '\n' + STAMP7, 1); n += 1
    # 2. accordion Pre-class antes do fim da tab-exercises
    assert '</div><!-- /tab-exercises -->' in s
    s = s.replace('</div><!-- /tab-exercises -->', preclass + '\n</div><!-- /tab-exercises -->', 1); n += 1
    # 3. complementares antes do fim da tab-complementary
    assert '</div><!-- /tab-complementary -->' in s
    s = s.replace('</div><!-- /tab-complementary -->', complementary + '\n</div><!-- /tab-complementary -->', 1); n += 1
    # 4. audioMap
    assert 'var audioMap = {' in s
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1
    # 5. totalLessons 6 -> 7
    s2 = re.sub(r'var totalLessons=6;', 'var totalLessons=7;', s)
    assert s2 != s, f'{path}: var totalLessons=6 nao encontrado'
    s = s2; n += 1
    # 6. menu card IN CLASS (so prof)
    if is_prof:
        anchor = ('      <div><div style="font-weight:600;font-size:.95rem">Making Plans</div>'
                  '<div style="font-size:.8rem;color:var(--text-dim)">Going to vs will -- planning a congress trip -- 28 slides</div></div>\n'
                  '    </a>\n  </div>\n</div>')
        assert anchor in s, f'{path}: ancora do menu (card 6) nao encontrada'
        repl = anchor.replace('    </a>\n  </div>\n</div>', '    </a>\n' + MENU_CARD)
        s = s.replace(anchor, repl, 1); n += 1
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  + {os.path.relpath(path, ROOT)}: {n} insercoes')


patch(os.path.join(ROOT, 'public', 'professor', f'{SLUG}.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', f'{SLUG}.html'), False)
print('hubs integrados.')
