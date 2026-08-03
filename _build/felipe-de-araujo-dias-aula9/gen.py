#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 9 do Felipe de Araujo Dias — This Time Next Week.
Present continuous para futuro + future continuous. Modelo de FALA (aula IMPAR).
Aula do eixo GERAL (70/30): fim de semana, futebol, familia e viagem.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 9

IMG_TITLE = 'https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1517649763962-0c623066013b?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_CALL = 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Kick-off', 'the moment a football match starts',
     'Kick-off is at nine sharp, so the girls are arriving at a quarter past eight.'),
    ('To pick up', 'to collect somebody or something from a place',
     'I am picking up two of her friends on the way.'),
    ('Long weekend', 'a weekend with an extra day off because of a holiday',
     'It is a long weekend, so nobody is answering emails on Monday.'),
    ('To be off', 'to not be at work, because of a holiday or a day off',
     'I am off on Friday, so call my mobile if anything breaks.'),
    ('To make it', 'to manage to arrive or to be somewhere as planned',
     'If the traffic is bad I am not going to make it before kick-off.'),
    ('Get-together', 'an informal meeting of friends or family, usually at somebody home',
     'We are having a get-together at my sister house after the match.'),
    ('To run late', 'to be later than planned',
     'If I am running late, I will send you a message.'),
    ('Layover', 'the time you spend in an airport between two flights',
     'He has a nine hour layover in Lisbon on the way home.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Kick-off', 'd'], ['2', 'To pick up', 'b'],
                   ['3', 'Long weekend', 'g'], ['4', 'To be off', 'a'],
                   ['5', 'To make it', 'h'], ['6', 'Get-together', 'c'],
                   ['7', 'To run late', 'f'], ['8', 'Layover', 'e']],
         'defs': [['a', 'To not be at work, because of a holiday or a day off'],
                  ['b', 'To collect somebody or something from a place'],
                  ['c', 'An informal meeting of friends or family, usually at somebody home'],
                  ['d', 'The moment a football match starts'],
                  ['e', 'The time you spend in an airport between two flights'],
                  ['f', 'To be later than planned'],
                  ['g', 'A weekend with an extra day off because of a holiday'],
                  ['h', 'To manage to arrive or to be somewhere as planned']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: to run late is the problem, and not to make it is the '
                  'result. You can run late and still make it, and that is the whole story of '
                  'a Saturday morning.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Saturday starts early. ', ['1'], ' is at nine, so I am ', ['2'],
                   ' two of her friends at a quarter to eight. If the traffic on Marginal is '
                   'bad we are not going to ', ['3'],
                   ' it in time, and I hate arriving after the first minute. After the match we '
                   'are having a ', ['4'], ' at my sister house. It is a ', ['5'],
                   ', so nobody is in a hurry and nobody is answering email. I am ', ['6'],
                   ' on Monday too. If I am ', ['7'],
                   ' in the evening, my friends will start without me. On Sunday Lars is flying '
                   'home with a nine hour ', ['8'], ' in Lisbon, which sounds worse than my Saturday.'],
         'bank': ['kick-off', 'picking up', 'make', 'get-together', 'long weekend',
                  'off', 'running late', 'layover']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'A colleague from another country asks what you are doing this '
                           'weekend. Give four arrangements with times, and one thing you are '
                           'not doing.'],
            ['Scenario 2', 'Somebody wants to meet you on Saturday. Find a window together: say '
                           'when you are busy, when you are free, and agree on a time and a place.'],
            ['Scenario 3', 'Describe an ordinary Saturday morning in your family as if it were '
                           'happening right now, hour by hour, from waking up to lunch.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each plan again in the form the cue asks for.',
         'items': [['go to the match on Saturday', 'arrangement'],
                   ['at ten on Saturday, watch the match', 'in progress'],
                   ['have a get-together at one', 'arrangement'],
                   ['this time next week, fly home', 'in progress']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'A colleague asks what you are doing at the weekend. Answer with three '
                          'arrangements and a time for each.',
             'tips': ['Fixed plans take the present continuous: I am taking, we are having.',
                      'A plan with no time is not an arrangement. Give the hour.']},
            {'situation': 'They ask whether you are free on Saturday afternoon. You are not, '
                          'until four.',
             'tips': ['Say what you are doing, not just no.',
                      'Then offer the window you do have.']},
            {'situation': 'They ask what you will be doing at nine on Saturday morning.',
             'tips': ['A picture of a moment: I will be watching...',
                      'The time expression comes first or last, never in the middle.']},
            {'situation': 'The traffic is terrible and you are going to arrive after kick-off. '
                          'Call and say so.',
             'tips': ['I am running late, and the evidence is in front of you: going to.',
                      'Give a new time, not an apology.']},
            {'situation': 'They ask what you are doing on the Monday of the long weekend.',
             'tips': ['I am off. Then say what you are doing with the day.',
                      'Finish with a question back about their holiday.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['I am going to the match on Saturday.',
                  'At ten on Saturday I will be watching the match.',
                  'We are having a get-together at one.',
                  'This time next week I will be flying home.'],
         'note': ('The present continuous is an appointment already in the diary. will be doing '
                  'is a photograph of a moment that has not arrived yet.')},
    ],
}

