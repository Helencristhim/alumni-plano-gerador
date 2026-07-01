# -*- coding: utf-8 -*-
IMG = "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&q=80"
TITLE = "Making It Stick -- Follow-Ups & Relationships"
DESC = ("Networking language, follow-ups and long-term relationships. Key words: to stay in touch, to circle back, "
        "to keep someone posted, mutual benefit, long-term relationship, business card, rate sheet, product presentation, "
        "preferred partner, exclusive deal, room block, volume agreement. Structures: polite modal verbs -- 'could' "
        "(requests), 'would' (offers), and 'should' (recommendations), always followed by the base verb.")

VOCAB = [
    ("To stay in touch", "to keep contact with someone over time (manter contato)", "Let us stay in touch after the fair."),
    ("To circle back", "to return to a topic or contact someone again later (retomar depois)", "I will circle back next week with the details."),
    ("To keep someone posted", "to keep someone informed of news (manter alguém informado)", "I will keep you posted on the dates."),
    ("Mutual benefit", "an advantage for both sides (benefício mútuo)", "This deal is a mutual benefit for us both."),
    ("Long-term relationship", "a professional connection that lasts for years (relacionamento de longo prazo)", "We are building a long-term relationship."),
    ("Business card", "a small card with your name and contact details (cartão de visita)", "Here is my business card."),
    ("Rate sheet", "a document listing a hotel's prices (tabela de tarifas)", "Could you send me your rate sheet?"),
    ("Product presentation", "a talk that introduces what a company offers (apresentação de produto)", "We would love to give you a product presentation."),
    ("Preferred partner", "a company you work with first, by agreement (parceiro preferencial)", "You are now our preferred partner in Brazil."),
    ("Exclusive deal", "an offer only one partner receives (acordo exclusivo)", "We can offer you an exclusive deal."),
    ("Room block", "a group of rooms reserved for one client or event (bloqueio de quartos)", "We should reserve a room block for the group."),
    ("Volume agreement", "a deal based on selling a large number of bookings (acordo por volume)", "A volume agreement gives you better rates."),
]

MATCH = [
    ("To stay in touch", "to keep contact with someone over time"),
    ("To circle back", "to return to a topic or contact someone again later"),
    ("To keep someone posted", "to keep someone informed of news"),
    ("Mutual benefit", "an advantage for both sides"),
    ("Long-term relationship", "a professional connection that lasts for years"),
    ("Business card", "a small card with your name and contact details"),
    ("Rate sheet", "a document listing a hotel's prices"),
    ("Product presentation", "a talk that introduces what a company offers"),
    ("Preferred partner", "a company you work with first, by agreement"),
    ("Exclusive deal", "an offer only one partner receives"),
    ("Room block", "a group of rooms reserved for one client or event"),
    ("Volume agreement", "a deal based on selling a large number of bookings"),
]

CONTEXT = ("Two days after the fair, Andrea writes a follow-up to Paulo, a partner she met in Portugal. \"It was a "
           "pleasure to meet you,\" she begins. \"<strong>Could</strong> you send me your <strong>rate sheet</strong> "
           "for next season?\" Paulo replies warmly. \"Of course. I <strong>would</strong> love to give you a short "
           "<strong>product presentation</strong>, too.\" Andrea sees the opportunity. \"There is a real "
           "<strong>mutual benefit</strong> here. You <strong>should</strong> visit our destination in high season.\" "
           "Paulo agrees and offers to make Escape Turismo a <strong>preferred partner</strong> with an "
           "<strong>exclusive deal</strong>. \"Let us <strong>stay in touch</strong>,\" Andrea says. \"I will "
           "<strong>keep you posted</strong> and <strong>circle back</strong> with the details. This is the start of a "
           "great <strong>long-term relationship</strong>.\"")

CONTEXT_QUIZ = [
    ("1. Why does Andrea say \"Could you send me your rate sheet?\" instead of \"Send me the rate sheet\"?",
     [("A", "Because 'could' makes the request polite and professional.", True),
      ("B", "Because 'could' talks about the past.", False),
      ("C", "Because 'could' is only used for ability.", False)]),
    ("2. \"You should visit our destination in high season\" is:",
     [("A", "A polite request.", False),
      ("B", "A recommendation or piece of advice.", True),
      ("C", "A promise about the past.", False)]),
    ("3. Which sentence correctly follows a modal with the base verb?",
     [("A", "I would love to help you.", True),
      ("B", "You should to visit us.", False),
      ("C", "Could you to send the rates?", False)]),
]

