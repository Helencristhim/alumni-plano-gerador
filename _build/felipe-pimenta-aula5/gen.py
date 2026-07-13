#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 5 — Making Your Case (Board Updates & Investor Communications).
Gramatica: reported speech (backshift, say/tell, reporting verbs, perguntas indiretas).
Modelo: PADRAO-FALA (aula IMPAR, REGRA 29) — dialogo line-by-line + role-play.
Callback (REGRA 20): o warm-up retoma wish/if only e o vocab da aula 4.

Desenho pedagogico: o Listening 1 traz as palavras DIRETAS da investidora; o dialogo
seguinte e o Felipe REPORTANDO essas mesmas palavras a CEO. O aluno ouve a fonte e
produz o report — reported speech deixa de ser exercicio e vira tarefa.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 5
SLUG = 'felipe-pimenta'

VOCAB = [
    ("To disclose", "to make information official, on the record",
     "divulgar oficialmente",
     "She asked whether we had disclosed the covenant breach."),
    ("Guidance", "the forecast a company officially gives the market",
     "proje&#231;&#227;o oficial ao mercado",
     "The CEO said that we would raise our guidance for the year."),
    ("Covenant", "a promise inside a loan contract that you must not break",
     "cl&#225;usula contratual, covenant",
     "We are two points away from breaking the covenant."),
    ("Dilution", "the fall in your ownership when new shares are issued",
     "dilui&#231;&#227;o",
     "He warned that the round would cause serious dilution."),
    ("Term sheet", "the summary of the key terms of an investment",
     "term sheet, memorando de termos",
     "She told me the term sheet would arrive on Friday."),
    ("Cap table", "the list of who owns what in the company",
     "quadro societ&#225;rio, cap table",
     "The cap table gets messy after three rounds."),
    ("To raise capital", "to get new money from investors",
     "captar recursos",
     "They asked how much capital we intended to raise."),
    ("To reiterate", "to say something again, deliberately, so it sticks",
     "reiterar",
     "I reiterated that the numbers had been audited."),
    ("To caution", "to warn carefully, without alarming anyone",
     "alertar, ponderar",
     "She cautioned that the market might not reopen this year."),
    ("Quarterly results", "the numbers a company reports every three months",
     "resultados trimestrais",
     "He walked the board through the quarterly results in ten minutes."),
    ("To walk through", "to explain something step by step, patiently",
     "conduzir passo a passo",
     "Let me walk you through what the investor actually said."),
    ("Investor deck", "the slide deck you present to investors",
     "apresenta&#231;&#227;o a investidores",
     "The investor deck says one thing; the cap table says another."),
]

PHASES = ["The Message", "The Language of the Board", "The Code",
          "The Briefing", "Practice", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Tonight you become the messenger. An investor "
    "says something in a room. You have to carry it, exactly, into another room -- to your CEO, to your board. Get "
    "one word wrong and you start a crisis.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 5 &middot; The Messenger", "What They Actually", "Said",
    "A CFO spends half of his life repeating other people's words. In English, that has a grammar."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 4 ANTES do tema novo (REGRA 20). Peca uma frase: "
    "'Give me one I wish I had... about last week.' Depois abra o tema: 'Now, the last time someone important told "
    "you something and you had to repeat it to your CEO. What did they say -- exactly?' Deixe falar. Anote quantas "
    "vezes ele fragmenta ao tentar reportar.",
    "Chapter 1: The Message",
    "You Are the", "Messenger",
    "Someone said something important. Your CEO asks: \"What exactly did they say?\" Tell me."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Explique a aposta. Reportar mal e a forma mais rapida de destruir a "
    "confianca de um board -- porque cada palavra sua vira decisao de milhoes. E, no ingles, reportar exige uma "
    "mecanica que o portugues NAO exige: o tempo verbal recua. E aqui que o Felipe vai travar, e e por isso que a "
    "aula existe.",
    "Why This Is Dangerous", "Every Word You Repeat Becomes a", "Decision",
    [("Report it loosely", "the board acts on the wrong information"),
     ("Report it literally", "you sound like a transcript, not a CFO"),
     ("Report it precisely", "you become the person they call first")],
    "\"She said the market MIGHT not reopen\" and \"She said the market WILL not reopen\" are two different companies, one year apart."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of the boardroom, the backshift -- the "
    "gear change English makes and Portuguese does not -- and a real briefing where you carry an investor message "
    "to your CEO.' Antecipe: o listening dele HOJE e a fonte que ele vai ter de reportar depois. Ele vai precisar "
    "prestar atencao de verdade.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "guidance, covenant, dilution, cap table..."),
     ("2. The Code", "\"We will\" &rarr; He said they would"),
     ("3. The Briefing", "carry the investor's words to your CEO")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. These are the ones that appear in the minutes "
    "of every board meeting you will ever attend.' Passe ao proximo.",
    "Chapter 2: The Language of the Board", "The Words of the", "Boardroom",
    "12 words &mdash; the vocabulary of investor relations.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'covenant': 'If we "
    "break a covenant, is that a mistake or a contract breach? (A contract breach -- the bank can call the loan.)' "
    "CCQ 'guidance': 'Is guidance a private forecast or a public promise? (Public -- the market trades on it.)' CCQ "
    "'dilution': 'If we issue new shares, does my percentage go up or down? (Down.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'To reiterate', 'to caution' e 'to walk through' "
    "sao REPORTING VERBS -- e vao ser as ferramentas da gramatica de hoje. Aponte isso agora: 'These three are not "
    "just words. They are how you report without sounding like a robot.' CCQ 'to reiterate': 'Do I reiterate "
    "something new, or something I already said? (Already said -- on purpose.)'",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'covenant' (CUV-uh-nant -- NAO 'co-VEN-ant'), "
    "'dilution' (di-LOO-shun), 'to reiterate' (ree-IT-uh-rate, 4 silabas), 'guidance' (GUY-dance). 'Covenant' com "
    "o stress errado e a palavra que mais faz banqueiro estrangeiro franzir a testa.",
    ["Covenant", "Dilution", "To reiterate", "Guidance", "Cap table"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas sao frases de ata de conselho.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"We are two points away from breaking the ", "covenant", ".\""),
     ("\"He warned that the round would cause serious ", "dilution", ".\""),
     ("\"Let me ", "walk you through", " what the investor actually said.\""),
     ("\"The CEO said that we would raise our ", "guidance", " for the year.\""),
     ("\"I ", "reiterated", " that the numbers had been audited.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. English does something Portuguese does not: "
    "when you repeat someone, the verb takes a step back in time.' Passe ao proximo.",
    "Chapter 3: The Code", "The", "Backshift",
    "\"We will raise\" &rarr; She said they would raise", L.IMG['code']))

