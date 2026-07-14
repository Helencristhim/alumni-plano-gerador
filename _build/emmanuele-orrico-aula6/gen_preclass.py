#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 6 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13 (A2 => ZERO portugues na tela do aluno): vocab card com DEFINICAO EM INGLES
    (sem traducao), matching palavra EN <-> definicao EN, grammar tip em ingles, hints em
    ingles ("Hint: ..."), speech card SEM .speech-translation, survival card SEM .sp-pt,
    instrucoes e quizzes em ingles simples. O portugues so sobrevive onde o aluno NAO ve
    (comentarios, docstring, data-teacher dos slides -- que nao estao neste arquivo).
  - REGRA 13 (densidade A2): 10 palavras novas
  - REGRA 22: ZERO palavra das aulas 1-5 como vocab NOVO. Fora, de proposito (ja ensinadas):
    aula 1: pharmaceutical company / immunology / national manager / field team / global meeting /
            results / launch / disease area / to be responsible for / to manage
    aula 2: schedule / report / field visit / medical rep / demand plan / headquarters /
            to attend / to review / to prepare / to travel
    aula 3: quarter / target / challenge / opportunity / growth / to achieve / to exceed /
            to miss / market access / prescription volume
    aula 4: small talk / congress / colleague / executive / stakeholder / pipeline /
            to introduce / to network / currently / to look forward to
    aula 5: business plan / goal / deadline / strategy / quarterly review / to announce /
            to organize / product approval / reimbursement / global alignment
    Trocas feitas em relacao ao curriculo da aula 6 (que colidia com o que ja foi ensinado):
      launch (v/n) -> campaign      (launch ja e vocab NOVO da aula 1)
      pipeline     -> ongoing       (pipeline ja e vocab NOVO da aula 4)
      currently    -> to focus on   (currently ja e vocab NOVO da aula 4)
    Mantidos do curriculo: roll out, track, on track, update, discuss, milestone.
    Adicionado: progress (ancora INCONTAVEL da gramatica nova).
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 6 IN CLASS (mesmo tema: o update de progresso
    para o time Global; mesmo vocab; mesma gramatica: how many / how much + a lot of /
    a few / a little / some / any)
  - GRAMATICA NOVA (o curriculo pedia present continuous, que JA foi ensinado na aula 4,
    e a aula 7 ja leva o 'will'): contaveis x incontaveis + quantificadores.
    O present continuous entra so como REVISAO em circulacao, nunca como conteudo novo.
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma explicito): NUNCA nomear "verbo to be" -- nem "contaveis/incontaveis"
    como rotulo gramatical na tela do aluno. A regra e ensinada por UMA pergunta pratica:
    "can you count it?".
