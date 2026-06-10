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
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'tania-rosa-aula8.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'tania-rosa-aula8.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'tania-rosa-aula9.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'tania-rosa-aula9.html')

AUDIO_DIR = '/audio/tania-rosa-aula9/'

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

# (text, voice). file derived from snake(text).
GEN = [
    # --- vocab words (8 new) — learner female = ellen ---
    ("Relatives", "ellen"), ("Grandparents", "ellen"), ("Cousin", "ellen"),
    ("Niece", "ellen"), ("Nephew", "ellen"), ("Schedule", "ellen"),
    ("Sightseeing", "ellen"), ("Itinerary", "ellen"),
    # --- pre-class fill-in-the-blank data-phrase + speech + survival (student=ellen) ---
    ("Let's visit our grandparents this summer.", "ellen"),
    ("Shall we go sightseeing on Sunday?", "ellen"),
    ("Why don't we book the hotel today?", "ellen"),
    ("How about visiting the museum?", "ellen"),
    ("Let's plan the itinerary together.", "ellen"),
    ("Shall we invite all our relatives?", "ellen"),
    ("Let's plan our family trip together.", "ellen"),
    ("Why don't we visit our grandparents?", "ellen"),
    ("How about going sightseeing on Sunday?", "ellen"),
    ("Let's check the schedule and book the hotel.", "ellen"),
    ("Shall we go sightseeing tomorrow?", "ellen"),
    ("How about planning the itinerary together?", "ellen"),
    # --- dialogue (Tania=ellen, Sofia=rachel) ---
    ("Sofia, let's plan our family trip to the coast.", "ellen"),
    ("Great idea! Shall we invite our cousins too?", "rachel"),
    ("Yes, let's invite all our relatives. How about visiting our grandparents on the way?", "ellen"),
    ("Perfect. Why don't we book the hotel this week?", "rachel"),
    ("Good plan. Let's check the schedule for the flights.", "ellen"),
    ("Shall we go sightseeing when we arrive?", "rachel"),
    ("Of course. My niece and nephew love the beach.", "ellen"),
    ("Then let's plan the itinerary together tonight.", "rachel"),
    ("How about making a list of activities for everyone?", "ellen"),
    ("Let's do it. This trip will be wonderful for the whole family.", "rachel"),
    # --- listening 1 (phone call) — listening 2 reuses a subset of these ---
    ("Hi Sofia, let's talk about the family trip.", "ellen"),
    ("Sure! Shall we go in July or August?", "rachel"),
    ("Let's go in July. How about a week at the beach?", "ellen"),
    ("Why don't we bring our parents and grandparents?", "rachel"),
    ("Yes, and let's invite our cousins, nieces, and nephews.", "ellen"),
    ("Shall we book two big rooms for everyone?", "rachel"),
    ("Good idea. Let's check the schedule and plan the itinerary.", "ellen"),
    ("Let's make this a trip the whole family remembers.", "rachel"),
    # --- order sequence (single mp3, ellen) ---
    ("[ORDER]Let's plan our family trip. Shall we invite our relatives? Why don't we book the hotel? Let's check the schedule. How about going sightseeing?", "ellen"),
]

PHRASES = []
seen = set()
for text, voice in GEN:
    if text in seen:
        continue
    seen.add(text)
    if text.startswith("[ORDER]"):
        PHRASES.append({"text": text[7:], "file": "order_l9_ordering.mp3", "voice": voice, "key": "[order-l9]"})
    else:
        PHRASES.append({"text": text, "file": snake(text) + ".mp3", "voice": voice, "key": text})

# callback audio (re-uses existing aula8 mp3s — NOT regenerated)
CALLBACK = {
    "Insurance": "/audio/tania-rosa-aula8/insurance.mp3",
    "Pharmacy": "/audio/tania-rosa-aula8/pharmacy.mp3",
    "I need to see a doctor.": "/audio/tania-rosa-aula8/i_need_to_see_a_doctor.mp3",
    "You have to take this medicine twice a day.": "/audio/tania-rosa-aula8/you_have_to_take_this_medicine_twice_a_day.mp3",
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
    "{prompt:'Suggest visiting your grandparents this weekend.',answer:'\"Let\\'s visit our grandparents this weekend.\"'},"
    "{prompt:'Ask your sister if you should go sightseeing.',answer:'\"Shall we go sightseeing on Sunday?\"'},"
    "{prompt:'Suggest booking the hotel today.',answer:'\"Why don\\'t we book the hotel today?\"'},"
    "{prompt:'Suggest visiting the museum with the family.',answer:'\"How about visiting the museum together?\"'},"
    "{prompt:'Suggest inviting all the relatives.',answer:'\"Let\\'s invite all our relatives.\"'},"
    "{prompt:'Suggest planning the itinerary tonight.',answer:'\"Shall we plan the itinerary tonight?\"'}"
    "];")
prof_js = re.sub(r'var challenges=\[.*?\];', new_challenges, prof_js, count=1, flags=re.S)
assert new_challenges in prof_js, 'challenges swap failed'

# helper: build JS array literal with single-quoted strings (apostrophes -> \')
def js_arr(items):
    return 'var lines=[' + ','.join("'%s'" % s.replace("\\", "\\\\").replace("'", "\\'") for s in items) + '];'

# listening 1 lines (phone call)
L1 = ["Hi Sofia, let's talk about the family trip.",
      "Sure! Shall we go in July or August?",
      "Let's go in July. How about a week at the beach?",
      "Why don't we bring our parents and grandparents?",
      "Yes, and let's invite our cousins, nieces, and nephews.",
      "Shall we book two big rooms for everyone?",
      "Good idea. Let's check the schedule and plan the itinerary.",
      "Let's make this a trip the whole family remembers."]
