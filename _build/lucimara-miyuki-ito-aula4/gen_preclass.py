#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-4 do hub) da Lucimara — aula 4.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: Lucimara e B1 => ZERO portugues na tela da aluna. Vocab card leva DEFINICAO em
ingles simples; o matching casa palavra EN <-> definicao EN; grammar tip, hints, quizzes,
instrucoes e survival card: tudo em ingles. Sem .speech-translation, sem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 4 IN CLASS (mesmo tema/gramatica/vocab).
REGRA 22: nenhuma palavra das aulas 1-3 volta como vocab card novo.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(4)  # deterministico

# (word, definicao EN, exemplo)
# As definicoes sao UNICAS entre si e cada uma carrega function words (a/the/to/you/that/...)
VOCAB = [
    ("Overbooked", "when a flight or a hotel has sold more seats or rooms than it really has",
     "The flight is overbooked, so somebody has to take a later one."),
    ("Delay notice", "the message that tells you your flight will leave later than planned",
     "I got the delay notice on my phone before I left the hotel."),
    ("To rebook", "to change your reservation to a different flight or a different day",
     "If they cancel the flight, they will rebook me at no extra cost."),
    ("Voucher", "a paper or a code that pays for one thing: a meal, a hotel, a taxi",
     "The airline gave me a voucher for dinner at the terminal."),
    ("Compensation", "extra money a company must pay you because it made you lose time",
     "After a six-hour delay, you can ask the airline for compensation."),
    ("Refund", "your money back, because you did not get the service you paid for",
     "If they cancel the flight and I don't fly, I will request a refund."),
    ("Travel insurance", "a policy that pays you back when the trip goes wrong: illness, lost bags, canceled flights",
     "My travel insurance covers a night in a hotel near the airport."),
    ("Alternative route", "a different way to reach the same place, when the first way is closed",
     "There is no direct flight tonight, so we will find an alternative route."),
    ("Complaint", "a formal statement that says, in writing, that something went wrong",
     "She filed a complaint with the airline the same night."),
    ("To sort out", "to solve a problem, step by step, until it is finished",
     "Don't worry -- the agent will sort it out before midnight."),
    ("To end up", "to be in a situation you did not plan, after everything changed",
     "I ended up sleeping in a hotel two minutes from the terminal."),
    ("To board", "to get on the plane, when they finally call your row",
     "We will board in twenty minutes at gate B twelve."),
]

# definicoes tem de ser unicas (o data-answer casa string pura com o value da option)
assert len({v[1] for v in VOCAB}) == len(VOCAB), 'definicoes do matching precisam ser UNICAS'

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-4">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1530521954074-e64f6810b32d?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 04 -- Pre-class</div>')
A('      <h3>If I Miss My Flight -- Handling Problems, Contingencies, and Unexpected Situations</h3>')
A('      <div class="lesson-desc">The board turns red in Miami: the flight is canceled, sixty people are in the line, '
  'and there is a meeting in Manhattan at nine in the morning. Key words: overbooked, delay notice, to rebook, voucher, '
  'compensation, refund, travel insurance, alternative route, complaint, to sort out, to end up, to board. '
  'Structure: <strong>first conditional</strong> &mdash; the grammar of plan B '
  '("<strong>If</strong> the flight <strong>is</strong> canceled, I <strong>will ask</strong> for a voucher." / '
  '"<strong>Unless</strong> they rebook me, I&#8217;ll end up sleeping at the airport." / '
  '"I&#8217;ll be fine <strong>as long as</strong> I board before midnight.").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Take your time &mdash; listen twice, say it out loud. These are the twelve words you will never need &mdash; until the night you need all twelve at the same time.</p>')
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

# ---------- Stage 1.2 — Matching (REGRA 13: definicao em INGLES; REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the right definition. Watch the pair that confuses everybody: a <strong>refund</strong> is YOUR money back; <strong>compensation</strong> is EXTRA money, for the trouble.</p>')
A('      <div class="match-grid" id="match-l4">')
defs = [v[1] for v in VOCAB]
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
A('        <p>It is seven in the evening in Miami, and the board turns red. The <strong>delay notice</strong> '
  'arrived an hour ago, and now the flight to New York is canceled. Lucimara does not panic. She builds a plan '
  'in her head, and the plan is a sentence: <strong>if</strong> the line <strong>is</strong> too long, she '
  '<strong>will call</strong> the airline while she waits.</p>')
A('        <p style="margin-top:.8rem">At the desk, the agent says the next direct flight is '
  '<strong>overbooked</strong>. She does not accept the first no. "<strong>If</strong> you <strong>can</strong> '
  'get me into JFK before eight, I <strong>will take</strong> any route," she says. It is an '
  '<strong>alternative route</strong>, through Charlotte, and it works. "I <strong>will be</strong> fine '
  '<strong>as long as</strong> I <strong>am</strong> in Manhattan by eight."</p>')
