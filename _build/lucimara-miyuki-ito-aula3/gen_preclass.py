#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-3 do hub) da Lucimara — aula 3.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluna B1 => ZERO portugues na tela. Vocab card = definicao EN, matching =
palavra EN <-> definicao EN, grammar tip em ingles, hints "Hint: ...", speech card sem
traducao, survival card sem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 3 IN CLASS (mesmo tema/gramatica/vocab).
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(3)  # deterministico

# (word, definicao EN, exemplo)
# A definicao EN e a MESMA string usada no vocab card e no matching (data-answer/option).
VOCAB = [
    ("Fare", "the money you pay for a ride in a taxi, a bus or the subway",
     "How much is the fare to the Upper West Side?"),
    ("Tip", "extra money you leave for the person who served you",
     "In New York, twenty percent is the normal tip at a restaurant."),
    ("Block", "the distance from one street corner to the next one",
     "The subway station is three blocks from the hotel."),
    ("Subway line", "one train route in the subway, with a number or a letter",
     "Take the 1 line uptown and get off at 79th Street."),
    ("Diner", "a simple American restaurant that serves breakfast all day",
     "We had lunch at a diner on Ninth Avenue."),
    ("To-go order", "food you take with you instead of eating it at the table",
     "I'm in a hurry -- could you make it a to-go order?"),
    ("Sales tax", "the extra percentage added to the price when you pay at the register",
     "The price on the tag doesn't include sales tax."),
    ("Fitting room", "the small room in a store where you put the clothes on to see if they fit",
     "Could I try this on? Where is the fitting room?"),
    ("Receipt", "the paper that proves you paid -- the P is silent",
     "Could I have a receipt, please?"),
    ("Rush hour", "the time of day when the trains and the streets are full of people",
     "Don't take the subway at rush hour with a suitcase."),
    ("To hail (a cab)", "to raise your hand in the street to stop a taxi",
     "She hailed a cab on Fifth Avenue and gave the driver the address."),
    ("To figure out", "to understand something after some effort -- not immediately",
     "It took me ten minutes to figure out the subway map."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-3">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1514565131-fce0801e5785?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 03 -- Pre-class</div>')
A('      <h3>Getting Around and Getting Things Done -- Taxis, Subways, Restaurants, and Shops</h3>')
A('      <div class="lesson-desc">The city in motion: a cab on Fifth Avenue, the subway at rush hour, lunch at a diner, '
  'and a store where the price at the register is not the price on the tag. Key words: fare, tip, block, subway line, '
  'diner, to-go order, sales tax, fitting room, receipt, rush hour, to hail a cab, to figure out. '
  'Structure: <strong>past simple</strong> vs. <strong>present perfect</strong> in the travel story '
  '("When I <strong>went</strong> to New York in 2023, I <strong>took</strong> a cab everywhere -- but this time '
  "I<strong>'ve already used</strong> the subway twice\").</div>")
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Take your time &mdash; listen twice, then say it out loud. These are the twelve words you use with money in your hand: the taxi, the subway, the check at the restaurant, and the register at the store.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    speak = w.replace('(', '').replace(')', '')
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{speak}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 13: word EN <-> definicao EN; REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the definition that explains it.</p>')
A('      <div class="match-grid" id="match-l3">')
defs = [v[1] for v in VOCAB]
assert len(set(defs)) == len(defs), 'definicoes do matching precisam ser UNICAS'
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text calmly, twice, and then answer the questions.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>When Lucimara <strong>went</strong> to New York in 2023, she <strong>took</strong> a cab everywhere. '
  'She <strong>hailed</strong> one outside the hotel every morning, she <strong>paid</strong> the '
  '<strong>fare</strong> in cash, and she never <strong>asked</strong> for a <strong>receipt</strong>. '
  'That trip <strong>is</strong> closed: it <strong>has</strong> a date, so English <strong>uses</strong> the '
  'past simple.</p>')
A('        <p style="margin-top:.8rem">This time is different, and the trip <strong>is not over</strong>. She '
  '<strong>has already used</strong> the subway twice: the 1 <strong>line</strong>, uptown, three '
  '<strong>blocks</strong> from the hotel. She <strong>has never taken</strong> it at '
  '<strong>rush hour</strong>, and honestly she <strong>has not figured out</strong> the map yet. Yesterday she '
  '<strong>had</strong> lunch at a <strong>diner</strong> on Ninth Avenue and <strong>left</strong> a twenty '
  'percent <strong>tip</strong> &mdash; that <strong>happened</strong>, it <strong>has</strong> a day, so: past '
  'simple again. But this afternoon, on Fifth Avenue, she <strong>has already tried on</strong> a coat in the '
  '<strong>fitting room</strong>, and at the register she <strong>learned</strong> the New York lesson: the '
  'price on the tag <strong>is not</strong> the price you pay, because of the <strong>sales tax</strong>.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Why is "she <strong>went</strong> to New York in 2023" in the past simple, and not in the present perfect?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the trip is still happening.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the sentence GIVES THE DATE (in 2023) &mdash; the trip is closed. With an explicit date, English needs the past simple.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the result matters more than the moment.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "She <strong>has already used</strong> the subway twice." What does <strong>already</strong> + present perfect tell you here?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The trip is STILL OPEN &mdash; and so far she has used the subway twice. The number can still go up.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> She used the subway twice in 2023.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She is going to use the subway twice tomorrow.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "She <strong>has never taken</strong> it at rush hour." Why <strong>taken</strong>, and not <strong>took</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because <strong>took</strong> only exists in British English.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because both forms are correct &mdash; it makes no difference.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because after <strong>have / has</strong> the verb changes form: the past participle. take &rarr; <strong>taken</strong>, go &rarr; <strong>gone</strong>, eat &rarr; <strong>eaten</strong>.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have gone to New York in 2023 and I have took a cab."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I went to New York in 2023 and I took a cab &mdash; but this time I\'ve already used the subway."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I go to New York in 2023 and I have already take the subway."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Past Simple vs. Present Perfect (the travel story)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two trips, two tenses. One question tells you which one to use.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Tense</th><th style="padding:.7rem;text-align:left">When you use it</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Past Simple<br>went &middot; took &middot; paid</td><td style="padding:.6rem">A CLOSED moment. You say WHEN it happened (in 2023, last night, yesterday, ten minutes ago), or you tell the sequence of a story.</td><td style="padding:.6rem">"When I <strong>went</strong> to New York in 2023, I <strong>took</strong> a cab everywhere."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + past participle</td><td style="padding:.6rem">The trip is still OPEN, or the experience covers your whole life. The moment does NOT matter. Signal words: already, never, ever, so far, this time, twice.</td><td style="padding:.6rem">"This time I<strong>\'ve already used</strong> the subway twice."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">have / has + not + past participle. In speech: <strong>haven\'t</strong> / <strong>hasn\'t</strong>.</td><td style="padding:.6rem">"I <strong>haven\'t figured out</strong> the subway map yet."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">Have + subject + <strong>ever</strong> + past participle? (= at any time in your life)</td><td style="padding:.6rem">"<strong>Have you ever tried</strong> a New York diner?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">THE PAST PARTICIPLE<br>(the piece that trips you up)</td><td style="padding:.6rem" colspan="2">After <strong>have / has</strong>, the verb CHANGES FORM: take &rarr; <strong>taken</strong> (never "have took"), go &rarr; <strong>gone</strong>, eat &rarr; <strong>eaten</strong>, pay &rarr; <strong>paid</strong>, buy &rarr; <strong>bought</strong>, do &rarr; <strong>done</strong>.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">The one test</td><td style="padding:.6rem" colspan="2">Ask yourself ONE question: <strong>can this number still change today?</strong> If it can &rarr; present perfect. If it is closed and it has a date &rarr; past simple. 2023 is closed. September is still open.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> (1) An explicit date with the present perfect is IMPOSSIBLE: the moment you say <em>in 2023</em>, the verb has to go back to the past simple &mdash; "I <strong>went</strong>", never "I have gone... in 2023". (2) The wrong participle after <em>have</em>: "I have never <strong>took</strong>" is the mistake that gives your level away. The correct form is "I have never <strong>taken</strong>".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("took", "Hint: the sentence gives the date (in 2023) -- a closed moment, so past simple",
     "In 2023 I took a cab from JFK to Midtown.",
     '"In 2023 I ', ' a cab from JFK to Midtown."'),
    ("already", "Hint: the trip is still open -- this word comes before the past participle",
     "This time I have already used the subway twice.",
     '"This time I have ', ' used the subway twice."'),
    ("taken", "Hint: after have, the verb take becomes a past participle",
     "I have never taken the subway at rush hour.",
     '"I have never ', ' the subway at rush hour."'),
    ("fare", "Hint: the money you pay for the ride",
     "How much is the fare to the Upper West Side?",
     '"How much is the ', ' to the Upper West Side?"'),
    ("receipt", "Hint: the paper that proves you paid -- the P is silent",
     "Could I have a receipt, please?",
     '"Could I have a ', ', please?"'),
    ("sales tax", "Hint: the percentage that shows up only at the register",
     "The price on the tag doesn't include sales tax.",
     '"The price on the tag doesn\'t include ', '."'),
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
    (3, "Order the soup of the day and a coffee."),
    (5, "Take the receipt and head out to the subway."),
    (1, "Walk two blocks to the diner on Ninth Avenue."),
    (4, "Ask for the check and add a twenty percent tip."),
    (2, "Ask for a table for one and read the specials."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the New York Lunch in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">One lunch hour in Manhattan. Put the steps in the real order &mdash; from the sidewalk to the subway station.</p>')
A('      <div class="order-container" id="order-l3">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l3\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    "How much is the fare to the Upper West Side?",
    "When I went to New York in 2023, I took a cab everywhere.",
    "This time I've already used the subway twice.",
    "Could I have the check, please? Is the tip included?",
    "Could I try this on? Where is the fitting room?",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, say it out loud, and only then record. Pay attention to what Americans SWALLOW: <em>restaurant</em> has two syllables in their mouth (RES-trant), not three; <em>receipt</em> sounds like ri-SEET, with a silent P; and <em>fare</em> rhymes with <em>air</em>. Saying "less" here is saying it RIGHT.</p>')
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
    ("You are on Fifth Avenue with two shopping bags, and you want a taxi. What do you do and say?",
     [("Call the hotel and ask them to send a car &mdash; you can never get a taxi on the street.", False),
      ("Raise your hand to hail one and say: \"The Lucerne Hotel, 79th and Amsterdam, please.\"", True),
      ("Wait quietly at the curb until someone stops for you.", False)]),
    ("The driver says the price fast and the street is noisy. The best reaction is:",
     [("Pretend you understood and pay whatever he asks for at the end.", False),
      ("\"Sorry, it's loud out here. Let me read that back to you: about thirty-two dollars. Is that right?\"", True),
      ("\"Repeat, repeat!\"", False)]),
    ("You want to tell a colleague about the 2023 trip. Which sentence is correct?",
     [("\"I have gone to New York in 2023 and I have took a cab.\"", False),
      ("\"I went to New York in 2023 and I took a cab everywhere.\"", True),
      ("\"I go to New York in 2023 and I have already take a cab.\"", False)]),
    ("The check arrives at the diner: subtotal $24.00, total $26.13, and the <em>tip</em> line is blank. That means:",
     [("The tip is already in the total, so you do not have to do anything.", False),
      ("The total already includes the <strong>sales tax</strong>, but the tip is the part you write in &mdash; about 20% of the subtotal.", True),
      ("There is a mistake on the check and you should complain about it.", False)]),
    ("In the store on Fifth Avenue you like a coat and you want to try it on. You say:",
     [("\"Could I try this on? Where is the fitting room?\"", True),
      ("\"I want to use this coat now, please.\"", False),
      ("\"Where is the room for the clothes?\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of a day in New York.</p>')
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
A('        <div class="think-question">Tell the story of one real trip: a taxi you took, a restaurant you went to, or a store you walked into &mdash; in New York, in Europe, or in China. Use the past simple for what happened (I took, I went, I paid, I asked). Then compare it with now: what have you already done on this trip, and what have you never done? Finish with one thing you still haven\'t figured out. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-3"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 3</h4>')
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
