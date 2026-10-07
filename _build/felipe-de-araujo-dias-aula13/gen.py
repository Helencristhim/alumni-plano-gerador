#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 13 do Felipe de Araujo Dias — Numbers in a Results Meeting.
Quantificadores + contaveis e incontaveis. Modelo de FALA (aula IMPAR, REGRA 29).
Tema: apresentar o resultado mensal das quatro areas dele em voz alta.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 13

IMG_TITLE = 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_MEET = 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Revenue', 'the money a company receives from selling its products',
     'Revenue grew in September, but our costs grew faster.'),
    ('Margin', 'the difference between the selling price and the cost, often as a percentage',
     'A higher margin means more money stays in the company.'),
    ('Year-on-year', 'compared with the same period of the year before',
     'Shrinkage is down three percent year-on-year.'),
    ('Spending', 'the amount of money that is used on something',
     'We cut spending on outside cleaning by a fifth.'),
    ('Overtime', 'extra hours that people work after their normal working day',
     'We paid too much overtime in the last week of the month.'),
    ('Stock level', 'how much product you have in the warehouse at one moment',
     'Stock levels are higher than we planned for October.'),
    ('To drop', 'to go down, or to become less',
     'The number of incidents dropped to eleven this month.'),
    ('Slightly', 'a little, not very much',
     'Maintenance costs were slightly above the budget.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Revenue', 'e'], ['2', 'Margin', 'a'], ['3', 'Year-on-year', 'g'],
                   ['4', 'Spending', 'c'], ['5', 'Overtime', 'h'], ['6', 'Stock level', 'b'],
                   ['7', 'To drop', 'f'], ['8', 'Slightly', 'd']],
         'defs': [['a', 'The difference between the selling price and the cost, often as a '
                        'percentage'],
                  ['b', 'How much product you have in the warehouse at one moment'],
                  ['c', 'The amount of money that is used on something'],
                  ['d', 'A little, not very much'],
                  ['e', 'The money a company receives from selling its products'],
                  ['f', 'To go down, or to become less'],
                  ['g', 'Compared with the same period of the year before'],
                  ['h', 'Extra hours that people work after their normal working day']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: revenue is the money that comes in, and the margin is what '
                  'stays. A month can have more revenue and less margin at the same time.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Here are the September numbers. ', ['1', 'revenue'],
                   ' in the stores was up, but our ', ['2', 'margin'],
                   ' was a little lower, because costs grew too. Shrinkage is down three percent ',
                   ['3', 'year-on-year'], '. We reduced ', ['4', 'spending'],
                   ' on outside cleaning, but we paid a lot of ', ['5', 'overtime'],
                   ' in the last week. The ', ['6', 'stock level'],
                   's at the distribution center are high. The number of incidents continued to ',
                   ['7', 'drop'], ', and maintenance was only ', ['8', 'slightly'],
                   ' above the budget.'],
         'bank': ['revenue', 'margin', 'year-on-year', 'spending', 'overtime', 'stock level',
                  'drop', 'slightly']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Present last month in one of your areas: one number that went up, '
                           'one that dropped, and one that stayed the same. Use much, many or a '
                           'lot of in every sentence.'],
            ['Scenario 2', 'Your director asks why there was so much overtime. Explain how many '
                           'people, how many hours, and what you will do about it.'],
            ['Scenario 3', 'Talk about your city: is there much traffic, are there many parks, '
                           'is there enough public transport?'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each sentence again with the word the cue asks for.',
         'items': [['We had a small number of incidents.', 'a few'],
                   ['We did not spend a lot on cleaning.', 'much'],
                   ['There were not a lot of complaints.', 'many'],
                   ['We had a smaller number of breakdowns than in August.', 'fewer']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'Your director asks how much overtime you paid last month.',
             'tips': ['Overtime is uncountable: how much, a lot of, too much.',
                      'Give the number, then the reason.']},
            {'situation': 'Someone asks how many incidents there were in the stores.',
             'tips': ['Incidents are countable: how many, a few, fewer.',
                      'Compare with the month before.']},
            {'situation': 'Finance asks if there is any room in the budget for new lockers.',
             'tips': ['A little room, or very little room: the difference matters.',
                      'Say how much, then what you would need.']},
            {'situation': 'A colleague says the warehouse has too many pallets on the floor.',
             'tips': ['Too many pallets, too much stock.',
                      'Say what the stock level should be.']},
            {'situation': 'Present one good number and one bad number from your month, in two '
                          'sentences.',
             'tips': ['Good news first, then the problem.',
                      'Use dropped or slightly at least once.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['We had a few incidents.',
                  "We didn't spend much on cleaning.",
                  "There weren't many complaints.",
                  'We had fewer breakdowns than in August.'],
         'note': ('Countable things take many, a few and fewer. Uncountable things take much, a '
                  'little and less. A lot of works with both.')},
    ],
}

