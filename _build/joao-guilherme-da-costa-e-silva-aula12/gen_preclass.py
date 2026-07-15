#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 12 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
B2 -> ZERO português na tela do aluno (REGRA 13): definição em inglês, grammar tip
em inglês, survival/speech sem tradução. Matching EMBARALHADO por linha (REGRA 24).
REGRA 29: previewa a aula 12 IN CLASS (mesmo tema/gramática/vocab — conflito com
fornecedor internacional, pushing back sem burning bridges, e as orações de
concessão/contraste: although / even though / while / whereas / despite / however).
REGRA 22: gramática RE-ESCOPADA para concessão/contraste (future perfect/continuous
já foi a aula 9; passivo já foi a aula 6). Vocab NOVO, sem colisão com aulas 1-11.
"""
import os
import random

random.seed(12)

HERE = os.path.dirname(os.path.abspath(__file__))

# (word, speak, definition_en, example)
VOCAB = [
    ("Assertive", "Assertive",
     "confident and direct without being aggressive or passive -- you say the hard thing clearly and respectfully",
     "\"Assertive is not aggressive: I stated our position plainly, but I never attacked the person.\""),
    ("To defuse", "To defuse",
     "to reduce the tension in a situation before it escalates into a fight",
     "\"When he got defensive, I defused it: 'I'm not blaming you, I'm reading the schedule.'\""),
    ("A sticking point", "A sticking point",
     "the single issue that is blocking an agreement while everything else is settled",
     "\"We agreed on the schedule; the only sticking point was who pays for the recovery shifts.\""),
    ("An impasse", "An impasse",
     "a deadlock where neither side will move and the discussion cannot go forward",
     "\"To break the impasse, I proposed we table the cost question and agree the delivery sequence first.\""),
    ("Common ground", "Common ground",
     "the points both sides already agree on, used as a starting place to rebuild the talk",
     "\"Before arguing about the cause, we found common ground: we both wanted Line 4 delivered.\""),
    ("To meet halfway", "To meet halfway",
     "to compromise so that each side gives up something to reach a deal",
     "\"I couldn't accept full blame, but I offered to meet them halfway on the schedule.\""),
    ("To hold someone accountable", "To hold someone accountable",
     "to make someone answer for what they were responsible for",
     "\"The plan holds both sides accountable: their slip, and our nine-day drawing delay.\""),
    ("Remediation plan", "Remediation plan",
     "an agreed plan of actions to fix a failure and recover the schedule",
     "\"We left the call with a remediation plan, not a winner and a loser.\""),
    ("To draw the line", "To draw the line",
     "to set a firm limit that you will not cross, however much pressure you are under",
     "\"I conceded the drawing delay, but I drew the line at signing sole responsibility.\""),
    ("To table a proposal", "To table a proposal",
     "in American English, to postpone discussion of a proposal until a later point",
     "\"Let's table the penalty clause for now and agree the recovery sequence first.\""),
    ("Goodwill", "Goodwill",
     "the trust and positive relationship two parties have built and want to protect",
     "\"A formal dispute would win the point and burn two years of goodwill.\""),
    ("To smooth things over", "To smooth things over",
     "to repair a relationship after friction or a disagreement",
     "\"The start was tense, but we smoothed things over and both signed the plan.\""),
]

SURVIVAL = [
    "Although we were late on one revision, that does not explain the whole delay.",
    "I'm not saying you dropped the ball; I'm saying the schedule shows a gap.",
    "Let's find the common ground first, then draw the line where the evidence draws it.",
    "I can commit to a remediation plan. However, I can't accept sole responsibility.",
    "Despite the tension, I'd rather meet you halfway than lose a month to a dispute.",
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
    for word, speak, d, ex in VOCAB:
        rows.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{esc(word)}</span>'
            f'<span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{esc(d)}</span></div>'
            f'<div class="vocab-card-example">{esc(ex)}</div></div>'
            f'<button class="audio-btn" data-speak="{esc(speak)}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
    return '\n'.join(rows)


def match_grid():
    defs = [d for _, _, d, _ in VOCAB]
    rows = []
    for word, _, d, _ in VOCAB:
        opts = defs[:]
        while True:
            random.shuffle(opts)
            if opts != defs:
                break
        o = ''.join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in opts)
        rows.append(
            f'        <div class="match-row" data-answer="{esc(d)}">'
            f'<span class="match-word" style="flex:0 0 210px">{esc(word)}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    return '\n'.join(rows)


CONTEXT = """<p>A German supplier, GleisTech, has missed three delivery milestones on Line 4, and this morning a letter arrived claiming the whole delay was Motiva's fault: the technical drawings were approved nine days late. Jo&#227;o Guilherme is the engineer who has to answer it &mdash; this afternoon, on a call. His manager's brief is exact: do not go in swinging, and do not roll over. The goal is not to win an argument; it is to leave with a <strong>remediation plan</strong> and a supplier who still wants the next contract. In other words, protect the <strong>goodwill</strong>.</p>
        <p>The grammar of that call is the grammar of concession. Watch how a firm point is built on top of a fact you accept. <em>"<strong>Although</strong> we were nine days late on the January revision, that does not explain a three-month slip."</em> The <em>although</em>-clause gives ground; the main clause holds it. <em>"<strong>While</strong> I accept the drawing was late, the delay after approval is yours to resolve."</em> <em>"Our records show March, <strong>whereas</strong> the baseline called for January."</em> And when the connector takes no clause: <em>"<strong>Despite</strong> the late approval, we kept the line moving"</em> &mdash; <em>despite</em> + a noun, never <em>despite we were late</em>. Each sentence concedes something true, then draws a line exactly where the evidence draws it.</p>
        <p>So Jo&#227;o runs the call the assertive way, which is neither aggressive nor passive. He <strong>defuses</strong> the defensiveness &mdash; <em>"I'm not saying you dropped the ball; I'm saying the schedule shows a gap"</em> &mdash; and looks for <strong>common ground</strong> before arguing about cause. When they reach a <strong>sticking point</strong> over who pays for the recovery shifts, he does not let it become an <strong>impasse</strong>: he offers to <strong>meet</strong> them <strong>halfway</strong> on the schedule while he <strong>draws the line</strong> on sole responsibility. He <strong>tables</strong> the hardest clause so nobody has to lose face, keeps both sides <strong>accountable</strong> to a revised sequence, and <strong>smooths things over</strong> before the call ends &mdash; the point made, the bridge intact. <em>"<strong>Despite</strong> the tension, I'd rather meet you halfway than lose a month to a dispute."</em></p>"""

