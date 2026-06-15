# -*- coding: utf-8 -*-
"""Gera preclass.html (ex-lesson-4) da Simone aula 4 — Phone & Video Calls.
Mantem o formato exato do modelo (fabiana-aula4). Matching embaralhado (REGRA 24)."""
import random, os

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(404)

# (word, hint_def_en, example_en, pt_word)
VOCAB = [
    ("Voicemail", "a recorded message left when no one answers", "I left a voicemail when she did not pick up.", "Correio de voz", "correio de voz"),
    ("Hold on", "to wait for a short time on the phone", "Could you hold on while I open the contract?", "Aguardar", "aguardar"),
    ("Reach", "to succeed in contacting someone", "I tried to reach you all morning.", "Contatar", "contatar"),
    ("Available", "free and able to talk or meet", "Is Mr. Pearson available right now?", "Dispon&#237;vel", "dispon&#237;vel"),
    ("Connection", "the signal quality during a call", "Sorry, the connection is very weak today.", "Conex&#227;o", "conex&#227;o"),
    ("Mute", "to turn your microphone off", "Please mute your mic when you are not speaking.", "Silenciar", "silenciar"),
    ("Speak up", "to talk more loudly", "Could you speak up? I can barely hear you.", "Falar mais alto", "falar mais alto"),
    ("Call back", "to return someone's phone call", "I will call you back after the meeting.", "Retornar a liga&#231;&#227;o", "retornar a liga&#231;&#227;o"),
    ("Hang up", "to end a phone or video call", "Let us not hang up before we confirm the date.", "Desligar", "desligar"),
    ("Clarify", "to make something clearer", "Could you clarify the last clause for me?", "Esclarecer", "esclarecer"),
]

PT = [v[4] for v in VOCAB]

def esc_js(s):
    return s.replace("'", "\\'")

def vocab_cards():
    out = []
    for w, hint, ex, ptw, _ in VOCAB:
        out.append(
            '        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
            f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{hint}</span></div>'
            f'<div class="vocab-card-example">"{ex}" ({ptw})</div></div>'
            f'<button class="audio-btn" onclick="speakText(\'{esc_js(w)}\',this)">Listen</button></div>')
    return "\n".join(out)

def match_rows():
    out = []
    for w, _, _, _, ptw in VOCAB:
        opts = PT[:]
        # embaralha ate ficar diferente da ordem-base (REGRA 24)
        while True:
            random.shuffle(opts)
            if opts != PT:
                break
        opt_html = '<option value="">Selecione...</option>' + "".join(
            f'<option value="{o}">{o}</option>' for o in opts)
        out.append(
            f'        <div class="match-row" data-answer="{ptw}">'
            f'<span class="match-word" style="flex:0 0 130px">{w}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>')
    return "\n".join(out)

# Stage 1.5 fill-in (sentence_before, answer, hint, phrase, sentence_after)
FILLS = [
    ('"I tried to ', 'reach', 'Hint: succeed in contacting', 'I tried to reach you all morning.', ' you all morning."'),
    ('"Is Mr. Pearson ', 'available', 'Hint: free to talk now', 'Is Mr. Pearson available right now?', ' right now?"'),
    ('"Sorry, the ', 'connection', 'Hint: the signal quality', 'Sorry, the connection is very weak today.', ' is very weak today."'),
    ('"Could you ', 'clarify', 'Hint: make it clearer', 'Could you clarify the last clause for me?', ' the last clause for me?"'),
    ('"I will call you ', 'back', 'Hint: return the call', 'I will call you back after the meeting.', ' after the meeting."'),
    ('"Please ', 'mute', 'Hint: turn the mic off', 'Please mute your mic when you are not speaking.', ' your mic when you are not speaking."'),
]

def fills():
    out = []
    for before, ans, hint, phrase, after in FILLS:
        out.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{before}'
            f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{after}</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    return "\n".join(out)

# Stage 2 order items (text, correct_order)
ORDER = [
    ("Simone calls Mark back and opens the video call.", 2),
    ("Mark cannot reach Simone, so he leaves a voicemail.", 1),
    ("Simone closes the call and leaves a voicemail update for her team.", 5),
    ("The connection is weak, so they speak up and clarify the open points.", 3),
    ("They agree on the indemnity number and the new timeline.", 4),
]

