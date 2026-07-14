#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 8 da Danielle Moreira (B2, People & Culture / Maple Bear).

AULA 8 = MIDPOINT REVIEW (consolidacao das aulas 1-7) + 1 estrutura NOVA.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..7
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 8 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).

GRAMATICA DA AULA 8 (nova; nao repete a1..a7):
  PARTICIPLE CLAUSES -- a gramatica do sumario executivo.
    - perfect participle:  "Having reviewed the findings, I would propose three things."
    - present participle:  "The index came back at 58, leaving us nine points below."
    - past participle:     "Asked about the timeline, most of the faculty said the same."
    - abertura fixa:       "Given the response rate..." / "Based on the findings..."

  POR QUE NAO O QUE O CURRICULO PEDIU: o curriculo pede "hedging as a system" como
  foco novo -- mas hedging JA foi ensinado na aula 5 (cleft & hedging) E na aula 6
  (causative passive & hedging data). E lista "modal perfects" -- ensinados na aula 2
  (third conditional + modal perfects). Ambos colidem (REGRA 22). Hedging e modal
  perfect voltam nesta aula como REVISAO (que e o proposito de uma aula de review),
  e a estrutura NOVA passa a ser participle clauses.
"""
import re
import random

random.seed(8)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Takeaway", "the one thing you want the room to still remember tomorrow morning",
     "conclus&#227;o principal / mensagem que fica",
     "If they remember one takeaway from this review, it should be that the culture is not broken -- it is unheard."),
    ("Caveat", "the limit you attach to your own claim, before somebody else attaches it for you",
     "ressalva",
     "One caveat: these are preliminary numbers, and the November survey may move them."),
    ("Rationale", "the reasoning behind a decision, stated out loud so the room can argue with it",
     "justificativa / racional",
     "Nobody objected to the plan. They objected to never having been given the rationale for it."),
    ("Trade-off", "what you agree to lose in order to gain something you want more",
     "compensa&#231;&#227;o / troca",
     "Every people strategy is a trade-off. A leader who presents one without naming the cost is presenting a wish."),
    ("Traction", "the point at which an initiative starts moving without you pushing it",
     "tra&#231;&#227;o / ades&#227;o",
     "The mentorship program is finally gaining traction: three teams asked to join without being invited."),
    ("Quick win", "a small, fast, visible result that buys you the credit to attempt the slow one",
     "vit&#243;ria r&#225;pida",
     "I need one quick win before December, or nobody will fund the two-year work."),
    ("Roadblock", "the obstacle that stops the work, as opposed to the one that merely slows it",
     "obst&#225;culo / barreira",
     "The real roadblock was never the budget. It was that two directors had stopped speaking."),
    ("Track record", "the history of what you have actually delivered, which speaks before you do",
     "hist&#243;rico de entregas",
     "In a new country, you have no track record. The first review is where you begin building one."),
    ("Preliminary", "true so far, and openly not final yet",
     "preliminar",
     "These are preliminary findings. Treating them as conclusions is how a review loses a room."),
    ("Tangible", "concrete enough to be counted, shown, or disagreed with",
     "tang&#237;vel / concreto",
     "Give the board one tangible number per slide, or the whole review sounds like a feeling."),
    ("To take stock of", "to stop, and honestly assess where you actually are",
     "fazer um balan&#231;o de",
     "Eight lessons in, it is worth taking stock of what has moved and what has not."),
    ("To fall short of", "to miss a target you had publicly committed to",
     "ficar aqu&#233;m de / n&#227;o atingir",
     "We fell short of the response rate we projected, and I would rather report that than bury it."),
    ("To build on", "to use what already worked as the foundation of the next step",
     "construir sobre / partir de",
     "The focus groups worked. What I propose is to build on them rather than start again."),
    ("To iron out", "to resolve the small remaining problems in something that basically works",
     "resolver / aparar as arestas",
     "The framework is sound. We have six weeks to iron out the details before the launch."),
    ("The jury is still out", "it is genuinely too early to say, and pretending otherwise costs you credibility",
     "ainda &#233; cedo para dizer",
     "On whether the new onboarding is working, the jury is still out. Ask me again in March."),
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

# ---------- Stage 1.5 fill-in-the-blank (as 4 formas de participle clause) ----------
BLANKS = [
    ("", "Having reviewed",
     "Hint: perfect participle (having + past participle) = the action that came FIRST. Never 'Having review'",
     "Having reviewed the focus groups, I would propose that we build on them rather than start again.",
     "the focus groups, I would propose that we build on them rather than start again."),
    ("The trust index came back at fifty-eight,", "leaving",
     "Hint: present participle (-ing) for the RESULT of the previous action. Never 'and it left'",
     "The trust index came back at fifty-eight, leaving us nine points below the benchmark.",
     "us nine points below the benchmark."),
    ("", "Asked",
     "Hint: past participle for a PASSIVE meaning ('When they were asked...'). Never 'Asking'",
     "Asked about the timeline, most of the faculty said exactly the same thing.",
     "about the timeline, most of the faculty said exactly the same thing."),
    ("", "Given",
     "Hint: fixed opening &mdash; 'Given + noun' = 'Considering / In view of'",
     "Given the response rate, the caveat belongs on the first slide, not the last.",
     "the response rate, the caveat belongs on the first slide, not the last."),
    ("", "Based on",
     "Hint: fixed opening &mdash; 'Based on + noun'. The participle must refer to the SUBJECT of the main clause",
     "Based on the preliminary findings, I am proposing two quick wins and one long piece of work.",
     "the preliminary findings, I am proposing two quick wins and one long piece of work."),
    ("Three teams asked to join without being invited,", "suggesting",
     "Hint: present participle for what the action SUGGESTS / produces. Never 'what suggests'",
     "Three teams asked to join without being invited, suggesting that the program is finally gaining traction.",
     "that the program is finally gaining traction."),
]
fills = []
for pre, ans, hint, phrase, post in BLANKS:
    SPEAKABLE.append(phrase)
    opening = f'"{pre} ' if pre else '"'
    fills.append(
        f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{opening}'
        f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
        f'data-phrase="{phrase}" placeholder="___"> {post}"</div>'
        f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
        f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
    )
fill_items = '\n'.join(fills)

# ---------- Stage 3 pronunciation ----------
SPEECH = [
    ("Having taken stock of the first six months, I would propose two quick wins and one long piece of work.",
     "Tendo feito um balan&#231;o dos primeiros seis meses, eu proporia duas vit&#243;rias r&#225;pidas e um trabalho longo."),
    ("We fell short of the response rate we projected, and I would rather report that than bury it.",
     "N&#243;s ficamos aqu&#233;m da taxa de resposta que projetamos, e eu prefiro reportar isso a enterrar."),
    ("Given the preliminary numbers, one caveat belongs on the first slide, not the last.",
     "Diante dos n&#250;meros preliminares, uma ressalva pertence ao primeiro slide, n&#227;o ao &#250;ltimo."),
    ("The focus groups worked, so what I propose is to build on them rather than start again.",
     "Os grupos focais funcionaram, ent&#227;o o que eu proponho &#233; partir deles em vez de recome&#231;ar."),
    ("On whether the new onboarding is working, the jury is still out. Ask me again in March.",
     "Sobre se o novo onboarding est&#225; funcionando, ainda &#233; cedo para dizer. Me pergunte de novo em mar&#231;o."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 08 -- Pre-class</div>
      <h3>Midpoint Review -- Consolidating HR Leadership Language for Canada</h3>
      <div class="lesson-desc">The midpoint: the lesson where you stop, take stock and PRESENT what you found &mdash; without inflating what worked or burying what fell short. All the language of lessons 1 to 7 comes back here as REVIEW (causative passive, cleft, inversion, third conditional, reporting verbs, hedging), inside a single executive presentation. Key words: takeaway, caveat, rationale, trade-off, traction, quick win, roadblock, track record, preliminary, tangible, to take stock of, to fall short of, to build on, to iron out, the jury is still out. New structure: participle clauses &mdash; the grammar of the executive summary (Having reviewed the findings... / ...leaving us nine points below the benchmark / Asked about the timeline... / Given the response rate...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="8" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="8">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the vocabulary of someone who presents a midpoint review &mdash; and survives the questions that come after it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l8">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Mariana Vidal had twenty-two slides and eleven minutes, and she lost the room on slide three. <strong>Having spent</strong> six months on the most careful cultural work of her career, she opened the midpoint review by explaining her methodology. By the time she arrived at what she had actually found, the Chief Operating Officer had stopped taking notes. The work was excellent. The review was a failure, and the two facts have nothing to do with each other.</p>
        <p style="margin-top:.8rem">The mistake was not nerves, and it was not her English. It was sequence. A senior room does not want the journey; it wants the <strong>takeaway</strong>, and it wants it first. <strong>Asked</strong> afterwards what he had needed, the COO was blunt: one <strong>tangible</strong> number, the <strong>rationale</strong> behind her recommendation, and the <strong>caveat</strong> she was clearly holding back. <strong>Given</strong> eleven minutes, he said, spend one of them telling me what you found and ten defending it.</p>
        <p style="margin-top:.8rem">She rebuilt the deck in a single evening. The new version opened with a sentence, not a slide: the culture here is not broken, it is unheard, and the response rate is the proof. Then the number, then the <strong>trade-off</strong>. <strong>Based on</strong> the <strong>preliminary</strong> findings, she proposed two <strong>quick wins</strong> and one long piece of work, naming what each would cost. She said out loud that the survey had <strong>fallen short of</strong> the target she had promised in June, <strong>leaving</strong> her with a smaller sample than she had wanted &mdash; and that she would rather report that than bury it. On the new onboarding, she said, the <strong>jury is still out</strong>: ask me again in March.</p>
        <p style="margin-top:.8rem">The COO approved the plan in four minutes. What convinced him was not the confidence. It was the <strong>caveat</strong>. A leader who names the limit of her own data is a leader whose numbers can be trusted the next time she brings some &mdash; and that, more than any single result, is how a <strong>track record</strong> begins.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. "<strong>Having spent</strong> six months on the work, she opened by explaining her methodology." &mdash; what is the perfect participle (<em>having</em> + past participle) saying here?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That both actions happened at the same time: she spent six months while she was opening the presentation.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That the participle action came <strong>FIRST</strong>: the six months of work, then the opening. It is how you pack the whole story into one subordinate clause and go straight to the point.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she is still spending the six months, because <em>having</em> marks the present continuous.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "<strong>Asked</strong> afterwards what he had needed, the COO was blunt." &mdash; why <em>Asked</em> and not <em>Asking</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because the subject (the COO) <strong>RECEIVES</strong> the action: somebody asked HIM. A passive participle = past participle. "Asking" would mean HE was the one asking.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because after a comma English always requires a past participle.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "ask" is an irregular verb and does not take an -ing form.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why exactly did Mariana lose the room on slide three?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because her English was not precise enough for a senior Canadian audience.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because of sequence: she opened with her methodology instead of her takeaway, and by the time she reached what she had found, the COO had stopped listening.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the cultural work itself was weak, and the room could see it immediately.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What actually convinced the COO to approve the plan in four minutes?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Her confidence, and the fact that she never admitted any weakness in the data.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The two quick wins, which meant the project would show results before December.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> The caveat &mdash; because a leader who names the limit of her own data is a leader whose numbers can be trusted the next time, and that is where a track record begins.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Participle Clauses</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The grammar of the executive summary: it takes TWO sentences and turns the less important one into a short clause, with no subject and no connector &mdash; leaving the main clause with all the weight. It is what separates someone who NARRATES from someone who SUMMARIZES.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. Perfect participle<br><strong>Having</strong> + past participle</td><td style="padding:.6rem">The action that came FIRST. It packs the whole past into five words.</td><td style="padding:.6rem"><strong>Having reviewed</strong> the findings, I would propose two quick wins.<br><span style="color:var(--text-dim)">= After I reviewed the findings, I would propose...</span></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. Present participle<br>verbo + <strong>-ing</strong></td><td style="padding:.6rem">The RESULT or consequence of the main clause. It almost always comes AFTER the comma.</td><td style="padding:.6rem">The index came back at fifty-eight, <strong>leaving</strong> us nine points below the benchmark.<br><span style="color:var(--text-dim)">= ...and this left us nine points below.</span></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. Past participle<br>the participle alone</td><td style="padding:.6rem">A PASSIVE meaning: something was done TO the subject.</td><td style="padding:.6rem"><strong>Asked</strong> about the timeline, most of the faculty said the same thing.<br><span style="color:var(--text-dim)">= When they were asked about the timeline...</span></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. Fixed openings<br><strong>Given</strong> / <strong>Based on</strong> / <strong>Drawing on</strong></td><td style="padding:.6rem">The executive opening. It anchors the recommendation in the evidence, before you say what it is.</td><td style="padding:.6rem"><strong>Given</strong> the response rate, the caveat belongs on slide one.<br><strong>Based on</strong> the preliminary findings, I am proposing...</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">The golden rule</td><td style="padding:.6rem" colspan="2">The participle and the main clause must share the <strong>SAME SUBJECT</strong>. If they do not, the sentence collapses (the classic <em>dangling participle</em>) &mdash; and in English it does not sound odd: it sounds <em>wrong</em>.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (mistake no. 1 &mdash; the dangling participle):</strong> "<em>Having reviewed the findings, the response rate was disappointing</em>" is WRONG: YOU reviewed the findings, not the response rate. The subject of the main clause has to be the one who performs the participle. Correct: "Having reviewed the findings, <strong>I</strong> found the response rate disappointing." Foolproof test: ask "who did it?" &#8594; the answer has to be the subject of the main clause.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (mistake no. 2):</strong> <em>having</em> takes a PAST PARTICIPLE, never an infinitive or a base form. "Having <em>review</em> the data" &#8594; "Having <strong>reviewed</strong> the data". And the passive participle is the participle alone, without <em>being</em>: "<em>Being asked</em> about the timeline" is possible, but the executive register prefers the dry "<strong>Asked</strong> about the timeline".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Why this matters to you:</strong> you have eleven minutes and a COO who stops taking notes on slide three. The participle clause is the tool that compresses "We reviewed the findings, and after that I prepared a proposal" into "<strong>Having reviewed the findings, I would propose...</strong>" &mdash; and gives your seconds back to the only part the room wants to hear: what you found, and what you are going to do.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Review of lessons 1-7 (today it all comes back):</strong> causative passive (<em>We had the survey designed by...</em>), cleft (<em>What the team needs is...</em>), inversion (<em>Never have I seen...</em>), third conditional + modal perfects (<em>If we had asked earlier, we would have known / we should have addressed it</em>), reporting verbs (<em>He acknowledged that... / She agreed to...</em>) and hedging (<em>It would appear that... / To a certain extent...</em>). This is not new content: these are your tools. Today you use them ALL in a single presentation.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct participle form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Midpoint Review in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order you will run the midpoint review with the Canadian leadership. Remember Mariana's mistake: the room wants the end first.</p>
      <div class="order-container" id="order-l8">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">Name the caveat yourself, before anyone else does: what you fell short of, and what the jury is still out on.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">Close by asking for the one decision you actually came for, with a date attached to it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">Open with the takeaway, in one sentence, before a single slide: the culture is not broken, it is unheard.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">Propose what comes next: two quick wins to build on, one long piece of work, and the trade-off each one costs.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">Put one tangible number on the table, and give the rationale behind it before anybody has to ask.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l8')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that hold your midpoint review together, from start to finish.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your midpoint review with the Canadian leadership.</p>
      <div class="quiz-item"><div class="quiz-question">You have eleven minutes with the COO. Your first sentence is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Let me start by walking you through the methodology we used and the four phases of the assessment.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;The takeaway first: the culture here is not broken, it is unheard &mdash; and the response rate is the evidence. Everything else I say today defends that sentence.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Thank you all so much for your time today. I know how busy everyone is at this time of year.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the participle clause correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Having reviewed the findings, the response rate was disappointing.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Having reviewed the findings, I would propose that we build on the focus groups rather than start again.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Having review the findings, I am proposing two quick wins.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You promised a seventy percent response rate in June. It came back at thirty-eight. The COO has not asked about it yet. You:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;One caveat, and I would rather give it to you than have you find it: we fell short of the rate I projected in June. It leaves me a smaller sample, and it is itself a finding about how heard this team feels.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Say nothing about it. He has not asked, the work is strong, and the number would only distract from the recommendation.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;The response rate was low, but honestly that happens with every survey, so I would not read anything into it.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks: &ldquo;Is the new onboarding working?&rdquo; You genuinely do not know yet. The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Yes, definitely. Everyone I have spoken to seems very positive about it.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;I have no idea. It is impossible to measure something like that.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;On that one, the jury is still out. The first cohort finishes in February, so I will have a tangible number for you in March &mdash; and not before.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He pushes back: &ldquo;Two quick wins? I want the whole framework by Q2.&rdquo; You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;We can do that, and I would want you to see the trade-off: pulling the framework into Q2 means the baseline gets taken after the change rather than before, which costs us the ability to prove that any of it worked.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;That is not possible. Q2 is far too early for something of this size.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Of course, no problem at all. I will have the whole framework ready by Q2.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">You have eleven minutes with the Canadian leadership team, and this is the midpoint review. Give it. Open with your takeaway in ONE sentence, before any detail. Then: one tangible number and the rationale behind it; the caveat you are holding (what you fell short of, and what the jury is still out on); and what you propose next -- two quick wins to build on, one long piece of work, and the trade-off each one costs. Open at least two sentences with a participle clause (Having reviewed... / Given... / Based on...), and use six words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-8"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 8</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-7 pode voltar como vocab card ----------
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
    'cultural intelligence', 'high-context culture', 'low-context culture',
    'power distance', 'individualism and collectivism', 'indirect communication',
    'assertiveness', 'cultural humility', 'work-life integration', 'inclusive leadership',
    'to bridge cultural gaps', 'to read between the lines', 'to account for',
    'to set out', 'to take into consideration',
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-7'
assert 12 <= len(VOCAB) <= 15, f'REGRA 13 (B2 = 12-15 palavras): {len(VOCAB)}'

# ---------- aula 9 reserva vocabulario proprio: nao roubar ----------
RESERVADO_A9 = {'key result', 'initiative', 'roadmap', 'talent pipeline',
                'retention rate', 'headcount'}
steal = {w for w, _, _, _ in VOCAB if w.lower() in RESERVADO_A9}
assert not steal, f'vocabulario reservado para a aula 9: {steal}'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
