#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 3 — What Should Have Happened (Modal Perfects).
Gramatica: should have / shouldn't have / could have / must have / might have.
Modelo: PADRAO-FALA (aula IMPAR, REGRA 29) — dialogo line-by-line + role-play.
Callback (REGRA 20): o warm-up retoma o third conditional e o vocab da aula 2.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

N = 3
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Performance review", "the formal meeting where your work is evaluated",
     "avalia&#231;&#227;o de desempenho",
     "My performance review is on Thursday, and the forecast will come up."),
    ("Shortfall", "the gap between the number you promised and the one you delivered",
     "d&#233;ficit, diferen&#231;a a menor",
     "We closed the quarter with a two million shortfall."),
    ("Variance", "the difference between the budget and what actually happened",
     "vari&#226;ncia, varia&#231;&#227;o or&#231;ament&#225;ria",
     "The variance report explains every line above five percent."),
    ("Root cause", "the real reason behind a problem, not the symptom",
     "causa raiz",
     "The root cause was a hiring freeze nobody told us about."),
    ("Bottleneck", "the one point that slows everything else down",
     "gargalo",
     "Approvals were the bottleneck, not the sales team."),
    ("To escalate", "to take an issue to someone more senior",
     "escalar, levar &#224; inst&#226;ncia superior",
     "She should have escalated the problem in week two."),
    ("To flag", "to point out a risk early, before it becomes a problem",
     "sinalizar, apontar",
     "Somebody must have flagged this before the board meeting."),
    ("Accountability", "owning the result, whether it is good or bad",
     "responsabiliza&#231;&#227;o, presta&#231;&#227;o de contas",
     "Accountability is not blame &mdash; it is knowing whose call it was."),
    ("To miss a target", "to fail to reach the number you committed to",
     "n&#227;o bater a meta",
     "We missed the target by eight percent, and I own that."),
    ("Turnaround", "the recovery of a business or a number that was failing",
     "recupera&#231;&#227;o, virada",
     "The turnaround took two quarters and a very hard conversation."),
    ("Mitigation", "the action you take to reduce a risk you cannot remove",
     "mitiga&#231;&#227;o",
     "Our mitigation was to hold ten percent of the budget back."),
    ("Milestone", "a key checkpoint that proves a plan is on track",
     "marco",
     "We could have caught it at the first milestone."),
]

PHASES = ["The Quarter That Slipped", "The Language of Review", "The Code",
          "The Review Meeting", "Practice", "Your Turn", "Wrap-Up"]

S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Last week you explained a deal that failed. "
    "Tonight, something harder: you sit in judgment. A number was missed, and you have to say what should have "
    "happened -- to your CEO, and to your own team.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 3 &middot; The Review", "What Should Have", "Happened",
    "Three words separate a leader from a complainer: should, could, must."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 2 ANTES do tema novo (REGRA 20). Peca uma frase "
    "de third conditional sobre a semana dele: 'Give me one: if I had..., I would have...'. Depois pergunte o "
    "novo: 'Now, a target your team missed. Not the deal -- the number.' Deixe falar. ZERO correcao: anote onde "
    "ele fragmenta.",
    "Chapter 1: The Quarter That Slipped",
    "A Number Your Team", "Missed",
    "Not a failed deal this time. A forecast, a budget, a target. What happened, and whose call was it?"))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Explique a diferenca. O third conditional (aula 2) analisa um passado "
    "IMAGINARIO inteiro. O modal perfect e mais cirurgico: aponta UMA acao especifica que faltou -- e ele carrega "
    "JULGAMENTO. 'She should have escalated' nao e uma hipotese, e uma avaliacao. E por isso que ele e a lingua da "
    "performance review.",
    "Two Tools, Two Jobs", "Analysis vs", "Judgment",
    [("If we had...", "an imaginary past &mdash; pure analysis (Lesson 2)"),
     ("She should have...", "one missing action &mdash; and a verdict on it"),
     ("It must have been...", "a confident deduction about what happened")],
    "The board does not want your hypothesis. It wants to know what should have happened, and who should have made it happen."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of a review, the four modal perfects, and "
    "a real performance review -- where you are on BOTH sides of the table.' Antecipe o role-play: ele vai dar "
    "feedback E receber.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "shortfall, variance, root cause, bottleneck..."),
     ("2. The Code", "should have &middot; could have &middot; must have"),
     ("3. The Review", "give feedback, and take it")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'These are the twelve words of every quarterly review you have "
    "ever sat in -- in Portuguese. Tonight they become yours in English.' Passe ao proximo.",
    "Chapter 2: The Language of Review", "The Words of a", "Missed Number",
    "12 words &mdash; the vocabulary of accountability.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Felipe tenta, depois revele. CCQ 'shortfall': 'Is a "
    "shortfall the number you got, or the GAP between promise and result? (The gap.)' CCQ 'root cause': 'Sales fell "
    "because approvals were slow. Is slow sales the root cause, or the symptom? (The symptom.)' CCQ 'bottleneck': "
    "'If a process has five steps, how many bottlenecks does it usually have? (One -- the slowest.)'",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Accountability' e o conceito-chave da aula -- e "
    "NAO e 'culpa'. CCQ: 'If I am accountable for the forecast and it is wrong, does that mean it is my fault? "
    "(No -- it means it was my call to make, and I own the result.)' CCQ 'mitigation': 'Does mitigation remove the "
    "risk, or reduce it? (Reduce it.)'",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'variance' (VAIR-ee-ans, 3 silabas), 'accountability' "
    "(a-coun-ta-BIL-i-ty -- 6 silabas, stress na 5a; brasileiro trava aqui), 'bottleneck' (BOT-l-neck, o 'tt' vira "
    "um tap americano), 'mitigation' (mit-i-GAY-shun). E o stress errado que faz o interlocutor pedir 'sorry?'.",
    ["Variance", "Accountability", "Bottleneck", "Mitigation", "Turnaround"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Todas sao frases que ele ja disse em portugues numa reuniao de resultados.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"We closed the quarter with a two million ", "shortfall", ".\""),
     ("\"Approvals were the ", "bottleneck", " &mdash; not the sales team.\""),
     ("\"The ", "root cause", " was a hiring freeze nobody told us about.\""),
     ("\"She should have ", "escalated", " the problem in week two.\""),
     ("\"", "Accountability", " is not blame &mdash; it is knowing whose call it was.\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. Four little structures that let you judge the "
    "past without attacking the person.' Passe ao proximo.",
    "Chapter 3: The Code", "Should, Could,", "Must",
    "The grammar of a verdict", L.IMG['code']))

