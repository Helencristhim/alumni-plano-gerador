#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 2 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 12 termos + 3 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova na aula 1 (nenhuma do bloco ex-lesson-1)
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 2 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(2)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Cultural diagnosis", "a structured reading of what a culture really is, based on evidence",
     "diagn&#243;stico cultural",
     "Before I propose anything, I would like to run a cultural diagnosis."),
    ("Core values", "the few principles a company will not trade away, even under pressure",
     "valores essenciais",
     "Core values are not what is on the wall. They are what survives a hard decision."),
    ("Psychological safety", "the belief that you can speak up or disagree without being punished",
     "seguran&#231;a psicol&#243;gica",
     "Psychological safety is built in the meeting where someone disagrees with you."),
    ("Onboarding experience", "the first weeks of a new hire, and how those weeks actually feel",
     "experi&#234;ncia de integra&#231;&#227;o",
     "The onboarding experience was excellent for one week, and abandoned by the second."),
    ("Culture fit", "how well a person's way of working matches the way the team already works",
     "ader&#234;ncia cultural",
     "We hire for culture fit, and then we punish the first person who thinks differently."),
    ("Belonging", "the feeling that you can be yourself at work and still be part of the team",
     "pertencimento",
     "Belonging is high here. Safety is not. Those are two different problems."),
    ("Disengagement", "when people still do the job but stop caring about the outcome",
     "desengajamento",
     "Disengagement is quiet. It is the last thing you see and the first thing that happens."),
    ("Attrition", "the slow loss of people over time, one by one",
     "perda gradual de talentos",
     "Attrition never arrives as a crisis. It arrives as a resignation, and then another one."),
    ("Turnover rate", "the percentage of people who leave the company in a year",
     "taxa de rotatividade",
     "Our turnover rate climbed from nine percent to twenty six percent in three years."),
    ("Toxic culture", "a culture where fear, blame or disrespect have become normal",
     "cultura t&#243;xica",
     "It is not a toxic culture. It is a specific problem that nobody names."),
    ("Exit interview", "the conversation with someone who is leaving, where the truth comes out",
     "entrevista de desligamento",
     "They filed the exit interviews. Nobody ever read them."),
    ("Pulse survey", "a short, frequent survey that measures how people feel right now",
     "pesquisa de pulso",
     "If they had run a pulse survey that year, they would have seen it coming."),
    ("To foster a culture of", "to create the conditions for a behavior to grow",
     "cultivar uma cultura de",
     "You foster a culture of speaking up by protecting the first person who does it."),
    ("To look into", "to investigate something properly before you judge it",
     "investigar, apurar",
     "Before we judge the team, we should look into what happened in that meeting."),
    ("The elephant in the room", "the obvious problem everyone can see and nobody names",
     "o elefante na sala",
     "Let me name the elephant in the room: nobody here disagrees with a director."),
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
        f'<span class="vocab-card-def">{d}</span></div>'
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
        f'<span class="match-word" style="flex:0 0 170px">{w}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
        f'<option value="">Select...</option>{o}</select></div>'
    )
match_rows = '\n'.join(rows)

# ---------- Stage 1.5 fill-in-the-blank ----------
BLANKS = [
    ("If leadership", "had run", "Hint: the IF half &mdash; had + past participle (never would)",
     "If leadership had run a pulse survey, they would have seen it coming.",
     "a pulse survey, they would have seen it coming."),
    ("If someone had read the exit interviews, they", "would have found",
     "Hint: the result half &mdash; would have + past participle",
     "If someone had read the exit interviews, they would have found the problem.",
     "the problem."),
    ("We", "should have addressed", "Hint: a criticism of what was not done &mdash; should have + past participle",
     "We should have addressed the disengagement in the first quarter.",
     "the disengagement in the first quarter."),
    ("The coordinators", "might not have resigned",
     "Hint: careful speculation &mdash; might not have + past participle",
     "The coordinators might not have resigned if psychological safety had been higher.",
     "if psychological safety had been higher."),
    ("They", "could have fostered", "Hint: an option that was there &mdash; could have + past participle",
     "They could have fostered a culture of speaking up.",
     "a culture of speaking up."),
    ("If the onboarding experience", "had continued",
     "Hint: the IF half, in the past &mdash; had + past participle",
     "If the onboarding experience had continued after week one, she would have stayed.",
     "after week one, she would have stayed."),
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
    ("Before I propose anything, I would like to run a cultural diagnosis.",
     "Antes de propor qualquer coisa, eu gostaria de conduzir um diagn&#243;stico cultural."),
    ("It would appear that the issue is psychological safety, not belonging.",
     "Tudo indica que a quest&#227;o &#233; seguran&#231;a psicol&#243;gica, n&#227;o pertencimento."),
    ("If someone had looked into the exit interviews, we would have known a year ago.",
     "Se algu&#233;m tivesse investigado as entrevistas de desligamento, a gente saberia disso h&#225; um ano."),
    ("To some extent, the team might have felt that disagreeing carried a cost.",
     "At&#233; certo ponto, o time pode ter sentido que discordar tinha um custo."),
    ("Let me name the elephant in the room, and you can tell me if I am wrong.",
     "Deixe-me nomear o elefante na sala, e voc&#234;s me dizem se eu estiver errada."),
]
sp = []
for phrase, pt in SPEECH:
    SPEAKABLE.append(phrase)
    sp.append(
        f'      <div class="speech-card" data-phrase="{phrase}">\n'
        f'        <div class="speech-phrase">{phrase}</div>\n'
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
        f'<span class="sp-en">{en}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
    )