TIP_TITLE = "Polite Modals: could / would / should"
TIP_SUB = "Como fazer pedidos, ofertas e recomendações com educação (explicação em inglês e português)."
TIP_ROWS = [
    ("could + base verb", "Pedido educado ou sugestão leve. A polite request or soft suggestion.", "<strong>Could</strong> you <strong>send</strong> the rates?"),
    ("would + base verb", "Oferta calorosa ou desejo profissional. A warm offer or wish.", "I <strong>would love</strong> to help."),
    ("should + base verb", "Recomendação ou conselho. A recommendation or advice.", "You <strong>should visit</strong> in high season."),
    ("Regra de ouro / Golden rule", "Depois de could, would e should, use o verbo na base, SEM 'to'. After a modal, use the base verb, no 'to'.", "should visit (not <strong>should to visit</strong>)"),
]

FILL = [
    ('"', "Could", "Dica: pedido educado antes do verbo", "Could you send me your rate sheet?", ' you send me your rate sheet?"'),
    ('"I ', "would", "Dica: oferta calorosa, 'would love to'", "I would love to schedule a product presentation.", ' love to schedule a product presentation."'),
    ('"You ', "should", "Dica: recomendação, conselho", "You should visit our destination in high season.", ' visit our destination in high season."'),
    ('"Let us ', "stay", "Dica: manter contato depois da feira", "Let us stay in touch after the fair.", ' in touch after the fair."'),
    ('"I will ', "keep", "Dica: manter o parceiro informado", "I will keep you posted on the dates.", ' you posted on the dates."'),
    ('"There is a real ', "mutual benefit", "Dica: vantagem para os dois lados", "There is a real mutual benefit here.", ' here for both companies."'),
]

ORDER_INTRO = "Coloque os passos de uma mensagem de follow-up na ordem correta."
ORDER = [
    "Thank the person for meeting you at the fair.",
    "Make a polite request for the rate sheet.",
    "Offer a product presentation.",
    "Explain the mutual benefit of working together.",
    "Agree to stay in touch and keep them posted.",
]

SPEECH = [
    ("It was a pleasure to meet you at the fair.", "Foi um prazer conhecer você na feira."),
    ("Could you send me your rate sheet?", "Você poderia me enviar a sua tabela de tarifas?"),
    ("I would love to schedule a call.", "Eu adoraria marcar uma ligação."),
    ("You should visit our destination in high season.", "Você deveria visitar o nosso destino na alta temporada."),
    ("Let us stay in touch. I will keep you posted.", "Vamos manter contato. Eu vou te manter informado."),
]

QUIZ = [
    ("You want to ask a partner for their rate sheet, politely. You say:",
     [("A", "Send me the rate sheet now.", False),
      ("B", "Could you send me your rate sheet?", True),
      ("C", "Could you to send me your rate sheet?", False)]),
    ("You want to make a warm offer to a partner. The best choice is:",
     [("A", "I would love to give you a product presentation.", True),
      ("B", "I would loved to give you a product presentation.", False),
      ("C", "I will love giving you a product presentation.", False)]),
    ("A partner asks when to visit. You recommend high season. You say:",
     [("A", "You should to visit in high season.", False),
      ("B", "You should visiting in high season.", False),
      ("C", "You should visit in high season.", True)]),
    ("You want to end the message warmly and keep the door open. You say:",
     [("A", "Let us stay in touch. I will keep you posted.", True),
      ("B", "Let us stay in touch. I will keeping you posted.", False),
      ("C", "Let us to stay in touch. I keep you posted.", False)]),
]

THINK = ("Imagine you met a great supplier at a fair two days ago. Record a short follow-up message. Thank them, make a "
         "polite request with 'could', a warm offer with 'would', and a recommendation with 'should', and agree to stay "
         "in touch. Take your time.")

SURVIVAL = [
    ("It was a pleasure to meet you at the fair.", "Foi um prazer conhecer você na feira."),
    ("Could you send me your rate sheet?", "Você poderia me enviar a sua tabela de tarifas?"),
    ("I would love to schedule a call.", "Eu adoraria marcar uma ligação."),
    ("You should visit our destination in high season.", "Você deveria visitar o nosso destino na alta temporada."),
    ("Let us stay in touch. I will keep you posted.", "Vamos manter contato. Eu vou te manter informado."),
]
