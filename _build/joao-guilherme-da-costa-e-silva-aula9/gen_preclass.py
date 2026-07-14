#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 9 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 9 IN CLASS (mesmo tema/gramática/vocab — future perfect e
future continuous na call de comissionamento em velocidade nativa).
"""
import os
import random

random.seed(9)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Integration test", "the test that proves the separate systems talk to each other -- not that each one works alone", "teste de integra&#231;&#227;o",
     "\"The integration test between the interlocking and the control center starts on the fifteenth.\""),
    ("Site readiness", "whether the place itself -- power, access, safety -- can actually receive the equipment and the crews", "prontid&#227;o do canteiro / da obra",
     "\"I will confirm site readiness on the twelfth, once the power supply is energized.\""),
    ("Look-ahead schedule", "the short window of the plan: the next three weeks, activity by activity, in detail", "cronograma de curto prazo (pr&#243;ximas 3 semanas)",
     "\"The three-week look-ahead schedule shows the integration test starting on the fifteenth.\""),
    ("Open action", "a task with a name on it and a date on it, and it is not closed yet", "a&#231;&#227;o em aberto (com dono e prazo)",
     "\"By Friday we will have closed every open action from the last call.\""),
    ("Outstanding item", "something that was agreed, is still not done, and is still on the list at the end of the meeting", "pend&#234;ncia",
     "\"Three outstanding items remain, and none of them can wait until the ramp-up.\""),
    ("Provisional acceptance", "the client takes the system into service -- with a list of defects still attached to it", "aceita&#231;&#227;o provis&#243;ria (entrada em servi&#231;o com pend&#234;ncias)",
     "\"Provisional acceptance is planned for the end of the third quarter.\""),
    ("Final acceptance", "nothing is left open, the warranty period is over, and the last payment is released", "aceita&#231;&#227;o definitiva",
     "\"Final acceptance will not be granted until every outstanding item is closed.\""),
    ("Defects liability period", "the window after handover in which the supplier still fixes, at its own cost, whatever fails", "per&#237;odo de garantia / responsabilidade por defeitos",
     "\"The defects liability period runs for twelve months between provisional and final acceptance.\""),
    ("Ramp-up", "the gradual climb from the first test run to full service, week by week", "ramp-up: subida gradual at&#233; a opera&#231;&#227;o plena",
     "\"By the time the ramp-up begins in November, we will have trained every operator.\""),
    ("Interface management", "making two suppliers' systems meet without a gap -- and owning the gap when there is one", "gest&#227;o de interfaces",
     "\"Interface management between signaling and rolling stock sits with me.\""),
    ("Dry run", "a full rehearsal of the real operation, with nothing at stake and everybody watching", "ensaio geral / simulado",
     "\"This time next week we will be running a dry run of the failover procedure.\""),
    ("To phase out", "to remove something gradually, on a planned date, until it is gone for good", "descontinuar, eliminar gradualmente",
     "\"The manual workarounds will be phased out before provisional acceptance, not after.\""),
    ("To factor in", "to include something in the calculation BEFORE you commit to the date", "levar em conta (no c&#225;lculo, antes de assumir o prazo)",
     "\"Have you factored in the night-shift restrictions on the site?\""),
    ("To run something by someone", "to repeat or check something with somebody, so that they can follow it or approve it", "repassar / confirmar algo com algu&#233;m",
     "\"Could you run the acceptance dates by me one more time?\""),
]

SURVIVAL = [
    ("By the twelfth we will have confirmed site readiness in writing.",
     "Até o dia doze teremos confirmado a prontidão do canteiro por escrito."),
    ("This time next week we will be running a dry run of the failover procedure.",
     "A esta hora na semana que vem estaremos rodando um ensaio do procedimento de failover."),
    ("Could you run that by me one more time?",
     "Você poderia repassar isso comigo mais uma vez?"),
    ("Just to confirm — are you saying that the workarounds come out before provisional acceptance?",
     "Só para confirmar — você está dizendo que as soluções paliativas saem antes da aceitação provisória?"),
    ("I want to make sure I'm following: the deadline you're referring to is the twelfth, not the fifteenth.",
     "Quero ter certeza de que estou acompanhando: o prazo a que você se refere é o dia doze, não o dia quinze."),
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
            f'<span class="vocab-card-def">{esc(d)} ({esc(pt)})</span></div>'
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


CONTEXT = """<p>The call starts at eight and Fiona Hartley, the project director in London, has another one at half past. She goes straight in. Where are we on <strong>site readiness</strong>? Because by the twelfth she needs the power supply energized, or the <strong>integration test</strong> does not happen. She speaks the way people speak when they are late: the auxiliaries collapse, <em>will have</em> becomes <em>will'uv</em>, <em>will be</em> almost disappears, and the dates arrive in the middle of long sentences with no emphasis at all.</p>
        <p>So Jo&#227;o Guilherme does the thing that feels wrong and is right: he stops her. <em>I want to make sure I am following &mdash; the deadline you are referring to is the twelfth, and that is for site readiness, not for the test itself.</em> She says "Correct" and carries on. Five seconds. Then he forecasts, and every sentence carries a date. <strong>By the fifteenth we will have energized</strong> the power supply and <strong>closed</strong> the two <strong>open actions</strong> on the cable route. <strong>We will be working</strong> nights from the eighth to hold that date. <strong>This time next week we will be running</strong> a <strong>dry run</strong> of the failover procedure. <strong>By the time the ramp-up starts</strong> in November, every operator <strong>will have been trained</strong>.</p>
        <p>Then comes the part that decides the money. <strong>Provisional acceptance</strong> at the end of the third quarter; <strong>final acceptance</strong> twelve months later, with the <strong>defects liability period</strong> running in between. And the manual workarounds, Fiona says, get <strong>phased out</strong> BEFORE provisional acceptance, not after &mdash; she has seen too many projects where the temporary fix quietly becomes the design. Jo&#227;o asks her to <strong>run</strong> the acceptance dates <strong>by</strong> him one more time, because he wants to <strong>factor</strong> them <strong>in</strong> before he sends the three-week <strong>look-ahead schedule</strong>. And he closes the call the way a call has to be closed: <em>Just to confirm &mdash; are you saying that no workaround survives provisional acceptance? Then by the thirtieth we will have cleared every <strong>outstanding item</strong> on that list.</em> He did not understand every word she said. He understood every date &mdash; and that is the entire job."""