"""
import random

random.seed(6)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada TAMBEM no matching), exemplo)
VOCAB = [
    ("Campaign", "an organized set of actions to bring a medicine to doctors",
     "The dermatology campaign is on track in eleven centers."),
    ("Milestone", "an important point in a project, where you check if you are on time",
     "The first milestone is complete."),
    ("Update", "new information about the situation of a project",
     "Here is a short update on the campaign."),
    ("Progress", "the movement forward in a project",
     "We have a lot of progress in the private market."),
    ("To roll out", "to start something step by step, in more and more places",
     "We are rolling it out in four more centers this month."),
    ("To track", "to follow the numbers of a project, to see where it is",
     "My team is tracking the delays in the public market."),
    ("On track", "going well -- at the right speed, at the right time",
     "The campaign is on track in eleven centers."),
    ("Ongoing", "happening now, and not finished yet",
     "The roll-out is ongoing in four centers."),
    ("To focus on", "to give your attention and your time to one thing",
     "This month we are focusing on the private market."),
    ("To discuss", "to talk about something with other people, to make a decision",
     "On Friday we are going to discuss the delays."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-6">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 06 -- Pre-class</div>')
w('      <h3>How Is It Going? -- Reporting Progress to the Global Team</h3>')
w('      <div class="lesson-desc">The check-in in the middle of the road: Marc already has the PLAN, now he wants the PROGRESS. '
  'How many centers are on track, how much real progress there is, what the delays are &mdash; and how to say all of that in '
  'three lines, without saying sorry. Key words: campaign, milestone, update, progress, to roll out, to track, on track, ongoing, '
  'to focus on, to discuss. Structures: <strong>how many</strong> x <strong>how much</strong>, and the quantifiers '
  '<strong>a lot of</strong>, <strong>a few</strong>, <strong>a little</strong>, <strong>some</strong> and <strong>any</strong> &mdash; '
  'one question decides all of them: <em>can you count it?</em> Expression of the lesson: "So far, so good."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words of a progress report &mdash; the words the Global team wants to hear on a Friday call.</p>')
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
w('      <div class="match-grid" id="match-l6">')
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
w('        <p>It is Friday, and Marc is on the call. He already has the plan &mdash; today he wants the <strong>progress</strong>. '
  '"So, how is it going?" he asks. Emmanuele opens her <strong>update</strong>. "The first <strong>milestone</strong> is complete, '
  'and the dermatology <strong>campaign</strong> is <strong>on track</strong>."</p>')
w('        <p style="margin-top:.8rem">"<strong>How many</strong> centers are active?" &mdash; "Eleven. And we are <strong>rolling '
  'it out</strong> in four more this month." Marc writes the number down. "And <strong>how much</strong> progress is there in the '
  'private market?" &mdash; "<strong>A lot of</strong> progress," she says. "This month we are <strong>focusing on</strong> the big '
  'hospitals."</p>')
w('        <p style="margin-top:.8rem">Then the difficult part, and she does not apologize for it. "We have <strong>a few</strong> '
  'delays in the public market. There is not <strong>much</strong> information about the reimbursement yet, so my team is '
  '<strong>tracking</strong> it every week. The roll-out there is still <strong>ongoing</strong>." Marc nods. "Are there <strong>any</strong> '
  'problems you cannot solve alone?" &mdash; "Not yet. <strong>So far, so good.</strong> But on Friday I would like to '
  '<strong>discuss</strong> the delays with you."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why does Marc ask "<strong>How many</strong> centers" and not "How much centers"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because you can COUNT them: one center, two centers, three centers. Things you can count take <strong>how many</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "centers" is a short word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a question, and every question uses "how many".</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. And why does he ask "<strong>How much</strong> progress" in the next line?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "progress" is already a plural word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because you CANNOT count it: nobody says "one progress, two progresses". Things you cannot count take <strong>how much</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the question is about money.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. She says "We have <strong>a few</strong> delays" and "there is not <strong>much</strong> information". Why are the two words different?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "delays" is a bad thing and "information" is a good thing.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the first sentence is affirmative and the second one is negative &mdash; only for that.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because you can count <strong>delays</strong> (one delay, two delays) &rarr; <strong>a few</strong>. And you cannot count <strong>information</strong> &rarr; <strong>much</strong>.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which update is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have many progress, and there is not many information about the reimbursement."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have a lot of progress, and there is not much information about the reimbursement."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have much progresses, and there are not much informations about the reimbursement."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- One question decides everything: can you count it?</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Before you choose the word, count in your head: one center, two centers &mdash; yes, you can count it. One progress, two progresses &mdash; no, that does not exist. This one question gives you the answer every time.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>how many</strong> &middot; <strong>a few</strong></td>'
  '<td style="padding:.6rem">For things you CAN count: 1 center, 2 centers, 3 centers.</td>'
  '<td style="padding:.6rem"><strong>How many</strong> centers are on track? &middot; We have <strong>a few</strong> delays.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>how much</strong> &middot; <strong>a little</strong></td>'
  '<td style="padding:.6rem">For things you CANNOT count. You never say "two progresses".</td>'
  '<td style="padding:.6rem"><strong>How much</strong> progress is there? &middot; We have <strong>a little</strong> time.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>a lot of</strong></td>'
  '<td style="padding:.6rem">It works for BOTH &mdash; your safety net. When you are not sure, use this one.</td>'
  '<td style="padding:.6rem"><strong>a lot of</strong> centers &middot; <strong>a lot of</strong> progress</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>some</strong> / <strong>any</strong></td>'
  '<td style="padding:.6rem"><strong>some</strong> = you HAVE it. <strong>any</strong> = you ASK, or you do NOT have it.</td>'
  '<td style="padding:.6rem">We have <strong>some</strong> good news. &middot; Are there <strong>any</strong> updates? &middot; There is not <strong>any</strong> news yet.</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">The list to learn by heart</td>'
  '<td style="padding:.6rem" colspan="2">You never count these words in English: <strong>progress</strong>, <strong>information</strong>, <strong>news</strong>, <strong>time</strong>, <strong>work</strong>, <strong>feedback</strong>. '
  'They have no plural, and they never take "a": never "an information", never "two progresses", never "many feedbacks".</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  '<strong>"many progress"</strong> and <strong>"how much centers"</strong> &mdash; both are wrong, and both for the same reason: the wrong word for the wrong side of the question. '
  'The quick fix: count first. <em>One center, two centers</em> &rarr; you can count it &rarr; <strong>many / a few</strong>. '
  '<em>One progress, two progresses?</em> &rarr; that does not exist &rarr; <strong>much / a little</strong>. '
  'And the most expensive mistake of all: <strong>"an information"</strong>. In English it does NOT exist. '
  'It is always <strong>some information</strong> &mdash; and the same goes for <strong>news</strong> ("The news <strong>is</strong> good", never "the news are").</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("many", "Hint: you can count centers -- one center, two centers",
     "How many centers are active?",
     '"How ', ' centers are active?"'),
    ("much", "Hint: you cannot count progress -- nobody says two progresses",
     "How much progress is there in the private market?",
     '"How ', ' progress is there in the private market?"'),
    ("a lot of", "Hint: the safety net -- it works for both sides (three words)",
     "We have a lot of progress this month.",
     '"We have ', ' progress this month."'),
    ("a few", "Hint: you can count delays -- one delay, two delays (two words)",
     "We have a few delays in the public market.",
     '"We have ', ' delays in the public market."'),
    ("much", "Hint: you cannot count information, and the sentence is negative",
     "There is not much information about the reimbursement yet.",
     '"There is not ', ' information about the reimbursement yet."'),
    ("any", "Hint: it is a question -- you do not know yet if there is one",
     "Are there any updates from your side?",
     '"Are there ', ' updates from your side?"'),
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
    (1, "Good morning, Marc. Here is the update on the dermatology campaign."),
    (2, "The first milestone is complete, and we are on track."),
    (3, "We have a lot of progress in the private market: eleven centers are active."),
    (4, "But we have a few delays in the public market, because there is not much information about the reimbursement yet."),
    (5, "So far, so good."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Update in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the update in the correct order, from the opening to the closing. Look at the professional pattern: good news first, problem after, closing at the end.</p>')
w('      <div class="order-container" id="order-l6">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l6\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Here is a short update on the dermatology campaign.",
    "The first milestone is complete, and we are on track.",
    "We have a lot of progress in the private market.",
    "We have a few delays, and there is not much information yet.",
    "So far, so good.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of the Friday update. Note the stress: <strong>campaign</strong> is strong on the second part (kam-PEIN), and <strong>progress</strong>, as a noun, is strong on the first part (PRO-gres).</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the call with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc opens the call: "So, how is it going?" The best way to start is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Sorry, I have a lot of problems and my English is not good."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Here is a short update on the dermatology campaign. The first milestone is complete, and we are on track."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am going to send you forty slides tomorrow."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks how many centers are active. You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "There is much centers active."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Eleven centers are active, and we are rolling it out in four more this month."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have a little centers active."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to say there is a LOT of progress in the private market. The safe way is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We have a lot of progress in the private market."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We have many progress in the private market."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have many progresses in the private market."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Now the difficult part: there are two or three delays, and almost no information about the reimbursement. You report:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have a little delays and there is not many information."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have a few delays in the public market, and there is not much information about the reimbursement yet."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am very sorry, we have many delays and I do not have an information."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Before you close the call, you want to know if he has news. You ask:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Do you have some updates from your side?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Are there any updates from your side?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Are there many update from your side?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for two minutes, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">It is Friday, and Marc Dubois opens the call with one question: "So, how is it going?" '
  'Give him the update on a REAL project of yours (atopic dermatitis, asthma or COPD), in this order: (1) open it -- "Here is a short '
  'update on..."; (2) the good news, and the things you can COUNT (how many centers are active, how many doctors your team is visiting, '
  'how many milestones are complete); (3) the things you CANNOT count (how much progress there is in the market, how much time you still '
  'have, how much information is still missing); (4) the problems -- say them honestly, and do not apologize for them; (5) ask him one '
  'question back ("Are there any updates from your side?"); and (6) close with the expression of the lesson: "So far, so good." '
  'Speak for two minutes. Do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-6"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 6</h4>')
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
