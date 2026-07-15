#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 11 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Aula de MILESTONE REVIEW (revisão/consolidação, exceção à REGRA 22 via whitelist).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 11 IN CLASS (mesmo tema/gramática/vocab — mixed conditional
NOVO + consolidação de third conditional / cleft / causative / inversion / future
perfect, na call de debrief pós-inspeção com a fornecedora francesa).
B2: ZERO português na tela do aluno (REGRA 13). Survival/speech só em inglês.
"""
import os
import random

random.seed(11)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Leverage", "an advantage you can actually use to get a better outcome in a negotiation", "",
     "\"The signed inspection protocol is our leverage -- they agreed to the criteria in writing.\""),
    ("Scope creep", "the slow, unapproved growth of a project beyond what was originally agreed", "",
     "\"Three extra tests appeared with no change order -- that is scope creep, and we are not paying for it.\""),
    ("Inspection protocol", "the agreed, written procedure for how an inspection is carried out and documented", "",
     "\"Both sides signed the inspection protocol before the factory acceptance test.\""),
    ("Status update", "a short, regular report on where every open item stands right now", "",
     "\"I send a written status update every Friday, whether there is good news in it or not.\""),
    ("The elephant in the room", "the obvious problem everyone can see but nobody wants to name", "",
     "\"Let me name the elephant in the room: the delay started on your side, not ours.\""),
    ("Deliverable", "a concrete item the project must produce and hand over", "",
     "\"The test report is a contractual deliverable, not a favor, and it is three weeks late.\""),
    ("Milestone", "a fixed checkpoint that marks real, verifiable progress", "",
     "\"We are at the halfway milestone, and on paper we are eight weeks behind.\""),
    ("Stakeholder", "anyone with a real interest in how the project turns out", "",
     "\"Every stakeholder on this package is watching the halfway milestone, so the number has to be honest.\""),
    ("Compliance", "meeting the rules, standards and contract to the letter", "",
     "\"On compliance we are exposed, so I would rather be slow and right than fast and wrong.\""),
    ("Commissioning", "the phase of testing and proving a system before it goes into service", "",
     "\"If the retest fails, commissioning slips, and the recovery plan moves with it.\""),
    ("Handover", "the formal transfer of a finished system, with its documents, to the client", "",
     "\"If those checks had been run in February, the handover would still be on its original date.\""),
    ("Procurement", "the process of sourcing, ordering and buying equipment and services", "",
     "\"Our procurement team released the cable schedule late, and I am going to own that in the room.\""),
    ("To escalate", "to raise an issue to a higher authority when it cannot be solved locally", "",
     "\"I will escalate to my manager only if you refuse to retest the three failed checks.\""),
    ("Sign-off", "the formal approval that closes an item or a phase", "",
     "\"We will have the results independently verified before any sign-off on this package.\""),
]

SURVIVAL = [
    "Let me name the elephant in the room: part of this delay is ours, and I own it.",
    "It was the missing checks that caused the delay, not the cable schedule.",
    "If your team had run the checks, we wouldn't be renegotiating this milestone now.",
    "We are going to have the three units retested against the full protocol, at your cost.",
    "By the end of the month we will have agreed a recovery plan, and you will have a status update every Friday.",
]


def esc(s):
    out = []
    for ch in s:
        out.append(ch if ord(ch) < 128 else f'&#{ord(ch)};')
    return ''.join(out)


def vocab_cards():
    rows = []
    for word, d, _pt, ex in VOCAB:
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


CONTEXT = """<p>Halfway through the program, and the numbers are not comfortable. The signaling package is eight weeks behind at the M6 <strong>milestone</strong>. Both sides signed the <strong>inspection protocol</strong> in February, and it lists three checks as mandatory hold points. Camille Laurent, the project manager for the French supplier, ran the factory test with only two of them and logged the result as a pass. That is Jo&#227;o's <strong>leverage</strong>, and it is in writing.</p>
        <p>She opens on the offensive: the whole delay, she says, is Motiva's, because the cable schedule arrived late. So Jo&#227;o does the thing that takes nerve &mdash; he names <strong>the elephant in the room</strong> before she can use it. <em>Our <strong>procurement</strong> team released the cable schedule late, and I own that.</em> Then he turns. <em>If your team had run the three checks, we <strong>wouldn't be</strong> renegotiating this <strong>milestone</strong> now.</em> Notice the tense: the cause is in the past, the result is happening today &mdash; that is the mixed conditional, and it is the one new structure of the lesson. <em>It was the third deferred check that caused this, not the cable schedule alone</em>, he adds, putting the spotlight exactly where it belongs.</p>
        <p>Camille calls it a documentation point and refuses a retest. Jo&#227;o holds the line on <strong>compliance</strong>: a deferred check is not a passed check, and he cannot grant <strong>sign-off</strong> on a hold point that was skipped. <em>We are going to <strong>have</strong> the three units <strong>retested</strong> against the full protocol, at your cost.</em> When she pushes, he lays out the deal without raising his voice: he owns the cable delay in writing, she retests at her cost, and by the end of the month they <strong>will have agreed</strong> a recovery plan. She gets a written <strong>status update</strong> every Friday until <strong>handover</strong>. If she refuses the retest, he will <strong>escalate</strong> &mdash; and neither of them wants that. He did not learn a new language for this call. He reached for one he already had."""

