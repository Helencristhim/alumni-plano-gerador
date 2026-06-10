#!/usr/bin/env python3
"""Assemble Rafael Gasparelli Lima — Aula 6 (Review) standalone professor + aluno files.
Scaffold = public/professor/rafael-gasparelli-lima.html (CSS + JS copied verbatim, REGRA 34)."""
import os, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SCAFFOLD = os.path.join(ROOT, 'public', 'professor', 'rafael-gasparelli-lima.html')
SLUG = 'rafael-gasparelli-lima'

scaffold = open(SCAFFOLD, encoding='utf-8').read()
slides6 = open(os.path.join(HERE, 'slides6.html'), encoding='utf-8').read()
preclass6 = open(os.path.join(HERE, 'preclass6.html'), encoding='utf-8').read()
complementary6 = open(os.path.join(HERE, 'complementary6.html'), encoding='utf-8').read()
phrases = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))

# ---- audioMap from phrases.json ----
def audiomap_js():
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        v = json.dumps('/audio/%s/%s' % (SLUG, p['file']), ensure_ascii=False)
        lines.append('  %s: %s' % (k, v))
    return '<script>\nvar audioMap = {\n' + ',\n'.join(lines) + '\n};\n</script>'

# ---- HEAD (verbatim from scaffold, swap audioMap) ----
body_idx = scaffold.index('<body>')
head = scaffold[:body_idx]
am_start = head.index('<script>')
am_end = head.index('</script>', am_start) + len('</script>')
head = head[:am_start] + audiomap_js() + head[am_end:]

# ---- MAIN JS (verbatim, patched) ----
js_start = scaffold.index('<script>', body_idx)
js_end = scaffold.index('</script>', js_start) + len('</script>')
mainjs = scaffold[js_start:js_end]
# single-lesson progress
mainjs = mainjs.replace('var totalLessons = 5;', 'var totalLessons = 1; var lessonNums = [6];')
mainjs = mainjs.replace('for (var l = 1; l <= totalLessons; l++) {',
                        'for (var li = 0; li < lessonNums.length; li++) { var l = lessonNums[li];')
assert 'var lessonNums = [6];' in mainjs, 'totalLessons patch failed'
assert 'var l = lessonNums[li];' in mainjs, 'loop patch failed'

# ---- dialogue6 + quick fire data injected before </script> ----
INJECT = r'''
// ===== AULA 6 DATA (REVIEW) =====
dialogueLines['dialogue6'] = [
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'Good morning, Rafael. Thank you for inviting me to your <span class="vocab-highlight">headquarters</span>.'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'Good morning, Sarah. Pleased to meet you in person. Welcome to <span class="vocab-highlight">Grupo Picunha</span>.'},
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'<span class="vocab-highlight">Could</span> you tell me a little about the company?'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'Of course. We <span class="vocab-highlight">operate</span> in two industries: iron manufacturing and agriculture. Our <span class="vocab-highlight">revenue</span> comes from both divisions.'},
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'Impressive. What does a typical day look like for you?'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'I <span class="vocab-highlight">usually</span> wake up early, take my son to school, and then I attend meetings all morning. I <span class="vocab-highlight">rarely</span> have a free hour before lunch.'},
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'I understand. <span class="vocab-highlight">Can</span> we arrange a short meeting with your legal team this afternoon?'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'Of course. <span class="vocab-highlight">Could</span> you send me the topics by email? Then I will prepare the room.'},
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'Perfect. Is there a <span class="vocab-highlight">conference room</span> near your office?'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'Yes, <span class="vocab-highlight">there is</span>. There is a conference room next to my office on the fifth floor, and <span class="vocab-highlight">there are</span> three meeting rooms on this floor.'},
  {avatar:'sarah',cls:'sarah-bubble',voice:'ellen',text:'Wonderful. Is there a <span class="vocab-highlight">parking lot</span> for visitors?'},
  {avatar:'rafael',cls:'rafael-bubble',voice:'arthur',text:'Yes, there is a large parking lot behind the building. Let me show you around.'}
];
qfData[11] = [
  {q:'A partner asks: "What does your company do?" Your answer:', a:'"We operate in two industries: iron manufacturing and agriculture. Our revenue comes from both divisions."'},
  {q:'Someone asks: "Where is your headquarters?" Your answer:', a:'"Our headquarters is in São Paulo, Brazil."'},
  {q:'A colleague asks: "What do you usually do before work?" Your answer:', a:'"I usually wake up early, take my son to school, and train jiu-jitsu."'},
  {q:'You want to politely ask a partner to send the meeting topics. What do you say?', a:'"Could you send me the topics by email, please?"'},
  {q:'A visitor asks: "Is there a conference room on your floor?" Your answer:', a:'"Yes, there is. There is a conference room next to my office on the fifth floor."'},
  {q:'Someone asks: "How often do you work overtime?" Your answer:', a:'"I rarely work overtime, and I never work on weekends."'}
];
qfData[12] = [
  {q:'A visitor asks: "Is there a parking lot?" Your answer:', a:'"Yes, there is. There is a large parking lot behind the building."'},
  {q:'A partner asks: "How many meeting rooms are there on your floor?" Your answer:', a:'"There are three meeting rooms on my floor."'},
  {q:'You want to arrange a meeting for the afternoon. What do you say?', a:'"Can we arrange a meeting for this afternoon?"'},
  {q:'Someone asks: "Does your company have subsidiaries?" Your answer:', a:'"Yes, we have subsidiaries in agriculture and iron manufacturing."'},
  {q:'A partner asks: "What is your role?" Your answer:', a:'"I am a director, and I manage the legal department."'},
  {q:'You did not understand a fast speaker. What do you say?', a:'"Could you repeat that, please?"'}
];
qfIndex[11] = 0; qfIndex[12] = 0; qfCorrect[11] = 0; qfCorrect[12] = 0;
'''
mainjs = mainjs[:-len('</script>')] + INJECT + '</script>'

