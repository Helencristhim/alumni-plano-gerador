#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-2 do hub) da Lucimara — aula 2.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 2 IN CLASS (mesmo tema/gramatica/vocab).
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(2)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Terminal", "the part of the airport where you get on or off your plane",
     "terminal", "My flight to New York leaves from Terminal 3."),
    ("Carry-on", "the small bag you take with you inside the plane",
     "bagagem de m&#227;o", "I only travel with a carry-on when the trip is short."),
    ("Baggage claim", "the area where you pick up your suitcases after a flight",
     "esteira de bagagem", "Could you tell me where the baggage claim is?"),
    ("Check-in counter", "the desk where you show your ticket and leave your bags",
     "balc&#227;o de check-in", "The check-in counter closes one hour before the flight."),
    ("Boarding pass", "the document that lets you get on the plane",
     "cart&#227;o de embarque", "I've already downloaded my boarding pass."),
    ("Layover", "a short stop in another city between two flights",
     "escala / conex&#227;o", "I have a two-hour layover in Atlanta."),
    ("Customs", "the place where officers check what you are bringing into the country",
     "alf&#226;ndega", "I haven't gone through customs yet."),
    ("Front desk", "the reception of a hotel, where you check in",
     "recep&#231;&#227;o do hotel", "Please leave your bags at the front desk."),
    ("Concierge", "the hotel employee who helps guests with restaurants, taxis and tickets",
     "concierge (funcion&#225;rio que orienta os h&#243;spedes)",
     "The concierge has already booked a table for us."),
    ("Itinerary", "the plan of your trip: dates, flights and hotels",
     "itiner&#225;rio / roteiro", "My itinerary says the fair starts at nine."),
    ("Confirmation number", "the code that proves you have a reservation",
     "n&#250;mero de confirma&#231;&#227;o / localizador",
     "I have my confirmation number here."),
    ("Jet lag", "the tired feeling after a long flight between time zones",
     "cansa&#231;o do fuso hor&#225;rio", "The jet lag always hits me at four in the morning."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-2">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 02 -- Pre-class</div>')
A('      <h3>Arriving and Settling In -- Airports, Hotels, and the First Hours in a New City</h3>')
A('      <div class="lesson-desc">Aterrissar em Nova York, passar pela imigra&#231;&#227;o e fazer o check-in do hotel &mdash; '
  'as primeiras horas, que ningu&#233;m ensina. Key words: terminal, carry-on, baggage claim, check-in counter, '
  'boarding pass, layover, customs, front desk, concierge, itinerary, confirmation number, jet lag. '
  'Structure: present perfect com <strong>just</strong> / <strong>already</strong> / <strong>yet</strong> '
  '("I&#8217;ve just landed", "I haven&#8217;t checked in yet") e o contraste com o past simple da narrativa '
  '("I landed at nine and took a cab").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras das primeiras horas em qualquer cidade nova.</p>')
A('      <div class="vocab-cards">')
for w, de, pt, ex in VOCAB:
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de} ({pt})</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a tradu&#231;&#227;o correta.</p>')
A('      <div class="match-grid" id="match-l2">')
pts = [v[2] for v in VOCAB]
for w, de, pt, ex in VOCAB:
    opts = pts[:]
    while True:
        random.shuffle(opts)
        if opts != pts:
            break
    o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
    A(f'        <div class="match-row" data-answer="{pt}"><span class="match-word" style="flex:0 0 150px">{w}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)"><option value="">Select...</option>{o}</select></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.3 — Grammar in Context ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto com calma, duas vezes, e depois responda &#224;s perguntas.</p>')
