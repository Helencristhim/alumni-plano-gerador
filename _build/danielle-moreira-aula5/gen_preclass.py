#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 5 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1, 2, 3 e 4
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 5 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(5)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Cultural intelligence", "the ability to read a culture you were not raised in, and adjust inside it without losing yourself",
     "intelig&#234;ncia cultural",
     "Cultural intelligence is not knowing many cultures. It is functioning well inside one you do not know yet."),
    ("High-context culture", "a culture where the meaning lives around the words: in the tone, the pause, the relationship",
     "cultura de contexto alto",
     "In a high-context culture, we will look into it can mean no, and everyone in the room knows it."),
    ("Low-context culture", "a culture where the meaning lives in the words themselves: say it, write it down, and it is settled",
     "cultura de contexto baixo",
     "Canada leans low-context: if it was not said out loud, do not assume the room heard it."),
    ("Power distance", "how far the boss feels from the room, and how safe it is to contradict one in public",
     "dist&#226;ncia hier&#225;rquica",
     "It was the power distance, not the language, that kept them silent in that meeting."),
    ("Individualism and collectivism", "whether a person is measured on their own result, or on what the group delivered together",
     "individualismo e coletivismo",
     "Our reward system rewards the individual. Our culture rewards the group. That gap is the problem."),
    ("Indirect communication", "saying the difficult thing by making it easy to infer, never by naming it",
     "comunica&#231;&#227;o indireta",
     "Indirect communication is not dishonesty. It is a different address for the same message."),
    ("Assertiveness", "stating your position clearly and holding it, without attacking the person who disagrees",
     "assertividade",
     "Assertiveness travels badly. What reads as clear in Toronto can read as harsh in Sao Paulo."),
    ("Cultural humility", "assuming your way is one way, not the way, and staying curious once you are in the room",
     "humildade cultural",
     "I am not arriving with a Brazilian model to install. That is cultural humility, and it is also strategy."),
    ("Work-life integration", "a life where the work and the rest of it share the same day, on purpose, not in two sealed halves",
     "integra&#231;&#227;o entre vida e trabalho",
     "Two days at the office and two at home is work-life integration. Managing it is a skill, not a perk."),
    ("Inclusive leadership", "leading so that the quietest person in the room still ends up speaking",
     "lideran&#231;a inclusiva",
     "Everyone was invited and three people spoke. That was not inclusive leadership. That was a guest list."),
    ("To bridge cultural gaps", "to build the crossing between two ways of working, instead of picking one of them",
     "construir pontes entre culturas",
     "My job is not to choose a culture. It is to bridge cultural gaps between two of them."),
    ("To read between the lines", "to hear what was meant, when it was never actually said",
     "ler nas entrelinhas",
     "In Brazil you learn to read between the lines. In Canada you learn to say the line."),
    ("To account for", "to include a factor in your reasoning, deliberately, because it changes the result",
     "levar em conta / considerar",
     "Any diagnosis that does not account for power distance will read the silence as agreement."),
    ("To set out", "to state expectations clearly, at the start, so that nobody has to guess later",
     "estabelecer / deixar claro desde o in&#237;cio",
     "I would rather set out the expectations in week one than defend them in month six."),
    ("To take into consideration", "to weigh a factor before deciding, not after",
     "levar em considera&#231;&#227;o",
     "We should take into consideration that this team has never been asked for its opinion before."),
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

