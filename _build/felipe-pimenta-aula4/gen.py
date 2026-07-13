#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 4 — Wishes, Regrets, and What Could Be Different.
Gramatica: wish / if only + unreal past (past simple, past perfect, would).
Modelo: LEITURA (aula PAR, REGRA 29) — ic-reading + gist + true/false + discussao.
Callback (REGRA 20): o warm-up retoma os modal perfects e o vocab da aula 3.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 4
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Restructuring", "reorganizing a company, often with job cuts",
     "reestrutura&#231;&#227;o",
     "The restructuring took ninety people out of a team of six hundred."),
    ("To lay off", "to end someone's job because the company needs fewer people",
     "demitir (por corte de quadro)",
     "We laid off ninety people, and I signed every letter."),
    ("Severance", "the money a company pays the people it lets go",
     "verba rescis&#243;ria",
     "I wish we had offered a longer severance package."),
    ("Morale", "how motivated and confident a team feels",
     "moral da equipe",
     "Morale did not fall because of the cuts. It fell because of the silence."),
    ("Attrition", "people leaving the company slowly, over time",
     "rotatividade, perda natural",
     "If only we had managed it through attrition instead of layoffs."),
    ("Workload", "the amount of work one person is carrying",
     "carga de trabalho",
     "The workload of the people who stayed doubled overnight."),
    ("Candid", "honest and direct, even when it is uncomfortable",
     "franco, direto",
     "She was candid with the team, and they never forgot it."),
    ("Trade-off", "what you give up in order to get something else",
     "troca, sacrif&#237;cio necess&#225;rio",
     "Every restructuring is a trade-off between cash and trust."),
    ("To voice a concern", "to say openly that you are worried about something",
     "expressar uma preocupa&#231;&#227;o",
     "Two directors voiced a concern, and I wish I had listened."),
    ("Goodwill", "the trust and credit you have built up with people",
     "boa vontade, cr&#233;dito de confian&#231;a",
     "We spent ten years building goodwill and lost it in one meeting."),
    ("Headwinds", "outside forces that make growth harder",
     "ventos contr&#225;rios",
     "We were facing real headwinds &mdash; but that is not an excuse for how we told them."),
    ("Resentment", "the quiet anger people keep after they feel wronged",
     "ressentimento",
     "Resentment is what silence leaves behind."),
]

PHASES = ["The Room Nobody Wants", "The Language of Loss", "The Letter",
          "The Code", "The Conversation", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Tonight is the most human lesson in this "
    "program. Numbers do not resent you. People do. And there is a grammar for the things you wish you had done "
    "differently.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 4 &middot; Regrets", "The Things You Wish You Had", "Said",
    "Every CFO signs the letter. Very few know how to talk about it afterwards."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 3 ANTES do tema novo (REGRA 20). Peca um modal "
    "perfect sobre a semana dele: 'One thing your team should have done, and one thing they could have done.' "
    "Depois abra o tema: 'Now something you carry: a conversation with a person, not a number.' Deixe falar. ZERO "
    "correcao.",
    "Chapter 1: The Room Nobody Wants",
    "A Conversation You Still", "Carry",
    "Not a deal, not a target. A person, a room, and something you wish you had said differently."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Tres ferramentas, tres trabalhos. O third conditional (aula 2) analisa. "
    "O modal perfect (aula 3) julga. O WISH e a unica que carrega EMOCAO -- e por isso e a unica que funciona quando "
    "voce fala com uma PESSOA, nao com um board. Um CFO que so tem as duas primeiras soa como um relatorio.",
    "Three Tools, Three Jobs", "Analysis, Judgment,", "Regret",
    [("If we had...", "an imaginary past &mdash; analysis (Lesson 2)"),
     ("She should have...", "a verdict on one action (Lesson 3)"),
     ("I wish I had...", "regret &mdash; the only one with a heartbeat")],
    "\"We should have offered better severance\" is a finding. \"I wish we had offered better severance\" is an apology. Only one of them repairs anything."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of a restructuring, a real letter written "
    "by a CEO who got it wrong, and the grammar of regret.' Antecipe: o role-play final e a conversa que ele "
    "provavelmente vai ter de verdade um dia.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "severance, morale, attrition, goodwill..."),
     ("2. The Letter", "read a restructuring done badly &mdash; and one done right"),
     ("3. The Code", "I wish I had... &middot; If only we had...")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. Six of them are about money. Six of them are "
    "about what money cannot fix.' Passe ao proximo.",
    "Chapter 2: The Language of Loss", "The Words of a", "Restructuring",
    "12 words &mdash; half spreadsheet, half human.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'attrition': 'If ten "
    "people resign on their own over a year, is that attrition or a layoff? (Attrition.)' CCQ 'severance': 'Is "
    "severance a salary or a payment when you leave? (When you leave.)' CCQ 'morale': 'Can morale fall even when "
    "nobody is fired? (Yes -- silence is enough.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Goodwill' e 'resentment' sao o coracao da aula. "
    "CCQ 'goodwill': 'Is goodwill something you buy, or something you build? (Build -- over years.)' CCQ "
    "'trade-off': 'In a restructuring, what is the trade-off? (Cash now, trust later.)' CCQ 'candid': 'Is being "
    "candid the same as being harsh? (No -- candid is honest AND respectful.)'",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'severance' (SEV-er-ance, 3 silabas), 'morale' "
    "(mo-RAL -- stress na 2a; o brasileiro diz MO-ral e vira outra palavra), 'attrition' (a-TRISH-un), 'resentment' "
    "(re-ZENT-ment). 'Morale' errado e o que mais confunde o interlocutor.",
    ["Severance", "Morale", "Attrition", "Resentment", "Goodwill"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas sao frases de uma reestruturacao real.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"", "Morale", " did not fall because of the cuts. It fell because of the silence.\""),
     ("\"We spent ten years building ", "goodwill", " and lost it in one meeting.\""),
     ("\"The ", "workload", " of the people who stayed doubled overnight.\""),
     ("\"Two directors ", "voiced a concern", ", and I wish I had listened.\""),
     ("\"Every restructuring is a ", "trade-off", " between cash and trust.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao leitura (1 min):</strong> Diga: 'Two letters. Same week, same industry, same number of "
    "people. One of them destroyed a company culture. Read them like an employee, not like a CFO.' Passe ao "
    "proximo.",
    "Chapter 3: The Letter", "Two Letters, One", "Restructuring",
    "Read them the way the team read them.", L.IMG['context']))

