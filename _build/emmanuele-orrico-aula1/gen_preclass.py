#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ~80% bilingue (definicao EN + traducao PT)
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula IN CLASS (mesmo tema/gramatica/vocab)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be": a gramatica entra como o CODIGO do trabalho dela
    (I work at / I manage / I am responsible for) e "I am responsible for" e tratado
    como FRASE PRONTA, nao como conjugacao.
"""
import random

random.seed(33)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Pharmaceutical company", "a company that makes medicines",
     "empresa farmac&#234;utica",
     "Sanofi is a pharmaceutical company."),
    ("Immunology", "the area of medicine that studies the defense system of the body",
     "imunologia",
     "I work in immunology."),
    ("National manager", "the person who leads a business in the whole country",
     "gerente nacional",
     "I am the national demand manager for Brazil."),
    ("Field team", "the people who visit doctors in hospitals and clinics",
     "time de campo",
     "My field team visits doctors every week."),
    ("Global meeting", "a meeting with colleagues from other countries",
     "reuni&#227;o com o time Global",
     "We have a global meeting every month."),
    ("Results", "the numbers that show how the business is going",
     "resultados",
     "I present the results to the Global team."),
    ("Launch", "the moment a company brings a new medicine to the market",
     "lan&#231;amento",
     "The launch starts in September."),
    ("Disease area", "a group of illnesses that one team takes care of",
     "&#225;rea terap&#234;utica",
     "Asthma is one of my disease areas."),
    ("To be responsible for", "to take care of something as part of your job",
     "ser respons&#225;vel por",
     "I am responsible for eight disease areas."),
    ("To manage", "to lead a team or a business",
     "gerenciar / liderar",
     "I manage the immunology portfolio in Brazil."),
]

LISTEN_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-1">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Aula 01 -- Pre-class</div>')
w('      <h3>Diagnostic + First Words -- Who Is Emmanuele Orrico?</h3>')
w('      <div class="lesson-desc">Apresentar-se e descrever o seu papel numa call com o time Global da Sanofi. '
  'Key words: pharmaceutical company, immunology, national manager, field team, global meeting, results, launch, '
  'disease area, to be responsible for, to manage. Structures: I work at... / I manage... / I am responsible for... '
  '(fatos sobre o seu trabalho), o -s de my team visits, e as frases prontas para pedir que repitam ou falem mais devagar.</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as dez palavras que voc&#234; usa em portugu&#234;s todo dia na Sanofi &mdash; agora em ingl&#234;s.</p>')
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
w('      <div class="match-grid" id="match-l1">')
all_defs = [d for _, d, _, _ in VOCAB]
for word, dfn, _pt, _ex in VOCAB:
    opts = all_defs[:]
    # REGRA 24: embaralhar as opcoes -- ordem DIFERENTE em cada linha
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
w('        <p>Emmanuele Orrico <strong>works</strong> at Sanofi, a <strong>pharmaceutical company</strong>. '
  'She <strong>is</strong> the national demand <strong>manager</strong> in Brazil, and she <strong>manages</strong> '
  'the <strong>immunology</strong> portfolio. "I <strong>am responsible for</strong> eight <strong>disease areas</strong>," '
  'she says. "Asthma, COPD and atopic dermatitis, for example." Her <strong>field team</strong> <strong>visits</strong> '
  'doctors every week, and the team <strong>talks</strong> about the patients and the treatments. Every month, '
  'Emmanuele <strong>presents</strong> the <strong>results</strong> in a <strong>global meeting</strong> with '
  'colleagues from France, Canada and Japan. She <strong>does not work</strong> in oncology, and she '
  '<strong>does not manage</strong> the factory. She <strong>manages</strong> the demand. In September, the '
  'company <strong>starts</strong> a new <strong>launch</strong>, and in August the Global team <strong>visits</strong> '
  'Brazil. "I <strong>present</strong> the <strong>results</strong>, the challenges and the opportunities," she says.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Por que dizemos "My field team visits doctors" e n&#227;o "My field team visit doctors"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque "my team" &#233; UM grupo (como he/she/it) &mdash; e a&#237; o verbo ganha -S.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque a a&#231;&#227;o est&#225; acontecendo agora, neste momento.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque a a&#231;&#227;o aconteceu no passado.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. "I am responsible for eight disease areas." Nesta frase, "am responsible for" &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Uma a&#231;&#227;o que ela est&#225; fazendo agora.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Uma FRASE PRONTA para dizer do que voc&#234; cuida no trabalho &mdash; use inteira, sem montar nada.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Uma forma de falar sobre o futuro.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "She does not work in oncology." O que essa frase diz?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Ela trabalhou em oncologia no passado.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Oncologia N&#195;O faz parte do trabalho dela &mdash; a negativa usa does not (doesn\'t) + verbo.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ela vai come&#231;ar a trabalhar em oncologia.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence about her job is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She work in Sanofi and responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She works at Sanofi and she is responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She works in Sanofi and she responsible for eight disease areas."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Falando do seu trabalho: I work at / I manage / I am responsible for</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">O c&#243;digo que abre TODA reuni&#227;o com a Global: como dizer quem voc&#234; &#233; e do que voc&#234; cuida (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I / you / we / they + verbo</td>'
  '<td style="padding:.6rem">Fatos sobre o seu trabalho. Facts about your job.</td>'
  '<td style="padding:.6rem">I <strong>work</strong> at Sanofi.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">he / she / my team + verbo <strong>+ s</strong></td>'
  '<td style="padding:.6rem">A MESMA ideia, mas para uma pessoa ou UM grupo. O -s &#233; o erro n&#186; 1 do brasileiro.</td>'
  '<td style="padding:.6rem">My team <strong>visits</strong> doctors.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">FRASE PRONTA: I am responsible for + coisa</td>'
  '<td style="padding:.6rem">N&#227;o tem nada para montar. Pegue o bloco inteiro e use. Ready phrase &mdash; just reuse it.</td>'
  '<td style="padding:.6rem">I <strong>am responsible for</strong> eight disease areas.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa: don\'t / doesn\'t + verbo</td>'
  '<td style="padding:.6rem">Para dizer o que N&#195;O &#233; seu. To say what is not yours.</td>'
  '<td style="padding:.6rem">I <strong>don\'t work</strong> in oncology.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa: Do / Does + pessoa + verbo?</td>'
  '<td style="padding:.6rem">Para PERGUNTAR ao colega (e n&#227;o s&#243; responder).</td>'
  '<td style="padding:.6rem"><strong>Do you work</strong> in immunology?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">at vs in</td><td style="padding:.6rem" colspan="2">'
  'Empresa pede <strong>at</strong>: "I work <strong>at</strong> Sanofi". &#193;rea/pa&#237;s pede <strong>in</strong>: '
  '"I work <strong>in</strong> immunology", "I work <strong>in</strong> Brazil".</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> '
  'em portugu&#234;s, "sou respons&#225;vel" j&#225; tem o verbo dentro da palavra &mdash; por isso o brasileiro escreve '
  '"I responsible for...", que em ingl&#234;s N&#195;O existe. A frase certa &#233; sempre <strong>I am responsible for...</strong>, '
  'inteira, sem pensar. E "trabalho NA Sanofi" vira <strong>at</strong> Sanofi, nunca "in Sanofi".</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("work", "Dica: fato sobre o seu trabalho &mdash; verbo simples, sem -s depois de I",
     "I work at Sanofi, in Brazil.",
     '"I ', ' at Sanofi, in Brazil."'),
    ("am responsible for", "Dica: a FRASE PRONTA para dizer do que voc&#234; cuida",
     "I am responsible for eight disease areas.",
     '"I ', ' eight disease areas."'),
    ("visits", "Dica: \"my field team\" &#233; UM grupo &mdash; o verbo ganha -s",
     "My field team visits doctors every week.",
     '"My field team ', ' doctors every week."'),
    ("manage", "Dica: depois de I, o verbo fica simples",
     "I manage the immunology portfolio in Brazil.",
     '"I ', ' the immunology portfolio in Brazil."'),
    ("don't work", "Dica: negativa depois de I &mdash; don\'t + verbo",
     "I don't work in oncology.",
     '"I ', ' in oncology."'),
    ("at", "Dica: empresa sempre pede esta preposi&#231;&#227;o",
     "I work at Sanofi.",
     '"I work ', ' Sanofi."'),
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
    (1, "Thank the Global team for the call and confirm everyone can hear you."),
    (2, "Introduce yourself: your name and the company you work at."),
    (3, "Describe your role: what you manage and what you are responsible for."),
    (4, "Talk about your field team and the disease areas you take care of."),
    (5, "Confirm that you present the results to the Global team in August."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Global Call in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma primeira call com o time Global na ordem correta.</p>')
w('      <div class="order-container" id="order-l1">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l1\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l1\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l1\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l1\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    ("My name is Emmanuele Orrico, and I work at Sanofi.",
     "Meu nome &#233; Emmanuele Orrico e eu trabalho na Sanofi."),
    ("I am the national demand manager for immunology.",
     "Eu sou a gerente nacional de demanda de imunologia."),
    ("I am responsible for eight disease areas.",
     "Eu sou respons&#225;vel por oito &#225;reas terap&#234;uticas."),
    ("My field team visits doctors every week.",
     "Meu time de campo visita m&#233;dicos toda semana."),
    ("Sorry, could you repeat that, please?",
     "Desculpe, voc&#234; poderia repetir, por favor?"),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases que abrem qualquer reuni&#227;o com o time Global.</p>')
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
w('      <div class="quiz-item"><div class="quiz-question">Marc, do time Global, pergunta: "So, what do you do at Sanofi?" Voc&#234; responde:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I do the immunology things in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am the national demand manager, and I manage the immunology portfolio in Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I responsible for the immunology in Sanofi."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Ele pergunta: "Which disease areas are you responsible for?" A melhor resposta &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I responsible for eight disease areas."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am responsible for eight disease areas: asthma, COPD and atopic dermatitis, for example."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Eight disease areas is my responsible."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Voc&#234; quer falar do seu time de campo. Qual frase est&#225; correta?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "My field team visits doctors every week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "My field team visit doctors every week."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My field team is visit doctors every week."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Algu&#233;m pergunta se voc&#234; cuida de oncologia. Voc&#234; N&#195;O cuida. Voc&#234; diz:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I no work in oncology."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I not work in oncology."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "I don\'t work in oncology. I work in immunology."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">A pergunta veio r&#225;pida demais e voc&#234; N&#195;O entendeu. O movimento mais profissional &#233;:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Ficar em sil&#234;ncio e esperar que algu&#233;m mude de assunto.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, could you repeat that, please?" &mdash; ou "Could you speak more slowly, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Pedir desculpas pelo seu ingl&#234;s e parar de participar da reuni&#227;o.</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 60 segundos, sem script. Esta grava&#231;&#227;o &#233; o seu BASELINE: vamos ouvi-la de novo na aula 17.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">You are starting a video call with the Sanofi Global team. Introduce yourself: '
  'your name and your company (I work at...), your role (I am the national demand manager), what you take care of '
  '(I am responsible for...), and what your field team does every week (My team visits...). Finish with one sentence '
  'about August, when the Global team visits Brazil. Take your time and do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-1"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
SURVIVAL = [
    ("My name is Emmanuele Orrico, and I work at Sanofi.",
     "Meu nome &#233; Emmanuele Orrico e eu trabalho na Sanofi."),
    ("I am the national demand manager for immunology.",
     "Eu sou a gerente nacional de demanda de imunologia."),
    ("I am responsible for eight disease areas.",
     "Eu sou respons&#225;vel por oito &#225;reas terap&#234;uticas."),
    ("Sorry, could you repeat that, please?",
     "Desculpe, voc&#234; poderia repetir, por favor?"),
    ("Let me think for a second.",
     "Deixe-me pensar um segundo."),
]
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 1</h4>')
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
