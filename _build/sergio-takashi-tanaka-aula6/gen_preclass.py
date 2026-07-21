# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 6 (Sergio) — data-driven p/ garantir matching correto/embaralhado."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (word, definition, example) — 10 palavras NOVAS (tema: ler um documento formal de risco; gramatica: passive voice)
VOCAB = [
    ("Audit", "an official examination of a company&#39;s accounts and controls", "\"The audit was completed by an external team.\""),
    ("Deficiency", "a weakness or fault found in a control", "\"Each deficiency was recorded in the report.\""),
    ("Remediation", "the action taken to correct a problem", "\"A remediation plan is required by the committee.\""),
    ("To submit", "to send a document formally for review", "\"The report was submitted to the regulator.\""),
    ("To disclose", "to make information official and known", "\"The breach must be disclosed at once.\""),
    ("Statement", "a formal written record of accounts or facts", "\"The monthly statement was submitted late.\""),
    ("Oversight", "official supervision by an authority", "\"The desk is placed under closer oversight.\""),
    ("Minutes", "the written record of what a meeting decided", "\"The minutes of the meeting were enclosed.\""),
    ("Clause", "a specific section or condition in a formal document", "\"The letter refers to clause four of the rules.\""),
    ("To require", "to make something necessary or mandatory", "\"A remediation plan is required before the next quarter.\""),
]

defs = [d for _, d, _ in VOCAB]


def shuffled(correct, i):
    """Rotaciona as definicoes de modo que a correta NUNCA fique na mesma posicao (REGRA 24)."""
    for shift in range(1, len(defs)):
        rot = defs[shift:] + defs[:shift]
        if rot.index(correct) != i:
            return rot
    raise AssertionError("nao consegui embaralhar")


out = []
out.append('<div class="lesson-card" id="ex-lesson-6">')
out.append('  <div class="lesson-header" onclick="toggleLesson(this)">')
out.append('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80\')"></div>')
out.append('    <div class="lesson-header-content">')
out.append('      <div class="lesson-number">Lesson 06 -- Pre-class</div>')
out.append('      <h3>The Audit Report -- Reading a Formal Risk Document</h3>')
out.append('      <div class="lesson-desc">Reading an internal audit report before it is submitted to the regulator. Key words: audit, deficiency, remediation, to submit, to disclose, statement, oversight, minutes, clause, to require. Structure: the passive voice (be + past participle) to read what was done, what was found, and what is required.</div>')
out.append('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>')
out.append('    </div>')
out.append('    <div class="expand-icon">&#9660;</div>')
out.append('  </div>')
out.append('  <div class="lesson-body">')
out.append('')

