#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-2 do hub) do Ziláudio — aula 2.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 2 IN CLASS — mesmo vocab, mesma gramatica.
REGRA 22: 8 palavras NOVAS, zero colisao com a aula 1 (acre/yield/season/machinery/
storage/truck/weather/silo).

A2 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = present simple
3a pessoa (has/produces) + how much / how many + numeros grandes.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(22)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Acre", "a unit of land used to measure a farm in the United States",
     "The farm covers two thousand acres."),
    ("Yield", "the amount of crop that a field produces",
     "In a good season, the yield is high."),
    ("Season", "a part of the year for growing or for harvesting",
     "The rainy season starts in October."),
    ("Machinery", "the big machines a farm uses to work the land",
     "We use modern machinery on the farm."),
    ("Storage", "a place where you keep the crop after the harvest",
     "We need more storage for the soybean."),
    ("Truck", "a big vehicle that carries the crop on the road",
     "Ten trucks carry the crop to the port."),
    ("Weather", "the sun, the rain and the heat over the fields",
     "The weather is important for the harvest."),
    ("Silo", "a tall tower where a farm keeps its grain",
     "We keep the soybean in a tall silo."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-2">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 02 -- Pre-class</div>')
A('      <h3>My Farm, My Numbers</h3>')
A('      <div class="lesson-desc">Describe your operation in numbers to an international buyer. '
  'Key words: acre, yield, season, machinery, storage, truck, weather, silo. Structure: the present '
  'simple in the <strong>third person</strong> (the farm has, it produces) and the difference between '
  '<strong>how much</strong> and <strong>how many</strong>. Prepositions in focus: '
  '<strong>on</strong>, <strong>from</strong>, <strong>to</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words that describe the size and the work of a farm.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado / REGRA 13: definicao EN) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>')
A('      <div class="match-grid" id="match-l2">')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text slowly, twice, and then answer the questions.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>John Miller <strong>is</strong> a farmer <strong>in</strong> Iowa. His farm <strong>has</strong> two thousand '
  '<strong>acres</strong>. He <strong>grows</strong> corn and soybeans <strong>on</strong> his land, and the farm '
  '<strong>produces</strong> a lot of food. <strong>In</strong> a good <strong>season</strong>, the '
  '<strong>yield</strong> <strong>is</strong> high. He <strong>has</strong> modern <strong>machinery</strong>: '
  'three tractors and two big harvesters.</p>')
