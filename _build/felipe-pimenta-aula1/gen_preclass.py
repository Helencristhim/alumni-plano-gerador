#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 do Felipe Pimenta (B2, CFO fintech).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - GATE botao morto: NENHUM texto vai dentro do argumento string de um onclick.
    Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase), onde o
    apostrofo e caractere comum. Assim o ingles mantem a contracao natural
    (I've, don't, it's) SEM quebrar o handler inline.
"""
import re
import random

random.seed(11)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Gross margin", "the money left after you subtract production costs",
     "margem bruta",
     "Our gross margin improved by two points this quarter."),
    ("Budget", "the plan for how much a company can spend",
     "or&#231;amento",
     "We're still inside the budget we approved in January."),
    ("Forecast", "a prediction of future financial numbers",
     "previs&#227;o",
     "I present the forecast to the board every quarter."),
    ("Earnings", "the profit a company makes in a period",
     "lucros, resultados",
     "Our earnings grew by eighteen percent this year."),
    ("Private equity", "firms that buy, grow and resell private companies",
     "private equity",
     "Before that, I spent two years in private equity."),
    ("Cash flow", "the money moving in and out of a business",
     "fluxo de caixa",
     "Cash flow is healthy, and we don't have short term debt."),
    ("Headcount", "the total number of employees",
     "quadro de funcion&#225;rios",
     "We haven't increased our headcount since March."),
    ("Stakeholder", "anyone with an interest in how the company performs",
     "parte interessada",
     "Every stakeholder wants numbers they can trust."),
    ("To oversee", "to be in charge of something and supervise it",
     "supervisionar",
     "I oversee the finance team at a fintech."),
    ("To deal with", "to handle a task or a problem regularly",
     "lidar com",
     "I deal with investors, auditors and the board."),
    ("To report to", "to have someone as your direct manager",
     "reportar-se a",
     "I report to the chief executive and to the board."),
    ("Background", "your education and professional history",
     "forma&#231;&#227;o, trajet&#243;ria",
     "My background is in corporate finance and controlling."),
]

DEFS = [d for _, d, _, _ in VOCAB]

# ---------- guarda-corpo: nada falavel pode entrar em argumento de onclick ----------
SPEAKABLE = []


def speak_btn(text, cls='audio-btn', label='Listen'):
    """Botao de audio: o texto viaja em data-speak (ATRIBUTO), nunca no onclick."""
    assert '"' not in text, f'aspas duplas quebram o atributo: {text}'
    SPEAKABLE.append(text)
    return (f'<button class="{cls}" data-speak="{text}" '
            f'onclick="speakText(this.dataset.speak,this)">{label}</button>')


# ---------- Stage 1.1 vocab cards ----------
cards = []
for w, d, pt, ex in VOCAB:
    cards.append(
        '        <div class="vocab-card-pc"><div class="vocab-card-content">'
        f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
        f'<span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{d} ({pt})</span></div>'
        f'<div class="vocab-card-example">"{ex}"</div></div>'
        f'{speak_btn(w)}</div>'
    )
vocab_cards = '\n'.join(cards)

# ---------- Stage 1.2 matching (REGRA 24: embaralhado, ordem distinta por linha) ----------
rows = []
for w, d, _, _ in VOCAB:
    opts = DEFS[:]
    while True:
        random.shuffle(opts)
        if opts != DEFS:
            break
    o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
    rows.append(
        f'        <div class="match-row" data-answer="{d}">'
        f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
        f'<option value="">Select...</option>{o}</select></div>'
    )
match_rows = '\n'.join(rows)

# ---------- Stage 1.5 fill-in-the-blank ----------
# forma PLENA no drill (e o que a gramatica ensina); data-phrase = atributo (seguro)
BLANKS = [
    ("I", "have been", "Dica: dura&#231;&#227;o at&#233; agora &mdash; have + partic&#237;pio",
     "I have been a CFO for three years.", "a CFO for three years."),
    ("In my current role, I", "oversee", "Dica: cargo atual, rotina &mdash; present simple",
     "In my current role, I oversee the finance team.", "the finance team."),
    ("Before that, I", "worked", "Dica: tempo terminado (from 2021 to 2023) &mdash; past simple",
     "Before that, I worked in private equity from 2021 to 2023.",
     "in private equity from 2021 to 2023."),
    ("We", "have just closed", "Dica: not&#237;cia muito recente &mdash; have just + partic&#237;pio",
     "We have just closed our first funding round.", "our first funding round."),
    ("I have worked in corporate finance", "since", "Dica: ponto de partida (2014)",
     "I have worked in corporate finance since 2014.", "2014."),
    ("I have known our chief executive", "for", "Dica: per&#237;odo (two years)",
     "I have known our chief executive for two years.", "two years."),
]
fills = []
for pre, ans, hint, phrase, post in BLANKS:
    SPEAKABLE.append(phrase)
    fills.append(
        f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre} '
        f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
        f'data-phrase="{phrase}" placeholder="___"> {post}"</div>'
        f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
        f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
    )
fill_items = '\n'.join(fills)

# ---------- Stage 3 pronunciation (fala real => CONTRACAO natural) ----------
SPEECH = [
    ("In my current role, I oversee the finance team at a fintech.",
     "No meu cargo atual, eu supervisiono o time de finan&#231;as de uma fintech."),
    ("I've been a CFO for three years.",
     "Sou CFO h&#225; tr&#234;s anos."),
    ("Before that, I spent two years in private equity.",
     "Antes disso, passei dois anos em private equity."),
    ("My background is in corporate finance and controlling.",
     "Minha forma&#231;&#227;o &#233; em finan&#231;as corporativas e controladoria."),
    ("I'm responsible for the budget, the forecast and investor reporting.",
     "Sou respons&#225;vel pelo or&#231;amento, pela previs&#227;o e pelo reporte a investidores."),
]
sp = []
for phrase, pt in SPEECH:
    SPEAKABLE.append(phrase)
    sp.append(
        f'      <div class="speech-card" data-phrase="{phrase}">\n'
        f'        <div class="speech-phrase">{phrase}</div>\n'
        f'        <div class="speech-translation">{pt}</div>\n'
        f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
        f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
        f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
        f'        <div class="speech-result"></div>\n'
        f'      </div>'
    )
speech_cards = '\n'.join(sp)

# ---------- Survival card (fala real => CONTRACAO natural) ----------
sv = []
for i, (en, pt) in enumerate(SPEECH, 1):
    sv.append(
        f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
        f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
    )
survival = '\n'.join(sv)

HTML = f'''<div class="lesson-card" id="ex-lesson-1">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 01 -- Pre-class</div>
      <h3>Diagnostic Session -- Who Is Felipe Pimenta in English?</h3>
      <div class="lesson-desc">Contar a sua trajet&#243;ria de CFO numa screening call internacional. Key words: gross margin, budget, forecast, earnings, private equity, cash flow, headcount, stakeholder, to oversee, to deal with, to report to, background. Structures: present perfect (experi&#234;ncia e dura&#231;&#227;o com for/since) vs present simple (cargo atual) vs past simple (tempo terminado).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as palavras que voc&#234; j&#225; usa em portugu&#234;s todo dia &mdash; agora em ingl&#234;s.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l1">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Felipe <strong>is</strong> the Chief Financial Officer of a fintech. He <strong>oversees</strong> the finance team and <strong>deals with</strong> investors, auditors and the board. He <strong>reports to</strong> the chief executive. "I <strong>have been</strong> a CFO for three years," he says, "and I <strong>have worked</strong> in corporate finance <strong>since</strong> 2014." His <strong>background</strong> is in controlling. Before the fintech, he <strong>worked</strong> at a <strong>private equity</strong> firm, where he <strong>built</strong> models and <strong>listened</strong> to meetings in English without saying much. Today his week <strong>is</strong> different: he <strong>reviews</strong> the <strong>budget</strong>, <strong>presents</strong> the <strong>forecast</strong>, and <strong>watches</strong> the <strong>gross margin</strong> and the <strong>cash flow</strong> closely. This quarter, <strong>earnings</strong> <strong>grew</strong> by eighteen percent and the team <strong>has just closed</strong> its first funding round. The company <strong>has not increased</strong> its <strong>headcount</strong> since March, and every <strong>stakeholder</strong> <strong>wants</strong> numbers they can trust.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Por que dizemos "I have been a CFO for three years" e n&#227;o "I am a CFO for three years"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque come&#231;ou no passado e continua at&#233; agora &mdash; present perfect com for.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque a a&#231;&#227;o terminou e n&#227;o tem mais liga&#231;&#227;o com o presente.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque &#233; uma rotina que ele repete toda semana.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "Before the fintech, he worked at a private equity firm" usa past simple porque:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A experi&#234;ncia continua at&#233; hoje.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &#201; um per&#237;odo terminado da carreira dele.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &#201; algo que est&#225; acontecendo agora.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence about his current role is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "He is overseeing the finance team since three years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "He oversees the finance team and reports to the chief executive."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "He has overseen the finance team in 2023."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Perfect vs Present Simple vs Past Simple</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como contar a sua carreira com o tempo verbal certo &mdash; o que todo entrevistador testa nos primeiros dois minutos (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + past participle</td><td style="padding:.6rem">Experi&#234;ncia e dura&#231;&#227;o at&#233; agora. Experience and duration up to now (for / since).</td><td style="padding:.6rem">I <strong>have been</strong> a CFO for three years.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">just + present perfect</td><td style="padding:.6rem">Not&#237;cia muito recente. Very recent news.</td><td style="padding:.6rem">We <strong>have just closed</strong> our first round.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / you / we + verb (he/she + s)</td><td style="padding:.6rem">Cargo atual e rotina. Current role and routine.</td><td style="padding:.6rem">I <strong>oversee</strong> the finance team.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Past Simple<br>verb + -ed</td><td style="padding:.6rem">A&#231;&#227;o terminada, tempo terminado. Finished action, finished time (in 2022).</td><td style="padding:.6rem">I <strong>worked</strong> in private equity in 2022.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa (present perfect)</td><td style="padding:.6rem">have / has + not + partic&#237;pio. Na fala, contra&#237;do: <strong>haven't</strong>.</td><td style="padding:.6rem">We <strong>haven't</strong> increased our headcount.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">How long + have + sujeito + partic&#237;pio?</td><td style="padding:.6rem"><strong>How long have you been</strong> a CFO?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">for vs since</td><td style="padding:.6rem" colspan="2"><strong>for</strong> + per&#237;odo (for three years) &middot; <strong>since</strong> + ponto de partida (since 2014)</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> em portugu&#234;s dizemos "sou CFO h&#225; tr&#234;s anos" com o presente. Em ingl&#234;s, dura&#231;&#227;o at&#233; agora <strong>nunca</strong> usa o present simple: "I am a CFO for three years" est&#225; errado &mdash; o certo &#233; "I <strong>have been</strong> a CFO for three years" (na fala, <strong>I've been</strong>).</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Screening Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma screening call com um headhunter na ordem correta.</p>
      <div class="order-container" id="order-l1">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Describe your current role: what you oversee and who you report to.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Ask about the next step and agree on a follow-up.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Thank the recruiter for the call and confirm you have time to talk.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Explain why you are interested in an international move.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Summarize your background in two sentences.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l1')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem qualquer entrevista.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma entrevista em ingl&#234;s.</p>
      <div class="quiz-item"><div class="quiz-question">The recruiter asks: "So, tell me what you do." You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I do the finance things in a company."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "In my current role, I oversee the finance team at a fintech and report to the chief executive."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I'm overseeing the finance team since three years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">She asks: "How long have you been a CFO?" The best answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I'm a CFO for three years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I've been a CFO for three years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I'm being a CFO since three years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to mention a finished period of your career. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Before that, I spent two years in private equity."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Before that, I've spent two years in private equity."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Before that, I'm spending two years in private equity."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">She asks what is new at your company. You mention very recent news:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We closed just our first funding round."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We've just closed our first funding round."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We're just closing our first funding round last week."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You didn't understand a question and you need a moment. The most professional move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Answer something vague and hope she doesn't notice.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, could you rephrase that? I want to make sure I understand the question."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Switch to Portuguese and explain that your English isn't good.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">A headhunter opens the call: "Tell me about yourself and why you're interested in an international role." Introduce yourself: your current role (present simple), how long you've been in finance (present perfect, for/since), the finished chapters of your career (past simple), and what you're looking for now. Take your time and don't read from a script.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-1"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 1</h4>
{survival}
    </div>

  </div>
</div>
'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

# ---------- auto-verificacao do GATE botao morto ----------
bad = re.findall(r"speakText\('[^']*'[^)]*\)", HTML)
assert not bad, f'texto dentro de argumento de onclick (botao morto): {bad[:3]}'
assert 'this.dataset.speak' in HTML

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
print('com contracao:', sorted({s for s in SPEAKABLE if "'" in s}))
