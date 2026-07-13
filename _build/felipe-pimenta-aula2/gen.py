#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 2 — Talking About What Went Wrong (Past Financial Decisions).
Gramatica: third conditional + hedging (in hindsight).
Modelo: LEITURA (aula PAR, REGRA 29) — ic-reading + gist + true/false.
Callback (REGRA 20): o warm-up retoma o vocab da aula 1 (background, private equity).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
from felipe_lib import *  # noqa: F401,F403
import felipe_lib as L    # noqa: E402

N = 2
SLUG = 'felipe-pimenta'

VOCAB = [
    ("Write-off", "an amount a company accepts it has completely lost",
     "baixa cont&#225;bil, preju&#237;zo reconhecido",
     "The failed acquisition ended in a thirty million write-off."),
    ("Due diligence", "the detailed check you run on a company before you buy it",
     "auditoria pr&#233;via",
     "In hindsight, our due diligence was far too fast."),
    ("Valuation", "the price the market puts on a company",
     "avalia&#231;&#227;o, valuation",
     "The valuation looked cheap until we read the contracts."),
    ("Burn rate", "how fast a company spends its cash every month",
     "taxa de queima de caixa",
     "Their burn rate doubled in six months."),
    ("Runway", "how many months of cash a company has left",
     "f&#244;lego de caixa",
     "That deal cut our runway from eighteen months to nine."),
    ("Red flag", "an early warning sign that something is wrong",
     "sinal de alerta",
     "The auditor's note was a red flag, and we ignored it."),
    ("Assumption", "something you accept as true without proof",
     "premissa, suposi&#231;&#227;o",
     "The whole model rested on one optimistic assumption."),
    ("To underestimate", "to think something is smaller or easier than it really is",
     "subestimar",
     "We underestimated how long the integration would take."),
    ("Downside", "the loss you face if things go badly",
     "cen&#225;rio negativo, risco de perda",
     "Nobody at the table modeled the downside."),
    ("Contingency", "money or a plan you keep in reserve for problems",
     "reserva de conting&#234;ncia",
     "We should have kept a contingency for the tax liability."),
    ("Hindsight", "understanding an event only after it has happened",
     "retrospecto",
     "Hindsight makes every bad deal look obvious."),
    ("To overpay", "to pay more than something is really worth",
     "pagar acima do valor",
     "If we had walked away, we would not have overpaid."),
]

PHASES = ["The Deal That Failed", "The Language of Loss", "The Post-Mortem",
          "The Code", "In the Room", "Your Turn", "Wrap-Up"]

# ------------------------------------------------------------------ slides
S = []

S.append(L.s_title(
    1, 1,
    "<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Every CFO has one deal they wish they "
    "could undo. Tonight we learn to talk about it -- in the language of people who own their mistakes "
    "without being destroyed by them.' NAO cumprimente de forma scriptada (REGRA 27A).",
    "Lesson 2 &middot; Post-Mortem", "The Deal You Wish You Could", "Undo",
    "Owning a bad decision is not weakness. In English, it is the most senior thing you can do."))

S.append(L.s_hook(
    2, 1,
    "<strong>Warm-up + callback (5 min):</strong> Retome a aula 1 ANTES do tema novo (REGRA 20). Pergunte: "
    "'Last time you told your story -- your background, your years in private equity. Tonight: what is one "
    "decision from those years you would take back?'. Deixe falar 2-3 min, ZERO correcao. Anote onde ele "
    "fragmenta -- o gap dele e falar sob pressao, e falar de erro E pressao.",
    "Chapter 1: The Deal That Failed",
    "One Decision You Would", "Take Back",
    "Think of your years in private equity, or a call you made as CFO. No names, no numbers. Just the decision."))

S.append(L.s_cards3(
    3, 1,
    "<strong>Enquadramento (3 min):</strong> Explique POR QUE esta aula existe. Em portugues, admitir erro soa "
    "como confissao. Em ingles corporativo, existe uma gramatica INTEIRA que serve para admitir o erro E "
    "proteger a sua autoridade: o third conditional + hedging. Quem nao tem essa gramatica ou nega o erro ou "
    "se humilha. O Felipe precisa do meio-termo.",
    "Why This Lesson Exists", "Admitting a Mistake Is a", "Grammar",
    [("Deny it", "you lose trust with the board"),
     ("Apologize too much", "you lose authority in the room"),
     ("Third conditional", "you own it, you analyze it, you stay senior")],
    "\"If we had run proper due diligence, we wouldn't have overpaid.\" That sentence protects you and the truth at the same time."))

S.append(L.s_cards3(
    4, 1,
    "<strong>Objetivo (2 min):</strong> Diga: 'Three missions: the words of a loss, a real post-mortem memo, "
    "and the grammar of hindsight.' Antecipe o role-play final: ele vai apresentar o post-mortem para o board.",
    "Tonight's Goal", "Three", "Missions",
    [("1. The Words", "write-off, red flag, runway, downside..."),
     ("2. The Memo", "read a real post-mortem of a failed deal"),
     ("3. The Code", "If we had..., we would have...")]))

S.append(L.s_chapter(
    5, 2,
    "<strong>Transicao vocab (1 min):</strong> Diga: 'First, the vocabulary of a deal that goes wrong. Twelve "
    "words. You have lived every one of them.' Passe ao proximo.",
    "Chapter 2: The Language of Loss", "The Words of a", "Bad Deal",
    "12 words &mdash; the ones nobody teaches you in an English course.", L.IMG['vocab']))

S.append(L.s_vocab(
    6, 2,
    "<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista em ingles, Felipe tenta a palavra, depois revele. "
    "CCQ 'burn rate': 'If a company burns two million a month and has ten million, what is the runway? "
    "(Five months.)' CCQ 'red flag': 'Is a red flag proof that something is wrong, or a warning? (A warning "
    "-- a signal to look closer.)' Toque o audio e peca que repita.",
    "1-6", VOCAB[:6], 1, 0))

