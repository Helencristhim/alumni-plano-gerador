#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finalize Milton Aula 8:
  A) derive aluno aula8 from prof aula8 (2 tabs, badge ALUNO)
  B) update prof + aluno hubs: aulas 6/7/8 Pre-class as INLINE ACCORDIONS
     (lift lesson-card from standalone), merge audioMaps, add stamp8 +
     totalLessons->8; prof also gets the aula8 IN CLASS menu card.
"""
import os, re

WT = '/home/dan/dev/work/better/wt-milton'
def P(*a): return os.path.join(WT, *a)

# ---------------------------------------------------------------- A) derive aluno aula8
def derive_aluno(N):
    src = P('public/professor/milton-sayegh-aula%s.html' % N)
    dst = P('public/aluno/milton-sayegh-aula%s.html' % N)
    a = open(src, encoding='utf-8').read()
    def sub1(pat, repl, s):
        s2, n = re.subn(pat, lambda m: repl, s, count=1, flags=re.S)
        assert n == 1, "derive sub failed: %s" % pat[:60]
        return s2
    a = a.replace("Professor View — Milton Sayegh | Aula %s" % N, "Aluno — Milton Sayegh | Aula %s" % N)
    a = a.replace('<span class="view-badge">PROFESSOR VIEW</span>', '<span class="view-badge">ALUNO</span>')
    a = a.replace('<span class="prof-badge">Professor View</span>', '<span class="prof-badge">ALUNO</span>')
    a = sub1(r'<div class="tabs">.*?</div>',
        '<div class="tabs">\n    <button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button>\n    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n  </div>', a)
    a = sub1(r'<!-- ========== TAB 1: PLANEJAMENTO ========== -->.*?(<!-- ========== TAB 2: PRE-CLASS ========== -->)', r'\1', a)
    a = a.replace('<div class="tab-content" id="tab-exercises">', '<div class="tab-content active" id="tab-exercises">')
    a = sub1(r'<!-- ========== TAB 3: IN CLASS ========== -->.*?(<!-- ========== TAB 4: COMPLEMENTARES ========== -->)', r'\1', a)
    a = sub1(r'<!-- ========== SLIDES WRAPPER.*?</div><!-- /slides-wrapper -->\n', '', a)
    open(dst, 'w', encoding='utf-8').write(a)
    print("  derived", dst)

derive_aluno(8)

# ---------------------------------------------------------------- helpers
def get_lesson_card(standalone_path, N):
    """Lift the <div class="lesson-card open" id="ex-lesson-N"> ... </div><!-- /lesson-card --> block, set closed."""
    s = open(standalone_path, encoding='utf-8').read()
    m = re.search(r'<div class="lesson-card open" id="ex-lesson-%s">.*?</div><!-- /lesson-card -->' % N, s, re.S)
    assert m, "lesson-card not found in %s" % standalone_path
    block = m.group(0).replace('lesson-card open" id="ex-lesson-%s"' % N, 'lesson-card" id="ex-lesson-%s"' % N, 1)
    return block

def get_audiomap(standalone_path):
    s = open(standalone_path, encoding='utf-8').read()
    m = re.search(r'var audioMap = \{(.*?)\n\};', s, re.S)
    assert m, "audioMap not found in %s" % standalone_path
    body = m.group(1)
    entries = re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+)"', body)
    return entries  # list of (key, path)

def merge_audiomap(hub_html, new_entries):
    m = re.search(r'(var audioMap = \{)(.*?)(\n\};)', hub_html, re.S)
    assert m, "hub audioMap not found"
    body = m.group(2)
    have = set(re.findall(r'\n\s*"((?:[^"\\]|\\.)*)"\s*:', body))
    add = []
    for k, v in new_entries:
        if k not in have:
            add.append('    "%s": "%s"' % (k, v)); have.add(k)
    if not add:
        return hub_html
    insert = ",\n" + ",\n".join(add)
    return hub_html[:m.start(2)] + body.rstrip() + insert + hub_html[m.end(2):]

def replace_link_with_accordion(hub_html, N, accordion):
    """Replace the '<!-- LESSON N — LINK ... </a>' block with the accordion."""
    pat = r'<!-- LESSON %s — LINK TO STANDALONE FILE -->\n<a href="[^"]*milton-sayegh-aula%s\.html"[^>]*>\n.*?\n</a>' % (N, N)
    new, n = re.subn(pat, lambda m: accordion, hub_html, count=1, flags=re.S)
    assert n == 1, "link block for aula %s not found" % N
    return new

# ---------------------------------------------------------------- B) update a hub
def update_hub(view):
    hub = P('public/%s/milton-sayegh.html' % view)
    h = open(hub, encoding='utf-8').read()
    base = 'public/%s/milton-sayegh-aula%s.html'

    # 1) replace aula6 & aula7 Pre-class link cards with inline accordions
    for N in (6, 7):
        acc = get_lesson_card(P(base % (view, N)), N)
        h = replace_link_with_accordion(h, N, acc)

    # 2) insert aula8 accordion right after aula7 accordion (before reset-btn)
    acc8 = get_lesson_card(P(base % (view, 8)), 8)
    assert '<button class="reset-btn"' in h, "reset-btn anchor missing in %s hub" % view
    h = h.replace('<button class="reset-btn"', acc8 + '\n\n<button class="reset-btn"', 1)

    # 3) merge audioMaps from standalone 6/7/8
    for N in (6, 7, 8):
        h = merge_audiomap(h, get_audiomap(P(base % (view, N))))

    # 4) stamp8 (after stamp7) if missing
    if 'id="stamp8"' not in h:
        h = h.replace(
            '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>''',
            '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>
        <div class="stamp" id="stamp8" data-label="Review" style="background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80')"></div>''', 1)

    # 5) totalLessons 7 -> 8
    h = h.replace('var totalLessons = 7;', 'var totalLessons = 8;')      # prof formatting
    h = h.replace('var totalLessons=7;', 'var totalLessons=8;')          # aluno minified

    # 6) prof only: aula8 IN CLASS menu card after aula7's
    if view == 'professor':
        a7card = ('<a href="/professor/milton-sayegh-aula7.html?autostart=1" style="text-decoration:none;color:inherit">\n'
                  '<div class="inclass-lesson-card" style="cursor:pointer">\n'
                  '  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>\n'
                  '  <div class="ilc-info">\n'
                  '    <div class="ilc-number">LESSON 07 — 60 MINUTES</div>\n'
                  '    <div class="ilc-title">Numbers and Data</div>\n'
                  '    <div class="ilc-desc">Presenting Financial Information — 32 slides</div>\n'
                  '  </div>\n'
                  '  <div class="ilc-arrow">&#8594;</div>\n'
                  '</div>\n'
                  '</a>')
        a8card = ('<a href="/professor/milton-sayegh-aula8.html?autostart=1" style="text-decoration:none;color:inherit">\n'
                  '<div class="inclass-lesson-card" style="cursor:pointer">\n'
                  '  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>\n'
                  '  <div class="ilc-info">\n'
                  '    <div class="ilc-number">LESSON 08 — 60 MINUTES</div>\n'
                  '    <div class="ilc-title">Review and Consolidation</div>\n'
                  '    <div class="ilc-desc">Putting Lessons 1-7 Together — 32 slides</div>\n'
                  '  </div>\n'
                  '  <div class="ilc-arrow">&#8594;</div>\n'
                  '</div>\n'
                  '</a>')
        assert h.count(a7card) == 1, "aula7 IN CLASS card anchor not found uniquely"
        h = h.replace(a7card, a7card + '\n\n' + a8card, 1)

    open(hub, 'w', encoding='utf-8').write(h)
    print("  updated %s hub" % view)

update_hub('professor')
update_hub('aluno')
print("DONE")
