#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 3 do Felipe de Araujo Dias — The Supplier Call (perguntas indiretas).
Modelo de FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays.
Gera slides.html / preclass.html / complementary.html / config.json.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 3

IMG_TITLE = 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_CALL = 'https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Lead time', 'the number of days between an order and the delivery',
     'The lead time is forty days, so nothing arrives before March.'),
    ('Purchase order', 'the official document that says what a company buys and when',
     'The purchase order still shows the old date.'),
    ('Batch', 'a group of products made or delivered together at the same time',
     'The first batch leaves the factory on the eighteenth.'),
    ('Shipment', 'the goods that travel together in one delivery',
     'The shipment arrives two weeks after the store opening.'),
    ('To delay', 'to make something happen later than planned',
     'A busy port delays every container by three days.'),
    ('To confirm', 'to say officially that something is certain',
     'Please confirm the new date in writing.'),
    ('Quote', 'a written price for an order or a job',
     'The quote does not include freight to Santos.'),
    ('To push back', 'to ask politely for a later date, or to say no without closing the door',
     'If the fabric is late, we push back the delivery to April.'),
]

VOCAB_WORDS = [w for w, _, _ in VOCAB]

# ---------------------------------------------------------------- IN CLASS blocks

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Lead time', 'f'], ['2', 'Purchase order', 'c'], ['3', 'Batch', 'a'],
                   ['4', 'Shipment', 'g'], ['5', 'To delay', 'b'], ['6', 'To confirm', 'h'],
                   ['7', 'Quote', 'd'], ['8', 'To push back', 'e']],
         'defs': [['a', 'A group of products made or delivered together at the same time'],
                  ['b', 'To make something happen later than planned'],
                  ['c', 'The official document that says what a company buys and when'],
                  ['d', 'A written price for an order or a job'],
                  ['e', 'To ask politely for a later date, or to say no without closing the door'],
                  ['f', 'The number of days between an order and the delivery'],
                  ['g', 'The goods that travel together in one delivery'],
                  ['h', 'To say officially that something is certain']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a quote is a price, a purchase order is a promise. '
                  'You ask for the first and you sign the second.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['We asked three factories for a ', ['1'],
                   ' and the cheapest one had the longest ', ['2'],
                   '. I signed the ', ['3'], ' on Monday. The first ', ['4'],
                   ' leaves in March, and the whole ', ['5'],
                   ' travels in one container. If the fabric arrives late, they ',
                   ['6'], ' everything by ten days, so I ', ['7'],
                   ' the delivery to April and ask them to ', ['8'],
                   ' the new date in writing.'],
         'bank': ['quote', 'lead time', 'purchase order', 'batch', 'shipment',
                  'delay', 'push back', 'confirm']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'You need three pieces of information from a supplier you have '
                           'never spoken to: the ship date, the price of freight and who signs '
                           'the change. Ask all three, and start each one differently.'],
            ['Scenario 2', 'A factory has just told you the lead time is fifteen days longer. '
                           'Ask why, ask what is possible, and ask for it in writing. Do not '
                           'accuse anybody.'],
            ['Scenario 3', 'You have to push the delivery back by three weeks and the supplier '
                           'will not like it. Say it politely, give one reason, and finish with '
                           'a question.'],
        ]},
        {'kind': 'rephrase', 'title': 'Say each question again, starting with the words in brackets.',
         'items': [['When does the first batch leave? (Could you tell me...)', 'polite'],
                   ['Is the quote still valid? (Do you know...)', 'polite'],
                   ['Who signs the purchase order? (Would you mind telling me...)', 'polite'],
                   ['Can you confirm the shipment today? (I was wondering...)', 'polite']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'A new supplier answers the phone. You need the ship date of the '
                          'first batch, and you have never spoken to this person before.',
             'tips': ['Open with Could you tell me, not with a bare question.',
                      'After when, the sentence goes back to normal order: subject, then verb.']},
            {'situation': 'You are not sure whether the price on the quote includes freight. '
                          'Ask, without suggesting the supplier hid it.',
             'tips': ['A yes-or-no question needs if or whether inside.',
                      'Do you know if the quote includes freight?']},
            {'situation': 'The purchase order has the wrong date. Ask who can change it and '
                          'how long it takes.',
             'tips': ['Who is already the subject, so nothing moves after it.',
                      'Ask the second question in the same breath, not in a new email.']},
            {'situation': 'Your manager is on the call and asks you to check whether the '
                          'factory can deliver two weeks earlier. Ask the supplier.',
             'tips': ['I was wondering whether you could... is the softest opener you have.',
                      'Give the reason before the question, not after.']},
            {'situation': 'The supplier gives you a date you cannot accept. Push back without '
                          'saying no.',
             'tips': ['Name the problem, then ask what is possible.',
                      'That date does not work for us. Could you tell me what is possible?']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['Could you tell me when the first batch leaves?',
                  'Do you know if the quote is still valid?',
                  'Would you mind telling me who signs the purchase order?',
                  'I was wondering whether you can confirm the shipment today.'],
         'note': ('The polite opener carries the question. Everything after it goes back to '
                  'normal order: subject, then verb, and no does or do.')},
    ],
}

