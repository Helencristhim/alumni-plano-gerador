#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 9 (Sandra) nos hubs prof e aluno (aditivo)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public/professor/sandra-hayasaki.html')
ALUNO = os.path.join(ROOT, 'public/aluno/sandra-hayasaki.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

preclass = read(os.path.join(HERE, 'preclass.html')).strip()
complementary = read(os.path.join(HERE, 'complementary.html')).strip()
snip = read(os.path.join(HERE, 'hub_snippets.html'))

# audioMap entries (linhas .mp3 entre marcadores 4 e 5) + order
amap_lines = []
grab = False
for line in snip.splitlines():
    if '4. ENTRADAS de audioMap' in line: grab = True; continue
    if '5. Ajustar' in line: grab = False
    if grab and '.mp3' in line: amap_lines.append(line.rstrip())
amap_lines.append('  "[order-l9]": "/audio/sandra-hayasaki/a9_order_shopping.mp3",')
amap_block = '\n'.join(amap_lines)

STAMP9 = ('        <div class="stamp" id="stamp9" data-label="Shopping" '
          "style=\"background-image:url('https://images.unsplash.com/photo-1542838132-92c53300491e?w=200&q=80')\"></div>")

CARD = '''    <a href="/professor/sandra-hayasaki-aula9.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>
      <div><div style="font-weight:600;font-size:.95rem">At the Supermarket</div><div style="font-size:.8rem;color:var(--text-dim)">How much / how many + quantities -- 27 slides</div></div>
    </a>'''

ANCHOR_AMAP = '  "[order-l8]": "/audio/sandra-hayasaki/a8_order_day.mp3",\n};'
ANCHOR_STAMP8 = ('        <div class="stamp" id="stamp8" data-label="Review" '
                 "style=\"background-image:url('https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=200&q=80')\"></div>")
ANCHOR_EXERCISES_CLOSE = '</div><!-- /tab-exercises -->'
ANCHOR_COMP_CLOSE = '</div><!-- /tab-complementary -->'

def patch(path, is_prof):
    s = read(path)
    n0 = len(s)
    # 1. audioMap
    assert s.count(ANCHOR_AMAP) == 1, f'{path}: anchor audioMap'
    s = s.replace(ANCHOR_AMAP,
                  '  "[order-l8]": "/audio/sandra-hayasaki/a8_order_day.mp3",\n' + amap_block + '\n};', 1)
    # 2. stamp9
    assert ANCHOR_STAMP8 in s, f'{path}: anchor stamp8'
    s = s.replace(ANCHOR_STAMP8, ANCHOR_STAMP8 + '\n' + STAMP9, 1)
    # 3. ex-lesson-9 accordion (antes do fechamento da tab-exercises)
    assert s.count(ANCHOR_EXERCISES_CLOSE) == 1, f'{path}: anchor tab-exercises'
    s = s.replace(ANCHOR_EXERCISES_CLOSE, preclass + '\n\n' + ANCHOR_EXERCISES_CLOSE, 1)
    # 4. complementary
    assert ANCHOR_COMP_CLOSE in s, f'{path}: anchor complementary'
    s = s.replace(ANCHOR_COMP_CLOSE, complementary + '\n' + ANCHOR_COMP_CLOSE, 1)
    # 5. totalLessons -> 9
    assert 'var totalLessons=8;' in s, f'{path}: totalLessons'
    s = s.replace('var totalLessons=8;', 'var totalLessons=9;', 1)
    # 6. IN CLASS card (so prof tem a tab)
    if is_prof:
        anchor_card = ('      <div><div style="font-weight:600;font-size:.95rem">Review Block 1</div>'
                       '<div style="font-size:.8rem;color:var(--text-dim)">All structures + frequency words -- 27 slides</div></div>\n'
                       '    </a>\n  </div>')
        assert anchor_card in s, f'{path}: anchor card IN CLASS'
        s = s.replace(anchor_card, anchor_card.rsplit('\n  </div>', 1)[0] + '\n' + CARD + '\n  </div>', 1)
    write(path, s)
    print(f'  patched {os.path.relpath(path, ROOT)} (+{len(s)-n0} chars)')

patch(PROF, True)
patch(ALUNO, False)
print('done')
