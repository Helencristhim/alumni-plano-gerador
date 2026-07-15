#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 17 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 17 IN CLASS (mesmo tema/gramática/vocab -- presenting KPIs,
milestones and budget deviations: o léxico de project controls e os tempos future
perfect / future continuous que transformam um forecast num compromisso). B2 (REGRA 13):
ZERO português na tela do aluno.
"""
import os
import random

random.seed(17)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("KPI (key performance indicator)", "a single number that shows whether the project is on track", "",
     "\"On-time milestone delivery is the KPI the board watches most closely.\""),
    ("Burn rate", "how fast the project is spending its budget right now", "",
     "\"Our burn rate spiked in April when we expedited the axle-counter units.\""),
    ("Run rate", "the current pace of spending, projected forward as if it continues", "",
     "\"At this run rate, the package will finish six percent over budget.\""),
    ("Forecast", "an updated projection of the final cost or completion date, based on progress so far", "",
     "\"The forecast puts final completion at the end of Q3, not Q2.\""),
    ("Earned value", "the budgeted value of the work you have actually finished, measured in money", "",
     "\"Earned value says we are behind: less work is done than the calendar suggests.\""),
    ("Cost variance", "the gap between what the finished work should have cost and what it did cost", "",
     "\"The cost variance crossed the threshold, so it went red on the dashboard.\""),
    ("Drawdown", "the amount of budget released and used from the total over time", "",
     "\"This month's drawdown was higher than plan because of the expedited shipment.\""),
    ("To come in over budget", "to end up costing more than the amount that was planned", "",
     "\"The axle-counter package came in over budget by four percent.\""),
    ("To come in under budget", "to end up costing less than the amount that was planned", "",
     "\"Two smaller packages came in under budget and offset part of the overrun.\""),
    ("Threshold", "the limit a number must stay within before it triggers an alarm or action", "",
     "\"Anything above the two-percent threshold has to be explained to the board.\""),
    ("Ballpark figure", "a rough, approximate number -- not one anyone should hold you to", "",
     "\"As a ballpark figure, expect around six percent over on that package.\""),
    ("To break even", "to reach the point where the money coming in matches the money going out", "",
     "\"The savings elsewhere let the programme break even on the minor packages.\""),
    ("Bottom line", "the final, decisive figure -- or the single most important point", "",
     "\"The bottom line: schedule green, cost amber, one variance to explain.\""),
    ("To move the needle", "to make a real, measurable difference to the result", "",
     "\"That saving is real, but it does not move the needle on the total.\""),
]

SURVIVAL = [
    ("Let me lead with the bottom line before I go into the detail.", ""),
    ("The axle-counter package came in over budget, above the threshold, and it's mine to explain.", ""),
    ("By the end of Q3 we will have completed the site acceptance tests.", ""),
    ("This time next month the crew will be running the SATs on nights.", ""),
    ("That's a ballpark figure, not the forecast -- I'll confirm the firm number by Friday.", ""),
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


CONTEXT = """<p>Tomorrow Jo&#227;o presents the Line 4 numbers to the programme board. Ingrid Vogel, the finance director on the German partner's side, already has the dashboard open: schedule green, cost amber, and one red line &mdash; the axle-counter package has <strong>come in over budget</strong>, a <strong>cost variance</strong> of four percent, above the two-percent <strong>threshold</strong>. Engineers present numbers the wrong way round: context, cause, and the figure at the end, like a proof. A board reads the other way &mdash; the number first, the story second. So Jo&#227;o will lead with the <strong>bottom line</strong>, name the deviation before Ingrid points at it, and only then explain the why.</p>
        <p>The cause is honest and short. Two units failed the incoming inspection, so the team expedited replacements, and that pushed the <strong>burn rate</strong> up in April. At that <strong>run rate</strong>, the package lands about four percent over, and the <strong>earned value</strong> sits at sixty-two against a plan of sixty-six &mdash; a little behind on completed work, not just on money. Two smaller packages <strong>came in under budget</strong> and nearly let the minor scope <strong>break even</strong>, but Jo&#227;o will say it plainly: that does not <strong>move the needle</strong> on the total. The number that matters is the one he has committed a date to.</p>
        <p>His grammar is what turns that date into a promise. A forecast is not a hope, so he does not say <em>we hope to finish by Q3</em>. He says: <em>by the end of Q3 we <strong>will have completed</strong> the site acceptance tests, and by the time the board meets again we <strong>will have closed</strong> the variance.</em> That is the future perfect &mdash; a result finished before a point, stated with <em>by</em>, never <em>until</em>. And when Ingrid asks what the team is doing right now to recover, he uses the future continuous: <em>this time next month the crew <strong>will be running</strong> the SATs on nights.</em> One tense promises a completed state; the other shows the work already in motion. Together they let a four-percent overrun sound like a number under control &mdash; because the number Jo&#227;o names first always is."""