S.append(L.s_blocks(
    11, 3,
    "<strong>Leitura + gist (7 min):</strong> Felipe le em SILENCIO primeiro (2-3 min), sem dicionario. Depois "
    "pergunte a ideia central ANTES de mostrar as alternativas. Pergunta-chave para provocar: 'Both companies cut "
    "ninety people. Why did only one of them lose its best engineers three months later?'",
    "Read for the Main Idea", "The Letter That", "Broke a Company",
    ["reading", "gist"]))

S.append(L.s_blocks(
    12, 3,
    "<strong>True or False (5 min):</strong> Felipe responde ORALMENTE e JUSTIFICA com o trecho do texto antes de "
    "clicar. A justificativa e o exercicio -- e ela que forca frase completa sob pressao.",
    "Check Understanding", "True or", "False?", ["tf"]))

S.append(L.s_blocks(
    13, 3,
    "<strong>Discussao (6 min):</strong> Aqui o Felipe FALA -- e o tema e pessoal. Ele ja demitiu gente. Nao "
    "corrija durante; anote. Se ele trocar para o portugues, aponte para a tela e espere. Este e o slide em que a "
    "aula vira conversa de verdade.",
    "Discuss", "Talk It", "Through", ["guiding"]))

S.append(L.s_chapter(
    14, 4,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. One word -- wish -- and a verb tense that "
    "lies on purpose.' Passe ao proximo.",
    "Chapter 4: The Code", "The Grammar of", "Regret",
    "I wish I had... &middot; If only we had...", L.IMG['code']))

S.append(L.s_discovery(
    15, 4,
    "<strong>Grammar discovery (7 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos. Pergunte: 'Two of "
    "these are about NOW and two are about the PAST. Which is which -- and how do you know?' Espere ele notar que o "
    "tempo verbal 'anda para tras' um passo. So entao clique 'Reveal the Rule'. CCQ: 'I wish I HAD more time -- do "
    "I have time now? (No.) I wish I HAD TOLD them -- did I tell them? (No.) I wish they WOULD tell us -- am I "
    "talking about the past or complaining about a habit? (Complaining.)'",
    [("\"I wish I <span style=\"color:#b45309;font-weight:700\">had</span> more time before the announcement.\"",
      "I wish I had more time before the announcement."),
     ("\"I wish I <span style=\"color:#15803d;font-weight:700\">had listened</span> to the two directors.\"",
      "I wish I had listened to the two directors."),
     ("\"If only we <span style=\"color:#15803d;font-weight:700\">had offered</span> a longer severance package.\"",
      "If only we had offered a longer severance package."),
     ("\"I wish the board <span style=\"color:#1d4ed8;font-weight:700\">would decide</span> faster.\"",
      "I wish the board would decide faster.")],
    "Two are about <span style=\"color:#b45309;font-weight:700\">now</span>, two are about the "
    "<span style=\"color:#15803d;font-weight:700\">past</span>, and one is a "
    "<span style=\"color:#1d4ed8;font-weight:700\">complaint</span>. The tense always steps one pace backwards. Why?",
    [("wish + past simple",
      "A regret about NOW. The reality is the opposite of what you say.",
      "I wish I <strong>had</strong> more time. (I don't.)"),
     ("wish + past perfect",
      "A regret about the PAST. Your main tool tonight.",
      "I wish I <strong>had listened</strong>. (I didn't.)"),
     ("wish + would + verb",
      "A complaint about someone else's behavior &mdash; never about yourself.",
      "I wish the board <strong>would decide</strong> faster."),
     ("If only...",
      "The same structures, but stronger and more emotional. Use it once, not five times.",
      "<strong>If only we had</strong> managed it through attrition."),
     ("wish + could",
      "A regret about ability, present or past.",
      "I wish I <strong>could have protected</strong> that team."),
    ],
    "The tense lies on purpose: it steps back one pace to signal \"this is not real.\" That is why it is called the "
    "<strong>unreal past</strong> &mdash; the same trick behind <em>if I were you</em>.",
    "rule4"))