QUIZZES_CONTEXT = [
    ("1. \"<em>If your team had run the checks, we wouldn't be renegotiating this milestone now.</em>\" Why <em>wouldn't be</em> and not <em>wouldn't have been</em>?",
     [("Because <em>wouldn't be</em> is more polite in a negotiation.", False),
      ("Because the cause is in the PAST but the result is in the PRESENT &mdash; that is a mixed conditional, and a present result takes <em>would</em> + base verb, not <em>would have</em> + participle.", True),
      ("Because English does not allow <em>have been</em> after <em>wouldn't</em>.", False)]),
    ("2. \"<em>If I were an engineer who cut corners, I would have signed that off.</em>\" What does the past-simple condition (<em>were</em>) do here?",
     [("It describes a permanent truth about who he IS, used to explain a decision he made in the PAST.", True),
      ("It refers to a specific moment last February.", False),
      ("It is simply a more formal way of writing <em>was</em>.", False)]),
    ("3. \"<em>It was the third deferred check that caused this, not the cable schedule.</em>\" What is this structure doing?",
     [("It is hiding who is responsible, to keep the tone soft.", False),
      ("It is a cleft sentence &mdash; it puts one specific cause under a spotlight and pushes the blame to the exact right place.", True),
      ("It is a mixed conditional linking past and present.", False)]),
    ("4. Camille opens by blaming Motiva's late cable schedule for everything. Why does Jo&#227;o name Motiva's own fault FIRST?",
     [("To apologize and end the disagreement quickly.", False),
      ("Because naming the elephant in the room himself takes the weapon out of her hand &mdash; once he owns his side, there is nothing left for her to attack, and the protocol carries the rest.", True),
      ("Because the cable schedule is the real and only cause of the delay.", False)]),
]

BLANKS = [
    ("wouldn't be", "Hint: PAST cause, PRESENT result -- the mixed conditional takes <em>would</em> + base verb, not <em>would have</em>",
     "If your team had run the checks, we wouldn't be renegotiating this milestone now.",
     '"If your team had run the checks, we ', ' renegotiating this milestone now."'),
    ("were", "Hint: a PRESENT permanent truth in the if-clause takes the past simple -- and <em>were</em> for all persons",
     "If I were an engineer who cut corners, I would have signed that off months ago.",
     '"If I ', ' an engineer who cut corners, I would have signed that off months ago."'),
    ("It was", "Hint: cleft (Lesson 8) -- put the real cause under a spotlight",
     "It was the three missing checks that caused the delay, not the cable schedule.",
     '"', ' the three missing checks that caused the delay, not the cable schedule."'),
    ("have", "Hint: causative (Lesson 6) -- you arrange it, they do it, they pay: <em>have</em> + object + past participle",
     "We are going to have the three units retested against the full protocol.",
     '"We are going to ', ' the three units retested against the full protocol."'),
    ("will have agreed", "Hint: future perfect (Lesson 9) -- done BEFORE a date: <em>will have</em> + past participle",
     "By the end of the month we will have agreed a recovery plan.",
     '"By the end of the month we ', ' a recovery plan."'),
    ("escalate", "Hint: to raise the issue to a higher authority when it cannot be solved locally",
     "I will escalate this only if you refuse to retest the three checks.",
     '"I will ', ' this only if you refuse to retest the three checks."'),
]

