#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html (bloco ex-lesson-1 do hub) da Lucimara — aula 1.

REGRA 4: as 5 etapas obrigatorias (1.1 vocab, 1.2 matching, 1.3 grammar in context,
1.4 grammar tip, 1.5 fill-in) + Stage 2 (ordering), Stage 3 (pronuncia), Stage 4 (quiz
situacional), Stage 5 (producao livre) + survival card.
REGRA 24: as opcoes do dropdown saem EMBARALHADAS (ordem != ordem das palavras).
REGRA 7.1: todo texto de audio vai em data-speak="...", nunca dentro de string JS.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preclass.html')
random.seed(55)  # deterministico

# (word, definicao EN, traducao PT, exemplo)
VOCAB = [
    ("Industry", "a group of companies that make the same kind of product",
     "ind&#250;stria / setor", "I work in the chemical industry."),
    ("Supplier", "a company that sells you the materials you need",
     "fornecedor", "Most of our suppliers are in China."),
    ("Regulatory", "connected to the official rules a product must follow",
     "regulat&#243;rio (Anvisa)", "I am responsible for regulatory affairs."),
    ("Trade fair", "a big event where companies show their products to buyers",
     "feira de neg&#243;cios", "I go to a trade fair in Lyon every November."),
    ("Headquarters", "the main office of a company, where the leadership sits",
     "sede / matriz", "Our headquarters is in Guarulhos."),
    ("To negotiate", "to talk with someone until you both agree on a price or a deal",
     "negociar", "I negotiate prices with our Chinese partners."),
    ("Commute", "the trip you make between home and work",
     "trajeto casa-trabalho", "My commute takes forty minutes each way."),
    ("Fluent", "able to speak a language easily, without stopping to think",
     "fluente", "I want to be fluent before my next trip."),
    ("Confident", "sure that you can do something well",
     "confiante / seguro", "I feel confident when I read, but not when I listen."),
    ("Stuck", "not able to move forward, because something is blocking you",
     "travado / empacado", "I get stuck when people speak very fast."),
    ("To catch", "to hear and understand what somebody said",
     "captar / entender o que foi dito", "Sorry, I didn't catch that."),
    ("Abroad", "in or to another country",
     "no exterior / fora do pa&#237;s", "I travel abroad every two or three months."),
]

VOL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
       '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
       '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

p = []
A = p.append

A('<div class="lesson-card" id="ex-lesson-1">')
A('  <div class="lesson-header" onclick="toggleLesson(this)">')
A('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=600&q=80\')"></div>')
A('    <div class="lesson-header-content">')
A('      <div class="lesson-number">Aula 01 -- Pre-class</div>')
A('      <h3>Who Is Lucimara? -- Diagnostic Session and Personal Introduction</h3>')
A('      <div class="lesson-desc">Apresentar-se e falar do seu trabalho numa feira internacional em Nova York. '
  'Key words: industry, supplier, regulatory, trade fair, headquarters, negotiate, commute, fluent, confident, '
  'stuck, catch, abroad. Structures: present simple (rotina) vs present continuous (agora) vs present perfect '
  '(for/since). E as frases que salvam qualquer conversa quando voc&#234; n&#227;o entende o que o outro disse.</div>')
A('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>')
A('    </div>')
A('    <div class="expand-icon">&#9660;</div>')
A('  </div>')
A('  <div class="lesson-body">')

# ---------- Stage 1.1 — Vocabulary cards ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Sem pressa &mdash; ou&#231;a duas vezes, repita em voz alta. S&#227;o as doze palavras que descrevem o seu trabalho e a sua rotina.</p>')
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
A('      <div class="match-grid" id="match-l1">')
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
A('        <p>Lucimara <strong>is</strong> a director in the chemical <strong>industry</strong>. She <strong>works</strong> in Guarulhos, '
  'where the company <strong>headquarters</strong> <strong>is</strong>, and she <strong>lives</strong> in Perdizes, so her <strong>commute</strong> '
  '<strong>takes</strong> forty minutes each way. Every month she <strong>negotiates</strong> prices with <strong>suppliers</strong> in China, and '
  'twice a year she <strong>goes</strong> to a <strong>trade fair</strong> <strong>abroad</strong>. "I <strong>have worked</strong> in this industry '
  '<strong>for</strong> twenty years," she says, "and I <strong>have been</strong> a director <strong>since</strong> 2015." Right now, her team '
  '<strong>is preparing</strong> a new product registration, and she <strong>is studying</strong> English again, because in September she '
  '<strong>is going</strong> to New York. She <strong>reads</strong> <strong>regulatory</strong> documents in English without a problem and she '
  '<strong>feels</strong> <strong>confident</strong> on the phone with old partners. But when an American speaks fast, she <strong>gets</strong> '
  '<strong>stuck</strong>: she <strong>does not catch</strong> the end of the sentence. She <strong>wants</strong> to be <strong>fluent</strong> &mdash; '
  'and, more than that, she <strong>wants</strong> to understand.</p>')
