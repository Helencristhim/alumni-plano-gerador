#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-2 do hub) da Lucimara — aula 2.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluna B1 => ZERO portugues na tela. Definicao em ingles simples no lugar da
traducao; matching = palavra EN <-> DEFINICAO EM INGLES; hints, enunciados, grammar tip,
quiz e survival card em ingles. Sem .speech-translation, sem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 2 IN CLASS (mesmo tema/gramatica/vocab).
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(2)  # deterministico

# (word, definicao EN — unica, usada no vocab card E como resposta do matching, exemplo)
VOCAB = [
    ("Terminal", "the part of the airport where you get on or off your plane",
     "My flight to New York leaves from Terminal 3."),
    ("Carry-on", "the small bag you take with you inside the plane",
     "I only travel with a carry-on when the trip is short."),
    ("Baggage claim", "the area where you pick up your suitcases after a flight",
     "Could you tell me where the baggage claim is?"),
    ("Check-in counter", "the desk where you show your ticket and leave your bags",
     "The check-in counter closes one hour before the flight."),
    ("Boarding pass", "the document that lets you get on the plane",
     "I've already downloaded my boarding pass."),
    ("Layover", "a short stop in another city between two flights",
     "I have a two-hour layover in Atlanta."),
    ("Customs", "the place where officers check what you are bringing into the country",
     "I haven't gone through customs yet."),
    ("Front desk", "the reception of a hotel, where you check in",
     "Please leave your bags at the front desk."),
    ("Concierge", "the hotel employee who helps guests with restaurants, taxis and tickets",
     "The concierge has already booked a table for us."),
    ("Itinerary", "the plan of your trip, with the dates, the flights and the hotels",
     "My itinerary says the fair starts at nine."),
    ("Confirmation number", "the code that proves you have a reservation",
     "I have my confirmation number here."),
    ("Jet lag", "the tired feeling after a long flight between time zones",
     "The jet lag always hits me at four in the morning."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-2">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 02 -- Pre-class</div>')
A('      <h3>Arriving and Settling In -- Airports, Hotels, and the First Hours in a New City</h3>')
A('      <div class="lesson-desc">Landing in New York, going through immigration and checking in at the hotel &mdash; '
  'the first hours, the ones nobody teaches you. Key words: terminal, carry-on, baggage claim, check-in counter, '
  'boarding pass, layover, customs, front desk, concierge, itinerary, confirmation number, jet lag. '
  'Structure: present perfect with <strong>just</strong> / <strong>already</strong> / <strong>yet</strong> '
  '("I&#8217;ve just landed", "I haven&#8217;t checked in yet") and the contrast with the past simple of the story '
  '("I landed at nine and took a cab").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Take your time &mdash; listen twice, then say it out loud. These are the twelve words of the first hours in any new city.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 13: word <-> English definition; REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the definition that explains it.</p>')
A('      <div class="match-grid" id="match-l2">')
defs = [v[1] for v in VOCAB]
assert len(set(defs)) == len(defs), 'as definicoes do matching precisam ser UNICAS'
for w, de, ex in VOCAB:
    opts = defs[:]
    while True:
        random.shuffle(opts)
        if opts != defs:
            break
    o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
    A(f'        <div class="match-row" data-answer="{de}"><span class="match-word" style="flex:0 0 150px">{w}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)"><option value="">Select...</option>{o}</select></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.3 — Grammar in Context ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text slowly, twice, and then answer the questions.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>It is nine fifteen at night at <strong>Terminal</strong> Four. Lucimara <strong>has just landed</strong> in New York. '
  'She <strong>landed</strong> at nine, <strong>walked</strong> to passport control and <strong>answered</strong> two questions: '
  '"Business or pleasure?" and "How long are you staying?" &mdash; that part <strong>is</strong> over, and the past simple '
  '<strong>tells</strong> the story. Now she <strong>is</strong> at <strong>baggage claim</strong>. Her suitcase '
  '<strong>has already arrived</strong> on belt six; her <strong>carry-on</strong> <strong>has never left</strong> her shoulder. '
  'She <strong>has not gone</strong> through <strong>customs</strong> <strong>yet</strong>, but she <strong>has</strong> nothing to '
  'declare. At the hotel, the <strong>front desk</strong> only <strong>needs</strong> her <strong>confirmation number</strong>, '
  'because she <strong>has already completed</strong> the online check-in. One problem: the room <strong>is not</strong> ready '
  '<strong>yet</strong>. So she <strong>leaves</strong> her bags, and the <strong>concierge</strong> '
  '<strong>recommends</strong> a small restaurant two blocks away. At eleven she <strong>is</strong> finally in her room. '
  'She <strong>has not unpacked</strong> <strong>yet</strong> &mdash; and she <strong>will not</strong> tonight. The '
  '<strong>jet lag</strong> <strong>is going</strong> to wake her at four in the morning, and her '
  '<strong>itinerary</strong> <strong>says</strong> the trade fair <strong>starts</strong> at nine.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "She <strong>has just landed</strong>." What does <strong>just</strong> add to the sentence?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> It happened a few minutes ago &mdash; very recently.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> It happened a long time ago and it is over.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It is going to happen in a few minutes.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "She <strong>has not gone</strong> through customs <strong>yet</strong>." What does this sentence say?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She has already gone through customs.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She has not gone through customs so far &mdash; but she still will. <strong>yet</strong> = up to now, not.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She will never go through customs.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. Why is "She <strong>landed</strong> at nine, <strong>walked</strong> to passport control and <strong>answered</strong> two questions" in the past simple, and not in the present perfect?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the action is still happening now.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because it is a SEQUENCE of finished actions, with the time said out loud (at nine) &mdash; it is a story.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the result now matters more than the moment.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct at the front desk?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have completed the online check-in yesterday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I\'ve already completed the online check-in, and I have my confirmation number here."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I already complete the online check-in yet."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Perfect with just / already / yet (and the contrast with the Past Simple)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Three small words that change everything.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Word</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">just<br>have + <strong>just</strong> + past participle</td><td style="padding:.6rem">It happened a few minutes ago. It goes BEFORE the past participle.</td><td style="padding:.6rem">I <strong>have just landed</strong>. (I&#8217;ve just landed.)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">already<br>have + <strong>already</strong> + past participle</td><td style="padding:.6rem">It is done &mdash; often earlier than expected. Affirmative sentences. It goes BEFORE the past participle.</td><td style="padding:.6rem">I <strong>have already completed</strong> the online check-in.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">yet<br>haven&#8217;t + past participle + <strong>yet</strong></td><td style="padding:.6rem">Not up to now (negative) or "so far?" (question). It always goes AT THE END of the sentence.</td><td style="padding:.6rem">I <strong>haven&#8217;t checked in yet</strong>. / <strong>Have</strong> you checked in <strong>yet</strong>?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">have / has + not + past participle. In speech: <strong>haven&#8217;t</strong> / <strong>hasn&#8217;t</strong>.</td><td style="padding:.6rem">My bag <strong>hasn&#8217;t arrived</strong> yet.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">Have + subject + past participle ... yet?</td><td style="padding:.6rem"><strong>Have you picked up</strong> your bags <strong>yet</strong>?</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">Past Simple<br>verb in the past</td><td style="padding:.6rem" colspan="2">When you SAY THE TIME or tell the sequence (a story), English needs the past simple: "I <strong>landed</strong> at nine and <strong>took</strong> a cab." NEVER "I have landed at nine."</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the two classic mistakes:</strong> (1) <strong>yet</strong> goes AT THE END: "I haven&#8217;t checked in <strong>yet</strong>", never "I haven&#8217;t yet checked in" in everyday speech. (2) With an explicit time or date, the present perfect is FORBIDDEN: "I <strong>landed</strong> at nine" (right) and not "I have landed at nine" (wrong). The practical rule: <em>when WHEN matters</em> &rarr; past simple; <em>when THE RESULT NOW matters</em> &rarr; present perfect.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("just", "Hint: it happened a few minutes ago -- it goes before the past participle",
     "I have just landed in New York.",
     '"I have ', ' landed in New York."'),
    ("already", "Hint: it is done, earlier than expected -- it goes before the past participle",
     "I have already completed the online check-in.",
     '"I have ', ' completed the online check-in."'),
    ("yet", "Hint: not up to now -- it goes at the END of the sentence",
     "I haven't checked in yet.",
     '"I haven\'t checked in ', '."'),
    ("hasn't", "Hint: the negative of has -- the bag has not arrived",
     "My bag hasn't arrived yet.",
     '"My bag ', ' arrived yet."'),
    ("landed", "Hint: the time is said out loud (at nine) -- past simple, never present perfect",
     "My flight landed at nine, and I took a cab to the hotel.",
     '"My flight ', ' at nine, and I took a cab to the hotel."'),
    ("confirmation number", "Hint: the code that proves you have a reservation",
     "Here is my confirmation number.",
     '"Here is my ', '."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence &mdash; as many times as you want.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering ----------
ORDER = [
    (4, "Take a taxi to the hotel and give the driver the address."),
    (2, "Pick up your suitcase at baggage claim, belt six."),
    (5, "At the front desk, give your name and your confirmation number."),
    (1, "Land at the terminal and answer the officer at passport control."),
    (3, "Go through customs -- green line if you have nothing to declare."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Arrival in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You have just landed in New York. Put the steps in the real order &mdash; from the runway to the hotel front desk.</p>')
A('      <div class="order-container" id="order-l2">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l2\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    "Excuse me, I have a reservation under the name Ito.",
    "I've just landed, and I haven't checked in yet.",
    "I've already completed the online check-in. Here is my confirmation number.",
    "Could you tell me where the baggage claim is?",
    "My flight landed at nine, and I took a cab straight to the hotel.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, say it out loud, and only then record. Pay attention to the linking: <em>I&#8217;ve just</em> sounds almost like one single word, and <em>haven&#8217;t</em> almost disappears in fast speech &mdash; that is exactly what swallows the sentence at the airport.</p>')
for en in SPEECH:
    A(f'      <div class="speech-card" data-phrase="{en}">')
    A(f'        <div class="speech-phrase">{en}</div>')
    A('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    A('        <div class="speech-result"></div>')
    A('      </div>')
A('    </div>')

# ---------- Stage 4 — Situational quiz ----------
QUIZ = [
    ("You get to the hotel front desk after a ten-hour flight. You say:",
     [("\"Excuse me, I have a reservation under the name Ito.\"", True),
      ("\"Hello, I want a room now, please.\"", False),
      ("\"I am Ito. Give me the key.\"", False)]),
    ("The receptionist asks: \"Have you checked in online yet?\" The best answer is:",
     [("\"Yes, I already complete it yet.\"", False),
      ("\"Yes, I've already completed the online check-in.\"", True),
      ("\"Yes, I have completed it at three o'clock yesterday.\"", False)]),
    ("You want to tell a colleague the story of your arrival, with the times and the sequence. Which one is correct?",
     [("\"I have landed at nine and I have taken a cab.\"", False),
      ("\"I landed at nine, took a cab, and got to the hotel at ten.\"", True),
      ("\"I land at nine and take a cab yesterday.\"", False)]),
    ("Your suitcase has not come out on the belt. You look for an employee and say:",
     [("\"My bag hasn't arrived yet. I've already waited twenty minutes at belt six.\"", True),
      ("\"My bag not arrive. Problem.\"", False),
      ("\"I don't have bag yet already.\"", False)]),
    ("It is nine at night and the room is not ready yet. The most effective reaction is:",
     [("Accept it in silence and wait standing in the lobby, without asking anything.", False),
      ("\"I understand. Could I leave my bags here and have a coffee while I wait?\"", True),
      ("Apologize for your English and give up the room.", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the first hours in New York.</p>')
for i, (q, opts) in enumerate(QUIZ, 1):
    A(f'      <div class="quiz-item"><div class="quiz-question">{q}</div><div class="quiz-options">')
    for letter, (txt, ok) in zip('ABC', opts):
        A(f'        <div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(ok).lower()}">'
          f'<span class="option-letter">{letter}</span> {txt}</div>')
    A('      </div></div>')
A('    </div>')

# ---------- Stage 5 — Free production ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 90 seconds, with no script.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">It is your first night in New York. You have just arrived at the hotel and the room is not ready yet. Tell the story of your arrival: what time your flight landed, what you did at passport control and at baggage claim (past simple), and what you have already done and what you have not done yet (present perfect with just / already / yet). Finish by asking the front desk two questions. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-2"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 2</h4>')
for i, en in enumerate(SPEECH, 1):
    A(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
A('    </div>')

A('')
A('  </div>')
A('</div>')

html = '\n'.join(p) + '\n'
open(OUT, 'w', encoding='utf-8').write(html)
print(f'preclass.html: {len(html)//1024} KB | vocab={len(VOCAB)} match={len(VOCAB)} '
      f'quiz={len(QUIZ)+4} blanks={len(BLANKS)} speech={len(SPEECH)} order=1 think=1 '
      f'| divs {html.count("<div")}/{html.count("</div>")}')
