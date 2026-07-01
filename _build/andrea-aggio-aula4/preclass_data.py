# -*- coding: utf-8 -*-
IMG = "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=600&q=80"
TITLE = "Talking About Your World -- Trips & Highlights"
DESC = ("Describing past experiences, trips and professional highlights. Key words: highlight, achievement, challenge, "
        "outcome, to turn out, to end up, tour operator, contract negotiation, hotel inspection, fam trip, rates, commission. "
        "Structures: past simple (regular and irregular verbs) and past questions with 'did'.")

VOCAB = [
    ("Highlight", "the best or most memorable part of an experience (ponto alto, destaque)", "The highlight of the trip was the hotel inspection."),
    ("Achievement", "something good you succeeded in doing (conquista, realização)", "Signing that contract was a real achievement."),
    ("Challenge", "a difficult task that tests your skills (desafio)", "The biggest challenge was the tight schedule."),
    ("Outcome", "the final result of an action or event (resultado)", "The outcome of the meeting was very positive."),
    ("To turn out", "to happen in a particular way in the end (acabar sendo, resultar)", "The trip turned out better than expected."),
    ("To end up", "to finally be in a situation or place (acabar em, terminar)", "We ended up signing three new contracts."),
    ("Tour operator", "a company that creates and sells travel packages (operadora de turismo)", "We partnered with a local tour operator."),
    ("Contract negotiation", "the discussion to agree the terms of a deal (negociação de contrato)", "The contract negotiation took two days."),
    ("Hotel inspection", "a visit to check a hotel's quality (vistoria de hotel)", "I did a hotel inspection before signing."),
    ("Fam trip", "a familiarization trip for agents to experience a destination (viagem de familiarização)", "We joined a fam trip to Portugal."),
    ("Rates", "the prices a hotel charges (tarifas, diárias)", "We agreed on special rates for next season."),
    ("Commission", "the percentage a company earns on each sale (comissão)", "The commission on that package is fifteen percent."),
]

MATCH = [
    ("Highlight", "the best or most memorable part of an experience"),
    ("Achievement", "something good you succeeded in doing"),
    ("Challenge", "a difficult task that tests your skills"),
    ("Outcome", "the final result of an action or event"),
    ("To turn out", "to happen in a particular way in the end"),
    ("To end up", "to finally be in a situation or place"),
    ("Tour operator", "a company that creates and sells travel packages"),
    ("Contract negotiation", "the discussion to agree the terms of a deal"),
    ("Hotel inspection", "a visit to check a hotel's quality"),
    ("Fam trip", "a familiarization trip for agents to experience a destination"),
    ("Rates", "the prices a hotel charges"),
    ("Commission", "the percentage a company earns on each sale"),
]

CONTEXT = ("Last November, Andrea <strong>attended</strong> WTM in London. She <strong>went</strong> with a clear goal: to find new "
           "hotel partners. The first two days <strong>were</strong> a real <strong>challenge</strong>, because the halls were huge "
           "and the schedule was tight. On the third day, she <strong>met</strong> Ricardo, a <strong>tour operator</strong> from "
           "Lisbon. He <strong>invited</strong> her on a <strong>fam trip</strong> to Portugal, where she <strong>did</strong> a full "
           "<strong>hotel inspection</strong> of six properties. The <strong>contract negotiation</strong> <strong>was</strong> tough, "
           "but in the end it <strong>turned out</strong> perfectly: they <strong>agreed</strong> on great <strong>rates</strong> and a "
           "fair <strong>commission</strong>. Andrea <strong>ended up</strong> signing three new contracts. The <strong>highlight</strong>, "
           "she says, was the moment she realized her English no longer got in the way.")

CONTEXT_QUIZ = [
    ("1. Why do we say \"Last November, Andrea attended WTM\"?",
     [("A", "Because it is a finished action at a finished time (past simple).", True),
      ("B", "Because it is happening right now.", False),
      ("C", "Because it is a routine she repeats every week.", False)]),
    ("2. \"She met Ricardo\" uses 'met' (not 'meeted') because:",
     [("A", "The verb 'meet' is regular and adds -ed.", False),
      ("B", "The verb 'meet' is irregular, so its past form changes completely.", True),
      ("C", "It is a present tense verb.", False)]),
    ("3. Which past question is correct?",
     [("A", "Did you signed the contract?", False),
      ("B", "Did you sign the contract?", True),
      ("C", "Did you signing the contract?", False)]),
]

