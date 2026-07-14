#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 2 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
"""
import os
import random

random.seed(2)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("To specialize in", "to focus your career on one specific area of expertise", "especializar-se em",
     "\"I specialize in CBTC signaling for metro lines.\""),
    ("To coordinate", "to organize people and activities so that they work together", "coordenar",
     "\"I coordinate the design team and the field team.\""),
    ("To liaise with", "to be the bridge between two sides and exchange information with them", "fazer a ponte com",
     "\"I liaise with the German and Spanish suppliers every week.\""),
    ("To carry out", "to perform and complete a task, a test or an inspection", "realizar, executar",
     "\"We carry out the inspection at the supplier's factory.\""),
    ("To look into", "to investigate a problem before you answer or decide", "investigar",
     "\"I will look into the delay and come back to you tomorrow.\""),
    ("To come up with", "to propose a solution or produce an idea", "bolar, propor",
     "\"The team came up with a workaround in two days.\""),
    ("Interface document", "the document that defines how two systems connect to each other", "documento de interface",
     "\"The interface document is signed by both suppliers.\""),
    ("Subcontractor", "a company hired by the main contractor to do one part of the work", "subcontratada",
     "\"The cabling is done by a local subcontractor.\""),
    ("Procurement", "the process of buying the equipment and the services a project needs", "suprimentos, compras",
     "\"Procurement placed the order three months late.\""),
    ("Handover", "the formal moment when you transfer a finished system to the client", "entrega formal",
     "\"The handover to the operator is planned for June.\""),
    ("Workstream", "one parallel line of work inside a bigger project", "frente de trabalho",
     "\"I run the signaling workstream on the Line 5 extension.\""),
    ("Counterpart", "the person who has the same role as you in the other company", "contraparte",
     "\"My counterpart in Madrid signs the interface document.\""),
    ("Lead time", "the time between placing an order and receiving the equipment", "prazo de entrega",
     "\"The lead time for the interlocking is nine months.\""),
    ("Tip of the iceberg", "a small visible problem that signals a much bigger one under the surface", "ponta do iceberg",
     "\"The late drawings are just the tip of the iceberg.\""),
]

SURVIVAL = [
    ("I'm responsible for the signaling workstream on the Line 5 extension.",
     "Sou responsável pela frente de sinalização da extensão da Linha 5."),
    ("My role involves coordinating the design and field teams.",
     "Meu papel envolve coordenar as equipes de projeto e de campo."),
    ("We're currently in the process of closing the design review.",
     "Estamos atualmente em processo de fechar a revisão de projeto."),
    ("If the interface document had arrived earlier, we would have completed the handover on time.",
     "Se o documento de interface tivesse chegado antes, teríamos concluído a entrega no prazo."),
    ("One of the main challenges we face is the lead time for the interlocking.",
     "Um dos principais desafios que enfrentamos é o prazo de entrega do intertravamento."),
]


def esc(s):
    """ASCII-safe: acentos e aspas viram entidades HTML."""
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        else:
            out.append(f'&#{ord(ch)};')
    return ''.join(out)


def vocab_cards():
    rows = []
    for word, d, pt, ex in VOCAB:
        rows.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{esc(word)}</span>'
            f'<span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{esc(d)}</span></div>'
            f'<div class="vocab-card-example">{esc(ex)}</div></div>'
            f'<button class="audio-btn" data-speak="{esc(word)}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
    return '\n'.join(rows)


def match_grid():
    defs = [d for _, d, _, _ in VOCAB]
    rows = []
    for word, d, _, _ in VOCAB:
        opts = defs[:]
        while True:
            random.shuffle(opts)
            if opts != defs:
                break
        o = ''.join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in opts)
        rows.append(
            f'        <div class="match-row" data-answer="{esc(d)}">'
            f'<span class="match-word" style="flex:0 0 150px">{esc(word)}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    return '\n'.join(rows)


CONTEXT = """<p>Jo&#227;o Guilherme <strong>is responsible for</strong> the signaling <strong>workstream</strong> on the Line 5 extension. He <strong>specializes in</strong> CBTC, he <strong>coordinates</strong> the design team and the field team, and he <strong>liaises with</strong> every supplier on the package. His <strong>counterpart</strong> at each supplier signs the <strong>interface document</strong> that defines how the two systems connect. Every quarter he <strong>carries out</strong> a factory inspection in Europe, and the cabling on site is done by a local <strong>subcontractor</strong>.</p>
        <p>The project is three months late, and the retrospective is honest. <strong>If</strong> the <strong>interface document</strong> <strong>had arrived</strong> in January, the team <strong>would have completed</strong> the design review before the summer. <strong>If</strong> <strong>procurement</strong> <strong>had been</strong> involved in that review, the order <strong>would have been placed</strong> in January and the nine-month <strong>lead time</strong> <strong>would not have hurt</strong> the schedule. <strong>If</strong> somebody <strong>had looked into</strong> the first alarm in March, the team <strong>would have come up with</strong> a workaround in April.</p>
        <p>Today the <strong>handover</strong> to the operator is still officially planned for June, and nobody believes that date. As Jo&#227;o says on the call with the new supplier: "Honestly, the late document is only the <strong>tip of the iceberg</strong>. One of the main challenges we face is the <strong>lead time</strong>, and I would rather bring a realistic date than an optimistic one."</p>"""