A('        <p style="margin-top:.8rem">The machines <strong>work</strong> <strong>from</strong> September '
  '<strong>to</strong> November. After the harvest, John <strong>keeps</strong> the corn <strong>in</strong> two tall '
  '<strong>silos</strong>. Every week, ten <strong>trucks</strong> <strong>carry</strong> the corn <strong>from</strong> '
  'the farm <strong>to</strong> the river. "The <strong>weather</strong> <strong>is</strong> the big question," he '
  '<strong>says</strong>.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. The text says "the farm <strong>has</strong>" and "it <strong>produces</strong>". Where does the <strong>-s</strong> come from?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It is a plural: the farm has many things.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> In the present simple, <strong>he / she / it / the farm</strong> takes <strong>-s</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It only happens with the verb "to have".</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. A buyer wants to know the number of trucks. Which question is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "How much trucks does the farm have?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "How many trucks does the farm have?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "How many truck does the farm have?"</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "The machines work <strong>from</strong> September <strong>to</strong> November." What does this tell us?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The machines only work in September.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> They start in September and stop in November.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> They work from Iowa to the river.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. You cannot count rain the way you count trucks. So you ask:</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "How much rain do you get in the season?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "How many rain do you get in the season?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "How many rains do you get in the season?"</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- How Much, How Many, and the Third Person</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two number questions, one small verb ending. Ask yourself: can I count it?</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">How many</td><td style="padding:.6rem">Things you can COUNT: trucks, silos, acres, tons.</td><td style="padding:.6rem">How <strong>many</strong> trucks do you use?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">How much</td><td style="padding:.6rem">Things you do NOT count: rain, soybean, storage, machinery.</td><td style="padding:.6rem">How <strong>much</strong> rain do you get?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Third person<br>he / she / it / the farm + verb<strong>-s</strong></td><td style="padding:.6rem">With he, she, it or the farm, the verb takes <strong>-s</strong>.</td><td style="padding:.6rem">The farm <strong>has</strong>. It <strong>produces</strong>.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Number + unit</td><td style="padding:.6rem">After a number, the unit stays as it is &mdash; no extra word.</td><td style="padding:.6rem">two thousand <strong>hectares</strong> &middot; fifty <strong>tons</strong></td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">on &middot; from &middot; to</td><td style="padding:.6rem" colspan="2"><strong>on</strong> + a surface (on the farm, on the land) &middot; <strong>from ... to</strong> + one point to another, in time or in space (from January to March, from the farm to the port)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> never say "how much trucks" &mdash; you can count trucks, so it is "how <strong>many</strong> trucks". And with <strong>the farm</strong> or <strong>it</strong>, the verb is never bare: "The farm <strong>has</strong>", not "The farm have".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("has", "Hint: third person of 'have' -- the farm / it",
     "The farm has two thousand hectares.",
     '"The farm ', ' two thousand hectares."'),
    ("many", "Hint: for things you can count, like trucks",
     "How many trucks do you use?",
     '"How ', ' trucks do you use?"'),
    ("much", "Hint: for things you cannot count, like rain",
     "How much rain do you get in the season?",
     '"How ', ' rain do you get in the season?"'),
    ("from", "Hint: the preposition for the start of a period",
     "The harvest runs from January to March.",
     '"The harvest runs ', ' January to March."'),
    ("on", "Hint: the preposition for a surface, like the land",
     "We grow soybeans on the farm.",
     '"We grow soybeans ', ' the farm."'),
    ("produces", "Hint: third person of 'produce' -- the farm / it",
     "In a good season, it produces fifty tons.",
     '"In a good season, it ', ' fifty tons."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence &mdash; as many times as you want.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering ----------
ORDER = [
    (3, "Say what you produce, and how much per hectare."),
    (1, "Say the size of the farm in hectares."),
    (5, "Ask the buyer a question back about his numbers."),
    (2, "Say your main crop, and when the harvest runs."),
    (4, "Say how you store and move the crop: silos and trucks."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Farm Report in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">A buyer asks for your numbers. Put the parts of your farm report in a natural order.</p>')
A('      <div class="order-container" id="order-l2">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l2\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (A2: frases de 5-7 palavras) ----------
SPEECH = [
    "The farm has two thousand hectares.",
    "How many trucks do you use?",
    "We store the soybean in two silos.",
    "The harvest runs from January to March.",
    "It produces fifty tons per hectare.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, repeat it out loud, and only then record. Listen and record as many times as you want &mdash; repetition is the method, not a sign of difficulty.</p>')
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
    ("A buyer asks: \"How big is your farm?\" The best answer is:",
     [("\"My farm is two thousand.\"", False),
      ("\"The farm has two thousand hectares.\"", True),
      ("\"Two thousand hectares is my farm big.\"", False)]),
    ("He asks: \"How many silos do you have?\" You answer:",
     [("\"We have two silos on the farm.\"", True),
      ("\"How much silos? Two.\"", False),
      ("\"We have two silo on the farm.\"", False)]),
    ("He asks: \"How much soybean do you produce?\" The best answer is:",
     [("\"We produce fifty tons per hectare.\"", True),
      ("\"We produce many soybean.\"", False),
      ("\"How many? Fifty.\"", False)]),
    ("He asks: \"When is the harvest?\" You answer:",
     [("\"The harvest is in January until March.\"", False),
      ("\"The harvest runs from January to March.\"", True),
      ("\"The harvest runs at January to March.\"", False)]),
    ("You want to describe the machines on your farm. Which sentence is correct?",
     [("\"The farm have modern machinery.\"", False),
      ("\"The farm has many machinery.\"", False),
      ("\"The farm has modern machinery: three tractors.\"", True)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment with an international buyer.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. Use the real numbers of your farm.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">A buyer from the United States wants to understand your operation. Describe your farm in numbers: the size in hectares, your main crop, the yield, when the harvest runs (<strong>from ... to</strong>), how you store the crop (silos) and how many trucks you use. Use <strong>the farm has</strong> and <strong>it produces</strong> with the <strong>-s</strong>. Finish with one question back to him about his numbers. Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-2"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
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