A('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
A('        <p>It is nine fifteen at night at <strong>Terminal</strong> Four. Lucimara <strong>has just landed</strong> in New York. '
  'She <strong>landed</strong> at nine, <strong>walked</strong> to passport control and <strong>answered</strong> two questions: '
  '"Business or pleasure?" and "How long are you staying?" &mdash; that part <strong>is</strong> over, and the past simple '
  '<strong>tells</strong> the story. Now she <strong>is</strong> at <strong>baggage claim</strong>. Her suitcase '
  '<strong>has already arrived</strong> on belt six; her <strong>carry-on</strong> <strong>has never left</strong> her shoulder. '
  'She <strong>has not gone</strong> through <strong>customs</strong> <strong>yet</strong>, but she <strong>has</strong> nothing to '
  'declare. At the hotel, the <strong>front desk</strong> only <strong>needs</strong> her <strong>confirmation number</strong>, '
  'because she <strong>has already completed</strong> the online check-in. One problem: the room <strong>is not</strong> ready '
  '<strong>yet</strong>. So she <strong>leaves</strong> her bags, and the <strong>concierge</strong> '
  '<strong>recommends</strong> a small restaurant two blocks away. At eleven she <strong>is</strong> finally in her room. '
  'She <strong>has not unpacked</strong> <strong>yet</strong> &mdash; and she <strong>will not</strong> tonight. The '
  '<strong>jet lag</strong> <strong>is going</strong> to wake her at four in the morning, and her '
  '<strong>itinerary</strong> <strong>says</strong> the trade fair <strong>starts</strong> at nine.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "She <strong>has just landed</strong>." O que <strong>just</strong> acrescenta?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Aconteceu agora h&#225; pouco &mdash; poucos minutos atr&#225;s.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Aconteceu h&#225; muito tempo e j&#225; acabou.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Vai acontecer daqui a pouco.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "She <strong>has not gone</strong> through customs <strong>yet</strong>." O que essa frase diz?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Ela j&#225; passou pela alf&#226;ndega.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Ainda n&#227;o passou &mdash; mas ainda vai passar. <strong>yet</strong> = at&#233; agora, n&#227;o.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ela nunca vai passar pela alf&#226;ndega.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. Por que "She <strong>landed</strong> at nine, <strong>walked</strong> to passport control and <strong>answered</strong> two questions" est&#225; no past simple, e n&#227;o no present perfect?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque a a&#231;&#227;o continua acontecendo agora.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque &#233; uma SEQU&#202;NCIA de a&#231;&#245;es terminadas, com hora dita (at nine) &mdash; narrativa.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o resultado dela importa mais do que o momento.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct at the front desk?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have completed the online check-in yesterday."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I\'ve already completed the online check-in, and I have my confirmation number here."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I already complete the online check-in yet."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Perfect com just / already / yet (e o contraste com o Past Simple)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Tr&#234;s palavrinhas que mudam tudo &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Word</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">just<br>have + <strong>just</strong> + partic&#237;pio</td><td style="padding:.6rem">Aconteceu agora h&#225; pouco. A few minutes ago. Vem ANTES do partic&#237;pio.</td><td style="padding:.6rem">I <strong>have just landed</strong>. (I&#8217;ve just landed.)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">already<br>have + <strong>already</strong> + partic&#237;pio</td><td style="padding:.6rem">J&#225; foi feito &mdash; muitas vezes antes do esperado. Afirmativa. Vem ANTES do partic&#237;pio.</td><td style="padding:.6rem">I <strong>have already completed</strong> the online check-in.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">yet<br>haven&#8217;t + partic&#237;pio + <strong>yet</strong></td><td style="padding:.6rem">Ainda n&#227;o (negativa) ou j&#225;? (pergunta). Vem SEMPRE NO FIM da frase.</td><td style="padding:.6rem">I <strong>haven&#8217;t checked in yet</strong>. / <strong>Have</strong> you checked in <strong>yet</strong>?</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem">have / has + not + partic&#237;pio. Na fala: <strong>haven&#8217;t</strong> / <strong>hasn&#8217;t</strong>.</td><td style="padding:.6rem">My bag <strong>hasn&#8217;t arrived</strong> yet.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">Have + sujeito + partic&#237;pio ... yet?</td><td style="padding:.6rem"><strong>Have you picked up</strong> your bags <strong>yet</strong>?</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">Past Simple<br>verbo no passado</td><td style="padding:.6rem" colspan="2">Quando voc&#234; DIZ A HORA ou conta a sequ&#234;ncia (narrativa), o ingl&#234;s exige past simple: "I <strong>landed</strong> at nine and <strong>took</strong> a cab." NUNCA "I have landed at nine."</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (os dois erros cl&#225;ssicos):</strong> (1) <strong>yet</strong> vai no FIM: "I haven&#8217;t checked in <strong>yet</strong>", nunca "I haven&#8217;t yet checked in" na conversa do dia a dia. (2) Com hora/data expl&#237;cita, o present perfect &#233; PROIBIDO: "I <strong>landed</strong> at nine" (certo) e n&#227;o "I have landed at nine" (errado). A regra pr&#225;tica: <em>quando importa QUANDO</em> &rarr; past simple; <em>quando importa O RESULTADO agora</em> &rarr; present perfect.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("just", "Dica: aconteceu agora h&#225; pouco &mdash; vem antes do partic&#237;pio",
     "I have just landed in New York.",
     '"I have ', ' landed in New York."'),
    ("already", "Dica: j&#225; foi feito, antes do esperado &mdash; vem antes do partic&#237;pio",
     "I have already completed the online check-in.",
     '"I have ', ' completed the online check-in."'),
    ("yet", "Dica: ainda n&#227;o &mdash; vem no FIM da frase",
     "I haven't checked in yet.",
     '"I haven\'t checked in ', '."'),
    ("hasn't", "Dica: negativa de has &mdash; a mala ainda n&#227;o chegou",
     "My bag hasn't arrived yet.",
     '"My bag ', ' arrived yet."'),
    ("landed", "Dica: hora expl&#237;cita (at nine) &mdash; past simple, nunca present perfect",
     "My flight landed at nine, and I took a cab to the hotel.",
     '"My flight ', ' at nine, and I took a cab to the hotel."'),
    ("confirmation number", "Dica: o c&#243;digo que prova que voc&#234; tem uma reserva",
     "Here is my confirmation number.",
     '"Here is my ', '."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase. Toque em Listen para ouvir a frase inteira &mdash; e ou&#231;a quantas vezes quiser.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering ----------
ORDER = [
    (4, "Take a taxi to the hotel and give the driver the address."),
    (2, "Pick up your suitcase at baggage claim, belt six."),
    (5, "At the front desk, give your name and your confirmation number."),
    (1, "Land at the terminal and answer the officer at passport control."),
    (3, "Go through customs -- green line if you have nothing to declare."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Arrival in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Voc&#234; acabou de pousar em Nova York. Coloque as etapas na ordem real &mdash; da pista at&#233; a recep&#231;&#227;o do hotel.</p>')
A('      <div class="order-container" id="order-l2">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l2\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l2\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l2\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l2\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    ("Excuse me, I have a reservation under the name Ito.",
     "Com licen&#231;a, eu tenho uma reserva no nome Ito."),
    ("I've just landed, and I haven't checked in yet.",
     "Acabei de pousar e ainda n&#227;o fiz o check-in."),
    ("I've already completed the online check-in. Here is my confirmation number.",
     "J&#225; fiz o check-in online. Aqui est&#225; o meu n&#250;mero de confirma&#231;&#227;o."),
    ("Could you tell me where the baggage claim is?",
     "Voc&#234; poderia me dizer onde fica a esteira de bagagem?"),
    ("My flight landed at nine, and I took a cab straight to the hotel.",
     "Meu voo pousou &#224;s nove e eu peguei um t&#225;xi direto para o hotel."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. Preste aten&#231;&#227;o nas ligadas: <em>I&#8217;ve just</em> vira quase uma palavra s&#243;, e <em>haven&#8217;t</em> some na fala r&#225;pida &mdash; &#233; exatamente isso que engole a frase no aeroporto.</p>')
for en, pt in SPEECH:
    A(f'      <div class="speech-card" data-phrase="{en}">')
    A(f'        <div class="speech-phrase">{en}</div>')
    A(f'        <div class="speech-translation">{pt}</div>')
    A('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    A('        <div class="speech-result"></div>')
    A('      </div>')
A('    </div>')

# ---------- Stage 4 — Situational quiz ----------
QUIZ = [
    ("Voc&#234; chega &#224; recep&#231;&#227;o do hotel depois de um voo de dez horas. Voc&#234; diz:",
     [("\"Excuse me, I have a reservation under the name Ito.\"", True),
      ("\"Hello, I want a room now, please.\"", False),
      ("\"I am Ito. Give me the key.\"", False)]),
    ("O recepcionista pergunta: \"Have you checked in online yet?\" A melhor resposta &#233;:",
     [("\"Yes, I already complete it yet.\"", False),
      ("\"Yes, I've already completed the online check-in.\"", True),
      ("\"Yes, I have completed it at three o'clock yesterday.\"", False)]),
    ("Voc&#234; quer contar a hist&#243;ria da chegada para um colega, com hora e sequ&#234;ncia. Qual est&#225; correta?",
     [("\"I have landed at nine and I have taken a cab.\"", False),
      ("\"I landed at nine, took a cab, and got to the hotel at ten.\"", True),
      ("\"I land at nine and take a cab yesterday.\"", False)]),
    ("A sua mala n&#227;o apareceu na esteira. Voc&#234; procura um funcion&#225;rio e diz:",
     [("\"My bag hasn't arrived yet. I've already waited twenty minutes at belt six.\"", True),
      ("\"My bag not arrive. Problem.\"", False),
      ("\"I don't have bag yet already.\"", False)]),
    ("S&#227;o nove da noite e o quarto ainda n&#227;o est&#225; pronto. A rea&#231;&#227;o mais eficaz &#233;:",
     [("Aceitar em sil&#234;ncio e esperar de p&#233; no lobby, sem perguntar nada.", False),
      ("\"I understand. Could I leave my bags here and have a coffee while I wait?\"", True),
      ("Pedir desculpas pelo seu ingl&#234;s e desistir do quarto.", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real das primeiras horas em Nova York.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o existe resposta certa ou errada &mdash; fale por 90 segundos, sem script.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">It is your first night in New York. You have just arrived at the hotel and the room is not ready yet. Tell the story of your arrival: what time your flight landed, what you did at passport control and at baggage claim (past simple), and what you have already done and what you have not done yet (present perfect with just / already / yet). Finish by asking the front desk two questions. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-2"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 2</h4>')
for i, (en, pt) in enumerate(SPEECH, 1):
    A(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span>'
      f'<span class="sp-pt">{pt}</span>'
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
