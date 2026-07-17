#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 15 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

AULA 15 = MILESTONE REVIEW / FLUENCY SESSION ("Putting It All Together -- From Maceio
to Seoul"). Consolidacao das aulas 1-14 numa simulacao de Seul em 3 atos (recepcao /
round table / jantar-debrief). Portanto:
  - VOCAB e REUSADO DE PROPOSITO (nao 8 palavras ineditas): as 8 palavras-chave do dia da
    conferencia (delegation, conference, agenda, colleague, clarify, priority, recommend,
    debrief) JA foram ensinadas nas aulas 1-14. O check_vocab_progression vai acusar
    repeticao -- o conserto correto e a whitelist vocab_allow_repeat.json (aula de review).
  - GRAMATICA e REVISADA, nao nova: o Grammar Tip e uma CAIXA DE FERRAMENTAS de TODOS os
    tempos ja vistos (present/past/future/comparativos/modais/verb+to/-ing). Sem
    grammar_point novo no config -> o slide de grammar do IN CLASS nao emite data-grammar
    e o check_grammar_progression ignora a aula (alem da isencao por titulo "Milestone Review").

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => ZERO portugues na tela da aluna (definicao em ingles simples; instrucoes,
    hints, quiz, grammar tip e survival todos em ingles). PT so no data-teacher / Planejamento.
  - REGRA 29: o Pre-class PREVIEWA a aula 15 IN CLASS (mesmo tema: a simulacao de Seul;
    mesmo vocab; a mesma revisao de tempos). Aula de review = isenta do gate de coerencia.
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao / sensacao de nunca avancar): frase-identidade
    "I speak English, and I am improving" no survival card; tom que celebra a tentativa;
    Clarinha (neta) como motivacao; enquadramento de um TERCO do programa cumprido.
