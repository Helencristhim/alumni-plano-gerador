#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linka a Aula 7 no hub eduarda-gabriel.html (prof + aluno) seguindo a convencao atual:
- Pre-class = accordion INLINE (ex-lesson-7, colapsado, igual 1-6)  [prof + aluno]
- IN CLASS  = card -> standalone (?autostart=1)                      [prof]
- stamp7, totalLessons 6->7, + 19 chaves de audio do pre-class no audioMap [prof + aluno]
REGRA 38 ja existe no hub (exitSlideMode/#inclass). Idempotente."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')
ALUNO= os.path.join(ROOT, 'public', 'aluno', 'eduarda-gabriel.html')

accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
accordion = accordion.replace('<div class="lesson-card open" id="ex-lesson-7">',
                              '<div class="lesson-card" id="ex-lesson-7">', 1)
assert 'class="lesson-card" id="ex-lesson-7"' in accordion
PRECLASS_BLOCK = '<!-- AULA 7 -- Pre-class inline (accordion, igual aulas 1-6) -->\n' + accordion + '\n\n'

ph = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))
pre = [p for p in ph if not p['file'].startswith('listening_') and not re.match(r'd\d', p['file'])]
assert len(pre) == 19, len(pre)
AUDIO_ENTRIES = ''.join(
    '  %s: %s,\n' % (json.dumps(p['key'], ensure_ascii=False),
                     json.dumps('/audio/eduarda-gabriel/' + p['file'], ensure_ascii=False))
    for p in pre)

STAMP6 = '<div class="stamp" id="stamp6" data-label="Ice-Break" style="background-image:url(\'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=200&q=80\')"></div>'
STAMP7 = STAMP6 + '\n<div class="stamp" id="stamp7" data-label="Turn-Take" style="background-image:url(\'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80\')"></div>'

IC6_END = '      <div><div style="font-weight:600;font-size:.95rem">Ice-Breaking in International Settings</div><div style="font-size:.8rem;color:var(--text-dim)">Social English &amp; question forms -- 27 slides</div></div>\n    </a>'
IC7_CARD = IC6_END + '\n    <a href="/professor/eduarda-gabriel-aula7.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">07</div>\n      <div><div style="font-weight:600;font-size:.95rem">Turn-Taking: Interrupting &amp; Yielding Politely</div><div style="font-size:.8rem;color:var(--text-dim)">Discourse markers &amp; interruption phrases -- 27 slides</div></div>\n    </a>'

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-7"' in s:
        print('  SKIP (ja linkado):', path); return
    subs = [
        (STAMP6, STAMP7, 'stamp7'),
        ('  var totalLessons = 6;', '  var totalLessons = 7;', 'totalLessons'),
        ('</div><!-- /tab-exercises -->', PRECLASS_BLOCK + '</div><!-- /tab-exercises -->', 'preclass accordion'),
        ('var audioMap = {\n', 'var audioMap = {\n' + AUDIO_ENTRIES, 'audioMap'),
    ]
    if is_prof:
        subs.insert(2, (IC6_END, IC7_CARD, 'inclass card'))
    for old, new, label in subs:
        assert s.count(old) == 1, 'anchor x%d for %s in %s' % (s.count(old), label, path)
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s)
    print('  patched:', path)

print('PROF:');  patch(PROF, True)
print('ALUNO:'); patch(ALUNO, False)
