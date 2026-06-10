#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Link Aula 6 into the monolithic eduarda-gabriel.html (prof + aluno) per REGRA 34/29.
Prof: Pre-class link card + IN CLASS menu card + stamp6 + totalLessons 5->6.
Aluno: Pre-class link card + stamp6 + totalLessons 5->6.
Idempotent-ish: asserts each anchor matches exactly once; aborts if already patched."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROF = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')
ALUNO= os.path.join(ROOT, 'public', 'aluno', 'eduarda-gabriel.html')

def patch(path, subs):
    s = open(path, encoding='utf-8').read()
    if 'eduarda-gabriel-aula6.html' in s:
        print('  SKIP (already linked):', path); return
    for old, new, label in subs:
        assert s.count(old) == 1, 'anchor x%d for %s in %s' % (s.count(old), label, path)
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s)
    print('  patched:', path)

PRECLASS_LINK = lambda view: (
'</div><!-- /lesson-card lesson-5 -->\n\n</div><!-- /tab-exercises -->',
'</div><!-- /lesson-card lesson-5 -->\n\n'
'<!-- AULA 6 -- arquivo separado (REGRA 34) -->\n'
'<a href="/%s/eduarda-gabriel-aula6.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-bottom:1.5rem" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'  <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
'  <div><div style="font-weight:600;font-size:.95rem">Ice-Breaking in International Settings</div><div style="font-size:.8rem;color:var(--text-dim)">Social English &amp; question forms &mdash; Pre-class + IN CLASS</div></div>\n'
'</a>\n\n</div><!-- /tab-exercises -->' % view,
'preclass link')

STAMP6 = (
"<div class=\"stamp\" id=\"stamp5\" data-label=\"Client\" style=\"background-image:url('https://images.unsplash.com/photo-1553877522-43269d4ea984?w=200&q=80')\"></div>",
"<div class=\"stamp\" id=\"stamp5\" data-label=\"Client\" style=\"background-image:url('https://images.unsplash.com/photo-1553877522-43269d4ea984?w=200&q=80')\"></div>\n"
"<div class=\"stamp\" id=\"stamp6\" data-label=\"Ice-Break\" style=\"background-image:url('https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=200&q=80')\"></div>",
'stamp6')

TOTALLESSONS = ('  var totalLessons = 5;', '  var totalLessons = 6;', 'totalLessons')

INCLASS_CARD = (
'      <div><div style="font-weight:600;font-size:.95rem">First Client Call</div><div style="font-size:.8rem;color:var(--text-dim)">Review &amp; Simulation -- All structures integrated -- 27 slides</div></div>\n    </div>',
'      <div><div style="font-weight:600;font-size:.95rem">First Client Call</div><div style="font-size:.8rem;color:var(--text-dim)">Review &amp; Simulation -- All structures integrated -- 27 slides</div></div>\n    </div>\n'
'    <a href="/professor/eduarda-gabriel-aula6.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
'      <div><div style="font-weight:600;font-size:.95rem">Ice-Breaking in International Settings</div><div style="font-size:.8rem;color:var(--text-dim)">Social English &amp; question forms -- 27 slides</div></div>\n'
'    </a>',
'inclass menu card')

print('PROFESSOR:')
patch(PROF, [PRECLASS_LINK('professor'), INCLASS_CARD, STAMP6, TOTALLESSONS])
print('ALUNO:')
patch(ALUNO, [PRECLASS_LINK('aluno'), STAMP6, TOTALLESSONS])