S.append(L.s_vocab(
    7, 2,
    "<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. 'Hindsight' e 'downside' sao o coracao da aula "
    "-- insista. CCQ 'assumption': 'Is an assumption a fact? (No -- something we accept as true without proof.)' "
    "CCQ 'contingency': 'Is a contingency money you plan to spend, or money you hope NOT to spend? (Money you "
    "hope not to spend.)'",
    "7-12", VOCAB[6:], 2, 6))

S.append(L.s_pron(
    8, 2,
    "<strong>Pronunciation drill (3 min):</strong> Foque em: 'due diligence' (DUE DIL-i-gence, 3 silabas no "
    "diligence), 'valuation' (val-yu-AY-shun -- brasileiro erra pondo o stress no VAL), 'contingency' "
    "(con-TIN-gen-cy), 'hindsight' (HIND-site, som limpo de /aɪ/). O stress errado e o que faz o interlocutor "
    "pedir para repetir -- e e aqui que o Felipe trava.",
    ["Due diligence", "Valuation", "Contingency", "Hindsight", "Burn rate"]))

S.append(L.s_fill(
    9, 2,
    "<strong>Vocab in context (3 min):</strong> Leia cada frase. Felipe diz a palavra que falta ANTES de clicar. "
    "Se travar, de a primeira letra. Todas sao frases que ele ja ouviu em reuniao -- em portugues.",
    "In Context", "Fill the", "Gap", "Say the missing word first, then click to check",
    [("\"The auditor's note was a clear ", "red flag", ", and we ignored it.\""),
     ("\"We wrote the loss off the books &mdash; a thirty million ", "write-off", ".\""),
     ("\"Nobody in that meeting modeled the ", "downside", ".\""),
     ("\"Their cash was falling fast: the ", "burn rate", " had doubled.\""),
     ("\"The entire model rested on one optimistic ", "assumption", ".\"")]))

S.append(L.s_chapter(
    10, 3,
    "<strong>Transicao leitura (1 min):</strong> Diga: 'This is a real document: a post-mortem memo. When a deal "
    "fails, someone has to write this. One day, that someone is you.' Passe ao proximo.",
    "Chapter 3: The Post-Mortem", "The Memo Nobody Wants to", "Write",
    "Read it the way the board will read it.", L.IMG['context']))

S.append(L.s_blocks(
    11, 3,
    "<strong>Leitura + gist (7 min):</strong> Felipe le em SILENCIO primeiro (2 min), sem dicionario. Depois "
    "pergunte a ideia central ANTES de mostrar as alternativas -- so entao clique no gist. Nao traduza nada. "
    "Se ele pedir uma palavra, devolva: 'What do you think it means, from the context?'",
    "Read for the Main Idea", "A Post-Mortem of a Failed", "Acquisition",
    ["reading", "gist"]))

S.append(L.s_blocks(
    12, 3,
    "<strong>True or False (5 min):</strong> Felipe responde ORALMENTE e JUSTIFICA com o trecho do texto antes "
    "de clicar. A justificativa e o exercicio -- e ela que forca frase completa. Clicar revela verdict + "
    "justificativa (toggle, REGRA 27E).",
    "Check Understanding", "True or", "False?", ["tf"]))

S.append(L.s_blocks(
    13, 3,
    "<strong>Discussao (5 min):</strong> Aqui o Felipe FALA. Estas perguntas puxam a experiencia real dele na "
    "Aqua Capital. Nao corrija durante -- anote. Se ele trocar para o portugues, so aponte para a tela e espere. "
    "O silencio e seu aliado.",
    "Discuss", "Talk It", "Through", ["guiding"]))

S.append(L.s_chapter(
    14, 4,
    "<strong>Transicao grammar (1 min):</strong> Diga: 'Now the code. One structure changes a confession into an "
    "analysis.' Passe ao proximo.",
    "Chapter 4: The Code", "The Grammar of", "Hindsight",
    "If we had known... we would have...", L.IMG['code']))

S.append(L.s_discovery(
    15, 4,
    "<strong>Grammar discovery (7 min):</strong> NAO de a regra primeiro. Leia os 4 exemplos. Pergunte: 'What is "
    "the real story here -- did we run the due diligence, yes or no?' (Nao.) 'And did we overpay?' (Sim.) So "
    "entao clique 'Reveal the Rule'. CCQ: 'If we HAD run diligence -- did we run it? (No.) We WOULD HAVE seen "
    "the risk -- did we see it? (No.)' O third conditional descreve um passado que NAO aconteceu.",
    [("\"If we <span style=\"color:#15803d;font-weight:700\">had run</span> proper due diligence, we "
      "<span style=\"color:#1d4ed8;font-weight:700\">would have seen</span> the risk.\"",
      "If we had run proper due diligence, we would have seen the risk."),
     ("\"If the board <span style=\"color:#15803d;font-weight:700\">had modeled</span> the downside, we "
      "<span style=\"color:#1d4ed8;font-weight:700\">wouldn't have overpaid</span>.\"",
      "If the board had modeled the downside, we wouldn't have overpaid."),
     ("\"We <span style=\"color:#1d4ed8;font-weight:700\">would have kept</span> our runway if we "
      "<span style=\"color:#15803d;font-weight:700\">hadn't closed</span> that deal.\"",
      "We would have kept our runway if we hadn't closed that deal."),
     ("\"<span class=\"accent\" style=\"font-weight:700\">In hindsight</span>, the valuation "
      "<span class=\"accent\" style=\"font-weight:700\">may have been</span> too optimistic.\"",
      "In hindsight, the valuation may have been too optimistic.")],
    "The green verbs are in the <span style=\"color:#15803d;font-weight:700\">past perfect</span>. "
    "The blue ones are <span style=\"color:#1d4ed8;font-weight:700\">would have + participle</span>. "
    "So &mdash; did any of it actually happen?",
    [("Third Conditional<br>If + past perfect, would have + participle",
      "An imaginary past. The condition did NOT happen, so the result did NOT happen either.",
      "If we <strong>had run</strong> diligence, we <strong>would have seen</strong> it."),
     ("Negative<br>hadn't / wouldn't have",
      "The same imaginary past, the other way round.",
      "We <strong>wouldn't have overpaid</strong> if we <strong>hadn't rushed</strong>."),
     ("Order is free",
      "Either half can come first. Comma only when the if-half opens.",
      "We would have kept our runway <strong>if we hadn't closed</strong>."),
     ("Hedging<br>in hindsight / arguably / may have been",
      "Softens the blame so you stay senior instead of sounding defensive.",
      "<strong>In hindsight</strong>, the valuation <strong>may have been</strong> optimistic.")],
    "Say it out loud as a native does: <strong>If we'd run</strong> diligence, we<strong>'d have seen</strong> it. "
    "The contraction is not laziness &mdash; it is the sound of fluency.",
    "rule2"))

