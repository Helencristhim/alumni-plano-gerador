#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder Simone Aula 3 — Email Essentials: Corporate Emails.
Gera professor + aluno a partir do shell da Elaine aula15 (CSS/JS verbatim),
trocando accent + conteudo + audioMap + data-teacher. Conteudo 100% ORIGINAL (REGRA 39).
Auto-monta audioMap escaneando speakText()/data-phrase do HTML gerado -> phrases.json.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))           # wt-simone
PROF_TPL = '/tmp/elaine-prof.html'
ALUNO_TPL = '/tmp/elaine-aluno.html'
SLUG = 'simone-quiles-de-santana-marques'
OUT_PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula3.html')
OUT_ALUNO = os.path.join(ROOT, 'public', 'aluno', SLUG + '-aula3.html')
AUDIO_WEB = '/audio/' + SLUG + '/'

# ----------------------------------------------------------------------------
# AUDIO: phrase -> voice. arthur=male, ellen=female. Words(1-2)=arthur.
# ----------------------------------------------------------------------------
WORDS = ['Subject line','Recipient','Attachment','Regarding','Forward','Reply','Follow up','Best regards']
PHRASES = {w: 'arthur' for w in WORDS}
PHRASES.update({
    # emergency (pre-class welcome)
    'Could you repeat that, please?': 'ellen',
    'I am not sure I understand. Could you explain?': 'arthur',
    'Could you speak more slowly, please?': 'ellen',
    'I am not sure how to say this in English.': 'arthur',
    'Thank you for your patience.': 'ellen',
    # callback aula 2 (present simple / draft / deadline)
    'I usually start work at nine o’clock.': 'ellen',
    'I often draft contracts in the afternoon.': 'arthur',
    # core email sentences
    'I am writing regarding the contract.': 'ellen',
    'Please find the report attached.': 'arthur',
    'Could you please send me the document?': 'ellen',
    'I look forward to your reply.': 'arthur',
    'Please find the document attached.': 'ellen',
    'Could you please reply by Friday?': 'arthur',
    'I will forward the email to the legal team.': 'ellen',
    'Best regards, Simone.': 'arthur',
    'I will follow up next week.': 'ellen',
    'Could you please send me the file?': 'arthur',
    'Dear Mr. Carter, I hope this email finds you well.': 'ellen',
    # dialogue (David = arthur, Simone = ellen)
    'Hi Simone, did you send the email to the client?': 'arthur',
    'Not yet. I am writing it now, regarding the new contract.': 'ellen',
    'Great. Please attach the signed document.': 'arthur',
    'Of course. I will add it as an attachment.': 'ellen',
    'Can you also forward it to the legal team?': 'arthur',
    'Sure. I will forward it to them today.': 'ellen',
    'Perfect. Ask them to reply by Friday.': 'arthur',
    'I will. I will also follow up on Monday.': 'ellen',
    'Excellent. How do you close the email?': 'arthur',
    'I always write Best regards and my name.': 'ellen',
    'That is very professional. Thank you, Simone.': 'arthur',
    'You are welcome. I will send it now.': 'ellen',
})
# listening / order pseudo-keys: key -> (text, voice)
LISTENING = {
    'listening3_email': ("Dear Mr. Carter. I am writing regarding the service contract for Telefonica. "
                         "Please find the signed document attached. Could you please review it and reply by Friday? "
                         "If you have any questions, let me know. Best regards, Simone.", 'ellen'),
    'listening3_followup': ("Hello, this is Simone from Telefonica. I am following up on the email I sent last week "
                            "regarding the contract. I have not received your reply yet. Could you please confirm that "
                            "you received the attachment? Thank you, and best regards.", 'ellen'),
    '[order-l3]': ("Simone opens a new email and writes the subject line and the recipient. She adds the contract as an "
                   "attachment. She writes a short message regarding the contract. She closes with Best regards and her "
                   "name. Then she sends the email and follows up the next week.", 'ellen'),
}

def fname(s):
    s = s.lower().replace('’', "'")
    s = re.sub(r"[^a-z0-9]+", '_', s).strip('_')
    return s[:60] + '.mp3'

# ============================================================================
# CONTENT FRAGMENTS
# ============================================================================
TITLE_PROF = ('<title>Professor View &mdash; Simone Quiles de Santana Marques | Aula 3 | '
              'Email Essentials: Corporate Emails | Business English | Alumni by Better</title>')
