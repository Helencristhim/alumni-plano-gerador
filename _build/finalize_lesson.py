#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finalize Milton lesson N (generic): derive aluno + update prof/aluno hubs
(inline accordion, audioMap merge, stamp, totalLessons, prof IN CLASS card).
Usage: python3 finalize_lesson.py <N>
"""
import os, re, sys
WT = '/home/dan/dev/work/better/wt-milton'
def P(*a): return os.path.join(WT, *a)
N = int(sys.argv[1])

META = {
    9:  dict(title="Contracts and Agreements", desc="Legal Vocabulary & the Past Simple",
            label="Contracts", img="https://images.unsplash.com/photo-1450101499163-c8848c66ca85",
            mins=60, slides=32),
    10: dict(title="Supply Chain", desc="From Brazil to the U.S. - the Passive Voice",
            label="Supply", img="https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3",
            mins=60, slides=32),
}[N]

def derive_aluno(N):
    src = P('public/professor/milton-sayegh-aula%d.html' % N)
    dst = P('public/aluno/milton-sayegh-aula%d.html' % N)
    a = open(src, encoding='utf-8').read()
    def sub1(pat, repl, s):
        s2, n = re.subn(pat, lambda m: repl, s, count=1, flags=re.S); assert n == 1, "derive: %s" % pat[:50]; return s2
    a = a.replace("Professor View — Milton Sayegh | Aula %d" % N, "Aluno — Milton Sayegh | Aula %d" % N)
    a = a.replace('<span class="view-badge">PROFESSOR VIEW</span>', '<span class="view-badge">ALUNO</span>')
    a = sub1(r'<div class="tabs">.*?</div>',
        '<div class="tabs">\n    <button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button>\n    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n  </div>', a)
    a = sub1(r'<!-- ========== TAB 1: PLANEJAMENTO ========== -->.*?(<!-- ========== TAB 2: PRE-CLASS ========== -->)', r'\1', a)
    a = a.replace('<div class="tab-content" id="tab-exercises">', '<div class="tab-content active" id="tab-exercises">')
    a = sub1(r'<!-- ========== TAB 3: IN CLASS ========== -->.*?(<!-- ========== TAB 4: COMPLEMENTARES ========== -->)', r'\1', a)
    a = sub1(r'<!-- ========== SLIDES WRAPPER.*?</div><!-- /slides-wrapper -->\n', '', a)
    open(dst, 'w', encoding='utf-8').write(a); print("  derived", dst)

derive_aluno(N)

def get_lesson_card(path, N):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'<div class="lesson-card open" id="ex-lesson-%d">.*?</div><!-- /lesson-card -->' % N, s, re.S)
    assert m, "lesson-card %d not in %s" % (N, path)
    return m.group(0).replace('lesson-card open" id="ex-lesson-%d"' % N, 'lesson-card" id="ex-lesson-%d"' % N, 1)

def get_audiomap(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'var audioMap = \{(.*?)\n\};', s, re.S); assert m
    return re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+)"', m.group(1))

def merge_audiomap(h, entries):
    m = re.search(r'(var audioMap = \{)(.*?)(\n\};)', h, re.S); assert m
    body = m.group(2); have = set(re.findall(r'\n\s*"((?:[^"\\]|\\.)*)"\s*:', body))
    add = ['    "%s": "%s"' % (k, v) for k, v in entries if k not in have and not have.add(k)]
    if not add: return h
    return h[:m.start(2)] + body.rstrip() + ",\n" + ",\n".join(add) + h[m.end(2):]

def update_hub(view):
    hub = P('public/%s/milton-sayegh.html' % view); h = open(hub, encoding='utf-8').read()
    acc = get_lesson_card(P('public/%s/milton-sayegh-aula%d.html' % (view, N)), N)
    assert ('id="ex-lesson-%d"' % N) not in h, "ex-lesson-%d already in %s hub" % (N, view)
    assert '<button class="reset-btn"' in h
    h = h.replace('<button class="reset-btn"', acc + '\n\n<button class="reset-btn"', 1)
    h = merge_audiomap(h, get_audiomap(P('public/%s/milton-sayegh-aula%d.html' % (view, N))))
    # stamp N after stamp N-1
    h = re.sub(r'(<div class="stamp" id="stamp%d"[^>]*></div>)' % (N-1),
        lambda m: m.group(1) + ('\n        <div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'%s?w=200&q=80\')"></div>' % (N, META["label"], META["img"])),
        h, count=1)
    assert ('id="stamp%d"' % N) in h, "stamp%d not added" % N
    h = h.replace('var totalLessons = %d;' % (N-1), 'var totalLessons = %d;' % N)
    h = h.replace('var totalLessons=%d;' % (N-1), 'var totalLessons=%d;' % N)
    if view == 'professor':
        card = ('<a href="/professor/milton-sayegh-aula%d.html?autostart=1" style="text-decoration:none;color:inherit">\n'
                '<div class="inclass-lesson-card" style="cursor:pointer">\n'
                '  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>\n'
                '  <div class="ilc-info">\n'
                '    <div class="ilc-number">LESSON %02d — %d MINUTES</div>\n'
                '    <div class="ilc-title">%s</div>\n'
                '    <div class="ilc-desc">%s — %d slides</div>\n'
                '  </div>\n  <div class="ilc-arrow">&#8594;</div>\n</div>\n</a>') % (
                N, N, META["mins"], META["title"], META["desc"], META["slides"])
        assert '</div><!-- /tab-inclass -->' in h
        h = h.replace('</div><!-- /tab-inclass -->', card + '\n\n</div><!-- /tab-inclass -->', 1)
    open(hub, 'w', encoding='utf-8').write(h); print("  updated %s hub" % view)

update_hub('professor'); update_hub('aluno'); print("DONE aula", N)
