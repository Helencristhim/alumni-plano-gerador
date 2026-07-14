#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-1 do hub) da Lucimara — aula 1.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluna B1 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(55)  # deterministico

# (word, definicao EN, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Industry", "a group of companies that make the same kind of product",
     "I work in the chemical industry."),
    ("Supplier", "a company that sells you the materials you need",
     "Most of our suppliers are in China."),
    ("Regulatory", "connected to the official rules a product must follow",
     "I am responsible for regulatory affairs."),
    ("Trade fair", "a big event where companies show their products to buyers",
     "I go to a trade fair in Lyon every November."),
    ("Headquarters", "the main office of a company, where the leadership sits",
     "Our headquarters is in Guarulhos."),
    ("To negotiate", "to talk with someone until you both agree on a price or a deal",
     "I negotiate prices with our Chinese partners."),
    ("Commute", "the trip you make between home and work",
     "My commute takes forty minutes each way."),
    ("Fluent", "able to speak a language easily, without stopping to think",
     "I want to be fluent before my next trip."),
    ("Confident", "sure that you can do something well",
     "I feel confident when I read, but not when I listen."),
    ("Stuck", "not able to move forward, because something is blocking you",
     "I get stuck when people speak very fast."),
    ("To catch", "to hear and understand what somebody said",
     "Sorry, I didn't catch that."),
    ("Abroad", "in or to another country",
     "I travel abroad every two or three months."),
]

VOL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
       '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
       '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-1">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 01 -- Pre-class</div>')
