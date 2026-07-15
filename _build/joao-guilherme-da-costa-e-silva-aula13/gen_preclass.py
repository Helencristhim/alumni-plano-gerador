#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 13 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 13 IN CLASS (mesmo tema/gramática/vocab -- past perfect e
past perfect continuous na reconstrução de um non-conformance sobre normas técnicas).
B2 (REGRA 13): ZERO português na tela do aluno.
"""
import os
import random

random.seed(13)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Provision", "a specific requirement written into a standard or a contract", "",
     "\"The provision on grounding is in Annex D, not in the main clause.\""),
    ("To stipulate", "to state a requirement clearly and formally in a written document", "",
     "\"The contract stipulates the standard in its current revision.\""),
    ("Wording", "the exact words of a clause, on which its whole meaning depends", "",
     "\"One word changed in the wording, and the obligation changed with it.\""),
    ("Loophole", "a gap in the wording that lets one side avoid an obligation", "",
     "\"They read the old annex as a loophole; I read it as an oversight.\""),
    ("To supersede", "when a newer revision replaces and cancels an earlier one", "",
     "\"Revision D superseded revision C in December.\""),
    ("Amendment", "a formal, documented change to a standard or a contract", "",
     "\"The amendment rewrote one provision and left the rest untouched.\""),
    ("Annex", "an extra section at the back of a standard, where the detailed requirements live", "",
     "\"Everybody reads the main clause; nobody reads Annex D.\""),
    ("Normative reference", "another standard that a standard makes mandatory by citing it", "",
     "\"The normative reference points to a document that had also been revised.\""),
    ("Discrepancy", "a conflict between two documents that are supposed to agree", "",
     "\"The discrepancy was between the certificate and the current revision.\""),
    ("Order of precedence", "the rule that decides which document wins when they conflict", "",
     "\"The order of precedence puts the contract above the supplier's data sheet.\""),
    ("Caveat", "a warning or condition attached to a statement or an approval", "",
     "\"I will approve it, with one caveat: subject to the amended annex.\""),
    ("Grey area", "a point the wording does not clearly cover", "",
     "\"Whose responsibility the revision check was is a grey area.\""),
    ("Fine print", "the detailed conditions, easy to miss, that carry the real obligations", "",
     "\"The fine print is where the deadline and the penalty actually live.\""),
    ("The devil is in the details", "a saying: the small details are where the real problems hide", "",
     "\"The clause looked clean, but the devil is in the details.\""),
]

SURVIVAL = [
    ("By the time we caught the discrepancy, the supplier had already shipped the units.", ""),
    ("They had been manufacturing to a superseded revision for three months.", ""),
    ("Neither side had flagged it, so the discrepancy was shared, not a breach.", ""),
    ("Which document takes precedence here -- the contract, or the standard?", ""),
    ("Before we sign anything, I want that provision spelled out and the annex reference fixed.", ""),
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


CONTEXT = """<p>The purchase order reached the German supplier in January, and at that moment revision C of the signaling standard was current, so the axle counters were certified to it. What nobody knew was that a committee <strong>amendment</strong> had already been approved in December, and that amendment had <strong>superseded</strong> revision C and rewritten a single <strong>provision</strong> in <strong>Annex D</strong>. It was not published on the portal until March. So by the time it appeared, the supplier had been manufacturing to the old revision for almost three months, and had already shipped the first batch.</p>
        <p>The <strong>discrepancy</strong> only surfaced in April, when Jo&#227;o Guilherme's inspector opened Annex D at the factory acceptance test. By then, both sides had been working from a document that no longer applied. The contract had <strong>stipulated</strong> the standard "in its current revision", and the <strong>wording</strong> mattered: current meant current on the day of delivery, and by February the current revision had already changed. Nobody on either side had checked the portal, and nobody had flagged it. It was not a <strong>loophole</strong> somebody had exploited; it was a <strong>grey area</strong> both teams had fallen into, because the main clause had stayed the same and neither had opened the annex.</p>
        <p>So Jo&#227;o did the thing that settles a dispute: he reconstructed the sequence, event by event, in the past. He established what had happened first, how long each side had been working from the superseded revision, and what neither party had done. Then he applied the <strong>order of precedence</strong> &mdash; the contract governs, and the contract pointed at a standard that had moved &mdash; and proposed a <strong>caveat</strong>: accept nothing until the provision is spelled out and the annex reference is fixed. He did not win by assigning blame. He won by putting the events in order, because once the timeline was clear, the liability stopped being an argument and became a date."""