QUIZZES_CONTEXT = [
    ("1. \"<em>Although</em> we were nine days late on the January revision, that does not explain a three-month slip.\" What is the main point of the sentence?",
     [("That Motiva caused the whole delay.", False),
      ("That the nine-day delay is real but does NOT explain the rest &mdash; the although-clause concedes a fact, and the MAIN clause carries the weight.", True),
      ("That the January revision was never late.", False)]),
    ("2. Which sentence is grammatically correct?",
     [("\"Despite we were late on the drawings, we kept the line moving.\"", False),
      ("\"Despite the late approval, we kept the line moving.\"", True),
      ("\"Despite of the late approval, we kept the line moving.\"", False)]),
    ("3. \"Our records show delivery in March, <em>whereas</em> the baseline called for January.\" What does <em>whereas</em> do here?",
     [("It draws a clean contrast between two facts placed side by side.", True),
      ("It apologizes for the March delivery.", False),
      ("It means 'because', giving the reason for the delay.", False)]),
    ("4. The manager says the goal of the call is to leave with a remediation plan and a supplier who still wants to work with Motiva. What is he protecting?",
     [("The penalty clause.", False),
      ("The goodwill &mdash; the working relationship, so pushing back must never become burning the bridge.", True),
      ("His own promotion.", False)]),
]

BLANKS = [
    ("Although", "Hint: concede a fact in a full clause, then make your real point (needs a subject + verb after it)",
     "Although we were late on one revision, the rest of the delay began on their side.",
     '"', ' we were late on one revision, the rest of the delay began on their side."'),
    ("Despite", "Hint: concede with a NOUN, not a clause -- goes before 'the tension', never before 'we were'",
     "Despite the tension, I'd rather meet them halfway than lose a month.",
     '"', ' the tension, I\'d rather meet them halfway than lose a month."'),
    ("whereas", "Hint: draw a clean contrast between two facts side by side",
     "Our records show March, whereas the baseline called for January.",
     '"Our records show March, ', ' the baseline called for January."'),
    ("However", "Hint: a full stop, then a pivot to the second sentence -- takes a comma after it",
     "I can commit to a joint plan. However, I can't accept sole responsibility.",
     '"I can commit to a joint plan. ', ', I can\'t accept sole responsibility."'),
    ("common ground", "Hint: the points both sides already agree on, used to restart the talk",
     "Before arguing about the cause, we found common ground.",
     '"Before arguing about the cause, we found ', '."'),
    ("draw the line", "Hint: set a firm limit you will not cross",
     "I conceded the drawing delay, but I had to draw the line at sole responsibility.",
     '"I conceded the drawing delay, but I had to ', ' at sole responsibility."'),
]

