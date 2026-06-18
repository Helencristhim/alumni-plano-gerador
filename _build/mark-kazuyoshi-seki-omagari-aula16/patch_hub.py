#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch aditivo do hub (prof + aluno) da Aula 16 do Mark. NAO toca aulas 1-15."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()

# audioMap entries (entre <script> e </script> da secao 4) + [order-l16] (extra_audio)
m = re.search(r'<!-- 4\. ENTRADAS.*?<script>\n(.*?)</script>', snip, re.S)
entries = m.group(1).rstrip('\n')
entries += '\n  "[order-l16]": "/audio/mark-kazuyoshi-seki-omagari/pc16_order_reported.mp3",'

# stamp16 (builder atual não emite snippet de stamp; montamos aqui a partir do config)
stamp = '''<div class="stamp" id="stamp16" data-label="Said and Done" style="background-image:url('https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?w=200&q=80')"></div>'''

STAMP15 = '''<div class="stamp" id="stamp15" data-label="The People" style="background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80')"></div>'''

ACCORD_ANCHOR = '</div><!-- /tab-exercises -->'
COMP_ANCHOR = '</div>\n</div>\n\n</div><!-- /container -->'

CARD = ('    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" '
        'onclick="window.location.href=\'/professor/mark-kazuyoshi-seki-omagari-aula16.html?autostart=1\'" '
        'onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">16</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Said and Done</div><div style="font-size:.8rem;color:var(--text-dim)">Phase 2 &mdash; reported questions, for retelling what people asked &mdash; 28 slides</div></div>\n'
        '    </div>')
CARD_ANCHOR = ('<div><div style="font-weight:600;font-size:.95rem">The People Who Make It Work</div><div style="font-size:.8rem;color:var(--text-dim)">Phase 2 &mdash; relative clauses (defining and non-defining) to describe people and things &mdash; 28 slides</div></div>\n    </div>')


def patch(path, is_prof):
    c = open(path, encoding='utf-8').read()
    orig = c
    # 1. audioMap
    assert c.count('var audioMap = {') == 1
    c = c.replace('var audioMap = {\n', 'var audioMap = {\n' + entries + '\n', 1)
    # 2. stamp16
    assert c.count(STAMP15) == 1, f'{path}: stamp15 anchor'
    c = c.replace(STAMP15, STAMP15 + '\n' + stamp, 1)
    # 3. accordion pre-class
    assert c.count(ACCORD_ANCHOR) == 1, f'{path}: accordion anchor'
    c = c.replace(ACCORD_ANCHOR, '\n' + accordion + '\n' + ACCORD_ANCHOR, 1)
    # 4. complementary
    assert c.count(COMP_ANCHOR) == 1, f'{path}: complementary anchor'
    c = c.replace(COMP_ANCHOR, '</div>\n\n' + complementary + '\n</div>\n\n</div><!-- /container -->', 1)
    # 5. totalLessons
    c = re.sub(r'var totalLessons\s*=\s*15;', 'var totalLessons=16;', c, count=1)
    # 6. IN CLASS card (prof only)
    if is_prof:
        assert c.count(CARD_ANCHOR) == 1, f'{path}: card anchor'
        c = c.replace(CARD_ANCHOR, CARD_ANCHOR + '\n' + CARD, 1)
    assert c != orig
    open(path, 'w', encoding='utf-8').write(c)
    print(f'patched {os.path.relpath(path, ROOT)}  (+{len(c)-len(orig)} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'mark-kazuyoshi-seki-omagari.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'mark-kazuyoshi-seki-omagari.html'), False)
print('OK')
