#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 9 — Defining What Matters (Investment Narratives).
Gramatica: relative clauses (defining vs non-defining, that/which/who, reduced, whose).
Modelo: PADRAO-FALA (aula IMPAR, REGRA 29) — dialogo line-by-line + role-play.
Callback (REGRA 20): o warm-up retoma as 6 ferramentas do Bloco 1 (aula 8).

Ponto pedagogico: a virgula MUDA O FATO. "The analysts who left" (alguns sairam) vs
"The analysts, who left" (TODOS sairam). Para um CFO, isso nao e estilo — e risco legal.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 9
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Thesis", "the core argument for why an investment will work",
     "tese de investimento",
     "The thesis that underpins this round is very simple."),
    ("Moat", "the durable advantage your competitors cannot copy",
     "barreira competitiva, moat",
     "A moat that a competitor can buy is not a moat."),
    ("Traction", "real evidence that customers actually want it",
     "tra&#231;&#227;o",
     "Traction is the only number investors believe without checking."),
    ("Unit economics", "whether a single customer makes you money",
     "economia unit&#225;ria",
     "The unit economics, which improved all year, are now positive."),
    ("Churn", "the rate at which customers leave you",
     "churn, taxa de cancelamento",
     "The churn that worried us in March has halved."),
    ("Scalability", "whether growth gets cheaper as you get bigger",
     "escalabilidade",
     "Scalability is what separates a business from a job."),
    ("Addressable market", "the customers you could realistically reach",
     "mercado endere&#231;&#225;vel",
     "The addressable market, which nobody has measured properly, is the weak part."),
    ("Differentiator", "the one thing that makes a customer choose you",
     "diferencial",
     "Our differentiator is the licence that took four years to win."),
    ("Track record", "the proof of what you have actually done before",
     "hist&#243;rico comprovado",
     "Investors back a track record, not a forecast."),
    ("To underpin", "to be the foundation that something rests on",
     "sustentar, embasar",
     "The assumption that underpins the model is the one to attack first."),
    ("Value creation", "the real increase in worth that you produce",
     "gera&#231;&#227;o de valor",
     "Value creation is not the same as growth, and the board confuses them."),
    ("Exit", "how the investors eventually get their money out",
     "sa&#237;da, exit",
     "Nobody funds a company whose exit nobody can describe."),
]

PHASES = ["The Pitch", "The Language of the Thesis", "The Code",
          "The Investor", "Practice", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Tonight, precision. Not the numbers -- you have "
    "those. The comma. Because in English a comma can change a fact, and a CFO who does not control that is a CFO "
    "who signs things he did not mean.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 9 &middot; Precision", "Defining What", "Matters",
    "One comma. Two completely different companies. Tonight we take control of it."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 8 ANTES do tema novo (REGRA 20). Peca DUAS "
    "ferramentas diferentes numa frase so sobre a semana dele. Depois abra o tema com a pergunta de investidor: "
    "'In one sentence: why would somebody invest in your company?' Deixe falar. Anote se ele consegue definir sem "
    "listar.",
    "Chapter 1: The Pitch",
    "Why Would Anyone Invest in Your", "Company?",
    "One sentence. Not a list of features &mdash; an argument."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Mostre o poder da virgula com o exemplo mais violento que existe para "
    "um CFO. Escreva as duas frases e pergunte: 'How many analysts do we still have?' Na primeira, alguns ficaram. "
    "Na segunda, TODOS sairam. Mesmas palavras. Uma virgula. Diga: 'This is not style. In a contract, this is "
    "money.'",
    "One Comma. Two Companies.", "The Comma Changes the", "Fact",
    [("\"The analysts who left...\"", "SOME left. Others stayed. (defining)"),
     ("\"The analysts, who left, ...\"", "ALL of them left. (non-defining)"),
     ("In a contract", "that difference is a number &mdash; and a lawsuit")],
    "The clause without commas DEFINES which ones you mean. The clause with commas is an aside — it applies to all of them."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of an investment thesis, the relative "
    "clause -- which defines and which merely describes -- and a real pitch to the investor who has already backed "
    "you once.' Antecipe: o role-play final e a defesa da tese dele sob ataque.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "thesis, moat, traction, churn, unit economics..."),
     ("2. The Code", "that / which / who &middot; the comma that changes everything"),
     ("3. The Pitch", "defend your thesis to an investor who knows you")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words. Every one of them appears in the first two "
    "minutes of any investment conversation you will ever have.' Passe ao proximo.",
    "Chapter 2: The Language of the Thesis", "The Words of an Investment", "Case",
    "12 words &mdash; the vocabulary of the pitch.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'moat': 'If a "
    "competitor can buy the same technology tomorrow, is it a moat? (No -- a moat must be hard to copy.)' CCQ "
    "'traction': 'Is a signed letter of intent traction? (Weak traction. Revenue is traction.)' CCQ 'unit "
    "economics': 'If we lose money on every customer but grow fast, do we have a business? (No -- we have a very "
    "expensive hobby.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'To underpin' e 'value creation' sao o coracao da "
    "aula. CCQ 'to underpin': 'If an assumption underpins the model, what happens if it is wrong? (Everything above "
    "it falls.)' CCQ 'value creation vs growth': 'Can a company grow and destroy value at the same time? (Yes -- and "
    "most do.)' Esse CCQ costuma acender o Felipe, porque e o mundo dele.",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'thesis' (THEE-sis -- o brasileiro diz 'TE-sis'), "
    "'moat' (rima com 'boat' -- som limpo, uma silaba), 'churn' (CHURN -- o /ɜr/ e dificil, nao e 'shern'), "
    "'scalability' (skay-la-BIL-i-ty). 'Churn' mal pronunciado e a palavra que mais faz investidor pedir para "
    "repetir.",
    ["Thesis", "Moat", "Churn", "Scalability", "Traction"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Repare: cada frase ja contem uma relative clause. Aponte isso.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"The assumption that underpins the model is the ", "thesis", " of the whole round.\""),
     ("\"A ", "moat", " that a competitor can buy is not a moat.\""),
     ("\"The ", "churn", " that worried us in March has halved.\""),
     ("\"Nobody funds a company whose ", "exit", " nobody can describe.\""),
     ("\"Investors back a ", "track record", ", not a forecast.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. Two clauses that look identical and mean "
    "opposite things. The difference is a comma -- and the difference is your job.' Passe ao proximo.",
    "Chapter 3: The Code", "Defining vs", "Describing",
    "The comma that changes the fact", L.IMG['code']))

