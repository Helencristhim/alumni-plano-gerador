# -*- coding: utf-8 -*-
IMG = "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80"
TITLE = "Back in the Game -- Your Professional Identity"
DESC = ("Describing your role and your current projects at the travel agency. Key words: manage, oversee, "
        "coordinate, handle, liaise with, be responsible for, travel agency, hospitality industry, hotel portfolio, "
        "incoming tourism, outbound travel, destination management. Structures: present simple (role & routine) vs "
        "present continuous (projects happening right now).")

VOCAB = [
    ("Manage", "to be in charge of a team or an area (gerenciar, chefiar)", "I manage a team of eight people."),
    ("Oversee", "to watch over work and make sure it is done well (supervisionar)", "I oversee every deal the agency signs."),
    ("Coordinate", "to organize people and tasks so they work together (coordenar)", "I coordinate the calendar for all our trips."),
    ("Handle", "to deal with a task, a client, or a problem (lidar com, cuidar de)", "I handle the biggest clients myself."),
    ("Liaise with", "to stay in contact and work closely with someone (articular com)", "I liaise with hoteliers across Europe."),
    ("Be responsible for", "to have the duty to take care of something (ser responsável por)", "I am responsible for the European itineraries."),
    ("Travel agency", "a company that plans and sells trips to clients (agência de viagens)", "I work for a travel agency in Brazil."),
    ("Hospitality industry", "the sector of hotels, restaurants and tourism (setor de hotelaria)", "The hospitality industry is growing fast."),
    ("Hotel portfolio", "the group of hotels a company works with (portfólio de hotéis)", "We are expanding our hotel portfolio."),
    ("Incoming tourism", "visitors who come into your country (turismo receptivo)", "Incoming tourism to Europe is booming."),
    ("Outbound travel", "travelers who go abroad from your country (turismo emissivo)", "We are launching a new outbound travel program."),
    ("Destination management", "organizing the services and experiences at a place (gestão de destinos)", "Destination management is a big part of our work."),
]

MATCH = [
    ("Manage", "to be in charge of a team or an area"),
    ("Oversee", "to watch over work and make sure it is done well"),
    ("Coordinate", "to organize people and tasks so they work together"),
    ("Handle", "to deal with a task, a client, or a problem"),
    ("Liaise with", "to stay in contact and work closely with someone"),
    ("Be responsible for", "to have the duty to take care of something"),
    ("Travel agency", "a company that plans and sells trips to clients"),
    ("Hospitality industry", "the sector of hotels, restaurants and tourism"),
    ("Hotel portfolio", "the group of hotels a company works with"),
    ("Incoming tourism", "visitors who come into your country"),
    ("Outbound travel", "travelers who go abroad from your country"),
    ("Destination management", "organizing the services and experiences at a place"),
]

CONTEXT = ("Andrea <strong>is</strong> the Commercial Director at Escape Turismo, a <strong>travel agency</strong> in Brazil. "
           "Every week, she <strong>manages</strong> the commercial team, <strong>oversees</strong> the biggest deals, and "
           "<strong>liaises with</strong> hoteliers all over Europe. She <strong>is responsible for</strong> the European "
           "itineraries, so she <strong>coordinates</strong> the calendar and <strong>handles</strong> the key clients herself. "
           "This season, however, is different. Right now, the agency <strong>is going</strong> through fast growth. At the moment, "
           "her team <strong>is expanding</strong> the <strong>hotel portfolio</strong> in southern Europe and <strong>is launching</strong> "
           "a new <strong>outbound travel</strong> program for corporate clients. Andrea says the routine keeps the agency running, "
           "but the new projects keep it alive.")

CONTEXT_QUIZ = [
    ("1. Why do we say \"Every week, she manages the commercial team\"?",
     [("A", "Because it is a routine and a permanent part of her role (present simple).", True),
      ("B", "Because it is happening only at this exact moment.", False),
      ("C", "Because it finished in the past and has no link to now.", False)]),
    ("2. \"Right now, the agency is going through fast growth\" uses the present continuous because:",
     [("A", "It is a permanent fact that is always true.", False),
      ("B", "It describes a temporary situation happening around now.", True),
      ("C", "It is a routine she repeats every week.", False)]),
    ("3. Which sentence about a current project is correct?",
     [("A", "At the moment, her team expands the hotel portfolio.", False),
      ("B", "At the moment, her team is expanding the hotel portfolio.", True),
      ("C", "At the moment, her team is expand the hotel portfolio.", False)]),
]