A('      </div>')
A('      <div class="quiz-item"><div class="quiz-question">1. Por que dizemos "I <strong>have worked</strong> in this industry for twenty years" e n&#227;o "I work in this industry for twenty years"?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque come&#231;ou no passado e CONTINUA at&#233; hoje &mdash; present perfect com <strong>for</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque terminou e n&#227;o tem mais liga&#231;&#227;o com o presente.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque &#233; uma rotina que ela repete toda semana.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">2. "Right now, her team <strong>is preparing</strong> a new product registration." Por que present continuous?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque acontece todos os dias, e a rotina dela.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque est&#225; acontecendo AGORA, neste per&#237;odo &mdash; n&#227;o &#233; a rotina de sempre.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque come&#231;ou h&#225; vinte anos e continua.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">3. "She <strong>has been</strong> a director <strong>since</strong> 2015." O que essa frase diz?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Ela foi diretora em 2015 e depois deixou o cargo.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Ela virou diretora em 2015 e AINDA &#233; diretora hoje.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ela vai virar diretora em 2015.</div></div></div>')
A('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her routine is correct?</div><div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She is negotiating with suppliers every month."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She negotiates with suppliers every month, and her commute takes forty minutes."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She has negotiated with suppliers every month since twenty years."</div></div></div>')
A('    </div>')