QUIZZES_CONTEXT = [
    ("1. \"<em>By the time the discrepancy surfaced, the supplier had already shipped the first batch.</em>\" What does <em>had shipped</em> tell you?",
     [("That the shipping and the discovery happened at the same time.", False),
      ("That the shipping came FIRST &mdash; <em>had</em> + past participle marks the earlier of two past events, and in a dispute that order is the liability.", True),
      ("That the shipping had not happened yet when the discrepancy surfaced.", False)]),
    ("2. \"<em>They had been manufacturing to the old revision for three months.</em>\" Why <em>had been manufacturing</em> and not <em>were manufacturing</em>?",
     [("Because <em>had been manufacturing</em> sounds more formal.", False),
      ("Because it measures a DURATION that had built up to a past point &mdash; the plain past continuous cannot show that the three months came before the amendment appeared.", True),
      ("Because English does not allow the past continuous with <em>for three months</em>.", False)]),
    ("3. The contract stipulated the standard \"in its current revision\". Why did the certificate still not comply?",
     [("Because the current revision had changed before delivery &mdash; an amendment had superseded revision C by the shipping date, so the certificate pointed at a revision that no longer applied.", True),
      ("Because the contract had named revision D specifically.", False),
      ("Because the supplier had never certified the units at all.", False)]),
    ("4. Why does Jo&#227;o call it a shared discrepancy rather than a breach?",
     [("Because the supplier had signed a confession.", False),
      ("Because neither side had checked the portal and neither had flagged the amendment &mdash; it was a grey area both had fallen into, not an obligation one side had knowingly avoided.", True),
      ("Because the amendment had never actually been approved.", False)]),
]

BLANKS = [
    ("had already shipped", "Hint: the EARLIER of two past events -- <em>had</em> + past participle marks what came first",
     "By the time we caught the discrepancy, the supplier had already shipped the forty units.",
     '"By the time we caught the discrepancy, the supplier ', ' the forty units."'),
    ("had been manufacturing", "Hint: a DURATION running up to a past point -- <em>had been</em> + verb with -ing",
     "They had been manufacturing to revision C for three months before the amendment reached them.",
     '"They ', ' to revision C for three months before the amendment reached them."'),
    ("had superseded", "Hint: the earlier event -- a newer revision had replaced the old one before the units shipped",
     "Before the units left the factory, the amendment had superseded revision C.",
     '"Before the units left the factory, the amendment ', ' revision C."'),
    ("had checked", "Hint: what nobody had done up to that past point -- <em>had</em> + past participle",
     "Nobody had checked the portal, so the discrepancy had gone unnoticed for weeks.",
     '"Nobody ', ' the portal, so the discrepancy had gone unnoticed for weeks."'),
    ("stipulated", "Hint: to state a requirement clearly and formally in the contract",
     "The contract had stipulated the standard in its current revision.",
     '"The contract had ', ' the standard in its current revision."'),
    ("precedence", "Hint: the rule that decides which document wins when two conflict",
     "Which document takes precedence, the contract or the standard?",
     '"Which document takes ', ', the contract or the standard?"'),
]

