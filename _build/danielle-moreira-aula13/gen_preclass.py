#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 13 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes), ZERO PT na tela
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..12
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 13 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).

PIVOT (REGRA 22 — critico): o curriculo pedia "Brazil vs. Canada — Cross-Cultural
  Differences in Organizational Behavior" com gramatica "used to / be used to / get
  used to" e vocab power distance / individualism vs collectivism / high-context /
  low-context. TODOS ja ensinados: o TEMA duplica a aula 5 (cleft) e a aula 10, a
  gramatica used-to JA foi dada na aula 10, e os 4 termos de cultura JA foram vocab
  cards da aula 5. Pivotado para um angulo INEDITO no eixo Brasil<->Canada: as REGRAS
  NAO-ESCRITAS do escritorio canadense (rapport, small talk, etiqueta, understatement),
  com gramatica FRESCA — wish / if only — para a aluna VOZAR a propria adaptacao
  cultural sem soar reclamona.

GRAMATICA DA AULA 13 (nova; nao repete a1..a12):
  wish / if only
  wish + past simple (presente irreal) · wish + past perfect (arrependimento) ·
  wish + would (comportamento do outro) · if only (enfase). O verbo recua no tempo
  porque a frase admite que aquilo NAO e a realidade.
"""
import re
import random

random.seed(13)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT (ref interna, NAO vai pra tela), exemplo)
VOCAB = [
    ("Rapport", "an easy, trusting connection built with someone through repeated warm contact",
     "sintonia / boa rela&#231;&#227;o",
     "In Brazil the rapport came fast; here it is built more slowly, mostly in the small talk before the meeting starts."),
    ("Small talk", "light, informal conversation that builds a connection before the real business starts",
     "conversa fiada / bate-papo leve",
     "The six minutes of small talk are not filler here; they are how the team warms up and how trust is earned."),
    ("Egalitarian", "treating everyone as equals, with little visible distance between senior and junior people",
     "igualit&#225;rio",
     "The office is strikingly egalitarian: the VP is on a first-name basis with everyone and lines up for coffee like the rest of us."),
    ("Cordiality", "friendly, polite warmth in professional dealings, without being close friends",
     "cordialidade",
     "The cordiality is real but measured; people are warm to you long before they are actually close to you."),
    ("Punctuality", "the habit of starting and finishing exactly on time",
     "pontualidade",
     "Punctuality is not a virtue you get credit for here; it is the baseline, and arriving late reads as disrespect."),
    ("Formality", "the degree of official, reserved behavior a setting expects, in titles, dress and tone",
     "formalidade",
     "I arrived with Brazilian meeting formality and here it created the opposite of respect, a distance I did not intend."),
    ("Understatement", "deliberately describing something as smaller or milder than it really is",
     "eufemismo / atenua&#231;&#227;o",
     "'It's a bit of a concern' was an understatement; it meant the whole plan was in trouble, and I read it too literally."),
    ("Code-switching", "adjusting how you speak or behave to fit a different cultural setting",
     "alternar entre c&#243;digos culturais",
     "I already code-switch between Portuguese and English; now I am learning to code-switch between two office cultures."),
    ("Etiquette", "the unwritten code of polite behavior expected in a particular group",
     "etiqueta / protocolo social",
     "There is a whole etiquette here that no onboarding document mentions, and breaking it quietly costs you."),
    ("Reciprocity", "the give-and-take of trust and favors that keeps a relationship balanced",
     "reciprocidade",
     "The reciprocity is real: invest in the small talk first, and people invest back in you."),
    ("To break the ice", "to ease the initial awkwardness when people do not yet know each other",
     "quebrar o gelo",
     "A question about the weekend is how you break the ice here, and the meeting goes better for it."),
    ("To read the room", "to sense the unspoken mood and dynamics of a group before you act",
     "sentir o clima do ambiente",
     "I have to read the room, not just the words, because the real objection is rarely said out loud."),
    ("To hit it off", "to form a warm rapport with someone very quickly",
     "se dar bem logo de cara",
     "I hit it off with the operations lead over coffee, and that one conversation opened three doors."),
    ("To save face", "to protect your own or someone else's dignity in front of others",
     "salvar as apar&#234;ncias / evitar constrangimento",
     "I raised the problem privately so the coordinator could save face, and she fixed it the same day."),
    ("The unwritten rules", "the implicit norms everyone is expected to follow without being told",
     "as regras n&#227;o-escritas",
     "The unwritten rules are where the real culture lives, and they are exactly what no document ever gives you."),
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
        f'<span class="match-word" style="flex:0 0 170px">{w}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
        f'<option value="">Select...</option>{o}</select></div>'
    )
match_rows = '\n'.join(rows)

# ---------- Stage 1.5 fill-in-the-blank (wish / if only) ----------
# (pre, resposta, hint, frase completa (audio), post) -- espacamento EXPLICITO em pre/post
BLANKS = [
    ("I wish the team ", "made",
     "Hint: wish + PAST SIMPLE for a present you want changed. made, not &ldquo;makes&rdquo; -- the verb steps back in time",
     "I wish the team made more small talk before we start.",
     " more small talk before we start."),
    ("I wish I ", "had asked",
     "Hint: wish + PAST PERFECT for a regret about the past. had + past participle (NOT &ldquo;would have asked&rdquo;)",
     "I wish I had asked about the etiquette on day one.",
     " about the etiquette on day one."),
    ("I wish people ", "wouldn't",
     "Hint: wish + WOULD for a behavior in OTHERS you want changed. would (NOT &ldquo;will&rdquo;)",
     "I wish people wouldn't read my silence as agreement.",
     " read my silence as agreement."),
    ("If only I ", "had read",
     "Hint: if only + PAST PERFECT for an emphatic past regret. had + past participle",
     "If only I had read the room, I would have caught the understatement.",
     " the room, I would have caught the understatement."),
    ("I wish I ", "were",
     "Hint: wish + WERE for all persons (formal). NOT &ldquo;was&rdquo; in careful register",
     "I wish I were further along with the unwritten rules, but I am getting there.",
     " further along with the unwritten rules, but I am getting there."),
    ("I wish the meetings ", "started",
     "Hint: wish + PAST SIMPLE for a present you want changed. started, not &ldquo;start&rdquo;",
     "I wish the meetings started on time, so I model the punctuality myself.",
     " on time, so I model the punctuality myself."),
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
    "I wish the meetings got to the point faster, but the small talk is where the rapport is built, so I break the ice first.",
    "I wish I had asked about the etiquette on day one, because I read the formality of this office wrong.",
    "I wish people wouldn't read my silence as agreement, so I now say let me think on that out loud.",
    "If only I had read the room, I would have caught the understatement behind the word interesting.",
    "The reciprocity here is real: I invest in the small talk first, and the team invests back. I am code-switching, not resisting.",
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

HTML = f'''<div class="lesson-card" id="ex-lesson-13">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 13 -- Pre-class</div>
      <h3>The Unwritten Rules -- Rapport and Etiquette in the Canadian Office</h3>
      <div class="lesson-desc">Decoding the etiquette no document gives you: the small talk that has to come before business, the flat, egalitarian way people speak to their VP, the punctuality that is expected not admired, the understatement that hides a real objection. And the grammar to voice your own adaptation without sounding like you are complaining. Key words: rapport, small talk, egalitarian, cordiality, punctuality, formality, understatement, code-switching, etiquette, reciprocity, to break the ice, to read the room, to hit it off, to save face, the unwritten rules. Structure: wish / if only &mdash; wish + past simple (I wish the team made...), wish + past perfect (I wish I had asked...), wish + would (I wish people wouldn't...), if only for emphasis. The verb steps back in time because the sentence admits: this is not how things are, this is how I would want them.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="13" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="13">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. This is the vocabulary of the office culture nobody writes into a handbook.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with the correct definition.</p>
      <div class="match-grid" id="match-l13">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On her first Monday in the Toronto office, Danielle walked into the nine o'clock meeting with her agenda open and ready. Nobody else opened one. For six minutes the room talked about the weekend, the snow, someone's dog. She waited, a little impatient, and then did the efficient thing: she started on item one. She could feel the temperature of the room drop. It took her three days and a quiet word from Nathan to understand why. In Brazil, getting straight to business is a way of <strong>respecting</strong> people's time. Here, skipping the <strong>small talk</strong> does not read as focused. It reads as cold, and the <strong>rapport</strong> she needed was being built in exactly the minutes she had tried to skip.</p>
        <p style="margin-top:.8rem">There is a way to talk about a frustration like that which keeps you inside the culture instead of standing outside it, judging &mdash; and it is a grammar. She did not say &ldquo;these meetings are inefficient&rdquo;. She said, &ldquo;<strong>I wish</strong> the meetings <strong>got</strong> to the point a little faster &mdash; but the small talk is where the trust is built, so I'm learning to <strong>break the ice</strong> first.&rdquo; Notice the verb. She means <em>now</em>, yet the verb is <strong>got</strong>, in the past. That backward step is the whole point: it is English admitting <em>this is not how things are; this is how I would want them</em>. And by the time she adds what she is already doing about it, she is no longer a newcomer complaining. She is a leader adapting.</p>
        <p style="margin-top:.8rem">The <strong>etiquette</strong> kept surprising her. The office was strikingly <strong>egalitarian</strong> &mdash; the VP went by her first name and stood in the coffee line like everyone else &mdash; so the <strong>formality</strong> Danielle had arrived with created distance, not respect. And the disagreement was almost never on the table. When a colleague called her plan &ldquo;interesting&rdquo; and &ldquo;not quite there yet&rdquo;, that was an <strong>understatement</strong>: a real objection wearing a polite coat. &ldquo;<strong>If only</strong> I <strong>had read</strong> the room,&rdquo; she told Nathan afterwards, &ldquo;I would have caught it.&rdquo; The regret takes <strong>had read</strong>, the past perfect, because she is looking back and wanting a different past &mdash; and naming a mistake that cleanly, without drowning in it, is one of the most senior things a leader can do.</p>
        <p style="margin-top:.8rem">The rule that took the longest to trust was <strong>reciprocity</strong>. The <strong>cordiality</strong> was real but measured; people were warm long before they were close. And there was one thing she wanted other people to change, not just survive: &ldquo;I <strong>wish</strong> people <strong>wouldn't</strong> read my silence as agreement.&rdquo; When she went quiet, she was weighing something, not consenting. So she began saying &ldquo;let me think on that out loud&rdquo; &mdash; it let everyone <strong>save face</strong> and it kept things clear. None of this meant she was becoming someone else. She was <strong>code-switching</strong>, the same way she already switched between Portuguese and English. And Nathan was right: within a month, she had <strong>hit it off</strong> with the team, because she had learned the one thing no handbook teaches &mdash; that the culture lives in the <strong>unwritten rules</strong>, and you read them by wishing out loud what you would change, and adapting while you do.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does &ldquo;I wish the meetings got to the point faster&rdquo; use &ldquo;got&rdquo; and not &ldquo;get&rdquo;, even though she means now?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the meetings got faster in the past and are slow again now.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because after &ldquo;wish&rdquo;, a present situation you want to be different steps back into the past simple. The backward verb is English admitting this is not reality &mdash; it is what she would want.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because &ldquo;wish&rdquo; can only be followed by an irregular verb.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Mistake number one of this lesson: why is &ldquo;I wish I would have asked about the etiquette&rdquo; wrong?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A regret about the past takes the past perfect: &ldquo;I wish I <strong>had asked</strong>&rdquo;. &ldquo;Would have asked&rdquo; is the classic error &mdash; save &ldquo;would&rdquo; for a behavior in others you want changed.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because &ldquo;etiquette&rdquo; cannot be the object of &ldquo;ask about&rdquo;.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because a regret must always use the present perfect, &ldquo;have asked&rdquo;.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Mistake number two: why is &ldquo;I wish people will stop reading my silence as agreement&rdquo; wrong?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because &ldquo;silence&rdquo; is uncountable and cannot be read.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> When you want SOMEONE ELSE to change a behavior, wish takes <strong>would</strong>, not &ldquo;will&rdquo;: &ldquo;I wish people <strong>wouldn't</strong> read my silence as agreement.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence should be in the passive voice.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What did the colleague actually mean by calling the plan &ldquo;interesting&rdquo; and &ldquo;not quite there yet&rdquo;?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That the plan was genuinely intriguing and almost finished.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It was an understatement &mdash; a real objection said softly. In this culture the disagreement is often in the room, not on the table, so she had to read the room, not the words.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That the plan had already been approved by the VP.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">5. What is the difference between the newcomer who resists a culture and the leader who adapts to it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The leader hides every frustration and pretends everything is fine.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The newcomer says &ldquo;this is wrong&rdquo; and stands outside judging. The leader says &ldquo;I wish it worked differently, and here is what I am doing meanwhile&rdquo; &mdash; same frustration, but inside the culture, working with it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The leader simply imposes the Brazilian way until the team adjusts.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Wish &amp; If Only</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">&ldquo;Wish&rdquo; and &ldquo;if only&rdquo; let you name a frustration precisely without complaining. The trick is that the verb after them steps BACKWARD in time &mdash; that backward step is the language marking &ldquo;this is not how things are&rdquo;. Which tense you step back to depends on what you mean.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">You mean</th><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Example (your Canadian office)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. A <strong>present</strong> situation you want to be different</td><td style="padding:.6rem">wish + <strong>past simple</strong></td><td style="padding:.6rem">I wish the team <strong>made</strong> more small talk.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. Same, more <strong>formal</strong> (all persons)</td><td style="padding:.6rem">wish + <strong>were</strong></td><td style="padding:.6rem">I wish I <strong>were</strong> further along with the etiquette.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. A <strong>regret</strong> about the past</td><td style="padding:.6rem">wish + <strong>past perfect</strong> (had + p.p.)</td><td style="padding:.6rem">I wish I <strong>had asked</strong> about the etiquette on day one.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. You want <strong>someone else</strong> to change a behavior</td><td style="padding:.6rem">wish + <strong>would</strong> + base verb</td><td style="padding:.6rem">I wish people <strong>wouldn't</strong> read my silence as agreement.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">5. <strong>Emphatic</strong> wish or regret</td><td style="padding:.6rem" colspan="2"><strong>if only</strong> + the same tense rules: <strong>If only</strong> I <strong>had read</strong> the room.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Watch out (mistake number 1):</strong> after &ldquo;wish&rdquo;, a present you want changed goes into the <strong>past simple</strong>. &ldquo;I wish I <em>know</em> the rules&rdquo; is WRONG &rarr; &ldquo;I wish I <strong>knew</strong> the rules&rdquo;. Portuguese uses a present/subjunctive here, and translating literally keeps the verb in the present. English needs the backward step.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Watch out (mistake number 2):</strong> a past regret takes the <strong>past perfect</strong>, never &ldquo;would have&rdquo;. &ldquo;I wish I <em>would have asked</em>&rdquo; &rarr; &ldquo;I wish I <strong>had asked</strong>&rdquo;. Keep <strong>would</strong> for a behavior in OTHERS you want changed &mdash; and there it is &ldquo;would&rdquo;, never &ldquo;will&rdquo;: &ldquo;I wish they <strong>would</strong> listen&rdquo;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Why this matters to you:</strong> &ldquo;This office is wrong&rdquo; puts you outside the culture, judging it &mdash; and no one lets an outsider change anything. &ldquo;I <strong>wish</strong> it worked differently, and here is what I am doing meanwhile&rdquo; puts you inside it, adapting. Same frustration, opposite impression. The backward-stepping verb is what signals you know it is <em>your</em> wish, not <em>their</em> failing.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>The three-move reframe:</strong> <strong>WISH</strong> (name the frustration, verb in the past) &rarr; <strong>OWN</strong> (what you are already doing about it) &rarr; <strong>INVITE</strong> (open the door without imposing your norm). Skip the middle move and it is a complaint; skip the last and it is a demand.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form after wish / if only. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Reframe in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves in the order that turns a frustration about the Canadian office into a leader's adaptation.</p>
      <div class="order-container" id="order-l13">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Own the adaptation you are already making: so I am learning to break the ice first and treat the small talk as where the rapport is built.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Close on reciprocity, not resentment: the more I invest in the culture first, the more the team invests back, and I am code-switching into it, not resisting it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Name the frustration as a wish, verb stepped back in time: I wish the meetings got to the point a little faster.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Invite the other person without imposing your norm: and when you do have a real concern, I would genuinely rather you told me plainly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Acknowledge the reason the rule exists here: but the small talk is not filler, it is how this team builds trust.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l13')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These five carry a frustration into an adaptation without a single complaint.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of your first month in the Canadian office.</p>
      <div class="quiz-item"><div class="quiz-question">Your VP asks, in a 1:1, how you are settling in. The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Honestly, everything here is so indirect and slow. It is frustrating.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;It's an adjustment. I wish I had asked about the etiquette on day one, but I am learning fast &mdash; I break the ice first now, and I read the room for the understatement instead of waiting for a direct no.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Everything is perfect, no problems at all.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses &ldquo;wish&rdquo; CORRECTLY?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I wish I know the unwritten rules of this office.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;I wish I would have understood the formality here sooner.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;I wish I had understood the formality here sooner, and I wish people wouldn't read my silence as agreement.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A colleague says your proposal is &ldquo;interesting&rdquo; and &ldquo;might need a bit more thought&rdquo;. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Read it as a real objection wearing a polite coat, and ask one follow-up: &ldquo;I want to make sure I read the room right &mdash; what would make it stronger?&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Take it as approval and move the proposal forward.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Tell them to stop being indirect and just say what they mean.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want the team to stop treating your thinking pauses as consent. The best way to voice it is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Stop assuming I agree just because I am quiet.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I wish people wouldn't read my silence as agreement &mdash; when I go quiet I am weighing something. So I've started saying &lsquo;let me think on that out loud&rsquo; to keep it clear.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;It is not my fault you misread me.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Your mentor in Brazil asks what you would change about your first week. The answer that reads as senior is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Nothing, it was fine.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;If only I had understood that the culture lives in the small things &mdash; the small talk, the first names, the understatement &mdash; not in the org chart. I read the policies before I came; I wish I had asked about the unwritten rules.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I would have told them how we do it in Brazil on day one.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. Speak for two or three minutes, with no script.</p>
      <div class="think-card">
        <div class="think-question">It is your first 1:1 with your Canadian VP, three weeks into the move. She asks how you are settling into the office culture. Name two or three things you wish were different about the way this office works &mdash; each as a proper wish, with the verb stepped back in time (past simple for a present you want changed, had + past participle for a regret, would for a behavior in others) &mdash; and pair every wish with the adaptation you are already making. Close warmly: you are adjusting, not regretting the move. Use wish and if only correctly throughout, and at least six words from this lesson (rapport, small talk, egalitarian, understatement, etiquette, to read the room, to code-switch, reciprocity).</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-13"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 13</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-12 pode voltar como vocab card ----------
# Extraido do hub public/professor/danielle-moreira.html (aulas 1..12), normalizado lower.
JA_ENSINADO = {
    'accountability', 'actionable insight', 'a double-edged sword', 'alignment', 'anecdotal',
    'assertiveness', 'assumption', 'attrition', 'bandwidth', 'baseline', 'behavioral pattern',
    'belonging', 'benchmark', 'bilingual education', 'blind spot', 'buy-in', 'cascading goals',
    'causation', 'caveat', 'change management', 'common ground', 'conflict resolution',
    'confounding variable', 'constructive feedback', 'core values', 'corrective action',
    'correlation', 'counterpoint', 'credibility', 'cross-functional', 'cultural assessment',
    'cultural diagnosis', 'cultural humility', 'cultural intelligence', 'culture fit',
    'data storytelling', 'defensiveness', 'deliverable', 'diagnostic tool', 'disengagement',
    'diversity and inclusion', 'employee journey', 'employee value proposition', 'employer brand',
    'engagement survey', 'entrenched', 'entry plan', 'exit interview', 'findings', 'focus group',
    'framework', 'franchisor', 'frontline staff', 'gap analysis', 'groundwork', 'growth mindset',
    'handover', 'headquarters', 'high-context culture', 'hybrid model', 'inclusive leadership',
    'indirect communication', 'individualism and collectivism', 'influence without authority',
    'in hindsight', 'key performance indicator', 'leading indicator', 'learning curve', 'legacy',
    'listening tour', 'low-context culture', 'mandate', 'margin of error', 'merit', 'milestone',
    'non-violent communication', 'okr', 'onboarding experience', 'organizational culture', 'outlier',
    'peer-reviewed', 'people analytics', 'people strategy', 'performance cycle', 'performance gap',
    'power distance', 'precedent', 'predecessor', 'preliminary', 'premise', 'psychological contract',
    'psychological safety', 'pulse survey', 'quick win', 'ramp-up period', 'rationale', 'reservation',
    'resistance to change', 'response rate', 'rigor', 'roadblock', 'root cause', 'sample size',
    'senior leadership', 'stakeholder', 'statistical significance', 'status quo', 'succession planning',
    'takeaway', 'talent retention', 'tangible', 'the elephant in the room', 'the jury is still out',
    'tipping point', 'toxic culture', 'track record', 'traction', 'trade-off', 'transition period',
    'trust index', 'turnaround', 'turnover rate', 'uphill battle', 'vantage point', 'wake-up call',
    'workforce planning', 'work-life integration',
}
for w, _, _, _ in VOCAB:
    assert w.lower() not in JA_ENSINADO, f'REGRA 22: "{w}" ja foi ensinado nas aulas 1-12'

print('preclass.html gerado:', len(HTML) // 1024, 'KB; vocab', len(VOCAB), 'itens; speakable', len(set(SPEAKABLE)))
