#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 4 do Felipe de Araujo Dias — The Trip to Chicago (past simple).
Modelo de LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 4

IMG_TITLE = 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1494522855154-9297ac14b55f?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Boarding pass', 'the document that lets you get on the plane',
     'I printed my boarding pass at midnight.'),
    ('Baggage claim', 'the place in an airport where you collect your suitcase',
     'I waited forty minutes at baggage claim.'),
    ('Customs', 'the government desk that checks what you bring into a country',
     'I walked through customs with nothing to declare.'),
    ('To check in', 'to register at an airport desk, at a hotel or online',
     'I could not check in before three in the afternoon.'),
    ('Booking', 'an arrangement you made in advance for a room, a table or a seat',
     'I made the booking in January and asked for a quiet room.'),
    ('Aisle', 'the space you walk along between two rows of seats',
     'Ten hours is a long time, so I always ask for an aisle seat.'),
    ('Trade fair', 'a large event where companies show their products to buyers',
     'The trade fair in Chicago happens every March.'),
    ('Badge', 'the card with your name that you wear at an event',
     'Show your badge to the driver and he will let you on.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Boarding pass', 'd'], ['2', 'Baggage claim', 'g'],
                   ['3', 'Customs', 'a'], ['4', 'To check in', 'f'],
                   ['5', 'Booking', 'b'], ['6', 'Aisle', 'h'],
                   ['7', 'Trade fair', 'c'], ['8', 'Badge', 'e']],
         'defs': [['a', 'The government desk that checks what you bring into a country'],
                  ['b', 'An arrangement you made in advance for a room, a table or a seat'],
                  ['c', 'A large event where companies show their products to buyers'],
                  ['d', 'The document that lets you get on the plane'],
                  ['e', 'The card with your name that you wear at an event'],
                  ['f', 'To register at an airport desk, at a hotel or online'],
                  ['g', 'The place in an airport where you collect your suitcase'],
                  ['h', 'The space you walk along between two rows of seats']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: you make a booking weeks before, and you check in on the '
                  'day. One is the promise, the other is the moment it becomes real.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['The trip started badly. I printed my ', ['1'],
                   ' at midnight and the machine gave me a middle seat instead of the ', ['2'],
                   ' seat I asked for. In Chicago I waited forty minutes at ', ['3'],
                   ', walked through ', ['4'],
                   ' with nothing to declare, and reached the hotel at two. I could not ',
                   ['5'], ' before three, so I sat in the lobby and read the ', ['6'],
                   ' again to be sure. The next morning somebody handed me a ', ['7'],
                   ' with my name spelled wrong, and the ', ['8'],
                   ' opened twenty minutes late. It was still the best week of the year.'],
         'bank': ['boarding pass', 'aisle', 'baggage claim', 'customs', 'check in',
                  'booking', 'badge', 'trade fair']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The Trip He Could Not Avoid',
         'paras': [
             'The trade fair in Chicago happened every March, and for eleven years somebody '
             'else went. This time nobody else could. So on a Sunday night he printed his '
             'boarding pass, checked in online, and asked for an aisle seat, because ten hours '
             'is a long time next to a window. He slept badly and left for the airport at four '
             'in the morning.',
             'The flight was fine. The problem started at immigration. The officer asked three '
             'questions and he understood two of them. He said the name of his company, he said '
             'four days, and then the officer asked something about the purpose of the visit '
             'that he did not catch. He asked the officer to repeat it slowly, and the officer '
             'did. Nobody was rude. Nothing terrible happened. He collected his suitcase at '
             'baggage claim, walked through customs with nothing to declare, and took a taxi to '
             'the hotel, where he checked in with a booking he made himself in January. The '
             'next morning somebody put a badge in his hand with his name on it, and for three '
             'days he spoke English with people from nine countries. He came home tired, and he '
             'came home different.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'How to get a good seat on a long flight', False],
                     ['b', 'The trip that changed what he thought he could do', True],
                     ['c', 'Why trade fairs are better than online meetings', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['He went to the Chicago trade fair every year.', 'f',
             'The fair happened every March, but for eleven years somebody else went.'],
            ['He understood every question at immigration.', 'f',
             'He understood two of the three, and asked the officer to repeat the last one.'],
            ['He made the hotel booking himself.', 't',
             'The text says he checked in with a booking he made himself in January.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'A colleague who has never travelled for work asks what happened on '
                           'your first international trip. Tell it in six sentences, all in the '
                           'past, and finish with what you would do differently.'],
            ['Scenario 2', 'Somebody at the fair asks about your flight and your hotel. Answer '
                           'without saying it was fine. Give three facts and one problem.'],
            ['Scenario 3', 'Your manager asks what you got out of four days in Chicago. Say who '
                           'you met, what you agreed, and one thing that surprised you.'],
        ]},
        {'kind': 'rephrase', 'title': 'Say each sentence again in the past, with the time word.',
         'items': [['I check in online.', 'last night'],
                   ['He takes a taxi from the airport.', 'yesterday'],
                   ['We do not speak English at the fair.', 'last year'],
                   ['Do you collect your bag at baggage claim?', 'in Chicago']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'The immigration officer asks the purpose of your visit and how long '
                          'you are staying. Answer both, in full sentences.',
             'tips': ['Business, and the name of the event. Not just work.',
                      'Four days, and the date you fly home.']},
            {'situation': 'Somebody at the fair asks whether this is your first time in the '
                          'United States. Answer and add two sentences, in the past.',
             'tips': ['Yes or no is not an answer. Say when, and where.',
                      'Regular verbs take -ed; the useful irregular ones here are went, came, '
                      'took, spoke.']},
            {'situation': 'The hotel says they have no record of your booking. Explain what you '
                          'did and when.',
             'tips': ['Give the month and the channel: I made the booking in January, through '
                      'the fair.',
                      'Say what you asked for, so they can find the note.']},
            {'situation': 'Your suitcase did not arrive. Tell the airline what happened and what '
                          'you need.',
             'tips': ['Three past facts: the flight, the time you landed, the tag number.',
                      'Finish with what you need, not with how you feel.']},
            {'situation': 'A colleague asks what went wrong on the trip. Tell one problem and '
                          'how it ended.',
             'tips': ['After did not, the verb goes back to the base form.',
                      'End with the solution, not with the complaint.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['I checked in online last night.',
                  'He took a taxi from the airport yesterday.',
                  'We did not speak English at the fair last year.',
                  'Did you collect your bag at baggage claim in Chicago?'],
         'note': ('Only one word in the sentence carries the past. When did shows up, the verb '
                  'goes straight back to the base form.')},
    ],
}

