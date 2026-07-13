#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 10 — Negotiating Your Future (Career Transition).
Gramatica: mixed conditionals + gerunds vs infinitives.
Modelo: LEITURA (aula PAR, REGRA 29) — ic-reading + gist + true/false + discussao.
Callback (REGRA 20): o warm-up retoma as relative clauses e o vocab da aula 9.

ARCO: Sarah Whitmore, a headhunter da AULA 1, volta — agora com a oferta na mesa.
A aula 1 foi a screening call. A aula 10 e a negociacao. O aluno FECHA um ciclo.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 10
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Relocation", "moving to another country to take the job",
     "realoca&#231;&#227;o, mudan&#231;a de pa&#237;s",
     "The relocation package covers the move, but not the school fees."),
    ("Equity package", "the shares you receive as part of your pay",
     "pacote de a&#231;&#245;es",
     "If I had negotiated the equity package harder, I would own twice as much today."),
    ("Vesting", "the schedule over which your shares actually become yours",
     "vesting, per&#237;odo de aquisi&#231;&#227;o",
     "Four-year vesting means leaving early costs you real money."),
    ("Notice period", "how long you must keep working after you resign",
     "aviso pr&#233;vio",
     "My notice period is three months, and they want me in six weeks."),
    ("Counteroffer", "the offer your current employer makes to keep you",
     "contraproposta",
     "Accepting a counteroffer usually means leaving anyway, twelve months later."),
    ("Compensation", "the whole package: salary, bonus and equity together",
     "remunera&#231;&#227;o total",
     "Compensation is not salary. Confusing them is how executives get underpaid."),
    ("Sign-on bonus", "money paid simply for joining",
     "b&#244;nus de contrata&#231;&#227;o",
     "I asked for a sign-on bonus to cover the bonus I would forfeit."),
    ("To weigh up", "to consider carefully, comparing the options",
     "sopesar, ponderar",
     "I spent a month weighing up the offer before deciding to accept."),
    ("Non-compete", "a clause that stops you joining a rival for a period",
     "cl&#225;usula de n&#227;o concorr&#234;ncia",
     "The non-compete was twelve months, and that was my deal breaker."),
    ("Deal breaker", "the one thing you will not accept, whatever else they offer",
     "ponto inegoci&#225;vel",
     "Everything is negotiable except the deal breaker. Know yours before you start."),
    ("To turn down", "to refuse an offer",
     "recusar",
     "If I were more risk-averse, I would have turned it down."),
    ("Buyout", "money the new employer pays to cover what you lose by leaving",
     "compra do b&#244;nus perdido",
     "They agreed to a buyout of the bonus I was giving up."),
]

PHASES = ["The Offer", "The Language of the Deal", "The Case",
          "The Code", "The Negotiation", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'In Lesson 1, Sarah Whitmore called you about a "
    "role in London. Tonight she calls back -- with an offer on the table. Everything you have learned in nine "
    "lessons comes down to this conversation.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 10 &middot; The Offer", "Negotiating Your", "Future",
    "The call you took in Lesson 1 became an offer. Tonight you negotiate it."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 9 ANTES do tema novo (REGRA 20). Peca uma defining "
    "clause: 'Define your career in one sentence -- the licence that took you four years to win.' Depois abra o "
    "tema, e va direto ao osso: 'If you took a job in London next year, what would change in your life -- and what "
    "would you lose?' Deixe falar. Este warm-up ja e mixed conditional.",
    "Chapter 1: The Offer",
    "What Would Actually", "Change?",
    "London, next year. What changes tomorrow &mdash; and what do you give up to get it?"))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Explique a mecanica emocional da negociacao de carreira. O erro do "
    "executivo brasileiro nao e pedir pouco: e nao saber SEPARAR o que e negociavel do que e deal breaker -- e, na "
    "hora, aceitar tudo por gratidao. A gramatica de hoje serve exatamente para isso: pesar um passado que nao "
    "aconteceu contra um presente que poderia ser outro.",
    "Why Executives Get This Wrong", "Gratitude Is Not a", "Strategy",
    [("Everything is negotiable", "except the ONE thing that is not"),
     ("Know your deal breaker", "before the call, never during it"),
     ("Mixed conditional", "\"If I had taken it, I would be in London now\"")],
    "The offer is not a gift. It is the beginning of a conversation — and they expect you to have one."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of an offer letter, a real case of an "
    "executive who negotiated badly, and the two structures that let you weigh a life you did not choose against "
    "the one you have.' Antecipe o role-play: a negociacao completa com a Sarah.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "vesting, non-compete, buyout, deal breaker..."),
     ("2. The Case", "the executive who said yes too fast"),
     ("3. The Code", "mixed conditionals &middot; gerunds vs infinitives")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. Not knowing three of them has cost executives "
    "millions.' Passe ao proximo.",
    "Chapter 2: The Language of the Deal", "The Words of an Offer", "Letter",
    "12 words &mdash; the vocabulary of your next contract.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'vesting': 'I have "
    "four-year vesting and I leave after two. How much of the equity is mine? (Half -- and that is why leaving early "
    "is expensive.)' CCQ 'compensation vs salary': 'Are they the same? (No -- and confusing them is how executives "
    "get underpaid.)' CCQ 'counteroffer': 'If I accept my current employer\\'s counteroffer, am I safe? (Usually not "
    "-- most people leave anyway within a year.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Deal breaker' e 'buyout' sao o coracao da aula. "
    "CCQ 'deal breaker': 'How many deal breakers should you have? (One or two. If everything is a deal breaker, you "
    "are not negotiating -- you are refusing.)' CCQ 'buyout': 'I lose a bonus by leaving in March. What do I ask "
    "for? (A buyout -- and if you do not ask, nobody offers it.)' Este ultimo e dinheiro real na mesa.",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'vesting' (VEST-ing), 'non-compete' (non-com-PEET), "
    "'relocation' (ree-lo-KAY-shun), 'compensation' (com-pen-SAY-shun). Peca 'non-compete' tres vezes: e a palavra "
    "que ele vai ter de dizer em voz alta, com calma, no momento mais tenso da negociacao.",
    ["Vesting", "Non-compete", "Relocation", "Compensation", "Deal breaker"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas sao frases de uma negociacao real.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"Everything is negotiable except the ", "deal breaker", ". Know yours before you start.\""),
     ("\"I asked for a ", "sign-on bonus", " to cover the bonus I would forfeit.\""),
     ("\"They agreed to a ", "buyout", " of the bonus I was giving up.\""),
     ("\"The ", "non-compete", " was twelve months, and that was my line.\""),
     ("\"", "Compensation", " is not salary. Confusing them is how executives get underpaid.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao leitura (1 min):</strong> Diga: 'A case study. An executive who got the job he wanted and "
    "negotiated it badly. Read it as a warning, not as a story.' Passe ao proximo.",
    "Chapter 3: The Case", "The Executive Who Said Yes Too", "Fast",
    "Read it as a warning.", L.IMG['context']))

