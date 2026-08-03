#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 10 do Felipe de Araujo Dias — Getting What You Need Politely.
Modais de pedido e permissao. Modelo de LEITURA (aula PAR, REGRA 29).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 10

IMG_TITLE = 'https://images.unsplash.com/photo-1596526131083-e8c633c948d2?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Favor', 'something helpful you do for somebody when you do not have to',
     'May I ask you for a favor before we start?'),
    ('Heads-up', 'a warning given in advance so somebody has time to prepare',
     'Could you give my team a heads-up when your volumes change?'),
    ('To chase', 'to contact somebody again and again because you are waiting for something',
     'I have been chasing that signature since Monday.'),
    ('Workaround', 'a temporary way around a problem, without fixing the cause',
     'We found a workaround, but the dock is still the problem.'),
    ('To sign off', 'to give official approval to something',
     'Could you sign off the amendment before Friday?'),
    ('Reminder', 'a short message that helps somebody remember what they have to do',
     'This is a reminder, not a complaint.'),
    ('To be swamped', 'to have far too much work at the same time',
     'If I am swamped on Tuesday, I will sign on Monday evening instead.'),
    ('Bandwidth', 'the time and the energy a person or a team actually has available',
     'I will not have the bandwidth before Thursday.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Favor', 'e'], ['2', 'Heads-up', 'b'], ['3', 'To chase', 'g'],
                   ['4', 'Workaround', 'a'], ['5', 'To sign off', 'h'],
                   ['6', 'Reminder', 'c'], ['7', 'To be swamped', 'f'],
                   ['8', 'Bandwidth', 'd']],
         'defs': [['a', 'A temporary way around a problem, without fixing the cause'],
                  ['b', 'A warning given in advance so somebody has time to prepare'],
                  ['c', 'A short message that helps somebody remember what they have to do'],
                  ['d', 'The time and the energy a person or a team actually has available'],
                  ['e', 'Something helpful you do for somebody when you do not have to'],
                  ['f', 'To have far too much work at the same time'],
                  ['g', 'To contact somebody again and again because you are waiting'],
                  ['h', 'To give official approval to something']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a heads-up arrives before the problem and a reminder arrives '
                  'after it. Send the first one and you almost never have to send the second.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['May I ask you for a ', ['1'], '? I need somebody to ', ['2'],
                   ' the amendment before Friday. This is a ', ['3'],
                   ', not a complaint: I know you are ', ['4'],
                   ' this week and that nobody has the ', ['5'],
                   ' for one more document. If Friday is impossible, give me a ', ['6'],
                   ' today and we will build a ', ['7'],
                   ' with legal. I would rather do that than ', ['8'],
                   ' you every morning until Monday.'],
         'bank': ['favor', 'sign off', 'reminder', 'swamped', 'bandwidth',
                  'heads-up', 'workaround', 'chase']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The Email That Asks Without Offending',
         'paras': [
             'There is a particular email that every operations team writes about twice a week, '
             'and almost nobody writes well. It asks somebody for something they do not have to '
             'give: a favor, an exception, a signature before Friday. The writer knows the '
             'request is inconvenient, so they do one of two things, and both of them fail. '
             'Either they write four paragraphs of apology and the request disappears inside '
             'them, or they write one line that reads like an order, and somebody in another '
             'country decides they are rude.',
             'The good version is short and it has three parts, in this order. First a heads-up: '
             'one sentence that says what this is about, so the reader knows before deciding how '
             'to feel about it. Then the request itself, in one sentence, with the deadline '
             'inside it. Then the way out: a sentence that makes it easy to say no, or to say '
             'later. Would you mind signing it before Friday? If Friday is impossible, could you '
             'tell me when it is possible? Notice that nothing in it is softer than the truth. '
             'Politeness in English is not about being vague. It is about leaving the other '
             'person a door.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why operations teams write too many emails', False],
                     ['b', 'A polite request is short, clear and leaves a way out', True],
                     ['c', 'How to apologize properly in a professional email', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['The text says a polite email should open with an apology.', 'f',
             'It says four paragraphs of apology make the request disappear inside them.'],
            ['The request should have the deadline inside it.', 't',
             'The second part is the request in one sentence, with the deadline inside it.'],
            ['Being polite in English means being vague.', 'f',
             'The text says politeness is not about being vague. It is about leaving the other '
             'person a door.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Ask a supplier you barely know for an exception, out loud, in three '
                           'sentences: the heads-up, the request with the deadline, and the way '
                           'out.'],
            ['Scenario 2', 'Somebody asks you for something you cannot do this week. Say no '
                           'without closing the door, and offer one alternative.'],
            ['Scenario 3', 'You have chased the same signature three times. Ask a fourth time '
                           'without sounding annoyed, and without pretending you are not.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each request again, starting with the words in brackets.',
         'items': [['Send me the file. (Could you...)', 'polite'],
                   ['Sign it before Friday. (Would you mind...)', 'most polite'],
                   ['I want to use your name in the email. (May I...)', 'permission'],
                   ['Give my team a warning next time. (Could you...)', 'polite']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'You need a signature from somebody senior who does not report to you, '
                          'and you need it in two days.',
             'tips': ['Heads-up first, request second, way out third.',
                      'Put the deadline inside the request, not in a separate sentence.']},
            {'situation': 'You want permission to use somebody name in an email to their boss.',
             'tips': ['Permission is May I, not Could you.',
                      'Say what you will write, so they are not surprised.']},
            {'situation': 'A colleague asks you for a favor and you genuinely cannot do it this '
                          'week.',
             'tips': ['I am afraid I cannot this week, but I could on Monday.',
                      'Give one reason. Not three.']},
            {'situation': 'You have chased the same document three times and it is now urgent.',
             'tips': ['Name the fact without the emotion: this is my fourth message.',
                      'Then ask for the smallest possible next step, not the whole thing.']},
            {'situation': 'Somebody has done you a big favor and you want to offer something '
                          'back.',
             'tips': ['Ask what would help them, instead of guessing.',
                      'Would it help if I...? is the sentence you are missing.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['Could you send me the file?',
                  'Would you mind signing it before Friday?',
                  'May I use your name in the email?',
                  'Could you give my team a warning next time?'],
         'note': ('Would you mind is followed by the -ing form, and Could you and May I are '
                  'followed by the bare verb. Never by to.')},
    ],
}

