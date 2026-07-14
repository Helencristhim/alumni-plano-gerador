#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-5 do hub) da Lucimara — aula 5.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: a aluna e B1 -> ZERO portugues na tela. Vocab card leva DEFINICAO em ingles
(nunca traducao), matching e palavra EN <-> definicao EN, grammar tip so em ingles,
hint do fill-in em ingles, speech card SEM .speech-translation, survival card SEM .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 5 IN CLASS (mesmo tema/gramatica/vocab).
REGRA 22: nenhuma palavra das aulas 1-4 volta como vocab card novo. O curriculo pedia
'layover', mas layover JA FOI ENSINADA na aula 2 -> trocada por 'red-eye' (mesmo campo
semantico: o trajeto/o voo), que e nova e serve a viagem de setembro dela.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(5)  # deterministico

# (word, definicao EN, exemplo)
# A definicao serve ao vocab card E ao matching (REGRA 13): unicas entre si.
VOCAB = [
    ("Hypothetical", "imagined, not real -- a situation you are only supposing",
     "That is a hypothetical question, but I would say yes."),
    ("Would rather", "to prefer one thing to another, when you have to choose",
     "I would rather arrive early and be tired than lose a whole day."),
    ("Ideal", "the best possible version of something, in a perfect world",
     "In an ideal world, I would spend three days just walking around Brooklyn."),
    ("Budget", "the money you plan to spend, decided before you spend it",
     "We set a budget of three thousand dollars for the week."),
    ("To stretch (a budget)", "to make the money go further than you expected",
     "If we cooked breakfast at the apartment, we would stretch the budget."),
    ("Red-eye", "an overnight flight that leaves late and lands early in the morning",
     "If I took the red-eye, I would gain a whole day in the city."),
    ("Detour", "a longer way, off the direct route -- and often the better one",
     "We took a detour through Brooklyn, and it was the best part of the trip."),
    ("Spontaneous", "decided on the spot, with no plan at all",
     "The best night of the trip was completely spontaneous."),
    ("Off the beaten path", "away from the places every tourist goes",
     "If I had one free day, I would go somewhere off the beaten path."),
    ("To splurge", "to spend a lot of money on one special thing, on purpose",
     "I would splurge on one great dinner, not on the hotel."),
    ("To cut back (on)", "to spend or use less of something, so the money lasts",
     "If we cut back on taxis, we would have more money for restaurants."),
    ("To get away", "to travel somewhere to escape your routine, even for a weekend",
     "I need to get away for a few days -- even a long weekend would help."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-5">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 05 -- Pre-class</div>')
A('      <h3>What Would You Do? -- Dream Trips, Hypotheticals, and the Week You Would Choose</h3>')
A('      <div class="lesson-desc">In Lesson 4 the trip broke and you fixed it. Now the trip goes right &mdash; and the '
  'question changes: if you had one free week in New York, what would you do with it? Key words: '
  'hypothetical, would rather, ideal, budget, to stretch (a budget), red-eye, detour, spontaneous, off the beaten '
  'path, to splurge, to cut back, to get away. Structure: <strong>second conditional</strong> &mdash; the grammar '
  'of the world that does not exist yet ("<strong>If</strong> I <strong>had</strong> a free week in New York, I '
  '<strong>would walk</strong> a different neighborhood every day." / "<strong>If</strong> I <strong>were</strong> '
  'you, I<strong>&#8217;d</strong> take the ferry.") + <strong>I wish + past simple</strong> ("I <strong>wish</strong> '
  'I <strong>had</strong> more time in this city.").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Take your time &mdash; listen twice, then say it out loud. These are the twelve words of someone who is deciding on a trip: what you would do, what you prefer, where you would spend more and where you would spend less.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    speak = w.replace('(', '').replace(')', '')
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{speak}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 13: definicao EN; REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition. Watch out for the pair that confuses everyone: <strong>to splurge</strong> is to spend a LOT on purpose, on ONE thing; <strong>to stretch a budget</strong> is the opposite &mdash; to make the same money go further.</p>')
A('      <div class="match-grid" id="match-l5">')
defs = [v[1] for v in VOCAB]
for w, de, ex in VOCAB:
    opts = defs[:]
    while True:
        random.shuffle(opts)
        if opts != defs:
            break
    o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
    A(f'        <div class="match-row" data-answer="{de}"><span class="match-word" style="flex:0 0 150px">{w}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)"><option value="">Select...</option>{o}</select></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.3 — Grammar in Context ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text slowly, twice, and then answer the questions.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>The travel agent asks Lucimara a <strong>hypothetical</strong> question, and it is the only question '
  'that matters: "<strong>If</strong> you <strong>had</strong> one free week in New York, what <strong>would</strong> '
  'you <strong>do</strong> with it?" Nothing is decided yet. The week does not exist. That is exactly why the verb '
  'changes.</p>')
A('        <p style="margin-top:.8rem">She does not hesitate. "<strong>If</strong> I <strong>had</strong> that week, '
  'I <strong>would walk</strong>," she says. "One neighborhood a day, on foot. In an <strong>ideal</strong> world, '
  'I <strong>would spend</strong> three days just in Brooklyn &mdash; somewhere <strong>off the beaten path</strong>, '
  'not another museum." The agent smiles. "<strong>If</strong> I <strong>were</strong> you, I <strong>would take</strong> '
  'the ferry instead of the train. The ferry is a <strong>detour</strong>, and the <strong>detour</strong> is where the '
  'trip actually happens."</p>')
A('        <p style="margin-top:.8rem">Then the flight. "<strong>If</strong> you <strong>took</strong> the '
  '<strong>red-eye</strong> on Saturday, you <strong>would land</strong> at seven in the morning and you '
  '<strong>would gain</strong> a whole day." She thinks for two seconds. "I <strong>would rather</strong> arrive early '
  'and be tired than lose a Sunday." And the money? "<strong>If</strong> I <strong>cut back</strong> on the hotel, I '
  '<strong>could stretch</strong> the <strong>budget</strong> into two great dinners. I <strong>would splurge</strong> '
  'on the food, never on the room."</p>')
A('        <p style="margin-top:.8rem">One evening stays open, with no plan in it at all. Because the best night of her '
  'last trip was completely <strong>spontaneous</strong> &mdash; and you cannot book that. "I <strong>wish</strong> I '
  '<strong>had</strong> more days and fewer plans," she says. "I <strong>wish</strong> I <strong>were</strong> braver '
  'when I travel." And then, the real sentence, the one that has nothing hypothetical about it: in September, she '
  '<strong>is going</strong> to <strong>get away</strong> &mdash; and this time she will do it in English.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "<strong>If</strong> I <strong>had</strong> one free week, I <strong>would walk</strong>." Why is the verb after <strong>if</strong> in the PAST, if she is talking about September?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because she is telling us about something that already happened.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the past here does not mark TIME, it marks DISTANCE from reality. The free week does not exist yet &mdash; it is imagination. That is the rule of the second conditional: <strong>if + past simple, would + verb</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because in English the future always uses the past.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. What is the difference between these two sentences: "<strong>If</strong> my flight <strong>is</strong> canceled, I <strong>will</strong> rebook" (Lesson 4) and "<strong>If</strong> I <strong>had</strong> a free week, I <strong>would</strong> walk" (today)?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The first one is REAL and can happen tomorrow (<strong>will</strong>). The second one is IMAGINED &mdash; a world that does not exist yet (<strong>would</strong>). The same word <em>if</em>, two different distances.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> There is none &mdash; <em>will</em> and <em>would</em> are the same thing.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The first one is formal and the second one is informal.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "<strong>If</strong> I <strong>were</strong> you, I would take the ferry." Why <strong>were</strong>, and not <strong>was</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because <em>you</em> is plural.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because in the second conditional the verb <em>to be</em> becomes <strong>were</strong> for EVERYONE &mdash; I, he, she, it. It is the mark that this is NOT true: I am not you.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because <em>was</em> does not exist in American English.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If I would have more time, I would visit the MoMA every day."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "If I had more time, I would visit the MoMA every day &mdash; and I wish I had more time."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "If I have more time, I would visited the MoMA every day."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Second Conditional + I wish (the grammar of the world that does not exist)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">One sentence, two halves &mdash; and only one of them takes <em>would</em>.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Piece</th><th style="padding:.7rem;text-align:left">Form / Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">The condition<br>(if...)</td><td style="padding:.6rem"><strong>if</strong> + PAST SIMPLE. The past here is not time: it is DISTANCE from reality. <strong>Never</strong> <em>would</em> in this half.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>had</strong> a free week..."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">The result</td><td style="padding:.6rem"><strong>would</strong> + base verb (no <em>to</em>). In fast speech it shrinks to <strong>&#8217;d</strong> &mdash; and almost disappears.</td><td style="padding:.6rem">"...I <strong>would walk</strong> everywhere." / "I<strong>&#8217;d</strong> walk everywhere."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">to be = <strong>were</strong></td><td style="padding:.6rem">In the second conditional, <em>to be</em> becomes <strong>were</strong> for EVERYONE (I / he / she / it). It is the mark of the unreal.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>were</strong> you, I&#8217;d take the ferry."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem"><strong>didn&#8217;t</strong> in the condition, <strong>wouldn&#8217;t</strong> in the result.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>didn&#8217;t</strong> have the meeting, I <strong>wouldn&#8217;t</strong> stay in Midtown."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem"><strong>What would</strong> + subject + verb + <strong>if</strong> + past simple? This is the question that opens the conversation.</td><td style="padding:.6rem">"<strong>What would</strong> you <strong>do if</strong> you <strong>had</strong> one free week?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">would rather</td><td style="padding:.6rem">= to prefer (between two options). After it, the verb comes in the BASE form &mdash; no <em>to</em>. The contrast uses <strong>than</strong>.</td><td style="padding:.6rem">"I <strong>would rather</strong> <strong>arrive</strong> early <strong>than</strong> lose a Sunday."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I wish +<br>past simple</td><td style="padding:.6rem">You want NOW to be different. Same trick: past = unreal. It is not about the past, it is about today.</td><td style="padding:.6rem">"I <strong>wish</strong> I <strong>had</strong> more time." (= but I do not) / "I <strong>wish</strong> I <strong>were</strong> braver."</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">first x second<br>(the only question)</td><td style="padding:.6rem" colspan="2">Ask yourself one thing: <strong>can this really happen?</strong> If yes &rarr; <em>if</em> + present + <strong>will</strong> (Lesson 4: "If my flight is canceled, I <strong>will</strong> rebook."). If not, if it is only imagination &rarr; <em>if</em> + past + <strong>would</strong> ("If I <strong>had</strong> a free week, I <strong>would</strong> walk."). The <em>if</em> is the same. What changes is the distance.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake (there are two, and both come from your first language):</strong> (1) <em>would</em> after <em>if</em>: your head wants a <em>would</em> in BOTH halves &mdash; "if I <s>would have</s> more time". English does not allow it: <em>would</em> lives ONLY in the result half. After <em>if</em>, past simple, always. (2) <em>was</em> instead of <em>were</em>: "if I <s>was</s> you" is the most common mistake in the world &mdash; and the correct form, the one that sounds like real English, is <strong>if I were you</strong>. Keep that whole phrase as one block.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("had", "Hint: after if, PAST SIMPLE -- never would",
     "If I had a free week in New York, I would walk everywhere.",
     '"If I ', ' a free week in New York, I would walk everywhere."'),
    ("would visit", "Hint: this is the RESULT half -- this is where would goes (two words)",
     "If I had more time, I would visit the MoMA every day.",
     '"If I had more time, I ', ' the MoMA every day."'),
    ("were", "Hint: in the second conditional, the verb to be takes the SAME form for everyone",
     "If I were you, I would take the ferry instead of the train.",
     '"If I ', ' you, I would take the ferry instead of the train."'),
    ("would rather", "Hint: two words -- the way to say that you PREFER one option",
     "I would rather arrive early and be tired than lose a whole day.",
     '"I ', ' arrive early and be tired than lose a whole day."'),
    ("wish", "Hint: one single word, to say that you want NOW to be different",
     "I wish I had more time in this city.",
     '"I ', ' I had more time in this city."'),
    ("red-eye", "Hint: the flight that leaves late at night and lands at dawn",
     "If I took the red-eye, I would gain a whole day in the city.",
     '"If I took the ', ', I would gain a whole day in the city."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence &mdash; as many times as you want.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering ----------
ORDER = [
    (3, "Choose where to splurge and where to cut back: the food, not the room."),
    (1, "Answer the big question: if you had one free week, what would you do?"),
    (5, "Leave one evening completely open -- no plan, on purpose."),
    (2, "Pick the flight: the red-eye, and gain a whole day in the city."),
    (4, "Take the ferry instead of the train, and let the detour happen."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Build the Perfect Week, in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">This is how you plan a dream week: in the order the decisions really happen &mdash; from the big question to the evening you leave empty.</p>')
A('      <div class="order-container" id="order-l5">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l5\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    "If I had a free week in New York, I would walk a different neighborhood every day.",
    "If I were you, I'd take the ferry instead of the train.",
    "I would rather arrive early and be tired than lose a whole day.",
    "I wish I had more time in this city.",
    "If we cut back on the hotel, we could stretch the budget into two great dinners.",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the sentence, say it out loud, and only then record. Today the target is ONE sound: the shrinking <strong>would</strong>. In an American mouth, <em>I would</em> becomes <strong>I&#8217;d</strong> (one single syllable), <em>she would</em> becomes <strong>she&#8217;d</strong>, <em>we would</em> becomes <strong>we&#8217;d</strong>. And <em>&#8220;If I were you, I&#8217;d&#8230;&#8221;</em> comes out glued together, almost like one word. It is not laziness: it is correct English &mdash; and it is why you do not hear the <em>would</em> when they speak.</p>')
for en in SPEECH:
    A(f'      <div class="speech-card" data-phrase="{en}">')
    A(f'        <div class="speech-phrase">{en}</div>')
    A('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    A('        <div class="speech-result"></div>')
    A('      </div>')
A('    </div>')

# ---------- Stage 4 — Situational quiz ----------
QUIZ = [
    ("The travel agent asks: <em>&#8220;If you had one free week in New York, what would you do?&#8221;</em> Which answer is correct?",
     [("\"If I have one free week, I will walk a different neighborhood every day.\"", False),
      ("\"If I had one free week, I would walk a different neighborhood every day.\"", True),
      ("\"If I would have one free week, I would walk a different neighborhood every day.\"", False)]),
    ("You want to say that you prefer the overnight flight to losing a Sunday. You say:",
     [("\"I would rather take the red-eye than lose a Sunday.\"", True),
      ("\"I would rather to take the red-eye than lose a Sunday.\"", False),
      ("\"I would rather taking the red-eye that lose a Sunday.\"", False)]),
    ("The budget is good, but it is not unlimited. You decide to spend a lot on dinner and save on the hotel. You say:",
     [("I would <strong>cut back</strong> on the dinners and <strong>splurge</strong> on the room.", False),
      ("I would <strong>splurge</strong> on the food and <strong>cut back</strong> on the hotel &mdash; that way we <strong>stretch</strong> the budget.", True),
      ("I would <strong>stretch</strong> the dinners and <strong>splurge</strong> the budget.", False)]),
    ("Which sentence is correct?",
     [("\"If I was you, I would stay in Brooklyn.\"", False),
      ("\"If I were you, I would stay in Brooklyn.\"", True),
      ("\"If I am you, I would stay in Brooklyn.\"", False)]),
    ("Careful &mdash; this one is REAL, it can happen tomorrow: your flight may be canceled. Which sentence works?",
     [("\"If my flight is canceled, I will rebook at the desk.\"", True),
      ("\"If my flight was canceled, I would rebook at the desk.\"", False),
      ("\"If my flight would be canceled, I will rebook at the desk.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer. The last one is a trap, on purpose: not every <em>if</em> takes a <em>would</em>.</p>')
for i, (q, opts) in enumerate(QUIZ, 1):
    A(f'      <div class="quiz-item"><div class="quiz-question">{q}</div><div class="quiz-options">')
    for letter, (txt, ok) in zip('ABC', opts):
        A(f'        <div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(ok).lower()}">'
          f'<span class="option-letter">{letter}</span> {txt}</div>')
    A('      </div></div>')
A('    </div>')

# ---------- Stage 5 — Free production ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 90 seconds, with no script.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">Plan your perfect week in New York, out loud. If you had seven free days in September, and the budget were generous but not unlimited, what would you do each day? Be specific: name a neighborhood, a kind of restaurant, one thing you would do that is off the beaten path. Say where you would splurge and where you would cut back. Then finish with two wishes: "I wish I had..." and "I wish I were..." Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-5"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 5</h4>')
for i, en in enumerate(SPEECH, 1):
    A(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
A('    </div>')

A('')
A('  </div>')
A('</div>')

html = '\n'.join(p) + '\n'
open(OUT, 'w', encoding='utf-8').write(html)
print(f'preclass.html: {len(html)//1024} KB | vocab={len(VOCAB)} match={len(VOCAB)} '
      f'quiz={len(QUIZ)+4} blanks={len(BLANKS)} speech={len(SPEECH)} order=1 think=1 '
      f'| divs {html.count("<div")}/{html.count("</div>")}')
