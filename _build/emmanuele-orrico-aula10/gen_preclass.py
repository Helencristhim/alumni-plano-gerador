#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 10 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Aula 10 (PAR -> modelo de LEITURA): "How Much and How Many? -- Talking About Patients,
Data and Market Access". Fecha o bloco 6-10.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13 (A2 => ZERO portugues na tela do aluno): vocab card com DEFINICAO EM INGLES,
    matching palavra EN <-> definicao EN, grammar tip em ingles, hints em ingles
    ("Hint: ..."), speech card SEM .speech-translation, survival card SEM .sp-pt.
  - REGRA 22: ZERO palavra das aulas 1-9 como vocab NOVO. As 7 palavras desta aula
    (patient population, coverage, funding, data, evidence, dose, treatment) NAO aparecem
    como vocab card em nenhuma aula 1-9. Colisoes do curriculo (reimbursement -> aula 5;
    market access / access -> aula 3) foram DESCARTADAS de proposito e substituidas por
    itens novos do dominio clinico/dados.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 10 IN CLASS (mesmo tema: os numeros do acesso
    a mercado; MESMO vocab das 7 palavras; mesma gramatica: how many / how much + a lot of /
    a few / several / a little + o chunk 'used to')
  - GRAMATICA da aula: contaveis x incontaveis aplicados a dados clinicos + 'several' (novo)
    + o chunk 'used to' (passado que nao e mais verdade hoje) -- introduzido formalmente.
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma explicito): NUNCA nomear "verbo to be" -- nem "contaveis/incontaveis"
    como rotulo. A regra e ensinada por UMA pergunta pratica: "can you count it?".
