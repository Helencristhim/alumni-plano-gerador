#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 7 — Emphasis That Commands Attention.
Gramatica: inversion (negative fronting) + cleft sentences (what.../it is... that...).
Modelo: PADRAO-FALA (aula IMPAR, REGRA 29) — dialogo line-by-line + role-play.
Callback (REGRA 20): o warm-up retoma a causativa e o vocab da aula 6.

Ponto pedagogico central (gap do aluno): a CLEFT SENTENCE nao e so enfase — ela COMPRA
TEMPO. "What I would say is..." da ao Felipe meio segundo de processamento antes do
conteudo. E a arma direta contra fragmentar sob pressao.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 7
SLUG = 'felipe-pimenta'

VOCAB = [
    ("To underscore", "to make one point stand out on purpose",
     "sublinhar, enfatizar",
     "Let me underscore one number before we move on."),
    ("Compelling", "so convincing that people actually act",
     "convincente, irresist&#237;vel",
     "The case was compelling, and the board approved it in nine minutes."),
    ("Pivotal", "the fact or moment that everything turns on",
     "decisivo, crucial",
     "That was the pivotal quarter. Everything after it was consequence."),
    ("Takeaway", "the one thing you want people to remember",
     "mensagem-chave",
     "If there is one takeaway tonight, it is this."),
    ("Succinct", "short and complete at the same time",
     "conciso",
     "Be succinct. A board stops listening after ninety seconds."),
    ("Conviction", "the force of genuinely believing what you are saying",
     "convic&#231;&#227;o",
     "Your numbers were right. What was missing was conviction."),
    ("Gravitas", "the seriousness and weight that makes a room go quiet",
     "peso, autoridade natural",
     "Gravitas is not volume. It is what you leave out."),
    ("To land", "to make a message actually arrive and stay",
     "fazer a mensagem chegar",
     "The message did not land, and that is on me, not on them."),
    ("Unequivocal", "leaving absolutely no room for doubt",
     "inequ&#237;voco",
     "Let me be unequivocal: we will not break the covenant."),
    ("Understatement", "saying less than you mean, on purpose, for power",
     "eufemismo deliberado",
     "Saying we are not entirely comfortable is an understatement, and everyone knows it."),
    ("To leverage", "to use something you already have to get more",
     "alavancar",
     "We leveraged the audit to buy ourselves six months."),
    ("Nuance", "a small difference that changes the whole meaning",
     "sutileza, nuance",
     "The nuance between cautioned and warned cost us a quarter."),
]

PHASES = ["The Room Goes Quiet", "The Language of Weight", "The Code",
          "The Boardroom", "Practice", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Your numbers have always been right. Tonight is "
    "about the other half -- the half that makes a room stop and listen. And it is not volume. It is syntax.' NAO "
    "cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 7 &middot; Emphasis", "Emphasis That Commands", "Attention",
    "Being right is not the same as being heard. Tonight we fix the second one."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 6 ANTES do tema novo (REGRA 20). Peca uma "
    "causativa: 'One thing you had done last week -- not by you.' Depois abra o tema: 'Now: a moment when you were "
    "RIGHT, and the room did not listen. What happened?' Deixe falar. Este warm-up abre a ferida certa.",
    "Chapter 1: The Room Goes Quiet",
    "A Time You Were Right and Nobody", "Listened",
    "Your analysis was correct. The room moved on anyway. What was missing?"))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Este e o slide mais importante do programa para o gap dele. Explique: a "
    "cleft sentence NAO e so enfase -- ela COMPRA TEMPO. Quando o Felipe comeca com 'What I would say is...', ele "
    "ganha meio segundo de processamento ANTES de precisar do conteudo. E por isso que executivos nativos usam "
    "tanto: nao e elegancia, e engenharia cognitiva. Diga isso com todas as letras.",
    "The Secret Nobody Tells You", "These Structures Buy You", "Time",
    [("\"We need discipline.\"", "4 words. No runway. You are already exposed."),
     ("\"What we need is discipline.\"", "the first 4 words cost you nothing to produce"),
     ("The effect", "you sound emphatic &mdash; and you get half a second to think")],
    "This is the direct answer to fragmenting under pressure. The cleft gives your mouth something safe to say while your brain catches up."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of weight, the inversion -- where English "
    "flips the sentence to hit harder -- and the cleft, which is your new best friend under pressure.' Antecipe o "
    "role-play: ele vai defender uma posicao impopular no board.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "gravitas, conviction, takeaway, nuance..."),
     ("2. Inversion", "\"Not once did we...\" &middot; \"Never have I...\""),
     ("3. The Cleft", "\"What matters is...\" &middot; \"It is X that...\"")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'Twelve words about weight. Not one of them is about volume.' "
    "Passe ao proximo.",
    "Chapter 2: The Language of Weight", "The Words That Make a Room", "Stop",
    "12 words &mdash; the vocabulary of authority.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'succinct': 'Is "
    "succinct the same as short? (No -- short can be incomplete. Succinct is short AND complete.)' CCQ 'pivotal': "
    "'Can a quarter be important without being pivotal? (Yes -- pivotal means everything TURNS on it.)' CCQ "
    "'conviction': 'Can you have the right numbers and no conviction? (Yes -- and the board will feel it.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Gravitas' e 'understatement' sao o coracao da "
    "aula. CCQ 'gravitas': 'Is gravitas about speaking loudly? (No -- it is often about what you LEAVE OUT.)' CCQ "
    "'understatement': 'If a British banker says \\'we are not entirely comfortable\\', how bad is it? (Very bad. "
    "Understatement is a power move.)' Este ultimo CCQ costuma abrir a cabeca do aluno.",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'gravitas' (GRAV-i-tas -- stress na 1a), 'succinct' "
    "(suk-SINKT -- o brasileiro come o 'k'), 'unequivocal' (un-e-KWIV-o-cal, 5 silabas, stress na 3a -- e a mais "
    "dificil da aula), 'nuance' (NOO-ahns). Peca que ele diga 'unequivocal' tres vezes: e a palavra que ele vai "
    "querer usar no board.",
    ["Gravitas", "Succinct", "Unequivocal", "Nuance", "Compelling"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas sao frases de sala de conselho.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"Your numbers were right. What was missing was ", "conviction", ".\""),
     ("\"", "Gravitas", " is not volume. It is what you leave out.\""),
     ("\"Let me be ", "unequivocal", ": we will not break the covenant.\""),
     ("\"If there is one ", "takeaway", " tonight, it is this.\""),
     ("\"The message did not ", "land", ", and that is on me, not on them.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. English can flip a sentence upside down to "
    "make it hit harder -- and it can put a spotlight on exactly one word. Neither trick exists in Portuguese.' "
    "Passe ao proximo.",
    "Chapter 3: The Code", "Inversion and the", "Cleft",
    "\"Not once did we...\" &middot; \"What matters is...\"", L.IMG['code']))

