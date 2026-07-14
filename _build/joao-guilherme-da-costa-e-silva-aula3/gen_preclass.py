#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 3 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 3 IN CLASS (mesmo tema/gramática/vocab).
"""
import os
import random

random.seed(3)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Non-conformance", "a documented failure to meet a requirement of the specification", "não conformidade",
     "\"We raised a non-conformance on the cable routing.\""),
    ("Punch list", "the list of small open items that must be closed before acceptance", "lista de pendências",
     "\"Three items on the punch list are still open.\""),
    ("Hold point", "a stage where the work must STOP until the inspection has been done", "ponto de parada obrigatória",
     "\"The cable test is a hold point -- nobody continues without us.\""),
    ("Witness point", "an inspection you may attend, but the work does not stop if you do not", "ponto de testemunho",
     "\"The insulation test is a witness point, not a hold point.\""),
    ("Inspection test plan (ITP)", "the document that lists every test, who attends it and when", "plano de inspeção e testes",
     "\"The ITP defines every hold point on the project.\""),
    ("Factory acceptance test (FAT)", "the test you run at the supplier's factory, before anything is shipped", "teste de aceitação em fábrica",
     "\"The FAT in Berlin is scheduled for October.\""),
    ("Site acceptance test (SAT)", "the same test, repeated on site after the equipment is installed", "teste de aceitação em campo",
     "\"The SAT starts two weeks after installation.\""),
    ("Escalation", "taking an unresolved issue to a higher level of management", "escalonamento",
     "\"If the date slips again, escalation is the only option left.\""),
    ("Corrective action", "the concrete step a supplier takes to fix a non-conformance", "ação corretiva",
     "\"We agreed on a corrective action with a deadline.\""),
    ("Waiver", "a formal written permission to skip one requirement, just once", "dispensa formal",
     "\"They asked for a waiver on the insulation test.\""),
    ("Baseline schedule", "the approved schedule that every delay is measured against", "cronograma de referência",
     "\"The revised baseline schedule is three weeks late.\""),
    ("To follow up on", "to check again on something you have already asked for", "dar seguimento a, cobrar",
     "\"I'm following up on the ITP we requested last week.\""),
    ("To flag up", "to raise a problem early, so that nobody is surprised later", "sinalizar",
     "\"I want to flag up a risk on the delivery date.\""),
    ("To push back on", "to question or resist a request politely, but firmly", "questionar, resistir a",
     "\"I have to push back on that date -- it is not realistic.\""),
]

SURVIVAL = [
    ("I'd like to follow up on the revised baseline schedule.",
     "Gostaria de dar seguimento ao cronograma de referência revisado."),
    ("The inspection test plan should have been submitted by last Friday.",
     "O plano de inspeção e testes deveria ter sido enviado até a sexta-feira passada."),
    ("There must have been a miscommunication about the hold points.",
     "Deve ter havido um ruído de comunicação sobre os pontos de parada."),
    ("To some extent I understand your position, however I have to push back on that date.",
     "Em certa medida eu entendo a sua posição, no entanto preciso questionar essa data."),
    ("Can we agree on a corrective action and a new deadline?",
     "Podemos combinar uma ação corretiva e um novo prazo?"),
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


CONTEXT = """<p>It is Monday morning and Jo&#227;o Guilherme is chairing the status meeting with CASCO. Four items are open on the <strong>punch list</strong>. The revised <strong>baseline schedule</strong> is three weeks overdue, the <strong>inspection test plan</strong> was submitted with no <strong>hold points</strong>, a <strong>waiver</strong> was requested on the insulation test, and a <strong>non-conformance</strong> is still waiting for a <strong>corrective action</strong>.</p>
        <p>He opens the call. "I would like to <strong>follow up on</strong> the schedule. It <strong>should have reached</strong> us on June 10th, and we are now planning the <strong>site acceptance test</strong> without a date. There <strong>must have been</strong> a bottleneck on your side." The supplier answers that her team <strong>might have been</strong> waiting for the interface document &mdash; but that document was signed in April, and Jo&#227;o has to <strong>push back on</strong> it. Politely: "To some extent I understand your position, however the document was signed in April."</p>
        <p>Then he <strong>flags up</strong> the second issue. The ITP arrived with <strong>witness points</strong> only, which means the factory never stops for Motiva. "That <strong>should have been</strong> discussed with us before the plan was submitted." They agree on a corrective action, a new date, and one last rule: if the date slips again, <strong>escalation</strong> is the next step. The <strong>factory acceptance test</strong> in October is already at risk, and nobody wants to discover that in an email."""

QUIZZES_CONTEXT = [
    ("1. \"The revised baseline schedule should have reached us on June 10th.\" O cronograma chegou no dia 10 de junho?",
     [("N&#227;o. <em>Should have</em> + partic&#237;pio descreve uma obriga&#231;&#227;o que N&#195;O foi cumprida &mdash; a cr&#237;tica recai sobre a A&#199;&#195;O, n&#227;o sobre a pessoa.", True),
      ("Sim. Chegou no prazo e o item foi fechado.", False),
      ("Ainda n&#227;o sabemos &mdash; a frase fala do futuro.", False)]),
    ("2. \"There must have been a bottleneck on your side.\" O que o <em>must have</em> expressa aqui?",
     [("Uma obriga&#231;&#227;o n&#227;o cumprida.", False),
      ("Uma DEDU&#199;&#195;O l&#243;gica: pela evid&#234;ncia, o falante est&#225; quase certo do que aconteceu.", True),
      ("Uma possibilidade remota e incerta.", False)]),
    ("3. Por que \"It should have been discussed with us\" &#233; mais profissional do que \"You didn't discuss it with us\"?",
     [("Porque &#233; mais longa e soa mais formal.", False),
      ("Porque afirma um fato sobre o PROCESSO sem atacar a pessoa &mdash; o fornecedor pode concordar sem perder a face, e a reuni&#227;o termina em a&#231;&#227;o corretiva, e n&#227;o em briga.", True),
      ("Porque evita mencionar o problema.", False)]),
    ("4. Which sentence is correct?",
     [("\"The supplier should had submitted the ITP in May.\"", False),
      ("\"The supplier should have submitted the ITP in May.\"", True),
      ("\"The supplier should have submit the ITP in May.\"", False)]),
]

BLANKS = [
    ("should have reached", "Dica: obriga&#231;&#227;o N&#195;O cumprida &mdash; should have + partic&#237;pio",
     "The revised baseline schedule should have reached us on June 10th.",
     '"The revised baseline schedule ', ' us on June 10th."'),
    ("must have been", "Dica: DEDU&#199;&#195;O sobre o passado &mdash; must have + partic&#237;pio (nunca \"must be\")",
     "There must have been a miscommunication about the hold points.",
     '"There ', ' a miscommunication about the hold points."'),
    ("might have been sent", "Dica: possibilidade INCERTA &mdash; might have + partic&#237;pio (voz passiva)",
     "The drawings might have been sent to the wrong contact.",
     '"The drawings ', ' to the wrong contact."'),
    ("follow up on", "Dica: cobrar de novo algo que voc&#234; j&#225; pediu &mdash; e a preposi&#231;&#227;o &#233; ON",
     "I would like to follow up on the revised baseline schedule.",
     '"I would like to ', ' the revised baseline schedule."'),
    ("push back on", "Dica: questionar com firmeza e educa&#231;&#227;o &mdash; e a preposi&#231;&#227;o &#233; ON",
     "I have to push back on that date, it is not realistic.",
     '"I have to ', ' that date, it is not realistic."'),
    ("corrective action", "Dica: o passo concreto que o fornecedor toma para corrigir uma n&#227;o conformidade",
     "Can we agree on a corrective action and a new deadline?",
     '"Can we agree on a ', ' and a new deadline?"'),
]

ORDER = [
    (1, "Thank the supplier for joining and state the agenda: the open items on the punch list."),
    (2, "Follow up on the overdue item and say what should have happened, and when."),
    (3, "Deduce the cause with a modal perfect, instead of accusing the supplier."),
    (4, "Push back diplomatically when the supplier moves the responsibility to you."),
    (5, "Agree on a corrective action with a date, and say what happens if the date slips again."),
]

SPEECH = [
    ("I'd like to follow up on the revised baseline schedule.",
     "Gostaria de dar seguimento ao cronograma de referência revisado."),
    ("The inspection test plan should have been submitted by last Friday.",
     "O plano de inspeção e testes deveria ter sido enviado até a sexta-feira passada."),
    ("There must have been a miscommunication about the hold points.",
     "Deve ter havido um ruído de comunicação sobre os pontos de parada."),
    ("To some extent I understand your position, however I have to push back on that date.",
     "Em certa medida eu entendo a sua posição, no entanto preciso questionar essa data."),
    ("Can we agree on a corrective action and a new deadline?",
     "Podemos combinar uma ação corretiva e um novo prazo?"),
]

QUIZZES_SIT = [
    ("You open the status meeting. The revised baseline schedule is three weeks overdue. You say:",
     [("\"You are three weeks late. Again.\"", False),
      ("\"I'd like to follow up on the revised baseline schedule &mdash; it should have reached us on June 10th.\"", True),
      ("\"Where is the schedule? I asked many times.\"", False)]),
    ("The supplier blames YOU: \"We were waiting for your interface document.\" It was signed in April. You answer:",
     [("\"To some extent I understand your position, however the interface document was signed in April. I have to push back on that.\"", True),
      ("\"That is a lie and you know it.\"", False),
      ("\"Ok, maybe it was our fault, let's move on.\"", False)]),
    ("The ITP arrived with no hold points, only witness points. The most professional way to raise it is:",
     [("\"You removed our hold points on purpose.\"", False),
      ("\"I'd like to flag up an issue: the ITP has no hold points. That should have been discussed with us before it was submitted.\"", True),
      ("\"The ITP is wrong. Send it again.\"", False)]),
    ("The equipment arrived damaged and nobody knows why. You want to deduce the cause without accusing anyone. You say:",
     [("\"Somebody in your factory was careless.\"", False),
      ("\"There must have been a problem in transport &mdash; or it might have been damaged before it left the factory.\"", True),
      ("\"It must be a problem in transport last week.\"", False)]),
    ("The supplier asks for a waiver that saves them three days in the factory but risks three weeks on site. You:",
     [("\"Sure, no problem, we can skip that test.\"", False),
      ("\"One could argue that three days in the factory cost us three weeks during the site acceptance test. I'm afraid I have to push back on that waiver.\"", True),
      ("\"Waivers are always forbidden here.\"", False)]),
]


def quiz_html(items, start=1):
    out = []
    for i, (q, opts) in enumerate(items):
        qq = q if q[0].isdigit() else f'{q}'
        o = []
        for j, (text, correct) in enumerate(opts):
            letter = 'ABC'[j]
            o.append(
                f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}">'
                f'<span class="option-letter">{letter}</span> {text}</div>')
        out.append(
            f'      <div class="quiz-item"><div class="quiz-question">{qq}</div>'
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l3\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l3\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l3\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Function / Fun&#231;&#227;o</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Afirmativa<br><strong>should have</strong> + partic&#237;pio</td><td style="padding:.6rem">Obriga&#231;&#227;o que N&#195;O foi cumprida. A cr&#237;tica recai sobre a a&#231;&#227;o, nunca sobre a pessoa. An obligation that was not met.</td><td style="padding:.6rem">"The ITP <strong>should have been</strong> submitted on June 3rd."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>must have</strong> + partic&#237;pio</td><td style="padding:.6rem">DEDU&#199;&#195;O l&#243;gica sobre o passado: pela evid&#234;ncia, voc&#234; est&#225; quase certo. Soa anal&#237;tico, n&#227;o acusat&#243;rio.</td><td style="padding:.6rem">"There <strong>must have been</strong> a bottleneck on your side."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>might / may have</strong> + partic&#237;pio</td><td style="padding:.6rem">POSSIBILIDADE incerta. Abre uma porta e deixa o outro salvar a face.</td><td style="padding:.6rem">"The drawings <strong>might have been sent</strong> to the wrong contact."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa / imposs&#237;vel<br><strong>could not have</strong> + partic&#237;pio</td><td style="padding:.6rem">IMPOSSIBILIDADE: a evid&#234;ncia descarta a hip&#243;tese.</td><td style="padding:.6rem">"They <strong>could not have run</strong> the FAT without the cabinet."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">What <strong>should have happened</strong>? / <strong>Could</strong> it <strong>have been</strong> lost?</td><td style="padding:.6rem"><strong>"What should have happened</strong> after the design review?"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Na fala (contra&#231;&#227;o)</td><td style="padding:.6rem">O <em>have</em> reduz para /&#601;v/ &mdash; &#233; o que voc&#234; realmente ouve numa call.</td><td style="padding:.6rem">"It <strong>should've been</strong> flagged up." &middot; "They <strong>must've missed</strong> it."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">"You didn't deliver" ataca uma pessoa e a reuni&#227;o trava. "<strong>This should have been delivered</strong>" afirma um fato sobre o processo &mdash; e o fornecedor pode concordar sem perder a face. &#201; assim que voc&#234; sai da reuni&#227;o com uma <strong>a&#231;&#227;o corretiva</strong>, e n&#227;o com um inimigo.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (dois erros de brasileiro):</strong> (1) depois de um modal vem SEMPRE <strong>have</strong>, nunca <em>had</em> &mdash; "should <strong>have</strong> submitted", jamais "should <em>had</em> submitted"; (2) para deduzir sobre o PASSADO em ingl&#234;s n&#227;o basta o presente: "it <em>must be</em> a miscommunication" fala do agora. Sobre o passado, o correto &#233; "there <strong>must have been</strong> a miscommunication".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Hedging &mdash; a linguagem da discord&#226;ncia diplom&#225;tica:</strong> "<strong>It would appear that...</strong>" (ao inv&#233;s de "you are wrong"), "<strong>One could argue that...</strong>" (ao inv&#233;s de "that makes no sense"), "<strong>To some extent I understand your position, however...</strong>" (ao inv&#233;s de "no"). S&#227;o as tr&#234;s f&#243;rmulas que sustentam uma discord&#226;ncia sem romper a rela&#231;&#227;o &mdash; e que ficam bem na ata que o diretor vai ler."""