LISTENINGS = [
    {'file': 'a4_listening1.mp3', 'voice': 'arthur',
     'text': ('Good evening, this is a boarding announcement for flight eight four two to '
              'Chicago O Hare. We are boarding at gate twelve. We board by group, and group '
              'four begins in about ten minutes. Please have your boarding pass and your '
              'passport open and ready. If your bag does not fit in the box at the gate, we '
              'check it here at no cost, and you collect it at baggage claim in Chicago. The '
              'flight time this evening is nine hours and fifty minutes. Thank you for your '
              'patience.')},
    {'file': 'a4_listening2.mp3', 'voice': 'nordic_f',
     'text': ('Hello Felipe, this is Ingrid from the fair office. I saw that you registered '
              'last week, so everything is ready. I printed your badge this morning and you '
              'collect it at the west desk, not at the main entrance, because the main queue '
              'was two hours long last year. Three practical things. The opening session '
              'started late every year, so please do not run. Lunch is included on Tuesday and '
              'Wednesday only. And we moved the supplier meetings to hall B, because hall A was '
              'too small in March. If you did not receive the new map, write to me and I will '
              'send it again. See you on Tuesday.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l4]', 'file': 'pc4_order_trip.mp3', 'voice': 'ellen',
     'text': ('First, he printed his boarding pass and checked in online on Sunday night. Then '
              'he answered three questions at immigration and asked the officer to repeat one '
              'of them. After that, he collected his suitcase at baggage claim and walked '
              'through customs. Next, he took a taxi to the hotel and checked in with a booking '
              'he made in January. Finally, he collected his badge and spent three days at the '
              'trade fair.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Este slide s&oacute; abre a tela e '
    'd&aacute; o tema. Aula de LEITURA &mdash; avise que hoje h&aacute; um texto no meio.',
    'Chapter 1: The Trip He Could Not Avoid', 'The Trip to', 'Chicago',
    'Immigration, a hotel desk and four days of English', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 3 (3 min): na aula 3 ele aprendeu a PERGUNTAR sem soar rude. '
    'Fa&ccedil;a a ponte: hoje ele vai CONTAR o que aconteceu. Pe&ccedil;a que use pelo menos '
    'duas palavras da aula 3 (shipment, quote, to confirm, to push back) ao responder. Se ele '
    'parar na primeira frase, devolva: And then what happened?',
    'You Asked the Questions.', 'Now Tell the Story',
    'Last time you got the information out of somebody else. Today the information is yours: '
    'something happened, it is finished, and somebody wants to hear it. English has one tense '
    'for that, and it is shorter than you think.',
    'Tell me about the last time you travelled for work. Start with the day you left.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Avise que ele n&atilde;o precisa entender toda palavra do '
    'texto &mdash; a primeira leitura &eacute; pela ideia geral. Passe ao pr&oacute;ximo.',
    ['Eight words that a business trip cannot happen without.',
     'Read a short text about a trip that went almost right, and find the main idea.',
     'Tell four days of your own life in the past, without stopping to translate.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words Between', 'Two Airports',
    '8 words you need between the front door and the fair', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'baggage claim: Is it before or after immigration? (Depois.) CCQ para customs: Do they check '
    'my passport or my suitcase there? (A mala.) Pron&uacute;ncia: em customs o stress cai no '
    'come&ccedil;o (CUS-toms).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para aisle: Is the aisle a seat or the '
    'space between seats? (O corredor &mdash; e o assento ao lado dele.) ATEN&Ccedil;&Atilde;O '
    '&Agrave; PRON&Uacute;NCIA: aisle soa como I-L, o S &eacute; MUDO. Fa&ccedil;a ele repetir '
    'tr&ecirc;s vezes.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note no fim como ponte para a leitura.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta &mdash; repare que o texto j&aacute; est&aacute; todo '
    'no passado, de prop&oacute;sito.',
    'Use the Words', 'One Trip, from', 'Midnight to Monday',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o leitura (1 min): diga: Read for the main idea first. Do not '
    'translate word by word, and do not stop at every new word.',
    'Chapter 3: Read the Trip', 'The Trip He Could', 'Not Avoid',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist: ele '
    'clica a alternativa e a certa fica verde. N&atilde;o pe&ccedil;a tradu&ccedil;&atilde;o. Se '
    'travar numa palavra, pergunte o que ele acha que significa pelo contexto.',
    'Read for the Main Idea', 'The Trip He Could', 'Not Avoid', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): ingl&ecirc;s americano de aeroporto, r&aacute;pido e com '
    'n&uacute;meros. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. &Eacute; exatamente '
    'o &aacute;udio que ele vai ouvir em GRU e em ORD. Toque duas vezes; 0.75x s&oacute; se ele '
    'pedir.',
    1, 'The Gate', 'Announcement',
    'The last announcement before boarding. Sound first, no text.',
    'a4_listening1.mp3', SLUG,
    [('Which gate is it, and which group boards soon?',
      'Gate twelve. Group four begins in about ten minutes.'),
     ('What happens if your bag does not fit in the box?',
      'They check it at the gate at no cost, and you collect it at baggage claim.'),
     ('How long is the flight?', 'Nine hours and fifty minutes.')]))

S.append(L.s_chapter(
    13, 4,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: You just read a whole trip in one '
    'tense. Now we look at how it is built. Ele pediu um refresh de presente, passado e futuro '
    '&mdash; esta &eacute; a segunda parte.',
    'Chapter 4: What Already Happened', 'One Tense for', 'Everything Finished',
    'The past simple, and the -ed that only appears once', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Two '
    'of these verbs just added -ed. Two changed completely. And one lost its past. Which one, '
    'and why? S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In I did not catch it, where is '
    'the past? (No did.) Pron&uacute;ncia do -ed: asked soa ASKT, printed soa PRIN-tid.',
    'past simple',
    [('"I <span class="accent" style="font-weight:700">printed</span> my boarding pass on Sunday night."',
      'I printed my boarding pass on Sunday night.'),
     ('"The officer <span class="accent" style="font-weight:700">asked</span> three questions."',
      'The officer asked three questions.'),
     ('"He <span class="accent" style="font-weight:700">took</span> a taxi to the hotel."',
      'He took a taxi to the hotel.'),
     ('"I <span class="accent" style="font-weight:700">did not catch</span> the last one."',
      'I did not catch the last one.')],
    'rule4',
    ['Form', 'Use it for', 'Example'],
    [['Regular verbs', 'Add -ed. The spelling is easy; the sound is not.',
      'ask &rarr; asked &middot; print &rarr; printed &middot; walk &rarr; walked'],
     ['Irregular verbs', 'A different word. There is no rule, only a list worth learning.',
      'take &rarr; took &middot; come &rarr; came &middot; speak &rarr; spoke &middot; '
      'catch &rarr; caught'],
     ['Negative', 'did not + the BASE form. The past is already inside did.',
      'I <strong>did not catch</strong> it. Never: I did not caught it.'],
     ['Question', 'Did + subject + BASE form. Same rule, same reason.',
      '<strong>Did you check in</strong> online?'],
     ['To be', 'was and were, with no did at all.',
      'The flight <strong>was</strong> fine. Nobody <strong>was</strong> rude.']],
    ('The past appears once per sentence. If did is there, the verb goes back to the base form '
     'and gives the past away.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica '
    'para comparar. Toggle: clicar de novo fecha. Foque o ouvido no -ed final, que ele costuma '
    'engolir.',
    'Grammar Practice', 'Finish the', 'Sentence',
    'Say the full sentence, then click to compare',
    [('I ______ (print) my boarding pass at midnight.',
      'I printed my boarding pass at midnight.'),
     ('She ______ (take) the shuttle from the hotel.',
      'She took the shuttle from the hotel.'),
     ('We ______ (not / receive) the new map.', 'We did not receive the new map.'),
     ('______ you ______ (check in) online or at the desk?',
      'Did you check in online or at the desk?')]))

S.append(L.s_mistake(
    16, 4,
    'Common mistake (3 min): os tr&ecirc;s erros de passado que aparecem em toda primeira '
    'viagem. Pe&ccedil;a que ele leia as vers&otilde;es CERTAS em voz alta, duas vezes cada.',
    [('I did not caught the question.', 'I did not catch the question.'),
     ('Did you checked in online?', 'Did you check in online?'),
     ('He was went to Chicago in March.', 'He went to Chicago in March.')],
    ('Two pasts in one sentence is one too many. After did and after was, the other verb goes '
     'back to its simplest form.')))

S.append(L.s_dialogue(
    17, 4,
    'Di&aacute;logo (6 min): recep&ccedil;&atilde;o de hotel. Clique Next Line a cada fala. Nas '
    'falas do FELIPE, pe&ccedil;a que ELE fale primeiro, com o texto tapado. Repare na fala 11: '
    'ele usa uma pergunta indireta da aula 3 &mdash; aponte isso em voz alta, &eacute; a '
    'primeira vez que ele reusa gram&aacute;tica antiga sem ajuda.',
    'The Hotel', 'Desk',
    [('felipe', 'F', 'arthur',
      'Good evening. I have a <span class="vocab-highlight">booking</span> for four nights. '
      'The name is Dias.'),
     ('diane', 'D', 'ellen',
      'Good evening, Mr Dias. Let me find it. Did you book directly with us, or through the fair?'),
     ('felipe', 'F', 'arthur',
      'Through the fair. I made the booking in January, and I asked for a quiet room.'),
     ('diane', 'D', 'ellen',
      'I can see the note. You asked for a floor away from the elevator, and we kept one for '
      'you. May I see your passport?'),
     ('felipe', 'F', 'arthur', 'Of course. Here it is.'),
     ('diane', 'D', 'ellen',
      'Thank you. Your room is on the ninth floor, and breakfast is from six thirty to ten.'),
     ('felipe', 'F', 'arthur',
      'Perfect. One question. I arrived without an adapter. Do you have one?'),
     ('diane', 'D', 'ellen',
      'We do. I will send it up. Did you fly in this afternoon?'),
     ('felipe', 'F', 'arthur',
      'This morning. Immigration took an hour, and then the taxi took another one.'),
     ('diane', 'D', 'ellen',
      'That sounds like a long day. The <span class="vocab-highlight">trade fair</span> shuttle '
      'leaves from the front door at eight.'),
     ('felipe', 'F', 'arthur',
      'Good to know. Could you tell me where the shuttle stops at the convention center?'),
     ('diane', 'D', 'ellen',
      'At the south entrance. Show your <span class="vocab-highlight">badge</span> to the '
      'driver and he will let you on.')]))

S.append(L.s_comprehension(
    18, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre a RECEPCIONISTA e sobre o hotel, '
    'n&atilde;o sobre ele. Ele responde de mem&oacute;ria ANTES de clicar.',
    'Did You Catch It?', 'About the', 'Hotel',
    [('What did the hotel do about the request he made in January?',
      'They kept a room on a floor away from the elevator.'),
     ('What time does the trade fair shuttle leave, and from where?',
      'At eight, from the front door of the hotel.'),
     ('What does the shuttle driver need to see?', 'His badge.')]))

S.append(L.s_artifact(
    19, 4,
    'Artefato (4 min): o cart&atilde;o de embarque dele. Pe&ccedil;a que ele LEIA em voz alta e '
    'depois responda as tr&ecirc;s perguntas. Na primeira, exija frase completa no passado, '
    'n&atilde;o s&oacute; o n&uacute;mero do assento.',
    'Real Document', 'The Boarding', 'Pass',
    'BOARDING PASS', 'FLIGHT 842',
    [('Passenger', 'DIAS / FELIPE DE ARAUJO'),
     ('From', 'Sao Paulo GRU'),
     ('To', 'Chicago ORD'),
     ('Date', 'March 8'),
     ('Boarding', '21:40 &middot; Gate 12'),
     ('Seat', '24C &middot; aisle'),
     ('Baggage', '1 checked &middot; tag GRU-441'),
     ('Group', '4')],
    [('Where does he sit, and did he choose it?',
      'Seat 24C, on the aisle. He asked for it when he checked in online.'),
     ('What does he have to collect at baggage claim?',
      'One checked bag, tag GRU-441.'),
     ('What time does boarding start, and at which gate?',
      'Boarding starts at 21:40, at gate 12.')]))

S.append(L.s_listening(
    20, 4,
    'Listening 2 (5 min): sotaque n&oacute;rdico, uma organizadora de feira. LEIA AS PERGUNTAS '
    'COM ELE ANTES do play. Ela fala mais devagar que o americano, mas com ritmo diferente '
    '&mdash; pergunte no fim o que soou estranho. Toque duas vezes.',
    2, 'The Message from', 'the Fair Office',
    'The organizer leaves you three practical instructions. Sound first, no text.',
    'a4_listening2.mp3', SLUG,
    [('Where does he collect his badge, and why not at the main entrance?',
      'At the west desk. The main queue was two hours long last year.'),
     ('On which days is lunch included?', 'Tuesday and Wednesday only.'),
     ('Why did they move the supplier meetings?',
      'Hall A was too small in March, so they moved them to hall B.')]))

S.append(L.s_blocks(
    21, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez. Ele responde EM VOZ ALTA antes de '
    'abrir as Tips. Exija passado em toda resposta &mdash; e conte quantas vezes ele coloca dois '
    'passados na mesma frase.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    22, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you tell the trip. Three rounds, '
    'less help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    23, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija seis frases, todas no passado. No '
    'rephrase, ele repete a frase com a palavra de tempo entre par&ecirc;nteses. Sem gabarito na '
    'tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    24, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM '
    'VOZ ALTA antes de clicar. Score no topo.',
    [('I did not received the new map.', 'I did not receive the new map.'),
     ('Did you took the shuttle or a taxi?', 'Did you take the shuttle or a taxi?'),
     ('He was checked in at three in the afternoon.',
      'He checked in at three in the afternoon.'),
     ('We speaked English for three days.', 'We spoke English for three days.')]))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; o oficial de imigra&ccedil;&atilde;o. '
    'Seja seco, n&atilde;o hostil, e fale r&aacute;pido de prop&oacute;sito. Se ele n&atilde;o '
    'entender, espere que ele pe&ccedil;a repeti&ccedil;&atilde;o &mdash; n&atilde;o repita '
    'antes.',
    'Role-Play 1 &mdash; Guided', 'The Immigration', 'Desk',
    'Situation',
    'You land in Chicago. The officer asks the purpose of your visit, how long you are staying, '
    'where you are staying, and whether you have anything to declare. Answer all four.',
    ['business', 'trade fair', 'four days', 'a hotel downtown', 'nothing to declare']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; a recepcionista e a reserva '
    'sumiu. Insista uma vez que n&atilde;o h&aacute; nada no sistema, para for&ccedil;ar ele a '
    'contar o que fez, quando e por qual canal.',
    'Role-Play 2 &mdash; Semi-Free', 'The Booking That', 'Disappeared',
    'Situation',
    'The hotel cannot find your booking. Say when you booked, through which channel, what you '
    'asked for, and what you need tonight. Stay calm and stay in the past.',
    ['in January', 'through the fair', 'a quiet room']))

S.append(L.s_roleplay(
    27, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa, nem para corrigir. Cronometre noventa segundos e anote os erros de passado para '
    'a pr&oacute;xima aula. CELEBRE no fim.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Tell the whole trip to a colleague who has never left Brazil: the night before, the flight, '
    'immigration, the hotel, the three days at the fair, and one thing that surprised you. '
    'Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    28, 6,
    'Answer key (2 min): o accordion nasce fechado. S&oacute; abra depois que ele tentou as '
    'quatro do rephrase. Clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    29,
    'Survival lines (3 min): leia cada frase, toque o &aacute;udio, pe&ccedil;a repeti&ccedil;'
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco que ele leva no bolso para '
    'Chicago.',
    'Say It with', 'Confidence',
    ['I checked in online and I asked for an aisle seat.',
     'I did not catch that. Could you repeat it, please?',
     'I have a booking for four nights, under the name Dias.',
     'I flew in this morning, and immigration took an hour.',
     'Nothing to declare, thank you.']))

S.append(L.s_checklist(
    30,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 4 e liberam o quarto stamp.',
    4,
    ['I can tell four days of my life in the past, without stopping.',
     'I use -ed for regular verbs and I know the irregular ones I need.',
     'I never put two pasts in the same sentence.',
     'I can get through immigration and a hotel desk on my own.',
     'I know the words: boarding pass, baggage claim, customs, check in, booking, aisle, '
     'trade fair, badge.']))

S.append(L.s_badge(
    31,
    'Encerramento (2 min): diga: Lesson 4 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar noventa segundos contando a &uacute;ltima viagem dele, toda no passado, e '
    'mandar no WhatsApp antes da pr&oacute;xima aula. Pr&oacute;xima aula: What Went Wrong at '
    'the DC.',
    4, 'The Trip to Chicago',
    'You crossed a border, a hotel desk and a trade fair in English today, Felipe.',
    'What Went Wrong at the DC'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'The Trip to Chicago -- Immigration, Hotel, Trade Fair',
    'short_title': 'The Trip to Chicago',
    'menu_desc': ('Reading lesson: the business trip he could not avoid, and the one tense '
                  'English uses for everything that is already finished'),
    'grammar_point': 'past simple',
    'characters': {'felipe': 'arthur', 'diane': 'ellen'},
    'phases': ['The Trip He Could Not Avoid', 'Your Words', 'Read the Trip',
               'What Already Happened', 'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80',
    'desc': ('The words a business trip runs on: boarding pass, baggage claim, customs, to '
             'check in, booking, aisle, trade fair, badge. Structure: the past simple, regular '
             'and irregular, and the -ed that disappears after did. Mission: tell four days of '
             'your own life without stopping to translate.'),
    'context_paras': [
        'Last March I <strong>flew</strong> to Chicago for the first time. I '
        '<strong>printed</strong> my boarding pass on Sunday night, I '
        '<strong>checked in</strong> online, and I <strong>asked</strong> for an aisle seat. '
        'The flight <strong>was</strong> long but quiet. At immigration the officer '
        '<strong>asked</strong> me three questions and I <strong>did not catch</strong> the '
        'last one, so I <strong>asked</strong> him to repeat it slowly.',
        'Then everything <strong>went</strong> quickly. I <strong>collected</strong> my '
        'suitcase at baggage claim, I <strong>walked</strong> through customs with nothing to '
        'declare, and I <strong>took</strong> a taxi to the hotel. The hotel '
        '<strong>did not have</strong> my booking at first, but they '
        '<strong>found</strong> it. The next morning I <strong>collected</strong> my badge and '
        'I <strong>spoke</strong> English for three days with people from nine countries. '
        'Nobody <strong>laughed</strong>. Nobody <strong>walked</strong> away.'],
    'context_quiz': [
        ('Why is it <em>I did not catch</em> and not <em>I did not caught</em>?',
         [('Because catch is irregular and irregular verbs never change.', False),
          ('Because did already carries the past, so the verb goes back to the base form.', True),
          ('Because the sentence is negative, and negatives use the present.', False)]),
        ('Which verbs in the text are irregular?',
         [('printed, checked, asked, collected, walked', False),
          ('flew, went, took, found, spoke', True),
          ('was, laughed, walked, declare', False)]),
        ('Why does the text say <em>the flight was long</em> and not <em>the flight did be '
         'long</em>?',
         [('Because to be never uses did. It has its own past: was and were.', True),
          ('Because long is an adjective and adjectives block did.', False),
          ('Because the flight is a thing, not a person.', False)]),
    ],
    'tip_title': 'The Past Simple',
    'tip_intro': ('One tense for everything that is finished. The hard part is not the -ed. It '
                  'is remembering that the past only shows up once per sentence.'),
    'tip_rows': [
        ['Regular: verb + -ed', 'Most verbs. The spelling is regular, the sound is not.',
         'I <strong>asked</strong> &middot; I <strong>printed</strong> &middot; '
         'I <strong>walked</strong>'],
        ['Irregular: a new word',
         'A short list you use every day. Learn them in pairs, not alphabetically.',
         'go &rarr; <strong>went</strong> &middot; take &rarr; <strong>took</strong> &middot; '
         'speak &rarr; <strong>spoke</strong> &middot; fly &rarr; <strong>flew</strong>'],
        ['Negative: did not + base',
         'Same for regular and irregular. The verb loses its past because did already has it.',
         'I <strong>did not catch</strong> it &middot; I <strong>did not go</strong>'],
        ['Question: did + subject + base', 'No -ed anywhere in the question.',
         '<strong>Did you check in</strong> online? &middot; <strong>Did he take</strong> '
         'the shuttle?'],
        ['To be: was / were',
         'The one verb with no did. <em>I was, you were, he was, we were, they were</em>. '
         'Negative: <em>was not</em>, <em>were not</em>.'],
        ['The sound of -ed',
         'Three sounds, never a full extra syllable unless the verb ends in t or d: '
         '<em>asked</em> = askt, <em>arrived</em> = arrivd, <em>printed</em> = PRIN-tid.'],
    ],
    'tip_note': ('A habit worth building: before you say a past sentence, decide which single '
                 'word will carry the past. If two words are fighting for it, one of them is wrong.'),
    'blanks': [
        ('Last night I ', 'printed', 'Hint: regular verb, add -ed. To make a paper copy.',
         'Last night I printed my boarding pass.', ' my boarding pass.'),
        ('I ', 'took', 'Hint: irregular. The past of take.',
         'I took a taxi from the airport to the hotel.',
         ' a taxi from the airport to the hotel.'),
        ('I ', 'did not catch',
         'Hint: three words. After did the verb goes back to the base form.',
         'I did not catch the last question.', ' the last question.'),
        ('The officer ', 'asked', 'Hint: regular verb, add -ed. It sounds like askt.',
         'The officer asked me three questions.', ' me three questions.'),
        ('I collected my suitcase at ', 'baggage claim',
         'Hint: two words. The place where the suitcases arrive.',
         'I collected my suitcase at baggage claim.', '.'),
        ('The flight ', 'was', 'Hint: three letters. To be never uses did.',
         'The flight was long but quiet.', ' long but quiet.'),
    ],
    'order_title': 'Put the Trip in Order',
    'order_intro': 'Listen first, then put the five parts of the trip in the order you hear them.',
    'order': [
        (4, 'Next, he took a taxi to the hotel and checked in with a booking he made in January.'),
        (2, 'Then he answered three questions at immigration and asked the officer to repeat one '
            'of them.'),
        (5, 'Finally, he collected his badge and spent three days at the trade fair.'),
        (1, 'First, he printed his boarding pass and checked in online on Sunday night.'),
        (3, 'After that, he collected his suitcase at baggage claim and walked through customs.'),
    ],
    'speech': [
        'I checked in online and I asked for an aisle seat.',
        'I did not catch that. Could you repeat it, please?',
        'I have a booking for four nights, under the name Dias.',
        'I flew in this morning, and immigration took an hour.',
        'Nothing to declare, thank you.',
    ],
    'quiz_intro': 'You are travelling for work. Choose the best thing to say.',
    'quiz': [
        ('The immigration officer asks how long you are staying. You say:',
         [('I stay four days for a trade fair.', False),
          ('Four days. I am here for a trade fair.', True),
          ('I did stayed four days.', False)]),
        ('A colleague asks about your flight. The most natural answer is:',
         [('The flight was long, but I slept for six hours.', True),
          ('The flight did be long, but I did slept six hours.', False),
          ('The flight is long, but I sleep six hours.', False)]),
        ('The hotel cannot find your reservation. You explain:',
         [('I did booked in January through the fair.', False),
          ('I booked in January, through the fair, and I asked for a quiet room.', True),
          ('I am booking in January through the fair.', False)]),
        ('Somebody asks whether you enjoyed the trade fair. You say:',
         [('Did you enjoy? Yes, I enjoy very much.', False),
          ('Yes. I met nine suppliers and I spoke English for three days.', True),
          ('Yes, I did enjoyed and I did met nine suppliers.', False)]),
    ],
    'think': ('Think about the last time you travelled, for work or not. Record about ninety '
              'seconds, all in the past. Start with the day before you left and what you '
              'prepared. Then say what happened at the airport, what happened when you arrived, '
              'and one thing that did not go as planned. Use at least four words from this '
              'lesson, and at least three irregular verbs. Finish with what you would do '
              'differently next time. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"The past simple tense" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on regular and irregular verbs, with the pronunciation of -ed at the end. '
         'Connection to Lesson 4: it is the same tense you used to tell the whole trip, drilled '
         'by two British speakers at a comfortable speed.',
         'Tip: pay attention to the -ed sounds. Say each example out loud before they explain '
         'it, and check whether you added a syllable that is not there.',
         'https://www.youtube.com/watch?v=PgsG98vByiw', 'Watch on YouTube'),
        ('video', 'airport', 'Video Lesson',
         'Airport vocabulary: speak English at the airport',
         'A practical walk through check-in, security, the gate and baggage claim, with the '
         'exact phrases people use. Connection to Lesson 4: half of these words were on your '
         'boarding pass today, and the other half you will need in March.',
         'Tip: watch it the night before your next flight, not the week before. It sticks better.',
         'https://www.youtube.com/watch?v=-IRIJpA7FzY', 'Watch on YouTube'),
        ('video', 'hotel', 'Video Lesson',
         'How to check in at a hotel in English',
         'A full hotel check-in from arrival to room key, including what to say when something '
         'is wrong with the booking. Connection to Lesson 4: it is the dialogue you practised, '
         'with three variations you did not see.',
         'Tip: watch once, then close your eyes and say the guest part out loud from memory. '
         'Then watch again.',
         'https://www.youtube.com/watch?v=dd7iOYx5TWc', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