# ---------- Stage 1.5 fill-in-the-blank ----------
BLANKS = [
    ("It was the", "power distance that",
     "Dica: it-cleft &mdash; It was + a causa + THAT (nunca 'what')",
     "It was the power distance that produced the silence, not agreement.",
     "produced the silence, not agreement."),
    ("What surprised me most", "was",
     "Dica: wh-cleft &mdash; What + ora&#231;&#227;o + WAS. Nunca acrescente 'it was' depois",
     "What surprised me most was the directness of the feedback.",
     "the directness of the feedback."),
    ("It was the academic directors", "who",
     "Dica: para PESSOAS o cleft usa who; e o verbo &#233; sempre It WAS, mesmo no plural",
     "It was the academic directors who pushed back, three days later, in writing.",
     "pushed back, three days later, in writing."),
    ("More often", "than not",
     "Dica: hedging de tend&#234;ncia &mdash; a express&#227;o completa &#233; 'more often than not'",
     "More often than not, difficult feedback in our Brazilian teams is delivered indirectly.",
     ", difficult feedback in our Brazilian teams is delivered indirectly."),
    ("It would", "appear that",
     "Dica: hedging de leitura de dado &mdash; nunca 'it would seem to appear'",
     "It would appear that the silence has more to do with hierarchy than with language.",
     "the silence has more to do with hierarchy than with language."),
    ("Any diagnosis that does not", "account for",
     "Dica: phrasal verb &mdash; account FOR (nunca 'account the')",
     "Any diagnosis that does not account for power distance will read the silence as agreement.",
     "power distance will read the silence as agreement."),
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
    ("More often than not, difficult feedback in our Brazilian teams is delivered indirectly.",
     "Na maioria das vezes, um feedback dif&#237;cil nos nossos times brasileiros &#233; dado de forma indireta."),
    ("It was the power distance that produced the silence, not agreement.",
     "Foi a dist&#226;ncia hier&#225;rquica que produziu o sil&#234;ncio, e n&#227;o a concord&#226;ncia."),
    ("Any diagnosis that does not account for hierarchy will read the silence as agreement.",
     "Qualquer diagn&#243;stico que n&#227;o leve a hierarquia em conta vai ler o sil&#234;ncio como concord&#226;ncia."),
    ("What this faculty needs is not a program. It is to be asked before it is told.",
     "O que este corpo docente precisa n&#227;o &#233; de um programa. &#201; ser perguntado antes de ser informado."),
    ("That said, I would be careful not to overgeneralize. My job is to bridge cultural gaps, not to rank them.",
     "Dito isso, eu teria cuidado para n&#227;o generalizar demais. Meu trabalho &#233; construir pontes entre culturas, n&#227;o ranque&#225;-las."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-5">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517935706615-2717063c2225?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 05 -- Pre-class</div>
      <h3>Brazil vs. Canada -- Articulating Cultural Differences with Academic and Executive Teams</h3>
      <div class="lesson-desc">Explicar a diferen&#231;a entre a cultura brasileira e a canadense a uma sala de doutores e diretores &mdash; sem estere&#243;tipo, sem generaliza&#231;&#227;o e sem recuar da observa&#231;&#227;o: nomear a dimens&#227;o, sustentar com evid&#234;ncia, e p&#244;r a causa certa sob o holofote. Key words: cultural intelligence, high-context culture, low-context culture, power distance, individualism and collectivism, indirect communication, assertiveness, cultural humility, work-life integration, inclusive leadership, to bridge cultural gaps, to read between the lines, to account for, to set out, to take into consideration. Structure: cleft sentences (It was the power distance that... / What this team needs is...) + hedging para an&#225;lise cultural comparada (One could argue that... / More often than not... / It would appear that... / For the most part...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. Este &#233; o vocabul&#225;rio com que os acad&#234;micos canadenses j&#225; descrevem voc&#234; &mdash; a partir de agosto, &#233; o vocabul&#225;rio com que voc&#234; descreve a sala.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l5">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The first session went beautifully, and that was the problem. Nadia Ferraz had flown in to run a cultural assessment with the academic faculty of a bilingual school group, and for ninety minutes not one professor objected to anything she proposed. She wrote in her notes that the room was aligned. Six weeks later, the plan was quietly dead. <strong>It was not the plan that failed</strong>, her director told her afterwards. <strong>It was the way she read the room that failed</strong>, and the two are not the same thing.</p>
        <p style="margin-top:.8rem">She had walked into a <strong>low-context culture</strong> carrying the instincts of a <strong>high-context</strong> one. In the country she came from, you <strong>read between the lines</strong>: the pause tells you the answer, and a polite silence in a meeting is rarely a yes. Here, silence meant something else entirely. Two of those professors had run their faculties for twenty years, and they did not contradict a visitor in public. They contradicted her on Friday, in an email, in three careful paragraphs, copied to her director. Any diagnosis that fails to <strong>account for</strong> that kind of <strong>power distance</strong> will read a quiet room as consent.</p>
        <p style="margin-top:.8rem"><strong>What she learned that quarter was</strong> not a technique. It was a posture. <strong>One could argue that</strong> her mistake had been a sentence in the first draft of her brief, a sentence with no hedge in it at all: <em>they avoid conflict here</em>. <strong>More often than not</strong>, she would write later, difficult feedback in that faculty was delivered indirectly &mdash; and <strong>it would appear that</strong> it was the hierarchy, rather than any dislike of conflict, that explained it. <strong>For the most part</strong>, her second brief said the same things as the first. The difference was that this one could be argued with, and so it was read. <strong>What that faculty had needed all along was</strong> not another framework. It was <strong>cultural humility</strong>, and one question nobody had ever asked them: what do <em>you</em> think the problem is?</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Por que a frase &#233; "It was the power distance <strong>that</strong> produced the silence" e n&#227;o "...<strong>what</strong> produced the silence"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque no it-cleft o elo &#233; sempre <strong>that</strong> (ou <strong>who</strong>, para pessoas). O "what" &#233; transfer&#234;ncia direta do portugu&#234;s "foi o que...".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque "what" s&#243; existe em perguntas.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito &#233; abstrato e n&#227;o admite pronome relativo.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "<strong>What she learned that quarter was</strong> not a technique." &mdash; por que N&#195;O se diz "What she learned that quarter <em>it was</em> not a technique"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque "it" nunca pode aparecer numa frase que come&#231;a com "What".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque o wh-cleft <strong>j&#225; tem</strong> o verbo (What ... <strong>was</strong>). Acrescentar "it was" &#233; dizer duas vezes &mdash; &#233; o "o que ela aprendeu... <em>foi</em>" do portugu&#234;s vazando.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito da frase &#233; feminino.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why was the first session a problem <em>because</em> it went beautifully?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the professors had not read the brief before the meeting.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because nobody objected in the room, and she recorded that silence as alignment &mdash; when the disagreement was simply going to arrive later, in writing.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the faculty agreed with the plan and then changed their minds six weeks later.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What made the second brief succeed where the first one failed?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It contained different findings, based on a second round of data.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> It was shorter, and it avoided any comparison between the two cultures.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> It said the same things, but as tendencies with hedging rather than as rules &mdash; so the faculty could argue with it, and therefore read it.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Cleft Sentences &amp; Hedging</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A gram&#225;tica do holofote: a frase se parte em duas para empurrar UM peda&#231;o para a luz &mdash; e o hedging &#233; o que impede que essa luz vire estere&#243;tipo (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">It-cleft<br><strong>It was</strong> + X + <strong>that</strong> / <strong>who</strong></td><td style="padding:.6rem">A faca. Escolhe UMA causa e exclui as outras. Picks the cause, rules the rest out.</td><td style="padding:.6rem"><strong>It was the power distance that</strong> produced the silence, not the language.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Wh-cleft<br><strong>What</strong> + ora&#231;&#227;o + <strong>is / was</strong> + X</td><td style="padding:.6rem">O palco. Segura a sala at&#233; a &#250;ltima palavra. Holds the room, then lands it.</td><td style="padding:.6rem"><strong>What this faculty needs is</strong> to be asked before it is told.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Sempre <strong>It was</strong></td><td style="padding:.6rem">Mesmo com plural. Never "It were".</td><td style="padding:.6rem"><strong>It was</strong> the academic directors <strong>who</strong> pushed back.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Hedging: tend&#234;ncia</td><td style="padding:.6rem">Transforma regra em tend&#234;ncia. Turns a rule into a tendency.</td><td style="padding:.6rem"><strong>More often than not</strong>, feedback here is delivered indirectly.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Hedging: leitura de dado</td><td style="padding:.6rem">Uma interpreta&#231;&#227;o, n&#227;o um veredito. An interpretation, not a verdict.</td><td style="padding:.6rem"><strong>It would appear that</strong> the silence has more to do with hierarchy.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Hedging: abrir e proteger</td><td style="padding:.6rem">Abre a tese e depois a blinda. Opens the claim, then protects it.</td><td style="padding:.6rem"><strong>One could argue that</strong>... &middot; <strong>For the most part</strong>... &middot; <strong>That said, I would be careful not to overgeneralize.</strong></td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Collocation</td><td style="padding:.6rem" colspan="2">take <strong>into</strong> consideration (nunca "take in consideration") &middot; <strong>account for</strong> a factor (nunca "account the factor") &middot; <strong>set out</strong> the expectations (nunca "set the expectations out of") &middot; <strong>bridge</strong> cultural gaps (nunca "make a bridge in the culture")</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1):</strong> no it-cleft o elo &#233; <strong>that</strong>, nunca "what". "It was the power distance <em>what</em> made them silent" &#233; o portugu&#234;s "foi o que" chegando inteiro. Para pessoas, use <strong>who</strong>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> no wh-cleft o verbo j&#225; est&#225; l&#225;. "What surprised me most <em>it was</em> the directness" diz o verbo duas vezes. O certo &#233; "What surprised me most <strong>was</strong> the directness".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Dosagem:</strong> hedging n&#227;o &#233; inseguran&#231;a &mdash; &#233; PRECIS&#195;O. "Brazilians avoid conflict" &#233; um estere&#243;tipo e um doutor derruba em dez segundos. "More often than not, difficult feedback in our Brazilian teams is delivered indirectly" &#233; uma observa&#231;&#227;o, e ele vai discutir com voc&#234; em vez de descartar voc&#234;.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>A combina&#231;&#227;o que voc&#234; quer:</strong> hedge + cleft na MESMA frase. "<strong>It would appear that it was</strong> the power distance, rather than the language, <strong>that</strong> kept them quiet." &#201; a frase mais s&#234;nior desta aula.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Cultural Briefing in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos na ordem em que voc&#234; vai conduzir a primeira sess&#227;o com o time acad&#234;mico canadense.</p>
      <div class="order-container" id="order-l5">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l5')"><span class="order-num">?</span><span class="order-text">Put the real cause under the spotlight: it was the power distance that produced the silence, not agreement.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l5')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l5')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l5')"><span class="order-num">?</span><span class="order-text">Close by handing the room the question nobody has asked them: what do you think the problem is?</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l5')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l5')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l5')"><span class="order-num">?</span><span class="order-text">Set out the expectations on day one: what this session is, what it is not, and what happens with the findings.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l5')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l5')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l5')"><span class="order-num">?</span><span class="order-text">Protect the claim before anyone attacks it: that said, there is more variation inside each country than between them.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l5')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l5')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l5')"><span class="order-num">?</span><span class="order-text">State the observation as a tendency, never as a rule: more often than not, difficult feedback here is delivered indirectly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l5')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l5')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l5')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases da sua primeira sess&#227;o com o time acad&#234;mico canadense, na ordem em que voc&#234; vai dizer.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da sua sess&#227;o com os acad&#234;micos canadenses.</p>
      <div class="quiz-item"><div class="quiz-question">A Canadian professor asks: &ldquo;Are you not at risk of overgeneralizing about two entire countries?&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;You are right. I will remove that part of the brief.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I would be, if I were describing people. I am describing tendencies: more often than not, difficult feedback in our Brazilian teams is delivered indirectly.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;No. The data is very clear about how Brazilians behave.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Nobody objected in the diagnostic session. What do you write in your report?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;It would appear that it was the power distance in the room, rather than agreement, that produced the silence.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;The faculty is fully aligned with the proposed plan.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;The faculty was not interested enough to comment.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses a cleft correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;It was the hierarchy what kept them quiet.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;What surprised me most it was the directness of the feedback.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;It was the academic directors who pushed back, and they did it in writing.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You are asked to summarize your approach to the Canadian division in one sentence. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I will bring the Brazilian culture program and adapt it to the local reality.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;What I am bringing is not a model. It is a diagnosis, and my job is to bridge cultural gaps rather than rank them.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I will observe first and decide later whether we need a strategy at all.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Everyone was invited to the culture session, and three people spoke. What is the correct reading?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The session was inclusive: nobody was excluded from the invitation.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That was a guest list, not inclusive leadership &mdash; and any diagnosis that does not account for who felt safe to speak is measuring the wrong thing.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The other participants had nothing to add, which is normal in academic teams.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">A Canadian director asks you on a video call: how is leading People &amp; Culture in Canada going to be different from what you did in Brazil? Answer as the senior HR leader you are about to become on August 1st. Name two dimensions, hedge both of them, put the real cause under the spotlight with at least two cleft sentences, and use six words from this lesson. End with what you are NOT going to do.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-5"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 5</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-4 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-4'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
