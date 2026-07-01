# -*- coding: utf-8 -*-
IMG = "https://images.unsplash.com/photo-1511578314322-379afb476865?w=600&q=80"
TITLE = "The Art of Small Talk -- Conversations at the Fair"
DESC = ("Starting and sustaining conversations at international tourism fairs. Key words: small talk, icebreaker, "
        "conversation opener, common ground, follow-up question, to wrap up, booth, exhibitor, delegate, keynote speaker, "
        "badge, panel session. Structures: question formation (present simple, present continuous) and present perfect "
        "for experience (How long have you...?).")

VOCAB = [
    ("Small talk", "light, friendly conversation about everyday topics (bate-papo, conversa leve)", "A little small talk breaks the ice at any fair."),
    ("Icebreaker", "something you say to start a conversation comfortably (quebra-gelo)", "A good icebreaker is a simple question about the event."),
    ("Conversation opener", "a first line used to begin a chat (frase de abertura)", "My favorite conversation opener is: what brings you here?"),
    ("Common ground", "a shared interest or experience two people have (interesse em comum)", "We found common ground in our love of travel."),
    ("Follow-up question", "a question that keeps the conversation going (pergunta de continuidade)", "A follow-up question shows you are really listening."),
    ("To wrap up", "to bring a conversation to a friendly close (encerrar, finalizar)", "Let us wrap up and exchange cards."),
    ("Booth", "a small stand where a company shows its products at a fair (estande)", "Come by our booth this afternoon."),
    ("Exhibitor", "a company or person showing products at a fair (expositor)", "As an exhibitor, I meet dozens of delegates a day."),
    ("Delegate", "a person who attends a conference to represent a company (delegado, participante)", "Every delegate wears a badge at the fair."),
    ("Keynote speaker", "the main speaker at a conference (palestrante principal)", "The keynote speaker takes the stage at four."),
    ("Badge", "the name card you wear at an event (crachá)", "Please wear your badge at all times."),
    ("Panel session", "a talk where several experts discuss a topic (mesa-redonda, painel)", "The panel session on sustainable travel starts soon."),
]

MATCH = [
    ("Small talk", "light, friendly conversation about everyday topics"),
    ("Icebreaker", "something you say to start a conversation comfortably"),
    ("Conversation opener", "a first line used to begin a chat"),
    ("Common ground", "a shared interest or experience two people have"),
    ("Follow-up question", "a question that keeps the conversation going"),
    ("To wrap up", "to bring a conversation to a friendly close"),
    ("Booth", "a small stand where a company shows its products at a fair"),
    ("Exhibitor", "a company or person showing products at a fair"),
    ("Delegate", "a person who attends a conference to represent a company"),
    ("Keynote speaker", "the main speaker at a conference"),
    ("Badge", "the name card you wear at an event"),
    ("Panel session", "a talk where several experts discuss a topic"),
]

CONTEXT = ("At the fair, a <strong>delegate</strong> named Daniel walks up to Andrea's <strong>booth</strong>. "
           "\"<strong>Are</strong> you enjoying the fair so far?\" he asks &mdash; a warm <strong>icebreaker</strong>. "
           "\"I <strong>am</strong>, thanks,\" Andrea says. \"It is my third time here. <strong>Is</strong> this your first ITB?\" "
           "They quickly find <strong>common ground</strong>: both love hospitality. Andrea keeps the conversation going with a good "
           "<strong>follow-up question</strong>: \"How long <strong>have</strong> you worked in hospitality?\" Daniel is an "
           "<strong>exhibitor</strong> from Lisbon. \"For about ten years,\" he says. \"I <strong>have</strong> just launched a small hotel "
           "group. <strong>Have</strong> you seen the <strong>keynote speaker</strong> yet?\" Before they <strong>wrap up</strong>, they "
           "exchange cards and agree to keep in touch.")

CONTEXT_QUIZ = [
    ("1. Why does Daniel start with \"Are you enjoying the fair?\"",
     [("A", "Because it is a friendly icebreaker to start a conversation.", True),
      ("B", "Because he wants to end the conversation quickly.", False),
      ("C", "Because he is asking about a finished event in the past.", False)]),
    ("2. \"How long have you worked in hospitality?\" uses the present perfect because:",
     [("A", "It asks about something happening only right now.", False),
      ("B", "It asks about experience and duration up to now.", True),
      ("C", "It is a routine that repeats every week.", False)]),
    ("3. Which question is formed correctly?",
     [("A", "You are enjoying the fair?", False),
      ("B", "Are you enjoying the fair?", True),
      ("C", "Enjoying you the fair?", False)]),
]

