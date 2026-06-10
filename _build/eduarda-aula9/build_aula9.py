#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build standalone Aula 6 (Eduarda Gabriel) — Eduarda's FIRST separate per-lesson file (REGRA 34).
Scaffold (CSS + JS engine + Planejamento tab) = the monolithic public/professor/eduarda-gabriel.html
(aulas 1-5 inline). We reuse its proven slide engine (enterSlideMode/lessonRanges/goToSlide
scrollTop reset/revealVocab/initPlayer/toggleCheck/nextDialogueLine/challenges).
Fragments authored in _build/eduarda-aula6/*.html ; audio from phrases.json.
Outputs:
  public/professor/eduarda-gabriel-aula6.html  (4 tabs)
  public/aluno/eduarda-gabriel-aula6.html      (2 tabs)
NEVER touches the monolithic eduarda-gabriel.html.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))            # wt-eduarda/
MONO     = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel.html')
PROF_OUT = os.path.join(ROOT, 'public', 'professor', 'eduarda-gabriel-aula9.html')
ALUNO_OUT= os.path.join(ROOT, 'public', 'aluno', 'eduarda-gabriel-aula9.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

TAIL_SCRIPTS = (
    '<script src="/lib/lesson-progress.js"></script>\n'
    '<script src="/lib/controle-aulas.js"></script>\n'
    '<script src="/lib/activity-sync.js"></script>\n'
)

mono     = read(MONO)
slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))

N = len(re.findall(r'data-slide="\d+"', slides))
assert N == 27, 'expected 27 slides, got %d' % N

# ---- 1. CSS block (verbatim from monolith) + REGRA 38 helpers ----
css = mono[mono.index('<style>'):mono.index('</style>')+len('</style>')]
EXIT_CSS = (
".exit-btn{padding:7px 16px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;white-space:nowrap}\n"
".exit-btn:hover{opacity:.85}\n"
".hub-back{display:inline-flex;align-items:center;gap:.3rem;margin-left:1rem;padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:var(--bg-card);color:var(--accent);font-size:.78rem;font-weight:600;text-decoration:none;font-family:'Inter',sans-serif}\n"
".hub-back:hover{background:var(--accent);color:#fff;border-color:var(--accent)}\n"
"body.slide-mode .hub-back{display:none}\n"
)
css = css.replace('</style>', EXIT_CSS + '</style>')

# ---- 2. JS block (the MAIN engine <script> — the one with var totalSlides; the hub may
#         have extra helper <script>s after it, e.g. the REGRA 38 block) ----
js_start = mono.rfind('<script>', 0, mono.index('var totalSlides'))
js_end   = mono.index('</script>', js_start) + len('</script>')
js = mono[js_start:js_end]

# ---- 2a. patch slide-engine state for a single standalone lesson (slides 1..N) ----
js, n = re.subn(r'var totalSlides = 135;', 'var totalSlides = %d;' % N, js)
assert n == 1, 'totalSlides patch'

js, n = re.subn(r'var lessonRanges = \{.*?\};',
                'var lessonRanges = { 9: {start: 1, end: %d} };' % N, js, flags=re.S)
assert n == 1, 'lessonRanges patch'

js, n = re.subn(r'var currentLesson = 1;', 'var currentLesson = 9;', js)
assert n == 1, 'currentLesson patch'

SLIDE_PHASES = '{1:1,2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:4,13:4,14:4,15:4,16:5,17:5,18:5,19:5,20:5,21:5,22:6,23:6,24:6,25:6,26:7,27:7}'
js, n = re.subn(r'var slidePhases = \{.*?\};', 'var slidePhases = ' + SLIDE_PHASES + ';', js, flags=re.S)
assert n == 1, 'slidePhases patch'

# ---- 2b. replace lesson-1 quick-challenge array with aula-9 summarizing situations ----
CHALLENGES = '''var challenges = [
  { prompt: 'The meeting is ending. How do you start your summary?', answer: '"Before we finish, let me sum up the main points."' },
  { prompt: 'Report what your colleague Daniel said.', answer: '"Daniel said that we will move now."' },
  { prompt: 'A colleague did not follow. Paraphrase the decision more simply.', answer: '"In other words, we act now but stay flexible."' },
  { prompt: 'Give the most important point of the meeting.', answer: '"The key takeaway is: act now and review in two weeks."' },
  { prompt: 'Check that everyone understood and agrees.', answer: '"Just to confirm, are we all on the same page?"' },
  { prompt: 'Assign the next steps at the end.', answer: '"Each person has one action item, and we report back Friday."' }
];
var challengeIndex = 0;'''
js, n = re.subn(r'var challenges = \[.*?\];\nvar challengeIndex = 0;', lambda m: CHALLENGES, js, flags=re.S)
assert n == 1, 'challenges patch'

# ---- 2c. null-guard the dots builder (aluno page has no #slideDots) ----
js, n = re.subn(r"var dotsEl = document\.getElementById\('slideDots'\);",
                "var dotsEl = document.getElementById('slideDots'); if(!dotsEl) return;", js)
assert n == 1, 'slideDots guard'

# ---- 2d. REGRA 38 — Exit/Esc volta ao hub na aba IN CLASS + autostart vindo do menu ----
EXTRA_JS = (
"\n// ===== REGRA 38 — Exit volta ao hub (IN CLASS) =====\n"
"function exitSlideMode() {\n"
"  document.body.classList.remove('slide-mode');\n"
"  window.location.href = '/professor/eduarda-gabriel.html#inclass';\n"
"}\n"
"document.addEventListener('keydown', function(e) {\n"
"  if (e.key === 'Escape' && document.body.classList.contains('slide-mode')) exitSlideMode();\n"
"});\n"
"document.addEventListener('DOMContentLoaded', function() {\n"
"  var first = document.querySelector('.slide[data-slide=\"1\"]');\n"
"  if (first && new URLSearchParams(window.location.search).get('autostart') === '1') enterSlideMode(1);\n"
"});\n"
)
assert js.count('</script>') == 1, 'expected single </script> in js block'
js = js.replace('</script>', EXTRA_JS + '</script>')

# ---- 3. Planejamento tab (verbatim from monolith — full 50-aula curriculum) ----
pstart = mono.index('<div class="tab-content active" id="tab-planning">')
pend   = mono.index('<div class="tab-content" id="tab-exercises">')
planning = mono[pstart:pend].rstrip()

# ---- 4. phase-bar + phase-labels (verbatim) ----
phase_bar = mono[mono.index('<div class="phase-bar"'):mono.index('<div class="slides-container"')]

# ---- 5. audioMap from phrases.json ----
def audiomap_js():
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        v = json.dumps('/audio/eduarda-gabriel/' + p['file'], ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return 'var audioMap = {\n' + ',\n'.join(lines) + '\n};'
AUDIOMAP = audiomap_js()

# ---- 6. shared HEAD ----
def head(title):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n'
        + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='eduarda-gabriel';window.TOTAL_AULAS=50;</script>\n"
        '</head>\n')

STAMPS = ('<div class="stamps-row">\n'
  '<div class="stamp" id="stamp1" data-label="Who Is" style="background-image:url(\'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp2" data-label="Floor" style="background-image:url(\'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp3" data-label="Numbers" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp4" data-label="Deal Room" style="background-image:url(\'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp5" data-label="Client" style="background-image:url(\'https://images.unsplash.com/photo-1553877522-43269d4ea984?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp6" data-label="Ice-Break" style="background-image:url(\'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp7" data-label="Turn-Take" style="background-image:url(\'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp8" data-label="Defend" style="background-image:url(\'https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp9" data-label="Summary" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>\n'
  '</div>')

def header(badge, hubhref):
    return ('<body>\n\n'
      '<div class="logo-bar">\n'
      '  <img src="/assets/logo-alumni.png" alt="Alumni by Better">\n'
      '  <span class="prof-badge">' + badge + '</span>\n'
      '  <a href="' + hubhref + '" class="hub-back" title="Voltar para a lista de aulas">&#8592; Aulas</a>\n'
      '  <span class="slide-counter" id="slideCounter">01 / %02d</span>\n' % N
      + '</div>\n\n'
      '<div class="main-content">\n\n'
      '<div class="header">\n'
      '  <div class="header-content">\n'
      '    <div class="passport-badge">Business English -- 50 Aulas</div>\n'
      '    <h1>Eduarda Gabriel</h1>\n'
      '    <p class="subtitle">De &ldquo;eu travo quando a conversa fica longa&rdquo; a falar com confian&ccedil;a em calls de reestrutura&ccedil;&atilde;o e Chapter 11</p>\n'
      '    <div class="student-info">\n'
      '      <span>B1+ (Intermedi&aacute;rio)</span>\n'
      '      <span>S&atilde;o Paulo, SP</span>\n'
      '      <span>Investment Banking Associate / Houlihan Lokey</span>\n'
      '      <span>60 min / Online / 1x semana</span>\n'
      '    </div>\n'
      '    <div class="progress-passport">\n'
      '      <div class="progress-label"><span>Aula 9 &mdash; Summarizing &amp; Clarifying in Real Time</span><span id="progressPercent">0%</span></div>\n'
      '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>\n'
      + STAMPS + '\n'
      '    </div>\n'
      '  </div>\n'
      '</div>\n\n'
      '<div class="container">\n\n'
      '<div class="speed-control">\n'
      '  <span class="speed-label">Velocidade:</span>\n'
      '  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>\n'
      '  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>\n'
      '  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>\n'
      '  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>\n'
      '</div>\n\n')

WELCOME = '''<div class="exercise-section" style="margin-bottom:1.5rem">
  <div class="section-header-row">
    <h4>Welcome, Eduarda!</h4>
    <span class="badge badge-vocab">Onboarding</span>
  </div>
  <p style="font-size:.88rem;line-height:1.7;margin-bottom:1rem">This week you learn to close a meeting clearly: summarize the main points, report what others said with <strong>reporting verbs</strong>, and paraphrase to check understanding. Review these emergency phrases before class.</p>
  <div style="display:grid;gap:0.8rem">
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Let me sum up the main points.</strong><button class="audio-btn" onclick="speakText('Let me sum up the main points.', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">The key takeaway is: act now and review in two weeks.</strong><button class="audio-btn" onclick="speakText('The key takeaway is: act now and review in two weeks.', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Just to confirm, are we all on the same page?</strong><button class="audio-btn" onclick="speakText('Just to confirm, are we all on the same page?', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">I will send a recap email to the team.</strong><button class="audio-btn" onclick="speakText('I will send a recap email to the team.', this)">Listen</button></div>
  </div>
</div>'''

TABS_PROF = '''<div class="tabs-wrapper">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
    <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>
</div>'''

TABS_ALUNO = '''<div class="tabs-wrapper">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>
</div>'''

INCLASS_MENU = '''<div class="tab-content" id="tab-inclass">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 9</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(1)" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>
      <div><div style="font-weight:600;font-size:.95rem">Summarizing &amp; Clarifying in Real Time</div><div style="font-size:.8rem;color:var(--text-dim)">Reporting verbs &amp; paraphrasing &mdash; ''' + str(N) + ''' slides</div></div>
    </div>
  </div>
</div>'''

TAIL = '''<!-- Teacher T Icon -->
<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

<!-- Navigation Bar -->
<div class="nav-bar">
  <button class="exit-btn" onclick="exitSlideMode()" aria-label="Exit to lesson list">&#10005; Exit</button>
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="slide-dots" id="slideDots"></div>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button>
</div>

<div class="confetti-container" id="confettiContainer"></div>'''

AUDIT = '''<!--
SCENARIO FIT — Aula 9
Can-do: "I can close a meeting: summarize the main points, report what others said, and check understanding by paraphrasing."
Gramatica-alvo: reporting verbs (say/tell/suggest + (that) + clause) + paraphrasing frames (in other words / put simply).
Vocab-alvo: sum up, recap, in other words, key takeaway, follow, on the same page, put simply, action item.
Cenario escolhido: fim da reuniao do comite — Eduarda resume as decisoes e Clara confirma/parafraseia.
Por que elicita o alvo: ao fechar uma reuniao o aluno e OBRIGADO a resumir ("Let me sum up..."), reportar o que cada pessoa disse ("Daniel said that...", "Anna suggested..."), parafrasear ("in other words...") e confirmar entendimento ("are we all on the same page?"). >70% dos itens-alvo sao naturalmente elicitados. Habitat natural do focoLinguistico "reporting verbs + paraphrasing".

CONTINUIDADE — Aula 9
Itens novos desta aula: sum up, recap, in other words, key takeaway, follow, on the same page, put simply, action item; reporting verbs + paraphrasing.
Itens revisados (de aulas anteriores): defender posicao da Aula 8 (in my view / first conditional — o conteudo resumido vem das decisoes da Aula 8); go ahead (Aula 7).
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 8 — o aluno (1) da uma opiniao ("In my view...") e (2) usa um first conditional ("If we wait, we will..."); so entao faz a ponte para o tema de hoje (a reuniao acabou; agora ele resume o que foi decidido).
NB: vocabulario novo distinto. A Aula 2 ensinou "clarify"; a Aula 9 NAO re-ensina "clarify" como novo — usa vocabulario diferente (sum up, recap, in other words, key takeaway, put simply, on the same page, action item) + reporting verbs.
-->
'''

# ---- assemble PROFESSOR ----
prof = (
    head('Professor View &mdash; Eduarda Gabriel | Aula 9 | Summarizing &amp; Clarifying | Alumni by Better')
    + header('Professor View', '/professor/eduarda-gabriel.html#inclass')
    + AUDIT
    + TABS_PROF + '\n\n'
    + '<!-- ========== TAB 1: PLANEJAMENTO ========== -->\n' + planning + '\n\n'
    + '<!-- ========== TAB 2: PRE-CLASS ========== -->\n'
    + '<div class="tab-content" id="tab-exercises">\n' + WELCOME + '\n' + preclass + '\n</div>\n\n'
    + '<!-- ========== TAB 3: IN CLASS ========== -->\n' + INCLASS_MENU + '\n\n'
    + '<!-- ========== TAB 4: COMPLEMENTARES ========== -->\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<!-- SLIDES WRAPPER (IN CLASS) -->\n<div class="slides-wrapper">\n\n'
    + phase_bar
    + slides + '\n</div><!-- /slides-container -->\n</div><!-- /slides-wrapper -->\n\n'
    + TAIL + '\n\n'
    + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n'
)

# ---- assemble ALUNO (2 tabs) ----
aluno = (
    head('Aluno &mdash; Eduarda Gabriel | Aula 9 | Summarizing &amp; Clarifying | Alumni by Better')
    + header('Aluno', '/aluno/eduarda-gabriel.html')
    + TABS_ALUNO + '\n\n'
    + '<!-- ========== TAB: PRE-CLASS ========== -->\n'
    + '<div class="tab-content active" id="tab-exercises">\n' + WELCOME + '\n' + preclass + '\n</div>\n\n'
    + '<!-- ========== TAB: COMPLEMENTARES ========== -->\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div><!-- /tab-complementary -->\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="confetti-container" id="confettiContainer"></div>\n\n'
    + js + '\n' + TAIL_SCRIPTS + '</body>\n</html>\n'
)

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)

print('OK  (N=%d slides)' % N)
print('  professor:', PROF_OUT, len(prof), 'bytes')
print('  aluno    :', ALUNO_OUT, len(aluno), 'bytes')
print('  audioMap keys:', len(phrases))
