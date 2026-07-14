#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 2 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas e ZERO PORTUGUES na tela da aluna. Vocab card e
    matching levam DEFINICAO EM INGLES simples (nunca traducao). Grammar Tip, instrucoes,
    hints, quiz, survival e speech cards: tudo em ingles A2. O PT do professor
    (Planejamento / data-teacher) NAO vive neste arquivo.
  - REGRA 22: ZERO palavra da aula 1 como vocab NOVO (nada de results / launch /
    immunology / field team / global meeting / disease area / to manage...)
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 2 IN CLASS (mesma rotina, mesmo vocab,
    mesma gramatica: present simple + always/usually/often/sometimes/never)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be": a gramatica entra pela agenda REAL dela.
"""
import random

random.seed(2)

OUT = 'preclass.html'

# (word, definicao EN simples (a MESMA string usada no matching), exemplo)
VOCAB = [
    ("Schedule", "the plan of your week: what happens and when",
     "My schedule is full on Mondays."),
    ("Report", "a document with numbers and information about the business",
     "I read the field reports every Tuesday."),
    ("Field visit", "a day outside the office, with the team, visiting doctors",
     "I do a field visit twice a month."),
    ("Medical rep", "the person who talks to doctors about our medicines",
     "Every medical rep visits ten doctors a week."),
    ("Demand plan", "the plan that says how much medicine the market needs",
     "We review the demand plan every Monday."),
    ("Headquarters", "the main office of the company",
     "Our headquarters are in Paris."),
    ("To attend", "to go to a meeting or a call",
     "I attend the global call every Thursday."),
    ("To review", "to look at something again and check it",
     "I review the numbers before the meeting."),
    ("To prepare", "to get something ready before it happens",
     "I prepare the presentation on Fridays."),
    ("To travel", "to go to another city for work",
     "I sometimes travel to other cities."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-2">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 02 -- Pre-class</div>')
w('      <h3>Your Day and Your Work Routine -- A Week at Sanofi Brazil</h3>')
w('      <div class="lesson-desc">Describe your typical week to the Global team: Monday with the demand plan, '
  'the field visit, the global call on Thursday, the reports on Friday. Key words: schedule, report, field visit, '
  'medical rep, demand plan, headquarters, to attend, to review, to prepare, to travel. Structures: present simple '
  'for your routine + always / usually / often / sometimes / never (always BEFORE the verb), the negative '
  'I don&#39;t travel and the question Do you...? Expression of the lesson: "It is part of the job."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words that are in your week, every week.</p>')
w('      <div class="vocab-cards">')
for word, dfn, ex in VOCAB:
    w(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{dfn}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{word}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.2 (REGRA 24)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its definition.</p>')
w('      <div class="match-grid" id="match-l2">')
all_defs = [d for _, d, _ in VOCAB]
for word, dfn, _ex in VOCAB:
    opts = all_defs[:]
    while True:
        random.shuffle(opts)
        if opts != all_defs:
            break
    o = ''.join(f'<option value="{d}">{d}</option>' for d in opts)
    w(f'        <div class="match-row" data-answer="{dfn}">'
      f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
      f'<option value="">Select...</option>{o}</select></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.3
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>Emmanuele <strong>always starts</strong> her week with numbers. On Monday, she <strong>reviews</strong> the '
  '<strong>demand plan</strong> with her team and she <strong>checks</strong> the <strong>schedule</strong> for the week. '
  'On Tuesday, the <strong>medical reps</strong> <strong>usually send</strong> their <strong>reports</strong>. On Wednesday, '
  'she <strong>often does</strong> a <strong>field visit</strong> and <strong>visits</strong> doctors with a rep. On Thursday, '
  'she <strong>always attends</strong> the global call with <strong>headquarters</strong> in Paris. On Friday, she '
  '<strong>prepares</strong> the reports for the next week. She <strong>sometimes travels</strong> to other cities, but she '
  '<strong>never travels</strong> on Fridays. She <strong>does not schedule</strong> meetings on Friday, and she '
  '<strong>doesn&#39;t work</strong> at the weekend. "Monday is never quiet," she says. "<strong>It is part of the job</strong>."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why do we say "I always review" and not "I review always"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because always, usually, often, sometimes and never come BEFORE the main verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the frequency word always comes at the end of the sentence.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the action is happening now, at this moment.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "The medical reps usually send their reports." If the sentence is about ONE rep, what changes?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Nothing changes: "One rep usually send their reports."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The verb takes -s: "One rep usually sends his reports." (the same rule as my team visits, from lesson 1)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The verb goes to the past.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "She never travels on Fridays." What does this sentence say?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That she travels on some Fridays.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Zero Fridays: never = 0%. And note that the sentence does NOT take don&#39;t &mdash; never is already the negative.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she traveled last Friday.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her week is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She attend always the global call on Thursday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She always attends the global call on Thursday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She always attend the global call on Thursday."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Talking About Your Week: always, usually, often, sometimes, never</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to say WHAT you do and HOW OFTEN you do it.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I / we / they + <strong>always, usually, often, sometimes, never</strong> + verb</td>'
  '<td style="padding:.6rem">The frequency word comes BEFORE the verb, never after it.</td>'
  '<td style="padding:.6rem">I <strong>always review</strong> the demand plan.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">he / she / my team + verb <strong>+ s</strong></td>'
  '<td style="padding:.6rem">One person or one team: the verb takes -s (the same rule as lesson 1).</td>'
  '<td style="padding:.6rem">My team <strong>usually sends</strong> the reports.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative: I <strong>don&#39;t</strong> / she <strong>doesn&#39;t</strong> + verb</td>'
  '<td style="padding:.6rem">To say what is NOT in your week. Careful: with <strong>never</strong> you do not use don&#39;t (never is already the negative).</td>'
  '<td style="padding:.6rem">I <strong>don&#39;t travel</strong> on Fridays.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question: <strong>Do / Does</strong> + person + verb?</td>'
  '<td style="padding:.6rem">To ASK your colleague about his week (and not only to answer).</td>'
  '<td style="padding:.6rem"><strong>Do you travel</strong> every month?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">How often? / When?</td><td style="padding:.6rem" colspan="2">'
  'always (100%) &middot; usually &middot; often &middot; sometimes &middot; never (0%). Time expressions go at the start or at the end: '
  '<strong>every week</strong>, <strong>on Mondays</strong>, <strong>twice a month</strong>.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many Brazilian students say "I go always to the call", with the frequency word AFTER the verb. In English this sounds wrong. '
  'The place is always BEFORE the verb: <strong>I always go</strong>. And a question needs <strong>Do</strong> at the start: '
  '"Do you attend the call?", never only "You attend the call?".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("always review", "Hint: the frequency word (100%) comes before the verb",
     "On Monday, I always review the demand plan.",
     '"On Monday, I ', ' the demand plan."'),
    ("usually send", "Hint: they &mdash; verb with no -s, with the frequency word in front",
     "The medical reps usually send their reports on Tuesday.",
     '"The medical reps ', ' their reports on Tuesday."'),
    ("attend", "Hint: the verb for going to a meeting or a call",
     "I attend the global call every Thursday.",
     '"I ', ' the global call every Thursday."'),
    ("don't travel", "Hint: the negative after I &mdash; don&#39;t + verb",
     "I don't travel on Fridays.",
     '"I ', ' on Fridays."'),
    ("prepare", "Hint: to get something ready before it happens",
     "On Friday, I prepare the reports for the next week.",
     '"On Friday, I ', ' the reports for the next week."'),
    ("Do you attend", "Hint: a question in English starts with Do",
     "Do you attend the global call every week?",
     '"', ' the global call every week?"'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    w(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div>'
      f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 2 (order)
ORDER = [
    (1, "Monday: review the demand plan with the team."),
    (2, "Tuesday: read the field reports from the medical reps."),
    (3, "Wednesday: do a field visit and see doctors with a rep."),
    (4, "Thursday: attend the global call with headquarters in Paris."),
    (5, "Friday: prepare the reports for the next week."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Week in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the days of a typical week at Sanofi in the correct order.</p>')
w('      <div class="order-container" id="order-l2">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l2\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "On Monday, I always review the demand plan with my team.",
    "I often do a field visit with a medical rep.",
    "I attend the global call every Thursday.",
    "I sometimes travel, but I never travel on Fridays.",
    "It is part of the job.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. These five sentences answer the question: what does your week look like?</p>')
for en in SPEECH:
    w(f'      <div class="speech-card" data-phrase="{en}">')
    w(f'        <div class="speech-phrase">{en}</div>')
    w('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    w('        <div class="speech-result"></div>')
    w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 4 (quiz situacional)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each situation in a real meeting with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc asks: "What do you do on Mondays?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I review always the demand plan."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "On Monday, I always review the demand plan with my team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Monday I am review the demand plan."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "How often do you travel?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I travel sometimes, but Friday no."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I sometimes travel to other cities, but I never travel on Fridays."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I don&#39;t never travel on Fridays."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to talk about what your team does every week. Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "My team usually sends the field reports on Tuesday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "My team send usually the field reports on Tuesday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My team is send the field reports on Tuesday."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ASK Marc if he goes to the Monday call. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You attend the Monday call?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Attend you the Monday call?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Do you attend the Monday call?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">It was a busy week and someone from Global says that. The professional and natural answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, my work is very bad this week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Yes, it was a busy week. It is part of the job."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I am part of the job."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 90 seconds, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Marc Dubois asks you to describe your typical week at Sanofi. Start with "Every week, I..." and '
  'talk about five days: what you always do, what you usually do, what you often do, what you sometimes do, and what you never do. '
  'Use the words from this lesson (demand plan, field visit, medical rep, reports, global call, headquarters). Finish with the '
  'expression of the lesson: "It is part of the job." Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-2"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
SURVIVAL = [
    "On Monday, I always review the demand plan with my team.",
    "I often do a field visit with a medical rep.",
    "I attend the global call every Thursday.",
    "I sometimes travel, but I never travel on Fridays.",
    "It is part of the job.",
]
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 2</h4>')
for i, en in enumerate(SURVIVAL, 1):
    w(f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
      f'<span class="sp-en">{en}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
w('    </div>')
w('')
w('  </div>')
w('</div>')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {OUT} ({len(VOCAB)} vocab, {len(BLANKS)} blanks, {len(SPEECH)} speech cards)')
