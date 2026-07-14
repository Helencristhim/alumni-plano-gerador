#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 3 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ZERO portugues na tela da aluna. Definicao em
    ingles simples no lugar da traducao; matching palavra EN <-> definicao EN; grammar tip
    em ingles; hint em ingles; sem .speech-translation; sem .sp-pt. O portugues so
    sobrevive onde a aluna NAO ve (planejamento / data-teacher).
  - REGRA 22: ZERO palavra das aulas 1 e 2 como vocab NOVO. Fora, de proposito:
    results / launch / immunology / field team / global meeting / disease area / to manage /
    schedule / report / field visit / medical rep / demand plan / headquarters / to attend /
    to review / to prepare / to travel
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 3 IN CLASS (mesmo tema: o business review do
    trimestre passado; mesmo vocab; mesma gramatica: past simple regular + 5 irregulares)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be": "It was a difficult quarter" entra como FRASE PRONTA.
"""
import random

random.seed(3)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), exemplo)
VOCAB = [
    ("Quarter", "a period of three months in the business year",
     "Last quarter was very busy."),
    ("Target", "the number the company wants you to reach",
     "We had a high target in dermatology."),
    ("Challenge", "something difficult in the business",
     "We faced a challenge with market access."),
    ("Opportunity", "a chance to grow the business",
     "The private market is a big opportunity."),
    ("Growth", "when the numbers go up",
     "The growth came from the private market."),
    ("To achieve", "to reach the number you needed",
     "We achieved our target in dermatology."),
    ("To exceed", "to go above the number you needed",
     "In Q2, the team exceeded the target."),
    ("To miss", "to not reach the number you needed",
     "We missed the target in asthma."),
    ("Market access", "when a medicine is approved and paid for, so patients can get it",
     "Market access was slow in the public market."),
    ("Prescription volume", "how many prescriptions the doctors write for your medicine",
     "Prescription volume went up in June."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-3">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 03 -- Pre-class</div>')
w('      <h3>What Happened Last Quarter? -- Reporting Past Results</h3>')
w('      <div class="lesson-desc">Tell the Global team what happened last quarter: the target you achieved in dermatology, '
  'the target you missed in asthma, the market access challenge, and the growth in the private market. Key words: quarter, target, '
  'challenge, opportunity, growth, to achieve, to exceed, to miss, market access, prescription volume. Structures: past simple '
  '&mdash; regular verbs with -ed (achieved, missed, presented) and the five irregular verbs of the business review (went, had, gave, '
  'met, came), the negative didn&#39;t achieve, and the time expressions last quarter / in April / two months ago. '
  'Phrase of the lesson: "Once in a while, we have unexpected results."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words you see in every business review.</p>')
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
w('      <div class="match-grid" id="match-l3">')
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
w('        <p>Last <strong>quarter</strong> was busy, but Emmanuele <strong>had</strong> good news for Paris. In April, she '
  '<strong>presented</strong> the plan to the Global team. In May, her team <strong>met</strong> sixty new doctors in the private '
  'market. In June, <strong>prescription volume</strong> <strong>went</strong> up, and the <strong>growth</strong> '
  '<strong>came</strong> from the private market. In dermatology, the team <strong>exceeded</strong> the <strong>target</strong>: '
  'they <strong>achieved</strong> one hundred and eight percent. In asthma, they <strong>missed</strong> the target. The '
  '<strong>challenge</strong> was <strong>market access</strong> in the public market: the process <strong>was</strong> slow, and '
  'they <strong>didn&#39;t achieve</strong> the number. But Emmanuele also <strong>saw</strong> an <strong>opportunity</strong>. '
  '"<strong>Once in a while, we have unexpected results</strong>," she says. "Then we learn, and we go again."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why do "achieved", "missed" and "presented" end in -ED?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because the action is FINISHED: last quarter is over. Most verbs take -ed in the past.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the action is happening now, at this moment.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the subject is "the team" (only one thing).</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "Her team met sixty new doctors." Why is it NOT "meeted"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the verb is in the present.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because meet is one of the five irregular verbs of the business review: meet &rarr; met. Irregular verbs do NOT take -ed.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the verb never changes after "team".</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "They didn&#39;t achieve the number." Why is it NOT "didn&#39;t achieved"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the sentence is about the future.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "achieve" is an irregular verb.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because the past is already inside <strong>did</strong>. After didn&#39;t, the verb goes back to normal &mdash; only ONE past mark in each sentence.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about last quarter is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Last quarter we exceed the target in dermatology."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Last quarter we didn&#39;t achieved the target in asthma."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Last quarter we exceeded the target in dermatology, and the growth came from the private market."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Saying what HAPPENED: -ed and the five irregular verbs</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A result is always in the past. This is how English says what is finished.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Verb + <strong>-ed</strong> (regular verbs)</td>'
  '<td style="padding:.6rem">The action is FINISHED. The quarter is over. The form is the SAME for I, you, we, they, he and she.</td>'
  '<td style="padding:.6rem">We <strong>achieved</strong> the target. / She <strong>presented</strong> the plan.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">The <strong>5 irregular verbs</strong> of the business review</td>'
  '<td style="padding:.6rem">They do NOT take -ed: they become a new word. There are only five &mdash; learn them and you cover most of the meeting.</td>'
  '<td style="padding:.6rem">go &rarr; <strong>went</strong> &middot; have &rarr; <strong>had</strong> &middot; give &rarr; <strong>gave</strong> &middot; meet &rarr; <strong>met</strong> &middot; come &rarr; <strong>came</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative: <strong>didn&#39;t</strong> + NORMAL verb</td>'
  '<td style="padding:.6rem">Only ONE past mark in each sentence, and it is already inside <strong>did</strong>. So the verb goes back to normal.</td>'
  '<td style="padding:.6rem">We <strong>didn&#39;t achieve</strong> the target. (never "didn&#39;t achieved")</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">When? (time expressions)</td>'
  '<td style="padding:.6rem" colspan="2"><strong>last</strong> quarter &middot; <strong>last</strong> week &middot; <strong>in</strong> April &middot; two months <strong>ago</strong> ("ago" comes AFTER the time, never before) &middot; yesterday</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Ready-made phrase: <strong>It was a difficult quarter.</strong></td>'
  '<td style="padding:.6rem">Nothing to build, nothing to change. It is ONE block: take it and use it.</td>'
  '<td style="padding:.6rem"><strong>It was</strong> a good quarter for dermatology.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Careful (common mistake):</strong> '
  'in your language, the past is already inside the verb. That is why people say "we didn&#39;t achieved" &mdash; the past TWICE. '
  'In English, the past is inside <strong>did</strong>, and the verb goes back to normal: <strong>we didn&#39;t achieve</strong>. '
  'The opposite also happens: "last quarter" already says it is the past, so people forget the -ED and say "last quarter we exceed". '
  'In English, the VERB has to show it too: <strong>we exceeded</strong>.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("exceeded", "Hint: to go above the target &mdash; regular verb, with -ed",
     "Last quarter, we exceeded the target in dermatology.",
     '"Last quarter, we ', ' the target in dermatology."'),
    ("missed", "Hint: to NOT reach the target &mdash; regular verb, with -ed",
     "We missed the target in asthma.",
     '"We ', ' the target in asthma."'),
    ("met", "Hint: one of the five irregular verbs &mdash; the past of meet",
     "In May, my team met sixty new doctors.",
     '"In May, my team ', ' sixty new doctors."'),
    ("came", "Hint: one of the five irregular verbs &mdash; the past of come",
     "The growth came from the private market.",
     '"The growth ', ' from the private market."'),
    ("didn't achieve", "Hint: negative &mdash; didn&#39;t + NORMAL verb (no -ed)",
     "We didn't achieve the target in the public market.",
     '"We ', ' the target in the public market."'),
    ("had", "Hint: one of the five irregular verbs &mdash; the past of have",
     "Two months ago, we had a challenge with market access.",
     '"Two months ago, we ', ' a challenge with market access."'),
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
    (1, "In April, we started the quarter with a clear target."),
    (2, "In May, my team met sixty new doctors in the private market."),
    (3, "In June, prescription volume grew and we exceeded the target in dermatology."),
    (4, "At the end of the quarter, we missed the target in asthma, because market access was slow."),
    (5, "Last week, I presented the results to the Global team."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Quarter in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the events of last quarter in the correct order.</p>')
w('      <div class="order-container" id="order-l3">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l3\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Last quarter, we achieved our target in dermatology.",
    "We missed the target in asthma, because market access was slow.",
    "The growth came from the private market.",
    "Once in a while, we have unexpected results.",
    "Let me check the number and come back to you.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of your August presentation. Watch the -ED: achiev<strong>ed</strong> = one sound; exceed<strong>ed</strong> = one extra syllable.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment of the business review with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc asks: "How was last quarter in dermatology?" You answer:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Last quarter we exceed the target."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Last quarter, we exceeded the target in dermatology. We achieved one hundred and eight percent."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Last quarter we are exceeding the target."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "Did you reach the target in asthma?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "No, we didn&#39;t achieved the target."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "No, sorry, sorry. It is my fault."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "No. We missed the target in asthma, because market access was slow."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "Where did the growth come from?" Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The growth came from the private market. My team met sixty new doctors."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The growth comed from the private market. My team meeted sixty new doctors."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The growth is come from the private market."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to say WHEN the challenge started (two months ago). You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Ago two months, market access was slow."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Two months ago, market access was slow."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Before two months, market access was slow."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The Global VP says the numbers go up and down every quarter. The natural, professional answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, sometimes my work is very bad."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Yes. Once in a while, we have unexpected results. Then we learn, and we go again."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I am unexpected results."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for two minutes, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">The Global team gives you two minutes at the quarterly business review. Tell them what happened '
  'last quarter at Sanofi Brazil, in this order: first the target (what you achieved and what you exceeded), then the challenge (what '
  'you missed, and why &mdash; use "because"), and finally the opportunity (the new doctors, the private market, where the growth came '
  'from). Use the past: -ed verbs and your five irregulars (went, had, gave, met, came). Close with the expression of the lesson: '
  '"Once in a while, we have unexpected results." Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-3"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 3</h4>')
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
