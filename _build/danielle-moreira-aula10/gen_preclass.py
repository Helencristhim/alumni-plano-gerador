#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 10 da Danielle Moreira (B2, People & Culture / Maple Bear).

Tema: People Analytics -- Making the Numbers Talk (modelo de LEITURA, aula PAR / REGRA 29).
Gramatica NOVA: passiva de relato (reporting passives) + comparativos de dados.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = ZERO portugues na tela do aluno; 15 itens de vocab (10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..9
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 10 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(10)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT [NAO renderizada, B2], exemplo)
VOCAB = [
    ("Data storytelling", "turning a table of numbers into a claim a decision-maker can actually act on",
     "narrativa com dados",
     "Data storytelling is not decoration. It is the discipline of making a number say the one true thing it can, and no more."),
    ("Correlation", "two things moving together, which is not yet a reason for one another",
     "correla&#231;&#227;o",
     "Engagement rose while turnover fell, but that is a correlation. The mentorship program is not proven by it."),
    ("Causation", "one thing actually producing another, which a chart can hint at but never prove",
     "causa&#231;&#227;o / rela&#231;&#227;o de causa",
     "Causation is the claim a room of researchers will make you earn. A line on a slide is not enough to earn it."),
    ("Confounding variable", "a hidden third factor driving both numbers, and the first thing a researcher looks for",
     "vari&#225;vel de confus&#227;o",
     "The reorganization is the confounding variable here: it landed in the same quarter, and either event could be moving the numbers."),
    ("Statistical significance", "the test of whether a result is real or just the noise of a small sample",
     "signific&#226;ncia estat&#237;stica",
     "At this sample size I would not claim statistical significance. I would call it directional and ask for a second read."),
    ("Sample size", "how many people the number actually rests on, and the fastest way to overclaim",
     "tamanho da amostra",
     "Before you defend the finding, defend the sample size. Thirty responses cannot carry a company-wide claim."),
    ("Outlier", "the single extreme case that quietly drags an average somewhere it should not go",
     "valor extremo / at&#237;pico",
     "One team tripled its score. That team is an outlier, and it skews the mean more than it should."),
    ("Margin of error", "the honest band around a number that amateurs drop and researchers demand",
     "margem de erro",
     "Keep the margin of error on the slide. It makes the number look smaller and makes you look like you have done this before."),
    ("Leading indicator", "a signal that moves before the outcome does, so you can act while it still matters",
     "indicador antecedente",
     "Treat the onboarding window as a leading indicator, rather than waiting for turnover to confirm the problem a quarter too late."),
    ("Actionable insight", "a finding a manager can do something with on Monday, not just admire on a slide",
     "insight acion&#225;vel",
     "The actionable insight does not depend on the causal claim. It is the one thing a manager can act on this week."),
    ("To control for", "to hold a variable steady so it cannot secretly explain your result",
     "controlar (uma vari&#225;vel)",
     "Once we control for tenure, the gap narrows but does not close, and it is that residual gap I am reporting."),
    ("To skew", "to pull a distribution to one side, usually through an outlier or a bad sample",
     "distorcer / enviesar",
     "Drop the outlier and the effect shrinks but survives. Left in, it skews the whole story toward the flattering explanation."),
    ("To read too much into", "to draw a bigger conclusion than the data can honestly carry",
     "tirar conclus&#227;o exagerada de",
     "The fastest way to lose a research audience is to read too much into a chart that shows correlation and call it proof."),
    ("To tease out", "to separate a real signal from the noise around it",
     "isolar / extrair (um sinal)",
     "After all the honesty, I can still tease out the one signal that survives every rival explanation."),
    ("To connect the dots", "to turn separate findings into one coherent story",
     "ligar os pontos",
     "My job is to connect the dots into a single actionable insight, not to make each number say more than it can."),
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

# ---------- Stage 1.5 fill-in-the-blank (reporting passives) ----------
BLANKS = [
    ("It is", "estimated that",
     "Hint: impersonal report -- It + is + ESTIMATED THAT + a full clause with a finite verb (rose, not to rise)",
     "It is estimated that turnover among new managers rose by twelve percent last year.",
     "turnover among new managers rose by twelve percent last year."),
    ("Turnover is", "thought to be",
     "Hint: personal report -- subject + is + THOUGHT TO BE + linked. Never 'thought to being'",
     "Turnover is thought to be closely linked to how onboarding is run.",
     "closely linked to how onboarding is run."),
    ("Retention is", "reported to have",
     "Hint: the perfect report -- is + REPORTED TO HAVE + improved. The result reaches back into the past",
     "Retention is reported to have improved since the mentorship program began.",
     "improved since the mentorship program began."),
    ("New joiners are twice", "as likely as",
     "Hint: data comparative -- twice AS LIKELY AS tenured staff. The comparison needs both 'as'",
     "New joiners are twice as likely as tenured staff to leave in the first year.",
     "tenured staff to leave in the first year."),
    ("The drop is believed to", "reflect",
     "Hint: after 'believed to' comes the BASE verb -- reflect, never 'reflecting' and never 'to reflect'",
     "The drop is believed to reflect the reorganization, though it cannot be proven.",
     "the reorganization, though it cannot be proven."),
    ("I could not fully", "control for",
     "Hint: the honest caveat -- I could not CONTROL FOR the reorganization. The verb keeps its 'for'",
     "I could not fully control for the reorganization, so I am reporting the residual effect, not the raw one.",
     "the reorganization, so I am reporting the residual effect, not the raw one."),
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

# ---------- Stage 3 pronunciation ----------
SPEECH = [
    ("It is estimated that turnover among new managers rose by twelve percent last year.",
     ""),
    ("Engagement is thought to be linked to onboarding, but I would not yet call that causation.",
     ""),
    ("New joiners are twice as likely as tenured staff to leave in the first year.",
     ""),
    ("The reorganization is the confounding variable I could not control for, so I am flagging it myself.",
     ""),
    ("What survives every rival explanation is a leading indicator, and that is the one thing I am asking you to act on.",
     ""),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-10">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 10 -- Pre-class</div>
      <h3>People Analytics -- Making the Numbers Talk</h3>
      <div class="lesson-desc">Presenting an HR finding to the Academic Council without overclaiming: separate correlation from causation, name the confounding variable before Dr. Prescott does, keep the margin of error visible, and hand the room one actionable insight. Key words: data storytelling, correlation, causation, confounding variable, statistical significance, sample size, outlier, margin of error, leading indicator, actionable insight, to control for, to skew, to read too much into, to tease out, to connect the dots. Structure: reporting passives (It is estimated that turnover rose... / Turnover is thought to be linked to... / Retention is reported to have improved...) + data comparatives (twice as likely as / a threefold increase / significantly higher than).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="10" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="10">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the language of the People Analytics brief you present to the Canadian Academic Council &mdash; the difference between a chart and a decision.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l10">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The most dangerous sentence in any analytics deck is the confident one. Two lines move together on the screen &mdash; engagement climbs, turnover falls &mdash; and the temptation is to stand up and announce that the mentorship program did it. In front of a room of researchers, that is the sentence that ends the presentation. Two numbers moving together is a <strong>correlation</strong>, and a correlation is not yet a cause. <strong>It is estimated that</strong> turnover among new managers fell nine points last quarter, and it is tempting to <strong>read too much into</strong> that &mdash; but the honest analyst asks what else changed in the same window.</p>
        <p style="margin-top:.8rem">Almost always, the answer is a <strong>confounding variable</strong>. Here, the reorganization landed in exactly the quarter the mentorship launched, and it <strong>is thought to have</strong> shifted the workload of half the teams. Either event could be moving the numbers, and no chart can separate them. So you name the variable you could not <strong>control for</strong> out loud, before anyone else does. <strong>Turnover is believed to be</strong> linked to onboarding, you say &mdash; not caused by it. The distinction is the whole of your credibility.</p>
        <p style="margin-top:.8rem">Then comes the discipline. One team tripled its score after a change of manager; that team is an <strong>outlier</strong>, and it will <strong>skew</strong> the average until you set it aside. You check the <strong>sample size</strong>, and you keep the <strong>margin of error</strong> on the slide even though it makes the number look smaller. <strong>Statistical significance is reported to</strong> matter less to executives than it should &mdash; which is precisely why keeping it marks you as someone who has done this before.</p>
        <p style="margin-top:.8rem">And still there is something true to say. You <strong>tease out</strong> the one signal that survives every rival explanation, and you call it what it is: a <strong>leading indicator</strong>, a thing that moves before the outcome does, not a proof. New joiners, for instance, <strong>are twice as likely as</strong> tenured staff to leave in the first year, and that gap holds even after you control for the reorganization. You <strong>connect the dots</strong> into a single <strong>actionable insight</strong> &mdash; watch the onboarding window monthly, rather than waiting for turnover to confirm the problem a quarter too late. The number never speaks for itself. Your job is to make it say the one true thing it can.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why do we say &ldquo;It <strong>is estimated that</strong> turnover fell nine points&rdquo; and not &ldquo;It <strong>is estimated</strong> turnover to fall nine points&rdquo;?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because the impersonal report takes <strong>that + a full clause</strong> with a finite verb (fell), not an infinitive. &ldquo;It is estimated&rdquo; is followed by a whole sentence, not by &ldquo;to fall&rdquo;.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because &ldquo;estimate&rdquo; cannot be used in the passive voice in English.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the number is plural, which forces the infinitive.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. &ldquo;Turnover <strong>is thought to be</strong> linked to onboarding.&rdquo; &mdash; why is this stronger, in that room, than &ldquo;Onboarding <strong>causes</strong> turnover&rdquo;?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the passive is always more polite than the active, regardless of meaning.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the reporting passive states a finding without claiming causation as fact &mdash; it attributes the link to the evidence, which is exactly what a research audience demands.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;causes&rdquo; is grammatically incorrect after the word onboarding.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why keep the <em>margin of error</em> on the slide when it makes the number look smaller?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because researchers cannot read a chart without one printed on it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because keeping it marks you as someone who has done this before, rather than someone overclaiming a fragile number.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the margin of error is what proves causation once and for all.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What does the writer say is left to present, once you have refused to overclaim?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Nothing &mdash; an honest analyst has no conclusion to offer.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The raw correlation, presented louder and with more confidence.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> The one signal that survives every rival explanation &mdash; a leading indicator you connect into a single actionable insight a manager can act on.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reporting Passives &amp; Data Comparatives</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The grammar of the analyst who states a finding without owning it as fact: you attribute the claim to the evidence, which is exactly the register a room of researchers trusts.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Impersonal report<br><strong>It is</strong> + reported/estimated/thought + <strong>that</strong> + clause</td><td style="padding:.6rem">State a finding as the field's, not yours. Note: <strong>that</strong> + a full clause with a finite verb.</td><td style="padding:.6rem"><strong>It is estimated that</strong> turnover rose by twelve percent.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Personal report<br>subject + <strong>is thought/believed to</strong> + base verb</td><td style="padding:.6rem">Raise the subject to the front. After <strong>to</strong> comes the base verb: be, reflect, drive.</td><td style="padding:.6rem"><strong>Turnover is thought to be</strong> linked to onboarding.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Perfect report<br>is + <strong>reported to have</strong> + past participle</td><td style="padding:.6rem">The result reaches back into the past &mdash; it already happened.</td><td style="padding:.6rem"><strong>Retention is reported to have</strong> improved since March.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Why it sounds senior</td><td style="padding:.6rem" colspan="2">&ldquo;Onboarding <strong>causes</strong> turnover&rdquo; claims causation as fact &mdash; and a researcher will destroy it. &ldquo;Turnover <strong>is thought to be linked to</strong> onboarding&rdquo; states the same finding while conceding it is a reading of evidence, not a proof. That concession IS your credibility.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Data comparatives</td><td style="padding:.6rem">Compare two groups precisely, without overclaiming size.</td><td style="padding:.6rem">New joiners are <strong>twice as likely as</strong> tenured staff to leave &middot; a <strong>threefold increase</strong> &middot; <strong>significantly higher than</strong> the benchmark</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Collocation</td><td style="padding:.6rem" colspan="2"><strong>control for</strong> a variable &middot; <strong>tease out</strong> a signal &middot; <strong>read too much into</strong> a chart &middot; an outlier <strong>skews</strong> the average &middot; <strong>connect the dots</strong> into an insight</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the number one slip):</strong> the impersonal report needs <strong>that + a finite clause</strong>. &ldquo;It is estimated <em>turnover to rise</em>&rdquo; is a word-for-word import; the English is &ldquo;It is estimated <strong>that turnover rose</strong>&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (the other slip):</strong> after &ldquo;<strong>is thought to</strong>&rdquo; comes the <strong>base verb</strong>, not the <em>-ing</em> form. &ldquo;is thought <em>to reflecting</em>&rdquo; &rarr; &ldquo;is thought <strong>to reflect</strong>&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>The line that wins the room:</strong> a reporting passive plus the honest caveat, in one sentence. &ldquo;<strong>The drop is believed to be linked to</strong> the reorganization, which I could not fully <strong>control for</strong> &mdash; so I am reporting it as a leading indicator, not a cause.&rdquo;</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Finding in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order you will present the finding to the Academic Council &mdash; honesty first, conclusion last.</p>
      <div class="order-container" id="order-l10">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Set the outlier aside and check the sample size, then keep the margin of error on the slide.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Hand the room one actionable insight a manager can act on this Monday, without depending on the causal claim.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Show the correlation plainly &mdash; two lines moving together &mdash; and refuse to call it a cause yet.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Tease out the one signal that survives, and name it a leading indicator rather than a proof.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Name the confounding variable yourself &mdash; the reorganization you could not control for &mdash; before anyone raises it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l10')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences you will actually say in front of the council.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment in front of the Academic Council.</p>
      <div class="quiz-item"><div class="quiz-question">Dr. Prescott says: &ldquo;Your two lines move together, so the mentorship program raised engagement. Yes?&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Yes. The data clearly proves the program caused the improvement.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;It is a correlation I cannot yet attribute &mdash; the reorganization landed in the same quarter. What I can defend is a leading indicator, not a cause.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I am not sure. Maybe it did, maybe it did not.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">One team tripled its score after a new manager arrived. How do you present it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;That team is an outlier and it skews the average on this sample size. Set it aside and the effect shrinks but survives &mdash; that is the version I would act on.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;It is our strongest result, so I built the whole recommendation around it.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I removed it quietly so nobody would ask about the sample size.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the reporting passive correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;It is estimated turnover to rise by twelve percent this year.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Turnover is thought to reflecting the reorganization.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;It is estimated that turnover rose by twelve percent, and it is thought to be linked to onboarding.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Prescott asks: &ldquo;Did you control for tenure? New joiners always score differently.&rdquo; You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Tenure does not matter for engagement, so I left it out.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;You are right, and I should have said so first. Once we control for tenure the gap narrows but does not close, and it is that residual gap I am reporting.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I did not, but a third of the sample is new, so it probably balances out.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The council asks: &ldquo;So what do we actually do with this on Monday?&rdquo; The strongest close is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Wait for next quarter's turnover figures to confirm everything first.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;One thing: treat the onboarding window as a leading indicator and watch it monthly, rather than waiting for turnover to confirm the problem a quarter too late. That does not depend on the causal claim.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Approve the full culture strategy today, on the strength of these two lines.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">You are presenting one people-analytics finding to the Canadian Academic Council. In two minutes: state the correlation you found, name the confounding variable you could not control for, admit the sample size and margin of error, then tease out the one signal that survives and turn it into an actionable insight. Use at least two reporting passives (it is estimated that... / is thought to be...), one data comparative (twice as likely as / a threefold increase), and six words from this lesson. End with the single thing a manager should do on Monday.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-10"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 10</h4>
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

# ---------- REGRA 13: ZERO portugues na tela (B2). Nenhum campo PT e renderizado. ----------
assert 'speech-translation' not in HTML, 'B2 nao leva traducao'
assert 'sp-pt' not in HTML, 'B2 nao leva sp-pt'

# ---------- REGRA 22: nenhuma palavra das aulas 1-9 pode voltar como vocab card ----------
JA_ENSINADO = {
    # aula 1
    'organizational culture', 'employee journey', 'people strategy', 'framework',
    'stakeholder', 'alignment', 'to roll out', 'headquarters', 'franchisor',
    'bilingual education', 'hybrid model', 'senior leadership', 'to make headway',
    'to take a stance', 'to carry out',
    # aula 2
    'cultural diagnosis', 'core values', 'psychological safety', 'onboarding experience',
    'culture fit', 'belonging', 'disengagement', 'attrition', 'turnover rate',
    'toxic culture', 'exit interview', 'pulse survey', 'to foster a culture of',
    'to look into', 'the elephant in the room',
    # aula 3
    'okr', 'key performance indicator', 'cascading goals', 'deliverable', 'milestone',
    'accountability', 'cross-functional', 'bandwidth', 'buy-in', 'to put forward',
    'to push back', 'to move the needle', 'to cut to the chase', 'to bring about',
    'to circle back to',
    # aula 4
    'talent retention', 'engagement survey', 'performance cycle', 'succession planning',
    'employer brand', 'people analytics', 'workforce planning', 'change management',
    'psychological contract', 'diversity and inclusion', 'influence without authority',
    'employee value proposition', 'to make a compelling case', 'to phase out',
    'a double-edged sword',
    # aula 5
    'cultural intelligence', 'high-context culture', 'low-context culture', 'power distance',
    'individualism and collectivism', 'indirect communication', 'assertiveness',
    'cultural humility', 'work-life integration', 'inclusive leadership',
    'to bridge cultural gaps', 'to read between the lines', 'to account for', 'to set out',
    'to take into consideration',
    # aula 6
    'cultural assessment', 'diagnostic tool', 'baseline', 'response rate', 'focus group',
    'trust index', 'root cause', 'gap analysis', 'findings', 'benchmark',
    'to run a diagnostic', 'to gather insights', 'to surface an issue', 'to come up with',
    'to open a can of worms',
    # aula 7
    'constructive feedback', 'conflict resolution', 'blind spot', 'defensiveness',
    'resistance to change', 'non-violent communication', 'growth mindset',
    'behavioral pattern', 'performance gap', 'corrective action', 'to take ownership of',
    'to address head-on', 'to follow through on', 'to sugarcoat', 'to beat around the bush',
    # aula 8
    'takeaway', 'caveat', 'rationale', 'trade-off', 'traction', 'quick win', 'roadblock',
    'track record', 'preliminary', 'tangible', 'to take stock of', 'to fall short of',
    'to build on', 'to iron out', 'the jury is still out',
    # aula 9
    'counterpoint', 'reservation', 'premise', 'assumption', 'merit', 'anecdotal', 'rigor',
    'peer-reviewed', 'common ground', 'to concede', 'to take issue with',
    "to play devil's advocate", 'to stand your ground', 'to defer to', 'to hold water',
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-9'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
