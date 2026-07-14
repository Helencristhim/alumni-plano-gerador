#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-6 do hub) da Lucimara — aula 6.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 6 IN CLASS (mesmo tema/gramatica/vocab).

REGRA 22 — CURRICULO CORRIGIDO (o curriculo da aula 6 estava quebrado nos DOIS eixos):
  GRAMATICA: o curriculo pedia FIRST CONDITIONAL -- que ja foi ensinada na aula 4.
    Trocada por MODAIS DE OBRIGACAO / PERMISSAO / PROIBICAO (have to / don't have to /
    must / can't / be allowed to). Gramatica nova (a1 present simple+continuous,
    a2 present perfect, a3 past simple x present perfect, a4 first conditional,
    a5 second conditional + I wish) e serve ao tema como uma luva: uma cidade e um
    conjunto de regras. NAO se usou 'used to', que o curriculo reserva para a aula 9.
  VOCABULARIO: 4 dos 9 itens do curriculo ja tinham sido ensinados --
    'terminal' e 'baggage claim' (aula 2), 'fare' (aula 3), 'customs declaration'
    (encosta em 'customs', aula 2). E 'delay' colide semanticamente com 'delay notice'
    (aula 4) -> tambem descartada. Sobraram 4 realmente novas (connecting flight,
    rideshare, check-in kiosk, departure gate), abaixo do minimo B1 de 10-12 (REGRA 13).
    Completadas com 8 palavras novas do MESMO campo semantico (mobilidade urbana /
    transporte local): turnstile, to tap in, platform, express train, to transfer,
    uptown, shuttle, curbside.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(6)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Connecting flight", "the second flight you take, after the first one lands, on the same trip",
     "voo de conex&#227;o",
     "I have a connecting flight in Atlanta, and I have to change terminals."),
    ("Departure gate", "the door at the airport where you wait, and where you get on the plane",
     "port&#227;o de embarque",
     "You don't have to be at the departure gate two hours early."),
    ("Check-in kiosk", "the machine you use to check yourself in, without talking to anybody",
     "totem de autoatendimento (check-in)",
     "If the line at the counter is long, you can use the check-in kiosk instead."),
    ("Rideshare", "a car you order on an app, like Uber or Lyft, instead of a taxi",
     "carro de aplicativo (Uber, Lyft)",
     "At JFK you have to meet your rideshare on the second floor."),
    ("Curbside", "the edge of the street, where cars stop to pick you up or drop you off",
     "meio-fio (onde o carro encosta)",
     "Rideshare cars are not allowed to wait at the curbside for more than a minute."),
    ("Turnstile", "the metal gate you go through to enter the subway, one person at a time",
     "catraca",
     "You have to tap your card before you go through the turnstile."),
    ("To tap in", "to touch your card or your phone on the reader, to pay and go in",
     "encostar o cart&#227;o (para entrar e pagar)",
     "You don't have to buy a ticket anymore -- you can just tap in with your credit card."),
    ("Platform", "the long floor next to the tracks, where you stand and wait for the train",
     "plataforma (do metr&#244;)",
     "The uptown platform and the downtown platform are on different sides."),
    ("Express train", "a train that skips most stations and only stops at the big ones",
     "trem expresso (pula esta&#231;&#245;es)",
     "The express train doesn't stop at my station, so I have to take the local one."),
    ("To transfer", "to get off one train and get on another one, to finish your trip",
     "baldear (trocar de trem)",
     "You have to transfer at Times Square if you want to go downtown."),
    ("Uptown", "toward the north of Manhattan, where the street numbers get bigger",
     "para o norte de Manhattan (o oposto &#233; downtown)",
     "I was going uptown, but my hotel was downtown -- forty blocks the wrong way."),
    ("Shuttle", "a small bus or train that goes back and forth between two places only",
     "van/trem de liga&#231;&#227;o (que s&#243; vai e volta)",
     "You have to take the shuttle from the terminal to the subway station."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-6">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 06 -- Pre-class</div>')
A('      <h3>Getting Around Like a Local -- Airports, Transit, and the Rules of the City</h3>')
A('      <div class="lesson-desc">Na aula 5 voc&#234; escolheu a semana perfeita. Agora voc&#234; tem de CHEGAR l&#225; &mdash; e a cidade '
  'tem regras que ningu&#233;m te explica. Do totem de check-in em Guarulhos &#224; catraca em Manhattan. Key words: '
  'connecting flight, departure gate, check-in kiosk, rideshare, curbside, turnstile, to tap in, platform, express '
  'train, to transfer, uptown, shuttle. Structure: <strong>modais de obriga&#231;&#227;o, permiss&#227;o e '
  'proibi&#231;&#227;o</strong> &mdash; a gram&#225;tica de uma regra ("You <strong>have to</strong> tap your card '
  'before the turnstile." / "You <strong>don&#8217;t have to</strong> buy a ticket." / "You <strong>can&#8217;t</strong> '
  'smoke on the platform." / "You <strong>are allowed to</strong> take a bike, but not at rush hour."). O ponto que '
  'decide tudo: <strong>don&#8217;t have to</strong> (&#233; opcional) e <strong>can&#8217;t</strong> (&#233; proibido) '
  's&#227;o OPOSTOS &mdash; em portugu&#234;s os dois come&#231;am com "n&#227;o".</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras que est&#227;o entre o avi&#227;o e o hotel: metade delas est&#225; escrita numa placa, e ningu&#233;m l&#234; a placa para voc&#234;.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a tradu&#231;&#227;o correta. Aten&#231;&#227;o ao par que confunde: o <strong>check-in kiosk</strong> &#233; a M&#193;QUINA (voc&#234; n&#227;o fala com ningu&#233;m); o <em>check-in counter</em> da aula 2 &#233; o BALC&#195;O, com gente atr&#225;s. Em setembro, a fila de um tem quarenta pessoas e a do outro tem duas.</p>')
A('      <div class="match-grid" id="match-l6">')
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
A('        <p>The line at the counter has forty people in it. The line at the <strong>check-in kiosk</strong> has two. '
  'Lucimara <strong>does not have to</strong> talk to anybody: she scans her passport, she prints her tag, and she '
  'walks to the <strong>departure gate</strong>. Her <strong>connecting flight</strong> leaves Atlanta at seven '
  'forty.</p>')
A('        <p style="margin-top:.8rem">Eleven hours later, at Kennedy, her <strong>rideshare</strong> driver calls. He '
  'speaks fast, and he says he <strong>can&#8217;t</strong> wait. What nobody told either of them: at that airport, '
  'rideshare cars <strong>are not allowed to</strong> stop at the <strong>curbside</strong> on the arrivals level. He '
  '<strong>has to</strong> come up to Level 2. So he cancels, and she takes the <strong>shuttle</strong> to the '
  'station instead.</p>')
A('        <p style="margin-top:.8rem">At the station there is a man in a booth. Her suitcase is too big for the '
  '<strong>turnstile</strong>. "You <strong>have to</strong> use the wide gate," he says, "and you <strong>have '
  'to</strong> <strong>tap in</strong> there too." She asks whether she <strong>has to</strong> buy a ticket. She '
  '<strong>doesn&#8217;t</strong>. She <strong>can</strong> just tap the credit card that is already in her hand.</p>')
A('        <p style="margin-top:.8rem">Then she asks the question that saves the whole trip: which <strong>platform</strong> '
  '<strong>does</strong> she <strong>have to</strong> be on &mdash; <strong>uptown</strong> or downtown? Both platforms '
  'say E. Both trains are the same color. One goes to her hotel in Midtown. The other one is an <strong>express '
  'train</strong> going forty blocks the wrong way, and it <strong>would not</strong> stop again for a long time. She '
  'takes the downtown side. She <strong>doesn&#8217;t have to</strong> <strong>transfer</strong> at all.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "She <strong>does not have to</strong> talk to anybody." O que isso significa sobre o balc&#227;o com gente?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Que ela est&#225; PROIBIDA de falar com o atendente do balc&#227;o.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Que falar com o atendente &#233; OPCIONAL &mdash; ela pode, se quiser, mas n&#227;o precisa. <strong>Don&#8217;t have to</strong> = n&#227;o &#233; obrigat&#243;rio (e nada te impede).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Que ela n&#227;o consegue falar ingl&#234;s suficiente para isso.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. Qual &#233; a diferen&#231;a entre "he <strong>can&#8217;t</strong> wait" e "she <strong>doesn&#8217;t have to</strong> buy a ticket"?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> S&#227;o OPOSTOS. <strong>Can&#8217;t</strong> = proibido/imposs&#237;vel (a regra o impede). <strong>Doesn&#8217;t have to</strong> = opcional (nada a impede &mdash; ela s&#243; n&#227;o precisa).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Nenhuma &mdash; as duas s&#227;o negativas, ent&#227;o querem dizer a mesma coisa.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A primeira &#233; formal e a segunda &#233; informal.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "Which platform <strong>does</strong> she <strong>have to</strong> be on?" Por que aparece o <strong>does</strong> na pergunta?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque toda pergunta em ingl&#234;s come&#231;a com <em>does</em>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque <strong>have to</strong> &#233; um verbo NORMAL &mdash; e verbo normal precisa de <em>do/does</em> para perguntar. Por isso se diz "<strong>Do I have to</strong> transfer?" e nunca "<s>Do I must</s> transfer?".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque a frase est&#225; no passado.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You mustn&#8217;t buy a ticket &mdash; you can just tap your card." (isto PRO&#205;BE a pessoa de comprar bilhete!)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "You don&#8217;t have to buy a ticket &mdash; you can just tap your card."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You don&#8217;t must to buy a ticket &mdash; you can just tap your card."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Have to / Don&#8217;t have to / Can&#8217;t / Be allowed to (a gram&#225;tica de uma regra)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Uma cidade &#233; um conjunto de regras &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Forma</th><th style="padding:.7rem;text-align:left">Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">have to<br>(afirmativa)</td><td style="padding:.6rem"><strong>OBRIGA&#199;&#195;O</strong> &mdash; a regra de outra pessoa, n&#227;o a sua vontade. &#201; o que o americano DIZ (o <em>must</em> ele mais escreve do que fala).</td><td style="padding:.6rem">"You <strong>have to</strong> tap your card." (voc&#234; TEM DE encostar o cart&#227;o)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">must</td><td style="padding:.6rem">A MESMA obriga&#231;&#227;o, mas voc&#234; quase sempre a <strong>l&#234;</strong>: placas, regulamentos, contratos. Raro na fala.</td><td style="padding:.6rem">"Passengers <strong>must</strong> hold the handrail." (placa no metr&#244;)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600;color:#15803d">don&#8217;t have to<br>(negativa 1)</td><td style="padding:.6rem"><strong>N&#195;O H&#193; OBRIGA&#199;&#195;O</strong> &mdash; &#233; OPCIONAL. Voc&#234; pode fazer, se quiser: ningu&#233;m te impede. <strong>Isto N&#195;O &#233; proibi&#231;&#227;o.</strong></td><td style="padding:.6rem">"You <strong>don&#8217;t have to</strong> buy a ticket." (n&#227;o PRECISA &mdash; mas pode)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600;color:#b91c1c">can&#8217;t / must not<br>(negativa 2)</td><td style="padding:.6rem"><strong>PROIBI&#199;&#195;O</strong> &mdash; &#233; vedado. Se fizer, h&#225; consequ&#234;ncia.</td><td style="padding:.6rem">"You <strong>can&#8217;t</strong> smoke on the platform." (n&#227;o PODE)</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">can /<br>be allowed to</td><td style="padding:.6rem"><strong>PERMISS&#195;O</strong> &mdash; a regra diz que sim. <em>Be allowed to</em> &#233; a forma mais formal (e a que aparece em aviso oficial).</td><td style="padding:.6rem">"You <strong>are allowed to</strong> take a bike, but not at rush hour."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">A pergunta</td><td style="padding:.6rem"><strong>Do I have to&#8230;?</strong> / <strong>Am I allowed to&#8230;?</strong> &mdash; <em>have to</em> &#233; verbo normal: pede <em>do/does</em>.</td><td style="padding:.6rem">"<strong>Do I have to</strong> transfer?" &mdash; nunca "<s>Do I must transfer?</s>"</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">O som<br>(o mais importante)</td><td style="padding:.6rem" colspan="2">Na boca de um americano, <em>have to</em> N&#195;O soa como <em>have to</em>: vira <strong>HAFTA</strong>, com F. <em>has to</em> vira <strong>HASTA</strong>. <em>got to</em> vira <strong>GOTTA</strong>. E <em>don&#8217;t have to</strong> vira <strong>DOAN-HAFTA</strong>, tudo grudado. <strong>&#201; por isso que voc&#234; nunca ouviu esta gram&#225;tica</strong> &mdash; ela est&#225; em todo lugar, mas n&#227;o soa como as palavras que voc&#234; aprendeu.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro que troca o sentido da frase):</strong> em portugu&#234;s, "<em>n&#227;o precisa</em> comprar bilhete" e "<em>n&#227;o pode</em> comprar bilhete" come&#231;am as duas com "n&#227;o" &mdash; e a cabe&#231;a junta as duas num neg&#243;cio s&#243;. Em ingl&#234;s elas s&#227;o <strong>OPOSTAS</strong>: <strong style="color:#15803d">don&#8217;t have to</strong> te LIBERTA (&#233; opcional), <strong style="color:#b91c1c">mustn&#8217;t / can&#8217;t</strong> te PROIBE. Se voc&#234; disser "you mustn&#8217;t buy a ticket" para um turista, voc&#234; acabou de proibi-lo de comprar bilhete. A pergunta que resolve, sempre: <em>essa frase LIBERTA ou IMPEDE?</em></p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("have to", "Dica: obriga&#231;&#227;o &mdash; a regra da cidade (duas palavras)",
     "You have to tap your card before you go through the turnstile.",
     '"You ', ' tap your card before you go through the turnstile."'),
    ("don't have to", "Dica: n&#227;o &#233; proibido &mdash; &#233; s&#243; OPCIONAL (tr&#234;s palavras)",
     "You don't have to buy a ticket -- you can just tap your credit card.",
     '"You ', ' buy a ticket -- you can just tap your credit card."'),
    ("can't", "Dica: proibido mesmo &mdash; h&#225; consequ&#234;ncia (uma palavra)",
     "You can't smoke on the platform.",
     '"You ', ' smoke on the platform."'),
    ("allowed", "Dica: permiss&#227;o formal &mdash; Am I ___ to...?",
     "Am I allowed to take this suitcase through the gate?",
     '"Am I ', ' to take this suitcase through the gate?"'),
    ("transfer", "Dica: descer de um trem e pegar outro",
     "You have to transfer at 42nd Street to go downtown.",
     '"You have to ', ' at 42nd Street to go downtown."'),
    ("express", "Dica: o trem que pula quase todas as esta&#231;&#245;es",
     "The express train doesn't stop at my station, so I have to take the local one.",
     '"The ', ' train doesn\'t stop at my station, so I have to take the local one."'),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase. Toque em Listen para ouvir a frase inteira &mdash; e ou&#231;a quantas vezes quiser. Preste aten&#231;&#227;o no som: o <em>have to</em> vai soar como <strong>HAFTA</strong>.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    A(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
A('    </div>')

# ---------- Stage 2 — Ordering ----------
ORDER = [
    (3, "Take the shuttle from the terminal to the subway station."),
    (1, "Use the check-in kiosk, and skip the line of forty people at the counter."),
    (4, "Tap in at the wide gate, because the suitcase does not fit through the turnstile."),
    (2, "Walk to the departure gate and board the connecting flight."),
    (5, "Check the platform -- downtown, not uptown -- and get on the express train."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: The Sixty-Two Minutes, in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Do totem em Guarulhos at&#233; a plataforma certa em Nova York &mdash; a viagem inteira, na ordem em que ela realmente acontece.</p>')
A('      <div class="order-container" id="order-l6">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l6\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation (= survival card da aula) ----------
SPEECH = [
    ("Excuse me, do I have to transfer to get to Midtown?",
     "Com licen&#231;a, eu preciso baldear para chegar ao Midtown?"),
    ("Which platform do I have to be on -- uptown or downtown?",
     "Em qual plataforma eu tenho de estar &mdash; sentido norte ou sentido sul?"),
    ("You don't have to buy a ticket -- you can just tap your credit card.",
     "Voc&#234; n&#227;o precisa comprar bilhete &mdash; d&#225; para s&#243; encostar o cart&#227;o de cr&#233;dito."),
    ("Am I allowed to take this suitcase through the gate?",
     "Eu posso passar com esta mala pelo port&#227;o?"),
    ("Let me check I understood: the E train, downtown platform, no transfer.",
     "Deixa eu confirmar se entendi: o trem E, plataforma sentido sul, sem baldea&#231;&#227;o."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. O alvo de hoje &#233; UM som: o <strong>have to</strong> grudado. Na boca de um americano, <em>have to</em> vira <strong>HAFTA</strong> (com F!), <em>has to</em> vira <strong>HASTA</strong>, e <em>don&#8217;t have to</em> vira <strong>DOAN-HAFTA</strong>, tudo numa coisa s&#243;. Se sair "have &middot; to", separadinho, est&#225; errado &mdash; mesmo estando certo. N&#227;o &#233; pregui&#231;a: &#233; o ingl&#234;s certo &mdash; e &#233; exatamente por isso que voc&#234; n&#227;o escuta a obriga&#231;&#227;o quando eles falam.</p>')
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
    ("Voc&#234; est&#225; com uma mala grande e a catraca &#233; estreita demais. Voc&#234; pergunta ao agente da esta&#231;&#227;o:",
     [("\"Do I must use another gate?\"", False),
      ("\"Do I have to use another gate? This suitcase doesn't fit through the turnstile.\"", True),
      ("\"I am allowed use another gate?\"", False)]),
    ("Duas plataformas, mesma letra, mesma cor. Voc&#234; tem quatro segundos. A pergunta que salva a viagem &#233;:",
     [("\"Which platform do I have to be on -- uptown or downtown?\"", True),
      ("\"How do I get to Midtown?\" (e ent&#227;o vem uma resposta de quinze segundos que voc&#234; n&#227;o entende)", False),
      ("\"Where is the train?\"", False)]),
    ("Uma turista atr&#225;s de voc&#234; est&#225; na fila da m&#225;quina, prestes a comprar um bilhete que ela n&#227;o precisa. Voc&#234; quer LIBERT&#193;-LA. Voc&#234; diz:",
     [("\"You mustn't buy a ticket -- you can just tap your card.\" (isto a PRO&#205;BE de comprar!)", False),
      ("\"You don't have to buy a ticket -- you can just tap your credit card.\"", True),
      ("\"You can't buy a ticket -- you can just tap your card.\"", False)]),
    ("O motorista do seu rideshare est&#225; parado no n&#237;vel 1, onde o embarque &#233; proibido, e a pol&#237;cia est&#225; mandando os carros circularem. Voc&#234; diz:",
     [("\"You don't have to wait on Level 1 -- you have to come up to Level 2.\"", False),
      ("\"You can't wait on Level 1 -- you have to come up to Level 2. Pickup is only allowed at the curbside upstairs.\"", True),
      ("\"You are not allowed come up to Level 2.\"", False)]),
    ("O agente te deu a linha, a plataforma e a baldea&#231;&#227;o, tudo muito r&#225;pido. Antes de sair andando, voc&#234;:",
     [("Agradece e sai andando, torcendo para ter entendido.", False),
      ("\"Let me check I understood: the E train, downtown platform, no transfer. Is that right?\"", True),
      ("\"Sorry, can you repeat everything again from the beginning?\" (e ele repete igualmente r&#225;pido)", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta. A quest&#227;o 3 &#233; a armadilha da aula: nem toda negativa &#233; um "n&#227;o".</p>')
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
A('        <div class="think-question">Explain the rules of your own factory in Guarulhos to a foreign visitor who has never been there. What does he have to do before he goes in? What does he NOT have to do (careful -- this is the hard one: it means it is optional, not forbidden)? And what is he not allowed to do, under any circumstances? Use have to, don&#8217;t have to, can&#8217;t and be allowed to. This is tonight&#8217;s grammar on the ground where you are the expert -- so take your time, and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-6"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 6</h4>')
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
