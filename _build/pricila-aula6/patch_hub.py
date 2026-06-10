#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch the pricila-adamo hubs (professor + aluno) for Aula 6:
  - ex-lesson-6 accordion inline (collapsed) in tab-exercises (REGRA 15, requirement #1)
  - audioMap entries for aula 6 (so hub Listen buttons work)
  - stamp6 in stamps-row (REGRA 29)
  - var totalLessons 5 -> 6
  - (prof only) IN CLASS menu card linking to the standalone aula6 (REGRA 34)
  - (prof only) #inclass deep-link handler (REGRA 38)
Idempotent: skips a file that already contains id="ex-lesson-6".
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read()
phrases  = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))

IMG = 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05'

ACCORDION = (
'<div class="lesson-card" id="ex-lesson-6">\n'
'  <div class="lesson-header" onclick="toggleLesson(this)">\n'
'    <div class="lesson-header-img" style="background-image:url(\'' + IMG + '?w=600&q=80\')"></div>\n'
'    <div class="lesson-header-content">\n'
'      <div class="lesson-number">Aula 06 -- Pre-class</div>\n'
'      <h3>At the Airport</h3>\n'
'      <div class="lesson-desc">Checking In and Boarding: polite requests (Could I...? / Would you mind...?)</div>\n'
'      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>\n'
'    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n'
'  <div class="lesson-body">\n' + preclass + '\n  </div>\n'
'</div><!-- /lesson-card Aula 6 -->\n'
)

STAMP6 = '<div class="stamp" id="stamp6" data-label="Airport" style="background-image:url(\'' + IMG + '?w=200&q=80\')"></div>\n'

INCLASS_CARD = (
'    <a href="/professor/pricila-adamo-aula6.html?autostart=1" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
'      <div><div style="font-weight:600;font-size:.95rem">At the Airport</div><div style="font-size:.8rem;color:var(--text-dim)">Checking In &amp; Boarding -- 29 slides</div></div>\n'
'    </a>\n'
)

INCLASS_HASH = (
'<script>\n'
'document.addEventListener("DOMContentLoaded", function () {\n'
'  if (window.location.hash === "#inclass") {\n'
'    var b = document.querySelector(\'.tab-btn[onclick*="inclass"]\');\n'
'    if (b) b.click();\n'
'  }\n'
'});\n'
'</script>\n'
)

def audiomap_entries(existing):
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        if (k + ':') in existing or (k + ' :') in existing:
            continue
        v = json.dumps('/audio/pricila-adamo/' + p['file'], ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return (',\n'.join(lines) + ',\n') if lines else ''

def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-6"' in h:
        print('  skip (already patched):', path); return
    # 1. audioMap entries before the audioMap-closing };
    am_open = h.index('var audioMap = {')
    am_close = h.index('};', am_open)
    am_region = h[am_open:am_close]
    entries = audiomap_entries(am_region)
    if entries:
        # ensure the last pre-existing entry ends with a comma before appending
        last = am_region.rstrip()
        prefix = '' if (last.endswith(',') or last.endswith('{')) else ',\n'
        h = h[:am_close] + prefix + entries + h[am_close:]
    # 2. stamp6 after stamp5
    h = h.replace(
        '<div class="stamp" id="stamp5" data-label="Health" style="background-image:url(\'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=200&q=80\')"></div>\n',
        '<div class="stamp" id="stamp5" data-label="Health" style="background-image:url(\'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=200&q=80\')"></div>\n' + STAMP6,
        1)
    # 3. accordion before tab-exercises close
    marker = '</div><!-- /tab-exercises -->'
    assert marker in h, 'tab-exercises marker missing in ' + path
    h = h.replace(marker, ACCORDION + '\n' + marker, 1)
    # 4. totalLessons 5 -> 6
    h = h.replace('var totalLessons = 5;', 'var totalLessons = 6;')
    if is_prof:
        # 5. IN CLASS menu card after the aula5 anchor
        aula5_href = '<a href="/professor/pricila-adamo-aula5.html?autostart=1"'
        idx = h.index(aula5_href)
        close = h.index('</a>', idx) + len('</a>') + 1  # include trailing newline
        h = h[:close] + INCLASS_CARD + h[close:]
        # 6. #inclass handler before </body>
        h = h.replace('</body>', INCLASS_HASH + '</body>', 1)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched:', path, '(+%d audioMap entries)' % entries.count('/audio/'))

patch(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('hub patch done')