S.append(L.s_blocks(
    11, 3,
    "<strong>Leitura + gist (7 min):</strong> Felipe le em SILENCIO (2-3 min), sem dicionario. Depois pergunte a "
    "ideia central ANTES das alternativas. Pergunta para provocar: 'He got the job he wanted. So why is this a "
    "cautionary tale?'",
    "Read for the Main Idea", "The Cost of Saying", "Yes",
    ["reading", "gist"]))

S.append(L.s_blocks(
    12, 3,
    "<strong>True or False (5 min):</strong> Felipe responde ORALMENTE e JUSTIFICA com o trecho do texto antes de "
    "clicar. Exija frase completa &mdash; e, se der, com mixed conditional.",
    "Check Understanding", "True or", "False?", ["tf"]))

S.append(L.s_blocks(
    13, 3,
    "<strong>Discussao (6 min):</strong> Aqui o Felipe FALA -- e o tema e o futuro REAL dele. Este e provavelmente o "
    "slide mais importante do programa inteiro para ele. Nao corrija durante; ANOTE. Se ele hesitar em nomear o "
    "proprio deal breaker, insista com carinho: e a pergunta que ele precisa saber responder em ingles ANTES de a "
    "Sarah ligar de verdade.",
    "Discuss", "Talk It", "Through", ["guiding"]))

S.append(L.s_chapter(
    14, 4,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. Two structures: one weighs the life you did "
    "not choose, and the other decides what you are willing to do.' Passe ao proximo.",
    "Chapter 4: The Code", "Mixed Conditionals &amp;", "The Verb After the Verb",
    "\"If I had taken it, I would be in London now.\"", L.IMG['code']))

S.append(L.s_discovery(
    15, 4,
    "<strong>Grammar discovery (8 min):</strong> NAO de a regra primeiro. Leia os exemplos 1 e 2. Pergunte: 'Look at "
    "the two halves. One is about the PAST and the other is about NOW. Is that allowed?' Espere ele perceber que SIM "
    "-- e que e exatamente isso que a vida real exige. So entao clique 'Reveal the Rule'. CCQ: 'If I HAD TAKEN that "
    "job -- when? (Past.) I WOULD BE in London -- when? (Now.) So the condition is past and the result is present. "
    "That is a MIXED conditional.'",
    [("\"If I <span style=\"color:#15803d;font-weight:700\">had taken</span> that job, I "
      "<span style=\"color:#b45309;font-weight:700\">would be</span> in London now.\" <em>(past &rarr; now)</em>",
      "If I had taken that job, I would be in London now."),
     ("\"If I <span style=\"color:#b45309;font-weight:700\">were</span> more risk-averse, I "
      "<span style=\"color:#15803d;font-weight:700\">would have turned it down</span>.\" <em>(now &rarr; past)</em>",
      "If I were more risk-averse, I would have turned it down."),
     ("\"I am <span style=\"color:#7c3aed;font-weight:700\">considering relocating</span>, and I have "
      "<span style=\"color:#1d4ed8;font-weight:700\">decided to negotiate</span>.\"",
      "I am considering relocating, and I have decided to negotiate."),
     ("\"I <span style=\"color:#7c3aed;font-weight:700\">stopped negotiating</span>\" vs \"I "
      "<span style=\"color:#1d4ed8;font-weight:700\">stopped to negotiate</span>\" &mdash; <em>opposite "
      "meanings.</em>",
      "I stopped negotiating. I stopped to negotiate.")],
    "In the first two, one half is about the <span style=\"color:#15803d;font-weight:700\">past</span> and the other "
    "about <span style=\"color:#b45309;font-weight:700\">now</span>. Is that allowed? And in the last one &mdash; "
    "what on earth changed?",
    [("Mixed: past &rarr; present",
      "A past condition with a result you are living TODAY. The most useful conditional in a career conversation.",
      "<strong>If I had taken</strong> that job, <strong>I would be</strong> in London now."),
     ("Mixed: present &rarr; past",
      "Who you ARE explains what you DID. Rarer, and it sounds very senior.",
      "<strong>If I were</strong> more risk-averse, <strong>I would have turned</strong> it down."),
     ("Verb + GERUND",
      "consider, avoid, risk, involve, keep, delay, suggest, mind.",
      "I am <strong>considering relocating</strong>."),
     ("Verb + INFINITIVE",
      "decide, agree, offer, refuse, manage, hope, intend, plan, afford.",
      "I have <strong>decided to negotiate</strong>."),
     ("Preposition + GERUND (always)",
      "After ANY preposition, the verb takes -ing. No exceptions.",
      "committed <strong>to relocating</strong> / interested <strong>in moving</strong>"),
     ("The meaning trap",
      "<em>stop doing</em> = you quit it. <em>stop to do</em> = you paused IN ORDER to do it.",
      "I <strong>stopped negotiating</strong>. &ne; I <strong>stopped to negotiate</strong>."),
    ],
    "The mixed conditional is how adults talk about the roads they did not take. And the gerund/infinitive choice is "
    "how you say what you are <em>willing</em> to do &mdash; which, in a negotiation, is the whole game.",
    "rule10"))

