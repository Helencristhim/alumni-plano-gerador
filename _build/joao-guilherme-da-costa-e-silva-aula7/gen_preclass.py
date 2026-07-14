#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 7 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 7 IN CLASS (mesmo tema/gramática/vocab — discurso indireto
+ verbos de relato na revisão trimestral de prazo).
"""
import os
import random

random.seed(7)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Schedule slippage", "time lost against the plan, a few days at a time, until the date is gone", "derrapagem de prazo",
     "\"The schedule slippage on the installation package is now six weeks.\""),
    ("Variance", "the measured difference between the plan and reality -- the number in the report", "varia&#231;&#227;o (medida, plano x real)",
     "\"The schedule variance is minus thirty working days against the plan.\""),
    ("Critical path", "the chain of activities that decides the end date: delay any of them and the project moves", "caminho cr&#237;tico",
     "\"Signal installation is on the critical path, so this delay is not absorbable.\""),
    ("Float", "the spare time an activity has before it starts delaying the whole project", "folga (de cronograma)",
     "\"That activity had ten days of float. The supplier has used all of it.\""),
    ("Recovery schedule", "the revised plan that shows exactly how the lost time will be won back", "cronograma de recupera&#231;&#227;o",
     "\"A recovery schedule is required within ten days, not another apology.\""),
    ("Contingency plan", "what you do if the recovery fails -- the plan you hope not to use", "plano de conting&#234;ncia",
     "\"Our contingency plan is to commission the line in two stages instead of one.\""),
    ("Risk mitigation", "action taken now to make a risk smaller, before it becomes a delay", "mitiga&#231;&#227;o de risco",
     "\"Dual sourcing the cable was risk mitigation, and it is why we are only six weeks late.\""),
    ("Post-mortem review", "a session held after the fact, to find out why it happened and never repeat it", "revis&#227;o pos-projeto (li&#231;&#245;es aprendidas)",
     "\"We will hold a post-mortem review once the line is commissioned, not now.\""),
    ("Steering committee", "the senior group that decides what the project team is not allowed to decide alone", "comit&#234; diretor / comit&#234; gestor",
     "\"If we cannot agree a date today, this goes to the steering committee in April.\""),
    ("Buy-in", "real agreement from the people who could block you -- not just their signature", "ades&#227;o, apoio real",
     "\"I have the approval. What I do not have yet is buy-in from the operations team.\""),
    ("To make headway", "to make real progress against something that is pushing back", "avan&#231;ar, progredir (contra resist&#234;ncia)",
     "\"We are finally making headway on the interface drawings.\""),
    ("To reach a consensus", "to arrive at a position that everybody in the room can live with", "chegar a um consenso",
     "\"We reached a consensus on the sequence, not on the date.\""),
    ("To take a stance", "to state a position publicly, and then stand behind it when it is challenged", "assumir uma posi&#231;&#227;o publicamente",
     "\"Motiva has taken a stance on the delay: no payment against an unapproved schedule.\""),
    ("To bring about", "to cause something to happen, usually after effort and resistance", "provocar, ocasionar (um resultado)",
     "\"It took two escalations to bring about a resolution.\""),
]

SURVIVAL = [
    ("The schedule variance is minus thirty working days, and the activity is on the critical path.",
     "A variação de prazo é de menos trinta dias úteis, e a atividade está no caminho crítico."),
    ("On 3 June you assured us that the relay would ship on the fifteenth.",
     "Em 3 de junho vocês nos garantiram que o relé seria despachado no dia quinze."),
    ("Your company undertook to submit a recovery schedule within ten days.",
     "A empresa de vocês se comprometeu a apresentar um cronograma de recuperação em dez dias."),
    ("To some extent, both parties share responsibility. The float, however, belongs to the project.",
     "Até certo ponto, as duas partes dividem a responsabilidade. A folga, porém, é do projeto."),
    ("If we can reach a consensus today, this does not have to go to the steering committee.",
     "Se chegarmos a um consenso hoje, isto não precisa subir para o comitê diretor."),
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


CONTEXT = """<p>The quarterly review opens at ten, and Elena Vargas opens it with the good news: her team is working weekends and they are finally <strong>making headway</strong> on site. Jo&#227;o Guilherme lets her finish, and then he puts the number on the table. The <strong>schedule variance</strong> on the signaling installation is minus thirty working days. The activity sits on the <strong>critical path</strong>, so the <strong>float</strong> is zero and nothing absorbs it. Six weeks of <strong>schedule slippage</strong>, and the passenger waits six weeks longer.</p>
        <p>Elena has been preparing her version for a month. The interface drawings arrived late from Motiva, she says, and her team could not start. She is partly right, and Jo&#227;o says so: to some extent, both parties share responsibility, and the drawings were issued eight days late. Then she goes further. <em>I never promised you the fifteenth</em>, she says. <em>I said we would do our best.</em> And this is the moment the meeting is won or lost &mdash; not by raising the voice, but by reading the record. <strong>On 3 June you assured us that</strong> the relay <strong>would ship</strong> on the fifteenth, and the minutes were circulated to you that same afternoon. In the last review your team <strong>told us that</strong> the installation <strong>was</strong> on track. Your planner <strong>claimed that</strong> the cable <strong>had already been dispatched</strong>; the carrier's records show it left the warehouse eleven days later. And on 12 June your company <strong>undertook to submit</strong> a <strong>recovery schedule</strong> within ten days. Twenty-two days have passed, and nothing has been received.</p>
        <p>Elena stops. <em>That is fair</em>, she <strong>acknowledges</strong>. <em>The schedule was not sent, and I should have called you.</em> Nobody was accused, nothing was denied, and the argument about memory is over &mdash; because a dated record cannot be argued with, only explained. So she asks what he needs. He asks for three things: a <strong>recovery schedule</strong> by Friday, a <strong>contingency plan</strong> if the retest fails, and a weekly call, so that the next slip reaches him in three days and not in three weeks. She asks for one thing back: two weeks of <strong>float</strong> from the testing activity. He refuses. The float belongs to the project. And if they can <strong>reach a consensus</strong> today, none of this has to go to the <strong>steering committee</strong> in April."""

QUIZZES_CONTEXT = [
    ("1. \"On 3 June you <em>assured us that</em> the relay <em>would</em> ship.\" Por que o verbo recua de <em>will</em> para <em>would</em>?",
     [("Porque <em>would</em> &#233; mais educado do que <em>will</em>.", False),
      ("Porque o recuo marca que a frase &#233; uma CITA&#199;&#195;O do que ELA disse, e n&#227;o uma promessa que JO&#195;O est&#225; fazendo agora. Sem o recuo (\"you assured us the relay <em>will</em> ship\"), a frase deixa de ser o registro dela e vira o compromisso dele.", True),
      ("Porque em ingl&#234;s t&#233;cnico &#233; proibido usar <em>will</em>.", False)]),
    ("2. Elena diz \"I never promised you the fifteenth\". O que ENCERRA a discuss&#227;o?",
     [("Levantar o tom e repetir que ela prometeu.", False),
      ("O REGISTRO: a data (3 de junho), o verbo de relato (<em>assured us</em>) e a ata circulada na mesma tarde. Contra um registro datado n&#227;o se discute &mdash; s&#243; se explica.", True),
      ("Chamar o comit&#234; diretor imediatamente.", False)]),
    ("3. \"Your planner <em>claimed that</em> the cable <em>had already been dispatched</em>.\" O que o verbo CLAIMED comunica que SAID n&#227;o comunicaria?",
     [("Que Jo&#227;o DUVIDA da afirma&#231;&#227;o &mdash; <em>claim</em> marca que o que foi dito n&#227;o se confirmou. <em>Said</em> seria neutro; <em>claimed</em> j&#225; abre a checagem.", True),
      ("Que o planejador gritou.", False),
      ("Que a afirma&#231;&#227;o era oficial e est&#225; comprovada.", False)]),
    ("4. Which sentence is correct?",
     [("\"Your company assured us to submit a recovery schedule within ten days.\"", False),
      ("\"Your company undertook to submit a recovery schedule within ten days.\"", True),
      ("\"Your company said us that it would submit a recovery schedule within ten days.\"", False)]),
]

BLANKS = [
    ("assured us that", "Dica: verbo de relato de COMPROMISSO &mdash; e depois dele vem <em>that</em> + ora&#231;&#227;o, com o verbo recuado",
     "On 3 June you assured us that the relay would ship on the fifteenth.",
     '"On 3 June you ', ' the relay would ship on the fifteenth."'),
    ("told us that", "Dica: TELL exige a pessoa (told US). SAY nunca leva pessoa direta &mdash; \"said us\" n&#227;o existe",
     "In the last review your team told us that the installation was on track.",
     '"In the last review your team ', ' the installation was on track."'),
    ("had already been dispatched", "Dica: recuo do <em>present perfect</em> (<em>has been</em>) para o <em>past perfect</em>: <em>had been</em> + partic&#237;pio",
     "Your planner claimed that the cable had already been dispatched.",
     '"Your planner claimed that the cable ', '."'),
    ("undertook to submit", "Dica: obriga&#231;&#227;o formal &mdash; e este &#233; o verbo de relato que pede INFINITIVO (<em>to</em> + verbo), n&#227;o <em>that</em>",
     "Your company undertook to submit a recovery schedule within ten days.",
     '"Your company ', ' a recovery schedule within ten days."'),
    ("critical path", "Dica: a cadeia de atividades que determina a data final &mdash; nela a folga &#233; zero",
     "The activity is on the critical path, so there is no float to absorb the delay.",
     '"The activity is on the ', ', so there is no float to absorb the delay."'),
    ("reach a consensus", "Dica: chegar a uma posi&#231;&#227;o que todos na sala aceitam &mdash; o verbo &#233; <em>reach</em>, nunca <em>arrive at</em>",
     "If we can reach a consensus today, this does not have to go to the steering committee.",
     '"If we can ', ' today, this does not have to go to the steering committee."'),
]

ORDER = [
    (1, "Open with the number: the schedule variance is minus thirty working days."),
    (2, "Say why nothing absorbs it: the activity is on the critical path and the float is zero."),
    (3, "Concede what is true: to some extent, both parties share responsibility for the late drawings."),
    (4, "Put the promise on the record with the date: on 3 June you assured us that the relay would ship."),
    (5, "Name the obligation that was never met: your company undertook to submit a recovery schedule."),
    (6, "Close with the demand and the consequence: a recovery schedule by Friday, or the steering committee in April."),
]

SPEECH = [
    ("The schedule variance is minus thirty working days, and the activity is on the critical path.",
     "A variação de prazo é de menos trinta dias úteis, e a atividade está no caminho crítico."),
    ("On 3 June you assured us that the relay would ship on the fifteenth.",
     "Em 3 de junho vocês nos garantiram que o relé seria despachado no dia quinze."),
    ("Your planner claimed that the cable had already been dispatched.",
     "O planejador de vocês alegou que o cabo já havia sido despachado."),
    ("Your company undertook to submit a recovery schedule within ten days.",
     "A empresa de vocês se comprometeu a apresentar um cronograma de recuperação em dez dias."),
    ("To some extent, both parties share responsibility. The float, however, belongs to the project.",
     "Até certo ponto, as duas partes dividem a responsabilidade. A folga, porém, é do projeto."),
]

QUIZZES_SIT = [
    ("Elena abre a reuni&#227;o com a boa not&#237;cia (\"the team is working weekends\"). Voc&#234; responde:",
     [("\"Thank you, Elena. Let me start with the number, and then I would like to hear you. The schedule variance on the installation is minus thirty working days, and the activity is on the critical path.\"", True),
      ("\"Weekends are the minimum I expect at this point.\"", False),
      ("\"That is good to hear. So, how are things going in general?\"", False)]),
    ("\"I never promised you the fifteenth. I said we would do our best.\" A resposta mais forte &#233;:",
     [("\"You did promise it, and everybody in that call heard you.\"", False),
      ("\"That is why I am reading from the minutes. On 3 June you assured us that the relay would ship on the fifteenth, and the minutes were circulated to you the same afternoon.\"", True),
      ("\"All right, perhaps I misunderstood you. Let us move on.\"", False)]),
    ("\"The interface drawings arrived late from your side.\" Ela est&#225; PARCIALMENTE certa. Voc&#234; responde:",
     [("\"That has nothing to do with the delay we are discussing.\"", False),
      ("\"You are right, and I accept that the delay is shared.\"", False),
      ("\"To some extent, both parties share responsibility, and the drawings were issued eight days late. The slippage we are discussing, however, is thirty days.\"", True)]),
    ("\"Give us two weeks of float from the testing activity and we recover everything.\" Voc&#234; recusa:",
     [("\"I am afraid the float belongs to the project, not to the package that is late. If I hand it over now, I have nothing left when something unplanned happens.\"", True),
      ("\"Fine, take the two weeks, but this is the last time.\"", False),
      ("\"I do not have the authority to discuss float with you.\"", False)]),
    ("Ela pede que a reuni&#227;o n&#227;o seja escalada. Voc&#234; diz sim NOS SEUS TERMOS:",
     [("\"I cannot promise anything, it is out of my hands.\"", False),
      ("\"If we can reach a consensus today &mdash; a recovery schedule by Friday and a contingency plan &mdash; this does not have to go to the steering committee in April.\"", True),
      ("\"Do not worry, I will keep this between us whatever happens.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l7\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l7\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l7\')">&#9660;</button></span></div>')
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
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Eles disseram / They said</th><th style="padding:.7rem;text-align:left">Fun&#231;&#227;o / Function</th><th style="padding:.7rem;text-align:left">Voc&#234; relata / You report</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>will</em> &rarr; <strong>would</strong></td><td style="padding:.6rem">A promessa recua um passo no tempo &mdash; e passa a ser um REGISTRO do que eles prometeram, n&#227;o uma promessa sua.</td><td style="padding:.6rem">"You assured us that the relay <strong>would</strong> ship on the fifteenth."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>is / are</em> &rarr; <strong>was / were</strong></td><td style="padding:.6rem">O presente deles vira passado seu: era verdade para eles, naquele momento.</td><td style="padding:.6rem">"Your team told us that the installation <strong>was</strong> on track."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>has been</em> &rarr; <strong>had been</strong></td><td style="padding:.6rem">O perfeito vira mais-que-perfeito. &#201; a linha que DATA uma alega&#231;&#227;o &mdash; e datar &#233; o que permite checar.</td><td style="padding:.6rem">"Your planner claimed that the cable <strong>had been</strong> dispatched."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600"><em>can</em> &rarr; <strong>could</strong> &middot; <em>must</em> &rarr; <strong>had to</strong></td><td style="padding:.6rem">Os modais tamb&#233;m recuam. <em>Must</em> &#233; a exce&#231;&#227;o: vira <em>had to</em>.</td><td style="padding:.6rem">"They said they <strong>could</strong> recover two weeks, and that we <strong>had to</strong> wait."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><em>say</em> x <strong>tell</strong></td><td style="padding:.6rem"><strong>TELL</strong> exige a pessoa (<em>told us / told me</em>). <strong>SAY</strong> N&#195;O aceita pessoa direta: &#233; <em>said that</em> ou <em>said TO me</em>. "He said me" simplesmente n&#227;o existe.</td><td style="padding:.6rem">"He <strong>told us</strong> that..." &middot; "He <strong>said</strong> that..."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">O verbo escolhe o PESO</td><td style="padding:.6rem"><strong>said</strong> (neutro) &middot; <strong>claimed</strong> (voc&#234; duvida) &middot; <strong>assured us</strong> (comprometeram-se, com confian&#231;a) &middot; <strong>acknowledged / conceded</strong> (admitiram contra o pr&#243;prio interesse) &middot; <strong>denied</strong> (negaram) &middot; <strong>undertook / committed to</strong> (obriga&#231;&#227;o formal).</td><td style="padding:.6rem">"They <strong>assured</strong> us" prende. "They <strong>said</strong>" n&#227;o prende.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">"You are always late" &#233; uma acusa&#231;&#227;o &mdash; e uma acusa&#231;&#227;o se nega, se defende e se discute por tr&#234;s semanas. "<strong>On 3 June you assured us that the relay would ship on the fifteenth</strong>" &#233; o MESMO fato virado REGISTRO: tem data, tem verbo de relato, tem recuo. Contra um registro n&#227;o se discute &mdash; s&#243; se explica. E quem explica, negocia.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (tr&#234;s erros de brasileiro):</strong> (1) <em>"He said me that..."</em> &mdash; em portugu&#234;s dizemos "ele ME disse", mas SAY nunca leva a pessoa: &#233; <strong>told me</strong> (ou <em>said to me</em>); (2) N&#195;O recuar o verbo &mdash; em portugu&#234;s o recuo &#233; opcional ("ele disse que o rel&#234; SAI dia 15"), mas em ingl&#234;s "he said the relay <em>will</em> ship" deixa de citar o outro e vira uma promessa SUA; (3) <em>"They assured us TO send the schedule"</em> &mdash; <strong>assure</strong> pede <em>that</em> + ora&#231;&#227;o; quem pede infinitivo &#233; <strong>undertake / commit / promise</strong>: "they <strong>undertook to send</strong> the schedule".</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Colloca&#231;&#245;es da revis&#227;o de prazo:</strong> <strong>compress</strong> the schedule (nunca "reduce"), <strong>secure</strong> buy-in, <strong>reach</strong> a consensus (nunca "arrive at"), <strong>mitigate</strong> a risk, <strong>make</strong> headway (NUNCA "have progress"), <strong>absorb</strong> a delay, <strong>take</strong> a stance, <strong>bring about</strong> a resolution.</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Hedging (para conceder sem ceder):</strong> "<em>To some extent, both parties share responsibility for...</em>" &middot; "<em>One could argue that the delay was partly caused by...</em>" &middot; "<em>That is fair, and I will record it. It does not change what is on the critical path.</em>"</p>"""