A('        <p style="margin-top:.8rem">The agent <strong>rebooks</strong> her and gives her a meal '
  '<strong>voucher</strong> and a hotel <strong>voucher</strong>. There is one condition, and it is the only '
  'thing that matters tonight: <strong>unless</strong> she <strong>checks in</strong> at the counter before '
  'four thirty, the system <strong>will release</strong> her seat. So she sets three alarms. She '
  '<strong>ends up</strong> eating a bad sandwich at eleven at night, in a terminal she never planned to see, '
  'but her <strong>travel insurance</strong> <strong>will cover</strong> the hotel.</p>')
A('        <p style="margin-top:.8rem">Tomorrow she <strong>will file</strong> a <strong>complaint</strong>, '
  'and <strong>if</strong> the airline <strong>agrees</strong>, she <strong>will get</strong> '
  '<strong>compensation</strong> &mdash; and a <strong>refund</strong> for the segment she never flew. But '
  'tonight only one thing counts: she <strong>sorted it out</strong> in English, and she '
  '<strong>will board</strong> at five in the morning.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "<strong>If</strong> you <strong>can</strong> get me into JFK before eight, I <strong>will take</strong> any route." Why is the verb after <strong>if</strong> in the present, if she is talking about the FUTURE?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because she is talking about now, not about the future.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because that is the iron rule of the first conditional: after <strong>if</strong>, the verb stays in the PRESENT. <strong>Will</strong> lives in the OTHER half of the sentence (the result).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the future does not exist in English.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "<strong>Unless</strong> she checks in before four thirty, the system will release her seat." What does <strong>unless</strong> mean here?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> <strong>If not</strong> &mdash; so: if she does NOT check in by four thirty, she loses her seat. The negative is already INSIDE <em>unless</em>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> <strong>Because</strong> &mdash; she loses her seat because she checked in.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> <strong>Until</strong> &mdash; she has to wait until four thirty.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "I will be fine <strong>as long as</strong> I <strong>am</strong> in Manhattan by eight." What does <em>as long as</em> do in this sentence?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It talks about duration: she will be fine for a long time.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It sets the ONLY condition that matters: to be in Manhattan by eight. If that happens, the rest (the route, the time of the flight, the hotel) does not matter.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It compares two flights.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If the flight will be canceled, I will ask for a voucher."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Unless they don\'t rebook me, I will file a complaint."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "If the flight is canceled, I will ask for a voucher &mdash; and unless they rebook me tonight, I\'ll file a complaint."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- First Conditional (the grammar of plan B)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">One sentence, two halves.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Piece</th><th style="padding:.7rem;text-align:left">Form / Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">The condition<br>(if...)</td><td style="padding:.6rem"><strong>if</strong> + SIMPLE PRESENT. <strong>Never</strong> <em>will</em> here &mdash; not even when you are talking about tomorrow.</td><td style="padding:.6rem">"<strong>If</strong> the flight <strong>is</strong> canceled..."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">The result</td><td style="padding:.6rem"><strong>will</strong> + base verb (no <em>to</em>). In fast speech it becomes <strong>&#8217;ll</strong>.</td><td style="padding:.6rem">"...I <strong>will ask</strong> for a voucher." / "I<strong>&#8217;ll</strong> ask."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">In both halves: <strong>doesn&#8217;t / don&#8217;t</strong> in the condition, <strong>won&#8217;t</strong> in the result.</td><td style="padding:.6rem">"<strong>If</strong> my bag <strong>doesn&#8217;t</strong> arrive, I <strong>won&#8217;t</strong> have a suit for the fair."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem"><strong>Will</strong> + subject + verb + <strong>if</strong> + present? This is the question you ask at the desk.</td><td style="padding:.6rem">"<strong>Will</strong> I <strong>get</strong> a hotel voucher <strong>if</strong> the flight <strong>is</strong> canceled?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">unless</td><td style="padding:.6rem">= <strong>if not</strong>. The negative is ALREADY inside it &mdash; so the verb after it comes in the AFFIRMATIVE.</td><td style="padding:.6rem">"<strong>Unless</strong> they <strong>rebook</strong> me, I&#8217;ll file a complaint."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">as long as<br>provided that</td><td style="padding:.6rem">= the ONLY condition that matters. Same grammar as <em>if</em>: present after it.</td><td style="padding:.6rem">"I&#8217;ll be fine <strong>as long as</strong> I <strong>board</strong> before midnight."</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">The order<br>and the comma</td><td style="padding:.6rem" colspan="2">The two halves can change places. Comma <strong>only</strong> when the condition opens the sentence: "<strong>If</strong> it is delayed<strong>,</strong> I will ask." / "I will ask <strong>if</strong> it is delayed." (no comma)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake (there are two, and both come from your first language):</strong> (1) <em>will</em> after <em>if</em>: your ear hears a future, so your head writes "if the flight <s>will be</s> delayed". English locks the door: after <em>if</em>, present, always. The <em>will</em> lives in the other half. (2) A double negative with <em>unless</em>: "unless they <s>don&#8217;t</s> rebook me" says, word for word, "if they do NOT NOT rebook me" &mdash; the opposite of what you wanted to say. <em>Unless</em> already means <em>if not</em>: the verb after it comes in the AFFIRMATIVE.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("is", "Hint: after if, the verb stays in the PRESENT -- never with will",
     "If the flight is canceled, I will ask for a voucher.",
     '"If the flight ', ' canceled, I will ask for a voucher."'),
    ("will ask", "Hint: this is the RESULT half -- this is where will belongs",
     "If my flight is delayed, I will ask for compensation.",
     '"If my flight is delayed, I ', ' for compensation."'),
    ("Unless", "Hint: one single word, and it already means if not",
     "Unless they rebook me tonight, I will end up sleeping at the airport.",
     '"', ' they rebook me tonight, I will end up sleeping at the airport."'),
    ("as long as", "Hint: three words -- the ONLY condition that matters",
     "I will be fine as long as I board before midnight.",
     '"I will be fine ', ' I board before midnight."'),
    ("voucher", "Hint: the paper that pays for the dinner and the hotel -- it is not money",
     "The airline gave me a voucher for dinner at the terminal.",
     '"The airline gave me a ', ' for dinner at the terminal."'),
    ("refund", "Hint: YOUR money back -- not the extra money for the trouble",
     "If they cancel the flight and I do not fly, I will request a refund.",
     '"If they cancel the flight and I don\'t fly, I will request a ', '."'),
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
    (4, "Take the hotel voucher and find the shuttle at door three."),
    (2, "Ask the agent for the options and offer a condition: any route before eight."),
    (5, "Set three alarms -- check-in at the counter closes at four thirty."),
    (1, "Read the delay notice on your phone and walk to the desk."),
    (3, "Accept the alternative route through Charlotte and confirm the times out loud."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Long Night in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">The night the flight falls apart. Put the steps in the real order &mdash; from the notice on your phone to the alarm in the hotel.</p>')
A('      <div class="order-container" id="order-l4">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l4\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    "My flight has been canceled. What are my options tonight?",
    "If you can get me there before eight, I'll take any route.",
    "Will I get a meal voucher and a hotel voucher for tonight?",
    "Unless there is a seat tonight, I'll end up sleeping at the airport.",
    "I'd like to file a complaint and request compensation.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, say it out loud, and only then record. Watch the stressed syllable, which in English breaks the whole word when it lands in the wrong place: <em>voucher</em> (VOW-cher, the VOU rhymes with NOW), <em>compensation</em> (com-pen-SAY-shun), <em>insurance</em> (in-SHOOR-ans), <em>complaint</em> (com-PLAYNT, with an audible final T). And the <em>I&#8217;ll</em> almost disappears in fast speech &mdash; and that is correct.</p>')
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
    ("The board says CANCELED and you reach the desk. What is your FIRST sentence?",
     [("\"This is absurd! I have a meeting tomorrow!\"", False),
      ("\"Good evening. My flight to New York has been canceled. What are my options tonight?\"", True),
      ("\"I want to speak with your manager, please.\"", False)]),
    ("The agent says the next direct flight is <strong>overbooked</strong>. You offer a condition:",
     [("\"If you can get me into JFK before eight, I'll take any route.\"", True),
      ("\"If you will get me into JFK before eight, I take any route.\"", False),
      ("\"When you get me into JFK, I take any route.\"", False)]),
    ("You are going to wait seven hours in Miami. What does the airline OWE you?",
     [("Nothing &mdash; a delay is the passenger&#8217;s own risk.", False),
      ("A meal <strong>voucher</strong> and, with a long wait, a hotel <strong>voucher</strong> &mdash; but you have to ASK for them.", True),
      ("A free new ticket to any destination in the world.", False)]),
    ("You did not fly and you want the money for the ticket back. You ask for a:",
     [("<strong>compensation</strong> &mdash; because the airline made you lose time.", False),
      ("<strong>refund</strong> &mdash; the money for the service you paid for and did not get.", True),
      ("<strong>voucher</strong> &mdash; a credit to spend at the airport.", False)]),
    ("Which sentence is correct?",
     [("\"Unless they don't rebook me, I will file a complaint.\"", False),
      ("\"Unless they rebook me tonight, I'll end up sleeping at the airport.\"", True),
      ("\"Unless they will rebook me, I end up sleeping at the airport.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the night the trip breaks.</p>')
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
A('        <div class="think-question">Build your plan B for September, out loud. Your flight to New York is delayed in Miami, and your meeting is at nine the next morning. What will you do? Use at least five conditional sentences: "If the flight is canceled, I will..." / "Unless they rebook me tonight, I will..." / "As long as I land before eight, I will be fine." / "If my bag doesn\'t arrive, I will..." / "If the hotel asks for a credit card, I will..." Then finish with the real question: what is the one thing that would still scare you at that desk, in English?</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-4"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
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
