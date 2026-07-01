#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
random.seed(1414)

N = 14
GRAD = "background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&q=80')"
TITLE = "Decisions and Offers -- 'Will' for Spontaneous Choices"
DESC = ("Making decisions, offers, and promises at the moment of speaking with will (will + base verb), "
        "plus predictions and the difference from going to. New words: volunteer, reassure, commit, "
        "guarantee, ensure, promptly, arrange, confirm, notify, remind, reliable, cope.")

# word, def_en, pt, example
VOCAB = [
    ("Volunteer", "to offer to do something without being asked", "voluntariar-se / se oferecer", "I will volunteer to lead the panel."),
    ("Reassure", "to make someone feel less worried", "tranquilizar", "I will reassure the team about the audit."),
    ("Commit", "to promise to do something", "comprometer-se", "I will commit to the new deadline."),
    ("Guarantee", "to promise something will happen", "garantir", "I guarantee the team will cope well."),
    ("Ensure", "to make sure something happens", "assegurar / garantir", "I will ensure everything runs smoothly."),
    ("Promptly", "quickly, without delay", "prontamente", "I will notify you promptly."),
    ("Arrange", "to organize or plan something", "organizar / arranjar", "I will arrange the documents today."),
    ("Confirm", "to say something is definitely true", "confirmar", "I will confirm the schedule this afternoon."),
    ("Notify", "to officially tell someone", "notificar / avisar", "I will notify the candidates right away."),
    ("Remind", "to help someone remember", "lembrar / relembrar", "I will remind everyone about the meeting."),
    ("Reliable", "that you can trust to do well", "confi&aacute;vel", "She is reliable and always delivers."),
    ("Cope", "to deal with a difficult situation", "lidar / dar conta", "The team will cope well with the pressure."),
]

defs = [v[1] for v in VOCAB]

def esc(s):
    return s.replace("'", "&#39;")

out = []
out.append(f'<div class="lesson-card" id="ex-lesson-{N}">')
out.append('  <div class="lesson-header" onclick="toggleLesson(this)">')
out.append(f'    <div class="lesson-header-img" style="{GRAD}"></div>')
out.append('    <div class="lesson-header-content">')
out.append(f'      <div class="lesson-number">Lesson {N} -- Pre-class</div>')
out.append(f'      <h3>{TITLE}</h3>')
out.append(f'      <div class="lesson-desc">{DESC}</div>')
out.append(f'      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{N}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{N}">0%</span></div>')
out.append('    </div>')
out.append('    <div class="expand-icon">&#9660;</div>')
out.append('  </div>')
out.append('  <div class="lesson-body">')

