#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 8 do Felipe de Araujo Dias — The Plan for Next Quarter (will vs going to).
Modelo de LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 8

IMG_TITLE = 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Forecast', 'the number you expect for a future period, based on what you know now',
     'The forecast is ninety-four per cent in July and ninety-seven in August.'),
    ('Target', 'the number you have agreed to reach',
     'The target is ninety-eight per cent on-time delivery.'),
    ('Budget', 'the money a team is allowed to spend in a period',
     'The budget is six per cent below last quarter.'),
    ('Quarter', 'a period of three months in a company year',
     'Once a quarter the same meeting happens in every retail company on earth.'),
    ('To roll out', 'to introduce something new across a company, site by site',
     'We are going to roll out the new picking system in three sites.'),
    ('Bottleneck', 'the one point in a process that slows everything else down',
     'The inbound dock at Guarulhos is the bottleneck of the whole quarter.'),
    ('Stakeholder', 'a person or a group with a real interest in how a project ends',
     'Marketing is a stakeholder in this decision, so they hear it before the board does.'),
    ('Capacity', 'the maximum a site, a machine or a team can handle',
     'We are at ninety per cent of capacity, and that is why nothing has room to go wrong.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Forecast', 'd'], ['2', 'Target', 'g'], ['3', 'Budget', 'a'],
                   ['4', 'Quarter', 'f'], ['5', 'To roll out', 'b'],
                   ['6', 'Bottleneck', 'h'], ['7', 'Stakeholder', 'c'],
                   ['8', 'Capacity', 'e']],
         'defs': [['a', 'The money a team is allowed to spend in a period'],
                  ['b', 'To introduce something new across a company, site by site'],
                  ['c', 'A person or a group with a real interest in how a project ends'],
                  ['d', 'The number you expect for a future period, based on what you know now'],
                  ['e', 'The maximum a site, a machine or a team can handle'],
                  ['f', 'A period of three months in a company year'],
                  ['g', 'The number you have agreed to reach'],
                  ['h', 'The one point in a process that slows everything else down']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a target is what you promised, a forecast is what you '
                  'expect. When the two are different, that is the whole meeting.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Every ', ['1'], ' we sit down with the same two numbers. The ', ['2'],
                   ' is ninety-eight per cent on time, and the ', ['3'],
                   ' says ninety-four in July. The gap has one reason: the inbound dock is the ',
                   ['4'], ' and we are already at ninety per cent of ', ['5'],
                   '. We are going to ', ['6'],
                   ' the new picking system in three sites to fix it, and the ', ['7'],
                   ' for that is already approved. Marketing is the other ', ['8'],
                   ' here, so they hear it before the board does.'],
         'bank': ['quarter', 'target', 'forecast', 'bottleneck', 'capacity',
                  'roll out', 'budget', 'stakeholder']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The Meeting Where Nobody Says Maybe',
         'paras': [
             'Once a quarter, in every retail company on earth, the same meeting happens. '
             'Somebody stands up with a forecast, somebody else asks about the budget, and '
             'everybody in the room already knows which two numbers are going to be a problem. '
             'The meeting has a reputation for being boring. It is not boring. It is the only '
             'hour in the quarter where a decision costs money in public.',
             'The English of that meeting is smaller than people expect. There are two futures '
             'in it, and they do not mean the same thing. One of them is for what the evidence '
             'already shows: the container is three weeks late, so the collection is going to '
             'arrive after the opening. Nobody decided that. You can see it coming from the '
             'shipping report. The other future is for what somebody decides in the room: fine, '
             'we will move the campaign to July. The first one is a reading of the world. The '
             'second one is a promise made in front of eight people. Say the wrong one and you '
             'either promise something you cannot control, or you sound like a person who has '
             'no plan at all.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why quarterly meetings should be shorter', False],
                     ['b', 'Two futures: the one you see coming and the one you decide', True],
                     ['c', 'How to build a forecast from historical data', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['The text says the quarterly meeting is boring.', 'f',
             'It says the meeting has that reputation, but that it is the only hour where a '
             'decision costs money in public.'],
            ['Going to is used for what the evidence already shows.', 't',
             'The text gives the late container as the example: you can see it coming from the '
             'shipping report.'],
            ['Will is used for decisions taken before the meeting.', 'f',
             'It is for what somebody decides in the room, in front of eight people.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Present next quarter in four sentences: the target, the forecast, '
                           'the reason for the gap, and what you are going to do about it.'],
            ['Scenario 2', 'Your director asks for something in the middle of the meeting and '
                           'you decide on the spot. Say yes with a date, and say what you will '
                           'not be able to do because of it.'],
            ['Scenario 3', 'Somebody asks what happens if the container is late again. Give the '
                           'reading of the evidence first, then the decision you would take.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Choose the right future, and say the whole sentence.',
         'items': [['Look at the shipping report. The collection ______ arrive late.',
                    'evidence'],
                   ['Fine. We ______ move the campaign to July.', 'decision now'],
                   ['We ______ hire six people in May and six in September.', 'plan already made'],
                   ['Do not worry, I ______ send you the numbers this afternoon.', 'promise now']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'Your director asks how next quarter looks. Give the target and the '
                          'forecast in two sentences.',
             'tips': ['The target is agreed, so it is a fact in the present.',
                      'The forecast is a reading of the data: going to.']},
            {'situation': 'She asks why there is a gap between the two numbers.',
             'tips': ['Name the bottleneck, and say what it is going to do if nothing changes.',
                      'One cause, one consequence. Not three.']},
            {'situation': 'She asks you, right now, to move a deadline. You agree in the room.',
             'tips': ['A decision made at this second takes will.',
                      'Give a date with it, or it is not a decision.']},
            {'situation': 'She asks whether you are going to need more people, and you already '
                          'have the plan.',
             'tips': ['The plan already exists, so it is going to, not will.',
                      'Give the two waves and the months.']},
            {'situation': 'She asks what happens if the roll-out slips to four sites instead of '
                          'five.',
             'tips': ['Read the evidence first, then decide out loud.',
                      'It is going to cost us... so we will...']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['Look at the shipping report. The collection is going to arrive late.',
                  'Fine. We will move the campaign to July.',
                  'We are going to hire six people in May and six in September.',
                  'Do not worry, I will send you the numbers this afternoon.'],
         'note': ('going to reads the world or repeats a plan you already have. will is the '
                  'decision you make at the second you speak.')},
    ],
}

