#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 3 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 3 IN CLASS (mesmo tema/gramática/vocab).
"""
import os
import random

random.seed(3)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Non-conformance", "a documented failure to meet a requirement of the specification", "não conformidade",
     "\"We raised a non-conformance on the cable routing.\""),
    ("Punch list", "the list of small open items that must be closed before acceptance", "lista de pendências",
     "\"Three items on the punch list are still open.\""),
    ("Hold point", "a stage where the work must STOP until the inspection has been done", "ponto de parada obrigatória",
     "\"The cable test is a hold point -- nobody continues without us.\""),
    ("Witness point", "an inspection you may attend, but the work does not stop if you do not", "ponto de testemunho",
     "\"The insulation test is a witness point, not a hold point.\""),
    ("Inspection test plan (ITP)", "the document that lists every test, who attends it and when", "plano de inspeção e testes",
     "\"The ITP defines every hold point on the project.\""),
    ("Factory acceptance test (FAT)", "the test you run at the supplier's factory, before anything is shipped", "teste de aceitação em fábrica",
     "\"The FAT in Berlin is scheduled for October.\""),
    ("Site acceptance test (SAT)", "the same test, repeated on site after the equipment is installed", "teste de aceitação em campo",
     "\"The SAT starts two weeks after installation.\""),
    ("Escalation", "taking an unresolved issue to a higher level of management", "escalonamento",
     "\"If the date slips again, escalation is the only option left.\""),
    ("Corrective action", "the concrete step a supplier takes to fix a non-conformance", "ação corretiva",
     "\"We agreed on a corrective action with a deadline.\""),
    ("Waiver", "a formal written permission to skip one requirement, just once", "dispensa formal",
     "\"They asked for a waiver on the insulation test.\""),
    ("Baseline schedule", "the approved schedule that every delay is measured against", "cronograma de referência",
     "\"The revised baseline schedule is three weeks late.\""),
    ("To follow up on", "to check again on something you have already asked for", "dar seguimento a, cobrar",
     "\"I'm following up on the ITP we requested last week.\""),
    ("To flag up", "to raise a problem early, so that nobody is surprised later", "sinalizar",
     "\"I want to flag up a risk on the delivery date.\""),
    ("To push back on", "to question or resist a request politely, but firmly", "questionar, resistir a",
     "\"I have to push back on that date -- it is not realistic.\""),
]

SURVIVAL = [
    ("I'd like to follow up on the revised baseline schedule.",
     "Gostaria de dar seguimento ao cronograma de referência revisado."),
    ("The inspection test plan should have been submitted by last Friday.",
     "O plano de inspeção e testes deveria ter sido enviado até a sexta-feira passada."),
    ("There must have been a miscommunication about the hold points.",
     "Deve ter havido um ruído de comunicação sobre os pontos de parada."),
    ("To some extent I understand your position, however I have to push back on that date.",
     "Em certa medida eu entendo a sua posição, no entanto preciso questionar essa data."),
    ("Can we agree on a corrective action and a new deadline?",
     "Podemos combinar uma ação corretiva e um novo prazo?"),
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
            f'<span class="match-word" style="flex:0 0 190px">{esc(word)}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    return '\n'.join(rows)


CONTEXT = """<p>It is Monday morning and Jo&#227;o Guilherme is chairing the status meeting with CASCO. Four items are open on the <strong>punch list</strong>. The revised <strong>baseline schedule</strong> is three weeks overdue, the <strong>inspection test plan</strong> was submitted with no <strong>hold points</strong>, a <strong>waiver</strong> was requested on the insulation test, and a <strong>non-conformance</strong> is still waiting for a <strong>corrective action</strong>.</p>
        <p>He opens the call. "I would like to <strong>follow up on</strong> the schedule. It <strong>should have reached</strong> us on June 10th, and we are now planning the <strong>site acceptance test</strong> without a date. There <strong>must have been</strong> a bottleneck on your side." The supplier answers that her team <strong>might have been</strong> waiting for the interface document &mdash; but that document was signed in April, and Jo&#227;o has to <strong>push back on</strong> it. Politely: "To some extent I understand your position, however the document was signed in April."</p>
        <p>Then he <strong>flags up</strong> the second issue. The ITP arrived with <strong>witness points</strong> only, which means the factory never stops for Motiva. "That <strong>should have been</strong> discussed with us before the plan was submitted." They agree on a corrective action, a new date, and one last rule: if the date slips again, <strong>escalation</strong> is the next step. The <strong>factory acceptance test</strong> in October is already at risk, and nobody wants to discover that in an email."""

QUIZZES_CONTEXT = [
    ("1. \"The revised baseline schedule should have reached us on June 10th.\" Did the schedule arrive on June 10th?",
     [("No. <em>Should have</em> + past participle describes an obligation that was NOT met &mdash; the criticism lands on the ACTION, not on the person.", True),
      ("Yes. It arrived on time and the item was closed.", False),
      ("We still do not know &mdash; the sentence is about the future.", False)]),
    ("2. \"There must have been a bottleneck on your side.\" What does <em>must have</em> express here?",
     [("An obligation that was not met.", False),
      ("A logical DEDUCTION: from the evidence, the speaker is almost certain about what happened.", True),
      ("A remote, uncertain possibility.", False)]),
    ("3. Why is \"It should have been discussed with us\" more professional than \"You didn't discuss it with us\"?",
     [("Because it is longer and sounds more formal.", False),
      ("Because it states a fact about the PROCESS without attacking the person &mdash; the supplier can agree without losing face, and the meeting ends in a corrective action instead of a fight.", True),
      ("Because it avoids mentioning the problem.", False)]),
    ("4. Which sentence is correct?",
     [("\"The supplier should had submitted the ITP in May.\"", False),
      ("\"The supplier should have submitted the ITP in May.\"", True),
      ("\"The supplier should have submit the ITP in May.\"", False)]),
]

BLANKS = [
    ("should have reached", "Hint: an obligation that was NOT met &mdash; should have + past participle",
     "The revised baseline schedule should have reached us on June 10th.",
     '"The revised baseline schedule ', ' us on June 10th."'),
    ("must have been", "Hint: a DEDUCTION about the past &mdash; must have + past participle (never &#39;must be&#39;)",
     "There must have been a miscommunication about the hold points.",
     '"There ', ' a miscommunication about the hold points."'),
    ("might have been sent", "Hint: an UNCERTAIN possibility &mdash; might have + past participle (passive voice)",
     "The drawings might have been sent to the wrong contact.",
     '"The drawings ', ' to the wrong contact."'),
    ("follow up on", "Hint: to chase again something you have already asked for &mdash; and the preposition is ON",
     "I would like to follow up on the revised baseline schedule.",
     '"I would like to ', ' the revised baseline schedule."'),
    ("push back on", "Hint: to question something firmly but politely &mdash; and the preposition is ON",
     "I have to push back on that date, it is not realistic.",
     '"I have to ', ' that date, it is not realistic."'),
    ("corrective action", "Hint: the concrete step a supplier takes to fix a non-conformance",
     "Can we agree on a corrective action and a new deadline?",
     '"Can we agree on a ', ' and a new deadline?"'),
]

ORDER = [
    (1, "Thank the supplier for joining and state the agenda: the open items on the punch list."),
    (2, "Follow up on the overdue item and say what should have happened, and when."),
    (3, "Deduce the cause with a modal perfect, instead of accusing the supplier."),
    (4, "Push back diplomatically when the supplier moves the responsibility to you."),
    (5, "Agree on a corrective action with a date, and say what happens if the date slips again."),
]

SPEECH = [
    ("I'd like to follow up on the revised baseline schedule.",
     "Gostaria de dar seguimento ao cronograma de referência revisado."),
    ("The inspection test plan should have been submitted by last Friday.",
     "O plano de inspeção e testes deveria ter sido enviado até a sexta-feira passada."),
    ("There must have been a miscommunication about the hold points.",
     "Deve ter havido um ruído de comunicação sobre os pontos de parada."),
    ("To some extent I understand your position, however I have to push back on that date.",
     "Em certa medida eu entendo a sua posição, no entanto preciso questionar essa data."),
    ("Can we agree on a corrective action and a new deadline?",
     "Podemos combinar uma ação corretiva e um novo prazo?"),
]

QUIZZES_SIT = [
    ("You open the status meeting. The revised baseline schedule is three weeks overdue. You say:",
     [("\"You are three weeks late. Again.\"", False),
      ("\"I'd like to follow up on the revised baseline schedule &mdash; it should have reached us on June 10th.\"", True),
      ("\"Where is the schedule? I asked many times.\"", False)]),
    ("The supplier blames YOU: \"We were waiting for your interface document.\" It was signed in April. You answer:",
     [("\"To some extent I understand your position, however the interface document was signed in April. I have to push back on that.\"", True),
      ("\"That is a lie and you know it.\"", False),
      ("\"Ok, maybe it was our fault, let's move on.\"", False)]),
    ("The ITP arrived with no hold points, only witness points. The most professional way to raise it is:",
     [("\"You removed our hold points on purpose.\"", False),
      ("\"I'd like to flag up an issue: the ITP has no hold points. That should have been discussed with us before it was submitted.\"", True),
      ("\"The ITP is wrong. Send it again.\"", False)]),
    ("The equipment arrived damaged and nobody knows why. You want to deduce the cause without accusing anyone. You say:",
     [("\"Somebody in your factory was careless.\"", False),
      ("\"There must have been a problem in transport &mdash; or it might have been damaged before it left the factory.\"", True),
      ("\"It must be a problem in transport last week.\"", False)]),
    ("The supplier asks for a waiver that saves them three days in the factory but risks three weeks on site. You:",
     [("\"Sure, no problem, we can skip that test.\"", False),
      ("\"One could argue that three days in the factory cost us three weeks during the site acceptance test. I'm afraid I have to push back on that waiver.\"", True),
      ("\"Waivers are always forbidden here.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Affirmative<br><strong>should have</strong> + past participle</td><td style="padding:.6rem">An obligation that was NOT met. The criticism lands on the action, never on the person.</td><td style="padding:.6rem">"The ITP <strong>should have been</strong> submitted on June 3rd."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>must have</strong> + past participle</td><td style="padding:.6rem">A logical DEDUCTION about the past: from the evidence, you are almost certain. It sounds analytical, not accusatory.</td><td style="padding:.6rem">"There <strong>must have been</strong> a bottleneck on your side."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>might / may have</strong> + past participle</td><td style="padding:.6rem">An uncertain POSSIBILITY. It opens a door and lets the other side save face.</td><td style="padding:.6rem">"The drawings <strong>might have been sent</strong> to the wrong contact."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative / impossible<br><strong>could not have</strong> + past participle</td><td style="padding:.6rem">IMPOSSIBILITY: the evidence rules the hypothesis out.</td><td style="padding:.6rem">"They <strong>could not have run</strong> the FAT without the cabinet."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">What <strong>should have happened</strong>? / <strong>Could</strong> it <strong>have been</strong> lost?</td><td style="padding:.6rem"><strong>"What should have happened</strong> after the design review?"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">In speech (contraction)</td><td style="padding:.6rem">The <em>have</em> reduces to /&#601;v/ &mdash; that is what you actually hear on a call.</td><td style="padding:.6rem">"It <strong>should've been</strong> flagged up." &middot; "They <strong>must've missed</strong> it."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">"You didn't deliver" attacks a person and the meeting stalls. "<strong>This should have been delivered</strong>" states a fact about the process &mdash; and the supplier can agree without losing face. That is how you walk out of the meeting with a <strong>corrective action</strong> instead of an enemy.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (two classic mistakes):</strong> (1) after a modal, it is ALWAYS <strong>have</strong>, never <em>had</em> &mdash; "should <strong>have</strong> submitted", never "should <em>had</em> submitted"; (2) to deduce something about the PAST, the present tense is not enough: "it <em>must be</em> a miscommunication" talks about right now. About the past, the correct form is "there <strong>must have been</strong> a miscommunication".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Hedging &mdash; the language of diplomatic disagreement:</strong> "<strong>It would appear that...</strong>" (instead of "you are wrong"), "<strong>One could argue that...</strong>" (instead of "that makes no sense"), "<strong>To some extent I understand your position, however...</strong>" (instead of a flat "no"). These are the three formulas that carry a disagreement without breaking the relationship &mdash; and that read well in the minutes your director will see."""


