#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build standalone Aula 9 (Tania Rosa) — SEPARATE files per REGRA 34.
Theme: Family Travel — Coordinating with Family
Grammar: Suggestions (let's / shall we / why don't we / how about)
Vocabulary: family + trip-coordination
Sources:
  - public/professor/tania-rosa-aula8.html  -> CSS + full JS (slides machinery)
  - public/aluno/tania-rosa-aula8.html       -> CSS + reduced JS (pre-class only)
Outputs:
  - public/professor/tania-rosa-aula9.html  (4 tabs, 37 slides)
  - public/aluno/tania-rosa-aula9.html       (2 tabs)
  - _build/tania-aula9/phrases.json          (canonical audio list)
NEVER touches the monolithic tania-rosa.html (linking handled separately).
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))            # wt-tania/
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'tania-rosa-aula9.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'tania-rosa-aula9.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'tania-rosa-aula10.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'tania-rosa-aula10.html')

AUDIO_DIR = '/audio/tania-rosa-aula10/'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

prof_scaffold  = read(PROF_SCAFFOLD)
aluno_scaffold = read(ALUNO_SCAFFOLD)

# ============================================================== AUDIO PHRASES
# voice: ellen = Tania (student/female protagonist), rachel = Sofia (sister),
#        arthur = male narrator (alternation)
def snake(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9' ]", '', s)
    s = s.replace("'", '')
    s = re.sub(r' +', '_', s.strip())
    return s[:56]

# (text, voice). file derived from snake(text). REVIEW lesson — Tania=ellen, friend/traveler=arthur.
GEN = [
    # --- vocab REVIEW words (one per theme) — student female = ellen ---
    ("Passport", "ellen"), ("Boarding pass", "ellen"), ("Reservation", "ellen"),
    ("Directions", "ellen"), ("Menu", "ellen"), ("Souvenir", "ellen"),
    ("Landmark", "ellen"), ("Itinerary", "ellen"),
    # --- review key phrases (fill data-phrase + speech + survival; student=ellen) ---
    ("Here is my passport. I am flying to Paris.", "ellen"),
    ("I would like to check in, please.", "ellen"),
    ("Could I have the menu, please?", "ellen"),
    ("How much is this souvenir?", "ellen"),
    ("I have been to many countries.", "ellen"),
    ("I need to find a pharmacy.", "ellen"),
    ("Let's plan our next trip together.", "ellen"),
    ("Could you tell me the way to the museum?", "ellen"),
    ("Can you help me with my luggage?", "ellen"),
    ("I would like a table for two, please.", "ellen"),
    ("Shall we go sightseeing tomorrow?", "ellen"),
    ("Go straight and turn left.", "ellen"),
    # --- dialogue: friend interviews Tania about her whole trip (Tania=ellen, friend=arthur) ---
    ("So Tânia, you traveled alone in English! How was the airport?", "arthur"),
    ("Great! I said: Here is my passport. Can you help me with my luggage?", "ellen"),
    ("And the hotel?", "arthur"),
    ("I said: I would like to check in. I have a reservation.", "ellen"),
    ("How did you get around the city?", "arthur"),
    ("I asked: Could you tell me the way to the museum?", "ellen"),
    ("And the restaurant?", "arthur"),
    ("I said: Could I have the menu, please? The food was wonderful.", "ellen"),
    ("Did you have any problems?", "arthur"),
    ("Once I felt sick, so I said: I need to find a pharmacy. Let's plan the next trip together!", "ellen"),
    # --- listening 1: Tania (now the expert) helps a new traveler (Tania=ellen, traveler=arthur) ---
    ("Excuse me, you speak English well. Can you help me? I am lost.", "arthur"),
    ("Of course! Go straight and turn left. The hotel is near the restaurant.", "ellen"),
    ("Thank you! I also need to check in for my flight tomorrow.", "arthur"),
    ("At the airport, say: Here is my passport and my boarding pass.", "ellen"),
    ("And how do I order food at a restaurant?", "arthur"),
    ("Say: Could I have the menu, please? It is easy.", "ellen"),
    ("What if I feel sick?", "arthur"),
    ("Say: I need to find a pharmacy. You will be fine!", "ellen"),
    # --- order sequence (single mp3, ellen) ---
    ("[ORDER]Here is my passport. I would like to check in. Could you tell me the way to the museum? Could I have the menu, please? Let's go sightseeing.", "ellen"),
]

PHRASES = []
seen = set()
for text, voice in GEN:
    if text in seen:
        continue
    seen.add(text)
    if text.startswith("[ORDER]"):
        PHRASES.append({"text": text[7:], "file": "order_l10_ordering.mp3", "voice": voice, "key": "[order-l10]"})
    else:
        PHRASES.append({"text": text, "file": snake(text) + ".mp3", "voice": voice, "key": text})

# callback audio (re-uses existing aula9 mp3s — NOT regenerated)
CALLBACK = {
    "Let's plan our family trip together.": "/audio/tania-rosa-aula9/lets_plan_our_family_trip_together.mp3",
    "Shall we invite all our relatives?": "/audio/tania-rosa-aula9/shall_we_invite_all_our_relatives.mp3",
    "Why don't we visit our grandparents?": "/audio/tania-rosa-aula9/why_dont_we_visit_our_grandparents.mp3",
    "How about going sightseeing on Sunday?": "/audio/tania-rosa-aula9/how_about_going_sightseeing_on_sunday.mp3",
}

def audiomap_js():
    lines = []
    for p in PHRASES:
        lines.append('  %s: %s' % (json.dumps(p['key'], ensure_ascii=False),
                                    json.dumps(AUDIO_DIR + p['file'], ensure_ascii=False)))
    for k, v in CALLBACK.items():
        lines.append('  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)))
    return 'var audioMap = {\n' + ',\n'.join(lines) + '\n};'

AUDIOMAP = audiomap_js()

# ============================================================== CSS + JS extract
def extract_css(html):
    return html[html.index('<style>'):html.index('</style>') + len('</style>')]

PROF_CSS  = extract_css(prof_scaffold)
ALUNO_CSS = extract_css(aluno_scaffold)

def extract_inline_js(html):
    # the big inline <script> is the one that defines switchTab()
    anchor = html.index('function switchTab(tabId)')
    js_start = html.rindex('<script>', 0, anchor)
    js_end   = html.index('</script>', anchor) + len('</script>')
    return html[js_start:js_end]

PROF_JS_RAW  = extract_inline_js(prof_scaffold)
ALUNO_JS_RAW = extract_inline_js(aluno_scaffold)

# --- prof JS: swap lesson-8-specific data for aula 9 ---
prof_js = PROF_JS_RAW

# quick-fire challenges (suggestions)
new_challenges = ("var challenges=["
    "{prompt:'At check-in, show your passport.',answer:'\"Here is my passport. I am flying to Paris.\"'},"
    "{prompt:'Ask the way to the hotel restaurant.',answer:'\"Could you tell me where the restaurant is, please?\"'},"
    "{prompt:'Order food at a restaurant.',answer:'\"Could I have the menu, please?\"'},"
    "{prompt:'Ask the price of a souvenir.',answer:'\"How much is this souvenir?\"'},"
    "{prompt:'You feel sick. Find help.',answer:'\"Excuse me, I need to find a pharmacy.\"'},"
    "{prompt:'Suggest sightseeing with your family.',answer:'\"Let\\'s go sightseeing together.\"'}"
    "];")
prof_js = re.sub(r'var challenges=\[.*?\];', new_challenges, prof_js, count=1, flags=re.S)
assert new_challenges in prof_js, 'challenges swap failed'

# helper: build JS array literal with single-quoted strings (apostrophes -> \')
def js_arr(items):
    return 'var lines=[' + ','.join("'%s'" % s.replace("\\", "\\\\").replace("'", "\\'") for s in items) + '];'

# listening 1 lines (Tania helps a new traveler — review of all structures)
L1 = ["Excuse me, you speak English well. Can you help me? I am lost.",
      "Of course! Go straight and turn left. The hotel is near the restaurant.",
      "Thank you! I also need to check in for my flight tomorrow.",
      "At the airport, say: Here is my passport and my boarding pass.",
      "And how do I order food at a restaurant?",
      "Say: Could I have the menu, please? It is easy.",
      "What if I feel sick?",
      "Say: I need to find a pharmacy. You will be fine!"]
l1_js = js_arr(L1)

# listening 2 lines (subset reuse — Tania's advice)
L2 = ["Of course! Go straight and turn left. The hotel is near the restaurant.",
      "At the airport, say: Here is my passport and my boarding pass.",
      "Say: Could I have the menu, please? It is easy.",
      "Say: I need to find a pharmacy. You will be fine!"]
l2_js = js_arr(L2)

# replace the two `var lines=[...]` arrays in order (1st = listening1, 2nd = listening2)
_repl = [l1_js, l2_js]
_idx = [0]
def _sub_lines(m):
    out = _repl[_idx[0]]
    _idx[0] += 1
    return out
prof_js, _n = re.subn(r'var lines=\[.*?\];', _sub_lines, prof_js, count=2, flags=re.S)
assert _n == 2, 'expected 2 var lines arrays, replaced %d' % _n
assert l1_js in prof_js and l2_js in prof_js, 'listening lines swap failed'

# localStorage keys
prof_js = prof_js.replace('alumni-progress-tania-rosa-aula9', 'alumni-progress-tania-rosa-aula10')
prof_js = prof_js.replace("'tania-rosa-aula9-professor'", "'tania-rosa-aula10-professor'")

aluno_js = ALUNO_JS_RAW
aluno_js = aluno_js.replace('alumni-progress-tania-rosa-aula9', 'alumni-progress-tania-rosa-aula10')
aluno_js = aluno_js.replace("'tania-rosa-aula9-aluno'", "'tania-rosa-aula10-aluno'")

# ============================================================== HEAD
def head(title, css):
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">\n'
        '<script>\n' + AUDIOMAP + '\n</script>\n'
        + css + '\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
        '<script src="/lib/supabase-config.js"></script>\n'
        "<script>window.STUDENT_SLUG='tania-rosa';window.TOTAL_AULAS=10;</script>\n"
        '</head>\n')

STAMPS = '''<div class="stamps-row">
<div class="stamp" id="stamp1" data-label="Traveler" style="background-image:url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&q=80')"></div>
<div class="stamp" id="stamp2" data-label="Airport" style="background-image:url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=200&q=80')"></div>
<div class="stamp" id="stamp3" data-label="Hotel" style="background-image:url('https://images.unsplash.com/photo-1566073771259-6a8506099945?w=200&q=80')"></div>
<div class="stamp" id="stamp4" data-label="Food" style="background-image:url('https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80')"></div>
<div class="stamp" id="stamp5" data-label="City" style="background-image:url('https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=200&q=80')"></div>
<div class="stamp" id="stamp6" data-label="Shopping" style="background-image:url('https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80')"></div>
<div class="stamp" id="stamp7" data-label="Health" style="background-image:url('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=200&q=80')"></div>
<div class="stamp" id="stamp8" data-label="Review" style="background-image:url('https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=200&q=80')"></div>
<div class="stamp" id="stamp9" data-label="Family" style="background-image:url('https://images.unsplash.com/photo-1511895426328-dc8714191300?w=200&q=80')"></div>
<div class="stamp" id="stamp10" data-label="Mastery" style="background-image:url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80')"></div>
</div>'''

PROF_HEADER = '''<body>

<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">Professor View</span>
  <span class="slide-counter" id="slideCounter">01 / 37</span>
</div>

<div class="main-content">

<div class="header">
  <div class="header-content">
    <div class="passport-badge">Travel English — 10 Aulas</div>
    <h1>Tânia Rosa</h1>
    <p class="subtitle">De viajante que trava na hora H a comunicadora autônoma que circula pelo mundo com confiança</p>
    <div class="student-info">
      <span>A2</span>
      <span>Perfil Cosmopolita</span>
      <span>60 min / Online</span>
      <span>3x por semana</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label"><span>Aula 10 — Review & Confidence</span><span id="progressPercent">0%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
''' + STAMPS + '''
    </div>
  </div>
</div>

<div class="container">

<div class="speed-control">
  <span class="speed-label">Velocidade:</span>
  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
</div>
'''

ALUNO_HEADER = '''<body>
<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge" style="background:var(--navy);border-color:var(--navy)">ALUNO</span>
</div>
<div class="main-content">
<div class="header">
  <div class="header-content">
    <div class="passport-badge">Travel English — 10 Aulas</div>
    <h1>Tânia Rosa</h1>
    <p class="subtitle">De viajante que trava na hora H a comunicadora autônoma que circula pelo mundo com confiança</p>
    <div class="student-info"><span>A2</span><span>Perfil Cosmopolita</span><span>60 min / Online</span><span>3x por semana</span></div>
    <div class="progress-passport"><div class="progress-label"><span>Aula 10 — Review & Confidence</span><span id="progressPercent">0%</span></div><div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
''' + STAMPS + '''</div>
  </div>
</div>
<div class="container">
<div class="speed-control"><span class="speed-label">Velocidade:</span><button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button><button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button><button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button><button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button></div>
'''

# ============================================================== PLANNING (from scaffold, adapted)
p0 = prof_scaffold.index('<div class="tab-content active" id="tab-planning">')
p1 = prof_scaffold.index('<!-- ========== TAB 2: PRE-CLASS ========== -->')
planning = prof_scaffold[p0:p1].rstrip()
# promise box -> Aula 10 (scaffold is aula9)
planning = planning.replace('Promessa da Aula 9', 'Promessa da Aula 10')
planning = planning.replace(
    'After this lesson, Tânia will confidently coordinate a family trip in English — make suggestions, plan activities, and organize the itinerary with relatives using <em>let’s</em>, <em>shall we</em>, <em>why don’t we</em>, and <em>how about</em>.',
    'After this final lesson, Tânia will confidently handle a full trip from start to finish in English — checking in, getting around, ordering, shopping, talking culture, handling emergencies, and planning with family — combining every structure from the course.')
# move highlighted row 9 -> row 10
planning = planning.replace(
    '<tr style="background:rgba(156,70,104,.08)"><td><strong>9</strong></td><td><strong>Family Travel — Coordinating with Family</strong></td><td><strong>Suggestions (let’s, shall we, why don’t we, how about), family vocabulary</strong></td><td><strong>Family trip planning role-play</strong></td><td><strong>Record 1-min about favorite family trip</strong></td></tr>',
    '<tr><td>9</td><td>Family Travel — Coordinating with Family</td><td>Suggestions (let’s, shall we, why don’t we, how about), family vocabulary</td><td>Family trip planning role-play</td><td>Record 1-min about favorite family trip</td></tr>')
planning = planning.replace(
    '<tr><td>10</td><td>Putting It All Together — Review and Confidence</td><td>All structures reviewed</td><td>Full travel simulation: airport to sightseeing</td><td>Final reflection recording</td></tr>',
    '<tr style="background:rgba(156,70,104,.08)"><td><strong>10</strong></td><td><strong>Putting It All Together — Review and Confidence</strong></td><td><strong>All structures reviewed</strong></td><td><strong>Full travel simulation: airport to sightseeing</strong></td><td><strong>Final reflection recording</strong></td></tr>')
assert 'Promessa da Aula 10' in planning, 'planning promise swap failed'
assert planning.count('background:rgba(156,70,104,.08)"><td><strong>10</strong>') == 1, 'row10 highlight failed'

# ============================================================== FRAGMENTS
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phasebar = prof_scaffold[prof_scaffold.index('<div class="phase-bar" id="phaseBar">'):prof_scaffold.index('<div class="slides-container" id="slidesContainer">')]
slides   = read(os.path.join(HERE, 'slides.html'))

N = len(re.findall(r'data-slide="\d+"', slides))
assert N == 37, 'expected 37 slides, got %d' % N

AUDIT = '''<!--
SCENARIO FIT — Aula 10 (REVIEW)
Can-do: "I can handle a whole trip from start to finish in English, combining every structure from the course."
Gramatica-alvo: REVISAO de TODAS as estruturas — present simple, can/could, would like, imperative + prepositions, could I have, how much/comparatives, present perfect (been to), need to/have to, suggestions (let's/shall we).
Vocab-alvo (revisao): passport, boarding pass, reservation, directions, menu, souvenir, landmark, itinerary (um por tema do curso).
Cenario escolhido: (1) uma amiga ENTREVISTA a Tania sobre como ela lidou com toda a viagem; (2) a Tania, agora EXPERT, AJUDA um viajante novo. Mais um role-play de simulacao completa (airport -> hotel -> directions -> restaurant -> sightseeing).
Por que elicita o alvo: recapitular a viagem inteira e ENSINAR outro viajante obriga a aluna a reusar uma frase-chave de CADA aula ("Here is my passport", "I would like to check in", "Could you tell me the way...", "Could I have the menu", "I have been to...", "I need to find a pharmacy", "Let's go sightseeing"). >70% dos itens-alvo sao elicitados naturalmente.

CONTINUIDADE — Aula 10
Itens novos desta aula: NENHUM (aula de revisao/consolidacao — REGRA 22/37: tudo e revisado, nada apresentado como novo).
Itens revisados (de aulas anteriores): TODOS — present simple (A1), can/could (A2), would like (A3), imperative/prepositions (A4), could I have (A5), how much/comparatives (A6), present perfect been to (A7), need to/have to (A8), suggestions let's/shall we (A9).
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 9 — a aluna USA "Let's plan our family trip together." e "Shall we / Why don't we / How about ...?" (suggestions), fazendo a ponte planejamento em familia -> agora a viagem inteira na pratica.
-->
'''

TABS_PROF = '''<div class="tabs-wrapper">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
    <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>
</div>'''

INCLASS_MENU = '''<!-- ========== TAB 3: IN CLASS ========== -->
<div class="tab-content" id="tab-inclass">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS — Select Lesson</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode();" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">10</div>
      <div><div style="font-weight:600;font-size:.95rem">Putting It All Together</div><div style="font-size:.8rem;color:var(--text-dim)">Review and Confidence — 37 slides</div></div>
    </div>
  </div>
</div>'''

TAIL = '''<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

<div class="nav-bar">
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="slide-dots" id="slideDots"></div>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button>
</div>

<div class="confetti-container" id="confettiContainer"></div>'''

LIBS = ('<script src="/lib/lesson-progress.js"></script>\n'
        '<script src="/lib/controle-aulas.js"></script>\n'
        '<script src="/lib/activity-sync.js"></script>\n')

# ============================================================== ASSEMBLE PROFESSOR
prof = (
    head('Professor View &mdash; Tânia Rosa | Aula 10 | Review and Confidence | Alumni by Better', PROF_CSS)
    + PROF_HEADER
    + AUDIT
    + TABS_PROF + '\n\n'
    + planning + '\n\n'
    + '<!-- ========== TAB 2: PRE-CLASS ========== -->\n'
    + '<div class="tab-content" id="tab-exercises">\n' + preclass + '\n</div>\n\n'
    + INCLASS_MENU + '\n\n'
    + '<!-- ========== TAB 4: COMPLEMENTARES ========== -->\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div>\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<!-- ============================== SLIDES WRAPPER (IN CLASS) ============================== -->\n'
    + '<div class="slides-wrapper">\n\n'
    + phasebar
    + '<div class="slides-container" id="slidesContainer">\n\n'
    + slides + '\n</div>\n</div>\n\n'
    + TAIL + '\n\n'
    + prof_js + '\n' + LIBS + '</body>\n</html>\n'
)

# ============================================================== ASSEMBLE ALUNO
aluno = (
    head('Aluno &mdash; Tânia Rosa | Aula 10 | Review and Confidence | Alumni by Better', ALUNO_CSS)
    + ALUNO_HEADER
    + '<div class="tabs-wrapper"><div class="tabs"><button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button><button class="tab-btn" onclick="switchTab(\'complementary\')">Complementares</button></div></div>\n'
    + '<div class="tab-content active" id="tab-exercises">\n' + preclass + '\n</div>\n\n'
    + '<div class="tab-content" id="tab-complementary">\n' + compl + '\n</div>\n\n'
    + '</div><!-- /container -->\n</div><!-- /main-content -->\n\n'
    + '<div class="confetti-container" id="confettiContainer"></div>\n\n'
    + aluno_js + '\n' + LIBS + '</body>\n</html>\n'
)

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(PHRASES, f, ensure_ascii=False, indent=2)

# ============================================================== AUDIO COVERAGE CHECK
def covered_keys():
    keys = set(p['key'] for p in PHRASES) | set(CALLBACK.keys())
    return keys

def used_phrases(html):
    used = set()
    for m in re.findall(r"speakText\('((?:[^'\\]|\\.)*)'", html):
        used.add(m.replace("\\'", "'").replace('\\\\', '\\'))
    for m in re.findall(r'data-phrase="([^"]+)"', html):
        used.add(m)
    return used

keys = covered_keys()
missing = set()
for fn, html in (('prof', prof), ('aluno', aluno)):
    for u in used_phrases(html):
        if u not in keys:
            missing.add(u)
if missing:
    print('!!! MISSING AUDIO for %d phrase(s):' % len(missing))
    for m in sorted(missing): print('   -', repr(m))
else:
    print('AUDIO COVERAGE OK — every speakText/data-phrase has an audioMap entry')

print('OK  N=%d slides' % N)
print('  professor:', PROF_OUT, len(prof), 'bytes')
print('  aluno    :', ALUNO_OUT, len(aluno), 'bytes')
print('  phrases to generate:', len(PHRASES))
