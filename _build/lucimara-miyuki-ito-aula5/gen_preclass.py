#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-5 do hub) da Lucimara — aula 5.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
REGRA 29: este Pre-class PREVIEWA a aula 5 IN CLASS (mesmo tema/gramatica/vocab).
REGRA 22: nenhuma palavra das aulas 1-4 volta como vocab card novo. O curriculo pedia
'layover', mas layover JA FOI ENSINADA na aula 2 -> trocada por 'red-eye' (mesmo campo
semantico: o trajeto/o voo), que e nova e serve a viagem de setembro dela.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(5)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Hypothetical", "imagined, not real -- a situation you are only supposing",
     "hipot&#233;tico (imagin&#225;rio, n&#227;o real)",
     "That is a hypothetical question, but I would say yes."),
    ("Would rather", "to prefer one thing to another, when you have to choose",
     "preferir (entre duas op&#231;&#245;es)",
     "I would rather arrive early and be tired than lose a whole day."),
    ("Ideal", "the best possible version of something, in a perfect world",
     "ideal (a vers&#227;o perfeita)",
     "In an ideal world, I would spend three days just walking around Brooklyn."),
    ("Budget", "the money you plan to spend, decided before you spend it",
     "or&#231;amento (o quanto voc&#234; planeja gastar)",
     "We set a budget of three thousand dollars for the week."),
    ("To stretch (a budget)", "to make the money go further than you expected",
     "esticar / fazer render (o or&#231;amento)",
     "If we cooked breakfast at the apartment, we would stretch the budget."),
    ("Red-eye", "an overnight flight that leaves late and lands early in the morning",
     "voo noturno (chega de madrugada)",
     "If I took the red-eye, I would gain a whole day in the city."),
    ("Detour", "a longer way, off the direct route -- and often the better one",
     "desvio (o caminho mais longo)",
     "We took a detour through Brooklyn, and it was the best part of the trip."),
    ("Spontaneous", "decided on the spot, with no plan at all",
     "espont&#226;neo (decidido na hora)",
     "The best night of the trip was completely spontaneous."),
    ("Off the beaten path", "away from the places every tourist goes",
     "fora do circuito tur&#237;stico",
     "If I had one free day, I would go somewhere off the beaten path."),
    ("To splurge", "to spend a lot of money on one special thing, on purpose",
     "gastar alto (em algo especial)",
     "I would splurge on one great dinner, not on the hotel."),
    ("To cut back (on)", "to spend or use less of something, so the money lasts",
     "cortar / reduzir (gastos)",
     "If we cut back on taxis, we would have more money for restaurants."),
    ("To get away", "to travel somewhere to escape your routine, even for a weekend",
     "dar uma escapada (viajar para espairecer)",
     "I need to get away for a few days -- even a long weekend would help."),
]

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-5">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 05 -- Pre-class</div>')
A('      <h3>What Would You Do? -- Dream Trips, Hypotheticals, and the Week You Would Choose</h3>')
A('      <div class="lesson-desc">Na aula 4 a viagem quebrou e voc&#234; consertou. Agora a viagem d&#225; certo &mdash; e a '
  'pergunta muda: se voc&#234; tivesse uma semana livre em Nova York, o que voc&#234; faria com ela? Key words: '
  'hypothetical, would rather, ideal, budget, to stretch (a budget), red-eye, detour, spontaneous, off the beaten '
  'path, to splurge, to cut back, to get away. Structure: <strong>second conditional</strong> &mdash; a gram&#225;tica '
  'do mundo que ainda n&#227;o existe ("<strong>If</strong> I <strong>had</strong> a free week in New York, I '
  '<strong>would walk</strong> a different neighborhood every day." / "<strong>If</strong> I <strong>were</strong> '
  'you, I<strong>&#8217;d</strong> take the ferry.") + <strong>I wish + past simple</strong> ("I <strong>wish</strong> '
  'I <strong>had</strong> more time in this city.").</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras de quem est&#225; decidindo uma viagem: o que voc&#234; faria, o que voc&#234; prefere, onde voc&#234; gastaria mais e onde gastaria menos.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a tradu&#231;&#227;o correta. Aten&#231;&#227;o ao par que confunde: <strong>to splurge</strong> &#233; gastar ALTO de prop&#243;sito, em UMA coisa; <strong>to stretch a budget</strong> &#233; o oposto &mdash; fazer o mesmo dinheiro render mais.</p>')
A('      <div class="match-grid" id="match-l5">')
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
A('        <p>The travel agent asks Lucimara a <strong>hypothetical</strong> question, and it is the only question '
  'that matters: "<strong>If</strong> you <strong>had</strong> one free week in New York, what <strong>would</strong> '
  'you <strong>do</strong> with it?" Nothing is decided yet. The week does not exist. That is exactly why the verb '
  'changes.</p>')
