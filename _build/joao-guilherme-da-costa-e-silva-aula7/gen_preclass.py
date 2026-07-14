#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 7 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 7 IN CLASS (mesmo tema/gramática/vocab — discurso indireto
+ verbos de relato na revisão trimestral de prazo).
"""
import os
import random

random.seed(7)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Schedule slippage", "time lost against the plan, a few days at a time, until the date is gone", "derrapagem de prazo",
     "\"The schedule slippage on the installation package is now six weeks.\""),
    ("Variance", "the measured difference between the plan and reality -- the number in the report", "varia&#231;&#227;o (medida, plano x real)",
     "\"The schedule variance is minus thirty working days against the plan.\""),
    ("Critical path", "the chain of activities that decides the end date: delay any of them and the project moves", "caminho cr&#237;tico",
     "\"Signal installation is on the critical path, so this delay is not absorbable.\""),
    ("Float", "the spare time an activity has before it starts delaying the whole project", "folga (de cronograma)",
     "\"That activity had ten days of float. The supplier has used all of it.\""),
    ("Recovery schedule", "the revised plan that shows exactly how the lost time will be won back", "cronograma de recupera&#231;&#227;o",
     "\"A recovery schedule is required within ten days, not another apology.\""),
    ("Contingency plan", "what you do if the recovery fails -- the plan you hope not to use", "plano de conting&#234;ncia",
     "\"Our contingency plan is to commission the line in two stages instead of one.\""),
    ("Risk mitigation", "action taken now to make a risk smaller, before it becomes a delay", "mitiga&#231;&#227;o de risco",
     "\"Dual sourcing the cable was risk mitigation, and it is why we are only six weeks late.\""),
    ("Post-mortem review", "a session held after the fact, to find out why it happened and never repeat it", "revis&#227;o pos-projeto (li&#231;&#245;es aprendidas)",
     "\"We will hold a post-mortem review once the line is commissioned, not now.\""),
    ("Steering committee", "the senior group that decides what the project team is not allowed to decide alone", "comit&#234; diretor / comit&#234; gestor",
     "\"If we cannot agree a date today, this goes to the steering committee in April.\""),
    ("Buy-in", "real agreement from the people who could block you -- not just their signature", "ades&#227;o, apoio real",
     "\"I have the approval. What I do not have yet is buy-in from the operations team.\""),
    ("To make headway", "to make real progress against something that is pushing back", "avan&#231;ar, progredir (contra resist&#234;ncia)",
     "\"We are finally making headway on the interface drawings.\""),
    ("To reach a consensus", "to arrive at a position that everybody in the room can live with", "chegar a um consenso",
     "\"We reached a consensus on the sequence, not on the date.\""),
    ("To take a stance", "to state a position publicly, and then stand behind it when it is challenged", "assumir uma posi&#231;&#227;o publicamente",
     "\"Motiva has taken a stance on the delay: no payment against an unapproved schedule.\""),
    ("To bring about", "to cause something to happen, usually after effort and resistance", "provocar, ocasionar (um resultado)",
     "\"It took two escalations to bring about a resolution.\""),
]

SURVIVAL = [
    ("The schedule variance is minus thirty working days, and the activity is on the critical path.",
     "A variação de prazo é de menos trinta dias úteis, e a atividade está no caminho crítico."),
    ("On 3 June you assured us that the relay would ship on the fifteenth.",
     "Em 3 de junho vocês nos garantiram que o relé seria despachado no dia quinze."),
    ("Your company undertook to submit a recovery schedule within ten days.",
     "A empresa de vocês se comprometeu a apresentar um cronograma de recuperação em dez dias."),
    ("To some extent, both parties share responsibility. The float, however, belongs to the project.",
     "Até certo ponto, as duas partes dividem a responsabilidade. A folga, porém, é do projeto."),
    ("If we can reach a consensus today, this does not have to go to the steering committee.",
     "Se chegarmos a um consenso hoje, isto não precisa subir para o comitê diretor."),
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


CONTEXT = """<p>The quarterly review opens at ten, and Elena Vargas opens it with the good news: her team is working weekends and they are finally <strong>making headway</strong> on site. Jo&#227;o Guilherme lets her finish, and then he puts the number on the table. The <strong>schedule variance</strong> on the signaling installation is minus thirty working days. The activity sits on the <strong>critical path</strong>, so the <strong>float</strong> is zero and nothing absorbs it. Six weeks of <strong>schedule slippage</strong>, and the passenger waits six weeks longer.</p>
        <p>Elena has been preparing her version for a month. The interface drawings arrived late from Motiva, she says, and her team could not start. She is partly right, and Jo&#227;o says so: to some extent, both parties share responsibility, and the drawings were issued eight days late. Then she goes further. <em>I never promised you the fifteenth</em>, she says. <em>I said we would do our best.</em> And this is the moment the meeting is won or lost &mdash; not by raising the voice, but by reading the record. <strong>On 3 June you assured us that</strong> the relay <strong>would ship</strong> on the fifteenth, and the minutes were circulated to you that same afternoon. In the last review your team <strong>told us that</strong> the installation <strong>was</strong> on track. Your planner <strong>claimed that</strong> the cable <strong>had already been dispatched</strong>; the carrier's records show it left the warehouse eleven days later. And on 12 June your company <strong>undertook to submit</strong> a <strong>recovery schedule</strong> within ten days. Twenty-two days have passed, and nothing has been received.</p>
        <p>Elena stops. <em>That is fair</em>, she <strong>acknowledges</strong>. <em>The schedule was not sent, and I should have called you.</em> Nobody was accused, nothing was denied, and the argument about memory is over &mdash; because a dated record cannot be argued with, only explained. So she asks what he needs. He asks for three things: a <strong>recovery schedule</strong> by Friday, a <strong>contingency plan</strong> if the retest fails, and a weekly call, so that the next slip reaches him in three days and not in three weeks. She asks for one thing back: two weeks of <strong>float</strong> from the testing activity. He refuses. The float belongs to the project. And if they can <strong>reach a consensus</strong> today, none of this has to go to the <strong>steering committee</strong> in April."""

QUIZZES_CONTEXT = [
    ("1. \"On 3 June you <em>assured us that</em> the relay <em>would</em> ship.\" Why does the verb step back from <em>will</em> to <em>would</em>?",
     [("Because <em>would</em> is more polite than <em>will</em>.", False),
      ("Because the backshift marks the sentence as a QUOTE of what SHE said, not a promise JOAO is making now. Without it (\"you assured us the relay <em>will</em> ship\"), the sentence stops being her record and turns into his own commitment.", True),
      ("Because <em>will</em> is not allowed in technical English.", False)]),
    ("2. Elena says \"I never promised you the fifteenth\". What ENDS the argument?",
     [("Raising your voice and repeating that she promised.", False),
      ("The RECORD: the date (3 June), the reporting verb (<em>assured us</em>) and the minutes circulated that same afternoon. A dated record cannot be argued with &mdash; it can only be explained.", True),
      ("Escalating to the steering committee straight away.", False)]),
    ("3. \"Your planner <em>claimed that</em> the cable <em>had already been dispatched</em>.\" What does CLAIMED communicate that SAID would not?",
     [("That Joao DOUBTS the statement &mdash; <em>claim</em> marks what was said as something that did not hold up. <em>Said</em> would be neutral; <em>claimed</em> already opens the check.", True),
      ("That the planner shouted.", False),
      ("That the statement was official and has been proven.", False)]),
    ("4. Which sentence is correct?",
     [("\"Your company assured us to submit a recovery schedule within ten days.\"", False),
      ("\"Your company undertook to submit a recovery schedule within ten days.\"", True),
      ("\"Your company said us that it would submit a recovery schedule within ten days.\"", False)]),
]

BLANKS = [
    ("assured us that", "Hint: the reporting verb of a COMMITMENT &mdash; and it is followed by <em>that</em> + clause, with the verb stepped back",
     "On 3 June you assured us that the relay would ship on the fifteenth.",
     '"On 3 June you ', ' the relay would ship on the fifteenth."'),
    ("told us that", "Hint: TELL needs the person (told US). SAY never takes the person directly &mdash; &#39;said us&#39; does not exist",
     "In the last review your team told us that the installation was on track.",
     '"In the last review your team ', ' the installation was on track."'),
    ("had already been dispatched", "Hint: step the <em>present perfect</em> (<em>has been</em>) back to the <em>past perfect</em>: <em>had been</em> + past participle",
     "Your planner claimed that the cable had already been dispatched.",
     '"Your planner claimed that the cable ', '."'),
    ("undertook to submit", "Hint: a formal obligation &mdash; and this is the reporting verb that takes an INFINITIVE (<em>to</em> + verb), not <em>that</em>",
     "Your company undertook to submit a recovery schedule within ten days.",
     '"Your company ', ' a recovery schedule within ten days."'),
    ("critical path", "Hint: the chain of activities that decides the end date &mdash; on it the float is zero",
     "The activity is on the critical path, so there is no float to absorb the delay.",
     '"The activity is on the ', ', so there is no float to absorb the delay."'),
    ("reach a consensus", "Hint: to arrive at a position that everybody in the room accepts &mdash; the verb is <em>reach</em>, never <em>arrive at</em>",
     "If we can reach a consensus today, this does not have to go to the steering committee.",
     '"If we can ', ' today, this does not have to go to the steering committee."'),
]

ORDER = [
    (1, "Open with the number: the schedule variance is minus thirty working days."),
    (2, "Say why nothing absorbs it: the activity is on the critical path and the float is zero."),
    (3, "Concede what is true: to some extent, both parties share responsibility for the late drawings."),
    (4, "Put the promise on the record with the date: on 3 June you assured us that the relay would ship."),
    (5, "Name the obligation that was never met: your company undertook to submit a recovery schedule."),
    (6, "Close with the demand and the consequence: a recovery schedule by Friday, or the steering committee in April."),
]

SPEECH = [
    ("The schedule variance is minus thirty working days, and the activity is on the critical path.",
     "A variação de prazo é de menos trinta dias úteis, e a atividade está no caminho crítico."),
    ("On 3 June you assured us that the relay would ship on the fifteenth.",
     "Em 3 de junho vocês nos garantiram que o relé seria despachado no dia quinze."),
    ("Your planner claimed that the cable had already been dispatched.",
     "O planejador de vocês alegou que o cabo já havia sido despachado."),
    ("Your company undertook to submit a recovery schedule within ten days.",
     "A empresa de vocês se comprometeu a apresentar um cronograma de recuperação em dez dias."),
    ("To some extent, both parties share responsibility. The float, however, belongs to the project.",
     "Até certo ponto, as duas partes dividem a responsabilidade. A folga, porém, é do projeto."),
]

QUIZZES_SIT = [
    ("Elena opens the meeting with the good news (\"the team is working weekends\"). You reply:",
     [("\"Thank you, Elena. Let me start with the number, and then I would like to hear you. The schedule variance on the installation is minus thirty working days, and the activity is on the critical path.\"", True),
      ("\"Weekends are the minimum I expect at this point.\"", False),
      ("\"That is good to hear. So, how are things going in general?\"", False)]),
    ("\"I never promised you the fifteenth. I said we would do our best.\" The strongest reply is:",
     [("\"You did promise it, and everybody in that call heard you.\"", False),
      ("\"That is why I am reading from the minutes. On 3 June you assured us that the relay would ship on the fifteenth, and the minutes were circulated to you the same afternoon.\"", True),
      ("\"All right, perhaps I misunderstood you. Let us move on.\"", False)]),
    ("\"The interface drawings arrived late from your side.\" She is PARTLY right. You reply:",
     [("\"That has nothing to do with the delay we are discussing.\"", False),
      ("\"You are right, and I accept that the delay is shared.\"", False),
      ("\"To some extent, both parties share responsibility, and the drawings were issued eight days late. The slippage we are discussing, however, is thirty days.\"", True)]),
    ("\"Give us two weeks of float from the testing activity and we recover everything.\" You refuse:",
     [("\"I am afraid the float belongs to the project, not to the package that is late. If I hand it over now, I have nothing left when something unplanned happens.\"", True),
      ("\"Fine, take the two weeks, but this is the last time.\"", False),
      ("\"I do not have the authority to discuss float with you.\"", False)]),
    ("She asks you not to escalate the meeting. You say yes ON YOUR OWN TERMS:",
     [("\"I cannot promise anything, it is out of my hands.\"", False),
      ("\"If we can reach a consensus today &mdash; a recovery schedule by Friday and a contingency plan &mdash; this does not have to go to the steering committee in April.\"", True),
      ("\"Do not worry, I will keep this between us whatever happens.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l7\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l7\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l7\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">They said</th><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">You report</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>will</em> &rarr; <strong>would</strong></td><td style="padding:.6rem">The promise steps back one tense &mdash; and becomes a RECORD of what they promised, not a promise of your own.</td><td style="padding:.6rem">"You assured us that the relay <strong>would</strong> ship on the fifteenth."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>is / are</em> &rarr; <strong>was / were</strong></td><td style="padding:.6rem">Their present becomes your past: it was true for them, at that moment.</td><td style="padding:.6rem">"Your team told us that the installation <strong>was</strong> on track."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>has been</em> &rarr; <strong>had been</strong></td><td style="padding:.6rem">The perfect becomes the past perfect. This is the line that DATES a claim &mdash; and a dated claim is one you can check.</td><td style="padding:.6rem">"Your planner claimed that the cable <strong>had been</strong> dispatched."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>can</em> &rarr; <strong>could</strong> &middot; <em>must</em> &rarr; <strong>had to</strong></td><td style="padding:.6rem">Modals step back too. <em>Must</em> is the exception: it becomes <em>had to</em>.</td><td style="padding:.6rem">"They said they <strong>could</strong> recover two weeks, and that we <strong>had to</strong> wait."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>say</em> x <strong>tell</strong></td><td style="padding:.6rem"><strong>TELL</strong> needs the person (<em>told us / told me</em>). <strong>SAY</strong> does NOT take the person directly: it is <em>said that</em> or <em>said TO me</em>. "He said me" does not exist.</td><td style="padding:.6rem">"He <strong>told us</strong> that..." &middot; "He <strong>said</strong> that..."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">The verb picks the WEIGHT</td><td style="padding:.6rem"><strong>said</strong> (neutral) &middot; <strong>claimed</strong> (you doubt it) &middot; <strong>assured us</strong> (they committed, with confidence) &middot; <strong>acknowledged / conceded</strong> (they admitted it against their own interest) &middot; <strong>denied</strong> (they denied it) &middot; <strong>undertook / committed to</strong> (a formal obligation).</td><td style="padding:.6rem">"They <strong>assured</strong> us" holds them. "They <strong>said</strong>" does not.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">What it is for</td><td style="padding:.6rem" colspan="2">"You are always late" is an accusation &mdash; and an accusation gets denied, defended and argued over for three weeks. "<strong>On 3 June you assured us that the relay would ship on the fifteenth</strong>" is the SAME fact turned into a RECORD: it has a date, a reporting verb, a backshift. A record cannot be argued with &mdash; it can only be explained. And whoever explains is already negotiating.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (three mistakes Brazilian speakers make):</strong> (1) <em>"He said me that..."</em> &mdash; SAY never takes the person: it is <strong>told me</strong> (or <em>said to me</em>); (2) NOT stepping the verb back &mdash; "he said the relay <em>will</em> ship" stops quoting the other side and turns into a promise of YOUR OWN; (3) <em>"They assured us TO send the schedule"</em> &mdash; <strong>assure</strong> takes <em>that</em> + clause; the verbs that take the infinitive are <strong>undertake / commit / promise</strong>: "they <strong>undertook to send</strong> the schedule".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Collocations of the schedule review:</strong> <strong>compress</strong> the schedule (never "reduce"), <strong>secure</strong> buy-in, <strong>reach</strong> a consensus (never "arrive at"), <strong>mitigate</strong> a risk, <strong>make</strong> headway (NEVER "have progress"), <strong>absorb</strong> a delay, <strong>take</strong> a stance, <strong>bring about</strong> a resolution.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Hedging (to concede without giving ground):</strong> "<em>To some extent, both parties share responsibility for...</em>" &middot; "<em>One could argue that the delay was partly caused by...</em>" &middot; "<em>That is fair, and I will record it. It does not change what is on the critical path.</em>"</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 07 -- Pre-class</div>
      <h3>Never Back Down -- The Quarterly Project Review</h3>
      <div class="lesson-desc">Six weeks of slippage on the installation, and a supplier who remembers the promise differently: how to open the meeting with the NUMBER, how to turn memory into a RECORD (date + reporting verb + backshift), and how to concede what is true without handing over the float of the project. Key words: schedule slippage, variance, critical path, float, recovery schedule, contingency plan, risk mitigation, post-mortem review, steering committee, buy-in, to make headway, to reach a consensus, to take a stance, to bring about. Structure: reported speech and reporting verbs (On 3 June you <em>assured us that</em> the relay <em>would</em> ship... / your company <em>undertook to submit</em>...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">In Lesson 6 you named the defect. Here you name the DELAY &mdash; and who pays for it. These are the words that separate a vague complaint from a schedule you can defend in a room: the variance, the critical path, the float that is not there. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l7">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reported Speech &amp; Reporting Verbs</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to turn what the other side said into a record &mdash; and why the reporting verb you pick decides how tightly it holds them.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Review Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a quarterly schedule review in the correct order &mdash; from the number to the consequence.</p>
      <div class="order-container" id="order-l7">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that open, hold and close a schedule review. Watch the stress: "VA-ri-ance" (on the first syllable, not "va-ri-AN-ce") and "com-MIT-tee" with a short -ee. And say SKED-jool, not SHED-jool.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Pick the strongest answer for each real moment of the quarterly review &mdash; including the moment the supplier denies the promise, and the moment she asks for the float of your project.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for 2 minutes, with no script and no stopping to correct yourself. Tone: precise on the number, even-handed in the concession, firm on the record.</p>
      <div class="think-card">
        <div class="think-question">You are chairing the quarterly review with a supplier who is six weeks behind. In ninety seconds: open with the variance and say why the float does not absorb it, concede the part that is genuinely yours (the drawings were eight days late), put two commitments on the record with their dates (On 3 June you assured us that... / On 12 June your company undertook to...), refuse to hand over the float from the testing activity, and close by saying what you need by Friday and what happens if it does not arrive.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-7"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 7</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