QUIZZES_CONTEXT = [
    ("1. \"<em>By the fifteenth we will have energized the power supply.</em>\" O que essa estrutura promete, exatamente?",
     [("Que a energiza&#231;&#227;o vai ACONTECER no dia quinze.", False),
      ("Que a energiza&#231;&#227;o estar&#225; CONCLU&#205;DA ANTES do dia quinze &mdash; <em>will have</em> + partic&#237;pio &#233; o tempo do PRAZO, e &#233; ele que o contrato l&#234;.", True),
      ("Que a energiza&#231;&#227;o come&#231;a no dia quinze e continua depois.", False)]),
    ("2. \"<em>This time next week we will be running a dry run.</em>\" Por que <em>will be running</em>, e n&#227;o <em>will run</em>?",
     [("Porque <em>will be running</em> &#233; mais formal.", False),
      ("Porque a a&#231;&#227;o estar&#225; EM ANDAMENTO naquele momento &mdash; nem terminada, nem come&#231;ando. <em>Will run</em> soaria como uma decis&#227;o tomada na hora.", True),
      ("Porque com <em>next week</em> o ingl&#234;s pro&#237;be o futuro simples.", False)]),
    ("3. \"<em>By the time the ramp-up starts, the workarounds will have been phased out.</em>\" Por que <em>starts</em>, e n&#227;o <em>will start</em>?",
     [("Porque depois de <em>by the time / when / before / as soon as</em> o ingl&#234;s escreve o futuro no PRESENTE. \"By the time it will start\" n&#227;o existe.", True),
      ("Porque o ramp-up j&#225; come&#231;ou.", False),
      ("Porque <em>start</em> &#233; um verbo irregular.", False)]),
    ("4. Fiona diz a nova data no MEIO de uma frase longa, sem &#234;nfase. Qual &#233; a rea&#231;&#227;o profissional?",
     [("Anotar o que deu para entender e conferir depois por e-mail, para n&#227;o parecer lento.", False),
      ("Interromper e confirmar em voz alta: \"Just to confirm &mdash; are you saying that provisional acceptance has moved to the twenty-third?\" Cinco segundos ali evitam tr&#234;s semanas de trabalho para a data errada.", True),
      ("Continuar a call e pedir que ela fale mais devagar da pr&#243;xima vez.", False)]),
]

