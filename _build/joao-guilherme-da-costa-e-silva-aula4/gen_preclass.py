#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 4 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 4 IN CLASS (mesmo tema/gramática/vocab).
"""
import os
import random

random.seed(4)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Contractual obligation", "something a party is legally required to do under the contract", "obrigação contratual",
     "\"This delay puts our contractual obligations at risk.\""),
    ("Penalty clause", "the part of the contract that sets what a party pays for a delay or a failure", "cláusula de penalidade",
     "\"The penalty clause becomes applicable after thirty days.\""),
    ("Breach of contract", "a failure to do what the contract requires, serious enough to have legal consequences", "quebra de contrato",
     "\"Three consecutive missed milestones may amount to a breach of contract.\""),
    ("Force majeure", "an extraordinary event beyond anyone's control that excuses a party from performing", "força maior",
     "\"They claimed force majeure after the strike at the port.\""),
    ("Liability", "legal responsibility for a cost, a damage or a loss", "responsabilidade legal",
     "\"Liability for the delay remains with the supplier.\""),
    ("Indemnity", "a promise written into the contract to compensate the other party for a specific loss", "indenização contratual",
     "\"The indemnity in Clause 9 covers the cost of the re-test.\""),
    ("Binding agreement", "an agreement that both parties are legally obliged to honor", "acordo vinculante",
     "\"The minutes of the call became a binding agreement.\""),
    ("Dispute resolution", "the formal process the contract defines for settling a disagreement", "resolução de disputas",
     "\"Clause 21 sets out the dispute resolution procedure.\""),
    ("Mediation", "a neutral third party helps both sides reach their own agreement; nothing is imposed", "mediação",
     "\"We proposed mediation before anyone mentioned lawyers.\""),
    ("Arbitration", "a neutral third party hears both sides and imposes a final decision", "arbitragem",
     "\"Arbitration is faster than court, and the decision is final.\""),
    ("To invoke", "to formally put a clause of the contract into effect", "invocar, acionar (uma cláusula)",
     "\"We are prepared to invoke the penalty clause.\""),
    ("To put forward", "to present a proposal or an argument for the other side to consider", "apresentar (uma proposta)",
     "\"Let me put forward a recovery plan.\""),
    ("To bite the bullet", "to accept a difficult decision that you have been avoiding", "encarar o que é difícil mas necessário",
     "\"We had to bite the bullet and re-plan the factory acceptance test.\""),
    ("A double-edged sword", "something with a clear benefit and an equally clear risk", "uma faca de dois gumes",
     "\"Escalation is a double-edged sword: it protects the date, and it costs the relationship.\""),
]

SURVIVAL = [
    ("It would be remiss of us not to flag that this is the third missed milestone.",
     "Seria uma falha nossa não sinalizar que este é o terceiro marco perdido."),
    ("Never has this package been three weeks behind the baseline schedule.",
     "Nunca este pacote esteve três semanas atrás do cronograma de referência."),
    ("Not only did the schedule slip, but no new date has been confirmed in writing.",
     "O cronograma não apenas atrasou, como nenhuma nova data foi confirmada por escrito."),
    ("I'm afraid we're left with no alternative but to invoke the penalty clause.",
     "Receio que não nos reste alternativa senão acionar a cláusula de penalidade."),
    ("We would much rather reach a resolution through mediation than pursue a formal complaint.",
     "Preferimos muito mais chegar a uma resolução por mediação do que abrir uma reclamação formal."),
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


CONTEXT = """<p>The fourth deadline is close, and the file on Jo&#227;o Guilherme's desk is no longer a schedule &mdash; it is a contract. <strong>Never has</strong> a supplier on this package missed three consecutive deadlines. The revised baseline schedule was due on 10 June, and it is still outstanding. <strong>Not only did</strong> the supplier fail to submit it, <strong>but</strong> they <strong>also</strong> declined to confirm a new date in writing. Under Clause 14, that is a failure to meet a <strong>contractual obligation</strong>, and the <strong>penalty clause</strong> becomes applicable after thirty days.</p>
        <p>The supplier blames a strike at the port and has claimed <strong>force majeure</strong>. Legal disagrees: the strike was announced six weeks in advance, so the <strong>liability</strong> for the delay remains with the supplier. <strong>Hardly had</strong> that argument been put forward <strong>when</strong> the supplier also asked for the <strong>indemnity</strong> in Clause 9 to be reviewed. Three missed milestones may amount to a <strong>breach of contract</strong>, but nobody wants to say that word out loud yet.</p>
        <p>So Jo&#227;o writes the email he has been avoiding. He states the position: "<strong>Under no circumstances do</strong> we want to <strong>invoke</strong> the penalty clause &mdash; but if the fourth deadline is missed, I am afraid we are left with no alternative." Then he <strong>puts forward</strong> a recovery plan, proposes <strong>mediation</strong> before anyone mentions <strong>arbitration</strong>, and asks for the minutes of the next call to be treated as a <strong>binding agreement</strong>. Escalation is <strong>a double-edged sword</strong>: it protects the date and it can cost the relationship. This time he decides to <strong>bite the bullet</strong>, and the <strong>dispute resolution</strong> procedure stays in the drawer &mdash; for now."""