LISTENINGS = [
    {'file': 'a3_listening1.mp3', 'voice': 'ellen',
     'text': ('Felipe, this is Rachel from logistics. Two things before your call. First, the '
              'purchase order for the spring batch is signed, but the quote we received does '
              'not include freight, so please ask them to confirm that in writing. Second, the '
              'lead time changed. It was forty days and now it is fifty-five, which means the '
              'shipment arrives after the store opening. I would not accept that date. If you '
              'have to push back, push back today, because the factory closes for a holiday on '
              'Friday. Call me when you have five minutes.')},
    {'file': 'a3_listening2.mp3', 'voice': 'indian_f',
     'text': ('Felipe, this is Priya. I promised you an answer today, so here it is. The fabric '
              'arrived this morning, which means the first batch leaves on the eighteenth, as '
              'we discussed. I have corrected the purchase order and the new date is already in '
              'your inbox. Two things you did not ask about. The freight quote is ready and it '
              'is nine per cent higher than last season, because the port is busy. And the '
              'second batch may need three extra days. If you want to push back the delivery to '
              'April, tell me before Thursday and nobody loses money. Speak soon.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l3]', 'file': 'pc3_order_call.mp3', 'voice': 'arthur',
     'text': ('First, Felipe thanks Priya for taking the call and says he has three questions. '
              'Then he asks when the first batch leaves the factory. After that, he asks whether '
              'the quote includes freight. Next, he asks who he should write to about it. '
              'Finally, he asks how many days they lose if the fabric is late.')},
]

# ---------------------------------------------------------------- slides

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada &mdash; voc&ecirc;s j&aacute; se '
    'cumprimentaram ao vivo. Este slide s&oacute; abre a tela e d&aacute; o tema. V&aacute; '
    'direto ao slide 2.',
    'Chapter 1: The Awkward Question', 'The Supplier', 'Call',
    'Getting the information you need without sounding rude', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 2 (3 min): ele acabou de aprender a separar rotina de '
    'agora. Fa&ccedil;a a ponte pedindo que use pelo menos tr&ecirc;s palavras da aula 2 '
    '(deadline, workload, to follow up, on site). Depois v&aacute; ao prompt em laranja e '
    'DEIXE ELE PERGUNTAR. Anote em sil&ecirc;ncio toda pergunta que sair na ordem errada '
    '&mdash; a aula existe para isso.',
    'You Can Describe It.', 'Now Ask About It',
    'Last time you said what you do and what you are doing this week. Today somebody on the '
    'other side of the world has the information, and the only way to get it is to ask. In '
    'Portuguese you soften a question with your voice. English does it with words.',
    'Ask me three things about my job. Any three. Do not think about grammar yet.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as tr&ecirc;s miss&otilde;es em tom de parceiro. Avise que no '
    'fim ele conduz sozinho uma call de fornecedor. Passe ao pr&oacute;ximo.',
    ['Eight words that a supply call cannot happen without.',
     'Turn a direct question into a polite one, and keep the word order right.',
     'Run a call with a supplier who is fifteen days late, without losing the relationship.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): diga que a pista em ingl&ecirc;s vem primeiro, ele '
    'tenta a palavra, e s&oacute; ent&atilde;o clique. N&atilde;o revele antes.',
    'Chapter 2: Your Words', 'The Words on the', 'Order',
    '8 words that live inside every supply conversation', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. Toque o '
    '&aacute;udio e pe&ccedil;a repeti&ccedil;&atilde;o. CCQ para lead time: Is the lead time '
    'the day of delivery, or the number of days? (The number of days.) CCQ para batch: If I '
    'order twelve thousand units in three batches, how many arrive together? (Four thousand.)',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para to confirm: If I say maybe, did '
    'I confirm? (No.) CCQ para to push back: Does push back mean to refuse? (No &mdash; it '
    'means to ask for a later date.) Pron&uacute;ncia: em purchase o ch soletra tch, e o final '
    '&eacute; fraco (PUR-chess).',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Clicar num par feito desfaz. Use o vocab-note no fim como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): o banco de palavras est&aacute; na tela. Ele '
    'escolhe e L&Ecirc; O PAR&Aacute;GRAFO INTEIRO em voz alta &mdash; a frase completa &eacute; '
    'o exerc&iacute;cio, n&atilde;o a palavra solta.',
    'Use the Words', 'One Order, from', 'Quote to Container',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga que ele j&aacute; sabe fazer '
    'perguntas &mdash; o problema &eacute; que a pergunta direta soa dura ao telefone com '
    'quem ele n&atilde;o conhece. Passe ao pr&oacute;ximo.',
    'Chapter 3: Softer, Not Weaker', 'The Same Question,', 'Two Doors',
    'How English makes a question polite without making it weak', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: The '
    'words after Could you tell me look like a statement, not a question. What happened to the '
    'word order? S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In Could you tell me when it '
    'ships, where is the question mark? (No fim da frase inteira &mdash; a pergunta &eacute; a '
    'primeira parte.)',
    'indirect questions',
    [('"<span class="accent" style="font-weight:700">Could you tell me</span> when the shipment leaves?"',
      'Could you tell me when the shipment leaves?'),
     ('"<span class="accent" style="font-weight:700">Do you know</span> if the quote includes freight?"',
      'Do you know if the quote includes freight?'),
     ('"<span class="accent" style="font-weight:700">I was wondering</span> whether you could confirm the date."',
      'I was wondering whether you could confirm the date.'),
     ('"<span class="accent" style="font-weight:700">Would you mind telling me</span> who signs the purchase order?"',
      'Would you mind telling me who signs the purchase order?')],
    'rule3',
    ['Direct question', 'Indirect question', 'What changes'],
    [['When does it ship?', 'Could you tell me when it ships?',
      'No does. The verb keeps the -s.'],
     ['Is the quote final?', 'Do you know if the quote is final?',
      'Add if or whether. Subject before verb.'],
     ['Who signs this?', 'Would you mind telling me who signs this?',
      'Who is already the subject, so nothing moves.'],
     ['Can you deliver in March?', 'I was wondering whether you can deliver in March.',
      'A statement, so no question mark.']],
    ('The polite opener carries the question. Everything after it goes back to normal order: '
     'subject, then verb.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica '
    'para comparar. Toggle: clicar de novo fecha. Se sair sem hesitar nas quatro, siga r&aacute;pido.',
    'Grammar Practice', 'Open the', 'Same Door Politely',
    'Say the full question, then click to compare',
    [('When does the second batch leave? (Could you tell me...)',
      'Could you tell me when the second batch leaves?'),
     ('Is the lead time still forty days? (Do you know...)',
      'Do you know if the lead time is still forty days?'),
     ('Who confirmed the purchase order? (I was wondering...)',
      'I was wondering who confirmed the purchase order.'),
     ('Can you send the quote today? (Would you mind telling me...)',
      'Would you mind telling me whether you can send the quote today?')]))

