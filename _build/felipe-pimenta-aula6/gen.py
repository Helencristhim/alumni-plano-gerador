#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 6 — Getting Things Done Through Others (Delegation).
Gramatica: causative have/get (have sth done, get sth done, have sb do, get sb to do).
Modelo: LEITURA (aula PAR, REGRA 29) — ic-reading + gist + true/false + discussao.
Callback (REGRA 20): o warm-up retoma o reported speech e o vocab da aula 5.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 6
SLUG = 'felipe-pimenta'

VOCAB = [
    ("To delegate", "to give someone a task AND the authority to do it",
     "delegar",
     "He delegates the task but keeps the decision, so nothing moves."),
    ("To hand over", "to pass responsibility for something to someone else",
     "repassar, transferir",
     "I handed the monthly close over to my controller in January."),
    ("Deliverable", "a concrete output someone owes you by a date",
     "entreg&#225;vel",
     "Name the deliverable and the date, or it will never arrive."),
    ("Workstream", "one parallel track of work inside a bigger project",
     "frente de trabalho",
     "Each workstream has one owner. Never two."),
    ("To loop in", "to add someone to a conversation they need to be in",
     "incluir na conversa",
     "Loop me in only if the number moves more than five percent."),
    ("Bandwidth", "the capacity someone has to take on more work",
     "capacidade, disponibilidade",
     "She does not have the bandwidth, and saying yes would be a lie."),
    ("Direct report", "a person who reports to you",
     "subordinado direto",
     "I have six direct reports and I was doing the work of three of them."),
    ("To outsource", "to pay an outside company to do the work",
     "terceirizar",
     "We outsourced the payroll and got two weeks a month back."),
    ("To chase up", "to follow up on something that is late",
     "cobrar, dar follow-up",
     "If you are chasing it up every week, you have not really delegated it."),
    ("To onboard", "to bring a new person or vendor up to speed",
     "integrar, fazer o onboarding",
     "We had the new controller onboarded in three weeks."),
    ("Remit", "the scope of what someone is responsible for",
     "al&#231;ada, escopo de responsabilidade",
     "That decision is inside her remit, so it is not my call."),
    ("Backlog", "the pile of work that is waiting to be done",
     "fila de trabalho, backlog",
     "My backlog was not a workload problem. It was a delegation problem."),
]

PHASES = ["The Bottleneck Is You", "The Language of Delegation", "The Essay",
          "The Code", "The Handover", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Tonight the subject is uncomfortable, because "
    "the bottleneck is not your team. It is you. And there is a grammar for stopping.' NAO cumprimente de forma "
    "scriptada (REGRA 27A).",
    "Lesson 6 &middot; Delegation", "Getting Things Done Through", "Others",
    "A CFO who does the work is not a CFO. He is a very expensive analyst."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 5 ANTES do tema novo (REGRA 20). Peca um report: "
    "'Someone told you something this week. Report it to me -- with the backshift.' Depois abra o tema, e va fundo: "
    "'Name one thing you did last week that a direct report should have done.' Deixe falar. Este warm-up costuma "
    "doer -- e por isso funciona.",
    "Chapter 1: The Bottleneck Is You",
    "One Thing You Did That You", "Shouldn't Have",
    "Not a mistake. A task. Something you did last week that somebody on your team should have done instead."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Este e o diagnostico. O Felipe e CFO, mas ainda faz trabalho de "
    "analista -- todo CFO promovido de dentro faz. E, quando ele tenta delegar em ingles, faltam DUAS coisas: o "
    "vocabulario (remit, deliverable, bandwidth) e a estrutura causativa. Sem elas, ele so consegue dizer 'please "
    "do this', que nao delega nada: apenas pede.",
    "The Real Diagnosis", "You Don't Have a Workload", "Problem",
    [("\"Please do this\"", "a request &mdash; you still own it"),
     ("\"I had the numbers audited\"", "the work happened, and not by you"),
     ("\"I got her to rebuild the model\"", "you moved a person, not a task")],
    "Your backlog is not a workload problem. It is a delegation problem &mdash; and in English it is also a grammar problem."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of delegation, an essay about why finance "
    "leaders are the worst delegators in any company, and the causative -- the structure that lets you say the work "
    "was done without saying you did it.' Antecipe o role-play: ele vai fazer um handover de verdade.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "remit, deliverable, bandwidth, workstream..."),
     ("2. The Essay", "why finance leaders never let go"),
     ("3. The Code", "have it done &middot; get her to do it")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. Without them, delegating in English collapses "
    "into please and thank you.' Passe ao proximo.",
    "Chapter 2: The Language of Delegation", "The Words That Move", "Work",
    "12 words &mdash; the vocabulary of letting go.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'to delegate': 'If I "
    "give you the task but I keep the decision, have I delegated? (No -- delegation includes the authority.)' CCQ "
    "'deliverable': 'Is &#39;improve the forecast&#39; a deliverable? (No -- a deliverable has a shape and a "
    "date.)' CCQ 'bandwidth': 'Is bandwidth about willingness or capacity? (Capacity.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Remit' e 'to chase up' sao o coracao da aula. CCQ "
    "'remit': 'If a decision is inside her remit, whose call is it? (Hers -- and you must not take it back.)' CCQ "
    "'to chase up': 'If I chase you up every week, did I really delegate? (No -- I just moved the task and kept the "
    "worry.)' Esse CCQ costuma acertar o Felipe em cheio.",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'deliverable' (de-LIV-er-a-ble, stress na 2a), "
    "'bandwidth' (BAND-width -- o brasileiro come o 'd'), 'remit' (REM-it como substantivo; re-MIT como verbo -- "
    "aqui e o substantivo, stress na 1a), 'outsource' (OUT-source). 'Remit' com stress errado vira outro sentido.",
    ["Deliverable", "Bandwidth", "Remit", "To outsource", "Workstream"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas descrevem exatamente a rotina dele.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"That decision is inside her ", "remit", ", so it is not my call.\""),
     ("\"If you are ", "chasing it up", " every week, you have not really delegated it.\""),
     ("\"She does not have the ", "bandwidth", ", and saying yes would be a lie.\""),
     ("\"Each ", "workstream", " has one owner. Never two.\""),
     ("\"Name the ", "deliverable", " and the date, or it will never arrive.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao leitura (1 min):</strong> Diga: 'An essay about why finance people are the worst delegators "
    "in any company. Read it as a diagnosis of yourself, not of your team.' Passe ao proximo.",
    "Chapter 3: The Essay", "Why Finance Leaders Never", "Let Go",
    "Read it as a diagnosis of yourself.", L.IMG['context']))

