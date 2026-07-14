#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 3 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 12 termos + 3 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1 e 2
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 3 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(3)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("OKR", "one goal you can say out loud, plus the numbers that prove you reached it",
     "objetivos e resultados-chave",
     "Our first OKR for Canada is one objective and three numbers. Nothing else."),
    ("Key performance indicator", "a number you watch all year to see whether the business is healthy",
     "indicador-chave de desempenho",
     "Engagement is the key performance indicator I will be judged on in Canada."),
    ("Cascading goals", "goals that flow down: the company sets one, and every team writes its own version",
     "desdobramento de metas",
     "Without cascading goals, nine academic teams will write nine different strategies."),
    ("Deliverable", "the concrete thing you promised to hand over, on a date",
     "entreg&#225;vel",
     "The onboarding journey is not an idea. It is a deliverable, and it has a date."),
    ("Milestone", "a checkpoint with a date on the way to the goal",
     "marco, etapa-chave",
     "Give me one milestone, one owner and one date. That is the whole meeting."),
    ("Accountability", "owning the result in public, whether it worked or not",
     "responsabiliza&#231;&#227;o pelo resultado",
     "A team that agrees with everything I say is not accountability. It is silence with good manners."),
    ("Cross-functional", "involving people from different teams who do not report to each other",
     "interfuncional, entre &#225;reas",
     "The group is cross-functional, which is exactly why nobody owns the date."),
    ("Bandwidth", "the time and attention a person or a team actually has left",
     "capacidade dispon&#237;vel",
     "They do not lack commitment. They lack bandwidth, and those are different problems."),
    ("Buy-in", "the moment people stop obeying a plan and start wanting it",
     "ades&#227;o genu&#237;na",
     "Their buy-in is not a nice-to-have. It is the deliverable."),
    ("To put forward", "to formally offer an idea so that a group can decide on it",
     "propor formalmente",
     "What I would like to put forward is one owner and one date."),
    ("To push back", "to disagree with a plan, professionally, and say so out loud",
     "discordar e se posicionar",
     "Please push back if you think the target is wrong. I would rather hear it now."),
    ("To move the needle", "to produce a change big enough to show up in the numbers",
     "mover o ponteiro, gerar impacto real",
     "Tell me which single milestone would actually move the needle this quarter."),
    ("To cut to the chase", "to give the point first and the story afterwards",
     "ir direto ao ponto",
     "Let me cut to the chase: two of the four objectives are off track."),
    ("To bring about", "to cause a change, not merely to want one",
     "provocar, causar (uma mudan&#231;a)",
     "This is the one change that would bring about real accountability."),
    ("To circle back to", "to return, on purpose, to a point you left open",
     "retomar (um ponto)",
     "Before we close, I would like to circle back to the onboarding deliverable."),
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
    ("If we had shipped the deliverable in the first quarter, we", "would be measuring",
     "Hint: the result is NOW &mdash; would + verb (never would have been)",
     "If we had shipped the deliverable in the first quarter, we would be measuring engagement right now.",
     "engagement right now."),
    ("If the goals", "had cascaded",
     "Hint: the IF half, in the past &mdash; had + past participle",
     "If the goals had cascaded last year, every academic team would have its own OKR today.",
     "last year, every academic team would have its own OKR today."),
    ("If I", "were not",
     "Hint: a PRESENT condition, formal register &mdash; were (never was, never would be)",
     "If I were not leading two countries, I would have delivered the diagnostic in July.",
     "leading two countries, I would have delivered the diagnostic in July."),
    ("If the group had more bandwidth, they", "would have hit",
     "Hint: the result stayed in the PAST &mdash; would have + past participle",
     "If the group had more bandwidth, they would have hit the milestone in June.",
     "the milestone in June."),
    ("If someone", "had owned",
     "Hint: the cause is in the past, the cost is today &mdash; had + past participle",
     "If someone had owned that deliverable, we would not be having this conversation today.",
     "that deliverable, we would not be having this conversation today."),
    ("What I would like to", "put forward",
     "Hint: to formally offer an idea so a group can decide on it &mdash; a phrasal verb from this lesson",
     "What I would like to put forward is one owner, one milestone and one date.",
     "is one owner, one milestone and one date."),
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
    ("Let me cut to the chase: two of the four objectives are off track.",
     "Vou direto ao ponto: dois dos quatro objetivos est&#227;o fora do prazo."),
    ("If we had shipped that deliverable in Q1, we would be measuring engagement right now.",
     "Se tiv&#233;ssemos entregado aquele entreg&#225;vel no primeiro trimestre, estar&#237;amos medindo engajamento agora."),
    ("What I would like to put forward is one owner, one milestone and one date.",
     "O que eu gostaria de propor &#233; um respons&#225;vel, um marco e uma data."),
    ("Building on that, my take on this is different, and here is the number behind it.",
     "Partindo disso, a minha leitura &#233; outra, e aqui est&#225; o n&#250;mero que a sustenta."),
    ("Please push back if you think the target is wrong. I would rather hear it now.",
     "Por favor, discorde se voc&#234; achar que a meta est&#225; errada. Prefiro ouvir isso agora."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-3">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 03 -- Pre-class</div>
      <h3>Speaking Like a Senior -- Executive Communication in 1:1s, OKRs and Strategic Alignment</h3>
      <div class="lesson-desc">Run a 1:1, read an OKR dashboard and lead a strategic alignment meeting in English: open with the number, put a proposal forward, disagree with a senior leader and close with one owner and one date. Key words: OKR, key performance indicator, cascading goals, deliverable, milestone, accountability, cross-functional, bandwidth, buy-in, to put forward, to push back, to move the needle, to cut to the chase, to bring about, to circle back to. Structure: mixed conditionals (a past cause with a cost today / a present condition with a past result) + executive discourse markers (Building on that... / My take on this is... / What I would like to propose is...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the vocabulary your Canadian peers already use every day &mdash; what separates the person who reports the meeting from the person who runs it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l3">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>It is the last week of the quarter at Maple Bear Canada, and the <strong>OKR</strong> dashboard is not kind. Two of the four objectives are off track. The onboarding <strong>deliverable</strong> slipped by six weeks; the <strong>cross-functional</strong> group that was supposed to own it has met exactly twice; and the engagement <strong>key performance indicator</strong> is still marked as not measured, because there is nothing live to measure. <strong>If</strong> someone <strong>had owned</strong> that deliverable in the first quarter, the team <strong>would not be having</strong> this conversation today. <strong>If</strong> the goals <strong>had cascaded</strong> across the nine academic teams last year, every one of them <strong>would have</strong> its own version of the objective right now, instead of nine different interpretations of it.</p>
        <p style="margin-top:.8rem">The directors blame <strong>bandwidth</strong>. Claire, the VP, does not. Her reading is colder and more useful: nobody owns the date, so nobody carries the <strong>accountability</strong> for it, and a <strong>milestone</strong> without an owner is a wish with a calendar. What she wants on Monday is not a status report. She wants the one milestone that would actually <strong>move the needle</strong>, and a proposal to reach it. And she wants Danielle to <strong>push back</strong> on her if the target itself is wrong &mdash; because half the leadership team agrees with everything she says, and that is not accountability. That is silence with good manners. <strong>If</strong> Claire <strong>were not</strong> the kind of leader who asks to be contradicted, she <strong>would have lost</strong> this team a long time ago.</p>
        <p style="margin-top:.8rem">So Danielle opens with the number, not the story. She <strong>cuts to the chase</strong>: two of four, six weeks late, no owner. Then she <strong>puts forward</strong> one owner, one milestone and one date &mdash; September fifteenth. The academic directors will resist, and she wants them to resist in the room rather than after it, because their <strong>buy-in</strong> is not a nice-to-have: it is the deliverable itself. That single change, she argues, is what would <strong>bring about</strong> real accountability. Before she closes, she <strong>circles back to</strong> the engagement number, and names the week it will finally be measured.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does "If someone had owned that deliverable, we would not be having this conversation today" use <em>would not be having</em> and not <em>would not have had</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because the cause is in the past, but the result is <strong>now</strong> &mdash; and a present result takes <strong>would + verb</strong>, never <em>would have</em>.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because both halves of the sentence are in the past.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the conversation can still happen in the future.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "If Claire were not the kind of leader who asks to be contradicted, she would have lost this team a long time ago." Which direction is this?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A past cause with a present result.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A <strong>present</strong> condition (this is how she is, permanently) with a <strong>past</strong> result &mdash; hence <em>were</em> + <em>would have lost</em>.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A real condition about the future.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, what is the real reason the onboarding deliverable is late?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The cross-functional group does not have the bandwidth to do the work.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Nobody owns the date, so nobody carries the accountability for it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The engagement KPI was measured too late in the quarter.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Mixed Conditionals</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The grammar of executive communication: the two halves of the sentence sit in <strong>different tenses</strong>, because the decision belongs to one time and the cost belongs to another.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Direction 1 &mdash; condition<br>if + had + past participle</td><td style="padding:.6rem">The decision that was NOT taken, back in the past. The past cause.</td><td style="padding:.6rem"><strong>If</strong> we <strong>had shipped</strong> it in Q1...</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Direction 1 &mdash; result<br>would + base verb</td><td style="padding:.6rem">The cost you feel <strong>today</strong>. The present result.</td><td style="padding:.6rem">...we <strong>would be measuring</strong> engagement right now.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Direction 2 &mdash; condition<br>if + past simple / <strong>were</strong></td><td style="padding:.6rem">A permanent limit of the present. The present cause.</td><td style="padding:.6rem"><strong>If</strong> I <strong>were not</strong> leading two countries...</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Direction 2 &mdash; result<br>would have + past participle</td><td style="padding:.6rem">The consequence that is already closed, in the past. The past result.</td><td style="padding:.6rem">...I <strong>would have delivered</strong> the diagnostic in July.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative</td><td style="padding:.6rem">had <strong>not</strong> + past participle / would <strong>not</strong> be + -ing</td><td style="padding:.6rem">If nobody <strong>had owned</strong> it, we <strong>wouldn't be</strong> here today.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question</td><td style="padding:.6rem">Where + would + subject + be + -ing + if...?</td><td style="padding:.6rem"><strong>Where would we be</strong> today if we had shipped it in Q1?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Discourse markers</td><td style="padding:.6rem" colspan="2"><strong>Building on that...</strong> (add to what was just said) &middot; <strong>My take on this is...</strong> (give your own reading) &middot; <strong>What I would like to propose is...</strong> (open a proposal) &middot; <strong>To circle back to...</strong> (return to an open point)</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the mixed-conditional slip):</strong> if the result is happening <strong>now</strong>, the result half is <strong>would be</strong> &mdash; never "would have been". "If we had launched in Q1, we <em>would have been</em> hitting our KPI now" is wrong; the correct form is "we <strong>would be</strong> hitting our KPI now".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (the classic slip):</strong> <em>would</em> <strong>NEVER</strong> goes into the <em>if</em> half. "If I <em>would be</em> less busy" is wrong &mdash; the correct form is "If I <strong>were</strong> less busy". And in formal register it is always <strong>if I were</strong>, never "if I was".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Collocation:</strong> in English it is <strong>align on</strong> priorities (never "align in"), <strong>reach</strong> a milestone (never "make a milestone"), and <strong>explain</strong> something <strong>to</strong> someone (never "explain me the OKR").</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the 1:1 in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves of an executive 1:1 in the order you will run them in Canada.</p>
      <div class="order-container" id="order-l3">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l3')"><span class="order-num">?</span><span class="order-text">Put forward one owner, one milestone and one date.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l3')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l3')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l3')"><span class="order-num">?</span><span class="order-text">Cut to the chase: open with the number, not with the story.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l3')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l3')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l3')"><span class="order-num">?</span><span class="order-text">Circle back to the engagement KPI and close with the date it will be measured.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l3')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l3')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l3')"><span class="order-num">?</span><span class="order-text">Say what the delay is costing you today: if it had shipped in Q1, you would be measuring engagement now.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l3')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l3')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l3')"><span class="order-num">?</span><span class="order-text">Invite them to push back on the date, in the room, before anyone leaves it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l3')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l3')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l3')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of your first 1:1 with each Canadian leader.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your first 1:1 and of the strategic alignment meeting.</p>
      <div class="quiz-item"><div class="quiz-question">Nathan opens the 1:1 with: "Quick sync. Where are we on the onboarding milestone?" You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Well, it is a long story. In March the group was formed, and then we had some issues with the schedule, and after that..."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Let me cut to the chase: it slipped six weeks, nobody owns the date, and I have a proposal."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Sorry, we are a bit late with that one. I will send you an update by email."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say that a decision from Q1 is still costing the company today. Which sentence is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "If we had shipped it in Q1, we would have been measuring engagement now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "If we had shipped it in Q1, we would be measuring engagement right now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "If we would have shipped it in Q1, we would be measuring engagement right now."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Claire, the VP, says September is unrealistic and asks for December. You disagree. The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You are wrong. December makes no sense at all."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Okay, December is fine. I will adjust the plan."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Building on that, my take on this is different: if we moved it to December, we would lose the buy-in we already have &mdash; and here is the number behind that."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The cross-functional group says it has no bandwidth. What is the diagnosis a senior leader gives?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Then bandwidth is not the problem. Nobody owns the date, so nobody is accountable for it."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Then we should remove the milestone from the OKR."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Then the group is not committed enough to this project."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You are closing the alignment meeting and want to return to a point you deliberately left open. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Before we close, I want to explain you the engagement KPI one more time."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Before we close, I would like to circle back to the engagement KPI and name the week it gets measured."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Before we close, let's align in the priorities of the engagement KPI."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">You are opening the strategic alignment meeting with the Canadian leadership on August 1st. Three items: where the culture initiative stands, the onboarding milestone, and your proposal for the diagnostic with the academic team. Open with the number, put forward one owner and one date, and say what the delay is costing you today. Use at least two mixed conditionals and five words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-3"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 3</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-2 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-2'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