QUIZZES_CONTEXT = [
    ("1. \"<em>By the end of Q3 we will have completed the site acceptance tests.</em>\" Why the future perfect and not the plain future?",
     [("Because the plain future is grammatically wrong after <em>by</em>.", False),
      ("Because it promises a result FINISHED before a deadline &mdash; <em>will have + completed</em> means done BY Q3, while <em>we will complete by Q3</em> only says it happens sometime around then.", True),
      ("Because the future perfect is only used for the past.", False)]),
    ("2. \"<em>This time next month the crew will be running the SATs on nights.</em>\" What does the future continuous show here?",
     [("That the SATs are already finished.", False),
      ("An action IN PROGRESS at a future point &mdash; at that moment next month, the testing is ongoing, which tells the board the recovery is already in motion.", True),
      ("That the crew ran the SATs last month.", False)]),
    ("3. Jo&#227;o says \"<em>by December we will have closed the variance</em>\", not \"<em>until December</em>\". Why <em>by</em>?",
     [("Because <em>until</em> and <em>by</em> mean exactly the same thing in English.", False),
      ("Because the future perfect takes <em>by</em> for the point a thing is done BY; <em>until</em> is for something that continues up to a point. Portuguese <em>ate</em> covers both, so the reflex is wrong.", True),
      ("Because <em>until</em> can never start a sentence.", False)]),
    ("4. Why does Jo&#227;o name the cost variance himself before Ingrid points at it?",
     [("Because a number the presenter names first reads as a number under control, while a number the board discovers reads as one out of control &mdash; even when it is the same number.", True),
      ("Because the board cannot see the dashboard.", False),
      ("Because hiding the variance is against the rules.", False)]),
]

BLANKS = [
    ("will have completed", "Hint: future perfect -- a result FINISHED before a deadline (will have + past participle)",
     "By the end of Q3 we will have completed the site acceptance tests on Line 4.",
     '"By the end of Q3 we ', ' the site acceptance tests on Line 4."'),
    ("will be running", "Hint: future continuous -- an action IN PROGRESS at a future point (will be + -ing)",
     "This time next month the crew will be running the SATs on nights to recover the two weeks.",
     '"This time next month the crew ', ' the SATs on nights to recover the two weeks."'),
    ("by", "Hint: the deadline word for a completed action -- not 'until'",
     "By December we will have closed the cost variance and brought the run rate back inside plan.",
     '"', ' December we will have closed the cost variance and brought the run rate back inside plan."'),
    ("bottom line", "Hint: the final, decisive figure you lead with",
     "Let me lead with the bottom line before I take you into the detail.",
     '"Let me lead with the ', ' before I take you into the detail."'),
    ("cost variance", "Hint: the gap between what the finished work should have cost and what it did",
     "The cost variance crossed the threshold, so it went red on the dashboard.",
     '"The ', ' crossed the threshold, so it went red on the dashboard."'),
    ("over budget", "Hint: to end up costing more than planned -- came in ___",
     "The axle-counter package came in over budget by four percent this period.",
     '"The axle-counter package came in ', ' by four percent this period."'),
]

