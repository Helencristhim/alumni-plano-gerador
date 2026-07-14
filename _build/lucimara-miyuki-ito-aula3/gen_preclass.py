#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-3 do hub) da Lucimara — aula 3.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 3 IN CLASS (mesmo tema/gramatica/vocab).
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(3)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Fare", "the money you pay for a ride in a taxi, a bus or the subway",
     "tarifa / valor da corrida", "How much is the fare to the Upper West Side?"),
    ("Tip", "extra money you leave for the person who served you",
     "gorjeta", "In New York, twenty percent is the normal tip at a restaurant."),
    ("Block", "the distance from one street corner to the next one",
     "quarteir&#227;o", "The subway station is three blocks from the hotel."),
    ("Subway line", "one train route in the subway, with a number or a letter",
     "linha de metr&#244;", "Take the 1 line uptown and get off at 79th Street."),
    ("Diner", "a simple American restaurant that serves breakfast all day",
     "lanchonete americana", "We had lunch at a diner on Ninth Avenue."),
    ("To-go order", "food you take with you instead of eating it at the table",
     "pedido para viagem", "I'm in a hurry -- could you make it a to-go order?"),
    ("Sales tax", "the extra percentage added to the price when you pay at the register",
     "imposto sobre vendas (somado no caixa)",
     "The price on the tag doesn't include sales tax."),
    ("Fitting room", "the small room in a store where you put the clothes on to see if they fit",
     "provador", "Could I try this on? Where is the fitting room?"),
    ("Receipt", "the paper that proves you paid -- the P is silent",
     "recibo / nota", "Could I have a receipt, please?"),
    ("Rush hour", "the time of day when the trains and the streets are full of people",
     "hor&#225;rio de pico", "Don't take the subway at rush hour with a suitcase."),
    ("To hail (a cab)", "to raise your hand in the street to stop a taxi",
     "chamar um t&#225;xi com a m&#227;o", "She hailed a cab on Fifth Avenue and gave the driver the address."),
    ("To figure out", "to understand something after some effort -- not immediately",
     "descobrir / sacar (com esfor&#231;o)", "It took me ten minutes to figure out the subway map."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-3">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1514565131-fce0801e5785?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 03 -- Pre-class</div>')
A('      <h3>Getting Around and Getting Things Done -- Taxis, Subways, Restaurants, and Shops</h3>')
A('      <div class="lesson-desc">A cidade em movimento: t&#225;xi na Fifth Avenue, metr&#244; na hora do rush, almo&#231;o num diner '
  'e uma loja onde o pre&#231;o do caixa n&#227;o &#233; o da etiqueta. Key words: fare, tip, block, subway line, diner, '
  'to-go order, sales tax, fitting room, receipt, rush hour, to hail a cab, to figure out. '
  'Structure: <strong>past simple</strong> x <strong>present perfect</strong> na narrativa de viagem '
  '("When I <strong>went</strong> to New York in 2023, I <strong>took</strong> a cab everywhere -- but this time '
  "I<strong>&#8217;ve already used</strong> the subway twice\").</div>")
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras que voc&#234; usa com dinheiro na m&#227;o: o t&#225;xi, o metr&#244;, a conta do restaurante e o caixa da loja.</p>')
A('      <div class="vocab-cards">')
for w, de, pt, ex in VOCAB:
    speak = w.replace('(', '').replace(')', '')
    A(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{de} ({pt})</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{speak}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
A('      </div>')
A('    </div>')

# ---------- Stage 1.2 — Matching (REGRA 24: embaralhado) ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a tradu&#231;&#227;o correta.</p>')
A('      <div class="match-grid" id="match-l3">')
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
A('        <p>When Lucimara <strong>went</strong> to New York in 2023, she <strong>took</strong> a cab everywhere. '
  'She <strong>hailed</strong> one outside the hotel every morning, she <strong>paid</strong> the '
  '<strong>fare</strong> in cash, and she never <strong>asked</strong> for a <strong>receipt</strong>. '
  'That trip <strong>is</strong> closed: it <strong>has</strong> a date, so English <strong>uses</strong> the '
  'past simple.</p>')
A('        <p style="margin-top:.8rem">This time is different, and the trip <strong>is not over</strong>. She '
  '<strong>has already used</strong> the subway twice: the 1 <strong>line</strong>, uptown, three '
  '<strong>blocks</strong> from the hotel. She <strong>has never taken</strong> it at '
  '<strong>rush hour</strong>, and honestly she <strong>has not figured out</strong> the map yet. Yesterday she '
  '<strong>had</strong> lunch at a <strong>diner</strong> on Ninth Avenue and <strong>left</strong> a twenty '
  'percent <strong>tip</strong> &mdash; that <strong>happened</strong>, it <strong>has</strong> a day, so: past '
  'simple again. But this afternoon, on Fifth Avenue, she <strong>has already tried on</strong> a coat in the '
  '<strong>fitting room</strong>, and at the register she <strong>learned</strong> the New York lesson: the '
  'price on the tag <strong>is not</strong> the price you pay, because of the <strong>sales tax</strong>.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Por que "she <strong>went</strong> to New York in 2023" est&#225; no past simple, e n&#227;o no present perfect?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque a viagem ainda est&#225; acontecendo.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque a frase DIZ A DATA (in 2023) &mdash; a viagem est&#225; fechada. Com data expl&#237;cita, o ingl&#234;s exige past simple.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o resultado dela importa mais do que o momento.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "She <strong>has already used</strong> the subway twice." O que <strong>already</strong> + present perfect diz aqui?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A viagem AINDA EST&#193; ABERTA &mdash; e, at&#233; agora, ela j&#225; usou o metr&#244; duas vezes. O n&#250;mero ainda pode subir.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Ela usou o metr&#244; duas vezes em 2023.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ela vai usar o metr&#244; duas vezes amanh&#227;.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "She <strong>has never taken</strong> it at rush hour." Por que <strong>taken</strong>, e n&#227;o <strong>took</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque <strong>took</strong> s&#243; existe em ingl&#234;s brit&#226;nico.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque as duas formas s&#227;o corretas &mdash; tanto faz.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Porque depois de <strong>have / has</strong> o verbo muda de forma: o partic&#237;pio. take &rarr; <strong>taken</strong>, go &rarr; <strong>gone</strong>, eat &rarr; <strong>eaten</strong>.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have gone to New York in 2023 and I have took a cab."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I went to New York in 2023 and I took a cab &mdash; but this time I\'ve already used the subway."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I go to New York in 2023 and I have already take the subway."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Past Simple x Present Perfect (a narrativa de viagem)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Duas viagens, dois tempos verbais &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Tense</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Past Simple<br>went &middot; took &middot; paid</td><td style="padding:.6rem">Momento FECHADO. Voc&#234; diz QUANDO (in 2023, last night, yesterday, ten minutes ago) ou conta a sequ&#234;ncia.</td><td style="padding:.6rem">"When I <strong>went</strong> to New York in 2023, I <strong>took</strong> a cab everywhere."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + partic&#237;pio</td><td style="padding:.6rem">A viagem ainda est&#225; ABERTA, ou a experi&#234;ncia &#233; a vida toda. O momento N&#195;O importa. Palavras-sinal: already, never, ever, so far, this time, twice.</td><td style="padding:.6rem">"This time I<strong>&#8217;ve already used</strong> the subway twice."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem">have / has + not + partic&#237;pio. Na fala: <strong>haven&#8217;t</strong> / <strong>hasn&#8217;t</strong>.</td><td style="padding:.6rem">"I <strong>haven&#8217;t figured out</strong> the subway map yet."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">Have + sujeito + <strong>ever</strong> + partic&#237;pio? (= alguma vez na vida)</td><td style="padding:.6rem">"<strong>Have you ever tried</strong> a New York diner?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">O PARTIC&#205;PIO<br>(a pe&#231;a que trava)</td><td style="padding:.6rem" colspan="2">Depois de <strong>have / has</strong>, o verbo MUDA DE FORMA: take &rarr; <strong>taken</strong> (nunca "have took"), go &rarr; <strong>gone</strong>, eat &rarr; <strong>eaten</strong>, pay &rarr; <strong>paid</strong>, buy &rarr; <strong>bought</strong>, do &rarr; <strong>done</strong>.</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">O teste &#250;nico</td><td style="padding:.6rem" colspan="2">Fa&#231;a UMA pergunta: <strong>isso ainda pode mudar hoje?</strong> Se sim &rarr; present perfect. Se est&#225; fechado e tem data &rarr; past simple. 2023 est&#225; fechado. Setembro ainda est&#225; aberto.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (os dois erros cl&#225;ssicos):</strong> (1) Data expl&#237;cita com present perfect &#233; PROIBIDA: em portugu&#234;s "eu j&#225; fui a Nova York em 2023" funciona, mas em ingl&#234;s, no instante em que voc&#234; diz <em>in 2023</em>, o verbo TEM de virar past simple &mdash; "I <strong>went</strong>", nunca "I have gone... in 2023". (2) Partic&#237;pio errado depois de <em>have</em>: "I have never <strong>took</strong>" &#233; o erro que mais denuncia o n&#237;vel. O certo &#233; "I have never <strong>taken</strong>".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("took", "Dica: a frase diz a data (in 2023) &mdash; momento fechado, past simple",
     "In 2023 I took a cab from JFK to Midtown.",
     '"In 2023 I ', ' a cab from JFK to Midtown."'),
    ("already", "Dica: a viagem ainda est&#225; aberta &mdash; vem antes do partic&#237;pio",
     "This time I have already used the subway twice.",
     '"This time I have ', ' used the subway twice."'),
    ("taken", "Dica: depois de have, o verbo take vira partic&#237;pio",
     "I have never taken the subway at rush hour.",
     '"I have never ', ' the subway at rush hour."'),
    ("fare", "Dica: o valor que voc&#234; paga pela corrida",
     "How much is the fare to the Upper West Side?",
     '"How much is the ', ' to the Upper West Side?"'),
    ("receipt", "Dica: o papel que prova que voc&#234; pagou &mdash; o P &#233; mudo",
     "Could I have a receipt, please?",
     '"Could I have a ', ', please?"'),
    ("sales tax", "Dica: a porcentagem que aparece s&#243; no caixa",
     "The price on the tag doesn't include sales tax.",
     '"The price on the tag doesn\'t include ', '."'),
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
    (3, "Order the soup of the day and a coffee."),
    (5, "Take the receipt and head out to the subway."),
    (1, "Walk two blocks to the diner on Ninth Avenue."),
    (4, "Ask for the check and add a twenty percent tip."),
    (2, "Ask for a table for one and read the specials."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the New York Lunch in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Uma hora de almo&#231;o em Manhattan. Coloque as etapas na ordem real &mdash; da cal&#231;ada at&#233; a esta&#231;&#227;o de metr&#244;.</p>')
A('      <div class="order-container" id="order-l3">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l3\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    ("How much is the fare to the Upper West Side?",
     "Quanto custa a corrida at&#233; o Upper West Side?"),
    ("When I went to New York in 2023, I took a cab everywhere.",
     "Quando fui a Nova York em 2023, peguei t&#225;xi para tudo."),
    ("This time I've already used the subway twice.",
     "Desta vez, eu j&#225; usei o metr&#244; duas vezes."),
    ("Could I have the check, please? Is the tip included?",
     "Pode trazer a conta, por favor? A gorjeta est&#225; inclusa?"),
    ("Could I try this on? Where is the fitting room?",
     "Posso experimentar? Onde fica o provador?"),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. Aten&#231;&#227;o ao que o americano ENGOLE: <em>restaurant</em> tem duas s&#237;labas na boca dele (RES-trant), n&#227;o tr&#234;s; <em>receipt</em> se diz ri-SEET, com o P mudo; e <em>fare</em> rima com <em>air</em>. Falar &#8220;menos&#8221; aqui &#233; falar CERTO.</p>')
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
    ("Voc&#234; est&#225; na Fifth Avenue, com duas sacolas, e quer um t&#225;xi. O que voc&#234; faz e diz?",
     [("Ligar para o hotel e pedir que mandem um carro &mdash; t&#225;xi na rua &#233; imposs&#237;vel.", False),
      ("Levantar a m&#227;o para chamar (hail) e dizer: \"The Lucerne Hotel, 79th and Amsterdam, please.\"", True),
      ("Esperar em sil&#234;ncio no meio-fio at&#233; algu&#233;m parar.", False)]),
    ("O motorista diz o valor r&#225;pido e a rua est&#225; barulhenta. A melhor rea&#231;&#227;o &#233;:",
     [("Fingir que entendeu e pagar o que ele pedir no fim.", False),
      ("\"Sorry, it's loud out here. Let me read that back to you: about thirty-two dollars. Is that right?\"", True),
      ("\"Repeat, repeat!\"", False)]),
    ("Voc&#234; quer contar ao colega sobre a viagem de 2023. Qual frase est&#225; correta?",
     [("\"I have gone to New York in 2023 and I have took a cab.\"", False),
      ("\"I went to New York in 2023 and I took a cab everywhere.\"", True),
      ("\"I go to New York in 2023 and I have already take a cab.\"", False)]),
    ("A conta do diner chegou: subtotal $24.00, total $26.13, e a linha do <em>tip</em> est&#225; em branco. Isso quer dizer:",
     [("Que a gorjeta j&#225; est&#225; inclusa no total e voc&#234; n&#227;o precisa fazer nada.", False),
      ("Que o total j&#225; tem o <strong>sales tax</strong>, mas a gorjeta &#233; voc&#234; que escreve &mdash; cerca de 20% do subtotal.", True),
      ("Que houve um erro na conta e voc&#234; deve reclamar.", False)]),
    ("Na loja da Fifth Avenue voc&#234; gostou de um casaco e quer experimentar. Voc&#234; diz:",
     [("\"Could I try this on? Where is the fitting room?\"", True),
      ("\"I want to use this coat now, please.\"", False),
      ("\"Where is the room for the clothes?\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de um dia em Nova York.</p>')
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
A('        <div class="think-question">Tell the story of one real trip: a taxi you took, a restaurant you went to, or a store you walked into &mdash; in New York, in Europe, or in China. Use the past simple for what happened (I took, I went, I paid, I asked). Then compare it with now: what have you already done on this trip, and what have you never done? Finish with one thing you still haven\'t figured out. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-3"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 3</h4>')
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