S.append(L.s_discovery(
    11, 3,
    "<strong>Grammar discovery (7 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos. Pergunte: 'All four "
    "talk about the past. But which one is a criticism, which one is a lost opportunity, and which one is a guess?' "
    "Espere ele separar. So entao clique 'Reveal the Rule'. CCQ: 'She SHOULD HAVE escalated -- did she escalate? "
    "(No.) Somebody MUST HAVE flagged it -- am I sure? (Yes, almost certain.) We COULD HAVE caught it -- did we? "
    "(No, but we had the chance.)'",
    [("\"She <span style=\"color:#dc2626;font-weight:700\">should have escalated</span> the problem in week two.\"",
      "She should have escalated the problem in week two."),
     ("\"We <span style=\"color:#b45309;font-weight:700\">could have caught</span> it at the first milestone.\"",
      "We could have caught it at the first milestone."),
     ("\"Somebody <span style=\"color:#15803d;font-weight:700\">must have flagged</span> this before the board met.\"",
      "Somebody must have flagged this before the board met."),
     ("\"The variance <span class=\"accent\" style=\"font-weight:700\">might have been</span> a timing issue.\"",
      "The variance might have been a timing issue.")],
    "All four are about the past. So which one is a "
    "<span style=\"color:#dc2626;font-weight:700\">criticism</span>, which is a "
    "<span style=\"color:#b45309;font-weight:700\">missed chance</span>, and which is a "
    "<span style=\"color:#15803d;font-weight:700\">deduction</span>?",
    [("should have + participle",
      "The right action that did NOT happen. A verdict &mdash; polite, but a verdict.",
      "She <strong>should have escalated</strong> it."),
     ("shouldn't have + participle",
      "The wrong action that DID happen.",
      "We <strong>shouldn't have signed</strong> before the audit."),
     ("could have + participle",
      "A real possibility that existed and was not taken. Softer than <em>should</em> &mdash; no blame.",
      "We <strong>could have caught</strong> it at the first milestone."),
     ("must have + participle",
      "A confident deduction: you are almost sure it happened.",
      "Somebody <strong>must have flagged</strong> this."),
     ("might / may have + participle",
      "A tentative deduction. Your hedging tool &mdash; it keeps the room calm.",
      "It <strong>might have been</strong> a timing issue.")],
    "In real speech they all contract to the same sound: <strong>should've</strong>, <strong>could've</strong>, "
    "<strong>must've</strong> &mdash; never \"should of\". Say them fast; that is how they are heard.",
    "rule3"))