TIP_TITLE = "Present Simple vs Present Continuous"
TIP_SUB = "Como falar do seu cargo (sempre) e dos seus projetos (agora) com o tempo verbal certo."
TIP_ROWS = [
    ("Present Simple<br>verb (he/she + s)", "Papel, rotina e fatos permanentes. Role, routine and permanent facts (usually, every year).", "I <strong>manage</strong> the commercial team."),
    ("Present Continuous<br>am / is / are + -ing", "Projetos temporarios acontecendo agora. Temporary projects happening now (right now, at the moment).", "We <strong>are expanding</strong> our portfolio."),
    ("Signal words", "Simple: every day, usually, always &middot; Continuous: right now, at the moment, currently, this season."),
    ("Stative verbs", "Verbos de estado (know, want, be) ficam no simple, nunca no continuous: <strong>I know</strong>, nao <em>I am knowing</em>."),
]

FILL = [
    ('"As Commercial Director, I ', "manage", "Dica: rotina/papel permanente, present simple", "As Commercial Director, I manage a team of eight people.", ' a team of eight people."'),
    ('"Right now, we ', "are expanding", "Dica: projeto temporário agora, am/is/are + -ing", "Right now, we are expanding our hotel portfolio.", ' our hotel portfolio."'),
    ('"Every year, our agency ', "works", "Dica: rotina, present simple com 'agency'", "Every year, our agency works with ten countries.", ' with ten countries."'),
    ('"At the moment, I ', "am working", "Dica: acontecendo agora, am + -ing", "At the moment, I am working on a new partnership.", ' on a new partnership."'),
    ('"I ', "know", "Dica: verbo de estado, fica no simple (não 'am knowing')", "I know many hoteliers in Europe.", ' many hoteliers in Europe."'),
    ('"This season, our team ', "is launching", "Dica: temporário nesta temporada, is + -ing", "This season, our team is launching a new program.", ' a new program."'),
]

ORDER_INTRO = "Coloque os passos de uma conversa profissional sobre o seu trabalho na ordem correta."
ORDER = [
    "Introduce yourself and your role at the agency.",
    "Explain what you usually do in a typical week.",
    "Describe a project your team is working on right now.",
    "Ask the other person about their current work.",
    "Suggest a way your two companies could work together.",
]

SPEECH = [
    ("I am the Commercial Director, and I manage our commercial team.", "Sou a Diretora Comercial e gerencio a nossa equipe comercial."),
    ("I am responsible for the European itineraries.", "Sou responsável pelos roteiros europeus."),
    ("Right now, we are expanding our hotel portfolio.", "Agora, estamos expandindo o nosso portfólio de hotéis."),
    ("At the moment, I am working on a new partnership in Italy.", "No momento, estou trabalhando em uma nova parceria na Itália."),
    ("Part of my job is to liaise with hoteliers and suppliers.", "Parte do meu trabalho é articular com hoteleiros e fornecedores."),
]

QUIZ = [
    ("A partner asks: \"What do you do at the agency?\" The best answer is:",
     [("A", "I am managing the commercial team since ten years.", False),
      ("B", "I manage the commercial team and I am responsible for the European itineraries.", True),
      ("C", "I do commercial things for the agency.", False)]),
    ("A partner asks: \"What is your team working on this season?\" You answer:",
     [("A", "Right now, we are expanding our hotel portfolio in Europe.", True),
      ("B", "Right now, we expand our hotel portfolio in Europe.", False),
      ("C", "Right now, we are expand our hotel portfolio in Europe.", False)]),
    ("You want to describe a permanent fact about the agency. Which is correct?",
     [("A", "Our agency is working with ten countries every year.", False),
      ("B", "Our agency works with ten countries every year.", True),
      ("C", "Our agency work with ten countries every year.", False)]),
    ("You want to say a stative verb correctly. Choose the natural sentence:",
     [("A", "I am knowing many hoteliers in Europe.", False),
      ("B", "I know many hoteliers in Europe.", True),
      ("C", "I am know many hoteliers in Europe.", False)]),
]

THINK = ("Imagine a new partner asks about your work. Describe your role using the present simple (what you manage, "
         "oversee, and are responsible for), and then describe two projects your team is working on right now using "
         "the present continuous. Take your time.")

SURVIVAL = [
    ("I am the Commercial Director, and I manage our commercial team.", "Sou a Diretora Comercial e gerencio a nossa equipe comercial."),
    ("I am responsible for our European itineraries.", "Sou responsável pelos nossos roteiros europeus."),
    ("Right now, we are expanding our hotel portfolio in Europe.", "Agora, estamos expandindo o nosso portfólio de hotéis na Europa."),
    ("At the moment, I am working on a new partnership.", "No momento, estou trabalhando em uma nova parceria."),
    ("Part of my job is to liaise with hoteliers and suppliers.", "Parte do meu trabalho é articular com hoteleiros e fornecedores."),
]
