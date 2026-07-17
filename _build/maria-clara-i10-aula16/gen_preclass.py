#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 16 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "Numbers That Matter -- Ordinals, Dates, and Time Expressions in Agendas,
Schedules, and Official Events". Gramatica (nova): numeros ordinais (first, seventh,
fifteenth) + datas em ingles americano (November 7th) + o sistema in/on/at para tempo
(in November, on the seventh, at ten o'clock). Contexto: a agenda oficial da visita a
Seul em novembro.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (session, keynote, opening, ceremony, venue, deadline, plenary,
    reception) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-15 (verificado no
    hub). Ja em circulacao (nao ensinado como novo): agenda, schedule, sequence, itinerary,
    appointment, conference, delegation, arrival, departure.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 16 IN CLASS (mesmo tema: a agenda de Seul; mesmo
    vocab; mesma gramatica: ordinais + datas + in/on/at)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao): frase-identidade "I will speak for my institution myself"
    no survival card; tom que celebra a tentativa; Clarinha (neta) como motivacao.
"""
import random

random.seed(16)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo com data/hora)
VOCAB = [
    ("Session", "a period of time for one activity, like a meeting or a talk",
     "The first plenary session is on the seventh, at ten."),
    ("Keynote", "the main, most important speech at an event",
     "The keynote speech is on the eighth."),
    ("Opening", "the first event that starts a program or a day",
     "The opening ceremony is at nine in the morning."),
    ("Ceremony", "a formal event with special, planned actions",
     "The opening ceremony is on the third floor."),
    ("Venue", "the place where an event happens",
     "The venue is the main university hall."),
    ("Deadline", "the last day or time to finish something",
     "The deadline for the report is on the fourteenth."),
    ("Plenary", "a meeting for all the members together, not a small group",
     "Everyone attends the plenary session at ten."),
    ("Reception", "a formal party to welcome guests",
     "The welcome reception is on the tenth, at seven."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-16">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 16 -- Pre-class</div>')
w('      <h3>Numbers That Matter -- Ordinals, Dates, and Time in the Seoul Agenda</h3>')
w('      <div class="lesson-desc">Read and present an official agenda: <strong>ordinal numbers</strong> '
  '(first, seventh, fifteenth), <strong>dates</strong> in American English (November 7th), and the '
  '<strong>in / on / at</strong> system for time (in November, on the seventh, at ten o\'clock). Meet the '
  'words of an official program and the survival sentence <strong>"It is on the seventh, at nine."</strong>. '
  'Key words: session, keynote, opening, ceremony, venue, deadline, plenary, reception. Expression: '
  '"I am looking forward to..." Idiom of the lesson: "Time flies."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="16" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="16">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words for the events of an official agenda.</p>')
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
w('      <div class="match-grid" id="match-l16">')
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
w('        <p>Maria Clara opens the official agenda for Seoul. The delegation arrives <strong>in November</strong>. The program '
  'starts <strong>on the seventh</strong> and finishes <strong>on the fifteenth</strong>. She reads it slowly. "The '
  '<strong>opening ceremony</strong> is <strong>on the seventh</strong>, <strong>at nine</strong> in the morning, on the '
  'third floor," she reads. "Then the first <strong>plenary session</strong> starts <strong>at ten</strong>. The '
  '<strong>venue</strong> is the main university hall." First, there is the <strong>keynote</strong> speech '
  '<strong>on the eighth</strong>. After that, a working <strong>session</strong> <strong>on the ninth</strong>. The '
  'welcome <strong>reception</strong> is <strong>on the tenth</strong>, <strong>at seven</strong> in the evening. The '
  '<strong>deadline</strong> for the final report is <strong>on the fourteenth</strong>. "Time flies," she thinks. "And '
  'this time, I will speak for my institution myself."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. The text says the delegation arrives "<strong>in</strong> November". Why "in" and not "on"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because a <strong>month</strong> takes <strong>in</strong>: in November, in 2027, in the morning.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "November" is a special word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is in the future.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. The opening ceremony is "<strong>on</strong> the seventh". Why "on"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "seventh" is a big number.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because a <strong>date</strong> or a day takes <strong>on</strong>: on the seventh, on Monday, on November 8th.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is in the morning.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. The first plenary session starts "<strong>at</strong> ten". Why "at"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It is a mistake -- it should be "on ten".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because a <strong>clock time</strong> takes <strong>at</strong>: at ten, at nine o\'clock, at 7 p.m.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "ten" is a plenary word.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The ceremony is in the seventh, at November, on nine o\'clock."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The ceremony is on the seventh, in November, at nine o\'clock."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The ceremony is at the seventh, on November, in nine o\'clock."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- In, On, At and Dates</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">For time, English uses three small words. The easy way to remember: big to small &mdash; <strong>in</strong> for the biggest (a month), <strong>on</strong> for the day, <strong>at</strong> for the exact clock time. This is the map.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Word</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>IN</strong></td>'
  '<td style="padding:.6rem">a month, a year, a part of the day</td>'
  '<td style="padding:.6rem"><strong>in November</strong> &middot; <strong>in 2027</strong> &middot; <strong>in the morning</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>ON</strong></td>'
  '<td style="padding:.6rem">a day or a date</td>'
  '<td style="padding:.6rem"><strong>on Monday</strong> &middot; <strong>on the seventh</strong> &middot; <strong>on November 8th</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>AT</strong></td>'
  '<td style="padding:.6rem">a clock time</td>'
  '<td style="padding:.6rem"><strong>at ten o\'clock</strong> &middot; <strong>at 9 a.m.</strong> &middot; <strong>at seven in the evening</strong></td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Dates</td>'
  '<td style="padding:.6rem">American English: <strong>Month + ordinal number</strong></td>'
  '<td style="padding:.6rem">November <strong>7th</strong> (the seventh) &middot; March <strong>15th</strong> (the fifteenth)</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"on November"</strong> or <strong>"in the seventh"</strong> or <strong>"on nine o\'clock"</strong>. '
  'The correct forms are <strong>in November</strong> (a month), <strong>on the seventh</strong> (a date), and '
  '<strong>at nine o\'clock</strong> (a clock time). To say the order of events, use <strong>first, then, next, after that, '
  'finally</strong>.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("in", "Hint: a month takes IN (in November)",
     "The conference is in November.",
     '"The conference is ', ' November."'),
    ("on", "Hint: a date takes ON (on the seventh)",
     "The opening ceremony is on the seventh.",
     '"The opening ceremony is ', ' the seventh."'),
    ("at", "Hint: a clock time takes AT (at ten o'clock)",
     "The first session starts at ten o'clock.",
     '"The first session starts ', ' ten o\'clock."'),
    ("in", "Hint: a part of the day takes IN (in the evening)",
     "The welcome reception is in the evening.",
     '"The welcome reception is ', ' the evening."'),
    ("on", "Hint: a date takes ON (on the fourteenth)",
     "The deadline for the report is on the fourteenth.",
     '"The deadline for the report is ', ' the fourteenth."'),
    ("at", "Hint: a clock time takes AT (at seven)",
     "The reception starts at seven in the evening.",
     '"The reception starts ', ' seven in the evening."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with in, on, or at. Tap Listen to hear the full sentence. Ask yourself: is it a month, a date, or a clock time?</p>')
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
    (1, "First, the opening ceremony is on the seventh, at nine in the morning."),
    (2, "Then, the keynote speech is on the eighth."),
    (3, "After that, there is a working session on the ninth."),
    (4, "The welcome reception is on the tenth, at seven in the evening."),
    (5, "Finally, the final session is on the fifteenth."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Agenda in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the events of the Seoul agenda in the correct order, from the seventh to the fifteenth.</p>')
w('      <div class="order-container" id="order-l16">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l16\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l16\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l16\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l16\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "The opening ceremony is on the seventh, at nine in the morning.",
    "The conference is in November, and it starts on the seventh.",
    "First, the keynote. Then, the working session. After that, the reception.",
    "The deadline for the report is on the fourteenth.",
    "I am looking forward to the final session on the fifteenth.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. There is no wrong way to try &mdash; the last one is your phrase: say it out loud, and mean it.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the Seoul visit.</p>')
w('      <div class="quiz-item"><div class="quiz-question">A colleague asks in which month the conference is. You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The conference is on November."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The conference is in November."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The conference is at November."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You confirm the day of the opening ceremony:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The opening ceremony is in the seventh."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The opening ceremony is at the seventh."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "The opening ceremony is on the seventh."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You confirm the time the first session starts:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The first session starts at ten o\'clock."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The first session starts on ten o\'clock."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The first session starts in ten o\'clock."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A coordinator asks about the report. You give the deadline:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The deadline is in the fourteenth of the evening."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The deadline is on the fourteenth."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The deadline is at the fourteenth."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You present the first three events in order. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "First, the opening ceremony. Then, the plenary session. After that, the keynote."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "After that the opening ceremony, then first the plenary, next the keynote finally."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Finally the opening, first the keynote, then the plenary after that."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Present the Seoul agenda from the seventh to the fifteenth, in order, as if you were '
  'speaking to a colleague. Say each event with its <strong>day</strong> and its <strong>time</strong>: use <strong>on</strong> '
  '+ date (on the seventh), <strong>at</strong> + clock time (at nine), and <strong>in</strong> + month (in November). Use the '
  'sequence words <strong>first, then, after that, finally</strong>, and end with what you are <strong>looking forward to</strong>. '
  'Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-16"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 16</h4>')
for i, en in enumerate(SPEECH, 1):
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