S.append(L.s_blocks(
    11, 3,
    "<strong>Leitura + gist (7 min):</strong> Felipe le em SILENCIO primeiro (2-3 min), sem dicionario. Depois "
    "pergunte a ideia central ANTES de mostrar as alternativas. Pergunta para provocar: 'The essay says the CFO who "
    "cannot delegate is usually the one who was best at the job. Does that describe anyone you know?'",
    "Read for the Main Idea", "The Expensive", "Analyst",
    ["reading", "gist"]))

S.append(L.s_blocks(
    12, 3,
    "<strong>True or False (5 min):</strong> Felipe responde ORALMENTE e JUSTIFICA com o trecho do texto antes de "
    "clicar. A justificativa e o exercicio &mdash; e ela que forca frase completa sob pressao.",
    "Check Understanding", "True or", "False?", ["tf"]))

S.append(L.s_blocks(
    13, 3,
    "<strong>Discussao (6 min):</strong> Aqui o Felipe FALA -- e o tema e o espelho dele. Nao corrija durante; "
    "anote. Se ele se defender ('mas no meu caso e diferente'), deixe: a defesa E o dado. Devolva no final.",
    "Discuss", "Talk It", "Through", ["guiding"]))

S.append(L.s_chapter(
    14, 4,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. Two verbs -- have and get -- that let you say "
    "the work happened without saying you did it.' Passe ao proximo.",
    "Chapter 4: The Code", "The", "Causative",
    "I had it done &middot; I got her to do it", L.IMG['code']))

S.append(L.s_discovery(
    15, 4,
    "<strong>Grammar discovery (8 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos. Pergunte: 'In all "
    "four, who did the actual work? And in which ones do we even know?' Espere ele perceber que nos dois primeiros a "
    "PESSOA some -- o foco vai pro RESULTADO. So entao clique 'Reveal the Rule'. CCQ: 'I HAD the numbers audited -- "
    "did I audit them? (No.) Did they get audited? (Yes.) So who cares who did it? (Exactly -- that is the point.)'",
    [("\"I <span style=\"color:#15803d;font-weight:700\">had</span> the numbers "
      "<span style=\"color:#15803d;font-weight:700\">audited</span> before the board met.\"",
      "I had the numbers audited before the board met."),
     ("\"We <span style=\"color:#15803d;font-weight:700\">got</span> the payroll "
      "<span style=\"color:#15803d;font-weight:700\">outsourced</span> in six weeks.\"",
      "We got the payroll outsourced in six weeks."),
     ("\"I <span style=\"color:#b45309;font-weight:700\">had my controller rebuild</span> the model.\"",
      "I had my controller rebuild the model."),
     ("\"I <span style=\"color:#1d4ed8;font-weight:700\">got her to take</span> the monthly close off my desk.\"",
      "I got her to take the monthly close off my desk.")],
    "In the first two, <span style=\"color:#15803d;font-weight:700\">who did the work?</span> We are not told, and "
    "we do not care. In the last two, we name the person &mdash; but look closely: "
    "<span style=\"color:#b45309;font-weight:700\">rebuild</span> vs "
    "<span style=\"color:#1d4ed8;font-weight:700\">to take</span>. Why the difference?",
    [("have + object + past participle",
      "The work got done. WHO did it is invisible &mdash; and that is the point. The result matters, not the hands.",
      "I <strong>had the numbers audited</strong>."),
     ("get + object + past participle",
      "Same meaning, slightly more informal, often with a hint of effort or difficulty.",
      "We <strong>got the payroll outsourced</strong>."),
     ("have + PERSON + bare infinitive",
      "You name the person. After <em>have</em>, NO <em>to</em>. It sounds like authority.",
      "I <strong>had my controller rebuild</strong> the model."),
     ("get + PERSON + TO + infinitive",
      "You name the person. After <em>get</em>, you MUST use <em>to</em>. It sounds like persuasion.",
      "I <strong>got her to rebuild</strong> the model."),
     ("The nuance",
      "<em>have</em> = you have the authority. <em>get</em> = you had to convince. Choose on purpose.",
      "I <strong>had</strong> him do it. / I <strong>got</strong> him to do it."),
    ],
    "The whole trick: after <strong>have</strong> + person, drop the <em>to</em>. After <strong>get</strong> + "
    "person, keep it. And with a <em>past participle</em>, the person disappears entirely &mdash; which is exactly "
    "how a CFO reports work he did not do.",
    "rule6"))