# ---------- Stage 1.4 — Grammar Tip ----------
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Simple vs Present Continuous vs Present Perfect (for / since)</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">As tr&#234;s estruturas que sustentam qualquer apresenta&#231;&#227;o pessoal em ingl&#234;s &mdash; explica&#231;&#227;o em ingl&#234;s e portugu&#234;s.</p>')
A('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
A('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
A('        <tbody>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / you / we + verb (he/she + s)</td><td style="padding:.6rem">Rotina, cargo, o que &#233; sempre verdade. Routine and permanent facts.</td><td style="padding:.6rem">I <strong>work</strong> in the chemical industry.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Continuous<br>am / is / are + verb-ing</td><td style="padding:.6rem">O que est&#225; acontecendo AGORA, neste m&#234;s. Not the routine &mdash; happening now.</td><td style="padding:.6rem">Right now, I <strong>am preparing</strong> a registration.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + past participle</td><td style="padding:.6rem">Come&#231;ou no passado e CONTINUA hoje. Duration up to now (for / since).</td><td style="padding:.6rem">I <strong>have worked</strong> here for twenty years.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem">have / has + not + partic&#237;pio. Na fala, contra&#237;do: <strong>haven\'t</strong>.</td><td style="padding:.6rem">I <strong>haven\'t</strong> been to Lyon this year.</td></tr>')
A('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">How long + have + sujeito + partic&#237;pio?</td><td style="padding:.6rem"><strong>How long have you been</strong> in the industry?</td></tr>')
A('          <tr><td style="padding:.6rem;font-weight:600">for vs since</td><td style="padding:.6rem" colspan="2"><strong>for</strong> + per&#237;odo (for twenty years) &middot; <strong>since</strong> + ponto de partida (since 2015)</td></tr>')
A('        </tbody>')
A('      </table></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro cl&#225;ssico do brasileiro):</strong> em portugu&#234;s dizemos "trabalho aqui <strong>h&#225;</strong> vinte anos" e "sou diretora <strong>desde</strong> 2015" &mdash; os dois no PRESENTE. Em ingl&#234;s, dura&#231;&#227;o at&#233; hoje <strong>nunca</strong> usa o present simple: "I work here for twenty years" est&#225; errado. O certo &#233; "I <strong>have worked</strong> here for twenty years" (na fala, <strong>I\'ve worked</strong>). E lembre: <strong>responsible FOR</strong>, nunca "responsible of".</p>')
A('    </div>')

# ---------- Stage 1.5 — Fill in the blank ----------
BLANKS = [
    ("have worked", "Dica: come&#231;ou h&#225; 20 anos e CONTINUA &mdash; have + partic&#237;pio",
     "I have worked in the chemical industry for twenty years.",
     '"I ', ' in the chemical industry for twenty years."'),
    ("am preparing", "Dica: est&#225; acontecendo agora, neste m&#234;s &mdash; am + verbo-ing",
     "Right now, I am preparing a new product registration.",
     '"Right now, I ', ' a new product registration."'),
    ("negotiate", "Dica: rotina, todo m&#234;s &mdash; present simple",
     "Every month, I negotiate prices with our suppliers in China.",
     '"Every month, I ', ' prices with our suppliers in China."'),
    ("for", "Dica: per&#237;odo de tempo (twenty years)",
     "I have been in this industry for twenty years.",
     '"I have been in this industry ', ' twenty years."'),
    ("since", "Dica: ponto de partida (2015)",
     "I have been a director since 2015.",
     '"I have been a director ', ' 2015."'),
    ("catch", "Dica: ouvir E entender o que a pessoa disse",
     "Sorry, I didn't catch that. Could you say it again more slowly?",
     '"Sorry, I didn\'t ', ' that. Could you say it again more slowly?"'),
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
    (3, "Say what you do: your job, your industry and what you are responsible for."),
    (5, "Agree on a next step: exchange cards and set a time to meet."),
    (1, "Say hello and introduce yourself: your name and your company."),
    (4, "Ask HIM a question: what does his company do, and what is he looking for?"),
    (2, "Say how long you have been in the industry, with for or since."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Voc&#234; acabou de conhecer algu&#233;m numa feira internacional. Coloque as etapas da conversa na ordem natural.</p>')
A('      <div class="order-container" id="order-l1">')
for n, t in ORDER:
    A(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l1\')">'
      f'<span class="order-num">?</span><span class="order-text">{t}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button></span></div>')
A('      </div>')
A('      <button class="verify-all-btn" onclick="checkOrder(\'order-l1\')">Check Order</button>')
A('    </div>')

# ---------- Stage 3 — Pronunciation ----------
SPEECH = [
    ("I'm a director in the chemical industry, and I'm responsible for production.",
     "Sou diretora na ind&#250;stria qu&#237;mica e sou respons&#225;vel pela produ&#231;&#227;o."),
    ("I've worked in this industry for twenty years.",
     "Trabalho nesta ind&#250;stria h&#225; vinte anos."),
    ("Right now, I'm preparing a new product registration.",
     "Neste momento, estou preparando um novo registro de produto."),
    ("Sorry, I didn't catch that. Could you say it again more slowly?",
     "Desculpe, n&#227;o captei. Voc&#234; poderia repetir mais devagar?"),
    ("I travel abroad every two or three months, mostly to New York.",
     "Viajo para o exterior a cada dois ou tr&#234;s meses, principalmente para Nova York."),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a a frase, repita em voz alta, e s&#243; ent&#227;o grave. Pode ouvir e regravar quantas vezes quiser &mdash; a repeti&#231;&#227;o &#233; o m&#233;todo, n&#227;o um sinal de dificuldade.</p>')
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
    ("Numa feira em Nova York, algu&#233;m pergunta: \"So, what do you do?\" Voc&#234; responde:",
     [("\"I do the chemical things in a company.\"", False),
      ("\"I'm a director in the chemical industry, and I'm responsible for production and regulatory affairs.\"", True),
      ("\"I am responsible of the production since twenty years.\"", False)]),
    ("Ele pergunta: \"How long have you been in the industry?\" A melhor resposta &#233;:",
     [("\"I am in this industry for twenty years.\"", False),
      ("\"I've worked in this industry for twenty years.\"", True),
      ("\"I work in this industry since twenty years.\"", False)]),
    ("Voc&#234; quer falar do projeto que est&#225; em andamento NESTE m&#234;s. Qual est&#225; correta?",
     [("\"Right now, we're preparing a new product registration.\"", True),
      ("\"Right now, we prepare a new product registration.\"", False),
      ("\"Right now, we have prepared a new product registration.\"", False)]),
    ("O americano fala r&#225;pido e voc&#234; perde o final da frase. O movimento mais profissional &#233;:",
     [("Sorrir, concordar com a cabe&#231;a e torcer para ningu&#233;m perceber.", False),
      ("\"Sorry, I didn't catch that. Could you say it again more slowly?\"", True),
      ("Pedir desculpas pelo seu ingl&#234;s e mudar de assunto.", False)]),
    ("Voc&#234; quer confirmar que entendeu o combinado. Voc&#234; diz:",
     [("\"Yes, yes, ok, ok.\"", False),
      ("\"Let me check I understood. You need the bio by Friday, right?\"", True),
      ("\"I don't know, sorry.\"", False)]),
]
A('')
A('    <div class="exercise-section">')
A('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma viagem ou de uma feira internacional.</p>')
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
A('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o existe resposta certa ou errada &mdash; fale por 90 segundos, sem script. Esta grava&#231;&#227;o &#233; o seu BASELINE: vamos ouvi-la de novo na aula 24 e na aula 48, e voc&#234; vai ouvir a diferen&#231;a com os seus pr&#243;prios ouvidos.</p>')
A('      <div class="think-card">')
A('        <div class="think-question">You are at an international trade fair in New York and someone you have never met says hello. Introduce yourself: your name, your job in the chemical industry (present simple), what you are responsible for, how long you have been in the industry (present perfect, for / since), and what your team is working on this month (present continuous). Finish by saying how often you travel abroad. Take your time and don\'t read from a script.</div>')
A('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
A('        <div id="think-result-1"></div>')
A('      </div>')
A('    </div>')

# ---------- Survival card ----------
A('')
A('    <div class="survival-card">')
A('      <h4>Survival Card -- Lesson 1</h4>')
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