"""
import random

random.seed(10)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada TAMBEM no matching), exemplo)
VOCAB = [
    ("Patient population", "all the people who have a disease and can take a treatment",
     "The patient population is large, and it is growing."),
    ("Coverage", "how much a health plan or the public system pays for a treatment",
     "Several new programs give better coverage in the private sector."),
    ("Funding", "the money that pays for a program or a treatment",
     "There is not much public funding yet."),
    ("Data", "the numbers and facts about results",
     "We have more data every quarter."),
    ("Evidence", "facts and studies that show a treatment works",
     "We have a lot of new evidence for the higher dose."),
    ("Dose", "the amount of a medicine a patient takes at one time",
     "There is a lot of evidence for the new dose."),
    ("Treatment", "the medical care and medicine a doctor gives to a patient",
     "The patient population for the dermatology treatment is large."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-10">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 10 -- Pre-class</div>')
w('      <h3>How Much and How Many? -- Talking About Patients, Data and Market Access</h3>')
w('      <div class="lesson-desc">The last lesson of the block: the numbers Global always asks for. '
  'How many patients can take the treatment, how much evidence there is for the dose, how much access there '
  'is in the public sector &mdash; and how to say what changed. Key words: patient population, coverage, funding, '
  'data, evidence, dose, treatment. Structures: <strong>how many</strong> x <strong>how much</strong>, the '
  'quantifiers <strong>a lot of</strong>, <strong>a few</strong>, <strong>several</strong>, <strong>a little</strong> '
  'and <strong>not much</strong> &mdash; one question decides them all: <em>can you count it?</em> &mdash; and the '
  'chunk <strong>used to</strong> for the past that is not true today.</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="10" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="10">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the seven words of market access &mdash; the words Global uses when they ask about your numbers.</p>')
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
w('      <div class="match-grid" id="match-l10">')
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
w('        <p>It is the business review, and Marc wants the numbers. "So, how many patients can take this '
  '<strong>treatment</strong>?" he asks. "The <strong>patient population</strong> is large, and it is growing," '
  'Emmanuele answers. "And <strong>how much</strong> evidence do we have for the higher <strong>dose</strong>?" '
  '&mdash; "<strong>A lot of</strong> new <strong>evidence</strong>, and more <strong>data</strong> every quarter."</p>')
w('        <p style="margin-top:.8rem">Then the access. "In the private sector there are <strong>several</strong> new '
  'programs, so <strong>coverage</strong> is better." Then the difficult part, and she does not apologize for it. '
  '"In the public sector there is not <strong>much</strong> <strong>funding</strong> yet, and the reimbursement '
  'decision is slow."</p>')
w('        <p style="margin-top:.8rem">Marc nods. "And two years ago?" &mdash; "Two years ago there <strong>used to</strong> '
  'be almost no access, so this is real progress. Patients <strong>used to</strong> wait a long time. Are there '
  '<strong>any</strong> updates on the reimbursement from your side?"</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why does Marc ask "<strong>How many</strong> patients" and not "How much patients"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because you can COUNT them: one patient, two patients, three patients. Things you can count take <strong>how many</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "patients" is a short word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a question, and every question uses "how many".</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. And why does he ask "<strong>How much</strong> evidence" in the next line?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "evidence" is already a plural word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because you CANNOT count it: nobody says "one evidence, two evidences". Things you cannot count take <strong>how much</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the question is about money.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. She says "<strong>several</strong> new programs" and "not <strong>much</strong> funding". Why are the two words different?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "programs" is a good thing and "funding" is a bad thing.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the first sentence is affirmative and the second one is negative &mdash; only for that.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because you can count <strong>programs</strong> (one program, two programs) &rarr; <strong>several</strong>. And you cannot count <strong>funding</strong> &rarr; <strong>much</strong>.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. What does "<strong>used to</strong>" tell us in "there used to be almost no access"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That there is still almost no access today.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That it was true in the past, but it is NOT true today &mdash; the access is better now.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she uses the access every day.</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- One question decides everything: can you count it?</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Before you choose the word, count in your head: one patient, two patients &mdash; yes, you can count it. One evidence, two evidences &mdash; no, that does not exist. And to compare the past with today, one small chunk does the work: <strong>used to</strong>.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>how many</strong> &middot; <strong>a few</strong> &middot; <strong>several</strong></td>'
  '<td style="padding:.6rem">For things you CAN count: 1 patient, 2 patients, 3 programs.</td>'
  '<td style="padding:.6rem"><strong>How many</strong> patients? &middot; We have <strong>several</strong> new programs.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>how much</strong> &middot; <strong>a little</strong></td>'
  '<td style="padding:.6rem">For things you CANNOT count. You never say "two evidences".</td>'
  '<td style="padding:.6rem"><strong>How much</strong> evidence? &middot; We have <strong>a little</strong> funding.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>a lot of</strong></td>'
  '<td style="padding:.6rem">It works for BOTH &mdash; your safety net. When you are not sure, use this one.</td>'
  '<td style="padding:.6rem"><strong>a lot of</strong> patients &middot; <strong>a lot of</strong> evidence</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>used to</strong> + verb</td>'
  '<td style="padding:.6rem">The past that is NOT true today. The verb stays in its base form (used to <strong>be</strong>, used to <strong>wait</strong>).</td>'
  '<td style="padding:.6rem">There <strong>used to</strong> be little access. &middot; Patients <strong>used to</strong> wait a long time.</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">The list to learn by heart</td>'
  '<td style="padding:.6rem" colspan="2">You never count these words in English: <strong>data</strong>, <strong>evidence</strong>, <strong>access</strong>, <strong>funding</strong>, <strong>coverage</strong>, <strong>information</strong>. '
  'They have no plural, and they never take "a": never "an evidence", never "two datas".</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  '<strong>"many evidence"</strong> and <strong>"how much patients"</strong> &mdash; both are wrong, and both for the same reason: the wrong word for the wrong side of the question. '
  'The quick fix: count first. <em>One patient, two patients</em> &rarr; you can count it &rarr; <strong>many / several</strong>. '
  '<em>One evidence, two evidences?</em> &rarr; that does not exist &rarr; <strong>much / a little</strong>. '
  'And after <strong>used to</strong>, the verb stays in its base form: <strong>used to be</strong>, never "used to been".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("many", "Hint: you can count patients -- one patient, two patients",
     "How many patients can take this treatment?",
     '"How ', ' patients can take this treatment?"'),
    ("much", "Hint: you cannot count evidence -- nobody says two evidences",
     "How much evidence do we have for the dose?",
     '"How ', ' evidence do we have for the dose?"'),
    ("a lot of", "Hint: the safety net -- it works for both sides (three words)",
     "We have a lot of new data this quarter.",
     '"We have ', ' new data this quarter."'),
    ("several", "Hint: you can count programs, and it means more than a few",
     "There are several new programs in the private sector.",
     '"There are ', ' new programs in the private sector."'),
    ("much", "Hint: you cannot count funding, and the sentence is negative",
     "There is not much public funding yet.",
     '"There is not ', ' public funding yet."'),
    ("used to", "Hint: the past that is not true today (two words)",
     "Two years ago there used to be almost no access.",
     '"Two years ago there ', ' be almost no access."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Before you write, ask the question: <strong>can you count it?</strong> Tap Listen to hear the full sentence.</p>')
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
    (1, "Good morning, Marc. Here is the market access update for Brazil."),
    (2, "The patient population is large, and it is growing."),
    (3, "We have a lot of new evidence for the higher dose, and several new programs in the private sector."),
    (4, "But there is not much public funding yet, and the reimbursement decision is slow."),
    (5, "Two years ago there used to be almost no access, so this is real progress."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Update in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the update in the correct order, from the opening to the closing. Look at the professional pattern: good news first, problem after, the change at the end.</p>')
w('      <div class="order-container" id="order-l10">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l10\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l10\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l10\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l10\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "The patient population is large, and it is growing.",
    "We have a lot of new evidence for the higher dose.",
    "There are several new programs in the private sector.",
    "There is not much public funding yet.",
    "Two years ago there used to be almost no access.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of the data update. Note: <strong>data</strong> is DAY-ta (American), <strong>evidence</strong> is strong on the first part (E-vi-dence), and <strong>used to</strong> sounds like "USE-to".</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the business review with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc asks: "How many patients can take this treatment?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "There is much patients in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The patient population is large, and it is growing."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have a little patients who can take it."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks how much evidence there is for the higher dose. The safe way is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We have a lot of new evidence for the higher dose."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We have many evidence for the higher dose."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have many evidences for the higher dose."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to report the new private-sector programs, which you can count. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "There is much programs in the private sector."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "There are several new programs in the private sector."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "There is a little programs in the private sector."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Now the difficult part: almost no money in the public sector. You report:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am very sorry, there is not many funding."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "There is not much public funding yet, and the decision is slow."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "There are not much fundings in the public sector."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to compare today with two years ago. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Two years ago there used to been almost no access."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Two years ago there used to be almost no access, so this is real progress."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Two years ago there use to be almost no access."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for two minutes, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Marc Dubois asks you one question in the business review: "Can you tell me about '
  'patient access for your main products in Brazil?" Give him the picture for a REAL product of yours (atopic '
  'dermatitis, asthma or COPD), in this order: (1) open it -- "Here is the market access update for..."; (2) the '
  'things you can COUNT (how many patients, how many programs); (3) the things you CANNOT count (how much evidence, '
  'how much funding, how much access); (4) the problems -- say them honestly, and do not apologize for them; '
  '(5) compare today with the past using "used to" ("Two years ago there used to be..."); and (6) ask him one '
  'question back ("Are there any updates on the reimbursement?"). Use at least four quantifiers (a lot of, several, '
  'a few, not much). Speak for two minutes. Do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-10"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 10</h4>')
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
