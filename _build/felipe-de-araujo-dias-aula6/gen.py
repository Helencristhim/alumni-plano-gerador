#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 6 do Felipe de Araujo Dias — Have You Ever...? (present perfect, experiencia).
Modelo de LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 6

IMG_TITLE = 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Keynote', 'the main talk of an event, given to everybody at the same time',
     'The keynote was better than last year.'),
    ('Booth', 'the small stand a company builds at a fair to receive visitors',
     'I have never seen a booth that big.'),
    ('Attendee', 'a person who is taking part in an event',
     'Three hundred attendees stood in the room with a coffee.'),
    ('To network', 'to meet people at an event in order to build useful contacts',
     'She comes to network, not to look at the booths.'),
    ('Small talk', 'light conversation about nothing important, used to open a door',
     'Small talk is not the conversation. It is the way in.'),
    ('Business card', 'the small card with your name, your role and how to reach you',
     'Here is my business card. Write to me next week.'),
    ('Icebreaker', 'something you say or do to start a conversation with a stranger',
     'The coffee upstairs is a terrible icebreaker, and it works every time.'),
    ('To catch up', 'to talk with somebody you have not seen for a long time, to hear their news',
     'We caught up for ten minutes before the keynote.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Keynote', 'f'], ['2', 'Booth', 'b'], ['3', 'Attendee', 'g'],
                   ['4', 'To network', 'a'], ['5', 'Small talk', 'h'],
                   ['6', 'Business card', 'c'], ['7', 'Icebreaker', 'd'],
                   ['8', 'To catch up', 'e']],
         'defs': [['a', 'To meet people at an event in order to build useful contacts'],
                  ['b', 'The small stand a company builds at a fair to receive visitors'],
                  ['c', 'The small card with your name, your role and how to reach you'],
                  ['d', 'Something you say or do to start a conversation with a stranger'],
                  ['e', 'To talk with somebody you have not seen for a long time'],
                  ['f', 'The main talk of an event, given to everybody at the same time'],
                  ['g', 'A person who is taking part in an event'],
                  ['h', 'Light conversation about nothing important, used to open a door']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: small talk is the conversation, an icebreaker is the first '
                  'sentence of it. You need the second one for about eight seconds, and then '
                  'you can forget it.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['The room was full of ', ['1'], ' with a coffee in one hand. I have never '
                   'been good at ', ['2'], ', so I stood next to the biggest ', ['3'],
                   ' and waited. A woman asked me whether I had seen the ', ['4'],
                   ' that morning, which is the oldest ', ['5'],
                   ' in the world, and it worked. Twenty minutes later we were still talking. '
                   'She gave me her ', ['6'], ' and I promised to ', ['7'],
                   ' with her in Lyon. I did not go there to ', ['8'],
                   '. I went there for the machines, and I came home with three people.'],
         'bank': ['attendees', 'small talk', 'booth', 'keynote', 'icebreaker',
                  'business card', 'catch up', 'network']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The Longest Twenty Minutes of the Fair',
         'paras': [
             'Every trade fair has a moment that nobody puts in the program. It is not the '
             'keynote and it is not the booth. It is the twenty minutes before lunch, when '
             'three hundred attendees stand in one room with a coffee in one hand and nothing '
             'to do with the other. Some people love that room. Most people look at their '
             'phone and wait for it to end.',
             'The people who love it are not more extroverted than everybody else. They have '
             'simply discovered that the whole thing runs on four questions. Have you been here '
             'before? Have you seen the keynote? Have you tried the coffee upstairs? Have you '
             'met anybody from Brazil? None of these questions is interesting, and that is '
             'exactly the point: they are doors, not conversations. The other person has to say '
             'something, and the second thing they say is where the real conversation starts. '
             'Nobody has ever built a supplier relationship by being clever in the first '
             'sentence. They have built it by asking a boring question and then listening to '
             'the answer.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why trade fairs should have shorter coffee breaks', False],
                     ['b', 'Networking runs on simple questions, not on clever ones', True],
                     ['c', 'How to prepare a keynote for an international audience', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['The people who enjoy networking are more extroverted than the others.', 'f',
             'The text says they are not more extroverted. They have discovered that it runs '
             'on four simple questions.'],
            ['The four questions in the text are interesting in themselves.', 'f',
             'The text says none of them is interesting, and that is the point: they are doors, '
             'not conversations.'],
            ['The real conversation usually starts after the first answer.', 't',
             'The text says the second thing the other person says is where the real '
             'conversation starts.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'You are standing alone in a room of three hundred people. Open a '
                           'conversation with the person next to you, keep it alive for four '
                           'exchanges, and get to what they do.'],
            ['Scenario 2', 'Somebody asks whether you have ever worked with a supplier in '
                           'Europe. Answer, and turn it into two questions back.'],
            ['Scenario 3', 'You met somebody at the fair last year and you see them again. '
                           'Catch up, and find one thing that has changed for them since then.'],
        ]},
        {'kind': 'rephrase', 'title': 'Turn each sentence into a question with ever.',
         'items': [['I have worked with a French supplier.', 'you'],
                   ['She has been to a trade fair in the United States.', 'she'],
                   ['They have used a speed meeting to find a partner.', 'they'],
                   ['He has given a keynote in English.', 'he']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'You are holding a coffee. The person beside you is holding a coffee. '
                          'Neither of you has spoken. Say the first sentence.',
             'tips': ['Boring is fine. Have you been here before? works every time.',
                      'A question is a door. A statement about yourself is a wall.']},
            {'situation': 'They answer in three words and look away. Keep it alive.',
             'tips': ['Ask about the event, not about them: Have you seen the keynote?',
                      'Then give them one fact about you, so they can ask something back.']},
            {'situation': 'They ask whether you have ever been to the United States. Answer in '
                          'more than one sentence.',
             'tips': ['Yes plus when and where. Or no plus what you would like to see.',
                      'The tense changes when you add a date: I went there in March.']},
            {'situation': 'You want their business card without sounding like you are selling '
                          'something.',
             'tips': ['Offer yours first, and say what you would write about.',
                      'Give a reason and a time: I will write to you next week about the guards.']},
            {'situation': 'You see somebody you met at last year fair and you cannot remember '
                          'their name.',
             'tips': ['Catch up without using the name: It has been a year. How has it been?',
                      'Their card will come out on its own if you ask what they are working on.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['Have you ever worked with a French supplier?',
                  'Has she ever been to a trade fair in the United States?',
                  'Have they ever used a speed meeting to find a partner?',
                  'Has he ever given a keynote in English?'],
         'note': ('ever sits between the subject and the participle, and it only appears in '
                  'questions. In the answer it disappears.')},
    ],
}

