#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 13 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "A Little, a Few, Too Much" -- quantificadores em relatorios de orcamento,
logistica de delegacao e decisoes do dia a dia (Maceio <-> Seul). Gramatica (expansao
da aula 9): too much / too many / not enough / too + adjetivo.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (sufficient, limited, allocate, exceed, balance, priority,
    approval, spending) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-12
    (verificado no hub -- 'available' e 'a request' ja existiam, por isso ficaram DE FORA).
    Em circulacao (nao ensinado como novo): budget, currency, document, seat, space,
    preparation, amount, resource, delegation, conference, flight, accommodation, visa.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 13 IN CLASS (mesmo tema: o orcamento limitado
    da segunda viagem; mesmo vocab; mesma gramatica: too much/too many/not enough/too+adj)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao): frase-identidade "I speak English, and I am improving"
    no survival card; tom que celebra a tentativa; Clarinha (neta) como motivacao.
"""
import random

random.seed(13)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo com quantificador)
VOCAB = [
    ("Sufficient", "enough for what you need, not more",
     "We do not have sufficient time before the trip."),
    ("Limited", "small in amount, with a fixed maximum",
     "The budget is limited this year, so we plan with care."),
    ("Allocate", "to give money or resources to a special purpose",
     "We allocate more money to the documents."),
    ("Exceed", "to go over a limit or an amount",
     "The spending must not exceed the budget."),
    ("Balance", "the money that is left in an account",
     "There is a small balance left for the second trip."),
    ("Priority", "the most important thing, the one you do first",
     "Documentation is our first priority."),
    ("Approval", "official permission to spend or to do something",
     "We need approval for the extra expenses."),
    ("Spending", "the money you use or pay out",
     "There is too much spending on accommodation."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-13">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 13 -- Pre-class</div>')
w('      <h3>A Little, a Few, Too Much -- The Budget Meeting</h3>')
w('      <div class="lesson-desc">Run the numbers for the second trip when the budget is limited: '
  'say what is <strong>too much</strong>, what is <strong>too many</strong>, and what is <strong>not enough</strong>, '
  'and use <strong>too + adjective</strong> for what is too expensive or too long. Key words: sufficient, limited, '
  'allocate, exceed, balance, priority, approval, spending. Structures: <strong>too much</strong> (uncountable) vs '
  '<strong>too many</strong> (countable), <strong>not enough</strong> (something is missing), and <strong>too + '
  'adjective</strong> (no "much"). Expression: "I agree / I disagree." Idiom of the lesson: "Cut corners."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="13" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="13">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words of the budget meeting.</p>')
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
w('      <div class="match-grid" id="match-l13">')
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
w('        <p>The budget for the second trip is <strong>limited</strong> this year. Maria Clara reads the report and sees the '
  'problem at once: there is <strong>too much spending</strong> on accommodation, because the hotel near the center is '
  '<strong>too expensive</strong>. There are also <strong>too many requests</strong> &mdash; every department wants a seat &mdash; '
  'but there are <strong>not enough approvals</strong> from the finance office. "We do not have <strong>enough money</strong> for '
  'the whole delegation," she says, "so we need a clear <strong>priority</strong>." Documentation is first: they cannot cut '
  'corners with the visas. She decides to <strong>allocate</strong> a little more to the documents and less to the extras, and '
  'she promises not to <strong>exceed</strong> the budget on the dinners. The <strong>balance</strong> left is small, but the '
  'plan is safe. "The agenda is <strong>too long</strong> for one afternoon," Bruno adds. "I agree," she says. "Let us cut it."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why is it "too many <strong>requests</strong>" and NOT "too much requests"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "requests" is a special word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because you can COUNT requests (1, 2, 3). Countable things take <strong>too many</strong>, never "too much".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is a question.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. The hotel is "too <strong>expensive</strong>". Why is there no "much"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because "expensive" is an adjective. With an adjective you use only <strong>too</strong> &mdash; "too much expensive" is wrong.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "expensive" is uncountable.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the hotel is far from the center.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. There are "<strong>not enough</strong> approvals". What does this mean?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> There are too many approvals.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> There are fewer approvals than they need &mdash; some are MISSING.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> There are exactly the right number of approvals.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about the budget is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have too much requests and not enough time, and the hotel is too much expensive."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have too many requests and not enough time, and the hotel is too expensive."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have too many spending and not enough seat."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Too Much, Too Many, Not Enough</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two questions decide everything: <strong>can you count it?</strong> and <strong>is it an adjective?</strong> This is how English says what is over the top and what is missing.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>too much</strong> + uncountable</td>'
  '<td style="padding:.6rem">More than is good &mdash; of something you CANNOT count: money, spending, time.</td>'
  '<td style="padding:.6rem">too <strong>much</strong> spending &middot; too <strong>much</strong> time</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>too many</strong> + countable</td>'
  '<td style="padding:.6rem">More than is good &mdash; of something you CAN count: requests, meetings, seats.</td>'
  '<td style="padding:.6rem">too <strong>many</strong> requests &middot; too <strong>many</strong> meetings</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>not enough</strong> + noun</td>'
  '<td style="padding:.6rem">Less than you need &mdash; something is MISSING. Works for both countable and uncountable.</td>'
  '<td style="padding:.6rem"><strong>not enough</strong> money &middot; <strong>not enough</strong> seats</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>too</strong> + adjective</td>'
  '<td style="padding:.6rem">A problem of quality, not quantity. NO "much" here &mdash; just too + the adjective.</td>'
  '<td style="padding:.6rem">too <strong>expensive</strong> &middot; too <strong>long</strong></td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready phrase: <strong>Cut corners.</strong></td>'
  '<td style="padding:.6rem">One idiom. It means to do a job badly to save money or time. In a budget, you say what you will NOT cut.</td>'
  '<td style="padding:.6rem">"We can\'t <strong>cut corners</strong> with the visas."</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"too much requests"</strong> or <strong>"too much expensive"</strong>. Swap them: it is '
  '<strong>too many requests</strong> (you can count them) and <strong>too expensive</strong> (an adjective &mdash; no "much"). '
  'And <strong>not enough</strong> always means something is missing.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("too much", "Hint: spending is uncountable -- you cannot count it",
     "There is too much spending on accommodation.",
     '"There is ', ' spending on accommodation."'),
    ("too many", "Hint: requests are countable -- 1, 2, 3 requests",
     "There are too many requests from the departments.",
     '"There are ', ' requests from the departments."'),
    ("not enough", "Hint: something is missing -- fewer than you need",
     "We have not enough approvals for the seats.",
     '"We have ', ' approvals for the seats."'),
    ("too expensive", "Hint: an adjective after too -- no much",
     "The hotel near the center is too expensive.",
     '"The hotel near the center is ', '."'),
    ("enough", "Hint: the right amount -- works for both",
     "We do not have enough budget for the second trip.",
     '"We do not have ', ' budget for the second trip."'),
    ("too long", "Hint: too + adjective -- a quality problem",
     "The agenda is too long for one afternoon.",
     '"The agenda is ', ' for one afternoon."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence. Ask yourself: can I count it? Is it an adjective?</p>')
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
    (1, "First, we read the budget report and see how much money is available."),
    (2, "Then, we decide the priority: documentation and travel come first."),
    (3, "We cut the spending on accommodation, because the hotel is too expensive."),
    (4, "After that, we allocate a little more money to the visas and less to the extras."),
    (5, "Finally, we ask the finance office for approval, and we do not exceed the budget."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Budget Plan in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of the budget meeting in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l13">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l13\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l13\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l13\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l13\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "There is too much spending on accommodation.",
    "There are too many requests and not enough approvals.",
    "The hotel is too expensive for the budget.",
    "Documentation is our priority, so we allocate more to it.",
    "I speak English, and I am improving.",
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the budget meeting with the finance officer.</p>')
w('      <div class="quiz-item"><div class="quiz-question">The officer asks: "How is the spending on the hotel?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "There are too many spending on the hotel."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "There is too much spending, because the hotel is too expensive."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The hotel is too much expensive."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "Do you have enough approvals for all the seats?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, there are too many approvals."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "No, there are not enough approvals &mdash; only four of eight are signed."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "No, there are not enough approval for the seats."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The officer wants to cut the documentation time. You disagree. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I disagree. Documentation is our priority &mdash; we can\'t cut corners with the visas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I agree. We have too many time for the documents."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, we should cut corners with the visas."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He says: "You are close to the maximum amount." You promise:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We will exceed the budget a little."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I agree. We will not exceed the budget, and we keep a healthy balance."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have too much amount for the dinners."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ASK the officer about the time before the trip. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "How many time do we have before the trip?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Do we have enough time, or is the preparation too short?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Is there too many time before November?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">You have one minute to present the budget for the second trip to the finance officer. '
  'Use the quantifiers: say what there is too much of and too many of; what is not enough; and one thing that is too expensive '
  'or too long. Give your priority, say what you will allocate and what you will not exceed, and use the expression "I agree" or '
  '"I disagree". Close with the idiom of the lesson: "We can\'t cut corners." Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-13"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 13</h4>')
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
