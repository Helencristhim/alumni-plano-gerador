#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
random.seed(1313)

N = 13
GRAD = "background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80')"
TITLE = "Plans and Intentions -- 'Going to' for Future Projects"
DESC = ("Talking about plans, intentions, and predictions with going to (am/is/are + going to + verb) "
        "in HR projects, including negatives and questions. New words: rollout, initiative, pipeline, "
        "objective, allocate, draft, intend, expansion, timeline, proposal, anticipate, upcoming.")

# word, def_en, pt, example
VOCAB = [
    ("Rollout", "the launch of a new plan or system", "lan&ccedil;amento", "The rollout is going to be gradual."),
    ("Initiative", "a new plan or effort to solve a problem", "iniciativa", "We are going to start a hiring initiative."),
    ("Pipeline", "planned upcoming work or projects", "fila de projetos / pipeline", "We anticipate a busy pipeline next year."),
    ("Objective", "a specific goal you plan to reach", "objetivo", "Our main objective is to reduce turnover."),
    ("Allocate", "to give resources to a plan or task", "alocar / destinar", "We are going to allocate more budget."),
    ("Draft", "a first version of a document", "rascunho / minuta", "I am going to draft the proposal this week."),
    ("Intend", "to plan to do something", "pretender / tencionar", "We intend to improve the onboarding process."),
    ("Expansion", "the growth of a business or team", "expans&atilde;o", "Next month we are going to start a big expansion."),
    ("Timeline", "the schedule of a plan over time", "cronograma", "We are going to review the timeline with the directors."),
    ("Proposal", "a plan you suggest for approval", "proposta", "I am going to prepare the proposal on Monday."),
    ("Anticipate", "to expect something to happen", "prever / antecipar", "We anticipate a busy quarter ahead."),
    ("Upcoming", "happening soon in the future", "pr&oacute;ximo / que est&aacute; por vir", "I want to explain our upcoming plans."),
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

# Stage 1.2 Matching (shuffled options != row order)
out.append('')
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Combine cada palavra com a defini&ccedil;&atilde;o correta. (Match each word with the correct definition.)</p>')
out.append(f'      <div class="match-grid" id="match-l{N}">')
for w, d, pt, ex in VOCAB:
    opts = defs[:]
    while True:
        random.shuffle(opts)
        # ensure the correct answer is NOT in the same index as the word's row position (extra safety) - just ensure shuffled
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
        <p>I want to explain our <strong>upcoming</strong> plans for the next quarter. We <strong>are going to</strong> launch a new hiring <strong>initiative</strong> in March, and we <strong>are going to allocate</strong> more budget to the training team. First, I <strong>am going to draft</strong> the <strong>proposal</strong> this week. Then we <strong>are going to review</strong> the <strong>timeline</strong> with the directors. Our main <strong>objective</strong> is to reduce turnover, so we <strong>intend</strong> to improve onboarding. We <strong>anticipate</strong> a busy <strong>pipeline</strong>, and the <strong>rollout</strong> <strong>is going to</strong> be gradual. I <strong>am not going to</strong> rush the <strong>expansion</strong>.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. When the text says "we are going to launch a new initiative in March", what does it express?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A finished action in the past.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A plan or intention decided for the future (going to + verb).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A daily routine.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What is the main objective of the plan?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> To reduce turnover.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> To cancel the training team.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> To rush the expansion.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence is the correct negative of "going to"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am going not to rush the expansion."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am not going to rush the expansion."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I not am going to rush the expansion."</div></div></div>
    </div>''')

# Stage 1.4 Grammar Tip
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Going To (Future)</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use <strong>going to</strong> para <strong>planos e inten&ccedil;&otilde;es</strong> j&aacute; decididos e para <strong>previs&otilde;es com evid&ecirc;ncia</strong>. Estrutura: <strong>am/is/are + going to + verbo base</strong>. Afirmativo: "We <strong>are going to</strong> launch the initiative." Negativo: "I <strong>am not going to</strong> rush it." Pergunta: "<strong>Are</strong> you <strong>going to</strong> draft the proposal?" (Voc&ecirc; vai / pretende...)</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Affirmative</td><td style="padding:.6rem">am/is/are + going to + verb</td><td style="padding:.6rem">"We <strong>are going to</strong> allocate more budget."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">am/is/are + not + going to</td><td style="padding:.6rem">"I <strong>am not going to</strong> rush the expansion."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">Am/Is/Are + subject + going to</td><td style="padding:.6rem">"<strong>Are</strong> you <strong>going to</strong> draft the proposal?"</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Prediction (evidence)</td><td style="padding:.6rem">going to for what you can see coming</td><td style="padding:.6rem">"The rollout <strong>is going to</strong> be gradual."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.8rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">Aten&ccedil;&atilde;o: use <strong>going to</strong> para planos j&aacute; decididos. O verbo depois de "going to" fica sempre na forma base (sem -s, sem -ing): "She <strong>is going to</strong> lead", n&atilde;o "is going to leads".</p>
    </div>''')

