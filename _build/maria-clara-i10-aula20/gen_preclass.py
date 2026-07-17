#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 20 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema (CAPSTONE do bloco -- ULTIMA aula da meta 20/20): "Presenting Yourself and Your Work --
Formal Self-Introduction and Institutional Pitch in International Settings". Gramatica (funcional,
nova): estruturar uma auto-apresentacao formal em quatro partes (open+thank -> role+institution ->
experience+expertise -> forward-looking close). Contexto: a plenaria de abertura de uma conferencia
em Seul, onde a Maria Clara se apresenta e apresenta sua instituicao.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em ingles
    simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival todos em
    ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (honored, expertise, partnership, opportunity, exchange, productive,
    contribution, collaboration) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-19
    (verificado no hub por grep). Ja em circulacao (nao ensinado como novo): institution,
    delegation, conference, career, leadership, administration, degree, responsible, represent.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 20 IN CLASS (mesmo tema: uma auto-apresentacao formal
    para a plenaria em Seul; mesmo vocab; mesma gramatica: as quatro partes da apresentacao)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um onclick.
    Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (jornada de 20 aulas): esta e a ultima aula da meta; a aula celebra o percurso e da a
    ela uma apresentacao formal PROPRIA, pronta para Seul; frase-identidade no survival card.