S.append(L.s_mistake(
    16, 4,
    "<strong>Common mistake (4 min):</strong> Tres erros. (1) O mixed conditional 'travado' -- o brasileiro forca "
    "'would have been' quando o resultado e AGORA. (2) 'I am considering to relocate' -- depois de CONSIDER e "
    "sempre gerundio. (3) O mais perigoso: 'to' como preposicao ('committed to negotiate') -- depois de "
    "PREPOSICAO e SEMPRE -ing. Peca que ele leia as certas DUAS vezes.",
    [("If I had taken that job, I would have been in London now.",
      "If I had taken that job, I would be in London now."),
     ("I am considering to relocate to London next year.",
      "I am considering relocating to London next year."),
     ("I am committed to negotiate the equity package.",
      "I am committed to negotiating the equity package.")],
    "If the result is happening <strong>NOW</strong>, use <strong>would + verb</strong>, not <em>would have</em>. "
    "After <strong>consider</strong> use <em>-ing</em>. And after ANY <strong>preposition</strong> &mdash; including "
    "the <em>to</em> in \"committed to\" &mdash; the verb ALWAYS takes <strong>-ing</strong>."))

S.append(L.s_fill(
    17, 4,
    "<strong>Grammar practice (5 min):</strong> Leia cada frase. Felipe escolhe a forma ORALMENTE antes de clicar. "
    "Se travar, pergunte: 'Is the result in the past, or is it your life today?'",
    "Practice", "Complete the", "Sentence", "Say it first, then click to check",
    [("\"If I had accepted the London offer, I ", "would be", " running a European finance team now.\""),
     ("\"If I ", "were", " more risk-averse, I would have turned it down.\""),
     ("\"I am seriously ", "considering relocating", ", but I have not decided yet.\""),
     ("\"I have ", "decided to negotiate", " the equity package before I sign anything.\""),
     ("\"I am committed to ", "negotiating", " in good faith, but the non-compete is my deal breaker.\""),
     ("\"I ", "stopped negotiating", " when they met my number. (I quit negotiating)\"")]))

S.append(L.s_chapter(
    18, 5,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Sarah Whitmore. Lesson 1, she called you for a screening "
    "call and you could barely take it. Tonight she has an offer, and you are going to negotiate it.' Este momento "
    "e emocionalmente importante -- deixe o Felipe sentir o arco. Passe ao proximo.",
    "Chapter 5: The Negotiation", "Sarah Calls", "Back",
    "Nine lessons later. Same voice, different man.", L.IMG['turn']))

S.append(L.s_dialogue(
    19, 5,
    "<strong>Dialogo (8 min):</strong> Voce e a Sarah, a MESMA headhunter da aula 1. Clique 'Next Line' a cada fala. "
    "Para cada fala do Felipe, peca que ELE fale primeiro. Observe se ele NEGOCIA ou se agradece e aceita. Se ele "
    "aceitar de primeira, pare e devolva: 'Felipe. They expect you to negotiate. Try again.' E a licao da noite.",
    "The Offer on the", "Table",
    [("sarah", "S", "ellen",
      "Felipe, they want you. Base is competitive, the equity package vests over four years, and they would like you "
      "in London in six weeks.",
      "Felipe, they want you. Base is competitive, the equity package vests over four years, and they would like you "
      "in London in six weeks."),
     ("felipe", "F", "arthur",
      "Thank you &mdash; that means a lot. I am seriously considering relocating, and I have decided to negotiate "
      "two things before I say yes. Six weeks is not possible: my "
      "<span class=\"vocab-highlight\">notice period</span> is three months.",
      "Thank you. That means a lot. I am seriously considering relocating, and I have decided to negotiate two "
      "things before I say yes. Six weeks is not possible: my notice period is three months."),
     ("sarah", "S", "ellen",
      "Notice can usually be shortened. What is the second thing?",
      "Notice can usually be shortened. What is the second thing?"),
     ("felipe", "F", "arthur",
      "If I leave in March, I forfeit my bonus. So I am asking for a "
      "<span class=\"vocab-highlight\">buyout</span> of what I give up, or a "
      "<span class=\"vocab-highlight\">sign-on bonus</span> that covers it. And I should say this plainly: the "
      "twelve-month <span class=\"vocab-highlight\">non-compete</span> is my "
      "<span class=\"vocab-highlight\">deal breaker</span>.",
      "If I leave in March, I forfeit my bonus. So I am asking for a buyout of what I give up, or a sign-on bonus "
      "that covers it. And I should say this plainly: the twelve-month non-compete is my deal breaker."),
     ("sarah", "S", "ellen",
      "Most candidates do not say that out loud. Why is it a deal breaker?",
      "Most candidates do not say that out loud. Why is it a deal breaker?"),
     ("felipe", "F", "arthur",
      "Because if the role did not work out, twelve months would leave me unemployable in my own sector. If I had "
      "understood that clause five years ago, I would be in a very different position today. I am committed to "
      "negotiating everything else in good faith &mdash; but not that.",
      "Because if the role did not work out, twelve months would leave me unemployable in my own sector. If I had "
      "understood that clause five years ago, I would be in a very different position today. I am committed to "
      "negotiating everything else in good faith. But not that.")]))

S.append(L.s_comprehension(
    20, 5,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a SARAH, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Sarah",
    [("What three things does Sarah put on the table?",
      "A competitive base, an equity package vesting over four years, and a start in London in six weeks."),
     ("What does she say about the notice period?",
      "That notice can usually be shortened."),
     ("What surprises her about Felipe?",
      "That he names his deal breaker out loud &mdash; she says most candidates do not.")]))