LISTENINGS = [
    {'file': 'a9_listening1.mp3', 'voice': 'ellen',
     'text': ('Hi Felipe, this is Bea from the club. Two changes for Saturday. We are playing at '
              'nine in the morning, not at eleven, because the other team is travelling from '
              'Campinas. Kick-off is at nine sharp, so the girls are arriving at a quarter past '
              'eight. And we are not using the usual field. We are playing on field three, '
              'behind the parking. One more thing. I am collecting the shirts after the match, '
              'so please do not take them home this time. If you are running late, send me a '
              'message and we will start without her.')},
    {'file': 'a9_listening2.mp3', 'voice': 'nordic_m',
     'text': ('Felipe, it is Lars. My flight lands on Thursday evening, so I am not coming to '
              'the office on Friday morning. I am sleeping. On Friday afternoon I am meeting '
              'your team at the distribution center, and on Saturday I am completely free. So, '
              'two questions. Are you going to the match on Saturday, and is there a spare '
              'ticket? I have never seen a game in Brazil and I am not leaving without one. And '
              'on Sunday I have a nine hour layover in Lisbon on the way home, which is a long '
              'time to sit in an airport. If you know anybody there, tell me. This time next '
              'week I will be sitting in that terminal thinking about it.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l9]', 'file': 'pc9_order_weekend.mp3', 'voice': 'arthur',
     'text': ('First, Lars asks what Felipe is doing on Saturday. Then Felipe says he is taking '
              'his daughter to her match and that kick-off is at nine. After that, he explains '
              'that they are having a get-together at his sister house until four. Next, Lars '
              'asks about the game in the evening and Felipe offers to get him a ticket. '
              'Finally, they agree to meet at seven, and Lars promises to send a message if he '
              'is running late.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Aula do eixo GERAL: fim de semana, '
    'futebol e fam&iacute;lia. Diga que hoje o vocabul&aacute;rio n&atilde;o &eacute; de '
    'trabalho e siga.',
    'Chapter 1: A Saturday With a Timetable', 'This Time', 'Next Week',
    'Weekend plans, a football match and a nine hour layover', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 8 (3 min): na aula 8 ele decidiu o futuro da empresa. Hoje '
    'combina o pr&oacute;prio fim de semana, que &eacute; mais dif&iacute;cil. Pe&ccedil;a que '
    'ele responda ao prompt e ESCUTE se ele usa What do you do at the weekend para falar do '
    'futuro &mdash; &eacute; o erro do slide 12. N&atilde;o corrija ainda.',
    'You Planned the Quarter.', 'Now Plan Saturday',
    'Last time the future was a forecast and a decision. This weekend is neither. It is a diary: '
    'other people, fixed hours, and a car that has to leave at a quarter to eight. English has a '
    'separate future for exactly that, and it is not will.',
    'What are you doing this weekend? Three things, with the time of each one.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as tr&ecirc;s miss&otilde;es. Diga que hoje ele vai combinar um '
    's&aacute;bado inteiro com um estrangeiro, ao vivo. Passe ao pr&oacute;ximo.',
    ['Eight words that only come out at the weekend.',
     'Two more futures: the appointment in your diary and the photograph of a moment.',
     'Arrange a whole Saturday with somebody who does not know your city.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of a', 'Free Saturday',
    '8 words that never appear in a quarterly review', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'kick-off: Is kick-off the whole match or the first second of it? (O primeiro segundo.) CCQ '
    'para to be off: If I am off, am I sick? (N&atilde;o necessariamente &mdash; s&oacute; '
    'n&atilde;o estou trabalhando.)',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para to make it: If I make it, did I '
    'arrive? (Sim, e a tempo.) CCQ para layover: Do I leave the airport during a layover? (Nem '
    'sempre &mdash; &eacute; o tempo entre dois voos.) Pron&uacute;ncia: get-together tem stress '
    'no get.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Este par&aacute;grafo &eacute; o s&aacute;bado dele '
    '&mdash; pergunte no fim o que est&aacute; errado em rela&ccedil;&atilde;o &agrave; vida '
    'real dele e deixe ele corrigir.',
    'Use the Words', 'One Saturday, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: Two more futures, and neither of '
    'them is will. One is your diary, one is a photograph. Passe ao pr&oacute;ximo.',
    'Chapter 3: The Diary and the Photograph', 'Already Arranged,', 'Already Happening',
    'Present continuous for plans, will be doing for moments', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Two '
    'of these are appointments and two are pictures of a moment. Which are which? S&oacute; '
    'DEPOIS clique em Reveal the Rule. CCQ: In I am taking her to the match on Saturday, did I '
    'decide this now? (N&atilde;o &mdash; j&aacute; est&aacute; combinado.) In This time next '
    'week I will be flying, am I flying right now? (N&atilde;o &mdash; &eacute; uma foto do '
    'futuro.)',
    'present continuous for future and future continuous',
    [('"I <span class="accent" style="font-weight:700">am taking</span> my daughter to her match on Saturday."',
      'I am taking my daughter to her match on Saturday.'),
     ('"We <span class="accent" style="font-weight:700">are having</span> a get-together at one."',
      'We are having a get-together at one.'),
     ('"This time next week I <span class="accent" style="font-weight:700">will be flying</span> home."',
      'This time next week I will be flying home.'),
     ('"At nine thirty you <span class="accent" style="font-weight:700">will be sitting</span> in the cold."',
      'At nine thirty you will be sitting in the cold.')],
    'rule9',
    ['Form', 'Use it for', 'Example'],
    [['am / is / are + -ing',
      'A fixed arrangement. There is a time, a place and usually another person.',
      'I <strong>am taking</strong> her to the match on Saturday.'],
     ['will be + -ing',
      'A picture of a moment in the future, seen while it is happening.',
      'This time next week I <strong>will be flying</strong> home.'],
     ['The time expression',
      'The future continuous almost always needs one: at nine, this time next week, all morning.',
      '<strong>At ten</strong> I will be watching the match.'],
     ['Not for decisions',
      'A decision taken at this second still takes will: <em>I will get you a ticket.</em>'],
     ['Negative and question',
      'I <strong>am not coming</strong> on Friday. <strong>Are you going</strong> to the game? '
      '<strong>Will you be working</strong> on Monday?']],
    ('The present continuous is an appointment already in your diary. will be doing is a '
     'photograph of a moment that has not arrived yet.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. Em '
    'cada item pergunte: is this an appointment or a photograph? A resposta escolhe a forma '
    'sozinha.',
    'Grammar Practice', 'Diary, or', 'Photograph?',
    'Say the full sentence, then click to compare',
    [('I ______ (pick up) two of her friends at a quarter to eight. It is arranged.',
      'I am picking up two of her friends at a quarter to eight.'),
     ('At ten on Saturday I ______ (watch) the match.',
      'At ten on Saturday I will be watching the match.'),
     ('We ______ (have) a get-together at my sister house at one.',
      'We are having a get-together at my sister house at one.'),
     ('This time next week Lars ______ (sit) in an airport in Lisbon.',
      'This time next week Lars will be sitting in an airport in Lisbon.')]))

S.append(L.s_mistake(
    12, 3,
    'Common mistake (3 min): volte ao que voc&ecirc; anotou no warm-up. O primeiro par &eacute; '
    'o mais comum e o mais audivel: usar o presente simples para perguntar sobre o fim de '
    'semana. Pe&ccedil;a que ele leia as vers&otilde;es CERTAS duas vezes cada.',
    [('What do you do this weekend?', 'What are you doing this weekend?'),
     ('This time next week I will fly home.', 'This time next week I will be flying home.'),
     ('He is arrive on Thursday evening.', 'He is arriving on Thursday evening.')],
    ('The present simple is for what always happens, not for this Saturday. And after will be, '
     'the verb needs the -ing or the picture does not move.')))

S.append(L.s_listening(
    13, 3,
    'Listening 1 (5 min): a treinadora do time da filha, americana, com duas mudan&ccedil;as e '
    'tr&ecirc;s hor&aacute;rios. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. &Eacute; o '
    'tipo de &aacute;udio que ele perde na vida real por causa dos n&uacute;meros. Toque duas '
    'vezes.',
    1, 'The Message from', 'the Club',
    'Two changes for Saturday, left the night before. Sound first, no text.',
    'a9_listening1.mp3', SLUG,
    [('What time is kick-off, and why did it change?',
      'Nine in the morning, because the other team is travelling from Campinas.'),
     ('Where are they playing this time?',
      'On field three, behind the parking, not on the usual field.'),
     ('What should the parents not do after the match?',
      'Take the shirts home. Bea is collecting them.')]))

S.append(L.s_chapter(
    14, 4,
    'Transi&ccedil;&atilde;o di&aacute;logo (1 min): diga: Now the conversation. Lars is the '
    'colleague from Oslo, he is here for four days, and he has never seen a game in Brazil. '
    'Passe ao pr&oacute;ximo.',
    'Chapter 4: Finding a Window', 'Two Diaries,', 'One Saturday',
    'Arranging a day with somebody who does not know your city', IMG_CALL))

S.append(L.s_dialogue(
    15, 4,
    'Di&aacute;logo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, pe&ccedil;a que '
    'ELE fale primeiro, com o texto tapado. Lars tem sotaque n&oacute;rdico. Aponte a fala 12: '
    'ele n&atilde;o diz s&oacute; n&atilde;o estou livre, ele diz O QUE est&aacute; fazendo '
    '&mdash; &eacute; a diferen&ccedil;a entre fechar e abrir a conversa.',
    'Two Diaries,', 'One Saturday',
    [('lars', 'L', 'nordic_m',
      'Felipe, before we start, what are you doing on Saturday?'),
     ('felipe', 'F', 'arthur',
      'In the morning I am taking my daughter to her match. '
      '<span class="vocab-highlight">Kick-off</span> is at nine.'),
     ('lars', 'L', 'nordic_m', 'Does she play every Saturday?'),
     ('felipe', 'F', 'arthur',
      'Almost. And after that we are having a <span class="vocab-highlight">get-together</span> '
      'at my sister house, so I am not free until four.'),
     ('lars', 'L', 'nordic_m',
      'That is fine. I am not doing anything until the evening. Is the match far?'),
     ('felipe', 'F', 'arthur',
      'Forty minutes, and I am <span class="vocab-highlight">picking up</span> two of her '
      'friends on the way, so it is a full car.'),
     ('lars', 'L', 'nordic_m', 'I understand. And in the evening? Are you going to the game?'),
     ('felipe', 'F', 'arthur',
      'I am. I am meeting two friends at seven and the game starts at nine thirty.'),
     ('lars', 'L', 'nordic_m',
      'Perfect. This time next week I will be flying home, so this is my only chance.'),
     ('felipe', 'F', 'arthur',
      'Then come. I will get you a ticket tomorrow. Where are you staying?'),
     ('lars', 'L', 'nordic_m',
      'In Pinheiros. If I am <span class="vocab-highlight">running late</span>, I will send you '
      'a message.'),
     ('felipe', 'F', 'arthur',
      'Do that. And bring a jacket. At nine thirty in July you will be sitting in the cold for '
      'two hours.')]))

S.append(L.s_comprehension(
    16, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre o LARS, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar. Se errar, volte ao di&aacute;logo e toque a fala.',
    'Did You Catch It?', 'About', 'Lars',
    [('What is Lars doing on Saturday until the evening?',
      'Nothing. He says he is not doing anything until then.'),
     ('Why does he say this is his only chance to see a game?',
      'Because this time next week he will be flying home.'),
     ('Where is he staying, and what will he do if he is running late?',
      'In Pinheiros. He will send Felipe a message.')]))

S.append(L.s_artifact(
    17, 4,
    'Artefato (4 min): a agenda do s&aacute;bado dele. Pe&ccedil;a que ele LEIA em voz alta e '
    'depois responda. A terceira pergunta &eacute; produ&ccedil;&atilde;o: exija o future '
    'continuous inteiro, com a express&atilde;o de tempo.',
    'Real Document', 'The Saturday', 'Timetable',
    'WEEKEND PLAN &mdash; SATURDAY', 'FELIPE',
    [('07:45', 'Leaving home &middot; picking up two of her friends'),
     ('09:00', 'Kick-off &middot; field three'),
     ('11:00', 'Shirts back to the coach, then lunch'),
     ('13:00', 'Get-together at my sister house'),
     ('16:00', 'Free'),
     ('19:00', 'Meeting two friends in Pinheiros'),
     ('21:30', 'The game starts'),
     ('Sunday', 'Lars is flying home &middot; 9h layover in Lisbon')],
    [('What is he doing at nine, and where?',
      'He is watching his daughter match, on field three.'),
     ('Between which hours is he not free?',
      'Between a quarter to eight in the morning and four in the afternoon.'),
     ('Say what he will be doing at ten on Saturday morning.',
      'At ten on Saturday morning I will be watching my daughter match.')]))

S.append(L.s_listening(
    18, 4,
    'Listening 2 (5 min): sotaque n&oacute;rdico, o mesmo Lars do di&aacute;logo. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Este &aacute;udio tem seis planos combinados em seis '
    'frases &mdash; pe&ccedil;a que ele reconstrua a agenda do Lars no fim. Toque duas vezes.',
    2, 'Lars Plans', 'His Four Days',
    'A message left the day before he flies. Sound first, no text.',
    'a9_listening2.mp3', SLUG,
    [('Why is Lars not coming to the office on Friday morning?',
      'His flight lands on Thursday evening, so he is sleeping.'),
     ('What does he want for Saturday, and why does it matter to him?',
      'A spare ticket for the match. He has never seen a game in Brazil.'),
     ('What is the problem with Sunday?',
      'He has a nine hour layover in Lisbon on the way home.')]))

S.append(L.s_blocks(
    19, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez. Ele responde EM VOZ ALTA antes de '
    'abrir as Tips. Exija HORA em toda resposta &mdash; plano sem hora n&atilde;o &eacute; '
    'arrangement, e a gram&aacute;tica desmonta junto.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    20, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you arrange it. Three rounds, less '
    'help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    21, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija quatro compromissos com hora. No '
    'rephrase ele escolhe a forma pela pista entre par&ecirc;nteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    22, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('What do you do this weekend?', 'What are you doing this weekend?'),
     ('I will be pick up her friends at a quarter to eight.',
      'I will be picking up her friends at a quarter to eight.'),
     ('At nine we will sitting in the stadium.', 'At nine we will be sitting in the stadium.'),
     ('He is arrive on Thursday evening.', 'He is arriving on Thursday evening.')]))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; o Lars. Pergunte pelo s&aacute;bado, '
    'ou&ccedil;a, e proponha um hor&aacute;rio que N&Atilde;O funciona, para que ele tenha de '
    'dizer o que est&aacute; fazendo em vez de dizer s&oacute; n&atilde;o.',
    'Role-Play 1 &mdash; Guided', 'What Are You Doing', 'on Saturday?',
    'Situation',
    'A colleague from abroad asks about your Saturday. Give four arrangements with times, say '
    'when you are not free and why, and offer the window you do have.',
    ['I am taking', 'kick-off is at', 'we are having', 'I am not free until',
     'I am meeting']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; o Lars de novo, mas agora com '
    'um problema: o voo dele mudou e ele chega s&aacute;bado de manh&atilde;. Toda a agenda '
    'combinada cai. Ele tem de remarcar ao vivo.',
    'Role-Play 2 &mdash; Semi-Free', 'The Plan That', 'Changed',
    'Situation',
    'His flight moved and everything you arranged has to move too. Rebuild the day out loud: '
    'what you are still doing, what you are cancelling, and what the two of you are doing '
    'instead.',
    ['I am still', 'we are not', 'instead']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa. Cronometre noventa segundos e conte quantos compromissos com hora ele produziu. '
    'Diga o n&uacute;mero no fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Describe your real next weekend, hour by hour, to somebody who has never been to your city: '
    'what you are doing and when, who you are seeing, what you will be doing at ten on Sunday '
    'morning, and one thing you are not doing on purpose. Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    26, 6,
    'Answer key (2 min): o accordion nasce fechado. S&oacute; abra depois que ele tentou as '
    'quatro do rephrase. Clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    27,
    'Survival lines (3 min): leia cada frase, toque o &aacute;udio, pe&ccedil;a repeti&ccedil;'
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco do pr&oacute;ximo fim de semana '
    'dele com estrangeiro.',
    'Say It with', 'Confidence',
    ['What are you doing on Saturday?',
     'I am taking my daughter to her match. Kick-off is at nine.',
     'I am not free until four, but I am meeting friends at seven.',
     'If I am running late, I will send you a message.',
     'This time next week I will be flying home.']))

S.append(L.s_checklist(
    28,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 9.',
    9,
    ['I can arrange a whole day with somebody, out loud, in English.',
     'I use am doing for a plan that already has a time and a place.',
     'I use will be doing for a moment I can picture in the future.',
     'I never ask what do you do when I mean this weekend.',
     'I know the words: kick-off, to pick up, long weekend, to be off, to make it, '
     'get-together, to run late, layover.']))

S.append(L.s_badge(
    29,
    'Encerramento (2 min): diga: Lesson 9 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar noventa segundos com o fim de semana real dele, hora por hora, e mandar no '
    'WhatsApp. Pr&oacute;xima aula: Getting What You Need Politely.',
    9, 'This Time Next Week',
    'You arranged a whole Saturday with a Norwegian today, Felipe, and nobody got lost.',
    'Getting What You Need Politely'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'This Time Next Week -- Arranging Plans',
    'short_title': 'This Time Next Week',
    'menu_desc': ('Speaking lesson: a Saturday with a timetable, a football match and a nine '
                  'hour layover, in the two futures that are not will'),
    'grammar_point': 'present continuous for future and future continuous',
    'characters': {'felipe': 'arthur', 'lars': 'nordic_m'},
    'phases': ['A Saturday With a Timetable', 'Your Words',
               'The Diary and the Photograph', 'Finding a Window', 'Real Talk', 'Your Turn',
               'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=600&q=80',
    'desc': ('The words of a free Saturday: kick-off, to pick up, long weekend, to be off, to '
             'make it, get-together, to run late, layover. Structure: present continuous for a '
             'fixed arrangement, and will be doing for a moment you can picture. Mission: '
             'arrange a whole day with somebody who does not know your city.'),
    'context_paras': [
        'On Saturday I <strong>am taking</strong> my daughter to her match. Kick-off is at nine, '
        'so I <strong>am picking up</strong> two of her friends at a quarter to eight. At one we '
        '<strong>are having</strong> a get-together at my sister house, and I '
        '<strong>am not</strong> free until four. In the evening I <strong>am meeting</strong> '
        'two friends at seven. None of that was decided just now. All of it is in the diary, '
        'with an hour and a place, and that is why every verb is in the -ing form of the '
        'present.',
        'Two sentences in that day are different. <em>At ten on Saturday morning I '
        '<strong>will be watching</strong> the match</em> is not an appointment. It is a '
        'photograph: pick a moment in the future and look at what is happening inside it. Same '
        'with Lars: <em>this time next week he <strong>will be sitting</strong> in an airport in '
        'Lisbon</em>. And when Lars asks for a ticket and I answer <em>I <strong>will get</strong> '
        'you one tomorrow</em>, that is neither. That is a decision, taken at the second I speak '
        'it, and it goes back to plain will.'],
    'context_quiz': [
        ('Why is it <em>I am picking up two of her friends</em> and not <em>I will pick up</em>?',
         [('Because picking up is a physical action and physical actions take -ing.', False),
          ('Because it is already arranged: there is an hour, a place and other people involved.',
           True),
          ('Because it happens before nine in the morning.', False)]),
        ('What does <em>At ten I will be watching the match</em> describe?',
         [('A decision he is taking right now about ten o clock.', False),
          ('A moment in the future, seen from inside, while it is happening.', True),
          ('A promise he made to his daughter.', False)]),
        ('Why does <em>I will get you a ticket tomorrow</em> use plain will?',
         [('Because it is a decision taken at the second he speaks it.', True),
          ('Because tickets are always in the simple future.', False),
          ('Because tomorrow is too close for the continuous.', False)]),
    ],
    'tip_title': 'Present Continuous for the Future and Future Continuous',
    'tip_intro': ('Two futures that have nothing to do with will. One is your diary. The other '
                  'is a photograph of a moment that has not happened yet.'),
    'tip_rows': [
        ['am / is / are + -ing',
         'A fixed arrangement: a time, a place, and usually another person who also knows.',
         'I <strong>am taking</strong> her to the match at nine.'],
        ['will be + -ing',
         'A moment in the future, seen from inside it while it is in progress.',
         'This time next week I <strong>will be flying</strong> home.'],
        ['The time expression',
         'The future continuous nearly always needs one: <em>at ten</em>, <em>this time next '
         'week</em>, <em>all Sunday morning</em>.'],
        ['Still plain will',
         'A decision taken at the second you speak, a promise or an offer: <em>I '
         '<strong>will get</strong> you a ticket.</em>'],
        ['Never the present simple for a plan',
         '<em>What <strong>are you doing</strong> this weekend?</em>, never <em>What do you do '
         'this weekend?</em>'],
        ['Negatives and questions',
         'I <strong>am not coming</strong> on Friday. <strong>Are you going</strong> to the '
         'game? <strong>Will you be working</strong> on Monday?'],
    ],
    'tip_note': ('A quick test: if somebody else already knows about the plan, it is an '
                 'arrangement and it takes am doing. If you are describing what a moment will '
                 'look like, it takes will be doing.'),
    'blanks': [
        ('On Saturday I ', 'am taking',
         'Hint: two words. It is already arranged, with an hour and a place.',
         'On Saturday I am taking my daughter to her match.', ' my daughter to her match.'),
        ('At ten on Saturday I ', 'will be watching',
         'Hint: three words. A photograph of a moment in the future.',
         'At ten on Saturday I will be watching the match.', ' the match.'),
        ('', 'Kick-off', 'Hint: one word with a hyphen. The moment the match starts.',
         'Kick-off is at nine sharp.', ' is at nine sharp.'),
        ('I am ', 'picking up', 'Hint: two words. To collect somebody on the way.',
         'I am picking up two of her friends at a quarter to eight.',
         ' two of her friends at a quarter to eight.'),
        ('If I am ', 'running late', 'Hint: two words. Later than planned.',
         'If I am running late, I will send you a message.', ', I will send you a message.'),
        ('He has a nine hour ', 'layover',
         'Hint: one word. The time between two flights, inside the airport.',
         'He has a nine hour layover in Lisbon.', ' in Lisbon.'),
    ],
    'order_title': 'Put the Saturday in Order',
    'order_intro': 'Listen first, then put the five parts of the conversation in the order you '
                   'hear them.',
    'order': [
        (5, 'Finally, they agree to meet at seven, and Lars promises to send a message if he is '
            'running late.'),
        (2, 'Then Felipe says he is taking his daughter to her match and that kick-off is at nine.'),
        (4, 'Next, Lars asks about the game in the evening and Felipe offers to get him a ticket.'),
        (1, 'First, Lars asks what Felipe is doing on Saturday.'),
        (3, 'After that, he explains that they are having a get-together at his sister house '
            'until four.'),
    ],
    'speech': [
        'What are you doing on Saturday?',
        'I am taking my daughter to her match. Kick-off is at nine.',
        'I am not free until four, but I am meeting friends at seven.',
        'If I am running late, I will send you a message.',
        'This time next week I will be flying home.',
    ],
    'quiz_intro': 'You are arranging a weekend with somebody. Choose the best thing to say.',
    'quiz': [
        ('A colleague wants to know your weekend plans. The natural question is:',
         [('What do you do this weekend?', False),
          ('What are you doing this weekend?', True),
          ('What will you do this weekend, normally?', False)]),
        ('The match is already arranged for nine on Saturday. You say:',
         [('I will take my daughter to her match at nine.', False),
          ('I am taking my daughter to her match at nine.', True),
          ('I take my daughter to her match at nine on Saturday.', False)]),
        ('You want to describe your Sunday morning as a picture. You say:',
         [('At ten on Sunday I will be driving to the airport.', True),
          ('At ten on Sunday I will drive to the airport, I think.', False),
          ('At ten on Sunday I will driving to the airport.', False)]),
        ('Your friend asks for a ticket and you decide, right now, to get one. You say:',
         [('I am getting you a ticket tomorrow.', False),
          ('I will get you a ticket tomorrow.', True),
          ('I will be get you a ticket tomorrow.', False)]),
    ],
    'think': ('Think about your real next weekend. Record about ninety seconds. Go hour by hour: '
              'say what you are doing and at what time, and who else knows about each plan. Use '
              'the present continuous for everything that is already arranged. Then pick two '
              'moments, one on Saturday and one on Sunday, and describe them from inside, with '
              'will be doing. Finish with one thing you are deliberately not doing this weekend, '
              'and why. Use at least four words from this lesson. Do not stop to correct '
              'yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"Present continuous and going to" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on the -ing future, and how it differs from going to. Connection to Lesson '
         '9: it is the arrangement half of what you practised, with the pronunciation of the '
         'contractions you keep missing.',
         'Tip: after each example, ask yourself whether another person already knows about that '
         'plan. That is the test.',
         'https://www.youtube.com/watch?v=-8660VeIj4U', 'Watch on YouTube'),
        ('video', 'continuous', 'Video Lesson',
         'Future continuous explained -- advanced English grammar',
         'A clear walk through will be doing, with business and everyday examples and the time '
         'expressions it needs. Connection to Lesson 9: it is the photograph half, the one you '
         'used for this time next week.',
         'Tip: write three sentences about next Tuesday at nine, at one and at eight. Then say '
         'them without reading.',
         'https://www.youtube.com/watch?v=BG-20HkLQzo', 'Watch on YouTube'),
        ('video', 'suggestions', 'Video Lesson',
         'Making suggestions and replies: let us, shall we, why do not we',
         'The small phrases that move a plan forward when two people are trying to find a '
         'window. Connection to Lesson 9: your role-play needed exactly these, and you had to '
         'invent them.',
         'Tip: choose three you would really say. Use them the next time somebody asks you to '
         'meet.',
         'https://www.youtube.com/watch?v=vqbUM80kQBk', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
