#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 8 — Progress Check and Integration (Felipe at the Midpoint).
Gramatica: INTEGRACAO das 6 estruturas do Bloco 1 (aulas 2-7).
Modelo: LEITURA (aula PAR, REGRA 29) — ic-reading + gist + true/false + discussao.
Callback (REGRA 20): a aula INTEIRA e callback — mas o vocab e NOVO (REGRA 22).

Desenho: a leitura e uma carta do comite de auditoria que USA as seis estruturas.
O aluno le, identifica, e depois PRODUZ. Assessment real, nao revisao passiva.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 8
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Working capital", "the cash tied up in running the business day to day",
     "capital de giro",
     "If we had managed working capital better, we would not have needed the loan."),
    ("EBITDA", "earnings before interest, taxes, depreciation and amortization",
     "EBITDA",
     "EBITDA is not cash, and the board should have been told that."),
    ("Liquidity", "how easily you can turn what you own into cash",
     "liquidez",
     "What we lacked was liquidity, not profit."),
    ("Solvency", "whether you can pay your debts over the long term",
     "solv&#234;ncia",
     "Liquidity is this month. Solvency is this decade."),
    ("Audit committee", "the group of directors that oversees financial reporting",
     "comit&#234; de auditoria",
     "The audit committee asked whether we had disclosed the provision."),
    ("Compliance", "following the rules and the regulations, on the record",
     "conformidade, compliance",
     "Not once have we had a compliance failure, and I intend to keep it that way."),
    ("Impairment", "writing an asset down because it lost value",
     "impairment, redu&#231;&#227;o ao valor recuper&#225;vel",
     "We had the asset tested and we booked an impairment."),
    ("Provision", "money set aside now for a loss that is likely later",
     "provis&#227;o",
     "I wish we had made a provision for the tax dispute."),
    ("Reconciliation", "checking that two sets of records actually agree",
     "concilia&#231;&#227;o",
     "I had the reconciliation done before the auditors arrived."),
    ("To restate", "to reissue financial statements that were wrong",
     "reapresentar demonstra&#231;&#245;es",
     "It was the revenue cut-off that forced us to restate."),
    ("Materiality", "whether a number is big enough to change a decision",
     "materialidade",
     "She cautioned that the error was below materiality, but not below embarrassment."),
    ("Headroom", "the space you still have before you hit a limit",
     "folga antes do limite",
     "We should have protected our headroom instead of spending it."),
]

PHASES = ["Where You Started", "The Language of the Close", "The Letter",
          "The Six Tools", "The Committee", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Esta e uma aula-ESPELHO: metade do programa passou. "
    "Diga: 'Seven lessons ago, you could not take a call in English. Tonight you are going to use six structures in "
    "one room, without me telling you which is which.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 8 &middot; Midpoint", "Everything You Have,", "At Once",
    "Halfway. Tonight nobody tells you which tool to reach for."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + diagnostico (6 min):</strong> Este warm-up E o assessment. Peca UMA frase de cada estrutura "
    "sobre a semana REAL dele -- sem consultar nada: (1) third conditional, (2) modal perfect, (3) I wish, (4) "
    "reported speech, (5) causative, (6) cleft. ANOTE quais saem sozinhas e quais travam. Esse mapa dirige o resto "
    "da aula e as aulas 9-16.",
    "Chapter 1: Where You Started",
    "Six Sentences About Your", "Week",
    "One for each tool you have learned. No notes. Whatever comes out is the diagnosis."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Mostre o mapa. Cada estrutura resolve UM problema comunicativo, e o "
    "erro do aluno intermediario e ter as seis e nao saber qual pegar. Hoje o treino nao e a estrutura: e a ESCOLHA "
    "da estrutura sob pressao. Diga isso com clareza.",
    "The Real Test", "Not the Tools. The", "Choice.",
    [("Analyze the past", "third conditional &middot; modal perfects"),
     ("Repair a relationship", "I wish &middot; if only"),
     ("Carry and command", "reported speech &middot; causative &middot; cleft")],
    "You have six tools. Tonight nobody hands you the right one — you reach for it yourself, under pressure. That is what fluency actually is."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of the annual close, a real audit committee "
    "letter that uses all six structures at once, and a full simulation where I stop helping you.' Antecipe: o "
    "role-play final e uma sessao inteira de comite de auditoria.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "liquidity, solvency, provision, materiality..."),
     ("2. The Letter", "spot all six structures in one document"),
     ("3. The Committee", "a full simulation &mdash; no help")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. These are the ones that decide whether an audit "
    "committee trusts you.' Passe ao proximo.",
    "Chapter 2: The Language of the Close", "The Words of the Annual", "Close",
    "12 words &mdash; the vocabulary of the audit committee.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'liquidity vs "
    "solvency': 'A company with great profit can still die. Which one is missing? (Liquidity -- cash this month.)' "
    "CCQ 'EBITDA': 'Is EBITDA cash? (No -- and confusing them has killed companies.)' CCQ 'working capital': 'Is it "
    "money you have, or money you have tied up? (Tied up.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ 'materiality': 'If an error is small but "
    "embarrassing, is it material? (Technically no -- but the committee will still ask. Materiality is a threshold, "
    "not an excuse.)' CCQ 'provision': 'Do I book a provision for a loss that is certain, or probable? (Probable -- "
    "that is the whole point.)' CCQ 'to restate': 'Is restating a mistake, or the correction of one? (The "
    "correction -- and it is the most expensive sentence in finance.)'",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'liquidity' (li-KWID-i-ty), 'solvency' (SOL-ven-cy), "
    "'materiality' (ma-teer-ee-AL-i-ty -- 6 silabas, a mais dificil), 'impairment' (im-PAIR-ment), 'reconciliation' "
    "(rec-on-sil-ee-AY-shun). Peca 'materiality' tres vezes: e a palavra que o comite usa para te encurralar.",
    ["Liquidity", "Solvency", "Materiality", "Impairment", "Reconciliation"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Repare: cada frase usa TAMBEM uma estrutura das aulas 2-7. Aponte isso.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"What we lacked was ", "liquidity", ", not profit.\""),
     ("\"I wish we had made a ", "provision", " for the tax dispute.\""),
     ("\"I had the ", "reconciliation", " done before the auditors arrived.\""),
     ("\"We should have protected our ", "headroom", " instead of spending it.\""),
     ("\"It was the revenue cut-off that forced us to ", "restate", ".\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao leitura (1 min):</strong> Diga: 'This letter is real. And it uses every single structure you "
    "have learned. Your job is not to understand it -- you already can. Your job is to SEE the machinery.' Passe ao "
    "proximo.",
    "Chapter 3: The Letter", "Six Tools, One", "Document",
    "You already understand it. Tonight you see how it is built.", L.IMG['context']))