LISTENINGS = [
    {'file': 'a13_listening1.mp3', 'voice': 'ellen',
     'text': ("Felipe, it's Rachel from the controller's office. I have the September figures for "
              "your four areas before tomorrow's meeting. The good news first. Shrinkage dropped "
              "again: it's down three percent year-on-year, and there were only a few incidents "
              "in the stores, eleven in total. Maintenance was slightly above the budget, not "
              "much, about two percent. The bad news is overtime. We paid a lot of overtime in "
              "the last week, almost four hundred hours, and most of it was at the distribution "
              "center. Stock levels are high, and there isn't much space left for October. You "
              "will get questions about that.")},
    {'file': 'a13_listening2.mp3', 'voice': 'british_m',
     'text': ("Felipe, it's Graham. Good presentation this morning, and very clear numbers. A "
              "few things for next month. First, the board liked the shrinkage figure, but they "
              "want to see how many incidents were shoplifting and how many were internal. "
              "Second, the overtime. Four hundred hours is too much, and I'd like to know how "
              "many people it was. If it was only a few people, that's a different problem. "
              "And one small point. You said less incidents. With people and things you can "
              "count, it's fewer. Not a big deal, but the board notices that kind of thing.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l13]', 'file': 'pc13_order_results.mp3', 'voice': 'arthur',
     'text': ("First, Felipe says that revenue in the stores was up in September. Then he "
              "explains that the margin was slightly lower, because costs grew too. After that, "
              "he says there were only a few incidents, and fewer than in August. Next, Graham "
              "asks how much overtime they paid. Finally, Felipe admits it was too much, and "
              "promises a plan for October.")},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de FALA. Hoje ele apresenta o mês das '
    'quatro áreas dele em voz alta, como na reunião de resultado. Diga o tema e siga.',
    'Chapter 1: The Monthly Meeting', 'Numbers in a', 'Results Meeting',
    'Presenting a month of figures out loud, and answering the questions after', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 12 (3 min): na aula 12 ele comparou duas propostas com '
    'números. Hoje os números são dele. Peça que ele responda ao prompt e ESCUTE se ele diz '
    'less incidents ou how much people &mdash; são os erros do Detective. Não corrija ainda.',
    'You Compared Two Offers.', 'Now Present Your Month',
    'Last lesson the numbers belonged to two suppliers. This time they are yours, and somebody '
    'at the table will ask how much, how many and why. In English, the question changes '
    'depending on what you are counting.',
    'Give me three numbers from your last month: one good, one bad, one surprising.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as três missões. Diga que no fim ele vai apresentar um mês '
    'inteiro em noventa segundos. Passe ao próximo.',
    ['Eight words for money, hours and what goes up or down.',
     'Much or many, little or few, less or fewer: what can you count?',
     'Present your month, then answer the questions nobody prepared you for.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'a Results Meeting',
    '8 words for the figures, the hours and the trend', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para revenue: Is '
    'revenue the money that stays in the company? (Não &mdash; é o que entra; o que fica é a '
    'margem.) CCQ para year-on-year: September against August, or against last September? (O '
    'setembro passado.) Pronúncia: revenue tem stress no RE (RE-ve-nue).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para overtime: Do people work overtime '
    'during the normal day? (Não &mdash; depois.) CCQ para slightly: If costs are slightly '
    'above, is it a big problem? (Não.) Repare: overtime e spending não têm plural.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta, como se estivesse na reunião. Cronometre: deve caber em quarenta '
    'segundos.',
    'Use the Words', 'One Month, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição gramática (1 min): diga: Before every number there is a question: can you count '
    'it? Passe ao próximo.',
    'Chapter 3: Can You Count It?', 'Much or Many,', 'Less or Fewer',
    'Quantifiers with countable and uncountable nouns', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: Look at the '
    'nouns after the orange words. Which ones can you count, one, two, three? Só DEPOIS clique '
    'em Reveal the Rule. CCQ: Can you say three overtimes? (Não &mdash; então é much e less.) '
    'Can you say three incidents? (Sim &mdash; então é many e fewer.)',
    'quantifiers with countable and uncountable nouns',
    [('"How <span class="accent" style="font-weight:700">much</span> overtime did we pay?"',
      'How much overtime did we pay?'),
     ('"How <span class="accent" style="font-weight:700">many</span> incidents were there?"',
      'How many incidents were there?'),
     ('"There were <span class="accent" style="font-weight:700">fewer</span> incidents than in August."',
      'There were fewer incidents than in August.'),
     ('"There is <span class="accent" style="font-weight:700">very little</span> space left in the warehouse."',
      'There is very little space left in the warehouse.')],
    'rule13',
    ['Countable (incidents, pallets, people)', 'Uncountable (overtime, money, space)', 'Both'],
    [['how many?', 'how much?', 'a lot of / lots of'],
     ['many', 'much (in questions and negatives)', 'some / any'],
     ['a few · few', 'a little · little', 'enough'],
     ['fewer', 'less', 'too much / too many'],
     ['the number of', 'the amount of', 'no / none']],
    ('Can you put a number in front of it? Then it takes many, few and fewer. If you cannot, it '
     'takes much, little and less.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: can you count it? A resposta escolhe a palavra sozinha.',
    'Grammar Practice', 'Can You', 'Count It?',
    'Say the full sentence, then click to compare',
    [('How ______ people worked overtime last week?',
      'How many people worked overtime last week?'),
     ("We didn't spend ______ money on cleaning in September.",
      "We didn't spend much money on cleaning in September."),
     ('There were ______ breakdowns this month than in August.',
      'There were fewer breakdowns this month than in August.'),
     ('There is only ______ space left at the distribution center.',
      'There is only a little space left at the distribution center.')]))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): a Rachel, da controladoria, americana, com os números do mês na véspera '
    'da reunião. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Muitos números juntos '
    '&mdash; peça que ele anote só três. Toque duas vezes.',
    1, 'The Figures Before', 'the Meeting',
    'A colleague sends the numbers the night before. Sound first, no text.',
    'a13_listening1.mp3', SLUG,
    [('How many incidents were there in the stores?',
      'Only a few: eleven in total.'),
     ('How much above the budget was maintenance?',
      'Slightly above, about two percent.'),
     ('What is the bad news, and where did most of it happen?',
      'Overtime: almost four hundred hours, mostly at the distribution center.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição diálogo (1 min): diga: Now the meeting. Graham, from the regional office, has '
    'the numbers in front of him and a lot of questions. Passe ao próximo.',
    'Chapter 4: The Meeting', 'Twenty Minutes,', 'Four Areas',
    'Presenting the month and answering the questions', IMG_MEET))

S.append(L.s_dialogue(
    14, 4,
    'Diálogo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, peça que ELE fale '
    'primeiro, com o texto tapado. Graham tem sotaque britânico, o mesmo da aula 8. Aponte a '
    'fala 8: ele assume o problema antes de ser cobrado.',
    'Twenty Minutes,', 'Four Areas',
    [('graham', 'G', 'british_m', 'Right, Felipe. Where do you want to start?'),
     ('felipe', 'F', 'arthur',
      'With the good news. <span class="vocab-highlight">Revenue</span> in the stores was up in '
      'September.'),
     ('graham', 'G', 'british_m', 'And the <span class="vocab-highlight">margin</span>?'),
     ('felipe', 'F', 'arthur',
      'Slightly lower, because our costs grew too. Not much, less than one percent.'),
     ('graham', 'G', 'british_m', 'How many incidents in the stores?'),
     ('felipe', 'F', 'arthur',
      'Only a few. Eleven, and that is fewer than in August.'),
     ('graham', 'G', 'british_m',
      'Good. And how much <span class="vocab-highlight">overtime</span> did you pay?'),
     ('felipe', 'F', 'arthur',
      'Too much. Almost four hundred hours, most of it in the last week.'),
     ('graham', 'G', 'british_m', 'Why so many hours?'),
     ('felipe', 'F', 'arthur',
      'Two big deliveries arrived on the same day, and there was very little space in the '
      'warehouse.'),
     ('graham', 'G', 'british_m', 'Can you bring a plan for October?'),
     ('felipe', 'F', 'arthur',
      'Yes. Fewer deliveries on Fridays, and a lower <span class="vocab-highlight">stock level</span> '
      'before the holidays.')]))

S.append(L.s_comprehension(
    15, 4,
    'Comprehension (3 min): as perguntas são sobre o GRAHAM, não sobre ele. Ele responde de '
    'memória ANTES de clicar.',
    'Did You Catch It?', 'About', 'Graham',
    [('What does Graham ask about right after the revenue?',
      'The margin.'),
     ('Which two numbers does he ask about with how many and how much?',
      'How many incidents, and how much overtime.'),
     ('What does he ask Felipe to bring for October?',
      'A plan.')]))

S.append(L.s_artifact(
    16, 4,
    'Artefato (4 min): o slide que ele mostra na reunião. Peça que ele APRESENTE em voz alta, '
    'linha por linha, sem ler: transformando cada número numa frase. A terceira pergunta é '
    'produção: exija fewer.',
    'Real Document', 'The Monthly', 'Dashboard',
    'SEPTEMBER RESULTS &mdash; FOUR AREAS', 'PRESENTER: FELIPE DIAS',
    [('Revenue (stores)', 'up 4% &middot; on target'),
     ('Margin', '0.8 points lower'),
     ('Shrinkage', 'down 3% year-on-year'),
     ('Store incidents', '11 &middot; August: 15'),
     ('Maintenance', '2% above budget'),
     ('Outside cleaning spending', 'down 20%'),
     ('Overtime (DC)', '390 hours &middot; target: 150'),
     ('Stock level (DC)', '94% full')],
    [('Which number is the best news, and which is the worst?',
      'Shrinkage down three percent is the best. Overtime at 390 hours against 150 is the worst.'),
     ('Is there much space left at the distribution center?',
      'No. It is ninety-four percent full, so there is very little space.'),
     ('Compare the incidents with August, using fewer.',
      'There were fewer incidents in September than in August: eleven against fifteen.')]))

S.append(L.s_listening(
    17, 4,
    'Listening 2 (5 min): sotaque britânico, o mesmo Graham do diálogo, depois da reunião. LEIA '
    'AS PERGUNTAS COM ELE ANTES do play. No fim ele corrige um erro do Felipe &mdash; peça que '
    'ele diga qual. Toque duas vezes.',
    2, 'Graham Sends', 'Feedback',
    'A message after the meeting, with one small correction. Sound first, no text.',
    'a13_listening2.mp3', SLUG,
    [('What does the board want to know about the incidents?',
      'How many were shoplifting and how many were internal.'),
     ('What does Graham want to know about the overtime?',
      'How many people it was.'),
     ('What small mistake does he correct?',
      'Felipe said less incidents. It should be fewer incidents.')]))

S.append(L.s_blocks(
    18, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as Tips. '
    'Exija um NÚMERO em toda resposta: na reunião de verdade, ninguém aceita a lot sem número '
    'logo depois.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    19, 6,
    'Transição prática (1 min): diga: Now you present. Three rounds, less help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    20, 6,
    'Scenarios + Rephrase (5 min): nos cenários exija pelo menos um contável e um incontável. No '
    'rephrase ele usa a palavra entre parênteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    21, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('There were less incidents than in August.', 'There were fewer incidents than in August.'),
     ('How much people worked overtime?', 'How many people worked overtime?'),
     ('We paid a lot of overtimes last week.', 'We paid a lot of overtime last week.'),
     ('There is very few space in the warehouse.', 'There is very little space in the warehouse.')]))