S.append(L.s_mistake(
    12, 3,
    'Common mistake (3 min): este &eacute; O erro do brasileiro em call de fornecedor &mdash; a '
    'ordem da pergunta direta sobrevive dentro da indireta. Pe&ccedil;a que ele leia as tr&ecirc;s '
    'vers&otilde;es CERTAS em voz alta, duas vezes cada, batendo o dedo na mesa no sujeito.',
    [('Could you tell me when does the shipment leave?',
      'Could you tell me when the shipment leaves?'),
     ('Do you know where is the factory?',
      'Do you know where the factory is?'),
     ('I was wondering that you can confirm the date.',
      'I was wondering whether you can confirm the date.')],
    ('Only the first part is a question. After when, where, who, if or whether, the sentence '
     'goes back to normal order and the auxiliary disappears.')))

S.append(L.s_listening(
    13, 3,
    'Listening 1 (5 min): ingl&ecirc;s americano, refer&ecirc;ncia. LEIA AS PERGUNTAS EM VOZ '
    'ALTA COM ELE ANTES de tocar &mdash; elas dizem o que procurar. O &aacute;udio tem dois '
    'n&uacute;meros e um prazo; &eacute; onde ele mais perde informa&ccedil;&atilde;o na vida '
    'real. Toque duas vezes. 0.75x s&oacute; se ele pedir.',
    1, 'The Voicemail from', 'Logistics',
    'A colleague leaves you a message before your supplier call. Sound first, no text.',
    'a3_listening1.mp3', SLUG,
    [('What is missing from the quote?',
      'Freight. Rachel wants the supplier to confirm that in writing.'),
     ('How did the lead time change?', 'It went from forty days to fifty-five.'),
     ('Why does Rachel say today and not tomorrow?',
      'Because the factory closes for a holiday on Friday.')]))