ORDER = [
    (1, "Name the elephant in the room first: our procurement team released the cable schedule late, and I own that."),
    (2, "Anchor the position in the signed protocol: it was the third deferred check that caused this, not the cable schedule alone."),
    (3, "Link the past to the present: if that check had been run, we wouldn't be renegotiating the milestone now."),
    (4, "Hold the line on compliance: a deferred check is not a passed check, so I cannot grant sign-off on it."),
    (5, "Direct the fix with the causative: we are going to have the three units retested at your cost."),
    (6, "Close with a dated commitment: by the end of the month we will have agreed a recovery plan and a weekly status update."),
]

SPEECH = SURVIVAL[:]

QUIZZES_SIT = [
    ("Camille opens: \"This milestone is behind because Motiva released the cable schedule late. Let us be clear about that.\" The strongest reply is:",
     [("\"Let me name the elephant in the room: our procurement team was late, and I own that. But a deferred check is not a passed check, and the protocol we both signed says so.\"", True),
      ("\"That is not true. The delay is entirely on your side.\"", False),
      ("\"You are right, it is our fault. Let us move on.\"", False)]),
    ("She says only two of the three mandatory checks were run, and calls the third a \"practical decision.\" You:",
     [("Accept it, since the units are probably fine anyway.", False),
      ("Reframe it on compliance: \"A deferred check is not a passed check. On compliance I cannot sign off on a skipped hold point, so we are going to have the three units retested against the full protocol.\"", True),
      ("Say you will check the protocol later and get back to her.", False)]),
    ("You want to connect the February mistake to today's delay without simply accusing her. You say:",
     [("\"Your team made a serious error and now we are all paying for it.\"", False),
      ("\"If that check had been run in February, we wouldn't be having this conversation now.\"", True),
      ("\"If that check would have been run, we would not have this problem.\"", False)]),
    ("She offers to log the third check as \"closed by analysis\" instead of re-running it. You push back:",
     [("\"That works for me, it saves everyone time.\"", False),
      ("\"Would that survive an audit? A skipped hold point closed on paper is exactly what a regulator looks for. We retest it, or I escalate.\"", True),
      ("\"I am not sure, let me ask my manager and decide next week.\"", False)]),
    ("She asks you to accept two extra tests \"so we are aligned.\" There is no change order. You say:",
     [("\"Of course, if it keeps us aligned we can add them.\"", False),
      ("\"Two extra tests with no change order is scope creep, and I am not signing off on it. We run the protocol we agreed, nothing more and nothing less.\"", True),
      ("\"Let us split the difference and add just one.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l11\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l11\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l11\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">What it does</th><th style="padding:.7rem;text-align:left">On the call</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>if</strong> + past perfect, <strong>would</strong> + base verb<br><span style="font-size:.78rem;color:var(--text-dim)">mixed conditional -- NEW today</span></td><td style="padding:.6rem">A PAST cause with a result you feel in the PRESENT. This is the one new step: it takes the third conditional from Lesson 2 and lands the result in the room you are in now.</td><td style="padding:.6rem">"If they <strong>had followed</strong> the protocol, we <strong>wouldn't be</strong> behind now."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>if</strong> + past simple, <strong>would have</strong> + participle<br><span style="font-size:.78rem;color:var(--text-dim)">mixed conditional -- the other direction</span></td><td style="padding:.6rem">A PRESENT, permanent truth that explains a PAST decision. The condition is who you ARE; the result is what you DID.</td><td style="padding:.6rem">"If I <strong>were</strong> an engineer who cut corners, I <strong>would have signed</strong> that off."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>It was ... that</strong> / <strong>What ... is</strong><br><span style="font-size:.78rem;color:var(--text-dim)">cleft -- Lessons 5 &amp; 8</span></td><td style="padding:.6rem">Puts one fact under a spotlight and pushes the blame or the request to the exact right place.</td><td style="padding:.6rem">"<strong>It was</strong> the missing checks <strong>that</strong> caused the delay, not the cable schedule."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>Never / Not only</strong> + auxiliary + subject<br><span style="font-size:.78rem;color:var(--text-dim)">inversion -- Lessons 4 &amp; 7</span></td><td style="padding:.6rem">Formal, emphatic, and it makes a supplier sit up. The auxiliary jumps in front of the subject.</td><td style="padding:.6rem">"<strong>Never have we</strong> accepted a test that skipped a mandatory hold point."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>have</strong> + object + past participle<br><span style="font-size:.78rem;color:var(--text-dim)">causative -- Lesson 6</span></td><td style="padding:.6rem">You arrange it; someone else does it; they pay. The language of an engineer who directs work.</td><td style="padding:.6rem">"We are going to <strong>have</strong> the three units <strong>retested</strong> at your cost."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>will have</strong> + past participle<br><span style="font-size:.78rem;color:var(--text-dim)">future perfect -- Lesson 9</span></td><td style="padding:.6rem">The tense of the deadline: done BEFORE a date, and the one a contract can hold you to.</td><td style="padding:.6rem">"By the end of the month we <strong>will have agreed</strong> a recovery plan."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600"><em>wish</em> (the near cousin)</td><td style="padding:.6rem" colspan="2"><strong>wish + past perfect</strong> = regret about the past ("I wish they <em>had flagged</em> it earlier"). <strong>wish + past simple</strong> = a present you want changed ("I wish I <em>had</em> more time on this"). <strong>wish + would</strong> = a complaint about someone's behavior ("I wish they <em>would send</em> a status update without being chased").</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (two classic mistakes):</strong> (1) <em>"If they had followed it, we wouldn't HAVE BEEN behind now"</em> &mdash; when the result is <strong>now</strong>, drop the <em>have been</em> and say <strong>be</strong>; (2) <em>"If I HAD BEEN an engineer who cut corners..."</em> &mdash; when the condition is a <strong>permanent truth</strong>, use the past simple: <strong>were</strong>. Your third conditional is so strong it wants both halves in the past &mdash; the mixed conditional refuses.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The point of a milestone review:</strong> none of these six is meant to be new &mdash; five of them you already own. What today trains is the difference between <strong>recognizing</strong> a structure (you read it, you understand it) and <strong>using</strong> it (it comes out of your mouth, under pressure, without you reaching for it). Take one real fact and say it five ways.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-11">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 11 -- Pre-class</div>
      <h3>Milestone Review -- Consolidating What You Know</h3>
      <div class="lesson-desc">Halfway through the program. Nothing is new today and everything is on the table at once: the structures you already own (third conditional, cleft, inversion, causative, future perfect) in a single post-inspection debrief call with a defensive French supplier &mdash; plus the one new bridge, the MIXED CONDITIONAL, that ties a mistake in the past to a problem you are living now. Key words: leverage, scope creep, inspection protocol, status update, the elephant in the room, deliverable, milestone, stakeholder, compliance, commissioning, handover, procurement, to escalate, sign-off. Structure (new): mixed conditionals (If they <em>had followed</em> the protocol, we <em>wouldn't be</em> behind now).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="11" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="11">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">A milestone review is a consolidation, so most of these words are the spine of the whole program &mdash; and a few are new: the ones that name a problem instead of hiding it. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l11">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Mixed Conditionals &amp; the Structures You Own</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">One new bridge (the mixed conditional) and five structures from earlier lessons, on one page.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Debrief in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put in the right order the moves of an engineer who runs a defensive supplier through every structure he owns &mdash; from naming his own side's fault to closing with a dated commitment.</p>
      <div class="order-container" id="order-l11">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l11')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Say it as you would in the room &mdash; calm, unhurried, and precise. Watch the stress: LEV-er-age, com-PLY-ance, pro-CURE-ment.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the debrief call &mdash; including the shortcut she offers and the scope creep she slips in.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two minutes, with no script and without stopping to correct yourself. The point of a milestone review: reach for the structures, do not wait for them.</p>
      <div class="think-card">
        <div class="think-question">You are running the post-inspection debrief with Camille, the French supplier's project manager, and she is defensive about the delay. In two minutes: name Motiva's own fault first, anchor everything in the inspection protocol both sides signed, link the deferred check in February to the problem you are living now with a mixed conditional, direct the retest with the causative, refuse a compliance shortcut and any scope creep, and close with a dated commitment and a weekly status update.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-11"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 11</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