# Stage 1.1 Vocab cards
out.append('')
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&ccedil;a cada palavra e leia o exemplo. A tradu&ccedil;&atilde;o em portugu&ecirc;s est&aacute; entre par&ecirc;nteses. (Listen and read the example.)</p>')
out.append('      <div class="vocab-cards">')
for w, d, pt, ex in VOCAB:
    out.append(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{esc(d)} ({pt})</span></div><div class="vocab-card-example">"{esc(ex)}"</div></div><button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>')
out.append('      </div>')
out.append('    </div>')

# Stage 1.2 Matching (shuffled)
out.append('')
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Combine cada palavra com a defini&ccedil;&atilde;o correta. (Match each word with the correct definition.)</p>')
out.append(f'      <div class="match-grid" id="match-l{N}">')
for w, d, pt, ex in VOCAB:
    opts = defs[:]
    while True:
        random.shuffle(opts)
        if opts != defs:
            break
    o_html = '<option value="">Select...</option>' + ''.join(f'<option value="{esc(o)}">{esc(o)}</option>' for o in opts)
    out.append(f'        <div class="match-row" data-answer="{esc(d)}"><span class="match-word" style="flex:0 0 130px">{w}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{o_html}</select></div>')
out.append('      </div>')
out.append('    </div>')

# Stage 1.3 Grammar in Context
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda as perguntas. (Read the text and answer the questions.)</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Sofia is sick and cannot run the interviews tomorrow. Do not worry &mdash; I <strong>will handle</strong> it. I <strong>will step</strong> in and lead the panel myself. I <strong>will confirm</strong> the room this afternoon, and I <strong>will notify</strong> the candidates <strong>promptly</strong>. I <strong>reassure</strong> you: I <strong>will not cancel</strong> anything. I <strong>guarantee</strong> the team <strong>will cope</strong> well, because we are <strong>reliable</strong>. I <strong>will ensure</strong> everything runs smoothly, and I <strong>will send</strong> you a short update tonight.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. When the writer says "I will handle it", what does "will" express here?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A plan decided a long time ago.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A decision or offer made at the moment of speaking.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A past action.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which sentence is a promise?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I will not cancel anything."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Sofia is sick."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We are reliable."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What form of the verb comes after "will"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The -ing form: "I will handling."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The base form: "I will handle."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The -s form: "She will handles."</div></div></div>
    </div>''')

# Stage 1.4 Grammar Tip
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Will (Decisions &amp; Offers)</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use <strong>will</strong> para <strong>decis&otilde;es, ofertas e promessas feitas na hora</strong> de falar, e para <strong>previs&otilde;es de opini&atilde;o</strong> (I think...). Estrutura: <strong>will + verbo base</strong> (igual para todas as pessoas). Negativo: <strong>will not (won&#39;t)</strong>. Pergunta: "<strong>Will</strong> you help me?" Compare: <strong>going to</strong> = plano j&aacute; decidido antes; <strong>will</strong> = decis&atilde;o no momento.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Spontaneous decision</td><td style="padding:.6rem">will + base verb</td><td style="padding:.6rem">"I <strong>will handle</strong> it."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Offer / promise</td><td style="padding:.6rem">will + base verb</td><td style="padding:.6rem">"I <strong>will send</strong> you an update."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">will not / won&#39;t + base verb</td><td style="padding:.6rem">"I <strong>will not</strong> cancel anything."</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Prediction (opinion)</td><td style="padding:.6rem">I think + will</td><td style="padding:.6rem">"I think the auditors <strong>will be</strong> satisfied."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.8rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">Aten&ccedil;&atilde;o: depois de "will" o verbo fica sempre na forma base, sem -s e sem -ing: "She <strong>will lead</strong>", n&atilde;o "will leads" nem "will leading".</p>
    </div>''')

# Stage 1.5 Fill in the blank
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta de "will". A pista entre par&ecirc;nteses ajuda. (Complete each sentence. Tap Listen to hear it.)</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Do not worry, I <input class="blank-input" data-answer="will handle" data-hint="Hint: decision = will + base verb" data-phrase="Do not worry, I will handle it now." placeholder="___"> it now. (decision)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="will notify" data-hint="Hint: will + notify" data-phrase="I will notify the candidates right away." placeholder="___"> the candidates right away. (offer)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I promise I <input class="blank-input" data-answer="will not cancel" data-hint="Hint: negative = will not + base verb" data-phrase="I promise I will not cancel anything." placeholder="___"> anything. (promise, negative)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"<input class="blank-input" data-answer="Will" data-hint="Hint: question starts with Will" data-phrase="Will you help me with the audit?" placeholder="___"> you help me with the audit? (question)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="will arrange" data-hint="Hint: will + arrange" data-phrase="I will arrange the documents today." placeholder="___"> the documents today. (offer)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I think the auditors <input class="blank-input" data-answer="will be" data-hint="Hint: prediction = will + be" data-phrase="I think the auditors will be satisfied." placeholder="___"> satisfied. (prediction)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>''')

