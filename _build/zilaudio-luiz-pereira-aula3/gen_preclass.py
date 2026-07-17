#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-3 do hub) do Ziláudio — aula 3.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 3 IN CLASS — mesmo vocab (feira), mesma gramatica
(perguntas + could para pedidos educados; preposicoes at/with/next to).

A3 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = questions + could.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(3)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Booth", "a small space at a fair where a company shows its products",
     "Their booth is next to the entrance."),
    ("Badge", "a card with your name that you wear at a fair",
     "Please show your badge at the door."),
    ("Business Card", "a small card with your name, your job and your contact",
     "Could I have your business card?"),
    ("Exhibitor", "a company or a person who shows products at a fair",
     "Every exhibitor has a story to tell."),
    ("Brochure", "a small book with pictures and information about a product",
     "Do you have a brochure about your seeds?"),
    ("Handshake", "when two people hold hands to say hello or to close a deal",
     "A good handshake starts the business."),
    ("Contact", "a person you know who can help your business",
     "You are a good contact for us."),
    ("Industry", "all the companies that do the same kind of work",
     "We are both in the soybean industry."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-3">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 03 -- Pre-class</div>')
A('      <h3>Small Talk at the Trade Fair</h3>')
A('      <div class="lesson-desc">Walk up to a booth, start a conversation with a stranger, and swap contacts &mdash; in English. '
  'Key words: booth, badge, business card, exhibitor, brochure, handshake, contact, industry. Structure: '
  '<strong>questions</strong> (Do you...? Where...? What...?) and <strong>could</strong> for polite requests '
  '(Could I have your card?). Prepositions in focus: <strong>at</strong>, <strong>with</strong>, <strong>next to</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words you hear at every trade fair.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    speak = w.replace('Business Card', 'Business card')
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{speak}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado / REGRA 13: definicao EN) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text slowly, twice, and then answer the questions.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>Ziláudio <strong>is</strong> <strong>at</strong> a big <strong>booth</strong> <strong>at</strong> the fair. He walks up to an '
  '<strong>exhibitor</strong> and starts a conversation. "Hi, I\'m Ziláudio," he says. "<strong>What</strong> does your company '
  '<strong>do</strong>?" The exhibitor smiles. They talk <strong>with</strong> each other about soybeans and seeds.</p>')