S.append(L.s_mistake(
    12, 3,
    "<strong>Common mistake (4 min):</strong> Dois erros aqui. (1) 'should of' -- o brasileiro escreve o que ouve, "
    "e o certo e should HAVE / should've. (2) O portugues usa 'deveria ter escalado' e o brasileiro traduz para "
    "'she should escalated' ou 'she should have escalate'. O participio e obrigatorio. Peca que ele leia as certas "
    "em voz alta DUAS vezes.",
    [("She should escalated the problem in week two.",
      "She should have escalated the problem in week two."),
     ("We could of caught it at the first milestone.",
      "We could have caught it at the first milestone."),
     ("Somebody must flagged this before the board meeting.",
      "Somebody must have flagged this before the board meeting.")],
    "The pattern never changes: <strong>modal + have + past participle</strong>. Never \"should of\" (that is only "
    "how <strong>should've</strong> sounds), and never a bare verb after <em>have</em>."))

S.append(L.s_fill(
    13, 3,
    "<strong>Practice (4 min):</strong> Leia cada frase. Felipe escolhe o modal ORALMENTE antes de clicar. Se "
    "travar, pergunte: 'Verdict, missed chance, or deduction?'",
    "Practice", "Which", "Modal?", "Say it first, then click to check",
    [("\"The risk was obvious in March. She ", "should have escalated", " it then.\""),
     ("\"Nobody told us about the hiring freeze. We ", "couldn't have known", ".\""),
     ("\"The numbers were on his desk. He ", "must have seen", " the variance.\""),
     ("\"We ", "shouldn't have signed", " off before the audit was finished.\""),
     ("\"It ", "might have been", " a timing issue &mdash; let me check the cut-off date.\"")]))

S.append(L.s_fill(
    14, 3,
    "<strong>Detalhe: verdict vs no-blame (3 min):</strong> Regra de ouro do registro senior: SHOULD julga a pessoa, "
    "COULD julga a situacao. Numa performance review, comece por COULD e so use SHOULD quando o ponto for inegociavel. "
    "Felipe escolhe qual usar ANTES de revelar -- e explique POR QUE.",
    "Register", "Should or", "Could?", "Which one keeps the room on your side?",
    [("\"To a direct report you respect: 'We ", "could have", " caught this earlier.'\""),
     ("\"To the board, about your own call: 'I ", "should have", " pushed back harder.'\""),
     ("\"About a person who ignored a clear warning: 'She ", "should have", " escalated it.'\""),
     ("\"About a risk nobody could see: 'Honestly, we ", "couldn't have", " known.'\"")]))

S.append(L.s_chapter(
    15, 4,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'Claire Whitfield is your CEO. She is not angry. She is "
    "curious -- and that is a much harder room.' Passe ao proximo.",
    "Chapter 4: The Review Meeting", "Your CEO Wants the", "Whole Story",
    "The review begins", L.IMG['context']))

S.append(L.s_dialogue(
    16, 4,
    "<strong>Dialogo (7 min):</strong> Voce e a Claire, CEO. Clique 'Next Line' a cada fala. Para cada fala do "
    "Felipe, peca que ELE fale primeiro, depois toque o audio para comparar. Observe se ele consegue usar SHOULD "
    "sobre si mesmo e COULD sobre a equipe -- e a marca do lider. CELEBRE quando sair sozinho.",
    "The Quarterly", "Review",
    [("claire", "C", "ellen",
      "Felipe, the quarter closed eight percent below plan. Before we talk about the fix, I want your reading of "
      "the root cause.",
      "Felipe, the quarter closed eight percent below plan. Before we talk about the fix, I want your reading of "
      "the root cause."),
     ("felipe", "F", "arthur",
      "The <span class=\"vocab-highlight\">root cause</span> was approvals. They were the "
      "<span class=\"vocab-highlight\">bottleneck</span>, not the sales team. And I should have seen it sooner "
      "&mdash; the signal was in the February numbers.",
      "The root cause was approvals. They were the bottleneck, not the sales team. And I should have seen it "
      "sooner. The signal was in the February numbers."),
     ("claire", "C", "ellen",
      "Somebody must have noticed that in February. Why did it not reach me?",
      "Somebody must have noticed that in February. Why did it not reach me?"),
     ("felipe", "F", "arthur",
      "Two people flagged it internally. It should have been <span class=\"vocab-highlight\">escalated</span> to "
      "you in week two, and it was not. That is on me &mdash; I own the "
      "<span class=\"vocab-highlight\">accountability</span> for what reaches this room.",
      "Two people flagged it internally. It should have been escalated to you in week two, and it was not. That is "
      "on me. I own the accountability for what reaches this room."),
     ("claire", "C", "ellen",
      "I appreciate that. What could the team have done differently?",
      "I appreciate that. What could the team have done differently?"),
     ("felipe", "F", "arthur",
      "They could have caught it at the first <span class=\"vocab-highlight\">milestone</span>. The "
      "<span class=\"vocab-highlight\">mitigation</span> is a standing rule now: any "
      "<span class=\"vocab-highlight\">variance</span> above five percent goes to you the same week, not the same "
      "quarter.",
      "They could have caught it at the first milestone. The mitigation is a standing rule now: any variance above "
      "five percent goes to you the same week, not the same quarter.")]))