def patch_storage(js, suffix):
    js = js.replace("'%s-professor'" % SLUG, "'%s-aula6-%s'" % (SLUG, suffix))
    js = js.replace("'alumni-progress-%s'" % SLUG, "'alumni-progress-%s-aula6'" % SLUG)
    return js

# ---- PLANNING tab (verbatim from scaffold) ----
pl_start = scaffold.index('<div class="tab-content active" id="tab-planning">')
pl_end = scaffold.index('</div><!-- /tab-planning -->') + len('</div><!-- /tab-planning -->')
planning = scaffold[pl_start:pl_end]

# ---- WELCOME card (verbatim from scaffold) ----
wc_start = scaffold.index('<!-- WELCOME CARD -->')
wc_end = scaffold.index('<!-- LESSON 1 CARD -->')
welcome = scaffold[wc_start:wc_end].rstrip()

SCENARIO_FIT = '''<!-- SCENARIO FIT — Aula 6
Can-do: "I can introduce myself, describe my company and routine, make polite requests, and describe my office — in one conversation."
Gramatica-alvo (revisao): Present Simple, frequency adverbs, Can/Could (requests), There is/There are + prepositions.
Vocab-alvo (revisao, das aulas 1-5): headquarters, subsidiary, revenue, partnership, schedule, commute, conference room, parking lot.
Cenario escolhido: Rafael recebe uma parceira internacional (Sarah) na sede para uma visita de um dia.
Por que elicita o alvo: receber a visita obriga a apresentar-se e descrever a empresa (L1/L2), falar da rotina/agenda (L3), fazer pedidos educados para marcar reuniao (L4) e dar um tour do escritorio com There is/are (L5). Aderencia >= 90%.
-->
<!-- CONTINUIDADE — Aula 6
Itens novos desta aula: NENHUM (aula de revisao e consolidacao — REGRA 37; nada reintroduzido como novo).
Itens revisados (aulas 1-5): present simple, 3a pessoa -s, frequency adverbs, can/could, there is/are, prepositions; vocab de empresa/rotina/escritorio.
Callback no warm-up: slide 2 retoma Lesson 4 (apresentar-se) e Lesson 5 (descrever o escritorio com There is/There are) — o aluno USA, nao so reconhece.
-->
'''

# ---- IN CLASS menu (single card, REGRA 34 standalone) ----
inclass_menu = '''<div class="tab-content" id="tab-inclass">

<div class="inclass-lesson-card" onclick="startLesson(6)">
  <div class="ilc-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON 06 — 60 MINUTES</div>
    <div class="ilc-title">Putting It All Together</div>
    <div class="ilc-desc">Review &amp; Consolidation — Lessons 1-5 — 27 slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</div>

</div><!-- /tab-inclass -->'''

