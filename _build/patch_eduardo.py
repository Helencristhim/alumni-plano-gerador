#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch the hub (eduardo-chiba.html prof+aluno) for aula N. Usage: python3 _build/patch_eduardo.py N
Idempotent: ex-lesson-N accordion inline, audioMap adds, stampN, totalLessons->N, IN CLASS menu card (prof)."""
import os, re, json, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.abspath(os.path.join(HERE, '..'))
SLUG = 'eduardo-chiba'
PROF = os.path.join(WT, 'public', 'professor', f'{SLUG}.html')
ALUNO= os.path.join(WT, 'public', 'aluno', f'{SLUG}.html')
D = os.path.join(HERE, 'aula%d' % N)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

accordion = read(os.path.join(D, 'preclass.html')).rstrip()
phrases   = json.loads(read(os.path.join(D, 'phrases.json')))
meta      = json.loads(read(os.path.join(D, 'meta.json')))

pk = set(re.findall(r"speakText\('((?:[^'\\]|\\.)*)'", accordion))
pk |= set(re.findall(r'data-phrase="((?:[^"\\]|\\.)*)"', accordion))
pk = {k.replace("\\'", "'").replace('\\"', '"') for k in pk}

def patch_common(html, fname):
    assert ('id="ex-lesson-%d"' % N) not in html, f'{fname}: ex-lesson-{N} already present'
    # 1. audioMap adds (before the audioMap closing '};')
    am0 = html.index('var audioMap = {')
    amc = html.index('\n};', am0)
    block = html[am0:amc]
    existing = {k.replace('\\"', '"') for k in re.findall(r'"((?:[^"\\]|\\.)*)":\s*"/audio/%s/' % re.escape(SLUG), block)}
    adds = ['  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False))
            for p in phrases if p['key'] in pk and p['key'] not in existing]
    if adds:
        html = html[:amc] + ',\n' + ',\n'.join(adds) + html[amc:]
    # 2. Pre-class accordion (before tab-exercises close)
    EX_CLOSE = '</div><!-- /tab-exercises -->'
    assert EX_CLOSE in html, f'{fname}: tab-exercises close missing'
    html = html.replace(EX_CLOSE, '<!-- LESSON %d -->\n%s\n\n%s' % (N, accordion, EX_CLOSE), 1)
    # 3. stampN after stamp(N-1)
    m = re.search(r'<div class="stamp" id="stamp%d"[^>]*></div>' % (N-1), html)
    assert m, f'{fname}: stamp{N-1} anchor missing'
    stampN = '<div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'%s\')"></div>' % (N, meta['stamp_label'], meta['stamp_img'])
    html = html[:m.end()] + '\n        ' + stampN + html[m.end():]
    # 4. totalLessons -> N
    html = re.sub(r'var totalLessons = \d+;', 'var totalLessons = %d;' % N, html)
    return html

# PROFESSOR
prof = read(PROF)
prof = patch_common(prof, 'professor')
# 5. IN CLASS menu card (standalone link, REGRA 34b) — insert right after the previous aula's card </a>
prev_href = '/professor/%s-aula%d.html' % (SLUG, N-1)
pi = prof.find('<a href="%s"' % prev_href)
assert pi != -1, 'professor: previous menu card (aula %d) missing' % (N-1)
pj = prof.index('</a>', pi) + len('</a>')
CARD = ('\n    <a href="/professor/%s-aula%d.html" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n' % (SLUG, N)
  + '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>\n' % N
  + '      <div><div style="font-weight:600;font-size:.95rem">' + meta['title'] + '</div><div style="font-size:.8rem;color:var(--text-dim)">' + meta['menu_desc'] + ' -- %d slides</div></div>\n    </a>' % meta['slides_count'])
prof = prof[:pj] + CARD + prof[pj:]
# 6. #inclass handler (add once)
if "hash === '#inclass'" not in prof and 'hash === "#inclass"' not in prof:
    HA = '</script>\n<script src="/lib/lesson-progress.js"></script>'
    assert HA in prof, 'professor: handler anchor missing'
    H = ('</script>\n<script>\ndocument.addEventListener("DOMContentLoaded", function() {\n'
         '  if (window.location.hash === "#inclass") {\n'
         '    var b = document.querySelector(\'.tab-btn[onclick*="inclass"]\');\n    if (b) b.click();\n  }\n});\n'
         '</script>\n<script src="/lib/lesson-progress.js"></script>')
    prof = prof.replace(HA, H, 1)
write(PROF, prof)

# ALUNO
aluno = read(ALUNO)
aluno = patch_common(aluno, 'aluno')
write(ALUNO, aluno)
print('aula%d hub patched (prof: accordion+audioMap+stamp+menu; aluno: accordion+audioMap+stamp)' % N)
