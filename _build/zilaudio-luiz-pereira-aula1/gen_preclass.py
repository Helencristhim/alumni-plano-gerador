#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-1 do hub) do Ziláudio — aula 1.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 1 IN CLASS — mesmo vocab, mesma gramatica.

A2 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = present simple + to be.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(17)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Farmer", "a person who grows food on land",
     "I am a farmer in Mato Grosso."),
    ("Lawyer", "a person whose job is to work with the law",
     "I am a lawyer too."),
    ("Crop", "a plant that a farmer grows to sell",
     "Soybeans are our main crop."),
    ("Soybean", "a small bean that is sold all over the world",
     "We grow soybeans on our farm."),
    ("Harvest", "the time when a farmer collects the crop",
     "The harvest starts in January."),
    ("Field", "a piece of land where a crop grows",
     "Our fields are very big."),
    ("Hectare", "a unit that farmers use to measure land",
     "We farm two thousand hectares."),
    ("Supplier", "a company that sells you what you need for work",
     "Our supplier is in Cuiaba."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-1">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 01 -- Pre-class</div>')
A('      <h3>Introducing Yourself at Work</h3>')
A('      <div class="lesson-desc">Say who you are and what you do, in English, to someone who has never heard of Sorriso. '
  'Key words: farmer, lawyer, crop, soybean, harvest, field, hectare, supplier. Structure: present simple and the verb '
  '<strong>to be</strong> &mdash; the two forms behind every professional introduction. Prepositions in focus: '
  '<strong>in</strong>, <strong>at</strong>, <strong>for</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words that describe your work.</p>')
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
A('      <div class="match-grid" id="match-l1">')
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
A('        <p>Ziláudio <strong>is</strong> a <strong>farmer</strong> and a <strong>lawyer</strong>. He <strong>lives</strong> '
  '<strong>in</strong> Sorriso, <strong>in</strong> the state of Mato Grosso. He <strong>grows</strong> <strong>soybeans</strong>, '
  'and it <strong>is</strong> his main <strong>crop</strong>. His <strong>fields</strong> <strong>are</strong> very big: the farm '
  '<strong>is</strong> two thousand <strong>hectares</strong>. The <strong>harvest</strong> <strong>starts</strong> <strong>in</strong> '
  'January. He <strong>buys</strong> seeds from a <strong>supplier</strong> <strong>in</strong> Cuiaba.</p>')
A('        <p style="margin-top:.8rem">Ziláudio <strong>works</strong> <strong>at</strong> a law firm too. He <strong>is</strong> '
  'a lawyer <strong>for</strong> small companies. "I <strong>am</strong> a farmer and a lawyer," he <strong>says</strong>. '
  '"I <strong>work</strong> <strong>in</strong> two worlds." He <strong>travels</strong> to the United States two times a year, '
  'and he <strong>wants</strong> to speak English <strong>at</strong> work.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Why do we say "Ziláudio <strong>is</strong> a farmer" but "he <strong>grows</strong> soybeans"?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> <strong>Be</strong> says WHAT he is. A normal verb says what he DOES.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "farmer" is a long word and "soybeans" is short.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because one is the past and the other is the present.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. The text says "he <strong>grows</strong>", "he <strong>lives</strong>", "he <strong>works</strong>". Where does the <strong>-s</strong> come from?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It is a plural: he grows many things.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> In the present simple, <strong>he / she / it</strong> always takes <strong>-s</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It only happens with the verb "to grow".</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "He lives <strong>in</strong> Sorriso." "He works <strong>at</strong> a law firm." Why not the same word?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> They are the same. You can use in or at anywhere.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> <strong>At</strong> is for big places and <strong>in</strong> is for small places.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> <strong>In</strong> is for a city or a country. <strong>At</strong> is for a place where you do something, like a firm.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about Ziláudio is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "He is grow soybeans in Mato Grosso."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "He is a farmer, and he grows soybeans in Mato Grosso."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "He a farmer and grow soybeans in Mato Grosso."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- To Be and the Present Simple</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two forms. <strong>Be</strong> says what you ARE. The present simple says what you DO.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">To be<br>I am &middot; he / she / it is &middot; we / they are</td><td style="padding:.6rem">WHAT you are: your job, your place.</td><td style="padding:.6rem">I <strong>am</strong> a farmer.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / you / we + verb</td><td style="padding:.6rem">What you DO: your routine, what is always true.</td><td style="padding:.6rem">I <strong>grow</strong> soybeans.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Third person<br>he / she / it + verb<strong>-s</strong></td><td style="padding:.6rem">With he, she or it, the verb always takes <strong>-s</strong>.</td><td style="padding:.6rem">He <strong>grows</strong> soybeans.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">With <strong>be</strong>: am / is / are + not. With other verbs: <strong>do not</strong> / <strong>does not</strong> + verb.</td><td style="padding:.6rem">I <strong>am not</strong> a doctor. I <strong>do not</strong> grow corn.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">With <strong>be</strong>: Are you...? With other verbs: <strong>Do you</strong> + verb?</td><td style="padding:.6rem"><strong>Are you</strong> a farmer? <strong>Do you</strong> grow soybeans?</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">in &middot; at &middot; for</td><td style="padding:.6rem" colspan="2"><strong>in</strong> + a city or a country (in Sorriso, in Brazil) &middot; <strong>at</strong> + a place where you do something (at a law firm) &middot; <strong>for</strong> + who you work for, or how long (for small companies, for fifteen years)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> never use <strong>be</strong> and a normal verb together. "I am work in Sorriso" is wrong &mdash; it is either "I <strong>am</strong> a farmer" (be) or "I <strong>work</strong> in Sorriso" (present simple), never both. And in English you always need the subject: "<strong>I am</strong> a farmer", never "Am a farmer".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("am", "Hint: to be, first person -- it says WHAT you are",
     "I am a farmer and a lawyer.",
     '"I ', ' a farmer and a lawyer."'),
    ("grow", "Hint: what you DO -- present simple, first person, no -s",
     "I grow soybeans in Mato Grosso.",
     '"I ', ' soybeans in Mato Grosso."'),
    ("in", "Hint: the preposition for a city or a state",
     "Our farm is in Mato Grosso.",
     '"Our farm is ', ' Mato Grosso."'),
    ("at", "Hint: the preposition for a place where you work",
     "I work at a law firm too.",
     '"I work ', ' a law firm too."'),
    ("is", "Hint: to be, third person -- he, she or it",
     "The harvest is our busiest time.",
     '"The harvest ', ' our busiest time."'),
    ("for", "Hint: the preposition for who you work for",
     "I am a lawyer for small companies.",
     '"I am a lawyer ', ' small companies."'),
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
    (3, "Say where you are from: your city and your state."),
    (1, "Say hello and say your name."),
    (5, "Ask him a question back: what does he do?"),
    (2, "Say what you are: your job, or your two jobs."),
    (4, "Say what you grow, and how big the farm is."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Introduction in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">A buyer says hello to you. Put the steps of your introduction in the natural order.</p>')
A('      <div class="order-container" id="order-l1">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l1\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l1\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (A2: frases de 5-7 palavras) ----------
SPEECH = [
    "I'm Zilaudio. Nice to meet you.",
    "I'm a farmer and a lawyer.",
    "I grow soybeans in Mato Grosso.",
    "Our farm is near Sorriso.",
    "I work at a law firm too.",
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
    ("A buyer at a fair asks you: \"So, what do you do?\" You answer:",
     [("\"I am work with soybean.\"", False),
      ("\"I'm a farmer and a lawyer. I grow soybeans in Mato Grosso.\"", True),
      ("\"Farmer. Soybean. Brazil.\"", False)]),
    ("He asks: \"Where is your farm?\" The best answer is:",
     [("\"My farm is in Mato Grosso, near Sorriso.\"", True),
      ("\"My farm is at Mato Grosso, near Sorriso.\"", False),
      ("\"My farm stay in Mato Grosso.\"", False)]),
    ("He asks: \"How big is your farm?\" You answer:",
     [("\"It is two thousand hectares.\"", True),
      ("\"It has two thousand hectare.\"", False),
      ("\"Two thousand hectares is my farm big.\"", False)]),
    ("You want to say you also work in law. Which sentence is correct?",
     [("\"I am also work at a law firm.\"", False),
      ("\"I also work at a law firm.\"", True),
      ("\"I am also working at a law firm every day.\"", False)]),
    ("He has never heard of Sorriso. The most useful thing to say is:",
     [("\"Sorriso. You don't know it?\"", False),
      ("\"It is a small city. Not important.\"", False),
      ("\"It's in Mato Grosso, in the center of Brazil. We grow a lot of soybeans there.\"", True)]),
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. This recording is your BASELINE: we will listen to it again at the end of the seven lessons, and you will hear the difference with your own ears.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">A buyer from the United States says hello to you. He has never heard of Sorriso. Introduce yourself: your name, what you are (present simple with <strong>be</strong>), what you grow and how big the farm is, where you live (<strong>in</strong>), where else you work (<strong>at</strong>), and who you work for (<strong>for</strong>). Finish with one question back to him. Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-1"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 1</h4>')
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