def order_items():
    out = []
    for text, n in ORDER:
        out.append(
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
            f'<span class="order-num">?</span><span class="order-text">{text}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
    return "\n".join(out)

# Stage 3 speech cards (en, pt)
SPEECH = [
    ("Hi Mark, this is Simone speaking. I'm calling about the agreement.", "Oi Mark, aqui &#233; a Simone. Estou ligando sobre o contrato."),
    ("Sorry, could you speak up? The connection is weak.", "Desculpe, voc&#234; pode falar mais alto? A conex&#227;o est&#225; ruim."),
    ("Could you clarify the indemnity clause for me?", "Voc&#234; poderia esclarecer a cl&#225;usula de indeniza&#231;&#227;o para mim?"),
    ("Thanks for your time. I'll call you back this afternoon.", "Obrigada pelo seu tempo. Eu retorno a liga&#231;&#227;o &#224; tarde."),
]

def speech_cards():
    out = []
    for en, pt in SPEECH:
        out.append(
            f'      <div class="speech-card" data-phrase="{en}">\n'
            f'        <div class="speech-phrase">{en}</div>\n'
            f'        <div class="speech-translation">{pt}</div>\n'
            f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
            f'        <div class="speech-result"></div>\n      </div>')
    return "\n".join(out)

# Survival (en, pt)
SURVIVAL = [
    ("Hi, this is Simone speaking. I'm calling about the agreement.", "Oi, aqui &#233; a Simone. Estou ligando sobre o contrato."),
    ("Sorry, could you speak up? The connection is weak.", "Desculpe, pode falar mais alto? A conex&#227;o est&#225; ruim."),
    ("Could you clarify that point for me?", "Voc&#234; poderia esclarecer esse ponto para mim?"),
    ("Can I call you back in ten minutes?", "Posso retornar a liga&#231;&#227;o em dez minutos?"),
    ("Thanks for your time. Let's confirm the next step.", "Obrigada pelo seu tempo. Vamos confirmar o pr&#243;ximo passo."),
]

def survival():
    out = []
    for i, (en, pt) in enumerate(SURVIVAL, 1):
        out.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
            f'<button class="btn btn-listen" onclick="speakText(\'{esc_js(en)}\',this)">&#9835;</button></div>')
    return "\n".join(out)

HTML = f'''<div class="lesson-card" id="ex-lesson-4">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 04 -- Pre-class</div>
      <h3>Phone &amp; Video Calls -- Opening, Clarifying &amp; Closing</h3>
      <div class="lesson-desc">How to handle professional phone and video calls: open, clarify, and close. New vocabulary: voicemail, hold on, reach, available, connection, mute, speak up, call back, hang up, clarify. Functional phrases for the three phases of a call.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its translation.</p>
      <div class="match-grid" id="match-l4">
{match_rows()}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l4')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On Monday, Mark tried to <strong>reach</strong> Simone three times, but she was in court and not <strong>available</strong>, so he left a <strong>voicemail</strong>. When Simone heard it, she decided to <strong>call</strong> him <strong>back</strong> on a video call. At the start, the <strong>connection</strong> was weak, so Mark asked her to <strong>speak up</strong> and to <strong>clarify</strong> the indemnity clause. Simone opened the call clearly: "Hi Mark, this is Simone speaking. I'm calling about the agreement." She asked him to <strong>hold on</strong> while she opened the file, and she reminded a noisy colleague to <strong>mute</strong> his microphone. Before they could <strong>hang up</strong>, they confirmed the next step and agreed to talk again on Friday.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why did Mark leave a voicemail?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Simone was in court and not available.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The agreement was already signed.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He wanted to mute the call.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What did Mark ask Simone to do when the connection was weak?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Hang up immediately.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Speak up and clarify the clause.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Send the contract by mail.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. How does Simone open the call professionally?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Who is this?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Hi Mark, this is Simone speaking. I'm calling about the agreement."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "What do you want?"</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Phone Code</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Numa liga&#231;&#227;o profissional, siga tr&#234;s passos: abra, esclare&#231;a e encerre. / On a professional call, follow three steps: open, clarify, and close.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Phase / Fase</th><th style="padding:.7rem;text-align:left">When / Quando</th><th style="padding:.7rem;text-align:left">Example / Exemplo</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Opening / Abertura</td><td style="padding:.6rem">Identifique-se e diga o motivo / Identify yourself and your reason</td><td style="padding:.6rem"><strong>"Hi, this is Simone speaking. I'm calling about the agreement."</strong></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Clarifying / Esclarecer</td><td style="padding:.6rem">Confirme que entendeu; resolva a linha ruim / Check you understood; fix a bad line</td><td style="padding:.6rem"><strong>"Sorry, could you speak up? Could you clarify that?"</strong></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Closing / Encerrar</td><td style="padding:.6rem">Confirme o pr&#243;ximo passo antes de desligar / Confirm the next step before you hang up</td><td style="padding:.6rem"><strong>"Thanks for your time. I'll call you back."</strong></td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Key point / Ponto-chave</td><td style="padding:.6rem" colspan="2">Sempre se identifique primeiro, confirme que entendeu e encerre com o pr&#243;ximo passo antes de desligar.</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the full sentence.</p>
{fills()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the events in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l4]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l4">
{order_items()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l4')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each phrase, then record yourself saying it.</p>
{speech_cards()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best response for each professional situation.</p>
      <div class="quiz-item"><div class="quiz-question">The line is bad and you cannot hear the other person well. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Speak!"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Sorry, could you speak up? The connection is weak."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will hang up now."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You call a client but they do not answer. What is the professional thing to do?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Call ten more times in a row.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Leave a clear voicemail and ask them to call back.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Do nothing and wait.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You need to end the call, but you have not agreed on the next step. What do you do?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Hang up immediately.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Confirm the next step before you hang up.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Mute and leave the call.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think about an important phone or video call you have at work, perhaps with a counterpart on a contract. Record a short call: open it (say who you are and why you are calling), clarify one difficult point, and close it clearly with the next step. Use at least four new words from today.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-4"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 4</h4>
{survival()}
    </div>

  </div>
</div>
'''

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print("wrote preclass.html", len(HTML), "bytes")