S.append(L.s_mistake(
    16, 4,
    "<strong>Common mistake (4 min):</strong> O erro numero 1: o brasileiro diz 'I wish I would have listened' -- "
    "porque em portugues 'eu queria ter escutado' parece pedir um condicional. Em ingles, WISH + WOULD nunca se "
    "refere a voce mesmo: e so para reclamar do OUTRO. Sobre si mesmo e sempre HAD + participio. Segundo erro: "
    "'I wish I have' -- nunca presente depois de wish. Peca que ele leia as certas DUAS vezes.",
    [("I wish I would have listened to the two directors.",
      "I wish I had listened to the two directors."),
     ("I wish I have more time before the announcement.",
      "I wish I had more time before the announcement."),
     ("If only we would offer a longer severance package.",
      "If only we had offered a longer severance package.")],
    "After <strong>wish</strong>, the tense always steps BACK: <em>had</em> for now, <em>had + participle</em> for "
    "the past. <strong>wish + would</strong> exists, but only to complain about someone else &mdash; never about "
    "yourself."))

S.append(L.s_fill(
    17, 4,
    "<strong>Grammar practice (4 min):</strong> Leia cada frase. Felipe escolhe a forma ORALMENTE antes de clicar. "
    "Se travar, pergunte: 'Now, or the past? And is it about you, or about them?'",
    "Practice", "Complete the", "Sentence", "Say it first, then click to check",
    [("\"I wish I ", "had listened", " to the two directors who voiced a concern.\""),
     ("\"If only we ", "had managed", " it through attrition instead of layoffs.\""),
     ("\"I wish I ", "had", " more time before the announcement &mdash; but I don't.\""),
     ("\"I wish the board ", "would decide", " faster. It takes them months.\""),
     ("\"I wish I ", "could have protected", " that team, and I couldn't.\"")]))

S.append(L.s_chapter(
    18, 5,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Nadia Kovac runs People. She was in the room when you signed "
    "the letters. She has been waiting three months to say this.' Passe ao proximo.",
    "Chapter 5: The Conversation", "Your Head of People Wants a", "Word",
    "Three months after the cuts", L.IMG['turn']))

S.append(L.s_dialogue(
    19, 5,
    "<strong>Dialogo (7 min):</strong> Voce e a Nadia. Clique 'Next Line' a cada fala. Este dialogo NAO e uma "
    "reuniao de numeros -- e uma conversa entre dois adultos que erraram juntos. Peca que o Felipe fale a fala dele "
    "ANTES do audio. Observe: ele consegue dizer 'I wish' sem soar fraco? Esse e o teste.",
    "What We Wish We Had", "Done",
    [("nadia", "N", "ellen",
      "Felipe, the numbers recovered. But I lost four of my best people this quarter, and none of them were on the "
      "layoff list.",
      "Felipe, the numbers recovered. But I lost four of my best people this quarter, and none of them were on the "
      "layoff list."),
     ("felipe", "F", "arthur",
      "I know. And I wish I had listened to you in March, when you told me the "
      "<span class=\"vocab-highlight\">morale</span> problem would come from the silence, not from the cuts.",
      "I know. And I wish I had listened to you in March, when you told me the morale problem would come from the "
      "silence, not from the cuts."),
     ("nadia", "N", "ellen",
      "It was not only the silence. The <span class=\"vocab-highlight\">severance</span> was legal, but it was thin. "
      "People talk.",
      "It was not only the silence. The severance was legal, but it was thin. People talk."),
     ("felipe", "F", "arthur",
      "If only we had offered three months instead of one. We had the cash. That was a "
      "<span class=\"vocab-highlight\">trade-off</span> I got wrong &mdash; I protected the runway and I spent ten "
      "years of <span class=\"vocab-highlight\">goodwill</span> to do it.",
      "If only we had offered three months instead of one. We had the cash. That was a trade-off I got wrong. I "
      "protected the runway and I spent ten years of goodwill to do it."),
     ("nadia", "N", "ellen",
      "That is the most <span class=\"vocab-highlight\">candid</span> thing you have said all year. So what now?",
      "That is the most candid thing you have said all year. So what now?"),
     ("felipe", "F", "arthur",
      "Now I say this out loud, to the whole company, in exactly these words. I wish we had told them earlier and "
      "paid them better. And then I fix the <span class=\"vocab-highlight\">workload</span> of the people who "
      "stayed, because that is the part I can still change.",
      "Now I say this out loud, to the whole company, in exactly these words. I wish we had told them earlier and "
      "paid them better. And then I fix the workload of the people who stayed, because that is the part I can still "
      "change.")]))

S.append(L.s_comprehension(
    20, 5,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a NADIA, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Nadia",
    [("What is Nadia's problem, three months after the cuts?",
      "She lost four of her best people &mdash; and none of them were on the layoff list."),
     ("What does she say about the severance?",
      "It was legal, but thin &mdash; and people talk."),
     ("How does she react to Felipe's admission?",
      "She calls it the most candid thing he has said all year, and asks what he will do now.")]))