ORDER = [
    (1, "You lead with the bottom line -- one KPI, one figure -- where the project stands on schedule and on cost."),
    (2, "You own the cost variance yourself, naming the number before the board points at it on the dashboard."),
    (3, "You explain the cause briefly: two units failed inspection, you expedited them, and the burn rate spiked."),
    (4, "You forecast the recovery in the future perfect -- by the end of Q3 the variance will have been closed."),
    (5, "You describe the work already in motion in the future continuous, then invite the next question."),
]

SPEECH = [
    ("Let me lead with the bottom line before I go into the detail.", ""),
    ("The axle-counter package came in over budget, above the threshold.", ""),
    ("By the end of Q3 we will have completed the site acceptance tests.", ""),
    ("This time next month the crew will be running the SATs on nights.", ""),
    ("That's a ballpark figure, not the forecast -- I'll confirm it Friday.", ""),
]

QUIZZES_SIT = [
    ("Ingrid opens: \"I have the dashboard open -- just give me where we stand.\" The strongest reply is:",
     [("\"The bottom line: schedule is green, cost is amber -- one package four percent over budget, above threshold. Everything else is on plan.\"", True),
      ("\"Well, it's a long story, but back in March the axle counters were reprioritised, and then...\"", False),
      ("\"Overall I think we're doing quite well, considering everything.\"", False)]),
    ("There is a cost variance above threshold on her screen. You want to stay in control. You:",
     [("\"Let me name it first: the axle-counter package came in over budget, a four-percent variance above threshold -- it's mine to explain.\"", True),
      ("\"I was hoping we could talk about the good news before we get to that.\"", False),
      ("\"I'm not sure why it's red; the dashboard might be wrong.\"", False)]),
    ("She asks when the tests will be finished. You commit to a date. You say:",
     [("\"By the end of Q3 we will have completed the site acceptance tests.\"", True),
      ("\"Until the end of Q3 we will have completed the site acceptance tests.\"", False),
      ("\"We hope to more or less finish the tests around Q3, probably.\"", False)]),
    ("She asks what the team is doing right now to recover the schedule. You say:",
     [("\"This time next month the crew will be running the SATs on nights, so the recovery is already in motion.\"", True),
      ("\"This time next month the crew will run the SATs on nights.\"", False),
      ("\"We will probably do something about it at some point next month.\"", False)]),
    ("She wants a final cost off the top of your head, before the reforecast is done. You:",
     [("\"As a ballpark figure it's around six percent over -- but that's a ballpark, not the forecast; I'll have the firm number Friday.\"", True),
      ("\"It'll be exactly six percent over, you can hold me to that right now.\"", False),
      ("\"I really can't say anything at all until the reforecast is done.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l17\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l17\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l17\')">&#9660;</button></span></div>')
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
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>will have</strong> + past participle<br><span style="font-size:.78rem;color:var(--text-dim)">future perfect</span></td><td style="padding:.6rem">An action FINISHED before a future point. It answers the board's real question -- how much will be DONE by then -- and lands as a promise with a date on it.</td><td style="padding:.6rem">"By Q3 we <strong>will have completed</strong> the SATs."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>will be</strong> + verb-ing<br><span style="font-size:.78rem;color:var(--text-dim)">future continuous</span></td><td style="padding:.6rem">An action IN PROGRESS at a future point. It shows the work is already in motion -- something happening at that moment, not a plan on a slide.</td><td style="padding:.6rem">"Next month the crew <strong>will be running</strong> the SATs."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>BY</strong>, not <em>until</em></td><td style="padding:.6rem">The future perfect takes <strong>BY</strong> for its deadline &mdash; the point a thing is done by. <em>Until</em> is for something that CONTINUES up to a point. Portuguese <em>ate</em> covers both, so the reflex is to say "until" &mdash; and it breaks the sentence.</td><td style="padding:.6rem">"<strong>By</strong> December we will have closed it." (not <em>until</em>)</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">How it SOUNDS</td><td style="padding:.6rem" colspan="2">In speech <em>will have</em> collapses to <strong>"we'll've"</strong> /wɪləv/: <em>we will have closed it</em> becomes <strong>"we'll've closed it"</strong>. Listen for the reduced <em>'ll</em> and what comes after it: <strong>have + a participle</strong> (completed, closed) = finished by a point; <strong>be + an -ing</strong> (running, working) = in progress at a point; a <strong>bare verb</strong> (finish) = just a plain future, no date locked in.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (three classic mistakes):</strong> (1) <em>"By Q3 we will complete the tests"</em> &mdash; for a result finished by then, use the future perfect: <em>we will have completed</em>; (2) <em>"Until December we will have closed it"</em> &mdash; the deadline word is <strong>BY</strong>, not <em>until</em>; (3) <em>"Next month we will run the SATs"</em> when you mean ongoing &mdash; use the future continuous: <em>we will be running</em>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Numbers collocations:</strong> to <strong>lead with</strong> the bottom line &middot; the variance <strong>crossed</strong> the threshold &middot; the package <strong>came in</strong> over / under budget &middot; to <strong>move</strong> the needle &middot; at this <strong>run</strong> rate &middot; to <strong>close</strong> a variance &middot; to <strong>own</strong> a deviation.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The reflex to learn by heart:</strong> lead with the bottom line &rarr; own the deviation in your own words (before the board finds it) &rarr; forecast in the future perfect with a date (<em>by Q3 we will have closed it</em>) &rarr; show the recovery already moving in the future continuous (<em>next month the crew will be running the SATs</em>). A number you name first is a number under control."""


HTML = f"""<div class="lesson-card" id="ex-lesson-17">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1543286386-713bdd548da4?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 17 -- Pre-class</div>
      <h3>The Numbers Behind the Project -- Presenting KPIs, Milestones and Budget Deviations</h3>
      <div class="lesson-desc">The Line 4 programme board wants the numbers, not the story. How to present a KPI, a cost variance and a budget deviation the way a board reads them: lead with the bottom line, own the deviation before they find it, and forecast the recovery in dates you will hit. Key words: KPI, burn rate, run rate, forecast, earned value, cost variance, drawdown, to come in over/under budget, threshold, ballpark figure, to break even, bottom line, to move the needle. Structure: the two tenses that turn a forecast into a commitment -- the future perfect (<em>by Q3 we will have completed the SATs</em>) and the future continuous (<em>next month the crew will be running the SATs</em>), with <em>by</em>, never <em>until</em>.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="17" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="17">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Last week you held your ground against a supplier's claim. This week you present the project's numbers to your own board -- and a board reads the number first and the story second. These are the words of project controls. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l17">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Future Perfect &amp; Future Continuous</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two tenses that turn a forecast into a commitment: one for what will be FINISHED by a date, one for what will be IN PROGRESS at a moment.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence -- and notice how "will have" collapses into "we'll've", with a past participle right after.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Board Presentation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of presenting a budget deviation in the order a senior engineer actually takes them -- from the bottom line to inviting the next question.</p>
      <div class="order-container" id="order-l17">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l17')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Say it at real speed: "will have" collapses into "we'll've", with a plain participle straight after. Lead with the number.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the board review -- the reply that leads with the number and commits to a date instead of a hope.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two minutes, with no script and without stopping to correct yourself. Tone: calm, senior, in control -- lead with the number and forecast in dates you will hit.</p>
      <div class="think-card">
        <div class="think-question">You are in the board review and Ingrid says: "I have the dashboard open -- give me where we stand, and when this cost variance is gone." In two minutes: lead with the bottom line in one sentence, own the axle-counter deviation in your own words, explain the cause briefly, and forecast the recovery using the future perfect (<em>by Q3 we will have closed it</em>) and the future continuous (<em>next month the crew will be running the SATs</em>). Use <em>by</em>, never <em>until</em>. Do not build up to the number -- lead with it.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-17"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 17</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
