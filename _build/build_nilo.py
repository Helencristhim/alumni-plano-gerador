#!/usr/bin/env python3
"""Assembler for Nilo Mesquita Patussi standalone aulas (REGRA 20/34).
Usage: python3 _build/build_nilo.py N
Reuses rafael-gasparelli-lima.html as the CSS+JS ENGINE scaffold (same modern engine:
qfData/dialogueLines/startLesson/listening players), then overrides accent, header,
planning, welcome, audioMap and slug so the output is 100% Nilo. Reads
_build/nilo-aula{N}/ : meta.json, slides.html, preclass.html, complementary.html,
planning.html, welcome.html, phrases.json, inject.js."""
import os, json, re, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SCAFFOLD = os.path.join(ROOT, 'public', 'professor', 'rafael-gasparelli-lima.html')
SLUG = 'nilo-mesquita-patucci'
NAME = 'Nilo Mesquita Patussi'
D = os.path.join(HERE, 'nilo-aula%d' % N)

meta = json.load(open(os.path.join(D, 'meta.json'), encoding='utf-8'))
scaffold = open(SCAFFOLD, encoding='utf-8').read()
slides = open(os.path.join(D, 'slides.html'), encoding='utf-8').read()
preclass = open(os.path.join(D, 'preclass.html'), encoding='utf-8').read()
complementary = open(os.path.join(D, 'complementary.html'), encoding='utf-8').read()
planning = open(os.path.join(D, 'planning.html'), encoding='utf-8').read()
welcome = open(os.path.join(D, 'welcome.html'), encoding='utf-8').read().rstrip()
phrases = json.load(open(os.path.join(D, 'phrases.json'), encoding='utf-8'))
inject = open(os.path.join(D, 'inject.js'), encoding='utf-8').read()


def strip_leaks(js):
    """Remove rafael lesson-specific data baked into the engine script:
    Object.assign(audioMap, {...}) blocks (point to rafael audio) and
    setTimeout(...speakText('rafael phrase'...)) auto-play demos. The head
    audioMap (built from phrases.json) is the single source of truth."""
    # 1) drop every Object.assign(audioMap, {...}); block
    out, i = [], 0
    while True:
        k = js.find('Object.assign(audioMap', i)
        if k < 0:
            out.append(js[i:]); break
        out.append(js[i:k])
        e = js.find('});', k)
        i = e + 3 if e >= 0 else len(js)
    js = ''.join(out)
    # 2) drop setTimeout(function(){ speakText('literal'...); }, N); demos
    js = re.sub(r"setTimeout\(function\(\)\s*\{\s*speakText\('(?:[^'\\]|\\.)*'[^;]*;\s*\}\s*,\s*\d+\s*\);", '', js)
    # 3) drop any remaining bare literal speakText('...', btn); demo statements
    js = re.sub(r"speakText\('(?:[^'\\]|\\.)*'\s*,\s*btn\s*\);", '', js)
    # 4) drop rafael per-lesson dialogue/quick-fire data (we inject our own).
    #    separate assignments first (safe, non-greedy)...
    js = re.sub(r"dialogueLines\['dialogue\d+'\]\s*=\s*\[.*?\];", '', js, flags=re.S)
    js = re.sub(r"qfData\[\d+\]\s*=\s*\[.*?\];", '', js, flags=re.S)
    js = re.sub(r"qf(?:Index|Correct)\[\d+\]\s*=\s*\d+;", '', js)
    #    ...then empty the inline object declarations via brace matching (handles nesting)
    for decl in ('var dialogueLines = ', 'var qfData = '):
        p = js.find(decl)
        if p < 0:
            continue
        b = js.index('{', p)
        depth, k = 0, b
        while k < len(js):
            if js[k] == '{':
                depth += 1
            elif js[k] == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        js = js[:b] + '{}' + js[k + 1:]
    return js


def retarget(s):
    """Swap rafael identity -> nilo (slug, name, accent, dialogue avatars, title)."""
    s = s.replace('rafael-gasparelli-lima', SLUG)
    s = s.replace('Rafael Gasparello Lima', NAME).replace('Rafael Gasparelli Lima', NAME)
    # accent palette (wine) — swap EVERY hardcoded rafael blue to keep one accent
    s = s.replace('#2C5282', '#7B2D3B').replace('#2c5282', '#7B2D3B')
    s = s.replace('#3B82C4', '#9A4054').replace('#3b82c4', '#9A4054')
    s = re.sub(r'rgba\(\s*44\s*,\s*82\s*,\s*130', 'rgba(123, 45, 59', s)
    # title / focus label
    s = s.replace('Business & Legal English', 'Business English & FIFA')
    # dialogue avatar labels (Nilo=NIL, Carla=CAR)
    s = s.replace("line.avatar === 'tom' ? 'TOM' : 'RAF';",
                  "line.avatar === 'tom' ? 'TOM' : line.avatar === 'nilo' ? 'NIL' : line.avatar === 'carla' ? 'CAR' : 'RAF';")
    # dialogue avatar colors
    s = s.replace('.dialogue-avatar-ic.karen { background:#e67e22; }',
                  '.dialogue-avatar-ic.karen { background:#e67e22; }\n.dialogue-avatar-ic.nilo { background:var(--accent); }\n.dialogue-avatar-ic.carla { background:#9b59b6; }')
    return s


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
head = retarget(head)

js_start = scaffold.index('<script>', body_idx)
js_end = scaffold.index('</script>', js_start) + len('</script>')
mainjs = scaffold[js_start:js_end]
mainjs = re.sub(r'var totalLessons = \d+;', 'var totalLessons = 1; var lessonNums = [%d];' % N, mainjs, count=1)
mainjs = mainjs.replace('for (var l = 1; l <= totalLessons; l++) {',
                        'for (var li = 0; li < lessonNums.length; li++) { var l = lessonNums[li];')
assert 'var lessonNums = [%d];' % N in mainjs and 'var l = lessonNums[li];' in mainjs, 'JS patch failed'
mainjs = strip_leaks(mainjs)
mainjs = mainjs[:-len('</script>')] + '\n// ===== AULA %d DATA =====\n' % N + inject + '\n</script>'
mainjs = retarget(mainjs)


def patch_storage(js, suffix):
    js = js.replace("'%s-professor'" % SLUG, "'%s-aula%d-%s'" % (SLUG, N, suffix))
    js = js.replace("'alumni-progress-%s'" % SLUG, "'alumni-progress-%s-aula%d'" % (SLUG, N))
    return js


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
    return '''<div class="header" style="background-image:url('%s')">
  <div class="header-content">
    <div class="passport-badge">BUSINESS ENGLISH &amp; FIFA — Aula %d</div>
    <h1>%s</h1>
    <p class="subtitle">%s</p>
    <div class="student-info"><span>Bragança Paulista / São Paulo, SP</span><span>B1</span><span>CCO — Corinthians / Advogado Esportivo</span><span>90 min</span><span>Online</span></div>
    <div class="progress-passport">
      <div class="progress-label"><span>PROGRESS</span><span id="progressPercent">0%%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
    </div>
  </div>
</div>''' % (meta['header_img'], N, NAME, meta['subtitle'])


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

prof_body = '\n'.join(['<body>', meta.get('fit', ''), prof_logo, header_hero(),
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
planning_aluno = planning.replace('class="tab-content active" id="tab-planning"', 'class="tab-content" id="tab-planning"')
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
