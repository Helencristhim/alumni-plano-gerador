#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 da Rosangela (A2 -- ZERO portugues na tela, REGRA 13).

O matching sai com as opcoes EMBARALHADAS (REGRA 24) e com data-answer IDENTICO ao
value da <option> certa -- o checkMatch() so compara string.
Rode:  python3 _build/rosangela-pinheiro-de-oliveira-aula1/gen_preclass.py
"""
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))

# (palavra, definicao EM INGLES SIMPLES, frase de exemplo)
VOCAB = [
    ("Passport", "the small book that shows who you are when you travel to another country",
     "My passport is in my bag."),
    ("Boarding pass", "the paper that gives you your seat and lets you enter the plane",
     "Here is my boarding pass."),
    ("Gate", "the door in the airport where you enter the plane",
     "My gate is B14."),
    ("Flight", "one trip in a plane, from one city to another",
     "My flight is at seven o'clock."),
    ("Destination", "the city or the country where you are going",
     "My destination is Paris."),
    ("Carry-on", "a small bag that goes with you inside the plane, not under it",
     "My carry-on is very small."),
    ("Check-in", "the moment when you show your passport and give your bag to the airline",
     "The check-in is on the second floor."),
    ("Delay", "when the plane leaves later than the time on your ticket",
     "There is a delay of one hour."),
    ("Departure", "the moment when the plane leaves the airport",
     "The departure is at nine in the morning."),
    ("Terminal", "one of the big buildings of an airport, with a number or a letter",
     "My flight leaves from Terminal 3."),
]

SVG_LISTEN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')


def vocab_cards():
    out = ['      <div class="vocab-cards">']
    for w, d, ex in VOCAB:
        out.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
            f'<span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{d}</span></div>'
            f'<div class="vocab-card-example">"{ex}"</div></div>'
            f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">'
            f'Listen</button></div>')
    out.append('      </div>')
    return '\n'.join(out)


def matching():
    """REGRA 24: as opcoes de CADA linha vem embaralhadas (ordem != ordem das palavras)."""
    rnd = random.Random(68)  # semente fixa: build reproduzivel
    defs = [d for _, d, _ in VOCAB]
    out = ['      <div class="match-grid" id="match-l1">']
    for w, d, _ in VOCAB:
        opts = defs[:]
        while True:
            rnd.shuffle(opts)
            if opts != defs:  # nunca na mesma ordem das palavras
                break
        o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
        out.append(
            f'        <div class="match-row" data-answer="{d}">'
            f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    out.append('      </div>')
    return '\n'.join(out)


def quiz(items):
    out = []
    for q, opts in items:
        o = ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(c).lower()}">'
            f'<span class="option-letter">{"ABC"[i]}</span> {t}</div>'
            for i, (t, c) in enumerate(opts))
        out.append(f'      <div class="quiz-item"><div class="quiz-question">{q}</div>'
                   f'<div class="quiz-options">{o}</div></div>')
    return '\n'.join(out)


CONTEXT_QUIZ = [
    ('1. Why do we say "I <strong>am</strong> from S&#227;o Paulo" and not "I live from S&#227;o Paulo"?', [
        ('With a country or a city after "from", English uses the verb TO BE: I am from...', True),
        ('Because "from" is always followed by the verb "to live".', False),
        ('Because it is a question, and questions need "to be".', False)]),
    ('2. "I <strong>live</strong> in Vila Leopoldina." Why not "I am live in Vila Leopoldina"?', [
        ('Because "live" is already the verb. It does not need "am" in front of it.', True),
        ('Because "live" is a noun here.', False),
        ('Because the sentence is in the past.', False)]),
    ('3. "I <strong>travel</strong> to Europe once in a while." What does "once in a while" mean?', [
        ('Every single week, without exception.', False),
        ('Sometimes, but not often.', True),
        ('Only one time in my whole life.', False)]),
    ('4. "<strong>Where do you live?</strong>" Why does this question need DO, but "Where are you from?" does not?', [
        ('Because "live" is an irregular verb.', False),
        ('Because the question is about the future.', False),
        ('Because "to be" makes its own question (are you...?), and every other verb needs DO.', True)]),
]

SITUATIONAL_QUIZ = [
    ('A traveler at the gate asks: "Where are you from?" You answer:', [
        ('"I have from S&#227;o Paulo."', False),
        ('"I am from S&#227;o Paulo, in Brazil."', True),
        ('"I am live in S&#227;o Paulo."', False)]),
    ('He asks: "How old are you?" The correct answer is:', [
        ('"I have 68 years."', False),
        ('"I am 68 years old."', True),
        ('"I am 68 years."', False)]),
    ('You want to ask him where he lives. You say:', [
        ('"Where do you live?"', True),
        ('"Where you live?"', False),
        ('"Where are you live?"', False)]),
    ('The screen says your plane leaves two hours late. You tell your husband:', [
        ('"There is a delay of two hours."', True),
        ('"There is a gate of two hours."', False),
        ('"There is a terminal of two hours."', False)]),
    ('You do not understand what the agent said. The best thing to say is:', [
        ('Say nothing and hope it was not important.', False),
        ('"Sorry, I do not understand. Can you repeat, please?"', True),
        ('Ask your son to speak for you.', False)]),
]

FILL = [
    ('"I ', 'am', 'Hint: WHO you are -- the verb to be', ' from S&#227;o Paulo."',
     'I am from São Paulo.'),
    ('"I ', 'live', 'Hint: WHAT you do -- your routine, no "am" in front of it', ' in Vila Leopoldina."',
     'I live in Vila Leopoldina.'),
    ('"My flight ', 'is', 'Hint: one flight, so the verb to be is singular', ' at seven o\'clock."',
     'My flight is at seven o\'clock.'),
    ('"I ', 'travel', 'Hint: WHAT you do, once in a while', ' to Europe once in a while."',
     'I travel to Europe once in a while.'),
    ('"Where ', 'are', 'Hint: the verb to be comes BEFORE you in a question', ' you from?"',
     'Where are you from?'),
    ('"Where ', 'do', 'Hint: every verb that is not "to be" needs this in a question', ' you live?"',
     'Where do you live?'),
]

ORDER = [
    (1, 'The traveler next to you says hello and asks if the seat is free.'),
    (2, 'You say your name: "I am R" and your first name.'),
    (3, 'You say where you are from and where you live.'),
    (4, 'You say where you are going and what time your flight is.'),
    (5, 'You ask him one question back: "And you? Where are you from?"'),
]

SPEECH = [
    'Hello. I am Rosângela. I am from São Paulo.',
    'I live in Vila Leopoldina, and I travel to Europe once in a while.',
    'My flight is at seven o\'clock. My destination is Paris.',
    'Excuse me, which gate is my flight?',
    'Sorry, I do not understand. Can you repeat, please?',
]

SURVIVAL = [
    'Hello. I am Rosângela. I am from São Paulo.',
    'Here is my passport and my boarding pass.',
    'I am going to Paris. My flight is at seven o\'clock.',
    'Excuse me, which gate is my flight?',
    'Sorry, I do not understand. Can you repeat, please?',
]


def build():
    fills = []
    for pre, ans, hint, post, phrase in FILL:
        fills.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
            f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
            f'data-phrase="{phrase}" placeholder="___">{post}</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')

    # ordering embaralhado no HTML (data-order guarda a ordem certa)
    rnd = random.Random(14)
    shown = ORDER[:]
    rnd.shuffle(shown)
    orders = []
    for n, txt in shown:
        orders.append(
            f'        <div class="order-item" draggable="true" data-order="{n}" '
            f'onclick="selectOrderItem(this,\'order-l1\')"><span class="order-num">?</span>'
            f'<span class="order-text">{txt}</span><span class="order-arrows">'
            f'<button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button>'
            f'</span></div>')

    speeches = []
    for p in SPEECH:
        speeches.append(
            f'      <div class="speech-card" data-phrase="{p}">\n'
            f'        <div class="speech-phrase">{p}</div>\n'
            f'        <div class="speech-controls">'
            f'<button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">'
            f'&#9632; Stop</button></div>\n'
            f'        <div class="speech-result"></div>\n'
            f'      </div>')

    survival = []
    for i, p in enumerate(SURVIVAL, 1):
        survival.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{p}</span>'
            f'<button class="btn btn-listen" data-speak="{p}" '
            f'onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')

    html = f'''<div class="lesson-card" id="ex-lesson-1">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1530521954074-e64f6810b32d?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 01 -- Pre-class</div>
      <h3>Who Is Ros&#226;ngela? -- Diagnostic and Personal Introduction at the Airport Gate</h3>
      <div class="lesson-desc">Introduce yourself at the departure gate and understand an airport announcement. Key words: passport, boarding pass, gate, flight, destination, carry-on, check-in, delay, departure, terminal. Structures: the verb to be (I am / it is) for who you are, present simple (I live / I travel) for what you do, and questions with are / do. Expression: once in a while.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to every word and read the example. These are the ten words you already see on every screen of every airport.</p>
{vocab_cards()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match every word with the right meaning. Each answer is checked as soon as you pick it.</p>
{matching()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions below.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Ros&#226;ngela <strong>is</strong> at the airport. She <strong>is</strong> from S&#227;o Paulo, and she <strong>lives</strong> in Vila Leopoldina. She <strong>is</strong> 68 years old, and she <strong>travels</strong> to Europe <strong>once in a while</strong>, with her husband. Today her <strong>destination</strong> <strong>is</strong> Paris. Her <strong>flight</strong> <strong>is</strong> at seven o'clock, and the <strong>departure</strong> <strong>is</strong> from <strong>Terminal</strong> 3. Her <strong>passport</strong> and her <strong>boarding pass</strong> <strong>are</strong> in her <strong>carry-on</strong>. The <strong>check-in</strong> <strong>is</strong> quick, and she <strong>goes</strong> to the <strong>gate</strong>. But there <strong>is</strong> a <strong>delay</strong> of two hours, and the <strong>gate</strong> <strong>is</strong> B14 now. A traveler <strong>sits</strong> next to her and <strong>asks</strong>: "Where <strong>are</strong> you from?" Ros&#226;ngela <strong>answers</strong> alone, in English, for the first time.</p>
      </div>
{quiz(CONTEXT_QUIZ)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Verb To Be vs Present Simple</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Two structures tell your whole story at the gate: one for WHO you are, one for WHAT you do.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">To be<br>I <strong>am</strong> &middot; you <strong>are</strong> &middot; it <strong>is</strong></td><td style="padding:.6rem">WHO you are, WHERE you are from, WHAT time something happens.</td><td style="padding:.6rem">I <strong>am</strong> Ros&#226;ngela. I <strong>am</strong> from S&#227;o Paulo. My flight <strong>is</strong> at seven.</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present simple<br>I <strong>live</strong> &middot; I <strong>travel</strong> &middot; I <strong>go</strong></td><td style="padding:.6rem">WHAT you do: your routine and the facts of your life. No "am" in front of it.</td><td style="padding:.6rem">I <strong>live</strong> in Vila Leopoldina. I <strong>travel</strong> with my husband.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question with to be<br><strong>Are</strong> you...? <strong>Is</strong> it...?</td><td style="padding:.6rem">The verb to be makes its own question: it jumps in front of you.</td><td style="padding:.6rem"><strong>Where are you from? Is</strong> my flight on time?</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question with do<br><strong>Do</strong> you...?</td><td style="padding:.6rem">Every other verb needs DO to make a question.</td><td style="padding:.6rem"><strong>Where do you live? Do</strong> you travel a lot?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Age<br>I <strong>am</strong> 68 years old</td><td style="padding:.6rem">In English you never HAVE an age. You ARE your age.</td><td style="padding:.6rem">I <strong>am</strong> 68 years old.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The one rule to remember:</strong> use <strong>am / is / are</strong> for who you are, and the verb alone (<strong>live, travel, go</strong>) for what you do. Never both together: "I <strong>am live</strong>" does not exist.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete every sentence. Tap Listen to hear the full sentence.</p>
{chr(10).join(fills)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a conversation at the departure gate in the right order.</p>
      <div class="order-container" id="order-l1">
{chr(10).join(orders)}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l1')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to the model, then record yourself. Take your time: listen twice before you speak. These five lines open any conversation in any airport.</p>
{chr(10).join(speeches)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Pick the best answer for these real moments at the gate.</p>
{quiz(SITUATIONAL_QUIZ)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt. There is no right or wrong version. Speak for 60 seconds, with no script. This recording is your BASELINE: we listen to it again in Lesson 20.</p>
      <div class="think-card">
        <div class="think-question">You are at the departure gate. A traveler sits next to you and says: "Hello, is this seat free?" Introduce yourself. Say your name, where you are from (to be), where you live (present simple), how old you are, how often you travel (once in a while), and where you are going today. Finish with one question for him. Take your time and do not read from a script.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-1"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 1</h4>
{chr(10).join(survival)}
    </div>

  </div>
</div>
'''
    with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'wrote preclass.html ({len(html)//1024} KB) -- {len(VOCAB)} vocab, '
          f'{len(VOCAB)} match-rows, {len(CONTEXT_QUIZ) + len(SITUATIONAL_QUIZ)} quiz-items, '
          f'{len(FILL)} fill-blanks, {len(SPEECH)} speech-cards')


if __name__ == '__main__':
    build()