S.append(L.s_discovery(
    11, 3,
    "<strong>Grammar discovery (8 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos, mostrando a fala "
    "DIRETA e o report lado a lado. Pergunte: 'Look at the verbs. What happened to every single one of them?' "
    "Espere ele dizer 'they moved back'. So entao clique 'Reveal the Rule'. CCQ: 'She SAID the market WOULD reopen "
    "-- did she use the word would? (No! She said WILL. English moved it back for me.)' Este e o insight da aula: o "
    "recuo e AUTOMATICO, e o portugues nao faz isso.",
    [("<em>\"We will raise the guidance.\"</em> &rarr; She said they "
      "<span style=\"color:#15803d;font-weight:700\">would raise</span> the guidance.",
      "She said they would raise the guidance."),
     ("<em>\"The numbers are audited.\"</em> &rarr; He said the numbers "
      "<span style=\"color:#15803d;font-weight:700\">were</span> audited.",
      "He said the numbers were audited."),
     ("<em>\"We have already signed.\"</em> &rarr; They said they "
      "<span style=\"color:#15803d;font-weight:700\">had already signed</span>.",
      "They said they had already signed."),
     ("<em>\"Have you disclosed it?\"</em> &rarr; She "
      "<span class=\"accent\" style=\"font-weight:700\">asked whether we had disclosed</span> it.",
      "She asked whether we had disclosed it.")],
    "Look at the verbs on the right. <span style=\"color:#15803d;font-weight:700\">Every one of them took a step "
    "backwards in time.</span> Who told them to?",
    [("The backshift<br>(o recuo)",
      "When you report, each verb steps ONE tense back. English does this automatically; Portuguese does not.",
      "will &rarr; <strong>would</strong> &middot; is &rarr; <strong>was</strong> &middot; "
      "have &rarr; <strong>had</strong>"),
     ("say vs tell",
      "<em>tell</em> always needs a person right after it. <em>say</em> never does.",
      "She <strong>told me</strong> that... / She <strong>said that</strong>..."),
     ("Reported questions",
      "Use <em>whether</em> or <em>if</em>, and go back to STATEMENT word order. No inversion, no question mark.",
      "She <strong>asked whether we had</strong> disclosed it."),
     ("Reporting verbs",
      "<em>said</em> is the floor, not the ceiling. Choose the verb that carries the intent.",
      "She <strong>cautioned</strong> / <strong>reiterated</strong> / <strong>warned</strong> that..."),
     ("No backshift needed",
      "If it is STILL true, you may keep the present. Both are correct; the present sounds more confident.",
      "She said the covenant <strong>is</strong> still in force."),
    ],
    "The trap is the question: in Portuguese you keep the question shape (\"ela perguntou se n&#243;s "
    "<em>divulgamos</em>?\"). In English the question DIES: <strong>She asked whether we had disclosed it.</strong> "
    "No inversion. No question mark.",
    "rule5"))