LISTENINGS = [
    {'file': 'a10_listening1.mp3', 'voice': 'arthur',
     'text': ('Felipe, it is Daniel again. Two favors, and you can say no to both. First, could '
              'you take the Tuesday call for me? I am swamped with the audit and I will not have '
              'the bandwidth before Thursday. It is thirty minutes and you know that file better '
              'than I do. Second, and this one is bigger. Would you mind presenting the capacity '
              'study to the board yourself? I can do it, but it lands better from you. If either '
              'of those is impossible this week, just tell me and I will find another way. No '
              'explanation needed.')},
    {'file': 'a10_listening2.mp3', 'voice': 'indian_f',
     'text': ('Felipe, Priya here. Good news and a small request. The amendment is signed. I did '
              'it on Monday evening because Tuesday was impossible, and it is already with your '
              'legal team. Now the request. Would you mind sending the forecast on the first '
              'working day of the month, and not on the fifth? By the fifth we have already '
              'booked the fabric, so the number does not help us. And one more thing, if I may. '
              'Could you copy my colleague Anand on those emails? I am off for two weeks in '
              'September and I would rather he did not find out from the trucks either. Thank '
              'you for the yellow marks, by the way. That saved me an hour.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l10]', 'file': 'pc10_order_request.mp3', 'voice': 'ellen',
     'text': ('First, Felipe asks whether he may ask Priya for a favor. Then he asks her to sign '
              'off the amendment before Friday, and explains why. After that, Priya asks him to '
              'send only the two clauses that changed. Next, she asks for something in return: '
              'a heads-up whenever his volumes change. Finally, she says that if she is swamped '
              'on Tuesday she will sign on Monday evening instead.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Aula de LEITURA. O tema &eacute; o '
    'e-mail que ele escreve duas vezes por semana e que sempre sai errado em ingl&ecirc;s.',
    'Chapter 1: The Email Nobody Writes Well', 'Getting What You', 'Need Politely',
    'Asking for something the other person does not have to give', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 9 (3 min): na aula 9 ele combinou hor&aacute;rios com um colega. '
    'Hoje pede algo que a pessoa N&Atilde;O &eacute; obrigada a dar. Pe&ccedil;a que ele fa&ccedil;'
    'a o pedido em voz alta e ESCUTE se sai I need you to ou I want that you &mdash; s&atilde;o '
    'os dois padr&otilde;es que soam duros. N&atilde;o corrija ainda.',
    'You Arranged the Time.', 'Now Ask for the Favor',
    'Arranging a meeting is easy: both people want it. Asking for a signature two days early is '
    'not. The other person gains nothing and loses an afternoon, and the only thing standing '
    'between you and a no is how the sentence is built.',
    'Ask me, out loud, to sign something before Friday. Any way you like.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Diga que o texto do meio &eacute; sobre o e-mail dele. '
    'Passe ao pr&oacute;ximo.',
    ['Eight words for asking, waiting and being asked.',
     'Four ways to ask for the same thing, and the difference a country makes.',
     'Ask for an exception, and say no to one, without closing any doors.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of', 'Asking',
    '8 words for the favor, the wait and the no', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'heads-up: Does a heads-up come before or after the problem? (Antes.) CCQ para workaround: '
    'Does a workaround fix the cause? (N&atilde;o &mdash; s&oacute; contorna.) Pron&uacute;ncia: '
    'favor tem stress na primeira s&iacute;laba (FAY-ver).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para to be swamped: Is swamped a little '
    'busy or too busy? (Cheio demais.) CCQ para bandwidth: Is bandwidth about internet here? '
    '(N&atilde;o &mdash; &eacute; tempo e energia de pessoa.) Estas duas s&atilde;o o jeito '
    'educado de dizer n&atilde;o em ingl&ecirc;s corporativo.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Repare que o par&aacute;grafo J&Aacute; &eacute; um '
    'pedido educado inteiro &mdash; pergunte no fim quantas partes ele consegue identificar.',
    'Use the Words', 'One Request, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o leitura (1 min): diga: Read for the main idea first. Do not '
    'translate word by word.',
    'Chapter 3: Read the Email', 'Three Parts,', 'In This Order',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist. '
    'N&atilde;o pe&ccedil;a tradu&ccedil;&atilde;o. Pergunte no fim qual dos dois erros do texto '
    '&eacute; o dele &mdash; ele vai saber.',
    'Read for the Main Idea', 'The Email That Asks', 'Without Offending', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): desta vez ele est&aacute; do outro lado &mdash; algu&eacute;m pede um '
    'favor a ELE. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Repare em quantas portas '
    'de sa&iacute;da o Daniel deixa. Toque duas vezes.',
    1, 'Two Favors, and', 'You Can Say No',
    'A colleague asks you for something, twice. Sound first, no text.',
    'a10_listening1.mp3', SLUG,
    [('What is the first favor, and how long does it take?',
      'Taking the Tuesday call for him. Thirty minutes.'),
     ('Why can Daniel not do it himself?',
      'He is swamped with the audit and will not have the bandwidth before Thursday.'),
     ('What does he say if Felipe cannot do either of them?',
      'Just tell him and he will find another way. No explanation needed.')]))

S.append(L.s_chapter(
    13, 4,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: Four ways to ask for the same thing, '
    'and they are not interchangeable. Passe ao pr&oacute;ximo.',
    'Chapter 4: Four Doors', 'Can, Could,', 'May, Would You Mind',
    'The same request, four temperatures', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: These '
    'ask for the same thing. Put them in order, from the closest colleague to the person you '
    'have never met. S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In Would you mind signing '
    'it, if the answer is yes, did they agree? (N&atilde;O &mdash; yes significa que se '
    'incomoda.) Este detalhe j&aacute; custou reuni&atilde;o a muita gente.',
    'modals of request and permission',
    [('"<span class="accent" style="font-weight:700">Can you</span> send me the file?"',
      'Can you send me the file?'),
     ('"<span class="accent" style="font-weight:700">Could you</span> send me the file before Friday?"',
      'Could you send me the file before Friday?'),
     ('"<span class="accent" style="font-weight:700">May I</span> ask you for a favor?"',
      'May I ask you for a favor?'),
     ('"<span class="accent" style="font-weight:700">Would you mind</span> signing it today?"',
      'Would you mind signing it today?')],
    'rule10',
    ['Form', 'Use it for', 'Example'],
    [['Can you...?', 'Fast and neutral, with people you work with every day.',
      '<strong>Can you</strong> send me the file?'],
     ['Could you...?', 'The safe default at work, with anybody, in any country.',
      '<strong>Could you</strong> send it before Friday?'],
     ['May I...?', 'Asking for PERMISSION, not for an action. Formal, and about yourself.',
      '<strong>May I</strong> use your name in the email?'],
     ['Would you mind + -ing?',
      'The most polite. Note the -ing. And note that <em>yes</em> means no.',
      '<strong>Would you mind signing</strong> it today?'],
     ['Saying no with a door open',
      'I am afraid I cannot this week &middot; I would rather &middot; Could we do it on Monday '
      'instead?']],
    ('The modal is only half the job. Add a reason and a way out, and even a plain can sounds '
     'polite. Leave them out, and would you mind still sounds like an order.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. Em '
    'cada item pergunte primeiro: is this an action or permission? A resposta escolhe o modal '
    'sozinha.',
    'Grammar Practice', 'Same Request,', 'Four Temperatures',
    'Say the full sentence, then click to compare',
    [('______ you send me the two clauses that changed?',
      'Could you send me the two clauses that changed?'),
     ('______ I ask you for a favor before we start?',
      'May I ask you for a favor before we start?'),
     ('Would you mind ______ (sign) it before Friday?',
      'Would you mind signing it before Friday?'),
     ('I am afraid I ______ this week, but I ______ on Monday.',
      'I am afraid I cannot this week, but I could on Monday.')]))

S.append(L.s_mistake(
    16, 4,
    'Common mistake (3 min): volte ao que voc&ecirc; anotou no warm-up. O terceiro par &eacute; a '
    'tradu&ccedil;&atilde;o direta do portugu&ecirc;s e soa como ordem em qualquer pa&iacute;s. '
    'Pe&ccedil;a que ele leia as vers&otilde;es CERTAS duas vezes cada.',
    [('Could you to send me the file?', 'Could you send me the file?'),
     ('Would you mind to sign it today?', 'Would you mind signing it today?'),
     ('I want that you send me the file.', 'Could you send me the file?')],
    ('After can, could and may the verb comes bare, with no to. After would you mind it takes '
     'the -ing. And English has no I want that: the want disappears into the question.')))

S.append(L.s_dialogue(
    17, 4,
    'Di&aacute;logo (6 min): a mesma Priya da aula 3, agora do outro lado de um favor. Clique '
    'Next Line a cada fala. Nas falas do FELIPE, pe&ccedil;a que ELE fale primeiro, com o texto '
    'tapado. Aponte a fala 8: ela pede algo em troca, e &eacute; isso que transforma um favor '
    'numa rela&ccedil;&atilde;o.',
    'The Favor and', 'the Favor Back',
    [('felipe', 'F', 'arthur',
      'Priya, thank you for making time. May I ask you for a '
      '<span class="vocab-highlight">favor</span> before we start?'),
     ('priya', 'P', 'indian_f', 'Of course. Go ahead.'),
     ('felipe', 'F', 'arthur',
      'Could you <span class="vocab-highlight">sign off</span> the amendment before Friday? Our '
      'board pack closes at noon on Wednesday.'),
     ('priya', 'P', 'indian_f',
      'Wednesday. That is tight. What happens if it is not signed?'),
     ('felipe', 'F', 'arthur',
      'Then the second site opens without a contract, and I would rather not do that.'),
     ('priya', 'P', 'indian_f',
      'I understand. Would you mind sending me the two clauses that changed, instead of the '
      'whole document?'),
     ('felipe', 'F', 'arthur',
      'Not at all. I will send them this afternoon, marked in yellow.'),
     ('priya', 'P', 'indian_f', 'Good. And can I ask you something in return?'),
     ('felipe', 'F', 'arthur', 'Please.'),
     ('priya', 'P', 'indian_f',
      'Could you give my team a <span class="vocab-highlight">heads-up</span> when your volumes '
      'change? Last quarter we found out from the trucks.'),
     ('felipe', 'F', 'arthur',
      'That is fair. I will put you on the forecast list from this month.'),
     ('priya', 'P', 'indian_f',
      'Then we have a deal. If I am <span class="vocab-highlight">swamped</span> on Tuesday, I '
      'will sign on Monday evening instead.')]))

S.append(L.s_comprehension(
    18, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre a PRIYA, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar.',
    'Did You Catch It?', 'About', 'Priya',
    [('What does Priya ask for instead of the whole document?',
      'Only the two clauses that changed.'),
     ('What does she ask for in return?',
      'A heads-up for her team whenever his volumes change.'),
     ('What will she do if she is swamped on Tuesday?',
      'She will sign on Monday evening instead.')]))

S.append(L.s_artifact(
    19, 4,
    'Artefato (4 min): o e-mail do texto, escrito. Pe&ccedil;a que ele LEIA em voz alta e depois '
    'responda. A terceira pergunta &eacute; produ&ccedil;&atilde;o: exija a frase reescrita '
    'inteira, com o -ing.',
    'Real Document', 'The Four Line', 'Email',
    'NEW MESSAGE', 'TO: PRIYA RAMAN',
    [('Subject', 'Amendment 2 &mdash; signature before Friday'),
     ('Line 1', 'A quick heads-up: our board pack closes on Wednesday at noon.'),
     ('Line 2', 'Could you sign off amendment 2 before Friday?'),
     ('Line 3', 'I am sending only the two clauses that changed, marked in yellow.'),
     ('Line 4', 'If Friday is impossible, could you tell me when it is?'),
     ('Sign-off', 'Thank you &middot; Felipe'),
     ('Length', '4 lines &middot; 62 words'),
     ('Not in this email', 'No apology &middot; no history of the project')],
    [('Which line is the heads-up, and why does it come first?',
      'Line 1. The reader knows what it is about before deciding how to feel about it.'),
     ('Which line is the way out, and what does it make easy?',
      'Line 4. It makes it easy to say later instead of no.'),
     ('Say line 2 again, starting with Would you mind.',
      'Would you mind signing off amendment 2 before Friday?')]))

S.append(L.s_listening(
    20, 4,
    'Listening 2 (5 min): sotaque indiano, a mesma Priya da aula 3 e do di&aacute;logo. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Ela faz dois pedidos usando duas formas diferentes '
    '&mdash; pergunte no fim quais foram. Toque duas vezes.',
    2, 'Signed, and One', 'Small Request',
    'Priya answers the favor and asks for two of her own. Sound first, no text.',
    'a10_listening2.mp3', SLUG,
    [('When did Priya sign the amendment, and why then?',
      'On Monday evening, because Tuesday was impossible.'),
     ('What does she ask about the forecast?',
      'To send it on the first working day of the month, not on the fifth.'),
     ('Why does she want her colleague Anand copied on those emails?',
      'Because she is off for two weeks in September.')]))

S.append(L.s_blocks(
    21, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez. Ele responde EM VOZ ALTA antes de '
    'abrir as Tips. Exija as TR&Ecirc;S partes em toda resposta: aviso, pedido com prazo, '
    'sa&iacute;da. Se faltar a sa&iacute;da, devolva: and what if they cannot?',
    'Chapter 5: Real Talk', 'Ask on the', 'Spot', ['quickfire'],
    'Read each situation. Say the real sentence out loud first, then tap Tips.'))

S.append(L.s_chapter(
    22, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you ask, and you also refuse. '
    'Three rounds, less help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    23, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios exija as tr&ecirc;s partes. No rephrase '
    'ele reescreve o pedido come&ccedil;ando pelo abridor entre par&ecirc;nteses. Sem gabarito '
    'na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    24, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('Would you mind to send me the two clauses?',
      'Would you mind sending me the two clauses?'),
     ('Could you to sign it before Friday?', 'Could you sign it before Friday?'),
     ('I want that you copy your colleague.', 'Could you copy your colleague?'),
     ('May you send me the file this afternoon?',
      'Could you send me the file this afternoon?')]))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; a Priya. Diga sim, mas s&oacute; se '
    'as tr&ecirc;s partes aparecerem. Se ele pular o aviso ou a sa&iacute;da, responda com '
    'sil&ecirc;ncio e espere que ele complete.',
    'Role-Play 1 &mdash; Guided', 'The Signature Before', 'Friday',
    'Situation',
    'Ask a supplier you barely know to sign an amendment two days early. Three sentences: the '
    'heads-up, the request with the deadline inside it, and the way out.',
    ['a quick heads-up', 'Could you', 'before Friday', 'if that is impossible',
     'when it is possible']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 2 &mdash; semi-livre (4 min): agora INVERTA. Voc&ecirc; pede a ELE que apresente '
    'ao board na sexta, e ele est&aacute; sem tempo. Ele tem de dizer n&atilde;o sem fechar a '
    'porta. Insista uma vez: it really has to be you.',
    'Role-Play 2 &mdash; Semi-Free', 'Saying No Without', 'Closing the Door',
    'Situation',
    'Somebody asks you for something you genuinely cannot do this week. Say no, give one reason, '
    'and offer one alternative with a date. Do not apologize twice.',
    ['I am afraid', 'I am swamped', 'could we', 'instead']))

