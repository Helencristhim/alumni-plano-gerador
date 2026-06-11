#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Aula 5 nos hubs da Gleice (prof + aluno). ADD ONLY — nunca toca aulas 1-4.
Adiciona: stamp5, accordion Pre-class INLINE (ex-lesson-5), card no menu IN CLASS
(prof) -> standalone#slides, merge das entradas aula5_ no audioMap e totalLessons 4->5."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'gleice-leonardo-rocha-de-souza'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

pre = read(os.path.join(HERE, 'preclass.html'))
LESSON_CARD = pre[pre.index('<div class="lesson-card" id="ex-lesson-5">'):].rstrip() + '\n'

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Review" style="background-image:url(\'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=200&q=80\')"></div>'

CARD4_END = '<div style="font-size:.8rem;color:var(--text-dim)">Asking &amp; Answering Wh-Questions -- 28 slides</div></div>\n  </div>\n'

MENU_CARD = '''  <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="location.href='/professor/gleice-leonardo-rocha-de-souza-aula5.html#slides'" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
    <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
    <div><div style="font-weight:600;font-size:.95rem">Block 1 Review &mdash; Confidence Check</div><div style="font-size:.8rem;color:var(--text-dim)">Lessons 1-4 + the full simulation -- 28 slides</div></div>
  </div>
'''

aula5_prof = read(os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html'))
m = re.search(r'var audioMap = \{(.*?)\n\}', aula5_prof, re.S)
assert m, 'audioMap da aula 5 nao encontrado'
A5_ENTRIES = m.group(1).strip().rstrip(',') + ','

def patch(path, is_aluno):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    m4 = re.search(r'<div class="stamp[^"]*" id="stamp4"[^>]*></div>', h)
    assert m4, 'stamp4 nao encontrado em %s' % path
    h = must(h, m4.group(0), m4.group(0) + STAMP5)
    h = must(h, '</div><!-- /tab-exercises -->', LESSON_CARD + '</div><!-- /tab-exercises -->')
    h = must(h, 'var audioMap = {', 'var audioMap = {\n  ' + A5_ENTRIES)
    h = must(h, 'totalLessons = 4', 'totalLessons = 5')
    if not is_aluno:
        h = must(h, CARD4_END, CARD4_END + MENU_CARD)
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('aluno' if is_aluno else 'prof', after[0]-before[0], after[1]-before[1]))

patch(PROF, False)
patch(ALUN, True)
print('hub wired OK')
