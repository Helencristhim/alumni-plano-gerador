#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 6 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 6 IN CLASS (mesmo tema/gramática/vocab — passiva avançada + causativo).
"""
import os
import random

random.seed(6)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Deviation", "a departure from what the approved specification requires", "desvio (aprovado antes da execução)",
     "\"The deviation was accepted in writing, so no rework is required.\""),
    ("Submittal", "a document the supplier formally sends to the client for review and approval", "documento submetido à aprovação",
     "\"The submittal was returned with comments on Tuesday.\""),
    ("Approval workflow", "the sequence of reviews a document must pass before it is accepted", "fluxo de aprovação",
     "\"The drawing is stuck in the approval workflow, not on my desk.\""),
    ("Inspection release", "the formal authorization to ship, or to move to the next stage, after an inspection", "liberação de inspeção",
     "\"No inspection release has been issued, so nothing leaves the factory.\""),
    ("Out of tolerance", "outside the range of values the specification allows", "fora de tolerância",
     "\"The relay was found to be out of tolerance during the functional test.\""),
    ("Calibration certificate", "the document that proves an instrument was verified against a reference", "certificado de calibração",
     "\"The calibration certificate had not been issued at the time of the test.\""),
    ("Traceability", "being able to track a part back to its material, its test and its records", "rastreabilidade",
     "\"In signaling, a component without traceability does not exist.\""),
    ("Root cause", "the underlying reason a failure happened, not the symptom you can see", "causa raiz",
     "\"The root cause has not been identified yet, so the corrective action is premature.\""),
    ("Rework", "work that has to be done a second time to correct a defect", "retrabalho",
     "\"The rework will be carried out at the supplier's own cost.\""),
    ("Sign-off", "the formal written approval that closes a stage and lets the project move on", "aprovação formal, aceite",
     "\"I cannot give you sign-off until the calibration certificate is on file.\""),
    ("To downplay", "to make a problem sound smaller than it really is", "minimizar (um problema)",
     "\"He downplayed the failure: 'It is a minor deviation, nothing more.'\""),
    ("To raise a concern", "to put a risk formally on the record, before it becomes a problem", "levantar uma preocupação formalmente",
     "\"I would like to raise a concern about the traceability of that batch.\""),
    ("To hold your ground", "to keep your position when the other side pushes back", "manter a sua posição",
     "\"He downplayed it twice, and twice I held my ground.\""),
    ("To pass the buck", "to shift responsibility to somebody else instead of owning it (informal)", "empurrar a responsabilidade para outro",
     "\"Blaming the subcontractor is passing the buck: our contract is with you.\""),
]

SURVIVAL = [
    ("The relay was found to be out of tolerance during the functional test.",
     "O relé foi constatado fora de tolerância durante o teste funcional."),
    ("The calibration certificate had not been issued at the time of the test.",
     "O certificado de calibração não havia sido emitido na data do teste."),
    ("It would appear that the deviation was caused by the calibration drift.",
     "Tudo indica que o desvio foi causado pela deriva de calibração."),
    ("We need to have the report resubmitted by Friday.",
     "Precisamos que o relatório seja reenviado até sexta-feira."),
    ("Sign-off cannot be granted while the hold point remains open.",
     "O aceite não pode ser concedido enquanto o hold point permanecer aberto."),
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


CONTEXT = """<p>The factory acceptance test <strong>was carried out</strong> on a Tuesday morning, with Jo&#227;o Guilherme watching on a video link from S&#227;o Paulo. The safety relay <strong>was found to be</strong> <strong>out of tolerance</strong>: eleven milliseconds, against a specified range of five to seven. The test <strong>was witnessed</strong>, a hold point <strong>was triggered</strong>, and no <strong>inspection release</strong> <strong>was issued</strong>. Then the report arrived from the supplier, and every sentence in it had been written to make the failure disappear.</p>
        <p>Two things <strong>had not been done</strong> at the time of the test. The <strong>calibration certificate</strong> for the reference instrument <strong>had not been issued</strong>, and the <strong>root cause</strong> <strong>had not been identified</strong>. The report calls the failure a minor <strong>deviation</strong> and asks for a waiver, which is the polite way of asking Jo&#227;o to pay for somebody else's <strong>rework</strong>. On the call, the quality manager <strong>downplays</strong> it &mdash; "the unit works" &mdash; and then <strong>passes the buck</strong>: the calibration, she says, was performed by a subcontractor. Jo&#227;o <strong>holds his ground</strong>. A deviation is approved <em>before</em> the work; this was found <em>after</em> it. The contract is with her company, not with the subcontractor.</p>
        <p>So he states what has to happen, and he states it in the passive, because the obligation belongs to the procedure and not to him. "A corrective action <strong>must be implemented</strong> before the retest. We need to <strong>have the report resubmitted</strong> through the <strong>approval workflow</strong> by Friday, and we will <strong>have the relay retested</strong> with a valid certificate in place. I would also like to <strong>raise a concern</strong> about the <strong>traceability</strong> of that batch. <strong>Sign-off</strong> <strong>cannot be granted</strong> while the hold point remains open." Nobody <strong>was accused</strong>. Nothing <strong>was denied</strong>. And the relay is being retested on Thursday."""

QUIZZES_CONTEXT = [
    ("1. \"The relay was found to be out of tolerance.\" Por que o engenheiro escolhe o passivo, em vez de \"Your technician calibrated it badly\"?",
     [("Porque o passivo &#233; mais educado, ainda que mais fraco.", False),
      ("Porque o passivo tira a PESSOA da frase e deixa o FATO. Uma acusa&#231;&#227;o se contesta e se defende; uma constata&#231;&#227;o s&#243; pode ser FECHADA &mdash; e &#233; por isso que todo relat&#243;rio de inspe&#231;&#227;o &#233; escrito assim.", True),
      ("Porque em ingl&#234;s t&#233;cnico &#233; proibido usar a voz ativa.", False)]),
    ("2. \"The calibration certificate had not been issued at the time of the test.\" O que o passivo PERFEITO faz aqui que o passivo simples n&#227;o faria?",
     [("Data a aus&#234;ncia: no MOMENTO do teste, aquele documento ainda n&#227;o existia &mdash; e por isso ele n&#227;o cobre o teste. Emitir depois n&#227;o resolve.", True),
      ("Apenas soa mais formal; o sentido &#233; o mesmo de \"was not issued\".", False),
      ("Indica que o certificado nunca ser&#225; emitido.", False)]),
    ("3. \"We need to have the report resubmitted by Friday.\" QUEM reenvia o relat&#243;rio?",
     [("Eu mesmo, porque <em>have</em> significa \"ter que fazer\".", False),
      ("Ningu&#233;m &mdash; a frase apenas descreve uma inten&#231;&#227;o.", False),
      ("O FORNECEDOR. O causativo <em>have something done</em> diz que a a&#231;&#227;o &#233; EXIGIDA por mim e EXECUTADA por outro. Eu n&#227;o fa&#231;o o trabalho; eu o determino.", True)]),
    ("4. Which sentence is correct?",
     [("\"We need to have resubmitted the report by Friday.\"", False),
      ("\"We need to have the report resubmitted by Friday.\"", True),
      ("\"We need to have the report resubmit by Friday.\"", False)]),
]

BLANKS = [
    ("was found to be", "Dica: passivo de constata&#231;&#227;o &mdash; <em>be</em> + partic&#237;pio + <em>to be</em>. O rel&#234; &#233; o sujeito; o inspetor sumiu",
     "The relay was found to be out of tolerance during the functional test.",
     '"The relay ', ' out of tolerance during the functional test."'),
    ("had not been issued", "Dica: passivo PERFEITO &mdash; <em>had been</em> + partic&#237;pio. Na data do teste, o documento ainda n&#227;o existia",
     "The calibration certificate had not been issued at the time of the test.",
     '"The calibration certificate ', ' at the time of the test."'),
    ("must be implemented", "Dica: passivo com modal &mdash; modal + <strong>be</strong> + PARTIC&#205;PIO (nunca a forma base)",
     "A corrective action must be implemented before the retest.",
     '"A corrective action ', ' before the retest."'),
    ("have the report resubmitted", "Dica: causativo &mdash; <em>have</em> + OBJETO + partic&#237;pio. O objeto vem ANTES do partic&#237;pio",
     "We need to have the report resubmitted by Friday.",
     '"We need to ', ' by Friday."'),
    ("cannot be granted", "Dica: passivo com modal negativo &mdash; o aceite n&#227;o pode ser concedido por ningu&#233;m enquanto o hold point estiver aberto",
     "Sign-off cannot be granted while the hold point remains open.",
     '"Sign-off ', ' while the hold point remains open."'),
    ("root cause", "Dica: n&#227;o &#233; o sintoma (os 11 ms) &mdash; &#233; a raz&#227;o ATR&#193;S do sintoma",
     "The root cause has not been identified yet, so the corrective action is premature.",
     '"The ', ' has not been identified yet, so the corrective action is premature."'),
]

ORDER = [
    (1, "State the finding in the passive: the relay was found to be out of tolerance during the functional test."),
    (2, "Date what is missing: the calibration certificate had not been issued at the time of the test."),
    (3, "Refuse the word: a deviation is approved before the work, so a failure found after it is a non-conformance."),
    (4, "Put the responsibility back where the contract is, when the supplier blames the subcontractor."),
    (5, "Demand the work with the causative, and give the date: have the report resubmitted by Friday."),
    (6, "Hold the gate: sign-off cannot be granted while the hold point remains open."),
]

SPEECH = [
    ("The relay was found to be out of tolerance during the functional test.",
     "O relé foi constatado fora de tolerância durante o teste funcional."),
    ("The calibration certificate had not been issued at the time of the test.",
     "O certificado de calibração não havia sido emitido na data do teste."),
    ("A corrective action must be implemented before the retest.",
     "Uma ação corretiva precisa ser implementada antes do reteste."),
    ("We need to have the report resubmitted by Friday.",
     "Precisamos que o relatório seja reenviado até sexta-feira."),
    ("Sign-off cannot be granted while the hold point remains open.",
     "O aceite não pode ser concedido enquanto o hold point permanecer aberto."),
]

QUIZZES_SIT = [
    ("The supplier's quality manager opens with \"It is a minor deviation, the unit works.\" You answer:",
     [("\"A deviation is approved before the work. This was found after it, on a safety relay, so I am afraid that is a non-conformance.\"", True),
      ("\"You are wrong and you know it. That relay failed.\"", False),
      ("\"All right, if the unit works, I suppose we can look at it as a deviation.\"", False)]),
    ("She says the certificate was issued the Monday AFTER the test. The strongest reply is:",
     [("\"That is good news, we can close the point then.\"", False),
      ("\"The calibration certificate had not been issued at the time of the test, so it does not cover the test. The unit will have to be retested with a valid certificate in place.\"", True),
      ("\"Please send it to me and I will see what I can do.\"", False)]),
    ("\"The calibration was performed by our subcontractor, not by us.\" You answer:",
     [("\"Then I will take it up with your subcontractor directly.\"", False),
      ("\"That is not my problem, and it is not an excuse.\"", False),
      ("\"To some extent, I understand your position. However, our contract is with you, so the root cause still has to be identified on your side.\"", True)]),
    ("She asks what you need before the unit can be released. You want the work done by THEM, with a date:",
     [("\"We need to have the report resubmitted through the approval workflow by Friday, with the root cause and a corrective action plan.\"", True),
      ("\"We need to have resubmitted the report by Friday.\"", False),
      ("\"I will resubmit the report myself once you send me the data.\"", False)]),
    ("She asks for a provisional sign-off so the shipment is not delayed. You say no without closing the door:",
     [("\"I cannot sign anything, please stop asking me.\"", False),
      ("\"I am afraid sign-off cannot be granted while the hold point remains open. As soon as the retest passes and the certificate is on file, the inspection release can be issued the same day.\"", True),
      ("\"All right, provisionally, but do not tell anyone.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l6\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l6\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l6\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Fun&#231;&#227;o / Function</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Passivo simples<br><em>be</em> + partic&#237;pio</td><td style="padding:.6rem">O objeto vira sujeito e o agente CAI &mdash; porque &#233; &#243;bvio, porque &#233; desconhecido, ou porque nome&#225;-lo comecaria uma briga.</td><td style="padding:.6rem">"The submittal <strong>was returned</strong> with comments."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Passivo de constata&#231;&#227;o<br><em>be</em> + <em>found / reported / believed</em> + <strong>to be</strong></td><td style="padding:.6rem">O registro de todo relat&#243;rio de inspe&#231;&#227;o. Voc&#234; enuncia o FATO, n&#227;o a pessoa. Repare: <em>is believed to have been caused</em> N&#195;O &#233; o mesmo que <em>has been identified</em> &mdash; o fornecedor usa o primeiro justamente para n&#227;o assumir o segundo.</td><td style="padding:.6rem">"The relay <strong>was found to be</strong> out of tolerance."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Passivo perfeito<br><em>had been</em> + partic&#237;pio</td><td style="padding:.6rem">Data a AUS&#202;NCIA: no momento do teste, aquele documento ainda n&#227;o existia. &#201; a frase que impede o fornecedor de resolver o problema emitindo o certificado depois.</td><td style="padding:.6rem">"The certificate <strong>had not been issued</strong> at the time of the test."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Passivo com modal<br>modal + <strong>be</strong> + partic&#237;pio</td><td style="padding:.6rem">A obriga&#231;&#227;o pertence ao PROCEDIMENTO, n&#227;o a voc&#234; &mdash; e por isso ningu&#233;m a leva para o lado pessoal. Depois do modal vem <strong>be</strong>, sempre.</td><td style="padding:.6rem">"A corrective action <strong>must be implemented</strong>." &middot; "Sign-off <strong>cannot be granted</strong>."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Causativo<br><em>have</em> + OBJETO + partic&#237;pio</td><td style="padding:.6rem">Voc&#234; EXIGE a a&#231;&#227;o; outro a EXECUTA. A ordem &#233; fixa: a coisa vem antes do partic&#237;pio. <em>get something done</em> &#233; o mesmo, menos formal.</td><td style="padding:.6rem">"We need to <strong>have the report resubmitted</strong>." &middot; "I will <strong>get the relay retested</strong>."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Causativo com pessoa<br><em>have somebody</em> + FORMA BASE</td><td style="padding:.6rem">Quando voc&#234; PRECISA nomear quem faz. A&#237; o verbo volta &#224; forma base &mdash; sem <em>to</em>, sem partic&#237;pio.</td><td style="padding:.6rem">"I will <strong>have your team resubmit</strong> the report."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">"You calibrated it badly" &#233; uma acusa&#231;&#227;o &mdash; e tudo o que vier depois ser&#225; defesa. "<strong>The relay was found to be out of tolerance</strong>" &#233; o MESMO fato com a pessoa removida: ningu&#233;m &#233; atacado e nada pode ser negado. Depois, o causativo devolve o trabalho a quem pertence: "<strong>we need to have it retested</strong>" &mdash; n&#227;o por n&#243;s, por ELES, e at&#233; sexta.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (dois erros de brasileiro):</strong> (1) esquecer o <em>be</em> ou o partic&#237;pio depois do modal &mdash; "The report must be <em>resubmit</em>" e "A corrective action must <em>implemented</em>" est&#227;o errados; o certo &#233; "must <strong>be resubmitted</strong>" e "must <strong>be implemented</strong>"; (2) a ordem do causativo &mdash; em portugu&#234;s dizemos "preciso reenviar o relat&#243;rio", e sai "We need to have <em>resubmitted the report</em>", que em ingl&#234;s &#233; outro tempo verbal e outro sentido. No causativo o OBJETO vem ANTES: "have <strong>the report</strong> resubmitted".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Colloca&#231;&#245;es da reuni&#227;o de aprova&#231;&#227;o:</strong> <strong>carry out</strong> a test, <strong>issue</strong> a certificate (NUNCA "emit" &mdash; o falso amigo cl&#225;ssico), <strong>trigger</strong> a hold point, <strong>identify</strong> the root cause, <strong>raise</strong> a concern, <strong>grant</strong> sign-off, <strong>resubmit</strong> a report through the approval workflow.</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-6">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 06 -- Pre-class</div>
      <h3>Holding Your Ground -- The Supplier Approval Meeting</h3>
      <div class="lesson-desc">O rel&#234; de seguran&#231;a reprovou no FAT e o fornecedor chama de "minor deviation": como enunciar a falha sem acusar ningu&#233;m, exigir a a&#231;&#227;o corretiva sem fazer o trabalho, e manter o hold point fechado. Key words: deviation, submittal, approval workflow, inspection release, out of tolerance, calibration certificate, traceability, root cause, rework, sign-off, to downplay, to raise a concern, to hold your ground, to pass the buck. Structure: voz passiva avan&#231;ada (was found to be... / had not been issued / must be implemented) + causativo have something done ("We need to have the report resubmitted by Friday").</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 5 voc&#234; nomeou a si mesmo diante de uma banca. Aqui voc&#234; nomeia o DEFEITO &mdash; e quem paga por ele. S&#227;o as palavras da reuni&#227;o de aprova&#231;&#227;o: o que foi encontrado, o que ainda n&#227;o foi emitido, e o que o fornecedor vai tentar chamar de "menor". Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l6">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Advanced Passive &amp; Causative</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como enunciar uma falha sem acusar uma pessoa &mdash; e como exigir o conserto sem fazer o trabalho (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Approval Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma reuni&#227;o de hold point na ordem correta &mdash; da constata&#231;&#227;o at&#233; a recusa do aceite.</p>
      <div class="order-container" id="order-l6">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l6')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem, sustentam e fecham uma reuni&#227;o de aprova&#231;&#227;o. Repare no acento: ele cai no partic&#237;pio (was FOUND to be out of TOLerance) &mdash; e "certificate" termina em <em>-kit</em>, &#225;tono, nunca em <em>-keit</em>.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma reuni&#227;o de FAT &mdash; inclusive quando o fornecedor minimiza a falha ou empurra a culpa para o subcontratado.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: t&#233;cnico, impessoal na constata&#231;&#227;o, firme na exig&#234;ncia.</p>
      <div class="think-card">
        <div class="think-question">You are opening a hold-point meeting with the supplier's quality manager. In ninety seconds: state what was found during the functional test (The relay was found to be...), state what had not been done at the time of the test (The calibration certificate had not been...), refuse the word "deviation" and give the criterion, demand the root cause and the corrective action with a date (We need to have the report resubmitted...), and close by saying why sign-off cannot be granted yet.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-6"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 6</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