S.append(L.s_blocks(
    11, 3,
    "<strong>Leitura + gist (7 min):</strong> Felipe le em SILENCIO (2-3 min). Depois pergunte a ideia central ANTES "
    "das alternativas. E ENTAO o exercicio real da aula: 'Go back and find one third conditional, one modal perfect, "
    "one I wish, one reported speech, one causative, and one cleft.' Ele vai encontrar todas. E o momento em que o "
    "programa fica visivel para ele.",
    "Read for the Main Idea", "The Audit Committee", "Letter",
    ["reading", "gist"]))

S.append(L.s_blocks(
    12, 3,
    "<strong>True or False (5 min):</strong> Felipe responde ORALMENTE e JUSTIFICA com o trecho antes de clicar. "
    "Exija que a justificativa use a MESMA estrutura do texto -- se o texto diz 'should have', a justificativa dele "
    "tambem diz.",
    "Check Understanding", "True or", "False?", ["tf"]))

S.append(L.s_blocks(
    13, 3,
    "<strong>Discussao (6 min):</strong> Aqui o Felipe FALA -- e agora com as seis ferramentas na mesa. Nao corrija "
    "durante; ANOTE qual estrutura ele evita. A estrutura evitada e a licao das aulas 9-16.",
    "Discuss", "Talk It", "Through", ["guiding"]))

S.append(L.s_chapter(
    14, 4,
    "<strong>Transicao (1 min):</strong> Diga: 'Now we lay the six tools on the table, side by side, and you learn "
    "to grab the right one without looking.' Passe ao proximo.",
    "Chapter 4: The Six Tools", "One Problem, One", "Tool",
    "Analysis &middot; Judgment &middot; Regret &middot; Report &middot; Delegate &middot; Command",
    L.IMG['code']))

S.append(L.s_discovery(
    15, 4,
    "<strong>Grammar integration (8 min):</strong> Este slide NAO ensina nada novo -- ele obriga a ESCOLHER. Leia "
    "cada frase e pergunte: 'Which tool is this, and what job is it doing?' Felipe nomeia a estrutura ANTES de voce "
    "clicar. Se ele acertar as seis, o Bloco 1 esta consolidado. Se errar duas, voce ja sabe o que treinar nas "
    "aulas 9 a 16.",
    [("\"If we had managed working capital better, we wouldn't have needed the loan.\" &mdash; "
      "<span style=\"color:#0e7490;font-weight:700\">which tool?</span>",
      "If we had managed working capital better, we wouldn't have needed the loan."),
     ("\"We should have protected our headroom instead of spending it.\" &mdash; "
      "<span style=\"color:#b45309;font-weight:700\">which tool?</span>",
      "We should have protected our headroom instead of spending it."),
     ("\"She asked whether we had disclosed the provision.\" &mdash; "
      "<span style=\"color:#15803d;font-weight:700\">which tool?</span>",
      "She asked whether we had disclosed the provision."),
     ("\"What we lacked was liquidity, not profit.\" &mdash; "
      "<span style=\"color:#7c3aed;font-weight:700\">which tool?</span>",
      "What we lacked was liquidity, not profit.")],
    "Six tools. Six jobs. Name the tool, then name the JOB it is doing &mdash; that second answer is the one that "
    "matters.",
    [("Third conditional",
      "Analyze a past that did not happen. No blame, pure analysis.",
      "<strong>If we had</strong> managed it, we <strong>wouldn't have</strong> needed the loan."),
     ("Modal perfects",
      "Deliver a verdict on ONE action. should = person; could = situation.",
      "We <strong>should have protected</strong> our headroom."),
     ("Wish / if only",
      "Repair a relationship. The only tool with emotion in it.",
      "I <strong>wish we had made</strong> a provision."),
     ("Reported speech",
      "Carry someone else's words accurately. The tense steps back.",
      "She <strong>asked whether we had</strong> disclosed it."),
     ("Causative have/get",
      "Report work that happened without you. The doer disappears.",
      "I <strong>had the reconciliation done</strong>."),
     ("Inversion + cleft",
      "Command the room &mdash; and buy half a second to think.",
      "<strong>What we lacked was</strong> liquidity, not profit."),
    ],
    "The intermediate speaker owns all six and reaches for the wrong one. The fluent speaker reaches without "
    "looking. Tonight is about the reach.",
    "rule8"))