"""
import random

random.seed(15)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2, exemplo da simulacao de Seul) -- TODAS review
VOCAB = [
    ("Delegation", "a group of people who represent an institution at an event",
     "I lead the delegation from my university to Seoul."),
    ("Conference", "a large formal meeting where people share ideas and work",
     "The leadership conference in Seoul lasts three days."),
    ("Agenda", "the list of things to do or discuss, in order",
     "The first item on the agenda is the welcome reception."),
    ("Colleague", "a person you work with",
     "I met a colleague from a university in Portugal."),
    ("Clarify", "to make something clearer, to explain it better",
     "Could you clarify the second question, please?"),
    ("Priority", "the most important thing, the one you do first",
     "My priority is to present our work clearly."),
    ("Recommend", "to say that something is good and that someone should do it",
     "I recommend that we arrive early tomorrow."),
    ("Debrief", "a short meeting after an event to talk about how it went",
     "At the dinner debrief, we talked about the whole day."),
]

# As 5 frases que se repetem: safety net (slide 14) = survival card (slide 31) =
# Stage 3 pronuncia = survival do Pre-class. Reuso de audio proposital.
SPEECH = [
    "Hello, I am Maria Clara. I lead the delegation from my university.",
    "In my opinion, we should start with the main topic.",
    "Sorry, would you mind repeating that?",
    "No problem. I will handle the introduction.",
    "I speak English, and I am improving.",
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-15">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1538485399081-7191377e8241?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 15 -- Pre-class</div>')
w('      <h3>Milestone Review -- From Maceio to Seoul</h3>')
w('      <div class="lesson-desc">One third of the program is done. This is a <strong>review</strong>: '
  'you put it all together in a full Seoul simulation in three acts &mdash; the welcome '
  '<strong>reception</strong>, the <strong>round table</strong>, and the dinner <strong>debrief</strong>. '
  'No new grammar: you activate everything from Lessons 1 to 14 &mdash; present, past, future, '
  'comparatives, modals, and verb + to / -ing. Review words: delegation, conference, agenda, '
  'colleague, clarify, priority, recommend, debrief.</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="15" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="15">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You already know these eight words. Listen, read the example, and remember them &mdash; they are the words of a full conference day in Seoul.</p>')
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
w('      <div class="match-grid" id="match-l15">')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the story of the day and answer the questions. Notice all the tenses you already know.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>Maria Clara <strong>leads</strong> the <strong>delegation</strong> from her university &mdash; that is her role, '
  'every day. Right now, she <strong>is standing</strong> at the welcome reception in Seoul, and she <strong>is speaking</strong> '
  'English with no interpreter. Earlier, while the plane <strong>was landing</strong>, she <strong>reviewed</strong> the whole '
  '<strong>agenda</strong> one more time. At the <strong>conference</strong>, she <strong>met</strong> a <strong>colleague</strong> '
  'from Portugal, and they <strong>talked</strong> about their work. "My <strong>priority</strong> is to present clearly," she said. '
  'The morning <strong>was busier</strong> than she expected, and the interpreter did not arrive, so she thought: "No problem. '
  'I <strong>will handle</strong> the introduction." At the round table, when a speaker went too fast, she asked him to '
  '<strong>clarify</strong>: "Would you mind <strong>repeating</strong> that?" In the evening, at the dinner <strong>debrief</strong>, '
  'she <strong>recommended</strong> that the delegation <strong>should</strong> arrive early tomorrow. "It <strong>was</strong> a good '
  'day," she said. "And tomorrow <strong>is going to be</strong> even better."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. "Maria Clara <strong>leads</strong> the delegation" and "she <strong>is speaking</strong> English." Why two different forms?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Leads" is her role in general (present simple); "is speaking" is happening right now (present continuous).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> They mean exactly the same thing.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Is speaking" is the past of "leads".</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "While the plane <strong>was landing</strong>, she <strong>reviewed</strong> the agenda." What do these two tenses show together?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Two plans for the future.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A longer background action (was landing) and a shorter finished action inside it (reviewed).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she does both things every day.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. The interpreter did not arrive, so she said "I <strong>will handle</strong> the introduction." Why "will"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because it is a past event.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because "will" is for a decision she makes right now, in the moment.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a routine she does every day.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence from the day is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yesterday I meet a colleague, and I am agree with him."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I met a colleague, and I agree with him &mdash; tomorrow is going to be better."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I have 62 years, and I will handle it yesterday."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Your Toolbox (Review)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">No new rule today. This is your <strong>toolbox</strong> &mdash; every tense you built in Lessons 1 to 14, in one place, ready for Seoul. Pick the right tool for the moment.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Tool</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present simple</td>'
  '<td style="padding:.6rem">Who you are, your role, routines.</td>'
  '<td style="padding:.6rem">"I <strong>lead</strong> the delegation."</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present continuous</td>'
  '<td style="padding:.6rem">What is happening right now.</td>'
  '<td style="padding:.6rem">"Right now I <strong>am speaking</strong> English."</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Past simple &amp; continuous</td>'
  '<td style="padding:.6rem">A finished event, and what was happening around it.</td>'
  '<td style="padding:.6rem">"While we <strong>were waiting</strong>, we <strong>reviewed</strong> the agenda."</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">going to / will</td>'
  '<td style="padding:.6rem">Plans and decisions for tomorrow.</td>'
  '<td style="padding:.6rem">"I <strong>will handle</strong> the introduction."</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Comparatives &amp; superlatives</td>'
  '<td style="padding:.6rem">Compare two things, or name the top one.</td>'
  '<td style="padding:.6rem">"This hotel is <strong>better</strong> than the last one."</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Modals: should / could</td>'
  '<td style="padding:.6rem">Advice, options, and recommendations.</td>'
  '<td style="padding:.6rem">"We <strong>should</strong> arrive early. We <strong>could</strong> visit the palace."</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Verb + to / verb + -ing</td>'
  '<td style="padding:.6rem">Plans, preferences, and polite requests.</td>'
  '<td style="padding:.6rem">"I <strong>want to</strong> present. Would you mind <strong>repeating</strong> that?"</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Three habits to watch:</strong> '
  'age is <strong>to be</strong> ("I am 62 years old", never "I have 62 years"); the past changes the verb '
  '("I <strong>met</strong> a colleague", not "I meet"); and <strong>agree</strong> is already a verb '
  '("I <strong>agree</strong>", never "I am agree").</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("am speaking", "Hint: happening right now -- present continuous",
     "Right now I am speaking English at the reception.",
     '"Right now I ', ' English at the reception."'),
    ("met", "Hint: a finished action yesterday -- past simple of meet",
     "Yesterday I met a colleague from Portugal.",
     '"Yesterday I ', ' a colleague from Portugal."'),
    ("was waiting", "Hint: a longer background action -- past continuous",
     "While I was waiting, the interpreter arrived.",
     '"While I ', ', the interpreter arrived."'),
    ("will handle", "Hint: a decision you make now -- will",
     "No problem. I will handle the introduction.",
     '"No problem. I ', ' the introduction."'),
    ("should", "Hint: advice -- a modal verb",
     "We should arrive early for the reception.",
     '"We ', ' arrive early for the reception."'),
    ("to present", "Hint: after want, use verb + to",
     "I want to present our work at the round table.",
     '"I want ', ' our work at the round table."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the right tense. Tap Listen to hear the full sentence. Ask yourself: now, past, or future?</p>')
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
    (1, "First, at the welcome reception, I introduce myself and meet the other delegations."),
    (2, "Then, at ten o'clock, the round table starts, and each institution presents its work."),
    (3, "During the round table, I give my opinion and ask a speaker to clarify a question."),
    (4, "After the sessions, we have lunch and choose one of the afternoon workshops."),
    (5, "Finally, at the dinner debrief, we talk about the day and plan for tomorrow."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Day in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the moments of the conference day in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l15">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l15\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l15\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l15\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l15\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. These are your five phrases for Seoul &mdash; the last one is your phrase: say it out loud, and mean it.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the day in Seoul.</p>')
w('      <div class="quiz-item"><div class="quiz-question">At the reception, a colleague asks: "How was your trip?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "My trip is long yesterday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It was long, but it was fine. While we were waiting, we reviewed the agenda."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am travel and I am agree."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A speaker talks too fast and you miss the question. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Would you mind to repeat that?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, would you mind repeating that?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Repeat, please, I am not understand."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A colleague gives an opinion you do not share. You disagree politely:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I see your point, but in my opinion we should start with the work."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am agree, but no."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You are wrong, and I am right."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The interpreter will not be there, so you handle the introduction. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The interpreter is not here, so I cannot speak."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "No problem. I will handle the introduction."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will handled the introduction tomorrow yesterday."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">At the dinner debrief, a colleague asks what you recommend for tomorrow. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I recommend to arriving late."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I recommend that we arrive early, and we could visit the old palace after the sessions."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We should to arrive early tomorrow."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for two or three minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">This is your first full spoken benchmark: "My Seoul Introduction". Speak as if you are at the '
  'welcome reception on the first evening of the conference. Say who you are, your role, and your institution; something about '
  'your background; one thing you are looking forward to; and one question for your conversation partner. Use present, past, '
  'and future, and close with your phrase: "I speak English, and I am improving." Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-15"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card (A2 = sem sp-pt)
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 15</h4>')
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