S.append(L.s_mistake(
    16, 4,
    "<strong>Common mistake (4 min):</strong> ESTE e o erro de todo brasileiro senior. Em portugues: 'se eu "
    "SOUBESSE, eu NAO TERIA comprado' -- dois tempos simples. Em ingles o SE exige past perfect (had known) e o "
    "resultado exige would have. NUNCA 'if I would have'. Peca que ele leia as versoes certas em voz alta DUAS "
    "vezes -- e a frase que ele vai usar no board.",
    [("If we would have known the risk, we didn't buy the company.",
      "If we had known the risk, we wouldn't have bought the company."),
     ("If I knew about the tax liability, I would not sign the contract.",
      "If I had known about the tax liability, I wouldn't have signed the contract."),
     ("In the hindsight, we payed too much.",
      "In hindsight, we overpaid.")],
    "The if-half NEVER takes <strong>would</strong>. It takes the <strong>past perfect</strong> (had + participle). "
    "The other half takes <strong>would have + participle</strong>. And the expression is <strong>in hindsight</strong> "
    "&mdash; no article."))

S.append(L.s_fill(
    17, 4,
    "<strong>Grammar practice (4 min):</strong> Leia cada frase. Felipe monta o tempo verbal ORALMENTE antes de "
    "clicar. Se travar, pergunte: 'Did it happen? No? Then it is the imaginary past.'",
    "Practice", "Complete the", "Sentence", "Say it first, then click to check",
    [("\"If we had asked for the audited numbers, we ", "would have found", " the problem.\""),
     ("\"If the seller ", "hadn't hidden", " the tax liability, we would have paid less.\""),
     ("\"We wouldn't have lost the runway if we ", "had kept", " a contingency.\""),
     ("\"If I ", "had pushed back", " harder in that meeting, the deal would have died.\""),
     ("\"In hindsight, the assumption ", "may have been", " too optimistic.\"")]))

S.append(L.s_chapter(
    18, 5,
    "<strong>Transicao dialogo (1 min):</strong> Diga: 'The board wants an explanation. Diana Reis chairs the "
    "audit committee, and she is not hostile -- she is precise. That is worse.' Passe ao proximo.",
    "Chapter 5: In the Room", "The Audit Committee Wants a", "Word",
    "The meeting begins", L.IMG['turn']))

S.append(L.s_dialogue(
    19, 5,
    "<strong>Dialogo (7 min):</strong> Voce e a Diana, presidente do comite de auditoria. Clique 'Next Line' a "
    "cada fala. Para cada fala do Felipe, peca que ELE fale primeiro, depois toque o audio para comparar. CELEBRE "
    "quando o third conditional sair sem travar. Observe: ele consegue admitir o erro SEM se desculpar demais?",
    "Explain the", "Write-Off",
    [("diana", "D", "ellen",
      "Felipe, thank you for coming. The committee has read the memo. Before we discuss the numbers, I want to "
      "hear it from you: what went wrong?",
      "Felipe, thank you for coming. The committee has read the memo. Before we discuss the numbers, I want to "
      "hear it from you: what went wrong?"),
     ("felipe", "F", "arthur",
      "The short answer is that we moved too fast. If we had run proper <span class=\"vocab-highlight\">due "
      "diligence</span>, we would have found the tax liability before we signed.",
      "The short answer is that we moved too fast. If we had run proper due diligence, we would have found the "
      "tax liability before we signed."),
     ("diana", "D", "ellen",
      "There were <span class=\"vocab-highlight\">red flags</span>, though. The auditor's note. Why did nobody "
      "stop?",
      "There were red flags, though. The auditor's note. Why did nobody stop?"),
     ("felipe", "F", "arthur",
      "In <span class=\"vocab-highlight\">hindsight</span>, we underestimated that note. The "
      "<span class=\"vocab-highlight\">valuation</span> looked cheap, and cheap is persuasive. If I had pushed "
      "back harder, the deal would have died &mdash; and I should have let it die.",
      "In hindsight, we underestimated that note. The valuation looked cheap, and cheap is persuasive. If I had "
      "pushed back harder, the deal would have died, and I should have let it die."),
     ("diana", "D", "ellen",
      "That is a fair answer. So what protects us next time?",
      "That is a fair answer. So what protects us next time?"),
     ("felipe", "F", "arthur",
      "Three things: a modeled <span class=\"vocab-highlight\">downside</span>, a "
      "<span class=\"vocab-highlight\">contingency</span> of ten percent, and a rule that no deal closes without "
      "audited numbers. I have already written them into the process.",
      "Three things: a modeled downside, a contingency of ten percent, and a rule that no deal closes without "
      "audited numbers. I have already written them into the process.")]))

