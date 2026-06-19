#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 7 (At the Restaurant) -- matching 12x12 embaralhado (REGRA 24)."""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(70)

# (word, def_en, example, pt_value, pt_label)
VOCAB = [
    ("Appetizer", "a small dish served before the main course", "I would like an appetizer to start.", "entrada", "Entrada"),
    ("Main course", "the largest and most important dish of a meal", "For my main course, I will have the lamb.", "prato principal", "Prato principal"),
    ("Side dish", "a small dish served together with the main course", "The main course comes with a side dish of rice.", "acompanhamento", "Acompanhamento"),
    ("Dessert", "sweet food eaten at the end of a meal", "For dessert, the chocolate cake is excellent.", "sobremesa", "Sobremesa"),
    ("Beverage", "any kind of drink", "Every main course includes one free beverage.", "bebida", "Bebida"),
    ("Recommend", "to suggest something good to someone", "What do you recommend for tonight?", "recomendar", "Recomendar"),
    ("Server", "the person who takes your order in a restaurant", "I will ask the server for the menu.", "gar&ccedil;om", "Gar&ccedil;om"),
    ("Bill", "the paper that shows how much you must pay", "Could I have the bill, please?", "a conta", "A conta"),
    ("Tip", "extra money you leave for good service", "I always leave a tip for good service.", "gorjeta", "Gorjeta"),
    ("Spicy", "having a strong, hot flavor", "I prefer a dish that is not too spicy.", "apimentado", "Apimentado"),
    ("Allergy", "a bad reaction of the body to a certain food", "I have an allergy to nuts.", "alergia", "Alergia"),
    ("Refill", "a second serving of the same drink, often free", "The restaurant offers a free refill of water.", "reabastecimento", "Reabastecimento"),
]
PT_PAIRS = [(v[3], v[4]) for v in VOCAB]  # (value, label)


def vocab_cards():
    out = []
    for w, d, ex, _, _ in VOCAB:
        out.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
            f'<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div>'
            f'<div class="vocab-card-example">"{ex}"</div></div>'
            f'<button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>')
    return '\n'.join(out)


def match_rows():
    out = []
    for i, (w, _, _, ans, _) in enumerate(VOCAB):
        opts = PT_PAIRS[:]
        # shuffle until the correct answer is NOT at the same index as the word row
        while True:
            random.shuffle(opts)
            if [v for v, _ in opts].index(ans) != i:
                break
        opt_html = '<option value="">Selecione...</option>' + ''.join(
            f'<option value="{v}">{lab.lower() if lab[0].isupper() and not lab.startswith("&") else lab}</option>'
            for v, lab in [(v, l) for v, l in opts])
        # use the lower-case display label for options (matches aula 6 style)
        opt_html = '<option value="">Selecione...</option>' + ''.join(
            f'<option value="{v}">{disp(v)}</option>' for v, _ in opts)
        out.append(
            f'        <div class="match-row" data-answer="{ans}">'
            f'<span class="match-word" style="flex:0 0 130px">{w}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>')
    return '\n'.join(out)


def disp(value):
    # lower-case Portuguese display preserving &ccedil; entity
    return value  # values are already stored lower-case (entities kept)


FILLS = [
    ("would like", "Hint: a polite request for a thing", "I would like an appetizer to start, please."),
    ("could", "Hint: a polite way to ask a question", "Could I have the menu, please?"),
    ("recommend", "Hint: to suggest something good", "What do you recommend for the main course?"),
    ("will", "Hint: a decision made when ordering", "I will have the chocolate cake for dessert."),
    ("refill", "Hint: a second serving of the same drink", "Could I have a refill of water, please?"),
    ("allergy", "Hint: a bad reaction to a food", "Please tell the server about your allergy."),
]
FILL_SENT = [
    ('"I ', 'would like', ' an appetizer to start, please."'),
    ('"', 'Could', ' I have the menu, please?"'),
    ('"What do you ', 'recommend', ' for the main course?"'),
    ('"I ', 'will', ' have the chocolate cake for dessert."'),
    ('"Could I have a ', 'refill', ' of water, please?"'),
    ('"Please tell the server about your ', 'allergy', '."'),
]


def fill_items():
    out = []
    for (ans, hint, phrase), (pre, _, post) in zip(FILLS, FILL_SENT):
        out.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
            f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
            f'data-phrase="{phrase}" placeholder="___">{post}</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    return '\n'.join(out)


ORDER = [
    (1, "First, I read the menu and choose my dishes."),
    (2, "Then I ask the server what they recommend."),
    (3, "After that, I order an appetizer and a main course."),
    (4, "Next, I mention my allergy so the kitchen is careful."),
    (5, "Finally, when I finish my dessert, I ask for the bill and leave a tip."),
]


def order_items():
    shown = ORDER[:]
    random.shuffle(shown)
    out = []
    for order, text in shown:
        out.append(
            f'        <div class="order-item" draggable="true" data-order="{order}" onclick="selectOrderItem(this,\'order-l7\')">'
            f'<span class="order-num">?</span><span class="order-text">{text}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l7\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l7\')">&#9660;</button></span></div>')
    return '\n'.join(out)


SPEECH = [
    ("I would like an appetizer and a main course, please.",
     "Eu gostaria de uma entrada e um prato principal, por favor."),
    ("Could I have a beverage with no ice?",
     "Posso pedir uma bebida sem gelo?"),
    ("I have an allergy to nuts, so please be careful.",
     "Eu tenho alergia a castanhas, ent&atilde;o por favor tenha cuidado."),
    ("Could I have the bill, please? The dinner was excellent.",
     "Posso pedir a conta, por favor? O jantar estava excelente."),
]