S.append(L.s_mistake(
    12, 3,
    "<strong>Common mistake (4 min):</strong> Tres erros, todos de brasileiro. (1) Manter a ordem de pergunta no "
    "report ('she asked did we disclose'). (2) 'She said me' -- em ingles e TELL que pede pessoa, nunca SAY. (3) "
    "Esquecer o recuo ('he said the numbers are audited' quando se quer reportar o passado). Peca que ele leia as "
    "certas DUAS vezes.",
    [("She asked me did we disclose the covenant breach.",
      "She asked me whether we had disclosed the covenant breach."),
     ("She said me that the term sheet would arrive on Friday.",
      "She told me that the term sheet would arrive on Friday."),
     ("He said the round will cause serious dilution.",
      "He said the round would cause serious dilution.")],
    "<strong>tell</strong> takes a person (<em>tell me</em>), <strong>say</strong> does not (<em>say that</em>). And "
    "a reported question is NOT a question any more: <em>whether/if</em> + normal word order, no inversion."))

S.append(L.s_fill(
    13, 3,
    "<strong>Practice (4 min):</strong> Leia a fala direta em voz alta, depois Felipe faz o report ORALMENTE antes "
    "de clicar. Se travar, pergunte: 'What tense did she use? Now step it back one.'",
    "Practice", "Report", "It", "Say the reported version first, then click to check",
    [("\"We will send the term sheet on Friday.\" &rarr; She said they ", "would send",
      " the term sheet on Friday.\""),
     ("\"The numbers are audited.\" &rarr; He said the numbers ", "were", " audited.\""),
     ("\"We have already signed.\" &rarr; They said they ", "had already signed", ".\""),
     ("\"Have you disclosed the breach?\" &rarr; She asked ", "whether we had disclosed", " the breach.\""),
     ("\"How much do you want to raise?\" &rarr; They asked ", "how much we wanted to raise", ".\"")]))

S.append(L.s_fill(
    14, 3,
    "<strong>Reporting verbs (4 min):</strong> 'Said' e o chao, nao o teto. O verbo escolhido carrega a INTENCAO -- "
    "e um board le a sua escolha de verbo como um sinal. Felipe escolhe o verbo ANTES de revelar, e explica POR QUE. "
    "Este slide e o que separa um report competente de um report senior.",
    "Register", "Choose the", "Verb", "Which verb carries what she actually meant?",
    [("\"She said it twice, on purpose, so it would stick.\" &rarr; She ", "reiterated",
      " that the numbers had been audited.\""),
     ("\"She warned us gently, without alarming anyone.\" &rarr; She ", "cautioned",
      " that the market might not reopen.\""),
     ("\"She said no, clearly and on the record.\" &rarr; She ", "denied",
      " that the fund had withdrawn.\""),
     ("\"She explained it step by step, patiently.\" &rarr; She ", "walked us through",
      " the whole cap table.\"")]))

S.append(L.s_chapter(
    15, 4,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'You have just heard Ingrid, the lead investor, in her own "
    "words. Now Claire, your CEO, was not in that room. Everything she knows, she will know from you.' Passe ao "
    "proximo. IMPORTANTE: este dialogo vem DEPOIS dos listenings de proposito -- o Felipe reporta o que ACABOU de "
    "ouvir.",
    "Chapter 4: The Briefing", "Your CEO Was Not in the", "Room",
    "Everything she knows, she knows from you", L.IMG['context']))

S.append(L.s_dialogue(
    16, 4,
    "<strong>Dialogo (8 min):</strong> Voce e a Claire, CEO. Clique 'Next Line' a cada fala. ANTES de tocar cada "
    "fala do Felipe, peca que ELE reporte a Ingrid com as proprias palavras -- ele acabou de ouvir o audio. E o "
    "exercicio central da aula. Se ele esquecer o recuo, nao corrija: repita a pergunta e espere.",
    "What Did Ingrid", "Say?",
    [("claire", "C", "ellen",
      "Felipe, I could not join the call with Ingrid. Walk me through it. What did she actually say about the round?",
      "Felipe, I could not join the call with Ingrid. Walk me through it. What did she actually say about the round?"),
     ("felipe", "F", "arthur",
      "She said the fund was still committed, and that the <span class=\"vocab-highlight\">term sheet</span> would "
      "arrive on Friday. But she cautioned that the market might not reopen this year.",
      "She said the fund was still committed, and that the term sheet would arrive on Friday. But she cautioned "
      "that the market might not reopen this year."),
     ("claire", "C", "ellen",
      "Cautioned, or warned? Those are very different words, Felipe.",
      "Cautioned, or warned? Those are very different words, Felipe."),
     ("felipe", "F", "arthur",
      "Cautioned. She was careful, not alarmed. And she "
      "<span class=\"vocab-highlight\">reiterated</span> twice that our numbers had been audited &mdash; she wanted "
      "that on the record.",
      "Cautioned. She was careful, not alarmed. And she reiterated twice that our numbers had been audited. She "
      "wanted that on the record."),
     ("claire", "C", "ellen",
      "Did she raise the <span class=\"vocab-highlight\">covenant</span>?",
      "Did she raise the covenant?"),
     ("felipe", "F", "arthur",
      "She asked whether we had <span class=\"vocab-highlight\">disclosed</span> it to the bank. I told her we had, "
      "in writing, in March. She then asked how much capital we intended to "
      "<span class=\"vocab-highlight\">raise</span>, and I said we had not decided &mdash; because that is your "
      "call, not mine.",
      "She asked whether we had disclosed it to the bank. I told her we had, in writing, in March. She then asked "
      "how much capital we intended to raise, and I said we had not decided, because that is your call, not mine.")]))

