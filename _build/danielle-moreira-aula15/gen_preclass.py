#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 15 (FINAL) da Danielle Moreira — B2, People & Culture.

Esta e a ULTIMA aula do pacote (15/15): uma REVISAO em forma de SIMULACAO FINAL.
Por isso, POR DESIGN, ela NAO introduz conteudo novo:

  - REGRA 22 (vocab): o Pre-class REATIVA vocabulario JA ensinado (aulas 1..14) — nao
    ensina palavra nova. Como sao vocab-card-word que ja apareceram como novos em aulas
    anteriores, cada um esta na WHITELIST _build/model/vocab_allow_repeat.json
    ("danielle-moreira"). check_vocab_progression NAO tem isencao por titulo (so o
    check_grammar_progression tem), entao a whitelist e o caminho sancionado.
  - REGRA 22 (gramatica): NENHUMA estrutura nova. O config NAO define grammar_point,
    entao o standalone nao emite data-grammar. E o titulo da AULA contem "Final Review",
    o que isenta check_grammar_progression e coloca check_preclass_coherence em status
    REVIEW (coerencia de vocab dispensada — remix e legitimo numa revisao).
  - REGRA 4: as 5 etapas (1.1..1.5 + 2..5) CONTINUAM presentes — review nao pula etapa.
  - REGRA 29: o Pre-class previewa a aula 15 IN CLASS (a simulacao): o toolkit executivo
    e as frases-molde que a Danielle usa na reuniao de quinta com a lideranca canadense.
  - GATE botao morto (REGRA 7.1): todo texto falavel viaja em ATRIBUTO (data-speak /
    data-phrase), nunca dentro do argumento string de um onclick.
  - REGRA 13: B2 = ZERO portugues na tela do aluno.
