#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Aula 5 nos hubs da Karina (prof + aluno). ADD ONLY — nunca toca aulas 1-4.
Adiciona: stamp5, accordion Pre-class INLINE (ex-lesson-5, estilo Eduarda — igual a aula 4),
card no menu IN CLASS (prof) -> standalone#slides, e merge das entradas a5_ no audioMap."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'karina-macedo.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', 'karina-macedo.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

# accordion inline = só o lesson-card do preclass autoral (welcome já existe no hub)
pre = read(os.path.join(HERE, 'preclass.html'))
LESSON_CARD = pre[pre.index('<div class="lesson-card" id="ex-lesson-5">'):].rstrip() + '\n'

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Pitch" style="background-image:url(\'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80\')"></div>'

MENU4_END = '<div><div style="font-weight:600;font-size:.95rem">At the Aviation Fair -- Meeting People</div><div style="font-size:.8rem;color:var(--text-dim)">Greetings &amp; networking -- 28 slides</div></div>\n    </div>\n'

MENU_CARD = '''    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="window.location.href='/professor/karina-macedo-aula5.html#slides'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
      <div><div style="font-weight:600;font-size:.95rem">Review + Confidence Check</div><div style="font-size:.8rem;color:var(--text-dim)">Lessons 1-4 + the 2-minute pitch -- 28 slides</div></div>
    </div>
'''

# audioMap do hub: insere as entradas a5 logo após a abertura do objeto
phrases_map = {}
aula5_prof = read(os.path.join(ROOT, 'public', 'professor', 'karina-macedo-aula5.html'))
m = re.search(r'var audioMap = \{(.*?)\n\}', aula5_prof, re.S)
assert m, 'audioMap da aula 5 nao encontrado'
A5_ENTRIES = m.group(1).strip().rstrip(',') + ','

def patch(path, is_aluno):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    # stamp5 depois do stamp4
    m4 = re.search(r'<div class="stamp[^"]*" id="stamp4"[^>]*></div>', h)
    assert m4, 'stamp4 nao encontrado em %s' % path
    h = must(h, m4.group(0), m4.group(0) + STAMP5)
    # accordion ex-lesson-5 antes do fim da aba pre-class
    h = must(h, '</div><!-- /tab-exercises -->', LESSON_CARD + '</div><!-- /tab-exercises -->')
    # audioMap merge (entradas do hub depois ganham em duplicatas — ok, mesmo áudio)
    h = must(h, 'var audioMap = {', 'var audioMap = {\n  ' + A5_ENTRIES)
    if not is_aluno:
        h = must(h, MENU4_END, MENU4_END + MENU_CARD)
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('aluno' if is_aluno else 'prof', after[0]-before[0], after[1]-before[1]))

patch(PROF, False)
patch(ALUN, True)
print('hub wired OK')