S.append(L.s_roleplay(
    27, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa. Cronometre noventa segundos e conte quantas portas de sa&iacute;da ele deixou. '
    'Diga o n&uacute;mero no fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'One conversation, both directions. Ask for an exception you really need at work, hear a '
    'request back, and either accept it or refuse it with an alternative. Finish by agreeing on '
    'who does what and by when. Ninety seconds, no notes.',
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
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco frases do pr&oacute;ximo e-mail '
    'dif&iacute;cil dele.',
    'Say It with', 'Confidence',
    ['May I ask you for a favor before we start?',
     'Could you sign it off before Friday?',
     'Would you mind sending me only the two clauses that changed?',
     'If Friday is impossible, could you tell me when it is?',
     'I am afraid I cannot this week, but I could on Monday.']))

S.append(L.s_checklist(
    30,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 10 e o primeiro bloco de dez aulas.',
    10,
    ['I can ask for something the other person does not have to give.',
     'I build a request in three parts: heads-up, request with a deadline, way out.',
     'I use May I for permission and Could you for an action.',
     'I put the -ing after Would you mind, and never to after a modal.',
     'I know the words: favor, heads-up, to chase, workaround, to sign off, reminder, to be '
     'swamped, bandwidth.']))

S.append(L.s_badge(
    31,
    'Encerramento (2 min): diga: Lesson 10 complete, Felipe &mdash; ten lessons done. Homework '
    'ORALMENTE, nunca escrito na tela: escrever de verdade um e-mail de quatro linhas pedindo '
    'algo real esta semana, ler em voz alta, gravar e mandar no WhatsApp. Pr&oacute;xima aula: '
    'Rules and Policies.',
    10, 'Getting What You Need Politely',
    'Ten lessons, Felipe. Today you asked for something nobody owed you, and you left the door '
    'open.',
    'Rules and Policies'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Getting What You Need Politely -- Requests and Permission',
    'short_title': 'Getting What You Need Politely',
    'menu_desc': ('Reading lesson: the email everybody writes twice a week and almost nobody '
                  'writes well, and the four ways to ask for the same thing'),
    'grammar_point': 'modals of request and permission',
    'characters': {'felipe': 'arthur', 'priya': 'indian_f'},
    'phases': ['The Email Nobody Writes Well', 'Your Words', 'Read the Email', 'Four Doors',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1596526131083-e8c633c948d2?w=600&q=80',
    'desc': ('The words of asking and being asked: favor, heads-up, to chase, workaround, to '
             'sign off, reminder, to be swamped, bandwidth. Structure: can, could, may and '
             'would you mind, and what each one really costs. Mission: ask for an exception, '
             'and refuse one, without closing any doors.'),
    'context_paras': [
        'Here is the whole email. <strong>May I</strong> ask you for a favor before we start? '
        'A quick heads-up: our board pack closes on Wednesday at noon. <strong>Could you</strong> '
        'sign off amendment 2 before Friday? <strong>Would you mind</strong> sending me only the '
        'two clauses that changed, so that nobody has to read forty pages? And if Friday is '
        'impossible, <strong>could you</strong> tell me when it is?',
        'Four requests, four different doors. <em>May I</em> asks for permission and it is about '
        'me. <em>Could you</em> asks for an action and it works with anybody, anywhere. '
        '<em>Would you mind</em> is the most polite of all, and it takes the <strong>-ing</strong> '
        'form: <em>would you mind <strong>sending</strong></em>, never <em>to send</em>. And '
        'after can, could and may the verb comes bare: <em>could you <strong>sign</strong></em>, '
        'never <em>could you to sign</em>. English also has no <em>I want that you...</em>. The '
        'want disappears, and the question does the work.'],
    'context_quiz': [
        ('Why is it <em>Would you mind sending</em> and not <em>Would you mind to send</em>?',
         [('Because send is irregular.', False),
          ('Because mind is always followed by the -ing form.', True),
          ('Because the request is about the future.', False)]),
        ('What is the difference between <em>May I</em> and <em>Could you</em> in this email?',
         [('May I is more formal, but they mean the same thing.', False),
          ('May I asks for permission and is about the writer. Could you asks the other person '
           'to do something.', True),
          ('May I is only used in writing.', False)]),
        ('Why does the last sentence exist at all?',
         [('To make the email longer and therefore more polite.', False),
          ('To leave the reader a way out: they can say later instead of no.', True),
          ('To remind the reader of the deadline a second time.', False)]),
    ],
    'tip_title': 'Modals of Request and Permission',
    'tip_intro': ('Four ways to ask for the same thing, and they are not interchangeable. The '
                  'temperature changes, and so does what comes after the modal.'),
    'tip_rows': [
        ['Can you...?', 'Fast and neutral, with people you work with every day.',
         '<strong>Can you</strong> send me the file?'],
        ['Could you...?', 'The safe default at work, with anybody, in any country.',
         '<strong>Could you</strong> sign it before Friday?'],
        ['May I...?', 'Permission, and it is about you, not about them. Formal.',
         '<strong>May I</strong> use your name in the email?'],
        ['Would you mind + -ing?',
         'The most polite. Careful: <em>yes</em> means the person does mind, so it is a no.',
         '<strong>Would you mind signing</strong> it today?'],
        ['No <em>to</em> after a modal',
         'could you <strong>send</strong>, may I <strong>ask</strong>, can you <strong>copy</strong>. '
         'Never <em>could you to send</em>.'],
        ['Saying no with a door open',
         '<em>I am afraid I cannot this week</em> &middot; <em>I would rather...</em> &middot; '
         '<em>Could we do it on Monday instead?</em>'],
    ],
    'tip_note': ('The modal is half the job. The other half is the shape of the message: one '
                 'sentence of warning, one request with the deadline inside it, and one way out. '
                 'With those three, even a plain can sounds polite.'),
    'blanks': [
        ('', 'May', 'Hint: three letters. Permission, and it is about you.',
         'May I ask you for a favor before we start?',
         ' I ask you for a favor before we start?'),
        ('', 'Could', 'Hint: five letters. The safe default for asking somebody to do something.',
         'Could you sign off the amendment before Friday?',
         ' you sign off the amendment before Friday?'),
        ('Would you mind ', 'sending', 'Hint: after mind the verb takes -ing.',
         'Would you mind sending me only the two clauses?',
         ' me only the two clauses?'),
        ('Could you give my team a ', 'heads-up',
         'Hint: one word with a hyphen. A warning in advance.',
         'Could you give my team a heads-up when your volumes change?',
         ' when your volumes change?'),
        ('I am ', 'swamped', 'Hint: one word. Far too much work at the same time.',
         'I am swamped this week and I have no bandwidth before Thursday.',
         ' this week and I have no bandwidth before Thursday.'),
        ('I am afraid I ', 'cannot', 'Hint: one word. The polite refusal starts here.',
         'I am afraid I cannot this week, but I could on Monday.',
         ' this week, but I could on Monday.'),
    ],
    'order_title': 'Put the Conversation in Order',
    'order_intro': 'Listen first, then put the five parts of the conversation in the order you '
                   'hear them.',
    'order': [
        (2, 'Then he asks her to sign off the amendment before Friday, and explains why.'),
        (4, 'Next, she asks for something in return: a heads-up whenever his volumes change.'),
        (1, 'First, Felipe asks whether he may ask Priya for a favor.'),
        (5, 'Finally, she says that if she is swamped on Tuesday she will sign on Monday evening '
            'instead.'),
        (3, 'After that, Priya asks him to send only the two clauses that changed.'),
    ],
    'speech': [
        'May I ask you for a favor before we start?',
        'Could you sign it off before Friday?',
        'Would you mind sending me only the two clauses that changed?',
        'If Friday is impossible, could you tell me when it is?',
        'I am afraid I cannot this week, but I could on Monday.',
    ],
    'quiz_intro': 'You need something from somebody who does not owe it to you. Choose the best '
                  'thing to say.',
    'quiz': [
        ('You want a supplier to sign a document two days early. You say:',
         [('I want that you sign it before Friday.', False),
          ('Could you sign it off before Friday? Our board pack closes on Wednesday.', True),
          ('You need to sign it before Friday.', False)]),
        ('You want permission to mention somebody name in an email. You say:',
         [('Could you that I use your name?', False),
          ('May I use your name in the email?', True),
          ('Would you mind that I use your name?', False)]),
        ('You want to be as polite as possible about a signature today. You say:',
         [('Would you mind to sign it today?', False),
          ('Would you mind signing it today?', True),
          ('Would you mind you sign it today?', False)]),
        ('Somebody asks you for something you cannot do this week. The best answer is:',
         [('No, I am very busy, sorry, sorry.', False),
          ('I am afraid I cannot this week. Could we do it on Monday instead?', True),
          ('Maybe. I will see. It is difficult.', False)]),
    ],
    'think': ('Think about one real thing you need from somebody this month, that they are not '
              'obliged to give you. Record about ninety seconds. Build the request out loud in '
              'three parts: one sentence of heads-up, one sentence with the request and the '
              'deadline inside it, and one sentence that leaves them a way out. Then imagine '
              'they say no, and answer that. Then turn it around: refuse a request somebody has '
              'made to you, give one reason and offer one alternative with a date. Use at least '
              'four words from this lesson. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'modals', 'Grammar Video',
         'Uses of can and cannot: ability, possibility, requests and permission',
         'A clear breakdown of what can really does in English, including the two jobs it has in '
         'a request. Connection to Lesson 10: it separates the modal you already use from the '
         'ones you should be using at work.',
         'Tip: for every example, decide out loud whether it is ability, permission or a '
         'request. Then check.',
         'https://www.youtube.com/watch?v=jkNt2LT2s-o', 'Watch on YouTube'),
        ('youtube', 'polite', 'Grammar Video',
         '"How to be polite in English" -- Ask BBC Learning English',
         'Short and direct: what makes English sound polite, and why length is not the answer. '
         'Connection to Lesson 10: it says in five minutes what the reading text argues, from a '
         'British point of view.',
         'Tip: notice how often the politeness comes from the structure, not from extra words.',
         'https://www.youtube.com/watch?v=3NM72kTE2oQ', 'Watch on YouTube'),
        ('video', 'email', 'Video Lesson',
         'English for emails: formal and informal language -- British Council',
         'The difference between the email you send a colleague and the one you send a supplier '
         'you have never met. Connection to Lesson 10: your four line email lives exactly on '
         'that border.',
         'Tip: take one email you sent this week and rewrite it in four lines using the three '
         'parts from the lesson. Then compare the two.',
         'https://www.youtube.com/watch?v=3-QoPcJHQws', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
