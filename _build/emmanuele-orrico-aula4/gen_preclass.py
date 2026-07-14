#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 4 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ~80% bilingue (definicao EN + traducao PT)
  - REGRA 22: ZERO palavra das aulas 1, 2 e 3 como vocab NOVO. Fora, de proposito:
    pharmaceutical company / immunology / national manager / field team / global meeting /
    results / launch / disease area / to be responsible for / to manage / schedule / report /
    field visit / medical rep / demand plan / headquarters / to attend / to review /
    to prepare / to travel / quarter / target / challenge / opportunity / growth /
    to achieve / to exceed / to miss / market access / prescription volume
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 4 IN CLASS (mesmo tema: small talk no jantar/
    congresso do time Global; mesmo vocab; mesma gramatica: present continuous x present simple)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be" (palavra proibida com ela): a estrutura e apresentada como
    DUAS PECAS -- am / is / are + verbo-ING.
"""
import random

random.seed(4)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Small talk", "easy, friendly conversation before the real business starts",
     "conversa informal",
     "The dinner is two hours of small talk."),
    ("Congress", "a big professional event where doctors and companies meet",
     "congresso",
     "I go to the immunology congress every year."),
    ("Colleague", "a person who works with you, in your company or in another one",
     "colega de trabalho",
     "I met a colleague from the French team."),
    ("Executive", "a senior leader who makes the big decisions in a company",
     "executivo",
     "The executives from Paris are at the dinner."),
    ("Stakeholder", "a person or a group with an interest in your project",
     "parte interessada",
     "Doctors and payers are our main stakeholders."),
    ("Pipeline", "the new medicines a company is developing, before they reach the market",
     "portf&#243;lio em desenvolvimento",
     "We have three new products in the pipeline."),
    ("To introduce", "to say who you are, or to present one person to another",
     "apresentar(-se)",
     "Let me introduce myself: I am Emmanuele."),
    ("To network", "to meet new people at an event and build professional contacts",
     "fazer networking",
     "I network at every congress."),
    ("Currently", "now, in this period -- not every day, but at this moment in your life",
     "atualmente",
     "I am currently working on the asthma launch."),
    ("To look forward to", "to feel happy about something that is coming",
     "aguardar com expectativa",
     "I am looking forward to the congress."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-4">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Aula 04 -- Pre-class</div>')
w('      <h3>Breaking the Ice -- Small Talk at a Global Event</h3>')
w('      <div class="lesson-desc">O jantar antes da apresenta&#231;&#227;o: como abrir uma conversa com um desconhecido, '
  'dizer em uma frase o que voc&#234; est&#225; fazendo AGORA e manter a conversa viva at&#233; o fim. Key words: small talk, '
  'congress, colleague, executive, stakeholder, pipeline, to introduce, to network, currently, to look forward to. '
  'Structures: present continuous &mdash; am / is / are + verbo-ING para o que acontece AGORA (I am currently working on...), '
  'em contraste com o present simple do que &#233; sempre verdade (I work in immunology), mais a pergunta-chave da mesa: '
  '"What are you working on at the moment?" Express&#227;o da aula: "I am looking forward to working with your team."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as dez palavras da mesa do jantar e do corredor do congresso &mdash; nenhuma delas aparece num slide de resultado.</p>')
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
w('      <div class="match-grid" id="match-l4">')
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
w('        <p>It is the first evening of the <strong>congress</strong>, and Emmanuele is at the dinner table. She <strong>works</strong> '
  'in immunology &mdash; that is her job, and it does not change. But tonight nobody asks about her job. An <strong>executive</strong> '
  'from Paris turns to her and asks: "What <strong>are</strong> you <strong>working</strong> on at the moment?"</p>')
w('        <p style="margin-top:.8rem">Emmanuele breathes. "I am <strong>currently working</strong> on the immunology portfolio. Right now, my team '
  '<strong>is preparing</strong> a launch, and my field team <strong>is visiting</strong> the big centers." The executive smiles. "We '
  '<strong>are watching</strong> Brazil very closely this year," he says. "And I <strong>am looking</strong> at the <strong>pipeline</strong> '
  'for next year &mdash; two new molecules."</p>')
w('        <p style="margin-top:.8rem">She <strong>is not selling</strong> anything tonight. She is <strong>networking</strong>: she '
  '<strong>is meeting</strong> <strong>colleagues</strong> and <strong>stakeholders</strong> from twenty-two countries. And when the '
  'conversation ends, she says the sentence she practiced: "I am <strong>looking forward to</strong> working with your team." Tomorrow, '
  'in the meeting room, they already know her name.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Por que ela diz "I <strong>am working</strong> on the portfolio" e n&#227;o "I work on the portfolio"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque &#233; o projeto DESTE momento &mdash; come&#231;ou e vai terminar. AGORA, n&#227;o sempre.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque a a&#231;&#227;o j&#225; terminou no trimestre passado.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque "portfolio" &#233; uma palavra no plural.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. No mesmo texto ela diz "She <strong>works</strong> in immunology". Por que essa frase N&#195;O leva -ING?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque &#233; uma frase negativa.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque &#233; o trabalho dela &mdash; sempre verdade, n&#227;o muda no m&#234;s que vem. Isso &#233; present simple.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito &#233; "she" e depois de "she" o -ING nunca aparece.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "My team <strong>is preparing</strong> a launch." Por que N&#195;O &#233; "My team preparing a launch"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque "team" &#233; plural e pede "are".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque a estrutura tem SEMPRE duas pe&#231;as: <strong>am / is / are</strong> + verbo-<strong>ING</strong>. Sem a primeira pe&#231;a, a frase quebra.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque "prepare" &#233; um verbo irregular.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which question is correct at the dinner table?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What you are working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "What are you working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "What are you work on at the moment?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- O que voc&#234; est&#225; fazendo AGORA: am / is / are + verbo-ING</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A pergunta que voc&#234; mais vai ouvir num jantar de neg&#243;cios &#233; sobre AGORA, n&#227;o sobre sempre. Como o ingl&#234;s marca o agora (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I <strong>am</strong> / she <strong>is</strong> / we <strong>are</strong> + verbo-<strong>ING</strong></td>'
  '<td style="padding:.6rem">O projeto de AGORA: este m&#234;s, este ano, esta semana. Come&#231;ou e vai terminar &mdash; tem data de validade.</td>'
  '<td style="padding:.6rem">I <strong>am working</strong> on the launch. / My team <strong>is preparing</strong> the congress.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">S&#227;o <strong>DUAS pe&#231;as</strong>, nunca uma</td>'
  '<td style="padding:.6rem">Em portugu&#234;s "estou trabalhando" tem duas palavras, e em ingl&#234;s tamb&#233;m: <strong>am</strong> + <strong>working</strong>. Tirou uma das duas, a frase quebra.</td>'
  '<td style="padding:.6rem">We <strong>are launching</strong> a product. (nunca "we launching", nunca "we are launch")</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa: <strong>am not</strong> / <strong>is not</strong> + verbo-ING</td>'
  '<td style="padding:.6rem">Para dizer o que N&#195;O est&#225; acontecendo agora.</td>'
  '<td style="padding:.6rem">I <strong>am not working</strong> on that project this year.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Pergunta: <strong>What are you working on?</strong></td>'
  '<td style="padding:.6rem">A pergunta DA MESA. Decore como um bloco &#250;nico &mdash; n&#227;o monte palavra por palavra. Repare que <strong>are</strong> e <strong>you</strong> trocam de lugar.</td>'
  '<td style="padding:.6rem"><strong>What are you working on</strong> at the moment?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Sempre (present simple) x Agora (-ING)</td>'
  '<td style="padding:.6rem" colspan="2">I <strong>work</strong> in immunology = meu trabalho, n&#227;o muda &middot; I <strong>am working</strong> on the asthma launch = este m&#234;s, vai terminar. As palavras que pedem o -ING: <strong>right now</strong>, <strong>currently</strong>, <strong>at the moment</strong>, <strong>this month</strong>.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> '
  'em portugu&#234;s d&#225; para dizer "trabalho na campanha de asma" tanto para o sempre quanto para o agora &mdash; o mesmo verbo serve. '
  'Em ingl&#234;s N&#195;O: se voc&#234; disser "I work on the asthma launch" no jantar, o executivo entende que voc&#234; faz isso h&#225; anos e vai '
  'continuar para sempre. Para o projeto DESTE m&#234;s, o ingl&#234;s exige as duas pe&#231;as: <strong>I am working on the asthma launch</strong>. '
  'E o erro espelho tamb&#233;m acontece: como em portugu&#234;s "estou" some ("t&#244; trabalhando"), o brasileiro esquece o <strong>am</strong> e diz '
  '"I working on..." &mdash; que em ingl&#234;s n&#227;o &#233; frase.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("am working", "Dica: DUAS pe&#231;as -- am + o verbo com -ING",
     "I am currently working on the immunology portfolio.",
     '"I am currently ', ' on the immunology portfolio." (work)'),
    ("is preparing", "Dica: DUAS pe&#231;as -- is + o verbo com -ING (my team = uma coisa s&#243;)",
     "This month, my team is preparing the congress.",
     '"This month, my team ', ' the congress." (prepare)'),
    ("work", "Dica: SEMPRE verdade -- o trabalho dela n&#227;o muda. Sem -ING.",
     "I work in immunology.",
     '"I ', ' in immunology." (work -- sempre verdade)'),
    ("are launching", "Dica: DUAS pe&#231;as -- are + o verbo com -ING",
     "We are launching a new product in Brazil this month.",
     '"We ', ' a new product in Brazil this month." (launch)'),
    ("are you working", "Dica: na pergunta, are e you TROCAM de lugar",
     "What are you working on at the moment?",
     '"What ', ' on at the moment?" (work)'),
    ("am looking forward", "Dica: a express&#227;o da aula -- am + look com -ING",
     "I am looking forward to working with your team.",
     '"I ', ' to working with your team." (look forward)'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta do verbo entre par&#234;nteses. Aten&#231;&#227;o: uma delas &#233; sempre verdade e N&#195;O leva -ING. Toque em Listen para ouvir a frase inteira.</p>')
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
    (1, "Hello. I do not think we have met. I am Emmanuele Orrico, from Sanofi Brazil."),
    (2, "It is great to finally meet you in person."),
    (3, "I am currently working on the immunology portfolio."),
    (4, "And you? What are you working on at the moment?"),
    (5, "That is very interesting. I am looking forward to hearing more about it tomorrow."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque a conversa do jantar na ordem correta: da apresenta&#231;&#227;o at&#233; o fechamento.</p>')
w('      <div class="order-container" id="order-l4">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l4\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    ("Hello. I do not think we have met. I am Emmanuele, from Sanofi Brazil.",
     "Ol&#225;. Acho que n&#227;o nos conhecemos. Eu sou a Emmanuele, da Sanofi Brasil."),
    ("It is great to finally meet you in person.",
     "&#201; &#243;timo finalmente conhec&#234;-lo pessoalmente."),
    ("I am currently working on the immunology portfolio.",
     "Atualmente estou trabalhando no portf&#243;lio de imunologia."),
    ("And you? What are you working on at the moment?",
     "E voc&#234;? No que voc&#234; est&#225; trabalhando no momento?"),
    ("I am looking forward to working with your team.",
     "Estou ansiosa para trabalhar com o seu time."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases do jantar de agosto. Aten&#231;&#227;o: <strong>colleague</strong> tem duas s&#237;labas (KOL-eeg) e <strong>executive</strong> tem o acento na segunda (eg-ZEK-yu-tiv).</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real do jantar com o time Global.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; est&#225; sozinha na fila do caf&#233;. Um executivo que voc&#234; nunca viu est&#225; ao seu lado. Voc&#234; abre a conversa com:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Excuse me, sorry, my English is very bad."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Hello. I do not think we have met. I am Emmanuele, from Sanofi Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Who are you and what is your function in the company?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Ele pergunta: "What are you working on at the moment?" A melhor resposta &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I working on the immunology portfolio."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am work on the immunology portfolio."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "I am currently working on the immunology portfolio. Right now, my team is preparing a launch."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; quer contar o que &#233; SEMPRE verdade &mdash; a sua &#225;rea, o seu cargo. Voc&#234; diz:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I work in immunology. I am the National Demand Manager."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am working in immunology since always."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am work in immunology every day."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Agora voc&#234; quer devolver a pergunta para ele. A forma correta &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "And you? What you are working on?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "And you? What are you working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "And you? What are you work on?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A conversa est&#225; acabando e voc&#234; quer reencontrar essa pessoa amanh&#227;. Voc&#234; fecha com:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Ok. Bye bye. Finish."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It was great to meet you. I am looking forward to working with your team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am looking forward to work with your team yesterday."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; situa&#231;&#227;o abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 2 minutos, sem script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">It is August, and you are at the dinner with the Global team. An executive from Paris sits down next to you. '
  'Nobody introduces you &mdash; you start. In this order: (1) introduce yourself (name, company, and what you do &mdash; the things that are '
  'always true); (2) say what you are working on RIGHT NOW (use "I am currently working on..." and one sentence about what your team is '
  'preparing this month); (3) ask the other person what they are working on; (4) react to the answer ("That is very interesting"); and '
  '(5) close the conversation with the expression of the lesson: "I am looking forward to..." Speak for two minutes. Do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-4"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 4</h4>')
for i, (en, pt) in enumerate(SPEECH, 1):
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
