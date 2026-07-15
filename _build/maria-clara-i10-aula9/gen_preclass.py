#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 9 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). O portugues so sobrevive onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: ZERO palavra das aulas 1-8 como vocab NOVO. Fora, de proposito (ja em circulacao):
    delegation / conference / flight / accommodation / visa / agenda / schedule / institution.
    As 8 novas (budget, currency, document, seat, space, preparation, amount, resource) sao
    disjuntas do conjunto de vocab-card-word das aulas 1-8 (verificado no hub).
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 9 IN CLASS (mesmo tema: a logistica da viagem da
    delegacao para Seul; mesmo vocab; mesma gramatica: quantificadores much/many/a little/
    a few/enough/too much/too many, countable vs uncountable)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao): frase-identidade "I speak English, and I am improving"
    no survival card; tom que celebra a tentativa; Clarinha (neta) como motivacao.
"""
import random

random.seed(9)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo com quantificador)
VOCAB = [
    ("Budget", "the money you have for a plan or a trip",
     "We have enough budget for the flights."),
    ("Currency", "the money of a country, like the won in Korea",
     "I only have a little foreign currency for Seoul."),
    ("Document", "an official paper you need, like a passport or a visa",
     "We need a lot of documents for the delegation."),
    ("Seat", "a place where one person sits on a plane",
     "Do we have enough seats for the whole team?"),
    ("Space", "the free room you have for people or things",
     "There is not much space in the meeting room."),
    ("Preparation", "the work you do before an important event",
     "There is a lot of preparation before departure."),
    ("Amount", "how much of something you have",
     "We have a small amount of time before November."),
    ("Resource", "the money, people, and time you can use for a plan",
     "We do not have enough resources for two trips."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-9">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1538485399081-7191377e8241?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 09 -- Pre-class</div>')
w('      <h3>How Much? How Many? -- Quantifiers for the Seoul Trip</h3>')
w('      <div class="lesson-desc">Run the logistics of the delegation to Seoul: how much time, how many documents, '
  'how much budget, and whether there are enough seats. Key words: budget, currency, document, seat, space, preparation, '
  'amount, resource. Structures: quantifiers <strong>much / many</strong>, <strong>a little / a few</strong>, '
  '<strong>a lot of / enough</strong>, <strong>too much / too many</strong> &mdash; with the countable vs uncountable rule '
  '(can you count it? then MANY; you cannot? then MUCH). Question forms: <strong>How much?</strong> for time and money, '
  '<strong>How many?</strong> for seats and documents. Idiom of the lesson: "Time flies."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="9" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="9">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words of your pre-trip checklist.</p>')
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
w('      <div class="match-grid" id="match-l9">')
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
w('        <p>The delegation flies to Seoul in November, and there is <strong>a lot of preparation</strong>. Maria Clara does '
  'not have <strong>much time</strong> &mdash; only six weeks &mdash; and there are <strong>too many meetings</strong> in '
  'October. For the trip she needs <strong>a lot of documents</strong>: every person needs a passport and a visa, and <strong>a '
  'few visas</strong> are still not ready. The <strong>budget</strong> is fine: there is <strong>enough money</strong> for the '
  'flights, but only <strong>a little foreign currency</strong> for the hotel. On the plane there are <strong>not many seats</strong> '
  'left, only eight, so Bruno books them today. "How <strong>much amount</strong> do I keep for the meals? And how <strong>many '
  'seats</strong> do we still need?" she asks. There is <strong>a lot of</strong> work, but they have <strong>enough resources</strong>. '
  '"November is close already," she says. "<strong>Time flies!</strong>"</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why is it "too many <strong>meetings</strong>" and NOT "too much meetings"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "meetings" is a special word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because you can COUNT meetings (1, 2, 3). Countable things take <strong>many</strong>, never "much".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is a question.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. Why is it "not much <strong>time</strong>" and NOT "not many time"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because you CANNOT count time (no "one time, two times" for hours). Uncountable things take <strong>much</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "time" is always plural.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is negative.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. She has some money, but not a lot. Which is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have a few foreign currency."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I have a little foreign currency." (money is uncountable &rarr; a little)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I have a few currencies for the hotel."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about the trip is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have much documents but not many time."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have a lot of documents but not much time, and there are not many seats left."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have too much seats and too many budget."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- How Much? How Many?</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">One question decides everything: <strong>can you count it?</strong> This is how English says how much and how many.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Quantifier</th><th style="padding:.7rem;text-align:left">Use it with</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>many</strong> &middot; <strong>a few</strong> &middot; <strong>too many</strong></td>'
  '<td style="padding:.6rem"><strong>COUNTABLE</strong> things &mdash; you can count them: 1 seat, 2 seats, 3 seats.</td>'
  '<td style="padding:.6rem">too <strong>many</strong> meetings &middot; a <strong>few</strong> documents &middot; not <strong>many</strong> seats</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>much</strong> &middot; <strong>a little</strong> &middot; <strong>too much</strong></td>'
  '<td style="padding:.6rem"><strong>UNCOUNTABLE</strong> things &mdash; you cannot count them: time, money, space, preparation.</td>'
  '<td style="padding:.6rem">not <strong>much</strong> time &middot; a <strong>little</strong> money &middot; too <strong>much</strong> preparation</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>a lot of</strong> &middot; <strong>enough</strong></td>'
  '<td style="padding:.6rem"><strong>BOTH</strong> &mdash; countable and uncountable. Safe and easy when in doubt.</td>'
  '<td style="padding:.6rem">a lot of <strong>documents</strong> &middot; a lot of <strong>time</strong> &middot; <strong>enough</strong> seats &middot; <strong>enough</strong> money</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Questions: <strong>How many?</strong> / <strong>How much?</strong></td>'
  '<td style="padding:.6rem"><strong>How many</strong> for countable, <strong>How much</strong> for uncountable.</td>'
  '<td style="padding:.6rem">How <strong>many</strong> documents? &middot; How <strong>much</strong> time?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready phrase: <strong>Time flies.</strong></td>'
  '<td style="padding:.6rem">Nothing to build &mdash; one idiom. It means time passes very fast. Perfect for the countdown to November.</td>'
  '<td style="padding:.6rem">"November is close already. <strong>Time flies!</strong>"</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"much meetings"</strong> or <strong>"many time"</strong>. Swap them: it is '
  '<strong>many meetings</strong> (you can count them) and <strong>much time</strong> (you cannot). '
  'When in doubt, <strong>a lot of</strong> and <strong>enough</strong> work for both, every time.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("much", "Hint: time is uncountable -- you cannot count it",
     "We do not have much time before the conference.",
     '"We do not have ', ' time before the conference."'),
    ("many", "Hint: meetings are countable -- 1, 2, 3 meetings",
     "There are too many meetings in October.",
     '"There are too ', ' meetings in October."'),
    ("a few", "Hint: a small number of countable things (documents)",
     "A few visas are still not ready.",
     '"', ' visas are still not ready."'),
    ("a little", "Hint: a small amount of an uncountable thing (money)",
     "I only have a little foreign currency for the hotel.",
     '"I only have ', ' foreign currency for the hotel."'),
    ("enough", "Hint: works for both -- it means the right amount",
     "Do we have enough seats for the delegation?",
     '"Do we have ', ' seats for the delegation?"'),
    ("many", "Hint: seats are countable -- how many, not how much",
     "How many seats do we have on the flight?",
     '"How ', ' seats do we have on the flight?"'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence. Ask yourself: can I count it?</p>')
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
    (1, "First, we check how much time we have before November."),
    (2, "Then, we prepare a lot of documents for the delegation."),
    (3, "We ask the embassy about the visas, because a few are still not ready."),
    (4, "After that, we check the budget and the foreign currency for the trip."),
    (5, "Finally, we book the seats, because there are not many left."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Pre-Trip Checklist in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of the Seoul preparation in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l9">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l9\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l9\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l9\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l9\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "We do not have much time before the conference.",
    "We need a lot of documents for the delegation.",
    "Do we have enough seats for the delegation?",
    "I only have a little foreign currency.",
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the pre-trip logistics call with Bruno.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Bruno asks: "How much time do we have before Seoul?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have many time, about six weeks."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have a little time, about six weeks, so we need to start now."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have a few time before November."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "How many documents do we need?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We need much documents for the visas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We need a lot of documents, and a few visas are still not ready."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We need a little documents for the delegation."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Bruno asks about the money. There is money for the flights, but not much for the hotel. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We have many budget, no problem."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We have enough budget for the flights, but only a little currency for the hotel."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have a few money for the hotel."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Only eight seats are left on the flight. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "There are not many seats left, so we book them today."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "There is not much seats left."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "There are too much seats left."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ASK Bruno about the space in the meeting room. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "How many space do we have in the room?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "How much space do we have in the room?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "How much rooms do we have?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Bruno gives you one minute on the logistics call. Tell him the status of the Seoul trip, using quantifiers: '
  'how much time you have and how many meetings are before November; how many documents the delegation needs and how many visas are ready; '
  'whether there is enough budget and how much foreign currency you have; and how many seats are left on the flight. '
  'Say one thing that is too much or too many, and one thing that is enough. Close with the idiom of the lesson: "Time flies." '
  'Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-9"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 9</h4>')
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