S.append(L.s_discovery(
    11, 3,
    "<strong>Grammar discovery (8 min):</strong> NAO de a regra primeiro. Leia os pares 1 e 2 e faca A PERGUNTA: "
    "'How many analysts do we still have, in each sentence?' Espere. Este e o momento em que a aula acerta. So "
    "depois leia 3 e 4, e so entao clique 'Reveal the Rule'. CCQ: 'If I remove the clause, does the sentence still "
    "identify WHICH ones? If yes -- the clause is extra, so it takes commas. If no -- it is essential, no commas.'",
    [("\"The analysts <span style=\"color:#dc2626;font-weight:700\">who left</span> took the model with them.\" "
      "<em>(some left)</em>",
      "The analysts who left took the model with them."),
     ("\"The analysts<span style=\"color:#15803d;font-weight:700\">, who left,</span> took the model with them.\" "
      "<em>(they ALL left)</em>",
      "The analysts, who left, took the model with them."),
     ("\"The assumption <span style=\"color:#dc2626;font-weight:700\">that underpins</span> the model is "
      "optimistic.\"",
      "The assumption that underpins the model is optimistic."),
     ("\"Our lead investor<span style=\"color:#15803d;font-weight:700\">, who has backed us since 2019,</span> is "
      "in.\"",
      "Our lead investor, who has backed us since 2019, is in.")],
    "Sentences 1 and 2 have the same words. So tell me: in each one, "
    "<span style=\"color:#dc2626;font-weight:700\">how many analysts do we still have?</span>",
    [("Defining (no commas)",
      "Tells you WHICH ones. Essential &mdash; remove it and you no longer know who you mean.",
      "The analysts <strong>who left</strong> took the model. <em>(only those)</em>"),
     ("Non-defining (commas)",
      "Extra information about ALL of them. Remove it and the fact survives.",
      "The analysts<strong>, who left,</strong> took the model. <em>(all of them)</em>"),
     ("that / which / who",
      "<em>that</em> only in DEFINING clauses. <em>which</em> and <em>who</em> in both. Never <em>that</em> after "
      "a comma.",
      "the metric <strong>that</strong> matters / the metric, <strong>which</strong> matters,..."),
     ("Reduced relative",
      "Drop <em>that is / which are</em> entirely. Sounds far more native and saves you two words.",
      "the risks <strong>driving</strong> churn = the risks <em>that are</em> driving churn"),
     ("whose",
      "Possession &mdash; for people AND for companies.",
      "a company <strong>whose</strong> exit nobody can describe"),
     ("Preposition at the end",
      "Natural, correct English. Do not force <em>from which</em> unless you are writing a contract.",
      "the fund <strong>we raised from</strong> (not: from which we raised)"),
    ],
    "The test that never fails: <strong>take the clause out.</strong> If you still know WHICH ones you mean, the "
    "clause was extra &mdash; put the commas back. If you no longer know, it was essential &mdash; no commas.",
    "rule9"))

S.append(L.s_mistake(
    12, 3,
    "<strong>Common mistake (4 min):</strong> Tres erros. (1) 'that' depois de virgula -- NUNCA existe. (2) A "
    "virgula que muda o fato sem o Felipe perceber -- e o erro caro. (3) 'which' para pessoa (e who). Peca que ele "
    "leia as certas DUAS vezes E explique o que a virgula fez em cada uma.",
    [("Our lead investor, that has backed us since 2019, is in.",
      "Our lead investor, who has backed us since 2019, is in."),
     ("The analysts, who left, took the model. (when only SOME left)",
      "The analysts who left took the model. (no commas = only those who left)"),
     ("The assumption, that underpins the model, is optimistic.",
      "The assumption that underpins the model is optimistic.")],
    "<strong>that</strong> never follows a comma. And the comma is not decoration: without it the clause DEFINES "
    "which ones; with it, the clause describes ALL of them. In a contract, that is a number."))