S.append(L.s_chapter(
    14, 4,
    'Transi&ccedil;&atilde;o di&aacute;logo (1 min): diga: Now the call itself. You are you. '
    'Priya is the supplier, in India. Passe ao pr&oacute;ximo.',
    'Chapter 4: The Call', 'Fifteen Days', 'Late',
    'A video call with the supplier who has to move a date', IMG_CALL))

S.append(L.s_dialogue(
    15, 4,
    'Di&aacute;logo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, pe&ccedil;a que '
    'ELE fale primeiro, com o texto tapado, e s&oacute; depois toque o &aacute;udio para '
    'comparar. Nas falas da Priya, toque o &aacute;udio uma vez e pergunte o que ela disse. '
    'Ela tem sotaque indiano de prop&oacute;sito: metade dos fornecedores dele fala assim.',
    'The Call That Moves', 'a Date',
    [('felipe', 'F', 'arthur',
      'Good afternoon, Priya. Thank you for taking the call. I have three questions about the '
      'spring order.'),
     ('priya', 'P', 'indian_f', 'Of course, Felipe. Go ahead.'),
     ('felipe', 'F', 'arthur',
      'Could you tell me when the first <span class="vocab-highlight">batch</span> leaves the factory?'),
     ('priya', 'P', 'indian_f',
      'The eighteenth of March, if the fabric arrives on time.'),
     ('felipe', 'F', 'arthur',
      'I see. And do you know if that date is already in the '
      '<span class="vocab-highlight">purchase order</span>?'),
     ('priya', 'P', 'indian_f',
      'It is not. The order still says the fifth of March. I will correct it today.'),
     ('felipe', 'F', 'arthur',
      'Thank you. I was wondering whether the <span class="vocab-highlight">quote</span> '
      'includes freight to Santos.'),
     ('priya', 'P', 'indian_f',
      'It does not, I am afraid. Freight is quoted separately, and the port is busy this month.'),
     ('felipe', 'F', 'arthur',
      'That is useful to know. Would you mind telling me who I should write to about it?'),
     ('priya', 'P', 'indian_f',
      'Write to me. I <span class="vocab-highlight">confirm</span> every change in writing, so '
      'nothing is lost.'),
     ('felipe', 'F', 'arthur',
      'Perfect. One last thing. If the fabric is late, how many days do we lose?'),
     ('priya', 'P', 'indian_f',
      'Ten, normally. If it goes past ten, I call you before you have to ask.')]))