LISTENINGS = [
    {'file': 'a8_listening1.mp3', 'voice': 'arthur',
     'text': ('Felipe, it is Daniel. Two things before Thursday. First, the board pack closes on '
              'Wednesday at noon, so anything that arrives after that is not going to be in the '
              'room. Second, I have looked at your forecast and I have one question about the '
              'bottleneck at Guarulhos. If the inbound dock stays as it is, we are going to miss '
              'the target in July, and I would rather say that on Thursday than discover it in '
              'August. Bring one slide on it. I will give you five minutes at the start, not at '
              'the end. And do not bring the full budget. Bring the two lines that changed.')},
    {'file': 'a8_listening2.mp3', 'voice': 'british_m',
     'text': ('Felipe, Graham here. I have just come out of the regional call and I have news '
              'you will like and news you will not. The good one first. They have approved the '
              'twelve people, so you are going to get six in May and six in September, exactly '
              'as you asked. Now the other one. They are going to review every capital line in '
              'October, which means the picking system roll-out will probably be three sites, '
              'not five. I will fight for the fourth, but I will not promise it. One more thing. '
              'The board wants the on-time delivery number by store, not by region, from this '
              'quarter. That is going to take you a week, so start now. Speak on Thursday.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l8]', 'file': 'pc8_order_quarter.mp3', 'voice': 'ellen',
     'text': ('First, Graham asks whether the second distribution center is going to open in '
              'June or in July. Then Felipe explains that the container is three weeks late and '
              'that the collection is going to arrive after the opening. After that, Graham '
              'decides in the room that they will move the campaign to July. Next, they agree '
              'on twelve new people, in two waves. Finally, Felipe promises to send the plan '
              'before the board pack closes.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Aula de LEITURA. O tema &eacute; a '
    'reuni&atilde;o trimestral em ingl&ecirc;s &mdash; onde ele mais precisa soar seguro.',
    'Chapter 1: The Meeting Where Nobody Says Maybe', 'The Plan for', 'Next Quarter',
    'Two futures, and the money that depends on choosing the right one', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 7 (3 min): na aula 7 ele contou dez anos para tr&aacute;s. Hoje '
    'olha tr&ecirc;s meses para a frente. Pe&ccedil;a que ele responda ao prompt e ESCUTE se ele '
    'usa will para tudo &mdash; &eacute; o padr&atilde;o do brasileiro. N&atilde;o corrija ainda: '
    'anote e volte no slide 16.',
    'You Told Ten Years Back.', 'Now Three Months Forward',
    'Everything you said last time already happened. Next quarter has not. English splits the '
    'future in two, and the split is not about time at all: it is about who decided, and when.',
    'What is going to happen in your operation in the next three months? Two things, out loud.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Avise que o texto do meio &eacute; curto. Passe ao '
    'pr&oacute;ximo.',
    ['Eight words that only appear in a quarterly review.',
     'Split the future in two: what you can see coming, and what you decide in the room.',
     'Present a quarter in four sentences, and hold a decision under pressure.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of the', 'Quarterly Review',
    '8 words that decide how the hour goes', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'forecast vs target: Which one did I promise, and which one do I expect? (Target eu '
    'prometi; forecast eu espero.) Pron&uacute;ncia: forecast tem stress na primeira '
    's&iacute;laba (FORE-cast).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para bottleneck: If I fix the second '
    'slowest point, does the process get faster? (N&atilde;o &mdash; s&oacute; o gargalo '
    'manda.) CCQ para stakeholder: Is a stakeholder always my boss? (N&atilde;o &mdash; &eacute; '
    'quem tem interesse no resultado.)',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Este par&aacute;grafo &eacute; o resumo do trimestre '
    'dele &mdash; ser&aacute; reusado no role-play 1.',
    'Use the Words', 'One Quarter, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o leitura (1 min): diga: Read for the main idea first. Do not '
    'translate word by word.',
    'Chapter 3: Read the Meeting', 'Where Nobody', 'Says Maybe',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist. '
    'N&atilde;o pe&ccedil;a tradu&ccedil;&atilde;o. Pergunte no fim se a reuni&atilde;o dele '
    '&eacute; assim &mdash; ele vai ter uma opini&atilde;o forte.',
    'Read for the Main Idea', 'The Meeting Where', 'Nobody Says Maybe', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): o CFO, americano, direto. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES '
    'de tocar. Este &eacute; o tipo de recado que ele recebe de verdade. Toque duas vezes.',
    1, 'The CFO Sets', 'the Agenda',
    'A voicemail two days before the quarterly review. Sound first, no text.',
    'a8_listening1.mp3', SLUG,
    [('When does the board pack close, and what happens after that?',
      'Wednesday at noon. Anything that arrives later is not going to be in the room.'),
     ('What is Daniel worried about?',
      'The bottleneck at Guarulhos. If the inbound dock stays as it is, they are going to miss '
      'the target in July.'),
     ('What does he want Felipe to bring, and when will he speak?',
      'One slide on the bottleneck and the two budget lines that changed. He speaks for five '
      'minutes at the start.')]))

S.append(L.s_chapter(
    13, 4,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: Two futures. One you can point at, '
    'one you decide. Este &eacute; o terceiro e &uacute;ltimo bloco do refresh que ele pediu: '
    'presente, passado e agora futuro.',
    'Chapter 4: Two Futures', 'Evidence, or', 'Decision?',
    'going to reads the world. will decides.', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Two '
    'of these were decided before this conversation and two were decided during it. Which are '
    'which? S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In We will move the campaign, when '
    'did I decide? (Agora, nesta frase.) In We are going to hire six people, when did I decide? '
    '(Antes.)',
    'will vs going to',
    [('"The container is late, so the collection <span class="accent" style="font-weight:700">is going to arrive</span> after the opening."',
      'The container is late, so the collection is going to arrive after the opening.'),
     ('"Fine. We <span class="accent" style="font-weight:700">will move</span> the campaign to July."',
      'Fine. We will move the campaign to July.'),
     ('"We <span class="accent" style="font-weight:700">are going to hire</span> six people in May and six in September."',
      'We are going to hire six people in May and six in September.'),
     ('"Do not worry, I <span class="accent" style="font-weight:700">will send</span> you the numbers this afternoon."',
      'Do not worry, I will send you the numbers this afternoon.')],
    'rule8',
    ['Form', 'Use it for', 'Example'],
    [['going to + verb', 'Evidence you can point at right now, or a plan you already made.',
      'The dock is full, so we <strong>are going to</strong> miss July.'],
     ['will + verb', 'A decision taken at the second you speak. A promise, an offer, a refusal.',
      'Fine, we <strong>will</strong> move the campaign.'],
     ['will for what you think',
      'An opinion or a prediction with no evidence in front of you.',
      'I think the numbers <strong>will</strong> improve in August.'],
     ['Negative', 'will not (won&rsquo;t) &middot; am not / is not / are not going to',
      'I <strong>will not</strong> promise it. We <strong>are not going to</strong> cut the '
      'budget.'],
     ['Question', 'Will you...? asks for a decision. Are you going to...? asks about the plan.',
      '<strong>Are you going to</strong> need more people?']],
    ('going to reads the world or repeats a plan. will decides. If you can point at the '
     'evidence, you cannot use will.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. '
    'Em cada item pergunte primeiro: who decided, and when? A resposta escolhe o futuro sozinha.',
    'Grammar Practice', 'Which Future', 'Is It?',
    'Say the full sentence, then click to compare',
    [('Look at the shipping report. The collection ______ (arrive) after the opening.',
      'Look at the shipping report. The collection is going to arrive after the opening.'),
     ('Fine. We ______ (move) the campaign to July.', 'Fine. We will move the campaign to July.'),
     ('We ______ (hire) six people in May. It is already agreed.',
      'We are going to hire six people in May. It is already agreed.'),
     ('I ______ (not / promise) the fourth site, but I ______ (fight) for it.',
      'I will not promise the fourth site, but I will fight for it.')]))

S.append(L.s_mistake(
    16, 4,
    'Common mistake (3 min): volte ao que voc&ecirc; anotou no warm-up. O segundo par &eacute; o '
    'erro real dele: usar will onde a evid&ecirc;ncia est&aacute; na mesa. Pe&ccedil;a que ele '
    'leia as vers&otilde;es CERTAS duas vezes cada.',
    [('I will to send the forecast this afternoon.',
      'I will send the forecast this afternoon.'),
     ('The container is late, so the collection will arrive after the opening.',
      'The container is late, so the collection is going to arrive after the opening.'),
     ('We not going to cut the budget.', 'We are not going to cut the budget.')],
    ('After will the verb comes bare, with no to. And when the evidence is already on the table, '
     'English refuses will: the sentence has to say going to.')))

S.append(L.s_dialogue(
    17, 4,
    'Di&aacute;logo (6 min): a call trimestral com o regional. Clique Next Line a cada fala. Nas '
    'falas do FELIPE, pe&ccedil;a que ELE fale primeiro, com o texto tapado. Graham tem sotaque '
    'brit&acirc;nico. Aponte a fala 13: ele fecha com uma pergunta indireta da aula 3, sem ajuda.',
    'The Quarterly', 'Call',
    [('graham', 'G', 'british_m',
      'Right, Felipe. Before the numbers, one question. Is the second distribution center going '
      'to open in June or in July?'),
     ('felipe', 'F', 'arthur',
      'June. The building is ready and the team starts in May, so it is going to open on the ninth.'),
     ('graham', 'G', 'british_m',
      'Good. Then I will put June in the regional <span class="vocab-highlight">forecast</span> today.'),
     ('felipe', 'F', 'arthur',
      'There is one problem. The container from Tiruppur is three weeks late, so the spring '
      'collection is going to arrive after the opening.'),
     ('graham', 'G', 'british_m', 'How much of the collection?'),
     ('felipe', 'F', 'arthur',
      'About forty per cent. If we open with sixty, the store will look empty in the photographs.'),
     ('graham', 'G', 'british_m',
      'Then we will move the campaign to July and open quietly in June. Does that work for you?'),
     ('felipe', 'F', 'arthur',
      'It does. I will talk to marketing this afternoon and confirm by Thursday.'),
     ('graham', 'G', 'british_m',
      'And the <span class="vocab-highlight">budget</span>? Are you going to need more people '
      'for the second site?'),
     ('felipe', 'F', 'arthur',
      'Twelve, but not all at once. We are going to hire six in May and six in September.'),
     ('graham', 'G', 'british_m',
      'Fine. I will not touch your headcount line, then. Send me the plan before the board pack '
      'closes.'),
     ('felipe', 'F', 'arthur',
      'I will send it tomorrow morning. And Graham, could you tell me who signs the '
      '<span class="vocab-highlight">capacity</span> study?')]))

S.append(L.s_comprehension(
    18, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre o GRAHAM, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar.',
    'Did You Catch It?', 'About', 'Graham',
    [('What will Graham put in the regional forecast today?',
      'June, as the opening month of the second distribution center.'),
     ('What does Graham decide about the campaign, and when did he decide it?',
      'He will move it to July and open quietly in June. He decided it during the call.'),
     ('What does he promise not to touch?', 'Felipe headcount line.')]))

S.append(L.s_artifact(
    19, 4,
    'Artefato (4 min): o plano do trimestre dele. Pe&ccedil;a que ele LEIA em voz alta e depois '
    'responda. A terceira pergunta &eacute; produ&ccedil;&atilde;o: exija a frase inteira com o '
    'futuro certo.',
    'Real Document', 'The Quarterly', 'Plan',
    'QUARTERLY PLAN &mdash; Q3', 'SUPPLY CHAIN',
    [('Owner', 'Felipe de Ara&uacute;jo Dias'),
     ('Quarter', 'July to September'),
     ('Target', '98% on-time delivery to stores'),
     ('Forecast', '94% in July &middot; 97% in August'),
     ('Budget', 'R$ 4.2 million &middot; 6% below last quarter'),
     ('Headcount', '+12, in two waves'),
     ('Roll-out', 'New picking system &middot; 3 sites'),
     ('Main bottleneck', 'Inbound dock &middot; Guarulhos')],
    [('Which number is a promise, and which one is a reading of the data?',
      'Ninety-eight per cent is the target, agreed with the board. Ninety-four and ninety-seven '
      'are the forecast, what the data shows.'),
     ('What is going to happen at Guarulhos if nothing changes?',
      'The inbound dock is going to slow the whole quarter down. It is the bottleneck.'),
     ('Say the hiring plan out loud, with the right future.',
      'We are going to hire twelve people: six in May and six in September.')]))

S.append(L.s_listening(
    20, 4,
    'Listening 2 (5 min): sotaque brit&acirc;nico, o mesmo Graham do di&aacute;logo. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Ele mistura will e going to em oito frases seguidas '
    '&mdash; pergunte no fim qual foi decis&atilde;o e qual foi evid&ecirc;ncia. Toque duas '
    'vezes.',
    2, 'Good News and', 'Bad News',
    'Graham comes out of the regional call with both. Sound first, no text.',
    'a8_listening2.mp3', SLUG,
    [('What has been approved, and in which waves?',
      'The twelve people: six in May and six in September.'),
     ('What is going to happen in October, and what does it mean for the roll-out?',
      'They are going to review every capital line, so the roll-out will probably be three '
      'sites, not five.'),
     ('What does the board want differently from this quarter?',
      'The on-time delivery number by store, not by region.')]))

S.append(L.s_blocks(
    21, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez, todas dentro da MESMA '
    'reuni&atilde;o. Ele responde EM VOZ ALTA antes de abrir as Tips. Nas 3 e 5, force '
    'decis&atilde;o na hora: se ele hesitar, conte at&eacute; tr&ecirc;s em sil&ecirc;ncio.',
    'Chapter 5: Real Talk', 'The Quarterly', 'Review', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    22, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you run the meeting. Three rounds, '
    'less help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    23, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios exija os dois futuros na MESMA resposta. '
    'No rephrase ele escolhe o futuro pela pista entre par&ecirc;nteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    24, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('I will to send the plan tomorrow.', 'I will send the plan tomorrow.'),
     ('Look at the dock. We will miss the target in July.',
      'Look at the dock. We are going to miss the target in July.'),
     ('We not going to cut the budget this quarter.',
      'We are not going to cut the budget this quarter.'),
     ('Are you going to move the campaign? Yes, I go to move it.',
      'Are you going to move the campaign? Yes, I am going to move it.')]))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; o Graham. Fa&ccedil;a as '
    'perguntas na ordem do plano e nada mais. Corrija apenas will/going to; o resto anote.',
    'Role-Play 1 &mdash; Guided', 'Present the', 'Quarter',
    'Situation',
    'Present next quarter in four sentences: the target, the forecast, the reason for the gap, '
    'and what you are going to do about it. Then answer two questions.',
    ['the target is', 'the forecast is', 'the bottleneck', 'we are going to', 'roll out']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; o CFO e vai pedir algo no meio '
    'da reuni&atilde;o: antecipar o roll-out em duas semanas. Ele TEM de decidir na hora, em '
    'voz alta. N&atilde;o aceite I will think about it.',
    'Role-Play 2 &mdash; Semi-Free', 'A Decision in', 'the Room',
    'Situation',
    'The CFO asks you to bring the roll-out forward by two weeks, in front of the whole '
    'committee. Decide now: say yes or no with a date, say what it costs, and say what you will '
    'not be able to do because of it.',
    ['we will', 'that is going to', 'by the fifteenth']))

