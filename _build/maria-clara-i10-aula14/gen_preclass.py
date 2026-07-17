#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 14 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "Verbs That Take 'To' and Verbs That Take '-ing'" -- fazer planos, expressar
preferencias e navegar conversas institucionais (Maceio <-> Seul). Gramatica (nova):
verbo + to-infinitive (want to, need to, decide to, hope to, arrange to, tend to, prefer to)
vs. verbo + gerund (enjoy, avoid, keep, postpone, mind + -ing), + a armadilha
"looking forward TO meetING".

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (improve, hope, arrange, tend, prefer, keep, postpone, mind) sao
    DISJUNTAS do conjunto de vocab-card-word das aulas 1-13 (verificado no hub). As do
    curriculo que COLIDIAM foram trocadas: suggest, consider, avoid ja eram vocab-card;
    manage ja era "To manage". Em circulacao (nao ensinado como novo): confirm, appointment,
    conference, delegation, prepare, schedule, arrive, present.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 14 IN CLASS (mesmo tema: planos e preferencias
    para Seul; mesmo vocab; mesma gramatica: verb + to vs verb + -ing)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao): frase-identidade "I want to lead the meeting myself"
    no survival card; tom que celebra a tentativa; Clarinha (neta) como motivacao.
"""
import random

random.seed(14)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo com verb pattern)
VOCAB = [
    ("Improve", "to make something better than before",
     "I want to improve my English before November."),
    ("Hope", "to want something good to happen in the future",
     "I hope to travel without an interpreter."),
    ("Arrange", "to plan and organize a time for something",
     "I arranged to meet the rector at nine."),
    ("Tend", "to usually do something, as a habit",
     "I tend to prepare my meetings early."),
    ("Prefer", "to like one thing more than another one",
     "I prefer to speak English now, not Portuguese."),
    ("Keep", "to continue doing something, again and again",
     "I keep practicing every day, even when I am tired."),
    ("Postpone", "to move something to a later day or time",
     "We decided to postpone the budget call to Friday."),
    ("Mind", "to be bothered by something -- used in polite requests",
     "Would you mind repeating that, please?"),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-14">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 14 -- Pre-class</div>')
w('      <h3>Verbs That Take \'To\' and Verbs That Take \'-ing\' -- Making Plans</h3>')
w('      <div class="lesson-desc">Make plans and say what you prefer with the two verb patterns: '
  '<strong>verb + TO</strong> (want, need, decide, hope, arrange, tend, prefer) and '
  '<strong>verb + -ING</strong> (enjoy, avoid, keep, postpone, mind). Meet the false-friend trap '
  '<strong>"I am looking forward to meeting you"</strong> (here "to" is a preposition), and the '
  'survival phrase <strong>"Would you mind...?"</strong>. Key words: improve, hope, arrange, tend, '
  'prefer, keep, postpone, mind. Expression: "I am looking forward to..." Idiom of the lesson: '
  '"Keep it up."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="14" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="14">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight verbs for making plans and saying what you prefer.</p>')
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
w('      <div class="match-grid" id="match-l14">')
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
w('        <p>Maria Clara is planning the delegation to Seoul. "I <strong>want to improve</strong> my English before November," she '
  'tells Bruno, "so I <strong>keep practicing</strong> every morning." Bruno has good news: he <strong>arranged to meet</strong> the '
  'Korean team on Monday. The rector <strong>hopes to join</strong> the first dinner, but he <strong>tends to arrive</strong> late, so '
  'they do not worry. Maria Clara <strong>prefers to travel</strong> with a small bag, and she <strong>enjoys meeting</strong> new '
  'people at conferences. There is one problem: the budget call is on a bad day, so they <strong>decide to postpone</strong> it to '
  'Friday. "I do not <strong>mind changing</strong> the date," she says. "And I am <strong>looking forward to leading</strong> the '
  'meeting myself." Bruno smiles. "Keep it up," he says.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. She says "I want <strong>to improve</strong>". Why "to improve" and not "improving"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because <strong>want</strong> is a verb + TO verb. Want, need, decide, hope take <strong>to</strong> + the base verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "improve" cannot take -ing.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is in the future.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. She says "I <strong>keep practicing</strong>". Why "practicing" and not "to practice"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "practice" is a special word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because <strong>keep</strong> is a verb + -ING verb. Keep, enjoy, avoid, mind take the verb + <strong>-ing</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because she does it in the morning.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "I am <strong>looking forward to leading</strong>." Why "leading" and not "to lead"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It is a mistake -- it should be "to lead".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because in "looking forward <strong>to</strong>" the "to" is a PREPOSITION, so the verb takes <strong>-ing</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "lead" has no -ing form.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I want improving my English, and I enjoy to meet new people."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I want to improve my English, and I enjoy meeting new people."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I want to improving my English, and I enjoy meet new people."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Verb + To and Verb + -ing</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">After a first verb, English chooses one of two patterns. There is no easy rule &mdash; you learn the verbs in two groups. This is the map.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Pattern</th><th style="padding:.7rem;text-align:left">These verbs</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">verb + <strong>TO</strong> + base verb</td>'
  '<td style="padding:.6rem">want, need, decide, plan, hope, would like, arrange, tend, prefer</td>'
  '<td style="padding:.6rem">I <strong>want to improve</strong>. &middot; I <strong>hope to travel</strong>.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">verb + <strong>-ING</strong></td>'
  '<td style="padding:.6rem">enjoy, avoid, finish, consider, suggest, keep, postpone, mind</td>'
  '<td style="padding:.6rem">I <strong>enjoy meeting</strong>. &middot; I <strong>keep practicing</strong>.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Polite request: <strong>Would you mind</strong> + <strong>-ing</strong></td>'
  '<td style="padding:.6rem">The soft way to ask for something. Answer "Not at all" to say yes.</td>'
  '<td style="padding:.6rem"><strong>Would you mind repeating</strong> that?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Trap: <strong>looking forward to</strong> + <strong>-ing</strong></td>'
  '<td style="padding:.6rem">Here <strong>to</strong> is a PREPOSITION, not an infinitive &mdash; so the verb takes <strong>-ing</strong>, not the base form.</td>'
  '<td style="padding:.6rem">I am <strong>looking forward to meeting</strong> you. (NOT "to meet")</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"I want improving"</strong> or <strong>"I enjoy to meet"</strong>. Swap them: it is '
  '<strong>I want to improve</strong> (want takes TO) and <strong>I enjoy meeting</strong> (enjoy takes -ING). '
  'And after <strong>looking forward to</strong>, always use <strong>-ing</strong>.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("to improve", "Hint: want + TO + base verb",
     "I want to improve my English before November.",
     '"I want ', ' my English before November."'),
    ("meeting", "Hint: enjoy + verb-ING",
     "I enjoy meeting new people at conferences.",
     '"I enjoy ', ' new people at conferences."'),
    ("to meet", "Hint: arrange + TO + base verb",
     "She arranged to meet the rector at nine.",
     '"She arranged ', ' the rector at nine."'),
    ("practicing", "Hint: keep + verb-ING",
     "I keep practicing every morning.",
     '"I keep ', ' every morning."'),
    ("repeating", "Hint: Would you mind + verb-ING",
     "Would you mind repeating that, please?",
     '"Would you mind ', ' that, please?"'),
    ("to leading", "Hint: after looking forward TO, use -ING (to = preposition)",
     "I am looking forward to leading the meeting.",
     '"I am looking forward ', ' the meeting."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence. Ask yourself: does this verb take TO or -ING?</p>')
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
    (1, "First, I decide to lead the delegation myself, without an interpreter."),
    (2, "Then, I arrange to meet an English teacher every week."),
    (3, "I keep practicing every morning, even when I am tired."),
    (4, "I want to improve my speaking, so I avoid staying silent in meetings."),
    (5, "Finally, I am looking forward to speaking for my institution in Seoul."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Plan in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of Maria Clara\'s English plan in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l14">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l14\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l14\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l14\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l14\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "I want to improve my English, so I keep practicing.",
    "I arranged to meet the Korean team on Monday.",
    "I enjoy meeting new people, but I avoid speaking in large groups.",
    "Would you mind repeating that, please?",
    "I want to lead the meeting myself.",
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of planning the trip to Seoul.</p>')
w('      <div class="quiz-item"><div class="quiz-question">A colleague offers you an interpreter for the meeting. You want to speak yourself. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Thank you, but I prefer speak English myself."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Thank you, but I prefer to speak English myself."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Thank you, but I prefer to speaking English myself."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A waiter in Seoul speaks very fast. You ask him politely to say it again:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Would you mind to repeat that, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Would you mind repeat that, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Would you mind repeating that, please?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The meeting is on a bad day. You ask to move it to Friday:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Can we postpone the meeting to Friday?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Can we postpone to meet on Friday?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Can we postpone meeting the Friday?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The rector asks about your goal this year. You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I hope improving my English and I keep to study."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I hope to improve my English, and I keep studying every day."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I hope to improving my English, and I keep to studying."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You are excited about the trip. You tell Bruno:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am looking forward to meet the Korean team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am looking forward to meeting the Korean team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am looking forward meet the Korean team."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Tell your English journey in one or two minutes. Say what you '
  '<strong>want to</strong> improve this year, what you <strong>enjoy</strong> doing in English, and what you '
  '<strong>avoid</strong> or find difficult. Say what you <strong>keep</strong> doing to get better, and what you '
  'are <strong>looking forward to</strong> in Seoul. Use verb + to (want, hope, decide) and verb + -ing (enjoy, avoid, '
  'keep). Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-14"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 14</h4>')
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
