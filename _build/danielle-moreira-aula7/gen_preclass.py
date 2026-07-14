#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 7 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..6
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 7 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).

GRAMATICA DA AULA 7 (nova; nao repete a1..a6):
  reporting verbs + os 5 padroes de complementacao
  (V + that / V + -ing / V + prep + -ing / V + obj + to-inf / V + to-inf)
"""
import re
import random

random.seed(7)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Constructive feedback", "feedback that names the behavior and its impact, and leaves the person able to act on it",
     "feedback construtivo",
     "Constructive feedback is not softer feedback. It is feedback the other person can actually do something with."),
    ("Conflict resolution", "the work of turning a disagreement into a decision both sides can live with",
     "resolu&#231;&#227;o de conflitos",
     "Conflict resolution is not making the conflict disappear. It is making it produce something."),
    ("Blind spot", "the thing everyone on the team can see about you, except you",
     "ponto cego",
     "His blind spot is that he hears a question about a deadline as an accusation about his character."),
    ("Defensiveness", "the reflex of protecting yourself instead of hearing the point",
     "postura defensiva",
     "Defensiveness is not disagreement. It is the door closing before the sentence has finished."),
    ("Resistance to change", "the pushback a team produces when a change arrives without them",
     "resist&#234;ncia &#224; mudan&#231;a",
     "Resistance to change is rarely about the change. More often than not, it is about not having been asked."),
    ("Non-violent communication", "naming the observation, the impact and the request, and never the character of the person",
     "comunica&#231;&#227;o n&#227;o-violenta",
     "Non-violent communication separates the behavior from the person. That separation is the whole method."),
    ("Growth mindset", "treating an ability as something you build, not something you were issued at birth",
     "mentalidade de crescimento",
     "A growth mindset turns I am not good at this into I am not good at this yet."),
    ("Behavioral pattern", "a behavior that has happened often enough to stop being an accident",
     "padr&#227;o de comportamento",
     "One missed deadline is an incident. Three is a behavioral pattern, and it needs a different conversation."),
    ("Performance gap", "the distance between what was agreed and what was actually delivered",
     "lacuna de desempenho",
     "Name the performance gap with a number, or the whole conversation will sound like an opinion."),
    ("Corrective action", "the specific step, with a date on it, that closes the gap",
     "a&#231;&#227;o corretiva",
     "A conversation without a corrective action and a date is a conversation you will simply have again."),
    ("To take ownership of", "to accept that the outcome was yours, without being asked to",
     "assumir a responsabilidade por",
     "I am not asking you to agree with me. I am asking you to take ownership of the rollout."),
    ("To address head-on", "to raise the difficult thing directly, at the start, instead of circling it",
     "encarar de frente",
     "I would rather address it head-on today than manage the consequences of it for six months."),
    ("To follow through on", "to actually do the thing you agreed to do, after the meeting has ended",
     "cumprir / levar at&#233; o fim",
     "He agreed to every action in that meeting. He followed through on none of them."),
    ("To sugarcoat", "to make the message so gentle that the other person never hears the problem",
     "dourar a p&#237;lula / suavizar demais",
     "If you sugarcoat this, he will leave the call happy and nothing at all will change."),
    ("To beat around the bush", "to talk around the difficult point instead of naming it",
     "enrolar / n&#227;o ir direto ao ponto",
     "Do not beat around the bush with this team. Name the issue first, then protect the person."),
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
        f'<span class="vocab-card-def">{d} ({pt})</span></div>'
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

# ---------- Stage 1.5 fill-in-the-blank (os 5 padroes de reporting verb) ----------
BLANKS = [
    ("He apologized", "for reacting",
     "Dica: apologize FOR + verbo em -ing. Nunca 'apologized to react'",
     "He apologized for reacting defensively in front of the whole team.",
     "defensively in front of the whole team."),
    ("She suggested", "that I talk",
     "Dica: suggest + THAT + ora&#231;&#227;o (ou suggest + -ing). NUNCA 'suggested me to talk'",
     "She suggested that I talk to him before the next steering meeting.",
     "to him before the next steering meeting."),
    ("He denied", "missing",
     "Dica: deny + verbo em -ing. Nunca 'denied to miss'",
     "He denied missing the deadlines, and the three dates said otherwise.",
     "the deadlines, and the three dates said otherwise."),
    ("He accused the head office", "of imposing",
     "Dica: accuse somebody OF + verbo em -ing",
     "He accused the head office of imposing the initiative without consulting anyone.",
     "the initiative without consulting anyone."),
    ("He agreed", "to follow through",
     "Dica: agree + TO + infinitivo. Nunca 'agreed following'",
     "He agreed to follow through on the corrective action by the fifteenth.",
     "on the corrective action by the fifteenth."),
    ("I encouraged him", "to take ownership",
     "Dica: encourage + OBJETO + TO + infinitivo",
     "I encouraged him to take ownership of the rollout rather than explain it.",
     "of the rollout rather than explain it."),
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
    ("What I have noticed is a pattern, and I would rather address it head-on than manage it for six months.",
     "O que eu percebi &#233; um padr&#227;o, e eu prefiro encar&#225;-lo de frente a administr&#225;-lo por seis meses."),
    ("He denied missing the deadlines, but he acknowledged that his team had never been consulted.",
     "Ele negou ter perdido os prazos, mas reconheceu que o time dele nunca tinha sido consultado."),
    ("I am not asking you to agree with me. I am asking you to take ownership of the outcome.",
     "Eu n&#227;o estou pedindo que voc&#234; concorde comigo. Estou pedindo que voc&#234; assuma a responsabilidade pelo resultado."),
    ("If I sugarcoat this, you will leave the call happy and nothing at all will change.",
     "Se eu dourar a p&#237;lula, voc&#234; vai sair da chamada feliz e absolutamente nada vai mudar."),
    ("He apologized for reacting defensively, and he agreed to follow through on the corrective action.",
     "Ele pediu desculpas por ter reagido de forma defensiva, e concordou em cumprir a a&#231;&#227;o corretiva."),
]
sp = []
for phrase, pt in SPEECH:
    SPEAKABLE.append(phrase)
    sp.append(
        f'      <div class="speech-card" data-phrase="{phrase}">\n'
        f'        <div class="speech-phrase">{phrase}</div>\n'
        f'        <div class="speech-translation">{pt}</div>\n'
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
        f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
    )
survival = '\n'.join(sv)

HTML = f'''<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 07 -- Pre-class</div>
      <h3>Navigating Difficult Conversations -- Feedback, Accountability, and Conflict in a Canadian Context</h3>
      <div class="lesson-desc">Conduzir a conversa que ningu&#233;m quer ter: nomear um padr&#227;o de comportamento com evid&#234;ncia, atravessar a postura defensiva sem ferir a pessoa, fechar com uma a&#231;&#227;o corretiva com data &mdash; e depois REPORTAR a conversa para cima, com precis&#227;o. Key words: constructive feedback, conflict resolution, blind spot, defensiveness, resistance to change, non-violent communication, growth mindset, behavioral pattern, performance gap, corrective action, to take ownership of, to address head-on, to follow through on, to sugarcoat, to beat around the bush. Structure: reporting verbs e os cinco padr&#245;es de complementa&#231;&#227;o (he acknowledged THAT... / he denied MISSING... / he apologized FOR reacting... / I encouraged him TO take... / he agreed TO follow through...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. Este &#233; o vocabul&#225;rio de uma conversa dif&#237;cil que termina em acordo, e n&#227;o em ressentimento.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l7">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The conversation lasted forty minutes, and Ines Correia lost it in the first ninety seconds. She had rehearsed the opening for two days. She had a <strong>performance gap</strong> with three dates behind it, and a <strong>behavioral pattern</strong> that was no longer arguable. And then, at the door of the sentence, she flinched. She spent four minutes on how much the team valued him, and by the time she arrived at the deadlines, he had already worked out where she was going and had built the wall. She had tried not to wound him. What she had actually done was <strong>sugarcoat</strong> it, and a message that is <strong>sugarcoated</strong> is a message that never lands.</p>
        <p style="margin-top:.8rem">Her director asked for the debrief on the Thursday, and that is where the second lesson arrived. <strong>He acknowledged that</strong> the dates had slipped, Ines said. <strong>He denied being</strong> resistant to the project. <strong>He pointed out that</strong> nobody had asked him whether the timeline was realistic, and <strong>he accused the head office of imposing</strong> a plan built without a single question to the people who had to run it. <strong>He apologized for raising</strong> his voice. He did not apologize for anything he had said. And then, at the end, <strong>he agreed to follow through on</strong> one revised date, and <strong>he promised to bring</strong> the plan himself.</p>
        <p style="margin-top:.8rem">Her director listened to all of it and asked one question. And what did <em>you</em> ask <em>him</em>? Nothing, Ines said. There had not been room. That, her director told her, is the <strong>blind spot</strong>: she had walked in to deliver a verdict and had walked out with a confession she had never requested. <strong>Defensiveness</strong> is information, he said. It is a man telling you, badly, that something happened to him that you do not know about. Next time, name the pattern in the first thirty seconds, <strong>address</strong> it <strong>head-on</strong>, and then be quiet for long enough that he tells you the thing that is not in your spreadsheet. <strong>I would encourage you to close</strong> with one <strong>corrective action</strong> and a date &mdash; and, above all, <strong>I would advise you not to beat around the bush</strong> with a man who is already braced for the blow.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. "<strong>He denied being</strong> resistant to the project." &mdash; por que N&#195;O se diz "He denied <em>to be</em> resistant"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque "deny" nunca aceita complemento nenhum, s&#243; objeto direto.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque <strong>deny</strong> pede verbo em <strong>-ing</strong> (deny + -ing), nunca infinitivo. O padr&#227;o do verbo &#233; uma propriedade DELE, e tem de ser memorizado com ele.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque a frase est&#225; no passado, e no passado o infinitivo desaparece.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. O erro brasileiro n&#186; 1 desta aula: por que "She suggested <em>me to talk</em> to him" est&#225; errado?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque <strong>suggest</strong> N&#195;O aceita objeto + infinitivo. &#201; "suggested <strong>that I talk</strong> to him" ou "suggested <strong>talking</strong> to him". O "sugeriu para eu falar" do portugu&#234;s chega inteiro e derruba a frase.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque o correto seria "suggested me talking to him".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque "suggest" s&#243; existe na voz passiva.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, what did Ines actually do wrong in the first ninety seconds?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She opened with the three dates before she had built any rapport with him.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She spent four minutes praising him before naming the issue &mdash; so he saw the message coming and was already defending himself by the time it arrived.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She raised her voice, and he raised his voice back.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What does the director mean when he says that defensiveness is <em>information</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That a defensive employee is always hiding something, and the manager should keep pushing until it comes out.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> That defensiveness should simply be ignored, because it is an emotional reaction and not a professional one.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> That the defensiveness is telling her, badly, that something happened to him which is not in her spreadsheet &mdash; so the right move is to name the pattern and then be quiet.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reporting Verbs &amp; Their Patterns</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Cada reporting verb carrega o seu pr&#243;prio padr&#227;o, e o padr&#227;o N&#195;O se deduz do sentido: aprende-se junto com o verbo. &#201; a gram&#225;tica do debrief &mdash; a hora em que voc&#234; conta &#224; sua VP o que foi dito na sala (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Pattern</th><th style="padding:.7rem;text-align:left">Verbs / Verbos</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. verb + <strong>that</strong> + ora&#231;&#227;o</td><td style="padding:.6rem">acknowledge, point out, explain, insist, claim, admit, add</td><td style="padding:.6rem">He <strong>acknowledged that</strong> the deadlines had slipped.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. verb + <strong>-ing</strong></td><td style="padding:.6rem">deny, admit, suggest, recommend, mention</td><td style="padding:.6rem">He <strong>denied missing</strong> the deadlines. &middot; She <strong>suggested talking</strong> to him first.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. verb + <strong>preposi&#231;&#227;o</strong> + -ing</td><td style="padding:.6rem">apologize <strong>for</strong>, insist <strong>on</strong>, object <strong>to</strong>, accuse sb <strong>of</strong>, blame sb <strong>for</strong></td><td style="padding:.6rem">He <strong>apologized for reacting</strong> defensively. &middot; He <strong>accused</strong> the head office <strong>of imposing</strong> it.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. verb + <strong>objeto</strong> + <strong>to</strong> + infinitivo</td><td style="padding:.6rem">encourage, urge, advise, remind, ask, invite, warn</td><td style="padding:.6rem">I <strong>encouraged him to take</strong> ownership of the rollout.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">5. verb + <strong>to</strong> + infinitivo</td><td style="padding:.6rem">agree, refuse, promise, offer, threaten, decide</td><td style="padding:.6rem">He <strong>agreed to follow through</strong> on the corrective action.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Backshift</td><td style="padding:.6rem" colspan="2">Reportando no passado, o tempo recua UM passo: "the dates <em>have</em> slipped" &rarr; He acknowledged that the dates <strong>had</strong> slipped. Mas se o fato ainda vale hoje, manter o presente &#233; perfeitamente aceit&#225;vel: "He insists that the timeline <strong>is</strong> impossible."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1):</strong> <em>suggest</em> N&#195;O aceita objeto + infinitivo. "He suggested <em>me to talk</em> to her" &#233; o portugu&#234;s "sugeriu para eu falar" chegando inteiro. O certo &#233; "He suggested <strong>that I talk</strong> to her" ou "He suggested <strong>talking</strong> to her". O mesmo vale para <em>recommend</em>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> depois de PREPOSI&#199;&#195;O vem sempre <strong>-ing</strong>, nunca infinitivo. "He apologized <em>to react</em> defensively" &#8594; "He apologized <strong>for reacting</strong> defensively". Guarde as preposi&#231;&#245;es coladas ao verbo: apologize <strong>for</strong>, insist <strong>on</strong>, object <strong>to</strong>, accuse somebody <strong>of</strong>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Por que isto importa para voc&#234;:</strong> o reporting verb que voc&#234; escolhe J&#193; &#201; uma avalia&#231;&#227;o. "He <em>said</em> the timeline was impossible" &#233; neutro. "He <strong>insisted that</strong> the timeline was impossible" &#233; um homem que n&#227;o cede. "He <strong>acknowledged that</strong> the timeline was impossible" &#233; um homem que reconhece um fato contra si. Mesmo evento, tr&#234;s le&#237;turas &mdash; e a sua VP canadense vai ler exatamente a que voc&#234; escolheu.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>O debrief de tr&#234;s frases:</strong> o que ele <strong>acknowledged</strong>, o que ele <strong>denied</strong>, e o que ele <strong>agreed to do</strong>. Nesta ordem, e nada mais. &#201; o relat&#243;rio que a sua VP quer na quinta-feira.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com o padr&#227;o correto do reporting verb. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Difficult Conversation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos na ordem em que voc&#234; vai conduzir o 1:1 com um coordenador canadense resistente &#224; mudan&#231;a.</p>
      <div class="order-container" id="order-l7">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Hand him the microphone and go quiet: ask what you do not know, and listen past the defensiveness to the information underneath it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Debrief upward in three sentences: what he acknowledged, what he denied, and what he agreed to do.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Address it head-on in the first thirty seconds: name the issue without sugarcoating it and without beating around the bush.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Close with one corrective action and a date on it, and ask him to take ownership of that date in front of you.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Put the evidence on the table: the behavioral pattern, the three dates, and the performance gap between what was agreed and what arrived.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases que sustentam um 1:1 dif&#237;cil do come&#231;o ao fim, e o debrief que vem depois dele.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real do seu 1:1 com um coordenador canadense.</p>
      <div class="quiz-item"><div class="quiz-question">You open the 1:1. He has missed three deadlines. The most senior first sentence is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Before anything else, I want you to know how much this team values you and how happy we are with your work.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I want to address something head-on. Three dates on the rollout have slipped, and what I have noticed is a pattern rather than an incident.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;There is a small thing I wanted to mention, and it is really not a big deal at all.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He answers: &ldquo;So you are building a case against me.&rdquo; You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;It is not the behavior itself that concerns me. It is the impact, and this conversation ends with one corrective action that you and I agree on together.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;If you are going to be defensive, there is no point in continuing this conversation.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;No, no. Forget the deadlines. Let us talk about something else.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Your VP asks for the debrief. Which sentence reports the conversation with the most precision?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;He said a lot of things, and in the end he was fine with everything.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;He suggested me to change the timeline, and he denied to be resistant.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;He acknowledged that the dates had slipped, he denied being resistant to the project, and he agreed to follow through on a revised plan by the fifteenth.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the reporting verb pattern correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;He apologized to react defensively in front of the team.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;He accused the head office of imposing a plan that nobody had been asked about.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;She recommended me to speak with him before the steering meeting.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He goes quiet and then says: &ldquo;Nobody ever asked me if that timeline was possible.&rdquo; And he is right. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;You are right, and I am not going to argue with that. The pattern still stands, and so does the question I am asking you now: what would a realistic date look like?&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;That is not relevant. The deadlines were the deadlines.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;You are completely right, and I am sorry. Let us forget the three dates.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">Your Canadian VP calls you on Thursday and asks: how did the conversation with the coordinator go? Give her the debrief, as the senior HR leader you are about to become on August 1st. Three sentences on the conversation itself, with three different reporting verbs (what he acknowledged, what he denied, what he agreed to do). Then say what YOU got wrong in that room, and what the corrective action is, with a date on it. Use six words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-7"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 7</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-6 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-6'
assert 12 <= len(VOCAB) <= 15, f'REGRA 13 (B2 = 12-15 palavras): {len(VOCAB)}'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
