#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 6 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1, 2, 3, 4 e 5
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 6 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(6)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Cultural assessment", "a structured study of how an organization actually works, rather than how it says it works",
     "avalia&#231;&#227;o cultural",
     "A cultural assessment does not ask people to describe the culture. It puts the culture in a position where it has to show itself."),
    ("Diagnostic tool", "the instrument you choose to see with: a questionnaire, an interview protocol, a focus group",
     "instrumento de diagn&#243;stico",
     "The diagnostic tool is never neutral. Choose the wrong one and you will collect politeness and call it data."),
    ("Baseline", "the measurement you take before you change anything, so that later you can prove what moved",
     "linha de base / medi&#231;&#227;o inicial",
     "Have the baseline taken in September. Without it, every improvement in March is just your opinion."),
    ("Response rate", "the share of people who actually answered, and the first thing a skeptical room will attack",
     "taxa de resposta",
     "Thirty-one percent is not a technical failure. The response rate is the first finding."),
    ("Focus group", "a small room, a facilitator, and the sentences a questionnaire can never capture",
     "grupo focal",
     "A survey tells you how many. A focus group tells you why, and it tells you in ninety minutes."),
    ("Trust index", "a single number that tracks whether people believe what leadership tells them",
     "&#237;ndice de confian&#231;a",
     "Whatever the trust index comes back as, it will be lower than the leadership team believes."),
    ("Root cause", "the thing underneath the symptom, and the only thing worth fixing",
     "causa raiz",
     "Attrition is not a root cause. It is what a root cause looks like nine months later."),
    ("Gap analysis", "the distance between where the culture is today and where the strategy needs it to be",
     "an&#225;lise de lacunas",
     "The gap analysis is the only slide the board will remember, because it is the only one with a distance on it."),
    ("Findings", "what the data actually says, before anyone decides what to do about it",
     "achados / resultados",
     "Nobody in that faculty was ever told what the findings were. That is why they will not answer you now."),
    ("Benchmark", "an external number you compare yourself to, so that good stops being an opinion",
     "refer&#234;ncia externa / par&#226;metro",
     "Sixty-two means nothing on its own. Against the education benchmark of seventy-one, it means a great deal."),
    ("To run a diagnostic", "to put an organization through a structured examination before prescribing anything",
     "conduzir um diagn&#243;stico",
     "We are not here to run a diagnostic on you. We are here to run one with you."),
    ("To gather insights", "to collect what people mean, not only what they answered",
     "colher percep&#231;&#245;es",
     "The survey gathers numbers. The focus groups are where we gather insights."),
    ("To surface an issue", "to bring a problem out into the open, where the room can finally work on it",
     "trazer um problema &#224; tona",
     "A good focus group does not collect opinions. It surfaces the issue that everybody already knew about."),
    ("To come up with", "to produce an idea or a framework, usually under pressure",
     "criar / bolar (uma ideia, um modelo)",
     "Give me three weeks and I will come up with an instrument this faculty will actually answer."),
    ("To open a can of worms", "to raise one question that releases a dozen you did not plan for",
     "abrir uma caixa de Pandora",
     "I know I am opening a can of worms. I would rather open it on a Thursday than read it in an exit interview in March."),
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
    ("We had the questionnaire", "designed",
     "Dica: causativa passiva &mdash; have + OBJETO + particípio. O particípio vem DEPOIS do objeto",
     "We had the questionnaire designed by an external specialist.",
     "by an external specialist."),
    ("I am", "having",
     "Dica: a causativa tamb&#233;m vive no cont&#237;nuo &mdash; I am HAVING the focus groups facilitated",
     "I am having the focus groups facilitated in-house.",
     "the focus groups facilitated in-house."),
    ("Our goal is to have the baseline", "completed",
     "Dica: o padr&#227;o de prazo &mdash; to have + X + COMPLETED by + data",
     "Our goal is to have the baseline completed before we change anything.",
     "before we change anything."),
    ("I had Marc", "review",
     "Dica: have + PESSOA + verbo na forma base. NUNCA 'to review'",
     "I had Marc review the questions before they went out.",
     "the questions before they went out."),
    ("The data would", "suggest that",
     "Dica: hedging de leitura de dado &mdash; the data would SUGGEST THAT (nunca 'the data suggests strongly')",
     "The data would suggest that the response rate is itself the first finding.",
     "the response rate is itself the first finding."),
    ("Attrition is not a", "root cause",
     "Dica: o sintoma n&#227;o &#233; a causa &mdash; e a express&#227;o &#233; sempre no singular aqui",
     "Attrition is not a root cause. It is what a root cause looks like nine months later.",
     ". It is what a root cause looks like nine months later."),
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
    ("We had the questionnaire designed by an external specialist, and I had it reviewed in-house.",
     "Mandamos desenhar o question&#225;rio por um especialista externo, e eu mandei revis&#225;-lo internamente."),
    ("Our goal is to have the baseline completed before we change anything.",
     "Nosso objetivo &#233; ter a medi&#231;&#227;o inicial conclu&#237;da antes de mudarmos qualquer coisa."),
    ("The data would suggest that the response rate is itself the first finding.",
     "Os dados sugeririam que a pr&#243;pria taxa de resposta j&#225; &#233; o primeiro achado."),
    ("Attrition is not a root cause. It is what a root cause looks like nine months later.",
     "O turnover n&#227;o &#233; a causa raiz. &#201; a apar&#234;ncia de uma causa raiz nove meses depois."),
    ("I know I am opening a can of worms, and I would rather surface it now than read it in an exit interview.",
     "Sei que estou abrindo uma caixa de Pandora, e prefiro trazer isso &#224; tona agora a ler numa entrevista de desligamento."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-6">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 06 -- Pre-class</div>
      <h3>Diagnosing Culture -- Running a Cultural Assessment with the Canadian Team</h3>
      <div class="lesson-desc">Conduzir a avalia&#231;&#227;o cultural com o time canadense &mdash; e defender o instrumento diante de uma sala que j&#225; foi pesquisada uma vez e nunca soube o resultado: escolher a ferramenta, medir a linha de base antes de mudar qualquer coisa, e devolver os achados. Key words: cultural assessment, diagnostic tool, baseline, response rate, focus group, trust index, root cause, gap analysis, findings, benchmark, to run a diagnostic, to gather insights, to surface an issue, to come up with, to open a can of worms. Structure: causative passive (We had the questionnaire designed by... / I am having the focus groups facilitated... / Our goal is to have the baseline completed by...) + hedging de dado (The data would suggest that... / To some extent, the findings indicate...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. &#201; o vocabul&#225;rio do deck que a lideran&#231;a canadense l&#234; &mdash; a partir de setembro, &#233; o deck que voc&#234; escreve.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l6">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Every People and Culture leader who arrives in a new division wants to <strong>run a diagnostic</strong>. Very few of them stop to ask what a diagnostic does to the people being diagnosed. The <strong>diagnostic tool</strong> is never neutral. The moment a questionnaire lands in an inbox, the organization starts answering a question nobody wrote: is it safe to be honest here?</p>
        <p style="margin-top:.8rem">This is why the <strong>response rate</strong> is the first <strong>finding</strong>, and not a footnote. A team that has had its opinion collected before and was never told the outcome will answer at thirty percent &mdash; and the thirty percent who do answer are not a random sample. They are the angriest and the most loyal, and the middle of the organization is missing from the data. <strong>The data would suggest that</strong> a low response rate is not a technical failure at all. It is a <strong>trust index</strong> with no survey attached to it.</p>
        <p style="margin-top:.8rem">So the sequence matters more than the instrument. <strong>Have the baseline taken</strong> before you change anything, so that in March you can prove what moved instead of arguing about it. <strong>Have the expectations set out</strong> in writing before the first question is asked: who reads the <strong>findings</strong>, when, and what happens to them. One director in Toronto <strong>had the questionnaire designed</strong> by an external specialist and then <strong>had it reviewed</strong> by two people inside her own building, precisely so that the faculty could not dismiss it as a document written somewhere else. <strong>To some extent, the findings indicate</strong> that this single decision did more for her response rate than the questions ever did.</p>
        <p style="margin-top:.8rem">And when the results arrive, resist the symptom. Attrition is not a <strong>root cause</strong>; it is what a root cause looks like nine months later. A good <strong>focus group</strong> will not collect opinions &mdash; it will <strong>surface issues</strong> that have been quiet for a decade, and some of them will not be culture problems at all. You will <strong>open a can of worms</strong>. The <strong>gap analysis</strong> you present to the board will be clean; the room you leave behind will not. That is not a reason to skip the assessment. It is a reason to <strong>come up with</strong> a plan for the second week, and not only for the first.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Por que se diz "We <strong>had the questionnaire designed</strong> by a specialist" e n&#227;o "We <strong>had designed the questionnaire</strong> by a specialist"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque na causativa passiva o particípio vem <strong>depois</strong> do objeto (have + objeto + particípio). "We had designed" &#233; past perfect e significa que N&#211;S desenhamos.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque "design" n&#227;o admite voz passiva em ingl&#234;s.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito &#233; plural e exige invers&#227;o.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "I <strong>had Marc review</strong> the questions." &mdash; por que N&#195;O se diz "I had Marc <em>to review</em> the questions"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque "review" &#233; substantivo nessa posi&#231;&#227;o.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque depois de <strong>have + pessoa</strong> o verbo vem na forma base, sem "to". O "to" &#233; o portugu&#234;s "mandei ELE revisar" vazando.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque Marc &#233; nome pr&#243;prio e nomes pr&#243;prios n&#227;o levam infinitivo depois.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why is a low response rate a <em>finding</em> rather than a technical failure?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because the questionnaire was too long and people gave up halfway through it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because a team that was asked once and never told the outcome answers at thirty percent &mdash; so the rate is a trust index with no survey attached to it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because thirty percent is statistically sufficient for any cultural assessment.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What does the Toronto director's decision (an external specialist, then an in-house review) actually buy her?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A cheaper instrument, because the review work was not paid for.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> A shorter questionnaire, because two reviewers cut half of the questions.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Credibility &mdash; the faculty could not dismiss the survey as a document written somewhere else, and the text says it did more for the response rate than the questions did.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Causative Passive &amp; Hedging Data</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A gram&#225;tica de quem MANDA fazer: o sujeito n&#227;o executa a a&#231;&#227;o, mas responde por ela &mdash; que &#233; exatamente a posi&#231;&#227;o de uma gestora de People &amp; Culture (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Causativa passiva<br><strong>have</strong> + objeto + <strong>particípio</strong></td><td style="padding:.6rem">Voc&#234; mandou fazer; outra pessoa executou. You arranged it, someone else performed it.</td><td style="padding:.6rem">We <strong>had the questionnaire designed</strong> by an external specialist.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Causativa ativa<br><strong>have</strong> + pessoa + <strong>verbo base</strong></td><td style="padding:.6rem">Voc&#234; nomeia quem voc&#234; acionou. Sem "to". Never "to review".</td><td style="padding:.6rem">I <strong>had Marc review</strong> the questions before they went out.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Padr&#227;o de prazo<br><strong>to have</strong> + X + <strong>completed by</strong></td><td style="padding:.6rem">O compromisso de entrega, sem prometer quem faz o qu&#234;.</td><td style="padding:.6rem">Our goal is <strong>to have the baseline completed by</strong> the end of September.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>get</strong> no lugar de <strong>have</strong></td><td style="padding:.6rem" colspan="2">Mesma estrutura, menos formal, e sugere esfor&#231;o: "I finally <strong>got</strong> the 2024 data <strong>re-coded</strong>." Use <strong>have</strong> com o board; <strong>get</strong> com o time.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Passiva comum vs causativa</td><td style="padding:.6rem" colspan="2">"The survey <strong>was designed</strong> by a consultant" diz quem digitou &mdash; e apaga voc&#234;. "We <strong>had</strong> the survey <strong>designed</strong>" diz quem DECIDIU. Numa sala de diagn&#243;stico, ningu&#233;m pergunta quem digitou.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Hedging de dado</td><td style="padding:.6rem">Uma leitura do dado, n&#227;o um veredito. An interpretation, not a verdict.</td><td style="padding:.6rem"><strong>The data would suggest that</strong>... &middot; <strong>To some extent, the findings indicate</strong>...</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Collocation</td><td style="padding:.6rem" colspan="2"><strong>run</strong> a diagnostic &middot; <strong>gather</strong> insights &middot; <strong>surface</strong> an issue &middot; come up <strong>with</strong> a framework (nunca "come up a framework") &middot; <strong>open</strong> a can of worms</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1):</strong> a ORDEM. Em portugu&#234;s o verbo vem antes do objeto ("mandamos desenhar o question&#225;rio"); em ingl&#234;s o particípio vem DEPOIS ("had <em>the questionnaire</em> designed"). "We had designed the questionnaire" &#233; past perfect &mdash; significa que voc&#234; mesma o desenhou.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> nada de "to" depois de <strong>have + pessoa</strong>. "I had Marc <em>to review</em>" &#233; o "mandei ele revisar" chegando inteiro. O certo &#233; "I had Marc <strong>review</strong>".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>A combina&#231;&#227;o que voc&#234; quer:</strong> causativa + hedge na MESMA frase. "<strong>The data would suggest that</strong> we should <strong>have the baseline taken</strong> before September, rather than after." &#201; a frase mais s&#234;nior desta aula.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Assessment in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos na ordem em que voc&#234; vai conduzir a avalia&#231;&#227;o cultural com o time canadense.</p>
      <div class="order-container" id="order-l6">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l6')"><span class="order-num">?</span><span class="order-text">Go deeper: have the focus groups facilitated in-house, and gather the insights the survey could not capture.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l6')"><span class="order-num">?</span><span class="order-text">Read the findings back to the faculty first, before the board sees them, exactly as you promised in week one.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l6')"><span class="order-num">?</span><span class="order-text">Set out in writing who reads the findings and what happens to them, before a single question goes out.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l6')"><span class="order-num">?</span><span class="order-text">Run the gap analysis and look for the root cause underneath the symptom, not the attrition number itself.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l6')"><span class="order-num">?</span><span class="order-text">Have the baseline taken before you change anything, so that in March you can prove what actually moved.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l6')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases do seu kickoff de diagn&#243;stico com o time canadense.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da sua avalia&#231;&#227;o cultural no Canad&#225;.</p>
      <div class="quiz-item"><div class="quiz-question">A Canadian director asks: &ldquo;Who wrote this questionnaire? If it came from Brazil, we will see it in the first line.&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;It was written by our team in Brazil, but we adapted it for you.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;We had the questionnaire designed by an external specialist here, and I had it reviewed by two people in this building before it went out.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I do not think it matters who wrote it, as long as the questions are good.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Only thirty-one percent of the faculty answered the survey. What do you say to the leadership team?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;The data would suggest that the response rate is itself the first finding: a team that was asked once and never told the outcome answers at thirty.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;The survey failed. We should send it again next month with a reminder.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Thirty-one percent is enough. I will present the results as if the whole faculty had answered.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the causative correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;We had designed the survey by an external specialist.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;I had the consultant to present the findings to the faculty.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;I am having the focus groups facilitated in-house, and I had Marc review the questions first.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The board says: &ldquo;Attrition is up nine points. That is the culture problem.&rdquo; You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Agreed. I will build a retention program and present it next month.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Attrition is not a root cause. It is what a root cause looks like nine months later, and what I want to bring you is the thing underneath it.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;The number is high, but it is probably a coincidence of this quarter.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Marc warns you that the focus groups will bring up a decade of quiet resentment. What is the senior reading?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Cancel the focus groups and keep the assessment to the anonymous survey only.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I know I am opening a can of worms. I would rather surface it now, on a Thursday, than read it in an exit interview in March &mdash; so I have a plan for the second week, not only the first.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Run them anyway and leave the resentment out of the findings, because it is not strictly a culture issue.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">You are opening the diagnostic kickoff with the Canadian academic team. In two minutes: explain what cultural assessment you plan to have carried out, who arranged each part of it, when the baseline is taken, what you expect to find, and what happens to the findings. Use at least two causative structures, one hedge on a number, and six words from this lesson. End by naming the resistance you already know is in the room.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-6"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 6</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-5 pode voltar como vocab card ----------
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
    'cultural intelligence', 'high-context culture', 'low-context culture', 'power distance',
    'individualism and collectivism', 'indirect communication', 'assertiveness',
    'cultural humility', 'work-life integration', 'inclusive leadership',
    'to bridge cultural gaps', 'to read between the lines', 'to account for', 'to set out',
    'to take into consideration',
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-5'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
