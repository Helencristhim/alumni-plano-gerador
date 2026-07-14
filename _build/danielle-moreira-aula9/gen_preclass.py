#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 9 da Danielle Moreira (B2, People & Culture / Maple Bear).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5
  - REGRA 13: B2 = 12-15 itens de vocabulario (aqui 15: 10 termos + 5 expressoes)
  - REGRA 22: ZERO palavra ensinada como nova nas aulas 1..8
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: mesmo tema/gramatica/vocab da aula 9 IN CLASS (preview, nao outra aula)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).

GRAMATICA DA AULA 9 (nova; nao repete a1..a8):
  concessao + contra-argumento (concessive clauses)
  While/Although + clause · Granted... That said... · Much as I... · Even if... still
  A tese: o ponto DELE vai na oracao SUBORDINADA, o ponto DELA na oracao PRINCIPAL.

  (O curriculo pedia "hedging avancado" pela 3a vez -- ja dado nas aulas 5 e 6.
   Trocado por concessivas, que e a gramatica que o tema REALMENTE exige e que
   nao aparece em nenhuma das aulas 1-8.)
"""
import re
import random

random.seed(9)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), traducao PT, exemplo)
VOCAB = [
    ("Counterpoint", "an argument you place against the one on the table, without rejecting the person who made it",
     "contraponto",
     "My counterpoint is not that he is wrong about the sample. It is that the sample is not what the number is measuring."),
    ("Reservation", "a specific doubt you name out loud, rather than a general feeling of discomfort",
     "ressalva / reserva",
     "I have one reservation about the plan, and I would rather say it now than nod and take it to the corridor afterwards."),
    ("Premise", "the thing an argument stands on before it starts, and usually never proves",
     "premissa",
     "I take issue with the premise, not with the conclusion. If the premise holds, everything he said after it is correct."),
    ("Assumption", "something taken as true without evidence, and invisible to the person holding it",
     "pressuposto / suposi&#231;&#227;o",
     "The assumption in this room is that silence means agreement. The whole assessment exists to test that one sentence."),
    ("Merit", "the part of an argument that is genuinely good, whether or not you accept where it ends up",
     "m&#233;rito",
     "There is real merit in what he is saying about the sample. There is none at all in what he concludes from it."),
    ("Anecdotal", "based on individual stories rather than on systematic evidence, and it can still be true",
     "aned&#243;tico / baseado em casos isolados",
     "He called the focus groups anecdotal, and he is right. Anecdotal is not the same as wrong, and that is the sentence I have to be able to say."),
    ("Rigor", "the discipline that makes a finding survive somebody actively trying to break it",
     "rigor (met&#243;dico)",
     "They are not attacking me. They are applying the only rigor they have, and if my finding cannot survive it, I would rather know on Thursday."),
    ("Peer-reviewed", "checked by other specialists in the field before anybody is asked to believe it",
     "revisado por pares",
     "It is not peer-reviewed, and it was never meant to be. A diagnostic and a study are two different objects with two different jobs."),
    ("Common ground", "the part both sides already agree on, and the only place a disagreement can safely start",
     "terreno comum / ponto de acordo",
     "Let me start from the common ground: none of us believes that a faculty which says nothing is a faculty with nothing to say."),
    ("To concede", "to give a point away because it is true, not because you are losing",
     "conceder / reconhecer um ponto",
     "I will concede the sample before he takes it from me. What I will not concede is what the sample means."),
    ("To take issue with", "to disagree with one specific claim, deliberately and out loud, and never with the person",
     "discordar de / contestar (um ponto espec&#237;fico)",
     "I take issue with the premise, and not with a single thing you concluded from it."),
    ("To play devil's advocate", "to argue a position you do not actually hold, in order to test whether the other one survives",
     "bancar o advogado do diabo",
     "Let me play devil's advocate against my own finding for a moment, because you are going to do it anyway."),
    ("To stand your ground", "to hold your position under pressure, without raising your voice and without moving",
     "manter a sua posi&#231;&#227;o / n&#227;o recuar",
     "She conceded the sample without hesitating, and then she stood her ground on what it meant."),
    ("To defer to", "to accept somebody's authority on a point where they genuinely know more, as a choice and never a surrender",
     "ceder a / reconhecer a autoridade de",
     "I defer to this council entirely on the research question. I would not defer to anyone on what a sixty-two percent silence means."),
    ("To hold water", "(of an argument) to survive examination, used almost always in the negative",
     "se sustentar / ter fundamento",
     "That is a fair premise to test, and it does not hold water on exactly one point."),
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

# ---------- Stage 1.5 fill-in-the-blank (as 4 estruturas concessivas + 2 collocations) ----------
# (pre, resposta, hint, frase completa (audio), post) -- espacamento EXPLICITO em pre/post
BLANKS = [
    ("", "While",
     "Dica: concess&#227;o na subordinada + o SEU ponto na principal. While / Although / Even though",
     "While the sample is small, the pattern inside it is consistent.",
     " the sample is small, the pattern inside it is consistent."),
    ("Granted, the focus groups are anecdotal. ", "That said",
     "Dica: o piv&#244; que vem DEPOIS da concess&#227;o. That said / Having said that / Nonetheless",
     "Granted, the focus groups are anecdotal. That said, they are the only question anyone has asked this faculty in four years.",
     ", they are the only question anyone has asked this faculty in four years."),
    ("", "Much as I would like to",
     "Dica: concess&#227;o formal, no come&#231;o da frase. Much as I + verbo (nunca 'Much as I would like defending')",
     "Much as I would like to defend the response rate, I would rather replace it.",
     " defend the response rate, I would rather replace it."),
    ("", "Even if we accept that",
     "Dica: concess&#227;o hipot&#233;tica -- eu aceito a premissa dele E o meu ponto sobrevive assim mesmo (+ still)",
     "Even if we accept that the data is anecdotal, the silence still requires an explanation.",
     " the data is anecdotal, the silence still requires an explanation."),
    ("", "Despite the low response rate",
     "Dica: 'despite' &#233; PREPOSI&#199;&#195;O -- vem com substantivo ou -ing, NUNCA com ora&#231;&#227;o ('despite the response rate IS low' est&#225; errado)",
     "Despite the low response rate, the finding holds.",
     ", the finding holds."),
    ("I ", "take issue with",
     "Dica: take issue WITH (nunca 'take issue TO'). Discorda-se do ARGUMENTO, nunca da pessoa",
     "I take issue with the premise, and not with a single thing you concluded from it.",
     " the premise, and not with a single thing you concluded from it."),
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
    ("Granted, the sample is small, and I would not ask you to treat it as representative. That said, the sixty-two percent who said nothing are the finding.",
     "&#201; verdade, a amostra &#233; pequena, e eu n&#227;o pediria que voc&#234;s a tratassem como representativa. Dito isso, os sessenta e dois por cento que n&#227;o disseram nada s&#227;o o achado."),
    ("While it is not peer-reviewed, it was never designed to be. A diagnostic and a study answer two different questions.",
     "Embora n&#227;o seja revisado por pares, nunca foi concebido para ser. Um diagn&#243;stico e um estudo respondem a duas perguntas diferentes."),
    ("I defer to this council on the research question. I would not defer to anyone on what a sixty-two percent silence means.",
     "Eu cedo a este conselho na quest&#227;o de pesquisa. Eu n&#227;o cederia a ningu&#233;m sobre o que significa um sil&#234;ncio de sessenta e dois por cento."),
    ("Much as I would like to defend the response rate, I would rather replace it, with an instrument this council helps me build.",
     "Por mais que eu gostasse de defender a taxa de resposta, eu prefiro substitu&#237;-la &#8212; por um instrumento que este conselho me ajude a construir."),
    ("I take issue with the premise, and not with a single thing you concluded from it.",
     "Eu contesto a premissa, e nem uma &#250;nica coisa que voc&#234; concluiu a partir dela."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-9">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 09 -- Pre-class</div>
      <h3>Diplomatic Pushback -- Disagreeing With People Who Know More Than You</h3>
      <div class="lesson-desc">Discordar de um conselho acad&#234;mico de doutores sem capitular e sem brigar: conceder em voz alta o que &#233; verdade, sustentar o que &#233; seu, e transformar a obje&#231;&#227;o num pedido concreto. Key words: counterpoint, reservation, premise, assumption, merit, anecdotal, rigor, peer-reviewed, common ground, to concede, to take issue with, to play devil's advocate, to stand your ground, to defer to, to hold water. Structure: ora&#231;&#245;es concessivas (While / Although the sample is small, the pattern is consistent &middot; Granted... That said... &middot; Much as I would like to... &middot; Even if we accept that... still) &#8212; o ponto DELE vai na ora&#231;&#227;o subordinada, o seu vai na principal, e a sala lembra da principal.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="9" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="9">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada termo e leia o exemplo. Este &#233; o vocabul&#225;rio de quem discorda de um especialista e continua sendo levada a s&#233;rio.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l9">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Teresa Vidal lost the room in eleven seconds, and she lost it by agreeing. She had presented a culture assessment to an academic council once before, in Lisbon, and she had come out of it certain that the mistake had been arrogance. So this time she arrived humble. When the chair took off his glasses and said that a response rate of thirty-four percent was, in his field, <strong>anecdotal</strong> rather than evidence, she said: you are absolutely right, and I will redo the whole thing. Every word of that sentence was polite, and every word of it was true. It also told nine people that the culture work could wait a year, and they believed her, because she had said it herself.</p>
        <p style="margin-top:.8rem">There is a third answer, and it is not a personality &#8212; it is a structure. <strong>While the sample was small</strong>, the pattern inside it was consistent. <strong>Granted</strong>, four focus groups are not systematic. <strong>That said</strong>, they were the only occasion on which anybody had asked that faculty a question in four years. <strong>Even if we accept that</strong> the instrument is not <strong>peer-reviewed</strong>, a healthy faculty that is asked how it feels does not <strong>still</strong> decline to answer at a rate of two thirds. And <strong>much as she would have liked to</strong> defend the thirty-four percent, the senior move was to say, out loud and before anyone else could, that she would rather replace it &#8212; with an instrument the council itself helped her build.</p>
        <p style="margin-top:.8rem">Notice what those sentences do, because they all do the same thing twice. Each one <strong>concedes</strong> the part that is genuinely true, and each one puts that concession in the clause that <em>depends</em>. And then each one puts the finding &#8212; her finding, the one piece of ground that is hers &#8212; in the clause that <em>stands</em>. It is not decoration. A room walks out remembering the main clause. &ldquo;While the sample is small, the pattern is consistent&rdquo; and &ldquo;While the pattern is consistent, the sample is small&rdquo; contain exactly the same two facts and hand down opposite verdicts. Teresa never said a false word in Lisbon. She simply put her own weakness in the clause that survives, and the council heard her argue against herself in her own voice.</p>
        <p style="margin-top:.8rem">The chair told her something afterwards that she has repeated ever since. He said that every consultant who had ever stood in that room had arrived certain, and that he had never believed a single one of them; that <strong>rigor</strong> is not hostility, it is the only professional courtesy a researcher has to offer a stranger; and that what he had actually been trying to find out was not whether her data was perfect, but whether she knew where it was thin. <strong>To defer to</strong> him on the research question would have cost her nothing at all. <strong>To take issue with</strong> him on what a two-thirds silence means would have cost her nothing either &#8212; and it was the only thing in the building that was hers.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. "<strong>While the sample is small</strong>, the pattern is consistent." &mdash; por que a ordem das duas ora&#231;&#245;es MUDA o argumento?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> N&#227;o muda: as duas ora&#231;&#245;es cont&#234;m os mesmos fatos, ent&#227;o o sentido &#233; id&#234;ntico.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Porque a concessiva (While...) &#233; a ora&#231;&#227;o <strong>subordinada</strong> &#8212; ela fica gramaticalmente REBAIXADA. A sala sai lembrando da ora&#231;&#227;o <strong>principal</strong>. Invertendo a ordem, os mesmos dois fatos entregam veredictos OPOSTOS.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque em ingl&#234;s a concessiva sempre tem de vir no fim da frase.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. O erro brasileiro n&#186; 1 desta aula: por que "<em>Although</em> the sample is small, <em>but</em> the pattern is consistent" est&#225; errado?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Porque <strong>although</strong> e <strong>but</strong> fazem o MESMO trabalho, e o ingl&#234;s usa <strong>um</strong> dos dois, nunca os dois. &#201; o "embora... mas" do portugu&#234;s chegando inteiro.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque "although" s&#243; pode ser usado no fim da frase, nunca no come&#231;o.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Porque depois de "although" o verbo tem de ir para o passado.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. E o erro n&#186; 2: por que "<em>Despite the response rate is low</em>, the finding holds" est&#225; errado?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Porque "despite" s&#243; existe em ingl&#234;s brit&#226;nico.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Porque o correto seria "Despite that the response rate is low".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Porque <strong>despite</strong> / <strong>in spite of</strong> s&#227;o <strong>preposi&#231;&#245;es</strong>: v&#234;m com substantivo ou -ing, nunca com ora&#231;&#227;o. O certo &#233; "<strong>Despite the low response rate</strong>", "<strong>despite the fact that</strong> the response rate is low", ou simplesmente "<strong>although</strong>".</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. According to the text, what did Teresa actually do wrong in Lisbon?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She was arrogant with the chair, and she defended a number that could not be defended.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She agreed with everything. She conceded the whole assessment instead of only the part that was true &mdash; and by saying it herself, she persuaded nine people that the culture work could wait a year.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She used the wrong vocabulary, and the council could not follow her technical argument.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">5. What does the chair mean when he says that rigor is not hostility?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That researchers enjoy attacking consultants, and the only defense is to never show them weak data.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That breaking her argument is the only professional courtesy he has to offer a stranger &mdash; and that what he is really testing is not whether her data is perfect, but whether she knows where it is thin.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That he did not actually disagree with her, and was only being polite in front of the council.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Concession &amp; Counter-Argument</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A ora&#231;&#227;o concessiva &#233; a estrutura que faz DUAS coisas numa frase s&#243;: entrega ao outro o ponto em que ele est&#225; certo, e mant&#233;m o seu. E ela decide, em sil&#234;ncio, de qual dos dois a sala vai lembrar (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Estrutura</th><th style="padding:.7rem;text-align:left">O ponto DELE (subordinada)</th><th style="padding:.7rem;text-align:left">O ponto DELA (principal)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">1. <strong>While / Although / Even though</strong> + ora&#231;&#227;o, + principal</td><td style="padding:.6rem">While the sample is small,</td><td style="padding:.6rem">the pattern is consistent.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">2. <strong>Granted</strong>, ... <strong>That said</strong>, ...</td><td style="padding:.6rem">Granted, the groups are anecdotal.</td><td style="padding:.6rem">That said, they are the only question anyone asked.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">3. <strong>Much as I</strong> + verbo, + principal</td><td style="padding:.6rem">Much as I would like to defend it,</td><td style="padding:.6rem">I would rather replace it.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">4. <strong>Even if</strong> + ora&#231;&#227;o, + principal com <strong>still</strong></td><td style="padding:.6rem">Even if we accept that it is anecdotal,</td><td style="padding:.6rem">the silence still requires an explanation.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Piv&#244;s (usam-se em qualquer uma)</td><td style="padding:.6rem" colspan="2"><strong>That said</strong> &middot; <strong>Having said that</strong> &middot; <strong>Nonetheless</strong> &middot; <strong>Even so</strong> &middot; <strong>And yet</strong> &#8212; todos querem dizer a mesma coisa: <em>eu ouvi voc&#234;, e eu n&#227;o me movi.</em></td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (o erro n&#186; 1):</strong> "<em>Although</em> the sample is small, <em>but</em> the pattern is consistent" est&#225; ERRADO. <strong>Although</strong> e <strong>but</strong> fazem o mesmo trabalho, e o ingl&#234;s usa <strong>UM</strong> deles, jamais os dois. O "embora... mas" do portugu&#234;s n&#227;o sobrevive &#224; travessia. Escolha: "<strong>Although</strong> the sample is small, the pattern is consistent" OU "The sample is small, <strong>but</strong> the pattern is consistent".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Aten&#231;&#227;o (o erro n&#186; 2):</strong> <strong>despite</strong> e <strong>in spite of</strong> s&#227;o <strong>PREPOSI&#199;&#213;ES</strong> &#8212; v&#234;m com substantivo ou -ing, NUNCA com ora&#231;&#227;o. "Despite the response rate <em>is low</em>" &#8594; "<strong>Despite the low response rate</strong>" ou "<strong>Despite the fact that</strong> the response rate is low". Se voc&#234; quer a ora&#231;&#227;o inteira, o caminho f&#225;cil &#233; trocar por <strong>although</strong>.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>Por que isto importa para voc&#234;:</strong> a concessiva N&#195;O &#233; educa&#231;&#227;o &#8212; &#233; <strong>hierarquia</strong>. A ora&#231;&#227;o subordinada &#233; gramaticalmente rebaixada, e a sala sai lembrando da PRINCIPAL. "While the sample is small, the pattern is consistent" e "While the pattern is consistent, the sample is small" t&#234;m os MESMOS DOIS FATOS e entregam veredictos OPOSTOS. Sob press&#227;o, o instinto brasileiro &#233; p&#244;r a concess&#227;o por &#250;ltimo (soa mais humilde) &#8212; e isso inverte o seu pr&#243;prio argumento sem que voc&#234; diga uma palavra falsa. <strong>O ponto dele vem primeiro. Sempre.</strong></p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.5rem"><strong>A resposta de tr&#234;s movimentos:</strong> <strong>CONCEDE</strong> (d&#234; o que &#233; verdade, antes que tomem) &#8594; <strong>COUNTER</strong> (sustente o que &#233; seu, na ora&#231;&#227;o principal) &#8594; <strong>PROPOSE</strong> (transforme a obje&#231;&#227;o num pedido concreto, com data). Nesta ordem, e nada mais. Um pesquisador que ajuda voc&#234; a construir o instrumento n&#227;o passa mar&#231;o atacando o instrumento.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura concessiva correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Diplomatic Pushback in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os cinco movimentos na ordem em que voc&#234; vai enfrentar o conselho acad&#234;mico canadense.</p>
      <div class="order-container" id="order-l9">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Hold your finding in the main clause, where the room will remember it: that said, the sixty-two percent who said nothing are the finding.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Turn the objection into an ask: two members of the council, in March, building the next instrument with you.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Start from the common ground, and hand them the weakest part of your own work before anybody has to find it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Defer to them on the ground where they genuinely know more, and stand your ground on the one that is yours.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Concede the part of the objection that is genuinely true, out loud and without flinching: granted, the sample is small.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l9')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a. S&#227;o as cinco frases que sustentam uma discord&#226;ncia diplom&#225;tica do come&#231;o ao fim.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real do seu conselho acad&#234;mico no Canad&#225;.</p>
      <div class="quiz-item"><div class="quiz-question">Dr. Prescott says: &ldquo;Thirty-eight percent. In my field, that is not a finding. That is a rumor.&rdquo; The most senior answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;You are absolutely right. I will redo the whole assessment and come back when I have a proper number.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Granted, and I concede it without any reservation. That said, the sixty-two percent who chose not to answer are not missing data. They are the finding.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;With respect, thirty-eight percent is a perfectly normal response rate and the methodology is sound. I stand by the data.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence uses the concessive structure CORRECTLY?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Although the instrument is not peer-reviewed, but it was never designed to be.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Despite the sample is small, the pattern inside it is consistent.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;While the instrument is not peer-reviewed, it was never designed to be: a diagnostic and a study answer two different questions.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He says: &ldquo;You have been here six weeks. What could you possibly know about this faculty?&rdquo; You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;Very little, and that is precisely why I ran an assessment rather than arriving with a plan. I defer to this council on what the faculty is. I would not defer to anyone on what the response rate says about how it feels to be asked.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Six weeks is enough. I have twelve years of experience in organizational culture.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;You are right, I am too new. Perhaps the council should lead this work instead.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to disagree with his reasoning without attacking him. Which sentence does that?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I think you have misunderstood what this assessment is for.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I take issue with the premise, and not with a single thing you concluded from it. If the premise held, everything you said after it would be correct.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;That argument is simply wrong, and I can prove it.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He asks what exactly the council is being asked to approve. The strongest close is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;The culture strategy, in full, as it appears in the deck.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Nothing today. I would rather come back when the data is stronger.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;Not the strategy. One thing: a second round of the instrument, designed with two members of this council, in March. Much as I would like to defend the thirty-eight percent, I would rather replace it.&rdquo;</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. Fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">The Academic Council of Maple Bear Canada has four objections to your assessment: the sample is 38%, the focus groups are anecdotal, the instrument is not peer-reviewed, and you have been in the country for six weeks. Every one of them is fair. Answer all four, as the senior HR leader you are about to become on August 1st. Concede each one out loud, hold your finding in the main clause every single time, and close by turning the objection into an ask with a date on it. Use the four concessive structures (While... / Granted... That said... / Much as I would like to... / Even if we accept that... still) and six words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-9"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 9</h4>
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

# ---------- REGRA 22: nenhuma palavra das aulas 1-8 pode voltar como vocab card ----------
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
}
repeat = {w for w, _, _, _ in VOCAB if w.lower() in JA_ENSINADO}
assert not repeat, f'REGRA 22 violada: {repeat} ja foi ensinada nas aulas 1-8'
assert 12 <= len(VOCAB) <= 15, f'REGRA 13 (B2 = 12-15 palavras): {len(VOCAB)}'

print(f'wrote {OUT} ({len(HTML)//1024} KB)')
print(f'vocab={len(VOCAB)} match={len(VOCAB)} blanks={len(BLANKS)} speech={len(SPEECH)}')
print(f'frases falaveis (audioMap): {len(set(SPEAKABLE))}')