S.append(L.s_roleplay(
    27, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa. Cronometre noventa segundos e conte quantas vezes ele escolhe o futuro certo. '
    'Diga o n&uacute;mero no fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Open the quarterly review yourself: the target, the forecast, the gap and why it exists, '
    'the plan you already have, one decision you take live, and one thing you will not promise. '
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
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco da pr&oacute;xima reuni&atilde;o '
    'trimestral dele.',
    'Say It with', 'Confidence',
    ['The target is ninety-eight per cent, and the forecast is ninety-four.',
     'If nothing changes, we are going to miss July.',
     'Fine. We will move the campaign and I will confirm by Thursday.',
     'We are going to hire six people in May and six in September.',
     'I will fight for it, but I will not promise it today.']))

S.append(L.s_checklist(
    30,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 8.',
    8,
    ['I can present a quarter in four sentences.',
     'I use going to when the evidence is already on the table.',
     'I use will for the decision I take at that second.',
     'I never put to after will.',
     'I know the words: forecast, target, budget, quarter, to roll out, bottleneck, '
     'stakeholder, capacity.']))

S.append(L.s_badge(
    31,
    'Encerramento (2 min): diga: Lesson 8 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar noventa segundos apresentando o pr&oacute;prio trimestre e mandar no WhatsApp '
    'antes da pr&oacute;xima aula. Pr&oacute;xima aula: This Time Next Week.',
    8, 'The Plan for Next Quarter',
    'You held a decision under pressure today, Felipe, and you chose the right future for it.',
    'This Time Next Week'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'The Plan for Next Quarter -- Presenting Results and Plans',
    'short_title': 'The Plan for Next Quarter',
    'menu_desc': ('Reading lesson: the hour where a decision costs money in public, and the two '
                  'futures that decide how it goes'),
    'grammar_point': 'will vs going to',
    'characters': {'felipe': 'arthur', 'graham': 'british_m'},
    'phases': ['The Meeting Where Nobody Says Maybe', 'Your Words', 'Read the Meeting',
               'Two Futures', 'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80',
    'desc': ('The words of a quarterly review: forecast, target, budget, quarter, to roll out, '
             'bottleneck, stakeholder, capacity. Structure: going to for the evidence you can '
             'point at and for the plan you already have, will for the decision you take while '
             'you speak. Mission: present a quarter in four sentences and hold a decision under '
             'pressure.'),
    'context_paras': [
        'Here is next quarter in six lines. The target <strong>is</strong> ninety-eight per cent '
        'on time. The forecast <strong>is</strong> ninety-four in July, and everybody in the '
        'room can see why: the inbound dock is full, so we <strong>are going to</strong> miss '
        'the target in the first month. Nobody decided that. It is written in the shipping '
        'report, and you only have to read it out loud.',
        'The rest of the meeting is different. Somebody asks what we do about it, and I say: we '
        '<strong>will</strong> move the campaign to July, and I <strong>will</strong> confirm '
        'with marketing this afternoon. Those two are decisions, taken at the second I speak '
        'them. The hiring is a third case: we <strong>are going to</strong> hire six people in '
        'May and six in September, because that plan already existed before I walked into the '
        'room. Three futures in one paragraph, and only one of them is a promise.'],
    'context_quiz': [
        ('Why does the text use <em>we are going to miss the target</em> and not <em>we will '
         'miss</em>?',
         [('Because the evidence is already visible: the dock is full and the report shows it.',
           True),
          ('Because miss is a negative verb and negatives take going to.', False),
          ('Because it is about July, and July is far away.', False)]),
        ('Why is <em>we will move the campaign</em> in the will form?',
         [('Because moving a campaign is always a promise.', False),
          ('Because the decision is taken at the second he speaks it, in front of the room.',
           True),
          ('Because there is no evidence about campaigns.', False)]),
        ('Why is the hiring in <em>going to</em>?',
         [('Because the plan already existed before the meeting started.', True),
          ('Because hiring involves people and people take going to.', False),
          ('Because it happens in two different months.', False)]),
    ],
    'tip_title': 'Will and Going To',
    'tip_intro': ('Two futures that share a calendar and nothing else. The question is never '
                  'when it happens. It is who decided, and when.'),
    'tip_rows': [
        ['going to + verb', 'Evidence in front of you right now.',
         'The dock is full, so we <strong>are going to</strong> miss July.'],
        ['going to + verb', 'A plan that already existed before this conversation.',
         'We <strong>are going to</strong> hire six people in May.'],
        ['will + verb', 'A decision taken at the second you speak. Also promises and offers.',
         'Fine, we <strong>will</strong> move the campaign. I <strong>will</strong> send it '
         'tonight.'],
        ['will + verb', 'What you think or expect, with no evidence on the table.',
         'I think the numbers <strong>will</strong> improve in August.'],
        ['No <em>to</em> after will',
         'will send, will move, will confirm. Never <em>will to send</em>.'],
        ['Negatives and questions',
         '<em>will not</em> / <em>won&rsquo;t</em> &middot; <em>are not going to</em>. '
         '<em>Will you...?</em> asks for a decision; <em>Are you going to...?</em> asks about '
         'the plan.'],
    ],
    'tip_note': ('One question sorts almost everything: can I point at the reason right now? If '
                 'yes, it is going to. If the sentence is you deciding, it is will.'),
    'blanks': [
        ('The dock is full, so we ', 'are going to',
         'Hint: three words. The evidence is already on the table.',
         'The dock is full, so we are going to miss the target.', ' miss the target.'),
        ('Fine. We ', 'will', 'Hint: four letters. A decision taken at this second.',
         'Fine. We will move the campaign to July.', ' move the campaign to July.'),
        ('The ', 'forecast', 'Hint: one word. The number you expect, not the one you promised.',
         'The forecast is ninety-four per cent in July.', ' is ninety-four per cent in July.'),
        ('The inbound dock is the ', 'bottleneck',
         'Hint: one word. The point that slows everything else down.',
         'The inbound dock is the bottleneck of the whole quarter.', ' of the whole quarter.'),
        ('I ', 'will not', 'Hint: two words. He refuses to promise it today.',
         'I will not promise the fourth site today.', ' promise the fourth site today.'),
        ('We are going to ', 'roll out', 'Hint: two words. To introduce it site by site.',
         'We are going to roll out the new system in three sites.',
         ' the new system in three sites.'),
    ],
    'order_title': 'Put the Call in Order',
    'order_intro': 'Listen first, then put the five parts of the call in the order you hear them.',
    'order': [
        (4, 'Next, they agree on twelve new people, in two waves.'),
        (1, 'First, Graham asks whether the second distribution center is going to open in June '
            'or in July.'),
        (3, 'After that, Graham decides in the room that they will move the campaign to July.'),
        (5, 'Finally, Felipe promises to send the plan before the board pack closes.'),
        (2, 'Then Felipe explains that the container is three weeks late and that the collection '
            'is going to arrive after the opening.'),
    ],
    'speech': [
        'The target is ninety-eight per cent, and the forecast is ninety-four.',
        'If nothing changes, we are going to miss July.',
        'Fine. We will move the campaign and I will confirm by Thursday.',
        'We are going to hire six people in May and six in September.',
        'I will fight for it, but I will not promise it today.',
    ],
    'quiz_intro': 'You are in the quarterly review. Choose the best thing to say.',
    'quiz': [
        ('The shipping report shows a three week delay. You say:',
         [('The collection will arrive after the opening.', False),
          ('The collection is going to arrive after the opening.', True),
          ('The collection arrives after the opening, I think.', False)]),
        ('Your director asks you, right now, to move a deadline, and you agree. You say:',
         [('Fine, I am going to move it to the fifteenth.', False),
          ('Fine, we will move it to the fifteenth.', True),
          ('Fine, I will to move it to the fifteenth.', False)]),
        ('The hiring plan was approved last month. Somebody asks about it. You say:',
         [('We will hire six people in May.', False),
          ('We are going to hire six people in May.', True),
          ('We are hire six people in May.', False)]),
        ('Somebody asks whether you can guarantee the fourth site. You cannot. You say:',
         [('I will fight for it, but I will not promise it today.', True),
          ('I am going to fight for it, but I do not promise nothing.', False),
          ('I will to fight for it, but no promise.', False)]),
    ],
    'think': ('Think about the next three months in your own operation. Record about ninety '
              'seconds. Start with the target and the forecast, and say the number for each. '
              'Then explain the gap between them using going to, because the reason is already '
              'visible. Then name one decision you would take live in that meeting, using will, '
              'and one thing you would refuse to promise. Use at least four words from this '
              'lesson. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'Learn English tenses: future -- will or going to?',
         'A clear, slow explanation of the two futures with a board and a lot of examples. '
         'Connection to Lesson 8: it is the same split you used in the quarterly call, drilled '
         'until the choice becomes automatic.',
         'Tip: pause before each of her examples and choose the future out loud. Then check.',
         'https://www.youtube.com/watch?v=VX95vEL-OdU', 'Watch on YouTube'),
        ('youtube', 'future', 'Grammar Video',
         '"How to talk about the future" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes covering will, going to and the other ways English points forward. '
         'Connection to Lesson 8: it shows the two forms you learned next to the ones that are '
         'coming in the next lesson.',
         'Tip: listen once with your eyes closed. British speakers swallow will almost '
         'completely, and you need to hear that.',
         'https://www.youtube.com/watch?v=elPHkXNxi2g', 'Watch on YouTube'),
        ('video', 'update', 'Video Lesson',
         'How to give a project update in English at work',
         'The structure of a short, professional update: where we are, what is coming, what I '
         'need from you. Connection to Lesson 8: it is the four sentence presentation you '
         'practised, with the connectors that hold it together.',
         'Tip: write your own update for next quarter using her structure, then say it out loud '
         'without reading.',
         'https://www.youtube.com/watch?v=-5q6tNovay8', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