S.append(L.s_fill(
    13, 3,
    "<strong>Practice (4 min):</strong> Leia cada frase. Felipe escolhe o relativo ORALMENTE antes de clicar. Se "
    "travar, pergunte: 'Does this clause tell me WHICH one, or is it just extra?'",
    "Practice", "That, Which, or", "Who?", "Say it first, then click to check",
    [("\"The assumption ", "that", " underpins the model is the one to attack first.\""),
     ("\"Our lead investor, ", "who", " has backed us since 2019, is in for the round.\""),
     ("\"The unit economics, ", "which", " improved all year, are now positive.\""),
     ("\"Nobody funds a company ", "whose", " exit nobody can describe.\""),
     ("\"That is the fund ", "we raised from", " in 2022.\"")]))

S.append(L.s_fill(
    14, 3,
    "<strong>Reduced relatives (4 min):</strong> Esta e a marca do falante avancado: cortar 'that is / which are' e "
    "deixar so o particípio. Felipe produz a versao CURTA em voz alta antes de clicar. Duas palavras a menos, e o "
    "ingles fica nativo. Peca que ele sinta a diferenca de ritmo.",
    "Sound Native", "Cut the", "Words", "Say the shorter version first, then click to check",
    [("\"the risks that are driving our churn\" &rarr; \"the risks ", "driving", " our churn\""),
     ("\"the metric which was mentioned by the board\" &rarr; \"the metric ", "mentioned", " by the board\""),
     ("\"the assumption which underpins the model\" &rarr; \"the assumption ", "underpinning", " the model\""),
     ("\"the customers who are leaving us every month\" &rarr; \"the customers ", "leaving", " us every month\"")]))

S.append(L.s_chapter(
    15, 4,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Ingrid backed you once. That is worse than a stranger -- she "
    "remembers what you promised last time.' Passe ao proximo.",
    "Chapter 4: The Investor", "The Investor Who Already", "Backed You",
    "She remembers what you promised", L.IMG['context']))

S.append(L.s_dialogue(
    16, 4,
    "<strong>Dialogo (7 min):</strong> Voce e a Ingrid. Clique 'Next Line' a cada fala. Para cada fala do Felipe, "
    "peca que ELE fale primeiro. Observe se as relative clauses saem sozinhas -- e se ele consegue DEFINIR sem "
    "listar. Se ele listar features, pare e devolva: 'That is a list. Give me the thesis.'",
    "Defending the", "Thesis",
    [("ingrid", "I", "ellen",
      "Felipe, I backed you in 2022 on a thesis that turned out to be half right. Give me the new one, in one "
      "sentence.",
      "Felipe, I backed you in 2022 on a thesis that turned out to be half right. Give me the new one, in one "
      "sentence."),
     ("felipe", "F", "arthur",
      "The <span class=\"vocab-highlight\">thesis</span> is the licence. Our "
      "<span class=\"vocab-highlight\">differentiator</span> is a regulatory licence that took four years to win "
      "and that a competitor cannot simply buy.",
      "The thesis is the licence. Our differentiator is a regulatory licence that took four years to win and that a "
      "competitor cannot simply buy."),
     ("ingrid", "I", "ellen",
      "That is a <span class=\"vocab-highlight\">moat</span>. What about the "
      "<span class=\"vocab-highlight\">churn</span> that worried me last time?",
      "That is a moat. What about the churn that worried me last time?"),
     ("felipe", "F", "arthur",
      "The churn that worried you in March has halved. And the "
      "<span class=\"vocab-highlight\">unit economics</span>, which improved every quarter this year, are now "
      "positive &mdash; that is the number I would attack if I were you.",
      "The churn that worried you in March has halved. And the unit economics, which improved every quarter this "
      "year, are now positive. That is the number I would attack if I were you."),
     ("ingrid", "I", "ellen",
      "Then I will. What is the weakest part of your case?",
      "Then I will. What is the weakest part of your case?"),
     ("felipe", "F", "arthur",
      "The <span class=\"vocab-highlight\">addressable market</span>, which nobody has measured properly. The "
      "assumption that <span class=\"vocab-highlight\">underpins</span> our model is a market size that I cannot "
      "prove. I would rather tell you that now than have you find it in the data room.",
      "The addressable market, which nobody has measured properly. The assumption that underpins our model is a "
      "market size that I cannot prove. I would rather tell you that now than have you find it in the data room.")]))

S.append(L.s_comprehension(
    17, 4,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a INGRID, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Ingrid",
    [("What does Ingrid say about the thesis she backed in 2022?",
      "That it turned out to be only half right."),
     ("Which number did she worry about last time?",
      "The churn."),
     ("What does she ask for at the end?",
      "The weakest part of his case.")]))

