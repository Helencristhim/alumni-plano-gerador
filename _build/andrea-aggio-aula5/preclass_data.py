# -*- coding: utf-8 -*-
IMG = "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&q=80"
TITLE = "What's Next -- Plans, Goals & Commitments"
DESC = ("Talking about plans, goals and future commitments in professional contexts. Key words: to arrange, to schedule, "
        "to confirm, upcoming, to look forward to, commitment, MICE segment, corporate travel, luxury travel, all-inclusive, "
        "charter flight, ground operator. Structures: future forms -- 'going to' (plans), 'will' (decisions and offers), "
        "and present continuous for fixed arrangements.")

VOCAB = [
    ("To arrange", "to plan and organize something in advance (organizar, agendar)", "I will arrange a meeting for next week."),
    ("To schedule", "to fix a time for an event (marcar, agendar)", "We are going to schedule the fam trip for March."),
    ("To confirm", "to say officially that something is certain (confirmar)", "I will confirm the rates by email."),
    ("Upcoming", "happening soon, in the near future (próximo, que está por vir)", "Our upcoming fair is in Berlin."),
    ("To look forward to", "to feel happy about something that will happen (aguardar com expectativa)", "I look forward to working with you."),
    ("Commitment", "a promise or a plan you are sure about (compromisso)", "We made a firm commitment to expand."),
    ("MICE segment", "meetings, incentives, conferences and events travel (segmento de eventos corporativos)", "The MICE segment is growing fast."),
    ("Corporate travel", "business trips organized for companies (viagens corporativas)", "We are launching a corporate travel program."),
    ("Luxury travel", "high-end, premium travel experiences (turismo de luxo)", "Luxury travel is our fastest-growing area."),
    ("All-inclusive", "a package where meals and drinks are included (tudo incluído)", "Many clients prefer an all-inclusive package."),
    ("Charter flight", "a plane hired for a specific group or route (voo fretado)", "We are arranging a charter flight for the group."),
    ("Ground operator", "a local company that handles services at a destination (operador local, receptivo)", "Our ground operator will confirm the transfers."),
]

MATCH = [
    ("To arrange", "to plan and organize something in advance"),
    ("To schedule", "to fix a time for an event"),
    ("To confirm", "to say officially that something is certain"),
    ("Upcoming", "happening soon, in the near future"),
    ("To look forward to", "to feel happy about something that will happen"),
    ("Commitment", "a promise or a plan you are sure about"),
    ("MICE segment", "meetings, incentives, conferences and events travel"),
    ("Corporate travel", "business trips organized for companies"),
    ("Luxury travel", "high-end, premium travel experiences"),
    ("All-inclusive", "a package where meals and drinks are included"),
    ("Charter flight", "a plane hired for a specific group or route"),
    ("Ground operator", "a local company that handles services at a destination"),
]

CONTEXT = ("Andrea is planning next season with a partner named Henrik. \"We <strong>are going to</strong> expand our "
           "<strong>corporate travel</strong> program,\" he says, \"and we would love you for the <strong>MICE segment</strong>.\" "
           "Andrea already has some fixed plans. \"We <strong>are attending</strong> ITB in March,\" she replies, \"so let us "
           "<strong>schedule</strong> a meeting there.\" Henrik makes an offer on the spot: \"Before that, I <strong>will</strong> "
           "send you our <strong>upcoming</strong> rates and a draft agreement.\" Andrea agrees. \"If everything looks good, we "
           "<strong>will confirm</strong> the partnership and <strong>arrange</strong> a fam trip in April.\" It is a firm "
           "<strong>commitment</strong> from both sides. \"I really <strong>look forward to</strong> working with you,\" Andrea says.")

CONTEXT_QUIZ = [
    ("1. Why does Henrik say \"We are going to expand our program\"?",
     [("A", "Because it is a plan they decided before now (going to).", True),
      ("B", "Because he is deciding it at this exact moment.", False),
      ("C", "Because it already happened in the past.", False)]),
    ("2. \"We are attending ITB in March\" uses the present continuous because:",
     [("A", "It is a spontaneous decision made right now.", False),
      ("B", "It is a fixed arrangement already booked.", True),
      ("C", "It is a general fact that is always true.", False)]),
    ("3. Which sentence is a decision or offer made in the moment?",
     [("A", "I will send you the upcoming rates.", True),
      ("B", "We are going to expand next year.", False),
      ("C", "We are attending ITB in March.", False)]),
]

