#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-6 do hub) do Ziláudio — aula 6.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 6 IN CLASS — mesmo vocab, mesma gramatica.
REGRA 22: 8 palavras NOVAS, zero colisao com aulas 1-5 (price/ton/quote/discount/
delivery/payment/invoice/total).

A6 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = comparativos para
precos e ofertas (cheaper / higher / more expensive / better than) + preposicoes de
numero per / under / over.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(6)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Price", "the amount of money you pay for something",
     "What is the price per ton?"),
    ("Ton", "a unit of weight -- one thousand kilos",
     "I sell my soybeans by the ton."),
    ("Quote", "a paper that shows the price a seller offers you",
     "The quote shows the price and the delivery."),
    ("Discount", "money taken off the normal price",
     "They gave me a discount for a big order."),
    ("Delivery", "bringing the goods to the buyer",
     "The delivery is free in fourteen days."),
    ("Payment", "the money you send to pay for something",
     "I send the payment after the invoice."),
    ("Invoice", "a document that asks you to pay, with the total",
     "The invoice shows the total to pay."),
    ("Total", "the full amount, all the numbers added together",
     "The total is more than the price per ton."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-6">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 06 -- Pre-class</div>')
A('      <h3>Prices, Volumes and Quotes</h3>')
A('      <div class="lesson-desc">Read two real quotes from international buyers and choose the better offer. '
  'Key words: price, ton, quote, discount, delivery, payment, invoice, total. Structure: '
  '<strong>comparatives</strong> for prices and offers (cheaper, higher, more expensive, better than) and the '
  'prepositions of number <strong>per</strong>, <strong>under</strong> and <strong>over</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words that live inside a quote.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado / REGRA 13: definicao EN) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>')
A('      <div class="match-grid" id="match-l6">')
defs = [v[1] for v in VOCAB]
assert len(set(defs)) == len(defs), 'definicoes do matching precisam ser UNICAS'
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
A('        <p>Zilaudio has two <strong>quotes</strong> for his soybeans. Grainline offers a <strong>price</strong> of '
  '1,900 reais <strong>per</strong> ton. Riverport offers 1,850 reais per ton, so Riverport is <strong>cheaper</strong> '
  '<strong>than</strong> Grainline. But the price <strong>per</strong> ton is not the whole story.</p>')
A('        <p style="margin-top:.8rem">Grainline gives free <strong>delivery</strong> and a <strong>discount</strong> of 2% '
  'for orders <strong>over</strong> 1,000 tons. Riverport is <strong>faster</strong> on payment, but it charges for '
  'delivery and gives no discount. The <strong>total</strong> on the <strong>invoice</strong> is <strong>more important</strong> '
  '<strong>than</strong> the price per ton. Grainline gives 30 days to pay, so a <strong>higher</strong> price can still be '
  'the <strong>better</strong> offer.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. The text says Riverport is "<strong>cheaper than</strong>" Grainline. What does this show?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The two prices are the same.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It compares two prices &mdash; Riverport\'s is lower. This is the comparative.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Riverport has the highest price of all.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. Grainline gives a discount "for orders <strong>over</strong> 1,000 tons". An order of 800 tons:</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> gets the discount, because 800 is a big number.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> does not get the discount &mdash; 800 is under 1,000, not over.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> gets a bigger discount than 1,000 tons.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "expensive" is a long adjective. Its correct comparative is:</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> expensiver</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> more expensive</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> most expensive than</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Why can a <strong>higher</strong> price still be the <strong>better</strong> offer?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because of free delivery, a discount and more time to pay.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because a higher price is always better.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the price per ton is the only thing that matters.</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Comparatives, and per / under / over</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use the comparative + <strong>than</strong> to compare two things. Ask yourself: is the adjective short or long?</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Short adjective<br>+ <strong>-er</strong></td><td style="padding:.6rem">Short words. Add -er and than.</td><td style="padding:.6rem">cheap &#8594; <strong>cheaper</strong> &middot; high &#8594; <strong>higher</strong></td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>more</strong> + long<br>adjective</td><td style="padding:.6rem">Long words. Use more, never -er.</td><td style="padding:.6rem">expensive &#8594; <strong>more expensive</strong></td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Irregular</td><td style="padding:.6rem">A few change completely.</td><td style="padding:.6rem">good &#8594; <strong>better</strong> &middot; bad &#8594; <strong>worse</strong></td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">per</td><td style="padding:.6rem">For each one.</td><td style="padding:.6rem">1,900 reais <strong>per</strong> ton.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">under</td><td style="padding:.6rem">Less than this number.</td><td style="padding:.6rem">The price is <strong>under</strong> 1,900 reais.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">over</td><td style="padding:.6rem">More than this number.</td><td style="padding:.6rem">A discount for orders <strong>over</strong> 1,000 tons.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> never mix -er and more. Not "more cheap" &mdash; say "<strong>cheaper</strong>". And not "expensiver" &mdash; say "<strong>more expensive</strong>". Short words take -er; long words take more.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("cheaper", "Hint: comparative of 'cheap' -- a short adjective, add -er",
     "Riverport is cheaper than Grainline.",
     '"Riverport is ', ' than Grainline."'),
    ("more expensive", "Hint: comparative of 'expensive' -- a long adjective, use more",
     "Grainline is more expensive than Riverport.",
     '"Grainline is ', ' than Riverport."'),
    ("better", "Hint: irregular comparative of 'good'",
     "Free delivery is better than paid delivery.",
     '"Free delivery is ', ' than paid delivery."'),
    ("per", "Hint: the preposition that means 'for each'",
     "The price is 1,900 reais per ton.",
     '"The price is 1,900 reais ', ' ton."'),
    ("over", "Hint: the preposition that means 'more than this number'",
     "You get a discount for orders over 1,000 tons.",
     '"You get a discount for orders ', ' 1,000 tons."'),
    ("under", "Hint: the preposition that means 'less than this number'",
     "1,850 is under 1,900, so it is cheaper.",
     '"1,850 is ', ' 1,900, so it is cheaper."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence &mdash; as many times as you want.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering (steps to compare two quotes) ----------
ORDER = [
    (3, "Compare the price per ton: which one is cheaper?"),
    (1, "Open the two quotes and read them slowly."),
    (5, "Look at the total and the payment time, and choose the better offer."),
    (2, "Find the price, the discount, the delivery and the payment on each one."),
    (4, "Ask for a discount if your order is over 1,000 tons."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You compare two quotes. Put the steps in a natural order.</p>')
A('      <div class="order-container" id="order-l6">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l6\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (A2: frases de 5-7 palavras) ----------
SPEECH = [
    "What is your price per ton?",
    "Riverport is cheaper than Grainline.",
    "Can you give me a discount for a bigger order?",
    "The total is more important than the price per ton.",
    "I need 30 days to pay after the invoice.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, repeat it out loud, and only then record. Listen and record as many times as you want &mdash; repetition is the method, not a sign of difficulty.</p>')
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
    ("A supplier calls. You want to know the price for one ton. You ask:",
     [("\"What is your price per ton?\"", True),
      ("\"How much is the price of the ton for?\"", False),
      ("\"What price the ton?\"", False)]),
    ("Grainline is 1,900 and Riverport is 1,850 per ton. You compare them:",
     [("\"Grainline is more cheap than Riverport.\"", False),
      ("\"Riverport is cheaper than Grainline.\"", True),
      ("\"Riverport is the cheaper.\"", False)]),
    ("Your order is 1,200 tons. You ask politely for a lower price:",
     [("\"Give me discount now.\"", False),
      ("\"Can you give me a discount for a bigger order?\"", True),
      ("\"You make the price more cheap?\"", False)]),
    ("You explain why the cheaper quote is not always the best:",
     [("\"The price per ton is the only important thing.\"", False),
      ("\"The total is more important than the price per ton.\"", True),
      ("\"The price is more important than the total than.\"", False)]),
    ("The seller asks when you can pay. You need a month after the invoice:",
     [("\"I pay you until the invoice.\"", False),
      ("\"I need 30 days to pay after the invoice.\"", True),
      ("\"I need to pay for 30 days the invoice.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment with an international buyer.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">You have two quotes for your soybeans. Grainline offers 1,900 reais <strong>per</strong> ton, with free <strong>delivery</strong>, a 2% <strong>discount</strong> for orders <strong>over</strong> 1,000 tons, and 30 days to pay. Riverport offers 1,850 reais per ton, but charges for delivery and gives no discount. Compare the two offers out loud: which one is <strong>cheaper</strong> per ton, and which one has the better <strong>total</strong> and <strong>payment</strong>? Say which offer you choose and why. Use comparatives (cheaper, higher, more expensive, better than) and take your time.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-6"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 6</h4>')
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