S.append(L.s_comprehension(
    16, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre a PRIYA, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar. Se errar, volte ao di&aacute;logo e toque a fala.',
    'Did You Catch It?', 'About', 'Priya',
    [('When does the first batch leave, and what has to happen first?',
      'The eighteenth of March, if the fabric arrives on time.'),
     ('What is wrong with the purchase order?',
      'It still says the fifth of March. Priya will correct it today.'),
     ('What does Priya promise about changes?',
      'She confirms every change in writing, so nothing is lost.')]))

S.append(L.s_artifact(
    17, 4,
    'Artefato (4 min): documento real, com o nome dele. Pe&ccedil;a que ele LEIA o cart&atilde;o '
    'em voz alta e depois responda as tr&ecirc;s perguntas. Na terceira, exija a pergunta '
    'INDIRETA completa, n&atilde;o s&oacute; a informa&ccedil;&atilde;o.',
    'Real Document', 'The Purchase', 'Order',
    'RIACHUELO &mdash; PURCHASE ORDER', 'PO-2026-0418',
    [('Supplier', 'Meridian Textiles, Tiruppur'),
     ('Buyer', 'Felipe de Ara&uacute;jo Dias &mdash; Supply Chain'),
     ('Product', 'Spring collection, batch 1 of 3'),
     ('Quantity', '12,000 units'),
     ('Lead time', '55 days from confirmation'),
     ('Ship date', 'March 5'),
     ('Freight', 'Not included &mdash; quoted separately'),
     ('Status', 'Waiting for written confirmation')],
    [('The ship date on this document is wrong. What should it say?',
      'March 18. Priya said she would correct it the same day.'),
     ('The lead time is counted from which day?',
      'From the confirmation, not from the day the order was written.'),
     ('Ask about the freight, politely, in one sentence.',
      'Could you tell me how much the freight to Santos is?')]))

S.append(L.s_listening(
    18, 4,
    'Listening 2 (5 min): sotaque indiano, a mesma Priya do di&aacute;logo. LEIA AS PERGUNTAS '
    'COM ELE ANTES do play. Ela d&aacute; duas informa&ccedil;&otilde;es que ele n&atilde;o '
    'pediu &mdash; pergunte no fim quais foram. Toque duas vezes.',
    2, 'Priya Calls', 'Back',
    'The supplier answers all three questions in one message. Sound first, no text.',
    'a3_listening2.mp3', SLUG,
    [('What did Priya correct, and where is it now?',
      'The purchase order. The new date is already in his inbox.'),
     ('Why is the freight quote higher than last season?',
      'Because the port is busy. It is nine per cent higher.'),
     ('What is the last day to change the delivery to April?',
      'Thursday. After that, somebody loses money.')]))

S.append(L.s_blocks(
    19, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez. Ele responde EM VOZ ALTA antes de '
    'abrir as Tips &mdash; as Tips s&atilde;o apoio, nunca gabarito. Exija a pergunta inteira, '
    'com o abridor. Se ele soltar a pergunta direta, n&atilde;o corrija: repita o abridor e '
    'espere.',
    'Chapter 5: Real Talk', 'Ask It on the', 'Spot', ['quickfire'],
    'Read each situation. Ask out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    20, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you run the call. Three rounds, '
    'and each one gives you less help. Passe ao pr&oacute;ximo.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    21, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija tr&ecirc;s perguntas completas, '
    'n&atilde;o uma. No rephrase, ele repete a pergunta come&ccedil;ando pelo abridor entre '
    'par&ecirc;nteses. Sem gabarito na tela &mdash; o answer key vem tr&ecirc;s slides adiante.',
    'Say It Yourself', 'Three Situations,', 'Full Questions', ['practice']))

