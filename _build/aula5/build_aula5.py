#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Eduardo Chiba) — SEPARATE files per REGRA 34.
Scaffold = monolithic eduardo-chiba.html (CSS + JS + Planejamento + phase-bar, verbatim).
Adapts JS for a standalone single lesson: lessonRanges {5:[1..N]}, exitSlideMode -> hub#inclass (REGRA 38),
totalSlides/slidePhases/totalLessons. NEVER touches the monolith here (hub patched separately)."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.dirname(os.path.dirname(HERE))            # wt-eduardo/
SLUG = 'eduardo-chiba'
SCAFFOLD = os.path.join(WT, 'public', 'professor', f'{SLUG}.html')
PROF_OUT = os.path.join(WT, 'public', 'professor', f'{SLUG}-aula5.html')
ALUNO_OUT= os.path.join(WT, 'public', 'aluno', f'{SLUG}-aula5.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

scaffold = read(SCAFFOLD)
slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))

# ---- slide count + phases ----
slide_nums = [int(x) for x in re.findall(r'data-slide="(\d+)"', slides)]
N = len(slide_nums)
assert N >= 25, 'too few slides: %d' % N
assert slide_nums == list(range(1, N+1)), 'slides must be numbered 1..N: %s' % slide_nums
phase_map = {int(s): int(p) for s, p in re.findall(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', slides)}
SLIDEPHASES = '{' + ','.join('%d:%d' % (i, phase_map[i]) for i in range(1, N+1)) + '}'

# ---- 1. CSS block (verbatim) ----
css = scaffold[scaffold.index('<style>'):scaffold.index('</style>')+len('</style>')]

# ---- 2. JS block (last inline <script>) with standalone fixes ----
js_start = scaffold.rfind('<script>')
js = scaffold[js_start:scaffold.index('</script>', js_start)+len('</script>')]
def sub1(pat, rep, s):
    new = s.replace(pat, rep)
    assert new != s, 'JS patch not applied: %s' % pat[:60]
    return new
js = sub1('var lessonRanges = { 1: {start:1, end:27}, 2: {start:28, end:54}, 3: {start:55, end:81}, 4: {start:82, end:108} };',
          'var lessonRanges = { 5: {start:1, end:%d} };' % N, js)
js = sub1('var currentLesson = 1;', 'var currentLesson = 5;', js)
js = sub1('var totalSlides = 108;', 'var totalSlides = %d;' % N, js)
# slidePhases line starts with 'var slidePhases = {1:1,...};'
js = re.sub(r'var slidePhases = \{[^;]*\};', 'var slidePhases = %s;' % SLIDEPHASES, js, count=1)
assert SLIDEPHASES in js, 'slidePhases not applied'
js = sub1('  var totalLessons = 4;', '  var totalLessons = 5;', js)
# exitSlideMode (REGRA 38) + Esc handler — inject right after toggleLesson definition
EXIT = ("function toggleLesson(header) { header.parentElement.classList.toggle('open'); }\n\n"
        "function exitSlideMode() {\n"
        "  document.body.classList.remove('slide-mode');\n"
        "  window.location.href = '/professor/%s.html#inclass';\n"
        "}\n"
        "document.addEventListener('keydown', function(e) {\n"
        "  if (e.key === 'Escape' && document.body.classList.contains('slide-mode')) exitSlideMode();\n"
        "});\n" % SLUG)
js = sub1("function toggleLesson(header) { header.parentElement.classList.toggle('open'); }", EXIT, js)
assert 'exitSlideMode' in js and ('%s.html#inclass' % SLUG) in js, 'exit-to-hub missing'

# ---- 3. Planejamento tab (verbatim from scaffold) ----
planning = scaffold[scaffold.index('<div class="tab-content active" id="tab-planning">'):
                    scaffold.index('<div class="tab-content" id="tab-exercises">')].rstrip()

# ---- 4. phase-bar + phase-labels (verbatim) ----
phasebars = scaffold[scaffold.index('<div class="phase-bar"'):scaffold.index('<div class="slides-container"')]

# ---- 5. audioMap from phrases.json ----
AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False))
    for p in phrases) + '\n};'

