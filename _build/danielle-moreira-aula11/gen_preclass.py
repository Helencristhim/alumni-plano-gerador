#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 11 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..10
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 11 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).

GRAMATICA DA AULA 11 (nova; nao repete a1..a10):
  past perfect + past perfect continuous
  By the time + past simple, + past perfect (had + pp) ·
  had been + -ing (duracao ate um ponto no passado) ·
  had + pp + before/when (o "antes do antes") · already/never/just + past perfect.
  A tese: a virada e uma SEQUENCIA. O simple past conta O QUE aconteceu; o past
  perfect prova que foi um TRABALHO e nao sorte -- porque mostra a ORDEM (a causa
  antes do efeito).

  (O curriculo pedia "Diagnosing Culture" -- que REPETE a aula 6, ja ensinada
   [cultural assessment, focus group, response rate...]. Trocado por "The Turnaround
   Story", tema INEDITO que casa com a gramatica planejada [past perfect] e com o
   evento-alvo real da aluna: narrar ao board a virada do Brasil como base p/ o Canada.)
"""
import re
import random

random.seed(11)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Legacy", "what an earlier situation or leader leaves behind for you to deal with, good or bad",
     "legado / heran&#231;a",
     "The disengagement was not something I created; it was the legacy I inherited on my first day."),
    ("Groundwork", "the unglamorous preparation you do before anything visible can happen",
     "trabalho de base / alicerce",
     "By the time the numbers moved, the groundwork had already been in place for two quarters, and it was the only reason the turnaround held."),
    ("Tipping point", "the moment a slow change suddenly becomes visible and hard to reverse",
     "ponto de virada",
     "The resignation was the tipping point: after it, the culture problem could no longer be treated as a rumor."),
    ("Precedent", "an earlier case that sets the pattern for how the next one is judged",
     "precedente",
     "There was no precedent for a culture role in that office, so the first year was about proving the function should exist at all."),
    ("Turnaround", "the point at which a declining situation reverses and starts to recover",
     "reviravolta / recupera&#231;&#227;o",
     "The board wants to know whether the turnaround was leadership or luck, and the answer is in the sequence, not in the final number."),
    ("Entrenched", "so deeply established that it resists any attempt to change it",
     "enraizado / arraigado",
     "The pattern was entrenched: it had been building for two years before anyone was willing to name it."),
    ("Status quo", "the existing state of things, especially the one people quietly prefer not to disturb",
     "status quo / o estado atual das coisas",
     "Every turnaround is a fight with the status quo, and the status quo always had a head start."),
    ("In hindsight", "seeing clearly, after the fact, what was not obvious at the time",
     "em retrospecto / olhando para tr&#225;s",
     "In hindsight, I should have set the baseline earlier, before the culture had already deteriorated."),
    ("Wake-up call", "a shock that finally forces people to face a problem they had been ignoring",
     "alerta / sinal de alarme",
     "Her exit interview was the wake-up call the leadership team had been avoiding for a year."),
    ("Uphill battle", "a struggle that is hard the whole way because everything is working against you",
     "batalha &#225;rdua / luta dif&#237;cil",
     "Changing an entrenched culture is an uphill battle, and the first months move nothing you can measure."),
    ("To inherit", "to take over a situation, a team or a problem that somebody else created",
     "herdar (uma situa&#231;&#227;o / um time)",
     "I did not build that crisis. I inherited it, and then I gave it a name nobody had dared to use."),
    ("To trace back to", "to follow a problem to its true origin, however far back that is",
     "rastrear at&#233; / remontar a",
     "The attrition traced back to onboarding, a decision made two years before the resignations started."),
    ("To come to a head", "(of a building problem) to reach the point where it can no longer be ignored",
     "chegar a um ponto cr&#237;tico / estourar",
     "The tension had been growing for months, and it came to a head the week our most senior teacher resigned."),
    ("To gain momentum", "to start moving faster and become harder to stop, once it has begun",
     "ganhar tra&#231;&#227;o / impulso",
     "Once the new onboarding gained momentum, engagement climbed on its own, and my job became protecting it."),
    ("To reverse a trend", "to turn a line that was going the wrong way and make it go the right way",
     "reverter uma tend&#234;ncia",
     "We did not just slow the decline; we reversed the trend, and the exit interviews changed from warnings to thank-you notes."),
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

# ---------- Stage 1.5 fill-in-the-blank (4 estruturas de past perfect + 2 collocations) ----------
# (pre, resposta, hint, frase completa (audio), post) -- espacamento EXPLICITO em pre/post
BLANKS = [
    ("By the time the board reviewed the numbers, attrition ", "had already fallen",
     "Hint: past perfect for the event COMPLETED before another past moment. had + past participle (NOT &ldquo;already fell&rdquo;)",
     "By the time the board reviewed the numbers, attrition had already fallen for two quarters.",
     " for two quarters."),
    ("When I inherited the team, engagement ", "had been dropping",
     "Hint: past perfect CONTINUOUS for an action in progress up to a past point. had been + -ing (NOT &ldquo;had been dropped&rdquo;, NOT &ldquo;was dropping&rdquo;)",
     "When I inherited the team, engagement had been dropping for eighteen months.",
     " for eighteen months."),
    ("The problem ", "traced back to",
     "Hint: to follow a problem to its origin. trace back TO (never &ldquo;trace back at&rdquo;)",
     "The problem traced back to onboarding, a decision made two years earlier.",
     " onboarding, a decision made two years earlier."),
    ("Long before the results appeared, I ", "had rebuilt",
     "Hint: everything you BUILT goes in the past perfect, completed BEFORE the simple-past result. had + past participle",
     "Long before the results appeared, I had rebuilt onboarding and set up a quarterly pulse survey.",
     " onboarding and set up a quarterly pulse survey."),
    ("The tension ", "had been building",
     "Hint: past perfect continuous &mdash; had been + -ing &mdash; it stresses the DURATION before it came to a head",
     "The tension had been building for months before it came to a head.",
     " for months before it came to a head."),
    ("Once the new onboarding ", "gained momentum",
     "Hint: collocation. to GAIN momentum (never &ldquo;win momentum&rdquo;). It means it started moving on its own",
     "Once the new onboarding gained momentum, engagement climbed on its own.",
     ", engagement climbed on its own."),
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
    ("For two years before I arrived, attrition had been climbing, and nobody had yet traced it back to onboarding.",
     "Por dois anos antes de eu chegar, a rotatividade vinha subindo, e ningu&#233;m ainda a havia rastreado at&#233; o onboarding."),
    ("By the time the results appeared, the groundwork had already been in place for two quarters.",
     "Quando os resultados apareceram, o trabalho de base j&#225; estava montado havia dois trimestres."),
    ("The tension had been building for months, and it came to a head the week our most senior teacher resigned.",
     "A tens&#227;o vinha se acumulando havia meses, e estourou na semana em que nossa professora mais s&#234;nior pediu demiss&#227;o."),
    ("We did not just slow the decline. We reversed the trend, and the exit interviews became thank-you notes.",
     "N&#243;s n&#227;o apenas desaceleramos a queda. Revertemos a tend&#234;ncia, e as entrevistas de desligamento viraram bilhetes de agradecimento."),
    ("In hindsight, the turnaround was a sequence, not an accident, and the sequence is what I am bringing to Canada.",
     "Em retrospecto, a virada foi uma sequ&#234;ncia, n&#227;o um acaso, e &#233; a sequ&#234;ncia que estou levando ao Canad&#225;."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-11">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 11 -- Pre-class</div>
      <h3>The Turnaround Story -- Narrating What Had Already Changed</h3>
      <div class="lesson-desc">Telling the board the turnaround you led in Brazil &mdash; and proving it was a build, not luck. The tool is the past perfect: it lets you narrate the SEQUENCE, so your action lands against a problem that was already there and your results arrive AFTER the groundwork was already laid. Key words: legacy, groundwork, tipping point, precedent, turnaround, entrenched, status quo, in hindsight, wake-up call, uphill battle, to inherit, to trace back to, to come to a head, to gain momentum, to reverse a trend. Structure: past perfect (had + past participle) and past perfect continuous (had been + -ing) &mdash; By the time..., had already... &middot; had been climbing for two years &middot; had traced back to onboarding before anyone named it. The simple past says WHAT happened; the past perfect proves it was a sequence, and the sequence is the proof.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="11" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="11">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the vocabulary of someone who narrates a recovery and makes the board believe she caused it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l11">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Renata Alencar lost the room in the first minute, and she lost it by telling the truth in the wrong order. She had led a genuine <strong>turnaround</strong> in her last company &mdash; attrition halved, engagement recovered, a toxic pattern broken &mdash; and when the new board asked her to walk them through it, she said: &ldquo;I joined, I redesigned onboarding, and within a year the numbers turned around.&rdquo; Every word was true. It also sounded exactly like luck. Three events in a line, no cause between them, and a chair who had funded that story before and watched it die in a second country.</p>
        <p style="margin-top:.8rem">There is a way to tell the same three facts that proves the opposite, and it is not charisma &mdash; it is a tense. <strong>By the time she was even asked to fix it</strong>, the attrition <strong>had been climbing</strong> for two years, and nobody <strong>had traced</strong> it <strong>back to</strong> onboarding yet. That is the <strong>legacy</strong> she <strong>inherited</strong>; she did not create the crisis, she named it. Long before the numbers moved, she <strong>had rebuilt</strong> the onboarding, she <strong>had set up</strong> a quarterly pulse survey, and she <strong>had trained</strong> the leads on psychological safety. So when the most senior teacher resigned and the whole thing <strong>came to a head</strong>, the <strong>groundwork had already been in place</strong> for two quarters. The <strong>wake-up call</strong> did not catch her unprepared. It caught her ready.</p>
        <p style="margin-top:.8rem">Notice what the past perfect is actually doing, because it does the same job every time. It puts what was <em>already there</em> &mdash; the failing, the building, the preparing &mdash; <em>before</em> the simple-past event that everyone can see. &ldquo;I redesigned onboarding and engagement rose&rdquo; is two events that might be a coincidence. &ldquo;I <strong>had</strong> redesigned onboarding <em>before</em> engagement rose&rdquo; is a cause and an effect, in that order, and the order is the whole argument. The <strong>status quo</strong> was <strong>entrenched</strong> and it <strong>had</strong> a head start; changing it was an <strong>uphill battle</strong>; and the only way to prove you won it on purpose is to show the sequence &mdash; what <strong>had been</strong> failing, what you <strong>had</strong> built, and only then, what finally moved.</p>
        <p style="margin-top:.8rem"><strong>In hindsight</strong>, Renata said afterwards, the mistake was never the data. It was that she had handed the board a list when she should have handed them a timeline. A turnaround told in the simple past is a series of happy accidents. The same turnaround told with the past perfect underneath it is a method &mdash; and a method is the only thing that survives the trip to a country where you have not lived the culture yet, and where the <strong>groundwork</strong> will have to be laid again, from the very beginning.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does &ldquo;I <strong>had</strong> redesigned onboarding <em>before</em> engagement rose&rdquo; prove more than &ldquo;I redesigned onboarding and engagement rose&rdquo;?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It does not prove more &mdash; the two sentences carry the same information, so they make the same claim.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the past perfect fixes the ORDER: the cause (your action) is completed BEFORE the effect (the result). Two simple-past events side by side could be a coincidence; a past perfect before a simple past is a claim about cause.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the past perfect makes the sentence more polite and less arrogant.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. The number one mistake of this lesson: why is &ldquo;By the time the board met, we <em>already lost</em> thirty teachers&rdquo; wrong?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because an event completed BEFORE another past moment needs the past perfect: &ldquo;we <strong>had</strong> already <strong>lost</strong> thirty teachers&rdquo;. &ldquo;By the time&rdquo; is the classic trigger, and the simple past drops the sequence the whole story depends on.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because &ldquo;by the time&rdquo; can only be followed by the present tense.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;lost&rdquo; should be &ldquo;loosed&rdquo; in this context.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. And mistake number two: why is &ldquo;engagement <em>had been dropped</em> for eighteen months&rdquo; wrong?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because past perfect continuous does not exist in American English.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the correct form is &ldquo;engagement was dropped for eighteen months&rdquo;.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Because &ldquo;had been dropped&rdquo; is a PASSIVE (somebody dropped it). For an action in progress over time you need the past perfect CONTINUOUS: &ldquo;engagement <strong>had been dropping</strong> for eighteen months&rdquo; &mdash; had been + -ing.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. According to the text, what did Renata actually do wrong with the new board?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She lied about the numbers, and the board found out the attrition had not really halved.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She told three true facts as a flat list of simple-past events, with no sequence between them &mdash; so a real turnaround sounded like luck. She handed them a list when she should have handed them a timeline.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She was arrogant and took too much personal credit for the recovery.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">5. What does the text mean when it says a method &mdash; not a story of happy accidents &mdash; is what survives the trip to a second country?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That the exact same actions, in the same order, will produce the same numbers anywhere.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That what transfers to Canada is the SEQUENCE &mdash; diagnose the legacy, lay the groundwork, wait for the tipping point, reverse the trend &mdash; not the luck. In a culture she has not lived in, the groundwork has to be laid again from the beginning.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That she should simply repeat the Brazil presentation word for word to the Canadian team.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Past Perfect &amp; Past Perfect Continuous</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">The past perfect is the &ldquo;before the before&rdquo;. It puts the thing that was already true &mdash; the failing, the building, the preparing &mdash; in front of the simple-past event everyone can see. In a turnaround story, that ordering is not decoration: it is the difference between a sequence you caused and a coincidence you were standing next to.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Example (your Brazil turnaround)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. <strong>By the time</strong> + past simple, + <strong>past perfect</strong></td><td style="padding:.6rem">By the time X happened, Y <strong>had</strong> (already) <strong>+ past participle</strong></td><td style="padding:.6rem">By the time the board reviewed it, attrition <strong>had already fallen</strong>.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. <strong>Past perfect continuous</strong> (duration up to a past point)</td><td style="padding:.6rem"><strong>had been + -ing</strong> + for / since</td><td style="padding:.6rem">Engagement <strong>had been dropping</strong> for eighteen months.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. <strong>Past perfect</strong> + <strong>before</strong> + past simple</td><td style="padding:.6rem">S <strong>had + past participle</strong> ... before + past simple</td><td style="padding:.6rem">I <strong>had rebuilt</strong> onboarding before the numbers moved.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. <strong>already / never / just</strong> + past perfect</td><td style="padding:.6rem">had <strong>already / never / just</strong> + past participle</td><td style="padding:.6rem">The groundwork <strong>had already been</strong> in place for two quarters.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">The three layers of a turnaround</td><td style="padding:.6rem" colspan="2"><strong>Deep past</strong> (had been failing / had been building) &rarr; <strong>your build</strong> (had rebuilt, had set up) &rarr; <strong>the visible result</strong> (attrition fell, engagement rose). The past perfect owns the first two layers; the simple past owns the third.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (mistake number 1):</strong> after <strong>By the time</strong>, the earlier event needs the <strong>past perfect</strong>. &ldquo;By the time the board met, we <em>already lost</em> thirty teachers&rdquo; is WRONG &rarr; &ldquo;we <strong>had</strong> already <strong>lost</strong> thirty teachers&rdquo;. A first language may let you drop that earlier layer in speech; English does not, and dropping it here erases the very sequence your argument depends on.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (mistake number 2):</strong> <strong>had been + -ing</strong> (active, in progress) is not <strong>had been + past participle</strong> (passive, done to it). &ldquo;Engagement <em>had been dropped</em> for eighteen months&rdquo; says somebody dropped it. You mean it <strong>had been dropping</strong>. And use <strong>for</strong> + a period (for two years), <strong>since</strong> + a starting point (since 2023) &mdash; never &ldquo;since two years&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Why this matters to you:</strong> a turnaround told entirely in the simple past &mdash; &ldquo;I arrived, I changed onboarding, retention improved&rdquo; &mdash; is a to-do list, and a to-do list reads as luck. The same story with the past perfect underneath &mdash; &ldquo;attrition <strong>had been</strong> climbing for two years; long before it moved, I <strong>had</strong> rebuilt onboarding&rdquo; &mdash; is a method. The board is not testing whether your Brazil numbers are real. It is testing whether you can show the <strong>order</strong>, because the order is the only proof that it will happen again in Canada.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>The three-move story:</strong> <strong>BACKDROP</strong> (what had already been failing, in the past perfect continuous) &rarr; <strong>BUILD</strong> (what you had put in place, in the past perfect, before any result) &rarr; <strong>REVERSAL</strong> (what finally moved, in the simple past). In that order, and the order is the argument. Never lead with the result.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct past-perfect form. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Turnaround Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order in which you will narrate the Brazil turnaround to the board.</p>
      <div class="order-container" id="order-l11">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Show the groundwork you had already laid, completed before any result appeared: I had rebuilt onboarding and set up a pulse survey months before the numbers moved.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Close on the reversal and the method, not the luck: the trend reversed, and what I am bringing to Canada is the sequence, not the coincidence.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Set the backdrop in the past perfect continuous: for two years before I arrived, attrition had been climbing and engagement had been falling.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Mark the tipping point as a simple-past event against everything that was already ready: when it came to a head, the new system had already been running for a term.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Name the legacy you inherited and trace the problem to its root: the decline traced back to onboarding, a decision made long before the resignations.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l11')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences that carry a turnaround story from the backdrop to the method.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your board review.</p>
      <div class="quiz-item"><div class="quiz-question">The chair says: &ldquo;The attrition fell &mdash; but the whole sector recovered that year. How do you know it was you?&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;It was me. I redesigned onboarding and the numbers turned around within a year.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;By the time the market recovered, attrition had already been falling for two quarters. The groundwork had been laid eight months earlier, and the fall traces back to the onboarding redesign, not to the calendar.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I suppose we will never really know whether it was the market or the work.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the past perfect CORRECTLY?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;By the time the board met, we already lost thirty teachers.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;When I inherited the team, engagement had been dropped for eighteen months.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;When I inherited the team, engagement had been dropping for eighteen months, and nobody had traced it back to onboarding yet.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks: &ldquo;Walk me through what the situation was before you arrived.&rdquo; You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;When I inherited the team, engagement had been dropping for eighteen months, the pattern was entrenched, and nobody had traced it back to onboarding. I did not create the crisis; I named it.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;The situation was bad, and then I made it good.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Honestly, everything was already improving by the time I got there.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks what you would do differently. The answer that reads as senior is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Nothing. The turnaround worked, so I would repeat it exactly.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;In hindsight, I would have set the baseline earlier. By the time I measured it, the culture had already deteriorated for months, and I lost the cleanest before-and-after I could have had.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I would have asked for a bigger budget and more time.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He says: &ldquo;Canada is not Brazil. Why should we believe you can do it again?&rdquo; The strongest answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Because I did it once, so I can do it anywhere.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Because Canada and Brazil are basically the same kind of organization.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;You should not believe it yet, and I would not ask you to. The Brazil turnaround was a sequence, not an accident &mdash; groundwork, tipping point, reversal, in that order. I have not lived the Canadian status quo, and the groundwork will have to be laid again from the beginning. What transfers is the method.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">The Maple Bear board asks you to walk them through the Brazil turnaround and prove it was leadership, not luck &mdash; before they hand you Canada on August 1st. Tell it as a sequence, never as a list. Start with the backdrop (what HAD BEEN failing before you arrived, in the past perfect continuous), then the build (what you HAD put in place before any result appeared, in the past perfect), then the tipping point, and only then the reversal. Close by conceding that Canada is unproven and naming what actually transfers. Use the past perfect and past perfect continuous throughout, and at least six words from this lesson (legacy, groundwork, tipping point, to inherit, to trace back to, to come to a head, to reverse a trend).</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-11"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 11</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-10 pode voltar como vocab card ----------
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
    # aula 8
    'takeaway', 'caveat', 'rationale', 'trade-off', 'traction', 'quick win', 'roadblock',
    'track record', 'preliminary', 'tangible', 'to take stock of', 'to fall short of',
    'to build on', 'to iron out', 'the jury is still out',
    # aula 9
    'counterpoint', 'reservation', 'premise', 'assumption', 'merit', 'anecdotal', 'rigor',
    'peer-reviewed', 'common ground', 'to concede', 'to take issue with',
    "to play devil's advocate", 'to stand your ground', 'to defer to', 'to hold water',
    # aula 10
    'data storytelling', 'correlation', 'causation', 'confounding variable',
    'statistical significance', 'sample size', 'outlier', 'margin of error',
    'leading indicator', 'actionable insight', 'to control for', 'to skew',
    'to read too much into', 'to tease out', 'to connect the dots',
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-10'
assert 12 <= len(VOCAB) <= 15, f'REGRA 13 (B2 = 12-15 palavras): {len(VOCAB)}'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
