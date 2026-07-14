#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 5 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 5 IN CLASS (mesmo tema/gramática/vocab — cleft sentences).
"""
import os
import random

random.seed(5)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Track record", "a documented history of results you can point to, with dates and numbers", "histórico comprovado",
     "\"I can demonstrate a track record of delivering signaling packages on time.\""),
    ("Cross-functional", "involving people from different departments and disciplines at the same time", "multidisciplinar, entre áreas",
     "\"I lead cross-functional teams: signaling, civil works and the client.\""),
    ("High-stakes", "where the consequences of getting it wrong are serious and public", "de alto risco, com muito em jogo",
     "\"Signaling is a high-stakes discipline: the failure mode is a collision.\""),
    ("Resilience", "the ability to keep performing when the pressure does not stop", "resiliência",
     "\"What that year taught me was resilience, not patience.\""),
    ("Stakeholder management", "keeping everyone with an interest in the project informed, aligned and calm", "gestão de partes interessadas",
     "\"Stakeholder management is half the job: the client, the supplier and the regulator.\""),
    ("Value proposition", "the one concrete reason to choose you instead of the other candidate", "proposta de valor",
     "\"My value proposition is simple: I read the standard and I run the site.\""),
    ("Technical lead", "the engineer who owns the technical decisions on a project, and answers for them", "líder técnico",
     "\"I was the technical lead on the Line 5 signaling package.\""),
    ("Subject matter expert", "the person the team goes to when the answer is not in the manual", "especialista no assunto",
     "\"On interlocking logic, I am the subject matter expert for my team.\""),
    ("Performance-driven", "working against a number: a metric, a KPI, a measurable target", "orientado por desempenho",
     "\"It is a performance-driven environment: every milestone has an indicator.\""),
    ("Results-oriented", "asking to be judged by what you delivered, not by how busy you looked", "orientado a resultados",
     "\"I am results-oriented: judge me by the commissioning date, not by my hours.\""),
    ("To set out", "to explain your background clearly and in order, so the listener can follow it", "expor, apresentar em ordem",
     "\"Let me set out my experience in three steps.\""),
    ("To account for", "to explain a decision or a period that somebody is entitled to ask about", "justificar, explicar",
     "\"I can account for the two years when I stopped using English.\""),
    ("To burn the midnight oil", "to work late into the night to finish something that matters (informal)", "virar a noite trabalhando",
     "\"We burned the midnight oil for a week before the factory acceptance test.\""),
    ("To throw in the towel", "to give up when it gets hard -- the thing you say you did NOT do (informal)", "jogar a toalha, desistir",
     "\"That interview went badly, but I did not throw in the towel.\""),
]

SURVIVAL = [
    ("Let me set out my background in three steps.",
     "Deixe-me expor a minha trajetória em três etapas."),
    ("What I bring to this role is seven years of managing international suppliers.",
     "O que eu trago para esta posição são sete anos gerenciando fornecedores internacionais."),
    ("What sets me apart is that I read the standard and I run the site.",
     "O que me diferencia é que eu leio a norma e eu conduzo o campo."),
    ("One example that comes to mind is a supplier who missed three consecutive deadlines.",
     "Um exemplo que me vem à mente é um fornecedor que perdeu três prazos consecutivos."),
    ("I can account for it, and what I learned was that fluency is a habit, not a memory.",
     "Eu consigo explicar isso, e o que eu aprendi foi que fluência é um hábito, não uma lembrança."),
]


def esc(s):
    """ASCII-safe: acentos e aspas viram entidades HTML."""
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        else:
            out.append(f'&#{ord(ch)};')
    return ''.join(out)


def vocab_cards():
    rows = []
    for word, d, pt, ex in VOCAB:
        rows.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{esc(word)}</span>'
            f'<span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{esc(d)}</span></div>'
            f'<div class="vocab-card-example">{esc(ex)}</div></div>'
            f'<button class="audio-btn" data-speak="{esc(word)}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
    return '\n'.join(rows)


def match_grid():
    defs = [d for _, d, _, _ in VOCAB]
    rows = []
    for word, d, _, _ in VOCAB:
        opts = defs[:]
        while True:
            random.shuffle(opts)
            if opts != defs:
                break
        o = ''.join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in opts)
        rows.append(
            f'        <div class="match-row" data-answer="{esc(d)}">'
            f'<span class="match-word" style="flex:0 0 190px">{esc(word)}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{o}</select></div>')
    return '\n'.join(rows)


CONTEXT = """<p>It is four o'clock on a Tuesday and Jo&#227;o Guilherme is sitting in front of a panel of two. Sofie Claes, Head of Signaling Engineering, has twenty minutes and a shortlist of five engineers, all of them with seven years of experience. Experience is time, and everybody on that list has it. <strong>What wins the room is</strong> a <strong>track record</strong>: a project, a decision, an outcome.</p>
        <p>He opens carefully. "Let me <strong>set out</strong> my background in three steps. <strong>What I do</strong> at Motiva <strong>is</strong> own the signaling design for metro line extensions, from the specification to commissioning. <strong>What I bring to this role is</strong> seven years of managing German, French and Chinese suppliers under contractual pressure." Sofie is not impressed yet. She asks the question that decides everything: what makes him the right person, and not the other four? "<strong>What sets me apart is</strong> that I read the standard and I run the site. Most engineers do one or the other. <strong>It was in San Francisco, in 2023, that</strong> I did both on the same project." That is a <strong>value proposition</strong>, and it takes one sentence.</p>
        <p>Then comes the uncomfortable question, the one he did not prepare in March: there was a period when he was not using English. He does not apologize. He <strong>accounts for</strong> it. "<strong>What I learned from that experience was</strong> that fluency is a habit, not a memory. <strong>It was an interview, in March, that</strong> made me rebuild the habit." He did not <strong>throw in the towel</strong>, and the word for that, in an interview, is <strong>resilience</strong>. <strong>Stakeholder management</strong>, a <strong>cross-functional</strong> team, a <strong>high-stakes</strong> discipline where the failure mode is a collision: the engineering was always there. Tonight, so was the English."""

QUIZZES_CONTEXT = [
    ("1. \"What I bring to this role is seven years in signaling.\" Why is the verb <em>is</em>, and not <em>are</em>, if \"seven years\" is plural?",
     [("Because <em>What...</em> works like \"the thing that\" &mdash; a SINGULAR subject. The verb agrees with it, never with what follows.", True),
      ("Because English drops subject-verb agreement after <em>what</em>.", False),
      ("Because \"seven years\" is treated like an amount of money, so it turns singular.", False)]),
    ("2. \"It was in San Francisco that I ran my first commissioning cycle.\" What does this structure DO to the sentence?",
     [("It adds a new piece of information about San Francisco.", False),
      ("It puts ONE fact under the spotlight &mdash; the place &mdash; and tells the panel where to look. The information is the same; the weight is not.", True),
      ("It makes the sentence more formal, but the effect is purely decorative.", False)]),
    ("3. Why does \"What I bring to this role is seven years...\" work better in an interview than \"I have seven years of experience\"?",
     [("Because it is longer, and long sentences sound more professional.", False),
      ("Because it announces that something important is coming, saves the decisive information for the END &mdash; and buys you half a second to think.", True),
      ("Because it avoids the verb <em>have</em>, which is far too informal.", False)]),
    ("4. Which sentence is correct?",
     [("\"It was in San Francisco where I ran my first commissioning cycle.\"", False),
      ("\"What I bring to this role, it is deep expertise in signaling.\"", False),
      ("\"It was in San Francisco that I ran my first commissioning cycle.\"", True)]),
]

BLANKS = [
    ("What I bring to this role is", "Hint: wh-cleft &mdash; announce first, deliver second. The verb is <em>is</em>, singular",
     "What I bring to this role is seven years in railway signaling.",
     '"', ' seven years in railway signaling."'),
    ("It was in San Francisco that", "Hint: it-cleft &mdash; the spotlight falls on the PLACE. And the word is <em>that</em>, never <em>where</em>",
     "It was in San Francisco that I ran my first full commissioning cycle.",
     '"', ' I ran my first full commissioning cycle."'),
    ("What sets me apart is", "Hint: your value proposition in a single line",
     "What sets me apart is that I read the standard and I run the site.",
     '"', ' that I read the standard and I run the site."'),
    ("account for", "Hint: to explain a period or a decision &mdash; and the preposition is FOR",
     "I can account for the two years when I stopped using English.",
     '"I can ', ' the two years when I stopped using English."'),
    ("set out", "Hint: to lay out your background clearly and in order",
     "Let me set out my background in three steps.",
     '"Let me ', ' my background in three steps."'),
    ("track record", "Hint: it is not length of service &mdash; it is the evidence: a project, a decision, an outcome",
     "I can demonstrate a track record of delivering signaling packages on time.",
     '"I can demonstrate a ', ' of delivering signaling packages on time."'),
]

ORDER = [
    (1, "Set out your background in three steps, starting from the value and not from the biography."),
    (2, "State your value proposition in one cleft sentence: what sets you apart from the other candidates."),
    (3, "Prove it with a track record: one project, the decision you took, and the outcome."),
    (4, "Account for the uncomfortable question with evidence, not with an apology."),
    (5, "Close by asking the panel a question only an engineer would ask."),
]

SPEECH = [
    ("Let me set out my background in three steps.",
     "Deixe-me expor a minha trajetória em três etapas."),
    ("What I bring to this role is seven years of managing international suppliers.",
     "O que eu trago para esta posição são sete anos gerenciando fornecedores internacionais."),
    ("What sets me apart is that I read the standard and I run the site.",
     "O que me diferencia é que eu leio a norma e eu conduzo o campo."),
    ("It was in San Francisco, in 2023, that I ran my first full commissioning cycle.",
     "Foi em São Francisco, em 2023, que eu conduzi o meu primeiro ciclo completo de comissionamento."),
    ("I can account for it, and what I learned was that fluency is a habit, not a memory.",
     "Eu consigo explicar isso, e o que eu aprendi foi que fluência é um hábito, não uma lembrança."),
]

QUIZZES_SIT = [
    ("The panel opens with \"Tell me about yourself.\" You have ninety seconds. You start with:",
     [("\"I was born in S&#227;o Paulo and I studied electrical engineering...\"", False),
      ("\"Let me set out my background in three steps. What I do at Motiva is own the signaling design for metro line extensions.\"", True),
      ("\"Well, it is difficult to summarize seven years, but I will try.\"", False)]),
    ("\"Everyone on this shortlist has seven years. What makes you the right person?\" You answer:",
     [("\"What sets me apart is that I read the standard and I run the site. Most engineers do one or the other.\"", True),
      ("\"I am very dedicated and I always give my best.\"", False),
      ("\"I think my experience speaks for itself.\"", False)]),
    ("She asks for a conflict with an international supplier. The strongest opening is:",
     [("\"Suppliers are always late, it happens on every project.\"", False),
      ("\"One example that comes to mind is a supplier who missed three consecutive deadlines. What I did was put forward a recovery plan before anyone mentioned the penalty clause.\"", True),
      ("\"I would have to think about that one for a moment.\"", False)]),
    ("\"You were not using English intensively for a while. How do I know that will not be a problem?\" You answer:",
     [("\"I am sorry about my English, I know it is not perfect.\"", False),
      ("\"My English is fine, it was only a bad day in that interview.\"", False),
      ("\"I can account for it. What I learned from that period was that fluency is a habit, not a memory &mdash; and I have been in weekly training since March.\"", True)]),
    ("The technical director asks how you handle competing priorities. He wants ONE sentence, not three minutes. You say:",
     [("\"The way I approach this kind of challenge is to ask which item is on the critical path for safety approval.\"", True),
      ("\"It depends. Let me explain the relay logic first, and then the interlocking table, and then...\"", False),
      ("\"I work hard and I burn the midnight oil until everything is done.\"", False)]),
]


def quiz_html(items, start=1):
    out = []
    for i, (q, opts) in enumerate(items):
        qq = q if q[0].isdigit() else f'{q}'
        o = []
        for j, (text, correct) in enumerate(opts):
            letter = 'ABC'[j]
            o.append(
                f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}">'
                f'<span class="option-letter">{letter}</span> {text}</div>')
        out.append(
            f'      <div class="quiz-item"><div class="quiz-question">{qq}</div>'
            f'<div class="quiz-options">{"".join(o)}</div></div>')
    return '\n'.join(out)


def blanks_html():
    out = []
    for ans, hint, phrase, pre, post in BLANKS:
        out.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{esc(pre)}'
            f'<input class="blank-input" data-answer="{esc(ans)}" data-hint="{hint}" '
            f'data-phrase="{esc(phrase)}" placeholder="___">{esc(post)}</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    return '\n'.join(out)


def order_html():
    items = ORDER[:]
    random.shuffle(items)
    out = []
    for n, text in items:
        out.append(
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
    return '\n'.join(out)


def speech_html():
    out = []
    for en, pt in SPEECH:
        out.append(
            f'      <div class="speech-card" data-phrase="{esc(en)}">\n'
            f'        <div class="speech-phrase">{esc(en)}</div>\n'
            f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
            f'        <div class="speech-result"></div>\n'
            f'      </div>')
    return '\n'.join(out)


def survival_html():
    out = []
    for i, (en, pt) in enumerate(SURVIVAL, 1):
        out.append(
            f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
            f'<span class="sp-en">{esc(en)}</span>'
            f'<button class="btn btn-listen" data-speak="{esc(en)}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
    return '\n'.join(out)


GRAMMAR_TIP = """      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">wh-cleft<br><strong>What</strong> + subject + verb + <strong>is</strong> + the point</td><td style="padding:.6rem">You ANNOUNCE that something important is coming, and only then deliver it. The panel leans forward. The listener knows a headline is on its way.</td><td style="padding:.6rem">"<strong>What I bring to this role is</strong> seven years in signaling."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">it-cleft<br><strong>It was</strong> + the fact + <strong>that</strong> + the rest</td><td style="padding:.6rem">You put ONE fact under the spotlight: a place, a date, a person, a decision. The linking word is always <strong>that</strong> &mdash; never <em>where</em>, never <em>when</em>.</td><td style="padding:.6rem">"<strong>It was in San Francisco that</strong> I ran my first commissioning cycle."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>The reason</strong> + clause + <strong>is that</strong></td><td style="padding:.6rem">You take control of the story behind a decision before anybody reads it the wrong way.</td><td style="padding:.6rem">"<strong>The reason I moved into signaling is that</strong> safety is non-negotiable."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Agreement</td><td style="padding:.6rem">After <em>What...</em>, the verb is ALWAYS <strong>is</strong> / <strong>was</strong>, even in front of a plural &mdash; because <em>What</em> means "the thing that", a singular subject.</td><td style="padding:.6rem">"What I bring <strong>is</strong> seven years." (never <em>are</em>)</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Question / negative</td><td style="padding:.6rem">It behaves the same way: <strong>What</strong> he wants <strong>is</strong> a date. / <strong>What I do not do is</strong> promise dates I cannot defend.</td><td style="padding:.6rem">"<strong>What I do not do is</strong> promise a date I cannot defend."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">In speech</td><td style="padding:.6rem">The pause falls right BEFORE the <em>is</em>. That pause is thinking time &mdash; and it belongs to you.</td><td style="padding:.6rem">"What I learned from that experience &#8230; <strong>was</strong> that fluency is a habit."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Why it matters</td><td style="padding:.6rem" colspan="2">Under pressure, a nervous candidate dumps everything he knows into one long sentence &mdash; and the panel stops listening. A cleft sentence does the opposite: it tells the panel <strong>where to look</strong>. Same information, completely different candidate.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (two classic mistakes):</strong> (1) the repeated pronoun &mdash; the subject pronoun does NOT come back after the cleft: "What I bring to this role <em>it is</em>..." is wrong; the correct form is "What I bring to this role <strong>is</strong>..."; (2) the <em>where</em> &mdash; the English it-cleft demands <strong>that</strong>, even when you are pointing at a place: "It was in San Francisco <strong>that</strong> I ran my first commissioning cycle."</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>The four interview patterns:</strong> "<strong>One example that comes to mind is...</strong>" (the behavioral question), "<strong>What I learned from that experience was...</strong>" (the closing line of any story), "<strong>The way I approach this kind of challenge is...</strong>" (the method question) and "<strong>I would say my greatest strength in this area is...</strong>" (the direct question). Four skeletons: all you change is the filling."""