S.append(L.s_discovery(
    11, 3,
    "<strong>Grammar discovery (8 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos, e o par neutro ao "
    "lado de cada um. Pergunte: 'Same information. Same facts. So what changed?' Espere ele dizer que a ordem mudou "
    "e o peso mudou. So entao clique 'Reveal the Rule'. CCQ: 'Not once DID we consider it -- why did? (Because the "
    "negative jumped to the front, and it drags the auxiliary with it -- exactly like a question.)' Este e o insight.",
    [("<em>We never considered it.</em> &rarr; \"<span style=\"color:#dc2626;font-weight:700\">Not once did we "
      "consider</span> breaking the covenant.\"",
      "Not once did we consider breaking the covenant."),
     ("<em>I have never seen a cleaner audit.</em> &rarr; \"<span style=\"color:#dc2626;font-weight:700\">Never have "
      "I seen</span> a cleaner audit.\"",
      "Never have I seen a cleaner audit."),
     ("<em>We need discipline.</em> &rarr; \"<span style=\"color:#15803d;font-weight:700\">What we need is</span> "
      "discipline, not another forecast.\"",
      "What we need is discipline, not another forecast."),
     ("<em>The approvals cycle broke the quarter.</em> &rarr; \"<span style=\"color:#15803d;font-weight:700\">It was "
      "the approvals cycle that</span> broke the quarter.\"",
      "It was the approvals cycle that broke the quarter.")],
    "Same facts, same numbers. So what actually changed &mdash; and why does the second version of each pair make "
    "the room look up?",
    [("Negative inversion",
      "Put the negative FIRST, and the sentence flips into question order &mdash; auxiliary before subject.",
      "<strong>Not once did we</strong> consider it. / <strong>Never have I</strong> seen..."),
     ("Only when / Only if",
      "Same flip. Very common in boardrooms, and it sounds deliberate.",
      "<strong>Only when the audit closed did we</strong> commit."),
     ("Not only... but also",
      "Two hits instead of one. The first half inverts.",
      "<strong>Not only did we</strong> hold the covenant, <strong>but we also</strong> raised guidance."),
     ("The WHAT-cleft",
      "Put a spotlight on one idea &mdash; and buy yourself half a second before you have to produce it.",
      "<strong>What we need is</strong> discipline."),
     ("The IT-cleft",
      "Names the ONE thing that mattered, and quietly rules out everything else.",
      "<strong>It was the approvals cycle that</strong> broke the quarter."),
     ("The reason... is that",
      "The safest, most useful opener you own. Works under any pressure.",
      "<strong>The reason we held the line is that</strong> the audit was clean."),
    ],
    "Notice what the inversion does mechanically: the negative jumps to the front and <strong>drags the auxiliary "
    "with it</strong>, exactly like a question &mdash; \"<em>did we</em>\", \"<em>have I</em>\". That is the whole "
    "rule.",
    "rule7"))