S.append(L.s_listening(
    21, 5,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CFO speaks at a conference about the restructuring she got "
    "wrong. Just listen -- no text.' Toque SEM texto, 2 vezes. Peca que ele CONTE quantos 'I wish' ouviu. Ouvido "
    "antes de boca.",
    1, "Listening", "The CFO Who Got It", "Wrong",
    "A conference talk nobody expected her to give. Sound first &mdash; no text.",
    "a4_listening_cfo.mp3", SLUG,
    [("What does she say she wishes she had done differently?",
      "Told people earlier, and offered a longer severance package &mdash; they had the cash."),
     ("Why does she say morale fell?",
      "Because of the silence, not because of the cuts themselves."),
     ("What did the company lose that it had spent years building?",
      "Goodwill &mdash; and it cost them their best engineers, who were never on the list.")]))

S.append(L.s_listening(
    22, 5,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now the same week, from the other side of the table: a head of "
    "People who did it well.' Toque 2 vezes. Depois pergunte: 'What did she do that the first company did not?' O "
    "contraste dos DOIS audios e o argumento pedagogico da aula.",
    2, "Listening 2", "The One Who Did It", "Right",
    "The same cuts, a very different room. Sound first &mdash; no text.",
    "a4_listening_hr.mp3", SLUG,
    [("When did she tell the team the restructuring was coming?",
      "Six weeks before &mdash; she refused to let people find out on the day."),
     ("What did she do about the workload of the people who stayed?",
      "She cut projects, not just people &mdash; so the remaining workload was survivable."),
     ("What does she say she still wishes she had done?",
      "Fought harder for a longer severance package &mdash; she says she is not proud of that one.")]))

S.append(L.s_chapter(
    23, 6,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train the hardest sentence in the language: the one "
    "where you admit something to a person who was hurt by it.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Say It to Their", "Face",
    "Detective &middot; The Letter &middot; The Room", L.IMG['practice']))

S.append(L.s_error(
    24, 6,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. As duas primeiras "
    "sao O erro (wish + would have / wish + presente). Se ele achar sozinho, a regra pegou.",
    [("I wish I would have listened to the two directors.",
      "I wish I had listened to the two directors."),
     ("I wish I have more time before the announcement.",
      "I wish I had more time before the announcement."),
     ("If only we would offer a longer severance package.",
      "If only we had offered a longer severance package."),
     ("I wish the board decides faster. It takes them months.",
      "I wish the board would decide faster. It takes them months.")]))

S.append(L.s_artifact(
    25, 6,
    "<strong>Artefato (5 min):</strong> Este e o memo REAL de uma reestruturacao -- frio, correto, e devastador. "
    "Peca que o Felipe leia em voz alta, e depois REESCREVA cada linha em voz alta com 'I wish' / 'If only'. E o "
    "exercicio mais duro da aula: transformar um documento juridico numa frase humana.",
    "The Artifact", "The Restructuring", "Memo",
    "INTERNAL MEMO", "Confidential &middot; People &amp; Finance",
    [("Signed by", "Felipe Pimenta, CFO"),
     ("Roles eliminated", "90 of 600 (15%)"),
     ("Notice given to staff", "Same day"),
     ("Severance offered", "1 month (legal minimum)"),
     ("Concerns raised beforehand", "2 directors &mdash; not actioned"),
     ("Regretted attrition since", "4 senior engineers (not on list)"),
     ("Cash preserved", "USD 4.2m")],
    [("Rewrite \"Notice given: same day\" with I wish.",
      "\"I wish we had told them weeks earlier, not on the day.\""),
     ("Rewrite \"Severance: legal minimum\" with If only.",
      "\"If only we had offered three months instead of one. We had the cash.\""),
     ("Now the hardest line: \"Concerns raised &mdash; not actioned.\"",
      "\"I wish I had listened to the two directors who voiced a concern.\"")]))

S.append(L.s_quickfire(
    26, 6,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO. Exija a frase "
    "inteira com wish/if only. Este quick fire e emocionalmente pesado de proposito: e exatamente sob esse tipo de "
    "pressao que ele fragmenta e troca para o portugues.",
    "They Ask. You", "Answer."))

S.append(L.s_building(
    27, 6,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords. Felipe monta a frase COMPLETA em voz alta, "
    "depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes.",
    [("I / wish / I / listen / to the two directors (past regret)",
      "I wish I had listened to the two directors."),
     ("if only / we / offer / three months of severance (past regret, stronger)",
      "If only we had offered three months of severance."),
     ("I / wish / I / have / more time before the announcement (regret about NOW)",
      "I wish I had more time before the announcement."),
     ("I / wish / the board / decide faster (complaint about THEM)",
      "I wish the board would decide faster."),
     ("I / wish / I / can / protect that team (regret about ability, past)",
      "I wish I could have protected that team.")]))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Nadia. Abra com: 'I lost four good people this quarter, and "
    "none of them were on your list.' Felipe usa as keywords. Deixe conduzir. Observe se ele consegue dizer 'I wish' "
    "sem se defender na frase seguinte -- a defesa e o reflexo que mata a conversa.",
    "The Conversation with", "Nadia",
    "Your Head of People tells you the company is bleeding talent that was never on the layoff list. Do not defend "
    "the decision. Name what you wish you had done, own the trade-off you got wrong, and say what you will change "
    "for the people who stayed.",
    ["I wish I had listened when...", "If only we had offered...",
     "That was a trade-off I got wrong.", "What I can still change is..."]))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. Agora voce e um dos NOVENTA -- alguem que foi "
    "demitido e que encontra o Felipe num evento, seis meses depois. Nao seja agressivo: seja educado e triste. E "
    "MUITO mais dificil. O Felipe tem de ser candid sem se desculpar em excesso e sem esconder atras do 'a empresa "
    "decidiu'.",
    "The Person You Laid", "Off",
    "Six months later, at a conference, you meet someone you laid off. She is polite. She asks, quietly: \"Was there "
    "really no other way?\" Answer her honestly, as a person &mdash; not as a company.",
    ["Honestly, I wish we had...", "There was a trade-off, and I...",
     "What I got wrong was...", "You deserved to hear it earlier."],
    tint='.12'))

