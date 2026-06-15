#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 4 (Sandra) nos hubs prof e aluno (aditivo)."""
import os, re, sys

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
amap_lines.append('  "[order-l4]": "/audio/sandra-hayasaki/a4_order_family.mp3",')
amap_block = '\n'.join(amap_lines)

STAMP4 = ('        <div class="stamp" id="stamp4" data-label="Family" '
          "style=\"background-image:url('https://images.unsplash.com/photo-1511895426328-dc8714191300?w=200&q=80')\"></div>")

CARD = '''    <a href="/professor/sandra-hayasaki-aula4.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">04</div>
      <div><div style="font-weight:600;font-size:.95rem">My Family</div><div style="font-size:.8rem;color:var(--text-dim)">Possessives (my, your, his, her) -- 27 slides</div></div>
    </a>'''

ANCHOR_AMAP = '  "One hour is sixty minutes.": "/audio/sandra-hayasaki/aula3_one_hour_is_sixty_minutes.mp3"\n};'
ANCHOR_STAMP3 = '''        <div class="stamp" id="stamp3" data-label="Time" style="background-image:url('https://images.unsplash.com/photo-1495364141860-b0d03eccd065?w=200&q=80')"></div>'''
ANCHOR_LESSON3_CLOSE = '</div><!-- /lesson-card aula 3 -->\n\n</div><!-- /tab-exercises -->'
ANCHOR_COMP_CLOSE = '</div><!-- /tab-complementary -->'

def patch(path, is_prof):
    s = read(path)
    n0 = len(s)
    # 1. audioMap
    assert ANCHOR_AMAP in s, f'{path}: anchor audioMap nao encontrado'
    s = s.replace(ANCHOR_AMAP,
                  '  "One hour is sixty minutes.": "/audio/sandra-hayasaki/aula3_one_hour_is_sixty_minutes.mp3",\n'
                  + amap_block + '\n};', 1)
    # 2. stamp4
    assert ANCHOR_STAMP3 in s, f'{path}: anchor stamp3 nao encontrado'
    s = s.replace(ANCHOR_STAMP3, ANCHOR_STAMP3 + '\n' + STAMP4, 1)
    # 3. ex-lesson-4 accordion
    assert ANCHOR_LESSON3_CLOSE in s, f'{path}: anchor lesson3 close nao encontrado'
    s = s.replace(ANCHOR_LESSON3_CLOSE,
                  '</div><!-- /lesson-card aula 3 -->\n\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1)
    # 4. complementary
    assert ANCHOR_COMP_CLOSE in s, f'{path}: anchor complementary close nao encontrado'
    s = s.replace(ANCHOR_COMP_CLOSE, complementary + '\n' + ANCHOR_COMP_CLOSE, 1)
    # 5. totalLessons -> 4
    s = s.replace('var totalLessons=1;', 'var totalLessons=4;', 1)
    # 6. IN CLASS card (so prof tem a tab)
    if is_prof:
        anchor_card = ('      <div><div style="font-weight:600;font-size:.95rem">Numbers and Time</div>'
                       '<div style="font-size:.8rem;color:var(--text-dim)">Telling Time -- 30 slides</div></div>\n'
                       '    </a>\n  </div>')
        assert anchor_card in s, f'{path}: anchor card IN CLASS nao encontrado'
        s = s.replace(anchor_card, anchor_card.rsplit('\n  </div>',1)[0] + '\n' + CARD + '\n  </div>', 1)
    write(path, s)
    print(f'  patched {os.path.relpath(path, ROOT)} (+{len(s)-n0} chars)')

patch(PROF, True)
patch(ALUNO, False)
print('done')
