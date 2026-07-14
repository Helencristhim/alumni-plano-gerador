#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 6 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 6 IN CLASS (mesmo tema/gramática/vocab — passiva avançada + causativo).
"""
import os
import random

random.seed(6)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Deviation", "a departure from what the approved specification requires", "desvio (aprovado antes da execução)",
     "\"The deviation was accepted in writing, so no rework is required.\""),
    ("Submittal", "a document the supplier formally sends to the client for review and approval", "documento submetido à aprovação",
     "\"The submittal was returned with comments on Tuesday.\""),
    ("Approval workflow", "the sequence of reviews a document must pass before it is accepted", "fluxo de aprovação",
     "\"The drawing is stuck in the approval workflow, not on my desk.\""),
    ("Inspection release", "the formal authorization to ship, or to move to the next stage, after an inspection", "liberação de inspeção",
     "\"No inspection release has been issued, so nothing leaves the factory.\""),
    ("Out of tolerance", "outside the range of values the specification allows", "fora de tolerância",
     "\"The relay was found to be out of tolerance during the functional test.\""),
    ("Calibration certificate", "the document that proves an instrument was verified against a reference", "certificado de calibração",
     "\"The calibration certificate had not been issued at the time of the test.\""),
    ("Traceability", "being able to track a part back to its material, its test and its records", "rastreabilidade",
     "\"In signaling, a component without traceability does not exist.\""),
    ("Root cause", "the underlying reason a failure happened, not the symptom you can see", "causa raiz",
     "\"The root cause has not been identified yet, so the corrective action is premature.\""),
    ("Rework", "work that has to be done a second time to correct a defect", "retrabalho",
     "\"The rework will be carried out at the supplier's own cost.\""),
    ("Sign-off", "the formal written approval that closes a stage and lets the project move on", "aprovação formal, aceite",
     "\"I cannot give you sign-off until the calibration certificate is on file.\""),
    ("To downplay", "to make a problem sound smaller than it really is", "minimizar (um problema)",
     "\"He downplayed the failure: 'It is a minor deviation, nothing more.'\""),
    ("To raise a concern", "to put a risk formally on the record, before it becomes a problem", "levantar uma preocupação formalmente",
     "\"I would like to raise a concern about the traceability of that batch.\""),
    ("To hold your ground", "to keep your position when the other side pushes back", "manter a sua posição",
     "\"He downplayed it twice, and twice I held my ground.\""),
    ("To pass the buck", "to shift responsibility to somebody else instead of owning it (informal)", "empurrar a responsabilidade para outro",
     "\"Blaming the subcontractor is passing the buck: our contract is with you.\""),
]

SURVIVAL = [
    ("The relay was found to be out of tolerance during the functional test.",
     "O relé foi constatado fora de tolerância durante o teste funcional."),
    ("The calibration certificate had not been issued at the time of the test.",
     "O certificado de calibração não havia sido emitido na data do teste."),
    ("It would appear that the deviation was caused by the calibration drift.",
     "Tudo indica que o desvio foi causado pela deriva de calibração."),
    ("We need to have the report resubmitted by Friday.",
     "Precisamos que o relatório seja reenviado até sexta-feira."),
    ("Sign-off cannot be granted while the hold point remains open.",
     "O aceite não pode ser concedido enquanto o hold point permanecer aberto."),
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


CONTEXT = """<p>The factory acceptance test <strong>was carried out</strong> on a Tuesday morning, with Jo&#227;o Guilherme watching on a video link from S&#227;o Paulo. The safety relay <strong>was found to be</strong> <strong>out of tolerance</strong>: eleven milliseconds, against a specified range of five to seven. The test <strong>was witnessed</strong>, a hold point <strong>was triggered</strong>, and no <strong>inspection release</strong> <strong>was issued</strong>. Then the report arrived from the supplier, and every sentence in it had been written to make the failure disappear.</p>
        <p>Two things <strong>had not been done</strong> at the time of the test. The <strong>calibration certificate</strong> for the reference instrument <strong>had not been issued</strong>, and the <strong>root cause</strong> <strong>had not been identified</strong>. The report calls the failure a minor <strong>deviation</strong> and asks for a waiver, which is the polite way of asking Jo&#227;o to pay for somebody else's <strong>rework</strong>. On the call, the quality manager <strong>downplays</strong> it &mdash; "the unit works" &mdash; and then <strong>passes the buck</strong>: the calibration, she says, was performed by a subcontractor. Jo&#227;o <strong>holds his ground</strong>. A deviation is approved <em>before</em> the work; this was found <em>after</em> it. The contract is with her company, not with the subcontractor.</p>
        <p>So he states what has to happen, and he states it in the passive, because the obligation belongs to the procedure and not to him. "A corrective action <strong>must be implemented</strong> before the retest. We need to <strong>have the report resubmitted</strong> through the <strong>approval workflow</strong> by Friday, and we will <strong>have the relay retested</strong> with a valid certificate in place. I would also like to <strong>raise a concern</strong> about the <strong>traceability</strong> of that batch. <strong>Sign-off</strong> <strong>cannot be granted</strong> while the hold point remains open." Nobody <strong>was accused</strong>. Nothing <strong>was denied</strong>. And the relay is being retested on Thursday."""

QUIZZES_CONTEXT = [
    ("1. \"The relay was found to be out of tolerance.\" Why does the engineer choose the passive here, instead of \"Your technician calibrated it badly\"?",
     [("Because the passive is more polite, even though it is weaker.", False),
      ("Because the passive takes the PERSON out of the sentence and leaves the FACT. An accusation can be disputed and defended; a finding can only be CLOSED &mdash; and that is why every inspection report is written this way.", True),
      ("Because the active voice is not allowed in technical English.", False)]),
    ("2. \"The calibration certificate had not been issued at the time of the test.\" What does the PERFECT passive do here that the simple passive would not do?",
     [("It dates the absence: at the MOMENT of the test, that document did not exist yet &mdash; so it does not cover the test. Issuing it afterwards solves nothing.", True),
      ("It only sounds more formal; the meaning is the same as \"was not issued\".", False),
      ("It means the certificate will never be issued.", False)]),
    ("3. \"We need to have the report resubmitted by Friday.\" WHO resubmits the report?",
     [("I do, because <em>have</em> means \"to have to do something\".", False),
      ("Nobody &mdash; the sentence only describes an intention.", False),
      ("THE SUPPLIER. The causative <em>have something done</em> says the action is DEMANDED by me and CARRIED OUT by somebody else. I do not do the work; I require it.", True)]),
    ("4. Which sentence is correct?",
     [("\"We need to have resubmitted the report by Friday.\"", False),
      ("\"We need to have the report resubmitted by Friday.\"", True),
      ("\"We need to have the report resubmit by Friday.\"", False)]),
]

BLANKS = [
    ("was found to be", "Hint: the passive of a finding &mdash; <em>be</em> + participle + <em>to be</em>. The relay is the subject; the inspector has disappeared",
     "The relay was found to be out of tolerance during the functional test.",
     '"The relay ', ' out of tolerance during the functional test."'),
    ("had not been issued", "Hint: the PERFECT passive &mdash; <em>had been</em> + participle. On the date of the test, the document did not exist yet",
     "The calibration certificate had not been issued at the time of the test.",
     '"The calibration certificate ', ' at the time of the test."'),
    ("must be implemented", "Hint: the modal passive &mdash; modal + <strong>be</strong> + PARTICIPLE (never the base form)",
     "A corrective action must be implemented before the retest.",
     '"A corrective action ', ' before the retest."'),
    ("have the report resubmitted", "Hint: the causative &mdash; <em>have</em> + OBJECT + participle. The object comes BEFORE the participle",
     "We need to have the report resubmitted by Friday.",
     '"We need to ', ' by Friday."'),
    ("cannot be granted", "Hint: the negative modal passive &mdash; sign-off can be granted by nobody while the hold point is open",
     "Sign-off cannot be granted while the hold point remains open.",
     '"Sign-off ', ' while the hold point remains open."'),
    ("root cause", "Hint: not the symptom (the eleven milliseconds) &mdash; the reason BEHIND the symptom",
     "The root cause has not been identified yet, so the corrective action is premature.",
     '"The ', ' has not been identified yet, so the corrective action is premature."'),
]

ORDER = [
    (1, "State the finding in the passive: the relay was found to be out of tolerance during the functional test."),
    (2, "Date what is missing: the calibration certificate had not been issued at the time of the test."),
    (3, "Refuse the word: a deviation is approved before the work, so a failure found after it is a non-conformance."),
    (4, "Put the responsibility back where the contract is, when the supplier blames the subcontractor."),
    (5, "Demand the work with the causative, and give the date: have the report resubmitted by Friday."),
    (6, "Hold the gate: sign-off cannot be granted while the hold point remains open."),
]

SPEECH = [
    ("The relay was found to be out of tolerance during the functional test.",
     "O relé foi constatado fora de tolerância durante o teste funcional."),
    ("The calibration certificate had not been issued at the time of the test.",
     "O certificado de calibração não havia sido emitido na data do teste."),
    ("A corrective action must be implemented before the retest.",
     "Uma ação corretiva precisa ser implementada antes do reteste."),
    ("We need to have the report resubmitted by Friday.",
     "Precisamos que o relatório seja reenviado até sexta-feira."),
    ("Sign-off cannot be granted while the hold point remains open.",
     "O aceite não pode ser concedido enquanto o hold point permanecer aberto."),
]

QUIZZES_SIT = [
    ("The supplier's quality manager opens with \"It is a minor deviation, the unit works.\" You answer:",
     [("\"A deviation is approved before the work. This was found after it, on a safety relay, so I am afraid that is a non-conformance.\"", True),
      ("\"You are wrong and you know it. That relay failed.\"", False),
      ("\"All right, if the unit works, I suppose we can look at it as a deviation.\"", False)]),
    ("She says the certificate was issued the Monday AFTER the test. The strongest reply is:",
     [("\"That is good news, we can close the point then.\"", False),
      ("\"The calibration certificate had not been issued at the time of the test, so it does not cover the test. The unit will have to be retested with a valid certificate in place.\"", True),
      ("\"Please send it to me and I will see what I can do.\"", False)]),
    ("\"The calibration was performed by our subcontractor, not by us.\" You answer:",
     [("\"Then I will take it up with your subcontractor directly.\"", False),
      ("\"That is not my problem, and it is not an excuse.\"", False),
      ("\"To some extent, I understand your position. However, our contract is with you, so the root cause still has to be identified on your side.\"", True)]),
    ("She asks what you need before the unit can be released. You want the work done by THEM, with a date:",
     [("\"We need to have the report resubmitted through the approval workflow by Friday, with the root cause and a corrective action plan.\"", True),
      ("\"We need to have resubmitted the report by Friday.\"", False),
      ("\"I will resubmit the report myself once you send me the data.\"", False)]),
    ("She asks for a provisional sign-off so the shipment is not delayed. You say no without closing the door:",
     [("\"I cannot sign anything, please stop asking me.\"", False),
      ("\"I am afraid sign-off cannot be granted while the hold point remains open. As soon as the retest passes and the certificate is on file, the inspection release can be issued the same day.\"", True),
      ("\"All right, provisionally, but do not tell anyone.\"", False)]),
]


def quiz_html(items):
    out = []
    for q, opts in items:
        o = []
        for j, (text, correct) in enumerate(opts):
            letter = 'ABC'[j]
            o.append(
                f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}">'
                f'<span class="option-letter">{letter}</span> {text}</div>')
        out.append(
            f'      <div class="quiz-item"><div class="quiz-question">{q}</div>'
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
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
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Simple passive<br><em>be</em> + participle</td><td style="padding:.6rem">The object becomes the subject and the agent DROPS OUT &mdash; because it is obvious, because it is unknown, or because naming it would start a fight.</td><td style="padding:.6rem">"The submittal <strong>was returned</strong> with comments."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Passive of a finding<br><em>be</em> + <em>found / reported / believed</em> + <strong>to be</strong></td><td style="padding:.6rem">The register of every inspection report. You state the FACT, not the person. Note: <em>is believed to have been caused</em> is NOT the same as <em>has been identified</em> &mdash; the supplier reaches for the first one precisely in order not to commit to the second.</td><td style="padding:.6rem">"The relay <strong>was found to be</strong> out of tolerance."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Perfect passive<br><em>had been</em> + participle</td><td style="padding:.6rem">It dates the ABSENCE: at the time of the test, that document did not exist yet. This is the sentence that stops the supplier from making the problem go away by issuing the certificate afterwards.</td><td style="padding:.6rem">"The certificate <strong>had not been issued</strong> at the time of the test."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Modal passive<br>modal + <strong>be</strong> + participle</td><td style="padding:.6rem">The obligation belongs to the PROCEDURE, not to you &mdash; and that is why nobody takes it personally. After the modal comes <strong>be</strong>, always.</td><td style="padding:.6rem">"A corrective action <strong>must be implemented</strong>." &middot; "Sign-off <strong>cannot be granted</strong>."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Causative<br><em>have</em> + OBJECT + participle</td><td style="padding:.6rem">You DEMAND the action; somebody else CARRIES IT OUT. The order is fixed: the thing comes before the participle. <em>get something done</em> is the same, only less formal.</td><td style="padding:.6rem">"We need to <strong>have the report resubmitted</strong>." &middot; "I will <strong>get the relay retested</strong>."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Causative with a person<br><em>have somebody</em> + BASE FORM</td><td style="padding:.6rem">For when you DO need to name who does the work. Then the verb goes back to the base form &mdash; no <em>to</em>, no participle.</td><td style="padding:.6rem">"I will <strong>have your team resubmit</strong> the report."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">"You calibrated it badly" is an accusation &mdash; and everything that follows it will be a defense. "<strong>The relay was found to be out of tolerance</strong>" is the SAME fact with the person removed: nobody is attacked and nothing can be denied. Then the causative hands the work back to whoever owns it: "<strong>we need to have it retested</strong>" &mdash; not by us, by THEM, and by Friday.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the two classic traps):</strong> (1) dropping the <em>be</em> or the participle after the modal &mdash; "The report must be <em>resubmit</em>" and "A corrective action must <em>implemented</em>" are both wrong; the right forms are "must <strong>be resubmitted</strong>" and "must <strong>be implemented</strong>"; (2) the word order of the causative &mdash; the temptation is to say "We need to have <em>resubmitted the report</em>", which in English is a different tense and a different meaning altogether. In the causative the OBJECT comes FIRST: "have <strong>the report</strong> resubmitted".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Collocations of the approval meeting:</strong> <strong>carry out</strong> a test, <strong>issue</strong> a certificate (NEVER "emit" &mdash; the classic false friend), <strong>trigger</strong> a hold point, <strong>identify</strong> the root cause, <strong>raise</strong> a concern, <strong>grant</strong> sign-off, <strong>resubmit</strong> a report through the approval workflow.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-6">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 06 -- Pre-class</div>
      <h3>Holding Your Ground -- The Supplier Approval Meeting</h3>
      <div class="lesson-desc">The safety relay failed the factory acceptance test and the supplier calls it a "minor deviation": how to state the failure without accusing anybody, how to demand the corrective action without doing the work yourself, and how to keep the hold point closed. Key words: deviation, submittal, approval workflow, inspection release, out of tolerance, calibration certificate, traceability, root cause, rework, sign-off, to downplay, to raise a concern, to hold your ground, to pass the buck. Structure: the advanced passive (was found to be... / had not been issued / must be implemented) + the causative have something done ("We need to have the report resubmitted by Friday").</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">In Lesson 5 you put a name to yourself in front of an interview panel. Here you put a name to the DEFECT &mdash; and to whoever pays for it. These are the words of the approval meeting: what was found, what had not been issued yet, and what the supplier will try to call "minor". Listen to every term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match every term with the right definition.</p>
      <div class="match-grid" id="match-l6">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text, then answer the questions below.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Advanced Passive &amp; Causative</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to state a failure without accusing a person &mdash; and how to demand the fix without doing the work yourself.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete every sentence with the right structure. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Approval Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the stages of a hold-point meeting in the right order &mdash; from the finding to the refusal of sign-off.</p>
      <div class="order-container" id="order-l6">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l6')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to every sentence, then record yourself saying it. These are the five sentences that open, hold and close an approval meeting. Watch the stress: it falls on the participle (was FOUND to be out of TOLerance) &mdash; and "certificate" ends in <em>-kit</em>, unstressed, never <em>-keit</em>.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for every real moment of a factory acceptance test meeting &mdash; including the moment when the supplier downplays the failure or shifts the blame onto the subcontractor.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two minutes, with no script and with no stopping to correct yourself. Tone: technical, impersonal in the finding, firm in the demand.</p>
      <div class="think-card">
        <div class="think-question">You are opening a hold-point meeting with the supplier's quality manager. In ninety seconds: state what was found during the functional test (The relay was found to be...), state what had not been done at the time of the test (The calibration certificate had not been...), refuse the word "deviation" and give the criterion, demand the root cause and the corrective action with a date (We need to have the report resubmitted...), and close by saying why sign-off cannot be granted yet.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-6"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 6</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