S.append(L.s_comprehension(
    17, 4,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a CLAIRE, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar depois que ele responder.",
    "About", "Claire",
    [("What does Claire want before they discuss the fix?",
      "His reading of the root cause."),
     ("Which deduction does she make about February?",
      "That somebody must have noticed the problem &mdash; and she asks why it never reached her."),
     ("How does she move the conversation from Felipe to the team?",
      "She asks what the team could have done differently.")]))

S.append(L.s_listening(
    18, 4,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A COO opens a quarterly business review. Just listen -- no text.' "
    "Toque SEM texto, 2 vezes. As perguntas aparecem quando o audio termina. Peca que ele CONTE quantos modal "
    "perfects ouviu -- ouvido treinado antes de boca treinada.",
    1, "Listening", "The COO Opens the", "Review",
    "A quarterly business review, from the chair. Sound first &mdash; no text.",
    "a3_listening_coo.mp3", SLUG,
    [("What does the COO say about the shortfall?",
      "It was eight percent, and the root cause was the approval process, not the sales team."),
     ("What should have happened in week two?",
      "The variance should have been escalated to the leadership team."),
     ("What is the new rule?",
      "Any variance above five percent is escalated in the same week.")]))

S.append(L.s_listening(
    19, 4,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now the head of FP&amp;A gives her own retrospective. Same quarter, "
    "different chair.' Toque 2 vezes. Depois pergunte: 'She uses could have, not should have, about her team. Why?' "
    "&#201; O ponto da aula: o modal escolhe o registro.",
    2, "Listening 2", "The Retrospective", "From FP&amp;A",
    "The same quarter, seen from the team that missed it. Sound first &mdash; no text.",
    "a3_listening_fpa.mp3", SLUG,
    [("What does she say her team could have done?",
      "Caught the variance at the first milestone, instead of waiting for the month-end close."),
     ("What does she take responsibility for herself?",
      "Not escalating the bottleneck &mdash; she says she should have raised it earlier."),
     ("What does she refuse to do?",
      "Blame the sales team, because approvals were the real bottleneck.")]))

S.append(L.s_chapter(
    20, 5,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now we train: detective, the scorecard, and questions that "
    "come fast.' Passe ao proximo.",
    "Chapter 5: Practice", "Train Under", "Pressure",
    "Detective &middot; The Scorecard &middot; Quick Fire", L.IMG['practice']))

S.append(L.s_error(
    21, 5,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Felipe corrige ANTES de clicar. Os dois primeiros "
    "sao O erro classico (participio ausente / 'could of'). Trate como vitoria quando ele achar sozinho.",
    [("She should escalated the problem in week two.",
      "She should have escalated the problem in week two."),
     ("We could of caught it at the first milestone.",
      "We could have caught it at the first milestone."),
     ("He must saw the variance in the report.",
      "He must have seen the variance in the report."),
     ("We shouldn't signed off before the audit finished.",
      "We shouldn't have signed off before the audit finished.")]))

S.append(L.s_artifact(
    22, 5,
    "<strong>Artefato (4 min):</strong> Este e o scorecard que a Claire tem na mao ANTES da reuniao. Peca que o "
    "Felipe leia cada linha e transforme em UMA frase com modal perfect -- e que escolha should ou could de "
    "proposito, justificando o registro. E o exercicio mais dificil da aula, e o mais util.",
    "The Artifact", "The Quarterly", "Scorecard",
    "Q3 SCORECARD", "Finance &middot; Confidential",
    [("Reviewed with", "Felipe Pimenta, CFO"),
     ("Revenue vs plan", "&minus;8% (shortfall: USD 2.0m)"),
     ("Largest variance", "Approvals cycle &mdash; 21 days (plan: 7)"),
     ("Root cause", "Bottleneck in approvals, not sales"),
     ("First warning", "February close &mdash; not escalated"),
     ("Escalated to CEO", "Week 11 (should have been: week 2)"),
     ("Mitigation in place", "Variance &gt;5% escalated same week")],
    [("Turn \"First warning: not escalated\" into a modal perfect.",
      "\"It should have been escalated in week two.\""),
     ("Now say the same about your TEAM, without blaming them.",
      "\"They could have caught it at the first milestone.\""),
     ("Make a confident deduction about the February close.",
      "\"Somebody must have seen the variance in February.\"")]))

S.append(L.s_quickfire(
    23, 5,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO, antes de "
    "voce mostrar as tips. Exija a frase inteira com modal perfect -- resposta de 3 palavras nao conta. E aqui que "
    "ele fragmenta: velocidade importa mais que perfeicao.",
    "The CEO Asks. You", "Answer."))