QUIZZES_CONTEXT = [
    ("1. \"If the interface document had arrived in January, the team would have completed the design review before the summer.\" Did the document arrive in January?",
     [("No. The third conditional describes an IMAGINED past &mdash; the condition did not happen, so the result did not happen either.", True),
      ("Yes. It arrived in January and the design review was closed.", False),
      ("We still don&#39;t know &mdash; the sentence is about the future.", False)]),
    ("2. What is the correct form of the CONDITION in the third conditional?",
     [("If + would have + past participle", False),
      ("If + had + past participle", True),
      ("If + past simple", False)]),
    ("3. \"If procurement had been involved earlier, the order would have been placed in January.\" Why is this sentence more professional than \"Procurement forgot the order\"?",
     [("Because it is longer and sounds more formal.", False),
      ("Because it describes the PROCESS that failed, without blaming a person or a company &mdash; the language of a retrospective.", True),
      ("Because it avoids mentioning the delay.", False)]),
    ("4. Which sentence is correct?",
     [("\"If they would have signed the document, we would have finished on time.\"", False),
      ("\"If they had signed the document, we would finished on time.\"", False),
      ("\"If they had signed the document, we would have finished on time.\"", True)]),
]

BLANKS = [
    ("had arrived", "Hint: the CONDITION of the third conditional &mdash; had + past participle",
     "If the interface document had arrived in January, we would have completed the handover on time.",
     '"If the interface document ', ' in January, we would have completed the handover on time."'),
    ("would have completed", "Hint: the RESULT of the third conditional &mdash; would have + past participle",
     "If the supplier had delivered on time, we would have completed the commissioning in March.",
     '"If the supplier had delivered on time, we ', ' the commissioning in March."'),
    ("liaise with", "Hint: to be the bridge between two sides and exchange information with them",
     "I liaise with every supplier on the signaling package.",
     '"I ', ' every supplier on the signaling package."'),
    ("carry out", "Hint: to perform and complete an inspection (never say realize an inspection)",
     "We carry out the inspection at the factory before the shipment.",
     '"We ', ' the inspection at the factory before the shipment."'),
    ("responsible for", "Hint: never responsible OF &mdash; the preposition is for",
     "I am responsible for the signaling workstream on the Line 5 extension.",
     '"I am ', ' the signaling workstream on the Line 5 extension."'),
    ("lead time", "Hint: the time between placing an order and receiving the equipment",
     "The lead time for the interlocking is nine months.",
     '"The ', ' for the interlocking is nine months."'),
]