HTML = f"""<div class="lesson-card" id="ex-lesson-5">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1553773077-91673524aafa?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 05 -- Pre-class</div>
      <h3>Performing Under Pressure -- The International Job Interview</h3>
      <div class="lesson-desc">The international interview: how to turn seven years of experience into EVIDENCE, control what the panel hears first, and answer the uncomfortable question without apologizing. Key words: track record, cross-functional, high-stakes, resilience, stakeholder management, value proposition, technical lead, subject matter expert, performance-driven, results-oriented, to set out, to account for, to burn the midnight oil, to throw in the towel. Structure: cleft sentences ("What I bring to this role is...", "It was in San Francisco that...", "The reason I... is that...") + the four interview answer patterns.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Lessons 2 to 4 gave a name to the work: the actions, the inspection, the contract. This one gives a name to YOU &mdash; the words an interview panel is waiting to hear. You have already DONE all of this at Motiva; what is missing is the English label. Listen to each term and read the example.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l5">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions below.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Cleft Sentences</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to split a sentence in two so that you control what the panel hears first &mdash; and buy yourself half a second to think.</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct structure. Tap Listen to hear the whole sentence.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Interview in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the stages of an international interview answer in the right order.</p>
      <div class="order-container" id="order-l5">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l5')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that open, carry and close any interview. Notice the pause that falls right BEFORE the <em>is</em> &mdash; it belongs to you, and it is thinking time.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the strongest answer for each real moment of an international interview &mdash; including the uncomfortable question about your English.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. Speak for 2 minutes, with no script and without stopping to correct yourself. Tone: professional, confident, straight to the value.</p>
      <div class="think-card">
        <div class="think-question">"Tell me about yourself." You have ninety seconds with an international panel. Set out your background in three steps (Let me set out...), say what you bring to the role (What I bring to this role is...), prove it with one project (It was in San Francisco, in 2023, that...), state what makes you different from the other candidates (What sets me apart is...), and finish by accounting for the period when your English went quiet (I can account for it. What I learned from that experience was...).</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-5"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 5</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