"""
import random

random.seed(20)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo real)
VOCAB = [
    ("Honored", "feeling proud and grateful for a special moment or invitation",
     "I am honored to represent my university at this conference."),
    ("Expertise", "the special knowledge or skill you get from many years of work",
     "My expertise is in institutional leadership and higher education."),
    ("Partnership", "a relationship where two groups work together for a shared goal",
     "I hope this visit will start a strong partnership between our universities."),
    ("Opportunity", "a good chance or moment to do something useful or important",
     "This conference is a real opportunity to meet new colleagues."),
    ("Exchange", "to give something and receive something back, like ideas or information",
     "I am looking forward to exchanging ideas with you."),
    ("Productive", "creating good and useful results",
     "I hope our meeting will be productive."),
    ("Contribution", "something useful that you give or add to a project or a group",
     "I want to make a real contribution to this delegation."),
    ("Collaboration", "the work of two or more people together to create something",
     "This project is a collaboration between four universities."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-20">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 20 -- Pre-class</div>')
w('      <h3>Presenting Yourself and Your Work -- Formal Self-Introduction and Institutional Pitch</h3>')
w('      <div class="lesson-desc">The capstone of the block. Read a <strong>model</strong> of a formal self-introduction '
  'and learn the <strong>four moves</strong> that carry it: <strong>open and thank</strong> (Good afternoon. Thank you for '
  'having me. It is an honor to be here.), <strong>role and institution</strong> (I am a professor and institutional leader '
  'at...), <strong>experience and expertise</strong> (I have worked in higher education for over twenty years. My expertise '
  'is in...), and a <strong>forward-looking close</strong> (I am looking forward to exchanging ideas. / I hope this visit '
  'will lead to a productive partnership.). Key words: honored, expertise, partnership, opportunity, exchange, productive, '
  'contribution, collaboration. Recycled expression: "I am looking forward to..." Idiom reactivated: "I wear many hats."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="20" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="20">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words for presenting yourself and your work.</p>')
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
w('      <div class="match-grid" id="match-l20">')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the model introduction and answer the questions.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>Maria Clara stands up at the conference in Seoul. First, she <strong>opens</strong>: "Good afternoon, and thank you '
  'for having me. It is a true <strong>honor</strong> to be here." Then she gives her <strong>role</strong>: "I am a professor '
  'and an institutional leader at a federal university in Brazil." Next, her <strong>experience</strong>: "I have worked in '
  'higher education for more than twenty years, and my <strong>expertise</strong> is in institutional leadership." '
  'Finally, she <strong>closes</strong> looking forward: "For me, this conference is an <strong>opportunity</strong> to make a '
  '<strong>contribution</strong> and to learn from others. I am looking forward to <strong>exchanging</strong> ideas with you, '
  'and I hope this visit will lead to a <strong>productive</strong> <strong>partnership</strong> and a long '
  '<strong>collaboration</strong> between our institutions. Thank you very much."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Maria Clara starts with "Thank you for having me. It is an honor to be here." What is this?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The <strong>opening</strong> move: she greets and thanks the room.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The closing move: she is saying goodbye.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A question for the audience.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. She says "I have worked in higher education for more than twenty years." This is her:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Opening greeting.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> <strong>Experience</strong>: how long she has worked and her expertise.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A request for a different room.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "I am looking forward to exchanging ideas with you." Which move is this?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Her role and institution.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The <strong>forward-looking close</strong>: she opens the door to a partnership.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Her name and her job.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which order is correct for a formal introduction?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Experience &#8594; open &#8594; close &#8594; role.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Open &#8594; role &#8594; experience &#8594; close.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Close &#8594; experience &#8594; role &#8594; open.</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Four Moves of a Formal Introduction</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A formal self-introduction has <strong>four moves</strong>, always in the same order. Learn the order, and you can introduce yourself in any room in the world.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Move</th><th style="padding:.7rem;text-align:left">What you do</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. Open</td>'
  '<td style="padding:.6rem">Greet the room and thank them</td>'
  '<td style="padding:.6rem"><strong>Good afternoon. Thank you for having me here today.</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. Role</td>'
  '<td style="padding:.6rem">Say who you are and where you work</td>'
  '<td style="padding:.6rem"><strong>I am a professor and institutional leader at a federal university.</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. Experience</td>'
  '<td style="padding:.6rem">Share how long, and your expertise</td>'
  '<td style="padding:.6rem"><strong>I have worked in higher education for over twenty years.</strong></td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">4. Close</td>'
  '<td style="padding:.6rem">Look forward and open a partnership</td>'
  '<td style="padding:.6rem"><strong>I am looking forward to exchanging ideas with you.</strong></td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"I am working here since twenty years."</strong> or <strong>"My expertise are..."</strong> or '
  '<strong>"I look forward to exchange ideas."</strong>. The correct forms are <strong>I have worked here for twenty years</strong>, '
  '<strong>My expertise is...</strong> (singular), and <strong>I am looking forward to exchanging ideas</strong> (with -ing). '
  'You do not need perfect English &mdash; you need a clear, calm introduction that is yours.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("honored", "Hint: feeling proud and grateful for a special moment",
     "I am honored to be at this conference.",
     '"I am ', ' to be at this conference."'),
    ("expertise", "Hint: your special knowledge from many years of work",
     "My expertise is in institutional leadership.",
     '"My ', ' is in institutional leadership."'),
    ("forward", "Hint: looking ___ to = thinking with hope about the future",
     "I am looking forward to exchanging ideas with you.",
     '"I am looking ', ' to exchanging ideas with you."'),
    ("partnership", "Hint: two groups working together for a shared goal",
     "I hope this visit will start a productive partnership.",
     '"I hope this visit will start a productive ', '."'),
    ("opportunity", "Hint: a good chance to do something important",
     "This conference is a great opportunity to learn.",
     '"This conference is a great ', ' to learn."'),
    ("collaboration", "Hint: the work of two or more people together",
     "Good things happen through collaboration.",
     '"Good things happen through ', '."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence from a formal introduction. Tap Listen to hear the full sentence.</p>')
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
    (1, "Good afternoon. Thank you for having me here today."),
    (2, "My name is Maria Clara, and I am a professor and institutional leader."),
    (3, "I have worked in higher education for more than twenty years."),
    (4, "I am looking forward to exchanging ideas with you."),
    (5, "Thank you very much. I am happy to answer any questions."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Introduction in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the sentences in order, from the opening to the close of a formal introduction.</p>')
w('      <div class="order-container" id="order-l20">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l20\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l20\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l20\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l20\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Good afternoon. Thank you for having me here today.",
    "My name is Maria Clara, and it is an honor to be here.",
    "I have worked in higher education for more than twenty years.",
    "I am looking forward to exchanging ideas with you.",
    "After twenty lessons, I can present myself to the world, in English.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. There is no wrong way to try &mdash; the last one is your phrase: say it out loud, and mean it.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of a formal introduction.</p>')
w('      <div class="quiz-item"><div class="quiz-question">You stand up at the plenary. You open with:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Hi. So, yeah, I am here."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Good afternoon. Thank you for having me. It is an honor to be here."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Let\'s finish quickly, I am busy."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to say who you are and where you work. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am work in a university."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am a professor and institutional leader at a federal university in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My work is a professor since."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to share your experience. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have worked in higher education for more than twenty years. My expertise is in leadership."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am working here since twenty years. My expertise are leadership."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I work many time. Leadership my expertise."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to close your introduction, looking forward. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I look forward to exchange ideas and I want partnership."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am looking forward to exchanging ideas, and I hope this visit will lead to a productive partnership."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Okay, that is all. Bye."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Someone asks what you hope to get from the conference. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I don\'t know, nothing special."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am looking forward to exchanging ideas and making a real contribution."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You ask me too much question."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record your full self-introduction. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. This is your Block 4 production. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Imagine you are at the opening of the conference in Seoul. Give your whole formal '
  '<strong>self-introduction</strong>, in four moves: <strong>open and thank</strong> the room ("It is an <strong>honor</strong> '
  'to be here."), give your <strong>role and institution</strong>, share your <strong>experience</strong> and your '
  '<strong>expertise</strong>, and <strong>close</strong> looking forward ("I am looking forward to <strong>exchanging</strong> '
  'ideas... I hope for a <strong>productive</strong> <strong>partnership</strong>."). Take sixty to ninety seconds, and stay in '
  'English. This is you, speaking for your institution.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-20"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 20</h4>')
for i, en in enumerate(SPEECH, 1):
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
