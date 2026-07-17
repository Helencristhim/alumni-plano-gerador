#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-5 do hub) do Ziláudio — aula 5.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 13: aluno A2 => ZERO portugues na tela. Vocab card leva DEFINICAO em ingles simples,
o matching e palavra EN <-> definicao EN, o Grammar Tip e so em ingles, o hint do fill-in
e "Hint: ...", e nao ha .speech-translation nem .sp-pt.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 5 IN CLASS — mesmo vocab (reuniao/esclarecimento),
mesma gramatica (frases de resgate: repeat/slow down/explain/follow; preposicoes about/during/in).

A5 (REGRA 13): 8 palavras novas, frases de 5-7 palavras, gramatica = clarification requests.
A aula-chave do pacote: ele TRAVA quando nao entende uma palavra. Aqui aprende que nao
entender e normal e que ha uma frase pronta para cada buraco.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(5)  # deterministico

# (word, definicao EN simples, exemplo) — a definicao EN e o gabarito do matching (REGRA 13)
VOCAB = [
    ("Agenda", "a list of the things people will talk about in a meeting",
     "The first point on the agenda is the harvest."),
    ("Point", "one important idea that someone wants to say",
     "That is a good point, thank you."),
    ("Slide", "one screen of words or pictures that you show in a meeting",
     "Could you go back to the last slide?"),
    ("Clear", "easy to understand, with no confusion",
     "Now it is clear, thank you."),
    ("Repeat", "to say the same thing again",
     "Could you repeat that, please?"),
    ("Explain", "to make something easy to understand with more words",
     "Could you explain that word?"),
    ("Mean", "to have a sense; what a word tells you",
     "What does 'forecast' mean?"),
    ("Follow", "to understand what someone says, step by step",
     "Sorry, I'm not sure I follow."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-5">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Lesson 05 -- Pre-class</div>')
A('      <h3>When You Don\'t Understand</h3>')
A('      <div class="lesson-desc">Miss a word in a meeting and stay in the conversation &mdash; ask to repeat, slow down, '
  'and explain. Not understanding is normal; freezing is the only mistake. '
  'Key words: agenda, point, slide, clear, repeat, explain, mean, follow. Rescue phrases: '
  '<strong>Could you repeat that?</strong> &middot; <strong>What does that mean?</strong> &middot; '
  '<strong>Could you say it more slowly?</strong> Prepositions in focus: '
  '<strong>about</strong>, <strong>during</strong>, <strong>in</strong> (other words).</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Listen twice, then say the word out loud. These are the eight words you hear in every meeting.</p>')
A('      <div class="vocab-cards">')
for w, de, ex in VOCAB:
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado / REGRA 13: definicao EN) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>')
A('      <div class="match-grid" id="match-l5">')
defs = [v[1] for v in VOCAB]
assert len(set(defs)) == len(defs), 'definicoes do matching precisam ser UNICAS'
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
A('        <p>Ziláudio is in a meeting with Karen. She starts with the first <strong>point</strong> on the <strong>agenda</strong>: '
  'the harvest. She speaks fast, and Ziláudio misses one word. He does not stay quiet. "Sorry, could you '
  '<strong>repeat</strong> that?" he says. Karen says it again, and now it is <strong>clear</strong>.</p>')
A('        <p style="margin-top:.8rem"><strong>During</strong> the meeting, Karen shows a <strong>slide</strong> with a new word: '
  '"forecast". Ziláudio does not know it. "Sorry, I\'m not sure I <strong>follow</strong>. What does that word <strong>mean</strong>?" '
  'he asks. Karen is happy to <strong>explain</strong>: "A forecast is the price we expect in the future." '
  '"<strong>In</strong> other words, the future price," says Ziláudio. He did not understand every word &mdash; but he asked, '
  'and he stayed in the conversation.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Ziláudio misses a word. Instead of staying quiet, he says "Could you <strong>repeat</strong> that?" Why is this good?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Asking keeps him in the conversation. Silence would make him lose the meeting.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because you must repeat every word in a meeting.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "repeat" is a polite way to say goodbye.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. He does not know the word "forecast". What does he ask?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What means this word?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "What does that word <strong>mean</strong>?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This word is what?"</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. What is the real lesson of the text?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> You must understand every word, or the meeting is lost.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Not understanding is normal. Catch the main idea, and ask for the rest.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> You should never speak in a meeting in English.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. "A question <strong>_____</strong> the price." Which preposition is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> about (about = the topic of the question)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> during</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> in</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Rescue Phrases</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Each kind of trouble has its own phrase. You never stay quiet &mdash; you pick the phrase and ask.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">When</th><th style="padding:.7rem;text-align:left">Say this</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">You missed it</td><td style="padding:.6rem">Sorry, <strong>could you repeat</strong> that?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">It was too fast</td><td style="padding:.6rem"><strong>Could you say</strong> that more slowly?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">You don\'t know a word</td><td style="padding:.6rem"><strong>What does</strong> [word] <strong>mean</strong>?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">You are lost</td><td style="padding:.6rem">Sorry, <strong>I\'m not sure I follow</strong>.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">about &middot; during &middot; in</td><td style="padding:.6rem"><strong>about</strong> + the topic (a question about the price) &middot; <strong>during</strong> + a period of time (during the meeting) &middot; <strong>in</strong> other words (to say it a different way)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out -- the classic mistake:</strong> word order in "What does it <strong>mean</strong>?" &mdash; not "What means it?" And never translate word by word: "I no follow" is wrong &mdash; say "<strong>I\'m not sure I follow</strong>." Start with <strong>Sorry</strong> or <strong>Could you</strong>, and asking always sounds polite. Remember: asking is professional, not weak.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("repeat", "Hint: the verb for saying the same thing again",
     "Could you repeat that, please?",
     '"Could you ', ' that, please?"'),
    ("mean", "Hint: the verb for what a word tells you",
     "What does that word mean?",
     '"What does that word ', '?"'),
    ("follow", "Hint: the verb for understanding step by step",
     "Sorry, I'm not sure I follow.",
     '"Sorry, I\'m not sure I ', '."'),
    ("clear", "Hint: the adjective for easy to understand",
     "Now it is clear, thank you.",
     '"Now it is ', ', thank you."'),
    ("about", "Hint: the preposition for the topic of something",
     "I have a question about the price.",
     '"I have a question ', ' the price."'),
    ("during", "Hint: the preposition for inside a period of time",
     "Please stay during the whole meeting.",
     '"Please stay ', ' the whole meeting."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence &mdash; as many times as you want.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering (o que fazer quando nao entende) ----------
ORDER = [
    (3, "Ask them to repeat: \"Sorry, could you repeat that?\""),
    (1, "Stay calm. Missing a word is normal, not a problem."),
    (5, "Confirm the main idea: \"In other words...?\""),
    (2, "Catch the main idea, not every single word."),
    (4, "Ask the meaning: \"What does that word mean?\""),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: What to Do When You Don\'t Understand</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">You miss a word in a meeting. Put the five steps in the right order &mdash; from staying calm to confirming the idea.</p>')
A('      <div class="order-container" id="order-l5">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l5\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (as 5 frases-salva-conversa) ----------
SPEECH = [
    "Could you repeat that?",
    "What does that mean?",
    "Could you say it more slowly?",
    "Sorry, I didn't catch that.",
    "In other words...?",
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each rescue phrase, repeat it out loud, and only then record. Learn them until they come out without thinking &mdash; that is how you never freeze again.</p>')
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
    ("The other person speaks too fast and you can't keep up. You say:",
     [("\"Slow. Slow.\"", False),
      ("\"Could you say that more slowly, please?\"", True),
      ("\"You speak very fast.\"", False)]),
    ("You missed the last sentence completely. The polite way is:",
     [("\"Sorry, could you repeat that?\"", True),
      ("\"Again.\"", False),
      ("\"I don't hear.\"", False)]),
    ("You hear a word you don't know. You say:",
     [("\"That word is strange.\"", False),
      ("\"What means this word?\"", False),
      ("\"What does that word mean?\"", True)]),
    ("You are completely lost and don't know what to do. You say:",
     [("\"Sorry, I'm not sure I follow.\"", True),
      ("(stay quiet and hope)", False),
      ("\"I no understand nothing.\"", False)]),
    ("You want to check you got the main idea, in your own words. You say:",
     [("\"Repeat everything, please.\"", False),
      ("\"In other words, it is the future price?\"", True),
      ("\"Is correct or no?\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment when you get lost. Remember: asking is professional, not weak.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. The goal is simple: never go quiet.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">You are in a business meeting in English. The other person speaks fast and uses two words you do not know. Imagine the moment out loud: what do you say when you miss a sentence? What do you say when you hear a word you don\'t know? What do you say when you are lost? Use the rescue phrases &mdash; <strong>could you repeat that</strong>, <strong>what does that mean</strong>, <strong>I\'m not sure I follow</strong> &mdash; and stay in the conversation the whole time.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-5"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card (A2: sem .sp-pt — REGRA 16 + REGRA 13) ----------
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