LISTENINGS = [
    {'file': 'a6_listening1.mp3', 'voice': 'arthur',
     'text': ('Good morning, everybody, and welcome to the second day. Before the keynote, one '
              'word about the networking session at half past twelve. It happens in hall B, not '
              'in the main room, and it lasts forty minutes. If you have never done a speed '
              'meeting before, the rule is simple. You have five minutes with each person, and '
              'when the bell rings you move one seat to the left. Bring business cards. We have '
              'printed extra ones at the west desk for anybody who has run out. And if you have '
              'not booked a seat, come anyway. Six people cancelled this morning.')},
    {'file': 'a6_listening2.mp3', 'voice': 'french_f',
     'text': ('Felipe, it is Claire. I have just left hall B and I have good news. I have spoken '
              'to my friend Sophie and she has agreed to meet you at four, at her booth. She has '
              'worked with two retailers in Sao Paulo, so she has heard of your company. Two '
              'things you should know. She has never been to Brazil, so she will ask you a '
              'hundred questions. And she does not enjoy English on the phone, but she is fine '
              'in person. I have sent you her card by email. Have a good afternoon, and come and '
              'find me afterwards.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l6]', 'file': 'pc6_order_break.mp3', 'voice': 'ellen',
     'text': ('First, Claire asks whether the seat is free and sits down. Then she says her name '
              'and asks Felipe whether he has been to the fair before. After that, they talk '
              'about the keynote and about the first two suppliers he has met. Next, she tells '
              'him that she has worked with two Brazilian retailers. Finally, she gives him her '
              'card and offers to introduce him to a friend in hall B.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Aula de LEITURA. O tema &eacute; o '
    'que ele mais evita: os vinte minutos de caf&eacute; num congresso. Diga isso em voz alta '
    'e siga.',
    'Chapter 1: The Room Before Lunch', 'Have You', 'Ever...?',
    'Twenty minutes, three hundred strangers and four questions', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 5 (3 min): na aula 5 ele contou um incidente com hora e data. '
    'Fa&ccedil;a a ponte: hoje o assunto &eacute; experi&ecirc;ncia SEM data. Pe&ccedil;a que ele '
    'responda ao prompt e ESCUTE se ele coloca uma data na frase &mdash; se colocar, n&atilde;o '
    'corrija ainda, s&oacute; anote. O slide 14 resolve isso.',
    'You Can Tell What', 'Happened. And What You Have Done?',
    'Last time every sentence had a clock on it: at ten past two, for four hours. Now imagine '
    'somebody at a coffee break asks about your life instead of your night. There is no date in '
    'the answer, and English changes tense for exactly that.',
    'Name three things you have done in your career that you are proud of. No dates.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Avise que o texto do meio &eacute; curto e que ele '
    'n&atilde;o precisa entender toda palavra. Passe ao pr&oacute;ximo.',
    ['Eight words for the part of an event that is not on the program.',
     'Read a short text about the twenty minutes everybody dreads, and find the main idea.',
     'Open a conversation with a stranger and keep it alive for four exchanges.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of the', 'Coffee Break',
    '8 words for the part nobody puts in the program', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'keynote: Is a keynote one of many talks, or the main one? (A principal.) CCQ para attendee: '
    'Is the speaker an attendee? (Sim, todo mundo que participa &eacute;.) Pron&uacute;ncia: '
    'attendee tem o stress no FIM (atten-DEE).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para small talk: Is small talk about '
    'small things or about unimportant things? (Sobre coisas sem import&acirc;ncia, e serve para '
    'abrir a porta.) CCQ para to catch up: Do I catch up with a stranger? (N&atilde;o &mdash; '
    'com quem eu j&aacute; conhe&ccedil;o.)',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Repare que o par&aacute;grafo j&aacute; mistura '
    'present perfect e past simple &mdash; n&atilde;o explique agora.',
    'Use the Words', 'Twenty Minutes,', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o leitura (1 min): diga: Read for the main idea first. Do not '
    'translate word by word, and do not stop at every new word.',
    'Chapter 3: Read the Room', 'The Longest Twenty', 'Minutes',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist: ele '
    'clica a alternativa e a certa fica verde. N&atilde;o pe&ccedil;a tradu&ccedil;&atilde;o. '
    'Pergunte no fim se ele concorda com o texto &mdash; a opini&atilde;o dele vale a '
    'discuss&atilde;o.',
    'Read for the Main Idea', 'The Longest Twenty', 'Minutes of the Fair', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): o mestre de cerim&ocirc;nias do evento, americano, r&aacute;pido. LEIA '
    'AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. O &aacute;udio est&aacute; cheio de '
    'present perfect (have you never done, we have printed, who has run out) de prop&oacute;sito '
    '&mdash; n&atilde;o explique ainda. Toque duas vezes.',
    1, 'The Announcement Before', 'the Keynote',
    'The event host explains how the networking session works. Sound first, no text.',
    'a6_listening1.mp3', SLUG,
    [('Where is the networking session, and how long does it last?',
      'In hall B, not the main room, and it lasts forty minutes.'),
     ('What is the rule of the speed meeting?',
      'Five minutes with each person, and you move one seat to the left when the bell rings.'),
     ('What should you do if you have not booked a seat?',
      'Come anyway. Six people cancelled this morning.')]))

S.append(L.s_chapter(
    13, 4,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: You already used this tense twice '
    'today without noticing. Now we look at it. Passe ao pr&oacute;ximo.',
    'Chapter 4: A Life With No Dates', 'Have You Ever', 'Done It?',
    'The present perfect, and what happens the moment you say when', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Three '
    'of these sentences have no date at all. One does. What happened to the verb in that one? '
    'S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In I have been to Chicago, am I in Chicago '
    'now? (N&atilde;o &mdash; fui e voltei.) Este &eacute; o ponto que o brasileiro erra a vida '
    'inteira.',
    'present perfect for experience',
    [('"<span class="accent" style="font-weight:700">Have you ever been</span> to Chicago?"',
      'Have you ever been to Chicago?'),
     ('"I <span class="accent" style="font-weight:700">have never seen</span> a booth that big."',
      'I have never seen a booth that big.'),
     ('"She <span class="accent" style="font-weight:700">has met</span> three suppliers this morning."',
      'She has met three suppliers this morning.'),
     ('"I <span class="accent" style="font-weight:700">went</span> to the keynote at nine."',
      'I went to the keynote at nine.')],
    'rule6',
    ['Form', 'Use it for', 'Example'],
    [['have / has + past participle',
      'An experience in your life, with no date attached to it.',
      'I <strong>have been</strong> to Chicago.'],
     ['ever', 'Only in questions. It means at any time in your life.',
      '<strong>Have you ever</strong> worked with a French supplier?'],
     ['never', 'Not once. The sentence is already negative, so no <em>not</em>.',
      'I <strong>have never seen</strong> a booth that big.'],
     ['been or gone',
      '<em>been</em> = went and came back. <em>gone</em> = went and is still there.',
      'He <strong>has been</strong> to the fair. / He <strong>has gone</strong> to the fair.'],
     ['The moment you say when', 'yesterday, last year, at nine, in 2019 force the past simple.',
      'I <strong>went</strong> to the keynote at nine.']],
    ('The present perfect has no date. Add one and the sentence changes tense, every time, with '
     'no exceptions.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. '
    'Toggle: clicar de novo fecha. No item 4, pergunte POR QUE a data muda o tempo verbal '
    '&mdash; se ele explicar, aprendeu.',
    'Grammar Practice', 'With or Without', 'a Date',
    'Say the full sentence, then click to compare',
    [('______ you ever ______ (be) to a trade fair in Europe?',
      'Have you ever been to a trade fair in Europe?'),
     ('I ______ (never / meet) a supplier from Vietnam.',
      'I have never met a supplier from Vietnam.'),
     ('She ______ (give) me her business card this morning.',
      'She has given me her business card this morning.'),
     ('I ______ (see) the keynote yesterday, not today.',
      'I saw the keynote yesterday, not today.')]))

S.append(L.s_mistake(
    16, 4,
    'Common mistake (3 min): os tr&ecirc;s erros cl&aacute;ssicos do present perfect em '
    'brasileiro. O terceiro (data + present perfect) &eacute; o mais caro, porque soa errado '
    'para o ouvido nativo mesmo quando tudo o resto est&aacute; certo.',
    [('Have you ever went to Chicago?', 'Have you ever been to Chicago?'),
     ('I did never meet him.', 'I have never met him.'),
     ('I have seen the keynote yesterday.', 'I saw the keynote yesterday.')],
    ('After have or has the verb goes into the participle, never into the past. And the second '
     'a date appears, the whole sentence goes back to the past simple.')))

S.append(L.s_dialogue(
    17, 4,
    'Di&aacute;logo (6 min): o intervalo do caf&eacute;. Clique Next Line a cada fala. Nas falas '
    'do FELIPE, pe&ccedil;a que ELE fale primeiro, com o texto tapado. Claire tem sotaque '
    'franc&ecirc;s de prop&oacute;sito. Aponte que TODA a conversa nasce de uma pergunta chata '
    '&mdash; &eacute; a tese do texto.',
    'The Coffee', 'Break',
    [('claire', 'C', 'french_f',
      'Excuse me, is this seat free? Everything on that side is full.'),
     ('felipe', 'F', 'arthur',
      'Please. I have been standing for an hour, so I understand.'),
     ('claire', 'C', 'french_f',
      'Thank you. I am Claire, from Lyon. Have you been to this fair before?'),
     ('felipe', 'F', 'arthur', 'Never. It is my first time. And you?'),
     ('claire', 'C', 'french_f',
      'Three times. The first year I hated it. Now I come for the people, not for the '
      '<span class="vocab-highlight">booths</span>.'),
     ('felipe', 'F', 'arthur',
      'That is interesting. Have you seen the <span class="vocab-highlight">keynote</span> this morning?'),
     ('claire', 'C', 'french_f',
      'I have. It was better than last year. Have you met anybody from the logistics hall yet?'),
     ('felipe', 'F', 'arthur',
      'Not yet. I have only talked to two suppliers, and both of them were Brazilian.'),
     ('claire', 'C', 'french_f',
      'So you have travelled nine thousand kilometres to speak Portuguese.'),
     ('felipe', 'F', 'arthur',
      'I have, yes. That is exactly what I did yesterday, and I am not proud of it.'),
     ('claire', 'C', 'french_f',
      'Here is my <span class="vocab-highlight">business card</span>. I have worked with two '
      'Brazilian retailers, and I can introduce you to a friend in hall B.'),
     ('felipe', 'F', 'arthur',
      'Thank you. Could you tell me where her booth is? I will go before lunch.')]))

S.append(L.s_comprehension(
    18, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre a CLAIRE, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar. Se errar, volte ao di&aacute;logo e toque a fala.',
    'Did You Catch It?', 'About', 'Claire',
    [('How many times has Claire been to this fair, and why does she come now?',
      'Three times. She comes for the people, not for the booths.'),
     ('What does she say about the keynote?',
      'She has seen it, and it was better than last year.'),
     ('What does she offer him at the end?',
      'Her business card and an introduction to a friend in hall B.')]))

S.append(L.s_artifact(
    19, 4,
    'Artefato (4 min): o cracha dele no congresso. Pe&ccedil;a que ele LEIA em voz alta e depois '
    'responda. Na terceira pergunta exija a pergunta com ever, completa &mdash; &eacute; a '
    'produ&ccedil;&atilde;o, n&atilde;o a compreens&atilde;o.',
    'Real Document', 'The Conference', 'Badge',
    'GLOBAL RETAIL SUPPLY FORUM', 'CHICAGO 2026',
    [('Name', 'FELIPE DE ARA&Uacute;JO DIAS'),
     ('Company', 'Riachuelo &mdash; Brazil'),
     ('Role', 'Supply Chain Director'),
     ('Pass', 'Full access &middot; 3 days'),
     ('Halls', 'A, B and the logistics hall'),
     ('Booked', 'Keynote 09:00 &middot; Speed meeting 14:30'),
     ('Badge number', 'GRSF-1184'),
     ('Wi-fi', 'GUEST-GRSF26')],
    [('Which two sessions has he already booked?',
      'The keynote at nine and the speed meeting at half past two.'),
     ('What does the pass let him do?',
      'Full access to halls A, B and the logistics hall, for three days.'),
     ('Ask the person next to you about their pass, using ever.',
      'Have you ever bought a full access pass, or do you only come for one day?')]))

S.append(L.s_listening(
    20, 4,
    'Listening 2 (5 min): sotaque franc&ecirc;s, a mesma Claire do di&aacute;logo. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Cinco frases seguidas em present perfect &mdash; '
    'pergunte no fim quantas ele contou. Toque duas vezes.',
    2, 'Claire Has', 'Good News',
    'A voice message left after the coffee break. Sound first, no text.',
    'a6_listening2.mp3', SLUG,
    [('What has Claire arranged, and for when?',
      'A meeting with her friend Sophie at four, at Sophie booth.'),
     ('Why does she say Sophie will ask a hundred questions?',
      'Because Sophie has never been to Brazil.'),
     ('What has Claire already sent, and how?',
      'Sophie business card, by email.')]))

S.append(L.s_blocks(
    21, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez, todas dentro do MESMO intervalo de '
    'caf&eacute;. Ele responde EM VOZ ALTA antes de abrir as Tips. Na primeira, exija que ele '
    'diga a frase de verdade, n&atilde;o que descreva o que diria.',
    'Chapter 5: Real Talk', 'Open the', 'Conversation', ['quickfire'],
    'Read each situation. Say the real sentence out loud first, then tap Tips.'))

S.append(L.s_chapter(
    22, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you work the room. Three rounds, '
    'less help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    23, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija quatro trocas, n&atilde;o uma '
    'resposta. No rephrase ele transforma a afirma&ccedil;&atilde;o em pergunta com ever. Sem '
    'gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    24, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('Have you ever went to a fair in Europe?', 'Have you ever been to a fair in Europe?'),
     ('I have met her last year at the same booth.',
      'I met her last year at the same booth.'),
     ('She has never not given me her card.', 'She has never given me her card.'),
     ('I am here since Monday.', 'I have been here since Monday.')]))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; a pessoa ao lado, educada mas '
    'curta. Responda em tr&ecirc;s palavras nas duas primeiras vezes, para for&ccedil;&aacute;-lo '
    'a fazer a segunda e a terceira pergunta.',
    'Role-Play 1 &mdash; Guided', 'The First', 'Sentence',
    'Situation',
    'You are standing with a coffee next to somebody you have never met. Open the conversation, '
    'ask two questions with ever, and give them one fact about you so they can ask back.',
    ['Have you ever', 'first time', 'the keynote', 'and you?', 'small talk']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; a Sophie, do booth em hall B, e '
    'nunca foi ao Brasil. Fa&ccedil;a tr&ecirc;s perguntas seguidas sobre o pa&iacute;s antes de '
    'falar de neg&oacute;cio &mdash; &eacute; o que uma pessoa real faria.',
    'Role-Play 2 &mdash; Semi-Free', 'The Introduction in', 'Hall B',
    'Situation',
    'Claire introduced you to Sophie. Say who sent you, explain what your company does, ask what '
    'she has done with the two Brazilian retailers, and agree on one next step.',
    ['Claire sent me', 'Have you ever', 'next step']))

