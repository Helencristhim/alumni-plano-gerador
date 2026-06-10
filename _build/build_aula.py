#!/usr/bin/env python3
"""Generic assembler for Rafael Gasparelli Lima standalone aulas (REGRA 34).
Usage: python3 _build/build_aula.py N
Reads _build/rafael-aula{N}/ : meta.json, slides.html, preclass.html, complementary.html, phrases.json, inject.js
Copies CSS+JS verbatim from public/professor/rafael-gasparelli-lima.html (scaffold)."""
import os, json, re, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SCAFFOLD = os.path.join(ROOT, 'public', 'professor', 'rafael-gasparelli-lima.html')
SLUG = 'rafael-gasparelli-lima'
D = os.path.join(HERE, 'rafael-aula%d' % N)

meta = json.load(open(os.path.join(D, 'meta.json'), encoding='utf-8'))
scaffold = open(SCAFFOLD, encoding='utf-8').read()
slides = open(os.path.join(D, 'slides.html'), encoding='utf-8').read()
preclass = open(os.path.join(D, 'preclass.html'), encoding='utf-8').read()
complementary = open(os.path.join(D, 'complementary.html'), encoding='utf-8').read()
phrases = json.load(open(os.path.join(D, 'phrases.json'), encoding='utf-8'))
inject = open(os.path.join(D, 'inject.js'), encoding='utf-8').read()

def audiomap_js():
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        v = json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return '<script>\nvar audioMap = {\n' + ',\n'.join(lines) + '\n};\n</script>'

body_idx = scaffold.index('<body>')
head = scaffold[:body_idx]
am_start = head.index('<script>'); am_end = head.index('</script>', am_start) + len('</script>')
head = head[:am_start] + audiomap_js() + head[am_end:]

js_start = scaffold.index('<script>', body_idx)
js_end = scaffold.index('</script>', js_start) + len('</script>')
mainjs = scaffold[js_start:js_end]
mainjs = re.sub(r'var totalLessons = \d+;', 'var totalLessons = 1; var lessonNums = [%d];' % N, mainjs, count=1)
mainjs = mainjs.replace('for (var l = 1; l <= totalLessons; l++) {',
                        'for (var li = 0; li < lessonNums.length; li++) { var l = lessonNums[li];')
assert 'var lessonNums = [%d];' % N in mainjs and 'var l = lessonNums[li];' in mainjs, 'JS patch failed'
mainjs = mainjs[:-len('</script>')] + '\n// ===== AULA %d DATA =====\n' % N + inject + '\n</script>'

def patch_storage(js, suffix):
    js = js.replace("'%s-professor'" % SLUG, "'%s-aula%d-%s'" % (SLUG, N, suffix))
    js = js.replace("'alumni-progress-%s'" % SLUG, "'alumni-progress-%s-aula%d'" % (SLUG, N))
    return js

pl_start = scaffold.index('<div class="tab-content active" id="tab-planning">')
pl_end = scaffold.index('</div><!-- /tab-planning -->') + len('</div><!-- /tab-planning -->')
planning = scaffold[pl_start:pl_end]

wc_start = scaffold.index('<!-- WELCOME CARD -->'); wc_end = scaffold.index('<!-- LESSON 1 CARD -->')
welcome = scaffold[wc_start:wc_end].rstrip()

inclass_menu = '''<div class="tab-content" id="tab-inclass">

<div class="inclass-lesson-card" onclick="startLesson(%d)">
  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON %02d — 60 MINUTES</div>
    <div class="ilc-title">%s</div>
    <div class="ilc-desc">%s — %d slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</div>

</div><!-- /tab-inclass -->''' % (N, N, meta['title'], meta['ilc_desc'], meta['slides_count'])

