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

# ---------- Stage 1.5 fill-in-the-blank (as 4 formas de participle clause) ----------
BLANKS = [
    ("", "Having reviewed",
     "Dica: perfect participle (having + partic&#237;pio) = a a&#231;&#227;o que veio ANTES. Nunca 'Having review'",
     "Having reviewed the focus groups, I would propose that we build on them rather than start again.",
     "the focus groups, I would propose that we build on them rather than start again."),
    ("The trust index came back at fifty-eight,", "leaving",
     "Dica: present participle (-ing) para o RESULTADO da a&#231;&#227;o anterior. Nunca 'and it left'",
     "The trust index came back at fifty-eight, leaving us nine points below the benchmark.",
     "us nine points below the benchmark."),
    ("", "Asked",
     "Dica: past participle para sentido PASSIVO ('Quando foram perguntados...'). Nunca 'Asking'",
     "Asked about the timeline, most of the faculty said exactly the same thing.",
     "about the timeline, most of the faculty said exactly the same thing."),
    ("", "Given",
     "Dica: abertura fixa 'Given + substantivo' = 'Considerando / Diante de'",
     "Given the response rate, the caveat belongs on the first slide, not the last.",
     "the response rate, the caveat belongs on the first slide, not the last."),
    ("", "Based on",
     "Dica: abertura fixa 'Based on + substantivo' = 'Com base em'. E o participio se refere ao SUJEITO da frase",
     "Based on the preliminary findings, I am proposing two quick wins and one long piece of work.",
     "the preliminary findings, I am proposing two quick wins and one long piece of work."),
    ("Three teams asked to join without being invited,", "suggesting",
     "Dica: present participle para o que a a&#231;&#227;o SUGERE / produz. Nunca 'what suggests'",
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

HTML = f'''<div class="lesson-card" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 08 -- Pre-class</div>
      <h3>Midpoint Review -- Consolidating HR Leadership Language for Canada</h3>
      <div class="lesson-desc">Meio do caminho: a aula em que voc&#234; para, faz um balan&#231;o e APRESENTA o que encontrou &mdash; sem inflar o que deu certo e sem enterrar o que ficou aqu&#233;m. Toda a lingua das aulas 1 a 7 volta aqui como REVIS&#195;O (causative passive, cleft, invers&#227;o, third conditional, reporting verbs, hedging), dentro de uma &#250;nica apresenta&#231;&#227;o executiva. Key words: takeaway, caveat, rationale, trade-off, traction, quick win, roadblock, track record, preliminary, tangible, to take stock of, to fall short of, to build on, to iron out, the jury is still out. Structure (NOVA): participle clauses &mdash; a gram&#225;tica do sum&#225;rio executivo (Having reviewed the findings... / ...leaving us nine points below the benchmark / Asked about the timeline... / Given the response rate...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="8" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="8">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. Este &#233; o vocabul&#225;rio de quem apresenta um balan&#231;o &mdash; e sobrevive &#224;s perguntas que v&#234;m depois dele.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l8">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Mariana Vidal had twenty-two slides and eleven minutes, and she lost the room on slide three. <strong>Having spent</strong> six months on the most careful cultural work of her career, she opened the midpoint review by explaining her methodology. By the time she arrived at what she had actually found, the Chief Operating Officer had stopped taking notes. The work was excellent. The review was a failure, and the two facts have nothing to do with each other.</p>
        <p style="margin-top:.8rem">The mistake was not nerves, and it was not her English. It was sequence. A senior room does not want the journey; it wants the <strong>takeaway</strong>, and it wants it first. <strong>Asked</strong> afterwards what he had needed, the COO was blunt: one <strong>tangible</strong> number, the <strong>rationale</strong> behind her recommendation, and the <strong>caveat</strong> she was clearly holding back. <strong>Given</strong> eleven minutes, he said, spend one of them telling me what you found and ten defending it.</p>
        <p style="margin-top:.8rem">She rebuilt the deck in a single evening. The new version opened with a sentence, not a slide: the culture here is not broken, it is unheard, and the response rate is the proof. Then the number, then the <strong>trade-off</strong>. <strong>Based on</strong> the <strong>preliminary</strong> findings, she proposed two <strong>quick wins</strong> and one long piece of work, naming what each would cost. She said out loud that the survey had <strong>fallen short of</strong> the target she had promised in June, <strong>leaving</strong> her with a smaller sample than she had wanted &mdash; and that she would rather report that than bury it. On the new onboarding, she said, the <strong>jury is still out</strong>: ask me again in March.</p>
        <p style="margin-top:.8rem">The COO approved the plan in four minutes. What convinced him was not the confidence. It was the <strong>caveat</strong>. A leader who names the limit of her own data is a leader whose numbers can be trusted the next time she brings some &mdash; and that, more than any single result, is how a <strong>track record</strong> begins.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. "<strong>Having spent</strong> six months on the work, she opened by explaining her methodology." &mdash; o que o perfect participle (<em>having</em> + partic&#237;pio) est&#225; dizendo aqui?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Que as duas a&#231;&#245;es aconteceram ao mesmo tempo: ela gastou seis meses enquanto abria a apresenta&#231;&#227;o.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Que a a&#231;&#227;o do participle veio <strong>ANTES</strong> da outra: primeiro os seis meses de trabalho, depois a abertura. &#201; a forma de empacotar a hist&#243;ria toda numa or&#231;&#227;o subordinada e ir direto ao ponto.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Que ela ainda est&#225; gastando os seis meses, porque <em>having</em> indica presente cont&#237;nuo.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "<strong>Asked</strong> afterwards what he had needed, the COO was blunt." &mdash; por que <em>Asked</em> e n&#227;o <em>Asking</em>?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque o sujeito (o COO) <strong>SOFRE</strong> a a&#231;&#227;o: algu&#233;m perguntou A ELE. Participle passivo = past participle. "Asking" significaria que era ELE quem perguntava.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque depois de v&#237;rgula o ingl&#234;s sempre exige past participle.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque "ask" &#233; um verbo irregular e n&#227;o aceita a forma -ing.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. According to the text, why exactly did Mariana lose the room on slide three?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because her English was not precise enough for a senior Canadian audience.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because of sequence: she opened with her methodology instead of her takeaway, and by the time she reached what she had found, the COO had stopped listening.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the cultural work itself was weak, and the room could see it immediately.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. What actually convinced the COO to approve the plan in four minutes?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Her confidence, and the fact that she never admitted any weakness in the data.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The two quick wins, which meant the project would show results before December.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> The caveat &mdash; because a leader who names the limit of her own data is a leader whose numbers can be trusted the next time, and that is where a track record begins.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Participle Clauses</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A gram&#225;tica do sum&#225;rio executivo: ela pega DUAS frases e transforma a menos importante numa or&#231;&#227;o curta, sem sujeito e sem conectivo &mdash; deixando a frase principal com todo o peso. &#201; o que separa quem NARRA de quem RESUME (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. Perfect participle<br><strong>Having</strong> + partic&#237;pio</td><td style="padding:.6rem">A a&#231;&#227;o que veio ANTES. Empacota o passado inteiro em cinco palavras. <em>The action that came first.</em></td><td style="padding:.6rem"><strong>Having reviewed</strong> the findings, I would propose two quick wins.<br><span style="color:var(--text-dim)">= After I reviewed the findings, I would propose...</span></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. Present participle<br>verbo + <strong>-ing</strong></td><td style="padding:.6rem">O RESULTADO ou a consequ&#234;ncia da frase principal. Vem quase sempre DEPOIS da v&#237;rgula. <em>The result of what you just said.</em></td><td style="padding:.6rem">The index came back at fifty-eight, <strong>leaving</strong> us nine points below the benchmark.<br><span style="color:var(--text-dim)">= ...and this left us nine points below.</span></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. Past participle<br>partic&#237;pio sozinho</td><td style="padding:.6rem">Sentido PASSIVO: o sujeito SOFRE a a&#231;&#227;o. <em>Something was done TO the subject.</em></td><td style="padding:.6rem"><strong>Asked</strong> about the timeline, most of the faculty said the same thing.<br><span style="color:var(--text-dim)">= When they were asked about the timeline...</span></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. Aberturas fixas<br><strong>Given</strong> / <strong>Based on</strong> / <strong>Drawing on</strong></td><td style="padding:.6rem">A abertura de executivo. Ancora a recomenda&#231;&#227;o na evid&#234;ncia, antes de dizer qual &#233;.</td><td style="padding:.6rem"><strong>Given</strong> the response rate, the caveat belongs on slide one.<br><strong>Based on</strong> the preliminary findings, I am proposing...</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">A regra de ouro</td><td style="padding:.6rem" colspan="2">O participle e a frase principal t&#234;m de ter o <strong>MESMO SUJEITO</strong>. Se n&#227;o tiverem, a frase desaba (o cl&#225;ssico <em>dangling participle</em>) &mdash; e em ingl&#234;s ela n&#227;o soa estranha: ela soa <em>errada</em>.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1 &mdash; dangling participle):</strong> "<em>Having reviewed the findings, the response rate was disappointing</em>" est&#225; ERRADO: quem revisou os findings foi VOC&#202;, n&#227;o a taxa de resposta. O sujeito da frase principal tem de ser quem executa o participle. Certo: "Having reviewed the findings, <strong>I</strong> found the response rate disappointing." Teste infal&#237;vel: pergunte "quem fez isso?" &#8594; a resposta tem de ser o sujeito da frase principal.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> <em>having</em> pede PARTIC&#205;PIO, nunca infinitivo nem presente. "Having <em>review</em> the data" &#8594; "Having <strong>reviewed</strong> the data". E o participle passivo &#233; s&#243; o partic&#237;pio, sem <em>being</em>: "<em>Being asked</em> about the timeline" &#233; poss&#237;vel, mas o registro executivo prefere o seco "<strong>Asked</strong> about the timeline".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Por que isto importa para voc&#234;:</strong> voc&#234; tem 11 minutos e um COO que para de anotar no slide tr&#234;s. O participle clause &#233; a ferramenta que comprime "N&#243;s revisamos os achados, e depois disso eu preparei uma proposta" em "<strong>Having reviewed the findings, I would propose...</strong>" &mdash; e devolve os seus segundos para a &#250;nica parte que a sala quer ouvir: o que voc&#234; encontrou, e o que voc&#234; vai fazer.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Revis&#227;o das aulas 1-7 (hoje tudo volta):</strong> causative passive (<em>We had the survey designed by...</em>), cleft (<em>What the team needs is...</em>), invers&#227;o (<em>Never have I seen...</em>), third conditional + modal perfects (<em>If we had asked earlier, we would have known / we should have addressed it</em>), reporting verbs (<em>He acknowledged that... / She agreed to...</em>) e hedging (<em>It would appear that... / To a certain extent...</em>). N&#227;o s&#227;o conte&#250;do novo: s&#227;o as suas ferramentas. Hoje voc&#234; usa TODAS numa apresenta&#231;&#227;o s&#243;.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta do participle. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Midpoint Review in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos na ordem em que voc&#234; vai conduzir a apresenta&#231;&#227;o do balan&#231;o &#224; lideran&#231;a canadense. Lembre-se do erro da Mariana: a sala quer o fim primeiro.</p>
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
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases que sustentam a sua apresenta&#231;&#227;o de balan&#231;o do come&#231;o ao fim.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da sua apresenta&#231;&#227;o de meio de percurso &#224; lideran&#231;a canadense.</p>
      <div class="quiz-item"><div class="quiz-question">You have eleven minutes with the COO. Your first sentence is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Let me start by walking you through the methodology we used and the four phases of the assessment.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;The takeaway first: the culture here is not broken, it is unheard &mdash; and the response rate is the evidence. Everything else I say today defends that sentence.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Thank you all so much for your time today. I know how busy everyone is at this time of year.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the participle clause correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Having reviewed the findings, the response rate was disappointing.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Having reviewed the findings, I would propose that we build on the focus groups rather than start again.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Having review the findings, I am proposing two quick wins.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You promised a seventy percent response rate in June. It came back at thirty-eight. The COO has not asked about it yet. You:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;One caveat, and I would rather give it to you than have you find it: we fell short of the rate I projected in June. It leaves me a smaller sample, and it is itself a finding about how heard this team feels.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Say nothing about it. He has not asked, the work is strong, and the number would only distract from the recommendation.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;The response rate was low, but honestly that happens with every survey, so I would not read anything into it.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks: &ldquo;Is the new onboarding working?&rdquo; You genuinely do not know yet. The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Yes, definitely. Everyone I have spoken to seems very positive about it.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;I have no idea. It is impossible to measure something like that.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;On that one, the jury is still out. The first cohort finishes in February, so I will have a tangible number for you in March &mdash; and not before.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He pushes back: &ldquo;Two quick wins? I want the whole framework by Q2.&rdquo; You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;We can do that, and I would want you to see the trade-off: pulling the framework into Q2 means the baseline gets taken after the change rather than before, which costs us the ability to prove that any of it worked.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;That is not possible. Q2 is far too early for something of this size.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Of course, no problem at all. I will have the whole framework ready by Q2.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
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