S.append(L.s_roleplay(
    30, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: o discurso para a empresa inteira, ZERO pistas. NAO "
    "interrompa, NAO corrija. Cronometre 3 min. Diga antes: 'This is the speech you owe them. Say it the way you "
    "would actually want to say it.' CELEBRE muito: ele acabou de fazer em ingles a conversa mais dificil da vida "
    "corporativa.",
    "The Speech You", "Owe Them",
    "Address the whole company, three months after the restructuring. Be candid: say what you wish you had done "
    "differently, name the trade-off you got wrong, do not blame the board or the headwinds, and finish with the one "
    "thing you can still change &mdash; the workload of the people who stayed.",
    []))

S.append(L.s_chapter(
    31, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'You just apologized in English without losing an inch of "
    "authority. Most executives cannot do that in their own language.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You Were", "Candid",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("I wish I had listened to the people who voiced a concern.",
     "Eu queria ter escutado quem expressou uma preocupa&#231;&#227;o."),
    ("If only we had offered a longer severance package.",
     "Se ao menos tiv&#233;ssemos oferecido uma verba rescis&#243;ria maior."),
    ("That was a trade-off I got wrong, and I own it.",
     "Foi uma troca que eu errei, e eu assumo."),
    ("Morale did not fall because of the cuts. It fell because of the silence.",
     "A moral n&#227;o caiu por causa dos cortes. Caiu por causa do sil&#234;ncio."),
    ("What I can still change is the workload of the people who stayed.",
     "O que eu ainda posso mudar &#233; a carga de trabalho de quem ficou."),
]

S.append(L.s_survival(
    32, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Sao as 5 "
    "frases de uma conversa dificil com PESSOAS -- e valem inteiras numa entrevista quando perguntarem sobre "
    "lideranca em crise.",
    "Five Phrases for the", "Hard Conversation",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    33, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 4 no passaporte (registra no Supabase).",
    N,
    ["I can use I wish + past perfect to express regret about the past.",
     "I can use I wish + past simple for a regret about now.",
     "I can use I wish + would only to complain about someone else, never about myself.",
     "I can be candid about a decision I got wrong without losing authority.",
     "I know my words: restructuring, severance, morale, attrition, goodwill, trade-off."]))

S.append(L.s_complete(
    34, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 4 complete, Felipe. You earned your Candor Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) escrever 5 frases com 'I wish' sobre decisoes REAIS de "
    "lideranca dele -- 3 sobre o passado, 1 sobre agora, 1 reclamando do board -- e gravar lendo; (2) reler o memo "
    "do artefato e gravar a versao humana dele, em 60 segundos. Proxima aula: Making Your Case -- board updates e "
    "reported speech.",
    N, "Candor Badge", "You said the hardest sentence in the language. In English.",
    "Making Your Case -- Board Updates"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Wishes, Regrets, and What Could Be Different',
    'short_title': 'Wishes, Regrets, and What Could Be Different',
    'menu_desc': 'A restructuring told two ways + wish / if only',
    'desc': ('Falar de arrependimento com PESSOAS &mdash; n&#227;o com n&#250;meros. Uma reestrutura&#231;&#227;o '
             'contada de dois jeitos. Key words: restructuring, to lay off, severance, morale, attrition, workload, '
             'candid, trade-off, to voice a concern, goodwill, headwinds, resentment. Structures: wish / if only + '
             'unreal past &mdash; wish + past simple (agora), wish + past perfect (passado), wish + would '
             '(reclama&#231;&#227;o sobre o outro).'),
    'hub_img': 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'nadia': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. Metade &#233; planilha, metade &#233; o que a planilha '
                    'n&#227;o resolve.'),

    'context_text': (
        'The <strong>restructuring</strong> took ninety people out of a team of six hundred. Felipe signed every '
        'letter. The company <strong>laid off</strong> the ninety on a Tuesday morning, with no warning, and the '
        '<strong>severance</strong> was one month &mdash; the legal minimum. Two directors had '
        '<strong>voiced a concern</strong> in March, and nobody actioned it. '
        '<strong>I wish I had listened to them</strong>, Felipe says now. <strong>If only we had offered</strong> '
        'three months instead of one: the cash was there. It was a <strong>trade-off</strong>, and he got it wrong '
        '&mdash; he protected the runway and spent ten years of <strong>goodwill</strong> to do it. '
        '<strong>Morale</strong> did not fall because of the cuts. It fell because of the silence. Three months '
        'later, four senior engineers resigned. None of them had been on the list. That is '
        '<strong>attrition</strong>, and it is what <strong>resentment</strong> leaves behind. The '
        '<strong>workload</strong> of the people who stayed had doubled overnight, and nobody had said a word about '
        'it. The <strong>headwinds</strong> were real. They are still not an excuse. Today Felipe is '
        '<strong>candid</strong> about all of it, in public, because he has learned that '
        '<strong>I wish we had told them earlier</strong> repairs more than any memo ever did.'),

    'context_quiz': [
        ("\"I wish I had listened to them.\" O que realmente aconteceu?",
         [("Ele escutou os dois diretores.", False),
          ("Ele N&#195;O escutou &mdash; e se arrepende disso.", True),
          ("Ele vai escutar os dois diretores na pr&#243;xima vez.", False)]),
        ("Por que o texto diz que a moral caiu pelo sil&#234;ncio, e n&#227;o pelos cortes?",
         [("Porque ningu&#234;m se importa com demiss&#245;es.", False),
          ("Porque as pessoas aceitam a decis&#227;o dif&#237;cil, mas n&#227;o aceitam n&#227;o serem avisadas nem "
           "tratadas com franqueza.", True),
          ("Porque os cortes foram pequenos demais para importar.", False)]),
        ("Which sentence is correct English?",
         [("I wish I would have listened to the two directors.", False),
          ("I wish I had listened to the two directors.", True),
          ("I wish I have listened to the two directors.", False)]),
    ],

    'tip_title': 'Wish / If Only + Unreal Past',
    'tip_intro': ('Como falar de arrependimento &mdash; a &#250;nica gram&#225;tica desta trilha que carrega '
                  'emo&#231;&#227;o (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("wish + past simple",
         "Arrependimento sobre AGORA. A realidade &#233; o oposto do que voc&#234; diz. A regret about now.",
         "I wish I <strong>had</strong> more time. (I don't.)"),
        ("wish + past perfect",
         "Arrependimento sobre o PASSADO. A sua ferramenta principal. A regret about the past.",
         "I wish I <strong>had listened</strong>. (I didn't.)"),
        ("wish + would + verbo",
         "Reclama&#231;&#227;o sobre o comportamento do OUTRO. NUNCA sobre voc&#234; mesmo. A complaint about someone "
         "else.",
         "I wish the board <strong>would decide</strong> faster."),
        ("wish + could (have)",
         "Arrependimento sobre CAPACIDADE. A regret about ability.",
         "I wish I <strong>could have protected</strong> that team."),
        ("If only...",
         "As mesmas estruturas, mais fortes e mais emocionais. Use UMA vez, n&#227;o cinco.",
         "<strong>If only we had offered</strong> three months."),
        ("Por que o tempo 'anda para tr&#225;s'",
         "O passado aqui n&#227;o &#233; tempo: &#233; DIST&#194;NCIA da realidade. &#201; o <em>unreal past</em> &mdash; "
         "o mesmo truque de <em>if I were you</em>.",
         "I wish I <strong>were</strong> in that meeting."),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (o erro n&#186; 1 do brasileiro):</strong> "eu queria ter escutado" vira, '
                 'quase sempre, <em>"I wish I would have listened"</em> &mdash; e isso N&#195;O existe. Sobre '
                 'VOC&#202; MESMO &#233; sempre <strong>wish + had + partic&#237;pio</strong>: "I wish I '
                 '<strong>had listened</strong>". O <strong>wish + would</strong> existe, mas s&#243; para reclamar '
                 'do OUTRO: "I wish the board would decide faster". E nunca use presente depois de wish: "I wish I '
                 '<em>have</em>" est&#225; sempre errado.'),

    'blanks': [
        ("I wish I", "had listened", "Dica: arrependimento sobre o passado &mdash; had + partic&#237;pio",
         "I wish I had listened to the two directors.", "to the two directors."),
        ("If only we", "had offered", "Dica: arrependimento sobre o passado, mais forte",
         "If only we had offered a longer severance package.", "a longer severance package."),
        ("I wish I", "had", "Dica: arrependimento sobre AGORA &mdash; past simple depois de wish",
         "I wish I had more time before the announcement.", "more time before the announcement."),
        ("I wish the board", "would decide", "Dica: reclama&#231;&#227;o sobre o OUTRO &mdash; wish + would",
         "I wish the board would decide faster.", "faster."),
        ("I wish I", "could have protected", "Dica: arrependimento sobre capacidade, no passado",
         "I wish I could have protected that team.", "that team."),
        ("Morale fell because of the silence, and that is what", "resentment",
         "Dica: a raiva silenciosa que fica depois",
         "Morale fell because of the silence, and that is what resentment leaves behind.",
         "leaves behind."),
    ],

    'order_title': 'Put the Difficult Conversation in Order',
    'order_intro': ('Coloque as etapas de uma conversa franca sobre um erro de lideran&#231;a na ordem correta. '
                    'Inverter duas delas destr&#243;i a conversa.'),
    'order': [
        (3, "Name the trade-off you got wrong, without blaming the board or the headwinds."),
        (5, "Commit to the one thing you can still change &mdash; and be specific."),
        (1, "Listen first. Let them tell you what it cost, without interrupting."),
        (4, "Ask what would have made the difference for them."),
        (2, "Say what you wish you had done differently &mdash; and stop talking."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases da '
                     'conversa mais dif&#237;cil da vida corporativa.'),
    'speech': SURVIVAL,

    'quiz': [
        ("Your Head of People says you lost four good people. You answer:",
         [("\"I wish I would have listened to you in March.\"", False),
          ("\"I wish I had listened to you in March.\"", True),
          ("\"I wish I have listened to you in March.\"", False)]),
        ("You want to say the severance was too small &mdash; and you had the cash:",
         [("\"If only we would offer three months instead of one.\"", False),
          ("\"If only we had offered three months instead of one.\"", True),
          ("\"If only we offer three months instead of one.\"", False)]),
        ("The board takes months to approve anything, and it frustrates you. You say:",
         [("\"I wish the board would decide faster.\"", True),
          ("\"I wish the board had decided faster.\" (about their general habit)", False),
          ("\"I wish the board decides faster.\"", False)]),
        ("Someone you laid off asks: \"Was there really no other way?\" The most senior answer is:",
         [("\"The board made the decision. It wasn't really my call.\"", False),
          ("\"There was a trade-off, and I got it wrong. I wish we had told you earlier and paid you better.\"", True),
          ("\"I'm so sorry, it was terrible, I felt awful for weeks.\"", False)]),
        ("You want to admit a regret WITHOUT sounding weak in front of the board:",
         [("\"I feel really bad about what happened to those people.\"", False),
          ("\"I wish we had managed it through attrition. That was a trade-off I got wrong, and here is what "
            "changes.\"", True),
          ("\"Mistakes were made, but the headwinds were very strong.\"", False)]),
    ],

    'think': ("Three months after a restructuring, you address the whole company. Speak for 2-3 minutes. Use "
              "\"I wish + past perfect\" at least twice and \"If only\" once. Name the trade-off you got wrong. Do "
              "NOT blame the board or the headwinds. Finish with the one concrete thing you can still change for the "
              "people who stayed. Be candid &mdash; and do not apologize more than once."),

    'listenings': [
        {"file": "a4_listening_cfo.mp3", "voice": "ellen",
         "text": ("I was asked to talk about a success tonight, and I am going to talk about a failure instead, "
                  "because it is the more useful story. Two years ago we restructured. Ninety people out of six "
                  "hundred. We told them on a Tuesday morning with no warning, and we paid the legal minimum: one "
                  "month. I want to be precise about what went wrong, because it was not the decision. The company "
                  "genuinely could not carry that cost. What went wrong was everything around it. I wish we had "
                  "told people earlier. We had known for six weeks. And I wish we had offered three months of "
                  "severance instead of one, because we had the cash, and we chose the runway over the people. That "
                  "was a trade-off, and I got it wrong. Here is what it cost us. Morale did not fall because of the "
                  "cuts. It fell because of the silence. Three months later, four of our best engineers resigned, "
                  "and not one of them had been on the list. We spent ten years building goodwill and we spent it "
                  "all in a single morning. If only we had been honest six weeks earlier, I believe we would still "
                  "have those engineers today.")},
        {"file": "a4_listening_hr.mp3", "voice": "arthur",
         "text": ("We cut the same number of roles that year, and I want to tell you what we did differently, "
                  "because none of it was clever. It was just early and it was just honest. Six weeks before the "
                  "announcement, we told the whole company that a restructuring was coming. Not who, but that. "
                  "People hated it. They also respected it, and nobody found out on the day from a calendar invite. "
                  "The second thing we did was cut projects, not only people. If you remove ninety people and leave "
                  "the same amount of work behind, the workload of everyone who stays simply doubles, and you lose "
                  "them next. So we killed four initiatives publicly and we said which ones. The third thing is the "
                  "one I am not proud of. Our severance was two months, and I wish I had fought harder for three. I "
                  "argued in the room, and I lost, and I let it go. If only I had pushed once more. We kept our "
                  "people. We kept most of our goodwill. But that one still sits with me.")},
    ],

    'inclass_blocks': {
        "reading": [{
            "kind": "reading",
            "rtitle": "Two Letters, One Restructuring",
            "paras": [
                ("Two companies in the same industry cut ninety roles in the same month. On paper, the decisions "
                 "were identical: the headwinds were real, the cash was tight, and the cuts were unavoidable. A year "
                 "later, one of them had recovered. The other had lost half of its senior engineers &mdash; none of "
                 "whom had been on the layoff list."),
                ("The first company told nobody. Staff learned on a Tuesday morning from a calendar invite. The "
                 "severance was one month, the legal minimum, even though the company had the cash to pay three. Two "
                 "directors had voiced a concern weeks earlier; nothing was actioned. The CFO later said the "
                 "sentence that mattered: \"Morale did not fall because of the cuts. It fell because of the "
                 "silence.\""),
                ("The second company announced six weeks in advance that a restructuring was coming, without naming "
                 "anyone. People hated the six weeks. They also respected them. Crucially, that company cut "
                 "projects as well as people: four initiatives were killed in public, so that the workload of those "
                 "who stayed did not simply double overnight. Its severance was two months &mdash; still not "
                 "generous, and its head of People says openly that she wishes she had fought harder for three."),
                ("The lesson is not that layoffs can be made painless. They cannot. It is that goodwill, built over "
                 "a decade, can be spent in a single morning, and that resentment is what silence leaves behind. "
                 "The trade-off is never simply cash against jobs. It is cash against trust &mdash; and trust, "
                 "unlike cash, does not appear on any balance sheet until the day it is gone."),
            ],
            "source": "Case study &mdash; Leadership under pressure",
        }],
        "gist": [{
            "kind": "gist",
            "prompt": "What is the best one-line summary of this text?",
            "choices": [
                ["a", "Layoffs are always wrong and companies should avoid them at any cost.", False],
                ["b", "The two companies made the same decision; what separated them was warning, honesty and "
                      "cutting projects as well as people &mdash; silence, not the cuts, destroys trust.", True],
                ["c", "The first company failed because it cut too many people, and the second cut fewer.", False],
            ],
        }],
        "tf": [{
            "kind": "tf",
            "items": [
                ["The two companies cut a different number of roles.", "f",
                 "Both cut ninety roles in the same month; on paper the decisions were identical."],
                ["The first company could not afford a bigger severance package.", "f",
                 "It paid the legal minimum of one month even though it had the cash to pay three."],
                ["The second company warned staff before naming anyone.", "t",
                 "It announced six weeks in advance that a restructuring was coming, without naming individuals."],
                ["The second company cut projects as well as people.", "t",
                 "Four initiatives were killed in public so the remaining workload would not simply double."],
                ["The head of People at the second company is fully satisfied with what she did.", "f",
                 "She says openly that she wishes she had fought harder for a three-month severance."],
            ],
        }],
        "guiding": [{
            "kind": "guiding",
            "items": [
                "\"Morale did not fall because of the cuts. It fell because of the silence.\" Have you seen this "
                "happen &mdash; in your company or someone else's? Tell the story.",
                "The second company gave six weeks of warning, and people hated it. Would you have done that? What "
                "would it have cost you?",
                "Think of a hard decision you signed off on. What do you wish you had done differently &mdash; and "
                "what stopped you at the time?",
                "The text says trust does not appear on the balance sheet until the day it is gone. As a CFO, how "
                "would you argue for spending cash to protect it?",
            ],
        }],
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Was there really no other way?\"",
                 "tips": ["Honestly, I wish we had managed it through attrition.",
                          "There was a trade-off, and I got it wrong.",
                          "Do not hide behind \"the board decided\"."]},
                {"situation": "\"Why did nobody tell us it was coming?\"",
                 "tips": ["I wish we had told you six weeks earlier. We knew.",
                          "Own the silence. It is the part people never forgive."]},
                {"situation": "\"The severance was the legal minimum. Why?\"",
                 "tips": ["If only we had offered three months instead of one.",
                          "We had the cash. I chose the runway, and that was the wrong call."]},
                {"situation": "\"Two directors warned you in March. What happened?\"",
                 "tips": ["I wish I had listened to them.",
                          "One sentence. Do not explain it away."]},
                {"situation": "\"Those of us who stayed are doing double the work.\"",
                 "tips": ["That is the part I can still change.",
                          "We are cutting four projects, not just people."]},
                {"situation": "\"In an interview: tell me about a leadership decision you regret.\"",
                 "tips": ["Two years ago I signed off on a restructuring...",
                          "I wish we had told them earlier and paid them better.",
                          "Finish with what you changed &mdash; never with the apology."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Industry -- Season 2 (HBO Max)",
         "A temporada em que os cortes chegam &#224; mesa e cada personagem descobre o que vale a pena dizer em voz "
         "alta. Connection to Lesson 4: repare em quem &#233; <em>candid</em> e quem se esconde atr&#225;s do "
         "processo &mdash; e no pre&#231;o que cada um paga.",
         "Dica: assista com legenda em ingl&#234;s. Anote 3 frases com <em>wish</em> ou <em>if only</em> e leia em "
         "voz alta.",
         "https://www.hbo.com/industry"),
        ("Podcast", "podcast", "Planet Money (NPR) -- epis&#243;dios sobre layoffs e o custo humano das decis&#245;es",
         "Economia contada como hist&#243;ria humana, no ingl&#234;s mais claro que existe. Connection to Lesson 4: "
         "&#233; o vocabul&#225;rio de reestrutura&#231;&#227;o (severance, attrition, morale) na boca de quem viveu.",
         "Dica: ou&#231;a a 1x. Pare quando ouvir <em>I wish</em> e repita a frase inteira em voz alta.",
         "https://www.npr.org/sections/money/"),
        ("YouTube", "youtube", "TED -- Brené Brown e a coragem de conversas dif&#237;ceis",
         "Palestras sobre vulnerabilidade e lideran&#231;a: exatamente a habilidade que esta aula treina em "
         "ingl&#234;s. Connection to Lesson 4: ser <em>candid</em> sem perder autoridade &#233; uma t&#233;cnica, "
         "n&#227;o um tra&#231;o de personalidade.",
         "Dica: assista a 0.75x se precisar. Anote como ela admite erro SEM se desculpar mais de uma vez.",
         "https://www.youtube.com/@TED"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