TAIL_SCRIPTS = ('<script src="/lib/lesson-progress.js"></script>\n'
                '<script src="/lib/controle-aulas.js"></script>\n'
                '<script src="/lib/activity-sync.js"></script>\n')

def head(title):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n' + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='%s';window.TOTAL_AULAS=39;</script>\n" % SLUG
        + '</head>\n')

def header(badge):
    return ('<body>\n\n'
      '<div class="logo-bar">\n'
      '  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n'
      '  <span class="prof-badge">' + badge + '</span>\n'
      '  <span class="slide-counter" id="slideCounter">01 / %02d</span>\n' % N
      + '</div>\n\n'
      '<div class="main-content">\n\n'
      '<div class="header">\n  <div class="header-content">\n'
      '    <div class="passport-badge">Business English -- Lesson 5</div>\n'
      '    <h1>Eduardo Chiba</h1>\n'
      '    <p class="subtitle">Block 1 Review -- The Elevator Pitch</p>\n'
      '    <div class="student-info">\n'
      '      <span>B2</span>\n      <span>São Paulo, SP -- Jardins</span>\n'
      '      <span>Head of B2B Unit / Quinto Andar</span>\n      <span>60 min / Online</span>\n    </div>\n'
      '    <div class="progress-passport">\n'
      '      <div class="progress-label"><span>Overall Progress</span><span id="progressPercent">0%</span></div>\n'
      '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>\n'
      '      <div class="stamps-row">\n'
      '        <div class="stamp" id="stamp5" data-label="Elevator Pitch" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>\n'
      '      </div>\n    </div>\n  </div>\n</div>\n\n'
      '<div class="container">\n\n'
      '<div class="speed-control">\n'
      '  <span class="speed-label">Speed:</span>\n'
      '  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>\n'
      '  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>\n'
      '  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>\n'
      '  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>\n'
      '</div>\n\n')

TABS_PROF = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  '    <button class="tab-btn active" onclick="switchTab(\'planning\')">Planejamento</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'exercises\')">Pre-class</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'inclass\')">IN CLASS</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n'
  '  </div>\n</div>\n')

TABS_ALUNO = ('<div class="tabs-wrapper">\n  <div class="tabs">\n'
  '    <button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button>\n'
  '    <button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button>\n'
  '  </div>\n</div>\n')

INCLASS_MENU = ('<div class="tab-content" id="tab-inclass">\n'
  '  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.5rem;margin-bottom:1rem">IN CLASS -- Aula 5</h3>\n'
  '  <div style="display:flex;flex-direction:column;gap:.8rem">\n'
  '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(1)">\n'
  '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
  '      <div><div style="font-weight:600;font-size:.95rem">Block 1 Review -- The Elevator Pitch</div><div style="font-size:.8rem;color:var(--text-dim)">Identity, value &amp; comparatives, polite asks, present perfect -- %d slides</div></div>\n'
  '    </div>\n  </div>\n</div>\n' % N)

# Exit button shown in slide-mode (REGRA 38)
EXIT_BTN = ('<button onclick="exitSlideMode()" aria-label="Exit to hub" id="exitSlideBtn" style="position:fixed;top:5rem;left:1.5rem;z-index:520;display:none;align-items:center;gap:.4rem;background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.25);border-radius:8px;padding:.5rem .9rem;font:600 .8rem Inter,sans-serif;cursor:pointer"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg> Exit</button>\n'
  '<style>body.slide-mode #exitSlideBtn{display:flex}</style>\n')

TAIL = ('<div class="teacher-t" aria-label="Teacher instructions">T<div class="teacher-t-panel" id="teacherPanel"></div></div>\n\n'
  '<div class="nav-bar">\n'
  '  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" aria-label="Previous slide"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>\n'
  '  <div class="slide-dots" id="slideDots"></div>\n'
  '  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)" aria-label="Next slide"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>\n'
  '</div>\n\n'
  '<div class="confetti-container" id="confettiContainer"></div>\n')