S.append(L.s_comprehension(
    20, 5,
    "<strong>Comprehension (2 min):</strong> Pergunte sobre a DIANA, nunca sobre o Felipe (REGRA 27F). Clique para "
    "revelar cada resposta depois que ele responder.",
    "About", "Diana",
    [("What does Diana ask for before discussing the numbers?",
      "His own account &mdash; she wants to hear what went wrong from him."),
     ("Which detail does she push him on?",
      "The red flags &mdash; especially the auditor's note."),
     ("How does she react to his explanation?",
      "She calls it a fair answer, and asks what protects the company next time.")]))

S.append(L.s_listening(
    21, 5,
    "<strong>Listening 1 (5 min):</strong> Diga: 'A partner at a fund runs a post-mortem for his investors. Just "
    "listen -- no text.' Toque SEM texto, 2 vezes. As perguntas aparecem quando o audio termina. O listening dele "
    "e forte: use para dar confianca antes do role-play.",
    1, "Listening", "The Partner's", "Post-Mortem",
    "A fund partner explains a loss to his investors. Sound first &mdash; no text.",
    "a2_listening_partner.mp3", SLUG,
    [("What does the partner say about the due diligence?",
      "It was too fast &mdash; six weeks instead of the usual three months."),
     ("What was the red flag they ignored?",
      "The auditor's note about the tax liability."),
     ("What has the fund changed since?",
      "No deal closes without audited numbers and a modeled downside.")]))

S.append(L.s_listening(
    22, 5,
    "<strong>Listening 2 (4 min):</strong> Diga: 'Now a CEO tells the whole company the same story -- but she is "
    "protecting morale, not analyzing.' Toque 2 vezes. Depois pergunte: 'Which one sounded more senior, and why?' "
    "Compare o REGISTRO dos dois audios -- e o ponto pedagogico do slide.",
    2, "Listening 2", "The CEO Tells the", "Company",
    "The same failure, a different room. Sound first &mdash; no text.",
    "a2_listening_ceo.mp3", SLUG,
    [("What does the CEO refuse to do?",
      "Blame any single person on the team."),
     ("What does she say she would have done differently?",
      "She would have asked harder questions before signing."),
     ("What is the one rule she announces?",
      "Every deal now needs a modeled downside and a contingency.")]))

S.append(L.s_chapter(
    23, 6,
    "<strong>Transicao practice (1 min):</strong> Diga: 'Now you train under pressure -- detective, the memo, and "
    "the questions that come fast.' Passe ao proximo.",
    "Chapter 6: Your Turn", "Own the", "Room",
    "Detective &middot; The Memo &middot; The Board", L.IMG['practice']))

S.append(L.s_error(
    24, 6,
    "<strong>Detective (4 min):</strong> Leia cada frase com erro. Pergunte 'What is wrong here?'. Felipe corrige "
    "ANTES de clicar. Os dois primeiros sao O erro do third conditional -- se ele achar sozinho, a regra pegou.",
    [("If we would have known the risk, we didn't buy the company.",
      "If we had known the risk, we wouldn't have bought the company."),
     ("If I knew about the liability, I would not have signed.",
      "If I had known about the liability, I wouldn't have signed."),
     ("In the hindsight, we payed too much for that company.",
      "In hindsight, we overpaid for that company."),
     ("We would have keep the runway if we hadn't close the deal.",
      "We would have kept the runway if we hadn't closed the deal.")]))

S.append(L.s_artifact(
    25, 6,
    "<strong>Artefato (4 min):</strong> Este e o memo que o board le ANTES de chamar o Felipe. Peca que ele leia "
    "em voz alta e depois transforme cada linha numa frase de third conditional. Impacto: e o documento real que "
    "ele vai ter de escrever um dia -- e agora ele tem a lingua para isso.",
    "The Artifact", "The Post-Mortem", "Memo",
    "PROJECT HELIOS", "Post-Mortem &middot; Confidential",
    [("Prepared by", "Felipe Pimenta, CFO"),
     ("Deal", "Acquisition of a payments processor"),
     ("Write-off", "USD 30 million"),
     ("Due diligence", "6 weeks (standard: 12)"),
     ("Red flag missed", "Auditor's note on tax liability"),
     ("Runway impact", "18 months &rarr; 9 months"),
     ("Root cause", "Downside was never modeled")],
    [("Turn \"Due diligence: 6 weeks\" into a third conditional.",
      "\"If we had taken twelve weeks, we would have found the liability.\""),
     ("Turn \"Red flag missed\" into a third conditional.",
      "\"If we hadn't ignored the auditor's note, we wouldn't have signed.\""),
     ("Now hedge the root cause line, out loud.",
      "\"In hindsight, the downside may have been too easy to ignore.\"")]))

S.append(L.s_quickfire(
    26, 6,
    "<strong>Quick fire (5 min):</strong> UMA pergunta por vez. Felipe responde em voz alta, COMPLETO, antes de "
    "voce mostrar as tips. Nao aceite resposta de 3 palavras -- peca a frase inteira, com third conditional. Se "
    "travar, mostre as tips e peca de novo. Velocidade importa mais que perfeicao: e exatamente a pressao que o "
    "faz trocar para o portugues.",
    "The Board Asks. You", "Answer."))

S.append(L.s_building(
    27, 6,
    "<strong>Sentence Building (4 min):</strong> Mostre as keywords. Felipe monta a frase COMPLETA em voz alta, "
    "depois clica para comparar com o modelo. Toggle: clicar de novo fecha (REGRA 27E). NAO deixe ele ler o modelo "
    "antes de tentar -- o gabarito visivel mata o exercicio.",
    [("if / we / run / due diligence -> we / find / the liability",
      "If we had run due diligence, we would have found the liability."),
     ("if / the board / model / the downside -> we / not overpay",
      "If the board had modeled the downside, we wouldn't have overpaid."),
     ("we / keep / our runway -> if / we / not close / that deal",
      "We would have kept our runway if we hadn't closed that deal."),
     ("in hindsight / the valuation / may / be / too optimistic",
      "In hindsight, the valuation may have been too optimistic."),
     ("if / I / push back / harder -> the deal / die",
      "If I had pushed back harder, the deal would have died.")]))

