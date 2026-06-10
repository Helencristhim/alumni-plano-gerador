#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linka a Aula 9 no hub eduarda-gabriel.html (prof + aluno):
- Pre-class = accordion INLINE (ex-lesson-9, colapsado, igual 1-8)  [prof + aluno]
- IN CLASS  = card -> standalone (?autostart=1)                      [prof]
- stamp9, totalLessons 8->9, + 18 chaves de audio do pre-class no audioMap [prof + aluno]
REGRA 38 + DIALOGUE CONTRAST FIX ja existem no hub. Idempotente."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')
ALUNO= os.path.join(ROOT, 'public', 'aluno', 'eduarda-gabriel.html')

accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
accordion = accordion.replace('<div class="lesson-card open" id="ex-lesson-9">',
                              '<div class="lesson-card" id="ex-lesson-9">', 1)
assert 'class="lesson-card" id="ex-lesson-9"' in accordion
PRECLASS_BLOCK = '<!-- AULA 9 -- Pre-class inline (accordion, igual aulas 1-8) -->\n' + accordion + '\n\n'

ph = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))
pre = [p for p in ph if not p['file'].startswith('listening_') and not re.match(r'd\d', p['file'])]
assert len(pre) == 18, len(pre)
AUDIO_ENTRIES = ''.join(
    '  %s: %s,\n' % (json.dumps(p['key'], ensure_ascii=False),
                     json.dumps('/audio/eduarda-gabriel/' + p['file'], ensure_ascii=False))
    for p in pre)

STAMP8 = '<div class="stamp" id="stamp8" data-label="Defend" style="background-image:url(\'https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=200&q=80\')"></div>'
STAMP9 = STAMP8 + '\n<div class="stamp" id="stamp9" data-label="Summary" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>'

IC8_END = '      <div><div style="font-weight:600;font-size:.95rem">Defending a Position: Arguing with Data</div><div style="font-size:.8rem;color:var(--text-dim)">First conditional &amp; opinion frames -- 27 slides</div></div>\n    </a>'
IC9_CARD = IC8_END + '\n    <a href="/professor/eduarda-gabriel-aula9.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>\n      <div><div style="font-weight:600;font-size:.95rem">Summarizing &amp; Clarifying in Real Time</div><div style="font-size:.8rem;color:var(--text-dim)">Reporting verbs &amp; paraphrasing -- 27 slides</div></div>\n    </a>'

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-9"' in s:
        print('  SKIP (ja linkado):', path); return
    subs = [
        (STAMP8, STAMP9, 'stamp9'),
        ('  var totalLessons = 8;', '  var totalLessons = 9;', 'totalLessons'),
        ('</div><!-- /tab-exercises -->', PRECLASS_BLOCK + '</div><!-- /tab-exercises -->', 'preclass accordion'),
        ('var audioMap = {\n', 'var audioMap = {\n' + AUDIO_ENTRIES, 'audioMap'),
    ]
    if is_prof:
        subs.insert(2, (IC8_END, IC9_CARD, 'inclass card'))
    for old, new, label in subs:
        assert s.count(old) == 1, 'anchor x%d for %s in %s' % (s.count(old), label, path)
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s)
    print('  patched:', path)

print('PROF:');  patch(PROF, True)
print('ALUNO:'); patch(ALUNO, False)
