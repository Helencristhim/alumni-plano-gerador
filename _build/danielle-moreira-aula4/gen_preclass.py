#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 4 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 12 termos + 3 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1, 2 e 3
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 4 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
"""
import re
import random

random.seed(4)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Talent retention", "keeping the people you cannot afford to lose, and knowing what it costs when you do not",
     "reten&#231;&#227;o de talentos",
     "Talent retention is not a value. It is a number, and this year the number is four."),
    ("Engagement survey", "the instrument that measures how invested people are in the work",
     "pesquisa de engajamento",
     "The engagement survey had been running for four years, and nobody had ever read it region by region."),
    ("Performance cycle", "the yearly loop of goals, feedback and review a company runs on its people",
     "ciclo de avalia&#231;&#227;o de desempenho",
     "That region has not completed a performance cycle since the pandemic. Nobody noticed."),
    ("Succession planning", "deciding today who is ready to take a critical role tomorrow, before anyone resigns",
     "plano de sucess&#227;o",
     "Succession planning is the question nobody asks until the answer is urgent."),
    ("Employer brand", "what the market says about you as a place to work, when you are not in the room",
     "marca empregadora",
     "Our employer brand is doing our recruiting for us. Unfortunately, it is doing it badly."),
    ("People analytics", "using workforce data to make a people decision defensible in a room full of finance people",
     "an&#225;lise de dados de pessoas",
     "Retention as a value was ignored for four years. Retention as people analytics took eleven minutes."),
    ("Workforce planning", "deciding how many people, with which skills, you will need, and by when",
     "planejamento de quadro de pessoal",
     "Workforce planning is the difference between hiring in September and hiring in a panic in November."),
    ("Change management", "the discipline of taking people through a change they did not ask for",
     "gest&#227;o da mudan&#231;a",
     "Nobody asked for this change. That is not an obstacle to change management. That is change management."),
    ("Psychological contract", "the unwritten expectations between a company and a person, the promises nobody signed",
     "contrato psicol&#243;gico",
     "We never broke her contract. We broke the psychological contract, and she resigned six weeks later."),
    ("Diversity and inclusion", "who is in the room, and whether they can actually speak once they are there",
     "diversidade e inclus&#227;o",
     "Diversity is who you hire. Inclusion is whether they are still speaking in year two."),
    ("Influence without authority", "getting a decision made by people who do not work for you and never will",
     "influenciar sem autoridade formal",
     "Influence without authority is not a soft skill. In that room it is the only skill."),
    ("Employee value proposition", "the deal you offer: what a person actually gets in exchange for joining you and staying",
     "proposta de valor ao colaborador",
     "If our employee value proposition is only the salary, we will lose to whoever pays more."),
    ("To make a compelling case", "to argue something so well that saying no becomes the harder option",
     "construir um argumento irresist&#237;vel",
     "Make a compelling case, and then stop talking. The silence after a strong argument is not awkward."),
    ("To phase out", "to retire an old practice gradually, on purpose, instead of stopping it overnight",
     "descontinuar gradualmente",
     "We phase out the old performance cycle over two quarters. We do not switch it off in one."),
    ("A double-edged sword", "a real advantage that carries a real cost, at the same time",
     "uma faca de dois gumes",
     "Flexible work is a double-edged sword: it widens the talent pool and it weakens the informal culture."),
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
    ("Never", "have I seen",
     "Dica: invers&#227;o &mdash; depois de Never o auxiliar vem ANTES do sujeito (ordem de pergunta)",
     "Never have I seen a people strategy succeed without an owner in the room.",
     "a people strategy succeed without an owner in the room."),
    ("Not only", "did we redesign",
     "Dica: depois de Not only entra DID + verbo na FORMA BASE (redesign, nunca redesigned)",
     "Not only did we redesign the performance cycle, but we also rebuilt the onboarding.",
     "the performance cycle, but we also rebuilt the onboarding."),
    ("Hardly", "had we launched",
     "Dica: Hardly + HAD + sujeito + partic&#237;pio, e a segunda metade abre com when",
     "Hardly had we launched the pilot when the engagement scores began to rise.",
     "the pilot when the engagement scores began to rise."),
    ("Only when the directors owned the plan", "did it start",
     "Dica: Only when + ora&#231;&#227;o &mdash; a invers&#227;o cai na SEGUNDA metade da frase",
     "Only when the directors owned the plan did it start to move.",
     "to move."),
    ("What the data", "shows us is",
     "Dica: cleft de apresenta&#231;&#227;o &mdash; o dado antes da opini&#227;o",
     "What the data shows us is that one senior departure costs us eleven months of hiring.",
     "that one senior departure costs us eleven months of hiring."),
    ("I would like to", "draw your attention to",
     "Dica: collocation de apresenta&#231;&#227;o &mdash; nunca 'call your attention for'",
     "I would like to draw your attention to our succession coverage: two of nine critical roles.",
     "our succession coverage: two of nine critical roles."),
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
    ("What the data shows us is that one senior departure costs us eleven months of hiring.",
     "O que os dados nos mostram &#233; que uma sa&#237;da s&#234;nior nos custa onze meses de contrata&#231;&#227;o."),
    ("I would like to draw your attention to our succession coverage: two of nine critical roles.",
     "Eu gostaria de chamar a aten&#231;&#227;o de voc&#234;s para a nossa cobertura de sucess&#227;o: dois de nove cargos cr&#237;ticos."),
    ("Never have I seen a people strategy succeed without an owner in the room.",
     "Nunca vi uma estrat&#233;gia de pessoas dar certo sem um respons&#225;vel dentro da sala."),
    ("Flexible work is a double-edged sword, and I would rather manage it than deny it.",
     "O trabalho flex&#237;vel &#233; uma faca de dois gumes, e eu prefiro gerenciar isso a negar."),
    ("What this means in practice is one owner per pillar, one metric, and a review in ninety days.",
     "O que isso significa na pr&#225;tica &#233; um respons&#225;vel por pilar, uma m&#233;trica e uma revis&#227;o em noventa dias."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-4">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 04 -- Pre-class</div>
      <h3>Influencing Without Authority -- Presenting Your People Strategy to Canadian Leadership</h3>
      <div class="lesson-desc">Apresentar a estrat&#233;gia de pessoas a cinco l&#237;deres canadenses que N&#195;O se reportam a voc&#234;: abrir pelo dado, responder o custo com o custo de n&#227;o fazer nada, nomear o trade-off antes que a sala o nomeie, e sair da reuni&#227;o com um dono para cada pilar. Key words: talent retention, engagement survey, performance cycle, succession planning, employer brand, people analytics, workforce planning, change management, psychological contract, diversity and inclusion, influence without authority, employee value proposition, to make a compelling case, to phase out, a double-edged sword. Structure: invers&#227;o para &#234;nfase (Never have I seen... / Not only did we..., but we also... / Hardly had we... when...) + linguagem de apresenta&#231;&#227;o executiva (What the data shows us is... / I would like to draw your attention to... / The rationale behind this approach is... / What this means in practice is...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. Este &#233; o vocabul&#225;rio em que uma estrat&#233;gia de pessoas &#233; escrita &mdash; e o &#250;nico em que um board canadense est&#225; disposto a financiar uma.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l4">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>When Marina Ortiz joined the Halden Group as its first Director of People and Culture, she was given a title, almost no budget, and no authority whatsoever. The five regional directors did not report to her, they had built the company, and they had never once been asked to adopt a people strategy written by somebody who had been in the building for six weeks. Her predecessor had presented a beautiful framework to the board, had watched it approved, and had watched nothing happen afterwards. The plan was never rejected. It was simply never carried by anyone. <strong>Influence without authority</strong> was not a soft skill in that room. It was the only skill available to her.</p>
        <p style="margin-top:.8rem">So Marina spent a quarter inside the numbers before she proposed anything. The <strong>engagement survey</strong> had been running for four years, and nobody had ever read it region by region. When she did, the story stopped being about culture and started being about money: one region was losing its senior teachers at three times the rate of the others, every departure was costing eleven months of hiring, and that region had not completed a <strong>performance cycle</strong> since the pandemic. <strong>Talent retention</strong>, presented as a value, had been ignored for four years. Talent retention, presented as <strong>people analytics</strong>, took eleven minutes.</p>
        <p style="margin-top:.8rem">The board adopted her strategy in a single meeting. <strong>Never had</strong> she seen a plan survive because it was right; plans survive because somebody in the room decides to carry them. So she made <strong>a compelling case</strong>, and then she named the trade-off before anyone else could. <strong>Not only did</strong> the flexible model widen the talent pool, she told them, <strong>but it also</strong> weakened the informal culture that had held the company together for twenty years. It was <strong>a double-edged sword</strong>, and she intended to manage it rather than deny it. <strong>Hardly had</strong> she finished <strong>when</strong> the regional director who had quietly killed her predecessor's framework asked to own the first pilot.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Por que a frase &#233; "Never had she seen a plan survive" e n&#227;o "Never she had seen a plan survive"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque, quando a palavra de &#234;nfase (Never) vai para a frente, a frase pega emprestada a <strong>ordem de pergunta</strong>: o auxiliar vem ANTES do sujeito.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque &#233; uma pergunta ret&#243;rica disfar&#231;ada.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque o sujeito &#233; feminino e vem depois do verbo.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "Not only <strong>did</strong> the flexible model <strong>widen</strong> the talent pool..." &mdash; por que <em>widen</em> e n&#227;o <em>widened</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque a frase est&#225; no presente.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque o <strong>did</strong> j&#225; carrega o passado &mdash; o verbo principal volta para a <strong>forma base</strong>, exatamente como em "Did you widen it?".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque depois de "not only" o verbo nunca &#233; conjugado.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why did the previous framework fail?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The board rejected it because it was badly written.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The board approved it, and then nobody in the room ever carried it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The regional directors were never shown the framework at all.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What made the board adopt Marina's strategy, according to the text?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Her authority over the five regional directors.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The fact that her strategy was more correct than her predecessor's.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> She argued it with data, named the trade-off first, and somebody in the room decided to carry it.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Inversion for Emphasis</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A gram&#225;tica do peso: a palavra de &#234;nfase vai para a FRENTE da frase e o verbo auxiliar passa na frente do sujeito, como numa pergunta &mdash; mas n&#227;o &#233; pergunta, &#233; autoridade (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Never / Rarely / At no point<br>+ auxiliar + sujeito</td><td style="padding:.6rem">Convic&#231;&#227;o. Voc&#234; p&#245;e a sua carreira inteira atr&#225;s de uma afirma&#231;&#227;o. Conviction.</td><td style="padding:.6rem"><strong>Never have I seen</strong> a strategy succeed without an owner.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Not only + <strong>did</strong> + sujeito + verbo base<br>..., but ... also ...</td><td style="padding:.6rem">Escala. Duas conquistas num f&#244;lego s&#243;, sem virar lista. Scale.</td><td style="padding:.6rem"><strong>Not only did we redesign</strong> the cycle, <strong>but we also</strong> rebuilt the onboarding.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Hardly / Scarcely + <strong>had</strong><br>+ sujeito + partic&#237;pio + <strong>when</strong></td><td style="padding:.6rem">Velocidade. O resultado chegou antes da d&#250;vida. Speed.</td><td style="padding:.6rem"><strong>Hardly had we launched</strong> the pilot <strong>when</strong> the scores rose.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Only when / Only after<br>+ ora&#231;&#227;o + auxiliar + sujeito</td><td style="padding:.6rem">Condi&#231;&#227;o &#250;nica. S&#243; assim, e de nenhum outro jeito. The only condition.</td><td style="padding:.6rem"><strong>Only when they owned it did</strong> the plan move.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negativa</td><td style="padding:.6rem">A pr&#243;pria invers&#227;o J&#193; &#233; a negativa &mdash; nunca acrescente "not"</td><td style="padding:.6rem"><strong>At no point was</strong> succession planning discussed. (nunca "was not")</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">Invers&#227;o &#233; recurso de AFIRMA&#199;&#195;O. Em pergunta, use a ordem normal.</td><td style="padding:.6rem">Have you <strong>ever</strong> seen a plan survive without an owner?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Presentation language</td><td style="padding:.6rem" colspan="2"><strong>What the data shows us is...</strong> (o que os dados nos mostram &#233;...) &middot; <strong>I would like to draw your attention to...</strong> (eu gostaria de chamar a aten&#231;&#227;o de voc&#234;s para...) &middot; <strong>The rationale behind this approach is...</strong> (a raz&#227;o por tr&#225;s dessa abordagem &#233;...) &middot; <strong>What this means in practice is...</strong> (o que isso significa na pr&#225;tica &#233;...)</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1):</strong> depois da palavra de &#234;nfase, o sujeito N&#195;O pode vir antes do auxiliar. "Never <em>I have</em> seen" est&#225; errado &mdash; o certo &#233; "Never <strong>have I</strong> seen". A frase pega a ordem da pergunta, e s&#243; a ordem: nada de ponto de interroga&#231;&#227;o.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> se a frase original n&#227;o tem auxiliar, o ingl&#234;s <strong>empresta um</strong>: <em>We redesigned it</em> &rarr; "Not only <strong>did</strong> we <strong>redesign</strong> it". E o verbo principal volta &#224; forma base (redesign, nunca redesigned).</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Dosagem:</strong> invers&#227;o &#233; tempero, n&#227;o o prato. <strong>Duas ou tr&#234;s</strong> numa apresenta&#231;&#227;o de dez minutos soam a autoridade. <strong>Seis</strong> soam a teatro &mdash; e a sala p&#225;ra de ouvir o argumento para ouvir a performance.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Collocation:</strong> em ingl&#234;s &#233; <strong>make</strong> a compelling case (nunca "do a case"), <strong>draw</strong> your attention <strong>to</strong> (nunca "call your attention for"), e <strong>phase out</strong> a practice (nunca "phase off").</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Board Presentation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos da apresenta&#231;&#227;o na ordem em que voc&#234; vai conduzi-la diante da lideran&#231;a canadense.</p>
      <div class="order-container" id="order-l4">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l4')"><span class="order-num">?</span><span class="order-text">Name the trade-off yourself, before the room does: it is a double-edged sword, and here is how I manage it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l4')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l4')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l4')"><span class="order-num">?</span><span class="order-text">Open with the data, never with the belief: what the data shows us is that one senior departure costs eleven months of hiring.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l4')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l4')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l4')"><span class="order-num">?</span><span class="order-text">Close with the ask: one owner per pillar, one metric, and a review in ninety days.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l4')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l4')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l4')"><span class="order-num">?</span><span class="order-text">Draw their attention to the hole: succession coverage, two of nine critical roles.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l4')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l4')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l4')"><span class="order-num">?</span><span class="order-text">Answer the cost objection with the cost of doing nothing, in people analytics, and let them read both numbers.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l4')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l4')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l4')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases da sua apresenta&#231;&#227;o de 1&#186; de agosto, na ordem em que voc&#234; vai dizer.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da sua apresenta&#231;&#227;o ao board canadense.</p>
      <div class="quiz-item"><div class="quiz-question">You have one slide and a board that only wants to talk about cost. How do you open?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "People are our greatest asset, and I believe culture is what makes this company different."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "What the data shows us is that one senior departure costs us eleven months of hiring, and we have had four this year."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I would like to start by thanking everyone for the opportunity to be here today."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The CFO says retention is a problem for a good year, not for a year of budget cuts. The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I would not argue with the budget. Not only did our last two departures cost us eleven months of hiring, but they also took the succession plan with them &mdash; that is the cost of doing nothing."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I understand. Perhaps we can revisit the people strategy next year, then."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "But retention is about our values, and our values cannot have a budget line."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses inversion correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Not only we redesigned the performance cycle, but we also rebuilt the onboarding."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Never I have seen a people strategy succeed without an owner."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Hardly had we launched the pilot when the engagement scores began to rise."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Two directors will say the flexible model is destroying the culture they built. What do you do?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Avoid the subject. If nobody raises it, you do not have to defend it.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Name it first: "Flexible work is a double-edged sword &mdash; it widened our talent pool and it weakened the informal culture. I intend to manage that, not deny it."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Tell them the data proves they are wrong about the culture.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Nobody in the room reports to you. What is the only way your strategy actually gets carried?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Getting the board to approve it formally, in writing, before anyone leaves the room.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Escalating to headquarters in Brazil whenever a director resists.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Making a compelling case and then asking one of them to own the first pilot &mdash; approval is not adoption.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">It is August first. You are presenting your People &amp; Culture strategy for Maple Bear Canada to five leaders, and not one of them reports to you. Open with what the data shows, draw their attention to the gap, answer the cost objection with the cost of doing nothing, name one trade-off before they do, and close by asking each of them to own something. Use at least two inversions and six words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-4"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 4</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-3 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-3'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