QUIZZES_CONTEXT = [
    ("1. \"Never has a supplier on this package missed three consecutive deadlines.\" Por que o verbo vem ANTES do sujeito?",
     [("Porque e&#769; uma pergunta disfar&#231;ada.", False),
      ("Porque depois de uma express&#227;o negativa no in&#237;cio da frase (<em>Never</em>), o ingl&#234;s usa a ordem de PERGUNTA: auxiliar + sujeito + verbo. &#201; a invers&#227;o, e ela d&#225; PESO &#224; frase.", True),
      ("Porque o sujeito &#233; longo demais e vai para o fim.", False)]),
    ("2. \"Not only did they fail to submit the schedule...\" Por que <em>fail</em> e n&#227;o <em>failed</em>?",
     [("Porque depois do auxiliar <em>did</em> o verbo volta &#224; FORMA BASE &mdash; o passado j&#225; est&#225; no <em>did</em>.", True),
      ("Porque a frase fala do presente.", False),
      ("Porque <em>fail</em> &#233; um verbo irregular sem passado.", False)]),
    ("3. Por que \"I'm afraid we're left with no alternative but to invoke the penalty clause\" &#233; mais eficaz do que \"We will fine you\"?",
     [("Porque &#233; mais longa e soa mais formal.", False),
      ("Porque combina firmeza e sa&#237;da: afirma a consequ&#234;ncia contratual sem hostilidade, e deixa a porta aberta &mdash; o fornecedor pode agir sem perder a face.", True),
      ("Porque evita mencionar a penalidade.", False)]),
    ("4. Which sentence is correct?",
     [("\"Under no circumstances we will accept a fourth revision.\"", False),
      ("\"Under no circumstances will we accept a fourth revision.\"", True),
      ("\"Under no circumstances will accept we a fourth revision.\"", False)]),
]

BLANKS = [
    ("Never has", "Dica: express&#227;o negativa no in&#237;cio &rarr; auxiliar ANTES do sujeito (Never + has + sujeito + partic&#237;pio)",
     "Never has this package been three weeks behind the baseline schedule.",
     '"', ' this package been three weeks behind the baseline schedule."'),
    ("Not only did", "Dica: ap&#243;s o gatilho vem o auxiliar <em>did</em> + sujeito + verbo na FORMA BASE",
     "Not only did the schedule slip, but no new date has been confirmed in writing.",
     '"', ' the schedule slip, but no new date has been confirmed in writing."'),
    ("Hardly had", "Dica: dois eventos passados quase simult&#226;neos &mdash; Hardly + had + sujeito + partic&#237;pio ... when ...",
     "Hardly had we begun the factory acceptance test when a non-conformance was identified.",
     '"', ' we begun the factory acceptance test when a non-conformance was identified."'),
    ("will we accept", "Dica: a recusa mais forte do ingl&#234;s profissional &mdash; Under no circumstances + auxiliar + sujeito",
     "Under no circumstances will we accept a fourth revision of the schedule.",
     '"Under no circumstances ', ' a fourth revision of the schedule."'),
    ("invoke", "Dica: o verbo que combina com <em>penalty clause</em> &mdash; acionar formalmente uma cl&#225;usula",
     "I am afraid we are left with no alternative but to invoke the penalty clause.",
     '"I am afraid we are left with no alternative but to ', ' the penalty clause."'),
    ("put forward", "Dica: apresentar uma proposta para o outro lado considerar",
     "Let me put forward a recovery plan before anyone mentions arbitration.",
     '"Let me ', ' a recovery plan before anyone mentions arbitration."'),
]

