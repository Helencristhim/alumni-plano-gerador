#!/usr/bin/env python3
"""Link a standalone aula N into the monolithic prof+aluno files (REGRA 34 step 3).
Usage: python3 _build/link_aula.py N
Reads _build/rafael-aula{N}/meta.json for title, link_sub, stamp_img, stamp_label."""
import json, sys, re, os
N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
meta = json.load(open(os.path.join(HERE, 'rafael-aula%d' % N, 'meta.json'), encoding='utf-8'))
T = meta['title']; SUB = meta.get('link_sub', meta['ilc_desc']); IMG = meta['stamp_img']; LBL = meta['stamp_label']; SC = meta['slides_count']
PROF = os.path.join(ROOT, 'public', 'professor', 'rafael-gasparelli-lima.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'rafael-gasparelli-lima.html')

def preclass_card(area):
    return ('''<!-- LESSON %d — LINK (standalone, REGRA 34) -->
<a href="/%s/rafael-gasparelli-lima-aula%d.html" target="_blank"
   style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-top:1rem"
   onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
  <div style="width:48px;height:48px;background:var(--accent-light);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>
  <div><div style="font-weight:600;font-size:.95rem">%s</div><div style="font-size:.8rem;color:var(--text-dim)">%s</div></div>
</a>

<button class="reset-btn" onclick="resetProgress()">Resetar Progresso</button>''' % (N, area, N, N, T, SUB))

MENU = '''<a class="inclass-lesson-card" href="/professor/rafael-gasparelli-lima-aula%d.html" target="_blank" style="text-decoration:none">
  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON %02d — 60 MINUTES</div>
    <div class="ilc-title">%s</div>
    <div class="ilc-desc">%s — %d slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</a>

</div><!-- /tab-inclass -->''' % (N, N, T, SUB, SC)

STAMP = '''\n        <div class="stamp" id="stamp%d" data-label="%s" style="background-image:url('%s?w=200&q=80')"></div>''' % (N, LBL, IMG)

def do(path, prof):
    h = open(path, encoding='utf-8').read()
    # totalLessons bump (any current number -> N)
    h2 = re.sub(r'var totalLessons = \d+;', 'var totalLessons = %d;' % N, h, count=1)
    assert h2 != h, 'totalLessons not found in %s' % path; h = h2
    # pre-class card before reset button
    anc = '<button class="reset-btn" onclick="resetProgress()">Resetar Progresso</button>'
    assert h.count(anc) == 1, 'reset-btn anchor x%d' % h.count(anc)
    h = h.replace(anc, preclass_card('professor' if prof else 'aluno'), 1)
    # stamp after stamp(N-1)
    m = re.search(r'<div class="stamp" id="stamp%d"[^\n]*?</div>' % (N-1), h)
    assert m, 'stamp%d not found' % (N-1)
    h = h[:m.end()] + STAMP + h[m.end():]
    # IN CLASS menu (prof only) — insert after the last <a> menu card
    if prof:
        anc2 = '</a>\n\n</div><!-- /tab-inclass -->'
        assert h.count(anc2) == 1, 'menu anchor x%d' % h.count(anc2)
        h = h.replace(anc2, MENU, 1)
    open(path, 'w', encoding='utf-8').write(h)
    print('linked', path.split('/')[-1])

do(PROF, True)
do(ALUNO, False)
print('OK aula %d linked' % N)
