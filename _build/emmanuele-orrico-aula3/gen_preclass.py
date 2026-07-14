#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 3 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ~80% bilingue (definicao EN + traducao PT)
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

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Quarter", "a period of three months in the business year",
     "trimestre",
     "Last quarter was very busy."),
    ("Target", "the number the company wants you to reach",
     "meta",
     "We had a high target in dermatology."),
    ("Challenge", "something difficult in the business",
     "desafio",
     "We faced a challenge with market access."),
    ("Opportunity", "a chance to grow the business",
     "oportunidade",
     "The private market is a big opportunity."),
    ("Growth", "when the numbers go up",
     "crescimento",
     "The growth came from the private market."),
    ("To achieve", "to reach the number you needed",
     "alcan&#231;ar / atingir",
     "We achieved our target in dermatology."),
    ("To exceed", "to go above the number you needed",
     "superar",
     "In Q2, the team exceeded the target."),
    ("To miss", "to not reach the number you needed",
     "n&#227;o atingir",
     "We missed the target in asthma."),
    ("Market access", "when a medicine is approved and paid for, so patients can get it",
     "acesso ao mercado",
     "Market access was slow in the public market."),
    ("Prescription volume", "how many prescriptions the doctors write for your medicine",
     "volume de prescri&#231;&#245;es",
     "Prescription volume went up in June."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-3">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Aula 03 -- Pre-class</div>')
w('      <h3>What Happened Last Quarter? -- Reporting Past Results</h3>')
w('      <div class="lesson-desc">Contar ao time Global o que aconteceu no trimestre passado: a meta batida em dermatologia, '
  'a meta perdida em asma, o desafio de acesso ao mercado e o crescimento no mercado privado. Key words: quarter, target, '
  'challenge, opportunity, growth, to achieve, to exceed, to miss, market access, prescription volume. Structures: past simple '
  '&mdash; verbos regulares com -ed (achieved, missed, presented) e os cinco irregulares do business review (went, had, gave, '
  'met, came), a negativa didn&#39;t achieve e as express&#245;es de tempo last quarter / in April / two months ago. '
  'Express&#227;o da aula: "Once in a while, we have unexpected results."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as dez palavras que est&#227;o em todo slide de business review &mdash; agora em ingl&#234;s.</p>')
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
w('      <div class="match-grid" id="match-l3">')
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
w('        <p>Last <strong>quarter</strong> was busy, but Emmanuele <strong>had</strong> good news for Paris. In April, she '
  '<strong>presented</strong> the plan to the Global team. In May, her team <strong>met</strong> sixty new doctors in the private '
  'market. In June, <strong>prescription volume</strong> <strong>went</strong> up, and the <strong>growth</strong> '
  '<strong>came</strong> from the private market. In dermatology, the team <strong>exceeded</strong> the <strong>target</strong>: '
  'they <strong>achieved</strong> one hundred and eight percent. In asthma, they <strong>missed</strong> the target. The '
  '<strong>challenge</strong> was <strong>market access</strong> in the public market: the process <strong>was</strong> slow, and '
  'they <strong>didn&#39;t achieve</strong> the number. But Emmanuele also <strong>saw</strong> an <strong>opportunity</strong>. '
  '"<strong>Once in a while, we have unexpected results</strong>," she says. "Then we learn, and we go again."</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Por que "achieved", "missed" e "presented" terminam em -ED?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque a a&#231;&#227;o TERMINOU: o trimestre passado acabou. A maioria dos verbos ganha -ed no passado.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque a a&#231;&#227;o est&#225; acontecendo agora, neste momento.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito &#233; "the team" (uma coisa s&#243;).</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "Her team met sixty new doctors." Por que N&#195;O &#233; "meeted"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque o verbo est&#225; no presente.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque meet &#233; um dos cinco irregulares do business review: meet &rarr; met. Irregular N&#195;O leva -ed.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque depois de "team" o verbo nunca muda.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "They didn&#39;t achieve the number." Por que N&#195;O &#233; "didn&#39;t achieved"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque a frase &#233; sobre o futuro.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque "achieve" &#233; um verbo irregular.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Porque o passado j&#225; est&#225; dentro do <strong>did</strong>. Depois de didn&#39;t, o verbo volta ao normal &mdash; s&#243; UMA marca de passado por frase.</div>'
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
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Contando o que ACONTECEU: -ed e os cinco irregulares</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Resultado &#233; SEMPRE passado. Como o ingl&#234;s diz o que j&#225; terminou (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Verbo + <strong>-ed</strong> (regulares)</td>'
  '<td style="padding:.6rem">A a&#231;&#227;o TERMINOU. O trimestre acabou. Vale para I, you, we, they, he, she &mdash; a forma &#233; a MESMA para todos.</td>'
  '<td style="padding:.6rem">We <strong>achieved</strong> the target. / She <strong>presented</strong> the plan.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Os <strong>5 irregulares</strong> do business review</td>'
  '<td style="padding:.6rem">N&#195;O levam -ed: viram outra palavra. S&#227;o s&#243; cinco &mdash; decore estes e voc&#234; cobre 90% da reuni&#227;o.</td>'
  '<td style="padding:.6rem">go &rarr; <strong>went</strong> &middot; have &rarr; <strong>had</strong> &middot; give &rarr; <strong>gave</strong> &middot; meet &rarr; <strong>met</strong> &middot; come &rarr; <strong>came</strong></td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa: <strong>didn&#39;t</strong> + verbo NORMAL</td>'
  '<td style="padding:.6rem">S&#243; UMA marca de passado por frase, e ela j&#225; est&#225; dentro do <strong>did</strong>. Por isso o verbo volta ao normal.</td>'
  '<td style="padding:.6rem">We <strong>didn&#39;t achieve</strong> the target. (nunca "didn&#39;t achieved")</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Quando? (express&#245;es de tempo)</td>'
  '<td style="padding:.6rem" colspan="2"><strong>last</strong> quarter &middot; <strong>last</strong> week &middot; <strong>in</strong> April &middot; two months <strong>ago</strong> (o "ago" vem DEPOIS do tempo, nunca antes) &middot; yesterday</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Frase pronta: <strong>It was a difficult quarter.</strong></td>'
  '<td style="padding:.6rem">Nada para construir, nada para conjugar. &#201; UM BLOCO: pegue e use.</td>'
  '<td style="padding:.6rem"><strong>It was</strong> a good quarter for dermatology.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> '
  'em portugu&#234;s, "n&#227;o atingimos" j&#225; tem o passado no verbo. Por isso sai "we didn&#39;t achieved" &mdash; passado DUAS vezes. '
  'Em ingl&#234;s, o passado est&#225; no <strong>did</strong>, e o verbo volta ao normal: <strong>we didn&#39;t achieve</strong>. '
  'E o oposto tamb&#233;m acontece: como o "last quarter" j&#225; diz que &#233; passado, o brasileiro esquece o -ED e diz "last quarter we exceed". '
  'Em ingl&#234;s, o VERBO tamb&#233;m tem de marcar: <strong>we exceeded</strong>.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("exceeded", "Dica: passar ACIMA da meta &mdash; verbo regular, com -ed",
     "Last quarter, we exceeded the target in dermatology.",
     '"Last quarter, we ', ' the target in dermatology."'),
    ("missed", "Dica: N&#195;O atingir a meta &mdash; verbo regular, com -ed",
     "We missed the target in asthma.",
     '"We ', ' the target in asthma."'),
    ("met", "Dica: um dos cinco irregulares &mdash; meet no passado",
     "In May, my team met sixty new doctors.",
     '"In May, my team ', ' sixty new doctors."'),
    ("came", "Dica: um dos cinco irregulares &mdash; come no passado",
     "The growth came from the private market.",
     '"The growth ', ' from the private market."'),
    ("didn't achieve", "Dica: negativa &mdash; didn&#39;t + verbo NORMAL (sem -ed)",
     "We didn't achieve the target in the public market.",
     '"We ', ' the target in the public market."'),
    ("had", "Dica: um dos cinco irregulares &mdash; have no passado",
     "Two months ago, we had a challenge with market access.",
     '"Two months ago, we ', ' a challenge with market access."'),
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
    (1, "In April, we started the quarter with a clear target."),
    (2, "In May, my team met sixty new doctors in the private market."),
    (3, "In June, prescription volume grew and we exceeded the target in dermatology."),
    (4, "At the end of the quarter, we missed the target in asthma, because market access was slow."),
    (5, "Last week, I presented the results to the Global team."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Quarter in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os acontecimentos do trimestre passado na ordem correta.</p>')
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
    ("Last quarter, we achieved our target in dermatology.",
     "No trimestre passado, n&#243;s atingimos a nossa meta em dermatologia."),
    ("We missed the target in asthma, because market access was slow.",
     "N&#243;s n&#227;o atingimos a meta em asma, porque o acesso ao mercado estava lento."),
    ("The growth came from the private market.",
     "O crescimento veio do mercado privado."),
    ("Once in a while, we have unexpected results.",
     "De vez em quando, temos resultados inesperados."),
    ("Let me check the number and come back to you.",
     "Deixe-me conferir o n&#250;mero e eu retorno para voc&#234;."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases da apresenta&#231;&#227;o de agosto. Aten&#231;&#227;o ao -ED: achiev<strong>ed</strong> = um som s&#243;; exceed<strong>ed</strong> = uma s&#237;laba a mais.</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real do business review com o time Global.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Marc pergunta: "How was last quarter in dermatology?" Voc&#234; responde:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Last quarter we exceed the target."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Last quarter, we exceeded the target in dermatology. We achieved one hundred and eight percent."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Last quarter we are exceeding the target."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Ele pergunta: "Did you reach the target in asthma?" A melhor resposta &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "No, we didn&#39;t achieved the target."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "No, sorry, sorry. It is my fault."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "No. We missed the target in asthma, because market access was slow."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Ele pergunta: "Where did the growth come from?" Qual frase est&#225; correta?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The growth came from the private market. My team met sixty new doctors."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The growth comed from the private market. My team meeted sixty new doctors."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The growth is come from the private market."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; quer dizer QUANDO o desafio come&#231;ou (dois meses atr&#225;s). Voc&#234; diz:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Ago two months, market access was slow."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Two months ago, market access was slow."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Before two months, market access was slow."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">O VP Global comenta que os n&#250;meros sobem e descem todo trimestre. A resposta profissional e natural &#233;:</div>'
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 2 minutos, sem script.</p>')
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