TIP_TITLE = "The Past Simple"
TIP_SUB = "Como contar uma história no passado com a forma verbal certa (explicação em inglês e português)."
TIP_ROWS = [
    ("Regular verbs<br>verb + -ed", "Ação terminada, tempo terminado. Finished action, finished time.", "We <strong>signed</strong> the contract."),
    ("Irregular verbs<br>special past form", "Verbos comuns mudam completamente. Common verbs change.", "I <strong>went</strong> / met / did / flew."),
    ("Questions &amp; negatives<br>did + base verb", "Use 'did' + verbo na base (sem -ed). Use 'did' + base form.", "<strong>Did</strong> you <strong>meet</strong> them?"),
    ("Common irregulars", "go &rarr; went &middot; meet &rarr; met &middot; do &rarr; did &middot; fly &rarr; flew &middot; take &rarr; took &middot; be &rarr; was/were"),
]

FILL = [
    ('"Last November, I ', "attended", "Dica: verbo regular no passado, add -ed", "Last November, I attended a fair in London.", ' a fair in London."'),
    ('"On the third day, I ', "met", "Dica: irregular, meet vira 'met'", "On the third day, I met a tour operator.", ' a tour operator."'),
    ('"I ', "went", "Dica: irregular, go vira 'went'", "I went on a fam trip to Portugal.", ' on a fam trip to Portugal."'),
    ('"', "Did", "Dica: pergunta no passado, auxiliar 'Did'", "Did you negotiate good rates?", ' you negotiate good rates?"'),
    ('"The negotiation ', "turned", "Dica: regular, turn out vira 'turned out'", "The negotiation turned out perfectly.", ' out perfectly."'),
    ('"In the end, we ', "signed", "Dica: regular, sign vira 'signed'", "In the end, we signed three contracts.", ' three contracts."'),
]

ORDER_INTRO = "Coloque os passos de contar a história de uma viagem na ordem correta."
ORDER = [
    "Say where you went and when.",
    "Explain what your goal was.",
    "Describe the biggest challenge.",
    "Tell the highlight of the trip.",
    "Share the final outcome.",
]

SPEECH = [
    ("Last November, I attended a big fair in London.", "Em novembro passado, participei de uma grande feira em Londres."),
    ("The highlight was signing a new contract.", "O ponto alto foi assinar um novo contrato."),
    ("The biggest challenge was the tight schedule.", "O maior desafio foi a agenda apertada."),
    ("In the end, it turned out better than expected.", "No fim, acabou melhor do que o esperado."),
    ("I ended up with three new partners.", "Acabei com três novos parceiros."),
]

QUIZ = [
    ("A colleague asks: \"Where did you go last month?\" You answer:",
     [("A", "I go to Portugal last month.", False),
      ("B", "I went to Portugal last month.", True),
      ("C", "I am going to Portugal last month.", False)]),
    ("You want to ask about a past deal. Which is correct?",
     [("A", "Did you signed the contract?", False),
      ("B", "Did you sign the contract?", True),
      ("C", "Do you signed the contract?", False)]),
    ("You want to describe how a hard trip finished well. You say:",
     [("A", "It was tough at first, but in the end it turned out perfectly.", True),
      ("B", "It is tough, but it turns out perfectly.", False),
      ("C", "It will be tough, but it turned out perfectly.", False)]),
    ("You want to share a professional achievement. The best sentence is:",
     [("A", "I ended up with three new partners after the trip.", True),
      ("B", "I ending up with three new partners after the trip.", False),
      ("C", "I end up with three new partners after the trip.", False)]),
]

THINK = ("Imagine a colleague asks about a real professional trip or fair you attended. Tell the whole story in the past "
         "simple: where you went, what you did, who you met, the biggest challenge, and the final outcome. Take your time.")

SURVIVAL = [
    ("Last November, I attended a big fair in London.", "Em novembro passado, participei de uma grande feira em Londres."),
    ("The highlight was signing a new contract.", "O ponto alto foi assinar um novo contrato."),
    ("The biggest challenge was the tight schedule.", "O maior desafio foi a agenda apertada."),
    ("In the end, it turned out better than expected.", "No fim, acabou melhor do que o esperado."),
    ("I ended up with three new partners.", "Acabei com três novos parceiros."),
]