ORDER = [
    (1, "Thank the new supplier for joining and confirm everyone can hear you."),
    (2, "Describe your role: the workstream you are responsible for and who you coordinate."),
    (3, "Give the current status: where the project stands right now."),
    (4, "Explain what went wrong, using the third conditional instead of blaming anyone."),
    (5, "Name the main challenge ahead and agree on who looks into it, and by when."),
]

SPEECH = [
    ("I'm responsible for the signaling workstream on the Line 5 extension.",
     "Sou responsável pela frente de sinalização da extensão da Linha 5."),
    ("My role involves coordinating the design and field teams.",
     "Meu papel envolve coordenar as equipes de projeto e de campo."),
    ("I liaise with every supplier and I carry out the factory inspections.",
     "Faço a ponte com todos os fornecedores e realizo as inspeções de fábrica."),
    ("If the interface document had arrived earlier, we would have completed the handover on time.",
     "Se o documento de interface tivesse chegado antes, teríamos concluído a entrega no prazo."),
    ("Honestly, the late document is only the tip of the iceberg.",
     "Sinceramente, o documento atrasado é apenas a ponta do iceberg."),
]

QUIZZES_SIT = [
    ("A new supplier joins the project and asks: \"What exactly do you own here?\" You answer:",
     [("\"I am responsible of the signaling things on Line 5.\"", False),
      ("\"I'm responsible for the signaling workstream on the Line 5 extension, and I coordinate the design and field teams.\"", True),
      ("\"I make the signaling and I see the suppliers.\"", False)]),
    ("She asks why the design review is still open. The most professional answer is:",
     [("\"If the interface document had arrived in January, we would have closed the review before the summer.\"", True),
      ("\"The other supplier is incompetent and sent the document three months late.\"", False),
      ("\"If the interface document would have arrived in January, we would close the review.\"", False)]),
    ("You do not have the answer to a technical question during the call. You say:",
     [("\"I don't know, sorry.\"", False),
      ("\"I will look into it and come back to you on Friday with a date.\"", True),
      ("\"Ask my manager, it is not my area.\"", False)]),
    ("The late document is not the only problem. You want to signal a bigger issue without alarming anyone. You say:",
     [("\"Everything is fine, do not worry.\"", False),
      ("\"Honestly, the late document is only the tip of the iceberg.\"", True),
      ("\"This project is a complete disaster.\"", False)]),
    ("Which sentence describes the process of buying the equipment a project needs?",
     [("\"Procurement placed the order in April.\"", True),
      ("\"The handover placed the order in April.\"", False),
      ("\"The workstream placed the order in April.\"", False)]),
]


def quiz_html(items, start=1):
    out = []
    for i, (q, opts) in enumerate(items):
        qq = q if q[0].isdigit() else f'{q}'
        o = []
        for j, (text, correct) in enumerate(opts):
            letter = 'ABC'[j]
            o.append(
                f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}">'
                f'<span class="option-letter">{letter}</span> {text}</div>')
        out.append(
            f'      <div class="quiz-item"><div class="quiz-question">{qq}</div>'
            f'<div class="quiz-options">{"".join(o)}</div></div>')
    return '\n'.join(out)


def blanks_html():
    out = []
    for ans, hint, phrase, pre, post in BLANKS:
        out.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{esc(pre)}'
            f'<input class="blank-input" data-answer="{esc(ans)}" data-hint="{hint}" '
            f'data-phrase="{esc(phrase)}" placeholder="___">{esc(post)}</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    return '\n'.join(out)