S.append(L.s_error(
    22, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM '
    'VOZ ALTA antes de clicar. Score no topo. Clicar de novo fecha.',
    [('Could you tell me when does the container arrive?',
      'Could you tell me when the container arrives?'),
     ('Do you know if is the quote final?', 'Do you know if the quote is final?'),
     ('I was wondering that you could push back the date.',
      'I was wondering whether you could push back the date.'),
     ('Would you mind telling me who does sign the purchase order?',
      'Would you mind telling me who signs the purchase order?')]))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; a Priya. Responda curto e deixe '
    'buracos de prop&oacute;sito, para ele ter de perguntar de novo. Corrija s&oacute; a ordem '
    'das palavras dentro da pergunta indireta; o resto anote.',
    'Role-Play 1 &mdash; Guided', 'The First', 'Call',
    'Situation',
    'You are calling a supplier for the first time. Get three pieces of information: the ship '
    'date, whether freight is included, and who confirms changes. Use a different opener for '
    'each question.',
    ['Could you tell me', 'Do you know if', 'I was wondering whether', 'ship date',
     'freight', 'in writing']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 2 &mdash; semi-livre (4 min): menos apoio. Voc&ecirc; &eacute; um fornecedor que '
    'atrasou e est&aacute; na defensiva. Interrompa uma vez com Sorry, could you repeat that? '
    'para for&ccedil;ar reformula&ccedil;&atilde;o.',
    'Role-Play 2 &mdash; Semi-Free', 'The Late', 'Shipment',
    'Situation',
    'The factory is fifteen days late and your stores open in April. Find out why, find out '
    'what is possible, and ask for the new date in writing. Do not accuse anybody.',
    ['fifteen days', 'what is possible', 'in writing']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa, nem para corrigir. Cronometre noventa segundos e anote os erros para a '
    'pr&oacute;xima aula. CELEBRE no fim, independentemente do resultado.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'You have to push the delivery back by three weeks and the supplier will lose money. Open '
    'the call, explain the situation, ask two questions, offer one thing in return, and agree '
    'on what happens next. Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    26, 6,
    'Answer key (2 min): o accordion nasce fechado. S&oacute; abra depois que ele tentou as '
    'quatro do rephrase. &Eacute; controle do professor: clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    27,
    'Survival lines (3 min): leia cada frase, toque o &aacute;udio, pe&ccedil;a que ele repita '
    'olhando para a c&acirc;mera. S&atilde;o as cinco que ele leva para a pr&oacute;xima call '
    'de verdade.',
    'Say It with', 'Confidence',
    ['Could you tell me when the shipment leaves?',
     'Do you know if the quote includes freight?',
     'I was wondering whether we could move the date.',
     'Would you mind confirming that in writing?',
     'Sorry, I did not catch that. Could you say it again?']))

S.append(L.s_checklist(
    28,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz '
    'alta. Os 5 checks marcados fecham a aula 3 e liberam o terceiro stamp do passaporte.',
    3,
    ['I can ask a question politely without sounding weak.',
     'I keep the normal word order after when, where, who, if and whether.',
     'I never put does or do inside an indirect question.',
     'I can push back on a date without saying no.',
     'I know the words: lead time, purchase order, batch, shipment, delay, confirm, quote, '
     'push back.']))

S.append(L.s_badge(
    29,
    'Encerramento (2 min): diga: Lesson 3 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar tr&ecirc;s perguntas indiretas sobre um pedido real da semana dele e '
    'mandar no WhatsApp antes da pr&oacute;xima aula. Pr&oacute;xima aula: The Trip to Chicago.',
    3, 'The Supplier Call',
    'You asked eight questions today and none of them sounded rude, Felipe.',
    'The Trip to Chicago'))

SLIDES = '\n'.join(S)

# ---------------------------------------------------------------- spec