# Stage 2 Ordering
out.append(f'''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Offer in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os passos de oferecer ajuda numa emerg&ecirc;ncia na ordem correta. (Put the steps in the correct order.)</p>
      <div class="order-container" id="order-l{N}">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Give the next step: I will confirm the room this afternoon.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Promise: I will not cancel anything.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Reassure: do not worry, I will handle it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Notify people: I will notify the candidates promptly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Offer to step in: I will lead the panel myself.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{N}')">Check Order</button>
    </div>''')

# Stage 3 Pronunciation
SPEECH = [
    ("Do not worry, I will handle it.", "N&atilde;o se preocupe, eu cuido disso."),
    ("I will notify the candidates right away.", "Vou avisar os candidatos imediatamente."),
    ("I promise I will not cancel anything.", "Prometo que n&atilde;o vou cancelar nada."),
    ("Will you help me with the audit?", "Voc&ecirc; me ajuda com a auditoria?"),
    ("I guarantee the team will cope well.", "Garanto que a equipe vai dar conta bem."),
]
out.append('')
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&ccedil;a cada frase e depois grave voc&ecirc; mesma. (Listen, then record yourself.)</p>')
for en, pt in SPEECH:
    out.append(f'      <div class="speech-card" data-phrase="{esc(en)}">')
    out.append(f'        <div class="speech-phrase">{en}</div>')
    out.append(f'        <div class="speech-translation">{pt}</div>')
    out.append('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    out.append('        <div class="speech-result"></div>')
    out.append('      </div>')
out.append('    </div>')

# Stage 4 Situational Quiz
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada situa&ccedil;&atilde;o. (Choose the best answer for each situation.)</p>
      <div class="quiz-item"><div class="quiz-question">A colleague just told you Sofia is sick. You decide to help now. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am going to handle it." (you decided long ago)</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Do not worry, I will handle it."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I handle it yesterday."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to make a promise. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I promise I will not cancel anything."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I promise I not will cancel anything."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I promise I will cancelling anything."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You ask a colleague for help. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You will help me with the audit?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Will you help me with the audit?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Do you will help me with the audit?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You give your opinion about a future result. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I think the auditors will be satisfied."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I think the auditors will satisfied."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I think the auditors will be satisfy."</div></div></div>
    </div>''')

# Stage 5 Free Production
out.append(f'''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&ecirc; mesma respondendo a pergunta abaixo. N&atilde;o existe resposta certa ou errada. (Record yourself. There is no right or wrong answer.)</p>
      <div class="think-card">
        <div class="think-question">Imagine a colleague at work has a sudden problem (a sick teammate, a tight audit, a missing report). Offer your help on the spot: what you will do, what you promise you will not do, and one question you will ask. Use "will" and at least four new words. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{N}"></div>
      </div>
    </div>''')

# Survival card
SURV = [
    ("Do not worry, I will handle it.", "N&atilde;o se preocupe, eu cuido disso."),
    ("I will notify the candidates right away.", "Vou avisar os candidatos imediatamente."),
    ("I promise I will not cancel anything.", "Prometo que n&atilde;o vou cancelar nada."),
    ("Will you help me with the audit?", "Voc&ecirc; me ajuda com a auditoria?"),
    ("I guarantee the team will cope well.", "Garanto que a equipe vai dar conta bem."),
]
out.append('')
out.append('    <div class="survival-card">')
out.append(f'      <h4>Survival Card -- Lesson {N}</h4>')
for i, (en, pt) in enumerate(SURV, 1):
    out.append(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span><span class="sp-pt">{pt}</span><button class="btn btn-listen" onclick="speakText(\'{esc(en)}\',this)">&#9835;</button></div>')
out.append('    </div>')

out.append('')
out.append('  </div>')
out.append('</div>')

open('_build/murielle-xavier-aula14/preclass.html', 'w').write('\n'.join(out) + '\n')
print('wrote preclass.html')
import re
txt = '\n'.join(out)
print('speakText with &#39; in key:', len(re.findall(r"speakText\('[^']*&#39;", txt)))