def order_html():
    items = ORDER[:]
    random.shuffle(items)
    out = []
    for n, text in items:
        out.append(
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
    return '\n'.join(out)


def speech_html():
    out = []
    for en, pt in SPEECH:
        out.append(
            f'      <div class="speech-card" data-phrase="{esc(en)}">\n'
            f'        <div class="speech-phrase">{esc(en)}</div>\n'
            f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
            f'        <div class="speech-result"></div>\n'
            f'      </div>')
    return '\n'.join(out)


def survival_html():
    out = []
    for i, (en, pt) in enumerate(SURVIVAL, 1):
        out.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{esc(en)}</span>'
            f'<button class="btn btn-listen" data-speak="{esc(en)}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
    return '\n'.join(out)


GRAMMAR_TIP = """      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Affirmative<br>If + <strong>had</strong> + past participle, <strong>would have</strong> + past participle</td><td style="padding:.6rem">An imagined past: the condition did not happen, so the result did not happen either.</td><td style="padding:.6rem">If the supplier <strong>had delivered</strong> on time, we <strong>would have completed</strong> the handover in March.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem"><strong>wouldn't have</strong> + past participle. In speech, always contracted.</td><td style="padding:.6rem">If we <strong>had involved</strong> procurement earlier, we <strong>wouldn't have missed</strong> the milestone.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">What <strong>would have happened</strong> if + had + past participle?</td><td style="padding:.6rem"><strong>What would have happened if</strong> the order <strong>had been placed</strong> in January?</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">In speech (contraction)</td><td style="padding:.6rem">Both halves contract &mdash; this is what you actually hear on a call.</td><td style="padding:.6rem">If they<strong>'d</strong> sent the drawings, we<strong>'d have</strong> caught the error.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Second conditional (contrast)<br>If + past simple, would + verb</td><td style="padding:.6rem">An unreal present or future &mdash; not the past.</td><td style="padding:.6rem">If we <strong>had</strong> more time, we <strong>would run</strong> another test tomorrow.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">The third conditional lets you review a missed milestone as a <strong>process</strong> failure instead of one person&#39;s fault. It is the language of a professional retrospective &mdash; and what separates a senior engineer from an angry one.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (classic mistake):</strong> the temptation is to put <strong>would have</strong> in BOTH halves &mdash; "if the supplier <strong>would have</strong> delivered". In English that is WRONG: the condition ALWAYS takes <strong>had + past participle</strong> ("if the supplier <strong>had delivered</strong>"). <strong>Would have</strong> belongs only in the RESULT.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-2">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 02 -- Pre-class</div>
      <h3>Reactivating Your Professional Voice -- Roles, Responsibilities and Ongoing Projects</h3>
      <div class="lesson-desc">Describe your role at Motiva and run a project retrospective without blaming anyone. Key words: to specialize in, to coordinate, to liaise with, to carry out, to look into, to come up with, interface document, subcontractor, procurement, handover, workstream, counterpart, lead time, tip of the iceberg. Structure: third conditional (If + had + past participle, would have + past participle) + the patterns "I'm responsible for / My role involves / We're currently in the process of".</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">In Lesson 1 you named the THINGS on a project. Here you name the ACTIONS: what you do, who you do it with, and what you deliver. Listen to each term and read the example sentence.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match every term with the right definition.</p>
      <div class="match-grid" id="match-l2">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text, then answer the questions below it.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Third Conditional</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to tell the story of what SHOULD have happened on a project &mdash; without blaming anyone.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete every sentence with the right form. Tap Listen to hear the full sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Project Update in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a project update to a new supplier in the right order.</p>
      <div class="order-container" id="order-l2">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l2')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, then record yourself saying it. These five sentences describe your role in any international meeting.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Pick the strongest answer for these real moments of a project update.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. Speak for 90 seconds, with no script and no stopping to fix yourself.</p>
      <div class="think-card">
        <div class="think-question">A new international supplier joins your project today. Introduce your role (I'm responsible for... / My role involves...), describe where the project stands (We're currently in the process of...), explain ONE thing that went wrong using the third conditional (If the interface document had arrived in January, we would have...), and name the main challenge ahead (One of the main challenges we face is...). Do not blame anyone -- describe the process.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-2"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 2</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