HTML = f"""<div class="lesson-card" id="ex-lesson-3">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 03 -- Pre-class</div>
      <h3>Running and Following Status Meetings -- Reporting, Updating and Pushing Back</h3>
      <div class="lesson-desc">Conduzir uma reuni&#227;o de status com um fornecedor atrasado: relatar, deduzir a causa e questionar a data sem romper a rela&#231;&#227;o. Key words: non-conformance, punch list, hold point, witness point, inspection test plan (ITP), factory acceptance test (FAT), site acceptance test (SAT), escalation, corrective action, waiver, baseline schedule, to follow up on, to flag up, to push back on. Structure: modal perfects (should have / must have / might have / could not have + partic&#237;pio) + hedging ("It would appear that...", "One could argue that...", "To some extent I understand your position, however...").</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="3" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="3">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 2 voc&#234; nomeou as A&#199;&#213;ES do seu papel. Aqui voc&#234; nomeia a PAUTA da reuni&#227;o: o que se inspeciona, o que se encontra e o que se faz a respeito. Voc&#234; j&#225; conhece todos estes conceitos em portugu&#234;s &mdash; o trabalho &#233; s&#243; trocar a etiqueta. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l3">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Modal Perfects</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como dizer o que DEVERIA ter sido feito, deduzir POR QUE n&#227;o foi, e discordar sem romper a rela&#231;&#227;o (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Status Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma reuni&#227;o de status com um fornecedor atrasado na ordem correta.</p>
      <div class="order-container" id="order-l3">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l3')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem, conduzem e fecham qualquer reuni&#227;o de status em ingl&#234;s. Repare na contra&#231;&#227;o do <em>have</em> na fala: "should've been", "must've been".</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma reuni&#227;o de status &mdash; inclusive quando o fornecedor devolve a culpa para voc&#234;.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: profissional, firme, n&#227;o confrontador.</p>
      <div class="think-card">
        <div class="think-question">Open a status meeting with a supplier who is three weeks late on the revised baseline schedule. Follow up on the overdue item (I'd like to follow up on...), state the obligation that was not met (It should have reached us on...), deduce the cause without accusing anyone (There must have been... / It might have been...), push back diplomatically when the supplier moves the responsibility to you (To some extent I understand your position, however...), and close by agreeing on a corrective action with a new deadline.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-3"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 3</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