HTML = f"""<div class="lesson-card" id="ex-lesson-3">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 03 -- Pre-class</div>
      <h3>Running and Following Status Meetings -- Reporting, Updating and Pushing Back</h3>
      <div class="lesson-desc">Chair a status meeting with a late supplier: report the facts, deduce the cause and push back on the date without breaking the relationship. Key words: non-conformance, punch list, hold point, witness point, inspection test plan (ITP), factory acceptance test (FAT), site acceptance test (SAT), escalation, corrective action, waiver, baseline schedule, to follow up on, to flag up, to push back on. Structure: modal perfects (should have / must have / might have / could not have + past participle) + hedging ("It would appear that...", "One could argue that...", "To some extent I understand your position, however...").</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">In Lesson 2 you named the ACTIONS of your role. Here you name the AGENDA of the meeting: what gets inspected, what gets found, and what gets done about it. You already know every one of these concepts from the job &mdash; all you are changing is the label. Listen to each term and read the example sentence.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l3">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions below.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Modal Perfects</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to say what SHOULD have been done, deduce WHY it was not, and disagree without breaking the relationship.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Status Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the stages of a status meeting with a late supplier in the correct order.</p>
      <div class="order-container" id="order-l3">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l3')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that open, carry and close any status meeting. Notice how <em>have</em> contracts in speech: "should've been", "must've been".</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of a status meeting &mdash; including the one where the supplier hands the blame back to you.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for 2 minutes, with no script and without stopping to correct yourself. Tone: professional, firm, never confrontational.</p>
      <div class="think-card">
        <div class="think-question">Open a status meeting with a supplier who is three weeks late on the revised baseline schedule. Follow up on the overdue item (I'd like to follow up on...), state the obligation that was not met (It should have reached us on...), deduce the cause without accusing anyone (There must have been... / It might have been...), push back diplomatically when the supplier moves the responsibility to you (To some extent I understand your position, however...), and close by agreeing on a corrective action with a new deadline.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-3"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 3</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