def speech_cards():
    out = []
    for en, pt in SPEECH:
        out.append(
            f'      <div class="speech-card" data-phrase="{en}">\n'
            f'        <div class="speech-phrase">{en}</div>\n'
            f'        <div class="speech-translation">{pt}</div>\n'
            f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
            f'        <div class="speech-result"></div>\n      </div>')
    return '\n'.join(out)


SURVIVAL = [
    ("I would like to see the menu, please.", "Eu gostaria de ver o card&aacute;pio, por favor."),
    ("Could I have a beverage and a side dish?", "Posso pedir uma bebida e um acompanhamento?"),
    ("What do you recommend tonight?", "O que voc&ecirc; recomenda hoje &agrave; noite?"),
    ("I have an allergy, so please no nuts.", "Eu tenho alergia, ent&atilde;o por favor sem castanhas."),
    ("Could I have the bill, please?", "Posso pedir a conta, por favor?"),
]


def survival():
    out = []
    for i, (en, pt) in enumerate(SURVIVAL, 1):
        out.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
            f'<button class="btn btn-listen" onclick="speakText(\'{en}\',this)">&#9835;</button></div>')
    return '\n'.join(out)


HTML = f'''<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 07 -- Pre-class</div>
      <h3>At the Restaurant -- Ordering Politely</h3>
      <div class="lesson-desc">Order food politely with <strong>would like</strong> (a polite request), <strong>could / can I have</strong> (a polite question) and <strong>I will have</strong> (a decision when ordering). New restaurant vocabulary: appetizer, main course, side dish, dessert, beverage, recommend, server, bill, tip, spicy, allergy, refill.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its translation.</p>
      <div class="match-grid" id="match-l7">
{match_rows()}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l7')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>After a long day at the congress, Rubens sits down at a restaurant in Lisbon. The server comes to his table, and he is polite. First he asks, "<strong>Could I have</strong> the menu, please?" He reads it and decides. "I <strong>would like</strong> the grilled shrimp to start," he says, "and for the main course, what do you <strong>recommend</strong>?" The server suggests the roasted lamb. "Perfect, I <strong>will have</strong> the lamb," Rubens answers. He also mentions an important detail: "I have an <strong>allergy</strong> to nuts, so please be careful." At the end of the meal, he does not say "give me the bill." Instead, he asks politely: "<strong>Could I have</strong> the bill, please?" A polite request always sounds better, and the service is friendlier because of it.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. How does Rubens ask for the menu?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Could I have the menu, please?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Give me the menu now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Menu, fast."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Why does Rubens say "I would like" instead of "I want"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because it is more polite.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because it is in the past.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a question.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What does Rubens say instead of "give me the bill"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Could I have the bill, please?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Bring the bill, you must."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am going to take the bill."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Ordering Politely</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Usado para pedir comida com educa&ccedil;&atilde;o. / Used to order food politely.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form / Forma</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example / Exemplo</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I would like + noun</td><td style="padding:.6rem">Pedido educado / a polite request</td><td style="padding:.6rem">I <strong>would like</strong> an appetizer.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">I would like + to + verb</td><td style="padding:.6rem">Pedido educado (a&ccedil;&atilde;o) / polite request (action)</td><td style="padding:.6rem">I <strong>would like to order</strong> now.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Could / Can I have + noun?</td><td style="padding:.6rem">Pergunta educada / a polite question</td><td style="padding:.6rem"><strong>Could I have</strong> the menu?</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">I will have + noun</td><td style="padding:.6rem">Decis&atilde;o ao pedir / a decision when ordering</td><td style="padding:.6rem">I <strong>will have</strong> the lamb.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">What do you recommend?</td><td style="padding:.6rem">Pedir sugest&atilde;o / asking for advice</td><td style="padding:.6rem">What do you <strong>recommend</strong> tonight?</td></tr>
        </tbody>
      </table></div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:8px;padding:.8rem;margin-top:.8rem"><p style="font-size:.82rem;color:var(--text-mid)"><strong>Key point / Ponto-chave:</strong> <strong>would like</strong> &eacute; mais educado que <strong>want</strong>. Depois de <strong>could / can I have</strong>, use um substantivo (could I have the menu, n&atilde;o could I have to the menu). Termine pedidos com <strong>please</strong>.</p></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the full sentence.</p>
{fill_items()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Order the Steps</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the steps of ordering a meal in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l7]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l7">
{order_items()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each phrase, then record yourself saying it.</p>
{speech_cards()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best sentence for each situation.</p>
      <div class="quiz-item"><div class="quiz-question">You want to order your main course politely. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I would like the roasted lamb, please."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Give me the lamb."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will to have the lamb."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want the server to suggest something. What do you ask?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "What do you recommend?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "What you recommend?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Recommend me, what?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You finished eating and want to pay. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Could I have the bill, please?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I want bill now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Where is bill?"</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Imagine you are at a restaurant during your next trip. Order a full meal in one minute. Use would like and could I have for polite requests (I would like an appetizer..., could I have a beverage...), ask the server for advice (what do you recommend?), and mention any allergy. At the end, ask for the bill politely and say something about the tip.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>
        <div id="think-result-7"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 7</h4>
{survival()}
    </div>

  </div>
</div>
'''

open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8').write(HTML)
print('wrote preclass.html')