"""
import re
import random

random.seed(15)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT (ref interna, NAO vai pra tela), exemplo)
# TODAS ja ensinadas em aulas anteriores — reativacao proposital (whitelist). Curadoria:
# os 12 termos do toolkit executivo que a simulacao final integra.
VOCAB = [
    ("Mandate", "the authority and remit you were given to act on",
     "mandato / incumb&#234;ncia",
     "Let me frame my mandate: I was brought in to lead the cultural transformation of the Canadian division."),
    ("Stakeholder", "anyone with a stake in your work whose support you need",
     "parte interessada",
     "Every stakeholder in that room has read the Brazil numbers; my job is to turn interest into buy-in."),
    ("Buy-in", "genuine agreement and commitment to a plan, not just permission",
     "ades&#227;o / apoio real",
     "My predecessor rolled out the framework before he had the buy-in, so it never gained momentum."),
    ("Framework", "a structured set of principles you use to organize and act on a problem",
     "modelo / estrutura conceitual",
     "I am not importing a Brazilian framework; I am importing a diagnostic method and letting your context write the answers."),
    ("Credibility", "the trust and standing you build before you spend it on change",
     "credibilidade",
     "I earn credibility by listening first, and only then do I move the needle."),
    ("Psychological safety", "the felt safety to speak up, disagree and admit a mistake without fear",
     "seguran&#231;a psicol&#243;gica",
     "Success is the day a Canadian leader disagrees with me directly, because the psychological safety is real."),
    ("Developmental feedback", "input aimed at someone's growth, not a verdict on their past",
     "feedback de desenvolvimento",
     "I give developmental feedback that grows a person instead of shrinking them."),
    ("Actionable insight", "a conclusion from data that you can actually act on",
     "insight acion&#225;vel",
     "I tell a story with the data and tease out the actionable insight without reading too much into it."),
    ("Groundwork", "the early, unglamorous preparation that makes later change possible",
     "trabalho de base / alicerce",
     "I would rather build on the groundwork my predecessor laid than start over."),
    ("To move the needle", "to make real, measurable progress on something that matters",
     "fazer diferen&#231;a de verdade",
     "The fastest way to move the needle is to hear the real objection now, not after we launch."),
    ("To read the room", "to sense the unspoken mood of a group before you act",
     "sentir o clima do ambiente",
     "I read 'ambitious' as a polite objection, so I read the room and asked one follow-up."),
    ("To empower", "to give someone the authority and confidence to act on their own",
     "empoderar / dar autonomia",
     "I am not there to rescue the team; I am there to empower them to solve the next problem without me."),
]

DEFS = [d for _, d, _, _ in VOCAB]

# ---------- guarda-corpo: nada falavel pode entrar em argumento de onclick ----------
SPEAKABLE = []


def speak_btn(text, cls='audio-btn', label='Listen'):
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
        f'<span class="match-word" style="flex:0 0 180px">{w}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
        f'<option value="">Select...</option>{o}</select></div>'
    )
match_rows = '\n'.join(rows)

# ---------- Stage 1.5 fill-in-the-blank (structures across the program) ----------
# (pre, resposta, hint, frase completa (audio), post) -- espacamento EXPLICITO em pre/post
BLANKS = [
    ("By the end of my first year, I ", "will have run",
     "Hint: FUTURE PERFECT for what you will have delivered by a point in time. will have + past participle",
     "By the end of my first year, I will have run a full cultural diagnostic.",
     " a full cultural diagnostic."),
    ("He ", "had rolled out",
     "Hint: PAST PERFECT for the earlier action in a backstory. had + past participle",
     "He had rolled out the framework before he had the buy-in.",
     " the framework before he had the buy-in."),
    ("I ", "would rather",
     "Hint: ADVANCED MODAL to state a preference. would rather + base verb (no 'to')",
     "I would rather build on the groundwork than start over.",
     " build on the groundwork than start over."),
    ("If I ", "had prescribed",
     "Hint: THIRD CONDITIONAL, the if-clause. had + past participle (NOT 'would have')",
     "If I had prescribed a Brazilian answer on day one, I would have lost the room.",
     " a Brazilian answer on day one, I would have lost the room."),
    ("", "What",
     "Hint: CLEFT sentence for emphasis. Begin with 'What...' to spotlight the key idea",
     "What I am changing is the sequence, not the destination.",
     " I am changing is the sequence, not the destination."),
    ("I ", "wish",
     "Hint: WISH + past simple to voice adaptation, not complaint. I ___ the objections came sooner",
     "I wish the objections came sooner, so I read the room instead.",
     " the objections came sooner, so I read the room instead."),
]
fills = []
for pre, ans, hint, phrase, post in BLANKS:
    SPEAKABLE.append(phrase)
    fills.append(
        f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre}'
        f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
        f'data-phrase="{phrase}" placeholder="___">{post}"</div>'
        f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
        f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
    )
fill_items = '\n'.join(fills)

# ---------- Stage 3 pronunciation (= as 5 frases do Survival Card) ----------
SPEECH = [
    "Let me frame my mandate: I was brought in to lead the cultural transformation of this division, and by year one I will have run a full diagnostic.",
    "What I am changing is the sequence, not the destination. I would rather build on the groundwork than start over.",
    "I take the point about cultural distance, and where we may differ is on transfer. The method is neutral, even if the findings will not be.",
    "I'm reading ambitious as a gentle way of saying you're not yet convinced. Tell me if I have that wrong, because I'd rather hear the real objection now.",
    "Let me think on that out loud. I don't have a complete answer yet, and here is how I would find one.",
]
sp = []
for phrase in SPEECH:
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
for i, en in enumerate(SPEECH, 1):
    sv.append(
        f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
        f'<span class="sp-en">{en}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
    )
survival = '\n'.join(sv)

HTML = f'''<div class="lesson-card" id="ex-lesson-15">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1552581234-26160f608093?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 15 -- Pre-class</div>
      <h3>Full Simulation -- Danielle Leads the Room (Final Review)</h3>
      <div class="lesson-desc">The final review, and the debut it prepares you for: your first high-stakes meeting with the Canadian Maple Bear leadership. This is a preview of the simulation -- no new content, everything reactivated. Reload the executive toolkit (mandate, stakeholder, buy-in, framework, credibility, psychological safety, developmental feedback, actionable insight, groundwork, to move the needle, to read the room, to empower) and the whole grammar map -- future perfect, past perfect, advanced modals, wish / if only, third conditional and cleft sentences -- in the exact sentences you will say when you open the meeting, present your People &amp; Culture plan, and answer the two questions you did not prepare for. A celebration and a test: this is where you sound like the same senior leader in English that you already are in Portuguese.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="15" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="15">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Your executive toolkit, reactivated. You have met every one of these before -- listen, read the example, and recall where each one lands in the meeting.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l15">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions. This is a review -- watch every structure you built doing its one job in the room.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>It is nine o'clock on a Thursday in Toronto, and for the first time the room Danielle is opening is not in Portuguese. The VP has handed her the meeting, and she begins where a leader begins: with the <strong>mandate</strong>. &ldquo;I was brought in to lead the cultural transformation of the Canadian division,&rdquo; she says, and then, without apologising for the size of it, &ldquo;by the end of my first year I <strong>will have run</strong> a full diagnostic and rolled out a new onboarding experience.&rdquo; The <strong>future perfect</strong> is doing exactly one job there: projecting quiet confidence about what will already be true. Fifteen weeks ago, that sentence would have come out as a hope. Tonight it comes out as a plan.</p>
        <p style="margin-top:.8rem">A regional director asks the fair, sharp question: how is this different from what her predecessor tried and dropped? She does not trash him. &ldquo;He <strong>had rolled out</strong> the <strong>framework</strong> before he had the <strong>buy-in</strong>,&rdquo; she explains &mdash; the <strong>past perfect</strong> sequencing the backstory cleanly &mdash; &ldquo;so it never gained momentum.&rdquo; Then the cleft, placing the emphasis exactly where she wants it: &ldquo;<strong>What</strong> I am changing <strong>is</strong> the sequence, not the destination.&rdquo; And the advanced modal that guides without commanding: &ldquo;I <strong>would rather</strong> build on the <strong>groundwork</strong> he laid than start over.&rdquo; Same destination, a different order of operations; she earns <strong>credibility</strong> first, and only then does she <strong>move the needle</strong>.</p>
        <p style="margin-top:.8rem">The academic lead, a doctor, pushes back: a Brazil-designed framework may not transfer here. She concedes the fair part &mdash; &ldquo;I take the point about cultural distance&rdquo; &mdash; and holds her ground with a hedge, not a flat no: &ldquo;where we may differ is on transfer.&rdquo; If she <strong>had prescribed</strong> a Brazilian answer on day one, she <strong>would have lost</strong> the room; the <strong>third conditional</strong> lets her own that call without drowning in it. She is not importing conclusions, she says; she is importing a diagnostic method and letting their context <strong>read the room</strong> for itself.</p>
        <p style="margin-top:.8rem">Then Grant asks the question she could not prepare for: what does success look like for her, personally? She does not reach for the perfect sentence. She reaches for the true one. &ldquo;Let me think on that out loud,&rdquo; she says &mdash; the hedge that is honesty, not weakness &mdash; &ldquo;I'm not fully sure yet how I'd measure it, but success is the day a leader here disagrees with me directly, because the <strong>psychological safety</strong> is real.&rdquo; It is the whole program in one answer: <strong>developmental feedback</strong>, <strong>actionable insight</strong>, the confidence to <strong>empower</strong> a room to push back on her. Grant nods. &ldquo;That's the answer. Not the polished one &mdash; the true one.&rdquo; The English was only ever the vehicle. The leader was hers all along.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does &ldquo;by year one I will have run a full diagnostic&rdquo; use the future perfect?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the diagnostic already finished last year.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The future perfect (will have + past participle) projects confidence about what will already be true by a point in time &mdash; it turns a hope into a plan.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;year&rdquo; always requires the future perfect.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Why is &ldquo;He had rolled out the framework before he had the buy-in&rdquo; in the past perfect?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The past perfect sequences the earlier action in a backstory: the roll-out happened before the (later) point she is describing, so it steps one tense further back.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the sentence is a question.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;framework&rdquo; is an uncountable noun.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What does the cleft &ldquo;What I am changing is the sequence, not the destination&rdquo; achieve?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It makes the sentence more polite by adding a filler.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It spotlights the key idea &mdash; the sequence &mdash; and contrasts it with what is NOT changing, putting the emphasis exactly where she wants it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It puts the sentence into the passive voice.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. When Grant asks the question she didn't prepare for, what does she do &mdash; and why is it senior?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> She hedges honestly (&ldquo;let me think on that out loud&hellip; I'm not fully sure yet&rdquo;) and then commits to the true part. Naming uncertainty and still committing is more senior than a polished but hollow answer.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> She invents a confident-sounding number to fill the silence.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She refuses to answer and changes the subject.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">5. What is the through-line of the whole simulation &mdash; the point of the program?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That perfect grammar is what makes a room follow a leader.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The English was only ever the vehicle: Danielle is the same senior leader in English that she already was in Portuguese &mdash; she saw people clearly and told the truth, and that is what the room follows.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she should run the Canadian division exactly as she ran Brazil, unchanged.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Whole Map, One Job Each</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Nothing new here -- this is the consolidation. Across fifteen lessons you built these structures one at a time. In the room they are not rules to remember; each one simply does a single job. Read the map, then produce one sentence of your own with each structure.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Its one job</th><th style="padding:.7rem;text-align:left">Example (your Thursday meeting)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Future perfect</td><td style="padding:.6rem">Project confidence about what you will have delivered</td><td style="padding:.6rem">By year one I <strong>will have run</strong> a full diagnostic.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Past perfect</td><td style="padding:.6rem">Sequence a backstory -- what had happened before</td><td style="padding:.6rem">He <strong>had rolled out</strong> the framework before he had the buy-in.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Advanced modals</td><td style="padding:.6rem">Guide and disagree without commanding</td><td style="padding:.6rem">I <strong>would rather</strong> build on it than start over.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Wish / if only</td><td style="padding:.6rem">Voice adaptation, not complaint</td><td style="padding:.6rem">I <strong>wish</strong> the objections came sooner, so I read the room instead.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Third conditional</td><td style="padding:.6rem">Own a past call without drowning in it</td><td style="padding:.6rem">If I <strong>had prescribed</strong>, I <strong>would have lost</strong> the room.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Cleft sentences</td><td style="padding:.6rem">Put the emphasis exactly where you want it</td><td style="padding:.6rem"><strong>What</strong> I am changing <strong>is</strong> the sequence, not the destination.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Hedging</td><td style="padding:.6rem" colspan="2">Be honest about uncertainty, then commit: &ldquo;I'm <strong>not fully sure</strong> yet -- but here is what I <strong>am</strong> sure of.&rdquo;</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The only instruction for the room:</strong> do not reach for the perfect sentence &mdash; reach for the true one. Hedge honestly where you are genuinely unsure, then commit to what you know. The most senior thing in any language is a person who can say &ldquo;I don't have a complete answer yet, and here is how I would find one.&rdquo; You already do that in Portuguese; on Thursday you are just going to do it in English.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the right structure -- one blank, one structure from the map. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Meeting Opening in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order that opens the Thursday meeting like a leader, from the mandate to the close.</p>
      <div class="order-container" id="order-l15">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Contrast without blame, using a cleft: what I am changing is the sequence, not the destination -- I would rather build on the groundwork than start over.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Answer the uncomfortable question with hedge-then-commit: let me think on that out loud -- I'm not fully sure yet, but here is what I am sure of.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Frame the mandate without underselling it: I was brought in to lead the cultural transformation of this division.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Concede the fair part, then hold your ground: I take the point about cultural distance, and where we may differ is on transfer.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Project the plan with a future perfect: by the end of my first year I will have run a full diagnostic and rolled out a new onboarding experience.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l15')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These five are the ones you will recycle almost word for word in the real meeting.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the most senior answer for each moment of the Thursday leadership meeting.</p>
      <div class="quiz-item"><div class="quiz-question">Grant opens: &ldquo;Tell the room what you were brought here to do.&rdquo; The strongest opening is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Well, I'll just try to help out with the culture stuff a bit, if that's okay.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Let me frame my mandate: I was brought in to lead the cultural transformation of this division, and by year one I will have run a full diagnostic and rolled out a new onboarding experience.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Honestly I'm still figuring out what my job even is.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A director asks how this differs from what your predecessor dropped. The best answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;My predecessor had no idea what he was doing, honestly.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;He laid real groundwork, and I would rather build on it than start over. What I'm changing is the sequence: he rolled out the framework before he had the buy-in, so it never gained momentum.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;It's exactly the same plan, just with me running it.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The academic lead says a Brazil-designed framework may not transfer. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Concede the fair part and hold your ground with a hedge: &ldquo;I take the point about cultural distance, and where we may differ is on transfer &mdash; I'm importing a method, not conclusions, and letting your context write the answers.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Say &ldquo;No, you're wrong, it will transfer fine.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Drop the plan entirely to avoid the conflict.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Grant asks the question you didn't prepare for: &ldquo;What does success look like for you, personally?&rdquo; The most senior response:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Invent a confident metric on the spot so you don't look unsure.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Let me think on that out loud. I'm not fully sure yet how I'd measure it, but success is the day a leader here disagrees with me directly, because the psychological safety is real.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I'd rather not answer that one.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A director you haven't won over says your plan is &ldquo;ambitious&rdquo;. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Read the understatement and surface it: &ldquo;I'm reading &lsquo;ambitious&rsquo; as a gentle way of saying you're not yet convinced &mdash; tell me if I have that wrong, because I'd rather hear the real objection now.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Say &ldquo;Thanks!&rdquo; and take it as a compliment.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Tell them to stop being indirect and just say what they mean.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">This is your Thursday, for real. Open the meeting: frame your mandate (use a future perfect for what you will have delivered by year one), give a sixty-second overview of your People &amp; Culture plan for the Canadian division, and then answer, out loud, the question Grant would ask you: &ldquo;What does success look like for you, personally, in this role?&rdquo; Reach for the true sentence, not the perfect one -- hedge honestly where you are unsure, then commit. Use at least three structures from the map (future perfect, advanced modal, cleft, third conditional, wish) and at least five words from the toolkit (mandate, buy-in, groundwork, credibility, psychological safety, to move the needle, to empower).</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-15"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 15</h4>
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

# ---------- REGRA 22 (review): TODA palavra DEVE ja ter sido ensinada (reativacao) ----------
# O oposto da aula normal: numa REVISAO, o vocab e proposital-mente reciclado. Cada um
# esta na whitelist _build/model/vocab_allow_repeat.json. Extraido do hub (aulas 1..14).
JA_ENSINADO = {
    'accountability', 'actionable insight', 'a double-edged sword', 'active listening', 'alignment',
    'anecdotal', 'assertiveness', 'assumption', 'attrition', 'bandwidth', 'baseline', 'behavioral pattern',
    'belonging', 'benchmark', 'bilingual education', 'blind spot', 'boundary setting', 'buy-in',
    'career aspirations', 'cascading goals', 'causation', 'caveat', 'change management', 'coachable moment',
    'coaching mindset', 'code-switching', 'common ground', 'conflict resolution', 'confounding variable',
    'constructive challenge', 'constructive feedback', 'cordiality', 'core values', 'corrective action',
    'correlation', 'counterpoint', 'credibility', 'cross-functional', 'cultural assessment',
    'cultural diagnosis', 'cultural humility', 'cultural intelligence', 'culture fit', 'data storytelling',
    'defensiveness', 'deliverable', 'developmental feedback', 'diagnostic tool', 'difficult conversation',
    'disengagement', 'diversity and inclusion', 'egalitarian', 'employee journey',
    'employee value proposition', 'employer brand', 'engagement survey', 'entrenched', 'entry plan',
    'etiquette', 'exit interview', 'findings', 'focus group', 'formality', 'framework', 'franchisor',
    'frontline staff', 'gap analysis', 'groundwork', 'growth edge', 'growth mindset', 'handover',
    'headquarters', 'high-context culture', 'hybrid model', 'in hindsight', 'inclusive leadership',
    'indirect communication', 'individualism and collectivism', 'influence without authority',
    'key performance indicator', 'leading indicator', 'learning curve', 'legacy', 'listening tour',
    'low-context culture', 'mandate', 'margin of error', 'merit', 'milestone', 'non-violent communication',
    'okr', 'onboarding experience', 'organizational culture', 'outlier', 'peer-reviewed', 'people analytics',
    'people strategy', 'performance cycle', 'performance gap', 'power distance', 'precedent', 'predecessor',
    'preliminary', 'premise', 'psychological contract', 'psychological safety', 'pulse survey',
    'punctuality', 'quick win', 'ramp-up period', 'rapport', 'rationale', 'reciprocity', 'reframing',
    'reservation', 'resistance to change', 'response rate', 'rigor', 'roadblock', 'root cause', 'sample size',
    'senior leadership', 'small talk', 'sounding board', 'stakeholder', 'statistical significance',
    'status quo', 'stretch assignment', 'succession planning', 'takeaway', 'talent retention', 'tangible',
    'the elephant in the room', 'the jury is still out', 'the unwritten rules', 'tipping point',
    'to break the ice', 'to bite the bullet', 'to check in', 'to empower', 'to hit it off',
    'to move the needle', 'to read the room', 'to save face', 'to throw in the towel', 'toxic culture',
    'track record', 'traction', 'trade-off', 'transition period', 'trust deficit', 'trust index',
    'turnaround', 'turnover rate', 'understatement', 'uphill battle', 'vantage point', 'wake-up call',
    'workforce planning', 'work-life integration',
}
for w, _, _, _ in VOCAB:
    assert w.lower() in JA_ENSINADO, f'REVIEW: "{w}" nao foi ensinado antes — nao deveria ser novo na aula 15'

print('preclass.html gerado:', len(HTML) // 1024, 'KB; vocab', len(VOCAB), 'itens (todos reativados); speakable', len(set(SPEAKABLE)))
