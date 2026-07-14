#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 10 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
B2 -> ZERO português na tela do aluno (REGRA 13): definição em inglês, grammar tip
em inglês, survival/speech sem tradução. Matching EMBARALHADO por linha (REGRA 24).
REGRA 29: previewa a aula 10 IN CLASS (mesmo tema/gramática/vocab — entrevista
internacional, método STAR e used to / be used to / get used to).
"""
import os
import random

random.seed(10)

HERE = os.path.dirname(os.path.abspath(__file__))

# (word, speak, definition_en, example)
VOCAB = [
    ("STAR method", "STAR method",
     "a four-part way to structure an interview answer: Situation, Task, Action, Result",
     "\"When they ask for an example, I answer with the STAR method so nothing is missing.\""),
    ("Behavioral question", "Behavioral question",
     "a question that asks what you actually did in a real past situation (\"Tell me about a time...\")",
     "\"A behavioral question wants a story, not a philosophy.\""),
    ("Situational question", "Situational question",
     "a question about a hypothetical case (\"What would you do if...\")",
     "\"A situational question tests judgment; a behavioral one tests track record.\""),
    ("Transferable skills", "Transferable skills",
     "abilities you built in one role that carry over to a different job or industry",
     "\"They hire for transferable skills, not for one specific platform.\""),
    ("Gap analysis", "Gap analysis",
     "comparing where you are now with where the role needs you to be, and naming the difference",
     "\"Before the interview I did a gap analysis: what the role wants, and what I still have to prove.\""),
    ("Selling point", "Selling point",
     "the specific strength that makes you the right person, stated so the panel remembers it",
     "\"My selling point is the international interface: I have run it in three languages.\""),
    ("Culture fit", "Culture fit",
     "how well the way you work matches the way the company works",
     "\"Between two equal engineers, culture fit decides who gets the offer.\""),
    ("Notice period", "Notice period",
     "the time you must keep working for your current employer after you resign",
     "\"My notice period is thirty days, so I could start early next quarter.\""),
    ("Relocation", "Relocation",
     "moving to another city or country for a job",
     "\"The role is in Zurich, and relocation support is provided for the family.\""),
    ("To cut to the chase", "To cut to the chase",
     "to skip the preamble and get straight to the point that matters",
     "\"Let me cut to the chase: my strongest area is the international interface.\""),
    ("To read between the lines", "To read between the lines",
     "to understand the real meaning that is implied but not stated",
     "\"Read between the lines: they care more about range than about their exact product.\""),
    ("To think on your feet", "To think on your feet",
     "to respond well and quickly to something you did not prepare for",
     "\"A panel is designed to make you think on your feet, so a short pause is allowed.\""),
    ("To come across as", "To come across as",
     "to give a certain impression to the person judging you",
     "\"A calm pause makes you come across as senior, not slow.\""),
    ("To sell yourself short", "To sell yourself short",
     "to describe yourself as less capable than you really are",
     "\"Do not sell yourself short: you led the interface, so say you led it.\""),
]

SURVIVAL = [
    "I used to work on electrification, and I got used to owning the international interface.",
    "I'm used to running technical calls in English, under real schedule pressure.",
    "Let me give you a concrete example, using the STAR method.",
    "That is a good question -- let me think for a second.",
    "I would rather give you one real result than a list of skills.",
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
            f'<span class="match-word" style="flex:0 0 190px">{esc(word)}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    return '\n'.join(rows)


CONTEXT = """<p>An interview in Brussels went badly in March, and Jo&#227;o Guilherme has decided to reverse-engineer it. A recruiter, Claire Mercier, has now invited him to a <strong>competency-based</strong> panel for a Senior Signaling Engineer role in Zurich, and this time he is preparing the version of himself that walks out in control. He starts with a <strong>gap analysis</strong>: what the role needs, and what he still has to prove &mdash; and he <strong>reads between the lines</strong> of the posting, which values <strong>transferable skills</strong> and <strong>culture fit</strong> over any single product.</p>
        <p>The grammar of the interview is small, and it decides everything. Watch the word right after <em>used to</em>. <em>"I <strong>used to work</strong> on electrification"</em> &mdash; base verb &mdash; is a finished past habit: where he came from. <em>"I'm <strong>used to managing</strong> suppliers in three time zones"</em> &mdash; the <em>-ing</em> &mdash; is a state that is already normal for him. And <em>"I <strong>got used to reading</strong> CENELEC standards in English"</em> is the process in between: strange, then normal, over time. Same three words, three meanings, and a panel hears the difference. Together they narrate an arc &mdash; from, through, to &mdash; which is exactly what a hiring manager wants.</p>
        <p>So he builds his answers. When a <strong>behavioral question</strong> lands (\"Tell me about a time you managed a supplier conflict\"), he uses the <strong>STAR method</strong>: he <strong>cuts to the chase</strong>, names the story first, then runs Situation, Task, Action, Result &mdash; because the Result is the sentence that buys the job. When a <strong>situational question</strong> lands (\"What would you do if...\"), he thinks on his feet and takes the short pause that makes him <strong>come across as</strong> senior. He positions himself without arrogance: <em>\"I <strong>would rather</strong> give you one real result than a list of skills\"</em>, <em>\"I <strong>had better</strong> be specific here\"</em>, <em>\"we <strong>may as well</strong> start with the hardest project I have run\"</em>. And he refuses his oldest habit: he does not <strong>sell himself short</strong>. He owned the interface, so he says he owned it &mdash; and he closes the room on <strong>relocation</strong> and his <strong>notice period</strong> without hedging, landing on the one <strong>selling point</strong> the panel will remember."""

QUIZZES_CONTEXT = [
    ("1. \"I <em>used to work</em> on electrification.\" What does this tell the panel?",
     [("That he still works on electrification today.", False),
      ("That it is a FINISHED past habit &mdash; used to + base verb means it was true before and is over now. It is where he came FROM.", True),
      ("That he is currently learning electrification.", False)]),
    ("2. And \"I'm <em>used to managing</em> suppliers in three time zones\"? What CHANGES?",
     [("Nothing &mdash; it means the same as \"I used to manage\".", False),
      ("It is a mistake; after \"used to\" the verb should be the base form.", False),
      ("EVERYTHING: be used to + -ING is a STATE that is already normal for him NOW. \"I used to manage\" = finished; \"I'm used to managing\" = normal today.", True)]),
    ("3. When a <em>behavioral question</em> lands, what is the best move?",
     [("Cut to the chase, name the story first, and run STAR: Situation, Task, Action, Result &mdash; because the Result is what buys the job.", True),
      ("Give your general philosophy of conflict, without a specific example.", False),
      ("Say you cannot remember a specific time and describe your personality instead.", False)]),
    ("4. Which sentence is correct?",
     [("\"I would rather to give you one real result than a list of skills.\"", False),
      ("\"I would rather give you one real result than a list of skills.\"", True),
      ("\"I am used to give you one real result than a list of skills.\"", False)]),
]

BLANKS = [
    ("used to work", "Hint: a FINISHED past habit &mdash; used to + BASE verb (where you came from)",
     "I used to work on electrification before I specialized in signaling.",
     '"I ', ' on electrification before I specialized in signaling."'),
    ("used to managing", "Hint: a STATE that is normal NOW &mdash; be used to + -ING (not the base verb)",
     "I'm used to managing suppliers across three time zones.",
     '"I\'m ', ' suppliers across three time zones."'),
    ("got used to reading", "Hint: the PROCESS of adapting &mdash; get used to + -ING (strange, then normal)",
     "It took time, but I got used to reading CENELEC standards in English.",
     '"It took time, but I ', ' CENELEC standards in English."'),
    ("would rather", "Hint: preference, followed by the BASE verb with no \"to\"",
     "I would rather give you one real result than a list of skills.",
     '"I ', ' give you one real result than a list of skills."'),
    ("STAR method", "Hint: Situation, Task, Action, Result &mdash; the four-part structure",
     "Let me give you a concrete example, using the STAR method.",
     '"Let me give you a concrete example, using the ', '."'),
    ("come across as", "Hint: to give an impression &mdash; and it needs the little word \"as\"",
     "A calm pause makes you come across as senior, not slow.",
     '"A calm pause makes you ', ' senior, not slow."'),
]

ORDER = [
    (1, "Open with the arc: I used to work on electrification, and I got used to owning the interface."),
    (2, "State what is normal now: I'm used to running technical calls in English under pressure."),
    (3, "When the behavioral question lands, cut to the chase and name the story first."),
    (4, "Run the STAR structure: Situation, Task, Action, and above all the Result."),
    (5, "Position yourself: I would rather give you one real result than a list of skills."),
    (6, "Close the room: I'm open to relocation, and my notice period is thirty days."),
]

SPEECH = [
    "I used to work on electrification, and I got used to owning the international interface.",
    "I'm used to managing suppliers across three time zones on a live commissioning.",
    "Let me give you a concrete example, using the STAR method.",
    "I would rather give you one real result than a list of skills.",
    "I'm open to relocation, and my notice period is thirty days.",
]

QUIZZES_SIT = [
    ("The panel asks \"Tell me about yourself.\" The strongest opening is:",
     [("\"I only did some international work, nothing major, my English is not so good.\"", False),
      ("\"I'm a signaling engineer at Motiva. I used to work on electrification, and over three years I got used to owning the interface, so now I'm used to running it in English.\"", True),
      ("\"I'm experienced, communicative and good with international teams.\"", False)]),
    ("A behavioral question lands: \"Tell me about a time you managed a supplier conflict.\" You:",
     [("Give your general opinion on how conflicts should be handled.", False),
      ("Cut to the chase and run STAR: six units failed the EMC test (S), my task was to keep the design question open (T), I put the shared design on record (A), and all forty were re-verified at their cost (R).", True),
      ("Say you would rather not talk about conflicts.", False)]),
    ("You have never worked on their exact platform. The best framing is:",
     [("\"So maybe I am not really qualified for this role.\"", False),
      ("\"You hire for range, not one platform. My transferable skills carry over, and I got used to new standards fast at Motiva.\"", True),
      ("\"I used to working on other platforms, so it is fine.\"", False)]),
    ("They ask something you did not prepare. You want to think on your feet without looking lost. You say:",
     [("\"I don't know, sorry.\"", False),
      ("\"That is a good question &mdash; let me think for a second, because I would rather give you a real example than a general answer.\"", True),
      ("You stay completely silent and hope they move on.", False)]),
    ("Claire asks about relocation and your notice period. You answer:",
     [("\"I'm open to relocation &mdash; I got used to being deployed to site in 2023 &mdash; and my notice period is thirty days, so I could start early next quarter.\"", True),
      ("\"I am not sure, maybe I could move, I would have to think about it.\"", False),
      ("\"My notice period is a problem, so perhaps this will not work.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l10\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l10\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l10\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Meaning</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">used to + <em>base verb</em></td><td style="padding:.6rem">A past habit or state that is now FINISHED &mdash; where you came from. Negative/question drop the -d: "I <strong>didn't use to</strong>...", "<strong>Did</strong> you <strong>use to</strong>...?"</td><td style="padding:.6rem">"I <strong>used to work</strong> on electrification." &mdash; <em>I did, and I stopped.</em></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">be used to + <em>-ing / noun</em></td><td style="padding:.6rem">A STATE: it is already normal for you now. NOT the base verb &mdash; the <strong>-ing</strong>.</td><td style="padding:.6rem">"I'm <strong>used to managing</strong> suppliers." &mdash; <em>normal for me now.</em></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">get used to + <em>-ing / noun</em></td><td style="padding:.6rem">The PROCESS of becoming accustomed &mdash; from strange to normal, over time.</td><td style="padding:.6rem">"I <strong>got used to reading</strong> CENELEC in English." &mdash; <em>it became normal.</em></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">would rather / had better / may as well<br>+ <em>base verb</em> (no "to")</td><td style="padding:.6rem"><strong>would rather</strong> = preference. <strong>had better</strong> = strong advice, almost a warning. <strong>may as well</strong> = no better option, so let's.</td><td style="padding:.6rem">"I <strong>would rather</strong> give a result." &middot; "I <strong>had better</strong> be specific." &middot; "We <strong>may as well</strong> start with the hardest one."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">These structures narrate your <strong>evolution</strong> in one breath: "I <strong>used to work</strong> only in Portuguese; I <strong>got used to</strong> running calls in English; now I'm <strong>used to</strong> managing the interface across three countries." That arc &mdash; from, through, to &mdash; is exactly what a panel wants, and the verb form is the only thing that makes it come out right.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (habits carried over from Portuguese):</strong> (1) <em>"I am used to <span style="color:#dc2626">manage</span>"</em> &mdash; after be/get used to the verb takes <strong>-ing</strong>: <em>managing</em>. Your first language uses one form for both, which tempts you into the base verb; English needs the <em>-ing</em>; (2) <em>"I used to <span style="color:#dc2626">working</span>"</em> &mdash; a past habit takes the <strong>base verb</strong>: <em>used to work</em>; (3) <em>"I would rather <span style="color:#dc2626">to</span> give"</em> &mdash; would rather / had better / may as well take the <strong>base verb with no "to"</strong>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Interview collocations:</strong> <strong>value</strong> transferable skills, <strong>come across as</strong> confident (never "come across confident"), <strong>serve</strong> / <strong>work</strong> a notice period, <strong>be shortlisted for</strong> a role, <strong>provide</strong> relocation support, <strong>cut to</strong> the chase, <strong>answer</strong> a behavioral question, <strong>think on</strong> your feet.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The question to ask before every answer:</strong> "<em>Did I give them the Result?</em>" Most candidates tell the Situation and stop. The STAR answer without the R is a story with no ending &mdash; and it is the R that buys the job.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-10">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 10 -- Pre-class</div>
      <h3>The Interview Room -- Performing Under Pressure</h3>
      <div class="lesson-desc">The interview in Brussels went badly. This is the reverse-engineering: the STAR method for behavioral questions, and the grammar that narrates your evolution &mdash; used to / be used to / get used to. Key words: STAR method, behavioral question, situational question, transferable skills, gap analysis, selling point, culture fit, notice period, relocation, to cut to the chase, to read between the lines, to think on your feet, to come across as, to sell yourself short. Structure: used to + base verb (finished past) vs. be / get used to + -ing (accustomed), plus would rather / had better / may as well for positioning.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="10" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="10">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Last week you decoded native speech at full speed. Here you walk into the room. These are the words a hiring panel speaks: how they ask, what they judge, and the honest word for what you must never do to yourself. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l10">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Used To / Be Used To / Get Used To</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">One little word after "used to" decides the meaning &mdash; a base verb for a finished past, an -ing for what is normal now.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Build the Interview in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the moves of a strong panel answer in order &mdash; from the opening arc to closing the room on relocation.</p>
      <div class="order-container" id="order-l10">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l10')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Notice the -ing after "used to managing", and keep "trans-FER-a-ble" and "re-lo-CA-tion" stressed on the right syllable.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Pick the best answer for every real moment of the panel &mdash; the opening, the behavioral question, the platform gap, the unplanned question, and the close on relocation.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for 2 minutes, with no script and with no stopping to correct yourself. Tone: precise, evolving, and never smaller than you really are.</p>
      <div class="think-card">
        <div class="think-question">You have ninety seconds to answer "Tell me about yourself" for a Senior Signaling Engineer role in Zurich. Give the arc of your career using used to / got used to / am used to, land on your selling point (the international interface), and do not sell yourself short. Then handle one behavioral question in full STAR -- name the story first, and finish with the Result.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-10"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 10</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