S.append(L.s_building(
    24, 5,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords. Felipe monta a frase COMPLETA em voz alta, "
    "depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo antes de "
    "tentar.",
    [("she / escalate / the problem / week two (verdict)",
      "She should have escalated the problem in week two."),
     ("we / catch / it / first milestone (missed chance, no blame)",
      "We could have caught it at the first milestone."),
     ("somebody / flag / this / before the board met (confident deduction)",
      "Somebody must have flagged this before the board met."),
     ("we / not sign off / before the audit (wrong action that happened)",
      "We shouldn't have signed off before the audit."),
     ("the variance / be / a timing issue (tentative deduction)",
      "The variance might have been a timing issue.")]))

S.append(L.s_chapter(
    25, 6,
    "<strong>Transicao role-play (1 min):</strong> Diga: 'Now the real thing. Twice: once you receive the verdict, "
    "once you give it. The second is harder.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Both Sides of the", "Table",
    "Guided &gt; Semi-free &gt; Free", L.IMG['turn']))

S.append(L.s_roleplay(
    26, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Claire, CEO. Pergunte: 'Give me your reading of the "
    "shortfall.' Felipe usa as keywords. Deixe conduzir. Observe: ele usa SHOULD sobre si mesmo?",
    "Explain the", "Shortfall",
    "Your CEO asks for your reading of an eight percent miss. Give her the root cause, say what should have "
    "happened and when, and end with the mitigation you have already put in place.",
    ["The root cause was...", "It should have been escalated...", "We could have caught it at...",
     "The mitigation is..."]))

S.append(L.s_roleplay(
    27, 6,
    "<strong>Role-play Semi-free (5 min):</strong> INVERTA. Agora o Felipe e o chefe: voce e a analista de FP&amp;A "
    "que nao escalou o problema. Ele tem de dar o feedback duro SEM destruir a pessoa -- comecar por COULD, chegar "
    "no SHOULD, e terminar com o que muda. Se ele so usar 'should', pare e peca de novo mais suave. E o registro que "
    "esta em jogo, nao a gramatica.",
    "Now You Give the", "Verdict",
    "You are the CFO. Your FP&amp;A analyst saw the variance in February and did not escalate it. Give her the "
    "feedback: what she could have done, what she should have done, and what happens now. Do not destroy her &mdash; "
    "she is good, and you want to keep her.",
    ["You could have caught it at...", "It should have been escalated when...",
     "What I need from you next quarter is...", "Let us agree on the rule."],
    tint='.12'))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: a performance review inteira, ZERO pistas. NAO "
    "interrompa, NAO corrija no meio -- anote e devolva depois. Cronometre 3 min. CELEBRE: ele acabou de fazer nos "
    "dois papeis o que a maioria dos executivos brasileiros so consegue fazer em portugues.",
    "The Whole", "Review",
    "Run the full quarterly review, end to end. Open with the numbers, give the root cause, say what should have "
    "happened and who should have made it happen, take your own accountability, and close with the mitigation and "
    "the next milestone.",
    []))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Extensao / pressao (4 min):</strong> So faca se sobrar tempo E ele estiver fluindo. Aqui voce "
    "INTERROMPE de proposito, uma vez, no meio da resposta -- e exatamente o gatilho que o faz trocar para o "
    "portugues. Diga: 'Sorry, let me stop you there --' e faca a pergunta. Se ele se recuperar em ingles, a aula "
    "cumpriu o objetivo do programa.",
    "The", "Interruption",
    "The hardest version: the board member cuts you off in the middle of your answer and asks, \"But whose call was "
    "it, exactly?\" Do not restart your speech. Answer the question in one sentence, then take back the floor.",
    []))

