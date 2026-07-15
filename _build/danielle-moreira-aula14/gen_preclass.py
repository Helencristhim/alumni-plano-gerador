#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 14 da Danielle Moreira (B2, People & Culture / Maple Bear).

Tema: The Coaching 1:1 -- Developing People, Not Managing Them (modelo de LEITURA, aula PAR / REGRA 29).
Gramatica NOVA: advanced modals -- would rather / had better / may as well (+ basico subjunctivo
advisory). PIVOT: o curriculo original da a14 ("Mentoring / Difficult Conversations / Feedback")
DUPLICA a aula 7 (feedback ja gasto: constructive feedback, defensiveness, to sugarcoat...).
Re-escopado para "The Coaching 1:1" -- desenvolvimento/coaching de mentorado, angulo ainda nao
coberto, vocab novo. A gramatica pedida (would rather / had better / may as well) estava FRESCA.
NAO reensina wish/if only (aula 13) nem reported speech (aula 12).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = ZERO portugues na tela do aluno; 15 itens de vocab (10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..13
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 14 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(14)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT [NAO renderizada, B2], exemplo)
VOCAB = [
    ("Developmental feedback", "input aimed at helping someone grow, not at correcting a single past error",
     "feedback de desenvolvimento",
     "She reframed the review as developmental feedback, so Owen heard a path forward instead of a verdict on his past."),
    ("Growth edge", "the next skill or capacity a person is just ready to stretch into",
     "pr&#243;ximo n&#237;vel de crescimento",
     "His growth edge was not effort; it was asking for help before a deadline slipped, and she named it gently."),
    ("Coachable moment", "a short opening when someone is genuinely open to learning something",
     "momento propenso ao aprendizado",
     "The moment Owen admitted he was struggling was a coachable moment, and she did not waste it with advice he had not asked for."),
    ("Active listening", "listening fully to understand the person, not to prepare your reply",
     "escuta ativa",
     "Active listening meant she let the silence sit until Owen said the thing he had almost swallowed."),
    ("Reframing", "offering a different, more useful way to see the same situation",
     "ressignifica&#231;&#227;o",
     "Instead of correcting him, she tried reframing: he was not failing, he was on the steep part of a learning curve."),
    ("Sounding board", "a trusted person you think out loud with to test your own ideas",
     "interlocutor de confian&#231;a",
     "She offered to be a sounding board, not a judge, so he could think out loud without defending himself."),
    ("Stretch assignment", "a task set deliberately beyond someone's comfort zone to build capacity",
     "tarefa desafiadora de desenvolvimento",
     "The stretch assignment was deliberately a size too big, because that is where he would actually grow."),
    ("Coaching mindset", "leading by asking questions instead of handing over answers",
     "mentalidade de coaching",
     "A coaching mindset asks &lsquo;what would it look like if...?&rsquo; before it ever offers an answer."),
    ("Boundary setting", "making your limits clear, kindly and firmly, so expectations stay realistic",
     "estabelecimento de limites",
     "Boundary setting is not coldness; it is telling someone honestly what you can and cannot take on."),
    ("Career aspirations", "where a person genuinely hopes their career will go over time",
     "aspira&#231;&#245;es de carreira",
     "Once she understood his real career aspirations, the work she gave him finally pointed somewhere he wanted to go."),
    ("To empower", "to give someone the authority and the confidence to act on their own",
     "empoderar / dar autonomia",
     "The goal of the 1:1 was not to fix Owen but to empower him to solve the next problem without her."),
    ("To check in", "to briefly and deliberately ask how someone is really doing",
     "fazer um ponto de contato / acompanhar",
     "She had made a habit of checking in before a deadline, not after, so problems surfaced while they were still small."),
    ("To play to someone's strengths", "to give someone work that uses what they are already best at",
     "aproveitar os pontos fortes de algu&#233;m",
     "Rather than force him into spreadsheets, she chose to play to his strengths and let him run the interviews."),
    ("To bite the bullet", "to face a hard, unavoidable task instead of putting it off",
     "encarar o problema de frente",
     "Some conversations you can only postpone for so long; eventually you bite the bullet and name the issue."),
    ("To throw in the towel", "to give up and stop trying",
     "jogar a toalha / desistir",
     "He had been ready to throw in the towel, and one honest hour was the difference between quitting and staying."),
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

# ---------- Stage 1.5 fill-in-the-blank (advanced modals: would rather / had better / may as well) ----------
BLANKS = [
    ("I would rather", "address",
     "Hint: WOULD RATHER is followed by the bare infinitive (no 'to') -- would rather ADDRESS this now",
     "I would rather address this issue now than let it drift into next quarter.",
     "this issue now than let it drift into next quarter."),
    ("You had", "better",
     "Hint: strong advice = HAD BETTER + bare infinitive -- you HAD better loop them in first",
     "You had better loop in the academic team before you commit to that date.",
     "loop in the academic team before you commit to that date."),
    ("If the meeting is happening anyway, we", "may as well",
     "Hint: no better option, so do it = MAY AS WELL + bare infinitive",
     "If the meeting is happening anyway, we may as well use it to reset expectations.",
     "use it to reset expectations."),
    ("I would rather you", "didn't",
     "Hint: WOULD RATHER + a different subject takes the past form -- I would rather you DIDN'T promise it yet",
     "I would rather you didn't promise a date we cannot realistically hit.",
     "promise a date we cannot realistically hit."),
    ("You had better not", "wait",
     "Hint: negative strong advice = HAD BETTER NOT + bare infinitive -- had better not WAIT until it slips",
     "You had better not wait until the deadline slips to ask for help.",
     "until the deadline slips to ask for help."),
    ("I suggest that each mentee", "be",
     "Hint: advisory subjunctive stays in the base form -- I suggest that each mentee BE given a clear growth edge",
     "I suggest that each mentee be given a clear growth edge for the quarter.",
     "given a clear growth edge for the quarter."),
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
    ("I would rather we solved the root cause together than patch the same problem again next month.",
     ""),
    ("You had better talk to your manager before the deadline slips, not after -- it is far easier now.",
     ""),
    ("If you are going to redo the report anyway, you may as well use it to show what you have learned.",
     ""),
    ("Help me understand what got in the way -- I am not here to judge it, I am here to think it through with you.",
     ""),
    ("You are not failing; you are on the steep part of the learning curve, and I would rather grow you than replace you.",
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

HTML = f'''<div class="lesson-card" id="ex-lesson-14">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1543269865-cbf427effbad?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 14 -- Pre-class</div>
      <h3>The Coaching 1:1 -- Developing People, Not Managing Them</h3>
      <div class="lesson-desc">Running a developmental one-on-one with a talented mentee who is losing confidence and close to quitting: listen before you advise, reframe &ldquo;I am failing&rdquo; into &ldquo;I am on a learning curve&rdquo;, find the growth edge, and give the guidance that develops instead of the order that shrinks. Key words: developmental feedback, growth edge, coachable moment, active listening, reframing, sounding board, stretch assignment, coaching mindset, boundary setting, career aspirations, to empower, to check in, to play to someone's strengths, to bite the bullet, to throw in the towel. Structure: advanced modals -- would rather / had better / may as well (I would rather we solved the root cause / you had better talk to your manager before the deadline slips / if you are redoing it anyway, you may as well show what you learned).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="14" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="14">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the language of a leader who develops people in a one-on-one &mdash; the difference between telling a mentee what to do and coaching them into doing it themselves.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l14">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Owen, a junior coordinator Danielle mentors, had gone quiet for two weeks &mdash; deadlines slipping, replies getting shorter. In a voice note the night before their 1:1, he all but said he was ready to <strong>throw in the towel</strong>. Danielle knew the easy move was to fix it for him. She chose the harder one: a <strong>coaching mindset</strong>. She opened the meeting not with a verdict but with a question, and then did the thing that is hardest for a fast, capable leader &mdash; <strong>active listening</strong>, letting the silence sit until he named what was really wrong.</p>
        <p style="margin-top:.8rem">What came out was not laziness. Owen was drowning in tasks that did not <strong>play to his strengths</strong>, and he had been too proud to <strong>check in</strong> before things slipped. So she tried <strong>reframing</strong>: &ldquo;You are not failing &mdash; you are on the steep part of the learning curve.&rdquo; Then she guided, without commanding. &ldquo;I <strong>would rather</strong> we solved the root cause together than patch the same problem next month. And honestly, you <strong>had better</strong> talk to your manager before the next deadline slips, not after &mdash; it is far easier now.&rdquo; When Owen admitted he would have to redo a whole report anyway, she smiled: &ldquo;If you are redoing it regardless, you <strong>may as well</strong> use it to show exactly what you have learned.&rdquo;</p>
        <p style="margin-top:.8rem">This was the <strong>coachable moment</strong>, and she did not fill it with orders. She offered to be a <strong>sounding board</strong>, gave him <strong>developmental feedback</strong> instead of a scorecard, and named his real <strong>growth edge</strong>: not effort, but asking for help early. She set a <strong>stretch assignment</strong> just beyond his comfort &mdash; running the next round of interviews &mdash; because that is where growth actually happens, and it pointed straight at his <strong>career aspirations</strong>.</p>
        <p style="margin-top:.8rem">The point of the hour was never to rescue Owen. It was to <strong>empower</strong> him to solve the next problem without her. She modelled <strong>boundary setting</strong> too &mdash; telling him plainly what she could and could not take off his plate &mdash; so the help stayed real. He walked in ready to quit and walked out with one honest task and a reason to stay. Sometimes you have to <strong>bite the bullet</strong> and have the conversation; more often, you just have to ask the right question and then be quiet enough to hear the answer.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. &ldquo;I <strong>would rather</strong> we solved the root cause than patch it again&rdquo; &mdash; what does <em>would rather</em> express here?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A clear preference between two options &mdash; and with a different subject (<em>we</em>) it takes the past form (<em>solved</em>).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> An obligation, exactly the same in meaning as &ldquo;must&rdquo;.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A question asking Owen for permission to continue.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. &ldquo;You <strong>had better</strong> talk to your manager before the deadline slips&rdquo; &mdash; why <em>had better</em> and not just <em>should</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because <em>had better</em> is only about the past &mdash; it means &ldquo;it would have been better&rdquo;.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because <em>had better</em> is stronger than <em>should</em>: it is urgent advice that carries a warning &mdash; do it, or something bad follows &mdash; and it is followed by the bare verb (<em>talk</em>), no <em>to</em>.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because <em>had better</em> can only be used with the word <em>please</em>.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. &ldquo;If you are redoing it anyway, you <strong>may as well</strong> use it to show what you learned.&rdquo; What is the idea behind <em>may as well</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That the action is forbidden and should be avoided.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That since there is no better alternative, you might as well do the thing &mdash; it costs nothing extra and there is an upside.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That the speaker is unsure whether the action is even possible.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. According to the text, what was the real point of Danielle's 1:1 with Owen?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> To take the difficult tasks off his plate and solve the problem for him.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> To deliver a firm scorecard so he knew exactly where he had fallen short.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> To empower him to solve the next problem himself &mdash; by listening, reframing, and naming his growth edge instead of giving orders.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Advanced Modals: would rather / had better / may as well</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The modals that shift you from &ldquo;making a suggestion&rdquo; to &ldquo;executive guidance&rdquo; &mdash; warm, but directive. This is how a senior leader advises without commanding, and guides without shrinking the other person.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">would rather<br>+ <strong>bare</strong> infinitive</td><td style="padding:.6rem">A clear preference (same subject). No <em>to</em>.</td><td style="padding:.6rem">I <strong>would rather</strong> grow you than replace you. &middot; NOT &ldquo;would rather <em>to</em> grow&rdquo;.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">would rather + <strong>subject</strong><br>+ <strong>past</strong> form</td><td style="padding:.6rem">A preference about what <em>someone else</em> does &mdash; the verb goes to the past.</td><td style="padding:.6rem">I <strong>would rather you didn't</strong> promise that date. &middot; I <strong>would rather we solved</strong> the root cause.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">had better<br>+ <strong>bare</strong> infinitive</td><td style="padding:.6rem">Strong, urgent advice with a warning: do it, or a bad result follows. Negative: <strong>had better not</strong>.</td><td style="padding:.6rem">You <strong>had better</strong> loop in the team first. &middot; You <strong>had better not</strong> wait until it slips.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">may / might as well<br>+ <strong>bare</strong> infinitive</td><td style="padding:.6rem">No better option exists, so you might as well do it &mdash; low cost, clear upside.</td><td style="padding:.6rem">If you are redoing it anyway, you <strong>may as well</strong> show what you learned.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Advisory subjunctive<br>suggest / recommend / insist + that + <strong>base</strong> verb</td><td style="padding:.6rem">Formal directive language: the verb stays in the base form (no <em>-s</em>, <em>be</em> not <em>is</em>).</td><td style="padding:.6rem">I suggest that each mentee <strong>be</strong> given a clear growth edge. &middot; I recommend that he <strong>take</strong> the interviews.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it sounds senior</td><td style="padding:.6rem" colspan="2"><strong>would rather</strong> owns a preference without an order; <strong>had better</strong> lands a warning without raising your voice; <strong>may as well</strong> makes a decision feel easy. Together they are the tone of a leader who is empathetic and precise at the same time &mdash; guidance, not commands.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the number one slip):</strong> all three take the <strong>bare</strong> infinitive &mdash; no <em>to</em>. &ldquo;You had better <em>to</em> talk&rdquo; &rarr; &ldquo;You had better <strong>talk</strong>&rdquo;. &ldquo;I would rather <em>to</em> reframe&rdquo; &rarr; &ldquo;I would rather <strong>reframe</strong>&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (the other slip):</strong> with a different subject, <strong>would rather</strong> takes the past form. &ldquo;I would rather you <em>don't</em>&rdquo; &rarr; &ldquo;I would rather you <strong>didn't</strong>&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>The line that wins the room:</strong> &ldquo;I <strong>would rather</strong> grow you than replace you &mdash; but you <strong>had better</strong> ask for help before the next deadline, and if you are redoing the report anyway, you <strong>may as well</strong> use it to show me what changed.&rdquo;</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Coaching 1:1 in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order a leader runs a developmental one-on-one &mdash; listen first, empower last.</p>
      <div class="order-container" id="order-l14">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">Reframe the story: &ldquo;You are not failing &mdash; you are on the steep part of the learning curve.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">Set a stretch assignment that plays to their strengths, and empower them to run it without you.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">Open with a real question, not a verdict, and use active listening &mdash; let the silence sit.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">Name the growth edge and guide, not command: &ldquo;I would rather we solved the root cause; you had better ask early next time.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">Catch the coachable moment when they admit the real problem, and stay a sounding board, not a judge.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l14')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are sentences you will actually use in your next mentoring 1:1 &mdash; warm, but directive.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment in a developmental one-on-one.</p>
      <div class="quiz-item"><div class="quiz-question">A mentee says, &ldquo;I am just not good at this. Maybe I should quit.&rdquo; The most developmental response is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;You are right, it is not for everyone &mdash; let us talk about an exit.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Help me understand what got in the way. You are not failing &mdash; you are on the steep part of the learning curve, and I would rather grow you than replace you.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Just try harder and it will sort itself out.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to give urgent advice that carries a real warning, without shouting. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;You had better to talk to your manager today.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;You had better talk to your manager before the deadline slips &mdash; it is far easier now than later.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Maybe, if you feel like it, you could possibly mention it sometime.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the advanced modals correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I would rather to reframe the problem, and you had better to ask early.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;I would rather you don't promise a date, and we may as well to start today.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;I would rather you didn't promise a date, and since we are meeting anyway, we may as well start today.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A mentee is drowning in tasks that do not suit them. The coaching move is to:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Add more tasks so they toughen up and stop complaining.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Play to their strengths &mdash; give a stretch assignment that uses what they are best at &mdash; and empower them to run it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Quietly do the tasks yourself so nothing slips this quarter.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Your mentee opens up about being close to giving up. The strongest use of that moment is to:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Fill the silence with a list of instructions before they change their mind.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Treat it as a coachable moment &mdash; stay a sounding board, name their real growth edge, and offer developmental feedback, not a scorecard.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Note it for the performance review and move on to the next agenda item.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">Run a two-minute mock coaching 1:1 out loud. Your mentee has gone quiet and is close to throwing in the towel. Open with a real question, reframe their story, name one growth edge, and guide them with the advanced modals &mdash; use &ldquo;I would rather...&rdquo;, &ldquo;you had better...&rdquo; and &ldquo;you may as well...&rdquo; at least once each, plus at least six words from this lesson. Tone: warm, but directive.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-14"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 14</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-13 pode voltar como vocab card ----------
JA_ENSINADO = {
    'organizational culture', 'employee journey', 'people strategy', 'framework',
    'stakeholder', 'alignment', 'to roll out', 'headquarters', 'franchisor',
    'bilingual education', 'hybrid model', 'senior leadership', 'to make headway',
    'to take a stance', 'to carry out',
    'cultural diagnosis', 'core values', 'psychological safety', 'onboarding experience',
    'culture fit', 'belonging', 'disengagement', 'attrition', 'turnover rate',
    'toxic culture', 'exit interview', 'pulse survey', 'to foster a culture of',
    'to look into', 'the elephant in the room',
    'okr', 'key performance indicator', 'cascading goals', 'deliverable', 'milestone',
    'accountability', 'cross-functional', 'bandwidth', 'buy-in', 'to put forward',
    'to push back', 'to move the needle', 'to cut to the chase', 'to bring about',
    'to circle back to',
    'talent retention', 'engagement survey', 'performance cycle', 'succession planning',
    'employer brand', 'people analytics', 'workforce planning', 'change management',
    'psychological contract', 'diversity and inclusion', 'influence without authority',
    'employee value proposition', 'to make a compelling case', 'to phase out',
    'a double-edged sword',
    'cultural intelligence', 'high-context culture', 'low-context culture', 'power distance',
    'individualism and collectivism', 'indirect communication', 'assertiveness',
    'cultural humility', 'work-life integration', 'inclusive leadership',
    'to bridge cultural gaps', 'to read between the lines', 'to account for', 'to set out',
    'to take into consideration',
    'cultural assessment', 'diagnostic tool', 'baseline', 'response rate', 'focus group',
    'trust index', 'root cause', 'gap analysis', 'findings', 'benchmark',
    'to run a diagnostic', 'to gather insights', 'to surface an issue', 'to come up with',
    'to open a can of worms',
    'constructive feedback', 'conflict resolution', 'blind spot', 'defensiveness',
    'resistance to change', 'non-violent communication', 'growth mindset',
    'behavioral pattern', 'performance gap', 'corrective action', 'to take ownership of',
    'to address head-on', 'to follow through on', 'to sugarcoat', 'to beat around the bush',
    'takeaway', 'caveat', 'rationale', 'trade-off', 'traction', 'quick win', 'roadblock',
    'track record', 'preliminary', 'tangible', 'to take stock of', 'to fall short of',
    'to build on', 'to iron out', 'the jury is still out',
    'counterpoint', 'reservation', 'premise', 'assumption', 'merit', 'anecdotal', 'rigor',
    'peer-reviewed', 'common ground', 'to concede', 'to take issue with',
    "to play devil's advocate", 'to stand your ground', 'to defer to', 'to hold water',
    # aula 10
    'data storytelling', 'correlation', 'causation', 'confounding variable',
    'statistical significance', 'sample size', 'outlier', 'margin of error',
    'leading indicator', 'actionable insight', 'to control for', 'to skew',
    'to read too much into', 'to tease out', 'to connect the dots',
    # aula 11
    'legacy', 'groundwork', 'tipping point', 'precedent', 'turnaround', 'entrenched',
    'status quo', 'in hindsight', 'wake-up call', 'uphill battle', 'to inherit',
    'to trace back to', 'to come to a head', 'to gain momentum', 'to reverse a trend',
    # aula 12
    'entry plan', 'listening tour', 'ramp-up period', 'learning curve', 'credibility',
    'mandate', 'predecessor', 'transition period', 'frontline staff', 'vantage point',
    'handover', 'to hit the ground running', 'to take the reins', 'to size up', 'to lean on',
    # aula 13
    'rapport', 'small talk', 'egalitarian', 'cordiality', 'punctuality', 'formality',
    'understatement', 'code-switching', 'etiquette', 'reciprocity', 'to break the ice',
    'to read the room', 'to hit it off', 'to save face', 'the unwritten rules',
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-13'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