S.append(L.s_mistake(
    16, 4,
    "<strong>Common mistake (4 min):</strong> Estes sao os TRES erros que mais reapareceram nas aulas 2 a 7. Se "
    "algum ainda sair na fala dele hoje, este e o slide para voltar. Peca que ele leia as certas DUAS vezes -- e "
    "que diga em voz alta qual estrutura cada uma e.",
    [("If we would have known the risk, we didn't take the loan.",
      "If we had known the risk, we wouldn't have taken the loan."),
     ("I wish I would have made a provision for the dispute.",
      "I wish I had made a provision for the dispute."),
     ("She asked me did we disclose the impairment.",
      "She asked me whether we had disclosed the impairment.")],
    "Three lessons, three traps, one root: the if-half never takes <strong>would</strong>, <em>wish</em> about "
    "YOURSELF never takes <strong>would</strong>, and a reported question is <strong>not a question any more</strong>."))

S.append(L.s_fill(
    17, 4,
    "<strong>Integration practice (5 min):</strong> Aqui o Felipe escolhe a ESTRUTURA, nao so a palavra. Leia o "
    "contexto entre parenteses e deixe que ELE decida qual ferramenta usar. E o exercicio mais dificil do Bloco 1.",
    "Practice", "Pick the Right", "Tool", "Read the job. Choose the structure. Say it, then click.",
    [("\"(analyze: it did not happen) \"", "If we had made a provision", ", the restatement would not have hurt.\""),
     ("\"(verdict on one action) \"We ", "should have protected", " our headroom instead of spending it.\""),
     ("\"(repair: you are talking to a person) \"I ", "wish I had listened", " to the audit committee in March.\""),
     ("\"(carry her words) \"She ", "cautioned that the error was", " below materiality, but not below embarrassment.\""),
     ("\"(the work happened, not by you) \"I ", "had the reconciliation done", " before the auditors arrived.\""),
     ("\"(command the room) \"", "What we lacked was", " liquidity, not profit.\"")]))

S.append(L.s_chapter(
    18, 5,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Diana chairs the audit committee. You have met her twice. "
    "Tonight she asks about everything at once -- and she does not tell you which tool to use.' Passe ao proximo.",
    "Chapter 5: The Committee", "Everything, In One", "Room",
    "The audit committee, in full session", L.IMG['turn']))

S.append(L.s_dialogue(
    19, 5,
    "<strong>Dialogo (8 min):</strong> Voce e a Diana. Clique 'Next Line' a cada fala. Este dialogo e a prova do "
    "Bloco 1: CADA fala do Felipe usa uma estrutura diferente. ANTES de tocar o audio, peca que ele produza a fala "
    "-- e depois pergunte 'which tool did you just use?'. Se ele nomear certo, ele nao so fala: ele SABE o que "
    "fala.",
    "The Audit Committee", "Session",
    [("diana", "D", "ellen",
      "Felipe, three items. The restatement, the provision, and the covenant. Start wherever you like.",
      "Felipe, three items. The restatement, the provision, and the covenant. Start wherever you like."),
     ("felipe", "F", "arthur",
      "What forced the restatement was the revenue cut-off, not the audit. If we had run the "
      "<span class=\"vocab-highlight\">reconciliation</span> a week earlier, we would have caught it before the "
      "close.",
      "What forced the restatement was the revenue cut-off, not the audit. If we had run the reconciliation a week "
      "earlier, we would have caught it before the close."),
     ("diana", "D", "ellen",
      "And the <span class=\"vocab-highlight\">provision</span>? The committee was not told.",
      "And the provision? The committee was not told."),
     ("felipe", "F", "arthur",
      "It should have been disclosed in March, and it was not. I wish I had brought it to you myself instead of "
      "letting it sit in a report. That one is mine.",
      "It should have been disclosed in March, and it was not. I wish I had brought it to you myself instead of "
      "letting it sit in a report. That one is mine."),
     ("diana", "D", "ellen",
      "What did the auditor actually say about <span class=\"vocab-highlight\">materiality</span>?",
      "What did the auditor actually say about materiality?"),
     ("felipe", "F", "arthur",
      "She cautioned that the error was below <span class=\"vocab-highlight\">materiality</span> but not below "
      "embarrassment &mdash; her words. So I had the whole cut-off process re-tested, and I got the controller to "
      "sign it off personally. Not once will we let a number reach this room unreconciled again.",
      "She cautioned that the error was below materiality but not below embarrassment. Her words. So I had the "
      "whole cut-off process re-tested, and I got the controller to sign it off personally. Not once will we let a "
      "number reach this room unreconciled again.")]))

S.append(L.s_comprehension(
    20, 5,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a DIANA, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Diana",
    [("Which three items does Diana put on the table?",
      "The restatement, the provision, and the covenant."),
     ("What is her complaint about the provision?",
      "That the committee was not told about it."),
     ("What does she want to know about the auditor?",
      "What the auditor actually said about materiality.")]))

S.append(L.s_listening(
    21, 5,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CFO gives her year-in-review to the board. Every structure you "
    "know is in there. Listen -- no text.' Toque SEM texto, 2 vezes. Peca que ele IDENTIFIQUE as seis estruturas de "
    "ouvido. E o teste de escuta estrutural, nao so de compreensao.",
    1, "Listening", "The Year in", "Review",
    "Six structures, one speech. Sound first &mdash; no text.",
    "a8_listening_cfo.mp3", SLUG,
    [("What does she say about the restatement?",
      "That it was the revenue cut-off that forced it &mdash; and if they had reconciled earlier, they would have "
      "caught it."),
     ("What does she wish she had done?",
      "Brought the provision to the audit committee herself, instead of letting it sit in a report."),
     ("What did she have done, and what will she never allow again?",
      "She had the cut-off process re-tested; not once will she let an unreconciled number reach the board.")]))