l1_js = js_arr(L1)

# listening 2 lines (focus on suggestions — subset reuse)
L2 = ["Sure! Shall we go in July or August?",
      "Let's go in July. How about a week at the beach?",
      "Why don't we bring our parents and grandparents?",
      "Shall we book two big rooms for everyone?",
      "Good idea. Let's check the schedule and plan the itinerary."]
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
prof_js = prof_js.replace('alumni-progress-tania-rosa-aula8', 'alumni-progress-tania-rosa-aula9')
prof_js = prof_js.replace("'tania-rosa-aula8-professor'", "'tania-rosa-aula9-professor'")

aluno_js = ALUNO_JS_RAW
aluno_js = aluno_js.replace('alumni-progress-tania-rosa-aula8', 'alumni-progress-tania-rosa-aula9')
aluno_js = aluno_js.replace("'tania-rosa-aula8-aluno'", "'tania-rosa-aula9-aluno'")

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
      <div class="progress-label"><span>Aula 9 — Family Travel</span><span id="progressPercent">0%</span></div>
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
    <div class="progress-passport"><div class="progress-label"><span>Aula 9 — Family Travel</span><span id="progressPercent">0%</span></div><div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
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
# promise box -> Aula 9
planning = planning.replace('Promessa da Aula 8',
                            'Promessa da Aula 9')
planning = planning.replace(
    'After this lesson, Tânia will confidently handle any emergency abroad — ask for help, describe symptoms, and communicate with doctors and pharmacists in English.',
    'After this lesson, Tânia will confidently coordinate a family trip in English — make suggestions, plan activities, and organize the itinerary with relatives using <em>let’s</em>, <em>shall we</em>, <em>why don’t we</em>, and <em>how about</em>.')
# move highlighted row 8 -> row 9
planning = planning.replace(
    '<tr style="background:rgba(156,70,104,.08)"><td><strong>8</strong></td><td><strong>Emergency Situations — Health, Safety, and Asking for Help</strong></td><td><strong>Need to / Have to for obligations and necessities</strong></td><td><strong>Pharmacy role-play + Emergency card</strong></td><td><strong>Create personal emergency phrase card</strong></td></tr>',
    '<tr><td>8</td><td>Emergency Situations — Health, Safety, and Asking for Help</td><td>Need to / Have to for obligations and necessities</td><td>Pharmacy role-play + Emergency card</td><td>Create personal emergency phrase card</td></tr>')
planning = planning.replace(
    '<tr><td>9</td><td>Family Travel — Coordinating with Family</td><td>Suggestions (let us, shall we), family vocabulary</td><td>Family trip planning role-play</td><td>Record 1-min about favorite family trip</td></tr>',
    '<tr style="background:rgba(156,70,104,.08)"><td><strong>9</strong></td><td><strong>Family Travel — Coordinating with Family</strong></td><td><strong>Suggestions (let’s, shall we, why don’t we, how about), family vocabulary</strong></td><td><strong>Family trip planning role-play</strong></td><td><strong>Record 1-min about favorite family trip</strong></td></tr>')
assert 'Promessa da Aula 9' in planning, 'planning promise swap failed'
assert planning.count('background:rgba(156,70,104,.08)"><td><strong>9</strong>') == 1, 'row9 highlight failed'

# ============================================================== FRAGMENTS
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phasebar = prof_scaffold[prof_scaffold.index('<div class="phase-bar" id="phaseBar">'):prof_scaffold.index('<div class="slides-container" id="slidesContainer">')]
slides   = read(os.path.join(HERE, 'slides.html'))

N = len(re.findall(r'data-slide="\d+"', slides))
assert N == 37, 'expected 37 slides, got %d' % N

AUDIT = '''<!--
SCENARIO FIT — Aula 9
Can-do: "I can coordinate a family trip and make suggestions using let's, shall we, why don't we, and how about."
Gramatica-alvo: suggestions — Let's + base verb; Shall we + base verb?; Why don't we + base verb?; How about + verb-ing
Vocab-alvo: relatives, grandparents, cousin, niece, nephew, schedule, sightseeing, itinerary
Cenario escolhido: duas irmas (Tania e Sofia) planejando uma viagem em familia para a costa.
Por que elicita o alvo: planejar uma viagem JUNTO obriga o aluno a SUGERIR atividades e destinos ("Let's visit our grandparents", "Shall we go sightseeing?", "Why don't we book the hotel?", "How about visiting the museum?") e a nomear os familiares que vao (cousins, nieces, nephews, grandparents). >70% dos itens-alvo sao naturalmente elicitados.

CONTINUIDADE — Aula 9
Itens novos desta aula: relatives, grandparents, cousin, niece, nephew, schedule, sightseeing, itinerary; suggestions (let's / shall we / why don't we / how about).
Itens revisados (de aulas anteriores): need to / have to (Aula 8), insurance + pharmacy (Aula 8), would like / could I have (aulas 3 e 5), been to (Aula 7).
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 8 — o aluno USA "need to" / "have to" e as palavras insurance/pharmacy para preparar a viagem ("Before the trip you need to buy travel insurance" / "You have to find a pharmacy near the hotel"), fazendo a ponte emergencias -> agora planejar a viagem em familia.
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
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>
      <div><div style="font-weight:600;font-size:.95rem">Family Travel</div><div style="font-size:.8rem;color:var(--text-dim)">Coordinating with Family — 37 slides</div></div>
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
    head('Professor View &mdash; Tânia Rosa | Aula 9 | Family Travel | Alumni by Better', PROF_CSS)
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
    head('Aluno &mdash; Tânia Rosa | Aula 9 | Family Travel | Alumni by Better', ALUNO_CSS)
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