S.append(L.s_roleplay(
    22, 6,
    'Role-play 1 &mdash; guiado (4 min): você é o Graham. Peça o resultado de UMA área e faça '
    'duas perguntas: uma com how much, outra com how many. Ele usa as chips.',
    'Role-Play 1 &mdash; Guided', 'One Area,', 'Three Numbers',
    'Situation',
    'Present last month in one of your areas: one number that went up, one that dropped, and '
    'one problem. Then answer two questions about the numbers.',
    ['revenue was up', 'slightly', 'a few', 'fewer than', 'too much']))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é o diretor financeiro, irritado com a hora '
    'extra. Insista: why so much? Ele tem de explicar com números e propor um plano.',
    'Role-Play 2 &mdash; Semi-Free', 'Why So Much', 'Overtime?',
    'Situation',
    'Your finance director is unhappy with the overtime. Explain how many people and how many '
    'hours, why it happened, and what will be different next month.',
    ['how many people', 'very little space', 'fewer deliveries', 'less overtime']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos e conte quantos números ele disse. Depois faça UMA pergunta '
    'que ele não esperava. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Present your real last month in your four areas: the good news, the bad news, and the '
    'number you are most worried about. Use real numbers. Then answer one question from the '
    'table. Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    25, 6,
    'Answer key (2 min): o accordion nasce fechado. Só abra depois que ele tentou as quatro do '
    'rephrase. Clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    26,
    'Survival lines (3 min): leia cada frase, toque o áudio, peça repetição olhando para a '
    'câmera. São as cinco frases da próxima reunião de resultado dele.',
    'Say It with', 'Confidence',
    ['Let me start with the good news.',
     'Shrinkage is down three percent year-on-year.',
     'There were fewer incidents than in August.',
     'We paid too much overtime in the last week.',
     'There is very little space left in the warehouse.']))