S.append(L.s_roleplay(
    28, 6,
    "<strong>Role-play Guided (4 min):</strong> Voce e a Diana. Pergunte: 'Walk us through what went wrong.' "
    "Felipe usa as keywords na tela. Deixe ele conduzir. Observe se o third conditional sai sozinho ou se ele "
    "recorre ao passado simples.",
    "Walk Us Through the", "Failure",
    "The audit committee asks you to explain the write-off. Give them the sequence: what you did, what you missed, "
    "and what you would have done differently.",
    ["We moved too fast on...", "If we had run...", "In hindsight, we underestimated...",
     "We wouldn't have overpaid if..."]))

S.append(L.s_roleplay(
    29, 6,
    "<strong>Role-play Semi-free (4 min):</strong> Agora a Diana pergunta a PARTE DIFICIL: de quem foi a culpa. "
    "Menos pistas. O Felipe tem de assumir responsabilidade SEM entregar a equipe e SEM se humilhar -- e a "
    "corda-bamba do registro senior. Se ele culpar alguem, pare e devolva: 'Say that again, but own it.'",
    "Who Was", "Responsible?",
    "Diana asks the hard question: whose decision was it? Take responsibility without blaming your team and "
    "without apologizing your way out of the room. Then tell her what the process looks like now.",
    ["I signed off on it, so...", "Arguably, we all...", "What I would have done differently is...",
     "The process now requires..."],
    tint='.12'))

S.append(L.s_roleplay(
    30, 6,
    "<strong>Free Practice (5 min):</strong> A missao da aula: o post-mortem inteiro, do zero, ZERO pistas. NAO "
    "interrompa, NAO corrija no meio -- anote e devolva depois (o Felipe trava se for cortado). Cronometre 3 min. "
    "CELEBRE muito no final: ele acabou de fazer em ingles a coisa mais dificil que um CFO faz.",
    "The Whole", "Post-Mortem",
    "From \"Thank you for the time\" to \"Here is what changes\": present the post-mortem end to end. The deal, the "
    "assumption, the red flag, the write-off, what you would have done differently, and the three rules that "
    "protect the company now.",
    []))

S.append(L.s_chapter(
    31, 7,
    "<strong>Transicao wrap-up (1 min):</strong> Diga: 'You just did the hardest thing a CFO does in English: you "
    "owned a loss and stayed senior.' Passe ao proximo.",
    "Chapter 7: Wrap-Up", "You Owned", "It",
    "", L.IMG['wrap']))

SURVIVAL = [
    ("If we had run proper due diligence, we would have found the problem.",
     "Se tiv&#233;ssemos feito uma auditoria pr&#233;via adequada, ter&#237;amos encontrado o problema."),
    ("In hindsight, the valuation may have been too optimistic.",
     "Em retrospecto, a avalia&#231;&#227;o pode ter sido otimista demais."),
    ("We wouldn't have overpaid if the board had modeled the downside.",
     "N&#227;o ter&#237;amos pago acima do valor se o conselho tivesse modelado o cen&#225;rio negativo."),
    ("I signed off on it, so the decision was mine.",
     "Eu aprovei, ent&#227;o a decis&#227;o foi minha."),
    ("Here is what the process requires now.",
     "&#201; isto que o processo exige agora."),
]

S.append(L.s_survival(
    32, 7,
    "<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que o Felipe repita. Estas sao as "
    "5 frases que ele leva para QUALQUER conversa dificil sobre um erro -- board, investidor ou entrevista ('tell me "
    "about a failure').",
    "Five Phrases for the", "Post-Mortem",
    [p for p, _ in SURVIVAL]))

S.append(L.s_checklist(
    33, 7,
    "<strong>Checklist (2 min):</strong> Diga: 'Click each item if you feel confident.' Leia cada item. Os 5 checks "
    "marcados = aula completa e stamp 2 no passaporte (registra no Supabase).",
    N,
    ["I can explain a failed decision without denying it or apologizing too much.",
     "I can use the third conditional: if + past perfect, would have + participle.",
     "I can hedge with in hindsight, arguably, and may have been.",
     "I can read a post-mortem memo and turn each line into an analysis.",
     "I know my words: write-off, due diligence, red flag, runway, downside, contingency."]))

S.append(L.s_complete(
    34, 7,
    "<strong>Encerramento (2 min):</strong> Diga: 'Lesson 2 complete, Felipe. You earned your Hindsight Badge.' "
    "HOMEWORK (ORALMENTE, nunca escrito na tela): (1) escrever 5 frases de third conditional sobre decisoes REAIS "
    "da carreira dele (Aqua Capital ou fintech) e gravar lendo em voz alta; (2) na proxima reuniao de verdade, usar "
    "'in hindsight' UMA vez. Proxima aula: What Should Have Happened -- modal perfects (should have, could have, "
    "must have).",
    N, "Hindsight Badge", "You owned a thirty million loss. In English.",
    "What Should Have Happened"))

SLIDES = '\n'.join(S)