ORDER = [
    (1, "Open the call and flag the third missed milestone, with one inversion."),
    (2, "State the contractual position: Clause 14, the obligation, and when the penalty clause applies."),
    (3, "Take the force majeure claim apart with the fact: the strike was announced six weeks in advance."),
    (4, "Answer the question about the penalty clause: not now, but yes if the fourth deadline is missed."),
    (5, "Put forward a recovery plan and propose mediation before anyone mentions arbitration."),
    (6, "Close by treating the minutes of the call as a binding agreement."),
]

SPEECH = [
    ("It would be remiss of us not to flag that this is the third missed milestone.",
     "Seria uma falha nossa não sinalizar que este é o terceiro marco perdido."),
    ("Never has this package been three weeks behind the baseline schedule.",
     "Nunca este pacote esteve três semanas atrás do cronograma de referência."),
    ("Not only did the schedule slip, but no new date has been confirmed in writing.",
     "O cronograma não apenas atrasou, como nenhuma nova data foi confirmada por escrito."),
    ("I'm afraid we're left with no alternative but to invoke the penalty clause.",
     "Receio que não nos reste alternativa senão acionar a cláusula de penalidade."),
    ("We would much rather reach a resolution through mediation than pursue a formal complaint.",
     "Preferimos muito mais chegar a uma resolução por mediação do que abrir uma reclamação formal."),
]