S.append(L.s_listening(
    18, 4,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CFO delivers an investment thesis in ninety seconds. Listen for "
    "the relative clauses -- they are how he defines without listing.' Toque SEM texto, 2 vezes. Peca que ele CONTE "
    "as defining clauses.",
    1, "Listening", "The Ninety-Second", "Thesis",
    "How to define a company without listing its features. Sound first &mdash; no text.",
    "a9_listening_cfo.mp3", SLUG,
    [("What does he say the differentiator is?",
      "A regulatory licence that took four years to win and that a competitor cannot buy."),
     ("What does he say about the unit economics?",
      "That they improved every quarter and are now positive."),
     ("What does he volunteer as the weakest part?",
      "The addressable market, which nobody has measured properly.")]))

S.append(L.s_listening(
    19, 4,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now an investor explains what makes a thesis credible -- and what "
    "makes her walk away.' Toque 2 vezes. Depois pergunte: 'She says the best founders name their own weakest "
    "number. Why does that work?' E a licao mais valiosa da aula para uma entrevista.",
    2, "Listening 2", "What Makes an Investor", "Believe You",
    "An investor, on the thesis she funds. Sound first &mdash; no text.",
    "a9_listening_investor.mp3", SLUG,
    [("What does she say a thesis is NOT?",
      "A list of features &mdash; it is an argument, and it must be one sentence."),
     ("What does she say about founders who name their own weakest number?",
      "They earn credibility &mdash; because she will find it anyway, and the only question is who says it first."),
     ("What kind of moat does she refuse to fund?",
      "One a competitor can simply buy.")]))

S.append(L.s_chapter(
    20, 5,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the memo, and the questions "
    "investors ask when they are already interested.' Passe ao proximo.",
    "Chapter 5: Practice", "Define It", "Precisely",
    "Detective &middot; The Memo &middot; Quick Fire", L.IMG['practice']))

S.append(L.s_error(
    21, 5,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar E explica o que a "
    "virgula fez. O terceiro item e o mais importante da aula: o erro que muda o FATO, nao so a gramatica.",
    [("Our lead investor, that has backed us since 2019, is in.",
      "Our lead investor, who has backed us since 2019, is in."),
     ("The assumption, that underpins the model, is optimistic.",
      "The assumption that underpins the model is optimistic."),
     ("The analysts, who left, took the model with them. (only two of six left)",
      "The analysts who left took the model with them. (no commas = only those two)"),
     ("Nobody funds a company which exit nobody can describe.",
      "Nobody funds a company whose exit nobody can describe.")]))

S.append(L.s_artifact(
    22, 5,
    "<strong>Artefato (5 min):</strong> Este e o memo de investimento que a Ingrid vai levar ao comite dela. Peca "
    "que o Felipe leia cada linha e a transforme numa frase com relative clause -- DEFINING quando estiver "
    "restringindo, NON-DEFINING quando estiver comentando. E aqui que a virgula sai da teoria.",
    "The Artifact", "The Investment", "Memo",
    "INVESTMENT MEMO", "Series B &middot; Confidential",
    [("Company", "Fintech (Brazil) &mdash; CFO: F. Pimenta"),
     ("Thesis", "The regulatory licence"),
     ("Moat", "4 years to win; cannot be bought"),
     ("Churn", "Halved since March"),
     ("Unit economics", "Positive; improved every quarter"),
     ("Weakest point", "Addressable market &mdash; unmeasured"),
     ("Lead investor", "I. M&oslash;ller &mdash; backed since 2022")],
    [("Say the Moat line with a DEFINING clause (no commas).",
      "\"Our differentiator is a licence that took four years to win and that a competitor cannot buy.\""),
     ("Say the Lead investor line with a NON-DEFINING clause (commas).",
      "\"Our lead investor, who has backed us since 2022, is in for this round.\""),
     ("Say the Weakest point line &mdash; and choose the comma deliberately.",
      "\"The addressable market, which nobody has measured properly, is the weak part of the case.\"")]))

S.append(L.s_quickfire(
    23, 5,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO, com relative "
    "clause. REGRA: nada de listas. Se ele listar features, pare e devolva: 'That is a list. Define it.' Investidor "
    "pergunta rapido de proposito -- e sob essa velocidade que ele volta a listar.",
    "The Investor Asks. You", "Define."))

S.append(L.s_building(
    24, 5,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords E se a clause deve ser defining ou non-defining. "
    "Felipe monta a frase COMPLETA em voz alta, depois clica para comparar. Toggle: clicar de novo fecha (REGRA "
    "27E).",
    [("our differentiator / a licence / take four years to win (DEFINING, no commas)",
      "Our differentiator is a licence that took four years to win."),
     ("our lead investor / back us since 2022 / is in (NON-DEFINING, commas)",
      "Our lead investor, who has backed us since 2022, is in."),
     ("the churn / worry you in March / has halved (DEFINING, no commas)",
      "The churn that worried you in March has halved."),
     ("the unit economics / improve every quarter / are positive (NON-DEFINING, commas)",
      "The unit economics, which improved every quarter, are positive."),
     ("nobody funds a company / exit / nobody can describe (whose)",
      "Nobody funds a company whose exit nobody can describe.")]))