BLANKS = [
    ("will have confirmed", "Dica: PRAZO -- conclu&#237;do ANTES da data. <em>will have</em> + partic&#237;pio",
     "By the twelfth we will have confirmed site readiness in writing.",
     '"By the twelfth we ', ' site readiness in writing."'),
    ("will be running", "Dica: EM ANDAMENTO naquele momento. <em>will be</em> + verbo com -ing",
     "This time next week we will be running a dry run of the failover procedure.",
     '"This time next week we ', ' a dry run of the failover procedure."'),
    ("starts", "Dica: depois de <em>by the time</em> o verbo vai no PRESENTE, mesmo falando do futuro. Nunca <em>will start</em>",
     "By the time the ramp-up starts, the manual workarounds will have been phased out.",
     '"By the time the ramp-up ', ', the manual workarounds will have been phased out."'),
    ("will have been working", "Dica: mede a DURA&#199;&#195;O at&#233; aquele ponto: <em>will have been</em> + verbo com -ing",
     "By September the crews will have been working nights for six weeks.",
     '"By September the crews ', ' nights for six weeks."'),
    ("factor in", "Dica: incluir no c&#225;lculo ANTES de assumir a data (nunca \"consider in\")",
     "I need to factor in the night-shift restrictions before I commit to that date.",
     '"I need to ', ' the night-shift restrictions before I commit to that date."'),
    ("run that by me", "Dica: pedir que repitam para voc&#234; conferir -- a frase que salva a call",
     "Could you run that by me one more time?",
     '"Could you ', ' one more time?"'),
]

ORDER = [
    (1, "Catch the date she buried in the middle of the sentence: provisional acceptance has moved to the twenty-third."),
    (2, "Stop her and confirm it out loud: \"Just to confirm -- are you saying that provisional acceptance is now the twenty-third?\""),
    (3, "Ask her to repeat what you did not catch: \"Could you run the acceptance dates by me one more time?\""),
    (4, "Factor in what she cannot see: the night-shift restrictions on site."),
    (5, "Commit with the deadline tense: \"By the twenty-third we will have closed every outstanding item.\""),
    (6, "Say what will be happening, not finished: \"We will be working nights from the eighth to hold that date.\""),
]

SPEECH = [
    ("By the twelfth we will have confirmed site readiness in writing.",
     "Até o dia doze teremos confirmado a prontidão do canteiro por escrito."),
    ("This time next week we will be running a dry run of the failover procedure.",
     "A esta hora na semana que vem estaremos rodando um ensaio do procedimento de failover."),
    ("By the time the ramp-up starts, the manual workarounds will have been phased out.",
     "Quando o ramp-up começar, as soluções paliativas já terão sido descontinuadas."),
    ("Could you run that by me one more time?",
     "Você poderia repassar isso comigo mais uma vez?"),
    ("I want to make sure I'm following: the deadline you're referring to is the twelfth, not the fifteenth.",
     "Quero ter certeza de que estou acompanhando: o prazo a que você se refere é o dia doze, não o dia quinze."),
]

QUIZZES_SIT = [
    ("Fiona abre a call em velocidade m&#225;xima: \"Where are we on site readiness? By the twelfth I need that power supply energized.\" Voc&#234; responde:",
     [("\"I want to make sure I'm following -- the deadline you're referring to is the twelfth, and that is for site readiness, not for the integration test itself. Is that right?\"", True),
      ("\"Sorry, could you speak more slowly, please? My English is not very good.\"", False),
      ("\"Yes, yes, no problem, everything is on track.\"", False)]),
    ("Ela pede o status. A resposta mais forte &#233;:",
     [("\"We are working on it and I think we will finish before the test.\"", False),
      ("\"By the fifteenth we will have energized the power supply and closed the two open actions on the cable route, and we will be working nights from the eighth to hold that date.\"", True),
      ("\"The site will be ready, do not worry about that.\"", False)]),
    ("No meio de uma frase longa ela diz que a aceita&#231;&#227;o provis&#243;ria mudou para o dia 23. Voc&#234;:",
     [("Anota e confere depois no e-mail dela, para n&#227;o interromper.", False),
      ("Interrompe: \"Just to confirm -- are you saying that provisional acceptance has moved to the twenty-third? Then by the twenty-third we will have cleared every outstanding item.\"", True),
      ("Assume que ouviu errado e segue a call normalmente.", False)]),
    ("\"Let us just keep the manual workarounds until final acceptance, to be safe.\" Voc&#234; recusa:",
     [("\"The workarounds are phased out before provisional acceptance, not after. A temporary fix with no end date quietly becomes the design, and the operator pays to maintain it for thirty years.\"", True),
      ("\"All right, if that is easier for your team, we can keep them.\"", False),
      ("\"I do not have the authority to decide that.\"", False)]),
    ("Ela pergunta se voc&#234; mant&#233;m a data mesmo com a restri&#231;&#227;o de trabalho noturno no canteiro. Voc&#234; diz:",
     [("\"Yes, of course, we will make it work somehow.\"", False),
      ("\"I need to factor in the night-shift restrictions before I commit to that date. You will have the three-week look-ahead schedule tonight, and the date will be in it.\"", True),
      ("\"That is impossible. Nobody can work with these restrictions.\"", False)]),
]