TIP_TITLE = "Future Forms: going to / will / present continuous"
TIP_SUB = "Como falar de planos, decisões e agendas com a forma de futuro certa (explicação em inglês e português)."
TIP_ROWS = [
    ("going to<br>am/is/are going to + verb", "Planos e intenções decididos antes de agora. Plans and intentions.", "We <strong>are going to</strong> expand."),
    ("will<br>will + base verb", "Decisões, ofertas e promessas feitas agora. Decisions, offers, promises.", "I <strong>will</strong> send the rates."),
    ("Present Continuous<br>am/is/are + -ing", "Compromissos fixos já marcados. Fixed arrangements already booked.", "We <strong>are attending</strong> ITB."),
    ("look forward to", "Depois de 'look forward to', use o verbo em -ing. After 'look forward to', use -ing.", "I look forward <strong>to working</strong> with you."),
]

FILL = [
    ('"Perfect, I ', "will", "Dica: oferta/decisão na hora, use 'will'", "Perfect, I will send you the rates after the fair.", ' send you the rates after the fair."'),
    ('"Our plan is clear: we ', "are going to", "Dica: plano já decidido, 'are going to'", "Our plan is clear: we are going to expand our portfolio.", ' expand our portfolio."'),
    ('"It is already booked: we ', "are attending", "Dica: agenda fixa, present continuous", "It is already booked: we are attending ITB in March.", ' ITB in March."'),
    ('"I look ', "forward", "Dica: expressão fixa 'look forward to'", "I look forward to working with you.", ' to working with you."'),
    ('"Let us ', "schedule", "Dica: marcar um horário para a reunião", "Let us schedule a meeting for next week.", ' a meeting for next week."'),
    ('"Do not worry, I ', "will", "Dica: promessa na hora, use 'will'", "Do not worry, I will confirm the rates today.", ' confirm the rates today."'),
]

ORDER_INTRO = "Coloque os passos de uma conversa de planejamento na ordem correta."
ORDER = [
    "Share your main goal for next season.",
    "Say which fair you are already attending.",
    "Offer to send the upcoming rates.",
    "Schedule a meeting to discuss the details.",
    "Confirm the partnership and next steps.",
]

SPEECH = [
    ("Next season, we are going to expand our portfolio.", "Na próxima temporada, vamos expandir o nosso portfólio."),
    ("We are attending ITB in March.", "Vamos participar da ITB em março."),
    ("I will send you the rates by the end of the week.", "Vou te enviar as tarifas até o fim da semana."),
    ("Let us schedule a meeting and confirm the details.", "Vamos marcar uma reunião e confirmar os detalhes."),
    ("I look forward to working with you.", "Estou ansiosa para trabalhar com você."),
]

QUIZ = [
    ("A partner asks about your plans. The best answer is:",
     [("A", "We will expanding our portfolio next season.", False),
      ("B", "We are going to expand our portfolio next season.", True),
      ("C", "We are going to expanding our portfolio next season.", False)]),
    ("You want to talk about a fair that is already booked. Which is correct?",
     [("A", "We will attending ITB in March.", False),
      ("B", "We are attending ITB in March.", True),
      ("C", "We attend ITB in March, maybe.", False)]),
    ("A partner asks you to send the rates. You make an offer on the spot:",
     [("A", "Of course, I will send them by Friday.", True),
      ("B", "Of course, I am sending them last week.", False),
      ("C", "Of course, I sending them by Friday.", False)]),
    ("You want to end the call warmly. You say:",
     [("A", "I look forward to work with you.", False),
      ("B", "I look forward to working with you.", True),
      ("C", "I look forward work with you.", False)]),
]

THINK = ("Imagine a partner asks about your professional plans for the next three months. Describe your goals using "
         "'going to', mention a fair you are already attending (present continuous), and make one offer or promise with "
         "'will'. Take your time.")

SURVIVAL = [
    ("Next season, we are going to expand our portfolio.", "Na próxima temporada, vamos expandir o nosso portfólio."),
    ("We are attending ITB in March.", "Vamos participar da ITB em março."),
    ("I will send you the rates by the end of the week.", "Vou te enviar as tarifas até o fim da semana."),
    ("Let us schedule a meeting and confirm the details.", "Vamos marcar uma reunião e confirmar os detalhes."),
    ("I look forward to working with you.", "Estou ansiosa para trabalhar com você."),
]