S.append(L.s_mistake(
    16, 4,
    "<strong>Common mistake (4 min):</strong> Tres erros. (1) 'I had my controller TO rebuild' -- depois de HAVE + "
    "pessoa NAO existe 'to'. (2) 'I got her rebuild' -- depois de GET + pessoa o 'to' e OBRIGATORIO. (3) O mais "
    "comum e o mais grave: 'I audited the numbers' quando ele NAO auditou -- o brasileiro assume a autoria por "
    "falta de estrutura, e isso confunde o board sobre quem fez o que. Peca que ele leia as certas DUAS vezes.",
    [("I had my controller to rebuild the model.",
      "I had my controller rebuild the model."),
     ("I got her rebuild the model.",
      "I got her to rebuild the model."),
     ("I audited the numbers before the board met.",
      "I had the numbers audited before the board met.")],
    "After <strong>have</strong> + person: no <em>to</em>. After <strong>get</strong> + person: <em>to</em> is "
    "obligatory. And if you did not do the work yourself, do not say you did &mdash; use the causative and let the "
    "result speak."))

S.append(L.s_fill(
    17, 4,
    "<strong>Grammar practice (4 min):</strong> Leia cada frase. Felipe monta a estrutura ORALMENTE antes de clicar. "
    "Se travar, pergunte: 'Do you want to name the person, or only the result?'",
    "Practice", "Complete the", "Sentence", "Say it first, then click to check",
    [("\"I ", "had the numbers audited", " before the board met &mdash; I did not audit them myself.\""),
     ("\"We ", "got the payroll outsourced", " in six weeks, and it saved two weeks a month.\""),
     ("\"I ", "had my controller rebuild", " the model. (have + person: no 'to')\""),
     ("\"I ", "got her to take", " the monthly close off my desk. (get + person: 'to' required)\""),
     ("\"We ", "had the new controller onboarded", " in three weeks.\"")]))

S.append(L.s_chapter(
    18, 5,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Priya Raman is your FP&amp;A director. She is very good, and "
    "she has been waiting two years for you to actually let go of something.' Passe ao proximo.",
    "Chapter 5: The Handover", "The Conversation You Have Been", "Avoiding",
    "The handover begins", L.IMG['turn']))

S.append(L.s_dialogue(
    19, 5,
    "<strong>Dialogo (7 min):</strong> Voce e a Priya. Clique 'Next Line' a cada fala. Para cada fala do Felipe, "
    "peca que ELE fale primeiro. Observe: ele consegue entregar a AUTORIDADE junto com a tarefa, ou fica preso no "
    "'me manda antes que eu olho'? Se ele pedir para revisar tudo, pare e devolva: 'Is that delegation, or is that "
    "chasing up?'",
    "Handing Over the", "Close",
    [("priya", "P", "ellen",
      "Felipe, you asked to see me. Is this about the monthly close again?",
      "Felipe, you asked to see me. Is this about the monthly close again?"),
     ("felipe", "F", "arthur",
      "It is. I am <span class=\"vocab-highlight\">handing</span> it <span class=\"vocab-highlight\">over</span> to "
      "you &mdash; the whole thing, not the parts I find boring. From March, the close is inside your "
      "<span class=\"vocab-highlight\">remit</span>.",
      "It is. I am handing it over to you, the whole thing, not the parts I find boring. From March, the close is "
      "inside your remit."),
     ("priya", "P", "ellen",
      "The whole thing. Including signing it off, or including preparing it so that you sign it off?",
      "The whole thing. Including signing it off, or including preparing it so that you sign it off?"),
     ("felipe", "F", "arthur",
      "You sign it. That is the difference between this time and the last three times. I will have the audit "
      "trail reviewed once a quarter, and I want to be "
      "<span class=\"vocab-highlight\">looped in</span> only if a number moves more than five percent.",
      "You sign it. That is the difference between this time and the last three times. I will have the audit trail "
      "reviewed once a quarter, and I want to be looped in only if a number moves more than five percent."),
     ("priya", "P", "ellen",
      "Then I need two things: I need you to get finance systems to give me access, and I do not have the "
      "<span class=\"vocab-highlight\">bandwidth</span> unless something comes off my desk.",
      "Then I need two things: I need you to get finance systems to give me access, and I do not have the bandwidth "
      "unless something comes off my desk."),
     ("felipe", "F", "arthur",
      "Agreed. I will get the access sorted this week, and we are "
      "<span class=\"vocab-highlight\">outsourcing</span> payroll &mdash; that is four days a month back for you. "
      "The <span class=\"vocab-highlight\">deliverable</span> is the March close, signed by you, on the fifth "
      "working day.",
      "Agreed. I will get the access sorted this week, and we are outsourcing payroll, and that is four days a "
      "month back for you. The deliverable is the March close, signed by you, on the fifth working day.")]))

S.append(L.s_comprehension(
    20, 5,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a PRIYA, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Priya",
    [("What is Priya's first question about the handover?",
      "Whether she will sign the close off herself, or only prepare it for him to sign."),
     ("What two things does she say she needs?",
      "Access from finance systems &mdash; and something taken off her desk, because she has no bandwidth."),
     ("Why is she skeptical at the start?",
      "Because he has tried to hand the close over three times before, and always kept the sign-off.")]))