SPEC = {
    'n': N,
    'title': 'The Supplier Call -- Asking Without Sounding Rude',
    'short_title': 'The Supplier Call',
    'menu_desc': ('Speaking lesson: a call with a supplier who is fifteen days late, and the '
                  'polite question that gets a straight answer'),
    'grammar_point': 'indirect questions',
    'characters': {'felipe': 'arthur', 'priya': 'indian_f'},
    'phases': ['The Awkward Question', 'Your Words', 'Softer, Not Weaker', 'The Call',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&q=80',
    'desc': ('The words a supply call cannot happen without: lead time, purchase order, batch, '
             'shipment, to delay, to confirm, quote, to push back. Structure: direct and '
             'indirect questions, and the word order that changes inside them. Mission: get '
             'three pieces of information from a supplier without sounding rude.'),
    'context_paras': [
        'A first call with a supplier is a list of questions, and the list is always the same. '
        '<strong>Could you tell me</strong> when the first <strong>batch</strong> leaves? '
        '<strong>Do you know if</strong> the <strong>quote</strong> includes freight? '
        '<strong>Would you mind telling me</strong> who signs the change? Three questions, '
        'three openers, and the same information you would get with a direct question.',
        'The difference is what happens after the opener. A direct question turns the sentence '
        'around: <em>When does it ship?</em> An indirect question does not. Once you have said '
        '<strong>Could you tell me</strong>, the rest goes back to normal order: '
        '<strong>when it ships</strong>, and the <em>does</em> disappears. For a yes-or-no '
        'question you need <strong>if</strong> or <strong>whether</strong>: <em>Do you know '
        '<strong>whether</strong> the shipment is on time?</em> The opener is doing all the '
        'work, so the rest of the sentence can relax.'],
    'context_quiz': [
        ('Why does the text say <em>Could you tell me when it ships</em> and not '
         '<em>when does it ship</em>?',
         [('Because ship is an irregular verb after could.', False),
          ('Because the question is already in the opener. After it, the sentence goes back to '
           'normal order and the auxiliary disappears.', True),
          ('Because the indirect question is always in the past.', False)]),
        ('When do you need <em>if</em> or <em>whether</em> inside the question?',
         [('When the answer is yes or no, and there is no question word like when or who.', True),
          ('Every time you start with Could you tell me.', False),
          ('Only when you are writing, never when you are speaking.', False)]),
        ('What is the effect of the opener on the person listening?',
         [('It makes the question longer, so it is less clear.', False),
          ('It gives them a second to prepare, and it asks permission before it asks for '
           'information.', True),
          ('It shows that you are not sure of your own question.', False)]),
    ],
    'tip_title': 'Direct and Indirect Questions',
    'tip_intro': ('One question, two doors. The direct door is fast and fine with people you '
                  'know. The indirect door is what you use on a first call.'),
    'tip_rows': [
        ['Could you tell me...', 'The most common opener at work. Works with when, where, who, '
         'how much and with if.', 'Could you tell me <strong>when the batch ships</strong>?'],
        ['Do you know if / whether...', 'Yes-or-no questions. Whether is slightly more formal.',
         'Do you know <strong>if the quote is final</strong>?'],
        ['I was wondering...', 'The softest opener. It is a statement, so it ends with a full '
         'stop.', 'I was wondering <strong>whether you could confirm the date</strong>.'],
        ['Would you mind telling me...', 'Very polite, useful when you are asking for something '
         'the person may not want to give.',
         'Would you mind telling me <strong>who signs this</strong>?'],
        ['The word order',
         'After the opener: subject, then verb. No <em>do</em>, no <em>does</em>, no '
         '<em>did</em>. <em>Could you tell me when it <strong>arrives</strong></em>, never '
         '<em>when does it arrive</em>.'],
        ['Who as subject',
         'When the question word is already the subject, nothing moves at all: <em>Who signs '
         'this?</em> becomes <em>...who signs this</em>.'],
    ],
    'tip_note': ('A habit that fixes almost everything: say the opener, take a breath, and then '
                 'say the rest as if it were a statement. If it still sounds like a question '
                 'inside, the word order is wrong.'),
    'blanks': [
        ('Could you tell me when the first batch ',
         'leaves', 'Hint: normal order after when, so the verb keeps the -s.',
         'Could you tell me when the first batch leaves?', '?'),
        ('Do you know ', 'if',
         'Hint: two letters. A yes-or-no question needs this word inside.',
         'Do you know if the quote includes freight?', ' the quote includes freight?'),
        ('The ', 'lead time', 'Hint: two words. The number of days between order and delivery.',
         'The lead time is fifty-five days, not forty.', ' is fifty-five days, not forty.'),
        ('I was wondering ', 'whether',
         'Hint: seven letters. The more formal twin of if.',
         'I was wondering whether you could confirm the date.',
         ' you could confirm the date.'),
        ('Would you mind telling me who ', 'signs',
         'Hint: who is already the subject, so the verb takes the -s and nothing moves.',
         'Would you mind telling me who signs the purchase order?',
         ' the purchase order?'),
        ('If the fabric is late, we have to ', 'push back',
         'Hint: two words. To ask politely for a later date.',
         'If the fabric is late, we have to push back the delivery.', ' the delivery.'),
    ],
    'order_title': 'Put the Call in Order',
    'order_intro': 'Listen first, then put the five parts of the call in the order you hear them.',
    'order': [
        (3, 'After that, he asks whether the quote includes freight.'),
        (1, 'First, Felipe thanks Priya for taking the call and says he has three questions.'),
        (5, 'Finally, he asks how many days they lose if the fabric is late.'),
        (2, 'Then he asks when the first batch leaves the factory.'),
        (4, 'Next, he asks who he should write to about it.'),
    ],
    'speech': [
        'Could you tell me when the shipment leaves?',
        'Do you know if the quote includes freight?',
        'I was wondering whether we could move the date.',
        'Would you mind confirming that in writing?',
        'Sorry, I did not catch that. Could you say it again?',
    ],
    'quiz_intro': 'You are on a call with a supplier. Choose the best thing to say.',
    'quiz': [
        ('It is your first call with this supplier and you need the ship date. You say:',
         [('Could you tell me when does the first batch ship?', False),
          ('Could you tell me when the first batch ships?', True),
          ('Tell me the ship date of the first batch.', False)]),
        ('You want to know whether freight is in the price, and you do not want to sound '
         'suspicious. You say:',
         [('Do you know if the quote includes freight?', True),
          ('Do you know does the quote include freight?', False),
          ('The quote includes freight or not?', False)]),
        ('The supplier gives you a date three weeks too late. The most useful answer is:',
         [('That is impossible. We need it earlier.', False),
          ('That date does not work for our opening. Could you tell me what is possible?', True),
          ('I was wondering that you can deliver earlier.', False)]),
        ('You did not understand the number the supplier just said. You say:',
         [('Repeat, please. I did not understand nothing.', False),
          ('Sorry, I did not catch that. Could you say it again?', True),
          ('What? Say again the number.', False)]),
    ],
    'think': ('Think about one real order you are following this week. Record about ninety '
              'seconds. Start by saying what the order is and where it comes from. Then ask '
              'four questions about it out loud, each one with a different opener: Could you '
              'tell me, Do you know if, I was wondering whether, and Would you mind telling me. '
              'Finish by saying what you would do if the supplier pushed the date back by two '
              'weeks. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"Indirect Questions" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on exactly the structure you practised today, with two British speakers '
         'and a short quiz at the end. Connection to Lesson 3: it drills the one thing that is '
         'hard to hear in your own speech, which is the word order after the opener.',
         'Tip: pause after every example and say it again out loud before they explain it.',
         'https://www.youtube.com/watch?v=CzoxIVPtPgI', 'Watch on YouTube'),
        ('video', 'polite', 'Video Lesson',
         '"Make polite requests" -- English at Work, BBC Learning English',
         'A short office story where somebody has to ask a colleague for something difficult. '
         'Connection to Lesson 3: the openers are the same ones you used on the call with '
         'Priya, in a situation where being direct would cost you the favour.',
         'Tip: write down every phrase that softens a request. You will need three of them on '
         'your next supplier call.',
         'https://www.youtube.com/watch?v=QWBwCoecvkM', 'Watch on YouTube'),
        ('podcast', 'talk', 'Talk',
         '"10 ways to have a better conversation" -- Celeste Headlee, TED',
         'Eleven minutes of American English at natural speed, about asking questions that '
         'actually get answers. Connection to Lesson 3: half of a supply call is not grammar, '
         'it is knowing which question to ask second.',
         'Tip: watch once without subtitles. Then watch again and count how many of her ten '
         'rules you already follow in Portuguese.',
         'https://www.youtube.com/watch?v=R1vskiVDwl4', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