S.append(L.s_comprehension(
    17, 4,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a CLAIRE, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Claire",
    [("Why does Claire need Felipe to walk her through the call?",
      "She could not join it &mdash; everything she knows about it comes from him."),
     ("Which single word does she stop him on, and why?",
      "\"Cautioned\" &mdash; she wants to know if Ingrid was careful or alarmed. The verb changes the meaning."),
     ("What does she ask about directly?",
      "Whether Ingrid raised the covenant.")]))

S.append(L.s_listening(
    18, 4,
    "<strong>Listening 1 (6 min) &mdash; A FONTE:</strong> Diga: 'This is Ingrid, the lead investor, in her own "
    "words. Listen carefully -- because in ten minutes you will have to repeat every word of this to your CEO.' "
    "Toque SEM texto, 2 vezes. Deixe ele TOMAR NOTAS. Este audio nao e compreensao: e materia-prima para o dialogo "
    "e o role-play.",
    1, "Listening &middot; The Source", "Ingrid, in Her Own", "Words",
    "The lead investor speaks. Take notes &mdash; you will have to report this.",
    "a5_listening_investor.mp3", SLUG,
    [("What did she say about the term sheet?",
      "That it would arrive on Friday &mdash; and that the fund was still committed."),
     ("Did she warn, or did she caution?",
      "She cautioned: careful, not alarmed. She said the market might not reopen this year."),
     ("What did she ask about the covenant?",
      "Whether it had been disclosed to the bank &mdash; and she reiterated that the numbers had been audited.")]))

S.append(L.s_listening(
    19, 4,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now a CFO delivering quarterly results to the market. Notice how "
    "much of it is REPORTING what other people said.' Toque 2 vezes. Depois pergunte: 'Count the reporting verbs. "
    "How many did he use that were not said?'",
    2, "Listening 2", "The Quarterly", "Call",
    "A CFO reports to the market. Sound first &mdash; no text.",
    "a5_listening_cfo.mp3", SLUG,
    [("What did the board conclude about the guidance?",
      "That it should be raised &mdash; he reports that the board agreed to raise it."),
     ("What did the auditors confirm?",
      "That the quarterly results were clean, with no restatement."),
     ("What did he caution the market about?",
      "That the covenant headroom was narrow &mdash; two points &mdash; and that they were monitoring it monthly.")]))

S.append(L.s_chapter(
    20, 5,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the minutes, and the questions "
    "that come with no warning.' Passe ao proximo.",
    "Chapter 5: Practice", "Carry the Message", "Cleanly",
    "Detective &middot; The Minutes &middot; Quick Fire", L.IMG['practice']))

S.append(L.s_error(
    21, 5,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. A primeira e a "
    "pergunta reportada com ordem de pergunta (O erro). A segunda e 'said me'. Trate como vitoria quando ele achar "
    "sozinho.",
    [("She asked me did we disclose the covenant breach.",
      "She asked me whether we had disclosed the covenant breach."),
     ("She said me that the term sheet would arrive on Friday.",
      "She told me that the term sheet would arrive on Friday."),
     ("He said the round will cause serious dilution.",
      "He said the round would cause serious dilution."),
     ("They asked how much do we want to raise.",
      "They asked how much we wanted to raise.")]))

S.append(L.s_artifact(
    22, 5,
    "<strong>Artefato (5 min):</strong> A ata de reuniao E reported speech por escrito -- e por isso este artefato e "
    "perfeito. Peca que o Felipe leia cada linha e a diga em voz alta como REPORT falado, escolhendo o reporting "
    "verb. E a ponte entre o documento que ele ja sabe ler e a fala que ele ainda nao sabe produzir.",
    "The Artifact", "The Board", "Minutes",
    "BOARD MINUTES", "Q3 &middot; Confidential",
    [("Present", "F. Pimenta (CFO), C. Whitfield (CEO)"),
     ("Item 1 &mdash; Investor", "I. M&oslash;ller: fund still committed"),
     ("Item 2 &mdash; Term sheet", "Expected Friday"),
     ("Item 3 &mdash; Market", "Caution: may not reopen this year"),
     ("Item 4 &mdash; Covenant", "Disclosed to bank in March (in writing)"),
     ("Item 5 &mdash; Audit", "Numbers audited; reiterated on record"),
     ("Item 6 &mdash; Capital", "Amount: not yet decided (CEO's call)")],
    [("Say Item 1 and 2 out loud as one reported sentence.",
      "\"She said the fund was still committed, and that the term sheet would arrive on Friday.\""),
     ("Now Item 3 &mdash; and choose the verb carefully.",
      "\"She cautioned that the market might not reopen this year.\" (cautioned, not warned)"),
     ("Report Item 4 as a question she asked you.",
      "\"She asked whether we had disclosed it to the bank, and I told her we had.\"")]))

