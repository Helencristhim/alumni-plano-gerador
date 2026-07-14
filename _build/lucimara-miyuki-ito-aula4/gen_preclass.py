#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-4 do hub) da Lucimara — aula 4.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 4 IN CLASS (mesmo tema/gramatica/vocab).
REGRA 22: nenhuma palavra das aulas 1-3 volta como vocab card novo.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(4)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Overbooked", "when a flight or a hotel has sold more seats or rooms than it really has",
     "com overbooking (mais vendas do que lugares)",
     "The flight is overbooked, so somebody has to take a later one."),
    ("Delay notice", "the message that tells you your flight will leave later than planned",
     "aviso de atraso", "I got the delay notice on my phone before I left the hotel."),
    ("To rebook", "to change your reservation to a different flight or a different day",
     "remarcar (a passagem)", "If they cancel the flight, they will rebook me at no extra cost."),
    ("Voucher", "a paper or a code that pays for one thing: a meal, a hotel, a taxi",
     "voucher / vale", "The airline gave me a voucher for dinner at the terminal."),
    ("Compensation", "extra money a company must pay you because it made you lose time",
     "indeniza&#231;&#227;o (pelo transtorno)",
     "After a six-hour delay, you can ask the airline for compensation."),
    ("Refund", "your money back, because you did not get the service you paid for",
     "reembolso (o dinheiro de volta)",
     "If they cancel the flight and I don't fly, I will request a refund."),
    ("Travel insurance", "a policy that pays you back when the trip goes wrong: illness, lost bags, canceled flights",
     "seguro viagem", "My travel insurance covers a night in a hotel near the airport."),
    ("Alternative route", "a different way to reach the same place, when the first way is closed",
     "rota alternativa", "There is no direct flight tonight, so we will find an alternative route."),
    ("Complaint", "a formal statement that says, in writing, that something went wrong",
     "reclama&#231;&#227;o formal", "She filed a complaint with the airline the same night."),
    ("To sort out", "to solve a problem, step by step, until it is finished",
     "resolver (passo a passo)", "Don't worry -- the agent will sort it out before midnight."),
    ("To end up", "to be in a situation you did not plan, after everything changed",
     "acabar (numa situa&#231;&#227;o n&#227;o planejada)",
     "I ended up sleeping in a hotel two minutes from the terminal."),
    ("To board", "to get on the plane, when they finally call your row",
     "embarcar", "We will board in twenty minutes at gate B twelve."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-4">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1530521954074-e64f6810b32d?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 04 -- Pre-class</div>')
A('      <h3>If I Miss My Flight -- Handling Problems, Contingencies, and Unexpected Situations</h3>')
A('      <div class="lesson-desc">O painel fica vermelho em Miami: voo cancelado, fila de sessenta pessoas, e uma '
  'reuni&#227;o em Manhattan &#224;s nove da manh&#227;. Key words: overbooked, delay notice, to rebook, voucher, '
  'compensation, refund, travel insurance, alternative route, complaint, to sort out, to end up, to board. '
  'Structure: <strong>first conditional</strong> &mdash; a gram&#225;tica do plano B '
  '("<strong>If</strong> the flight <strong>is</strong> canceled, I <strong>will ask</strong> for a voucher." / '
  '"<strong>Unless</strong> they rebook me, I&#8217;ll end up sleeping at the airport." / '
  '"I&#8217;ll be fine <strong>as long as</strong> I board before midnight.").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras que voc&#234; nunca vai precisar &mdash; at&#233; a noite em que vai precisar das doze ao mesmo tempo.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a tradu&#231;&#227;o correta. Aten&#231;&#227;o ao par que confunde todo mundo: <strong>refund</strong> &#233; o SEU dinheiro de volta; <strong>compensation</strong> &#233; dinheiro A MAIS, pelo transtorno.</p>')
A('      <div class="match-grid" id="match-l4">')
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
A('        <p>It is seven in the evening in Miami, and the board turns red. The <strong>delay notice</strong> '
  'arrived an hour ago, and now the flight to New York is canceled. Lucimara does not panic. She builds a plan '
  'in her head, and the plan is a sentence: <strong>if</strong> the line <strong>is</strong> too long, she '
  '<strong>will call</strong> the airline while she waits.</p>')
A('        <p style="margin-top:.8rem">At the desk, the agent says the next direct flight is '
  '<strong>overbooked</strong>. She does not accept the first no. "<strong>If</strong> you <strong>can</strong> '
  'get me into JFK before eight, I <strong>will take</strong> any route," she says. It is an '
  '<strong>alternative route</strong>, through Charlotte, and it works. "I <strong>will be</strong> fine '
  '<strong>as long as</strong> I <strong>am</strong> in Manhattan by eight."</p>')
A('        <p style="margin-top:.8rem">The agent <strong>rebooks</strong> her and gives her a meal '
  '<strong>voucher</strong> and a hotel <strong>voucher</strong>. There is one condition, and it is the only '
  'thing that matters tonight: <strong>unless</strong> she <strong>checks in</strong> at the counter before '
  'four thirty, the system <strong>will release</strong> her seat. So she sets three alarms. She '
  '<strong>ends up</strong> eating a bad sandwich at eleven at night, in a terminal she never planned to see, '
  'but her <strong>travel insurance</strong> <strong>will cover</strong> the hotel.</p>')
A('        <p style="margin-top:.8rem">Tomorrow she <strong>will file</strong> a <strong>complaint</strong>, '
  'and <strong>if</strong> the airline <strong>agrees</strong>, she <strong>will get</strong> '
  '<strong>compensation</strong> &mdash; and a <strong>refund</strong> for the segment she never flew. But '
  'tonight only one thing counts: she <strong>sorted it out</strong> in English, and she '
  '<strong>will board</strong> at five in the morning.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "<strong>If</strong> you <strong>can</strong> get me into JFK before eight, I <strong>will take</strong> any route." Por que o verbo depois de <strong>if</strong> est&#225; no presente, se ela est&#225; falando do FUTURO?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque ela est&#225; falando de agora, n&#227;o do futuro.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque essa &#233; a regra de ferro do first conditional: depois de <strong>if</strong>, o verbo fica no PRESENTE. O <strong>will</strong> vive na OUTRA metade da frase (o resultado).</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque em ingl&#234;s o futuro n&#227;o existe.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "<strong>Unless</strong> she checks in before four thirty, the system will release her seat." O que <strong>unless</strong> significa aqui?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> <strong>If not</strong> &mdash; ou seja: SE ela N&#195;O fizer o check-in at&#233; 4h30, ela perde o assento. A negativa j&#225; est&#225; DENTRO do <em>unless</em>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> <strong>Because</strong> &mdash; ela perde o assento porque fez o check-in.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> <strong>Until</strong> &mdash; ela tem que esperar at&#233; as 4h30.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "I will be fine <strong>as long as</strong> I <strong>am</strong> in Manhattan by eight." O que <em>as long as</em> faz nessa frase?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Fala de dura&#231;&#227;o: ela vai ficar bem por muito tempo.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Fixa a &#218;NICA condi&#231;&#227;o que importa: chegar em Manhattan at&#233; as oito. Se isso acontecer, o resto (a rota, a hora do voo, o hotel) tanto faz.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Faz uma compara&#231;&#227;o entre dois voos.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If the flight will be canceled, I will ask for a voucher."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Unless they don\'t rebook me, I will file a complaint."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "If the flight is canceled, I will ask for a voucher &mdash; and unless they rebook me tonight, I\'ll file a complaint."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- First Conditional (a gram&#225;tica do plano B)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Uma frase, duas metades &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Piece</th><th style="padding:.7rem;text-align:left">Form / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">A condi&#231;&#227;o<br>(if...)</td><td style="padding:.6rem"><strong>if</strong> + PRESENTE SIMPLES. <strong>Nunca</strong> <em>will</em> aqui &mdash; mesmo falando de amanh&#227;.</td><td style="padding:.6rem">"<strong>If</strong> the flight <strong>is</strong> canceled..."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">O resultado</td><td style="padding:.6rem"><strong>will</strong> + verbo na base (sem <em>to</em>). Na fala vira <strong>&#8217;ll</strong>.</td><td style="padding:.6rem">"...I <strong>will ask</strong> for a voucher." / "I<strong>&#8217;ll</strong> ask."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem">Nas duas metades: <strong>doesn&#8217;t / don&#8217;t</strong> na condi&#231;&#227;o, <strong>won&#8217;t</strong> no resultado.</td><td style="padding:.6rem">"<strong>If</strong> my bag <strong>doesn&#8217;t</strong> arrive, I <strong>won&#8217;t</strong> have a suit for the fair."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem"><strong>Will</strong> + sujeito + verbo + <strong>if</strong> + presente? &#201; a pergunta que voc&#234; faz no balc&#227;o.</td><td style="padding:.6rem">"<strong>Will</strong> I <strong>get</strong> a hotel voucher <strong>if</strong> the flight <strong>is</strong> canceled?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">unless</td><td style="padding:.6rem">= <strong>if not</strong>. A negativa J&#193; EST&#193; dentro dele &mdash; por isso o verbo depois vem na AFIRMATIVA.</td><td style="padding:.6rem">"<strong>Unless</strong> they <strong>rebook</strong> me, I&#8217;ll file a complaint."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">as long as<br>provided that</td><td style="padding:.6rem">= a &#218;NICA condi&#231;&#227;o que importa. Mesma gram&#225;tica do <em>if</em>: presente depois.</td><td style="padding:.6rem">"I&#8217;ll be fine <strong>as long as</strong> I <strong>board</strong> before midnight."</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">A ordem<br>e a v&#237;rgula</td><td style="padding:.6rem" colspan="2">As duas metades podem trocar de lugar. V&#237;rgula <strong>s&#243;</strong> quando a condi&#231;&#227;o abre a frase: "<strong>If</strong> it is delayed<strong>,</strong> I will ask." / "I will ask <strong>if</strong> it is delayed." (sem v&#237;rgula)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (os dois erros cl&#225;ssicos, e os dois vem do portugu&#234;s):</strong> (1) <em>will</em> depois de <em>if</em>: em portugu&#234;s dizemos "SE o voo ESTIVER atrasado" &mdash; o futuro do subjuntivo SOA a futuro, e a cabe&#231;a traduz para "if the flight <s>will be</s> delayed". O ingl&#234;s TRAVA: depois de <em>if</em>, presente, sempre. (2) Dupla negativa com <em>unless</em>: "unless they <s>don&#8217;t</s> rebook me" quer dizer, ao p&#233; da letra, "se eles N&#195;O N&#195;O me remarcarem" &mdash; o contr&#225;rio do que voc&#234; queria dizer. <em>Unless</em> j&#225; &#233; <em>if not</em>: o verbo depois dele vem na AFIRMATIVA.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("is", "Dica: depois de <em>if</em>, o verbo fica no PRESENTE &mdash; nunca com will",
     "If the flight is canceled, I will ask for a voucher.",
     '"If the flight ', ' canceled, I will ask for a voucher."'),
    ("will ask", "Dica: esta &#233; a metade do RESULTADO &mdash; aqui sim entra o will",
     "If my flight is delayed, I will ask for compensation.",
     '"If my flight is delayed, I ', ' for compensation."'),
    ("Unless", "Dica: uma palavra s&#243;, que j&#225; significa <em>if not</em>",
     "Unless they rebook me tonight, I will end up sleeping at the airport.",
     '"', ' they rebook me tonight, I will end up sleeping at the airport."'),
    ("as long as", "Dica: tr&#234;s palavras &mdash; a &#218;NICA condi&#231;&#227;o que importa",
     "I will be fine as long as I board before midnight.",
     '"I will be fine ', ' I board before midnight."'),
    ("voucher", "Dica: o papel que paga o jantar e o hotel &mdash; n&#227;o &#233; dinheiro",
     "The airline gave me a voucher for dinner at the terminal.",
     '"The airline gave me a ', ' for dinner at the terminal."'),
    ("refund", "Dica: o SEU dinheiro de volta (n&#227;o &#233; a indeniza&#231;&#227;o)",
     "If they cancel the flight and I do not fly, I will request a refund.",
     '"If they cancel the flight and I don\'t fly, I will request a ', '."'),
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
    (4, "Take the hotel voucher and find the shuttle at door three."),
    (2, "Ask the agent for the options and offer a condition: any route before eight."),
    (5, "Set three alarms -- check-in at the counter closes at four thirty."),
    (1, "Read the delay notice on your phone and walk to the desk."),
    (3, "Accept the alternative route through Charlotte and confirm the times out loud."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Long Night in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">A noite em que o voo cai. Coloque as etapas na ordem real &mdash; do aviso no celular at&#233; o despertador do hotel.</p>')
A('      <div class="order-container" id="order-l4">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l4\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    ("My flight has been canceled. What are my options tonight?",
     "Meu voo foi cancelado. Quais s&#227;o as minhas op&#231;&#245;es hoje &#224; noite?"),
    ("If you can get me there before eight, I'll take any route.",
     "Se voc&#234; conseguir me colocar l&#225; antes das oito, eu pego qualquer rota."),
    ("Will I get a meal voucher and a hotel voucher for tonight?",
     "Eu vou receber um voucher de refei&#231;&#227;o e um de hotel para hoje?"),
    ("Unless there is a seat tonight, I'll end up sleeping at the airport.",
     "A n&#227;o ser que tenha um assento hoje, eu vou acabar dormindo no aeroporto."),
    ("I'd like to file a complaint and request compensation.",
     "Eu gostaria de abrir uma reclama&#231;&#227;o e pedir indeniza&#231;&#227;o."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. Aten&#231;&#227;o &#224; s&#237;laba t&#244;nica, que em ingl&#234;s derruba a palavra inteira quando cai no lugar errado: <em>voucher</em> (VOW-cher, o VOU rima com NOW), <em>compensation</em> (com-pen-SAY-shun), <em>insurance</em> (in-SHOOR-ans), <em>complaint</em> (com-PLAYNT, com o T final aud&#237;vel). E o <em>I&#8217;ll</em> quase some na fala r&#225;pida &mdash; e est&#225; certo assim.</p>')
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
    ("O painel diz CANCELED e voc&#234; chega ao balc&#227;o. Qual &#233; a PRIMEIRA frase?",
     [("\"This is absurd! I have a meeting tomorrow!\"", False),
      ("\"Good evening. My flight to New York has been canceled. What are my options tonight?\"", True),
      ("\"I want to speak with your manager, please.\"", False)]),
    ("O agente diz que o pr&#243;ximo voo direto est&#225; <strong>overbooked</strong>. Voc&#234; oferece uma condi&#231;&#227;o:",
     [("\"If you can get me into JFK before eight, I'll take any route.\"", True),
      ("\"If you will get me into JFK before eight, I take any route.\"", False),
      ("\"When you get me into JFK, I take any route.\"", False)]),
    ("Voc&#234; vai esperar sete horas em Miami. O que a companhia DEVE a voc&#234;?",
     [("Nada &mdash; atraso &#233; risco do passageiro.", False),
      ("Um <strong>voucher</strong> de refei&#231;&#227;o e, com espera longa, um <strong>voucher</strong> de hotel &mdash; mas voc&#234; precisa PEDIR.", True),
      ("Uma passagem nova de gra&#231;a para qualquer destino do mundo.", False)]),
    ("Voc&#234; n&#227;o voou e quer o dinheiro da passagem de volta. Voc&#234; pede um:",
     [("<strong>compensation</strong> &mdash; porque a companhia te fez perder tempo.", False),
      ("<strong>refund</strong> &mdash; o dinheiro do servi&#231;o que voc&#234; pagou e n&#227;o recebeu.", True),
      ("<strong>voucher</strong> &mdash; um vale para gastar no aeroporto.", False)]),
    ("Qual frase est&#225; correta?",
     [("\"Unless they don't rebook me, I will file a complaint.\"", False),
      ("\"Unless they rebook me tonight, I'll end up sleeping at the airport.\"", True),
      ("\"Unless they will rebook me, I end up sleeping at the airport.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da noite em que a viagem quebra.</p>')
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
A('        <div class="think-question">Build your plan B for September, out loud. Your flight to New York is delayed in Miami, and your meeting is at nine the next morning. What will you do? Use at least five conditional sentences: "If the flight is canceled, I will..." / "Unless they rebook me tonight, I will..." / "As long as I land before eight, I will be fine." / "If my bag doesn\'t arrive, I will..." / "If the hotel asks for a credit card, I will..." Then finish with the real question: what is the one thing that would still scare you at that desk, in English?</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-4"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 4</h4>')
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
