#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 5 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). O portugues so sobrevive onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: ZERO palavra das aulas 1-4 como vocab NOVO. Fora, de proposito (ja ensinadas):
    aula 1: pharmaceutical company / immunology / national manager / field team / global meeting /
            results / launch / disease area / to be responsible for / to manage
    aula 2: schedule / report / field visit / medical rep / demand plan / headquarters /
            to attend / to review / to prepare / to travel
    aula 3: quarter / target / challenge / opportunity / growth / to achieve / to exceed /
            to miss / market access / prescription volume
    aula 4: small talk / congress / colleague / executive / stakeholder / pipeline /
            to introduce / to network / currently / to look forward to
    Trocas feitas em relacao ao curriculo: launch->product approval, to prepare->to organize,
    to present->to announce, patient access->reimbursement, plan->business plan.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 5 IN CLASS (mesmo tema: os planos do proximo
    trimestre e a visita de agosto; mesmo vocab; mesma gramatica: going to + a forma -ing
    para o que ja esta confirmado no calendario)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma explicito): NUNCA nomear "verbo to be". "I am going to" entra como
    BLOCO PRONTO ("o bloco do plano"), nunca como conjugacao.
"""
import random

random.seed(5)

OUT = 'preclass.html'

# (word, definicao em ingles simples (A2) -- a MESMA string vai no matching, exemplo)
VOCAB = [
    ("Business plan", "the document with your goals and actions for the year",
     "I am going to send the business plan to Paris in April."),
    ("Goal", "the thing you want to reach in the future",
     "Our goal is the product approval in dermatology."),
    ("Deadline", "the last day to finish something",
     "The deadline for the business plan is April 30."),
    ("Strategy", "how you are going to reach the goal",
     "Our strategy is to work with the private hospitals."),
    ("Quarterly review", "the meeting every three months where each country presents the numbers",
     "I am going to present the numbers at the quarterly review."),
    ("To announce", "to tell everyone officially",
     "In May, we are going to announce the product approval."),
    ("To organize", "to plan and prepare the parts of an event or a meeting",
     "I am going to organize the visit to the hospitals."),
    ("Product approval", "when the agency says yes and doctors can prescribe the medicine",
     "The product approval is going to arrive in May."),
    ("Reimbursement", "when the health plan or the government pays for the medicine",
     "The reimbursement decision is going to change the plan."),
    ("Global alignment", "when Brazil and the Global team agree on the same plan",
     "We are going to work on global alignment before August."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-5">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 05 -- Pre-class</div>')
w('      <h3>What Are Your Plans? -- Launches, Meetings and Goals</h3>')
w('      <div class="lesson-desc">Tell the Global team what comes next: the goal of the quarter, the strategy in the private market, '
  'the deadlines and the August visit to Brazil. Key words: business plan, goal, deadline, strategy, quarterly review, to announce, '
  'to organize, product approval, reimbursement, global alignment. Structures: <strong>going to</strong> for plans and intentions '
  '(I am going to present / we are going to announce), the negative (we are not going to launch) and the question (what are you going to do?); '
  'and the <strong>-ing</strong> form for what is already CONFIRMED in the calendar (we are meeting the Global team on August 24). '
  'Phrase of the lesson: "It depends on the market conditions."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words of your business plan.</p>')
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
w('      <div class="match-grid" id="match-l5">')
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
w('        <p>Paris wants the plan. In April, Emmanuele <strong>is going to send</strong> the <strong>business plan</strong> to Marc. '
  'Her <strong>goal</strong> is the <strong>product approval</strong> in dermatology, and in May the team <strong>is going to '
  'announce</strong> it. Her <strong>strategy</strong> is the private market: she <strong>is going to organize</strong> twenty new '
  'meetings with the hospitals. In June, she <strong>is going to present</strong> the numbers at the <strong>quarterly review</strong>. '
  'The <strong>reimbursement</strong> decision <strong>is going to arrive</strong> in July, but nobody is sure: '
  '"<strong>It depends on the market conditions</strong>," she says. The team <strong>is not going to launch</strong> in the public '
  'market this year. Before August, Brazil and Paris <strong>are going to work</strong> on <strong>global alignment</strong>. And the '
  'visit? That one is already in the calendar: they <strong>are meeting</strong> the Global team on August 24. The <strong>deadline</strong> '
  'for the document is April 30. "What <strong>are you going to</strong> present?" Marc asks. She knows the answer now.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why is it "we are going to <strong>announce</strong>" and NOT "we are going to announcing"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "announce" is an irregular verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because after the <strong>going to</strong> block, the verb always comes back to its NORMAL form. Nothing changes in it.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is in the past.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "They <strong>are meeting</strong> the Global team on August 24." Why does this sentence have NO "going to"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because it is already CONFIRMED in the calendar, with a fixed date. A fixed appointment uses the -ing form.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the action is happening right now, at this moment.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the subject is plural ("they").</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "<strong>What are you going to</strong> present?" Why is it NOT "What you are going to present?"</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because in English every question starts with "what".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "present" needs -ing in a question.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because in a question the first two words CHANGE places: "you are" &rarr; "<strong>are you</strong>".</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about the next quarter is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I go to present the business plan at the quarterly review."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am going to present the business plan at the quarterly review, and we are meeting the Global team in August."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am going to presenting the business plan at the quarterly review."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Plan Block: GOING TO</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A plan is always the future. This is how English says what is going to happen.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I <strong>am going to</strong><br>We / You / They <strong>are going to</strong><br>He / She / It <strong>is going to</strong></td>'
  '<td style="padding:.6rem">A plan or an intention: you ALREADY DECIDED, but the date is not fixed yet. There is nothing to build &mdash; these are THREE ready blocks. Pick your block and go.</td>'
  '<td style="padding:.6rem">We <strong>are going to</strong> focus on the private market.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">+ verb in the <strong>NORMAL</strong> form</td>'
  '<td style="padding:.6rem">After <strong>going to</strong>, the verb NEVER changes: no -ed, no -ing, no -s.</td>'
  '<td style="padding:.6rem">going to <strong>announce</strong> &middot; going to <strong>present</strong> &middot; going to <strong>organize</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative: <strong>not</strong> INSIDE the block</td>'
  '<td style="padding:.6rem">The <strong>not</strong> goes in the middle of the block, never at the end of the sentence.</td>'
  '<td style="padding:.6rem">We <strong>are not going to</strong> launch in the public market.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question: the first two words <strong>change places</strong></td>'
  '<td style="padding:.6rem">"you are going to" becomes "<strong>are you</strong> going to".</td>'
  '<td style="padding:.6rem">What <strong>are you going to</strong> present in August?</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Already <strong>CONFIRMED</strong> in the calendar? Use the <strong>-ing</strong> form, with no "going to"</td>'
  '<td style="padding:.6rem">The date is fixed, the ticket is booked, it is in your calendar. Simple rule: <strong>in your head</strong> = going to; <strong>in your calendar</strong> = -ing.</td>'
  '<td style="padding:.6rem">We <strong>are meeting</strong> the Global team on August 24. &middot; They <strong>are arriving</strong> on Sunday.</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready phrase: <strong>It depends on the market conditions.</strong></td>'
  '<td style="padding:.6rem">Nothing to build here. It is the professional way to say "maybe" without sounding insecure &mdash; and without promising what is not in your hands.</td>'
  '<td style="padding:.6rem">"Is July safe?" &mdash; "<strong>It depends on the market conditions.</strong>"</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"I go to present"</strong>. That does NOT exist in English. The English block has three parts and you need all of them: '
  '<strong>I am going to present</strong>. '
  'And the other mistake, now that you know the -ING form from lesson 4: do not put -ING after the block. '
  'It is <strong>"we are going to launch"</strong>, never "we are going to launching".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("am going to", "Hint: the plan block with I -- three words",
     "I am going to present the business plan in August.",
     '"I ', ' present the business plan in August."'),
    ("are going to", "Hint: the plan block with WE -- three words",
     "We are going to focus on the private market this quarter.",
     '"We ', ' focus on the private market this quarter."'),
    ("is going to", "Hint: the plan block for one single thing (the decision)",
     "The reimbursement decision is going to arrive in July.",
     '"The reimbursement decision ', ' arrive in July."'),
    ("announce", "Hint: after going to, the verb comes back to the NORMAL form (no -ing, no -ed)",
     "In May, we are going to announce the product approval.",
     '"In May, we are going to ', ' the product approval."'),
    ("are not going to", "Hint: negative -- the NOT goes INSIDE the block",
     "We are not going to launch in the public market this year.",
     '"We ', ' launch in the public market this year."'),
    ("are meeting", "Hint: it is already confirmed in the calendar -- the -ing form, no going to",
     "We are meeting the Global team on August 24.",
     '"We ', ' the Global team on August 24. The date is confirmed."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence. Careful with the last one: that date is already in the calendar.</p>')
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
    (1, "In April, I am going to send the business plan to Paris."),
    (2, "In May, we are going to announce the product approval in dermatology."),
    (3, "In June, I am going to present the numbers at the quarterly review."),
    (4, "In July, the reimbursement decision is going to arrive."),
    (5, "On August 24, we are having dinner with the global team in Brazil."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Next Quarter in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the events of the next quarter in the correct order, from April to August.</p>')
w('      <div class="order-container" id="order-l5">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l5\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Our goal is the product approval in dermatology.",
    "We are going to focus on the private market this quarter.",
    "I am going to present the business plan in August.",
    "It depends on the market conditions.",
    "Let me send you the plan before the deadline.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. These are the five sentences of the August plan. Careful with the stress: <strong>STRA</strong>-te-gy &mdash; the strong part is the first one.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the planning call with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc asks: "What are your plans for the next quarter?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We go to focus on the private market."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Our goal is the product approval in dermatology. We are going to announce it in May."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Last quarter we exceeded the target in dermatology."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "And what is the strategy?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We are going to focusing on the private hospitals."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We are going to focus on the private hospitals. I am going to organize twenty new meetings."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I organize twenty meetings yesterday."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The Global VP asks if the reimbursement decision arrives in July. You CANNOT promise it. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, yes, no problem, July, sure."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I do not know. Sorry."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "The decision is going to arrive in July, but it depends on the market conditions."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The dinner with the Global team on August 24 is ALREADY confirmed in the calendar. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We are having dinner with the global team on August 24."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We have dinner with the global team every August 24."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We had dinner with the global team on August 24."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ASK Marc what he is going to present on the visit. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What you are going to present in Brazil?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "What are you going to present in Brazil?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "What are you going to presenting in Brazil?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for two minutes, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Marc Dubois gives you two minutes on the planning call. Tell him the plan for the next quarter '
  'at Sanofi Brazil, in this order: first the goal (what you are going to achieve, and when you are going to announce it), then the '
  'strategy (where you are going to focus, and what you are going to organize), and finally the deadlines (the business plan, the '
  'reimbursement decision). Say one thing that is already confirmed in the calendar, using the -ing form: "We are meeting the Global team '
  'on August 24." And when he asks about a date you cannot promise, use the expression of the lesson: "It depends on the market conditions." '
  'Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-5"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 5</h4>')
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
