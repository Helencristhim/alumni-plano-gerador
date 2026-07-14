#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 2 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ~80% bilingue (definicao EN + traducao PT)
  - REGRA 22: ZERO palavra da aula 1 como vocab NOVO (nada de results / launch /
    immunology / field team / global meeting / disease area / to manage...)
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 2 IN CLASS (mesma rotina, mesmo vocab,
    mesma gramatica: present simple + always/usually/often/sometimes/never)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be": a gramatica entra pela agenda REAL dela.
"""
import random

random.seed(2)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Schedule", "the plan of your week: what happens and when",
     "agenda / cronograma",
     "My schedule is full on Mondays."),
    ("Report", "a document with numbers and information about the business",
     "relat&#243;rio",
     "I read the field reports every Tuesday."),
    ("Field visit", "a day outside the office, with the team, visiting doctors",
     "visita de campo",
     "I do a field visit twice a month."),
    ("Medical rep", "the person who talks to doctors about our medicines",
     "representante m&#233;dico",
     "Every medical rep visits ten doctors a week."),
    ("Demand plan", "the plan that says how much medicine the market needs",
     "plano de demanda",
     "We review the demand plan every Monday."),
    ("Headquarters", "the main office of the company",
     "matriz / sede",
     "Our headquarters are in Paris."),
    ("To attend", "to go to a meeting or a call",
     "participar de (uma reuni&#227;o)",
     "I attend the global call every Thursday."),
    ("To review", "to look at something again and check it",
     "revisar / analisar",
     "I review the numbers before the meeting."),
    ("To prepare", "to get something ready before it happens",
     "preparar",
     "I prepare the presentation on Fridays."),
    ("To travel", "to go to another city for work",
     "viajar",
     "I sometimes travel to other cities."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-2">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Aula 02 -- Pre-class</div>')
w('      <h3>Your Day and Your Work Routine -- A Week at Sanofi Brazil</h3>')
w('      <div class="lesson-desc">Descrever a sua semana t&#237;pica para o time Global: segunda com o plano de demanda, '
  'a visita de campo, a call global de quinta, os relat&#243;rios de sexta. Key words: schedule, report, field visit, '
  'medical rep, demand plan, headquarters, to attend, to review, to prepare, to travel. Structures: present simple '
  'para rotina + always / usually / often / sometimes / never (sempre ANTES do verbo), a negativa I don&#39;t travel '
  'e a pergunta Do you...? Express&#227;o da aula: "It is part of the job."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as dez palavras que est&#227;o na sua agenda toda semana &mdash; agora em ingl&#234;s.</p>')
w('      <div class="vocab-cards">')
for word, dfn, pt, ex in VOCAB:
    w(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{dfn} ({pt})</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{word}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.2 (REGRA 24)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>')
w('      <div class="match-grid" id="match-l2">')
all_defs = [d for _, d, _, _ in VOCAB]
for word, dfn, _pt, _ex in VOCAB:
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>Emmanuele <strong>always starts</strong> her week with numbers. On Monday, she <strong>reviews</strong> the '
  '<strong>demand plan</strong> with her team and she <strong>checks</strong> the <strong>schedule</strong> for the week. '
  'On Tuesday, the <strong>medical reps</strong> <strong>usually send</strong> their <strong>reports</strong>. On Wednesday, '
  'she <strong>often does</strong> a <strong>field visit</strong> and <strong>visits</strong> doctors with a rep. On Thursday, '
  'she <strong>always attends</strong> the global call with <strong>headquarters</strong> in Paris. On Friday, she '
  '<strong>prepares</strong> the reports for the next week. She <strong>sometimes travels</strong> to other cities, but she '
  '<strong>never travels</strong> on Fridays. She <strong>does not schedule</strong> meetings on Friday, and she '
  '<strong>doesn&#39;t work</strong> at the weekend. "Monday is never quiet," she says. "<strong>It is part of the job</strong>."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Por que dizemos "I always review" e n&#227;o "I review always"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque always, usually, often, sometimes e never v&#234;m ANTES do verbo principal.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque em ingl&#234;s a palavra de frequ&#234;ncia vem sempre no fim da frase.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque a a&#231;&#227;o est&#225; acontecendo agora, neste momento.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "The medical reps usually send their reports." Se a frase falar de UM rep, o que muda?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Nada muda: "One rep usually send their reports."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> O verbo ganha -s: "One rep usually sends his reports." (mesma regra do my team visits, da aula 1)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> O verbo vai para o passado.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "She never travels on Fridays." O que essa frase diz?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Que ela viaja de vez em quando na sexta.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Zero sextas: never = 0%. E repare que a frase N&#195;O leva don&#39;t &mdash; never j&#225; &#233; a negativa.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Que ela viajou na sexta passada.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her week is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She attend always the global call on Thursday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She always attends the global call on Thursday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She always attend the global call on Thursday."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Falando da sua semana: always, usually, often, sometimes, never</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como dizer O QUE voc&#234; faz e COM QUE FREQU&#202;NCIA (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I / we / they + <strong>always, usually, often, sometimes, never</strong> + verbo</td>'
  '<td style="padding:.6rem">A palavra de frequ&#234;ncia vem ANTES do verbo. Em portugu&#234;s ela vem depois ("eu reviso sempre") &mdash; em ingl&#234;s, N&#195;O.</td>'
  '<td style="padding:.6rem">I <strong>always review</strong> the demand plan.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">he / she / my team + verbo <strong>+ s</strong></td>'
  '<td style="padding:.6rem">Uma pessoa ou UM time: o verbo ganha -s (a mesma regra da aula 1).</td>'
  '<td style="padding:.6rem">My team <strong>usually sends</strong> the reports.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa: I <strong>don&#39;t</strong> / she <strong>doesn&#39;t</strong> + verbo</td>'
  '<td style="padding:.6rem">Para dizer o que N&#195;O est&#225; na sua semana. Aten&#231;&#227;o: com <strong>never</strong> N&#195;O se usa don&#39;t (never j&#225; nega).</td>'
  '<td style="padding:.6rem">I <strong>don&#39;t travel</strong> on Fridays.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa: <strong>Do / Does</strong> + pessoa + verbo?</td>'
  '<td style="padding:.6rem">Para PERGUNTAR ao colega sobre a semana dele (e n&#227;o s&#243; responder).</td>'
  '<td style="padding:.6rem"><strong>Do you travel</strong> every month?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">How often? / Quando?</td><td style="padding:.6rem" colspan="2">'
  'always (100%) &middot; usually &middot; often &middot; sometimes &middot; never (0%). As express&#245;es de tempo v&#227;o no come&#231;o ou no fim: '
  '<strong>every week</strong>, <strong>on Mondays</strong>, <strong>twice a month</strong>.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> '
  'em portugu&#234;s dizemos "eu vou sempre &#224; call", com a palavra DEPOIS do verbo. Por isso sai "I go always to the call", '
  'que em ingl&#234;s soa errado. O lugar &#233; sempre ANTES: <strong>I always go</strong>. E a pergunta precisa do '
  '<strong>Do</strong> na frente: "Do you attend the call?", nunca s&#243; "You attend the call?".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("always review", "Dica: a palavra de frequ&#234;ncia (100%) vem ANTES do verbo",
     "On Monday, I always review the demand plan.",
     '"On Monday, I ', ' the demand plan."'),
    ("usually send", "Dica: eles (they) &mdash; verbo sem -s, com a palavra de frequ&#234;ncia na frente",
     "The medical reps usually send their reports on Tuesday.",
     '"The medical reps ', ' their reports on Tuesday."'),
    ("attend", "Dica: o verbo de ir a uma reuni&#227;o ou call",
     "I attend the global call every Thursday.",
     '"I ', ' the global call every Thursday."'),
    ("don't travel", "Dica: negativa depois de I &mdash; don&#39;t + verbo",
     "I don't travel on Fridays.",
     '"I ', ' on Fridays."'),
    ("prepare", "Dica: deixar pronto antes que aconte&#231;a",
     "On Friday, I prepare the reports for the next week.",
     '"On Friday, I ', ' the reports for the next week."'),
    ("Do you attend", "Dica: pergunta em ingl&#234;s come&#231;a com Do",
     "Do you attend the global call every week?",
     '"', ' the global call every week?"'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase. Toque em Listen para ouvir a frase inteira.</p>')
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
    (1, "Monday: review the demand plan with the team."),
    (2, "Tuesday: read the field reports from the medical reps."),
    (3, "Wednesday: do a field visit and see doctors with a rep."),
    (4, "Thursday: attend the global call with headquarters in Paris."),
    (5, "Friday: prepare the reports for the next week."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Week in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os dias de uma semana t&#237;pica na Sanofi na ordem correta.</p>')
w('      <div class="order-container" id="order-l2">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l2\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    ("On Monday, I always review the demand plan with my team.",
     "Na segunda, eu sempre reviso o plano de demanda com o meu time."),
    ("I often do a field visit with a medical rep.",
     "Eu frequentemente fa&#231;o uma visita de campo com um representante m&#233;dico."),
    ("I attend the global call every Thursday.",
     "Eu participo da call global toda quinta-feira."),
    ("I sometimes travel, but I never travel on Fridays.",
     "Eu &#224;s vezes viajo, mas nunca viajo &#224;s sextas."),
    ("It is part of the job.",
     "Faz parte do trabalho."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases que respondem "what does your week look like?".</p>')
for en, pt in SPEECH:
    w(f'      <div class="speech-card" data-phrase="{en}">')
    w(f'        <div class="speech-phrase">{en}</div>')
    w(f'        <div class="speech-translation">{pt}</div>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma reuni&#227;o com o time Global.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc pergunta: "What do you do on Mondays?" Voc&#234; responde:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I review always the demand plan."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "On Monday, I always review the demand plan with my team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Monday I am review the demand plan."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Ele pergunta: "How often do you travel?" A melhor resposta &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I travel sometimes, but Friday no."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I sometimes travel to other cities, but I never travel on Fridays."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I don&#39;t never travel on Fridays."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; quer falar do que o seu time faz toda semana. Qual frase est&#225; correta?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "My team usually sends the field reports on Tuesday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "My team send usually the field reports on Tuesday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My team is send the field reports on Tuesday."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; quer PERGUNTAR ao Marc se ele participa da call de segunda. Voc&#234; diz:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You attend the Monday call?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Attend you the Monday call?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Do you attend the Monday call?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A semana foi pesada e algu&#233;m do Global comenta isso. A resposta profissional e natural &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, my work is very bad this week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Yes, it was a busy week. It is part of the job."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I am part of the job."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 90 segundos, sem script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Marc Dubois asks you to describe your typical week at Sanofi. Start with "Every week, I..." and '
  'talk about five days: what you always do, what you usually do, what you often do, what you sometimes do, and what you never do. '
  'Use the words from this lesson (demand plan, field visit, medical rep, reports, global call, headquarters). Finish with the '
  'expression of the lesson: "It is part of the job." Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-2"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
SURVIVAL = [
    ("On Monday, I always review the demand plan with my team.",
     "Na segunda, eu sempre reviso o plano de demanda com o meu time."),
    ("I often do a field visit with a medical rep.",
     "Eu frequentemente fa&#231;o uma visita de campo com um representante m&#233;dico."),
    ("I attend the global call every Thursday.",
     "Eu participo da call global toda quinta-feira."),
    ("I sometimes travel, but I never travel on Fridays.",
     "Eu &#224;s vezes viajo, mas nunca viajo &#224;s sextas."),
    ("It is part of the job.",
     "Faz parte do trabalho."),
]
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 2</h4>')
for i, (en, pt) in enumerate(SURVIVAL, 1):
    w(f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
      f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
w('    </div>')
w('')
w('  </div>')
w('</div>')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {OUT} ({len(VOCAB)} vocab, {len(BLANKS)} blanks, {len(SPEECH)} speech cards)')