S.append(L.s_quickfire(
    23, 5,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO. Exija o "
    "recuo do tempo verbal em cada resposta. Aqui a pressao e alta de proposito: a CEO pergunta rapido, e e "
    "exatamente nesse ritmo que ele perde o backshift e volta pro presente.",
    "Your CEO Asks. You", "Report."))

S.append(L.s_building(
    24, 5,
    "<strong>Sentence Building (4 min):</strong> Mostre a fala DIRETA. Felipe produz o REPORT completo em voz alta, "
    "depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes.",
    [("\"We will send the term sheet on Friday.\" (she said)",
      "She said they would send the term sheet on Friday."),
     ("\"The numbers have been audited.\" (she reiterated)",
      "She reiterated that the numbers had been audited."),
     ("\"The market may not reopen this year.\" (she cautioned)",
      "She cautioned that the market might not reopen this year."),
     ("\"Have you disclosed the breach?\" (she asked)",
      "She asked whether we had disclosed the breach."),
     ("\"How much do you want to raise?\" (they asked)",
      "They asked how much we wanted to raise.")]))

S.append(L.s_chapter(
    25, 6,
    "<strong>Transicao role-play (1 min):</strong> Diga: 'Now the real thing. You carry the message -- and then "
    "someone tests whether you carried it honestly.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Carry the", "Message",
    "Guided &gt; Semi-free &gt; Free", L.IMG['turn']))

S.append(L.s_roleplay(
    26, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Claire, CEO. Abra com: 'Walk me through the call with "
    "Ingrid.' Felipe usa as keywords e as notas que tomou no Listening 1. Deixe conduzir. Observe se o backshift "
    "sai sozinho ou se ele volta pro presente.",
    "Brief Your", "CEO",
    "Your CEO missed the investor call. Walk her through it: what Ingrid said about the fund, the term sheet, the "
    "market, and the covenant. Choose your reporting verbs carefully &mdash; she will notice.",
    ["She said that...", "She cautioned that...", "She reiterated that...",
     "She asked whether we had..."]))

S.append(L.s_roleplay(
    27, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. Agora voce e um MEMBRO DO CONSELHO cetico, que "
    "estava na call e ouviu a MESMA Ingrid -- e que vai testar a honestidade do report. Interrompa com: 'That is "
    "not quite what she said, is it?' O Felipe tem de defender a escolha das palavras dele (cautioned vs warned) "
    "SEM recuar da versao. E o teste de precisao da aula.",
    "The Board Member Who Was", "Also There",
    "A board member was on the same call. He challenges your report: \"She warned us. You are softening it.\" "
    "Defend your words &mdash; precisely, and without backing down. The difference between cautioned and warned is "
    "the whole argument.",
    ["What she actually said was...", "She cautioned, she did not warn.",
     "Let me walk you through it again.", "I reiterated that..."],
    tint='.12'))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: o briefing inteiro, ZERO pistas. NAO interrompa, NAO "
    "corrija no meio. Cronometre 3 min. Peca que ele reporte a Ingrid do Listening 1 inteira, de memoria, para o "
    "board. CELEBRE muito: reportar com precisao sob pressao e o que faz um CFO ser chamado primeiro.",
    "The Whole", "Briefing",
    "Brief the full board on the investor call, end to end. Report what Ingrid said about the fund, the term sheet, "
    "the market and the covenant; report the questions she asked and how you answered them; and close with what you "
    "recommend the board decides.",
    []))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Extensao / pressao (4 min):</strong> So faca se sobrar tempo E ele estiver fluindo. Aqui voce muda o "
    "cenario no meio: 'Ingrid just called again. She has changed her mind about Friday.' Ele tem de reportar uma "
    "informacao NOVA, na hora, sem preparo. E a simulacao mais proxima da vida real dele.",
    "The Message", "Changes",
    "Mid-briefing, the investor calls again and changes one thing. Report the new message to the board immediately, "
    "flag exactly what changed from what you said five minutes ago, and say what it means for the decision in front "
    "of them.",
    []))