S.append(L.s_mistake(
    12, 3,
    "<strong>Common mistake (4 min):</strong> Dois erros. (1) Inverter e ESQUECER o auxiliar: 'Not once we "
    "considered' -- falta o DID. A inversao e obrigatoria, nao opcional. (2) A cleft sem o 'that/who': 'It was the "
    "approvals cycle broke the quarter'. Peca que ele leia as certas DUAS vezes, em voz alta e devagar -- e a "
    "musica da frase que ele precisa internalizar.",
    [("Not once we considered breaking the covenant.",
      "Not once did we consider breaking the covenant."),
     ("Never I have seen a cleaner audit.",
      "Never have I seen a cleaner audit."),
     ("It was the approvals cycle broke the quarter.",
      "It was the approvals cycle that broke the quarter.")],
    "When the negative goes to the front, the sentence flips into <strong>question order</strong>: auxiliary "
    "BEFORE the subject (<em>did we</em>, <em>have I</em>). And an IT-cleft always needs its "
    "<strong>that</strong> or <strong>who</strong>."))

S.append(L.s_fill(
    13, 3,
    "<strong>Practice (4 min):</strong> Leia a frase neutra. Felipe produz a versao com enfase ORALMENTE antes de "
    "clicar. Se travar, pergunte: 'Where do you want the spotlight?'",
    "Practice", "Add the", "Weight", "Say the emphatic version first, then click to check",
    [("\"We never considered it.\" &rarr; \"", "Not once did we consider", " breaking the covenant.\""),
     ("\"I have never seen a cleaner audit.\" &rarr; \"", "Never have I seen", " a cleaner audit.\""),
     ("\"We need discipline.\" &rarr; \"", "What we need is", " discipline, not another forecast.\""),
     ("\"The approvals cycle broke the quarter.\" &rarr; \"", "It was the approvals cycle that",
      " broke the quarter.\""),
     ("\"We held the line because the audit was clean.\" &rarr; \"", "The reason we held the line is that",
      " the audit was clean.\"")]))

S.append(L.s_fill(
    14, 3,
    "<strong>A cleft que compra tempo (4 min):</strong> ESTE slide e a arma dele. Estas aberturas custam ZERO "
    "esforco cognitivo e dao meio segundo de processamento. Peca que ele DECORE tres delas. Depois faca um teste "
    "cruel: pergunte algo dificil e exija que ele COMECE por uma delas, sempre. E a muleta que vira musculo.",
    "Under Pressure", "The Openers That Buy You", "Half a Second",
    "Memorize three. Use them when your brain needs a moment.",
    [("\"(you need a moment) &rarr; \"", "What I would say is", " that the covenant is the constraint.\""),
     ("\"(you want to name the cause) &rarr; \"", "The reason", " we missed the target is the approvals cycle.\""),
     ("\"(you want one spotlight) &rarr; \"", "What matters here is", " the cash, not the accounting.\""),
     ("\"(you must be absolute) &rarr; \"Let me be ", "unequivocal", ": we will not break the covenant.\"")]))

S.append(L.s_chapter(
    15, 4,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Diana Reis chairs the audit committee. You met her in Lesson "
    "2, when you had bad news. Tonight you have good news -- and she is going to test whether you can hold a line.' "
    "Passe ao proximo.",
    "Chapter 4: The Boardroom", "Hold the", "Line",
    "The board is not convinced. Yet.", L.IMG['context']))

S.append(L.s_dialogue(
    16, 4,
    "<strong>Dialogo (7 min):</strong> Voce e a Diana. Clique 'Next Line' a cada fala. Para cada fala do Felipe, "
    "peca que ELE fale primeiro. Observe: as clefts saem naturalmente ou ele volta pra frase neutra sob pressao? "
    "CELEBRE cada inversao que sair sozinha -- e o som de um executivo, nao de um aluno.",
    "Defending the", "Position",
    [("diana", "D", "ellen",
      "Felipe, three directors want to raise debt this quarter. You are the only one saying no. Convince me.",
      "Felipe, three directors want to raise debt this quarter. You are the only one saying no. Convince me."),
     ("felipe", "F", "arthur",
      "What we need is discipline, not another round of financing. Let me be "
      "<span class=\"vocab-highlight\">unequivocal</span>: not once have we come this close to the "
      "<span class=\"vocab-highlight\">covenant</span> ceiling, and I will not spend our headroom on optionality.",
      "What we need is discipline, not another round of financing. Let me be unequivocal: not once have we come "
      "this close to the covenant ceiling, and I will not spend our headroom on optionality."),
     ("diana", "D", "ellen",
      "The three of them would say you are being too conservative.",
      "The three of them would say you are being too conservative."),
     ("felipe", "F", "arthur",
      "The reason I am holding the line is that the cash is real and the growth is not, yet. It was the approvals "
      "cycle that broke last quarter, not the market &mdash; and that is a fix we control. Not only would new debt "
      "raise our cost of capital, but it would also hide the problem we just found.",
      "The reason I am holding the line is that the cash is real and the growth is not, yet. It was the approvals "
      "cycle that broke last quarter, not the market, and that is a fix we control. Not only would new debt raise "
      "our cost of capital, but it would also hide the problem we just found."),
     ("diana", "D", "ellen",
      "And if the board overrules you?",
      "And if the board overrules you?"),
     ("felipe", "F", "arthur",
      "Then I will execute it properly, and I will put my objection in the minutes. What I would say, though, is "
      "this: never have I seen a company regret waiting one quarter. If there is one "
      "<span class=\"vocab-highlight\">takeaway</span> tonight, it is that we do not need the money. We need the "
      "discipline.",
      "Then I will execute it properly, and I will put my objection in the minutes. What I would say, though, is "
      "this: never have I seen a company regret waiting one quarter. If there is one takeaway tonight, it is that "
      "we do not need the money. We need the discipline.")]))

