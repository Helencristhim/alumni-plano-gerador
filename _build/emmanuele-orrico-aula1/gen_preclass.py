#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; grammar tip, hints, quiz e survival em ingles).
    O portugues so sobrevive onde a aluna NAO ve (planejamento / data-teacher).
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula IN CLASS (mesmo tema/gramatica/vocab)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be": a gramatica entra como o CODIGO do trabalho dela
    (I work at / I manage / I am responsible for) e "I am responsible for" e tratado
    como FRASE PRONTA, nao como conjugacao.
"""
import random

random.seed(33)

OUT = 'preclass.html'

# (word, definicao em ingles simples (A2) -- usada no vocab card E no matching, exemplo)
# REGRA 13: A2 => a definicao EN SUBSTITUI a traducao PT. Zero portugues aqui.
VOCAB = [
    ("Pharmaceutical company", "a company that makes medicines",
     "Sanofi is a pharmaceutical company."),
    ("Immunology", "the study of how the body fights disease",
     "I work in immunology."),
    ("National manager", "the person who leads a business in the whole country",
     "I am the national demand manager for Brazil."),
    ("Field team", "the people who visit doctors in hospitals and clinics",
     "My field team visits doctors every week."),
    ("Global meeting", "a meeting with colleagues from other countries",
     "We have a global meeting every month."),
    ("Results", "the numbers that show how the business is going",
     "I present the results to the Global team."),
    ("Launch", "when a company puts a new medicine on the market",
     "The launch starts in September."),
    ("Disease area", "a group of illnesses that one team takes care of",
     "Asthma is one of my disease areas."),
    ("To be responsible for", "to take care of something as part of your job",
     "I am responsible for eight disease areas."),
    ("To manage", "to lead a team or a business",
     "I manage the immunology portfolio in Brazil."),
]

LISTEN_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-1">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 01 -- Pre-class</div>')
w('      <h3>Diagnostic + First Words -- Who Is Emmanuele Orrico?</h3>')
w('      <div class="lesson-desc">Introduce yourself and describe your job on a call with the Sanofi Global team. '
  'Key words: pharmaceutical company, immunology, national manager, field team, global meeting, results, launch, '
  'disease area, to be responsible for, to manage. Structures: I work at... / I manage... / I am responsible for... '
  '(facts about your job), the -s in my team visits, and the ready phrases to ask people to repeat or to speak more slowly.</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words you use at work every day.</p>')
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
w('      <div class="match-grid" id="match-l1">')
all_defs = [d for _, d, _ in VOCAB]
for word, dfn, _ex in VOCAB:
    opts = all_defs[:]
    # REGRA 24: embaralhar as opcoes -- ordem DIFERENTE em cada linha
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
w('        <p>Emmanuele Orrico <strong>works</strong> at Sanofi, a <strong>pharmaceutical company</strong>. '
  'She <strong>is</strong> the national demand <strong>manager</strong> in Brazil, and she <strong>manages</strong> '
  'the <strong>immunology</strong> portfolio. "I <strong>am responsible for</strong> eight <strong>disease areas</strong>," '
  'she says. "Asthma, COPD and atopic dermatitis, for example." Her <strong>field team</strong> <strong>visits</strong> '
  'doctors every week, and the team <strong>talks</strong> about the patients and the treatments. Every month, '
  'Emmanuele <strong>presents</strong> the <strong>results</strong> in a <strong>global meeting</strong> with '
  'colleagues from France, Canada and Japan. She <strong>does not work</strong> in oncology, and she '
  '<strong>does not manage</strong> the factory. She <strong>manages</strong> the demand. In September, the '
  'company <strong>starts</strong> a new <strong>launch</strong>, and in August the Global team <strong>visits</strong> '
  'Brazil. "I <strong>present</strong> the <strong>results</strong>, the challenges and the opportunities," she says.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why do we say "My field team visits doctors" and not "My field team visit doctors"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because "my team" is ONE group (like he / she / it) &mdash; so the verb takes -s.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the action is happening right now, at this moment.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the action happened in the past.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "I am responsible for eight disease areas." In this sentence, "am responsible for" is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> An action she is doing right now.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A READY PHRASE to say what you take care of at work &mdash; use the whole block, do not build it.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A way to talk about the future.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "She does not work in oncology." What does this sentence say?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She worked in oncology in the past.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Oncology is NOT part of her job &mdash; the negative uses does not (doesn\'t) + verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She is going to start working in oncology.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her job is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She work in Sanofi and responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She works at Sanofi and she is responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She works in Sanofi and she responsible for eight disease areas."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Talking About Your Job: I work at / I manage / I am responsible for</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The code that opens every call with the Global team: how to say who you are and what you take care of.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I / you / we / they + verb</td>'
  '<td style="padding:.6rem">Facts about your job.</td>'
  '<td style="padding:.6rem">I <strong>work</strong> at Sanofi.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">he / she / my team + verb <strong>+ s</strong></td>'
  '<td style="padding:.6rem">The SAME idea, but for one person or ONE group. This -s is easy to forget.</td>'
  '<td style="padding:.6rem">My team <strong>visits</strong> doctors.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">READY PHRASE: I am responsible for + thing</td>'
  '<td style="padding:.6rem">There is nothing to build. Take the whole block and use it.</td>'
  '<td style="padding:.6rem">I <strong>am responsible for</strong> eight disease areas.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative: don\'t / doesn\'t + verb</td>'
  '<td style="padding:.6rem">To say what is NOT your job.</td>'
  '<td style="padding:.6rem">I <strong>don\'t work</strong> in oncology.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question: Do / Does + person + verb?</td>'
  '<td style="padding:.6rem">To ASK your colleague something (not only to answer).</td>'
  '<td style="padding:.6rem"><strong>Do you work</strong> in immunology?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">at vs in</td><td style="padding:.6rem" colspan="2">'
  'A company takes <strong>at</strong>: "I work <strong>at</strong> Sanofi". An area or a country takes <strong>in</strong>: '
  '"I work <strong>in</strong> immunology", "I work <strong>in</strong> Brazil".</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Careful:</strong> '
  '"responsible" is not a verb, so "I responsible for..." does not exist in English. Always say the full block: '
  '<strong>I am responsible for...</strong> &mdash; one piece, no thinking. And a company always takes <strong>at</strong>: '
  '"I work <strong>at</strong> Sanofi", never "in Sanofi".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("work", "Hint: a fact about your job &mdash; simple verb after I, no -s",
     "I work at Sanofi, in Brazil.",
     '"I ', ' at Sanofi, in Brazil."'),
    ("am responsible for", "Hint: the READY PHRASE to say what you take care of",
     "I am responsible for eight disease areas.",
     '"I ', ' eight disease areas."'),
    ("visits", "Hint: my field team is ONE group &mdash; the verb takes -s",
     "My field team visits doctors every week.",
     '"My field team ', ' doctors every week."'),
    ("manage", "Hint: after I, the verb stays simple",
     "I manage the immunology portfolio in Brazil.",
     '"I ', ' the immunology portfolio in Brazil."'),
    ("don't work", "Hint: the negative after I &mdash; don\'t + verb",
     "I don't work in oncology.",
     '"I ', ' in oncology."'),
    ("at", "Hint: a company always takes this preposition",
     "I work at Sanofi.",
     '"I work ', ' Sanofi."'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence.</p>')
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
    (1, "Thank the Global team for the call and confirm everyone can hear you."),
    (2, "Introduce yourself: your name and the company you work at."),
    (3, "Describe your role: what you manage and what you are responsible for."),
    (4, "Talk about your field team and the disease areas you take care of."),
    (5, "Confirm that you present the results to the Global team in August."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Global Call in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a first call with the Global team in the correct order.</p>')
w('      <div class="order-container" id="order-l1">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l1\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l1\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "My name is Emmanuele Orrico, and I work at Sanofi.",
    "I am the national demand manager for immunology.",
    "I am responsible for eight disease areas.",
    "My field team visits doctors every week.",
    "Sorry, could you repeat that, please?",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that open any meeting with the Global team.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each situation.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc, from the Global team, asks: "So, what do you do at Sanofi?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I do the immunology things in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am the national demand manager, and I manage the immunology portfolio in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I responsible for the immunology in Sanofi."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "Which disease areas are you responsible for?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am responsible for eight disease areas: asthma, COPD and atopic dermatitis, for example."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Eight disease areas is my responsible."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to talk about your field team. Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "My field team visits doctors every week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "My field team visit doctors every week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My field team is visit doctors every week."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Someone asks if you take care of oncology. You do NOT. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I no work in oncology."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I not work in oncology."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "I don\'t work in oncology. I work in immunology."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The question was too fast and you did NOT understand. The most professional move is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Stay quiet and hope that someone changes the subject.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, could you repeat that, please?" &mdash; or "Could you speak more slowly, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Say sorry for your English and stop talking in the meeting.</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for 60 seconds, with no script. This recording is your BASELINE: we will listen to it again in lesson 17.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">You are starting a video call with the Sanofi Global team. Introduce yourself: '
  'your name and your company (I work at...), your role (I am the national demand manager), what you take care of '
  '(I am responsible for...), and what your field team does every week (My team visits...). Finish with one sentence '
  'about August, when the Global team visits Brazil. Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-1"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
SURVIVAL = [
    "My name is Emmanuele Orrico, and I work at Sanofi.",
    "I am the national demand manager for immunology.",
    "I am responsible for eight disease areas.",
    "Sorry, could you repeat that, please?",
    "Let me think for a second.",
]
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 1</h4>')
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
