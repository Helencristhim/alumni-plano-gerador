#!/usr/bin/env python3
"""Inline aulas 6-10 into the monolithic prof+aluno, matching the format of aulas 1-5:
- Pre-class: accordion lesson-card (not link card)
- IN CLASS: startLesson() inline slides (not target=_blank link)
Renumbers data-slide to continue after 144 (no collisions). Merges audioMap + dialogue/qf JS."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'rafael-gasparelli-lima.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'rafael-gasparelli-lima.html')
AULAS = [6, 7, 8, 9, 10]
BASE = 144           # slides 1-5 occupy data-slide 1..144
PER = 27             # each new aula has 27 slides

def offset(n): return BASE + PER * (n - 6)

# ---- collect fragments ----
preclass = {}; slides = {}; meta = {}; inject = {}; audio = {}
for n in AULAS:
    d = os.path.join(HERE, 'rafael-aula%d' % n)
    pc = open(os.path.join(d, 'preclass.html'), encoding='utf-8').read()
    preclass[n] = pc.replace('class="lesson-card open"', 'class="lesson-card"')  # collapsed like 1-5
    sl = open(os.path.join(d, 'slides.html'), encoding='utf-8').read()
    sl = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + offset(n)), sl)
    # only lesson-group 1 stays active in the monolithic (startLesson activates the rest)
    sl = sl.replace('class="lesson-group active" data-lesson-group', 'class="lesson-group" data-lesson-group')
    slides[n] = sl
    meta[n] = json.load(open(os.path.join(d, 'meta.json'), encoding='utf-8'))
    inject[n] = open(os.path.join(d, 'inject.js'), encoding='utf-8').read()
    for p in json.load(open(os.path.join(d, 'phrases.json'), encoding='utf-8')):
        audio[p['key']] = '/audio/rafael-gasparelli-lima/' + p['file']

def audiomap_assign():
    lines = ['  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)) for k, v in audio.items()]
    return 'Object.assign(audioMap, {\n' + ',\n'.join(lines) + '\n});'

def js_injection():
    return ('\n// ===== AULAS 6-10 (inline) =====\n' + audiomap_assign() + '\n' +
            '\n'.join(inject[n] for n in AULAS) + '\n')

def menu_card(n):
    return ('<div class="inclass-lesson-card" onclick="startLesson(%d)">\n'
            '  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>\n'
            '  <div class="ilc-info">\n'
            '    <div class="ilc-number">LESSON %02d — 60 MINUTES</div>\n'
            '    <div class="ilc-title">%s</div>\n'
            '    <div class="ilc-desc">%s — %d slides</div>\n'
            '  </div>\n'
            '  <div class="ilc-arrow">&#8594;</div>\n'
            '</div>' % (n, n, meta[n]['title'], meta[n].get('link_sub', meta[n]['ilc_desc']), meta[n]['slides_count']))

def process(path, prof):
    h = open(path, encoding='utf-8').read()
    area = 'professor' if prof else 'aluno'
    for n in AULAS:
        # 1) Pre-class link card -> accordion card
        pat = re.compile(r'<!-- LESSON %d — LINK \(standalone, REGRA 34\) -->.*?</a>' % n, re.DOTALL)
        assert pat.search(h), 'preclass link card %d not found in %s' % (n, path)
        h = pat.sub(lambda m: preclass[n].rstrip(), h, count=1)
    if prof:
        # 2) IN CLASS menu: replace the whole malformed 6-10 <a> block with clean startLesson divs
        menu_pat = re.compile(r'<a class="inclass-lesson-card" href="/professor/rafael-gasparelli-lima-aula6\.html".*</a>\s*</div><!-- /tab-inclass -->', re.DOTALL)
        assert menu_pat.search(h), 'menu block not found'
        new_menu = '\n\n'.join(menu_card(n) for n in AULAS) + '\n\n</div><!-- /tab-inclass -->'
        h = menu_pat.sub(lambda m: new_menu, h, count=1)
        # 3) insert slides before slides-container close
        anchor = '</div><!-- /slides-container -->'
        assert h.count(anchor) == 1
        block = '\n'.join(slides[n] for n in AULAS) + '\n\n  ' + anchor
        h = h.replace(anchor, block, 1)
    # 4) JS injection before main </script> (the one before lesson-progress.js)
    anchor2 = '</script>\n<script src="/lib/lesson-progress.js"></script>'
    assert h.count(anchor2) == 1, 'tail anchor x%d in %s' % (h.count(anchor2), path)
    h = h.replace(anchor2, js_injection() + '</script>\n<script src="/lib/lesson-progress.js"></script>', 1)
    open(path, 'w', encoding='utf-8').write(h)
    print('inlined ->', path.split('/')[-1])

process(PROF, True)
process(ALUNO, False)
print('DONE inline 6-10')
