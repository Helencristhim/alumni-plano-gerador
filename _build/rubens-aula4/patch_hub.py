#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire standalone Aula 4 into the Rubens hub (prof + aluno). ADD ONLY — never touch aulas 1-3.
Adds: stamp4, Pre-class link card, IN CLASS menu link card (prof), totalLessons 3->4, #inclass handler (prof)."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROF = os.path.join(ROOT, 'public', 'professor', 'rubens-tofolo.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', 'rubens-tofolo.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.60s' % (h.count(old), old)
    return h.replace(old, new)

STAMP3 = '<div class="stamp" id="stamp3" data-label="The Past" style="background-image:url(\'https://images.unsplash.com/photo-1449034446853-66c86144b0ad?w=200&q=80\')"></div>'
STAMP4 = '\n        <div class="stamp" id="stamp4" data-label="Life" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>'

PRE_CARD = '''<a href="%s" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-bottom:1.5rem" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
  <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">04</div>
  <div><div style="font-weight:600;font-size:.95rem">Life Experiences</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect: ever, never, already, yet -- Pre-class</div></div>
</a>
'''

MENU_CARD = '''    <a href="/professor/rubens-tofolo-aula4.html#slides" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">04</div>
      <div><div style="font-weight:600;font-size:.95rem">Life Experiences</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect: ever, never, already, yet -- 28 slides</div></div>
    </a>
'''

# 3rd IN CLASS card ends here (unique to aula 3):
MENU3_END = '<div><div style="font-weight:600;font-size:.95rem">Talking About the Past</div><div style="font-size:.8rem;color:var(--text-dim)">Past Simple regular and irregular verbs -- 40 slides</div></div>\n    </div>\n'

INCLASS_HANDLER = ("  if (btn) setAudioSpeed(saved, btn);\n"
                   "  if (window.location.hash === '#inclass') { var ib = document.querySelector('.tab-btn[onclick*=\"inclass\"]'); if (ib) ib.click(); }\n")

def patch(path, is_aluno):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    h = must(h, STAMP3, STAMP3 + STAMP4)
    href = '/aluno/rubens-tofolo-aula4.html' if is_aluno else '/professor/rubens-tofolo-aula4.html'
    h = must(h, '</div><!-- /tab-exercises -->', PRE_CARD % href + '</div><!-- /tab-exercises -->')
    h = must(h, '  var totalLessons = 3;', '  var totalLessons = 4;')
    if not is_aluno:
        h = must(h, MENU3_END, MENU3_END + MENU_CARD)
        h = must(h, '  if (btn) setAudioSpeed(saved, btn);\n', INCLASS_HANDLER)
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance introduced: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-12s div delta open=%d close=%d (balanced)' % ('aluno' if is_aluno else 'prof', after[0]-before[0], after[1]-before[1]))

patch(PROF, False)
patch(ALUN, True)
print('hub wired OK')
