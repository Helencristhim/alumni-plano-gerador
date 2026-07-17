#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-7 do hub) do Ziláudio — aula 7 (a ULTIMA).

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 7 IN CLASS — mesmo vocab (fechar um acordo),
mesma gramatica (would/could para negociar e concordar; preposicoes between/within/on).

A7 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = would/could na negociacao.
A ultima aula do pacote: ele fecha um acordo do preco a assinatura. O lado advogado dele
entra nos termos e na condicao. Junta tudo das aulas 1-6.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(7)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Offer", "a price or plan you are ready to give or accept",
     "Thank you for the offer, but the price is a little low."),
    ("Agree", "to say yes to a plan or a price",
     "I agree with your plan."),
    ("Terms", "the rules and conditions that are part of a deal",
     "The terms of the contract are clear."),
    ("Contract", "a written paper that says what both sides will do",
     "Please send me the contract to read."),
    ("Sign", "to write your name on a contract to make it official",
     "I will sign the contract today."),
    ("Deal", "an agreement between two sides to do business",
     "We have a deal!"),
    ("Condition", "one thing that must be true for the deal to happen",
     "I have one condition: payment within a week."),
    ("Partner", "a company or person you do business with",
     "Diana is a good business partner."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-7">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 07 -- Pre-class</div>')
A('      <h3>Making a Deal</h3>')
A('      <div class="lesson-desc">The final lesson. Close the deal &mdash; negotiate a better price, agree on the '
  'terms, and sign the contract. A low offer is not a no; it is the start of the talk. '
  'Key words: offer, agree, terms, contract, sign, deal, condition, partner. Deal phrases: '
  '<strong>Could we agree on...?</strong> &middot; <strong>I would accept...</strong> &middot; '
  '<strong>Would you consider...?</strong> Prepositions in focus: '
  '<strong>between</strong>, <strong>within</strong>, <strong>on</strong>.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words you need to close a deal.</p>')
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
A('      <div class="match-grid" id="match-l7">')
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
A('        <p>Diana wants to buy Ziláudio&apos;s soybeans, but her first <strong>offer</strong> is a little low. '
  'Ziláudio wants the <strong>deal</strong>, so he does not say no. "I could not accept that price," he says. '
  '"<strong>Could</strong> we <strong>agree</strong> on a little more?" Diana thinks about it. "<strong>Would</strong> '
  'you consider a longer <strong>contract</strong>?" she asks.</p>')
A('        <p style="margin-top:.8rem">"Yes, I <strong>would</strong>," says Ziláudio, "but only <strong>on</strong> good '
  '<strong>terms</strong>. My <strong>partner</strong> and I have one <strong>condition</strong>: payment '
  '<strong>within</strong> a week." Diana smiles. "That is fair. So, <strong>between</strong> us: a higher price, a longer '
  'contract, and payment within a week. Do we have a deal?" "We have a deal," says Ziláudio. "Send me the contract, and I will '
  '<strong>sign</strong> it today."</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Diana&apos;s first offer is low. Instead of saying no, Ziláudio asks "Could we <strong>agree</strong> on a little more?" Why is this good?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A low offer is not a no. Asking politely keeps the deal alive.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because you must always say yes to the first offer.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "agree" is a polite way to say goodbye.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. What does Ziláudio say to accept a longer contract?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I want a longer contract now."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Yes, I <strong>would</strong> &mdash; but only on good terms."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Maybe contract yes."</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. What is Ziláudio&apos;s one <strong>condition</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A shorter contract.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Payment within a week.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A lower price for the soybeans.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. "You will get the payment <strong>_____</strong> a week." Which preposition is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> within (within = inside a period of time)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> between</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> on</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Could &amp; Would</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two small words make you a good negotiator. <strong>Could</strong> asks. <strong>Would</strong> says what you accept or will do. Together they push for a better deal &mdash; and still sound polite.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">What you want to do</th><th style="padding:.7rem;text-align:left">Say this</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Ask politely in a deal</td><td style="padding:.6rem"><strong>Could we agree</strong> on a better price?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Say what you accept or will do</td><td style="padding:.6rem">I <strong>would accept</strong> a longer contract.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Suggest an idea gently</td><td style="padding:.6rem"><strong>Would you consider</strong> a higher offer?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Say a soft "no"</td><td style="padding:.6rem">I <strong>could not sign</strong> at that price.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">between &middot; within &middot; on</td><td style="padding:.6rem"><strong>between</strong> + two sides (between us) &middot; <strong>within</strong> + a period of time (within a week) &middot; <strong>on</strong> + terms (we agree on these terms)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> a direct "I want a better price" sounds rude in a negotiation. Start with <strong>Could we</strong> or <strong>I would</strong>, and the same idea sounds professional. And never translate word by word: "I no sign" is wrong &mdash; say "<strong>I could not sign</strong>." After <strong>could</strong> and <strong>would</strong>, use the base verb (agree, accept, sign) &mdash; not "to agree". Remember: negotiating is not fighting, it is asking.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("agree", "Hint: the verb for saying yes to a price",
     "Could we agree on a better price?",
     '"Could we ', ' on a better price?"'),
    ("would", "Hint: the modal for what you accept or will do",
     "I would accept a longer contract.",
     '"I ', ' accept a longer contract."'),
    ("terms", "Hint: the rules and conditions of a deal",
     "The terms of the contract are clear.",
     '"The ', ' of the contract are clear."'),
    ("sign", "Hint: the verb for writing your name on a contract",
     "I will sign the contract today.",
     '"I will ', ' the contract today."'),
    ("within", "Hint: the preposition for inside a period of time",
     "You will get the payment within a week.",
     '"You will get the payment ', ' a week."'),
    ("between", "Hint: the preposition for two sides of a deal",
     "This deal is between you and me.",
     '"This deal is ', ' you and me."'),
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

# ---------- Stage 2 — Ordering (os passos de fechar um acordo) ----------
ORDER = [
    (2, "If the price is low, ask: \"Could we agree on a little more?\""),
    (4, "When you both agree, say: \"We have a deal.\""),
    (1, "Listen to the buyer's offer."),
    (5, "Sign the contract."),
    (3, "Talk about the terms and your one condition."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: How to Close a Deal</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">A buyer makes you a low offer. Put the five steps in the right order &mdash; from the offer to the signature.</p>')
A('      <div class="order-container" id="order-l7">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l7\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l7\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l7\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l7\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (as 5 frases-do-acordo) ----------
SPEECH = [
    "Could we agree on a better price?",
    "I would accept a longer contract.",
    "Send me the contract and I will sign it.",
    "I have one condition: payment within a week.",
    "We have a deal.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each deal phrase, repeat it out loud, and only then record. Learn them until they come out without thinking &mdash; that is how you close a deal with no fear.</p>')
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
    ("A buyer makes a low offer. You want the deal, but not at that price. You say:",
     [("\"No. Too low.\"", False),
      ("\"Could we agree on a better price?\"", True),
      ("\"Your offer is bad.\"", False)]),
    ("The buyer asks for a longer contract and you accept. You say:",
     [("\"Yes, I would accept a longer contract.\"", True),
      ("\"Contract long yes.\"", False),
      ("\"I want a longer contract now.\"", False)]),
    ("You want to set your one condition about payment. You say:",
     [("\"You pay in one week, ok?\"", False),
      ("\"I have one condition: payment within a week.\"", True),
      ("\"Money fast, please.\"", False)]),
    ("You want to suggest a higher offer, gently. You say:",
     [("\"Would you consider a higher offer?\"", True),
      ("\"Give more money.\"", False),
      ("\"You must pay more.\"", False)]),
    ("You both agree on everything and you want to close. You say:",
     [("\"Ok, finish.\"", False),
      ("\"We have a deal. Send me the contract and I will sign it.\"", True),
      ("\"Maybe yes deal.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment in a negotiation. Remember: asking with could and would is professional, not weak.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. This is the last task of the program: show that you can close a deal in English.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">A buyer makes a low offer for your soybeans. You want the deal, but not at that price. Imagine the whole negotiation out loud: how do you ask for a better price? How do you say what you would accept? What is your one condition about payment? And how do you close the deal? Use the deal phrases &mdash; <strong>could we agree on...</strong>, <strong>I would accept...</strong>, <strong>we have a deal</strong> &mdash; from the low offer all the way to the signature.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-7"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 7</h4>')
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
