#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 12 da Danielle Moreira (B2, People & Culture / Maple Bear).

Tema: The First 90 Days -- Listening Before You Lead (modelo de LEITURA, aula PAR / REGRA 29).
Gramatica NOVA: reported speech + reporting verbs (backshift, say vs tell, verb+obj+to,
verb+gerund). PIVOT: o curriculo original da a12 (OKR + future perfect/continuous) DUPLICA
a aula 9 -- re-escopado para "First 90 Days" com gramatica ainda nao dada (aulas 1-11).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = ZERO portugues na tela do aluno; 15 itens de vocab (11 termos + 4 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..11
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 12 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(12)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT [NAO renderizada, B2], exemplo)
VOCAB = [
    ("Entry plan", "a deliberate 90-day plan for how a new leader will learn, decide, and act",
     "plano de entrada / de integra&#231;&#227;o",
     "The entry plan she finally presented had three phases -- learn, decide, act -- and she was still, deliberately, in the first."),
    ("Listening tour", "a structured round of one-on-one conversations a new leader holds before changing anything",
     "rodada de escuta",
     "Instead of restructuring, she spent the first quarter on a listening tour, sitting with the people who run the classrooms."),
    ("Ramp-up period", "the early stretch in a new role when you are still building context and cannot work at full speed",
     "per&#237;odo de adapta&#231;&#227;o inicial",
     "The ramp-up period is not wasted time, even though it feels like it, because you are used to full speed and suddenly you cannot."),
    ("Learning curve", "how steep and how long the climb is before a new role feels natural",
     "curva de aprendizado",
     "That discomfort is the learning curve, not a sign that you are failing."),
    ("Credibility", "the trust you earn that makes people act on what you say, before any authority forces them to",
     "credibilidade",
     "Credibility is not spent with the title. It is earned in the first quarter, one honest conversation at a time."),
    ("Mandate", "the clear authority and remit you are given to make a specific change happen",
     "mandato / al&#231;ada",
     "You have a real mandate here, and the temptation will be to spend it fast to prove you deserve it."),
    ("Predecessor", "the person who held your role before you, whose decisions you inherit",
     "antecessor(a)",
     "A predecessor who is honest about what went wrong is the most useful person you have in the first quarter."),
    ("Transition period", "the window between two leaders when a role is formally handed over",
     "per&#237;odo de transi&#231;&#227;o",
     "The mistake almost every senior hire makes is to treat the transition period as an audition."),
    ("Frontline staff", "the people who do the core daily work directly with students, furthest from head office",
     "equipe da linha de frente",
     "She sat with the frontline staff, not just the directors -- the people who actually run the classrooms."),
    ("Vantage point", "the position from which you see a situation, which shapes what you notice and miss",
     "ponto de observa&#231;&#227;o / perspectiva",
     "It came from a particular vantage point -- the classroom floor -- that a new leader only reaches by asking early."),
    ("Handover", "the formal passing of a role, its context, and its unfinished work from one person to the next",
     "passagem de bast&#227;o / transmiss&#227;o",
     "None of this was in the handover document, and none of it could have been."),
    ("To hit the ground running", "to be productive immediately in a new role, with no slow start",
     "come&#231;ar a todo vapor",
     "Everyone expects a senior hire to hit the ground running, but the smartest ones slow down first to speed up later."),
    ("To take the reins", "to formally assume control and responsibility for something",
     "assumir as r&#233;deas",
     "On Monday she takes the reins of the Canadian division, and the first decision is to make no big decision for ninety days."),
    ("To size up", "to assess a person or a situation quickly and shrewdly",
     "avaliar / medir",
     "Size up the culture before you try to move it."),
    ("To lean on", "to rely on someone for support or expertise",
     "apoiar-se em / contar com",
     "Lean on Gordon. He made the fast mistakes so you do not have to."),
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

# ---------- Stage 1.5 fill-in-the-blank (reported speech + reporting verbs) ----------
BLANKS = [
    ("Gordon", "told",
     "Hint: TELL takes a person object -- Gordon TOLD me. 'Said' would need no 'me' (said that...)",
     "Gordon told me that he had restructured the academic team too fast.",
     "me that he had restructured the academic team too fast."),
    ("He", "admitted",
     "Hint: choose the reporting verb that names how it was said -- he ADMITTED it (conceded a fault), not just 'said'",
     "He admitted that he had been wrong about almost all of it.",
     "that he had been wrong about almost all of it."),
    ("Ruth urged me", "to build",
     "Hint: verb + object + TO-infinitive -- urged me TO BUILD a simple entry plan. After 'urged me' comes 'to' + base verb",
     "Ruth urged me to build a simple entry plan with three phases.",
     "a simple entry plan with three phases."),
    ("The regional director warned me", "not to",
     "Hint: warn + object + NOT TO + base verb -- warned me NOT TO mistake their politeness for agreement",
     "The regional director warned me not to mistake their politeness for agreement.",
     "mistake their politeness for agreement."),
    ("One coordinator explained that the reorganizations", "had",
     "Hint: backshift -- reporting a past event moves one tense back: 'were reversed' becomes HAD been reversed",
     "One coordinator explained that the reorganizations had all been quietly reversed.",
     "all been quietly reversed."),
    ("She recommended", "waiting",
     "Hint: RECOMMEND is followed by the -ing form (a gerund) -- recommended WAITING, not 'to wait'",
     "She recommended waiting until the listening tour was finished before changing anything.",
     "until the listening tour was finished before changing anything."),
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
    ("Gordon told me he had restructured the team in his first month, and that he had been wrong about almost all of it.",
     ""),
    ("He urged me to decide nothing for ninety days and to spend the ramp-up period on a listening tour.",
     ""),
    ("One coordinator explained that past reorganizations had all been quietly reversed, so the team waits out new plans.",
     ""),
    ("The regional director warned me not to mistake their politeness for agreement.",
     ""),
    ("Credibility is not spent with the title; it is earned in the first quarter, one honest conversation at a time.",
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

HTML = f'''<div class="lesson-card" id="ex-lesson-12">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1454165833767-1e70af3e3fdc?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 12 -- Pre-class</div>
      <h3>The First 90 Days -- Listening Before You Lead</h3>
      <div class="lesson-desc">Taking the reins of the Canadian division without arriving as a stranger who changes everything on day one: run a listening tour, report back what the outgoing director and the frontline staff actually said, and earn credibility before spending the mandate. Key words: entry plan, listening tour, ramp-up period, learning curve, credibility, mandate, predecessor, transition period, frontline staff, vantage point, handover, to hit the ground running, to take the reins, to size up, to lean on. Structure: reported speech + reporting verbs (he admitted that he had been wrong / she urged me to slow down / they warned me not to restructure / one coordinator explained that the reorganizations had been reversed).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="12" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="12">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the language of your first ninety days leading the Canadian division &mdash; the difference between arriving as a stranger and arriving as a listener.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l12">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On her last day in the role, Gordon left Danielle a voice note about the one thing the <strong>handover</strong> document could not carry. He <strong>admitted that</strong> he had restructured the academic team in his first month, and he <strong>told her that</strong> he had been wrong about almost all of it &mdash; because he had changed the answer before he understood the question. His advice was the opposite of his instinct: he <strong>urged her to</strong> decide nothing for ninety days and to spend the <strong>ramp-up period</strong> on a <strong>listening tour</strong> instead.</p>
        <p style="margin-top:.8rem">So she did. Over eleven weeks she sat with the <strong>frontline staff</strong>, not just the directors, and asked what was genuinely broken. One coordinator <strong>explained that</strong> the last three reorganizations <strong>had</strong> each been announced as urgent and then quietly reversed, so the team had learned to wait out any new plan. Another <strong>admitted that</strong> morale was low, but <strong>insisted that</strong> the cause was not the workload &mdash; it was that nobody in head office had ever asked them anything before deciding. A regional director <strong>warned her not to</strong> mistake their politeness for agreement, and <strong>pointed out that</strong> a Canadian team will rarely say no to your face.</p>
        <p style="margin-top:.8rem">None of this could have reached her except from one <strong>vantage point</strong> &mdash; the classroom floor. The temptation the whole time was to act, because a <strong>mandate</strong> feels like something you are supposed to spend, and every week she did not restructure anything felt like wasted authority. But <strong>credibility</strong>, she was learning, is not spent with the title. It is earned in the first quarter, one honest conversation at a time.</p>
        <p style="margin-top:.8rem">By day eighty-nine she had a smaller, sharper plan than the one she would have written on day one. She had learned to <strong>lean on</strong> Gordon, whose early mistakes were now her shortcuts, and to <strong>size up</strong> a culture before trying to move it. Her <strong>entry plan</strong> had three phases &mdash; learn, decide, act &mdash; and she was still, deliberately, in the first. When a stakeholder asked why she had not fixed anything yet, she no longer heard a threat. She heard her cue to say, plainly, that she was still listening, on purpose, and that the listening was the work.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Gordon &ldquo;<strong>told her that</strong> he had been wrong&rdquo; &mdash; why <em>told her</em> and not <em>said her</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because <strong>tell</strong> takes a person object (tell <em>someone</em>), while <strong>say</strong> does not: you <em>tell her that...</em> but you <em>say that...</em> (or <em>say to her</em>).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because &ldquo;said&rdquo; cannot be used in the past tense at all.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;told&rdquo; is only correct when the sentence is a question.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. The coordinator &ldquo;explained that the reorganizations <strong>had</strong> been reversed&rdquo;. Why <em>had been</em> and not <em>were</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because &ldquo;reorganizations&rdquo; is plural, which forces the past perfect.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because reported speech <strong>backshifts</strong> one step: an event already past at the moment of speaking moves from <em>were reversed</em> to <em>had been reversed</em>.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the passive voice always requires &ldquo;had&rdquo; in English.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Why is &ldquo;He <strong>admitted that</strong> he had been wrong&rdquo; stronger, in a debrief, than &ldquo;He said that he had been wrong&rdquo;?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because &ldquo;admitted&rdquo; is more formal and formality is always better.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the reporting verb <strong>names how it was said</strong>: <em>admit</em> tells you he conceded a fault, which <em>say</em> would leave out. Choosing the verb is choosing the meaning.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;said&rdquo; is grammatically incorrect before &ldquo;that&rdquo;.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. According to the text, how is credibility earned in a new senior role?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It arrives automatically with the title and the mandate.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> By changing something visible in the first two weeks to look decisive.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> In the first quarter, one honest conversation at a time &mdash; by listening before acting, not by spending the mandate fast.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reported Speech &amp; Reporting Verbs</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The grammar of the leader who relays what a room told her &mdash; precisely, and without turning someone else's words into her own claim. In a listening tour, reporting well IS the work.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Backshift<br>verb + <strong>that</strong> + clause, one tense back</td><td style="padding:.6rem">Reporting a past moment, each tense steps back: <em>is</em>&rarr;<em>was</em>, <em>was</em>&rarr;<em>had been</em>.</td><td style="padding:.6rem">&ldquo;Morale is low&rdquo; &rarr; She said that morale <strong>was</strong> low. &middot; &ldquo;It was reversed&rdquo; &rarr; He explained it <strong>had been</strong> reversed.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Say vs tell</td><td style="padding:.6rem"><strong>tell</strong> takes a person (tell <em>me</em>); <strong>say</strong> does not (say <em>that</em>).</td><td style="padding:.6rem">He <strong>told me</strong> that... &middot; He <strong>said</strong> that... &middot; NOT &ldquo;he said me&rdquo;.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Verb + object + <strong>to</strong>-infinitive</td><td style="padding:.6rem">urge / advise / warn / ask / tell + someone + <strong>to</strong> + base verb. Negative: <strong>not to</strong>.</td><td style="padding:.6rem">He <strong>urged me to</strong> slow down. &middot; He <strong>warned me not to</strong> restructure.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Verb + <strong>-ing</strong> / that</td><td style="padding:.6rem"><strong>suggest / recommend</strong> take a gerund or a <em>that</em>-clause &mdash; never <em>to</em> + verb.</td><td style="padding:.6rem">She <strong>recommended waiting</strong>. &middot; She <strong>suggested that I wait</strong>. &middot; NOT &ldquo;recommended to wait&rdquo;.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Choose the reporting verb</td><td style="padding:.6rem" colspan="2"><strong>admit</strong> (concede a fault) &middot; <strong>insist</strong> (hold firm) &middot; <strong>point out</strong> (note a fact) &middot; <strong>warn</strong> (flag a risk) &middot; <strong>deny</strong> (reject) &middot; <strong>explain</strong> (give the reason). The verb carries the attitude that <em>say</em> leaves out.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it sounds senior</td><td style="padding:.6rem" colspan="2">Relaying a listening tour with the right reporting verbs shows you heard people precisely, without turning their words into your own verdict. &ldquo;A director <strong>warned me not to</strong> mistake politeness for agreement&rdquo; is exact and attributed; &ldquo;they all agree&rdquo; is your assumption &mdash; and the wrong one.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (the number one slip):</strong> <strong>say</strong> takes no person and <strong>tell</strong> requires one. &ldquo;He <em>said me</em>&rdquo; &rarr; &ldquo;He <strong>told me</strong>&rdquo; or &ldquo;He <strong>said</strong> that&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (the other slip):</strong> after <strong>recommend / suggest</strong> comes the <strong>-ing</strong> form or a <em>that</em>-clause, never <em>to</em>. &ldquo;recommended <em>to wait</em>&rdquo; &rarr; &ldquo;recommended <strong>waiting</strong>&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>The line that wins the room:</strong> the precise reporting verb plus a clean backshift. &ldquo;One coordinator <strong>explained that</strong> the reorganizations <strong>had</strong> all been reversed, so the team learned to wait &mdash; and another <strong>insisted that</strong> the real problem was never being asked.&rdquo;</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the First 90 Days in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order a new leader runs the first quarter &mdash; listen first, decide last.</p>
      <div class="order-container" id="order-l12">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Report back precisely what people said, using reported speech, without inventing a verdict of your own.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">On day ninety, present a smaller, sharper plan built on what you heard, not on what you assumed on day one.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Build a simple entry plan with three phases &mdash; learn, decide, act &mdash; and commit to staying in phase one.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Earn credibility before spending the mandate &mdash; resist changing anything visible just to look decisive.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Run a listening tour with the frontline staff, not just the directors, and ask what you must not touch.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l12')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are sentences you will actually use when you brief the board on your first quarter.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment in your first ninety days leading the Canadian division.</p>
      <div class="quiz-item"><div class="quiz-question">A stakeholder says: &ldquo;You have been here six weeks and changed nothing. When do you start leading?&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;You are right &mdash; I will announce a restructure this week so you can see progress.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I am leading. I am on a listening tour by design, not by hesitation &mdash; I told the team I would decide nothing for ninety days, and keeping that is the first decision.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I am not sure yet. Maybe I will change something soon, maybe not.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The board asks you to relay what the frontline staff told you. Which is the precise report?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;One coordinator explained that past reorganizations had all been reversed, and another admitted that morale was low but insisted the cause was never being asked.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Basically they all agree the place is a mess and want me to fix it fast.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;They said me that everything was fine, more or less.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses reported speech correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Gordon said me that he restructured too fast.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Ruth recommended to wait until the tour was finished.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;Gordon told me that he had restructured too fast, and Ruth recommended waiting until the tour was finished.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The Canadian team is unfailingly polite and agrees with everything. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Take the agreement at face value and move fast &mdash; they clearly support the plan.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Remember that a director warned you not to mistake politeness for agreement, and read the room from their vantage point &mdash; they will rarely say no to your face.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Assume the silence means resistance and cancel the plan entirely.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You have a huge mandate on day one. The strongest use of it is to:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Spend it immediately on the biggest visible change, before anyone questions your authority.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Hold it while you earn credibility one conversation at a time &mdash; a mandate spent before you understand the question buys the wrong change.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Hand it back to Gordon and ask him to keep running the division.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">You are briefing the board at the end of your first ninety days leading the Canadian division. In two minutes: describe your entry plan and your listening tour, then relay what three different people told you &mdash; use reported speech with three different reporting verbs (explained that... / admitted that... / warned me not to...) and a clean backshift. Use at least six words from this lesson, and end with the one thing you will do first, now that you have earned the credibility to do it.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-12"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 12</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-11 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-11'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