S.append(L.s_listening(
    21, 5,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CFO explains how she stopped doing her team\\'s job. Just listen "
    "-- no text.' Toque SEM texto, 2 vezes. Peca que ele CONTE quantas causativas ouviu. Ouvido antes de boca.",
    1, "Listening", "The CFO Who Stopped", "Doing the Work",
    "How she got two days a week back. Sound first &mdash; no text.",
    "a6_listening_cfo.mp3", SLUG,
    [("What did she realize about her backlog?",
      "It was not a workload problem &mdash; it was a delegation problem."),
     ("What did she have done, and what did she get people to do?",
      "She had the payroll outsourced and the numbers audited; she got her controller to take the monthly close."),
     ("What is her rule for being looped in?",
      "Only if a number moves more than five percent &mdash; otherwise it is inside her team's remit.")]))

S.append(L.s_listening(
    22, 5,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now a leadership coach on why delegation fails. He is blunt.' "
    "Toque 2 vezes. Depois pergunte: 'He says chasing up is the proof that you did not delegate. Do you agree?' Este "
    "audio costuma ser o mais desconfortavel da aula -- e o mais util.",
    2, "Listening 2", "Why Delegation", "Fails",
    "A coach, and he is not being kind. Sound first &mdash; no text.",
    "a6_listening_coach.mp3", SLUG,
    [("What does he say is the proof that you have not really delegated?",
      "That you are still chasing it up every week."),
     ("What two things must be handed over together?",
      "The task and the authority &mdash; giving the task but keeping the decision is not delegation."),
     ("What does he say about people who were very good at the job?",
      "They are the worst delegators, because letting go feels like a drop in quality.")]))

S.append(L.s_chapter(
    23, 6,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the matrix, and the handover "
    "itself.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Let It", "Go",
    "Detective &middot; The Matrix &middot; The Handover", L.IMG['practice']))

S.append(L.s_error(
    24, 6,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. As duas "
    "primeiras sao o 'to' no lugar errado (O erro da aula). A ultima e a mais importante: assumir autoria de "
    "trabalho que ele nao fez.",
    [("I had my controller to rebuild the model.",
      "I had my controller rebuild the model."),
     ("I got her rebuild the model last quarter.",
      "I got her to rebuild the model last quarter."),
     ("I audited the numbers before the board met.",
      "I had the numbers audited before the board met."),
     ("We got outsourced the payroll in six weeks.",
      "We got the payroll outsourced in six weeks.")]))

S.append(L.s_artifact(
    25, 6,
    "<strong>Artefato (5 min):</strong> Esta e a matriz de delegacao real do time dele. Peca que o Felipe leia cada "
    "linha e a diga em voz alta com uma estrutura causativa. Depois faca a pergunta que doi: 'Look at the last "
    "column. How many of these are still you?'",
    "The Artifact", "The Delegation", "Matrix",
    "FINANCE &mdash; OWNERSHIP", "Q1 &middot; Confidential",
    [("Owner (CFO)", "Felipe Pimenta"),
     ("Monthly close", "P. Raman &mdash; signs off (from March)"),
     ("Payroll", "Outsourced &mdash; vendor onboarded"),
     ("Audit trail", "Reviewed quarterly, not monthly"),
     ("Forecast model", "Rebuilt by controller"),
     ("Board pack", "Still CFO &mdash; not delegated"),
     ("Escalation rule", "Loop in CFO only if &gt;5% move")],
    [("Say the Payroll line with a causative.",
      "\"We had the payroll outsourced, and we had the vendor onboarded in three weeks.\""),
     ("Say the Forecast model line, naming the person.",
      "\"I had my controller rebuild the forecast model.\" (have + person: no 'to')"),
     ("Now the uncomfortable one: the board pack is still you. Why?",
      "\"I should get someone to draft it &mdash; I have been telling myself it is faster if I do it.\"")]))

S.append(L.s_quickfire(
    26, 6,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO, com "
    "estrutura causativa. Nao aceite 'I did it' quando ele nao fez. Exija a frase inteira -- e a pressao aqui e o "
    "ponto: sob velocidade, ele volta a assumir a autoria de tudo.",
    "Your CEO Asks. You", "Answer."))

S.append(L.s_building(
    27, 6,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords. Felipe monta a frase COMPLETA em voz alta, "
    "depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes.",
    [("I / the numbers / audit / before the board met (result only, no person)",
      "I had the numbers audited before the board met."),
     ("we / the payroll / outsource / in six weeks (result only, informal)",
      "We got the payroll outsourced in six weeks."),
     ("I / my controller / rebuild / the model (name the person, authority)",
      "I had my controller rebuild the model."),
     ("I / her / take / the monthly close off my desk (name the person, persuasion)",
      "I got her to take the monthly close off my desk."),
     ("we / the new controller / onboard / in three weeks (result only)",
      "We had the new controller onboarded in three weeks.")]))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Priya. Abra com: 'Is this about the monthly close again?' "
    "Felipe usa as keywords. Deixe conduzir. O teste: ele entrega o SIGN-OFF, ou so o trabalho? Se ele segurar a "
    "assinatura, pare e pergunte: 'So what exactly have you handed over?'",
    "Hand Over the", "Close",
    "You are handing the monthly close to your FP&amp;A director. Hand over the task AND the authority: name the "
    "deliverable, the date, who signs it off, and the one rule for when she loops you in.",
    ["I am handing over...", "It is inside your remit now.", "The deliverable is...",
     "Loop me in only if..."]))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. Agora voce e a Priya DIFICIL: ela diz que nao tem "
    "bandwidth e que ja tentou isso tres vezes. 'You always take it back, Felipe.' Ele tem de NEGOCIAR -- tirar algo "
    "do prato dela, dar acesso, e provar que desta vez e diferente. Se ele so insistir, ela recusa. E o role-play "
    "mais realista da aula.",
    "She Says", "No",
    "Priya pushes back: she has no bandwidth, and you have taken the close back from her three times before. Do not "
    "insist. Negotiate: what comes OFF her desk, what access she gets, and what proof you can give her that this "
    "time you will not take it back.",
    ["What can come off your desk is...", "I will have the payroll outsourced, which gives you...",
     "I will get you access to...", "You sign it. That is the difference."],
    tint='.12'))