ORDER = [
    (1, "Open by conceding the true part: although we were nine days late, that does not explain the whole slip."),
    (2, "Defuse the defensiveness: I'm not saying you dropped the ball; I'm saying the schedule shows a gap."),
    (3, "Find common ground before arguing about cause: we both want Line 4 back on its critical path."),
    (4, "Draw the line where the evidence draws it: the post-approval slip stays with your team."),
    (5, "Break the sticking point: table the cost clause for now and agree the delivery sequence first."),
    (6, "Close by smoothing things over: despite the tension, we leave with a remediation plan we both signed."),
]

SPEECH = [
    "Although we were nine days late on one revision, that does not explain a three-month slip.",
    "I'm not saying you dropped the ball; I'm saying the schedule shows a gap.",
    "Despite the late approval, we kept the installation line moving.",
    "I can commit to a remediation plan. However, I can't accept sole responsibility.",
    "Let's find the common ground first, then draw the line where the evidence draws it.",
]

QUIZZES_SIT = [
    ("The supplier opens by blaming your late drawings for the entire delay. Your strongest first move is:",
     [("\"That's completely wrong, the delay is entirely your fault.\"", False),
      ("\"Although we were nine days late on the January revision, and I accept that openly, the baseline schedule shows the rest of the delay began on your side.\"", True),
      ("\"You're right, it's all our fault, let's move on.\"", False)]),
    ("They get defensive and stop listening. To defuse it without giving up your position, you say:",
     [("\"You clearly dropped the ball on this one.\"", False),
      ("\"I'm not saying you dropped the ball -- I'm saying the schedule shows a gap, and I'd like us to close it together.\"", True),
      ("\"Fine, forget it, I'll escalate this to your director.\"", False)]),
    ("You reach a sticking point over who pays for the recovery shifts. To avoid an impasse, you:",
     [("Refuse to discuss anything else until they admit fault.", False),
      ("Offer to meet them halfway on the schedule while you draw the line on sole responsibility, and table the cost clause for later.", True),
      ("Agree to pay everything just to end the call.", False)]),
    ("They ask you to sign a document that assigns Motiva sole responsibility. You protect Motiva and the relationship by saying:",
     [("\"I'll sign whatever ends this argument.\"", False),
      ("\"I can commit to a joint remediation plan; however, I can't sign a document that assigns us sole responsibility. Let's table that clause and agree the sequence first.\"", True),
      ("\"No, and I'm ending this call now.\"", False)]),
    ("The call was tense but productive. To close it and keep the goodwill, you say:",
     [("\"Despite a difficult start, I think we've smoothed things over -- I'll send the remediation plan today so we hold each other accountable.\"", True),
      ("\"Well, that was a waste of time.\"", False),
      ("\"We'll talk when you're ready to admit the truth.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l12\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l12\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l12\')">&#9660;</button></span></div>')
    return '\n'.join(out)


def speech_html():
    out = []
    for en in SPEECH:
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
    for i, en in enumerate(SURVIVAL, 1):
        out.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{esc(en)}</span>'
            f'<button class="btn btn-listen" data-speak="{esc(en)}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
    return '\n'.join(out)


GRAMMAR_TIP = """      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">What follows it</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Although / Even though</td><td style="padding:.6rem">+ a FULL CLAUSE (subject + verb). Concede a fact, then make your real point in the main clause. <strong>Even though</strong> is the more emphatic version.</td><td style="padding:.6rem">"<strong>Although</strong> we were late on one revision, that does not explain the slip."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">While / Whereas</td><td style="padding:.6rem">+ a FULL CLAUSE. <strong>While</strong> = "although" or "at the same time as"; <strong>whereas</strong> draws a clean contrast between two facts.</td><td style="padding:.6rem">"Our records show March, <strong>whereas</strong> the baseline called for January."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Despite / In spite of</td><td style="padding:.6rem">+ a NOUN or an <strong>-ing</strong> form &mdash; NEVER a full clause. "despite the delay", "despite being late" &mdash; not "despite we were late".</td><td style="padding:.6rem">"<strong>Despite</strong> the late approval, we kept the line moving."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">However / Nevertheless</td><td style="padding:.6rem">Join two SEPARATE sentences: full stop before, comma after. They pivot the reader from one sentence to the next.</td><td style="padding:.6rem">"We accept the drawing delay. <strong>However,</strong> the schedule tells a different story."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">Concession is how you push back <strong>without burning the bridge</strong>. You give ground on a small, true point &mdash; "<strong>although</strong> we were nine days late" &mdash; and that concession buys the credibility to hold firm on the big one. The engineer who admits nothing is believed on nothing. Conceding first is not weakness; it is the move that keeps the room open.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (habits carried over from Portuguese):</strong> (1) <em>"<span style="color:#dc2626">Despite</span> we were late..."</em> &mdash; after <strong>despite / in spite of</strong> comes a NOUN or <strong>-ing</strong>, not a clause: "despite <strong>the delay</strong>", "despite <strong>being</strong> late". For a full clause, use <strong>although</strong>; (2) <em>"<span style="color:#dc2626">Despite of</span> the delay..."</em> &mdash; it is <strong>despite</strong> (no "of") or <strong>in spite of</strong> (with "of"), never "despite of"; (3) <em>"Although late, <span style="color:#dc2626">but</span> we kept moving"</em> &mdash; English uses <strong>although</strong> OR <strong>but</strong>, never both in the same sentence.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Conflict collocations:</strong> <strong>defuse</strong> a situation, <strong>reach</strong> an impasse, <strong>find</strong> common ground, <strong>meet</strong> someone <strong>halfway</strong>, <strong>hold</strong> someone <strong>accountable</strong>, <strong>draw</strong> the line, <strong>table</strong> a proposal, <strong>preserve</strong> goodwill, <strong>smooth</strong> things <strong>over</strong>, <strong>push back on</strong> a claim (not on a person).</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The question to ask before you reply in a conflict:</strong> "<em>What can I honestly concede first?</em>" Find the true point you can give away, concede it with <em>although</em>, and only then draw your line. Concede, then contrast &mdash; every time.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-12">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 12 -- Pre-class</div>
      <h3>Navigating Conflict -- Pushing Back Without Burning Bridges</h3>
      <div class="lesson-desc">A German supplier missed three delivery milestones and now blames Motiva's late drawing approval. This is how you answer: assertive, not aggressive; conceding the true part and holding the line on the rest. Key words: assertive, to defuse, a sticking point, an impasse, common ground, to meet halfway, to hold someone accountable, remediation plan, to draw the line, to table a proposal, goodwill, to smooth things over. Structure: concession and contrast &mdash; although / even though / while / whereas + a clause, despite / in spite of + a noun or -ing, and however / nevertheless between two sentences.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="12" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="12">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Last week you ran the milestone review. Tonight the milestone is missed &mdash; by a supplier who is now blaming you. These are the words of a conflict you win without burning the bridge: how you stay firm, how you give ground, and how you keep the relationship. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l12">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Concession &amp; Contrast</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Concede a true point, then hold your line. What changes is the grammar AFTER the connector &mdash; a clause, a noun, or a new sentence.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct connector or phrase. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Build the Conflict Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the moves of an assertive conflict call in order &mdash; from conceding the true part to closing with the bridge intact.</p>
      <div class="order-container" id="order-l12">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l12')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Keep "al-THOUGH" and "de-SPITE" stressed on the second syllable, and let "however" pivot with a small pause: "...delay. However, the schedule..."</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Pick the best answer for every real moment of the conflict call &mdash; the blame, the defensiveness, the sticking point, the document, and the close.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for 2 minutes, with no script and with no stopping to correct yourself. Tone: assertive, never aggressive &mdash; concede first, then hold the line.</p>
      <div class="think-card">
        <div class="think-question">You open the conflict call with GleisTech. In two minutes: concede the drawing delay openly using "although", defuse any defensiveness, find the common ground, and then draw the line on the post-approval slip using "whereas" or "however" &mdash; without ever attacking the person. Close by proposing a remediation plan that keeps both sides accountable and the goodwill intact.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-12"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 12</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