slides_wrapper = '''<div class="slides-wrapper">
  <div class="phase-bar">
    <div class="phase-segment current" data-phase="1"></div>
    <div class="phase-segment upcoming" data-phase="2"></div>
    <div class="phase-segment upcoming" data-phase="3"></div>
    <div class="phase-segment upcoming" data-phase="4"></div>
    <div class="phase-segment upcoming" data-phase="5"></div>
    <div class="phase-segment upcoming" data-phase="6"></div>
    <div class="phase-segment upcoming" data-phase="7"></div>
  </div>
  <div class="phase-labels">
    <div class="phase-label current" data-phase="1">The Dream</div>
    <div class="phase-label" data-phase="2">Packing Words</div>
    <div class="phase-label" data-phase="3">The Code</div>
    <div class="phase-label" data-phase="4">Getting There</div>
    <div class="phase-label" data-phase="5">Practice</div>
    <div class="phase-label" data-phase="6">Your Turn</div>
    <div class="phase-label" data-phase="7">Wrap-up</div>
  </div>

  <div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

  <div class="slides-container">

''' + slides6 + '''

  </div><!-- /slides-container -->

  <!-- NAV BAR -->
  <div class="nav-bar">
    <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
    <div class="slide-dots" id="slideDots"></div>
    <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></button>
  </div>

</div><!-- /slides-wrapper -->'''

SUPA_TAIL = '''<script src="/lib/lesson-progress.js"></script>
<script src="/lib/controle-aulas.js"></script>
<script src="/lib/activity-sync.js"></script>'''

SPEED = '''<div class="speed-control">
  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
</div>'''

def header_hero(badge):
    return '''<div class="header" style="background-image:url('https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=1400&q=80')">
  <div class="header-content">
    <div class="passport-badge">BUSINESS &amp; LEGAL ENGLISH — Aula 6 — Review</div>
    <h1>Rafael Gasparello Lima</h1>
    <p class="subtitle">Review &amp; Consolidation — Lessons 1-5</p>
    <div class="student-info">
      <span>São Paulo, SP</span><span>A2</span><span>Advogado / Diretor</span><span>60 min</span><span>Online</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label"><span>PROGRESS</span><span id="progressPercent">0%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
    </div>
  </div>
</div>'''

# ============ PROFESSOR ============
prof_logo = '''<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">PROFESSOR VIEW</span>
  <select class="lesson-selector" id="lessonSelector" onchange="startLesson(parseInt(this.value))" aria-label="Selecionar aula">
    <option value="6">Aula 6</option>
  </select>
  <span class="slide-counter" id="slideCounter">01 / 27</span>
</div>'''

prof_body = '\n'.join([
  '<body>', SCENARIO_FIT, prof_logo, header_hero('PROFESSOR VIEW'),
  '<div class="main-content">', '<div class="container">', SPEED,
  '''<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
  <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
  <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
  <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
</div>''',
  planning,
  '<div class="tab-content" id="tab-exercises">', welcome, preclass6, '</div><!-- /tab-exercises -->',
  inclass_menu,
  '<div class="tab-content" id="tab-complementary">', complementary6, '</div><!-- /tab-complementary -->',
  '</div><!-- /container -->', '</div><!-- /main-content -->',
  slides_wrapper,
  '<div class="confetti-container" id="confettiContainer"></div>',
  patch_storage(mainjs, 'professor'),
  SUPA_TAIL,
  '</body>', '</html>',
])
prof = head + prof_body

# ============ ALUNO (2 tabs: Pre-class + Complementares) ============
aluno_head = head.replace('Professor View', 'Aluno').replace('— Professor', '— Aluno')
aluno_logo = '''<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">ALUNO</span>
</div>'''
aluno_body = '\n'.join([
  '<body>', aluno_logo, header_hero('ALUNO'),
  '<div class="main-content">', '<div class="container">', SPEED,
  '''<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('exercises')">Pre-class</button>
  <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
</div>''',
  '<div class="tab-content active" id="tab-exercises">', welcome, preclass6, '</div><!-- /tab-exercises -->',
  '<div class="tab-content" id="tab-complementary">', complementary6, '</div><!-- /tab-complementary -->',
  '</div><!-- /container -->', '</div><!-- /main-content -->',
  '<div class="confetti-container" id="confettiContainer"></div>',
  patch_storage(mainjs, 'aluno'),
  SUPA_TAIL,
  '</body>', '</html>',
])
aluno = aluno_head + aluno_body

prof_path = os.path.join(ROOT, 'public', 'professor', '%s-aula6.html' % SLUG)
aluno_path = os.path.join(ROOT, 'public', 'aluno', '%s-aula6.html' % SLUG)
open(prof_path, 'w', encoding='utf-8').write(prof)
open(aluno_path, 'w', encoding='utf-8').write(aluno)
print('WROTE:', prof_path, '(%d bytes)' % len(prof))
print('WROTE:', aluno_path, '(%d bytes)' % len(aluno))
print('slides:', len(re.findall(r'data-slide="', slides6)), 'data-teacher:', len(re.findall(r'data-teacher=', slides6)))