S.append(L.s_roleplay(
    30, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: o handover inteiro, ZERO pistas. NAO interrompa, NAO "
    "corrija no meio. Cronometre 3 min. CELEBRE se ele entregar a autoridade: a maioria dos executivos nao consegue "
    "fazer isso nem em portugues.",
    "The Whole", "Handover",
    "Run the full handover, end to end. Name the workstream, the deliverable and the date; say who signs it off; say "
    "what you are taking off her desk to create the bandwidth; set the escalation rule; and say out loud the thing "
    "you are giving up &mdash; the control.",
    []))

S.append(L.s_chapter(
    31, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'You gave away a piece of your job tonight. In English. That "
    "is what the next level actually costs.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You Let It", "Go",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("I had the numbers audited before the board met.",
     "Mandei auditar os n&#250;meros antes da reuni&#227;o do conselho."),
    ("I got her to take the monthly close off my desk.",
     "Consegui que ela assumisse o fechamento mensal."),
    ("From March, the close is inside your remit &mdash; you sign it off.",
     "A partir de mar&#231;o, o fechamento est&#225; na sua al&#231;ada &mdash; voc&#234; assina."),
    ("Loop me in only if a number moves more than five percent.",
     "Me inclua s&#243; se algum n&#250;mero variar mais de cinco por cento."),
    ("The deliverable is the March close, on the fifth working day.",
     "O entreg&#225;vel &#233; o fechamento de mar&#231;o, no quinto dia &#250;til."),
]

S.append(L.s_survival(
    32, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Sao as 5 "
    "frases de qualquer delegacao -- e servem inteiras numa entrevista quando perguntarem 'how do you build a "
    "team?'.",
    "Five Phrases for the", "Handover",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    33, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 6 no passaporte (registra no Supabase).",
    N,
    ["I can use have/get + object + past participle to report work I did not do myself.",
     "I can use have + person + bare infinitive (no 'to') when I have the authority.",
     "I can use get + person + to + infinitive when I had to persuade.",
     "I can hand over a task AND the authority, and set the escalation rule.",
     "I know my words: remit, deliverable, workstream, bandwidth, to chase up, to loop in."]))

S.append(L.s_complete(
    34, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 6 complete, Felipe. You earned your Delegation Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) escolher UMA tarefa real que ele ainda faz e que nao deveria, "
    "e gravar o handover completo em ingles, em 90 segundos, com pelo menos 3 causativas; (2) na semana, fazer esse "
    "handover DE VERDADE -- e entregar o sign-off junto. Proxima aula: Emphasis That Commands Attention -- inversao "
    "e cleft sentences.",
    N, "Delegation Badge", "You gave away part of your job, Felipe. That is what leading costs.",
    "Emphasis That Commands Attention"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Getting Things Done Through Others -- Delegation',
    'short_title': 'Getting Things Done Through Others',
    'menu_desc': 'Handover real + causative have/get',
    'desc': ('Entregar a tarefa E a autoridade &mdash; e parar de ser o gargalo do pr&#243;prio time. Key words: to '
             'delegate, to hand over, deliverable, workstream, to loop in, bandwidth, direct report, to outsource, '
             'to chase up, to onboard, remit, backlog. Structures: causative have/get &mdash; have/get + objeto + '
             'partic&#237;pio (o resultado sem o autor), have + pessoa + infinitivo SEM to, get + pessoa + TO + '
             'infinitivo.'),
    'hub_img': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'priya': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. Sem estas palavras, delegar em ingl&#234;s vira "please" '
                    'e "thank you" &mdash; e isso n&#227;o delega nada.'),

    'context_text': (
        'For two years Felipe told himself he had a workload problem. He had six <strong>direct reports</strong> and '
        'he was doing the work of three of them. His <strong>backlog</strong> was not a workload problem; it was a '
        'delegation problem. He would <strong>delegate</strong> a task and keep the decision, which is not '
        'delegation at all &mdash; it is just moving the work and keeping the worry. He was still '
        '<strong>chasing</strong> the monthly close <strong>up</strong> every week, and a task you chase every week '
        'has not been handed over. So he changed it. He <strong>had</strong> the payroll '
        '<strong>outsourced</strong>, which gave his team four days a month back. He <strong>had</strong> the new '
        'vendor <strong>onboarded</strong> in three weeks. He <strong>had</strong> his controller '
        '<strong>rebuild</strong> the forecast model &mdash; note the form: <em>have</em> + person + verb, with no '
        '<em>to</em>. And he finally <strong>got</strong> his FP&amp;A director <strong>to take</strong> the monthly '
        'close off his desk &mdash; note this form too: <em>get</em> + person + <strong>to</strong> + verb. The '
        '<strong>deliverable</strong> was named, the date was fixed, and, for the first time, she signed it off '
        'herself. It was inside her <strong>remit</strong>. He asked to be <strong>looped in</strong> only if a '
        'number moved more than five percent. He <strong>had</strong> the audit trail <strong>reviewed</strong> once '
        'a quarter &mdash; and notice that in that sentence nobody is told who reviewed it, because it does not '
        'matter.'),

    'context_quiz': [
        ("\"I had the numbers audited before the board met.\" Quem auditou os n&#250;meros?",
         [("O Felipe auditou pessoalmente.", False),
          ("Outra pessoa auditou &mdash; e a frase de prop&#243;sito N&#195;O diz quem, porque o que importa &#233; o "
           "resultado.", True),
          ("Ningu&#233;m auditou ainda.", False)]),
        ("Por que \"I had my controller rebuild\" n&#227;o tem \"to\", mas \"I got her to take\" tem?",
         [("Porque depois de <em>have</em> + pessoa o infinitivo vem SEM <em>to</em>, e depois de <em>get</em> + "
           "pessoa o <em>to</em> &#233; obrigat&#243;rio.", True),
          ("Porque \"rebuild\" &#233; irregular e \"take\" &#233; regular.", False),
          ("Porque a primeira frase est&#225; no passado e a segunda no presente.", False)]),
        ("Which sentence is correct English?",
         [("I had my controller to rebuild the model.", False),
          ("I had my controller rebuild the model.", True),
          ("I had my controller rebuilding the model.", False)]),
    ],

    'tip_title': 'Causative have / get',
    'tip_intro': ('Como dizer que o trabalho foi feito &mdash; sem dizer que foi voc&#234; que fez '
                  '(explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("have + objeto + partic&#237;pio",
         "O trabalho foi feito. QUEM fez &#233; invis&#237;vel &mdash; e &#233; esse o ponto. The result matters, not "
         "the hands.",
         "I <strong>had the numbers audited</strong>."),
        ("get + objeto + partic&#237;pio",
         "Mesmo sentido, um pouco mais informal, com um toque de esfor&#231;o. Slightly more informal.",
         "We <strong>got the payroll outsourced</strong>."),
        ("have + PESSOA + infinitivo SEM to",
         "Voc&#234; nomeia a pessoa. Depois de <em>have</em>, N&#195;O existe <em>to</em>. Soa a AUTORIDADE.",
         "I <strong>had my controller rebuild</strong> the model."),
        ("get + PESSOA + TO + infinitivo",
         "Voc&#234; nomeia a pessoa. Depois de <em>get</em>, o <em>to</em> &#201; OBRIGAT&#211;RIO. Soa a "
         "PERSUAS&#195;O.",
         "I <strong>got her to rebuild</strong> the model."),
        ("A nuance que o board escuta",
         "<em>have</em> = voc&#234; tinha a al&#231;ada. <em>get</em> = voc&#234; teve de convencer. Escolha de "
         "prop&#243;sito.",
         "I <strong>had</strong> him do it. / I <strong>got</strong> him to do it."),
        ("Por que isso importa",
         "Sem a causativa, o brasileiro diz \"I audited the numbers\" &mdash; e assume autoria de trabalho que "
         "n&#227;o fez.",
         "N&#195;O: <em>I audited it.</em> &nbsp;SIM: <strong>I had it audited.</strong>"),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (o erro n&#186; 1 do brasileiro):</strong> o <em>to</em> no lugar errado. '
                 'Depois de <strong>have</strong> + pessoa, NUNCA use <em>to</em>: "I had my controller '
                 '<strong>rebuild</strong>". Depois de <strong>get</strong> + pessoa, SEMPRE use: "I got her '
                 '<strong>to rebuild</strong>". E o erro mais grave n&#227;o &#233; gramatical: &#233; dizer "I '
                 'audited the numbers" quando voc&#234; n&#227;o auditou. Isso confunde o board sobre quem fez o '
                 'qu&#234; &mdash; e um CFO vive dessa distin&#231;&#227;o.'),

    'blanks': [
        ("I", "had the numbers audited", "Dica: o resultado sem o autor &mdash; have + objeto + partic&#237;pio",
         "I had the numbers audited before the board met.", "before the board met."),
        ("We", "got the payroll outsourced", "Dica: get + objeto + partic&#237;pio (mais informal)",
         "We got the payroll outsourced in six weeks.", "in six weeks."),
        ("I", "had my controller rebuild", "Dica: have + PESSOA + infinitivo, SEM \"to\"",
         "I had my controller rebuild the forecast model.", "the forecast model."),
        ("I", "got her to take", "Dica: get + PESSOA + \"to\" + infinitivo (o \"to\" &#233; obrigat&#243;rio)",
         "I got her to take the monthly close off my desk.", "the monthly close off my desk."),
        ("From March, the close is inside your", "remit",
         "Dica: o escopo do que algu&#233;m responde &mdash; a al&#231;ada dela",
         "From March, the close is inside your remit.", "."),
        ("Loop me in only if a number", "moves more than five percent",
         "Dica: a regra de escala&#231;&#227;o &mdash; sem ela, voc&#234; delega e continua cobrando",
         "Loop me in only if a number moves more than five percent.", "."),
    ],

    'order_title': 'Put the Handover in Order',
    'order_intro': ('Coloque as etapas de um handover real na ordem correta. Pular a &#250;ltima &#233; o motivo '
                    'pelo qual a maioria das delega&#231;&#245;es falha.'),
    'order': [
        (2, "Name the deliverable and the date &mdash; not \"improve the close\", but a shape and a day."),
        (5, "Say out loud the thing you are giving up: the sign-off. And do not take it back."),
        (1, "Say what is moving into her remit &mdash; the whole thing, not the boring parts."),
        (4, "Set the escalation rule: when, exactly, does she loop you in?"),
        (3, "Create the bandwidth: name what comes OFF her desk to make room."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases de uma '
                     'delega&#231;&#227;o de verdade &mdash; aquela em que a autoridade vai junto.'),
    'speech': SURVIVAL,

    'quiz': [
        ("The board asks who audited the numbers. You did NOT audit them. You say:",
         [("\"I audited the numbers before the meeting.\"", False),
          ("\"I had the numbers audited before the meeting.\"", True),
          ("\"The numbers were audited by me.\"", False)]),
        ("You want to say you told your controller to rebuild the model (you had the authority):",
         [("\"I had my controller to rebuild the model.\"", False),
          ("\"I had my controller rebuild the model.\"", True),
          ("\"I had my controller rebuilding the model.\"", False)]),
        ("You had to persuade her to take the close. You say:",
         [("\"I got her take the monthly close off my desk.\"", False),
          ("\"I got her to take the monthly close off my desk.\"", True),
          ("\"I had her to take the monthly close off my desk.\"", False)]),
        ("Your director says she has no bandwidth. The right move is:",
         [("\"I understand, but this is important. Please find a way.\"", False),
          ("\"Then something comes off your desk. We are outsourcing payroll &mdash; that is four days a month "
            "back.\"", True),
          ("\"Fine, I'll keep doing it myself.\"", False)]),
        ("You handed over the close but you still review it every week. That means:",
         [("You have delegated well &mdash; you are staying close to the detail.", False),
          ("You have not delegated at all. If you are chasing it up every week, you kept it.", True),
          ("You have delegated the task but correctly kept the bandwidth.", False)]),
    ],

    'think': ("Pick one real task you still do that a direct report should own. Hand it over, out loud, for 2-3 "
              "minutes. Use have + object + past participle at least twice, have + person + bare infinitive once, "
              "and get + person + to + infinitive once. Name the deliverable and the date, say who signs it off, say "
              "what comes off their desk to create the bandwidth, and set the escalation rule. Then say the "
              "sentence you find hardest: what you are giving up."),

    'listenings': [
        {"file": "a6_listening_cfo.mp3", "voice": "ellen",
         "text": ("For two years I told myself I had a workload problem. I had six direct reports and I was doing "
                  "the work of three of them, and my backlog kept growing, and I kept saying yes to more. Then "
                  "somebody asked me a question that I did not enjoy. She asked me how many of the things on my desk "
                  "I was still chasing up every single week. The answer was most of them, and that is when I "
                  "understood. It was never a workload problem. It was a delegation problem. So here is what I "
                  "actually did. I had the payroll outsourced, which gave the team four days a month back. I had the "
                  "numbers audited by an external firm instead of doing the review myself. I had my controller "
                  "rebuild the forecast model, and I did not look at it until it was finished. And the hard one: I "
                  "got my FP and A director to take the monthly close completely off my desk, including the sign "
                  "off. Not preparing it for me to sign. Signing it. The rule now is simple. They loop me in only if "
                  "a number moves more than five percent. Everything else is inside their remit, and I have stopped "
                  "asking.")},
        {"file": "a6_listening_coach.mp3", "voice": "arthur",
         "text": ("I am going to say something that most senior leaders do not want to hear. If you are still "
                  "chasing it up every week, you did not delegate it. You just moved the work and kept the worry, "
                  "and that is the worst of both worlds, because now two people are anxious about the same task "
                  "instead of one. Real delegation hands over two things at the same time: the task and the "
                  "authority. If you give somebody the task and you keep the decision, you have not delegated. You "
                  "have created a very expensive assistant. And here is the part that stings. The people who are "
                  "worst at delegating are almost always the people who were best at the job. You were a brilliant "
                  "analyst, so every time you let go, the quality dips, and you feel that dip personally, and you "
                  "take it back. But a leader who never lets the quality dip is a leader whose team never grows. So "
                  "name the deliverable, name the date, name who signs it off, and then get out of the way.")},
    ],

    'inclass_blocks': {
        "reading": [{
            "kind": "reading",
            "rtitle": "The Expensive Analyst &mdash; Why Finance Leaders Never Let Go",
            "paras": [
                ("There is a particular kind of chief financial officer who arrives early, leaves late, and is "
                 "privately convinced that the company would stop without him. He is not lazy and he is not "
                 "disorganized. He is, in fact, the opposite: he is the person who was so good at the work that he "
                 "was promoted away from it, and who has never entirely accepted the promotion."),
                ("The symptom is easy to name. He delegates the task and keeps the decision. His controller prepares "
                 "the monthly close and he signs it off; his analyst builds the model and he rewrites the "
                 "assumptions; his team drafts the board pack and he stays up until midnight changing the slides. "
                 "Each of these looks like delegation. None of them is. Handing over a task while keeping the "
                 "authority does not create capacity. It creates a very expensive assistant."),
                ("The tell is the chase. If you are chasing something up every week, you have not handed it over; "
                 "you have merely moved the work and kept the worry, so that two people are now anxious about a task "
                 "that only one of them owns. The backlog on such a desk is never a workload problem. It is a "
                 "delegation problem wearing a workload costume."),
                ("The cure is unglamorous. Name the deliverable and the date. Say who signs it off, and mean it. "
                 "Create the bandwidth by taking something off the other person's desk, rather than simply adding to "
                 "it. Set one rule for escalation &mdash; loop me in only if a number moves more than five percent "
                 "&mdash; and then, having said all of that, do the single hardest thing in management: get out of "
                 "the way, and let the quality dip once, without taking it back."),
            ],
            "source": "Essay &mdash; On finance leadership",
        }],
        "gist": [{
            "kind": "gist",
            "prompt": "What is the best one-line summary of this essay?",
            "choices": [
                ["a", "Finance leaders are overworked because their companies do not hire enough analysts.", False],
                ["b", "The CFO who cannot delegate is usually the one who was best at the job; keeping the "
                      "authority while handing over the task creates an expensive assistant, not capacity.", True],
                ["c", "Delegation fails because most finance teams are not competent enough to be trusted.", False],
            ],
        }],
        "tf": [{
            "kind": "tf",
            "items": [
                ["The essay says the CFO who cannot delegate is lazy or disorganized.", "f",
                 "It says the opposite: he is the person who was so good at the work that he was promoted away "
                 "from it."],
                ["Handing over a task while keeping the decision counts as delegation.", "f",
                 "The essay calls that creating a very expensive assistant &mdash; it does not create capacity."],
                ["Chasing something up every week is a sign you have not really handed it over.", "t",
                 "The essay calls the chase \"the tell\": you moved the work and kept the worry."],
                ["The essay recommends creating bandwidth by taking something off the other person's desk.", "t",
                 "It says to create the bandwidth rather than simply adding to their load."],
                ["The essay says a good leader never lets the quality dip.", "f",
                 "It says the hardest thing is to let the quality dip once, without taking the task back."],
            ],
        }],
        "guiding": [{
            "kind": "guiding",
            "items": [
                "\"He was so good at the work that he was promoted away from it, and never entirely accepted the "
                "promotion.\" How much of that sentence is about you?",
                "The essay says the chase is the tell. What are you still chasing up every week &mdash; and what "
                "would happen if you stopped?",
                "Name one thing on your desk that a direct report should own. What has stopped you from handing over "
                "the sign-off, not just the work?",
                "\"Let the quality dip once, without taking it back.\" Could you actually do that? What would it "
                "cost you in the first month, and what would it buy you in the first year?",
            ],
        }],
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Who audited the numbers?\" (you didn't)",
                 "tips": ["I had the numbers audited before the board met.",
                          "have + object + past participle. The person disappears."]},
                {"situation": "\"Did you rebuild the forecast model yourself?\"",
                 "tips": ["No &mdash; I had my controller rebuild it.",
                          "have + person + bare infinitive. No 'to'."]},
                {"situation": "\"How did you finally get the close off your desk?\"",
                 "tips": ["I got my FP&A director to take it &mdash; including the sign-off.",
                          "get + person + TO + infinitive."]},
                {"situation": "\"She says she has no bandwidth. Now what?\"",
                 "tips": ["Then something comes off her desk. We had the payroll outsourced.",
                          "Never delegate by simply adding."]},
                {"situation": "\"You handed it over &mdash; so why are you still reviewing it weekly?\"",
                 "tips": ["I shouldn't be. If I'm chasing it up, I haven't delegated it.",
                          "The chase is the tell. Own it."]},
                {"situation": "\"What is still on your desk that shouldn't be?\"",
                 "tips": ["The board pack. I should get someone to draft it.",
                          "Name it out loud. That is the first honest step."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Silicon Valley -- Seasons 3-4 (HBO Max)",
         "Uma com&#233;dia sobre fundadores que n&#227;o conseguem soltar NADA &mdash; e o pre&#231;o exato disso. "
         "Connection to Lesson 6: cada crise da s&#233;rie come&#231;a com algu&#233;m que delegou a tarefa e "
         "manteve a decis&#227;o.",
         "Dica: assista com legenda em ingl&#234;s. Anote 3 frases causativas (have/get + particípio).",
         "https://www.hbo.com/silicon-valley"),
        ("Podcast", "podcast", "HBR / Harvard Business Review -- delega&#231;&#227;o e escala de lideran&#231;a",
         "Executivos falando sobre como pararam de ser o gargalo do pr&#243;prio time. Connection to Lesson 6: "
         "&#233; o vocabul&#225;rio da aula (remit, bandwidth, deliverable) na boca de quem lidera de verdade.",
         "Dica: ou&#231;a a 1x. Cada vez que ouvir \"I had...\" ou \"I got... to...\", pause e repita.",
         "https://www.youtube.com/@HarvardBusinessReview"),
        ("YouTube", "youtube", "McKinsey -- como l&#237;deres escalam times (span of control, ownership)",
         "Como estruturar remit, workstream e ownership num time de finan&#231;as. Connection to Lesson 6: &#233; a "
         "matriz de delega&#231;&#227;o do artefato da aula, explicada por quem a desenhou.",
         "Dica: assista a 0.75x se precisar. Anote as 5 palavras da aula que aparecem sem tradu&#231;&#227;o.",
         "https://www.youtube.com/@McKinsey"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
