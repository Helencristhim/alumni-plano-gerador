#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idempotent ADDITIVE inserter of aula 20 hub snippets into Sandra's hubs.
Inserts: (1) IN CLASS menu card [prof only], (2) stamp20, (3) ex-lesson-20 accordion,
(4) complementary aula 20 block, (5) audioMap entries; bumps totalLessons 19->20.
NEVER deletes anything. Re-running is a no-op (skips if marker already present)."""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

def block(start_marker, end_marker):
    s = SNIP.index(start_marker) + len(start_marker)
    e = SNIP.index(end_marker)
    return SNIP[s:e].strip('\n')

CARD = block('(inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
STAMP = block('(inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACC = block('(inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
COMP = block('(inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
# audioMap entries: between <script> and </script> in block 4
am = SNIP.index('<!-- 4. ENTRADAS')
am_s = SNIP.index('<script>', am) + len('<script>')
am_e = SNIP.index('</script>', am_s)
AUDIO = SNIP[am_s:am_e].strip('\n')

def process(path, is_prof):
    html = open(path, encoding='utf-8').read()
    orig = html
    changes = []

    # idempotency guard
    if 'id="ex-lesson-20"' in html and 'id="stamp20"' in html:
        print(f"  [{os.path.basename(path)}] already has aula 20 -> skip")
        return

    # 1. IN CLASS menu card (prof only) -- insert after aula19 <a>...</a>
    if is_prof:
        anchor = '/professor/sandra-hayasaki-aula19.html?autostart=1'
        i = html.index(anchor)
        close = html.index('</a>', i) + len('</a>')
        html = html[:close] + '\n' + CARD + html[close:]
        changes.append('inclass-card')

    # 2. STAMP -- insert right after stamp19 div (within stamps-row)
    sm = 'id="stamp19"'
    si = html.index(sm)
    end_stamp = html.index('></div>', si) + len('></div>')
    html = html[:end_stamp] + STAMP + html[end_stamp:]
    changes.append('stamp')

    # 3. ACCORDION -- insert right before '</div><!-- /tab-exercises -->'
    marker = '</div><!-- /tab-exercises -->'
    if marker in html:
        mi = html.index(marker)
        html = html[:mi] + ACC + '\n\n' + html[mi:]
        changes.append('accordion')
    else:
        cm = html.index('id="tab-complementary"')
        prev = html.rindex('<div class="tab-content"', 0, cm)
        html = html[:prev] + ACC + '\n\n' + html[prev:]
        changes.append('accordion(fallback)')

    # 4. COMPLEMENTARY -- insert the aula-20 media block right before the close marker
    comp_close = '</div><!-- /tab-complementary -->'
    cci = html.index(comp_close)
    html = html[:cci] + COMP + '\n\n' + html[cci:]
    changes.append('complementary')

    # 5. audioMap entries -- insert before the closing '};' of audioMap
    amap = html.index('var audioMap = {')
    amap_close = html.index('\n};', amap)
    html = html[:amap_close] + '\n' + AUDIO + html[amap_close:]
    changes.append('audioMap')

    # 6. totalLessons 19 -> 20
    html2 = html.replace('var totalLessons=19;', 'var totalLessons=20;')
    if html2 != html:
        changes.append('totalLessons')
        html = html2

    assert html != orig, "no change made!"
    open(path, 'w', encoding='utf-8').write(html)
    print(f"  [{os.path.basename(path)}] inserted: {', '.join(changes)}")

process(os.path.join(ROOT, 'public', 'professor', 'sandra-hayasaki.html'), True)
process(os.path.join(ROOT, 'public', 'aluno', 'sandra-hayasaki.html'), False)
print("done")