S.append(L.s_comprehension(
    17, 4,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a DIANA, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Diana",
    [("What does Diana tell Felipe at the start?",
      "That three directors want to raise debt, and he is the only one saying no."),
     ("What criticism does she put to him?",
      "That the three directors would call him too conservative."),
     ("What is her final challenge?",
      "She asks what he will do if the board overrules him.")]))

S.append(L.s_listening(
    18, 4,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A CEO opens a difficult all-hands. Listen for the shape of the "
    "sentences, not just the facts.' Toque SEM texto, 2 vezes. Peca que ele CONTE as inversoes e clefts. Ouvido "
    "antes de boca -- e este audio e deliberadamente denso nelas.",
    1, "Listening", "The Speech That", "Landed",
    "A CEO holds a room of four hundred people. Sound first &mdash; no text.",
    "a7_listening_ceo.mp3", SLUG,
    [("What is the one takeaway the CEO gives?",
      "That the company does not need more money &mdash; it needs discipline."),
     ("What does he say about the last quarter?",
      "That it was the approvals cycle that broke it, not the market &mdash; and that is a fix they control."),
     ("What does he say he will not do?",
      "Not once will he spend the covenant headroom on optionality.")]))

S.append(L.s_listening(
    19, 4,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now a CFO who lands a very hard message with almost no volume. "
    "She uses understatement.' Toque 2 vezes. Depois pergunte: 'She never raises her voice. So why is it "
    "terrifying?' O contraste entre os dois audios e o argumento da aula: gravitas nao e volume.",
    2, "Listening 2", "The Power of Saying", "Less",
    "She never raises her voice. Sound first &mdash; no text.",
    "a7_listening_cfo.mp3", SLUG,
    [("What does she mean by \"we are not entirely comfortable\"?",
      "It is an understatement &mdash; the position is serious, and everyone in the room knows it."),
     ("What does she say is missing, and what is not?",
      "The numbers were right; what was missing was conviction."),
     ("What is her rule about gravitas?",
      "Gravitas is not volume &mdash; it is what you leave out.")]))

S.append(L.s_chapter(
    20, 5,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the one-slide message, and "
    "pressure.' Passe ao proximo.",
    "Chapter 5: Practice", "Make It", "Land",
    "Detective &middot; The Takeaway &middot; Quick Fire", L.IMG['practice']))

S.append(L.s_error(
    21, 5,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. As duas primeiras "
    "sao o auxiliar esquecido na inversao (O erro). Trate como vitoria quando ele achar sozinho.",
    [("Not once we considered breaking the covenant.",
      "Not once did we consider breaking the covenant."),
     ("Never I have seen a cleaner audit.",
      "Never have I seen a cleaner audit."),
     ("It was the approvals cycle broke the quarter.",
      "It was the approvals cycle that broke the quarter."),
     ("Only when the audit closed we committed to the deal.",
      "Only when the audit closed did we commit to the deal.")]))

S.append(L.s_artifact(
    22, 5,
    "<strong>Artefato (5 min):</strong> Este e o cartao de mensagem-chave que executivos escrevem ANTES de entrar na "
    "sala. Peca que o Felipe leia cada linha e a diga em voz alta com inversao ou cleft. Depois o exercicio real: "
    "peca que ele escreva o TAKEAWAY da propria empresa dele, em uma frase, com cleft.",
    "The Artifact", "The One-Message", "Card",
    "BOARD &mdash; KEY MESSAGE", "Q4 &middot; Prepared by the CFO",
    [("Prepared by", "Felipe Pimenta, CFO"),
     ("The takeaway", "We do not need money. We need discipline."),
     ("The pivotal fact", "Approvals cycle &mdash; not the market"),
     ("What we will not do", "Spend covenant headroom on optionality"),
     ("The nuance", "Cash is real; growth is not, yet"),
     ("If overruled", "Execute properly; objection in the minutes"),
     ("Tone", "Unequivocal. Succinct. No volume.")],
    [("Say the takeaway line as a cleft.",
      "\"What we need is discipline, not another round of financing.\""),
     ("Say the pivotal fact as an IT-cleft.",
      "\"It was the approvals cycle that broke the quarter, not the market.\""),
     ("Say \"what we will not do\" with a negative inversion.",
      "\"Not once will we spend our covenant headroom on optionality.\"")]))

S.append(L.s_quickfire(
    23, 5,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. REGRA DESTE SLIDE: o Felipe DEVE comecar toda "
    "resposta com uma cleft ou inversao. Nao aceite frase neutra -- mande refazer. E chato de proposito: e assim que "
    "a estrutura vira reflexo, e o reflexo e o que sobrevive sob pressao.",
    "They Push. You", "Hold."))

