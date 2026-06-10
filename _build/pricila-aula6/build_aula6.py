#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build standalone Aula 6 (Pricila Adamo) — REGRA 34 + REGRA 38.
Scaffold (CSS + JS engine + Planejamento tab + phase-bar + WELCOME) = monolithic
public/professor/pricila-adamo.html (copper palette, full slide engine).
Fragments authored in _build/pricila-aula6/*.html ; audio from phrases.json.
Outputs:
  public/professor/pricila-adamo-aula6.html  (4 tabs)
  public/aluno/pricila-adamo-aula6.html      (2 tabs)
NEVER touches the monolithic pricila-adamo.html (hub patched separately).
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))            # wt-pricila/
SLUG = 'pricila-adamo'
MONO     = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
PROF_OUT = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula6.html')
ALUNO_OUT= os.path.join(ROOT, 'public', 'aluno', SLUG + '-aula6.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

TAIL_SCRIPTS = (
    '<script src="/lib/lesson-progress.js"></script>\n'
    '<script src="/lib/controle-aulas.js"></script>\n'
    '<script src="/lib/activity-sync.js"></script>\n'
    '<script src="/lib/contrast-guard.js"></script>\n'
)

mono     = read(MONO)
slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))

N = len(re.findall(r'data-slide="\d+"', slides))
assert N == 29, 'expected 29 slides, got %d' % N

# ---- 1. CSS block (verbatim from monolith) + REGRA 38 exit-button helpers ----
css = mono[mono.index('<style>'):mono.index('</style>')+len('</style>')]
EXIT_CSS = (
".exit-btn{padding:7px 16px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;white-space:nowrap}\n"
".exit-btn:hover{opacity:.85}\n"
".hub-back{display:inline-flex;align-items:center;gap:.3rem;margin-left:1rem;padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:var(--bg-card);color:var(--accent);font-size:.78rem;font-weight:600;text-decoration:none;font-family:'Inter',sans-serif}\n"
".hub-back:hover{background:var(--accent);color:#fff;border-color:var(--accent)}\n"
"body.slide-mode .hub-back{display:none}\n"
"[contenteditable][data-placeholder]:empty:before{content:attr(data-placeholder);color:var(--text-dim);font-style:italic}\n"
)
css = css.replace('</style>', EXIT_CSS + '</style>')

# ---- 2. JS block (the inline engine script that defines the slide state) ----
anchor   = mono.index('var totalSlides =')          # robust: target the engine, not trailing scripts
js_start = mono.rfind('<script>', 0, anchor)
js_end   = mono.index('</script>', anchor) + len('</script>')
js = mono[js_start:js_end]

# ---- 2a. patch slide-engine state for this standalone lesson (slides 1..N) ----
js, n = re.subn(r'var totalSlides = \d+;', 'var totalSlides = %d;' % N, js); assert n == 1, 'totalSlides'
SLIDE_PHASES = ('{1:1,2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:4,13:4,14:4,15:4,16:4,'
                '17:5,18:5,19:5,20:5,21:6,22:6,23:6,24:6,25:6,26:7,27:7,28:7,29:7}')
js, n = re.subn(r'var slidePhases = \{.*?\};', 'var slidePhases = ' + SLIDE_PHASES + ';', js, flags=re.S); assert n == 1, 'slidePhases'

# ---- 2b. replace lesson-1 challenges with aula-6 airport polite-request situations ----
CHALLENGES = '''var challenges = [
  { prompt: 'At check-in, ask for a window seat politely.', answer: '"Could I have a window seat, please?"' },
  { prompt: 'Your bag is heavy. Ask the agent for help, very politely.', answer: '"Would you mind helping me with my luggage?"' },
  { prompt: 'You want to check one suitcase. Tell the agent your wish.', answer: '"I would like to check one bag, please."' },
  { prompt: 'Ask the agent which gate your flight is.', answer: '"Could you tell me which gate it is, please?"' },
  { prompt: 'There is a delay. Ask politely when the flight will board.', answer: '"Could you tell me when the flight will board?"' },
  { prompt: 'You did not hear the gate number. Ask the agent to repeat it.', answer: '"Sorry, could you repeat that, please?"' }
];
var challengeIndex = 0; var challengeCorrect = 0;'''
js, n = re.subn(r'var challenges = \[.*?\];\s*var challengeIndex = 0; var challengeCorrect = 0;',
                lambda m: CHALLENGES, js, flags=re.S); assert n == 1, 'challenges'

# ---- 2c. null-guard the dots builder (aluno page has no #slideDots) ----
js, n = re.subn(r"var dotsEl = document\.getElementById\('slideDots'\);",
                "var dotsEl = document.getElementById('slideDots'); if(!dotsEl) return;", js); assert n == 1, 'slideDots guard'

# ---- 2d. per-aula localStorage key (do not collide with hub progress) ----
js = js.replace("'alumni-progress-pricila-adamo'", "'alumni-progress-pricila-adamo-aula6'")

# ---- 2e. REGRA 38 — Exit/Esc volta ao hub na aba IN CLASS + autostart vindo do menu ----
EXTRA_JS = (
"\n// ===== REGRA 38 — Exit volta ao hub (IN CLASS) =====\n"
"function exitSlideMode() {\n"
"  document.body.classList.remove('slide-mode');\n"
"  window.location.href = '/professor/pricila-adamo.html#inclass';\n"
"}\n"
"document.addEventListener('keydown', function(e) {\n"
"  if (e.key === 'Escape' && document.body.classList.contains('slide-mode')) exitSlideMode();\n"
"});\n"
"document.addEventListener('DOMContentLoaded', function() {\n"
"  var first = document.querySelector('.slide[data-slide=\"1\"]');\n"
"  if (first && new URLSearchParams(window.location.search).get('autostart') === '1') enterSlideMode();\n"
"});\n"
)
assert js.count('</script>') == 1, 'expected single </script> in js block'
js = js.replace('</script>', EXTRA_JS + '</script>')

# ---- 3. Planejamento tab (verbatim from monolith — full 40-aula curriculum) ----
pstart = mono.index('<div class="tab-content active" id="tab-planning">')
pend   = mono.index('</div><!-- /tab-planning -->') + len('</div><!-- /tab-planning -->')
planning = mono[pstart:pend]

# ---- 4. phase-bar + phase-labels (verbatim) ----
phase_bar = mono[mono.index('<div class="phase-bar"'):mono.index('<div class="slides-container"')]

# ---- 5. WELCOME card (aula-6 specific; all speakText phrases are in phrases.json) ----
welcome = '''<div class="exercise-section" style="margin-bottom:1.5rem">
  <div class="section-header-row"><h4>Welcome back, Pricila!</h4><span class="badge badge-vocab">Onboarding</span></div>
  <p style="font-size:.88rem;line-height:1.7;margin-bottom:1rem">Your passport is ready and your trip is starting. This week we go to the <strong>airport</strong>: how to <strong>check in</strong>, choose your seat, and <strong>board</strong> your flight &mdash; all with <strong>polite requests</strong>. Review these emergency phrases before class.</p>
  <div style="display:grid;gap:0.8rem">
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Could I have a window seat, please?</strong><button class="audio-btn" onclick="speakText('Could I have a window seat, please?', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Could you check my bag, please?</strong><button class="audio-btn" onclick="speakText('Could you check my bag, please?', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Would you mind helping me with my luggage?</strong><button class="audio-btn" onclick="speakText('Would you mind helping me with my luggage?', this)">Listen</button></div>
    <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><strong style="font-size:0.9rem">Excuse me, where is the gate?</strong><button class="audio-btn" onclick="speakText('Excuse me, where is the gate?', this)">Listen</button></div>
  </div>
</div>'''

# ---- 6. audioMap from phrases.json ----
def audiomap_js():
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        v = json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return 'var audioMap = {\n' + ',\n'.join(lines) + '\n};'
AUDIOMAP = audiomap_js()

# ---- 7. shared HEAD ----
def head(title):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n'
        + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='pricila-adamo';window.TOTAL_AULAS=40;</script>\n"
        '</head>\n')

STAMPS = ('<div class="stamps-row">\n'
  '<div class="stamp" id="stamp1" data-label="Who Is" style="background-image:url(\'https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp2" data-label="Life" style="background-image:url(\'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp3" data-label="Retire" style="background-image:url(\'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp4" data-label="Travel" style="background-image:url(\'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp5" data-label="Health" style="background-image:url(\'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp6" data-label="Airport" style="background-image:url(\'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=200&q=80\')"></div>\n'
  '</div>')

SPEED = ('<div class="speed-control">\n'
  '  <span class="speed-label">Velocidade:</span>\n'
  '  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>\n'
  '  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>\n'
  '  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>\n'
  '  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>\n'
  '</div>\n\n')

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
      '    <div class="passport-badge">Travel English -- 40 Aulas</div>\n'
      '    <h1>Pricila Adamo</h1>\n'
      '    <p class="subtitle">De &ldquo;eu sei o que quero dizer mas n&atilde;o consigo dizer&rdquo; para &ldquo;passaporte pronto, ingl&ecirc;s pronto&rdquo;</p>\n'
      '    <div class="student-info">\n'
      '      <span>B1+ (B2 operacional)</span>\n'
      '      <span>Araras, SP</span>\n'
      '      <span>Dentista em transi&ccedil;&atilde;o para aposentadoria</span>\n'
      '      <span>60 min / Online</span>\n'
      '    </div>\n'
      '    <div class="progress-passport">\n'
      '      <div class="progress-label"><span>Aula 6 &mdash; At the Airport: Checking In and Boarding</span><span id="progressPercent">0%</span></div>\n'
      '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>\n'
      + STAMPS + '\n'
      '    </div>\n'
      '  </div>\n'
      '</div>\n\n'
      '<div class="container">\n\n'
      + SPEED)

WELCOME_PROF = welcome  # reuse aula-1 welcome card (emergency phrases) verbatim

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
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 6</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode()" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>
      <div><div style="font-weight:600;font-size:.95rem">At the Airport &mdash; Checking In and Boarding</div><div style="font-size:.8rem;color:var(--text-dim)">Polite requests (Could I...? / Would you mind...?) &mdash; ''' + str(N) + ''' slides</div></div>
    </div>
  </div>
</div>'''

TAIL = '''<!-- TEACHER T -->
<div class="teacher-t">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

<!-- CONFETTI -->
<div class="confetti-container" id="confettiContainer"></div>

<!-- NAV BAR -->
<div class="nav-bar">
  <button class="exit-btn" onclick="exitSlideMode()" aria-label="Exit to lesson list">&#10005; Exit</button>
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" aria-label="Previous slide"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="slide-dots" id="slideDots"></div>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)" aria-label="Next slide"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>
</div>'''

AUDIT = '''<!--
SCENARIO FIT — Aula 6
Can-do: "I can check in for a flight, ask for what I need, and board a plane using polite requests (Could I...? / Would you mind...?)."
Gramatica-alvo: polite requests — Could I + have/get; Could you + verb; Would you mind + V-ing; I would like + to + verb; Can I vs Could I (degrees of politeness).
Vocab-alvo: check-in, boarding pass, gate, luggage, carry-on, aisle seat, window seat, delay.
Cenario escolhido: balcao de check-in + embarque no aeroporto (Pricila, dentista em transicao para aposentadoria que sonha viajar para a Australia, faz o check-in do seu voo).
Por que elicita o alvo: no balcao de check-in o aluno e OBRIGADO a pedir assento, despachar mala, perguntar o portao e lidar com um atraso — exatamente "Could I have...?", "Could you...?", "Would you mind...?", "I would like to...". >70% dos itens-alvo (8 vocab + 4 estruturas) sao naturalmente elicitados. Habitat natural do focoLinguistico "polite requests".

CONTINUIDADE — Aula 6
Itens novos desta aula: check-in, boarding pass, gate, luggage, carry-on, aisle seat, window seat, delay; pedidos educados (Could I / Could you / Would you mind + -ing / I would like to).
Itens revisados (de aulas anteriores): modais should/could/might da Aula 5 (Health & Wellness) — o "could" de conselho vira "could" de pedido educado; o sonho de viajar/explorar (Aula 3 retirement dream + Aula 4 travel); present perfect de experiencias (Aula 1).
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens — (1) o aluno da um conselho com should/could ("Before a long flight, you should arrive early; you could drink water") direto da Aula 5; (2) retoma o sonho de explorar a Australia (Aula 3/4) e faz a ponte: agora a viagem comeca DE VERDADE no aeroporto. Ponte explicita: o mesmo "could" do conselho agora faz um pedido educado.
NB: os substantivos de aeroporto apareceram apenas incidentalmente no artefato da Aula 1 (boarding pass / gate / seat num cartao de embarque) — nunca foram ENSINADOS como vocabulario. Aqui sao o foco lexical pela primeira vez, sem reintroduzir nada ja ensinado nas Aulas 1-5 (experience, journey, fluent, confident, struggle, routine, abroad, retire, accomplish, explore; wellness/balance/mindful/symptom/etc.).
-->
'''

# ---- assemble PROFESSOR ----
prof = (
    head('Professor View &mdash; Pricila Adamo | Aula 6 | At the Airport | Alumni by Better')
    + header('PROFESSOR VIEW', '/professor/pricila-adamo.html#inclass')
    + AUDIT
    + TABS_PROF + '\n\n'
    + '<!-- ========== TAB 1: PLANEJAMENTO ========== -->\n' + planning + '\n\n'
    + '<!-- ========== TAB 2: PRE-CLASS ========== -->\n'
    + '<div class="tab-content" id="tab-exercises">\n'
    + '<div class="lesson-card open" id="ex-lesson-6">\n'
    + '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
    + '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80\')"></div>\n'
    + '    <div class="lesson-header-content">\n'
    + '      <div class="lesson-number">Aula 06 -- Pre-class</div>\n'
    + '      <h3>At the Airport</h3>\n'
    + '      <div class="lesson-desc">Checking In and Boarding: polite requests (Could I...? / Would you mind...?)</div>\n'
    + '      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>\n'
    + '    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n'
    + '  <div class="lesson-body">\n' + WELCOME_PROF + '\n' + preclass + '\n  </div>\n</div>\n'
    + '</div>\n\n'
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
    head('Aluno &mdash; Pricila Adamo | Aula 6 | At the Airport | Alumni by Better')
    + header('ALUNO', '/aluno/pricila-adamo.html')
    + TABS_ALUNO + '\n\n'
    + '<!-- ========== TAB: PRE-CLASS ========== -->\n'
    + '<div class="tab-content active" id="tab-exercises">\n'
    + '<div class="lesson-card open" id="ex-lesson-6">\n'
    + '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
    + '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80\')"></div>\n'
    + '    <div class="lesson-header-content">\n'
    + '      <div class="lesson-number">Aula 06 -- Pre-class</div>\n'
    + '      <h3>At the Airport</h3>\n'
    + '      <div class="lesson-desc">Checking In and Boarding: polite requests (Could I...? / Would you mind...?)</div>\n'
    + '      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>\n'
    + '    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n'
    + '  <div class="lesson-body">\n' + WELCOME_PROF + '\n' + preclass + '\n  </div>\n</div>\n'
    + '</div>\n\n'
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