QUIZZES_SIT = [
    ("You open the escalation call. It is the third missed milestone on the package. You say:",
     [("\"This is the third time. Do you people ever deliver anything?\"", False),
      ("\"It would be remiss of us not to flag that this is the third missed milestone. Never has this package been three weeks behind the baseline schedule.\"", True),
      ("\"Sorry to bother you again, but could we maybe have an update, if it is not too much trouble?\"", False)]),
    ("The supplier claims force majeure. The strike at the port was announced six weeks in advance. You answer:",
     [("\"One could argue that a strike announced six weeks in advance does not meet the definition of force majeure in Clause 14. On that basis, liability for the delay remains with you.\"", True),
      ("\"That excuse is ridiculous and you know it.\"", False),
      ("\"Ok, if it was a strike, there is nothing we can do.\"", False)]),
    ("She asks you directly: \"Are you going to invoke the penalty clause?\" The best answer is:",
     [("\"Yes. The letter goes out today.\"", False),
      ("\"No, no, of course not. Let's not talk about that.\"", False),
      ("\"Under no circumstances do I want to start there. But if the fourth deadline is missed, I'm afraid we're left with no alternative but to invoke it.\"", True)]),
    ("They missed the date AND sent an incomplete revision. You want both facts in one sentence, with weight:",
     [("\"Not only did they miss the date, but they also sent an incomplete revision.\"", True),
      ("\"Not only they missed the date, but they also sent an incomplete revision.\"", False),
      ("\"They missed the date. Also the revision was incomplete. Also nobody called.\"", False)]),
    ("You want to propose a way out before anyone mentions lawyers. You say:",
     [("\"If this is not fixed by Friday, we will see you in arbitration.\"", False),
      ("\"Let me put forward a recovery plan. We would much rather reach a resolution through mediation than pursue a formal complaint.\"", True),
      ("\"We will decide internally and let you know what we have decided.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Gatilho</th><th style="padding:.7rem;text-align:left">Estrutura / Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>Never</strong> / Never before</td><td style="padding:.6rem">+ auxiliar + sujeito + verbo. A ordem vira ordem de PERGUNTA. Sinaliza que aquilo n&#227;o tem precedente &mdash; e que voc&#234; est&#225; contando.</td><td style="padding:.6rem">"<strong>Never has</strong> this package been three weeks behind the baseline schedule."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><strong>Not only</strong> ... but ... <strong>also</strong></td><td style="padding:.6rem">+ auxiliar + sujeito + verbo na FORMA BASE. Sem outro auxiliar, use <em>did</em>. Empilha duas falhas numa frase s&#243;.</td><td style="padding:.6rem">"<strong>Not only did they miss</strong> the date, but they <strong>also</strong> sent an incomplete revision."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>Hardly / Scarcely</strong> ... when<br><strong>No sooner</strong> ... than</td><td style="padding:.6rem">+ <em>had</em> + sujeito + partic&#237;pio. Dois eventos passados quase simult&#226;neos &mdash; mostra padr&#227;o, n&#227;o acidente.</td><td style="padding:.6rem">"<strong>Hardly had we begun</strong> the FAT <strong>when</strong> the connector failed."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negativa forte<br><strong>Under no circumstances</strong><br>At no time / On no account</td><td style="padding:.6rem">+ auxiliar + sujeito. A recusa mais forte do ingl&#234;s profissional. Use UMA vez &mdash; e para valer.</td><td style="padding:.6rem">"<strong>Under no circumstances will we</strong> accept a fourth revision."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa</td><td style="padding:.6rem">A invers&#227;o J&#193; usa a ordem de pergunta &mdash; por isso ela nunca aparece dentro de uma pergunta de verdade. A pergunta continua normal: <em>Are you going to invoke the penalty clause?</em></td><td style="padding:.6rem">"<strong>Are you going to invoke</strong> the penalty clause?" (sem invers&#227;o)</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Hedging antes da exig&#234;ncia</td><td style="padding:.6rem">A f&#243;rmula que sustenta firmeza sem agress&#227;o: um amortecedor ANTES do fato duro.</td><td style="padding:.6rem">"<strong>It would be remiss of us not to flag that...</strong>" &middot; "<strong>I'm afraid we're left with no alternative but to...</strong>"</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">"They have never missed three deadlines" &#233; um fato. "<strong>Never have they missed</strong> three deadlines" &#233; um fato COM UM CASO ATR&#193;S. A invers&#227;o eleva o registro e diz, em um segundo, que voc&#234; leu o contrato &mdash; e que este e-mail pode ser encaminhado ao diretor dele. Use <strong>uma ou duas vezes</strong> por e-mail. Tr&#234;s vezes soa teatral.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (dois erros de brasileiro):</strong> (1) manter a ordem normal depois do gatilho &mdash; "Never <em>the supplier has</em> missed..." est&#225; errado; o correto &#233; "Never <strong>has the supplier</strong> missed..."; (2) usar o passado depois de <em>did</em> &mdash; "Not only did they <em>failed</em>" est&#225; errado; depois do auxiliar vem a forma base: "Not only did they <strong>fail</strong>".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Colloca&#231;&#245;es do contrato:</strong> <strong>invoke</strong> a penalty clause (nunca "activate"), <strong>claim</strong> force majeure, <strong>put forward</strong> a proposal, <strong>pursue</strong> a formal complaint, <strong>address</strong> contractual obligations, <strong>reach</strong> a resolution, <strong>make</strong> a compelling case."""


HTML = f"""<div class="lesson-card" id="ex-lesson-4">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 04 -- Pre-class</div>
      <h3>Navigating Conflict and Escalation -- Diplomatic Assertiveness in High-Stakes Negotiations</h3>
      <div class="lesson-desc">O quarto prazo perdido: p&#244;r o contrato na mesa sem perder o fornecedor. Key words: contractual obligation, penalty clause, breach of contract, force majeure, liability, indemnity, binding agreement, dispute resolution, mediation, arbitration, to invoke, to put forward, to bite the bullet, a double-edged sword. Structure: inversion for emphasis (Never has... / Not only did... but also... / Hardly had... when... / Under no circumstances will...) + hedging de escalonamento ("It would be remiss of us not to flag that...", "I'm afraid we're left with no alternative but to...").</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 3 voc&#234; nomeou a PAUTA da reuni&#227;o. Aqui voc&#234; nomeia o que acontece quando a reuni&#227;o falha e o atraso vira contrato: o que o contrato obriga, o que ele custa e como a disputa termina. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l4">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Inversion for Emphasis</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como dar PESO a um fato sem levantar a voz &mdash; e como amortecer a exig&#234;ncia formal (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Escalation Call in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma chamada de escalonamento na ordem correta &mdash; da abertura ao acordo vinculante.</p>
      <div class="order-container" id="order-l4">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l4')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem, sustentam e fecham um escalonamento. Repare no acento: ele cai no gatilho da invers&#227;o (NEVER has..., NOT ONLY did...).</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma negocia&#231;&#227;o de conflito &mdash; inclusive quando o fornecedor pergunta, de frente, se voc&#234; vai acionar a penalidade.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: firme no contrato, aberto na rela&#231;&#227;o.</p>
      <div class="think-card">
        <div class="think-question">Open an escalation call with a supplier who has missed a third milestone. Flag it with one inversion (Never has... / Not only did...), state the contractual position (Under Clause 14... the penalty clause becomes applicable after thirty days), answer the force majeure claim with the fact (the strike was announced six weeks in advance), say what happens if the fourth deadline is missed (I'm afraid we're left with no alternative but to...), and close by putting forward a recovery plan and proposing mediation before anyone mentions arbitration.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-4"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 4</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
