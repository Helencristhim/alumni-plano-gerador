#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-4 do hub) do Ziláudio — aula 4.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 4 IN CLASS — mesmo vocab, mesma gramatica.
REGRA 22: 8 palavras NOVAS, zero colisao com aulas 1-3 (attachment/reply/deadline/request/
schedule/confirm/subject/regards).

A4 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = past simple para
acoes concluidas (sent/received/asked/attached, regular + irregular) + preposicoes de
tempo by / before / after.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(4)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Subject", "the short line that says what an e-mail is about",
     "The subject line says: Soybean order."),
    ("Attachment", "a file that you send together with an e-mail",
     "Please check the attachment in my e-mail."),
    ("Reply", "an answer that you send back to an e-mail",
     "I will send my reply by Friday."),
    ("Request", "a polite way to ask for something you need",
     "I have one request: send me the form."),
    ("Deadline", "the last day or time to finish something",
     "The deadline for the form is Friday."),
    ("Confirm", "to say clearly that something is correct or certain",
     "Can you confirm the total tons?"),
    ("Schedule", "a plan that shows when things happen: times and dates",
     "Our schedule this month is very tight."),
    ("Regards", "a polite word to close an e-mail before your name",
     "Best regards, Zilaudio."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-4">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1526628953301-3e589a6a8b74?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 04 -- Pre-class</div>')
A('      <h3>Reading a Business E-mail</h3>')
A('      <div class="lesson-desc">Read a real e-mail from an international buyer and find the request and the '
  'deadline. Key words: subject, attachment, reply, request, deadline, confirm, schedule, regards. Structure: '
  'the <strong>past simple</strong> for completed actions (I sent, I received, I asked, I attached) and the '
  'prepositions of time <strong>by</strong>, <strong>before</strong> and <strong>after</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words that live inside a business e-mail.</p>')
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
A('      <div class="match-grid" id="match-l4">')
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
A('        <p>David <strong>is</strong> a buyer <strong>from</strong> Chicago. Last Monday, he <strong>sent</strong> '
  'Zilaudio an e-mail. The <strong>subject</strong> line <strong>said</strong>: "Soybean order". He <strong>attached</strong> '
  'a short form and <strong>asked</strong> <strong>for</strong> two documents. In the e-mail, he <strong>made</strong> one '
  '<strong>request</strong>: a <strong>reply</strong> <strong>by</strong> Friday.</p>')
A('        <p style="margin-top:.8rem">Zilaudio <strong>received</strong> the e-mail <strong>on</strong> Wednesday. He '
  '<strong>checked</strong> the <strong>attachment</strong> and <strong>read</strong> the <strong>deadline</strong>. The '
  '<strong>schedule</strong> <strong>was</strong> tight, so he <strong>replied</strong> <strong>before</strong> the weekend. '
  'He <strong>wrote</strong>: "I <strong>confirm</strong> the tons and the price. Best <strong>regards</strong>, Zilaudio."</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. The text says "he <strong>sent</strong>", "he <strong>attached</strong>", "he <strong>asked</strong>". What do these verbs show?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Things David is doing right now.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Actions that are already done and finished &mdash; the past simple.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Things that will happen next week.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. David needs "a reply <strong>by</strong> Friday". This means:</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> He wants the reply exactly on Saturday.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Friday is the deadline &mdash; the reply must come not later than Friday.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He does not need a reply at all.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "send" is an irregular verb. In the text, its past form is:</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> sended</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> sent</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> sends</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. "He replied <strong>before</strong> the weekend." When did Zilaudio reply?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Earlier than the weekend &mdash; during the week.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> On Sunday, at the end of the weekend.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He did not reply.</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Past Simple, and by / before / after</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use the past simple for what is already done. Ask yourself: is the action finished?</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Regular past<br>verb + <strong>-ed</strong></td><td style="padding:.6rem">Most verbs. The action is done and finished.</td><td style="padding:.6rem">ask &#8594; <strong>asked</strong> &middot; attach &#8594; <strong>attached</strong></td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Irregular past<br>a new word</td><td style="padding:.6rem">A few verbs change completely. Learn them one by one.</td><td style="padding:.6rem">send &#8594; <strong>sent</strong> &middot; write &#8594; <strong>wrote</strong></td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">by</td><td style="padding:.6rem">Not later than this point &mdash; a deadline.</td><td style="padding:.6rem">Send your <strong>reply</strong> <strong>by</strong> Friday.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">before</td><td style="padding:.6rem">Earlier than this point in time.</td><td style="padding:.6rem">Write to me <strong>before</strong> the weekend.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">after</td><td style="padding:.6rem">Later than this point in time.</td><td style="padding:.6rem"><strong>After</strong> you reply, I will call you.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> never use the present for something already done. Not "I send you the price yesterday" &mdash; say "I <strong>sent</strong> you the price yesterday". And "send" is irregular: the past is <strong>sent</strong>, never "sended".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("sent", "Hint: past simple of 'send' -- it is irregular",
     "Last Monday I sent you the price.",
     '"Last Monday I ', ' you the price."'),
    ("received", "Hint: past simple of 'receive' -- a completed action",
     "I received your e-mail on Wednesday.",
     '"I ', ' your e-mail on Wednesday."'),
    ("attached", "Hint: past simple of 'attach' -- add -ed",
     "I attached a short form to the e-mail.",
     '"I ', ' a short form to the e-mail."'),
    ("by", "Hint: the preposition for a deadline",
     "Please send your reply by Friday.",
     '"Please send your reply ', ' Friday."'),
    ("after", "Hint: the preposition for later in time",
     "After you reply, I will call you.",
     '"', ' you reply, I will call you."'),
    ("confirm", "Hint: to say clearly that something is correct",
     "Can you confirm the total tons?",
     '"Can you ', ' the total tons?"'),
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

# ---------- Stage 2 — Ordering (parts of an e-mail, natural order) ----------
ORDER = [
    (3, "Request -- ask for or confirm what the buyer needs."),
    (1, "Subject -- the short line that says what the e-mail is about."),
    (5, "Regards -- the polite close, before your name."),
    (2, "Greeting -- open the e-mail: \"Dear David,\""),
    (4, "Deadline -- say when you will send your answer."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the E-mail in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You reply to the buyer. Put the parts of a business e-mail in a natural order.</p>')
A('      <div class="order-container" id="order-l4">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l4\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (A2: frases de 5-7 palavras) ----------
SPEECH = [
    "Thank you for your e-mail.",
    "I received your message and the attachment.",
    "I confirm the total tons and the price.",
    "I will send the form back by Friday.",
    "Best regards, Zilaudio.",
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
    ("The buyer asks you to confirm the price. The best reply is:",
     [("\"I confirm the total tons and the price.\"", True),
      ("\"Maybe the price is correct.\"", False),
      ("\"I confirmed you the price is.\"", False)]),
    ("David set a deadline: Friday. You want to say you will answer in time:",
     [("\"I will reply until Friday.\"", False),
      ("\"I will send my reply by Friday.\"", True),
      ("\"I reply for Friday.\"", False)]),
    ("He attached a form. You want to say you got it:",
     [("\"I receive your attachment now.\"", False),
      ("\"I received your e-mail and the attachment.\"", True),
      ("\"I received your e-mail and the attach.\"", False)]),
    ("You need his new plan of dates for the meeting. You ask:",
     [("\"Can you send me the new schedule?\"", True),
      ("\"Can you send me the new deadline schedule dates?\"", False),
      ("\"Where is the schedule of you?\"", False)]),
    ("You want to tell David what you already did last Monday:",
     [("\"Last Monday I send the documents.\"", False),
      ("\"Last Monday I sended the documents.\"", False),
      ("\"Last Monday I sent the documents.\"", True)]),
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">A buyer from the United States sent you an e-mail. He attached a form and asked for your total tons and your price, with a <strong>reply by Friday</strong>. Answer his e-mail out loud: thank him, say you <strong>received</strong> the message and the <strong>attachment</strong>, <strong>confirm</strong> the numbers, say you will send the form <strong>by Friday</strong>, and close with <strong>Best regards</strong>. Use the past simple for what you already did (I <strong>sent</strong>, I <strong>received</strong>). Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-4"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 4</h4>')
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