# ------------------------------------------------------------------ spec
SPEC = {
    'n': N,
    'title': 'Talking About What Went Wrong -- Past Financial Decisions',
    'short_title': 'Talking About What Went Wrong',
    'menu_desc': 'A post-mortem of a failed deal + third conditional',
    'desc': ('Explicar uma decis&#227;o financeira que deu errado sem negar o erro nem se humilhar. '
             'Key words: write-off, due diligence, valuation, burn rate, runway, red flag, assumption, '
             'to underestimate, downside, contingency, hindsight, to overpay. Structures: third conditional '
             '(if + past perfect, would have + particípio) e hedging (in hindsight, arguably, may have been).'),
    'hub_img': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80',
    'phases': PHASES,
    'vocab': VOCAB,
    'characters': {'felipe': 'arthur', 'diana': 'ellen'},

    'vocab_intro': ('Ou&#231;a cada termo e leia o exemplo. &#201; o vocabul&#225;rio de um neg&#243;cio que d&#225; '
                    'errado &mdash; o que ningu&#233;m ensina num curso de ingl&#234;s.'),

    'context_text': (
        'Two years ago, Felipe <strong>signed off</strong> on the acquisition of a small payments processor. '
        'The <strong>valuation</strong> looked cheap, and cheap is persuasive. The team ran the '
        '<strong>due diligence</strong> in six weeks instead of the usual twelve. The auditor left a short note '
        'about a tax liability &mdash; a <strong>red flag</strong> &mdash; and everyone <strong>underestimated</strong> '
        'it. The whole model rested on one optimistic <strong>assumption</strong>: that revenue would double in a year. '
        'It did not. The <strong>burn rate</strong> climbed, the <strong>runway</strong> fell from eighteen months to '
        'nine, and the company took a thirty million <strong>write-off</strong>. '
        '<strong>If the board had modeled the downside</strong>, it <strong>would have seen</strong> the risk. '
        '<strong>If Felipe had pushed back harder</strong>, the deal <strong>would have died</strong> &mdash; and he says '
        'today that he <strong>should have let it die</strong>. In <strong>hindsight</strong>, they '
        '<strong>overpaid</strong>. Nobody had kept a <strong>contingency</strong>. Today no deal closes without '
        'audited numbers, a modeled <strong>downside</strong>, and ten percent held back.'),

    'context_quiz': [
        ("Por que dizemos \"If the board had modeled the downside, it would have seen the risk\"?",
         [("Porque o conselho modelou o cen&#225;rio negativo e viu o risco.", False),
          ("Porque o conselho N&#195;O modelou &mdash; &#233; um passado imagin&#225;rio que n&#227;o aconteceu.", True),
          ("Porque o conselho vai modelar o cen&#225;rio negativo no pr&#243;ximo neg&#243;cio.", False)]),
        ("\"If Felipe had pushed back harder, the deal would have died.\" O que realmente aconteceu?",
         [("Ele insistiu e o neg&#243;cio morreu.", False),
          ("Ele N&#195;O insistiu, e o neg&#243;cio foi fechado.", True),
          ("Ele insistiu, mas o neg&#243;cio foi fechado mesmo assim.", False)]),
        ("Which sentence is correct English?",
         [("If we would have known the risk, we didn't buy the company.", False),
          ("If we had known the risk, we wouldn't have bought the company.", True),
          ("If we knew the risk, we would not bought the company.", False)]),
    ],

    'tip_title': 'Third Conditional + Hedging',
    'tip_intro': ('Como falar de um passado que N&#195;O aconteceu &mdash; a gram&#225;tica que transforma uma '
                  'confiss&#227;o em an&#225;lise (explica&#231;&#227;o em ingl&#234;s e portugu&#234;s).'),
    'tip_rows': [
        ("Third Conditional<br>If + past perfect, would have + participle",
         "Passado imagin&#225;rio: a condi&#231;&#227;o N&#195;O aconteceu, ent&#227;o o resultado tamb&#233;m N&#195;O aconteceu. "
         "An imaginary past &mdash; neither half happened.",
         "If we <strong>had run</strong> diligence, we <strong>would have seen</strong> it."),
        ("Negativa",
         "hadn't + partic&#237;pio / wouldn't have + partic&#237;pio.",
         "We <strong>wouldn't have overpaid</strong> if we <strong>hadn't rushed</strong>."),
        ("Ordem livre",
         "Qualquer metade vem primeiro. V&#237;rgula s&#243; quando a metade com <em>if</em> abre a frase.",
         "We would have kept our runway <strong>if we hadn't closed</strong>."),
        ("Na fala: contra&#231;&#227;o",
         "<strong>If we'd run</strong>... we<strong>'d have seen</strong>... &#201; assim que soa fluente.",
         "<strong>If we'd known</strong>, we<strong>'d have walked</strong> away."),
        ("Hedging<br>in hindsight / arguably / may have been",
         "Suaviza a culpa e mant&#233;m a sua autoridade. Softens blame without denying the fact.",
         "<strong>In hindsight</strong>, the valuation <strong>may have been</strong> optimistic."),
        ("Interrogativa",
         "What would you have done differently?",
         "<strong>What would you have done</strong> differently?"),
    ],
    'tip_note': ('<strong>Aten&#231;&#227;o (erro de brasileiro):</strong> em portugu&#234;s dizemos "se eu '
                 '<em>soubesse</em>, eu n&#227;o <em>teria comprado</em>". Em ingl&#234;s a metade com <em>if</em> '
                 'NUNCA leva <strong>would</strong>: &#233; <strong>if I had known</strong> (past perfect), e a outra '
                 'metade &#233; <strong>I wouldn\'t have bought</strong>. E a express&#227;o &#233; '
                 '<strong>in hindsight</strong> &mdash; sem artigo, nunca "in the hindsight".'),

    'blanks': [
        ("If we", "had run", "Dica: metade com if &mdash; past perfect (had + partic&#237;pio)",
         "If we had run proper due diligence, we would have found the problem.",
         "proper due diligence, we would have found the problem."),
        ("If the board had modeled the downside, we", "wouldn't have overpaid",
         "Dica: resultado imagin&#225;rio &mdash; would not have + partic&#237;pio (contra&#237;do)",
         "If the board had modeled the downside, we wouldn't have overpaid.", "."),
        ("We would have kept our runway if we", "hadn't closed",
         "Dica: metade com if, negativa &mdash; had not + partic&#237;pio (contra&#237;do)",
         "We would have kept our runway if we hadn't closed that deal.", "that deal."),
        ("In hindsight, the valuation", "may have been",
         "Dica: hedging &mdash; may + have + partic&#237;pio",
         "In hindsight, the valuation may have been too optimistic.", "too optimistic."),
        ("If I had pushed back harder, the deal", "would have died",
         "Dica: resultado imagin&#225;rio &mdash; would have + partic&#237;pio",
         "If I had pushed back harder, the deal would have died.", "."),
        ("We took a thirty million", "write-off",
         "Dica: o preju&#237;zo que a empresa reconhece nos livros",
         "We took a thirty million write-off on that acquisition.", "on that acquisition."),
    ],

    'order_title': 'Put the Post-Mortem in Order',
    'order_intro': ('Coloque as etapas de um post-mortem para o comit&#234; de auditoria na ordem correta. '
                    '&#201; a sequ&#234;ncia que mant&#233;m voc&#234; s&#234;nior na sala.'),
    'order': [
        (3, "Name the red flag you missed, without blaming any individual."),
        (5, "Close with the three rules that protect the company from now on."),
        (1, "State the facts: the deal, the write-off, the impact on the runway."),
        (4, "Say what you would have done differently, using the third conditional."),
        (2, "Explain the assumption the whole model rested on."),
    ],

    'speech_intro': ('Ou&#231;a cada frase e depois grave voc&#234; mesmo dizendo-a. S&#227;o as cinco frases de um '
                     'post-mortem &mdash; e as que respondem "tell me about a failure" numa entrevista.'),
    'speech': SURVIVAL,

    'quiz': [
        ("Diana asks: \"What would you have done differently?\" The best answer is:",
         [("\"If I would have known the risk, I didn't sign the contract.\"", False),
          ("\"If I had known about the tax liability, I wouldn't have signed the contract.\"", True),
          ("\"If I knew about the tax liability, I would not sign the contract.\"", False)]),
        ("You want to soften the blame without denying the fact. You say:",
         [("\"In the hindsight, the valuation was completely wrong.\"", False),
          ("\"In hindsight, the valuation may have been too optimistic.\"", True),
          ("\"The valuation was not my responsibility.\"", False)]),
        ("An investor asks who was responsible for the write-off. The most senior answer is:",
         [("\"The deal team pushed it through. I had my doubts.\"", False),
          ("\"I signed off on it, so the decision was mine. Here is what changes now.\"", True),
          ("\"I'm very sorry. It was completely my fault and I feel terrible about it.\"", False)]),
        ("You want to say the cash position got worse because of the deal:",
         [("\"That deal cut our runway from eighteen months to nine.\"", True),
          ("\"That deal cutted our runway since eighteen months.\"", False),
          ("\"That deal is cutting our runway for nine months.\"", False)]),
        ("In a job interview: \"Tell me about a decision you regret.\" You open with:",
         [("\"I don't really have any. My decisions have been good.\"", False),
          ("\"Two years ago I signed off on an acquisition. In hindsight, we moved too fast.\"", True),
          ("\"I regret many things but I prefer not to talk about it.\"", False)]),
    ],

    'think': ("A board member asks: \"Walk me through a financial decision that went wrong, and tell me what you "
              "would have done differently.\" Answer for 2-3 minutes. Use the third conditional (if we had..., we "
              "would have...) at least three times, and hedge at least once with \"in hindsight\" or \"arguably\". "
              "Take responsibility without blaming your team &mdash; and finish with what the process requires now."),

    'listenings': [
        {"file": "a2_listening_partner.mp3", "voice": "arthur",
         "text": ("Thank you all for joining. I want to be direct about the payments deal, because you deserve a "
                  "straight answer. We took a thirty million write-off, and the honest explanation is that we "
                  "moved too fast. We ran the due diligence in six weeks. Our standard is three months. If we had "
                  "taken the full three months, we would have found the tax liability, and I do not believe we "
                  "would have signed. There was a red flag: the auditor left a note, and we underestimated it. "
                  "In hindsight, the valuation looked cheap, and cheap is persuasive. Our whole model rested on "
                  "one assumption, that revenue would double, and it did not. Here is what has changed. No deal "
                  "closes without audited numbers. Every deal now carries a modeled downside, and we hold back a "
                  "contingency of ten percent. I would rather lose a deal than lose your trust.")},
        {"file": "a2_listening_ceo.mp3", "voice": "ellen",
         "text": ("Good morning, everyone. You have all seen the number, so let me talk about it openly. The "
                  "acquisition did not work, and we have taken a write-off. I want to say one thing very clearly: "
                  "I am not going to blame anyone on this team. The deal was approved by the board, and I signed "
                  "the recommendation. If I had asked harder questions before we signed, we would have caught the "
                  "problem, and I did not ask them. That is on me. What I want you to take from today is not fear. "
                  "It is a rule. From now on, every deal comes to the table with a modeled downside and a "
                  "contingency, and anyone in this company can raise a red flag without asking permission. We "
                  "underestimated a risk once. We are not going to underestimate the same one twice. Thank you for "
                  "the work you have put in this quarter.")},
    ],

    'inclass_blocks': {
        "reading": [{
            "kind": "reading",
            "rtitle": "Project Helios &mdash; Post-Mortem of a Failed Acquisition",
            "paras": [
                ("Two years ago the company acquired a small payments processor. The valuation looked cheap, and "
                 "cheap is persuasive. Under pressure to close before the quarter ended, the deal team ran the due "
                 "diligence in six weeks, half the usual time. The auditor left a short note about an unresolved "
                 "tax liability. Everyone read it. Nobody stopped."),
                ("The financial model rested on a single assumption: that revenue would double within a year. It "
                 "did not. Within two quarters the burn rate had climbed sharply and the runway had fallen from "
                 "eighteen months to nine. The tax liability surfaced exactly where the auditor said it would, and "
                 "the company took a write-off of thirty million dollars."),
                ("The lesson is not that the team was careless. It is that nobody in the room was asked to model "
                 "the downside. If the board had insisted on a downside case, it would have seen the risk. If the "
                 "CFO had pushed back on the timeline, the deal would have died &mdash; and in hindsight, it should "
                 "have. Arguably the strongest signal was the one that cost nothing to read: a two-line note from "
                 "an auditor."),
                ("Three rules now govern every acquisition. No deal closes without audited numbers. Every proposal "
                 "carries a modeled downside alongside the base case. And ten percent of the price is held back as "
                 "a contingency until the first audit clears. The company overpaid once. It does not intend to "
                 "overpay again."),
            ],
            "source": "Internal memo &mdash; Audit Committee, Q3",
        }],
        "gist": [{
            "kind": "gist",
            "prompt": "What is the best one-line summary of this memo?",
            "choices": [
                ["a", "The deal team was careless and should be replaced.", False],
                ["b", "A rushed process and an unmodeled downside turned a cheap-looking deal into a thirty "
                      "million write-off &mdash; and three new rules now prevent it.", True],
                ["c", "The acquisition succeeded, but the tax liability made it less profitable than expected.", False],
            ],
        }],
        "tf": [{
            "kind": "tf",
            "items": [
                ["The due diligence took the usual amount of time.", "f",
                 "It ran in six weeks &mdash; half the usual time &mdash; under pressure to close before quarter end."],
                ["The auditor warned about the tax liability before the deal closed.", "t",
                 "The auditor left a short note about an unresolved tax liability. Everyone read it; nobody stopped."],
                ["The company's runway got shorter after the acquisition.", "t",
                 "It fell from eighteen months to nine within two quarters."],
                ["The memo blames the deal team for being careless.", "f",
                 "It says explicitly that the lesson is not carelessness &mdash; nobody was asked to model the downside."],
                ["The company now holds back part of the price until the first audit clears.", "t",
                 "Ten percent is held back as a contingency."],
            ],
        }],
        "guiding": [{
            "kind": "guiding",
            "items": [
                "The memo says \"cheap is persuasive.\" Have you ever seen a low price stop people from asking hard "
                "questions? Tell the story.",
                "The auditor's note cost nothing to read, and it was the strongest signal. What is the equivalent "
                "\"two-line note\" that gets ignored in your company?",
                "If you had been the CFO on Project Helios, what would you have done differently &mdash; and at "
                "which exact moment?",
                "Which of the three new rules would have been hardest to sell to your board, and why?",
            ],
        }],
        "quickfire": [{
            "kind": "quickfire",
            "items": [
                {"situation": "\"Walk us through what went wrong.\"",
                 "tips": ["We moved too fast on the due diligence.",
                          "The model rested on one assumption, and it did not hold.",
                          "State facts first &mdash; analysis second."]},
                {"situation": "\"What would you have done differently?\"",
                 "tips": ["If we had taken the full twelve weeks, we would have found the liability.",
                          "if + past perfect -> would have + participle"]},
                {"situation": "\"There were red flags. Why did nobody stop?\"",
                 "tips": ["In hindsight, we underestimated the auditor's note.",
                          "Hedge, then own it &mdash; never blame the team."]},
                {"situation": "\"Whose decision was it, in the end?\"",
                 "tips": ["I signed off on it, so the decision was mine.",
                          "Own it in one short sentence. Then move to what changes."]},
                {"situation": "\"How do we know this will not happen again?\"",
                 "tips": ["No deal closes without audited numbers.",
                          "Every proposal now carries a modeled downside and a ten percent contingency."]},
                {"situation": "\"In an interview: tell me about a failure.\"",
                 "tips": ["Two years ago I signed off on an acquisition...",
                          "In hindsight, we moved too fast.",
                          "Finish with the rule you built from it."]},
            ],
        }],
    },

    'media': [
        ("Series", "series", "Industry -- Season 1 (HBO Max)",
         "Um banco de investimento em Londres, e gente jovem tendo de explicar posi&#231;&#245;es que deram errado "
         "para chefes que n&#227;o perdoam. Connection to Lesson 2: repare em como cada personagem admite um erro "
         "sem perder autoridade &mdash; e conte quantas vezes voc&#234; ouve \"if we had...\".",
         "Dica: assista com legenda em ingl&#234;s. Anote 3 frases de third conditional e leia em voz alta.",
         "https://www.hbo.com/industry"),
        ("Podcast", "podcast", "Acquired -- \"The Deal That Almost Killed Us\" (episodes on failed M&amp;A)",
         "Dois investidores dissecam aquisi&#231;&#245;es que destru&#237;ram valor, exatamente no vocabul&#225;rio "
         "desta aula: valuation, due diligence, write-off, downside. Connection to Lesson 2: &#233; o seu mundo, na "
         "sua l&#237;ngua-alvo, em velocidade nativa.",
         "Dica: ou&#231;a a 1x. Pare quando ouvir \"in hindsight\" e repita a frase inteira em voz alta.",
         "https://www.acquired.fm/"),
        ("YouTube", "youtube", "Aswath Damodaran -- \"When Acquisitions Destroy Value\" (NYU Stern)",
         "O professor de valuation mais conhecido do mundo explicando por que empresas pagam caro demais. "
         "Connection to Lesson 2: ele usa <em>overpay</em>, <em>assumption</em> e <em>downside</em> em cada "
         "minuto &mdash; e o ingl&#234;s dele &#233; claro e pausado.",
         "Dica: assista a 0.75x se precisar. Anote as 5 palavras da aula que ele usa sem traduzir.",
         "https://www.youtube.com/@AswathDamodaranonValuation"),
    ],
}

L.emit(SPEC, SLIDES, ROOT, HERE)
