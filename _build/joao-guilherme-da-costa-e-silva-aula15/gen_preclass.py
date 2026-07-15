#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 15 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 15 IN CLASS (mesmo tema/gramática/vocab -- speaking under
pressure: os modais would rather / had better / may as well e o léxico de manter o
controle numa entrevista/reunião hostil). B2 (REGRA 13): ZERO português na tela do aluno.
"""
import os
import random

random.seed(15)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Under pressure", "in a stressful situation that demands you perform right now", "",
     "\"He answers well under pressure, even when the question is hostile.\""),
    ("On the spot", "forced to answer or act immediately, with no time to prepare", "",
     "\"She put me on the spot with a question I had not expected.\""),
    ("To improvise", "to respond without preparation, using whatever you have in the moment", "",
     "\"When the slide failed, I had to improvise the whole explanation.\""),
    ("To stall for time", "to delay on purpose so you have a moment to think before you answer", "",
     "\"Repeating the question is a professional way to stall for time.\""),
    ("To pivot", "to change your approach smoothly when the first one stops working", "",
     "\"When she pushed back, I pivoted from the numbers to the recovery plan.\""),
    ("To reframe", "to present a problem in a different, more useful light", "",
     "\"I reframed the delay as a problem I had diagnosed and controlled.\""),
    ("To deflect", "to turn a hostile question aside without answering it head-on", "",
     "\"He deflected the personal jab and brought it back to the project.\""),
    ("To manage expectations", "to shape what someone believes will happen, so it stays realistic", "",
     "\"I'd rather manage their expectations early than apologize later.\""),
    ("To save face", "to protect your dignity or reputation in an awkward moment", "",
     "\"Owning the mistake let me save face better than hiding it would have.\""),
    ("To buy yourself some time", "to create a short, professional pause so you can gather your thoughts", "",
     "\"Let me pull up the data -- a clean way to buy yourself some time.\""),
    ("To turn the tables", "to reverse a disadvantage so the situation now works in your favor", "",
     "\"One good clarifying question turned the tables and put her on the back foot.\""),
    ("To keep your cool", "to stay calm and in control when the pressure rises", "",
     "\"She interrupted me twice, but I kept my cool and stayed on message.\""),
    ("To read the room", "to sense the mood of the people in front of you and adjust what you say", "",
     "\"He read the room, saw they were skeptical, and slowed down.\""),
    ("To maintain composure", "to stay outwardly calm and professional under stress", "",
     "\"Maintaining your composure matters more than having a perfect answer.\""),
]

SURVIVAL = [
    ("That's a fair question -- give me a moment to think it through.", ""),
    ("I'd rather address the delay directly than talk around it.", ""),
    ("Let me make sure I understand -- are you asking about the cause or the recovery?", ""),
    ("If the timeline is fixed, we may as well plan the recovery around it now.", ""),
    ("You had better lock that delivery date in writing before we commit.", ""),
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


CONTEXT = """<p>Last March, an interview with a Belgian rail company ended in silence. Jo&#227;o knew his field, but when the questions stopped following his script, his answers stopped coming, and he walked out feeling he had failed. Tomorrow he faces the same company again &mdash; and this time the goal is not a perfect answer, it is control. &#201;lise Laurent, the technical director, has been clear: she will interrupt him, she will ask why a project slipped three months <strong>under</strong> his watch, and she will not soften it. She is not testing his engineering. She is testing what he does when a question lands <strong>on the spot</strong>.</p>
        <p>The reflex he is building is simple. When the hostile question comes, he does not <strong>improvise</strong> something he does not believe. He <strong>buys himself some time</strong> out loud: <em>"That's a fair question &mdash; could you clarify what you mean by 'under my watch'?"</em> The clarifying question <strong>stalls</strong> professionally, moves the pressure back across the table, and makes him sound senior. Then he <strong>reframes</strong> the delay: not a failure that controlled him, but a problem he diagnosed early and kept under control. If she jabs at his credentials, he <strong>deflects</strong> the jab and brings it back to the project. Through all of it, he <strong>keeps his cool</strong> and <strong>reads the room</strong>, because the point was never to hide the delay &mdash; it was to talk about one without falling apart.</p>
        <p>His grammar carries the tone. He would rather address the delay directly than talk around it. He tells a wavering supplier that they had better confirm the date in writing before he commits. When the timeline will not move, he says they may as well plan the recovery around it now. These small modals are not decoration &mdash; <em>would rather</em> chooses, <em>had better</em> advises, <em>may as well</em> accepts reality without apology, and together they are the sound of a person thinking clearly while the room pushes. By the end of the call, the delay he had been so afraid of has become the best answer he gives all day."""

QUIZZES_CONTEXT = [
    ("1. \"<em>I'd rather address the delay directly than talk around it.</em>\" What does <em>would rather</em> signal here?",
     [("That Jo&#227;o is unsure and wants to avoid the topic.", False),
      ("A calm PREFERENCE between two options &mdash; he chooses the direct path over the evasive one, which signals control, not avoidance.", True),
      ("That he is giving the interviewer a strict order.", False)]),
    ("2. \"<em>You had better confirm the date in writing before we commit.</em>\" Why <em>had better</em> and not just <em>should</em>?",
     [("Because <em>had better</em> is only correct in the past tense.", False),
      ("Because <em>had better</em> is strong advice with an implied consequence &mdash; do it, or something bad follows &mdash; given from authority, not from fear.", True),
      ("Because <em>should</em> is grammatically wrong before a verb.", False)]),
    ("3. When &#201;lise puts him on the spot, why does Jo&#227;o repeat a clarifying question instead of answering at once?",
     [("Because he did not understand any of the question.", False),
      ("Because it stalls professionally: it buys thinking time, moves the pressure back across the table, and sounds like rigor rather than delay.", True),
      ("Because interviewers require every answer to start with a question.", False)]),
    ("4. \"<em>The timeline is fixed, so we may as well plan the recovery around it.</em>\" What does <em>may as well</em> mean?",
     [("That planning the recovery is a bad idea he is forced into.", False),
      ("That, given the situation, this is the sensible move left &mdash; he accepts reality without apologizing for it.", True),
      ("That there are still many better options he is ignoring.", False)]),
]

BLANKS = [
    ("would rather", "Hint: a calm PREFERENCE between two options -- 'd rather + bare verb, then 'than'",
     "I would rather address the delay directly than let it define the interview.",
     '"I ', ' address the delay directly than let it define the interview."'),
    ("had better", "Hint: strong advice with a warning -- 'd better + bare verb (HAD, never WOULD)",
     "You had better confirm the delivery date in writing before you commit to it.",
     '"You ', ' confirm the delivery date in writing before you commit to it."'),
    ("may as well", "Hint: the best option left when nothing better exists -- + bare verb",
     "The equipment is already late, so we may as well reschedule the test now.",
     '"The equipment is already late, so we ', ' reschedule the test now."'),
    ("buy", "Hint: to create a short pause so you can think -- ___ yourself some time",
     "Let me pull up the data -- a clean way to buy yourself some time without going silent.",
     '"Let me pull up the data -- a clean way to ', ' yourself some time without going silent."'),
    ("reframe", "Hint: to present the problem in a different, more useful light",
     "Instead of treating the question as an attack, reframe it as a request for information.",
     '"Instead of treating the question as an attack, ', ' it as a request for information."'),
    ("keep", "Hint: to stay calm and in control -- ___ your cool",
     "She interrupts you twice; the skill is to keep your cool and stay on message.",
     '"She interrupts you twice; the skill is to ', ' your cool and stay on message."'),
]

ORDER = [
    (1, "The interviewer lands a hostile question about the three-month delay, with no warning."),
    (2, "You keep your cool and buy yourself a moment instead of rushing to fill the silence."),
    (3, "You stall professionally with a clarifying question, moving the pressure back across the table."),
    (4, "You reframe the delay as a problem you diagnosed early and kept under control."),
    (5, "You read the room, invite the next question, and finish back in control of the conversation."),
]

SPEECH = [
    ("That's a fair question -- let me take a moment before I answer it.", ""),
    ("I'd rather give you the right number than a quick one.", ""),
    ("You had better confirm that date in writing before we commit.", ""),
    ("If the timeline is fixed, we may as well plan the recovery around it.", ""),
    ("Let me reframe that: the delay was diagnosed early and kept under control.", ""),
]

QUIZZES_SIT = [
    ("&#201;lise asks, sharply, why the project slipped three months under your watch. The strongest reply is:",
     [("\"That's a fair question -- could you clarify whether you mean the root cause or how I managed it once it appeared?\"", True),
      ("\"It was not really my fault, so I would rather not discuss it.\"", False),
      ("\"Um, well, these things happen on big projects.\"", False)]),
    ("She interrupts and challenges a figure you just gave. You want to stay in control. You say:",
     [("\"You are right, I am probably wrong about that number.\"", False),
      ("\"Let me pull up the exact figure -- I'd rather confirm it than guess on the record.\"", True),
      ("\"I do not remember the number, let us move on.\"", False)]),
    ("A supplier on a live call will not commit to a delivery date. You give firm advice:",
     [("\"You had better confirm that date in writing today, because the FAT schedule depends on it.\"", True),
      ("\"You would better send me the date whenever you can.\"", False),
      ("\"It is fine, take all the time you need.\"", False)]),
    ("The equipment clearly will not arrive in time and the meeting keeps arguing about it. You say:",
     [("\"We should keep waiting and hope it arrives.\"", False),
      ("\"The date isn't going to hold, so we may as well reschedule the FAT now and tell the client today.\"", True),
      ("\"There is nothing anyone can do about this.\"", False)]),
    ("&#201;lise says the delay makes her doubt you can handle a bigger project. You reframe and turn the tables:",
     [("\"Maybe you are right that I am not ready for it.\"", False),
      ("\"I understand the concern; what it actually shows is how I behave when a project goes wrong -- I diagnosed it early and kept it under control.\"", True),
      ("\"That is unfair, the delay was not my responsibility at all.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l15\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l15\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l15\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">What it does</th><th style="padding:.7rem;text-align:left">In the room</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>would rather</strong> + bare verb ... than ...<br><span style="font-size:.78rem;color:var(--text-dim)">preference</span></td><td style="padding:.6rem">You choose one option over another, calmly and on the record. It signals CONTROL, not avoidance. The verb after it takes NO <em>to</em>.</td><td style="padding:.6rem">"I<strong>'d rather</strong> <strong>address</strong> the delay directly <strong>than</strong> talk around it."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>had better</strong> + bare verb<br><span style="font-size:.78rem;color:var(--text-dim)">strong advice / warning</span></td><td style="padding:.6rem">Near an order, but softer &mdash; there is an implied <em>"or something bad happens"</em>. You give it from authority. It is <strong>HAD</strong> better, never <em>would</em> better.</td><td style="padding:.6rem">"You <strong>had better</strong> <strong>confirm</strong> that date in writing before we commit."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>may / might as well</strong> + bare verb<br><span style="font-size:.78rem;color:var(--text-dim)">the best option left</span></td><td style="padding:.6rem">Given the situation, this is the sensible move &mdash; you accept reality without apologizing for it. A calm, senior kind of shrug.</td><td style="padding:.6rem">"If the equipment hasn't arrived, we <strong>may as well</strong> <strong>reschedule</strong> the FAT now."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Bare infinitive &mdash; all three</td><td style="padding:.6rem">None of them takes <em>to</em>: never <em>"would rather TO address"</em>, never <em>"had better TO confirm"</em>. The verb stays bare.</td><td style="padding:.6rem">"We<strong>'d better</strong> <strong>lock</strong> the scope now." / "I<strong>'d rather</strong> <strong>wait</strong> than rush it."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">How it SOUNDS</td><td style="padding:.6rem" colspan="2">In speech <em>would</em> and <em>had</em> both collapse to <strong>'d</strong>: <em>I would rather</em> becomes <strong>"I'd rather"</strong>, <em>you had better</em> becomes <strong>"you'd better"</strong>. Do not confuse this <em>'d</em> with the past perfect's <em>'d</em> (<em>they'd shipped</em>): here the <em>'d</em> is followed by a <strong>bare infinitive</strong> (<em>rather address</em>, <em>better confirm</em>), not by a past participle. Listen for what comes after the <em>'d</em>, and you will always know which one it is.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (three classic mistakes):</strong> (1) <em>"I would rather TO address it"</em> &mdash; drop the <em>to</em>: <em>would rather address</em>; (2) <em>"You WOULD better confirm"</em> &mdash; it is <strong>HAD</strong> better, not <em>would</em> better; (3) <em>"We may as well TO reschedule"</em> &mdash; bare verb again: <em>may as well reschedule</em>. All three take a plain infinitive with no <em>to</em>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Pressure collocations:</strong> to <strong>buy</strong> yourself some time &middot; to <strong>keep</strong> your cool &middot; to <strong>read</strong> the room &middot; to <strong>manage</strong> expectations &middot; to <strong>stall for</strong> time &middot; to <strong>turn</strong> the tables &middot; to <strong>save</strong> face &middot; to be put <strong>on</strong> the spot.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The reflex to learn by heart:</strong> hostile question &rarr; <em>"That's a fair question &mdash; could you clarify...?"</em> (buy time) &rarr; reframe the problem as one you controlled &rarr; answer with a modal that keeps you senior (<em>I'd rather... / you had better... / we may as well...</em>). A pause you own reads as confidence; a pause you hide reads as panic."""


