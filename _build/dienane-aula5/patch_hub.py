#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Aula 5 nos hubs da Dienane (prof + aluno). ADD ONLY.
- ambos: stamp5, accordion Pre-class inline (ex-lesson-5), audioMap merge
- prof: card IN CLASS <a aula5.html?autostart=1> depois do card da aula 4"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'dienane-brandao-de-mesquita'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

pre = read(os.path.join(HERE, 'preclass.html'))
CARD5 = pre[pre.index('<div class="lesson-card" id="ex-lesson-5">'):].rstrip() + '\n'

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Time" style="background-image:url(\'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=200&q=80\')"></div>'

MENU_CARD5 = '''    <a href="/professor/dienane-brandao-de-mesquita-aula5.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
      <div><div style="font-weight:600;font-size:.95rem">Numbers and Time</div><div style="font-size:.8rem;color:var(--text-dim)">Telling time &amp; scheduling a meeting &mdash; 28 slides</div></div>
    </a>
'''

aula5 = read(os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html'))
m = re.search(r'var audioMap = \{(.*?)\n\}', aula5, re.S)
assert m, 'audioMap da aula 5 nao encontrado'
A5_ENTRIES = m.group(1).strip().rstrip(',') + ','

def patch(path, is_prof):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    m4 = re.search(r'<div class="stamp[^"]*" id="stamp4"[^>]*></div>', h)
    assert m4, 'stamp4 nao encontrado em %s' % path
    h = must(h, m4.group(0), m4.group(0) + STAMP5)
    h = must(h, '</div><!-- /tab-exercises -->', CARD5 + '</div><!-- /tab-exercises -->')
    h = must(h, 'var audioMap = {', 'var audioMap = {\n  ' + A5_ENTRIES)
    if is_prof:
        i = h.index('aula4.html?autostart=1')
        j = h.index('</a>', i) + len('</a>\n')
        h = h[:j] + MENU_CARD5 + h[j:]
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('prof' if is_prof else 'aluno', after[0]-before[0], after[1]-before[1]))

patch(PROF, True)
patch(ALUN, False)
print('hub wired OK')