S.append(L.s_listening(
    21, 5,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CFO who took the international job, five years on. Listen for "
    "the mixed conditionals -- they are how she talks about the road she did not take.' Toque SEM texto, 2 vezes.",
    1, "Listening", "Five Years", "Later",
    "A CFO who relocated, looking back. Sound first &mdash; no text.",
    "a10_listening_cfo.mp3", SLUG,
    [("What does she say she would be doing if she had stayed?",
      "She would still be running the same team in the same building &mdash; and she would be comfortable."),
     ("What does she say she regrets about the negotiation?",
      "Not negotiating the equity package &mdash; if she had pushed, she would own twice as much today."),
     ("What was her deal breaker, and did she hold it?",
      "The non-compete. She held it, and they removed it &mdash; because she asked.")]))

S.append(L.s_listening(
    22, 5,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now a headhunter explains how executives negotiate badly. He is "
    "very direct.' Toque 2 vezes. Depois pergunte: 'He says gratitude is the most expensive emotion in a "
    "negotiation. What does he mean?' Este audio existe para desarmar exatamente o reflexo do Felipe.",
    2, "Listening 2", "How Executives Negotiate", "Badly",
    "A headhunter, being honest. Sound first &mdash; no text.",
    "a10_listening_headhunter.mp3", SLUG,
    [("What does he say is the most expensive emotion in a negotiation?",
      "Gratitude &mdash; candidates say yes too fast because they feel grateful to have been chosen."),
     ("What does he say the company expects?",
      "That you will negotiate. They have budgeted for it, and saying yes immediately costs you money."),
     ("What does he say about naming your deal breaker?",
      "Say it out loud and early &mdash; it makes you easier to deal with, not harder.")]))

S.append(L.s_chapter(
    23, 6,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the offer letter, and the "
    "negotiation itself.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Ask for", "It",
    "Detective &middot; The Letter &middot; The Negotiation", L.IMG['practice']))

S.append(L.s_error(
    24, 6,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. A primeira e o "
    "mixed conditional 'travado'; a terceira e a preposicao + gerundio. Trate como vitoria quando ele achar sozinho.",
    [("If I had taken that job, I would have been in London now.",
      "If I had taken that job, I would be in London now."),
     ("I am considering to relocate to London next year.",
      "I am considering relocating to London next year."),
     ("I am committed to negotiate the equity package in good faith.",
      "I am committed to negotiating the equity package in good faith."),
     ("If I would be more risk-averse, I would have turned it down.",
      "If I were more risk-averse, I would have turned it down.")]))

S.append(L.s_artifact(
    25, 6,
    "<strong>Artefato (5 min):</strong> Esta e a oferta REAL. Peca que o Felipe leia cada linha e diga, em voz alta, "
    "(a) se aquilo e negociavel, (b) qual estrutura ele usaria para negociar. Depois a pergunta final, e deixe o "
    "silencio trabalhar: 'Which line is your deal breaker?'",
    "The Artifact", "The Offer", "Letter",
    "HARTLEY &amp; VANCE", "Offer &middot; Private &amp; Confidential"
    ,
    [("Candidate", "Felipe Pimenta"),
     ("Role", "Chief Financial Officer &mdash; London"),
     ("Base + bonus", "Competitive; reviewed annually"),
     ("Equity package", "Vesting over 4 years"),
     ("Sign-on bonus", "Not offered"),
     ("Start date", "6 weeks (notice period: 3 months)"),
     ("Non-compete", "12 months")],
    [("The start date conflicts with your notice. Negotiate it.",
      "\"Six weeks is not possible &mdash; my notice period is three months. Notice can usually be shortened, though.\""),
     ("You forfeit your bonus by leaving in March. Ask.",
      "\"I am asking for a buyout of the bonus I give up, or a sign-on bonus that covers it.\""),
     ("Name the deal breaker &mdash; and justify it with a mixed conditional.",
      "\"The twelve-month non-compete is my deal breaker. If the role did not work out, it would leave me "
      "unemployable in my own sector.\"")]))

S.append(L.s_quickfire(
    26, 6,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO. REGRA DESTE "
    "SLIDE: ele nao pode dizer 'yes' nem 'thank you, I accept' em nenhuma resposta. Toda resposta tem de PEDIR ou "
    "PONDERAR algo. E chato de proposito: o reflexo de gratidao e o inimigo, e so se desarma com repeticao.",
    "They Offer. You", "Negotiate."))

S.append(L.s_building(
    27, 6,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords. Felipe monta a frase COMPLETA em voz alta, "
    "depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes.",
    [("if / I / take / that job -> I / be / in London now (mixed: past -> present)",
      "If I had taken that job, I would be in London now."),
     ("if / I / be / more risk-averse -> I / turn it down (mixed: present -> past)",
      "If I were more risk-averse, I would have turned it down."),
     ("I / consider / relocate / but not decide yet (verb + gerund)",
      "I am considering relocating, but I have not decided yet."),
     ("I / decide / negotiate / the equity package (verb + infinitive)",
      "I have decided to negotiate the equity package."),
     ("I / be committed to / negotiate / in good faith (preposition + gerund)",
      "I am committed to negotiating in good faith.")]))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Sarah. Abra com a oferta exata do artefato. Felipe usa as "
    "keywords. O teste: ele NEGOCIA? Se ele agradecer e aceitar, pare e diga: 'They budgeted for a negotiation, "
    "Felipe. You just left money on the table. Again.'",
    "Negotiate the", "Offer",
    "Sarah presents the offer: competitive base, four-year vesting, London in six weeks, twelve-month non-compete. "
    "Negotiate. Do not say yes. Ask for the buyout, fix the start date, and name your deal breaker.",
    ["I am considering relocating, and I have decided to...", "My notice period is...",
     "I am asking for a buyout of...", "The non-compete is my deal breaker because..."]))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. Agora a Sarah PRESSIONA: 'They have another "
    "candidate, Felipe. If you push on the non-compete, they may walk.' Este e o momento em que a maioria cede. Ele "
    "tem de segurar o deal breaker SEM ser arrogante -- e sem agradecer demais. Se ele ceder, pare a aula e "
    "converse: e essa a conversa que ele precisa ter consigo mesmo antes de ter com a Sarah.",
    "They Might Walk", "Away",
    "Sarah applies pressure: there is another candidate, and pushing on the non-compete could kill the offer. Hold "
    "your deal breaker anyway. Explain WHY it is one &mdash; with a mixed conditional &mdash; and stay warm while "
    "you do it.",
    ["I understand the pressure, and I would still say...", "If the role did not work out, I would...",
     "I am committed to negotiating everything else...", "But not that."],
    tint='.12'))