TIP_TITLE = "Question Formation & Present Perfect"
TIP_SUB = "Como montar boas perguntas para abrir e sustentar uma conversa (explicação em inglês e português)."
TIP_ROWS = [
    ("Present Simple<br>Do / Does + subject + verb", "Fatos e rotinas. Facts and routines.", "<strong>Do</strong> you come here often?"),
    ("Present Continuous<br>Am / Is / Are + subject + -ing", "Algo acontecendo agora. Something happening now.", "<strong>Are</strong> you enjoying the fair?"),
    ("Present Perfect<br>Have / Has + subject + past participle", "Experiência e duração até agora. Experience and duration up to now.", "<strong>Have</strong> you been here before?"),
    ("Question words", "What (o que) &middot; Where (onde) &middot; How long (quanto tempo) &middot; Why (por que) &middot; Who (quem)"),
]

FILL = [
    ('"', "Do", "Dica: pergunta de rotina, present simple, auxiliar 'Do'", "Do you come to this fair every year?", ' you come to this fair every year?"'),
    ('"', "Are", "Dica: pergunta sobre agora, present continuous, auxiliar 'Are'", "Are you enjoying the panels so far?", ' you enjoying the panels so far?"'),
    ('"How long ', "have", "Dica: experiência até agora, present perfect, auxiliar 'have'", "How long have you worked in hospitality?", ' you worked in hospitality?"'),
    ('"I ', "have", "Dica: acabou de acontecer, present perfect com 'just'", "I have just arrived from Brazil.", ' just arrived from Brazil."'),
    ('"What ', "brings", "Dica: present simple, terceira pessoa 'What brings...'", "What brings you to the fair this year?", ' you to the fair this year?"'),
    ('"', "Have", "Dica: pergunta de experiência, present perfect, auxiliar 'Have'", "Have you been to the keynote yet?", ' you been to the keynote yet?"'),
]

ORDER_INTRO = "Coloque os passos de uma conversa de small talk na feira na ordem correta."
ORDER = [
    "Break the ice with a friendly opener.",
    "Introduce yourself and say what you do.",
    "Ask a follow-up question to learn more.",
    "Find some common ground.",
    "Wrap up and exchange cards.",
]

SPEECH = [
    ("Hi there! Are you enjoying the fair so far?", "Oi! Você está gostando da feira até agora?"),
    ("So, what brings you to the fair this year?", "Então, o que te traz à feira este ano?"),
    ("How long have you worked in hospitality?", "Há quanto tempo você trabalha com hotelaria?"),
    ("It sounds like we have a lot in common.", "Parece que temos muito em comum."),
    ("It was great to chat. Let us keep in touch.", "Foi ótimo conversar. Vamos manter contato."),
]

QUIZ = [
    ("A delegate stops by your booth. The best icebreaker is:",
     [("A", "You are enjoying the fair?", False),
      ("B", "Hi there! Are you enjoying the fair so far?", True),
      ("C", "Why you are here?", False)]),
    ("You want to ask about someone's experience. Which is correct?",
     [("A", "How long you work in hospitality?", False),
      ("B", "How long have you worked in hospitality?", True),
      ("C", "How long do you working in hospitality?", False)]),
    ("You want to keep the conversation going. The best follow-up question is:",
     [("A", "Okay, bye now.", False),
      ("B", "That is interesting! What brings you to the fair this year?", True),
      ("C", "I do not have more questions.", False)]),
    ("You want to end the chat warmly. You say:",
     [("A", "It was great to chat. Let us keep in touch.", True),
      ("B", "We finish now, goodbye.", False),
      ("C", "You are boring, I go.", False)]),
]

THINK = ("Imagine you are at an international tourism fair and a stranger walks up to your booth. Start a conversation: "
         "break the ice, introduce yourself, ask two follow-up questions, and find some common ground. Use at least three "
         "questions with Do, Are, or Have. Take your time.")

SURVIVAL = [
    ("Hi there! Are you enjoying the fair so far?", "Oi! Você está gostando da feira até agora?"),
    ("So, what brings you to the fair this year?", "Então, o que te traz à feira este ano?"),
    ("How long have you worked in hospitality?", "Há quanto tempo você trabalha com hotelaria?"),
    ("It sounds like we have a lot in common.", "Parece que temos muito em comum."),
    ("It was great to chat. Let us keep in touch.", "Foi ótimo conversar. Vamos manter contato."),
]