S.append(L.s_listening(
    22, 5,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now the audit committee chair gives HER assessment of the CFO. "
    "This is what they say about you when you leave the room.' Toque 2 vezes. Este audio e emocionalmente potente: "
    "e o retrato de um CFO que ganhou a confianca do comite -- e e exatamente onde o Felipe quer chegar.",
    2, "Listening 2", "What They Say When You", "Leave the Room",
    "The audit committee chair, on the CFO. Sound first &mdash; no text.",
    "a8_listening_chair.mp3", SLUG,
    [("What does the chair say separates a good CFO from a great one?",
      "Not the numbers &mdash; every CFO has those. It is whether they tell you the bad news before you find it."),
     ("What does she say about the CFO who admitted the provision failure?",
      "That he should have disclosed it in March &mdash; but that owning it, unprompted, is why they still trust him."),
     ("What is her final test of a finance leader?",
      "Whether the committee ever has to ask twice.")]))

S.append(L.s_chapter(
    23, 6,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now the simulation. And from here I stop helping you.' "
    "Passe ao proximo.",
    "Chapter 6: Your Turn", "No More", "Help",
    "Detective &middot; The Report &middot; The Full Session", L.IMG['practice']))

S.append(L.s_error(
    24, 6,
    "<strong>Detective (5 min):</strong> Estes quatro erros vem das aulas 2, 3, 4 e 5. Felipe corrige ANTES de "
    "clicar E nomeia a aula de onde veio o erro. Se ele nomear as quatro, o Bloco 1 esta solido.",
    [("If we would have made a provision, the restatement didn't hurt.",
      "If we had made a provision, the restatement wouldn't have hurt."),
     ("We should protected our headroom instead of spending it.",
      "We should have protected our headroom instead of spending it."),
     ("I wish I would have listened to the audit committee.",
      "I wish I had listened to the audit committee."),
     ("She asked me did we disclose the impairment.",
      "She asked me whether we had disclosed the impairment.")]))

S.append(L.s_artifact(
    25, 6,
    "<strong>Artefato (5 min):</strong> Este e o sumario que o comite le ANTES de chamar o CFO. Peca que o Felipe "
    "leia cada linha e a transforme em fala -- MAS escolhendo uma estrutura DIFERENTE para cada linha. Seis linhas, "
    "seis ferramentas. E o exercicio mais completo do programa ate aqui.",
    "The Artifact", "The Audit Committee", "Summary",
    "AUDIT COMMITTEE", "Annual Close &middot; Confidential",
    [("Reviewed with", "Felipe Pimenta, CFO"),
     ("Restatement", "Revenue cut-off (not the audit)"),
     ("Provision", "Tax dispute &mdash; not disclosed in March"),
     ("Reconciliation", "Run late; re-tested since"),
     ("Materiality", "Below threshold, above embarrassment"),
     ("Covenant headroom", "2 points &mdash; monitored monthly"),
     ("Committee verdict", "Trust maintained. Ask once, not twice.")],
    [("Line 2 (restatement) &mdash; use an it-cleft.",
      "\"It was the revenue cut-off that forced the restatement, not the audit.\""),
     ("Line 3 (provision) &mdash; use a modal perfect, then a wish.",
      "\"It should have been disclosed in March. I wish I had brought it to you myself.\""),
     ("Line 4 (reconciliation) &mdash; use a causative.",
      "\"I had the cut-off process re-tested, and I got the controller to sign it off.\"")]))

S.append(L.s_quickfire(
    26, 6,
    "<strong>Quick fire (6 min):</strong> UMA pergunta por vez, e AGORA sem apoio: o Felipe escolhe a estrutura "
    "sozinho. Depois de cada resposta, faca UMA pergunta: 'which tool was that?'. Se ele nomear, ele consolidou. Se "
    "hesitar, marque a estrutura -- e ela vira prioridade nas aulas 9-16.",
    "Six Tools. No", "Hints."))

S.append(L.s_building(
    27, 6,
    "<strong>Sentence Building (5 min):</strong> Cada item pede uma ESTRUTURA diferente, nomeada entre parenteses. "
    "Felipe monta a frase COMPLETA em voz alta, depois clica para comparar. Toggle: clicar de novo fecha (REGRA "
    "27E). Este e o Bloco 1 inteiro em seis frases.",
    [("if / we / reconcile / earlier -> we / catch / it (third conditional)",
      "If we had reconciled earlier, we would have caught it."),
     ("we / protect / our headroom / instead of spending it (modal perfect: verdict)",
      "We should have protected our headroom instead of spending it."),
     ("I / bring / the provision to you myself (wish: regret)",
      "I wish I had brought the provision to you myself."),
     ("she / caution / the error / below materiality (reported speech)",
      "She cautioned that the error was below materiality."),
     ("I / the cut-off process / re-test (causative: the doer disappears)",
      "I had the cut-off process re-tested."),
     ("we / lack / liquidity / not profit (cleft: command the room)",
      "What we lacked was liquidity, not profit.")]))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Diana. Abra com: 'Three items: the restatement, the "
    "provision, the covenant.' Felipe usa as keywords. Este e o unico role-play da noite com apoio -- aproveite "
    "para calibrar antes de tirar tudo.",
    "The Three", "Items",
    "The audit committee puts three items on the table: the restatement, the undisclosed provision, and the covenant "
    "headroom. Take them in any order &mdash; but use a different structure for each.",
    ["It was ... that forced the restatement.", "It should have been disclosed in March.",
     "I wish I had brought it to you myself.", "I had the process re-tested."]))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Sem apoio na tela. Voce e a Diana, e agora ela pergunta a coisa "
    "que ninguem quer ouvir: 'Should we still trust your numbers?' O Felipe tem de responder usando pelo menos "
    "TRES estruturas diferentes, sem que voce diga quais. Se ele usar so uma, pare e devolva: 'Say that again -- "
    "with more than one tool.'",
    "Should We Still Trust Your", "Numbers?",
    "The chair asks the question that ends careers: after a restatement and an undisclosed provision, why should "
    "the committee still trust you? Answer with at least three different structures. Own what is yours. Command the "
    "room at the end.",
    []))

