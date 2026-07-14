#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 12 termos + 3 expressoes)
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase), onde o
    apostrofo e caractere comum — o ingles mantem a contracao natural (I've, I'm,
    we're) SEM quebrar o handler inline.
"""
import re
import random

random.seed(32)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Organizational culture", "the shared values and behaviors that decide how work really happens",
     "cultura organizacional",
     "Organizational culture is what people do when nobody is measuring them."),
    ("Employee journey", "every stage a person goes through, from the first interview to the last day",
     "jornada do colaborador",
     "The employee journey starts long before the first day of work."),
    ("People strategy", "the long term plan for how a company attracts, grows and keeps its people",
     "estrat&#233;gia de pessoas",
     "Our people strategy has three pillars, and culture is the first one."),
    ("Framework", "a structured model you use to organize and explain your approach",
     "modelo estruturado, framework",
     "I don't bring answers, I bring a framework."),
    ("Stakeholder", "anyone with a real interest in the outcome of your work",
     "parte interessada",
     "Every stakeholder wants to know what changes for them."),
    ("Alignment", "the point where leadership, strategy and culture pull in the same direction",
     "alinhamento",
     "Alignment is when leadership says one thing and the team lives the same thing."),
    ("To roll out", "to launch something across a whole organization, step by step",
     "implantar, lan&#231;ar em escala",
     "We're rolling out the new employee journey across every region."),
    ("Headquarters", "the main office, where the senior decisions are made",
     "matriz, sede",
     "Headquarters owns the framework, but each market owns its own culture."),
    ("Franchisor", "the company that licenses its brand and its model to local operators",
     "franqueadora",
     "Maple Bear is a franchisor: we license the model, we don't run the schools."),
    ("Bilingual education", "teaching a full curriculum in two languages",
     "educa&#231;&#227;o bil&#237;ngue",
     "We work in bilingual education, from kindergarten to high school."),
    ("Hybrid model", "a way of working that mixes days at the office and days at home",
     "modelo h&#237;brido",
     "We're still learning how to build culture inside a hybrid model."),
    ("Senior leadership", "the executives who set the direction and own the decisions",
     "alta lideran&#231;a",
     "Senior leadership sets the direction, but the middle managers set the tone."),
    ("To make headway", "to make real progress on something difficult",
     "avan&#231;ar de verdade, progredir",
     "We're making headway on the hybrid model."),
    ("To take a stance", "to state a clear position and defend it",
     "tomar uma posi&#231;&#227;o",
     "Take a stance, but leave room for their input."),
    ("To carry out", "to conduct something you planned: research, an assessment, a review",
     "conduzir, realizar",
     "Before I propose anything, I want to carry out a cultural assessment."),
]

DEFS = [d for _, d, _, _ in VOCAB]

# ---------- guarda-corpo: nada falavel pode entrar em argumento de onclick ----------
SPEAKABLE = []


def speak_btn(text, cls='audio-btn', label='Listen'):
    """Botao de audio: o texto viaja em data-speak (ATRIBUTO), nunca no onclick."""
    assert '"' not in text, f'aspas duplas quebram o atributo: {text}'
    SPEAKABLE.append(text)
    return (f'<button class="{cls}" data-speak="{text}" '
            f'onclick="speakText(this.dataset.speak,this)">{label}</button>')


# ---------- Stage 1.1 vocab cards ----------
cards = []
for w, d, pt, ex in VOCAB:
    cards.append(
        '        <div class="vocab-card-pc"><div class="vocab-card-content">'
        f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
        f'<span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{d}</span></div>'
        f'<div class="vocab-card-example">"{ex}"</div></div>'
        f'{speak_btn(w)}</div>'
    )
vocab_cards = '\n'.join(cards)

# ---------- Stage 1.2 matching (REGRA 24: embaralhado, ordem distinta por linha) ----------
rows = []
for w, d, _, _ in VOCAB:
    opts = DEFS[:]
    while True:
        random.shuffle(opts)
        if opts != DEFS:
            break
    o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
    rows.append(
        f'        <div class="match-row" data-answer="{d}">'
        f'<span class="match-word" style="flex:0 0 170px">{w}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
        f'<option value="">Select...</option>{o}</select></div>'
    )
match_rows = '\n'.join(rows)

# ---------- Stage 1.5 fill-in-the-blank ----------
# forma PLENA no drill (e o que a gramatica ensina); data-phrase = atributo (seguro)
BLANKS = [
    ("I", "lead", "Hint: a permanent role &mdash; present simple",
     "I lead People and Culture at Maple Bear.", "People and Culture at Maple Bear."),
    ("At the moment, we", "are rolling out", "Hint: in progress right now &mdash; present continuous",
     "At the moment, we are rolling out the new employee journey.",
     "the new employee journey."),
    ("I", "have been leading", "Hint: it started in 2023 and it is still going &mdash; have been + -ing",
     "I have been leading the culture transformation since 2023.",
     "the culture transformation since 2023."),
    ("I", "have carried out", "Hint: a countable result, no time said &mdash; have + past participle",
     "I have carried out four cultural assessments.", "four cultural assessments."),
    ("I have been working in People and Culture", "for", "Hint: a period of time (eight years)",
     "I have been working in People and Culture for eight years.", "eight years."),
    ("I have been leading the culture transformation", "since", "Hint: a starting point (2023)",
     "I have been leading the culture transformation since 2023.", "2023."),
]
fills = []
for pre, ans, hint, phrase, post in BLANKS:
    SPEAKABLE.append(phrase)
    fills.append(
        f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre} '
        f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
        f'data-phrase="{phrase}" placeholder="___"> {post}"</div>'
        f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
        f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
    )
fill_items = '\n'.join(fills)

# ---------- Stage 3 pronunciation (fala real => CONTRACAO natural) ----------
SPEECH = [
    ("I lead People and Culture at Maple Bear, a franchisor in bilingual education.",
     "Eu lidero People &amp; Culture na Maple Bear, uma franqueadora de educa&#231;&#227;o bil&#237;ngue."),
    ("My role involves the employee journey and the people strategy behind it.",
     "Meu cargo abrange a jornada do colaborador e a estrat&#233;gia de pessoas por tr&#225;s dela."),
    ("I've been leading the culture transformation since 2023.",
     "Lidero a transforma&#231;&#227;o cultural desde 2023."),
    ("At the moment, we're rolling out the framework across every region.",
     "No momento, estamos implantando o framework em todas as regi&#245;es."),
    ("Before I propose anything, I want to carry out a cultural assessment.",
     "Antes de propor qualquer coisa, quero conduzir um diagn&#243;stico cultural."),
]
sp = []
for phrase, pt in SPEECH:
    SPEAKABLE.append(phrase)
    sp.append(
        f'      <div class="speech-card" data-phrase="{phrase}">\n'
        f'        <div class="speech-phrase">{phrase}</div>\n'
        f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
        f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
        f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
        f'        <div class="speech-result"></div>\n'
        f'      </div>'
    )
speech_cards = '\n'.join(sp)

# ---------- Survival card ----------
sv = []
for i, (en, pt) in enumerate(SPEECH, 1):
    sv.append(
        f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
        f'<span class="sp-en">{en}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
    )
survival = '\n'.join(sv)

HTML = f'''<div class="lesson-card" id="ex-lesson-1">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 01 -- Pre-class</div>
      <h3>Diagnostic Session -- Who Is Danielle in English?</h3>
      <div class="lesson-desc">Executive self-positioning in People &amp; Culture: say who you are, what your role involves and what you lead &mdash; in the senior register the Canadian team expects. Key words: organizational culture, employee journey, people strategy, framework, stakeholder, alignment, to roll out, headquarters, franchisor, bilingual education, hybrid model, senior leadership, to make headway, to take a stance, to carry out. Structures: present simple (permanent role) vs present continuous (in progress) vs present perfect continuous (for/since).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. These are the words you already use every day &mdash; now in the register the Canadian team uses.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l1">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Danielle <strong>leads</strong> People and Culture at Maple Bear, a <strong>franchisor</strong> in <strong>bilingual education</strong>. Her role <strong>involves</strong> the <strong>employee journey</strong> &mdash; every stage, from the first interview to the last day &mdash; and the <strong>people strategy</strong> behind it. She <strong>works</strong> closely with <strong>senior leadership</strong>, and she <strong>reports</strong> to the Chief People Officer at <strong>headquarters</strong>. "I <strong>have been leading</strong> the culture transformation since 2023," she says, "and I <strong>have been working</strong> in People and Culture <strong>for</strong> eight years." She <strong>has carried out</strong> four cultural assessments, and she <strong>has built</strong> a <strong>framework</strong> that every <strong>stakeholder</strong> can read. Right now the picture <strong>is</strong> different: at the moment, her team <strong>is rolling out</strong> the new employee journey across every region, and this year she <strong>is preparing</strong> to take on Canada. They <strong>are making headway</strong> on the <strong>hybrid model</strong>, although <strong>alignment</strong> between leadership and the schools <strong>is</strong> still the hardest part. In August she <strong>will meet</strong> the Canadian academic team &mdash; and, before she proposes anything, she <strong>wants</strong> to <strong>carry out</strong> a cultural assessment and <strong>take a stance</strong> of her own.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why do we say "I have been leading the culture transformation since 2023" and not "I am leading it since 2023"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because it started in the past and is still going now &mdash; present perfect continuous with since.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the action is over and has no link to the present.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is a permanent part of her role.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "At the moment, her team is rolling out the new employee journey" uses the present continuous because:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It is a permanent responsibility of the role.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It is in progress right now, temporary &mdash; not the permanent state of things.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It is a finished result, already counted.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence about her permanent role is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She is leading People and Culture since eight years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She leads People and Culture, and her role involves the employee journey."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She has been leading People and Culture in 2023."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Simple vs Present Continuous vs Present Perfect (Continuous)</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The three forms that carry your professional story &mdash; the ones the Canadian team will hear in your first two minutes.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / we + verb (she + s)</td><td style="padding:.6rem">Permanent role and what it involves.</td><td style="padding:.6rem">I <strong>lead</strong> People and Culture.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Continuous<br>am / is / are + -ing</td><td style="padding:.6rem">In progress right now, temporary (at the moment, this year).</td><td style="padding:.6rem">We <strong>are rolling out</strong> the framework.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Perfect Continuous<br>have been + -ing</td><td style="padding:.6rem">Started in the past and is <strong>still going</strong> &mdash; with for / since.</td><td style="padding:.6rem">I <strong>have been leading</strong> it since 2023.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have + past participle</td><td style="padding:.6rem">A finished, countable result, with no time said.</td><td style="padding:.6rem">I <strong>have carried out</strong> four assessments.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">have / has + not + past participle. In speech, contracted: <strong>haven't</strong>.</td><td style="padding:.6rem">We <strong>haven't</strong> rolled it out in Canada yet.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">How long + have + subject + been + -ing?</td><td style="padding:.6rem"><strong>How long have you been leading</strong> this?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">for vs since</td><td style="padding:.6rem" colspan="2"><strong>for</strong> + a period (for eight years) &middot; <strong>since</strong> + a starting point (since 2023)</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the classic senior slip):</strong> duration up to now <strong>never</strong> takes the present simple or the present continuous. "I am leading this transformation since 2023" is wrong &mdash; the correct form is "I <strong>have been leading</strong> this transformation since 2023" (in speech, <strong>I've been leading</strong>). Nothing makes you sound junior faster than this one.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Collocation (the other slip):</strong> we do not say "make a research" or "make an assessment" &mdash; we say <strong>carry out</strong> research / <strong>carry out</strong> an assessment. And it is not "responsible <em>by</em>", it is <strong>responsible for</strong>.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the First Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of your first conversation with the Canadian leadership in the correct order.</p>
      <div class="order-container" id="order-l1">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Take a stance: say what you bring and what you don't bring.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Say what your role involves: the employee journey and the people strategy.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Propose the first step: carry out a cultural assessment with each leader.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Introduce yourself: who you are and what you lead.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Explain how long you've been leading the culture transformation.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l1')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that open any conversation of yours in Canada.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your first week in Canada.</p>
      <div class="quiz-item"><div class="quiz-question">A Canadian director asks: "So, what do you do?" You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I work with the people in the company."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I lead People and Culture at Maple Bear, and my role involves the employee journey and the people strategy behind it."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am responsible by the culture things in the company."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks: "How long have you been doing this?" The best answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am leading the culture transformation since 2023."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I've been leading the culture transformation since 2023."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I lead the culture transformation for three years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to describe what your team is doing right now, this quarter. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "At the moment, we're rolling out the new employee journey across every region."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "At the moment, we roll out the new employee journey across every region."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "At the moment, we have rolled out the new employee journey since every region."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say you will run a cultural diagnosis before proposing anything. The natural collocation is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I want to make a research with the leaders."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I want to carry out a cultural assessment with the leaders."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I want to do a culture check in the leaders."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">An academic director challenges your framework in front of the team. The most senior move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Apologize, say your English isn't good enough, and move on.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "That's a fair challenge. To some extent, I agree &mdash; but let me take a stance: the framework is a starting point, not an answer."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Agree with everything to avoid conflict in the first meeting.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for two or three minutes, with no script. This recording is your baseline for the programme.</p>
      <div class="think-card">
        <div class="think-question">You've just joined a video call with two Canadian directors you have never met. Introduce yourself: your role (present simple), what you're rolling out right now (present continuous), how long you've been leading the culture transformation (present perfect continuous, for/since), and what you want to carry out in your first thirty days in Canada. Take your time, and don't read from a script.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-1"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 1</h4>
{survival}
    </div>

  </div>
</div>
'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

# ---------- auto-verificacao do GATE botao morto ----------
bad = re.findall(r"speakText\('[^']*'[^)]*\)", HTML)
assert not bad, f'texto dentro de argumento de onclick (botao morto): {bad[:3]}'
assert 'this.dataset.speak' in HTML

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
print('com contracao:', sorted({s for s in SPEAKABLE if "'" in s}))