# Stage 1.5 Fill in the blank
out.append('''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta de "going to". A pista entre par&ecirc;nteses ajuda. (Complete each sentence. Tap Listen to hear it.)</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="are going to" data-hint="Hint: we + are going to" data-phrase="We are going to launch a new hiring initiative." placeholder="___"> launch a new hiring initiative. (plan, we)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="am going to" data-hint="Hint: I + am going to" data-phrase="I am going to draft the proposal this week." placeholder="___"> draft the proposal this week. (plan, I)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"She <input class="blank-input" data-answer="is going to" data-hint="Hint: she + is going to" data-phrase="She is going to lead the expansion project." placeholder="___"> lead the expansion project. (plan, she)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="am not going to" data-hint="Hint: negative = am not going to" data-phrase="I am not going to rush the rollout." placeholder="___"> rush the rollout. (negative, I)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"<input class="blank-input" data-answer="Are" data-hint="Hint: question with you = Are ... going to" data-phrase="Are you going to review the timeline today?" placeholder="___"> you going to review the timeline today? (question)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"They <input class="blank-input" data-answer="are going to" data-hint="Hint: they + are going to" data-phrase="They are going to allocate two managers to the project." placeholder="___"> allocate two managers to the project. (plan, they)"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>''')

# Stage 2 Ordering
out.append(f'''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Plan in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os passos de apresentar um plano na ordem correta. (Put the steps in the correct order.)</p>
      <div class="order-container" id="order-l{N}">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Give the timeline: then we are going to review it with the directors.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Reassure: I am not going to rush the rollout.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Introduce the plan: we are going to launch a new initiative in March.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">State the objective: our objective is to reduce turnover.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l{N}')"><span class="order-num">?</span><span class="order-text">Say the first step: first, I am going to draft the proposal.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l{N}')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l{N}')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{N}')">Check Order</button>
    </div>''')

# Stage 3 Pronunciation
SPEECH = [
    ("We are going to launch a new hiring initiative.", "Vamos lan&ccedil;ar uma nova iniciativa de contrata&ccedil;&atilde;o."),
    ("First, I am going to draft the proposal.", "Primeiro, vou preparar o rascunho da proposta."),
    ("Our objective is to reduce turnover.", "Nosso objetivo &eacute; reduzir a rotatividade."),
    ("I am not going to rush the rollout.", "N&atilde;o vou apressar o lan&ccedil;amento."),
    ("Are you going to review the timeline?", "Voc&ecirc; vai revisar o cronograma?"),
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
      <div class="quiz-item"><div class="quiz-question">You announce a decided plan for next quarter. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "We going to launch the initiative."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "We are going to launch the initiative."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We are going to launched the initiative."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You say what you do NOT plan to do. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I am not going to rush the rollout."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am going not to rush the rollout."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I not going to rush the rollout."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You ask a colleague about their intention. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You are going to draft the proposal?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Are you going to draft the proposal?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Do you going to draft the proposal?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You make a prediction based on evidence (a busy pipeline). You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Next year is going to be busy."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Next year is going to busy."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Next year going to be busy."</div></div></div>
    </div>''')

# Stage 5 Free Production
out.append(f'''
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&ecirc; mesma respondendo a pergunta abaixo. N&atilde;o existe resposta certa ou errada. (Record yourself. There is no right or wrong answer.)</p>
      <div class="think-card">
        <div class="think-question">Present your plans for an upcoming HR project: what you and your team are going to do, your main objective, the first step you are going to take, and one thing you are not going to do. Use "going to" and at least four new words. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{N}"></div>
      </div>
    </div>''')

# Survival card
SURV = [
    ("We are going to launch a new hiring initiative.", "Vamos lan&ccedil;ar uma nova iniciativa de contrata&ccedil;&atilde;o."),
    ("First, I am going to draft the proposal.", "Primeiro, vou preparar o rascunho da proposta."),
    ("Our objective is to reduce turnover.", "Nosso objetivo &eacute; reduzir a rotatividade."),
    ("I am not going to rush the rollout.", "N&atilde;o vou apressar o lan&ccedil;amento."),
    ("Are you going to review the timeline?", "Voc&ecirc; vai revisar o cronograma?"),
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

open('_build/murielle-xavier-aula13/preclass.html', 'w').write('\n'.join(out) + '\n')
print('wrote preclass.html')
# sanity: no entity apostrophe collisions in speakText
import re
txt = '\n'.join(out)
bad = re.findall(r"speakText\('[^']*&#39;", txt)
print('speakText with &#39; in key:', len(bad))