S.append(L.s_roleplay(
    30, 6,
    "<strong>Free Practice (6 min) &mdash; A PROVA:</strong> A sessao inteira do comite, ZERO pistas, 4 minutos "
    "cronometrados. NAO interrompa, NAO corrija. Grave (celular/Zoom) -- este audio e o MARCO DO MEIO do programa e "
    "vai ser comparado com a gravacao da aula 1 e com a da aula 16. Diga isso a ele ANTES: a comparacao e a prova de "
    "que ele mudou.",
    "The Full", "Session",
    "Chair the whole audit committee session, end to end, for four minutes. Analyze the restatement, own the "
    "provision, report what the auditor said, describe what you had done about it, and close by commanding the room "
    "with a single takeaway. Six tools. No help. This one is recorded.",
    []))

S.append(L.s_chapter(
    31, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'Eight lessons ago you could not take a screening call. "
    "Tonight you chaired an audit committee.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "Halfway,", "And Changed",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("It was the revenue cut-off that forced the restatement, not the audit.",
     "Foi o corte de receita que for&#231;ou a reapresenta&#231;&#227;o, n&#227;o a auditoria."),
    ("It should have been disclosed in March, and it was not. That one is mine.",
     "Deveria ter sido divulgado em mar&#231;o, e n&#227;o foi. Essa &#233; minha."),
    ("She cautioned that the error was below materiality, but not below embarrassment.",
     "Ela ponderou que o erro estava abaixo da materialidade, mas n&#227;o abaixo do constrangimento."),
    ("I had the cut-off process re-tested, and I got the controller to sign it off.",
     "Mandei retestar o processo de corte e fiz o controller assinar."),
    ("What we lacked was liquidity, not profit.",
     "O que nos faltou foi liquidez, n&#227;o lucro."),
]

S.append(L.s_survival(
    32, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Estas cinco frases sao, cada uma, uma "
    "ESTRUTURA diferente do Bloco 1. Peca que o Felipe nomeie a ferramenta de cada uma enquanto repete. E o resumo "
    "do programa inteiro em cinco linhas.",
    "Five Phrases, Five", "Tools",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    33, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 8 no passaporte (registra no Supabase).",
    N,
    ["I can choose the right structure under pressure, without being told which one.",
     "I can analyze the past (third conditional) and judge one action (modal perfects).",
     "I can repair a relationship (I wish) and carry someone's words (reported speech).",
     "I can report work I did not do (causative) and command a room (inversion + cleft).",
     "I know my words: liquidity, solvency, provision, materiality, impairment, headroom."]))