A('      <h3>Who Is Lucimara? -- Diagnostic Session and Personal Introduction</h3>')
A('      <div class="lesson-desc">Introduce yourself and talk about your work at an international trade fair in New York. '
  'Key words: industry, supplier, regulatory, trade fair, headquarters, negotiate, commute, fluent, confident, '
  'stuck, catch, abroad. Structures: present simple (your routine) vs present continuous (right now) vs present perfect '
  '(for / since). And the phrases that save any conversation when you do not understand what the other person said.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Take your time &mdash; listen twice, then say it out loud. These are the twelve words that describe your work and your routine.</p>')
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
A('        <p>Lucimara <strong>is</strong> a director in the chemical <strong>industry</strong>. She <strong>works</strong> in Guarulhos, '
  'where the company <strong>headquarters</strong> <strong>is</strong>, and she <strong>lives</strong> in Perdizes, so her <strong>commute</strong> '
  '<strong>takes</strong> forty minutes each way. Every month she <strong>negotiates</strong> prices with <strong>suppliers</strong> in China, and '
  'twice a year she <strong>goes</strong> to a <strong>trade fair</strong> <strong>abroad</strong>. "I <strong>have worked</strong> in this industry '
  '<strong>for</strong> twenty years," she says, "and I <strong>have been</strong> a director <strong>since</strong> 2015." Right now, her team '
  '<strong>is preparing</strong> a new product registration, and she <strong>is studying</strong> English again, because in September she '
  '<strong>is going</strong> to New York. She <strong>reads</strong> <strong>regulatory</strong> documents in English without a problem and she '
  '<strong>feels</strong> <strong>confident</strong> on the phone with old partners. But when an American speaks fast, she <strong>gets</strong> '
  '<strong>stuck</strong>: she <strong>does not catch</strong> the end of the sentence. She <strong>wants</strong> to be <strong>fluent</strong> &mdash; '
  'and, more than that, she <strong>wants</strong> to understand.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Why do we say "I <strong>have worked</strong> in this industry for twenty years" and not "I work in this industry for twenty years"?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because it started in the past and it CONTINUES today &mdash; present perfect with <strong>for</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because it is finished and it has no connection with the present.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a routine that she repeats every week.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "Right now, her team <strong>is preparing</strong> a new product registration." Why present continuous?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because it happens every day &mdash; it is her routine.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because it is happening NOW, in this period &mdash; it is not the usual routine.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it started twenty years ago and it continues.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "She <strong>has been</strong> a director <strong>since</strong> 2015." What does this sentence tell you?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She was a director in 2015 and then she left the position.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She became a director in 2015 and she is STILL a director today.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She is going to become a director in 2015.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her routine is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She is negotiating with suppliers every month."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She negotiates with suppliers every month, and her commute takes forty minutes."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She has negotiated with suppliers every month since twenty years."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Simple vs Present Continuous vs Present Perfect (for / since)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The three structures behind any personal introduction in English.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / you / we + verb (he/she + s)</td><td style="padding:.6rem">Your routine, your job title, what is always true.</td><td style="padding:.6rem">I <strong>work</strong> in the chemical industry.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Continuous<br>am / is / are + verb-ing</td><td style="padding:.6rem">What is happening NOW, this month &mdash; not the routine.</td><td style="padding:.6rem">Right now, I <strong>am preparing</strong> a registration.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + past participle</td><td style="padding:.6rem">It started in the past and it CONTINUES today. Duration up to now (for / since).</td><td style="padding:.6rem">I <strong>have worked</strong> here for twenty years.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">have / has + not + past participle. In speech, contracted: <strong>haven\'t</strong>.</td><td style="padding:.6rem">I <strong>haven\'t</strong> been to Lyon this year.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">How long + have + subject + past participle?</td><td style="padding:.6rem"><strong>How long have you been</strong> in the industry?</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">for vs since</td><td style="padding:.6rem" colspan="2"><strong>for</strong> + a period of time (for twenty years) &middot; <strong>since</strong> + a starting point (since 2015)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> in your first language, duration up to now uses the PRESENT tense, so "I work here for twenty years" feels right. In English it is wrong: duration up to now <strong>never</strong> uses the present simple. The correct form is "I <strong>have worked</strong> here for twenty years" (in speech, <strong>I\'ve worked</strong>). And remember: <strong>responsible FOR</strong>, never "responsible of".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("have worked", "Hint: it started twenty years ago and it CONTINUES -- have + past participle",
     "I have worked in the chemical industry for twenty years.",
     '"I ', ' in the chemical industry for twenty years."'),
    ("am preparing", "Hint: it is happening now, this month -- am + verb-ing",
     "Right now, I am preparing a new product registration.",
     '"Right now, I ', ' a new product registration."'),
    ("negotiate", "Hint: a routine, every month -- present simple",
     "Every month, I negotiate prices with our suppliers in China.",
     '"Every month, I ', ' prices with our suppliers in China."'),
    ("for", "Hint: a period of time (twenty years)",
     "I have been in this industry for twenty years.",
     '"I have been in this industry ', ' twenty years."'),
    ("since", "Hint: a starting point (2015)",
     "I have been a director since 2015.",
     '"I have been a director ', ' 2015."'),
    ("catch", "Hint: to hear AND understand what the other person said",
     "Sorry, I didn't catch that. Could you say it again more slowly?",
     '"Sorry, I didn\'t ', ' that. Could you say it again more slowly?"'),
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
    (3, "Say what you do: your job, your industry and what you are responsible for."),
    (5, "Agree on a next step: exchange cards and set a time to meet."),
    (1, "Say hello and introduce yourself: your name and your company."),
    (4, "Ask HIM a question: what does his company do, and what is he looking for?"),
    (2, "Say how long you have been in the industry, with for or since."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You have just met someone at an international trade fair. Put the steps of the conversation in the natural order.</p>')
A('      <div class="order-container" id="order-l1">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l1\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l1\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    "I'm a director in the chemical industry, and I'm responsible for production.",
    "I've worked in this industry for twenty years.",
    "Right now, I'm preparing a new product registration.",
    "Sorry, I didn't catch that. Could you say it again more slowly?",
    "I travel abroad every two or three months, mostly to New York.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, repeat it out loud, and only then record. You can listen and record again as many times as you want &mdash; repetition is the method, not a sign of difficulty.</p>')
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
    ("At a trade fair in New York, someone asks you: \"So, what do you do?\" You answer:",
     [("\"I do the chemical things in a company.\"", False),
      ("\"I'm a director in the chemical industry, and I'm responsible for production and regulatory affairs.\"", True),
      ("\"I am responsible of the production since twenty years.\"", False)]),
    ("He asks: \"How long have you been in the industry?\" The best answer is:",
     [("\"I am in this industry for twenty years.\"", False),
      ("\"I've worked in this industry for twenty years.\"", True),
      ("\"I work in this industry since twenty years.\"", False)]),
    ("You want to talk about the project your team is running THIS month. Which sentence is correct?",
     [("\"Right now, we're preparing a new product registration.\"", True),
      ("\"Right now, we prepare a new product registration.\"", False),
      ("\"Right now, we have prepared a new product registration.\"", False)]),
    ("The American speaks fast and you miss the end of the sentence. The most professional move is:",
     [("Smile, nod, and hope that nobody notices.", False),
      ("\"Sorry, I didn't catch that. Could you say it again more slowly?\"", True),
      ("Apologize for your English and change the subject.", False)]),
    ("You want to confirm that you understood the agreement. You say:",
     [("\"Yes, yes, ok, ok.\"", False),
      ("\"Let me check I understood. You need the bio by Friday, right?\"", True),
      ("\"I don't know, sorry.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of a business trip or an international trade fair.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 90 seconds, with no script. This recording is your BASELINE: we will listen to it again in lesson 24 and in lesson 48, and you will hear the difference with your own ears.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">You are at an international trade fair in New York and someone you have never met says hello. Introduce yourself: your name, your job in the chemical industry (present simple), what you are responsible for, how long you have been in the industry (present perfect, for / since), and what your team is working on this month (present continuous). Finish by saying how often you travel abroad. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-1"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
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