HTML = f"""<div class="lesson-card" id="ex-lesson-15">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 15 -- Pre-class</div>
      <h3>Speaking Under Pressure -- Handling Tough Questions in Real Time</h3>
      <div class="lesson-desc">The Belgian interview, run again -- but this time with the tools to stay in control when a question lands on the spot. How to buy yourself time out loud, stall professionally, reframe a hostile question as information, and keep your cool instead of going silent. Key words: under pressure, on the spot, to improvise, to stall for time, to pivot, to reframe, to deflect, to manage expectations, to save face, to buy yourself some time, to turn the tables, to keep your cool, to read the room, to maintain composure. Structure: the modals that let you advise, prefer and distance without sounding weak -- <em>I'd rather</em> address this directly, you <em>had better</em> confirm that in writing, we <em>may as well</em> reschedule the FAT.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="15" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="15">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Last week you presented findings and took questions from a friendly client. This week the questions come at you hostile, in an interview, with no slides to hide behind. These are the words of staying in control when a question lands on the spot. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l15">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Would Rather / Had Better / May as Well</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Three modals that let you advise, prefer and accept reality without ever sounding cornered.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence -- and notice how the "would" and "had" both collapse into a 'd, with a plain verb right after.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Pressure Moment in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of handling a hostile question in the order a calm professional actually takes them -- from the question landing to finishing back in control.</p>
      <div class="order-container" id="order-l15">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l15')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Say it at real speed: <em>would</em> and <em>had</em> collapse into a 'd (<em>I'd rather</em>, <em>you'd better</em>) -- and a plain verb follows, never a "to". A pause you own reads as confidence.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each pressure moment of the interview -- the reply that keeps you in control instead of caving or improvising.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two minutes, with no script and without stopping to correct yourself. Tone: calm, honest, always in control -- reframe the delay instead of apologizing for it.</p>
      <div class="think-card">
        <div class="think-question">You are in the interview and &#201;lise asks, sharply: "Why did this project slip three months under your watch, and why should I trust you with a bigger one?" In two minutes: buy yourself a moment out loud, ask a clarifying question if you need one, reframe the delay as a problem you diagnosed early and kept under control, concede honestly what you would do differently, and use at least one of <em>would rather</em>, <em>had better</em> or <em>may as well</em> naturally. Do not fill the silence with noise -- own it.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-15"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 15</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