S.append(L.s_checklist(
    27,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 13.',
    13,
    ['I can present a month of results out loud, with real numbers.',
     'I ask how many for things I can count and how much for things I cannot.',
     'I say fewer incidents and less overtime.',
     'I use a few and a little, and I know they are different.',
     'I know the words: revenue, margin, year-on-year, spending, overtime, stock level, to '
     'drop, slightly.']))

S.append(L.s_badge(
    28,
    'Encerramento (2 min): diga: Lesson 13 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos apresentando o mês real de uma área dele, com números, e '
    'mandar no WhatsApp. Próxima aula: If the Container Is Late.',
    13, 'Numbers in a Results Meeting',
    'You presented four areas in English today, Felipe, and every number had a sentence around '
    'it.',
    'If the Container Is Late'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Numbers in a Results Meeting -- Presenting Figures',
    'short_title': 'Numbers in a Results Meeting',
    'menu_desc': ('Speaking lesson: a month of figures out loud, the questions after, and the '
                  'difference between much and many, less and fewer'),
    'grammar_point': 'quantifiers with countable and uncountable nouns',
    'characters': {'felipe': 'arthur', 'graham': 'british_m'},
    'phases': ['The Monthly Meeting', 'Your Words', 'Can You Count It?', 'The Meeting',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80',
    'desc': ('The words of a results meeting: revenue, margin, year-on-year, spending, '
             'overtime, stock level, to drop, slightly. Structure: much, many, a few, a little, '
             'less and fewer, with countable and uncountable nouns. Mission: present your month '
             'and answer the questions after.'),
    'context_paras': [
        'Let me start with the good news. There were only <strong>a few</strong> incidents in '
        'the stores this month, eleven, and that is <strong>fewer</strong> than in August. We '
        'also spent <strong>less</strong> money on outside cleaning. The bad news is the '
        'overtime. We paid <strong>a lot of</strong> overtime in the last week, almost four '
        'hundred hours, because there was <strong>very little</strong> space in the warehouse.',
        'Notice the pattern. Incidents, people and pallets can be counted, so we say <em>how '
        '<strong>many</strong></em>, <em>a <strong>few</strong></em> and <em><strong>fewer'
        '</strong></em>. Overtime, money and space cannot be counted, so we say <em>how '
        '<strong>much</strong></em>, <em>a <strong>little</strong></em> and <em><strong>less'
        '</strong></em>. <em>A lot of</em> works with both, and nobody ever says <em>three '
        'overtimes</em>.'],
    'context_quiz': [
        ('Why does the text say <em>fewer</em> incidents and not <em>less</em> incidents?',
         [('Because the number of incidents went down this month.', False),
          ('Because incidents can be counted.', True),
          ('Because fewer is the more formal word and less is the more informal word.', False)]),
        ('Why is it <em>a lot of overtime</em> and not <em>a lot of overtimes</em>?',
         [('Because overtime is uncountable, so it has no plural.', True),
          ('Because a lot of is singular.', False),
          ('Because overtime is a verb.', False)]),
        ('What is the problem in the warehouse?',
         [('There were too many incidents and too many people working overtime there.', False),
          ('There was very little space, so they paid a lot of overtime.', True),
          ('Cleaning was expensive.', False)]),
    ],
    'tip_title': 'Quantifiers with Countable and Uncountable Nouns',
    'tip_intro': ('Before every number there is one question: can you count it? The answer '
                  'decides the word that comes before the noun.'),
    'tip_rows': [
        ['how many? / how much?', 'many for things you can count, much for things you cannot.',
         'How <strong>many</strong> incidents? How <strong>much</strong> overtime?'],
        ['a few / a little', 'A small amount, and it is positive.',
         '<strong>A few</strong> incidents · <strong>a little</strong> space'],
        ['few / little', 'Not enough. It sounds negative.',
         'There is <strong>very little</strong> space left.'],
        ['fewer / less', 'Smaller number, smaller amount.',
         '<strong>fewer</strong> incidents · <strong>less</strong> money'],
        ['a lot of', 'Works with both, in every kind of sentence.',
         '<strong>a lot of</strong> pallets · <strong>a lot of</strong> overtime'],
        ['too many / too much', 'More than you want.',
         '<strong>too many</strong> deliveries · <strong>too much</strong> overtime'],
    ],
    'tip_note': ('Uncountable nouns never take a plural -s: <em>overtime</em>, '
                 '<em>spending</em>, <em>money</em>, <em>space</em>, <em>information</em>. And '
                 'much sounds natural in questions and negatives; in a positive sentence, use a '
                 'lot of.'),
    'blanks': [
        ('How ', 'many', 'Hint: one word. People can be counted.',
         'How many people worked overtime last week?', ' people worked overtime last week?'),
        ('How ', 'much', 'Hint: one word. Overtime cannot be counted.',
         'How much overtime did we pay in September?', ' overtime did we pay in September?'),
        ('There were ', 'fewer', 'Hint: one word. A smaller number of things you can count.',
         'There were fewer incidents than in August.', ' incidents than in August.'),
        ('There is very ', 'little', 'Hint: one word. Not enough, and you cannot count it.',
         'There is very little space left in the warehouse.', ' space left in the warehouse.'),
        ('Shrinkage is down three percent ', 'year-on-year',
         'Hint: three words with hyphens. Compared with last year.',
         'Shrinkage is down three percent year-on-year.', '.'),
        ('Maintenance was ', 'slightly', 'Hint: one word. A little, not very much.',
         'Maintenance was slightly above the budget.', ' above the budget.'),
    ],
    'order_title': 'Put the Meeting in Order',
    'order_intro': 'Listen first, then put the five parts of the meeting in the order you hear '
                   'them.',
    'order': [
        (3, 'After that, he says there were only a few incidents, and fewer than in August.'),
        (1, 'First, Felipe says that revenue in the stores was up in September.'),
        (5, 'Finally, Felipe admits it was too much, and promises a plan for October.'),
        (2, 'Then he explains that the margin was slightly lower, because costs grew too.'),
        (4, 'Next, Graham asks how much overtime they paid.'),
    ],
    'speech': [
        'Let me start with the good news.',
        'Shrinkage is down three percent year-on-year.',
        'There were fewer incidents than in August.',
        'We paid too much overtime in the last week.',
        'There is very little space left in the warehouse.',
    ],
    'quiz_intro': 'You are presenting your month in a results meeting. Choose the best thing to '
                  'say.',
    'quiz': [
        ('Your director wants to know the number of people on overtime. He asks:',
         [('How much people did work overtime in the last week of the month?', False),
          ('How many people worked overtime?', True),
          ('How many people did worked overtime?', False)]),
        ('There were eleven incidents this month and fifteen last month. You say:',
         [('There were fewer incidents than last month.', True),
          ('There were less incidents than last month, which is very good news for us.', False),
          ('There were few incidents than last month.', False)]),
        ('The warehouse is almost full. You say:',
         [('There is very few space in the warehouse for the deliveries next week.', False),
          ('There is a few space in the warehouse.', False),
          ('There is very little space in the warehouse.', True)]),
        ('You paid four hundred hours of overtime. You say:',
         [('We paid a lot of overtimes.', False),
          ('We paid a lot of overtime last week.', True),
          ('We paid many overtime.', False)]),
    ],
    'think': ('Think about your real last month in one of your four areas. Record about ninety '
              'seconds. Start with the good news, then the bad news, then the number you are '
              'most worried about. Use real numbers, or numbers close to the real ones. Use at '
              'least one how many, one how much, one fewer and one less. Then imagine your '
              'director asks why, and answer. Use at least four words from this lesson. Do not '
              'stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'Countable and uncountable nouns -- The Grammar Gameshow, BBC Learning English',
         'A quick quiz show on the nouns you can count and the ones you cannot, and the words '
         'that go with each. Connection to Lesson 13: overtime, money and space against '
         'incidents, people and pallets.',
         'Tip: play along. Answer each question out loud before the contestants do.',
         'https://www.youtube.com/watch?v=yay1OUgMSlo', 'Watch on YouTube'),
        ('youtube', 'fewer', 'Grammar Video',
         'Less vs fewer -- English In A Minute, BBC Learning English',
         'One minute on the mistake Graham corrected. Connection to Lesson 13: the difference '
         'that a board notices in a results meeting.',
         'Tip: after watching, say three fewer sentences and three less sentences about your '
         'own month.',
         'https://www.youtube.com/watch?v=7pm-YQGFs8E', 'Watch on YouTube'),
        ('video', 'data', 'Video Lesson',
         '7 effective tips for presenting data at work -- Jeff Su',
         'Practical advice on how to show numbers so that people remember them. Connection to '
         'Lesson 13: what to say before and after each number on your monthly dashboard.',
         'Tip: pick the one tip you never use, and use it in your next results meeting.',
         'https://www.youtube.com/watch?v=jizZKNnx9wA', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