A('        <p style="margin-top:.8rem">She does not hesitate. "<strong>If</strong> I <strong>had</strong> that week, '
  'I <strong>would walk</strong>," she says. "One neighborhood a day, on foot. In an <strong>ideal</strong> world, '
  'I <strong>would spend</strong> three days just in Brooklyn &mdash; somewhere <strong>off the beaten path</strong>, '
  'not another museum." The agent smiles. "<strong>If</strong> I <strong>were</strong> you, I <strong>would take</strong> '
  'the ferry instead of the train. The ferry is a <strong>detour</strong>, and the <strong>detour</strong> is where the '
  'trip actually happens."</p>')
A('        <p style="margin-top:.8rem">Then the flight. "<strong>If</strong> you <strong>took</strong> the '
  '<strong>red-eye</strong> on Saturday, you <strong>would land</strong> at seven in the morning and you '
  '<strong>would gain</strong> a whole day." She thinks for two seconds. "I <strong>would rather</strong> arrive early '
  'and be tired than lose a Sunday." And the money? "<strong>If</strong> I <strong>cut back</strong> on the hotel, I '
  '<strong>could stretch</strong> the <strong>budget</strong> into two great dinners. I <strong>would splurge</strong> '
  'on the food, never on the room."</p>')
A('        <p style="margin-top:.8rem">One evening stays open, with no plan in it at all. Because the best night of her '
  'last trip was completely <strong>spontaneous</strong> &mdash; and you cannot book that. "I <strong>wish</strong> I '
  '<strong>had</strong> more days and fewer plans," she says. "I <strong>wish</strong> I <strong>were</strong> braver '
  'when I travel." And then, the real sentence, the one that has nothing hypothetical about it: in September, she '
  '<strong>is going</strong> to <strong>get away</strong> &mdash; and this time she will do it in English.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. "<strong>If</strong> I <strong>had</strong> one free week, I <strong>would walk</strong>." Por que o verbo depois de <strong>if</strong> est&#225; no PASSADO, se ela est&#225; falando de setembro?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque ela est&#225; contando algo que j&#225; aconteceu.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque o passado aqui n&#227;o marca TEMPO, marca DIST&#194;NCIA da realidade. A semana livre ainda n&#227;o existe &mdash; &#233; imagina&#231;&#227;o. Essa &#233; a regra do second conditional: <strong>if + past simple, would + verbo</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque em ingl&#234;s o futuro sempre usa o passado.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. Qual &#233; a diferen&#231;a entre as duas frases: "<strong>If</strong> my flight <strong>is</strong> canceled, I <strong>will</strong> rebook" (aula 4) e "<strong>If</strong> I <strong>had</strong> a free week, I <strong>would</strong> walk" (hoje)?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A primeira &#233; REAL e pode acontecer amanh&#227; (<strong>will</strong>). A segunda &#233; IMAGINADA &mdash; um mundo que ainda n&#227;o existe (<strong>would</strong>). Mesma palavra <em>if</em>, dist&#226;ncias diferentes.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Nenhuma &mdash; <em>will</em> e <em>would</em> s&#227;o a mesma coisa.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A primeira &#233; formal e a segunda &#233; informal.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "<strong>If</strong> I <strong>were</strong> you, I would take the ferry." Por que <strong>were</strong>, e n&#227;o <strong>was</strong>?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque <em>you</em> &#233; plural.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque no second conditional o verbo <em>to be</em> vira <strong>were</strong> para TODO MUNDO &mdash; I, he, she, it. &#201; a marca de que aquilo N&#195;O &#233; verdade: eu n&#227;o sou voc&#234;.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque <em>was</em> n&#227;o existe em ingl&#234;s americano.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If I would have more time, I would visit the MoMA every day."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "If I had more time, I would visit the MoMA every day &mdash; and I wish I had more time."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "If I have more time, I would visited the MoMA every day."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Second Conditional + I wish (a gram&#225;tica do mundo que n&#227;o existe)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Uma frase, duas metades &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Piece</th><th style="padding:.7rem;text-align:left">Form / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">A condi&#231;&#227;o<br>(if...)</td><td style="padding:.6rem"><strong>if</strong> + PAST SIMPLE. O passado aqui n&#227;o &#233; tempo: &#233; DIST&#194;NCIA da realidade. <strong>Nunca</strong> <em>would</em> nesta metade.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>had</strong> a free week..."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">O resultado</td><td style="padding:.6rem"><strong>would</strong> + verbo na base (sem <em>to</em>). Na fala vira <strong>&#8217;d</strong> &mdash; e quase some.</td><td style="padding:.6rem">"...I <strong>would walk</strong> everywhere." / "I<strong>&#8217;d</strong> walk everywhere."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">to be = <strong>were</strong></td><td style="padding:.6rem">No second conditional, <em>to be</em> vira <strong>were</strong> para TODO MUNDO (I / he / she / it). &#201; a marca do irreal.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>were</strong> you, I&#8217;d take the ferry."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem"><strong>didn&#8217;t</strong> na condi&#231;&#227;o, <strong>wouldn&#8217;t</strong> no resultado.</td><td style="padding:.6rem">"<strong>If</strong> I <strong>didn&#8217;t</strong> have the meeting, I <strong>wouldn&#8217;t</strong> stay in Midtown."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem"><strong>What would</strong> + sujeito + verbo + <strong>if</strong> + past simple? &#201; a pergunta que abre a conversa.</td><td style="padding:.6rem">"<strong>What would</strong> you <strong>do if</strong> you <strong>had</strong> one free week?"</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">would rather</td><td style="padding:.6rem">= prefiro (entre duas op&#231;&#245;es). Depois dele, o verbo vem na BASE &mdash; sem <em>to</em>. O contraste usa <strong>than</strong>.</td><td style="padding:.6rem">"I <strong>would rather</strong> <strong>arrive</strong> early <strong>than</strong> lose a Sunday."</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I wish +<br>past simple</td><td style="padding:.6rem">Voc&#234; quer que o AGORA fosse diferente. Mesmo truque: passado = irreal. N&#227;o &#233; sobre o passado, &#233; sobre hoje.</td><td style="padding:.6rem">"I <strong>wish</strong> I <strong>had</strong> more time." (= but I don&#8217;t) / "I <strong>wish</strong> I <strong>were</strong> braver."</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">first x second<br>(a &#250;nica pergunta)</td><td style="padding:.6rem" colspan="2">Pergunte-se: <strong>isso pode acontecer de verdade?</strong> Se sim &rarr; <em>if</em> + presente + <strong>will</strong> (aula 4: "If my flight is canceled, I <strong>will</strong> rebook."). Se n&#227;o, se &#233; s&#243; imagina&#231;&#227;o &rarr; <em>if</em> + passado + <strong>would</strong> ("If I <strong>had</strong> a free week, I <strong>would</strong> walk."). O <em>if</em> &#233; o mesmo. O que muda &#233; a dist&#226;ncia.</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (os dois erros cl&#225;ssicos, e os dois v&#234;m do portugu&#234;s):</strong> (1) <em>would</em> depois de <em>if</em>: em portugu&#234;s dizemos "se eu TIVESSE mais tempo, eu VISITARIA" &mdash; e a cabe&#231;a quer p&#244;r um <em>would</em> nas DUAS metades: "if I <s>would have</s> more time". O ingl&#234;s TRAVA: <em>would</em> mora S&#211; na metade do resultado. Depois de <em>if</em>, passado simples, sempre. (2) <em>was</em> no lugar de <em>were</em>: "if I <s>was</s> you" &#233; o erro mais comum do mundo &mdash; e a forma correta, a que soa a ingl&#234;s de verdade, &#233; <strong>if I were you</strong>. Guarde essa frase inteira, como um bloco.</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("had", "Dica: depois de <em>if</em>, PAST SIMPLE &mdash; nunca would",
     "If I had a free week in New York, I would walk everywhere.",
     '"If I ', ' a free week in New York, I would walk everywhere."'),
    ("would visit", "Dica: esta &#233; a metade do RESULTADO &mdash; aqui sim entra o would (duas palavras)",
     "If I had more time, I would visit the MoMA every day.",
     '"If I had more time, I ', ' the MoMA every day."'),
    ("were", "Dica: no second conditional o verbo to be vira a MESMA forma para todo mundo",
     "If I were you, I would take the ferry instead of the train.",
     '"If I ', ' you, I would take the ferry instead of the train."'),
    ("would rather", "Dica: duas palavras &mdash; o jeito de dizer que voc&#234; PREFERE uma op&#231;&#227;o",
     "I would rather arrive early and be tired than lose a whole day.",
     '"I ', ' arrive early and be tired than lose a whole day."'),
    ("wish", "Dica: uma palavra s&#243;, para dizer que voc&#234; queria que o AGORA fosse diferente",
     "I wish I had more time in this city.",
     '"I ', ' I had more time in this city."'),
    ("red-eye", "Dica: o voo que sai tarde da noite e chega de madrugada",
     "If I took the red-eye, I would gain a whole day in the city.",
     '"If I took the ', ', I would gain a whole day in the city."'),
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
    (3, "Choose where to splurge and where to cut back: the food, not the room."),
    (1, "Answer the big question: if you had one free week, what would you do?"),
    (5, "Leave one evening completely open -- no plan, on purpose."),
    (2, "Pick the flight: the red-eye, and gain a whole day in the city."),
    (4, "Take the ferry instead of the train, and let the detour happen."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Build the Perfect Week, in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Como se planeja uma semana dos sonhos, na ordem em que as decis&#245;es realmente acontecem &mdash; da pergunta at&#233; a noite que voc&#234; deixa em branco.</p>')
A('      <div class="order-container" id="order-l5">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l5\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    ("If I had a free week in New York, I would walk a different neighborhood every day.",
     "Se eu tivesse uma semana livre em Nova York, eu caminharia por um bairro diferente todo dia."),
    ("If I were you, I'd take the ferry instead of the train.",
     "Se eu fosse voc&#234;, eu pegaria a balsa em vez do trem."),
    ("I would rather arrive early and be tired than lose a whole day.",
     "Eu prefiro chegar cedo e cansada a perder um dia inteiro."),
    ("I wish I had more time in this city.",
     "Eu queria ter mais tempo nesta cidade."),
    ("If we cut back on the hotel, we could stretch the budget into two great dinners.",
     "Se a gente cortasse no hotel, dava para esticar o or&#231;amento em dois jantares &#243;timos."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. O alvo de hoje &#233; UM som: o <strong>would</strong> encolhido. Na boca de um americano, <em>I would</em> vira <strong>I&#8217;d</strong> (uma s&#237;laba s&#243;), <em>she would</em> vira <strong>she&#8217;d</strong>, <em>we would</em> vira <strong>we&#8217;d</strong>. E <em>&#8220;If I were you, I&#8217;d&#8230;&#8221;</em> sai colado, quase como uma palavra s&#243;. N&#227;o &#233; pregui&#231;a: &#233; o ingl&#234;s certo &mdash; e &#233; por isso que voc&#234; n&#227;o escuta o <em>would</em> quando eles falam.</p>')
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
    ("O agente de viagens pergunta: <em>&#8220;If you had one free week in New York, what would you do?&#8221;</em> Qual resposta est&#225; correta?",
     [("\"If I have one free week, I will walk a different neighborhood every day.\"", False),
      ("\"If I had one free week, I would walk a different neighborhood every day.\"", True),
      ("\"If I would have one free week, I would walk a different neighborhood every day.\"", False)]),
    ("Voc&#234; quer dizer que prefere o voo noturno a perder um domingo. Voc&#234; diz:",
     [("\"I would rather take the red-eye than lose a Sunday.\"", True),
      ("\"I would rather to take the red-eye than lose a Sunday.\"", False),
      ("\"I would rather taking the red-eye that lose a Sunday.\"", False)]),
    ("O or&#231;amento &#233; bom, mas n&#227;o infinito. Voc&#234; decide gastar alto no jantar e economizar no hotel. Voc&#234; diz:",
     [("I would <strong>cut back</strong> on the dinners and <strong>splurge</strong> on the room.", False),
      ("I would <strong>splurge</strong> on the food and <strong>cut back</strong> on the hotel &mdash; that way we <strong>stretch</strong> the budget.", True),
      ("I would <strong>stretch</strong> the dinners and <strong>splurge</strong> the budget.", False)]),
    ("Qual frase est&#225; correta?",
     [("\"If I was you, I would stay in Brooklyn.\"", False),
      ("\"If I were you, I would stay in Brooklyn.\"", True),
      ("\"If I am you, I would stay in Brooklyn.\"", False)]),
    ("Cuidado &mdash; esta &#233; REAL, pode acontecer amanh&#227;: seu voo pode ser cancelado. Qual frase serve?",
     [("\"If my flight is canceled, I will rebook at the desk.\"", True),
      ("\"If my flight was canceled, I would rebook at the desk.\"", False),
      ("\"If my flight would be canceled, I will rebook at the desk.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta. A &#250;ltima &#233; uma armadilha de prop&#243;sito: nem todo <em>if</em> pede <em>would</em>.</p>')
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
A('        <div class="think-question">Plan your perfect week in New York, out loud. If you had seven free days in September, and the budget were generous but not unlimited, what would you do each day? Be specific: name a neighborhood, a kind of restaurant, one thing you would do that is off the beaten path. Say where you would splurge and where you would cut back. Then finish with two wishes: "I wish I had..." and "I wish I were..." Take your time and do not read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-5"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 5</h4>')
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
