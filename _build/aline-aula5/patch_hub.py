#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Aulas 4 E 5 nos hubs da Aline (prof + aluno). ADD ONLY.
Conserta os FAILs pré-existentes do validador (aula 4 sem stamp4 e sem
integração no hub do aluno) e integra a aula 5:
- ambos os hubs: stamp4+stamp5, accordions inline ex-lesson-4 (extraído do
  standalone da aula 4) e ex-lesson-5, merge audioMap (a4+a5)
- hub prof: card IN CLASS da aula 5 (?autostart=1) depois do card da aula 4"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'aline-sberci'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)

def lesson_card(src, n):
    """extrai o lesson-card ex-lesson-N completo da aba pre-class de um standalone"""
    start = src.index('<div class="lesson-card" id="ex-lesson-%d">' % n)
    end = src.index('</div><!-- /tab-exercises -->', start)
    card = src[start:end].rstrip()
    assert card.count('<div') == card.count('</div>'), 'card %d desbalanceado' % n
    return card + '\n'

def audio_entries(src):
    m = re.search(r'var audioMap = \{(.*?)\n\}', src, re.S)
    assert m, 'audioMap nao encontrado'
    return m.group(1).strip().rstrip(',') + ','

a4_prof  = read(os.path.join(ROOT, 'public', 'professor', SLUG + '-aula4.html'))
a4_aluno = read(os.path.join(ROOT, 'public', 'aluno', SLUG + '-aula4.html'))
a5_prof  = read(os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html'))
pre5 = read(os.path.join(HERE, 'preclass.html'))
CARD5 = pre5[pre5.index('<div class="lesson-card" id="ex-lesson-5">'):].rstrip() + '\n'

STAMP45 = ('\n        <div class="stamp" id="stamp4" data-label="Plans" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80\')"></div>'
           '\n        <div class="stamp" id="stamp5" data-label="Travel" style="background-image:url(\'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=200&q=80\')"></div>')

MENU_CARD5 = '''    <a href="/professor/aline-sberci-aula5.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>
      <div><div style="font-weight:600;font-size:.95rem">Have You Ever...? &mdash; Travel Stories</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect: ever / never &mdash; slides</div></div>
    </a>
'''

A4_ENTRIES = audio_entries(a4_prof)
A5_ENTRIES = audio_entries(a5_prof)

def patch(path, is_aluno):
    h = read(path); before = (h.count('<div'), h.count('</div>'))
    m3 = re.search(r'<div class="stamp[^"]*" id="stamp3"[^>]*></div>', h)
    assert m3, 'stamp3 nao encontrado em %s' % path
    h = must(h, m3.group(0), m3.group(0) + STAMP45)
    card4 = lesson_card(a4_aluno if is_aluno else a4_prof, 4)
    h = must(h, '</div><!-- /tab-exercises -->', card4 + CARD5 + '</div><!-- /tab-exercises -->')
    h = must(h, 'var audioMap = {', 'var audioMap = {\n  ' + A4_ENTRIES + '\n  ' + A5_ENTRIES)
    if not is_aluno:
        i = h.index('aline-sberci-aula4.html?autostart=1')
        j = h.index('</a>', i) + len('</a>\n')
        h = h[:j] + MENU_CARD5 + h[j:]
    after = (h.count('<div'), h.count('</div>'))
    assert (after[0]-before[0]) == (after[1]-before[1]), 'div imbalance: %s -> %s' % (before, after)
    with open(path, 'w', encoding='utf-8') as f: f.write(h)
    print('patched %-6s div delta open=%d close=%d (balanced)' % ('aluno' if is_aluno else 'prof', after[0]-before[0], after[1]-before[1]))

patch(PROF, False)
patch(ALUN, True)
print('hub wired OK (aulas 4 e 5)')