def quiz_html(items):
    out = []
    for q, opts in items:
        o = []
        for j, (text, correct) in enumerate(opts):
            letter = 'ABC'[j]
            o.append(
                f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}">'
                f'<span class="option-letter">{letter}</span> {text}</div>')
        out.append(
            f'      <div class="quiz-item"><div class="quiz-question">{q}</div>'
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l9\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l9\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l9\')">&#9660;</button></span></div>')
    return '\n'.join(out)


def speech_html():
    out = []
    for en, pt in SPEECH:
        out.append(
            f'      <div class="speech-card" data-phrase="{esc(en)}">\n'
            f'        <div class="speech-phrase">{esc(en)}</div>\n'
            f'        <div class="speech-translation">{esc(pt)}</div>\n'
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
            f'<span class="sp-en">{esc(en)}</span><span class="sp-pt">{esc(pt)}</span>'
            f'<button class="btn btn-listen" data-speak="{esc(en)}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
    return '\n'.join(out)


GRAMMAR_TIP = """      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Estrutura / Structure</th><th style="padding:.7rem;text-align:left">O que promete / What it promises</th><th style="padding:.7rem;text-align:left">Na call / On the call</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>will have</strong> + partic&#237;pio<br><span style="font-size:.78rem;color:var(--text-dim)">future perfect</span></td><td style="padding:.6rem">CONCLU&#205;DO antes daquele ponto no futuro. &#201; o tempo do PRAZO &mdash; o que o contrato l&#234; e o que algu&#233;m pode cobrar. Em portugu&#234;s: "at&#233; o dia doze <em>teremos confirmado</em>".</td><td style="padding:.6rem">"By the twelfth we <strong>will have confirmed</strong> site readiness."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>will be</strong> + verbo -ing<br><span style="font-size:.78rem;color:var(--text-dim)">future continuous</span></td><td style="padding:.6rem">EM ANDAMENTO naquele momento: nem terminado, nem come&#231;ando &mdash; acontecendo. Em portugu&#234;s: "semana que vem a esta hora <em>estaremos rodando</em>".</td><td style="padding:.6rem">"This time next week we <strong>will be running</strong> the dry run."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>will have been</strong> + verbo -ing<br><span style="font-size:.78rem;color:var(--text-dim)">future perfect continuous</span></td><td style="padding:.6rem">Mede a DURA&#199;&#195;O acumulada at&#233; aquele ponto. &#201; com ela que se justifica um custo ou um pedido de prazo.</td><td style="padding:.6rem">"By September the crews <strong>will have been working</strong> nights for six weeks."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>by</em> x <em>until</em></td><td style="padding:.6rem"><strong>BY</strong> = o prazo (n&#227;o mais tarde que). <strong>UNTIL</strong> = a dura&#231;&#227;o inteira. O portugu&#234;s cobre os dois com "at&#233;" &mdash; e por isso o brasileiro escreve "until Friday we will have finished", que em ingl&#234;s n&#227;o quer dizer nada.</td><td style="padding:.6rem">"<strong>By</strong> Friday" (prazo) &middot; "We will be testing <strong>until</strong> Friday" (dura&#231;&#227;o)</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>by the time</em> + PRESENTE</td><td style="padding:.6rem">Depois de <em>by the time / when / before / as soon as / until</em>, o futuro se escreve no PRESENTE. "By the time the ramp-up <em>will start</em>" N&#195;O existe.</td><td style="padding:.6rem">"By the time the ramp-up <strong>starts</strong>, the workarounds will have been phased out."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Como isso SOA</td><td style="padding:.6rem" colspan="2">Ningu&#233;m pronuncia esses tempos como eles s&#227;o escritos. <em>will have</em> vira <strong>/w&#618;l&#601;v/</strong> ("will'uv"), <em>we will have</em> vira <strong>"we'll've"</strong>, e <em>will be</em> quase desaparece. O tempo verbal N&#195;O some junto: ele sobrevive no <strong>PARTIC&#205;PIO, no fim da frase</strong> (<em>...we'll've CONFIRMED it</em>). Pare de ca&#231;ar o auxiliar que voc&#234; aprendeu na escola: escute a &#218;LTIMA palavra.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (tr&#234;s erros de brasileiro):</strong> (1) <em>"Until the twelfth we will have confirmed..."</em> &mdash; &#233; <strong>BY</strong> the twelfth: <em>until</em> &#233; dura&#231;&#227;o, <em>by</em> &#233; prazo; (2) <em>"By the time the test will start..."</em> &mdash; depois de <em>by the time</em> vai o PRESENTE: <strong>starts</strong>; (3) <em>"At ten we will run the test"</em> quando o que se quer dizer &#233; "estaremos rodando" &mdash; o correto &#233; <strong>we will be running</strong>: o futuro simples soa como uma decis&#227;o tomada naquele instante.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Colloca&#231;&#245;es do comissionamento:</strong> <strong>confirm</strong> site readiness (nunca "guarantee") &middot; <strong>close</strong> an open action (nunca "finish") &middot; <strong>clear</strong> the outstanding items &middot; <strong>grant</strong> provisional acceptance (o cliente CONCEDE; o fornecedor OBT&#201;M) &middot; <strong>phase out</strong> a workaround &middot; <strong>factor in</strong> a constraint (NUNCA "consider in") &middot; <strong>run</strong> a dry run &middot; <strong>manage</strong> the interfaces.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Clarifica&#231;&#227;o sob press&#227;o (decore as tr&#234;s):</strong> "<em>Could you run that by me one more time?</em>" &middot; "<em>Just to confirm &mdash; are you saying that...?</em>" &middot; "<em>I want to make sure I'm following: the deadline you're referring to is...</em>" &mdash; nenhuma delas &#233; um pedido de desculpas. S&#227;o o que um nativo diz quando perde uma data, e custam cinco segundos.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-9">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1590650153855-d9e808231d41?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 09 -- Pre-class</div>
      <h3>Say That Again -- The Commissioning Call at Full Speed</h3>
      <div class="lesson-desc">Uma diretora de projeto britanica, quarenta minutos e um cronograma de comissionamento em velocidade nativa: como PREVER com data (o que estar&#225; PRONTO x o que estar&#225; ACONTECENDO), onde o tempo verbal se esconde na fala r&#225;pida (o auxiliar some, o partic&#237;pio fica), e as tr&#234;s frases que param a call sem perder a cara. Key words: integration test, site readiness, look-ahead schedule, open action, outstanding item, provisional acceptance, final acceptance, defects liability period, ramp-up, interface management, dry run, to phase out, to factor in, to run something by someone. Structure: future perfect e future continuous (By the twelfth we <em>will have confirmed</em>... / This time next week we <em>will be running</em>...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="9" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="9">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 8 voc&#234; escreveu a pergunta com tempo. Agora a fase final do projeto chega FALADA, r&#225;pida, e no ritmo de outra pessoa. Estas s&#227;o as palavras do &#250;ltimo quil&#244;metro: quem aceita, quando, e o que ainda est&#225; em aberto. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l9">
{match_grid()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        {CONTEXT}
      </div>
{quiz_html(QUIZZES_CONTEXT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Future Perfect &amp; Future Continuous</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Os dois tempos com que se comanda um projeto &mdash; e por que eles quase somem na fala r&#225;pida (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura correta. Toque em Listen para ouvir a frase inteira &mdash; e repare em como o auxiliar quase desaparece.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Conference Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque na ordem correta os passos de quem NAO perde uma data numa call r&#225;pida &mdash; de pegar a informa&#231;&#227;o escondida at&#233; assumir o compromisso com o tempo verbal certo.</p>
      <div class="order-container" id="order-l9">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l9')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. Diga r&#225;pido, colando as palavras: <em>will have</em> vira "will'uv" e <em>will be</em> quase some &mdash; produzir a forma reduzida &#233; o que ensina o ouvido a reconhec&#234;-la. Aten&#231;&#227;o ao stress: pro-VI-sion-al, li-a-BI-li-ty, RED-i-ness (curto, como em "ready").</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da call &mdash; inclusive quando ela esconde a data nova no meio de uma frase longa.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: r&#225;pido o suficiente para acompanhar, preciso o bastante para nunca prometer a coisa errada.</p>
      <div class="think-card">
        <div class="think-question">You are on the commissioning call with the project director in London, and she is running the schedule at full speed. In two minutes: give her the status of site readiness with a date in front of every sentence, say what will have been finished by the twelfth and what your crews will be doing in between, catch the acceptance date she gives you and confirm it out loud, refuse to carry the manual workarounds past provisional acceptance, and close by summarizing what each side will have done by the end of the month.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-9"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 9</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