S.append(L.s_building(
    24, 5,
    "<strong>Sentence Building (4 min):</strong> Mostre a frase NEUTRA. Felipe produz a versao com peso, em voz "
    "alta, depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes.",
    [("we / never / consider / breaking the covenant (negative inversion)",
      "Not once did we consider breaking the covenant."),
     ("I / never / see / a cleaner audit (negative inversion)",
      "Never have I seen a cleaner audit."),
     ("we / need / discipline / not another forecast (what-cleft)",
      "What we need is discipline, not another forecast."),
     ("the approvals cycle / break / the quarter / not the market (it-cleft)",
      "It was the approvals cycle that broke the quarter, not the market."),
     ("new debt / raise / cost of capital / AND / hide the problem (not only... but also)",
      "Not only would new debt raise our cost of capital, but it would also hide the problem.")]))

S.append(L.s_chapter(
    25, 6,
    "<strong>Transicao role-play (1 min):</strong> Diga: 'Now you defend an unpopular position -- and the room is "
    "against you. Three rounds, and each one gives you less help.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Hold the Room", "Alone",
    "Guided &gt; Semi-free &gt; Free", L.IMG['turn']))

S.append(L.s_roleplay(
    26, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Diana. Abra com: 'Three directors want to raise debt. You "
    "are the only no. Convince me.' Felipe usa as keywords. Observe: ele abre com cleft, ou com frase neutra? Se "
    "abrir neutro, pare e mande recomecar.",
    "Defend the", "Position",
    "Three directors want to raise debt this quarter. You are the only one saying no. Make the case &mdash; and open "
    "with emphasis, not with a fact.",
    ["What we need is...", "Let me be unequivocal:", "The reason I am holding the line is that...",
     "It was ... that broke the quarter."]))

S.append(L.s_roleplay(
    27, 6,
    "<strong>Role-play Semi-free (5 min):</strong> Suba a aposta. Agora voce e um diretor HOSTIL, nao curioso. "
    "Interrompa. Diga 'that is not an answer'. Diga 'you are being conservative because you are scared'. O Felipe "
    "tem de sustentar a posicao SEM levantar a voz -- usando understatement e inversao. Se ele gritar ou se "
    "desculpar, perdeu a sala.",
    "The Hostile", "Director",
    "A director attacks, not asks: \"You are being conservative because you are afraid.\" Hold your ground without "
    "raising your voice. Use understatement. Use inversion. Do not apologize, and do not fill the silence.",
    ["I would put it differently:", "Not once have we...", "What I would say is...",
     "We are not entirely comfortable with..."],
    tint='.12'))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: dois minutos de fala, ZERO pistas, defendendo a "
    "posicao dele. NAO interrompa, NAO corrija no meio. Cronometre. Peca ANTES: 'Open with a cleft. Close with your "
    "one takeaway.' CELEBRE muito: sair de 'estou certo' para 'a sala parou' e a virada do programa.",
    "The Whole", "Argument",
    "Two minutes, standing your ground in front of a board that disagrees with you. Open with emphasis, name the "
    "pivotal fact with an IT-cleft, use one negative inversion, use one understatement, and close with a single "
    "unequivocal takeaway. Then stop talking.",
    []))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Extensao / silencio (4 min):</strong> So faca se sobrar tempo. Este e o exercicio mais dificil e mais "
    "valioso: depois que ele terminar o takeaway, voce NAO fala nada. Cinco segundos de silencio. A tentacao de "
    "preencher o silencio e o que destroi a gravitas -- e a maioria dos brasileiros preenche. Se ele aguentar o "
    "silencio, ele aprendeu a aula.",
    "The", "Silence",
    "Deliver your takeaway &mdash; and then hold the silence. Do not explain it, do not soften it, do not fill it. "
    "Gravitas is what you leave out. Five seconds. Say nothing.",
    []))

S.append(L.s_chapter(
    30, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'Tonight you stopped translating and started performing. That "
    "is a different language skill entirely.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "The Room", "Stopped",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("What we need is discipline, not another round of financing.",
     "O que precisamos &#233; disciplina, n&#227;o outra rodada de capta&#231;&#227;o."),
    ("Let me be unequivocal: we will not break the covenant.",
     "Vou ser inequ&#237;voco: n&#227;o vamos romper o covenant."),
    ("It was the approvals cycle that broke the quarter, not the market.",
     "Foi o ciclo de aprova&#231;&#245;es que quebrou o trimestre, n&#227;o o mercado."),
    ("Not once did we consider spending our covenant headroom.",
     "Em nenhum momento cogitamos gastar nossa folga de covenant."),
    ("What I would say is that the cash is real and the growth is not, yet.",
     "O que eu diria &#233; que o caixa &#233; real e o crescimento ainda n&#227;o &#233;."),
]

S.append(L.s_survival(
    31, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. As duas "
    "ultimas sao as que compram tempo -- peca que ele DECORE. Vao salvar a fala dele em toda reuniao dificil daqui "
    "pra frente.",
    "Five Phrases That", "Command the Room",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    32, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 7 no passaporte (registra no Supabase).",
    N,
    ["I can invert after a negative: Not once did we... / Never have I...",
     "I can use a what-cleft to put a spotlight on one idea.",
     "I can use an it-cleft to name the one thing that mattered.",
     "I can use these openers to buy myself half a second under pressure.",
     "I know my words: gravitas, conviction, takeaway, succinct, unequivocal, nuance."]))