S.append(L.s_roleplay(
    30, 6,
    "<strong>Free Practice (6 min):</strong> A missao da aula, e do bloco: a negociacao inteira, ZERO pistas, 4 "
    "minutos. NAO interrompa. Diga ANTES: 'This is the call you will actually have one day. Have it now, badly, "
    "with me -- so that you have it well, with them.' CELEBRE muito. Se ele negociar sem pedir desculpa por "
    "negociar, o programa cumpriu a promessa.",
    "The Whole", "Negotiation",
    "Take the negotiation end to end. Thank her once &mdash; and only once. Say what you are considering and what "
    "you have decided. Fix the start date against your notice period. Ask for the buyout. Name your deal breaker and "
    "justify it. Then ask HER what the company expects you to push on &mdash; and listen.",
    []))

S.append(L.s_chapter(
    31, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'Ten lessons ago, you could not take Sarah\\'s call. Tonight "
    "you negotiated with her.' Deixe isso pousar. Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You", "Negotiated",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("I am considering relocating, and I have decided to negotiate before I say yes.",
     "Estou considerando me mudar, e decidi negociar antes de dizer sim."),
    ("My notice period is three months, so six weeks is not possible.",
     "Meu aviso pr&#233;vio &#233; de tr&#234;s meses, ent&#227;o seis semanas n&#227;o &#233; poss&#237;vel."),
    ("I am asking for a buyout of the bonus I would forfeit.",
     "Estou pedindo a compra do b&#244;nus que eu perderia."),
    ("The twelve-month non-compete is my deal breaker.",
     "A cl&#225;usula de n&#227;o concorr&#234;ncia de doze meses &#233; meu ponto inegoci&#225;vel."),
    ("If I had taken that job five years ago, I would be in London now.",
     "Se eu tivesse aceitado aquele emprego cinco anos atr&#225;s, eu estaria em Londres agora."),
]

S.append(L.s_survival(
    32, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Estas cinco "
    "frases sao a negociacao inteira. Peca que ele grave no celular e ouca antes da proxima conversa de carreira "
    "REAL &mdash; porque ela vai acontecer.",
    "Five Phrases for the", "Negotiation",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    33, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 10 no passaporte (registra no Supabase).",
    N,
    ["I can use a mixed conditional: If I had taken it, I would be in London now.",
     "I can use the reverse: If I were more risk-averse, I would have turned it down.",
     "I know which verbs take a gerund (consider, avoid) and which take an infinitive (decide, agree).",
     "I know that after any preposition &mdash; including 'committed to' &mdash; the verb takes -ing.",
     "I can negotiate an offer without apologizing for negotiating, and name my deal breaker out loud."]))

S.append(L.s_complete(
    34, 7,
    "<strong>Encerramento (3 min):</strong> Diga: 'Lesson 10 complete, Felipe. You earned your Negotiator Badge.' "
    "Feche o arco em voz alta: na aula 1 ele mal conseguia atender a Sarah; hoje ele negociou com ela. HOMEWORK "
    "(ORALMENTE, nunca escrito na tela): (1) escrever o proprio DEAL BREAKER numa frase, em ingles, e gravar "
    "dizendo em voz alta ate sair sem hesitar; (2) escrever 3 mixed conditionals sobre decisoes de carreira que ele "
    "NAO tomou. Proxima aula: Holding the Room -- apresentacoes financeiras de alto risco.",
    N, "Negotiator Badge", "In Lesson 1 you could not take her call. Tonight you negotiated with her.",
    "Holding the Room -- High-Stakes Presentations"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Negotiating Your Future -- Career Transition',
    'short_title': 'Negotiating Your Future',
    'menu_desc': 'A oferta de Londres na mesa + mixed conditionals e gerunds/infinitives',
    'desc': ('A headhunter da aula 1 volta &mdash; agora com a oferta. Negociar sem pedir desculpa por negociar. '
             'Key words: relocation, equity package, vesting, notice period, counteroffer, compensation, sign-on '
             'bonus, to weigh up, non-compete, deal breaker, to turn down, buyout. Structures: mixed conditionals '
             '(passado &rarr; presente: "If I had taken it, I would be in London now"; presente &rarr; passado: "If '
             'I were more risk-averse, I would have turned it down") e gerunds vs infinitives (consider + -ing, '
             'decide + to, e depois de QUALQUER preposi&#231;&#227;o sempre -ing).'),
    'hub_img': 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'sarah': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. N&#227;o conhecer tr&#234;s destas palavras j&#225; custou '
                    'milh&#245;es a executivos muito bons.'),

    'context_text': (
        'Sarah called back. The offer was on the table: a competitive base, an <strong>equity package</strong> '
        '<strong>vesting</strong> over four years, London in six weeks, and a twelve-month '
        '<strong>non-compete</strong>. Most executives, at this exact moment, say thank you and say yes. Felipe did '
        'not. He said he was <strong>considering relocating</strong> &mdash; note the gerund after <em>consider</em> '
        '&mdash; and that he had <strong>decided to negotiate</strong> &mdash; note the infinitive after '
        '<em>decide</em>. His <strong>notice period</strong> was three months, so six weeks was not possible. '
        'Leaving in March meant forfeiting his bonus, so he asked for a <strong>buyout</strong> of what he was '
        'giving up, or a <strong>sign-on bonus</strong> that covered it. And then he did the thing that surprised '
        'her: he named his <strong>deal breaker</strong> out loud. The twelve-month non-compete. '
        '<strong>If the role did not work out, twelve months would leave him unemployable</strong> in his own '
        'sector. <strong>If he had understood that clause five years ago, he would be in a very different position '
        'today</strong> &mdash; a past condition, a present result. He was <strong>committed to negotiating</strong> '
        'everything else in good faith &mdash; note the <em>-ing</em>, because <em>to</em> here is a preposition, '
        'not an infinitive. Everything was negotiable. One thing was not.'),

    'context_quiz': [
        ("\"If I had understood that clause five years ago, I would be in a very different position today.\" Por que "
         "N&#195;O &#233; \"I would have been\"?",
         [("Porque a condi&#231;&#227;o &#233; passada, mas o RESULTADO &#233; agora &mdash; e um resultado presente "
           "pede <em>would + verbo</em>, n&#227;o <em>would have</em>.", True),
          ("Porque \"understand\" &#233; um verbo irregular.", False),
          ("Porque as duas formas s&#227;o igualmente corretas aqui.", False)]),
        ("Por que \"committed to negotiating\" e n&#227;o \"committed to negotiate\"?",
         [("Porque o <em>to</em> de \"committed to\" &#233; uma PREPOSI&#199;&#195;O &mdash; e depois de "
           "preposi&#231;&#227;o o verbo sempre vai para -ing.", True),
          ("Porque \"negotiate\" n&#227;o tem forma de infinitivo.", False),
          ("Porque \"committed\" exige sempre o gerúndio do verbo seguinte, mesmo sem preposi&#231;&#227;o.", False)]),
        ("Which sentence is correct English?",
         [("I am considering to relocate to London.", False),
          ("I am considering relocating to London.", True),
          ("I am considering relocate to London.", False)]),
    ],

    'tip_title': 'Mixed Conditionals + Gerunds vs Infinitives',
    'tip_intro': ('Como pesar a vida que voc&#234; N&#195;O escolheu &mdash; e como dizer o que voc&#234; est&#225; '
                  'disposto a fazer (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("Mixed: passado &rarr; presente",
         "Condi&#231;&#227;o no passado, resultado que voc&#234; VIVE HOJE. O condicional mais &#250;til de uma "
         "conversa de carreira.",
         "<strong>If I had taken</strong> that job, <strong>I would be</strong> in London now."),
        ("Mixed: presente &rarr; passado",
         "Quem voc&#234; &#201; explica o que voc&#234; FEZ. Mais raro, e soa muito s&#234;nior.",
         "<strong>If I were</strong> more risk-averse, <strong>I would have turned</strong> it down."),
        ("Verbo + GER&#218;NDIO",
         "consider, avoid, risk, involve, keep, delay, suggest, mind.",
         "I am <strong>considering relocating</strong>."),
        ("Verbo + INFINITIVO",
         "decide, agree, offer, refuse, manage, hope, intend, plan, afford.",
         "I have <strong>decided to negotiate</strong>."),
        ("Preposi&#231;&#227;o + GER&#218;NDIO (sempre)",
         "Depois de QUALQUER preposi&#231;&#227;o, o verbo vai para -ing. Sem exce&#231;&#227;o.",
         "committed <strong>to relocating</strong> / interested <strong>in moving</strong>"),
        ("A armadilha de sentido",
         "<em>stop doing</em> = voc&#234; parou de fazer. <em>stop to do</em> = voc&#234; parou PARA fazer.",
         "I <strong>stopped negotiating</strong>. &ne; I <strong>stopped to negotiate</strong>."),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (tr&#234;s erros de brasileiro):</strong> (1) o mixed conditional '
                 '"travado" &mdash; se o resultado &#233; AGORA, use <strong>would + verbo</strong> ("I would '
                 '<em>be</em> in London now"), nunca <em>would have been</em>. (2) "I am considering <em>to '
                 'relocate</em>" &mdash; depois de <strong>consider</strong> &#233; sempre <strong>-ing</strong>. (3) '
                 'O mais trai&#231;oeiro: em "committed <strong>to</strong>", o <em>to</em> &#233; '
                 'PREPOSI&#199;&#195;O, n&#227;o infinitivo &mdash; ent&#227;o &#233; "committed to '
                 '<strong>negotiating</strong>". Teste: se voc&#234; puder trocar o verbo por um substantivo '
                 '("committed to <em>the deal</em>"), &#233; preposi&#231;&#227;o &rarr; use -ing.'),

    'blanks': [
        ("If I had taken that job, I", "would be", "Dica: mixed &mdash; condi&#231;&#227;o no passado, resultado "
         "AGORA (nunca \"would have been\")",
         "If I had taken that job, I would be in London now.", "in London now."),
        ("If I", "were", "Dica: mixed ao contr&#225;rio &mdash; quem voc&#234; &#201; explica o que voc&#234; FEZ",
         "If I were more risk-averse, I would have turned it down.",
         "more risk-averse, I would have turned it down."),
        ("I am seriously", "considering relocating", "Dica: depois de <em>consider</em>, sempre ger&#250;ndio",
         "I am seriously considering relocating to London.", "to London."),
        ("I have", "decided to negotiate", "Dica: depois de <em>decide</em>, sempre infinitivo com <em>to</em>",
         "I have decided to negotiate the equity package.", "the equity package."),
        ("I am committed to", "negotiating", "Dica: o <em>to</em> aqui &#233; PREPOSI&#199;&#195;O &rarr; verbo em -ing",
         "I am committed to negotiating in good faith.", "in good faith."),
        ("The twelve-month non-compete is my", "deal breaker",
         "Dica: a &#250;nica coisa que voc&#234; N&#195;O aceita, aconte&#231;a o que acontecer",
         "The twelve-month non-compete is my deal breaker.", "."),
    ],

    'order_title': 'Put the Negotiation in Order',
    'order_intro': ('Coloque as etapas de uma negocia&#231;&#227;o de oferta na ordem correta. Dizer sim cedo demais '
                    '&#233; o erro que custa mais caro na carreira de um executivo.'),
    'order': [
        (2, "Say what you are considering and what you have decided &mdash; without saying yes."),
        (5, "Ask THEM what the company expects you to push on. Then listen."),
        (1, "Thank them once. Once, and no more."),
        (4, "Name your deal breaker out loud, and justify it with a mixed conditional."),
        (3, "Fix the practical conflicts: notice period, start date, the bonus you forfeit."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases da '
                     'negocia&#231;&#227;o que voc&#234; vai ter de verdade &mdash; provavelmente antes do que '
                     'imagina.'),
    'speech': SURVIVAL,

    'quiz': [
        ("You did not take a job five years ago. Today you are still in S&atilde;o Paulo. You say:",
         [("\"If I had taken that job, I would have been in London now.\"", False),
          ("\"If I had taken that job, I would be in London now.\"", True),
          ("\"If I took that job, I would be in London now.\"", False)]),
        ("You are thinking about it, but you have not decided. You say:",
         [("\"I am considering to relocate to London.\"", False),
          ("\"I am considering relocating to London.\"", True),
          ("\"I am considering relocate to London.\"", False)]),
        ("You want to say you will negotiate honestly. Which is correct?",
         [("\"I am committed to negotiate in good faith.\"", False),
          ("\"I am committed to negotiating in good faith.\"", True),
          ("\"I am committed for negotiating in good faith.\"", False)]),
        ("The offer arrives. You feel grateful. The most senior move is:",
         [("Say thank you and accept &mdash; they chose you, and pushing might annoy them.", False),
          ("Thank them once, then negotiate. They budgeted for it, and saying yes immediately costs you money.", True),
          ("Say nothing for a week to seem unavailable.", False)]),
        ("The twelve-month non-compete would end your career if the role failed. You say:",
         [("\"I'm not very comfortable with the non-compete, but I can probably live with it.\"", False),
          ("\"The twelve-month non-compete is my deal breaker. If the role did not work out, it would leave me "
            "unemployable in my own sector.\"", True),
          ("\"Can we maybe look at the non-compete at some point later?\"", False)]),
    ],

    'think': ("The headhunter from Lesson 1 calls back with a real offer: competitive base, four-year vesting, London "
              "in six weeks, twelve-month non-compete. Negotiate it out loud for 2-3 minutes. Thank her ONCE. Use "
              "\"I am considering + -ing\" and \"I have decided + to\". Fix the start date against your notice "
              "period, ask for a buyout of the bonus you forfeit, and name your deal breaker &mdash; justifying it "
              "with a mixed conditional. Do not apologize for negotiating."),

    'listenings': [
        {"file": "a10_listening_cfo.mp3", "voice": "ellen",
         "text": ("People ask me whether I regret relocating, and the honest answer is no, but it is more "
                  "complicated than that. If I had stayed, I would still be running the same team in the same "
                  "building, and I would be comfortable, and I think a part of me would have known that I had "
                  "stopped growing. So I do not regret the move. What I regret is the negotiation. I said yes far "
                  "too quickly, because I was grateful, and gratitude is an expensive emotion in a room like that. "
                  "I did not negotiate the equity package at all. I simply accepted what was written. If I had "
                  "pushed on it, even a little, I would own roughly twice as much of that company today, and I think "
                  "about that more often than I would like to admit. The one thing I did get right was the "
                  "non-compete. Twelve months would have made me unemployable in my own sector if the role had not "
                  "worked out, so I said, out loud, that it was my deal breaker. And do you know what happened? They "
                  "removed it. They removed it because I asked. That is the whole lesson.")},
        {"file": "a10_listening_headhunter.mp3", "voice": "arthur",
         "text": ("I have placed several hundred executives, and I am going to tell you the truth about how most of "
                  "them negotiate, which is badly. The single most expensive emotion in this process is gratitude. "
                  "The offer arrives, the candidate feels chosen, and they say yes within about six minutes. Please "
                  "understand what is happening on the other side of that table. The company has budgeted for a "
                  "negotiation. They expect one. They have left room in the offer precisely because they assume you "
                  "will push, and when you do not push, that room does not go to you. It simply stays with them. "
                  "Second point, and this one surprises people. Name your deal breaker out loud, and name it early. "
                  "Candidates think that admitting a hard limit makes them difficult. It does the opposite. It makes "
                  "you easy to deal with, because now I know exactly where the wall is, and I can build the offer "
                  "around it instead of discovering it three weeks later. Say it in one clear sentence. Say why. And "
                  "then stop talking, and let them solve it.")},
    ],

    'inclass_blocks': {
        "reading": [{
            "kind": "reading",
            "rtitle": "The Executive Who Said Yes Too Fast",
            "paras": [
                ("He had wanted the role for a decade. When the offer finally arrived &mdash; chief financial officer, "
                 "a European group, a title that would have taken another eight years at home &mdash; he read it "
                 "twice, felt something close to disbelief, and accepted it the same afternoon. He was, he says now, "
                 "profoundly grateful. Gratitude turned out to be the most expensive emotion of his career."),
                ("He did not negotiate the equity package. He simply accepted the vesting schedule as written, "
                 "because it did not occur to him that a schedule could be a subject of discussion. He did not ask "
                 "for a buyout of the bonus he forfeited by leaving in March, and nobody offered him one, because "
                 "nobody offers what is not requested. And he agreed to a twelve-month non-compete without reading "
                 "it closely, on the reasonable assumption that the role would work out."),
                ("The role did not work out. Eighteen months later, a new chief executive arrived with her own "
                 "finance leader, and he found himself, at forty-four, contractually forbidden from working in the "
                 "only sector he knew, for a year. If he had negotiated that single clause, he would be running a "
                 "finance function somewhere today. Instead he spent the year consulting, unhappily, on things that "
                 "did not interest him."),
                ("The lesson is not that he should have refused the job. He was right to take it. The lesson is that "
                 "a company that has decided to hire you has already budgeted for a negotiation and left room in the "
                 "offer, and that room does not disappear when you decline to use it &mdash; it simply stays with "
                 "them. Everything is negotiable except your deal breaker, and you must know which is which before "
                 "the call, never during it."),
            ],
            "source": "Case study &mdash; Executive careers",
        }],
        "gist": [{
            "kind": "gist",
            "prompt": "What is the best one-line summary of this case?",
            "choices": [
                ["a", "He should never have accepted an international role at his age.", False],
                ["b", "He was right to take the job, but gratitude made him accept without negotiating &mdash; and "
                      "the one clause he did not read cost him a year of his career.", True],
                ["c", "The company deceived him by hiding the non-compete clause in the contract.", False],
            ],
        }],
        "tf": [{
            "kind": "tf",
            "items": [
                ["He accepted the offer on the same day it arrived.", "t",
                 "He read it twice and accepted it the same afternoon."],
                ["He negotiated the vesting schedule of his equity package.", "f",
                 "He accepted it as written &mdash; it did not occur to him that it could be discussed."],
                ["He asked for a buyout of the bonus he forfeited.", "f",
                 "He did not ask, and nobody offered &mdash; because nobody offers what is not requested."],
                ["The text says he was wrong to take the job.", "f",
                 "It says explicitly that he was right to take it; the lesson is about the negotiation, not the "
                 "decision."],
                ["The company had already budgeted for a negotiation.", "t",
                 "The text says the room left in the offer stays with them if you decline to use it."],
            ],
        }],
        "guiding": [{
            "kind": "guiding",
            "items": [
                "\"Gratitude turned out to be the most expensive emotion of his career.\" Have you ever said yes too "
                "fast &mdash; to a job, a project, a number? What did it cost?",
                "If you had negotiated harder in your last career move, what would be different in your life today? "
                "Use a mixed conditional.",
                "What is YOUR deal breaker &mdash; the one clause you would refuse whatever else they offered? Say "
                "it out loud, in one sentence.",
                "The text says the room in an offer does not disappear if you decline to use it &mdash; it stays "
                "with them. Does that change how you would answer the phone next time?",
            ],
        }],
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"They want you in London in six weeks.\"",
                 "tips": ["My notice period is three months, so six weeks is not possible.",
                          "State the conflict as a fact. Do not apologize for it."]},
                {"situation": "\"The base is competitive. Are you happy?\"",
                 "tips": ["Compensation is not salary. I would want to look at the whole package.",
                          "Never answer the salary question with a yes."]},
                {"situation": "\"You'll forfeit your bonus by leaving in March.\"",
                 "tips": ["Then I am asking for a buyout of what I give up, or a sign-on bonus that covers it.",
                          "Nobody offers what is not requested."]},
                {"situation": "\"Are you willing to relocate?\"",
                 "tips": ["I am considering relocating, and I have decided to negotiate first.",
                          "consider + -ing / decide + to. Never say a bare yes."]},
                {"situation": "\"The non-compete is standard. Is that a problem?\"",
                 "tips": ["Twelve months is my deal breaker.",
                          "If the role did not work out, it would leave me unemployable in my sector."]},
                {"situation": "\"There is another candidate. Do not push too hard.\"",
                 "tips": ["I am committed to negotiating everything else in good faith. But not that.",
                          "Hold the line. Stay warm. Do not fill the silence."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Industry -- as negocia&#231;&#245;es de contrato e sa&#237;da (HBO Max)",
         "Personagens negociando contratos, b&#244;nus e cl&#225;usulas de sa&#237;da &mdash; e quase sempre "
         "aceitando r&#225;pido demais. Connection to Lesson 10: repare em quem nomeia o pr&#243;prio deal breaker e "
         "em quem s&#243; agradece.",
         "Dica: assista com legenda em ingl&#234;s. Anote 3 mixed conditionals e leia em voz alta.",
         "https://www.hbo.com/industry"),
        ("Podcast", "podcast", "HBR / Harvard Business Review -- negocia&#231;&#227;o de ofertas executivas",
         "Como negociar remunera&#231;&#227;o, equity e cl&#225;usulas sem queimar a rela&#231;&#227;o. Connection "
         "to Lesson 10: &#233; o vocabul&#225;rio exato da aula (vesting, non-compete, buyout) na boca de quem "
         "negocia para viver.",
         "Dica: ou&#231;a a 1x. Pare a cada gerund/infinitive que ouvir e diga em voz alta por que &#233; um e "
         "n&#227;o o outro.",
         "https://www.youtube.com/@HarvardBusinessReview"),
        ("YouTube", "youtube", "Wall Street Journal -- carreiras executivas e mobilidade internacional",
         "Reportagens sobre executivos que mudaram de pa&#237;s: o que ganharam, o que perderam, o que negociaram "
         "mal. Connection to Lesson 10: &#233; a sua pr&#243;pria decis&#227;o, contada por quem j&#225; a tomou.",
         "Dica: assista a 0.75x se precisar. Depois grave 60 segundos respondendo: qual &#233; o SEU deal breaker?",
         "https://www.youtube.com/@wsj"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