S.append(L.s_chapter(
    30, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'You carried another person\\'s words across a room, in "
    "English, without dropping one. That is the job.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You Carried the", "Message",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("She said the fund was still committed, and that the term sheet would arrive on Friday.",
     "Ela disse que o fundo continuava comprometido e que o term sheet chegaria na sexta."),
    ("She cautioned that the market might not reopen this year.",
     "Ela ponderou que o mercado pode n&#227;o reabrir este ano."),
    ("She reiterated that the numbers had been audited.",
     "Ela reiterou que os n&#250;meros haviam sido auditados."),
    ("She asked whether we had disclosed the covenant to the bank.",
     "Ela perguntou se t&#237;nhamos divulgado o covenant ao banco."),
    ("Let me walk you through exactly what was said.",
     "Deixe-me conduzi-lo passo a passo pelo que foi dito."),
]

S.append(L.s_survival(
    31, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Sao as 5 "
    "frases de qualquer briefing -- e as que ele vai usar na proxima call com investidor de verdade.",
    "Five Phrases for the", "Briefing",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    32, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 5 no passaporte (registra no Supabase).",
    N,
    ["I can report what someone said, with the tense stepping back one pace.",
     "I can use say and tell correctly &mdash; tell takes a person, say does not.",
     "I can report a question with whether/if and normal word order, not question order.",
     "I can choose the reporting verb that carries the intent: cautioned, reiterated, denied.",
     "I know my words: guidance, covenant, dilution, cap table, term sheet, to disclose."]))

S.append(L.s_complete(
    33, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 5 complete, Felipe. You earned your Boardroom Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) pegar a ultima reuniao REAL com investidor ou banco e escrever "
    "o report em 6 frases, todas com reported speech e reporting verbs diferentes -- e gravar lendo; (2) na proxima "
    "reuniao de verdade, reportar UMA fala usando 'she cautioned' ou 'he reiterated' em vez de 'she said'. Proxima "
    "aula: Getting Things Done Through Others -- delegacao e causative have/get.",
    N, "Boardroom Badge", "You carried the message, Felipe. Word for word.",
    "Getting Things Done Through Others"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Making Your Case -- Board Updates &amp; Investor Communications',
    'short_title': 'Making Your Case',
    'menu_desc': 'Briefing de investidor ao board + reported speech',
    'desc': ('Carregar as palavras de um investidor para dentro do board sem perder uma s&#237;laba. Key words: to '
             'disclose, guidance, covenant, dilution, term sheet, cap table, to raise capital, to reiterate, to '
             'caution, quarterly results, to walk through, investor deck. Structures: reported speech &mdash; o '
             'recuo do tempo verbal (backshift), say vs tell, perguntas indiretas (whether/if, sem '
             'invers&#227;o) e reporting verbs (cautioned, reiterated, denied).'),
    'hub_img': 'https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'claire': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. S&#227;o as palavras que aparecem na ata de todo conselho '
                    'de que voc&#234; vai participar.'),

    'context_text': (
        'Ingrid, the lead investor, called on a Tuesday. Felipe took the call alone; the CEO could not join. Ingrid '
        '<strong>said</strong> that the fund <strong>was</strong> still committed, and that the '
        '<strong>term sheet</strong> <strong>would</strong> arrive on Friday. She '
        '<strong>cautioned</strong> that the market <strong>might</strong> not reopen this year &mdash; she was '
        'careful, not alarmed, and the difference matters. She <strong>reiterated</strong> twice that the numbers '
        '<strong>had been</strong> audited, because she wanted that on the record. Then she '
        '<strong>asked whether</strong> the company <strong>had disclosed</strong> the <strong>covenant</strong> '
        'breach to the bank. Felipe <strong>told her</strong> that they <strong>had</strong>, in writing, in March. '
        'She also <strong>asked how much capital</strong> they <strong>intended</strong> to '
        '<strong>raise</strong>, and he <strong>said</strong> they <strong>had not decided</strong>. Notice what '
        'happens to every verb when Felipe repeats her: <em>will</em> becomes <strong>would</strong>, <em>is</em> '
        'becomes <strong>was</strong>, <em>have been</em> becomes <strong>had been</strong>. English steps back one '
        'pace. Portuguese does not. When he later <strong>walked</strong> the CEO <strong>through</strong> the call, '
        'she stopped him on a single word: <em>cautioned, or warned?</em> Two verbs, two different companies.'),

    'context_quiz': [
        ("Ingrid disse \"We will send the term sheet on Friday\". Como o Felipe reporta isso?",
         [("She said they will send the term sheet on Friday.", False),
          ("She said they would send the term sheet on Friday.", True),
          ("She said they send the term sheet on Friday.", False)]),
        ("Por que a CEO para o Felipe na palavra \"cautioned\"?",
         [("Porque <em>cautioned</em> (ponderar, com cuidado) e <em>warned</em> (alertar, com alarme) mudam "
           "completamente a leitura da mensagem &mdash; e o board decide com base nela.", True),
          ("Porque <em>cautioned</em> est&#225; gramaticalmente errado nessa frase.", False),
          ("Porque ela n&#227;o conhece a palavra <em>cautioned</em>.", False)]),
        ("Ingrid perguntou \"Have you disclosed it?\". Which report is correct English?",
         [("She asked had we disclosed it.", False),
          ("She asked whether we had disclosed it.", True),
          ("She asked did we disclose it?", False)]),
    ],

    'tip_title': 'Reported Speech (backshift, say/tell, perguntas indiretas)',
    'tip_intro': ('Como repetir as palavras de outra pessoa &mdash; a gram&#225;tica de metade do trabalho de um CFO '
                  '(explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("O recuo (backshift)",
         "Ao reportar, cada verbo recua UM tempo. O ingl&#234;s faz isso automaticamente; o portugu&#234;s N&#195;O. "
         "Each verb steps one tense back.",
         "will &rarr; <strong>would</strong> &middot; is &rarr; <strong>was</strong> &middot; have &rarr; "
         "<strong>had</strong>"),
        ("say vs tell",
         "<em>tell</em> SEMPRE pede uma pessoa logo depois. <em>say</em> NUNCA pede. <em>tell</em> needs a person; "
         "<em>say</em> does not.",
         "She <strong>told me</strong> that... / She <strong>said</strong> that..."),
        ("Perguntas reportadas",
         "Use <em>whether</em> ou <em>if</em> e volte &#224; ordem de AFIRMA&#199;&#195;O. Sem invers&#227;o, sem "
         "ponto de interroga&#231;&#227;o.",
         "She <strong>asked whether we had</strong> disclosed it."),
        ("Perguntas com wh-",
         "Mant&#233;m a palavra-pergunta, mas a ordem vira de afirma&#231;&#227;o.",
         "They <strong>asked how much we wanted</strong> to raise."),
        ("Reporting verbs",
         "<em>said</em> &#233; o ch&#227;o, n&#227;o o teto. O verbo carrega a INTEN&#199;&#195;O &mdash; e o board l&#234; "
         "a sua escolha.",
         "She <strong>cautioned</strong> / <strong>reiterated</strong> / <strong>denied</strong> that..."),
        ("Quando N&#195;O recuar",
         "Se ainda &#233; verdade agora, o presente &#233; permitido &mdash; e soa mais confiante.",
         "She said the covenant <strong>is</strong> still in force."),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (o erro n&#186; 1 do brasileiro):</strong> a pergunta reportada. Em '
                 'portugu&#234;s a forma de pergunta sobrevive ("ela perguntou se n&#243;s divulgamos"). Em '
                 'ingl&#234;s a pergunta MORRE: <em>"She asked <strong>did we disclose</strong>"</em> est&#225; '
                 'errado &mdash; o certo &#233; <strong>"She asked whether we had disclosed it."</strong> Sem '
                 'invers&#227;o, sem "?". E lembre: <strong>tell</strong> pede pessoa ("she told <em>me</em>"), '
                 '<strong>say</strong> n&#227;o ("she said <em>that</em>") &mdash; "she said me" n&#227;o existe.'),

    'blanks': [
        ("Ingrid said the fund", "was", "Dica: o recuo &mdash; \"is\" vira o qu&#234; ao reportar?",
         "Ingrid said the fund was still committed.", "still committed."),
        ("She said the term sheet", "would arrive", "Dica: o recuo &mdash; \"will arrive\" recua um tempo",
         "She said the term sheet would arrive on Friday.", "on Friday."),
        ("She", "cautioned", "Dica: alertar COM CUIDADO, sem alarmar &mdash; n&#227;o &#233; \"warned\"",
         "She cautioned that the market might not reopen this year.",
         "that the market might not reopen this year."),
        ("She reiterated that the numbers", "had been audited",
         "Dica: o recuo &mdash; \"have been audited\" recua um tempo",
         "She reiterated that the numbers had been audited.", "."),
        ("She asked", "whether we had disclosed",
         "Dica: pergunta reportada &mdash; whether + ordem de afirma&#231;&#227;o, sem invers&#227;o",
         "She asked whether we had disclosed the covenant to the bank.", "the covenant to the bank."),
        ("She", "told me", "Dica: o verbo que PEDE pessoa logo depois (say n&#227;o pede)",
         "She told me that the term sheet would arrive on Friday.",
         "that the term sheet would arrive on Friday."),
    ],

    'order_title': 'Put the Investor Briefing in Order',
    'order_intro': ('Coloque as etapas de um briefing ao board na ordem correta. Um board decide na sequ&#234;ncia '
                    'em que voc&#234; entrega a informa&#231;&#227;o.'),
    'order': [
        (2, "Report what she said, in her words, with the reporting verb she earned."),
        (5, "Close with what you recommend the board decides &mdash; and what is not your call."),
        (1, "State who you spoke to, when, and who else was on the call."),
        (4, "Report the questions she asked, and exactly how you answered them."),
        (3, "Separate what she stated as fact from what she merely cautioned about."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases de '
                     'qualquer briefing de investidor.'),
    'speech': SURVIVAL,

    'quiz': [
        ("Ingrid said: \"We will send the term sheet on Friday.\" You report:",
         [("\"She said they will send the term sheet on Friday.\"", False),
          ("\"She said they would send the term sheet on Friday.\"", True),
          ("\"She said me they send the term sheet on Friday.\"", False)]),
        ("Ingrid asked: \"Have you disclosed the covenant?\" You report:",
         [("\"She asked had we disclosed the covenant.\"", False),
          ("\"She asked whether we had disclosed the covenant.\"", True),
          ("\"She asked did we disclose the covenant?\"", False)]),
        ("She said it twice, deliberately, so it would stick. The right verb is:",
         [("\"She reiterated that the numbers had been audited.\"", True),
          ("\"She denied that the numbers had been audited.\"", False),
          ("\"She cautioned that the numbers had been audited.\"", False)]),
        ("She warned you gently, without alarming anyone. You report:",
         [("\"She warned that the market will not reopen.\"", False),
          ("\"She cautioned that the market might not reopen this year.\"", True),
          ("\"She said the market is not reopening.\"", False)]),
        ("A board member says your report softened her message. The best response is:",
         [("\"Maybe. I might have misheard her.\"", False),
          ("\"She cautioned, she did not warn. Let me walk you through exactly what she said.\"", True),
          ("\"You're right, I'll change it in the minutes.\"", False)]),
    ],

    'think': ("Your CEO could not join the investor call. Brief her for 2-3 minutes. Report what Ingrid said about "
              "the fund, the term sheet and the market; report the two questions she asked and how you answered "
              "them. Use the backshift throughout, use \"told\" at least once and \"said\" at least once (correctly), "
              "and choose your reporting verbs deliberately &mdash; cautioned is not warned. Finish with what you "
              "recommend, and what is not your call."),

    'listenings': [
        {"file": "a5_listening_investor.mp3", "voice": "ellen",
         "text": ("Felipe, thanks for making the time, and I am sorry Claire could not join us. Let me be direct, "
                  "because I know you will have to carry this back to her. First, the fund is still committed. "
                  "Nothing has changed on our side, and you can tell her that in exactly those words. The term "
                  "sheet will arrive on Friday, and it will look very close to what we discussed in June. Second, I "
                  "want to be careful here, and I am choosing my words: the market may not reopen this year. I am "
                  "not telling you it will close. I am telling you not to build a plan that depends on it. Third, "
                  "and I will say this twice because it matters: your numbers have been audited, and that is a real "
                  "asset in this environment. Your numbers have been audited. I want that on the record. Now, a "
                  "question. Have you disclosed the covenant position to the bank? And a second one: how much "
                  "capital are you actually intending to raise? Take your time on that one. I would rather have a "
                  "slow answer than a fast number.")},
        {"file": "a5_listening_cfo.mp3", "voice": "arthur",
         "text": ("Good afternoon, everyone, and thank you for joining our quarterly results call. Let me walk you "
                  "through the numbers and then through what the board and our auditors have told us. The auditors "
                  "confirmed that the quarterly results are clean. There is no restatement, and I want to be very "
                  "clear about that. The board met on Monday, and it agreed that we should raise our guidance for "
                  "the full year, on the strength of the last two quarters. So we are raising guidance today. I "
                  "would, however, caution you on one point. Our covenant headroom is narrow. It is two points, and "
                  "we are monitoring it monthly rather than quarterly. Our lead investor reiterated last week that "
                  "she remains committed, and she asked whether we had disclosed our covenant position to the bank. "
                  "We had, in writing, back in March. I will now hand over to the CEO, and then we will take your "
                  "questions.")},
    ],

    'inclass_blocks': {
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"What exactly did she say about the term sheet?\"",
                 "tips": ["She said it would arrive on Friday.",
                          "will &rarr; would. Step the verb back."]},
                {"situation": "\"Cautioned, or warned? Be precise.\"",
                 "tips": ["She cautioned. She was careful, not alarmed.",
                          "Defend the verb &mdash; it changes the decision."]},
                {"situation": "\"Did she say anything about the audit?\"",
                 "tips": ["She reiterated that the numbers had been audited.",
                          "reiterated = she said it twice, on purpose."]},
                {"situation": "\"Did she ask about the covenant?\"",
                 "tips": ["She asked whether we had disclosed it to the bank.",
                          "whether + statement order. No inversion."]},
                {"situation": "\"And what did you tell her?\"",
                 "tips": ["I told her we had, in writing, in March.",
                          "tell takes a person: told HER."]},
                {"situation": "\"How much did she say we should raise?\"",
                 "tips": ["She didn't. She asked how much we intended to raise.",
                          "Never invent a number she did not give you."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Succession -- Season 3 (HBO Max)",
         "Uma temporada inteira em que cada personagem reporta ao outro o que um terceiro disse &mdash; e cada "
         "escolha de verbo &#233; uma arma. Connection to Lesson 5: repare em como o mesmo fato muda de sentido "
         "conforme o reporting verb.",
         "Dica: assista com legenda em ingl&#234;s. Escolha uma cena e reescreva 3 falas em reported speech.",
         "https://www.hbo.com/succession"),
        ("Podcast", "podcast", "Acquired -- epis&#243;dios sobre rodadas, term sheets e cap tables",
         "Dois investidores reconstruindo negocia&#231;&#245;es reais &mdash; e o epis&#243;dio inteiro &#233;, na "
         "pr&#225;tica, reported speech em velocidade nativa. Connection to Lesson 5: term sheet, dilution, cap "
         "table e guidance aparecem no contexto exato da sua aula.",
         "Dica: ou&#231;a a 1x. Cada vez que ouvir \"he said that...\", pause e repita a frase inteira.",
         "https://www.acquired.fm/"),
        ("YouTube", "youtube", "Financial Times -- earnings calls e investor communications",
         "Como CFOs de verdade comunicam guidance, covenant e resultados trimestrais ao mercado. Connection to "
         "Lesson 5: &#233; o seu pr&#243;prio trabalho, na l&#237;ngua-alvo, com o vocabul&#225;rio da aula.",
         "Dica: assista a 0.75x se precisar. Anote 5 reporting verbs que N&#195;O sejam \"said\".",
         "https://www.youtube.com/@FinancialTimes"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