S.append(L.s_complete(
    33, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 7 complete, Felipe. You earned your Gravitas Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) escrever o TAKEAWAY da empresa dele em UMA frase com cleft, e "
    "gravar dizendo 10 vezes ate sair sem pensar; (2) na proxima reuniao real, abrir UMA resposta com 'What I would "
    "say is...' e reparar no meio segundo que ele ganha. Proxima aula: Progress Check -- Felipe no meio do caminho.",
    N, "Gravitas Badge", "You did not raise your voice, Felipe. And the room stopped.",
    "Progress Check and Integration"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Emphasis That Commands Attention',
    'short_title': 'Emphasis That Commands Attention',
    'menu_desc': 'Defender uma posi&#231;&#227;o no board + inversion e cleft sentences',
    'desc': ('Ser ouvido, e n&#227;o apenas estar certo. Key words: to underscore, compelling, pivotal, takeaway, '
             'succinct, conviction, gravitas, to land, unequivocal, understatement, to leverage, nuance. Structures: '
             'inversion (Not once did we... / Never have I... / Only when... did we... / Not only... but also) e '
             'cleft sentences (What we need is... / It was X that... / The reason... is that...). A cleft N&#195;O '
             '&#233; s&#243; &#234;nfase: ela COMPRA MEIO SEGUNDO de processamento &mdash; a arma direta contra '
             'fragmentar sob press&#227;o.'),
    'hub_img': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'diana': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. Doze palavras sobre PESO &mdash; e nenhuma delas &#233; '
                    'sobre volume.'),

    'context_text': (
        'Three directors wanted to raise debt. Felipe was the only one who said no, and he knew that being right '
        'would not be enough. <strong>What he needed was</strong> a way to be heard. So he did not open with a '
        'number. <strong>What we need is discipline</strong>, he said, <strong>not another round of financing</strong>. '
        'Then he made it <strong>unequivocal</strong>: <strong>not once had they come</strong> that close to the '
        'covenant ceiling, and <strong>not once would he spend</strong> that headroom on optionality. He named the '
        '<strong>pivotal</strong> fact with a spotlight on it: <strong>it was the approvals cycle that</strong> broke '
        'the quarter, not the market &mdash; and that is a fix they control. <strong>Not only would</strong> new debt '
        'raise the cost of capital, <strong>but it would also</strong> hide the problem they had just found. '
        '<strong>The reason he held the line was that</strong> the cash was real and the growth was not, yet. He was '
        '<strong>succinct</strong>. He used <strong>understatement</strong> rather than volume, because '
        '<strong>gravitas</strong> is not volume &mdash; it is what you leave out. His numbers had always been right. '
        'What had been missing was <strong>conviction</strong>, and the <strong>nuance</strong> of a sentence built '
        'to <strong>land</strong>. The board waited a quarter. The <strong>takeaway</strong> stuck.'),

    'context_quiz': [
        ("Por que \"Not once did we consider\" leva DID, se o verbo j&#225; est&#225; no passado?",
         [("Porque a negativa foi para a frente e ARRASTA o auxiliar junto &mdash; a frase vira ordem de pergunta.",
           True),
          ("Porque \"consider\" &#233; um verbo irregular.", False),
          ("Porque \"not once\" exige sempre o presente.", False)]),
        ("Qual &#233; o efeito de \"It was the approvals cycle that broke the quarter\"?",
         [("Coloca um holofote no ciclo de aprova&#231;&#245;es &mdash; e, silenciosamente, exclui todo o resto "
           "(o mercado, o time de vendas).", True),
          ("&#201; apenas uma forma mais longa e mais educada de dizer a mesma coisa.", False),
          ("Indica que o ciclo de aprova&#231;&#245;es ainda vai quebrar o trimestre.", False)]),
        ("Which sentence is correct English?",
         [("Never I have seen a cleaner audit.", False),
          ("Never have I seen a cleaner audit.", True),
          ("Never have seen I a cleaner audit.", False)]),
    ],

    'tip_title': 'Inversion + Cleft Sentences',
    'tip_intro': ('Como fazer uma sala parar &mdash; e, de quebra, como comprar meio segundo de processamento quando '
                  'a pergunta &#233; dif&#237;cil (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("Negative inversion",
         "A negativa vai para a FRENTE e arrasta o auxiliar com ela &mdash; a frase vira ordem de PERGUNTA. The "
         "negative fronts and the auxiliary follows.",
         "<strong>Not once did we</strong> consider it."),
        ("Never / Rarely / Under no circumstances",
         "Mesma mec&#226;nica. Soa deliberado, e um board escuta isso.",
         "<strong>Never have I</strong> seen a cleaner audit."),
        ("Only when / Only if",
         "Mesma invers&#227;o. Muito comum em sala de conselho.",
         "<strong>Only when the audit closed did we</strong> commit."),
        ("Not only... but also",
         "Dois golpes em vez de um. A primeira metade inverte.",
         "<strong>Not only did we</strong> hold, <strong>but we also</strong> raised guidance."),
        ("WHAT-cleft",
         "Holofote numa ideia s&#243;. E as 4 primeiras palavras custam ZERO esfor&#231;o &mdash; &#233; a&#237; que "
         "voc&#234; ganha tempo.",
         "<strong>What we need is</strong> discipline."),
        ("IT-cleft",
         "Nomeia A COISA que importou &mdash; e exclui todas as outras. Sempre com <em>that</em> ou <em>who</em>.",
         "<strong>It was the approvals cycle that</strong> broke the quarter."),
        ("The reason... is that",
         "A abertura mais segura que voc&#234; tem. Funciona sob qualquer press&#227;o.",
         "<strong>The reason we held the line is that</strong> the audit was clean."),
    ],
    'tip_note': ('<strong>O segredo que ningu&#233;m conta:</strong> a cleft n&#227;o &#233; s&#243; '
                 '&#234;nfase &mdash; ela <strong>COMPRA TEMPO</strong>. "What I would say is..." s&#227;o cinco '
                 'palavras que voc&#234; produz sem pensar, enquanto o c&#233;rebro monta o conte&#250;do. &#201; '
                 'engenharia cognitiva, n&#227;o eleg&#226;ncia &mdash; e &#233; a resposta direta ao seu h&#225;bito '
                 'de fragmentar sob press&#227;o. <strong>Aten&#231;&#227;o ao erro:</strong> na invers&#227;o, '
                 'NUNCA esque&#231;a o auxiliar ("Not once <em>we considered</em>" est&#225; errado; o certo &#233; '
                 '"Not once <strong>did we consider</strong>").'),

    'blanks': [
        ("", "Not once did we consider", "Dica: invers&#227;o negativa &mdash; a negativa vem primeiro e puxa o DID",
         "Not once did we consider breaking the covenant.", "breaking the covenant."),
        ("", "Never have I seen", "Dica: invers&#227;o negativa &mdash; auxiliar ANTES do sujeito",
         "Never have I seen a cleaner audit.", "a cleaner audit."),
        ("", "What we need is", "Dica: what-cleft &mdash; o holofote numa ideia s&#243;",
         "What we need is discipline, not another forecast.", "discipline, not another forecast."),
        ("", "It was the approvals cycle that", "Dica: it-cleft &mdash; nomeia A causa e exclui as outras (com THAT)",
         "It was the approvals cycle that broke the quarter.", "broke the quarter."),
        ("", "The reason", "Dica: a abertura mais segura sob press&#227;o",
         "The reason we held the line is that the audit was clean.",
         "we held the line is that the audit was clean."),
        ("Let me be", "unequivocal", "Dica: sem margem nenhuma para d&#250;vida",
         "Let me be unequivocal: we will not break the covenant.",
         ": we will not break the covenant."),
    ],

    'order_title': 'Put the High-Stakes Argument in Order',
    'order_intro': ('Coloque as etapas de uma defesa de posi&#231;&#227;o no board na ordem correta. Come&#231;ar '
                    'pelo n&#250;mero, e n&#227;o pela &#234;nfase, &#233; o erro que faz a sala parar de ouvir.'),
    'order': [
        (2, "Make it unequivocal &mdash; and use a negative inversion to draw the hard line."),
        (5, "Deliver the single takeaway, then STOP talking. Do not fill the silence."),
        (1, "Open with a cleft, not with a number. The spotlight comes before the data."),
        (4, "Concede what is fair &mdash; and use understatement, never volume."),
        (3, "Name the pivotal fact with an it-cleft, and rule out the alternatives."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. Decore as duas &#250;ltimas: '
                     's&#227;o as que compram meio segundo quando a pergunta &#233; dif&#237;cil.'),
    'speech': SURVIVAL,

    'quiz': [
        ("You want to say the company never considered breaking the covenant, with maximum force:",
         [("\"Not once we considered breaking the covenant.\"", False),
          ("\"Not once did we consider breaking the covenant.\"", True),
          ("\"We did not once considered breaking the covenant.\"", False)]),
        ("You want to name the ONE cause and rule out the others:",
         [("\"The approvals cycle broke the quarter.\"", False),
          ("\"It was the approvals cycle that broke the quarter, not the market.\"", True),
          ("\"It was the approvals cycle broke the quarter.\"", False)]),
        ("A director attacks you and your mind goes blank. The best thing to start saying is:",
         [("\"Sorry, can you repeat the question?\"", False),
          ("\"What I would say is that the covenant is the real constraint here.\"", True),
          ("\"Uh, well, I think that, you know, the numbers...\"", False)]),
        ("A British investor says \"we are not entirely comfortable.\" This means:",
         [("They are mildly hesitant but basically fine.", False),
          ("It is an understatement &mdash; they are seriously worried, and everyone in the room knows it.", True),
          ("They did not understand the presentation.", False)]),
        ("You want maximum emphasis on two advantages at once:",
         [("\"Not only we held the covenant, but we raised guidance too.\"", False),
          ("\"Not only did we hold the covenant, but we also raised guidance.\"", True),
          ("\"We held the covenant and also we raised guidance.\"", False)]),
    ],

    'think': ("You are the only person in the room arguing against raising debt this quarter. Speak for 2-3 minutes "
              "and hold your position. Open with a what-cleft (not with a number). Use at least one negative "
              "inversion, one it-cleft naming the pivotal fact, and one understatement. Do not raise your voice. "
              "Close with a single unequivocal takeaway &mdash; and then stop talking."),

    'listenings': [
        {"file": "a7_listening_ceo.mp3", "voice": "arthur",
         "text": ("Thank you all for coming. I am going to be very direct tonight, and I am going to be short. What "
                  "we need is discipline. What we do not need is another round of financing. Let me be unequivocal "
                  "about that, because I know there are three people in this room who disagree with me, and they "
                  "have earned the right to. Not once, in the eleven years of this company, have we come this close "
                  "to our covenant ceiling. And not once will I spend that headroom on optionality. Now, the last "
                  "quarter. It was the approvals cycle that broke it. It was not the market, it was not the sales "
                  "team, and it was not bad luck. It was a process we own, and therefore it is a process we can "
                  "fix. Not only would new debt raise our cost of capital, but it would also hide the very problem "
                  "we have just found, and we would congratulate ourselves for solving nothing. The reason I am "
                  "holding this line is simple. The cash is real. The growth is not, yet. If there is one takeaway "
                  "tonight, it is this: we do not need the money. We need the discipline.")},
        {"file": "a7_listening_cfo.mp3", "voice": "ellen",
         "text": ("I want to say something about how we talk in this company, and I am going to say it quietly. Last "
                  "month a director told me that our position was fine. I said, and I quote myself, that we were not "
                  "entirely comfortable. Everyone in that room understood exactly what I meant, and nobody needed me "
                  "to raise my voice. That is understatement, and it is the most powerful tool a finance leader "
                  "owns. Here is what I have learned in twenty years. Your numbers will almost always be right. That "
                  "is the easy part, and it is the part they hire you for. What is usually missing is not accuracy. "
                  "What is missing is conviction, and the shape of the sentence that carries it. Gravitas is not "
                  "volume. Gravitas is what you leave out. Say less. Say it once. And when you have said the one "
                  "thing that matters, do not explain it, do not soften it, and do not fill the silence. Let it "
                  "sit. The silence is doing your work for you.")},
    ],

    'inclass_blocks': {
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Three directors disagree with you. Why are you right?\"",
                 "tips": ["What we need is discipline, not another round of financing.",
                          "Open with the cleft. Never with a number."]},
                {"situation": "\"Have you ever come this close to the covenant before?\"",
                 "tips": ["Not once have we come this close.",
                          "Negative first &mdash; and drag the auxiliary with it."]},
                {"situation": "\"So the market broke the quarter?\"",
                 "tips": ["It was the approvals cycle that broke it, not the market.",
                          "it-cleft: name the one cause, rule out the rest."]},
                {"situation": "\"You are being too conservative.\"",
                 "tips": ["I would put it differently.",
                          "We are not entirely comfortable with that risk. (understatement)"]},
                {"situation": "\"Give me one reason to wait a quarter.\"",
                 "tips": ["Never have I seen a company regret waiting one quarter.",
                          "The reason I am holding the line is that the cash is real."]},
                {"situation": "\"What is your one message tonight?\" (then SAY NOTHING for 5 seconds)",
                 "tips": ["We do not need the money. We need the discipline.",
                          "Deliver it. Then hold the silence. Do not fill it."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Succession -- a cena do discurso de Logan (HBO Max)",
         "Um homem que faz uma sala inteira parar sem levantar a voz uma vez. Connection to Lesson 7: conte as "
         "invers&#245;es e as clefts &mdash; e repare em quanto tempo ele deixa o sil&#234;ncio trabalhar por ele.",
         "Dica: assista com legenda em ingl&#234;s. Escolha 3 falas e reescreva-as em forma neutra &mdash; sinta o "
         "que se perde.",
         "https://www.hbo.com/succession"),
        ("Podcast", "podcast", "Acquired -- as narrativas de founders e CEOs em momentos pivotais",
         "Hist&#243;rias reconstru&#237;das com o vocabul&#225;rio exato desta aula: pivotal, compelling, takeaway. "
         "Connection to Lesson 7: repare em como os entrevistados constroem &#234;nfase sem elevar o tom.",
         "Dica: ou&#231;a a 1x. Pare em cada \"What mattered was...\" ou \"It was X that...\" e repita a frase.",
         "https://www.acquired.fm/"),
        ("YouTube", "youtube", "TED -- palestras sobre presen&#231;a executiva e o poder da pausa",
         "Como a pausa, o understatement e a estrutura da frase constroem autoridade. Connection to Lesson 7: "
         "gravitas &#233; t&#233;cnica, e esta &#233; a aula que a transforma em gram&#225;tica.",
         "Dica: assista a 0.75x. Cronometre as pausas do palestrante depois da frase-chave &mdash; e copie.",
         "https://www.youtube.com/@TED"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