S.append(L.s_chapter(
    30, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'You judged the past tonight -- and you stayed a leader while "
    "you did it.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You Gave the", "Verdict",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("It should have been escalated in week two.",
     "Isso deveria ter sido escalado na segunda semana."),
    ("We could have caught it at the first milestone.",
     "Poder&#237;amos ter identificado no primeiro marco."),
    ("Somebody must have seen the variance in February.",
     "Algu&#233;m deve ter visto a vari&#226;ncia em fevereiro."),
    ("I own the accountability for what reaches this room.",
     "Eu assumo a responsabilidade pelo que chega a esta sala."),
    ("The root cause was the bottleneck in approvals, not the sales team.",
     "A causa raiz foi o gargalo nas aprova&#231;&#245;es, n&#227;o o time de vendas."),
]

S.append(L.s_survival(
    31, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Sao as 5 "
    "frases de qualquer review -- e servem inteiras numa entrevista quando perguntarem 'how do you handle "
    "underperformance?'.",
    "Five Phrases for the", "Review",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    32, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 3 no passaporte (registra no Supabase).",
    N,
    ["I can use should have / shouldn't have to say what was right or wrong.",
     "I can use could have for a missed chance, without blaming anyone.",
     "I can use must have and might have for deductions about the past.",
     "I can give hard feedback in English and keep the person on my side.",
     "I know my words: shortfall, variance, root cause, bottleneck, accountability."]))

S.append(L.s_complete(
    33, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 3 complete, Felipe. You earned your Accountability Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) pegar a ultima reuniao de resultados REAL dele e escrever 5 "
    "frases com modal perfect sobre ela -- 2 com should, 2 com could, 1 com must -- e gravar lendo; (2) na proxima "
    "review de verdade, dar UM feedback comecando por 'you could have'. Proxima aula: Wishes, Regrets, and What "
    "Could Be Different (wish / if only).",
    N, "Accountability Badge", "You judged the past, Felipe. And you stayed senior.",
    "Wishes, Regrets, and What Could Be Different"))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'What Should Have Happened -- Modal Perfects',
    'short_title': 'What Should Have Happened',
    'menu_desc': 'Performance review + modal perfects (should/could/must have)',
    'desc': ('Analisar um trimestre que n&#227;o bateu a meta e dar (e receber) feedback duro sem destruir a '
             'rela&#231;&#227;o. Key words: performance review, shortfall, variance, root cause, bottleneck, to '
             'escalate, to flag, accountability, to miss a target, turnaround, mitigation, milestone. Structures: '
             'modal perfects &mdash; should have / shouldn\'t have (veredito), could have (chance perdida, sem culpa), '
             'must have / might have (dedu&#231;&#227;o sobre o passado).'),
    'hub_img': 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'claire': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. &#201; o vocabul&#225;rio de toda reuni&#227;o de '
                    'resultados que voc&#234; j&#225; conduziu &mdash; agora em ingl&#234;s.'),

    'context_text': (
        'The quarter closed eight percent below plan: a two million <strong>shortfall</strong>. In the '
        '<strong>variance</strong> report, one line stood out. The approvals cycle had stretched from seven days to '
        'twenty-one. That was the <strong>bottleneck</strong>, and it was the <strong>root cause</strong> &mdash; not '
        'the sales team, as everyone had assumed. Two analysts <strong>flagged</strong> it in February. '
        '<strong>It should have been escalated</strong> to the CEO in week two, and it was not. '
        '<strong>Somebody must have seen</strong> the number at the February close &mdash; it was on the first page. '
        'The team <strong>could have caught</strong> it at the first <strong>milestone</strong>, and Felipe says that '
        'he <strong>should have pushed</strong> harder when he first saw the cycle time. He does not blame his '
        'analysts: <strong>accountability</strong>, he tells the board, is not the same as fault. It means knowing '
        'whose call it was. The <strong>mitigation</strong> is now a standing rule: any variance above five percent '
        'reaches the CEO the same week. The <strong>turnaround</strong> took one quarter.'),

    'context_quiz': [
        ("\"It should have been escalated in week two.\" O que realmente aconteceu?",
         [("Foi escalado na segunda semana, como devia.", False),
          ("N&#195;O foi escalado &mdash; e o certo era ter sido.", True),
          ("Ser&#225; escalado na segunda semana do pr&#243;ximo trimestre.", False)]),
        ("Por que o texto usa \"could have caught\" para o time, e \"should have pushed\" para o Felipe?",
         [("Porque could have &#233; uma chance perdida (sem culpa) e should have &#233; um veredito &mdash; ele "
           "cobra de si, n&#227;o do time.", True),
          ("Porque could have e should have significam exatamente a mesma coisa.", False),
          ("Porque could have &#233; passado e should have &#233; futuro.", False)]),
        ("Which sentence is correct English?",
         [("Somebody must saw the variance in February.", False),
          ("Somebody must have seen the variance in February.", True),
          ("Somebody must of seen the variance in February.", False)]),
    ],

    'tip_title': 'Modal Perfects (should / could / must have)',
    'tip_intro': ('Como julgar o passado sem atacar a pessoa &mdash; a gram&#225;tica de toda performance review '
                  '(explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("should have + past participle",
         "A a&#231;&#227;o certa que N&#195;O aconteceu. Um veredito educado. The right action that did not happen.",
         "She <strong>should have escalated</strong> it."),
        ("shouldn't have + past participle",
         "A a&#231;&#227;o errada que ACONTECEU. The wrong action that did happen.",
         "We <strong>shouldn't have signed</strong> off."),
        ("could have + past participle",
         "Uma chance real que existia e n&#227;o foi tomada. Mais suave &mdash; SEM culpa. A missed possibility.",
         "We <strong>could have caught</strong> it earlier."),
        ("couldn't have + past participle",
         "Era imposs&#237;vel. Protege voc&#234; e a equipe. It was impossible.",
         "We <strong>couldn't have known</strong> about the freeze."),
        ("must have + past participle",
         "Dedu&#231;&#227;o CONFIANTE sobre o passado. A confident deduction.",
         "Somebody <strong>must have seen</strong> it."),
        ("might / may have + past participle",
         "Dedu&#231;&#227;o CAUTELOSA. O seu hedging &mdash; mant&#233;m a sala calma.",
         "It <strong>might have been</strong> a timing issue."),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (dois erros de brasileiro):</strong> (1) o partic&#237;pio &#233; '
                 'obrigat&#243;rio &mdash; "she should have <strong>escalated</strong>", nunca "should escalated" nem '
                 '"should have escalate". (2) Na fala, <strong>should\'ve</strong> soa como "should of" &mdash; mas '
                 '"should of" N&#195;O existe na escrita. E o de ouro: <strong>should</strong> julga a pessoa, '
                 '<strong>could</strong> julga a situa&#231;&#227;o. Numa review, comece sempre pelo <em>could</em>.'),

    'blanks': [
        ("She", "should have escalated", "Dica: veredito &mdash; a a&#231;&#227;o certa que n&#227;o aconteceu",
         "She should have escalated the problem in week two.", "the problem in week two."),
        ("We", "could have caught", "Dica: chance perdida, sem culpa &mdash; could + have + partic&#237;pio",
         "We could have caught it at the first milestone.", "it at the first milestone."),
        ("Somebody", "must have seen", "Dica: dedu&#231;&#227;o confiante &mdash; must + have + partic&#237;pio",
         "Somebody must have seen the variance in February.", "the variance in February."),
        ("We", "shouldn't have signed", "Dica: a a&#231;&#227;o errada que aconteceu (contra&#237;do)",
         "We shouldn't have signed off before the audit was finished.",
         "off before the audit was finished."),
        ("Nobody told us about the freeze, so we", "couldn't have known",
         "Dica: era imposs&#237;vel &mdash; protege voc&#234; e a equipe",
         "Nobody told us about the freeze, so we couldn't have known.", "."),
        ("The variance", "might have been", "Dica: dedu&#231;&#227;o cautelosa (hedging)",
         "The variance might have been a timing issue.", "a timing issue."),
    ],

    'order_title': 'Put the Performance Review in Order',
    'order_intro': ('Coloque as etapas de uma review de resultados na ordem correta. &#201; a sequ&#234;ncia que '
                    'transforma uma bronca numa an&#225;lise.'),
    'order': [
        (2, "Name the root cause &mdash; and separate it from the symptom."),
        (5, "Agree the mitigation and the next milestone."),
        (1, "Open with the number: the shortfall and the variance, with no excuses."),
        (4, "Take your own accountability before you assign anyone else's."),
        (3, "Say what should have happened, and when."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases de uma '
                     'review &mdash; e as que respondem "how do you handle underperformance?" numa entrevista.'),
    'speech': SURVIVAL,

    'quiz': [
        ("Your CEO asks why the problem never reached her. The most senior answer is:",
         [("\"My analysts didn't tell me. I only found out last week.\"", False),
          ("\"It should have been escalated in week two, and it wasn't. I own that.\"", True),
          ("\"It should of been escalated in week two.\"", False)]),
        ("You give feedback to a good analyst who missed the variance. You start with:",
         [("\"You should have caught this. It was on the first page.\"", False),
          ("\"You could have caught this at the first milestone &mdash; let's talk about how.\"", True),
          ("\"You must have seen this and ignored it.\"", False)]),
        ("The numbers were clearly on his desk. You are almost certain he saw them:",
         [("\"He must have seen the variance in the report.\"", True),
          ("\"He must saw the variance in the report.\"", False),
          ("\"He should have seen the variance in the report.\"", False)]),
        ("Nobody could have predicted the hiring freeze. You protect your team:",
         [("\"We should have known about the freeze.\"", False),
          ("\"Nobody told us about the freeze, so we couldn't have known.\"", True),
          ("\"We could have known about the freeze if we wanted.\"", False)]),
        ("You are not sure yet whether the gap is real or just a timing issue. You say:",
         [("\"The variance must have been a timing issue.\"", False),
          ("\"The variance might have been a timing issue &mdash; let me check the cut-off date.\"", True),
          ("\"The variance is definitely a timing issue.\"", False)]),
    ],

    'think': ("Your CEO says: \"The quarter closed eight percent below plan. Walk me through it.\" Answer for 2-3 "
              "minutes. Give the root cause, use should have at least twice (once about yourself), could have at "
              "least once (about your team, without blaming them), and one deduction with must have or might have. "
              "Finish with the mitigation and the next milestone."),

    'listenings': [
        {"file": "a3_listening_coo.mp3", "voice": "arthur",
         "text": ("Good morning. Let me open the quarterly review with the number, because there is no point hiding "
                  "it. We closed eight percent below plan, a shortfall of two million dollars. Now, the root cause. "
                  "For weeks everyone in this building assumed the problem was the sales team. It was not. The "
                  "approvals cycle had stretched from seven days to twenty-one. That was the bottleneck. Two "
                  "analysts flagged it in February, and here is the part I want us all to sit with: it should have "
                  "been escalated to this leadership team in week two, and it was not. Somebody must have seen that "
                  "number at the February close, because it was on the first page of the variance report. We could "
                  "have caught it at the first milestone. From today there is one new rule, and it is not "
                  "negotiable. Any variance above five percent reaches this room in the same week, not the same "
                  "quarter. That is the mitigation. The turnaround starts now.")},
        {"file": "a3_listening_fpa.mp3", "voice": "ellen",
         "text": ("Thanks for making time. I want to give you my own retrospective on the quarter, from the team "
                  "that owns the numbers. First, what my team could have done. We could have caught the variance at "
                  "the first milestone, in February, instead of waiting for the month-end close in March. The "
                  "signal was there. It was small, and we treated it as noise. Second, what I should have done. I "
                  "saw the approvals cycle stretching, and I should have raised it with you directly rather than "
                  "adding a line to a report. That delay is mine, not theirs. What I am not going to do is blame "
                  "the sales team, because approvals were the real bottleneck and the data is very clear on that. "
                  "Going forward, my team escalates anything above five percent the same week, and we review the "
                  "cycle time at every milestone, not only at close.")},
    ],

    'inclass_blocks': {
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Why did the problem never reach me?\"",
                 "tips": ["It should have been escalated in week two, and it wasn't.",
                          "I own the accountability for what reaches this room.",
                          "Own it in one sentence &mdash; do not narrate."]},
                {"situation": "\"What could your team have done differently?\"",
                 "tips": ["They could have caught it at the first milestone.",
                          "could have = missed chance, no blame"]},
                {"situation": "\"Somebody must have seen this in February. Who?\"",
                 "tips": ["Two analysts flagged it internally.",
                          "The failure was the escalation, not the detection."]},
                {"situation": "\"Was this avoidable, honestly?\"",
                 "tips": ["The hiring freeze, no &mdash; we couldn't have known.",
                          "The approvals cycle, yes &mdash; we should have acted in February."]},
                {"situation": "\"Is the gap real, or just timing?\"",
                 "tips": ["It might have been a timing issue &mdash; let me check the cut-off date.",
                          "Hedge when you are not sure. Never guess with confidence."]},
                {"situation": "\"So what stops this happening again?\"",
                 "tips": ["Any variance above five percent reaches you the same week.",
                          "Finish every review with the mitigation and the next milestone."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Succession -- Season 2 (HBO Max)",
         "Reuni&#245;es de conselho em que cada frase &#233; um veredito sobre o passado. Connection to Lesson 3: "
         "conte quantos <em>should have</em> e <em>could have</em> aparecem numa &#250;nica cena de board &mdash; e "
         "repare em quem usa qual, e por qu&#234;.",
         "Dica: assista com legenda em ingl&#234;s. Escolha uma cena e reescreva 3 falas trocando should por could "
         "&mdash; sinta a mudan&#231;a de registro.",
         "https://www.hbo.com/succession"),
        ("Podcast", "podcast", "HBR IdeaCast -- epis&#243;dios sobre feedback e accountability",
         "A Harvard Business Review entrevistando executivos sobre conversas dif&#237;ceis, avalia&#231;&#227;o de "
         "desempenho e responsabiliza&#231;&#227;o. Connection to Lesson 3: &#233; o vocabul&#225;rio exato desta "
         "aula, falado por quem lidera.",
         "Dica: ou&#231;a a 1x. Pare a cada modal perfect que ouvir e repita a frase inteira em voz alta.",
         "https://www.youtube.com/@HarvardBusinessReview"),
        ("YouTube", "youtube", "McKinsey -- Performance management &amp; the quarterly review",
         "Como as maiores empresas do mundo estruturam uma review trimestral: root cause, variance, mitigation. "
         "Connection to Lesson 3: o ingl&#234;s &#233; claro e pausado, e cada termo da sua aula aparece no contexto "
         "real.",
         "Dica: assista a 0.75x se precisar. Anote as 5 palavras da aula que aparecem sem tradu&#231;&#227;o.",
         "https://www.youtube.com/@McKinsey"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
