#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 20 (Elaine) -- Phone Calls: Reservations. Splices authored
content into the proven aula9 scaffold (CSS+JS verbatim). Mirrors build_aula19.py.
NOTE: output goes to _standalone_ref/ (REGRA 34 reference copy) -- NOT public/. The CI
new-file gate (validate_lesson.py do MODELO) reprova o scaffold legado da Elaine, entao
a aula ENTREGUE e a INLINE no monolitico (ver inline_20.py)."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
REFDIR = os.path.join(HERE, '_standalone_ref')
os.makedirs(REFDIR, exist_ok=True)
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula9.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula9.html')
PROF_OUT  = os.path.join(REFDIR, 'elaine-mieko-pinho-aula20.html')
ALUNO_OUT = os.path.join(REFDIR, 'elaine-mieko-pinho-aula20-aluno.html')
SLUG = 'elaine-mieko-pinho'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, N

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]
def must(s, old, new):
    assert old in s, 'anchor missing: %.40s' % old
    return s.replace(old, new, 1)

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/' % SLUG + p['file'], ensure_ascii=False))
    for p in phrases) + '\n}'

def build(scaffold, badge_is_aluno):
    h = scaffold
    h = must(h, 'Aula 9 | Restaurant Basics', 'Aula 20 | Phone Calls: Reservations')
    i = h.index('var audioMap = {'); j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)
    if not badge_is_aluno:
        MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 20</h3>\n'
                '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
                '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)">\n'
                '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">20</div>\n'
                '      <div><div style="font-weight:600;font-size:.95rem">Phone Calls -- Reservations</div><div style="font-size:.8rem;color:var(--text-dim)">Making and answering a phone call -- 28 slides</div></div>\n'
                '    </div>\n  </div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
        h = must(h, 'var dialogueLine = 0;', 'var dialogueLine = 1;')
        h = must(h, "    if (dialogueLine >= 8) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';",
                    "    if (dialogueLine >= 10) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';")
    return h

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(build(read(PROF_SCAFFOLD), False))
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(build(read(ALUNO_SCAFFOLD), True))
print('OK aula20 standalone (ref) built; audioMap keys', len(phrases))
