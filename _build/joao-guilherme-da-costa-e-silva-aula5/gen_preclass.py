#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 5 do João Guilherme (REGRA 4: 5 etapas obrigatórias).
Matching com opções EMBARALHADAS por linha (REGRA 24). Acentos viram entidades HTML.
REGRA 29: previewa a aula 5 IN CLASS (mesmo tema/gramática/vocab — cleft sentences).
"""
import os
import random

random.seed(5)

HERE = os.path.dirname(os.path.abspath(__file__))

VOCAB = [
    ("Track record", "a documented history of results you can point to, with dates and numbers", "histórico comprovado",
     "\"I can demonstrate a track record of delivering signaling packages on time.\""),
    ("Cross-functional", "involving people from different departments and disciplines at the same time", "multidisciplinar, entre áreas",
     "\"I lead cross-functional teams: signaling, civil works and the client.\""),
    ("High-stakes", "where the consequences of getting it wrong are serious and public", "de alto risco, com muito em jogo",
     "\"Signaling is a high-stakes discipline: the failure mode is a collision.\""),
    ("Resilience", "the ability to keep performing when the pressure does not stop", "resiliência",
     "\"What that year taught me was resilience, not patience.\""),
    ("Stakeholder management", "keeping everyone with an interest in the project informed, aligned and calm", "gestão de partes interessadas",
     "\"Stakeholder management is half the job: the client, the supplier and the regulator.\""),
    ("Value proposition", "the one concrete reason to choose you instead of the other candidate", "proposta de valor",
     "\"My value proposition is simple: I read the standard and I run the site.\""),
    ("Technical lead", "the engineer who owns the technical decisions on a project, and answers for them", "líder técnico",
     "\"I was the technical lead on the Line 5 signaling package.\""),
    ("Subject matter expert", "the person the team goes to when the answer is not in the manual", "especialista no assunto",
     "\"On interlocking logic, I am the subject matter expert for my team.\""),
    ("Performance-driven", "working against a number: a metric, a KPI, a measurable target", "orientado por desempenho",
     "\"It is a performance-driven environment: every milestone has an indicator.\""),
    ("Results-oriented", "asking to be judged by what you delivered, not by how busy you looked", "orientado a resultados",
     "\"I am results-oriented: judge me by the commissioning date, not by my hours.\""),
    ("To set out", "to explain your background clearly and in order, so the listener can follow it", "expor, apresentar em ordem",
     "\"Let me set out my experience in three steps.\""),
    ("To account for", "to explain a decision or a period that somebody is entitled to ask about", "justificar, explicar",
     "\"I can account for the two years when I stopped using English.\""),
    ("To burn the midnight oil", "to work late into the night to finish something that matters (informal)", "virar a noite trabalhando",
     "\"We burned the midnight oil for a week before the factory acceptance test.\""),
    ("To throw in the towel", "to give up when it gets hard -- the thing you say you did NOT do (informal)", "jogar a toalha, desistir",
     "\"That interview went badly, but I did not throw in the towel.\""),
]

SURVIVAL = [
    ("Let me set out my background in three steps.",
     "Deixe-me expor a minha trajetória em três etapas."),
    ("What I bring to this role is seven years of managing international suppliers.",
     "O que eu trago para esta posição são sete anos gerenciando fornecedores internacionais."),
    ("What sets me apart is that I read the standard and I run the site.",
     "O que me diferencia é que eu leio a norma e eu conduzo o campo."),
    ("One example that comes to mind is a supplier who missed three consecutive deadlines.",
     "Um exemplo que me vem à mente é um fornecedor que perdeu três prazos consecutivos."),
    ("I can account for it, and what I learned was that fluency is a habit, not a memory.",
     "Eu consigo explicar isso, e o que eu aprendi foi que fluência é um hábito, não uma lembrança."),
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


CONTEXT = """<p>It is four o'clock on a Tuesday and Jo&#227;o Guilherme is sitting in front of a panel of two. Sofie Claes, Head of Signaling Engineering, has twenty minutes and a shortlist of five engineers, all of them with seven years of experience. Experience is time, and everybody on that list has it. <strong>What wins the room is</strong> a <strong>track record</strong>: a project, a decision, an outcome.</p>
        <p>He opens carefully. "Let me <strong>set out</strong> my background in three steps. <strong>What I do</strong> at Motiva <strong>is</strong> own the signaling design for metro line extensions, from the specification to commissioning. <strong>What I bring to this role is</strong> seven years of managing German, French and Chinese suppliers under contractual pressure." Sofie is not impressed yet. She asks the question that decides everything: what makes him the right person, and not the other four? "<strong>What sets me apart is</strong> that I read the standard and I run the site. Most engineers do one or the other. <strong>It was in San Francisco, in 2023, that</strong> I did both on the same project." That is a <strong>value proposition</strong>, and it takes one sentence.</p>
        <p>Then comes the uncomfortable question, the one he did not prepare in March: there was a period when he was not using English. He does not apologize. He <strong>accounts for</strong> it. "<strong>What I learned from that experience was</strong> that fluency is a habit, not a memory. <strong>It was an interview, in March, that</strong> made me rebuild the habit." He did not <strong>throw in the towel</strong>, and the word for that, in an interview, is <strong>resilience</strong>. <strong>Stakeholder management</strong>, a <strong>cross-functional</strong> team, a <strong>high-stakes</strong> discipline where the failure mode is a collision: the engineering was always there. Tonight, so was the English."""

QUIZZES_CONTEXT = [
    ("1. \"What I bring to this role is seven years in signaling.\" Por que o verbo &#233; <em>is</em>, e n&#227;o <em>are</em>, se \"seven years\" &#233; plural?",
     [("Porque <em>What...</em> funciona como \"the thing that\" &mdash; um sujeito SINGULAR. O verbo concorda com ele, nunca com o complemento.", True),
      ("Porque o ingl&#234;s ignora concord&#226;ncia depois de <em>what</em>.", False),
      ("Porque \"seven years\" &#233; tratado como dinheiro e vira singular.", False)]),
    ("2. \"It was in San Francisco that I ran my first commissioning cycle.\" O que essa estrutura FAZ com a frase?",
     [("Adiciona uma informa&#231;&#227;o nova sobre S&#227;o Francisco.", False),
      ("Coloca UM fato sob o holofote &mdash; o lugar &mdash; e diz &#224; banca onde olhar. A informa&#231;&#227;o &#233; a mesma; o peso, n&#227;o.", True),
      ("Torna a frase mais formal, mas o efeito &#233; apenas decorativo.", False)]),
    ("3. Por que \"What I bring to this role is seven years...\" funciona melhor numa entrevista do que \"I have seven years of experience\"?",
     [("Porque &#233; mais longa, e frases longas soam mais profissionais.", False),
      ("Porque anuncia que algo importante vem, guarda a informa&#231;&#227;o decisiva para o FIM &mdash; e ainda compra meio segundo de tempo para voc&#234; pensar.", True),
      ("Porque evita o verbo <em>have</em>, que &#233; informal demais.", False)]),
    ("4. Which sentence is correct?",
     [("\"It was in San Francisco where I ran my first commissioning cycle.\"", False),
      ("\"What I bring to this role, it is deep expertise in signaling.\"", False),
      ("\"It was in San Francisco that I ran my first commissioning cycle.\"", True)]),
]

BLANKS = [
    ("What I bring to this role is", "Dica: wh-cleft &mdash; anuncie primeiro, entregue depois. O verbo &#233; <em>is</em>, no singular",
     "What I bring to this role is seven years in railway signaling.",
     '"', ' seven years in railway signaling."'),
    ("It was in San Francisco that", "Dica: it-cleft &mdash; o holofote cai no LUGAR. E a palavra &#233; <em>that</em>, nunca <em>where</em>",
     "It was in San Francisco that I ran my first full commissioning cycle.",
     '"', ' I ran my first full commissioning cycle."'),
    ("What sets me apart is", "Dica: a sua proposta de valor em uma linha s&#243;",
     "What sets me apart is that I read the standard and I run the site.",
     '"', ' that I read the standard and I run the site."'),
    ("account for", "Dica: explicar um per&#237;odo ou uma decis&#227;o &mdash; e a preposi&#231;&#227;o &#233; FOR",
     "I can account for the two years when I stopped using English.",
     '"I can ', ' the two years when I stopped using English."'),
    ("set out", "Dica: expor a sua trajet&#243;ria de forma clara e em ordem",
     "Let me set out my background in three steps.",
     '"Let me ', ' my background in three steps."'),
    ("track record", "Dica: n&#227;o &#233; tempo de experi&#234;ncia &mdash; &#233; a evid&#234;ncia: projeto, decis&#227;o, resultado",
     "I can demonstrate a track record of delivering signaling packages on time.",
     '"I can demonstrate a ', ' of delivering signaling packages on time."'),
]

ORDER = [
    (1, "Set out your background in three steps, starting from the value and not from the biography."),
    (2, "State your value proposition in one cleft sentence: what sets you apart from the other candidates."),
    (3, "Prove it with a track record: one project, the decision you took, and the outcome."),
    (4, "Account for the uncomfortable question with evidence, not with an apology."),
    (5, "Close by asking the panel a question only an engineer would ask."),
]

SPEECH = [
    ("Let me set out my background in three steps.",
     "Deixe-me expor a minha trajetória em três etapas."),
    ("What I bring to this role is seven years of managing international suppliers.",
     "O que eu trago para esta posição são sete anos gerenciando fornecedores internacionais."),
    ("What sets me apart is that I read the standard and I run the site.",
     "O que me diferencia é que eu leio a norma e eu conduzo o campo."),
    ("It was in San Francisco, in 2023, that I ran my first full commissioning cycle.",
     "Foi em São Francisco, em 2023, que eu conduzi o meu primeiro ciclo completo de comissionamento."),
    ("I can account for it, and what I learned was that fluency is a habit, not a memory.",
     "Eu consigo explicar isso, e o que eu aprendi foi que fluência é um hábito, não uma lembrança."),
]

QUIZZES_SIT = [
    ("The panel opens with \"Tell me about yourself.\" You have ninety seconds. You start with:",
     [("\"I was born in S&#227;o Paulo and I studied electrical engineering...\"", False),
      ("\"Let me set out my background in three steps. What I do at Motiva is own the signaling design for metro line extensions.\"", True),
      ("\"Well, it is difficult to summarize seven years, but I will try.\"", False)]),
    ("\"Everyone on this shortlist has seven years. What makes you the right person?\" You answer:",
     [("\"What sets me apart is that I read the standard and I run the site. Most engineers do one or the other.\"", True),
      ("\"I am very dedicated and I always give my best.\"", False),
      ("\"I think my experience speaks for itself.\"", False)]),
    ("She asks for a conflict with an international supplier. The strongest opening is:",
     [("\"Suppliers are always late, it happens on every project.\"", False),
      ("\"One example that comes to mind is a supplier who missed three consecutive deadlines. What I did was put forward a recovery plan before anyone mentioned the penalty clause.\"", True),
      ("\"I would have to think about that one for a moment.\"", False)]),
    ("\"You were not using English intensively for a while. How do I know that will not be a problem?\" You answer:",
     [("\"I am sorry about my English, I know it is not perfect.\"", False),
      ("\"My English is fine, it was only a bad day in that interview.\"", False),
      ("\"I can account for it. What I learned from that period was that fluency is a habit, not a memory &mdash; and I have been in weekly training since March.\"", True)]),
    ("The technical director asks how you handle competing priorities. He wants ONE sentence, not three minutes. You say:",
     [("\"The way I approach this kind of challenge is to ask which item is on the critical path for safety approval.\"", True),
      ("\"It depends. Let me explain the relay logic first, and then the interlocking table, and then...\"", False),
      ("\"I work hard and I burn the midnight oil until everything is done.\"", False)]),
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
            f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l5\')">'
            f'<span class="order-num">?</span><span class="order-text">{esc(text)}</span>'
            f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l5\')">&#9650;</button>'
            f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l5\')">&#9660;</button></span></div>')
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
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">wh-cleft<br><strong>What</strong> + sujeito + verbo + <strong>is</strong> + o ponto</td><td style="padding:.6rem">Voc&#234; ANUNCIA que algo importante vem, e s&#243; ent&#227;o entrega. A banca se inclina para a frente. Em portugu&#234;s: "O que eu trago para este cargo &#233;...".</td><td style="padding:.6rem">"<strong>What I bring to this role is</strong> seven years in signaling."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">it-cleft<br><strong>It was</strong> + o fato + <strong>that</strong> + o resto</td><td style="padding:.6rem">Voc&#234; coloca UM fato sob o holofote: um lugar, uma data, uma pessoa, uma decis&#227;o. A palavra &#233; sempre <strong>that</strong> &mdash; nunca <em>where</em>, nunca <em>when</em>.</td><td style="padding:.6rem">"<strong>It was in San Francisco that</strong> I ran my first commissioning cycle."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600"><strong>The reason</strong> + ora&#231;&#227;o + <strong>is that</strong></td><td style="padding:.6rem">Voc&#234; assume o controle da hist&#243;ria por tr&#225;s de uma decis&#227;o, antes que algu&#233;m a interprete mal.</td><td style="padding:.6rem">"<strong>The reason I moved into signaling is that</strong> safety is non-negotiable."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Concord&#226;ncia</td><td style="padding:.6rem">Depois de <em>What...</em>, o verbo &#233; SEMPRE <strong>is</strong> / <strong>was</strong>, mesmo diante de um plural &mdash; porque <em>What</em> equivale a "the thing that", um sujeito singular.</td><td style="padding:.6rem">"What I bring <strong>is</strong> seven years." (nunca <em>are</em>)</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Interrogativa / negativa</td><td style="padding:.6rem">Funciona igual: <strong>What</strong> he wants <strong>is</strong> a date. / <strong>What I do not do is</strong> promise dates I cannot defend.</td><td style="padding:.6rem">"<strong>What I do not do is</strong> promise a date I cannot defend."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Na fala</td><td style="padding:.6rem">A pausa cai logo ANTES do <em>is</em>. Essa pausa &#233; tempo de pensar &mdash; e voc&#234; tem direito a ela.</td><td style="padding:.6rem">"What I learned from that experience &#8230; <strong>was</strong> that fluency is a habit."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Para que serve</td><td style="padding:.6rem" colspan="2">Sob press&#227;o, o candidato nervoso despeja tudo o que sabe numa frase longa &mdash; e a banca para de ouvir. A cleft sentence faz o contr&#225;rio: ela diz &#224; banca <strong>onde olhar</strong>. Mesma informa&#231;&#227;o, candidato completamente diferente.</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Aten&#231;&#227;o (dois erros de brasileiro):</strong> (1) o pronome repetido &mdash; em portugu&#234;s dizemos "O que eu trago para esse cargo, <em>isso &#233;</em>..."; em ingl&#234;s o pronome N&#195;O volta: "What I bring to this role <em>it is</em>..." est&#225; errado, o correto &#233; "What I bring to this role <strong>is</strong>..."; (2) o <em>where</em> &mdash; dizemos "foi em S&#227;o Francisco ONDE...", mas o it-cleft ingl&#234;s exige <strong>that</strong>: "It was in San Francisco <strong>that</strong> I ran my first commissioning cycle."</p>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem"><strong>Os quatro padr&#245;es da entrevista:</strong> "<strong>One example that comes to mind is...</strong>" (a pergunta comportamental), "<strong>What I learned from that experience was...</strong>" (o fechamento de qualquer hist&#243;ria), "<strong>The way I approach this kind of challenge is...</strong>" (a pergunta de m&#233;todo) e "<strong>I would say my greatest strength in this area is...</strong>" (a pergunta direta). S&#227;o quatro esqueletos: voc&#234; s&#243; troca o recheio."""


