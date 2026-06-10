#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generic standalone builder for Eduardo Chiba aula N (REGRA 34).
Usage: python3 _build/build_eduardo.py N
Reads _build/aula{N}/{slides,preclass,complementary}.html, phrases.json, meta.json.
Copies CSS+JS+Planejamento+phase-bar verbatim from the hub; adapts JS for one standalone lesson."""
import os, re, json, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.abspath(os.path.join(HERE, '..'))
SLUG = 'eduardo-chiba'
SCAFFOLD = os.path.join(WT, 'public', 'professor', f'{SLUG}.html')
PROF_OUT = os.path.join(WT, 'public', 'professor', f'{SLUG}-aula{N}.html')
ALUNO_OUT= os.path.join(WT, 'public', 'aluno', f'{SLUG}-aula{N}.html')
D = os.path.join(HERE, 'aula%d' % N)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

scaffold = read(SCAFFOLD)
slides   = read(os.path.join(D, 'slides.html'))
preclass = read(os.path.join(D, 'preclass.html'))
compl    = read(os.path.join(D, 'complementary.html'))
phrases  = json.loads(read(os.path.join(D, 'phrases.json')))
meta     = json.loads(read(os.path.join(D, 'meta.json')))   # {subtitle, menu_desc, passport}

slide_nums = [int(x) for x in re.findall(r'data-slide="(\d+)"', slides)]
S = len(slide_nums)
assert S >= 25, 'too few slides: %d' % S
assert slide_nums == list(range(1, S+1)), 'slides must be 1..S: %s' % slide_nums
phase_map = {int(s): int(p) for s, p in re.findall(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', slides)}
assert len(phase_map) == S, 'every slide needs data-phase'
SLIDEPHASES = '{' + ','.join('%d:%d' % (i, phase_map[i]) for i in range(1, S+1)) + '}'
# checklist must target this lesson
assert ('id="checklist-%d"' % N) in slides, 'slides need id="checklist-%d"' % N
assert ('data-lesson="%d"' % N) in slides, 'slides need data-lesson="%d"' % N

css = scaffold[scaffold.index('<style>'):scaffold.index('</style>')+len('</style>')]

# main inline script = the one that defines lessonRanges (NOT the trailing #inclass handler)
lr = scaffold.index('var lessonRanges')
js_start = scaffold.rfind('<script>', 0, lr)
js = scaffold[js_start:scaffold.index('</script>', lr)+len('</script>')]
def rx(pat, rep, s, n=1):
    new, k = re.subn(pat, rep, s, count=n)
    assert k == n, 'JS patch failed (%d/%d): %s' % (k, n, pat[:50])
    return new
js = rx(r'var lessonRanges = \{[^;]*\};', 'var lessonRanges = { %d: {start:1, end:%d} };' % (N, S), js)
js = rx(r'var currentLesson = \d+;', 'var currentLesson = %d;' % N, js)
js = rx(r'var totalSlides = \d+;', 'var totalSlides = %d;' % S, js)
js = rx(r'var slidePhases = \{[^;]*\};', 'var slidePhases = %s;' % SLIDEPHASES, js)
js = rx(r'var totalLessons = \d+;', 'var totalLessons = %d;' % N, js)
EXIT = ("function toggleLesson(header) { header.parentElement.classList.toggle('open'); }\n\n"
        "function exitSlideMode() {\n  document.body.classList.remove('slide-mode');\n"
        "  window.location.href = '/professor/%s.html#inclass';\n}\n"
        "document.addEventListener('keydown', function(e) {\n"
        "  if (e.key === 'Escape' && document.body.classList.contains('slide-mode')) exitSlideMode();\n});\n" % SLUG)
js = js.replace("function toggleLesson(header) { header.parentElement.classList.toggle('open'); }", EXIT, 1)
assert 'exitSlideMode' in js and ('%s.html#inclass' % SLUG) in js

planning = scaffold[scaffold.index('<div class="tab-content active" id="tab-planning">'):
                    scaffold.index('<div class="tab-content" id="tab-exercises">')].rstrip()
phasebars = scaffold[scaffold.index('<div class="phase-bar"'):scaffold.index('<div class="slides-container"')]

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False))
    for p in phrases) + '\n};'
TAIL_SCRIPTS = ('<script src="/lib/lesson-progress.js"></script>\n'
                '<script src="/lib/controle-aulas.js"></script>\n'
                '<script src="/lib/activity-sync.js"></script>\n')

def head(title):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n' + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='%s';window.TOTAL_AULAS=39;</script>\n</head>\n" % SLUG)

def header(badge):
    return ('<body>\n\n<div class="logo-bar">\n  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n'
      '  <span class="prof-badge">' + badge + '</span>\n'
      '  <span class="slide-counter" id="slideCounter">01 / %02d</span>\n</div>\n\n' % S
      + '<div class="main-content">\n\n<div class="header">\n  <div class="header-content">\n'
      '    <div class="passport-badge">Business English -- Lesson %d</div>\n' % N
      + '    <h1>Eduardo Chiba</h1>\n'
      '    <p class="subtitle">' + meta['subtitle'] + '</p>\n'
      '    <div class="student-info">\n      <span>B2</span>\n      <span>São Paulo, SP -- Jardins</span>\n'
      '      <span>Head of B2B Unit / Quinto Andar</span>\n      <span>60 min / Online</span>\n    </div>\n'
      '    <div class="progress-passport">\n'
      '      <div class="progress-label"><span>Overall Progress</span><span id="progressPercent">0%</span></div>\n'
      '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>\n'
      '      <div class="stamps-row">\n'
      + ('        <div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'%s\')"></div>\n' % (N, meta['stamp_label'], meta['stamp_img']))
      + '      </div>\n    </div>\n  </div>\n</div>\n\n<div class="container">\n\n'
      '<div class="speed-control">\n  <span class="speed-label">Speed:</span>\n'
      '  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>\n'
      '  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>\n'
      '  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>\n'
      '  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>\n</div>\n\n')

TABS_PROF = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  '    <button class="tab-btn active" onclick="switchTab(\'planning\')">Planejamento</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'exercises\')">Pre-class</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'inclass\')">IN CLASS</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n  </div>\n</div>\n')
TABS_ALUNO = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  '    <button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n  </div>\n</div>\n')

INCLASS_MENU = ('<div class="tab-content" id="tab-inclass">\n'
  '  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.5rem;margin-bottom:1rem">IN CLASS -- Aula %d</h3>\n' % N
  + '  <div style="display:flex;flex-direction:column;gap:.8rem">\n'
  '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(1)">\n'
  '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>\n' % N
  + '      <div><div style="font-weight:600;font-size:.95rem">' + meta['title'] + '</div><div style="font-size:.8rem;color:var(--text-dim)">' + meta['menu_desc'] + ' -- %d slides</div></div>\n' % S
  + '    </div>\n  </div>\n</div>\n')

EXIT_BTN = ('<button onclick="exitSlideMode()" aria-label="Exit to hub" id="exitSlideBtn" style="position:fixed;top:5rem;left:1.5rem;z-index:520;display:none;align-items:center;gap:.4rem;background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.25);border-radius:8px;padding:.5rem .9rem;font:600 .8rem Inter,sans-serif;cursor:pointer"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg> Exit</button>\n<style>body.slide-mode #exitSlideBtn{display:flex}</style>\n')
TAIL = ('<div class="teacher-t" aria-label="Teacher instructions">T<div class="teacher-t-panel" id="teacherPanel"></div></div>\n\n'
  '<div class="nav-bar">\n  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" aria-label="Previous slide"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>\n'
  '  <div class="slide-dots" id="slideDots"></div>\n'
  '  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)" aria-label="Next slide"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>\n</div>\n\n'
  '<div class="confetti-container" id="confettiContainer"></div>\n')

AUDIT = read(os.path.join(D, 'audit.txt'))   # SCENARIO FIT + CONTINUIDADE comment block
INJECT = ''
_ip = os.path.join(D, 'inject.js')
if os.path.exists(_ip):
    INJECT = '<script>\n' + read(_ip).rstrip() + '\n</script>\n'
WELCOME = ('<div class="exercise-section" style="margin-bottom:1.5rem">\n'
  '  <div class="section-header-row"><h4>Welcome back, Eduardo!</h4><span class="badge badge-vocab">Lesson %d</span></div>\n' % N
  + '  <p style="font-size:.88rem;color:var(--text-dim);margin-bottom:1rem">' + meta['welcome'] + '</p>\n</div>\n')

prof = (head('Professor View -- Eduardo Chiba | Aula %d | %s | Alumni by Better' % (N, meta['title']))
    + header('Professor View') + AUDIT + TABS_PROF + '\n' + planning + '\n\n'
    + '<!-- TAB 2: PRE-CLASS -->\n<div class="tab-content" id="tab-exercises">\n' + WELCOME + preclass + '\n</div>\n\n'
    + '<!-- TAB 3: IN CLASS -->\n' + INCLASS_MENU + '\n'
    + '<!-- TAB 4: COMPLEMENTARES -->\n<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="slides-wrapper" id="slidesWrapper">\n\n' + phasebars
    + '<div class="slides-container" id="slidesContainer">\n\n' + slides
    + '\n</div><!-- /slides-container -->\n\n' + EXIT_BTN + TAIL + '</div><!-- /slides-wrapper -->\n\n'
    + js + '\n' + INJECT + TAIL_SCRIPTS + '</body>\n</html>\n')

aluno = (head('Aluno -- Eduardo Chiba | Aula %d | %s | Alumni by Better' % (N, meta['title']))
    + header('Aluno') + TABS_ALUNO + '\n'
    + '<!-- TAB: PRE-CLASS -->\n<div class="tab-content active" id="tab-exercises">\n' + WELCOME + preclass + '\n</div>\n\n'
    + '<!-- TAB: COMPLEMENTARES -->\n<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="confetti-container" id="confettiContainer"></div>\n\n'
    + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n')

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK aula%d (S=%d slides) -> %d / %d bytes' % (N, S, len(prof), len(aluno)))