S.append(L.s_roleplay(
    27, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa. Cronometre noventa segundos, conte quantas perguntas ele fez, e diga o '
    'n&uacute;mero no fim &mdash; &eacute; a m&eacute;trica que importa aqui, n&atilde;o o erro. '
    'CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Work the room. Open a conversation with a stranger, find out three things about them, tell '
    'them two things about you, and leave with a reason to write to them next week. Ninety '
    'seconds, no notes.',
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
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco frases que abrem qualquer '
    'conversa de congresso.',
    'Say It with', 'Confidence',
    ['Have you been to this fair before?',
     'I have never done a speed meeting. How does it work?',
     'I have only met two people today, and both of them were Brazilian.',
     'Here is my card. I will write to you next week.',
     'It has been a year. How has it been for you?']))

S.append(L.s_checklist(
    30,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 6.',
    6,
    ['I can open a conversation with a stranger and keep it alive.',
     'I use have and has plus the participle for experience, with no date.',
     'I put ever only in questions, and never with not.',
     'I change to the past simple the moment I say when it happened.',
     'I know the words: keynote, booth, attendee, to network, small talk, business card, '
     'icebreaker, to catch up.']))

S.append(L.s_badge(
    31,
    'Encerramento (2 min): diga: Lesson 6 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar cinco perguntas com ever que ele faria a um estrangeiro no pr&oacute;ximo '
    'evento, e mandar no WhatsApp. Pr&oacute;xima aula: Since I Joined the Company.',
    6, 'Have You Ever...?',
    'You opened a room of three hundred strangers with a boring question today, Felipe. That is '
    'the trick.',
    'Since I Joined the Company'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Have You Ever...? -- Networking at a Conference',
    'short_title': 'Have You Ever...?',
    'menu_desc': ('Reading lesson: the twenty minutes before lunch that nobody puts in the '
                  'program, and the tense that has no date in it'),
    'grammar_point': 'present perfect for experience',
    'characters': {'felipe': 'arthur', 'claire': 'french_f'},
    'phases': ['The Room Before Lunch', 'Your Words', 'Read the Room', 'A Life With No Dates',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&q=80',
    'desc': ('The words of the part nobody puts in the program: keynote, booth, attendee, to '
             'network, small talk, business card, icebreaker, to catch up. Structure: the '
             'present perfect for experience, with ever and never, and what happens the moment '
             'you say a date. Mission: open a conversation with a stranger and keep it alive.'),
    'context_paras': [
        'I <strong>have been</strong> to four trade fairs and I <strong>have never</strong> '
        'enjoyed the coffee break. This year somebody sat next to me and asked whether I '
        '<strong>had</strong> a spare seat, and twenty minutes later I <strong>had</strong> '
        'three new contacts. She <strong>has come</strong> to this fair three times. She '
        '<strong>has worked</strong> with two Brazilian retailers. She <strong>has never '
        'been</strong> to Sao Paulo, and she wants to go.',
        'Notice what none of those sentences has: a date. <em>I have been to four trade fairs</em> '
        'is my life, not my calendar. The moment I put a time in, everything changes: I '
        '<strong>went</strong> to my first fair in 2019, and I <strong>saw</strong> the keynote '
        'yesterday at nine. Both of those are finished moments with a place on the clock, so '
        'they take the past simple. If you can answer the question <em>when?</em>, you cannot '
        'use <em>have</em>.'],
    'context_quiz': [
        ('Why does the text say <em>I have been to four trade fairs</em> and not <em>I went to '
         'four trade fairs</em>?',
         [('Because four is a plural number and plurals take have.', False),
          ('Because it is an experience in his life with no date attached to it.', True),
          ('Because trade fairs happen every year.', False)]),
        ('Why is it <em>I saw the keynote yesterday</em> and not <em>I have seen</em>?',
         [('Because yesterday is a finished time, and a date forces the past simple.', True),
          ('Because see is an irregular verb and irregular verbs avoid have.', False),
          ('Because the keynote is over and the fair is not.', False)]),
        ('What is the test the text gives you?',
         [('Count the words before the verb.', False),
          ('Ask yourself whether you can answer the question when. If you can, use the past '
           'simple.', True),
          ('Check whether the sentence is positive or negative.', False)]),
    ],
    'tip_title': 'Present Perfect for Experience',
    'tip_intro': ('One tense for your life and one for your calendar. The hard part is not the '
                  'form. It is noticing the second a date walks into the sentence.'),
    'tip_rows': [
        ['have / has + participle', 'An experience, with no date. Your life, not your calendar.',
         'I <strong>have been</strong> to Chicago. She <strong>has met</strong> him.'],
        ['ever', 'Questions only. It means at any time in your life.',
         '<strong>Have you ever</strong> worked with a French supplier?'],
        ['never', 'Not once. Already negative, so never add <em>not</em>.',
         'I <strong>have never seen</strong> a booth that big.'],
        ['been or gone',
         '<em>been</em> = went and came back. <em>gone</em> = went and is still there. Brazilians '
         'almost always want <em>been</em>.'],
        ['The participle',
         'Not the past. go &rarr; <strong>gone</strong>, see &rarr; <strong>seen</strong>, '
         'meet &rarr; <strong>met</strong>, speak &rarr; <strong>spoken</strong>, '
         'be &rarr; <strong>been</strong>.'],
        ['The date test',
         'If you can answer <em>when?</em>, use the past simple: <em>I saw it yesterday</em>. If '
         'you cannot, use the present perfect: <em>I have seen it</em>.'],
    ],
    'tip_note': ('Portuguese lets you say eu fui and eu tenho ido almost anywhere. English does '
                 'not. Before you speak, ask yourself whether there is a date in the sentence, '
                 'even a hidden one.'),
    'blanks': [
        ('', 'Have', 'Hint: four letters. The question starts with the auxiliary.',
         'Have you ever been to a trade fair in Europe?',
         ' you ever been to a trade fair in Europe?'),
        ('I have never ', 'met', 'Hint: the participle of meet. It is not meeted.',
         'I have never met a supplier from Vietnam.', ' a supplier from Vietnam.'),
        ('She has ', 'worked', 'Hint: regular verb. The participle is the same as the past.',
         'She has worked with two Brazilian retailers.', ' with two Brazilian retailers.'),
        ('I ', 'saw', 'Hint: yesterday is a date, so this is the past simple of see.',
         'I saw the keynote yesterday, not today.', ' the keynote yesterday, not today.'),
        ('He has ', 'been', 'Hint: he went and came back, so it is not gone.',
         'He has been to the fair three times.', ' to the fair three times.'),
        ('Here is my ', 'business card', 'Hint: two words. It has your name and how to reach you.',
         'Here is my business card. Write to me next week.', '. Write to me next week.'),
    ],
    'order_title': 'Put the Coffee Break in Order',
    'order_intro': 'Listen first, then put the five parts of the conversation in the order you '
                   'hear them.',
    'order': [
        (3, 'After that, they talk about the keynote and about the first two suppliers he has met.'),
        (5, 'Finally, she gives him her card and offers to introduce him to a friend in hall B.'),
        (1, 'First, Claire asks whether the seat is free and sits down.'),
        (4, 'Next, she tells him that she has worked with two Brazilian retailers.'),
        (2, 'Then she says her name and asks Felipe whether he has been to the fair before.'),
    ],
    'speech': [
        'Have you been to this fair before?',
        'I have never done a speed meeting. How does it work?',
        'I have only met two people today, and both of them were Brazilian.',
        'Here is my card. I will write to you next week.',
        'It has been a year. How has it been for you?',
    ],
    'quiz_intro': 'You are at a conference coffee break. Choose the best thing to say.',
    'quiz': [
        ('You want to know whether the person beside you has visited your country. You ask:',
         [('Have you ever went to Brazil?', False),
          ('Have you ever been to Brazil?', True),
          ('Did you ever have been to Brazil?', False)]),
        ('Somebody asks whether you have used a speed meeting before. You have not. You say:',
         [('No, I have never done one. How does it work?', True),
          ('No, I did never do one.', False),
          ('No, I have not never done one.', False)]),
        ('They ask when you saw the keynote. You say:',
         [('I have seen it this morning at nine.', False),
          ('I saw it this morning at nine.', True),
          ('I have seen it yesterday at nine.', False)]),
        ('You want to know what has changed for somebody since last year. You ask:',
         [('What has changed for you since last year?', True),
          ('What did change for you since last year?', False),
          ('What is changing for you since last year?', False)]),
    ],
    'think': ('Imagine you are at the coffee break of an international event and nobody knows '
              'you. Record about ninety seconds. Open with one boring question. Then tell three '
              'experiences from your career using have or has and no dates at all. Then tell one '
              'thing that happened at a specific moment, with the date, and notice how the verb '
              'changes. Use at least four words from this lesson and finish by asking two '
              'questions with ever. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"Present perfect and past simple" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on the exact border you crossed today: when the sentence has a date and '
         'when it does not. Connection to Lesson 6: it drills the one decision that makes a '
         'Brazilian sound fluent or not in the first minute of small talk.',
         'Tip: every time they give an example, say out loud whether there is a date in it '
         'before they explain why.',
         'https://www.youtube.com/watch?v=jwmKjgwlMk8', 'Watch on YouTube'),
        ('video', 'conference', 'Video Lesson',
         'How to start a conversation at a conference -- Derek Callan, Business English',
         'The first sentence, the second sentence, and how to leave a conversation without '
         'being rude. Connection to Lesson 6: these are the doors the reading text talks about, '
         'with the words to open them.',
         'Tip: choose two openers you would actually say out loud. Ignore the ones that feel '
         'like a script.',
         'https://www.youtube.com/watch?v=PVHD6OZC-l0', 'Watch on YouTube'),
        ('video', 'networking', 'Video Lesson',
         'Master networking at your first business event',
         'A longer, slower walk through a whole networking event, from arriving alone to '
         'exchanging cards. Connection to Lesson 6: it is your role-play, played out by two '
         'people, with the phrases you needed and could not find.',
         'Tip: watch it the evening before your next event, not a month before. It is a '
         'rehearsal, not a theory.',
         'https://www.youtube.com/watch?v=devFLykjU9Y', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
