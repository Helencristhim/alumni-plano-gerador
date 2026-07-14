#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 8 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 8 IN CLASS (mesmo tema/gramática/vocab — orações relativas
e precisão no RFI de EMC / aterramento).
"""
import os
import random

random.seed(8)

HERE = os.path.dirname(os.path.abspath(__file__))

# (word, speak, definition_en, pt, example)
VOCAB = [
    ("Request for information (RFI)", "Request for information",
     "a formal written question sent to a supplier when a document does not tell you enough",
     "solicita&#231;&#227;o de informa&#231;&#227;o (esclarecimento t&#233;cnico formal)",
     "\"The RFI that we submitted on Monday has not been answered.\""),
    ("Request for proposal (RFP)", "Request for proposal",
     "a formal invitation asking suppliers to propose a solution, with a price, for work not yet awarded",
     "solicita&#231;&#227;o de proposta (abre porta comercial)",
     "\"The rework is inside the contract, so this is an RFI, not an RFP.\""),
    ("Interoperability", "Interoperability",
     "the ability of two different systems to work together and understand each other",
     "interoperabilidade",
     "\"Each system passed alone. What has not been demonstrated is interoperability.\""),
    ("Electromagnetic compatibility (EMC)", "Electromagnetic compatibility",
     "whether equipment can operate without disturbing other equipment through electrical noise",
     "compatibilidade eletromagn&#233;tica",
     "\"Six units failed the electromagnetic compatibility test on 14 July.\""),
    ("Grounding", "Grounding",
     "the connection that gives electrical noise a safe path away from the equipment",
     "aterramento",
     "\"It was the grounding configuration, common to all forty units, that caused the interference.\""),
    ("Interlocking", "Interlocking",
     "the signaling logic that makes two conflicting movements impossible at the same time",
     "intertravamento",
     "\"The interlocking units that failed are on the northbound platform.\""),
    ("Fail-safe", "Fail-safe",
     "designed so that when it fails, it fails into the state that is safe",
     "&#224; prova de falhas (falha segura)",
     "\"A signal that loses power goes to red. That is what fail-safe means.\""),
    ("Redundancy", "Redundancy",
     "a second, independent path that keeps the system working when the first one fails",
     "redund&#226;ncia",
     "\"The redundancy that protects the northbound line has not been demonstrated.\""),
    ("Acceptance criteria", "Acceptance criteria",
     "the written conditions a deliverable must meet before anybody is allowed to accept it",
     "crit&#233;rios de aceita&#231;&#227;o",
     "\"The acceptance criteria that apply to this test are in clause 7.4, not in the email.\""),
    ("Workaround", "Workaround",
     "a temporary way of operating that lets you carry on while the real fix is still missing",
     "solu&#231;&#227;o paliativa / contorno",
     "\"A workaround is acceptable for the trial run. It is not acceptable for the handover.\""),
    ("Ambiguity", "Ambiguity",
     "when a sentence is clear, but can honestly be understood in two different ways",
     "ambiguidade",
     "\"The ambiguity in clause 7.4 is what the supplier is relying on.\""),
    ("To spell out", "To spell out",
     "to state something in complete detail, leaving nothing for the reader to assume",
     "detalhar, explicitar (sem deixar nada subentendido)",
     "\"The RFI has to spell out which units, against which criterion, and by when.\""),
    ("To devise", "To devise",
     "to think out and design a solution that did not exist before",
     "conceber, bolar (uma solu&#231;&#227;o)",
     "\"The workaround that your team devised is not written down anywhere.\""),
    ("To pin down", "To pin down",
     "to identify something exactly, when it has been vague or moving until now",
     "identificar com precis&#227;o, cravar",
     "\"Until we pin down the source of the interference, any fix is a guess.\""),
]

SURVIVAL = [
    ("The six interlocking units that failed the EMC test must be reworked at the supplier's cost.",
     "As seis unidades de intertravamento que reprovaram no ensaio de EMC devem ser retrabalhadas às custas do fornecedor."),
    ("The grounding configuration, which is common to all forty units, must be re-verified.",
     "A configuração de aterramento, que é comum às quarenta unidades, precisa ser reverificada."),
    ("Please confirm the standard to which the design was certified.",
     "Por favor, confirme a norma segundo a qual o projeto foi certificado."),
    ("The workaround that your team devised does not meet the acceptance criteria that apply at handover.",
     "A solução paliativa que a equipe de vocês concebeu não atende aos critérios de aceitação válidos no handover."),
    ("Until we pin down the source of the interference, any fix is a guess.",
     "Enquanto não identificarmos com precisão a fonte da interferência, qualquer correção é um chute."),
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
    for word, speak, d, pt, ex in VOCAB:
        rows.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{esc(word)}</span>'
            f'<span class="vocab-card-dot"> -- </span>'
            f'<span class="vocab-card-def">{esc(d)} ({esc(pt)})</span></div>'
            f'<div class="vocab-card-example">{esc(ex)}</div></div>'
            f'<button class="audio-btn" data-speak="{esc(speak)}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
    return '\n'.join(rows)


def match_grid():
    defs = [d for _, _, d, _, _ in VOCAB]
    rows = []
    for word, _, d, _, _ in VOCAB:
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


CONTEXT = """<p>Forty <strong>interlocking</strong> units were delivered for Line 5, and on 14 July six of them failed the <strong>electromagnetic compatibility</strong> test. Jo&#227;o Guilherme has to write the <strong>request for information</strong> that goes to the German supplier, and he has one afternoon to decide what the document actually asks for. The six that failed are the six installed closest to the traction return cable. But all forty were built to the same <strong>grounding</strong> configuration &mdash; and that is the sentence that will cost somebody money.</p>
        <p>Read the two versions carefully, because they contain the same words. <em>"The interlocking units <strong>that failed the EMC test</strong> must be reworked."</em> No commas: the clause RESTRICTS. It says WHICH units &mdash; those six, and nobody else. Now the second: <em>"The interlocking units<strong>, which failed the EMC test,</strong> must be reworked."</em> Two commas, and the clause no longer restricts anything: it simply ADDS a fact about all of them. It says that all forty failed. And all forty did not fail, so Jo&#227;o has just written a claim he cannot prove, and the first person to notice will be their lawyer. One comma. Thirty-four units.</p>
        <p>So he writes it the way it has to be written. The six units <strong>that failed</strong> are to be reworked at the supplier's cost. The grounding configuration<strong>, which is common to all forty units,</strong> must be re-verified &mdash; a fact about the whole batch, stated as a fact, without pretending the whole batch failed. Then he compresses, the way every standard on his shelf compresses: the report <strong>issued on 14 July</strong> does not cover the configuration, and the units <strong>radiating above the limit</strong> are the six on the northbound platform. And he closes with the two questions that no <strong>ambiguity</strong> survives: please confirm the standard <strong>to which the design was certified</strong>, and <strong>spell out</strong> the conditions <strong>under which</strong> the EMC test was performed &mdash; on the bench, or as installed? The supplier's answer arrives nine days later. Their team has <strong>devised</strong> a <strong>workaround</strong>, ferrite filters, and they are careful too: the filters will meet the <strong>acceptance criteria</strong> applicable <em>to the trial run</em>. Not to the handover. In a technical document, nobody writes a relative clause by accident."""

QUIZZES_CONTEXT = [
    ("1. \"The interlocking units <em>that failed the EMC test</em> must be reworked.\" Quantas unidades o fornecedor tem de retrabalhar?",
     [("As quarenta &mdash; a ora&#231;&#227;o descreve as unidades em geral.", False),
      ("As SEIS &mdash; sem v&#237;rgulas, a ora&#231;&#227;o RESTRINGE: ela diz QUAIS unidades. Tire a ora&#231;&#227;o e voc&#234; nem sabe mais do que se est&#225; falando.", True),
      ("Depende do contrato; a gram&#225;tica n&#227;o decide isso.", False)]),
    ("2. E na vers&#227;o \"The interlocking units<em>, which failed the EMC test,</em> must be reworked\"? O que MUDA?",
     [("Nada &mdash; a v&#237;rgula em ingl&#234;s &#233; s&#243; uma pausa de leitura.", False),
      ("Fica mais formal, mas o sentido &#233; o mesmo.", False),
      ("MUDA TUDO: com as duas v&#237;rgulas a ora&#231;&#227;o deixa de restringir e passa a ACRESCENTAR um fato sobre TODAS. A frase agora afirma que as quarenta reprovaram &mdash; o que &#233; falso, e ser&#225; usado contra quem escreveu.", True)]),
    ("3. \"The report <em>issued on 14 July</em> does not cover the grounding.\" Que estrutura &#233; essa?",
     [("Uma relativa REDUZIDA: caiu o <em>which was</em>. Sobrou o partic&#237;pio passado, com sentido PASSIVO &mdash; o relat&#243;rio QUE FOI emitido. &#201; assim que toda norma t&#233;cnica &#233; escrita.", True),
      ("Um erro: falta o verbo principal.", False),
      ("Um ger&#250;ndio, como em portugu&#234;s (\"o relat&#243;rio emitindo\").", False)]),
    ("4. Which sentence is correct?",
     [("\"Please confirm the standard to that the design was certified.\"", False),
      ("\"Please confirm the standard to which the design was certified.\"", True),
      ("\"Please confirm the standard which the design was certified to it.\"", False)]),
]

BLANKS = [
    ("that failed", "Dica: sem v&#237;rgulas, para RESTRINGIR &mdash; s&#243; as seis, e mais ningu&#233;m",
     "The six interlocking units that failed the EMC test must be reworked at the supplier's cost.",
     '"The six interlocking units ', ' the EMC test must be reworked at the supplier\'s cost."'),
    ("which is common to all forty units", "Dica: entre v&#237;rgulas, para ACRESCENTAR um fato sobre TODAS &mdash; e nunca <em>that</em> depois de v&#237;rgula",
     "The grounding configuration, which is common to all forty units, must be re-verified.",
     '"The grounding configuration, ', ', must be re-verified."'),
    ("issued", "Dica: relativa REDUZIDA &mdash; caiu o <em>which was</em> e ficou o partic&#237;pio PASSADO (sentido passivo)",
     "The report issued on 14 July does not cover the grounding configuration.",
     '"The report ', ' on 14 July does not cover the grounding configuration."'),
    ("radiating", "Dica: relativa reduzida ATIVA &mdash; caiu o <em>which are</em> e ficou o <em>-ing</em>: as unidades que EST&#195;O emitindo",
     "The units radiating above the limit are the six on the northbound platform.",
     '"The units ', ' above the limit are the six on the northbound platform."'),
    ("to which", "Dica: a preposi&#231;&#227;o vem ANTES de <em>which</em> &mdash; e depois de preposi&#231;&#227;o nunca cabe <em>that</em>",
     "Please confirm the standard to which the design was certified.",
     '"Please confirm the standard ', ' the design was certified."'),
    ("under which", "Dica: mesma estrutura formal &mdash; preposi&#231;&#227;o + <em>which</em>: em que CONDI&#199;&#213;ES o ensaio foi feito",
     "Please spell out the conditions under which the EMC test was performed.",
     '"Please spell out the conditions ', ' the EMC test was performed."'),
]

ORDER = [
    (1, "Restrict the scope: the six interlocking units that failed the EMC test are to be reworked."),
    (2, "Add the fact about all forty: the grounding configuration, which is common to the whole batch, has not been verified as installed."),
    (3, "Compress the evidence: the report issued on 14 July does not cover the configuration."),
    (4, "Ask formally: please confirm the standard to which the design was certified."),
    (5, "Ask formally again: please spell out the conditions under which the test was performed."),
    (6, "Close the workaround: the ferrite filters are accepted for the trial run only, and not for the handover."),
]

SPEECH = [
    ("The six interlocking units that failed the EMC test must be reworked at the supplier's cost.",
     "As seis unidades de intertravamento que reprovaram no ensaio de EMC devem ser retrabalhadas às custas do fornecedor."),
    ("The grounding configuration, which is common to all forty units, must be re-verified.",
     "A configuração de aterramento, que é comum às quarenta unidades, precisa ser reverificada."),
    ("The report issued on 14 July does not cover the grounding configuration.",
     "O relatório emitido em 14 de julho não cobre a configuração de aterramento."),
    ("Please confirm the standard to which the design was certified.",
     "Por favor, confirme a norma segundo a qual o projeto foi certificado."),
    ("The workaround that your team devised does not meet the acceptance criteria that apply at handover.",
     "A solução paliativa que a equipe de vocês concebeu não atende aos critérios de aceitação válidos no handover."),
]

QUIZZES_SIT = [
    ("Voc&#234; quer que o fornecedor retrabalhe APENAS as seis unidades reprovadas. Voc&#234; escreve:",
     [("\"The interlocking units, which failed the EMC test, must be reworked at your cost.\"", False),
      ("\"The six interlocking units that failed the EMC test on 14 July must be reworked at your cost.\"", True),
      ("\"Please rework the units with the interference problem as soon as possible.\"", False)]),
    ("Voc&#234; quer registrar que o aterramento &#233; o MESMO nas quarenta &mdash; sem afirmar que as quarenta reprovaram:",
     [("\"The forty units, which failed the EMC test, share the same grounding configuration.\"", False),
      ("\"The grounding configuration, which is common to all forty units, has not been verified in the installed condition.\"", True),
      ("\"All the units have a grounding problem that needs to be looked at.\"", False)]),
    ("Ingrid diz: \"Trinta e quatro unidades passaram, logo o projeto est&#225; correto.\" A resposta mais forte &#233;:",
     [("\"That is a reasonable hypothesis, and it may well be right. But thirty-four units passing a test does not demonstrate a design &mdash; and two of them passed by almost nothing.\"", True),
      ("\"That is not true and you know it.\"", False),
      ("\"All right. If thirty-four passed, let us close the design question.\"", False)]),
    ("Ela oferece filtros de ferrite \"que resolvem em uma semana\". Voc&#234; responde:",
     [("\"Perfect. If the emissions come down, we can consider it closed.\"", False),
      ("\"I will take the filters for the trial run. I will not take them for the handover, because a workaround does not meet the acceptance criteria that apply at handover.\"", True),
      ("\"We do not accept workarounds under any circumstances.\"", False)]),
    ("Voc&#234; precisa saber COMO eles ensaiaram (na bancada ou instalado). Voc&#234; pergunta:",
     [("\"How did you do the test exactly? Can you explain it to me?\"", False),
      ("\"Please spell out the conditions under which the EMC test was performed, and confirm the standard to which the design was certified.\"", True),
      ("\"The conditions which you tested the design in them are not clear.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l8\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l8\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l8\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Estrutura / Structure</th><th style="padding:.7rem;text-align:left">O que faz / What it does</th><th style="padding:.7rem;text-align:left">Exemplo</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Relativa RESTRITIVA<br><em>sem v&#237;rgulas</em><br>(<em>that</em> / <em>which</em> / <em>who</em>)</td><td style="padding:.6rem">RESTRINGE: diz QUAIS. Tire a ora&#231;&#227;o e voc&#234; n&#227;o sabe mais do que se fala. &#201; ela que define o ESCOPO do trabalho &mdash; e escopo &#233; dinheiro.</td><td style="padding:.6rem">"The six units <strong>that failed the EMC test</strong> must be reworked." &mdash; <em>s&#243; aquelas seis.</em></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Relativa N&#195;O-RESTRITIVA<br><em>entre duas v&#237;rgulas</em><br>(NUNCA <em>that</em>)</td><td style="padding:.6rem">ACRESCENTA um fato sobre TODAS. Tire a ora&#231;&#227;o e a frase continua de p&#233;. Depois de v&#237;rgula, s&#243; <em>which</em> (coisas) ou <em>who</em> (pessoas).</td><td style="padding:.6rem">"The units<strong>,</strong> which failed the test<strong>,</strong> must be reworked." &mdash; <em>TODAS as quarenta reprovaram.</em></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Relativa REDUZIDA<br><em>partic&#237;pio passado</em></td><td style="padding:.6rem">Cai o <em>which was / that were</em> quando o sentido &#233; PASSIVO. &#201; a compress&#227;o de toda norma t&#233;cnica que ele l&#234;.</td><td style="padding:.6rem">"the report <em>which was</em> <strong>issued</strong> on 14 July" &rarr; "the report <strong>issued on 14 July</strong>"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Relativa REDUZIDA<br><em>-ing</em></td><td style="padding:.6rem">Cai o <em>which is / that are</em> quando o sentido &#233; ATIVO: a unidade est&#225; FAZENDO, n&#227;o sofrendo.</td><td style="padding:.6rem">"the units <em>which are</em> <strong>radiating</strong> above the limit" &rarr; "the units <strong>radiating above the limit</strong>"</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Preposi&#231;&#227;o + <em>which</em></td><td style="padding:.6rem">O registro formal do RFI e da especifica&#231;&#227;o. A preposi&#231;&#227;o vem ANTES de <em>which</em> &mdash; e depois de preposi&#231;&#227;o nunca cabe <em>that</em>.</td><td style="padding:.6rem">"the standard <strong>to which</strong> the design was certified" &middot; "the conditions <strong>under which</strong> the test was performed"</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">Seis unidades reprovaram. Quarenta t&#234;m o mesmo aterramento. "The units <strong>that failed</strong>" compromete o fornecedor com <strong>seis</strong>. "The units<strong>, which failed,</strong>" afirma que as <strong>quarenta</strong> reprovaram &mdash; o que &#233; falso, e o advogado deles vai apontar isso na primeira leitura. E "the grounding configuration<strong>, which is common to all forty units,</strong> must be re-verified" consegue as quarenta <em>pelo motivo certo</em>. A gram&#225;tica aqui n&#227;o &#233; enfeite: ela &#233; o escopo do contrato.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (tr&#234;s erros de brasileiro):</strong> (1) <em>"The RFI that we submitted <span style="color:#dc2626">it</span> on Monday"</em> &mdash; em portugu&#234;s dizemos "o RFI que a gente mandou ELE"; em ingl&#234;s o pronome N&#195;O se repete: o <em>that</em> j&#225; &#233; o objeto; (2) <em>"the configuration, <span style="color:#dc2626">that</span> is common to all forty"</em> &mdash; depois de v&#237;rgula, <strong>that</strong> &#233; imposs&#237;vel: use <strong>which</strong>; (3) <em>"the cable <span style="color:#dc2626">installing</span> last week"</em> &mdash; o cabo n&#227;o est&#225; instalando nada: ele FOI instalado, ent&#227;o &#233; <strong>installed</strong> (partic&#237;pio passado). O portugu&#234;s cobre os dois casos com a mesma forma; o ingl&#234;s n&#227;o.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Colloca&#231;&#245;es do RFI:</strong> <strong>submit</strong> an RFI (nunca "send"), <strong>respond to</strong> technical queries (nunca "answer to"), <strong>verify compliance with</strong> the specs (nunca "compliance TO"), <strong>ensure</strong> interoperability, <strong>validate</strong> the design, <strong>exceed</strong> the emission limit, <strong>implement</strong> a workaround, <strong>fall outside</strong> the scope, <strong>meet</strong> the acceptance criteria.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>A pergunta que se faz antes de enviar:</strong> "<em>Can this sentence be read in a second way that costs me money?</em>" Se puder, ela ainda n&#227;o est&#225; pronta. Ambiguidade n&#227;o &#233; confus&#227;o: a frase amb&#237;gua parece perfeitamente clara &mdash; e &#233; exatamente por isso que passa.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1568992687947-868a62a9f521?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 08 -- Pre-class</div>
      <h3>Say Exactly What You Mean -- Writing the RFI</h3>
      <div class="lesson-desc">Seis unidades de intertravamento reprovaram no ensaio de EMC &mdash; e as quarenta foram constru&#237;das com a mesma configura&#231;&#227;o de aterramento. Como escrever o RFI que fecha o escopo nas seis, registra o fato sobre as quarenta e n&#227;o pode ser lido de dois jeitos. Key words: request for information (RFI), request for proposal (RFP), interoperability, electromagnetic compatibility (EMC), grounding, interlocking, fail-safe, redundancy, acceptance criteria, workaround, ambiguity, to spell out, to devise, to pin down. Structure: ora&#231;&#245;es relativas &mdash; restritiva x n&#227;o-restritiva (a v&#237;rgula que muda o contrato), relativas reduzidas e preposi&#231;&#227;o + <em>which</em>.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="8" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="8">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 7 voc&#234; transformou mem&#243;ria em registro. Aqui voc&#234; escreve o documento &mdash; e um documento t&#233;cnico n&#227;o &#233; lido, &#233; interpretado. S&#227;o as palavras do esclarecimento formal: o que se pergunta, o que se mede, e o que se aceita s&#243; provisoriamente. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l8">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Relative Clauses &amp; Precision</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como a v&#237;rgula decide o escopo &mdash; e por que a mesma frase, com e sem ela, compromete o fornecedor com seis unidades ou com quarenta (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the RFI in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os passos do RFI na ordem correta &mdash; do escopo restrito at&#233; o prazo de morte da solu&#231;&#227;o paliativa.</p>
      <div class="order-container" id="order-l8">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l8')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. Repare na PAUSA das v&#237;rgulas na segunda frase: em ingl&#234;s falado a n&#227;o-restritiva se OUVE &mdash; h&#225; uma pausa antes e depois, e ela &#233; o que avisa o interlocutor de que voc&#234; est&#225; falando de todas as quarenta. E diga in-ter-op-er-a-BIL-i-ty, com o acento na quinta s&#237;laba.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da call de esclarecimento t&#233;cnico &mdash; inclusive quando a fornecedora argumenta que trinta e quatro aprova&#231;&#245;es provam o projeto, ou oferece um paliativo como se fosse a solu&#231;&#227;o.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: preciso no escopo, honesto na incerteza, e imposs&#237;vel de reinterpretar.</p>
      <div class="think-card">
        <div class="think-question">You are opening the clarification call on RFI-114. In ninety seconds: restrict the scope to the six interlocking units that failed the EMC test on 14 July, add the fact about the grounding configuration that is common to all forty without claiming that all forty failed, refuse the argument that thirty-four passes prove the design, accept the ferrite filters for the trial run only and give them an end date, and close with the two questions you need in writing -- the standard to which the design was certified, and the conditions under which the test was performed.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-8"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 8</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