TITLE_ALUNO = ('<title>Aluno &mdash; Simone Quiles de Santana Marques | Aula 3 | '
               'Email Essentials: Corporate Emails | Business English | Alumni by Better</title>')

SCENARIO = """<!--
SCENARIO FIT -- Aula 3 (ORIGINAL, REGRA 39)
Can-do: "I can write and answer a corporate email: open formally, say what it is regarding, attach a document, make a polite request, and close professionally."
Foco-alvo: email structures -- opening / body / closing; pedidos formais ("Could you please...?", "Please find attached...", "I look forward to your reply.").
Vocab-alvo: subject line, recipient, attachment, regarding, forward, reply, follow up, best regards.
Cenario: Simone (advogada corporativa na Telefonica) escreve/responde um email a um cliente (Mr. Carter) sobre um contrato, e alinha o envio com o colega David (Londres).
Por que elicita o alvo: escrever um email corporativo OBRIGA abrir formalmente, dizer o assunto (regarding), anexar (attachment), pedir resposta (reply) e fechar (best regards).

CONTINUIDADE -- Aula 3
Itens novos: subject line, recipient, attachment, regarding, forward, reply, follow up, best regards; "Please find ... attached.", "Could you please ...?", "I look forward to your reply.", "Best regards".
Callback (slide 2 warm-up): retoma ATIVAMENTE 2 itens da Aula 2 (rotina/present simple) -- Simone ouve e repete "I usually start work at nine o'clock." e "I often draft contracts in the afternoon." e faz a ponte: depois de rascunhar os contratos, agora aprende a ESCREVER os emails ao redor deles.
-->"""

HEADER_PROF = """  <div class="header-content">
    <div class="passport-badge">Business + Legal English -- 48 Aulas</div>
    <h1>Simone Quiles de Santana Marques</h1>
    <p class="subtitle">De "sobreviver em reuni&otilde;es internacionais" a negociar contratos com confian&ccedil;a em ingl&ecirc;s</p>
    <div class="student-info">
      <span>A2-B1</span>
      <span>Advogada Corporativa</span>
      <span>Contratos e M&amp;A na Telef&ocirc;nica</span>
      <span>60 min / Online</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label"><span>Progresso Geral</span><span id="progressPercent">0%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
<div class="stamps-row">
<div class="stamp" id="stamp1" data-label="Contracts" style="background-image:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80')"></div>
<div class="stamp" id="stamp2" data-label="Corporate" style="background-image:url('https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=200&q=80')"></div>
<div class="stamp" id="stamp3" data-label="Meetings" style="background-image:url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=200&q=80')"></div>
<div class="stamp" id="stamp4" data-label="Legal" style="background-image:url('https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=200&q=80')"></div>
<div class="stamp" id="stamp5" data-label="Global" style="background-image:url('https://images.unsplash.com/photo-1526470608268-f674ce90ebd4?w=200&q=80')"></div>
</div>
    </div>
  """