survival = '\n'.join(sv)

HTML = f'''<div class="lesson-card" id="ex-lesson-2">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 02 -- Pre-class</div>
      <h3>The Language of Culture -- Diagnosing and Describing Culture</h3>
      <div class="lesson-desc">Diagnosing and describing organizational culture in English: read the numbers, name the problem and say the hard truth without losing the room. Key words: cultural diagnosis, core values, psychological safety, onboarding experience, culture fit, belonging, disengagement, attrition, turnover rate, toxic culture, exit interview, pulse survey, to foster a culture of, to look into, the elephant in the room. Structures: third conditional (if + had + past participle / would have + past participle) and modal perfects (should have / could have / might have), plus executive hedging (It would appear that... / To some extent...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the vocabulary a cultural diagnosis is written in &mdash; what separates an opinion about culture from a professional reading of it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l2">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Northline Academy was a network of bilingual schools with an excellent reputation and a serious problem. In three years, its <strong>turnover rate</strong> climbed from nine percent to twenty six percent. The company had written a beautiful set of <strong>core values</strong>, printed them and hung them in every corridor &mdash; and it had never once run a <strong>cultural diagnosis</strong> to find out whether anyone lived by them. The <strong>onboarding experience</strong> was excellent for one week and abandoned by the second. Managers stopped disagreeing with directors in meetings. The people who stayed delivered the curriculum and quietly stopped bringing new ideas: that is <strong>disengagement</strong>, and it is far more expensive than the <strong>attrition</strong> it produces. When the board finally asked what had gone wrong, the answer was uncomfortable. <strong>If</strong> leadership <strong>had run</strong> a <strong>pulse survey</strong> in that first year, they <strong>would have seen</strong> <strong>psychological safety</strong> collapsing. <strong>If</strong> someone <strong>had looked into</strong> the <strong>exit interviews</strong> instead of filing them, they <strong>would have found</strong> <strong>the elephant in the room</strong> by the second one. They <strong>should have addressed</strong> it during onboarding, and they <strong>could have fostered a culture of</strong> speaking up at almost no cost. The two coordinators who resigned <strong>might not have left</strong> if the culture <strong>had felt</strong> safe. The culture did not fail because it was a <strong>toxic culture</strong>. It failed because nobody was willing to name what everybody could already see.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does "If leadership had run a pulse survey, they would have seen it" use <em>had run</em> and not <em>would have run</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because the <em>if</em> half always takes <strong>had + past participle</strong> &mdash; <em>would</em> belongs only in the result half.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the survey was run, only too late.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the action can still happen in the future.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "The two coordinators might not have left" &mdash; why <em>might</em> and not <em>would</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because it is a direct criticism of leadership.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because it speculates carefully: it was likely, but nobody can state it as a certainty.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the fact happened and is confirmed.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, what came FIRST at Northline Academy?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The attrition &mdash; people resigned, and only then did they stop caring.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The disengagement &mdash; people stopped bringing ideas long before anyone resigned.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The toxic culture &mdash; the text says fear and blame were normal from day one.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Third Conditional + Modal Perfects</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The grammar of the diagnosis: every cultural diagnosis talks about a past that did NOT happen &mdash; "if they had done X, Y would not have happened".</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Condition (if)<br>if + had + past participle</td><td style="padding:.6rem">The past that did NOT happen.</td><td style="padding:.6rem"><strong>If</strong> they <strong>had run</strong> a pulse survey...</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Result<br>would have + past participle</td><td style="padding:.6rem">The consequence that, for that reason, did not happen either.</td><td style="padding:.6rem">...they <strong>would have seen</strong> it coming.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">should have + past participle</td><td style="padding:.6rem">Criticism: it was an obligation and it was not done. Judges.</td><td style="padding:.6rem">We <strong>should have addressed</strong> it earlier.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">could have + past participle</td><td style="padding:.6rem">An option that was there and was not taken. Softer.</td><td style="padding:.6rem">They <strong>could have fostered</strong> a culture of speaking up.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">might have + past participle</td><td style="padding:.6rem">Careful speculation, with no accusation. Speculates.</td><td style="padding:.6rem">The team <strong>might have felt</strong> unsafe.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">had <strong>not</strong> + past participle / would <strong>not</strong> have + past participle</td><td style="padding:.6rem">If they <strong>hadn't</strong> ignored it, she <strong>wouldn't have</strong> resigned.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">What + would + subject + have + past participle + if...?</td><td style="padding:.6rem"><strong>What would you have done</strong> if you had known?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Executive hedging</td><td style="padding:.6rem" colspan="2"><strong>It would appear that...</strong> &middot; <strong>To some extent...</strong> &mdash; the same truth, said in a way the room is willing to hear.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the classic slip):</strong> <em>would</em> <strong>NEVER</strong> goes in the <em>if</em> half. "If we <em>would have</em> known" is wrong &mdash; the correct form is "If we <strong>had</strong> known, we <strong>would have</strong> acted". In speech, everything contracts: <em>If we'd known, we'd have acted</em>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>In writing:</strong> it is always <strong>should have</strong>, never "should of" &mdash; even though, at native speed, the two sound exactly the same.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Collocation:</strong> in English we do not say "do a diagnosis" &mdash; we <strong>run</strong> / <strong>carry out</strong> / <strong>conduct</strong> a cultural diagnosis. And it is <strong>discuss the results</strong>, never "discuss <em>about</em> the results".</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Diagnosis in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a cultural diagnosis in the order you will run it in Canada.</p>
      <div class="order-container" id="order-l2">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">Name the elephant in the room, with the number that proves it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">Look into the evidence first: the pulse survey and the exit interviews.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">Ask the team what it would take to foster a culture of speaking up.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">Read the two numbers that contradict each other: belonging and psychological safety.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">Say what the company would have known if someone had read those interviews.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l2')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l2')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of your first cultural diagnosis in Canada.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your first diagnosis session with the academic team.</p>
      <div class="quiz-item"><div class="quiz-question">The pulse survey shows belonging at 78% and psychological safety at 41%. Nathan asks what it means. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Your culture is toxic. People are afraid of each other."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It would appear that the issue is safety, not belonging: people are proud to be here, and they still do not feel safe enough to disagree."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The numbers are fine. Forty one percent is normal in academia."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Nine exit interviews were filed and never read. Which sentence is grammatically correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If someone would have read them, we would have known."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "If someone had read them, we would have known."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "If someone had read them, we would know it a year ago."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to criticize a decision the directors made, without turning them into the accused. The most senior form is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You should have seen this coming. It was obvious."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "To some extent, the team might have felt that disagreeing carried a cost &mdash; that is a system problem, not a people problem."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Nobody here has the courage to say what they think."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say you will investigate the numbers properly before judging anyone. The natural collocation is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Before I take a stance, I want to look into the exit interviews."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Before I take a stance, I want to look the exit interviews."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Before I take a stance, I want to do a research in the exit interviews."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A director says: "Nobody ever complained to me, so the survey must be wrong." You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Then the survey is wrong. Let's move on."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "That is exactly the problem with this leadership team."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "To some extent, that is the finding: people might not have felt they could bring it to you. Could you tell me what happens here when someone disagrees with a director?"</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">Think of a real cultural challenge you saw or led at Maple Bear Brazil. Walk me through it: what happened, what you did, and &mdash; with what you know now &mdash; what you would have done differently if you had known then what you know today. Use at least two third conditionals, one modal perfect (should have / could have / might have), and five words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-2"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 2</h4>
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

# ---------- REGRA 22: nenhuma palavra da aula 1 pode voltar como vocab card ----------
AULA1 = {'organizational culture', 'employee journey', 'people strategy', 'framework',
         'stakeholder', 'alignment', 'to roll out', 'headquarters', 'franchisor',
         'bilingual education', 'hybrid model', 'senior leadership', 'to make headway',
         'to take a stance', 'to carry out'}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in AULA1}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada na aula 1'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
