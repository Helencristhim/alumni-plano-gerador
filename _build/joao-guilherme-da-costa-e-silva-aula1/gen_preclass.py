#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 1 do Joao Guilherme (B2, engenheiro de sinalizacao ferroviaria).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 => 12 palavras novas
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula IN CLASS (mesmo tema/gramatica/vocab)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase), onde o
    apostrofo e caractere comum. Assim o ingles mantem a contracao natural (I've,
    don't, it's) SEM quebrar o handler inline.
"""
import re
import random

random.seed(24)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Signaling system", "the equipment that controls train movement and keeps trains safely apart",
     "sistema de sinaliza&#231;&#227;o",
     "I design the signaling system for two metro lines."),
    ("Commissioning", "the final stage where you test and prove that a system works before it goes live",
     "comissionamento",
     "The commissioning of Line 5 starts in September."),
    ("Supplier", "the company that provides the equipment or the service",
     "fornecedor",
     "Our supplier is based in Germany."),
    ("Milestone", "a key date in the project that marks the end of a stage",
     "marco do projeto",
     "We missed the milestone by three weeks."),
    ("Deliverable", "a document or a product that the project must hand over",
     "entreg&#225;vel",
     "The test report is the next deliverable."),
    ("Stakeholder", "anyone with an interest in the outcome of the project",
     "parte interessada",
     "Every stakeholder wants a realistic schedule."),
    ("Compliance", "doing exactly what a standard or a contract requires",
     "conformidade",
     "Compliance with the European standard is mandatory."),
    ("Inspection", "a formal check to confirm quality before you accept the work",
     "inspe&#231;&#227;o",
     "The inspection takes place at the factory."),
    ("Specification", "the written document that defines what the equipment must do",
     "especifica&#231;&#227;o",
     "The specification says the response time is two seconds."),
    ("Scope", "everything the project includes, and nothing more",
     "escopo",
     "That request is outside the scope of the contract."),
    ("Deadline", "the date by which the work must be finished",
     "prazo final",
     "The supplier missed the deadline again."),
    ("To oversee", "to be in charge of a process and supervise it",
     "supervisionar",
     "I oversee the commissioning of the signaling system."),
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
    ("I", "have worked", "Dica: dura&#231;&#227;o at&#233; agora (for eight years) &mdash; have + partic&#237;pio",
     "I have worked in railway signaling for eight years.",
     "in railway signaling for eight years."),
    ("In my current role, I", "oversee", "Dica: cargo atual, rotina &mdash; present simple",
     "In my current role, I oversee the commissioning of the signaling system.",
     "the commissioning of the signaling system."),
    ("I", "have been working", "Dica: come&#231;ou em 2019 e CONTINUA &mdash; have been + verbo-ing",
     "I have been working with German suppliers since 2019.",
     "with German suppliers since 2019."),
    ("In 2023, I", "spent", "Dica: tempo terminado (in 2023) &mdash; past simple",
     "In 2023, I spent two months in San Francisco.", "two months in San Francisco."),
    ("I have worked in railway signaling", "for", "Dica: per&#237;odo (eight years)",
     "I have worked in railway signaling for eight years.", "eight years."),
    ("I have been working with German suppliers", "since", "Dica: ponto de partida (2019)",
     "I have been working with German suppliers since 2019.", "2019."),
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
    ("I'm a signaling engineer at Motiva, and I oversee the commissioning.",
     "Sou engenheiro de sinaliza&#231;&#227;o na Motiva e supervisiono o comissionamento."),
    ("I've worked in railway signaling for eight years.",
     "Trabalho com sinaliza&#231;&#227;o ferrovi&#225;ria h&#225; oito anos."),
    ("I've been working with German suppliers since 2019.",
     "Trabalho com fornecedores alem&#227;es desde 2019."),
    ("My main concern is the deadline for the factory inspection.",
     "Minha principal preocupa&#231;&#227;o &#233; o prazo da inspe&#231;&#227;o de f&#225;brica."),
    ("Sorry, could you rephrase that? I want to make sure I understand.",
     "Desculpe, voc&#234; poderia reformular? Quero ter certeza de que entendi."),
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

# ---------- Survival card ----------
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
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 01 -- Pre-class</div>
      <h3>Diagnostic + Reactivation -- Who Is Jo&#227;o Guilherme in English?</h3>
      <div class="lesson-desc">Apresentar-se e descrever o seu papel numa kick-off call com um fornecedor internacional. Key words: signaling system, commissioning, supplier, milestone, deliverable, stakeholder, compliance, inspection, specification, scope, deadline, to oversee. Structures: present simple (cargo atual) vs present perfect (experi&#234;ncia, for/since) vs present perfect continuous (o que continua) vs past simple (tempo terminado).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="1">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. S&#227;o as doze palavras que voc&#234; usa em portugu&#234;s todo dia na Motiva &mdash; agora em ingl&#234;s.</p>
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
        <p>Jo&#227;o Guilherme <strong>is</strong> a signaling engineer at Motiva. He <strong>oversees</strong> the <strong>commissioning</strong> of the <strong>signaling system</strong> on two metro lines, and he <strong>runs</strong> a weekly status meeting with the <strong>suppliers</strong>. "I <strong>have worked</strong> in railway signaling <strong>for</strong> eight years," he says, "and I <strong>have been working</strong> with German, French and Chinese <strong>suppliers</strong> <strong>since</strong> 2019." In 2023, he <strong>spent</strong> two months in San Francisco, where he <strong>commissioned</strong> equipment in the field. Today his week <strong>is</strong> a schedule: he <strong>reviews</strong> the <strong>specification</strong>, he <strong>prepares</strong> the factory <strong>inspection</strong>, and he <strong>checks</strong> <strong>compliance</strong> with the European standard, because <strong>compliance</strong> <strong>is</strong> mandatory. The next <strong>milestone</strong> <strong>is</strong> three weeks away and the test report, the first <strong>deliverable</strong>, <strong>has not arrived</strong> yet. The team <strong>has been waiting</strong> for the revised <strong>specification</strong> <strong>since</strong> March, the <strong>deadline</strong> <strong>is</strong> fixed, and the extra training the client asked for <strong>is</strong> outside the <strong>scope</strong>. Every <strong>stakeholder</strong> <strong>wants</strong> a schedule they can trust.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Por que dizemos "I have worked in railway signaling for eight years" e n&#227;o "I work in railway signaling for eight years"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque come&#231;ou no passado e continua at&#233; agora &mdash; present perfect com for.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque a a&#231;&#227;o terminou e n&#227;o tem mais liga&#231;&#227;o com o presente.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque &#233; uma rotina que ele repete toda semana.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "In 2023, he spent two months in San Francisco" usa past simple porque:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A experi&#234;ncia continua at&#233; hoje.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &#201; um per&#237;odo terminado, com tempo terminado (in 2023).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &#201; algo que est&#225; acontecendo agora.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. "The team has been waiting for the revised specification since March." O que essa frase diz?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A equipe esperou em mar&#231;o e j&#225; recebeu o documento.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A espera come&#231;ou em mar&#231;o e CONTINUA at&#233; agora &mdash; o documento n&#227;o chegou.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A equipe vai come&#231;ar a esperar em mar&#231;o.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. Which sentence about his current role is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "He is overseeing the commissioning since eight years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "He oversees the commissioning and runs a weekly status meeting."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "He has overseen the commissioning in 2023."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Simple vs Present Perfect vs Present Perfect Continuous vs Past Simple</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como contar a sua trajet&#243;ria com o tempo verbal certo &mdash; o que todo entrevistador e todo fornecedor testa nos primeiros dois minutos (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Simple<br>I / you / we + verb (he/she + s)</td><td style="padding:.6rem">Cargo atual e rotina. Current role and routine.</td><td style="padding:.6rem">I <strong>oversee</strong> the commissioning.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present Perfect<br>have / has + past participle</td><td style="padding:.6rem">Experi&#234;ncia e dura&#231;&#227;o at&#233; agora. Experience and duration up to now (for / since).</td><td style="padding:.6rem">I <strong>have worked</strong> in signaling for eight years.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present Perfect Continuous<br>have been + verb-ing</td><td style="padding:.6rem">Atividade que come&#231;ou no passado e CONTINUA agora. Still going on.</td><td style="padding:.6rem">I <strong>have been working</strong> with German suppliers since 2019.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Past Simple<br>verb + -ed / irregular</td><td style="padding:.6rem">A&#231;&#227;o terminada, tempo terminado. Finished action, finished time (in 2023).</td><td style="padding:.6rem">I <strong>spent</strong> two months in San Francisco in 2023.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa (present perfect)</td><td style="padding:.6rem">have / has + not + partic&#237;pio. Na fala, contra&#237;do: <strong>haven't</strong>.</td><td style="padding:.6rem">We <strong>haven't</strong> received the specification.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">How long + have + sujeito + partic&#237;pio?</td><td style="padding:.6rem"><strong>How long have you been</strong> in signaling?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">for vs since</td><td style="padding:.6rem" colspan="2"><strong>for</strong> + per&#237;odo (for eight years) &middot; <strong>since</strong> + ponto de partida (since 2019)</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (erro de brasileiro):</strong> em portugu&#234;s dizemos "sou engenheiro h&#225; oito anos" e "trabalho com alem&#227;es desde 2019" &mdash; os dois no PRESENTE. Em ingl&#234;s, dura&#231;&#227;o at&#233; agora <strong>nunca</strong> usa o present simple: "I am an engineer for eight years" est&#225; errado &mdash; o certo &#233; "I <strong>have been</strong> an engineer for eight years" (na fala, <strong>I've been</strong>).</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Kick-Off Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma kick-off call com um fornecedor internacional na ordem correta.</p>
      <div class="order-container" id="order-l1">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Describe your current role: what you oversee and which lines you work on.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Agree on the next step and confirm who sends what, and by when.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Thank the supplier for joining and confirm everyone can hear you.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Raise the delay on the specification and ask about the factory inspection.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l1')"><span class="order-num">?</span><span class="order-text">Introduce yourself: your name, your company and how long you have been in signaling.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l1')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem qualquer reuni&#227;o ou entrevista em ingl&#234;s.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma reuni&#227;o ou entrevista em ingl&#234;s.</p>
      <div class="quiz-item"><div class="quiz-question">The supplier's project manager asks: "So, tell me about your role." You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I do the signaling things in the company."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I'm a signaling engineer at Motiva, and I oversee the commissioning of the signaling system on two metro lines."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I'm overseeing the commissioning since eight years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">She asks: "How long have you been in signaling?" The best answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am in signaling for eight years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I've worked in railway signaling for eight years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I work in railway signaling since eight years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to mention a finished period of your career. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "In 2023, I spent two months in San Francisco."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "In 2023, I have spent two months in San Francisco."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "In 2023, I am spending two months in San Francisco."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The specification has not arrived and you are still waiting. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We wait for the specification since March."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We've been waiting for the specification since March."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We waited for the specification since March."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You didn't understand a question and you need a moment. The most professional move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Answer something vague and hope nobody notices.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, could you rephrase that? I want to make sure I understand."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Apologize for your English and switch to Portuguese.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 90 segundos, sem script. Esta grava&#231;&#227;o &#233; o seu BASELINE: vamos ouvi-la de novo na aula 12 e na aula 24.</p>
      <div class="think-card">
        <div class="think-question">You are starting a video call with a new international supplier. Introduce yourself: your current role at Motiva (present simple), how long you have been in railway signaling (present perfect, for/since), who you have been working with since 2019 (present perfect continuous), and what you did in San Francisco in 2023 (past simple). Finish with your main concern on the project. Take your time and don't read from a script.</div>
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
