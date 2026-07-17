#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 19 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "Talking About Clarinha" -- falar da familia e da neta Clarinha (3 anos, escola
bilingue) em ingles simples e confiante. Aula-DESBLOQUEIO (perfil): o filtro afetivo cai
no tema que ela ama. Foco gramatical NOVO: possessives (my/her/our + 's).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival
    todos em ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (proud, curious, bilingual, encourage, support, grow up,
    spend time, playground) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-18
    (verificado no hub -- 'granddaughter' e 'family' ja existiam, por isso ficaram DE FORA).
    Expressao: 'I am so proud of...'. Idioma: 'It runs in the family.'
  - check_grammar_progression: grammar_point NOVO = possessives (adjectives + 's),
    distinto dos 18 pontos ja usados (present simple, past simple, comparatives, etc.).
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 19 IN CLASS (mesmo tema: Clarinha/familia;
    mesmo vocab; mesma gramatica: possessives).
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (trauma de exposicao + gatilho emocional nº1): Clarinha como ancora afetiva;
    frase-identidade "I speak English, and I am improving" no survival card.
"""
import random

random.seed(19)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo)
VOCAB = [
    ("Proud", "very happy about something good that you, or someone close to you, did",
     "I am so proud of my granddaughter."),
    ("Curious", "wanting to learn and know more about everything",
     "Clarinha is a very curious child; she asks about everything."),
    ("Bilingual", "able to speak two languages",
     "She goes to a bilingual school and learns English and Portuguese."),
    ("Encourage", "to give someone hope and confidence to keep trying",
     "I encourage her to say a few words in English every day."),
    ("Support", "to help someone so they feel strong and safe",
     "A good family supports every child."),
    ("Grow up", "to become older and change from a child into an adult",
     "When she grows up, she will speak two languages."),
    ("Spend time", "to use your hours doing something, or being with someone",
     "We spend time together every weekend."),
    ("Playground", "an outdoor place where children play",
     "On Sunday, we went to the playground."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-19">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 19 -- Pre-class</div>')
w('      <h3>Talking About Clarinha -- Family &amp; Bilingual Moments</h3>')
w('      <div class="lesson-desc">Talk about your family and your granddaughter Clarinha in simple, warm English: '
  'describe her (<strong>curious</strong>, <strong>bilingual</strong>, <strong>proud</strong>), say who things '
  'belong to with <strong>possessives</strong> (my, her, our, and Clarinha\'s), and learn the warm phrases you can '
  'say to her right now. Key words: proud, curious, bilingual, encourage, support, grow up, spend time, playground. '
  'Grammar: possessive adjectives (my / her / our) and name + \'s. Expression: "I am so proud of..." '
  'Idiom of the lesson: "It runs in the family."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="19" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="19">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words to describe your family and Clarinha.</p>')
w('      <div class="vocab-cards">')
for word, dfn, ex in VOCAB:
    w(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{dfn}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{word}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.2 (REGRA 24)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its definition.</p>')
w('      <div class="match-grid" id="match-l19">')
all_defs = [d for _, d, _ in VOCAB]
for word, dfn, _ex in VOCAB:
    opts = all_defs[:]
    while True:
        random.shuffle(opts)
        if opts != all_defs:
            break
    o = ''.join(f'<option value="{d}">{d}</option>' for d in opts)
    w(f'        <div class="match-row" data-answer="{dfn}">'
      f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
      f'<option value="">Select...</option>{o}</select></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.3
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>This is <strong>my</strong> granddaughter, Clarinha. <strong>Her</strong> name is Clarinha, and she is three '
  'years old. She is very <strong>curious</strong> &mdash; she asks about everything, all day long. <strong>Her</strong> '
  'school is <strong>bilingual</strong>, so she is learning English and Portuguese at the same time. I am so '
  '<strong>proud</strong> of her. <strong>Our</strong> weekends are the best part of my week: we <strong>spend time</strong> '
  'together, we go to the <strong>playground</strong>, and I try to say small things in English. I <strong>encourage</strong> '
  'her every day, and I will always <strong>support</strong> her. When she <strong>grows up</strong>, she will speak two '
  'languages. <strong>Clarinha\'s</strong> curiosity is a gift &mdash; and I think it runs in the family.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. How does Maria Clara describe Clarinha?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Quiet and tired.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Very <strong>curious</strong> &mdash; she asks about everything.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Afraid of English.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. What kind of school does Clarinha go to?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A <strong>bilingual</strong> school (English and Portuguese).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> A school only in Portuguese.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> No school yet.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. What do they do on weekends?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> They stay far apart.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> They <strong>spend time</strong> together and go to the <strong>playground</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> They only watch television.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. In "<strong>Clarinha\'s</strong> curiosity", what does the \'s show?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That there are many children.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That the curiosity belongs to Clarinha (the owner).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That the sentence is a question.</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Possessives</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">To say who something belongs to, use a possessive adjective (my, your, his, her, our, their) right before the noun, or add \'s to a person\'s name. The word matches the person, not the noun after it.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">What it does</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>my, your, his, her, our, their</strong></td>'
  '<td style="padding:.6rem">A possessive adjective. It goes right before a noun to show who it belongs to.</td>'
  '<td style="padding:.6rem"><strong>my</strong> granddaughter &middot; <strong>her</strong> school &middot; <strong>our</strong> weekend</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>name + \'s</strong></td>'
  '<td style="padding:.6rem">Apostrophe + s after a person\'s name shows the owner.</td>'
  '<td style="padding:.6rem"><strong>Clarinha\'s</strong> smile &middot; my <strong>son\'s</strong> house</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">he &rarr; his, she &rarr; her</td>'
  '<td style="padding:.6rem">The possessive matches the person, not the noun. A woman = her; a man = his.</td>'
  '<td style="padding:.6rem"><strong>her</strong> name (Clarinha) &middot; <strong>his</strong> name (my son)</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready idiom: <strong>It runs in the family.</strong></td>'
  '<td style="padding:.6rem">It means a quality (like curiosity) is passed down from parents to children.</td>'
  '<td style="padding:.6rem">"Clarinha loves to learn &mdash; <strong>it runs in the family</strong>."</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"the toys of Clarinha"</strong> or <strong>"She name is..."</strong>. Use \'s and the right '
  'possessive: it is <strong>"Clarinha\'s toys"</strong> and <strong>"Her name is..."</strong>. And remember: a child '
  '<strong>is</strong> three years old, she does not "have" three years.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("My", "Hint: a possessive adjective before the noun 'granddaughter'",
     "My granddaughter is three years old.",
     '"', ' granddaughter is three years old."'),
    ("Her", "Hint: the possessive for a woman, before the noun 'school'",
     "Her school is bilingual.",
     '"', ' school is bilingual."'),
    ("Clarinha's", "Hint: add apostrophe s to the name to show the owner",
     "Clarinha's favorite game is hide-and-seek.",
     '"', ' favorite game is hide-and-seek."'),
    ("Our", "Hint: the possessive for 'we', before the noun 'weekends'",
     "Our weekends are for the playground.",
     '"', ' weekends are for the playground."'),
    ("proud", "Hint: the feeling you have about something good she did",
     "I am so proud of her.",
     '"I am so ', ' of her."'),
    ("grows up", "Hint: to become older, from child to adult",
     "When she grows up, she will speak two languages.",
     '"When she ', ', she will speak two languages."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence. Ask yourself: whose is it?</p>')
for ans, hint, phrase, pre, post in BLANKS:
    w(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div>'
      f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 2 (order)
ORDER = [
    (1, "First, you introduce Clarinha: \"This is my granddaughter, Clarinha.\""),
    (2, "Then, you say her age: \"She is three years old.\""),
    (3, "You describe her: \"She is very curious, and her school is bilingual.\""),
    (4, "After that, you say what you do: \"We spend time together at the playground.\""),
    (5, "Finally, you show your pride: \"I am so proud of her.\""),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Description in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of describing Clarinha in the correct order, from first to last.</p>')
w('      <div class="order-container" id="order-l19">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l19\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l19\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l19\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l19\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "This is my granddaughter, Clarinha.",
    "She is very curious, and her school is bilingual.",
    "I am so proud of her.",
    "We spend time together at the playground.",
    "When she grows up, she will speak two languages.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. There is no wrong way to try &mdash; these are the exact sentences you will use to talk about Clarinha.</p>')
for en in SPEECH:
    w(f'      <div class="speech-card" data-phrase="{en}">')
    w(f'        <div class="speech-phrase">{en}</div>')
    w('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    w('        <div class="speech-result"></div>')
    w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 4 (quiz situacional)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each family moment.</p>')
w('      <div class="quiz-item"><div class="quiz-question">A colleague asks about your family. You introduce Clarinha. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The granddaughter of me have three years."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "This is my granddaughter, Clarinha. She is three years old."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She name Clarinha, three years."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Clarinha says a new English word for the first time. You praise her. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Good job, sweetheart! I am so proud of you."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "No, wrong. Try again."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> (silence)</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to describe Clarinha\'s school. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The school of Clarinha is bilingual."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Her school is bilingual; she learns English and Portuguese."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She have a school with two languages."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Clarinha points at a dog and looks at you. You encourage her. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Say now the word, fast."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Can you say that in English? Yes, a dog!"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You do not know it."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A colleague asks why English matters to you. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "For no reason."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I want to speak English with Clarinha when she grows up."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "English is not important for me."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Imagine a colleague at the Seoul dinner has never met your family. Tell them about '
  'Clarinha and your children: who they are, how old Clarinha is, what she is like (curious, bilingual), what you do '
  'together on weekends, and why English matters to you. Use possessives (my, her, our, Clarinha\'s) and take your '
  'time.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-19"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
SURVIVAL = [
    "This is my granddaughter, Clarinha.",
    "She is very curious, and I am so proud of her.",
    "Can you say that in English?",
    "Let's read this together.",
    "I speak English, and I am improving.",
]
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 19</h4>')
for i, en in enumerate(SURVIVAL, 1):
    w(f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
      f'<span class="sp-en">{en}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
w('    </div>')
w('')
w('  </div>')
w('</div>')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {OUT} ({len(VOCAB)} vocab, {len(BLANKS)} blanks, {len(SPEECH)} speech cards)')