A('        <p style="margin-top:.8rem">Ziláudio wants more information. "<strong>Do</strong> you have a <strong>brochure</strong>?" he asks. '
  '"Of course," she says, and gives him one. Then he asks politely: "<strong>Could</strong> I have your <strong>business card</strong>?" '
  'She gives him her card, and he gives her his &mdash; a good <strong>contact</strong> in the same <strong>industry</strong>. '
  'Her <strong>booth</strong> <strong>is</strong> <strong>next to</strong> the entrance, so it is easy to find again.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Ziláudio says "<strong>Could</strong> I have your business card?" instead of "I want your card." Why?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> <strong>Could</strong> makes the request polite. "I want" sounds like an order.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "could" is the past of "can".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because you only use "could" with business cards.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "<strong>Do</strong> you have a brochure?" Why does the question start with <strong>do</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the answer is yes.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> In English, a question about an action needs a starter word: <strong>Do you</strong> + verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "brochure" is a French word.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "He is <strong>at</strong> the booth." "Her booth is <strong>next to</strong> the entrance." Why not the same word?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> They are the same. You can use at or next to anywhere.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> <strong>At</strong> is an exact point (at the booth). <strong>Next to</strong> means right beside something.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> <strong>At</strong> is for people and <strong>next to</strong> is for places.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which question is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Where you are from?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Where are you from?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "From where you are?"</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Asking Questions &amp; Being Polite</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A question starts with a special word. To ask for something, <strong>could</strong> is the polite key.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">be + you<br>Are you...? / Where are you...?</td><td style="padding:.6rem">Ask about a fact: place, name, job.</td><td style="padding:.6rem"><strong>Where are</strong> you from?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Do + you + verb<br>Do you...? / What do you...?</td><td style="padding:.6rem">Ask about an action or a habit.</td><td style="padding:.6rem"><strong>Do you</strong> have a brochure?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Could + I / you + verb</td><td style="padding:.6rem">Ask for something the polite way (a request).</td><td style="padding:.6rem"><strong>Could I</strong> have your card?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Short answer</td><td style="padding:.6rem">Answer with the same helper word.</td><td style="padding:.6rem">Yes, I <strong>do</strong>. / Of <strong>course</strong>, here you are.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">at &middot; with &middot; next to</td><td style="padding:.6rem" colspan="2"><strong>at</strong> + an exact point (at the booth, at the entrance) &middot; <strong>with</strong> + who you talk or work with (with an exhibitor) &middot; <strong>next to</strong> + right beside something (next to hall two)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> a question in English needs a starter word. "You have a card?" is wrong &mdash; say "<strong>Do you</strong> have a card?" And never ask for something with "I want" &mdash; it sounds like an order. Use "<strong>Could I</strong> have...?", the polite way. In business, polite always wins.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("Do", "Hint: the starter word for a question about an action",
     "Do you have a brochure?",
     '"', ' you have a brochure?"'),
    ("Could", "Hint: the polite word to ask for something",
     "Could I have your business card?",
     '"', ' I have your business card?"'),
    ("are", "Hint: the verb be, for a question about a fact",
     "Where are you from?",
     '"Where ', ' you from?"'),
    ("at", "Hint: the preposition for an exact point",
     "I am at booth twenty.",
     '"I am ', ' booth twenty."'),
    ("with", "Hint: the preposition for who you talk to",
     "I talk with an exhibitor.",
     '"I talk ', ' an exhibitor."'),
    ("next to", "Hint: the preposition for right beside something",
     "Our booth is next to the entrance.",
     '"Our booth is ', ' the entrance."'),
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
    (3, "Ask a question about their company: what do they do?"),
    (1, "Walk up to the booth and say hello with your name."),
    (5, "Say goodbye and keep the contact for the future."),
    (2, "Say what you are: a farmer from Mato Grosso."),
    (4, "Ask politely for a brochure and a business card."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You walk up to a booth at the fair. Put the steps of a good small-talk conversation in the natural order.</p>')
A('      <div class="order-container" id="order-l3">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l3\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (A2: frases de 5-7 palavras) ----------
SPEECH = [
    "Hi, I'm Zilaudio. Nice to meet you.",
    "What does your company do?",
    "Do you have a brochure?",
    "Could I have your business card?",
    "It was a pleasure. Let's stay in contact.",
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
    ("You arrive at a booth and want to start a conversation. You say:",
     [("\"Give me information.\"", False),
      ("\"Hi, I'm Zilaudio. What does your company do?\"", True),
      ("\"Booth. Company. What?\"", False)]),
    ("You want the exhibitor's brochure. The polite way is:",
     [("\"Could I have a brochure, please?\"", True),
      ("\"I want a brochure.\"", False),
      ("\"Give me the brochure.\"", False)]),
    ("You want the exhibitor's business card. You say:",
     [("\"Your card. Now.\"", False),
      ("\"Could I have your business card?\"", True),
      ("\"You have a card for me?\"", False)]),
    ("You want to know where the exhibitor is from. Which question is correct?",
     [("\"From where you come?\"", False),
      ("\"Where you are from?\"", False),
      ("\"Where are you from?\"", True)]),
    ("The conversation is over. You want to keep the contact. You say:",
     [("\"Goodbye. The end.\"", False),
      ("\"It was a pleasure. Let's stay in contact.\"", True),
      ("\"I go now. Bye.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment at the trade fair. Remember: polite always wins.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. Focus on being polite: use "Could I...?" when you ask for something.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">You are at a big agriculture fair. You walk up to a booth and meet an exhibitor for the first time. Start the conversation: say hello and your name, say what you are and what you grow, ask two questions about her company (with <strong>do</strong> or <strong>are</strong>), ask politely for a brochure and a business card (with <strong>could</strong>), and finish by keeping the contact. Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-3"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
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
