#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 17 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "Small Talk That Works" -- abrir, sustentar e fechar conversas em jantares e round
tables internacionais (Seul). Foco funcional (NAO nova estrutura gramatical): openers +
follow-up questions -- perguntas para abrir e reacoes+perguntas para sustentar.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (introduce, host, guest, impression, topic, conversation,
    background, polite) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-16
    (verificado no hub -- 'reception' ja existia, por isso ficou DE FORA). Expressoes:
    'By the way' (em circulacao desde a aula 15 de review) e o idioma NOVO 'Break the ice'
    (inedito no roster). Em circulacao (nao ensinado como novo): conference, delegation,
    institution, colleague, partner, formal.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 17 IN CLASS (mesmo tema: small talk no jantar
    de Seul; mesmo vocab; mesma logica: open / sustain / close)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao): frase-identidade "I speak English, and I am improving"
    no survival card; reframe "small talk has rules, and rules can be learned"; tom que
    celebra a tentativa; Clarinha (neta) como motivacao.
"""
import random

random.seed(17)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo)
VOCAB = [
    ("Introduce", "to tell your name, or to present one person to another",
     "Let me introduce myself: I am Maria Clara, from Brazil."),
    ("Host", "the person who organizes an event and receives the guests",
     "The host welcomed every guest at the door."),
    ("Guest", "a person who is invited to an event or a place",
     "I am a guest at the conference dinner tonight."),
    ("Impression", "the opinion people form about you when they first meet you",
     "A warm smile makes a good first impression."),
    ("Topic", "the subject you talk about in a conversation",
     "The weather is an easy topic to start with."),
    ("Conversation", "a talk between two or more people",
     "We had a short conversation before the session."),
    ("Background", "your job, your studies, and your work experience",
     "Tell me a little about your background."),
    ("Polite", "kind and respectful in the way you speak and act",
     "It is polite to ask about the other person too."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-17">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 17 -- Pre-class</div>')
w('      <h3>Small Talk That Works -- The Round Table</h3>')
w('      <div class="lesson-desc">Open, sustain, and close a conversation at an international dinner in Seoul: '
  'start with an easy <strong>question</strong>, react and ask back to keep it going, shift the topic gently with '
  '<strong>by the way</strong>, and close warmly. Key words: introduce, host, guest, impression, topic, conversation, '
  'background, polite. The three moves: <strong>open</strong> (a question), <strong>sustain</strong> (react + ask back), '
  'and <strong>close</strong> (a warm thank-you). Expression: "By the way." Idiom of the lesson: "Break the ice."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="17" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="17">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words of small talk at a dinner.</p>')
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
w('      <div class="match-grid" id="match-l17">')
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
w('        <p>At the conference dinner in Seoul, Maria Clara sits next to a <strong>guest</strong> she does not know. The '
  '<strong>host</strong> asked everyone to talk, so she decides to <strong>break the ice</strong>. She does not start with '
  'a flat statement; she <strong>opens</strong> with an easy question: <strong>"Is this your first time in Seoul?"</strong> '
  'The guest smiles and answers. To keep the <strong>conversation</strong> going, Maria Clara reacts and asks back: '
  '<strong>"That\'s interesting! And what about you?"</strong> Then she moves to a new <strong>topic</strong>: '
  '<strong>"By the way, what is your background?"</strong> It is <strong>polite</strong> to ask about the other person too. '
  'They talk for a few minutes, and she makes a great first <strong>impression</strong>. When it is time to leave, she does '
  'not stop in silence; she <strong>closes</strong> warmly: <strong>"It was really nice talking with you."</strong> Later, she '
  'wants to <strong>introduce</strong> the guest to a colleague from Brazil.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. How does Maria Clara OPEN the conversation?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> With a flat statement: "This is your first time in Seoul."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> With an easy <strong>question</strong>: "Is this your first time in Seoul?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> In silence, waiting for the guest to speak first.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. To SUSTAIN the conversation, what does she do?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She only answers, and then she stops.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She REACTS and then ASKS a question back: "That\'s interesting! And what about you?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She changes the table.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. What does "<strong>By the way</strong>" do in the text?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It closes the conversation.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It moves to a new <strong>topic</strong> gently, so the change feels natural.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It says goodbye.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence CLOSES a conversation the right way?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What you do at the university?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It was really nice talking with you."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You are from where?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Open, Sustain, Close</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Small talk has three moves. You OPEN with a question, you SUSTAIN by reacting and asking back, and you CLOSE with a warm thank-you. This is how you break the ice with anyone.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Move</th><th style="padding:.7rem;text-align:left">What you do</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>Open</strong></td>'
  '<td style="padding:.6rem">Start with an easy question, never a flat statement. Remember the helper: <strong>do</strong> or <strong>are</strong>, and the question word first.</td>'
  '<td style="padding:.6rem"><strong>Is this</strong> your first time here? &middot; <strong>How are you finding</strong> it?</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>Sustain</strong></td>'
  '<td style="padding:.6rem">React with a short response, then ASK A QUESTION BACK. This keeps the ball moving.</td>'
  '<td style="padding:.6rem">That\'s interesting! <strong>And what about you?</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>Shift topic</strong></td>'
  '<td style="padding:.6rem">Move to a new topic gently, so the change feels natural.</td>'
  '<td style="padding:.6rem"><strong>By the way,</strong> what is your background?</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>Close</strong></td>'
  '<td style="padding:.6rem">End with a warm thank-you, never in silence.</td>'
  '<td style="padding:.6rem"><strong>It was really nice talking with you.</strong></td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready phrase: <strong>Break the ice.</strong></td>'
  '<td style="padding:.6rem">One idiom. It means to say the first friendly words so people feel relaxed. You break the ice with an easy question.</td>'
  '<td style="padding:.6rem">"A simple question is the best way to <strong>break the ice</strong>."</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"What you do?"</strong> or <strong>"You are from where?"</strong>. A question needs its helper and '
  'the question word first: it is <strong>"What do you do?"</strong> and <strong>"Where are you from?"</strong>. And never end '
  'in silence &mdash; always close with <strong>"It was really nice talking with you."</strong></p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("Is this", "Hint: an opener is a question, not a statement",
     "Is this your first time in Seoul?",
     '"', ' your first time in Seoul?"'),
    ("How are you finding", "Hint: use are + the -ing form to ask an open question",
     "How are you finding the conference so far?",
     '"', ' the conference so far?"'),
    ("And what about you", "Hint: react, then ask the question back",
     "That's interesting! And what about you?",
     '"That\'s interesting! ', '?"'),
    ("By the way", "Hint: a soft way to move to a new topic",
     "By the way, what do you do exactly?",
     '"', ', what do you do exactly?"'),
    ("really nice talking", "Hint: close a conversation warmly, never in silence",
     "It was really nice talking with you.",
     '"It was ', ' with you."'),
    ("break the ice", "Hint: the idiom for the first friendly words",
     "A simple question is the best way to break the ice.",
     '"A simple question is the best way to ', '."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence. Ask yourself: does it open, sustain, shift, or close?</p>')
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
    (1, "First, you introduce yourself and open with an easy question."),
    (2, "Then, the other person answers, and you react with a short response."),
    (3, "You ask a question back to keep the conversation going."),
    (4, "After that, you shift to a new topic and say \"by the way\"."),
    (5, "Finally, you close the conversation warmly and say goodbye."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a small-talk conversation in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l17">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l17\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l17\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l17\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l17\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Is this your first time in Seoul?",
    "How are you finding the conference so far?",
    "That's interesting! And what about you?",
    "By the way, what is your background?",
    "It was really nice talking with you.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. There is no wrong way to try &mdash; these are the exact phrases you will use at the dinner.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the conference dinner.</p>')
w('      <div class="quiz-item"><div class="quiz-question">You sit next to a guest you do not know. You want to break the ice. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You are from where?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Hi, I\'m Maria Clara. Is this your first time in Seoul?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This is your first time in Seoul."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The guest tells you the food is wonderful. To keep the conversation going, you say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I know what you mean! And what about you &mdash; are you enjoying the conference?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Yes." (and then silence)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Goodbye, it was nice."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">There is a silence, and you want to change the topic. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Stop. New topic now."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "By the way, how are you finding the city?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "What you think about the city?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ask the guest about their work in a polite way. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What you do?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "So, what is your background? What do you do exactly?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You work where and why?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">It is time to leave the table. You close the conversation. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> (nothing &mdash; you just stand up and leave)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It was really nice talking with you. I hope we can continue later."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Finish. Bye."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">You meet a new guest at the Seoul conference dinner. Speak both sides of a short '
  'conversation: open with an easy question, react and ask a question back, shift the topic with "by the way", ask about '
  'their background in a polite way, and close warmly with "It was really nice talking with you." Take your time and do '
  'not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-17"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 17</h4>')
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