# Stage 1.1 Vocab cards
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>')
out.append('      <div class="vocab-cards">')
for w, d, ex in VOCAB:
    out.append(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div><div class="vocab-card-example">{ex}</div></div><button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>')
out.append('      </div>')
out.append('    </div>')
out.append('')

# Stage 1.2 Matching
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>')
out.append('      <div class="match-grid" id="match-l6">')
for i, (w, d, ex) in enumerate(VOCAB):
    opts = ['<option value="">Select...</option>']
    for o in shuffled(d, i):
        opts.append(f'<option value="{o}">{o}</option>')
    out.append(f'        <div class="match-row" data-answer="{d}"><span class="match-word" style="flex:0 0 150px">{w}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{"".join(opts)}</select></div>')
out.append('      </div>')
out.append('      <button class="verify-all-btn" onclick="verifyAllMatches(\'match-l6\')">Check Answers</button>')
out.append('    </div>')
out.append('')

# Stage 1.3 Grammar in Context
out.append('''    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The audit report follows a formal style. The controls <strong>were examined</strong> by the audit team, and two deficiencies <strong>were found</strong>. A limit <strong>was breached</strong> in March, and the breach <strong>was not disclosed</strong> to the committee on the same day. The monthly statement <strong>was submitted</strong> late twice. A remediation plan <strong>is required</strong>, and it <strong>must be approved</strong> by the committee. The report <strong>will be submitted</strong> to the regulator next week.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why do we say "the controls were examined" and not "the audit team examined the controls"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The passive voice puts the focus on the action and the object, not the doer.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The passive voice is only used for the future.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Were examined" means the same as "will examine".</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which sentence is a correct passive?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The report was submitted to the regulator."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The report submitted to the regulator."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The report was submit to the regulator."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What does the passive voice help you do when you read this report?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Follow what was done and what is required, even when the doer is not named.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Know exactly who is to blame in every sentence.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Understand only actions that will happen tomorrow.</div></div></div>
    </div>
''')

# Stage 1.4 Grammar Tip
out.append('''    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Passive Voice</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How formal reports describe what was done, found, and required &mdash; often without naming the doer.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present passive</td><td style="padding:.6rem">am / is / are + past participle</td><td style="padding:.6rem">A remediation plan <strong>is required</strong>.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Past passive</td><td style="padding:.6rem">was / were + past participle</td><td style="padding:.6rem">The report <strong>was submitted</strong> to the regulator.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">The doer (optional)</td><td style="padding:.6rem" colspan="2">Add <strong>by + person</strong> only when it matters: "The controls were examined <strong>by the audit team</strong>." Often the doer is left out.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Use</td><td style="padding:.6rem" colspan="2">Formal, impersonal writing &mdash; audit reports, regulator letters, committee minutes &mdash; where the action matters more than who did it.</td></tr>
        </tbody>
      </table></div>
    </div>
''')

# Stage 1.5 Fill in the blank
fills = [
    ("The controls", "were examined", "Hint: past passive of &quot;examine&quot;, plural subject", "The controls were examined by the audit team.", " by the audit team."),
    ("Two deficiencies", "were found", "Hint: past passive of &quot;find&quot;, plural subject", "Two deficiencies were found during the review.", " during the review."),
    ("A remediation plan", "is required", "Hint: present passive of &quot;require&quot;", "A remediation plan is required before the next quarter.", " before the next quarter."),
    ("The report", "was submitted", "Hint: past passive of &quot;submit&quot;", "The report was submitted to the regulator.", " to the regulator."),
    ("The plan must", "be approved", "Hint: after a modal, use be + past participle", "The plan must be approved by the committee.", " by the committee."),
    ("The breach was not", "disclosed", "Hint: past participle of &quot;disclose&quot;", "The breach was not disclosed on the same day.", " on the same day."),
]
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct passive form. Tap Listen to hear the whole sentence.</p>')
for pre, ans, hint, phrase, post in fills:
    out.append(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre} <input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{post}"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
out.append('    </div>')
out.append('')

# Stage 2 Order
order_items = [
    (1, "The desk&#39;s controls were examined by the internal audit team."),
    (2, "Two deficiencies were identified: a late statement and an undisclosed limit breach."),
    (3, "A remediation plan was prepared by the desk and approved by the committee."),
    (4, "The report was submitted to the regulator, and the minutes were enclosed."),
    (5, "The actions were completed on time, so no penalty was applied."),
]
display_order = [3, 5, 1, 4, 2]
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 2: Put the Report in Order</h4><span class="badge badge-order">Order</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of the audit process in the correct order.</p>')
out.append('      <div class="order-container" id="order-l6">')
d = dict(order_items)
for n in display_order:
    out.append(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')"><span class="order-num">?</span><span class="order-text">{d[n]}</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
out.append('      </div>')
out.append('      <button class="verify-all-btn" onclick="checkOrder(\'order-l6\')">Check Order</button>')
out.append('    </div>')
out.append('')

# Stage 3 Pronunciation
speech = [
    "The controls were examined and two deficiencies were found.",
    "A limit was breached, and it was not disclosed on the same day.",
    "The report was submitted to the regulator last week.",
    "A remediation plan is required and must be approved by the committee.",
    "The minutes of the meeting were enclosed with the report.",
]
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>')
for s in speech:
    out.append(f'      <div class="speech-card" data-phrase="{s}">')
    out.append(f'        <div class="speech-phrase">{s}</div>')
    out.append('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    out.append('        <div class="speech-result"></div>')
    out.append('      </div>')
out.append('    </div>')
out.append('')

# Stage 4 Situational Quiz
out.append('''    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation on the risk desk.</p>
      <div class="quiz-item"><div class="quiz-question">You report what the audit team did last week. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The controls examined last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The controls were examined last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The controls was examined last week."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You tell the committee what still needs to happen. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "A remediation plan must be approved before the next quarter."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "A remediation plan must approved before the next quarter."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "A remediation plan must be approve before the next quarter."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You explain how the report was sent. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The report was submit to the regulator."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The report was submitted to the regulator."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The report is submitted to the regulator yesterday."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe the two problems the audit found. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Two deficiencies were found, and the breach was not disclosed on time."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Two deficiencies were find, and the breach was not disclose on time."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Two deficiencies found, and the breach not disclosed on time."</div></div></div>
    </div>
''')

# Stage 5 Free Production
out.append('''    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think of a real control or process at XP. In the passive voice, describe how it is checked: what is reviewed, what was found last time, and what is required to fix it. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-6"></div>
      </div>
    </div>
''')

# Survival card
sc = [
    "The controls were examined and two deficiencies were found.",
    "A limit was breached, and it was not disclosed on the same day.",
    "A remediation plan is required and must be approved by the committee.",
    "The report was submitted to the regulator with the minutes enclosed.",
    "When a limit is breached, it must be disclosed at once.",
]
out.append('    <div class="survival-card">')
out.append('      <h4>Survival Card -- Lesson 6</h4>')
for i, s in enumerate(sc, 1):
    out.append(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{s}</span><button class="btn btn-listen" onclick="speakText(\'{s}\',this)">&#9835;</button></div>')
out.append('    </div>')
out.append('')
out.append('  </div>')
out.append('</div>')

open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('wrote preclass.html')