HTML = f"""<div class="lesson-card" id="ex-lesson-5">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1553773077-91673524aafa?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 05 -- Pre-class</div>
      <h3>Performing Under Pressure -- The International Job Interview</h3>
      <div class="lesson-desc">A entrevista internacional: como transformar sete anos de experi&#234;ncia em EVID&#202;NCIA, controlar o que a banca ouve primeiro e responder &#224; pergunta desconfort&#225;vel sem pedir desculpas. Key words: track record, cross-functional, high-stakes, resilience, stakeholder management, value proposition, technical lead, subject matter expert, performance-driven, results-oriented, to set out, to account for, to burn the midnight oil, to throw in the towel. Structure: cleft sentences ("What I bring to this role is...", "It was in San Francisco that...", "The reason I... is that...") + os quatro padr&#245;es de resposta de entrevista.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="5" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="5">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Nas aulas 2 a 4 voc&#234; nomeou o trabalho: as a&#231;&#245;es, a inspe&#231;&#227;o, o contrato. Aqui voc&#234; nomeia a SI MESMO &mdash; as palavras que uma banca de entrevista est&#225; esperando ouvir. Voc&#234; j&#225; FEZ tudo isto na Motiva; o que falta &#233; a etiqueta em ingl&#234;s. Ou&#231;a cada termo e leia o exemplo.</p>
      <div class="vocab-cards">
{vocab_cards()}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l5">
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
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Cleft Sentences</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Como dividir a frase em duas para controlar o que a banca ouve primeiro &mdash; e comprar meio segundo para pensar (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).</p>
{GRAMMAR_TIP}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a estrutura correta. Toque em Listen para ouvir a frase inteira.</p>
{blanks_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Interview in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Coloque as etapas de uma resposta de entrevista internacional na ordem correta.</p>
      <div class="order-container" id="order-l5">
{order_html()}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l5')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases que abrem, sustentam e fecham qualquer entrevista em ingl&#234;s. Repare na pausa que cai logo ANTES do <em>is</em> &mdash; ela &#233; sua, e ela &#233; tempo de pensar.</p>
{speech_html()}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real de uma entrevista internacional &mdash; inclusive a pergunta desconfort&#225;vel sobre o seu ingl&#234;s.</p>
{quiz_html(QUIZZES_SIT)}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. Fale por 2 minutos, sem script e sem parar para se corrigir. Tom: profissional, confiante, direto ao valor.</p>
      <div class="think-card">
        <div class="think-question">"Tell me about yourself." You have ninety seconds with an international panel. Set out your background in three steps (Let me set out...), say what you bring to the role (What I bring to this role is...), prove it with one project (It was in San Francisco, in 2023, that...), state what makes you different from the other candidates (What sets me apart is...), and finish by accounting for the period when your English went quiet (I can account for it. What I learned from that experience was...).</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-5"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 5</h4>
{survival_html()}
    </div>

  </div>
</div>
"""

with open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('preclass.html gerado:', len(HTML), 'chars')