S.append(L.s_chapter(
    25, 6,
    "<strong>Transicao role-play (1 min):</strong> Diga: 'Now you pitch. And the investor in front of you has "
    "already lost money on your last thesis.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Make the", "Case",
    "Guided &gt; Semi-free &gt; Free", L.IMG['turn']))

S.append(L.s_roleplay(
    26, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Ingrid. Abra com: 'Give me the thesis, in one sentence.' "
    "Felipe usa as keywords. O teste: ele DEFINE ou ele LISTA? Se listar, corte e peca de novo.",
    "The Thesis in One", "Sentence",
    "An investor asks for your thesis in one sentence. Define the company &mdash; do not list its features. Name the "
    "moat, and say precisely why a competitor cannot copy it.",
    ["The thesis is...", "Our differentiator is a ... that...",
     "The moat is the ... which...", "The assumption that underpins it is..."]))

S.append(L.s_roleplay(
    27, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. A Ingrid ataca o numero MAIS FRACO -- e ela ja "
    "sabe qual e. 'Your addressable market is a guess, Felipe.' Ele tem de CONCEDER com precisao (non-defining) e "
    "reconstruir a tese em cima do que e solido (defining). Se ele defender o indefensavel, perdeu a credibilidade.",
    "She Attacks Your Weakest", "Number",
    "The investor goes straight at the addressable market: \"That number is a guess.\" She is right. Concede it "
    "precisely, then rebuild the case on what you CAN prove &mdash; the licence, the churn, the unit economics.",
    ["You are right, and the addressable market, which...", "What I can prove is the ... that...",
     "The churn that worried you...", "I would rather tell you now than..."],
    tint='.12'))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: o pitch inteiro, ZERO pistas, 3 minutos cronometrados. "
    "NAO interrompa. Peca ANTES: 'Define the company in one sentence, then defend it. And name your own weakest "
    "number before I do.' CELEBRE se ele nomear a fraqueza sozinho -- e a marca de senioridade que investidor "
    "compra.",
    "The Whole", "Pitch",
    "Three minutes. Define the company in one sentence. Name the moat and why it cannot be copied. Give the traction "
    "and the unit economics. Then name your own weakest number before the investor finds it &mdash; and say what you "
    "will do about it.",
    []))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Extensao / a entrevista (4 min):</strong> So faca se sobrar tempo. Vire o cenario para a CARREIRA dele "
    "(trilha 30% Career): 'Now define YOURSELF the way you just defined the company. What is the licence that took "
    "you four years to win? What is your moat?' Este e o exercicio que conecta a aula 9 a aula 14 -- e costuma ser "
    "o momento mais forte do programa.",
    "Now Define", "Yourself",
    "Same structure, different subject: define your own career the way you just defined the company. What is the "
    "thing you have that took years to build and that a rival cannot simply buy? What is your track record, and "
    "what is your weakest number?",
    []))