S.append(L.s_complete(
    34, 7,
    "<strong>Encerramento (3 min):</strong> Diga: 'Lesson 8 complete, Felipe. Halfway. You earned your Midpoint "
    "Badge.' Toque a gravacao da aula 1 se tiver, e depois a de hoje. A diferenca e o argumento. HOMEWORK "
    "(ORALMENTE, nunca escrito na tela): (1) ouvir as duas gravacoes -- aula 1 e aula 8 -- e escrever 3 frases "
    "sobre o que mudou; (2) escolher a estrutura que ele MAIS evitou hoje e usa-la 3 vezes numa reuniao real esta "
    "semana. Proxima aula: Defining What Matters -- investment narratives e relative clauses.",
    N, "Midpoint Badge", "Eight lessons ago you could not take a call. Tonight you chaired a committee.",
    "Defining What Matters -- Investment Narratives"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Progress Check and Integration -- Felipe at the Midpoint',
    'short_title': 'Progress Check and Integration',
    'menu_desc': 'Simula&#231;&#227;o integrada de comit&#234; de auditoria + as 6 estruturas do Bloco 1',
    'desc': ('Metade do caminho. Escolher a ferramenta certa sob press&#227;o, sem ningu&#233;m dizer qual. Key '
             'words: working capital, EBITDA, liquidity, solvency, audit committee, compliance, impairment, '
             'provision, reconciliation, to restate, materiality, headroom. Structures: INTEGRA&#199;&#195;O do '
             'Bloco 1 &mdash; third conditional (an&#225;lise), modal perfects (veredito), wish/if only '
             '(repara&#231;&#227;o), reported speech (carregar palavras), causative have/get (delegar) e '
             'inversion/cleft (comandar a sala).'),
    'hub_img': 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'diana': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. Repare: cada exemplo usa TAMB&#201;M uma das seis '
                    'estruturas que voc&#234; aprendeu nas aulas 2 a 7.'),

    'context_text': (
        'The annual close did not go well, and the <strong>audit committee</strong> wanted an explanation. '
        '<strong>It was the revenue cut-off that</strong> forced the <strong>restatement</strong> &mdash; not the '
        'audit, as the rumor had it. <strong>If the team had run the reconciliation</strong> a week earlier, they '
        '<strong>would have caught</strong> it before the close. Then there was the <strong>provision</strong> for '
        'the tax dispute, which <strong>should have been disclosed</strong> in March and was not. '
        '<strong>I wish I had brought it to the committee myself</strong>, Felipe said, instead of letting it sit in '
        'a report. The auditor <strong>cautioned that</strong> the error <strong>was</strong> below '
        '<strong>materiality</strong>, but not below embarrassment. So Felipe <strong>had</strong> the whole cut-off '
        'process <strong>re-tested</strong>, and he <strong>got</strong> the controller <strong>to sign</strong> it '
        'off personally. <strong>Not once will</strong> an unreconciled number reach that room again. On the '
        '<strong>covenant</strong>, the <strong>headroom</strong> is two points, monitored monthly. And on the '
        'question the committee actually cared about &mdash; <strong>what the company lacked was liquidity</strong>, '
        'not profit. <strong>EBITDA</strong> was never the problem. <strong>Solvency</strong> was never in doubt. '
        'Six structures, one letter: that is what a finance leader sounds like in English.'),

    'context_quiz': [
        ("\"It was the revenue cut-off that forced the restatement, not the audit.\" Qual ferramenta &#233; essa, e "
         "para que serve?",
         [("It-cleft &mdash; p&#245;e o holofote na causa REAL e exclui as alternativas (o boato de que foi a "
           "auditoria).", True),
          ("Third conditional &mdash; analisa um passado que n&#227;o aconteceu.", False),
          ("Reported speech &mdash; carrega as palavras de outra pessoa.", False)]),
        ("\"It should have been disclosed in March, and it was not.\" O que essa estrutura faz que o third "
         "conditional N&#195;O faria?",
         [("Ela d&#225; um VEREDITO sobre uma a&#231;&#227;o espec&#237;fica &mdash; n&#227;o apenas analisa um "
           "cen&#225;rio hipot&#233;tico.", True),
          ("Ela expressa arrependimento emocional, como o <em>wish</em>.", False),
          ("Ela reporta o que outra pessoa disse.", False)]),
        ("Which sentence is correct English?",
         [("She asked me did we disclose the impairment.", False),
          ("She asked me whether we had disclosed the impairment.", True),
          ("She asked me if we disclose the impairment?", False)]),
    ],

    'tip_title': 'As 6 Ferramentas do Bloco 1 (integra&#231;&#227;o)',
    'tip_intro': ('Uma tabela, seis ferramentas, seis trabalhos. O falante intermedi&#225;rio tem todas e pega a '
                  'errada. O fluente pega sem olhar.'),
    'tip_rows': [
        ("Third conditional (Aula 2)",
         "ANALISAR um passado que n&#227;o aconteceu. Sem culpa, s&#243; an&#225;lise.",
         "<strong>If we had</strong> reconciled earlier, we <strong>would have</strong> caught it."),
        ("Modal perfects (Aula 3)",
         "VEREDITO sobre UMA a&#231;&#227;o. <em>should</em> julga a pessoa; <em>could</em> julga a "
         "situa&#231;&#227;o.",
         "It <strong>should have been</strong> disclosed in March."),
        ("Wish / if only (Aula 4)",
         "REPARAR uma rela&#231;&#227;o. A &#250;nica ferramenta com emo&#231;&#227;o dentro.",
         "<strong>I wish I had</strong> brought it to you myself."),
        ("Reported speech (Aula 5)",
         "CARREGAR as palavras de outro com precis&#227;o. O tempo verbal recua.",
         "She <strong>cautioned that</strong> the error <strong>was</strong> below materiality."),
        ("Causative have/get (Aula 6)",
         "REPORTAR trabalho que aconteceu sem voc&#234;. O autor desaparece.",
         "I <strong>had</strong> the process <strong>re-tested</strong>."),
        ("Inversion + cleft (Aula 7)",
         "COMANDAR a sala &mdash; e comprar meio segundo para pensar.",
         "<strong>What we lacked was</strong> liquidity, not profit."),
    ],
    'tip_note': ('<strong>O teste do meio do caminho:</strong> voc&#234; j&#225; tem as seis ferramentas. O que '
                 'separa o intermedi&#225;rio do fluente n&#227;o &#233; conhecer mais estruturas &mdash; &#233; '
                 '<strong>alcan&#231;ar a certa sem olhar</strong>, sob press&#227;o, quando algu&#233;m acabou de '
                 'fazer uma pergunta dif&#237;cil. E os tr&#234;s erros que voltam sempre: a metade com <em>if</em> '
                 'nunca leva <strong>would</strong>; o <em>wish</em> sobre VOC&#202; nunca leva <strong>would</strong>; '
                 'e a pergunta reportada <strong>deixa de ser pergunta</strong>.'),

    'blanks': [
        ("If we had reconciled a week earlier, we", "would have caught",
         "Dica: an&#225;lise de um passado que n&#227;o aconteceu (Aula 2)",
         "If we had reconciled a week earlier, we would have caught it before the close.",
         "it before the close."),
        ("The provision", "should have been disclosed",
         "Dica: veredito sobre UMA a&#231;&#227;o (Aula 3)",
         "The provision should have been disclosed in March.", "in March."),
        ("I", "wish I had brought", "Dica: repara&#231;&#227;o &mdash; a ferramenta com emo&#231;&#227;o (Aula 4)",
         "I wish I had brought it to the committee myself.", "it to the committee myself."),
        ("She", "cautioned that", "Dica: carregar as palavras dela &mdash; e escolher o verbo certo (Aula 5)",
         "She cautioned that the error was below materiality.",
         "the error was below materiality."),
        ("I", "had the cut-off process re-tested",
         "Dica: o trabalho aconteceu, e n&#227;o foi voc&#234; que fez (Aula 6)",
         "I had the cut-off process re-tested before the auditors arrived.",
         "before the auditors arrived."),
        ("", "What we lacked was", "Dica: comandar a sala &mdash; e ganhar meio segundo (Aula 7)",
         "What we lacked was liquidity, not profit.", "liquidity, not profit."),
    ],

    'order_title': 'Put the Audit Committee Session in Order',
    'order_intro': ('Coloque as etapas de uma sess&#227;o de comit&#234; de auditoria na ordem correta. A ordem '
                    '&#233; o que separa um CFO em quem se confia de um CFO que se interroga.'),
    'order': [
        (2, "Own what is yours before anyone has to ask &mdash; the undisclosed provision."),
        (5, "Close by commanding the room: one takeaway, then stop talking."),
        (1, "Name the real cause with a cleft &mdash; and kill the rumor."),
        (4, "Say what you had done about it, and who signed it off."),
        (3, "Report exactly what the auditor said, with the verb she earned."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. Cada uma &#233; uma '
                     'ESTRUTURA diferente do Bloco 1 &mdash; nomeie a ferramenta enquanto repete.'),
    'speech': SURVIVAL,

    'quiz': [
        ("You want to ANALYZE a past that did not happen (no blame). You use:",
         [("\"We should have reconciled earlier.\"", False),
          ("\"If we had reconciled earlier, we would have caught it.\"", True),
          ("\"I wish we had reconciled earlier.\"", False)]),
        ("You want to give a VERDICT on one specific action that was not taken:",
         [("\"If it had been disclosed in March, this would not have happened.\"", False),
          ("\"It should have been disclosed in March, and it was not.\"", True),
          ("\"What we needed was disclosure in March.\"", False)]),
        ("You are talking to a PERSON you let down, and you want to repair it:",
         [("\"It should have been escalated to you.\"", False),
          ("\"I wish I had brought it to you myself.\"", True),
          ("\"If I had brought it to you, you would have known.\"", False)]),
        ("The auditor said the error was small but awkward. You REPORT her:",
         [("\"She said the error is below materiality.\"", False),
          ("\"She cautioned that the error was below materiality, but not below embarrassment.\"", True),
          ("\"She asked was the error below materiality.\"", False)]),
        ("You want to COMMAND the room and name the one thing that mattered:",
         [("\"We didn't have enough liquidity, and profit was fine.\"", False),
          ("\"What we lacked was liquidity, not profit.\"", True),
          ("\"I wish we had had more liquidity.\"", False)]),
    ],

    'think': ("Chair a full audit committee session, out loud, for 3 minutes. You must use all six structures at "
              "least once: analyze the restatement (third conditional), give a verdict on the undisclosed provision "
              "(modal perfect), repair it with the committee (I wish), report what the auditor said (reported "
              "speech), describe what you had re-tested (causative), and close by commanding the room (cleft or "
              "inversion). Nobody will tell you which tool to use. Record this one &mdash; it is your midpoint "
              "baseline."),

    'listenings': [
        {"file": "a8_listening_cfo.mp3", "voice": "ellen",
         "text": ("Thank you. I will take the three items in the order the committee raised them. First, the "
                  "restatement. It was the revenue cut-off that forced it, not the audit, and I want to correct "
                  "that rumor here. If we had run the reconciliation a week earlier, we would have caught the "
                  "problem before the close, and none of us would be in this room tonight. Second, the provision "
                  "for the tax dispute. It should have been disclosed to you in March, and it was not. I wish I had "
                  "brought it to you myself instead of letting it sit inside a report that nobody was going to "
                  "read. That one is mine, and I am not going to dress it up. Third, what the auditor actually "
                  "said. She cautioned that the error was below materiality but not below embarrassment. Those were "
                  "her words, and I think they were fair. So here is what has happened since. I had the entire "
                  "cut-off process re-tested by an external firm, and I got the controller to sign it off "
                  "personally, in writing. Not once will an unreconciled number reach this committee again. What we "
                  "lacked this year was liquidity. It was never profit, and it was never solvency.")},
        {"file": "a8_listening_chair.mp3", "voice": "arthur",
         "text": ("People ask me what separates a good chief financial officer from a great one, and they always "
                  "expect me to say something about the numbers. It is never the numbers. Every CFO who reaches this "
                  "level has the numbers. What separates them is whether they tell you the bad news before you find "
                  "it yourself. Let me give you a real example. Last year our CFO came to the committee about a "
                  "provision that had not been disclosed. Nobody had asked him. Nobody would have found it for "
                  "another two quarters. He should have disclosed it in March, and he said so, in those words, "
                  "without being prompted and without a lawyer next to him. And that, precisely that, is why this "
                  "committee still trusts him. Here is my test, and it has never failed me. Does the committee ever "
                  "have to ask twice? If you have to ask a finance leader the same question twice, you do not have a "
                  "reporting problem. You have a trust problem, and no amount of reconciliation will fix it.")},
    ],

    'inclass_blocks': {
        "reading": [{
            "kind": "reading",
            "rtitle": "Letter from the Audit Committee &mdash; Annual Close",
            "paras": [
                ("The committee has reviewed the annual close and wishes to record the following. It was the revenue "
                 "cut-off that forced the restatement, and not the external audit, as had been suggested in some "
                 "quarters. Had the reconciliation been run a week earlier, the error would have been caught before "
                 "the close, and the restatement would not have been necessary at all."),
                ("On the provision for the tax dispute, the committee is less forgiving. It should have been "
                 "disclosed in March. It was not. The chief financial officer has acknowledged this without being "
                 "prompted, and told the committee, in his own words, that he wishes he had brought the matter to "
                 "us directly rather than allowing it to sit inside a report. The committee notes the candor and "
                 "considers the matter closed."),
                ("The external auditor cautioned that the error fell below materiality but, in her phrase, not below "
                 "embarrassment. The committee agrees. In response, the chief financial officer has had the entire "
                 "cut-off process re-tested by an independent firm and has had the controller sign it off "
                 "personally. Not once, he assured us, will an unreconciled figure reach this committee again."),
                ("On the covenant, headroom stands at two points and is now monitored monthly rather than quarterly. "
                 "The committee wishes to underscore a final point, because it has been widely misunderstood inside "
                 "the business. What the company lacked this year was liquidity. It was not profit, and it was never "
                 "solvency. EBITDA was never the issue. Cash, as always, was."),
            ],
            "source": "Audit Committee &mdash; Annual Close, item 4",
        }],
        "gist": [{
            "kind": "gist",
            "prompt": "What is the best one-line summary of this letter?",
            "choices": [
                ["a", "The committee has lost confidence in the CFO and is recommending his removal.", False],
                ["b", "The restatement was caused by a late reconciliation and the provision should have been "
                      "disclosed sooner; the CFO owned both unprompted, fixed the process, and the committee's "
                      "trust holds &mdash; the real problem was liquidity, not profit.", True],
                ["c", "The external audit made an error that forced the company to restate its results.", False],
            ],
        }],
        "tf": [{
            "kind": "tf",
            "items": [
                ["The external audit caused the restatement.", "f",
                 "It was the revenue cut-off that forced it &mdash; the letter corrects that suggestion explicitly."],
                ["The provision for the tax dispute was disclosed to the committee in March.", "f",
                 "It should have been disclosed in March, and it was not."],
                ["The CFO admitted the failure without being asked.", "t",
                 "He acknowledged it unprompted, and told the committee he wished he had brought it directly."],
                ["The auditor said the error was above materiality.", "f",
                 "She cautioned that it fell below materiality but, in her phrase, not below embarrassment."],
                ["The company's core problem was a lack of profit.", "f",
                 "What it lacked was liquidity. It was not profit, and it was never solvency."],
            ],
        }],
        "guiding": [{
            "kind": "guiding",
            "items": [
                "Find one third conditional, one modal perfect, one wish, one reported speech, one causative and one "
                "cleft in this letter. Read each one out loud and name the tool.",
                "The committee \"notes the candor and considers the matter closed.\" Why did owning it unprompted "
                "change the outcome &mdash; and would that work in your company?",
                "\"Below materiality, but not below embarrassment.\" What is the equivalent line in your own "
                "business right now?",
                "Halfway through this programme: which of the six tools do you still avoid when you are under "
                "pressure &mdash; and why that one?",
            ],
        }],
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Did the audit cause the restatement?\"",
                 "tips": ["It was the revenue cut-off that forced it, not the audit.",
                          "Tool: it-cleft. Kill the rumor, name the cause."]},
                {"situation": "\"Could this have been avoided?\"",
                 "tips": ["If we had run the reconciliation a week earlier, we would have caught it.",
                          "Tool: third conditional. Analysis, not blame."]},
                {"situation": "\"Why were we not told about the provision?\"",
                 "tips": ["It should have been disclosed in March, and it was not. That one is mine.",
                          "Tool: modal perfect. A verdict, and you take it."]},
                {"situation": "\"Do you regret how you handled it?\"",
                 "tips": ["I wish I had brought it to you myself.",
                          "Tool: wish. The only one with emotion in it."]},
                {"situation": "\"What did the auditor actually say?\"",
                 "tips": ["She cautioned that the error was below materiality, but not below embarrassment.",
                          "Tool: reported speech. Her verb, her words."]},
                {"situation": "\"So what have you actually done about it?\"",
                 "tips": ["I had the cut-off process re-tested, and I got the controller to sign it off.",
                          "Tool: causative. Then close with a cleft."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Industry -- Season 3 (HBO Max)",
         "A temporada em que os personagens finalmente t&#234;m de responder por tudo o que fizeram nas duas "
         "anteriores. Connection to Lesson 8: escolha UMA cena de confronto e identifique as seis estruturas do "
         "Bloco 1 nela.",
         "Dica: assista com legenda em ingl&#234;s. Pause a cada estrutura que reconhecer e nomeie a ferramenta em "
         "voz alta.",
         "https://www.hbo.com/industry"),
        ("Podcast", "podcast", "Planet Money (NPR) -- epis&#243;dios sobre restatements e fraudes cont&#225;beis",
         "Hist&#243;rias reais de empresas que tiveram de reapresentar demonstra&#231;&#245;es &mdash; com o "
         "vocabul&#225;rio exato desta aula. Connection to Lesson 8: liquidity, provision, materiality e restate no "
         "contexto em que doem.",
         "Dica: ou&#231;a a 1x. Escolha 5 frases e reescreva cada uma com uma ferramenta diferente do Bloco 1.",
         "https://www.npr.org/sections/money/"),
        ("YouTube", "youtube", "Aswath Damodaran -- liquidez, solv&#234;ncia e a diferen&#231;a que mata empresas",
         "O professor de valuation explicando por que lucro n&#227;o &#233; caixa &mdash; a tese central da carta "
         "desta aula. Connection to Lesson 8: &#233; o argumento do &#250;ltimo par&#225;grafo, desenvolvido em "
         "detalhe.",
         "Dica: assista a 0.75x se precisar. Depois explique a diferen&#231;a liquidity/solvency em voz alta, em "
         "ingl&#234;s, em 60 segundos.",
         "https://www.youtube.com/@AswathDamodaranonValuation"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