ORDER = [
    (1, "The purchase order arrives: revision C is current, and the supplier certifies the units to it."),
    (2, "Unknown to both sides, a committee amendment supersedes revision C and rewrites one provision in Annex D."),
    (3, "The supplier ships the first batch, still built to revision C, three months later."),
    (4, "At the factory acceptance test, the inspector opens Annex D and finds the discrepancy."),
    (5, "Both sides reconstruct the timeline and see that neither had checked the portal."),
    (6, "They agree it is a shared discrepancy and fix the annex reference in the contract."),
]

SPEECH = [
    ("By the time we caught the discrepancy, the supplier had already shipped the units.", ""),
    ("They had been manufacturing to a superseded revision for three months.", ""),
    ("The amendment had changed one provision in Annex D.", ""),
    ("Which document takes precedence here, the contract or the standard?", ""),
    ("Before we sign anything, I want that provision spelled out.", ""),
]

QUIZZES_SIT = [
    ("Sabine says the units were compliant when they left the factory. The strongest reply is:",
     [("\"When the units left the factory, revision C had already been superseded by the amendment, so they were built to a revision that no longer applied.\"", True),
      ("\"You are right, if they were compliant then, the case is closed.\"", False),
      ("\"Compliance does not matter once the units have shipped.\"", False)]),
    ("You want to explain why the inspector only caught the problem in April. You say:",
     [("\"The inspector was simply too slow to check.\"", False),
      ("\"By the time the inspector opened Annex D, the units had already been assembled and shipped, and nobody had cross-checked which revision was current.\"", True),
      ("\"There was no way anyone could have found the discrepancy.\"", False)]),
    ("Sabine argues the contract never named a specific revision. You push back:",
     [("\"You are correct, so there is no obligation at all.\"", False),
      ("\"The wording stipulated the standard in its current revision, and by the shipping date the current revision had already changed, so the requirement had moved with it.\"", True),
      ("\"The wording is not important; let us just move on.\"", False)]),
    ("She suggests accepting the units as they are, to save time. You answer:",
     [("\"Fine, if that is easier for your team, we will accept them.\"", False),
      ("\"I will consider it, with one caveat: I want that provision spelled out and the annex reference fixed before we sign anything.\"", True),
      ("\"That decision is not mine to make.\"", False)]),
    ("She asks whose fault the whole thing was. You reply:",
     [("\"It was entirely your fault, because you shipped the units.\"", False),
      ("\"Neither side had flagged the amendment and neither had updated its documents, so this is a shared discrepancy, not a breach.\"", True),
      ("\"It was entirely our fault, so we will absorb the cost.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l13\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l13\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l13\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">What it does</th><th style="padding:.7rem;text-align:left">In the report</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>had</strong> + past participle<br><span style="font-size:.78rem;color:var(--text-dim)">past perfect</span></td><td style="padding:.6rem">The EARLIER of two past events &mdash; the past before the past. It fixes the ORDER, and in a dispute the order is the liability.</td><td style="padding:.6rem">"By the time we flagged it, they <strong>had</strong> already <strong>shipped</strong> the units."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>had been</strong> + verb -ing<br><span style="font-size:.78rem;color:var(--text-dim)">past perfect continuous</span></td><td style="padding:.6rem">HOW LONG something had been going on up to that past point. It shows the problem was not new, and it justifies the scale of it.</td><td style="padding:.6rem">"They <strong>had been manufacturing</strong> to the old revision for three months."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>by the time / before / when</em> + PAST</td><td style="padding:.6rem">These words set the LATER past moment; the earlier action then takes the past perfect. Both clauses are in the past &mdash; the perfect just says which came first.</td><td style="padding:.6rem">"<strong>By the time</strong> the audit began, revision C <strong>had</strong> been superseded."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>already / just / never / not yet</em></td><td style="padding:.6rem"><strong>already</strong> = it had happened before then; <strong>never / not yet</strong> = it had not happened up to then. These words live inside the past perfect.</td><td style="padding:.6rem">"We <strong>had never received</strong> the amendment, and they <strong>had already closed</strong> the file."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">How it SOUNDS</td><td style="padding:.6rem" colspan="2">In speech <em>had</em> almost never survives as a full word: it collapses to <strong>'d</strong>. <em>we had</em> becomes <strong>"we'd"</strong>, <em>they had been</em> becomes <strong>"they'd been"</strong>, <em>it had</em> becomes <strong>"it'd"</strong>. The tense is carried by the <strong>PARTICIPLE at the end</strong> (<em>shipped, superseded, changed</em>), not by the little <em>'d</em> at the front. Stop hunting for a stressed <em>had</em>: listen for the participle, and you will hear the order.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (two classic mistakes):</strong> (1) <em>"When we caught it, the supplier already shipped the units"</em> &mdash; the earlier event needs <strong>had</strong> + past participle: <em>had already shipped</em>. Portuguese lets one simple past do the whole sequence, so the order disappears; (2) <em>"They were manufacturing for three months before..."</em> &mdash; a duration running up to a past point takes the <strong>past perfect continuous</strong>: <em>had been manufacturing</em>, never the plain past continuous.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Fine-print collocations:</strong> an amendment <strong>supersedes</strong> a revision (never "cancels") &middot; a contract <strong>stipulates</strong> a requirement &middot; a document <strong>takes</strong> precedence &middot; to <strong>spell out</strong> a provision &middot; to <strong>flag</strong> a discrepancy &middot; to <strong>fix</strong> an annex reference.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Reconstructing a sequence (learn the frame by heart):</strong> "<em>By the time X happened, Y had already happened.</em>" &middot; "<em>They had been doing Z for [time] before...</em>" &middot; "<em>Neither side had flagged it, so...</em>" &mdash; this is how a non-conformance stops being a fight and becomes a timeline.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-13">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1568992687947-868a62a9f521?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 13 -- Pre-class</div>
      <h3>Reading the Fine Print -- When the Standard Moved and Nobody Told You</h3>
      <div class="lesson-desc">Forty units certified to a revision that an amendment had already superseded: how to reconstruct the sequence of a non-conformance in the past perfect (what had happened FIRST, and how long each side had been working from the old revision), and how to pin down the fine print before you sign. Key words: provision, to stipulate, wording, loophole, to supersede, amendment, annex, normative reference, discrepancy, order of precedence, caveat, grey area, fine print, the devil is in the details. Structure: past perfect and past perfect continuous (By the time we caught it, the supplier <em>had already shipped</em>... / They <em>had been manufacturing</em> to the old revision for three months...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="13" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="13">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">In Lesson 12 you pushed back on a person. This week the conflict is with a DOCUMENT: a standard that had changed while nobody was reading the annex. These are the words of the fine print &mdash; who requires what, in which revision, and where the change was hidden. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l13">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Past Perfect &amp; Past Perfect Continuous</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The tense that reconstructs a sequence &mdash; and why the order of events decides the liability.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence &mdash; and notice how the "had" almost disappears into a 'd.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Non-Conformance in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the events of the dispute in the order they actually happened &mdash; from the purchase order to the shared agreement.</p>
      <div class="order-container" id="order-l13">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l13')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Say it fast, running the words together: <em>had</em> collapses into a 'd (<em>they'd already shipped</em>) &mdash; producing the reduced form is what trains your ear to catch it. Watch the stress: soo-per-SEED, dis-KREP-an-cy, PRESS-e-dence.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the dispute call &mdash; the reply that proves the order of events instead of assigning blame.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two minutes, with no script and without stopping to correct yourself. Tone: calm, precise, and always proving which event came first.</p>
      <div class="think-card">
        <div class="think-question">You are on the dispute call with the supplier's contracts manager. In two minutes: reconstruct the sequence of the non-conformance in the past perfect (what had already happened by the time your inspector flagged it, and how long each side had been working from the superseded revision), cite the wording of the contract, apply the order of precedence, concede your own side's missed update while holding theirs, and close by proposing a caveat: nothing is accepted until the provision is spelled out and the annex reference is fixed.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-13"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 13</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