AUDIT = ('<!--\n'
  'SCENARIO FIT -- Aula 5 (Block 1 Review)\n'
  'Can-do: "I can deliver a 60-second elevator pitch: who I am, my value proposition, my proof, and a polite ask."\n'
  'Gramatica-alvo (revisao do Bloco 1): present simple/continuous (identity), comparatives (better than), modals could/would (ask), present perfect (results).\n'
  'Vocab-alvo (revisao): value proposition, competitive advantage, pipeline, onboarding, milestone, revenue, benchmark, follow-up.\n'
  'Cenario escolhido: networking num PropTech summit -- montar e entregar um elevator pitch e responder perguntas de um investidor.\n'
  'Por que elicita o alvo: o pitch OBRIGA o aluno a se apresentar (present simple), comparar com concorrentes (comparativos), provar resultados com numeros (present perfect) e fazer um pedido educado (modais). >70% dos itens-alvo sao naturalmente elicitados.\n\n'
  'CONTINUIDADE -- Aula 5\n'
  'Itens novos desta aula: nenhum (e aula de REVISAO do Bloco 1).\n'
  'Itens revisados (Aulas 1-4): identidade/role (A1); value proposition, competitive advantage, comparativos (A2); proposal, negotiate, could/would, follow-up (A3); growth, benchmark, present perfect + dados (A4).\n'
  'Callback no warm-up (slide 2): retoma ATIVAMENTE 2+ itens da Aula 4 (present perfect com dado -- "We have grown by forty percent") e da Aula 2 (comparativo -- "faster than traditional agencies"). O aluno PRODUZ, nao so reconhece.\n'
  '-->\n')

WELCOME = ('<div class="exercise-section" style="margin-bottom:1.5rem">\n'
  '  <div class="section-header-row"><h4>Welcome back, Eduardo!</h4><span class="badge badge-vocab">Block 1 Review</span></div>\n'
  '  <p style="font-size:.88rem;color:var(--text-dim);margin-bottom:1rem">This is the review lesson for Block 1. You will put everything from Lessons 1-4 together into one tool: your 60-second elevator pitch. Complete the Pre-class before class.</p>\n'
  '</div>\n')

# ---- assemble PROFESSOR ----
prof = (
    head('Professor View -- Eduardo Chiba | Aula 5 | The Elevator Pitch | Alumni by Better')
    + header('Professor View') + AUDIT + TABS_PROF + '\n'
    + planning + '\n\n'
    + '<!-- ========== TAB 2: PRE-CLASS ========== -->\n'
    + '<div class="tab-content" id="tab-exercises">\n' + WELCOME + preclass + '\n</div>\n\n'
    + '<!-- ========== TAB 3: IN CLASS ========== -->\n' + INCLASS_MENU + '\n'
    + '<!-- ========== TAB 4: COMPLEMENTARES ========== -->\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="slides-wrapper" id="slidesWrapper">\n\n' + phasebars
    + '<div class="slides-container" id="slidesContainer">\n\n' + slides
    + '\n</div><!-- /slides-container -->\n\n' + EXIT_BTN + TAIL
    + '</div><!-- /slides-wrapper -->\n\n'
    + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n'
)

# ---- assemble ALUNO (2 tabs) ----
aluno = (
    head('Aluno -- Eduardo Chiba | Aula 5 | The Elevator Pitch | Alumni by Better')
    + header('Aluno') + TABS_ALUNO + '\n'
    + '<!-- ========== TAB: PRE-CLASS ========== -->\n'
    + '<div class="tab-content active" id="tab-exercises">\n' + WELCOME + preclass + '\n</div>\n\n'
    + '<!-- ========== TAB: COMPLEMENTARES ========== -->\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="confetti-container" id="confettiContainer"></div>\n\n'
    + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n'
)

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK (N=%d slides, slidePhases=%d)' % (N, len(phase_map)))
print('  professor:', PROF_OUT, len(prof), 'bytes')
print('  aluno    :', ALUNO_OUT, len(aluno), 'bytes')