slides_wrapper = '''<div class="slides-wrapper">
  <div class="phase-bar">
    <div class="phase-segment current" data-phase="1"></div><div class="phase-segment upcoming" data-phase="2"></div><div class="phase-segment upcoming" data-phase="3"></div><div class="phase-segment upcoming" data-phase="4"></div><div class="phase-segment upcoming" data-phase="5"></div><div class="phase-segment upcoming" data-phase="6"></div><div class="phase-segment upcoming" data-phase="7"></div>
  </div>
  <div class="phase-labels">
    <div class="phase-label current" data-phase="1">The Dream</div><div class="phase-label" data-phase="2">Packing Words</div><div class="phase-label" data-phase="3">The Code</div><div class="phase-label" data-phase="4">Getting There</div><div class="phase-label" data-phase="5">Practice</div><div class="phase-label" data-phase="6">Your Turn</div><div class="phase-label" data-phase="7">Wrap-up</div>
  </div>
  <div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>
  <div class="slides-container">

''' + slides + '''

  </div><!-- /slides-container -->
  <div class="nav-bar">
    <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
    <div class="slide-dots" id="slideDots"></div>
    <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>
  </div>
</div><!-- /slides-wrapper -->'''

SUPA_TAIL = '<script src="/lib/lesson-progress.js"></script>\n<script src="/lib/controle-aulas.js"></script>\n<script src="/lib/activity-sync.js"></script>'
SPEED = '''<div class="speed-control">
  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
</div>'''

def header_hero():
    return '''<div class="header" style="background-image:url('%s&w=1400&q=80')">
  <div class="header-content">
    <div class="passport-badge">BUSINESS &amp; LEGAL ENGLISH — Aula %d</div>
    <h1>Rafael Gasparello Lima</h1>
    <p class="subtitle">%s</p>
    <div class="student-info"><span>São Paulo, SP</span><span>A2</span><span>Advogado / Diretor</span><span>60 min</span><span>Online</span></div>
    <div class="progress-passport">
      <div class="progress-label"><span>PROGRESS</span><span id="progressPercent">0%%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
    </div>
  </div>
</div>''' % (meta['header_img'], N, meta['subtitle'])

prof_logo = '''<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">PROFESSOR VIEW</span>
  <select class="lesson-selector" id="lessonSelector" onchange="startLesson(parseInt(this.value))" aria-label="Selecionar aula">
    <option value="%d">Aula %d</option>
  </select>
  <span class="slide-counter" id="slideCounter">01 / %02d</span>
</div>''' % (N, N, meta['slides_count'])

TABS_PROF = '''<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
  <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
  <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
  <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
</div>'''

prof_body = '\n'.join(['<body>', meta.get('fit',''), prof_logo, header_hero(),
  '<div class="main-content">', '<div class="container">', SPEED, TABS_PROF, planning,
  '<div class="tab-content" id="tab-exercises">', welcome, preclass, '</div><!-- /tab-exercises -->',
  inclass_menu,
  '<div class="tab-content" id="tab-complementary">', complementary, '</div><!-- /tab-complementary -->',
  '</div><!-- /container -->', '</div><!-- /main-content -->', slides_wrapper,
  '<div class="confetti-container" id="confettiContainer"></div>',
  patch_storage(mainjs, 'professor'), SUPA_TAIL, '</body>', '</html>'])
prof = head + prof_body

aluno_head = head.replace('Professor View', 'Aluno').replace('— Professor', '— Aluno')
aluno_logo = '''<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">ALUNO</span>
</div>'''
TABS_ALUNO = '''<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('exercises')">Pre-class</button>
  <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
</div>'''
aluno_body = '\n'.join(['<body>', aluno_logo, header_hero(),
  '<div class="main-content">', '<div class="container">', SPEED, TABS_ALUNO,
  '<div class="tab-content active" id="tab-exercises">', welcome, preclass, '</div><!-- /tab-exercises -->',
  '<div class="tab-content" id="tab-complementary">', complementary, '</div><!-- /tab-complementary -->',
  '</div><!-- /container -->', '</div><!-- /main-content -->',
  '<div class="confetti-container" id="confettiContainer"></div>',
  patch_storage(mainjs, 'aluno'), SUPA_TAIL, '</body>', '</html>'])
aluno = aluno_head + aluno_body

pp = os.path.join(ROOT, 'public', 'professor', '%s-aula%d.html' % (SLUG, N))
ap = os.path.join(ROOT, 'public', 'aluno', '%s-aula%d.html' % (SLUG, N))
open(pp, 'w', encoding='utf-8').write(prof)
open(ap, 'w', encoding='utf-8').write(aluno)
print('WROTE', pp, len(prof), 'bytes')
print('WROTE', ap, len(aluno), 'bytes')
print('slides', len(re.findall(r'data-slide="', slides)), 'teacher', len(re.findall(r'data-teacher=', slides)))