S.append(L.s_chapter(
    30, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'Tonight you stopped listing and started defining. Investors "
    "fund definitions, not lists.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You", "Defined It",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("Our differentiator is a licence that took four years to win and that a competitor cannot buy.",
     "Nosso diferencial &#233; uma licen&#231;a que levou quatro anos para ser obtida e que um concorrente n&#227;o "
     "pode comprar."),
    ("The churn that worried you in March has halved.",
     "O churn que preocupou voc&#234; em mar&#231;o caiu pela metade."),
    ("The unit economics, which improved every quarter, are now positive.",
     "A economia unit&#225;ria, que melhorou a cada trimestre, agora &#233; positiva."),
    ("The assumption that underpins the model is the one I cannot prove.",
     "A premissa que sustenta o modelo &#233; a que eu n&#227;o consigo comprovar."),
    ("I would rather tell you now than have you find it in the data room.",
     "Prefiro te contar agora a deixar voc&#234; descobrir na data room."),
]

S.append(L.s_survival(
    31, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita e diga, em "
    "cada uma, se a clause e defining ou non-defining. A ultima e a mais valiosa da aula: e a frase que compra "
    "credibilidade com qualquer investidor.",
    "Five Phrases for the", "Pitch",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    32, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 9 no passaporte (registra no Supabase).",
    N,
    ["I can use a defining clause (no commas) to say WHICH one I mean.",
     "I can use a non-defining clause (commas) to add information about all of them.",
     "I know that 'that' never follows a comma, and that 'who' is for people.",
     "I can reduce a relative clause (the risks driving churn) and sound native.",
     "I know my words: thesis, moat, traction, churn, unit economics, to underpin."]))

S.append(L.s_complete(
    33, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 9 complete, Felipe. You earned your Precision Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) escrever a tese da empresa dele em UMA frase com defining "
    "clause, e gravar dizendo ate sair sem pensar; (2) escrever as mesmas duas frases sobre os analistas -- com e "
    "sem virgula -- e explicar em voz alta a diferenca de FATO. Proxima aula: Negotiating Your Future -- a "
    "transicao internacional, mixed conditionals e gerunds vs infinitives.",
    N, "Precision Badge", "You stopped listing, Felipe. You defined it.",
    "Negotiating Your Future -- Career Transition"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Defining What Matters -- Investment Narratives',
    'short_title': 'Defining What Matters',
    'menu_desc': 'Defender uma tese de investimento + relative clauses',
    'desc': ('Definir, e n&#227;o listar &mdash; e controlar a v&#237;rgula que muda o FATO. Key words: thesis, '
             'moat, traction, unit economics, churn, scalability, addressable market, differentiator, track record, '
             'to underpin, value creation, exit. Structures: relative clauses &mdash; defining (sem v&#237;rgula: '
             'diz QUAL) vs non-defining (com v&#237;rgula: comenta TODAS), that/which/who, whose, relativas '
             'reduzidas (the risks driving churn) e preposi&#231;&#227;o no fim.'),
    'hub_img': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'ingrid': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. Repare que cada exemplo J&#193; cont&#233;m uma relative '
                    'clause &mdash; &#233; assim que se define sem listar.'),

    'context_text': (
        'Ingrid backed the company in 2022 on a <strong>thesis</strong> <strong>that</strong> turned out to be half '
        'right. This time Felipe led with the argument, not the features. The <strong>differentiator</strong>, he '
        'said, is a regulatory licence <strong>that took four years to win</strong> and <strong>that a competitor '
        'cannot simply buy</strong> &mdash; and a <strong>moat</strong> <strong>that a rival can buy</strong> is not '
        'a moat at all. The <strong>churn</strong> <strong>that had worried her in March</strong> has halved. The '
        '<strong>unit economics</strong><strong>, which improved every quarter this year,</strong> are now positive. '
        'Notice the difference. <em>The churn that worried her</em> has no commas, because it tells you WHICH churn. '
        '<em>The unit economics, which improved,</em> has commas, because there is only one set of unit economics '
        'and the clause is merely extra. Then Felipe did the thing <strong>that</strong> investors remember. He named '
        'his own weakest number: the <strong>addressable market</strong><strong>, which nobody has measured '
        'properly</strong>. The assumption <strong>that underpins</strong> the whole model is a market size he '
        'cannot prove. Nobody funds a company <strong>whose exit</strong> nobody can describe &mdash; and nobody '
        'trusts a CFO <strong>who hides</strong> the number the data room will find anyway.'),

    'context_quiz': [
        ("\"The churn that worried her in March\" N&#195;O tem v&#237;rgula. Por qu&#234;?",
         [("Porque a clause DEFINE de qual churn estamos falando &mdash; ela &#233; essencial, e sem ela n&#227;o se "
           "sabe qual.", True),
          ("Porque \"churn\" &#233; uma palavra curta e n&#227;o precisa de v&#237;rgula.", False),
          ("Porque toda relative clause com <em>that</em> pode ou n&#227;o levar v&#237;rgula.", False)]),
        ("\"The unit economics, which improved every quarter, are positive.\" O que as v&#237;rgulas fazem aqui?",
         [("Elas marcam informa&#231;&#227;o EXTRA sobre a &#250;nica economia unit&#225;ria que existe &mdash; se "
           "voc&#234; remover a clause, o fato sobrevive.", True),
          ("Elas indicam que existem v&#225;rias economias unit&#225;rias e essa &#233; uma delas.", False),
          ("Elas s&#227;o obrigat&#243;rias sempre que se usa <em>which</em>.", False)]),
        ("Which sentence is correct English?",
         [("Our lead investor, that has backed us since 2022, is in.", False),
          ("Our lead investor, who has backed us since 2022, is in.", True),
          ("Our lead investor which has backed us since 2022 is in.", False)]),
    ],

    'tip_title': 'Relative Clauses (a v&#237;rgula que muda o fato)',
    'tip_intro': ('Como definir sem listar &mdash; e por que, para um CFO, a v&#237;rgula n&#227;o &#233; estilo: '
                  '&#233; risco (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("Defining (SEM v&#237;rgula)",
         "Diz QUAL. Essencial &mdash; tire a clause e voc&#234; n&#227;o sabe mais de quem se fala. Tells you WHICH "
         "one.",
         "The analysts <strong>who left</strong> took the model. <em>(only those)</em>"),
        ("Non-defining (COM v&#237;rgula)",
         "Informa&#231;&#227;o EXTRA sobre TODOS. Tire a clause e o fato sobrevive. Extra information.",
         "The analysts<strong>, who left,</strong> took the model. <em>(all of them)</em>"),
        ("that / which / who",
         "<em>that</em> S&#211; em defining. <em>which</em> e <em>who</em> nas duas. NUNCA <em>that</em> depois de "
         "v&#237;rgula.",
         "the metric <strong>that</strong> matters / the metric, <strong>which</strong> matters,..."),
        ("Relativa reduzida",
         "Corte <em>that is / which are</em>. Duas palavras a menos, e soa muito mais nativo.",
         "the risks <strong>driving</strong> churn"),
        ("whose",
         "Posse &mdash; para pessoas E para empresas.",
         "a company <strong>whose</strong> exit nobody can describe"),
        ("Preposi&#231;&#227;o no fim",
         "Ingl&#234;s natural e correto. N&#227;o force <em>from which</em> fora de contrato.",
         "the fund <strong>we raised from</strong>"),
    ],
    'tip_note': ('<strong>O teste que nunca falha:</strong> tire a clause da frase. Se voc&#234; ainda sabe QUAL '
                 'deles est&#225; sendo mencionado, a clause era extra &rarr; ponha as v&#237;rgulas. Se voc&#234; '
                 'N&#195;O sabe mais, ela era essencial &rarr; sem v&#237;rgulas. <strong>E por que isso importa '
                 'para voc&#234;:</strong> "The analysts <em>who left</em> took the model" significa que ALGUNS '
                 'sa&#237;ram. "The analysts<em>, who left,</em> took the model" significa que TODOS sa&#237;ram. '
                 'Mesmas palavras, fatos diferentes &mdash; e num contrato isso &#233; dinheiro.'),

    'blanks': [
        ("The assumption", "that", "Dica: defining &mdash; diz QUAL premissa (sem v&#237;rgula, e nunca \"which\" "
         "aqui se quiser o registro mais natural)",
         "The assumption that underpins the model is the one to attack first.",
         "underpins the model is the one to attack first."),
        ("Our lead investor,", "who", "Dica: non-defining, e o relativo de PESSOA (nunca \"that\" depois de "
         "v&#237;rgula)",
         "Our lead investor, who has backed us since 2022, is in for the round.",
         "has backed us since 2022, is in for the round."),
        ("The unit economics,", "which", "Dica: non-defining &mdash; informa&#231;&#227;o extra, entre v&#237;rgulas",
         "The unit economics, which improved every quarter, are now positive.",
         "improved every quarter, are now positive."),
        ("Nobody funds a company", "whose", "Dica: posse &mdash; a sa&#237;da DELA",
         "Nobody funds a company whose exit nobody can describe.", "exit nobody can describe."),
        ("The churn", "that worried you", "Dica: defining &mdash; diz QUAL churn (sem v&#237;rgula)",
         "The churn that worried you in March has halved.", "in March has halved."),
        ("the risks", "driving", "Dica: relativa REDUZIDA &mdash; corte \"that are\" e deixe s&#243; o "
         "part&#237;cipio",
         "The risks driving our churn are now under control.", "our churn are now under control."),
    ],

    'order_title': 'Put the Investment Pitch in Order',
    'order_intro': ('Coloque as etapas de um pitch de investimento na ordem correta. Come&#231;ar pelas features, e '
                    'n&#227;o pela tese, &#233; o erro que faz o investidor parar de ouvir.'),
    'order': [
        (2, "Name the moat &mdash; and say precisely why a competitor cannot buy it."),
        (5, "Name your OWN weakest number, before they find it in the data room."),
        (1, "Define the company in one sentence. An argument, never a list."),
        (4, "Show the unit economics and what changed this year."),
        (3, "Give the traction: the number they will believe without checking."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. Diga, em cada uma, se a clause '
                     '&#233; defining ou non-defining &mdash; e por qu&#234;.'),
    'speech': SURVIVAL,

    'quiz': [
        ("Only two of your six analysts left. You want to say THOSE TWO took the model:",
         [("\"The analysts, who left, took the model with them.\"", False),
          ("\"The analysts who left took the model with them.\"", True),
          ("\"The analysts, that left, took the model with them.\"", False)]),
        ("You want to add extra information about your only lead investor:",
         [("\"Our lead investor, that has backed us since 2022, is in.\"", False),
          ("\"Our lead investor, who has backed us since 2022, is in.\"", True),
          ("\"Our lead investor who has backed us since 2022 is in.\"", False)]),
        ("An investor asks for your thesis. The best answer is:",
         [("\"We have great technology, a strong team, good margins and happy customers.\"", False),
          ("\"Our differentiator is a licence that took four years to win and that a competitor cannot buy.\"", True),
          ("\"Our thesis is that we will grow a lot next year.\"", False)]),
        ("You want to sound native and cut two words from \"the risks that are driving churn\":",
         [("\"the risks which driving churn\"", False),
          ("\"the risks driving churn\"", True),
          ("\"the risks that driving churn\"", False)]),
        ("The investor is about to find your weakest number in the data room. The senior move is:",
         [("Say nothing &mdash; she might not notice it.", False),
          ("\"The addressable market, which nobody has measured properly, is the weak part. I would rather tell you "
            "now.\"", True),
          ("Defend the number and hope the conversation moves on.", False)]),
    ],

    'think': ("An investor who has already backed you once asks: \"Give me the new thesis, in one sentence.\" Answer "
              "for 2-3 minutes. Define the company &mdash; do not list features. Use at least two defining clauses "
              "(no commas) and one non-defining clause (commas), and reduce one relative clause. Name the moat and "
              "why it cannot be bought. Then name your own weakest number before she does, and say what you will do "
              "about it."),

    'listenings': [
        {"file": "a9_listening_cfo.mp3", "voice": "arthur",
         "text": ("Let me give you the thesis in one sentence, and then I will defend it. The thesis is the licence. "
                  "Our differentiator is a regulatory licence that took four years to win and that a competitor "
                  "cannot simply buy, and I want to be precise about that, because a moat that a rival can buy is "
                  "not a moat at all. It is a head start. On traction, we have four hundred enterprise customers, "
                  "and the churn that worried this room in March has halved since the summer. The unit economics, "
                  "which improved every single quarter this year, are now positive, and I would attack that number "
                  "first if I were sitting where you are sitting. Now the part nobody enjoys. The weakest element of "
                  "this case is the addressable market, which nobody has measured properly, including us. The "
                  "assumption that underpins our entire model is a market size that I cannot prove today. I would "
                  "rather tell you that now than have you find it in the data room in three weeks. Here is what I "
                  "will do about it before we close.")},
        {"file": "a9_listening_investor.mp3", "voice": "ellen",
         "text": ("People ask me what makes me believe a thesis, and the honest answer is that it is almost never "
                  "the deck. A thesis is not a list of features. A thesis is an argument, and if you cannot say it "
                  "in one sentence, you do not have one yet, you have a product description. The second thing is the "
                  "moat, and I am very strict about this word. If a competitor with money can simply buy the thing "
                  "you are calling a moat, it is not a moat. It is a head start, and head starts get eaten. A "
                  "licence that takes four years to win is a moat. A piece of software is usually not. And the third "
                  "thing, which is the one that actually decides it for me: the best founders and finance leaders "
                  "name their own weakest number before I do. I am going to find it. The data room will show me. So "
                  "the only real question is who says it first, and what that tells me about the person I am about "
                  "to hand a great deal of money to.")},
    ],

    'inclass_blocks': {
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Give me the thesis, in one sentence.\"",
                 "tips": ["Our differentiator is a licence that took four years to win.",
                          "An argument, not a list. Define, do not describe."]},
                {"situation": "\"Why is that a moat?\"",
                 "tips": ["Because a competitor cannot simply buy it.",
                          "A moat that a rival can buy is not a moat."]},
                {"situation": "\"What about the churn?\"",
                 "tips": ["The churn that worried you in March has halved.",
                          "Defining clause: WHICH churn. No commas."]},
                {"situation": "\"Are the unit economics positive yet?\"",
                 "tips": ["The unit economics, which improved every quarter, are now positive.",
                          "Non-defining: there is only one set. Commas."]},
                {"situation": "\"What is the weakest part of your case?\"",
                 "tips": ["The addressable market, which nobody has measured properly.",
                          "Name it before she does. That is what buys credibility."]},
                {"situation": "\"Why should I believe you this time?\"",
                 "tips": ["Because I would rather tell you now than have you find it in the data room.",
                          "Track record + candor. Nothing else works."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Silicon Valley -- as cenas de pitch (HBO Max)",
         "Dezenas de pitches, quase todos errados &mdash; e um ou dois certos. Connection to Lesson 9: repare em "
         "quem LISTA features e em quem DEFINE a tese numa frase. A diferen&#231;a &#233; a piada e &#233; a "
         "li&#231;&#227;o.",
         "Dica: assista com legenda em ingl&#234;s. Reescreva 3 pitches ruins como UMA frase com defining clause.",
         "https://www.hbo.com/silicon-valley"),
        ("Podcast", "podcast", "a16z Podcast -- teses de investimento, moats e unit economics",
         "Investidores explicando por que financiam uma empresa e n&#227;o outra, com o vocabul&#225;rio exato desta "
         "aula. Connection to Lesson 9: moat, traction, churn e addressable market na velocidade nativa.",
         "Dica: ou&#231;a a 1x. Pare em cada relative clause e diga se &#233; defining ou non-defining.",
         "https://a16z.com/podcasts/"),
        ("YouTube", "youtube", "Aswath Damodaran -- narrativa e n&#250;meros (story vs numbers)",
         "O professor que ensina que valuation &#233; uma HIST&#211;RIA disciplinada por n&#250;meros &mdash; "
         "exatamente a tese desta aula. Connection to Lesson 9: &#233; a ponte entre a planilha que voc&#234; domina "
         "e a narrativa que voc&#234; ainda n&#227;o.",
         "Dica: assista a 0.75x se precisar. Depois conte a hist&#243;ria da sua empresa em 60 segundos, em "
         "ingl&#234;s.",
         "https://www.youtube.com/@AswathDamodaranonValuation"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