# ---- PLANNING ----
def planning_block():
    rows = [
        (1,'Who Is Simone? -- Diagnostic + Self-Introduction','Present simple, professional vocabulary','Professional Identity Card + diagnostic','Record 90-sec self-introduction'),
        (2,'My Daily Routine -- Work at Telefonica','Present simple: affirm/neg/questions','Daily routine description','Listen to BEP + write 3 phrases'),
        (3,'Email Essentials -- Corporate Emails','Email structures: opening/body/closing','Read and respond to an email','Write a reply to a fictional email'),
        (4,'Phone and Video Calls','Phone phrases: opening/clarifying/closing','Simulated conference call','Record a voicemail in English'),
        (5,'Small Talk That Works','Question forms, conversation starters','Networking role-play','Watch a TED Talk + note phrases'),
        (6,'Meeting Basics','Modal verbs: can/could/should','Meeting participation simulation','Summarize a meeting in 5 sentences'),
        (7,'Expressing Opinions','Opinion phrases: I think, In my view','Debate simulation','Write an opinion paragraph'),
        (8,'Giving Updates','Present continuous + time expressions','Team update presentation','Record a 2-min update'),
        (9,'Asking Smart Questions','Question words + indirect questions','Q&amp;A session role-play','Prepare 5 meeting questions'),
        (10,'Travel English I','Travel vocabulary, "Could I..." requests','Airport/hotel role-play','Listen to a travel podcast'),
    ]
    tr = '\n'.join('      <tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in rows)
    return """<div class="tab-content active" id="tab-planning">

<div class="info-grid">
  <div class="info-item"><label>Nome</label><span>Simone Quiles de Santana Marques</span></div>
  <div class="info-item"><label>Profiss&atilde;o</label><span>Advogada Corporativa</span></div>
  <div class="info-item"><label>Empresa</label><span>Telef&ocirc;nica -- Contratos &amp; M&amp;A</span></div>
  <div class="info-item"><label>N&iacute;vel</label><span>A2-B1</span></div>
  <div class="info-item"><label>Foco</label><span>Business + Legal English</span></div>
  <div class="info-item"><label>Total de Aulas</label><span>48 aulas de 60 min</span></div>
  <div class="info-item"><label>Formato</label><span>Online (Zoom)</span></div>
  <div class="info-item"><label>Aula de Hoje</label><span>03 -- Email Essentials</span></div>
</div>

<div class="journey-box">
  <h4>Jornada de Transforma&ccedil;&atilde;o</h4>
  <p><strong>De:</strong> Profissional que evita escrever em ingl&ecirc;s e copia modelos prontos sem entender a estrutura</p>
  <p style="margin-top:.5rem"><strong>Para:</strong> Advogada que abre, conduz e fecha um email corporativo com clareza e confian&ccedil;a, em qualquer contexto internacional</p>
</div>

<div style="padding:1.2rem;background:var(--accent-dim);border:1px solid rgba(136,19,55,.2);border-radius:10px;margin-bottom:1.5rem">
  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-bottom:.5rem">Promessa do Programa</h4>
  <p style="font-size:.9rem;line-height:1.7">"De 'preciso de ajuda para cada email' para 'eu escrevo, respondo e fa&ccedil;o follow-up sozinha.'"</p>
</div>

<div class="sw-grid">
  <div class="sw-box strengths">
    <h4>For&ccedil;as</h4>
    <ul>
      <li>Vocabul&aacute;rio t&eacute;cnico-jur&iacute;dico s&oacute;lido em portugu&ecirc;s</li>
      <li>Disciplina e organiza&ccedil;&atilde;o de rotina de trabalho</li>
      <li>Leitura de contratos em ingl&ecirc;s no dia a dia</li>
      <li>Motiva&ccedil;&atilde;o clara: contexto de contratos e M&amp;A</li>
      <li>Aten&ccedil;&atilde;o a detalhes e formalidade</li>
    </ul>
  </div>
  <div class="sw-box weaknesses">
    <h4>Pontos de Melhoria</h4>
    <ul>
      <li>Inseguran&ccedil;a ao produzir texto formal do zero</li>
      <li>Registro: alternar entre formal e informal</li>
      <li>Frases-pedido educadas ("Could you please...?")</li>
      <li>Conectar abertura, corpo e fechamento de um email</li>
      <li>Flu&ecirc;ncia oral ao falar sobre o pr&oacute;prio trabalho</li>
    </ul>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">Curr&iacute;culo -- primeiras 10 de 48 Aulas</h3>
<div class="curriculum-wrapper">
  <table class="curriculum-table">
    <thead><tr><th>#</th><th>Tema</th><th>Foco Lingu&iacute;stico</th><th>Atividade Principal</th><th>Homework</th></tr></thead>
    <tbody>
""" + tr + """
    </tbody>
  </table>
</div>

</div><!-- /tab-planning -->"""

# ---- PRE-CLASS ----
VOCAB = [
    ('Subject line','the short title that says what the email is about','"Write a clear subject line." (assunto)','assunto'),
    ('Recipient','the person who receives the email','"Add the recipient’s email address." (destinatário)','destinatário'),
    ('Attachment','a file you send together with the email','"The contract is the attachment." (anexo)','anexo'),
    ('Regarding','about / concerning (formal)','"I am writing regarding the contract." (a respeito de)','a respeito de'),
    ('Forward','to send a received email to another person','"I will forward it to the team." (encaminhar)','encaminhar'),
    ('Reply','to answer an email','"Please reply by Friday." (responder)','responder'),
    ('Follow up','to send a second message to check progress','"I will follow up next week." (dar seguimento)','dar seguimento'),
    ('Best regards','a polite, formal way to close an email','"Best regards, Simone." (atenciosamente)','atenciosamente'),
]
PT_OPTS = ['assunto','destinatário','anexo','a respeito de','encaminhar','responder','dar seguimento','atenciosamente']

def shuffle(seq, k):
    # deterministic rotation so option order differs from word order (REGRA 24)
    return seq[k % len(seq):] + seq[:k % len(seq)]

def vocab_cards_pc():
    out = []
    for w, d, ex, pt in VOCAB:
        out.append('        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">%s</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">%s</span></div><div class="vocab-card-example">%s</div></div><button class="audio-btn" onclick="speakText(\'%s\',this)">Listen</button></div>' % (w, d, ex, w))
    return '\n'.join(out)

def match_rows_pc():
    out = []
    for i, (w, d, ex, pt) in enumerate(VOCAB):
        opts = shuffle(PT_OPTS, i + 3)
        os_ = '<option value="">Selecione...</option>' + ''.join('<option value="%s">%s</option>' % (o, o) for o in opts)
        out.append('        <div class="match-row" data-answer="%s"><span class="match-word">%s</span><select onchange="checkMatch(this)">%s</select></div>' % (pt, w, os_))
    return '\n'.join(out)

def exercises_inner():
    fills = [
        ('I am writing _____ the contract.','regarding','Dica: a respeito de','I am writing regarding the contract.'),
        ('Please find the document _____.','attached','Dica: anexado','Please find the document attached.'),
        ('Could you please _____ by Friday?','reply','Dica: responder','Could you please reply by Friday?'),
        ('I will _____ the email to the legal team.','forward','Dica: encaminhar','I will forward the email to the legal team.'),
        ('Best _____, Simone.','regards','Dica: fechamento formal','Best regards, Simone.'),
        ('I will follow _____ next week.','up','Dica: follow ___ = dar seguimento','I will follow up next week.'),
    ]
    fill_html = '\n'.join('      <div class="fill-blank-item"><div class="fill-blank-sentence">"%s" <input class="blank-input" data-answer="%s" data-hint="%s" data-phrase="%s" placeholder="___"></div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>' % (
        q.replace('_____','<span style="white-space:nowrap">___</span>') if False else q.split('_____')[0], a, h, p) for (q,a,h,p) in fills)
    # rebuild fill items properly with the input inside the sentence
    fill_items = []
    for q, a, h, p in fills:
        before, after = q.split('_____')
        fill_items.append('      <div class="fill-blank-item"><div class="fill-blank-sentence">"%s<input class="blank-input" data-answer="%s" data-hint="%s" data-phrase="%s" placeholder="___">%s"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>' % (before, a, h, p, after))
    fill_html = '\n'.join(fill_items)

    order_items = [
        (1,'Simone opens a new email and writes the subject line.'),
        (2,'She adds the recipient and writes "Dear Mr. Carter".'),
        (3,'She adds the contract as an attachment.'),
        (4,'She writes a short message regarding the contract.'),
        (5,'She closes with "Best regards" and follows up the next week.'),
    ]
    # present in shuffled visual order
    visual = [order_items[2], order_items[0], order_items[4], order_items[1], order_items[3]]
    order_html = '\n'.join('        <div class="order-item" draggable="true" data-order="%d" onclick="selectOrderItem(this,\'order-l3\')"><span class="order-num">?</span><span class="order-text">%s</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>' % (o, t) for (o, t) in visual)

    speech = ['I am writing regarding the contract.','Please find the document attached.','Could you please send me the file?','I look forward to your reply.']
    speech_html = '\n'.join('      <div class="speech-card" data-phrase="%s"><div class="speech-phrase">%s</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>' % (s, s) for s in speech)

    return """<div class="tab-content" id="tab-exercises">
<div class="exercise-section" style="margin-bottom:1.5rem">
  <div class="section-header-row">
    <h4>Welcome back, Simone!</h4>
    <span class="badge badge-vocab">Onboarding</span>
  </div>
  <p style="font-size:.88rem;color:var(--text-dim);margin-bottom:1rem">Antes da aula, complete as atividades de Pre-class. Aqui est&atilde;o 5 frases de emerg&ecirc;ncia que voc&ecirc; pode usar a qualquer momento na aula:</p>
  <div class="survival-card">
    <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Could you repeat that, please?</span><span class="sp-pt">Poderia repetir, por favor?</span><button class="audio-btn" onclick="speakText('Could you repeat that, please?',this)">Listen</button></div>
    <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I am not sure I understand. Could you explain?</span><span class="sp-pt">N&atilde;o tenho certeza se entendi. Poderia explicar?</span><button class="audio-btn" onclick="speakText('I am not sure I understand. Could you explain?',this)">Listen</button></div>
    <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Could you speak more slowly, please?</span><span class="sp-pt">Poderia falar mais devagar, por favor?</span><button class="audio-btn" onclick="speakText('Could you speak more slowly, please?',this)">Listen</button></div>
    <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I am not sure how to say this in English.</span><span class="sp-pt">N&atilde;o tenho certeza de como dizer isso em ingl&ecirc;s.</span><button class="audio-btn" onclick="speakText('I am not sure how to say this in English.',this)">Listen</button></div>
    <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Thank you for your patience.</span><span class="sp-pt">Obrigada pela paci&ecirc;ncia.</span><button class="audio-btn" onclick="speakText('Thank you for your patience.',this)">Listen</button></div>
  </div>
</div>
<div class="lesson-card" id="ex-lesson-3">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1596526131083-e8c633c948d2?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 03 -- Pre-class</div>
      <h3>Email Essentials -- Corporate Emails</h3>
      <div class="lesson-desc">Write and answer a corporate email: subject line, recipient, attachment, regarding, forward, reply, follow up, best regards. Structures: "Please find ... attached.", "Could you please ...?", "I look forward to your reply."</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
""" + vocab_cards_pc() + """
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its translation.</p>
      <div class="match-grid" id="match-l3">
""" + match_rows_pc() + """
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l3')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the email and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Simone writes an email to a client. The <strong>subject line</strong> says "Service Contract -- Telefonica". The <strong>recipient</strong> is Mr. Carter. She writes, "Dear Mr. Carter, I am writing <strong>regarding</strong> our contract. Please find the signed document <strong>attached</strong>. Could you please <strong>reply</strong> by Friday? I look forward to your reply. <strong>Best regards</strong>, Simone." Later, she will <strong>forward</strong> the email to the legal team and <strong>follow up</strong> next week.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Como Simone diz o assunto do email? / How does she say what the email is about?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am writing about regarding our contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am writing regarding our contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I writing our contract."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Como ela informa o anexo? / How does she mention the attachment?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Please find the signed document attached."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I send you the document in attach."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The document is in attachment."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Como ela fecha o email? / How does she close the email?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Bye bye, Simone."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Best regard, Simone."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Best regards, Simone."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Opening, Body, Closing</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">As tr&ecirc;s partes de um email corporativo. / The three parts of a corporate email.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Part / Parte</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example / Exemplo</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Opening / Abertura</td><td style="padding:.6rem">Cumprimentar e dizer o assunto / Greet &amp; state the topic</td><td style="padding:.6rem">Dear Mr. Carter, I am writing <strong>regarding</strong> the contract.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Body / Corpo</td><td style="padding:.6rem">Anexar e fazer o pedido / Attach &amp; request</td><td style="padding:.6rem"><strong>Please find</strong> the document <strong>attached</strong>. <strong>Could you please</strong> reply by Friday?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Closing / Fechamento</td><td style="padding:.6rem">Despedida educada / Polite sign-off</td><td style="padding:.6rem">I look forward to your reply. <strong>Best regards</strong>, Simone.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Tip:</strong> use <strong>"Please find attached"</strong> (n&atilde;o "I send you in attach") e <strong>"I look forward to your reply"</strong> (n&atilde;o "I wait your reply").</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the full sentence.</p>
""" + fill_html + """
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Email Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the steps in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l3]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l3">
""" + order_html + """
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l3')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation Practice</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Pratique as frases que voc&ecirc; vai usar nos emails.</p>
""" + speech_html + """
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best option for each situation.</p>
      <div class="quiz-item"><div class="quiz-question">You want to say the email is about the contract. / Voc&ecirc; quer dizer o assunto.</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I am writing regarding the contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I write for the contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This email is the contract."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You attached a file. How do you say it? / Voc&ecirc; anexou um arquivo.</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I send you in attach."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Please find the file attached."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The file is in the attach."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You ask the client to answer. / Voc&ecirc; pede uma resposta.</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Could you please reply by Friday?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Reply me until Friday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You reply Friday."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You close the email politely. / Voc&ecirc; fecha o email.</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I look forward to your reply. Best regard, Simone."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I look forward to your reply. Best regards, Simone."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I wait your reply. Bye, Simone."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">No right or wrong here. Think in English. Tap the mic and speak freely.</p>
      <div class="think-card"><div class="think-question">Imagine you write a corporate email to a client about a contract. Say hello, say what the email is regarding, mention the attachment, ask for a reply by Friday, and close politely. Use: I am writing regarding..., Please find ... attached, Could you please ...?, I look forward to your reply, Best regards.</div><div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div><div id="think-result-3"></div></div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 3</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I am writing regarding the contract.</span><span class="sp-pt">Escrevo a respeito do contrato.</span><button class="audio-btn" onclick="speakText('I am writing regarding the contract.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">Please find the document attached.</span><span class="sp-pt">Segue o documento em anexo.</span><button class="audio-btn" onclick="speakText('Please find the document attached.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Could you please reply by Friday?</span><span class="sp-pt">Poderia responder at&eacute; sexta?</span><button class="audio-btn" onclick="speakText('Could you please reply by Friday?',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I will follow up next week.</span><span class="sp-pt">Vou dar seguimento na semana que vem.</span><button class="audio-btn" onclick="speakText('I will follow up next week.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Best regards.</span><span class="sp-pt">Atenciosamente.</span><button class="audio-btn" onclick="speakText('Best regards',this)">Listen</button></div>
    </div>

  </div><!-- /lesson-body -->
</div><!-- /lesson-card L3 -->

</div><!-- /tab-exercises -->"""

# ---- IN CLASS MENU ----
INCLASS_MENU = """<div class="tab-content" id="tab-inclass">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 3</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">03</div>
      <div><div style="font-weight:600;font-size:.95rem">Email Essentials -- Corporate Emails</div><div style="font-size:.8rem;color:var(--text-dim)">Opening, body &amp; closing -- 28 slides</div></div>
    </div>
  </div>
</div>"""

# ---- COMPLEMENTARY ----
COMPLEMENTARY = """<div class="tab-content" id="tab-complementary">
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:.5rem">Materiais Complementares -- Aula 3</h3>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: Email Essentials -- Corporate Emails. Refor&ccedil;o fora de aula -- marque como conclu&iacute;do ao terminar.</p>

<div class="media-grid">
  <div class="media-card-wrapper" data-media="l3-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="17 2 12 7 7 2" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">S&eacute;rie</div>
        <h5>Suits -- the law-firm emails &amp; deals</h5>
        <p>S&eacute;rie sobre um escrit&oacute;rio de advocacia corporativo em Nova York. Perfeita para o seu contexto de contratos e M&amp;A: observe como os personagens escrevem emails, anexam documentos e fazem follow-up de neg&oacute;cios.</p>
        <p class="media-tip">Dica: assista com legenda em ingl&ecirc;s e anote toda express&atilde;o de email formal (regarding, attached, best regards) que aparecer.</p>
      </div>
    </div>
  </div>

  <div class="media-card-wrapper" data-media="l3-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.43z" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>"How to Write a Professional Email in English" (Business English)</h5>
        <p>V&iacute;deo curto mostrando abertura, corpo e fechamento de um email formal em ingl&ecirc;s, com as mesmas estruturas da aula: "I am writing regarding...", "Please find attached...", "Best regards".</p>
        <p class="media-tip">Dica: pause a cada frase-modelo e escreva a sua pr&oacute;pria vers&atilde;o para um email de contrato.</p>
        <a href="https://www.youtube.com/results?search_query=how+to+write+a+professional+email+in+english+business" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
      </div>
    </div>
  </div>

  <div class="media-card-wrapper" data-media="l3-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>Business English Pod (BEP) -- procure um epis&oacute;dio sobre emails</h5>
        <p>Podcast de ingl&ecirc;s de neg&oacute;cios com epis&oacute;dios sobre escrever emails, fazer pedidos educados e follow-up. Continua o BEP que voc&ecirc; ouviu na Aula 2.</p>
        <p class="media-tip">Dica: ou&ccedil;a um epis&oacute;dio sobre "writing emails" duas vezes e anote 5 frases-modelo &uacute;teis para o seu trabalho.</p>
        <a href="https://www.businessenglishpod.com/" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Open BEP &#8599;</a>
      </div>
    </div>
  </div>
</div>

</div><!-- /tab-complementary -->"""

# write the slides module separately (imported)
exec(open(os.path.join(HERE, 'slides.py')).read())

# ============================================================================
# AUDIO MAP (auto from generated HTML)
# ============================================================================
def build_audiomap(*htmls):
    found = set()
    for h in htmls:
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", h):
            found.add(m.group(1).replace("\\'", "'"))
        for m in re.finditer(r'data-phrase="([^"]+)"', h):
            found.add(m.group(1))
    # resolve voices + files
    amap = {}
    phrases_json = []
    unknown = []
    seen_files = {}
    for p in sorted(found):
        if p in LISTENING:
            text, voice = LISTENING[p]
            f = fname(p.strip('[]'))
        elif p in PHRASES:
            text, voice = p, PHRASES[p]
            f = fname(p)
        else:
            unknown.append(p); continue
        amap[p] = AUDIO_WEB + f
        if f not in seen_files:
            seen_files[f] = True
            phrases_json.append({'text': text, 'voice': voice, 'file': f})
    if unknown:
        raise SystemExit('PHRASES sem voz definida:\n  ' + '\n  '.join(repr(u) for u in unknown))
    return amap, phrases_json

# ============================================================================
# ASSEMBLE
# ============================================================================
def replace_between(text, start, end, new, label):
    pat = re.escape(start) + r'.*?' + re.escape(end)
    new_text, n = re.subn(pat, lambda m: new, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('replace_between FALHOU (%s): %d matches' % (label, n))
    return new_text

def replace_once(text, old, new, label):
    if text.count(old) < 1:
        raise SystemExit('replace_once: anchor ausente (%s)' % label)
    return text.replace(old, new, 1)

def scrub_leftovers(text):
    # neutraliza PII da Elaine em arrays JS orfaos do template (dead code, sem DOM no arquivo de 1 aula)
    reps = {
        '"I am from Brazil. I live in Indaiatuba, a small city in São Paulo."':
            '"I am from Brazil. I live in São Paulo."',
        '"I am a lawyer and I manage a family company."':
            '"I am a corporate lawyer at Telefonica."',
        'I would like to check in, please. My name is Elaine Pinho.':
            'I would like to check in, please. My name is Simone Quiles.',
        'I have a reservation under Elaine Pinho.':
            'I have a reservation under Simone Quiles.',
    }
    for a, b in reps.items():
        text = text.replace(a, b)
    return text

def accent_swap(text):
    text = text.replace('#5E4B6D', '#881337')   # --accent
    text = text.replace('#C4A8D8', '#E8A0B4')   # light-on-dark
    text = text.replace('#E0CFF0', '#F2C4D0')   # lighter-on-image
    text = text.replace('rgba(94,75,109,', 'rgba(136,19,55,')
    return text

def build_prof(amap):
    t = open(PROF_TPL, encoding='utf-8').read()
    # title
    t = replace_between(t, '<title>', '</title>', TITLE_PROF, 'title-prof')
    # scenario comment
    t = re.sub(r'<!--\nSCENARIO FIT.*?-->', lambda m: SCENARIO, t, count=1, flags=re.S)
    # accent vars (:root) + accent-light value
    t = t.replace('--accent-light: #C4A8D8;', '--accent-light: #E8A0B4;')
    t = t.replace('--accent-on-dark: #E0CFF0;', '--accent-on-dark: #F2C4D0;')
    # slide counter
    t = t.replace('<span class="slide-counter" id="slideCounter">01 / 28</span>',
                  '<span class="slide-counter" id="slideCounter">01 / 28</span>', 1)
    # header-content
    t = replace_between(t, '<div class="header-content">', '</div>\n</div>\n\n\n<div class="container">',
                        HEADER_PROF + '</div>\n</div>\n\n\n<div class="container">', 'header-prof')
    # supabase config
    t = replace_once(t, "window.STUDENT_SLUG='elaine-mieko-pinho';window.TOTAL_AULAS=32;",
                     "window.STUDENT_SLUG='" + SLUG + "';window.TOTAL_AULAS=48;", 'supabase')
    # planning
    t = replace_between(t, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->',
                        planning_block(), 'planning')
    # exercises
    t = replace_between(t, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->',
                        exercises_inner(), 'exercises')
    # inclass
    t = replace_between(t, '<div class="tab-content" id="tab-inclass">',
                        '</div>\n\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->',
                        INCLASS_MENU + '\n\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->', 'inclass')
    # complementary
    t = replace_between(t, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->',
                        COMPLEMENTARY, 'complementary')
    # slides
    t = replace_between(t, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->',
                        slides_block(), 'slides')
    # audioMap
    t = replace_between(t, 'var audioMap = {', '};', 'var audioMap = ' + json.dumps(amap, ensure_ascii=False, indent=0).replace('\n', '') + ';', 'audiomap-prof')
    # exitSlideMode redirect
    t = t.replace('/professor/elaine-mieko-pinho.html', '/professor/' + SLUG + '.html')
    # localStorage keys + totalLessons
    t = t.replace('alumni-progress-elaine-mieko-pinho', 'alumni-progress-' + SLUG)
    t = t.replace('elaine-mieko-pinho-aula9-professor', SLUG + '-aula3-professor')
    t = t.replace('var totalLessons = 9;', 'var totalLessons = 3;')
    t = accent_swap(t)
    t = scrub_leftovers(t)
    return t

def build_aluno(amap):
    t = open(ALUNO_TPL, encoding='utf-8').read()
    t = replace_between(t, '<title>', '</title>', TITLE_ALUNO, 'title-aluno')
    t = re.sub(r'<!--\nSCENARIO FIT.*?-->', lambda m: SCENARIO, t, count=1, flags=re.S)
    t = t.replace('--accent-light: #C4A8D8;', '--accent-light: #E8A0B4;')
    t = t.replace('--accent-on-dark: #E0CFF0;', '--accent-on-dark: #F2C4D0;')
    t = replace_between(t, '<div class="header-content">', '</div>\n</div>\n\n\n<div class="container">',
                        HEADER_PROF + '</div>\n</div>\n\n\n<div class="container">', 'header-aluno')
    t = replace_once(t, "window.STUDENT_SLUG='elaine-mieko-pinho';window.TOTAL_AULAS=32;",
                     "window.STUDENT_SLUG='" + SLUG + "';window.TOTAL_AULAS=48;", 'supabase-aluno')
    # aluno exercises (active)
    ex = exercises_inner().replace('<div class="tab-content" id="tab-exercises">',
                                   '<div class="tab-content active" id="tab-exercises">', 1)
    t = replace_between(t, '<div class="tab-content active" id="tab-exercises">', '</div><!-- /tab-exercises -->',
                        ex, 'exercises-aluno')
    t = replace_between(t, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->',
                        COMPLEMENTARY, 'complementary-aluno')
    t = replace_between(t, 'var audioMap = {', '};', 'var audioMap = ' + json.dumps(amap, ensure_ascii=False).replace('\n', '') + ';', 'audiomap-aluno')
    t = t.replace('alumni-progress-elaine-mieko-pinho', 'alumni-progress-' + SLUG)
    t = t.replace('elaine-mieko-pinho-aula9-aluno', SLUG + '-aula3-aluno')
    t = t.replace('var totalLessons = 9;', 'var totalLessons = 3;')
    t = accent_swap(t)
    t = scrub_leftovers(t)
    return t

if __name__ == '__main__':
    prof_slides = slides_block()
    ex_html = exercises_inner()
    amap, pj = build_audiomap(prof_slides, ex_html, COMPLEMENTARY)
    prof = build_prof(amap)
    open(OUT_PROF, 'w', encoding='utf-8').write(prof)
    aluno = build_aluno(amap)
    open(OUT_ALUNO, 'w', encoding='utf-8').write(aluno)
    json.dump(pj, open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('OK prof  ->', OUT_PROF, len(prof), 'bytes')
    print('OK aluno ->', OUT_ALUNO, len(aluno), 'bytes')
    print('audioMap entries:', len(amap), '| phrases to generate:', len(pj))
