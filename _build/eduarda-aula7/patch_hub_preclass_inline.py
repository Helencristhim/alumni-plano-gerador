#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-class da Aula 6 INLINE no hub (accordion ex-lesson-6, IGUAL as aulas 1-5),
no lugar do link-card. Convencao atual (cf. fix milton-preclass-accordion / elaine inline).
IN CLASS continua como link p/ o standalone (?autostart=1). Adiciona as 23 chaves de
audio do pre-class no audioMap de cada hub (prof + aluno). Idempotente."""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')
ALUNO= os.path.join(ROOT, 'public', 'aluno', 'eduarda-gabriel.html')

# accordion = preclass.html, mas COLAPSADO (sem 'open') como as aulas 1-5
accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
accordion = accordion.replace('<div class="lesson-card open" id="ex-lesson-6">',
                              '<div class="lesson-card" id="ex-lesson-6">', 1)
assert 'class="lesson-card" id="ex-lesson-6"' in accordion
NEW_BLOCK = '<!-- AULA 6 -- Pre-class inline (accordion, igual aulas 1-5) -->\n' + accordion

ph = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))
pre = [p for p in ph if not p['file'].startswith('dlg') and not p['file'].startswith('listening_')]
assert len(pre) == 23, len(pre)
AUDIO_ENTRIES = ''.join(
    '  %s: %s,\n' % (json.dumps(p['key'], ensure_ascii=False),
                     json.dumps('/audio/eduarda-gabriel/' + p['file'], ensure_ascii=False))
    for p in pre)

LINK_TMPL = (
'<!-- AULA 6 -- arquivo separado (REGRA 34) -->\n'
'<a href="/{view}/eduarda-gabriel-aula6.html"{tgt} style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-bottom:1.5rem" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'  <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
'  <div><div style="font-weight:600;font-size:.95rem">Ice-Breaking in International Settings</div><div style="font-size:.8rem;color:var(--text-dim)">Social English &amp; question forms &mdash; Pre-class + IN CLASS</div></div>\n'
'</a>')

def patch(path, view, tgt):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-6"' in s:
        print('  SKIP (ja inline):', path); return
    old = LINK_TMPL.format(view=view, tgt=tgt)
    assert s.count(old) == 1, 'link-card anchor x%d in %s' % (s.count(old), path)
    s = s.replace(old, NEW_BLOCK)
    assert s.count('var audioMap = {\n') == 1, 'audioMap anchor'
    s = s.replace('var audioMap = {\n', 'var audioMap = {\n' + AUDIO_ENTRIES, 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('  patched:', path)

print('PROF:');  patch(PROF, 'professor', '')
print('ALUNO:'); patch(ALUNO, 'aluno', ' target="_blank"')