HTML = f"""<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 07 -- Pre-class</div>
      <h3>Never Back Down -- The Quarterly Project Review</h3>
      <div class="lesson-desc">Seis semanas de atraso na instala&#231;&#227;o e uma fornecedora que lembra a promessa de outro jeito: como abrir a reuni&#227;o pelo N&#218;MERO, como transformar mem&#243;ria em REGISTRO (data + verbo de relato + recuo), e como conceder o que &#233; verdade sem entregar a folga do projeto. Key words: schedule slippage, variance, critical path, float, recovery schedule, contingency plan, risk mitigation, post-mortem review, steering committee, buy-in, to make headway, to reach a consensus, to take a stance, to bring about. Structure: discurso indireto e verbos de relato (On 3 June you <em>assured us that</em> the relay <em>would</em> ship... / your company <em>undertook to submit</em>...).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Na aula 6 voc&#234; nomeou o defeito. Aqui voc&#234; nomeia o ATRASO &mdash; e quem paga por ele. S&#227;o as palavras que separam "estamos atrasados" de um cronograma que se defende numa sala: a varia&#231;&#227;o, o caminho cr&#237;tico, a folga que n&#227;o existe. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l7">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reported Speech &amp; Reporting Verbs</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como transformar o que o outro disse em registro &mdash; e por que o verbo que voc&#234; escolhe decide o quanto ele prende (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Review Meeting in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque os passos de uma revis&#227;o trimestral de prazo na ordem correta &mdash; do n&#250;mero at&#233; a consequ&#234;ncia.</p>
      <div class="order-container" id="order-l7">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem, sustentam e fecham uma revis&#227;o de prazo. Repare no acento: "VA-ri-ance" (na primeira s&#237;laba, n&#227;o "va-ri-AN-ce") e "com-MIT-tee" com o -ee curto. E diga SKED-jool, n&#227;o SHED-jool.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da revis&#227;o trimestral &mdash; inclusive quando a fornecedora nega a promessa ou pede a folga do seu projeto.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: preciso no n&#250;mero, imparcial na concess&#227;o, firme no registro.</p>
      <div class="think-card">
        <div class="think-question">You are chairing the quarterly review with a supplier who is six weeks behind. In ninety seconds: open with the variance and say why the float does not absorb it, concede the part that is genuinely yours (the drawings were eight days late), put two commitments on the record with their dates (On 3 June you assured us that... / On 12 June your company undertook to...), refuse to hand over the float from the testing activity, and close by saying what you need by Friday and what happens if it does not arrive.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-7"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 7</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
