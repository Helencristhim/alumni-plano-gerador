#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 12 do Felipe de Araujo Dias — Two Suppliers, One Decision.
Comparativos e superlativos. Modelo de LEITURA (aula PAR, REGRA 29).
Tema: duas propostas de manutencao de empilhadeiras para o CD, lado a lado.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 12

IMG_TITLE = 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Proposal', 'a written offer that explains what a company will do and for how much',
     'We received two proposals for the forklift maintenance.'),
    ('Upfront cost', 'the money you pay at the start, before you get any benefit',
     'The upfront cost is higher, but the contract lasts three years.'),
    ('Running costs', 'the money you keep paying to use something over time',
     'Cheap machines often have the highest running costs.'),
    ('Reliable', 'able to be trusted to work well every time',
     'Their technicians are more reliable than anybody we have used before.'),
    ('Response time', 'how long it takes somebody to react after you call them',
     'A four hour response time is much better than two days.'),
    ('Trade-off', 'a situation where you accept something bad to get something good',
     'The trade-off is simple: we pay more and we stop less.'),
    ('To outweigh', 'to be more important or bigger than something else',
     'The savings do not outweigh the risk of a stopped line.'),
    ('Value for money', 'the quality you get compared with the price you pay',
     'The cheapest proposal is not always the best value for money.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Proposal', 'g'], ['2', 'Upfront cost', 'c'],
                   ['3', 'Running costs', 'e'], ['4', 'Reliable', 'h'],
                   ['5', 'Response time', 'a'], ['6', 'Trade-off', 'f'],
                   ['7', 'To outweigh', 'b'], ['8', 'Value for money', 'd']],
         'defs': [['a', 'How long it takes somebody to react after you call them'],
                  ['b', 'To be more important or bigger than something else'],
                  ['c', 'The money you pay at the start, before you get any benefit'],
                  ['d', 'The quality you get compared with the price you pay'],
                  ['e', 'The money you keep paying to use something over time'],
                  ['f', 'A situation where you accept something bad to get something good'],
                  ['g', 'A written offer that explains what a company will do and for how much'],
                  ['h', 'Able to be trusted to work well every time']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: the upfront cost is the number in the proposal, and the '
                  'running costs are the numbers that arrive later. Most bad decisions only look '
                  'at the first one.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['We have two ', ['1', 'proposal'],
                   's on the table, and the cheaper one is not the obvious choice. Its ',
                   ['2', 'upfront cost'], ' is lower, but its ', ['3', 'running costs'],
                   ' are higher, because the parts are not included. The other supplier is more ',
                   ['4', 'reliable'], ', and its ', ['5', 'response time'],
                   ' is four hours instead of two days. So here is the ', ['6', 'trade-off'],
                   ': we pay more every month and we stop the line less. For me, the risk of a '
                   'stopped dock will always ', ['7', 'outweigh'],
                   ' a small saving. In the end, the best ', ['8', 'value for money'],
                   ' is the one that keeps the trucks moving.'],
         'bank': ['proposal', 'upfront cost', 'running costs', 'reliable', 'response time',
                  'trade-off', 'outweigh', 'value for money']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'Two Proposals, Side by Side',
         'paras': [
             'Every supplier wins the first page. The first page of a proposal is the price, and '
             'the price is the easiest number to compare: one is cheaper, one is more expensive, '
             'and a busy director signs the cheaper one before lunch. Last month our team '
             'received two proposals for the forklift maintenance at the distribution center. '
             'NorthLift was about twenty-five percent cheaper than Atlas Handling. On page one, '
             'the decision was already made.',
             'Page three told a different story. NorthLift does not include spare parts, so every '
             'repair is a new invoice, and its response time is two days. Atlas keeps the most '
             'common parts on site and promises a technician in four hours. Last year a '
             'customer of NorthLift lost nine days of operation, and a customer of Atlas lost '
             'two. Over three years Atlas was not the most expensive option at all. It was the '
             'cheapest one, and by far the most reliable. The lesson is not that cheap is bad. '
             'It is that the best proposal is rarely the one with the best first page.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why NorthLift is a bad company', False],
                     ['b', 'Read past the price before you choose', True],
                     ['c', 'How to write a better proposal for a big retail client', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['On the first page, NorthLift was the cheaper proposal.', 't',
             'It says NorthLift was about twenty-five percent cheaper than Atlas Handling.'],
            ['NorthLift includes spare parts in the price.', 'f',
             'It does not include spare parts, so every repair is a new invoice.'],
            ['Over three years, Atlas was the most expensive option.', 'f',
             'Over three years it was the cheapest one, and by far the most reliable.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Your boss asks which of two suppliers you prefer. Compare them on '
                           'three points: price, speed and reliability. Then give your choice.'],
            ['Scenario 2', 'Compare two cities you have worked in. Say which one is bigger, '
                           'which one is easier to work in, and which one is the best for a '
                           'weekend.'],
            ['Scenario 3', 'A colleague wants the cheapest option for the new lockers. Explain '
                           'the trade-off without saying that he is wrong.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each comparison again in the form the cue asks for.',
         'items': [['Atlas is expensive. NorthLift is less expensive.', 'not as ... as'],
                   ['Atlas is fast. NorthLift is slow.', 'comparative'],
                   ['Of the three suppliers, Atlas is reliable.', 'superlative'],
                   ['NorthLift has a good price. Atlas has a good service.', 'better']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'Your director asks, in the corridor, which proposal is better. You '
                          'have thirty seconds.',
             'tips': ['One comparison per point: cheaper, faster, more reliable.',
                      'Finish with the trade-off in one sentence.']},
            {'situation': 'A supplier says their price is the lowest in the market. You know it '
                          'is not.',
             'tips': ['Name the other price: actually, it is not as low as...',
                      'Then ask what makes their offer better.']},
            {'situation': 'Compare the stadium of your team with another big stadium you know.',
             'tips': ['Bigger, older, louder, the best atmosphere.',
                      'Two-syllable adjectives usually take more.']},
            {'situation': 'Finance wants the cheaper option. Explain why the running costs '
                          'change the decision.',
             'tips': ['Start with the number they like, then the number they missed.',
                      'Much cheaper upfront, much more expensive over three years.']},
            {'situation': 'Someone asks for the best restaurant near the office for a client '
                          'lunch.',
             'tips': ['Superlative with the: the quietest, the most convenient.',
                      'Give one reason that matters for a client.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['NorthLift is not as expensive as Atlas.',
                  'Atlas is faster than NorthLift.',
                  'Of the three suppliers, Atlas is the most reliable.',
                  'NorthLift has a better price, but Atlas has a better service.'],
         'note': ('Short adjectives take -er and the -est. Longer ones take more and the most. '
                  'And good, bad and far have their own forms: better, worse, further.')},
    ],
}

LISTENINGS = [
    {'file': 'a12_listening1.mp3', 'voice': 'arthur',
     'text': ('Felipe, Mike from finance. I ran the numbers on the two forklift proposals. On '
              'the first year alone, NorthLift is cheaper, no question. About sixty thousand '
              'less. But when I add the parts, the picture changes. Their parts are not '
              'included, and our forklifts are old, so they break more often than most. '
              'Over three years, Atlas comes out about forty thousand cheaper. It is not the '
              'easiest number to explain to the board, because the first page looks worse. But '
              'it is the better deal. Call me before you decide.')},
    {'file': 'a12_listening2.mp3', 'voice': 'french_f',
     'text': ("Hello Felipe, it's Sophie Martin from Atlas Handling. Thank you for the meeting "
              "yesterday. You asked me why our price is higher than the other proposal, so let "
              "me answer in three points. First, our technicians are closer to you. The nearest "
              "one is twenty minutes from the distribution center. Second, we keep the most "
              "common parts on site, so a repair is faster and simpler. And third, our contract "
              "is longer, three years instead of one, so the monthly price is lower than it "
              "looks. I can't promise we are the cheapest. I can promise we are the fastest.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l12]', 'file': 'pc12_order_proposals.mp3', 'voice': 'ellen',
     'text': ('First, the team receives two proposals for the forklift maintenance. Then they '
              'see that NorthLift is much cheaper on the first page. After that, they read page '
              'three and find that the parts are not included. Next, they compare the response '
              'times: two days against four hours. Finally, they decide that Atlas is the better '
              'value for money over three years.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de LEITURA. O tema é a decisão que ele toma '
    'todo mês: dois fornecedores, uma escolha. Diga o tema e siga.',
    'Chapter 1: The First Page', 'Two Suppliers,', 'One Decision',
    'Comparing two offers when the cheaper one is not the answer', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 11 (3 min): na aula 11 ele explicou as regras do CD. Hoje ele '
    'escolhe quem faz a manutenção dentro dele. Peça que ele responda ao prompt e ESCUTE se sai '
    'more cheap ou more better &mdash; são os erros do Detective. Não corrija ainda.',
    'You Explained the Rules.', 'Now Choose the Supplier',
    'Last lesson you told a visitor what everybody has to do in your building. Today somebody '
    'has to keep that building running, and two companies want the job. One is cheaper. The '
    'question is whether cheaper is better.',
    'Think of two suppliers you know. Which one is better, and why? Three reasons.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Diga que o texto do meio é sobre uma decisão de compra '
    'parecida com as dele. Passe ao próximo.',
    ['Eight words for prices, risks and the choice between them.',
     'Cheaper, the cheapest, not as cheap as: comparing without guessing.',
     'Defend one proposal against another, out loud, with numbers.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'a Decision',
    '8 words for comparing two offers', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para upfront cost: '
    'Do you pay it at the start or every month? (No começo.) CCQ para running costs: Do they '
    'stop after you buy the machine? (Não.) Pronúncia: reliable tem stress no LY (ri-LY-a-ble).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para trade-off: Do you get only good '
    'things in a trade-off? (Não &mdash; ganha uma, perde outra.) CCQ para to outweigh: If the '
    'risk outweighs the saving, which one is bigger? (O risco.)',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta. O parágrafo já é uma recomendação inteira &mdash; pergunte no fim se '
    'ele assinaria a mesma decisão.',
    'Use the Words', 'One Decision, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição leitura (1 min): diga: Read for the main idea first. Do not translate word by '
    'word.',
    'Chapter 3: Read the Proposals', 'Page One,', 'Page Three',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist. Não '
    'peça tradução. Pergunte no fim se ele já assinou uma primeira página antes do almoço.',
    'Read for the Main Idea', 'Two Proposals,', 'Side by Side', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): o Mike, do financeiro, americano, com os números das duas propostas. '
    'LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Números e comparações na mesma frase '
    '&mdash; é o que ele perde na vida real. Toque duas vezes.',
    1, 'Mike Runs', 'the Numbers',
    'A colleague from finance compares the two offers. Sound first, no text.',
    'a12_listening1.mp3', SLUG,
    [('How much cheaper is NorthLift in the first year?',
      'About sixty thousand less.'),
     ('Why do the parts matter so much for us?',
      'Because our forklifts are old, so they break more often than most.'),
     ('Over three years, which proposal is cheaper, and by how much?',
      'Atlas, by about forty thousand.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição gramática (1 min): diga: Cheaper, the cheapest, not as cheap as. Three ways to '
    'compare, and one of them is the safest in a meeting. Passe ao próximo.',
    'Chapter 4: Side by Side', 'Cheaper, the Cheapest,', 'Not as Cheap As',
    'Comparing two things, or many', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: Which '
    'sentences compare two things, and which compare one thing with all the others? Só DEPOIS '
    'clique em Reveal the Rule. CCQ: In NorthLift is not as reliable as Atlas, which one is '
    'more reliable? (Atlas.) Mostre que not as... as é o jeito educado de dizer worse.',
    'comparatives and superlatives',
    [('"NorthLift is <span class="accent" style="font-weight:700">cheaper than</span> Atlas."',
      'NorthLift is cheaper than Atlas.'),
     ('"Atlas is <span class="accent" style="font-weight:700">more reliable than</span> NorthLift."',
      'Atlas is more reliable than NorthLift.'),
     ('"It was <span class="accent" style="font-weight:700">the most reliable</span> option of all."',
      'It was the most reliable option of all.'),
     ('"Their price is <span class="accent" style="font-weight:700">not as low as</span> it looks."',
      'Their price is not as low as it looks.')],
    'rule12',
    ['Form', 'Use it for', 'Example'],
    [['short adjective + -er than', 'Two things, one syllable (or ending in -y).',
      'NorthLift is <strong>cheaper than</strong> Atlas.'],
     ['more + long adjective + than', 'Two things, two or more syllables.',
      'Atlas is <strong>more reliable than</strong> NorthLift.'],
     ['the + -est / the most', 'One thing against all the others.',
      'It is <strong>the fastest</strong> and <strong>the most reliable</strong>.'],
     ['better / the best · worse / the worst', 'Good and bad have their own forms.',
      'Atlas is the <strong>better</strong> deal.'],
     ['not as + adjective + as', 'A softer way to say less, very useful in a meeting.',
      'It is <strong>not as cheap as</strong> it looks.'],
     ['much / a lot + comparative', 'To make the difference bigger.',
      'Four hours is <strong>much faster</strong> than two days.']],
    ('Never more cheaper and never more better. One comparison word is enough: either -er or '
     'more, never both.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: two things, or all of them? A resposta escolhe a forma sozinha.',
    'Grammar Practice', 'Two Things, or', 'All of Them?',
    'Say the full sentence, then click to compare',
    [('A four hour response time is much ______ (fast) than two days.',
      'A four hour response time is much faster than two days.'),
     ('Of the three proposals, Atlas is ______ (reliable).',
      'Of the three proposals, Atlas is the most reliable.'),
     ('NorthLift has a ______ (good) price, but a ______ (bad) service.',
      'NorthLift has a better price, but a worse service.'),
     ('The cheap proposal is not ______ (cheap) it looks.',
      'The cheap proposal is not as cheap as it looks.')]))

S.append(L.s_dialogue(
    16, 4,
    'Diálogo (6 min): Sophie, da Atlas, francesa, defendendo o preço mais alto. Clique Next Line '
    'a cada fala. Nas falas do FELIPE, peça que ELE fale primeiro, com o texto tapado. Aponte a '
    'fala 9: ele não ataca o preço, ele compara.',
    'Why Is Yours', 'More Expensive?',
    [('felipe', 'F', 'arthur',
      'Sophie, I will be direct. Your proposal is twenty-five percent more expensive than the '
      'other one.'),
     ('sophie', 'S', 'french_f',
      'I know. May I ask what is included in the other one?'),
     ('felipe', 'F', 'arthur', 'Maintenance and labor. The parts are separate.'),
     ('sophie', 'S', 'french_f',
      'Then the comparison is not fair. Our price includes the most common parts.'),
     ('felipe', 'F', 'arthur', 'And what is your <span class="vocab-highlight">response time</span>?'),
     ('sophie', 'S', 'french_f',
      'Four hours. The nearest technician is twenty minutes from your distribution center.'),
     ('felipe', 'F', 'arthur', 'Theirs is two days.'),
     ('sophie', 'S', 'french_f',
      'So ours is much faster. How many days did you lose last year?'),
     ('felipe', 'F', 'arthur',
      'Seven. And a stopped dock is more expensive than any '
      '<span class="vocab-highlight">proposal</span>.'),
     ('sophie', 'S', 'french_f',
      'Then the real question is the <span class="vocab-highlight">running costs</span>, not '
      'the first page.'),
     ('felipe', 'F', 'arthur',
      'Fair. Send me the three year numbers and I will compare them line by line.'),
     ('sophie', 'S', 'french_f',
      'You will have them tomorrow. I am not the cheapest, but I am the most '
      '<span class="vocab-highlight">reliable</span>.')]))

S.append(L.s_comprehension(
    17, 4,
    'Comprehension (3 min): as perguntas são sobre a SOPHIE, não sobre ele. Ele responde de '
    'memória ANTES de clicar.',
    'Did You Catch It?', 'About', 'Sophie',
    [('What does Sophie say is included in her price?',
      'The most common parts.'),
     ('How far is her nearest technician from the distribution center?',
      'Twenty minutes.'),
     ('What does she promise to send, and when?',
      'The three year numbers, tomorrow.')]))

S.append(L.s_artifact(
    18, 4,
    'Artefato (4 min): a tabela que o time dele montou. Peça que ele LEIA em voz alta, '
    'transformando cada linha numa comparação. A terceira pergunta é produção: exija not as... '
    'as.',
    'Real Document', 'The Comparison', 'Sheet',
    'PROPOSAL COMPARISON &mdash; FORKLIFT MAINTENANCE', 'FOR: FELIPE DIAS',
    [('Year 1 price', 'NorthLift 180k &middot; Atlas 240k'),
     ('Parts', 'NorthLift separate &middot; Atlas included'),
     ('Response time', 'NorthLift 48 hours &middot; Atlas 4 hours'),
     ('Nearest technician', 'NorthLift 90 min &middot; Atlas 20 min'),
     ('Days lost last year (references)', 'NorthLift 9 &middot; Atlas 2'),
     ('Contract', 'NorthLift 1 year &middot; Atlas 3 years'),
     ('3 year total (finance)', 'NorthLift 760k &middot; Atlas 720k'),
     ('Recommendation', 'Atlas Handling')],
    [('Which supplier is cheaper in the first year, and by how much?',
      'NorthLift, by sixty thousand.'),
     ('Which line changes the decision, and why?',
      'The three year total. Over three years Atlas is forty thousand cheaper.'),
     ('Compare the response times with not as... as.',
      'NorthLift is not as fast as Atlas.')]))

S.append(L.s_listening(
    19, 4,
    'Listening 2 (5 min): sotaque francês, a mesma Sophie do diálogo, no dia seguinte. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Ela usa um superlativo em cada argumento &mdash; peça que '
    'ele conte quantos no fim. Toque duas vezes.',
    2, 'Sophie Makes', 'Her Case',
    'A message with three reasons and one promise. Sound first, no text.',
    'a12_listening2.mp3', SLUG,
    [('What is her first point about the technicians?',
      'They are closer. The nearest one is twenty minutes from the distribution center.'),
     ('Why is a repair faster and simpler with Atlas?',
      'Because they keep the most common parts on site.'),
     ('What can she not promise, and what can she promise?',
      'She cannot promise they are the cheapest. She can promise they are the fastest.')]))

S.append(L.s_blocks(
    20, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as Tips. '
    'Exija pelo menos DUAS comparações por resposta, uma delas com número.',
    'Chapter 5: Real Talk', 'Compare on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    21, 6,
    'Transição prática (1 min): diga: Now you defend a choice. Three rounds, less help each '
    'time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    22, 6,
    'Scenarios + Rephrase (5 min): nos cenários exija comparativo E superlativo. No rephrase ele '
    'escolhe a forma pela pista entre parênteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    23, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('NorthLift is more cheaper than Atlas.', 'NorthLift is cheaper than Atlas.'),
     ('Atlas is the more reliable of the three.', 'Atlas is the most reliable of the three.'),
     ('Their service is more better than the other one.',
      'Their service is better than the other one.'),
     ('Our forklifts are older that theirs.', 'Our forklifts are older than theirs.')]))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 1 &mdash; guiado (4 min): você é o diretor financeiro. Pergunte: why not the '
    'cheaper one? Ele responde usando as chips, com números da tabela.',
    'Role-Play 1 &mdash; Guided', 'Why Not the', 'Cheaper One?',
    'Situation',
    'Your finance director wants the cheaper proposal. Compare the two suppliers on price, '
    'parts and response time, and recommend one.',
    ['cheaper than', 'more reliable', 'much faster', 'not as cheap as', 'the best value for money']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é o vendedor da NorthLift. Diga que o seu '
    'preço é o mais baixo do mercado. Ele tem de recusar comparando, sem ofender.',
    'Role-Play 2 &mdash; Semi-Free', 'The Lowest Price', 'in the Market',
    'Situation',
    'The cheaper supplier calls to say their price is the lowest in the market. Thank them, '
    'explain the trade-off, and say what would make their offer better.',
    ['the lowest', 'not as', 'running costs', 'outweigh']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos e conte quantas comparações ele fez. Diga o número no fim. '
    'CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Think of a real decision between two suppliers, two products or two cities. Present both '
    'options, compare them on at least three points, name the trade-off, and give your final '
    'choice. Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    27, 6,
    'Answer key (2 min): o accordion nasce fechado. Só abra depois que ele tentou as quatro do '
    'rephrase. Clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    28,
    'Survival lines (3 min): leia cada frase, toque o áudio, peça repetição olhando para a '
    'câmera. São as cinco frases da próxima reunião de compra dele.',
    'Say It with', 'Confidence',
    ['Their proposal is cheaper, but it is not as complete.',
     'A four hour response time is much faster than two days.',
     'Over three years, this is the better value for money.',
     'The cheapest option is not always the best one.',
     'The risk of a stopped dock outweighs the saving.']))

S.append(L.s_checklist(
    29,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 12.',
    12,
    ['I can compare two proposals out loud, with numbers.',
     'I use -er than for short words and more than for long ones.',
     'I use the -est or the most when I compare one thing with all the others.',
     'I never say more cheaper or more better.',
     'I know the words: proposal, upfront cost, running costs, reliable, response time, '
     'trade-off, to outweigh, value for money.']))

S.append(L.s_badge(
    30,
    'Encerramento (2 min): diga: Lesson 12 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos comparando dois fornecedores reais dele e mandar no '
    'WhatsApp. Próxima aula: Numbers in a Results Meeting.',
    12, 'Two Suppliers, One Decision',
    'You read past the first page today, Felipe, and you defended the decision with numbers.',
    'Numbers in a Results Meeting'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Two Suppliers, One Decision -- Comparing Offers',
    'short_title': 'Two Suppliers, One Decision',
    'menu_desc': ('Reading lesson: two proposals side by side, the cheaper first page and the '
                  'better deal, in comparatives and superlatives'),
    'grammar_point': 'comparatives and superlatives',
    'characters': {'felipe': 'arthur', 'sophie': 'french_f'},
    'phases': ['The First Page', 'Your Words', 'Read the Proposals', 'Side by Side',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80',
    'desc': ('The words of a decision: proposal, upfront cost, running costs, reliable, '
             'response time, trade-off, to outweigh, value for money. Structure: comparatives, '
             'superlatives and not as... as. Mission: defend one proposal against another, out '
             'loud, with numbers.'),
    'context_paras': [
        'On the first page, NorthLift is <strong>cheaper than</strong> Atlas: about twenty-five '
        'percent. But Atlas is <strong>faster</strong>, with a four hour response time against '
        'two days, and it is <strong>more reliable</strong>, because the most common parts are '
        'already on site. Of the three companies we looked at, Atlas had <strong>the best</strong> '
        'record: two days lost last year, against nine.',
        'So which proposal is <strong>better</strong>? NorthLift is <strong>not as '
        'expensive as</strong> Atlas in the first year. Over three years it is <strong>the most '
        'expensive</strong> option, because every part is a new invoice. Notice the pattern: '
        'short words take <em>-er</em> and <em>the -est</em>, long words take <em>more</em> and '
        '<em>the most</em>, and <em>good</em> becomes <em>better</em> and <em>the best</em>.'],
    'context_quiz': [
        ('Why is it <em>more reliable</em> and not <em>reliabler</em>?',
         [('Because reliable is a long adjective, so it takes more.', True),
          ('Because reliable is an irregular adjective, like good, bad and far.', False),
          ('Because more is used with every adjective in a formal business proposal.', False)]),
        ('What does <em>NorthLift is not as expensive as Atlas</em> mean?',
         [('NorthLift is cheaper than Atlas in the first year.', True),
          ('NorthLift and Atlas cost exactly the same amount of money every year.', False),
          ('NorthLift is more expensive than Atlas.', False)]),
        ('Over three years, which option is the most expensive?',
         [('Atlas, because the price on the first page is higher than the other.', False),
          ('NorthLift, because every part is a new invoice.', True),
          ('Both cost the same.', False)]),
    ],
    'tip_title': 'Comparatives and Superlatives',
    'tip_intro': ('Two things, or one thing against all the others. The length of the adjective '
                  'decides the form.'),
    'tip_rows': [
        ['short + -er than', 'One syllable, or two ending in -y.',
         'NorthLift is <strong>cheaper than</strong> Atlas.'],
        ['more + long + than', 'Two or more syllables.',
         'Atlas is <strong>more reliable than</strong> NorthLift.'],
        ['the + -est / the most', 'One against all the others.',
         'It is <strong>the fastest</strong> and <strong>the most reliable</strong>.'],
        ['Irregular', 'good, better, the best · bad, worse, the worst · far, further, the furthest.',
         'Atlas is <strong>the better</strong> deal.'],
        ['not as ... as', 'A softer way to say less.',
         'It is <strong>not as cheap as</strong> it looks.'],
        ['much / a lot', 'Makes the difference bigger.',
         'Four hours is <strong>much faster</strong> than two days.'],
    ],
    'tip_note': ('Never two comparison words together: not <em>more cheaper</em>, not <em>more '
                 'better</em>. And after a comparative comes <em>than</em>, never <em>that</em>.'),
    'blanks': [
        ('NorthLift is ', 'cheaper', 'Hint: one word. Short adjective, two things.',
         'NorthLift is cheaper than Atlas in the first year.', ' than Atlas in the first year.'),
        ('Atlas is ', 'more reliable', 'Hint: two words. Long adjective, two things.',
         'Atlas is more reliable than NorthLift.', ' than NorthLift.'),
        ('Of the three proposals, Atlas is ', 'the fastest',
         'Hint: two words. One against all the others.',
         'Of the three proposals, Atlas is the fastest.', '.'),
        ('Their price is not ', 'as low as', 'Hint: three words. A softer way to say higher.',
         'Their price is not as low as it looks.', ' it looks.'),
        ('A four hour ', 'response time', 'Hint: two words. How long they take to react.',
         'A four hour response time is much better than two days.',
         ' is much better than two days.'),
        ('The cheapest proposal is not always the best ', 'value for money',
         'Hint: three words. Quality compared with price.',
         'The cheapest proposal is not always the best value for money.', '.'),
    ],
    'order_title': 'Put the Decision in Order',
    'order_intro': 'Listen first, then put the five steps of the decision in the order you hear '
                   'them.',
    'order': [
        (4, 'Next, they compare the response times: two days against four hours.'),
        (1, 'First, the team receives two proposals for the forklift maintenance.'),
        (5, 'Finally, they decide that Atlas is the better value for money over three years.'),
        (2, 'Then they see that NorthLift is much cheaper on the first page.'),
        (3, 'After that, they read page three and find that the parts are not included.'),
    ],
    'speech': [
        'Their proposal is cheaper, but it is not as complete.',
        'A four hour response time is much faster than two days.',
        'Over three years, this is the better value for money.',
        'The cheapest option is not always the best one.',
        'The risk of a stopped dock outweighs the saving.',
    ],
    'quiz_intro': 'You are comparing two offers in a meeting. Choose the best thing to say.',
    'quiz': [
        ('You want to say that NorthLift costs less. You say:',
         [('NorthLift is more cheaper than Atlas on the first page of the proposal.', False),
          ('NorthLift is cheaper than Atlas.', True),
          ('NorthLift is cheapest that Atlas.', False)]),
        ('You compare Atlas with all the other suppliers. You say:',
         [('Atlas is the more reliable supplier of all the companies we spoke to.', False),
          ('Atlas is the most reliable of all.', True),
          ('Atlas is reliabler than all.', False)]),
        ('You want to say, politely, that the price is high. You say:',
         [('Your price is not as low as the other proposal.', True),
          ('Your price is more higher than the other.', False),
          ('Your price is the most high.', False)]),
        ('The service of Atlas is good, and the service of NorthLift is less good. You say:',
         [('Atlas has a more good service than NorthLift, in my personal opinion.', False),
          ('Atlas has a gooder service.', False),
          ('Atlas has a better service than NorthLift.', True)]),
    ],
    'think': ('Think about a real decision between two suppliers, two machines or two service '
              'contracts that you made, or have to make soon. Record about ninety seconds. '
              'Present the two options, then compare them on at least three points: price, '
              'speed and reliability. Use one comparative, one superlative and one not as... as. '
              'Name the trade-off, and finish with your choice and the reason. Use at least '
              'four words from this lesson. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'Comparatives and superlatives -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on the two forms, with the spelling rules and the irregular ones. '
         'Connection to Lesson 12: it is the grammar behind every line of your comparison sheet.',
         'Tip: pause after each example and say the same sentence about two suppliers you know.',
         'https://www.youtube.com/watch?v=FAhpT7BH7GE', 'Watch on YouTube'),
        ('youtube', 'asas', 'Grammar Video',
         'As ... as comparatives -- English In A Minute, BBC Learning English',
         'One minute on as... as and not as... as, the softer way to compare in a meeting. '
         'Connection to Lesson 12: the sentence you used to tell Sophie her price was high.',
         'Tip: make three not as... as sentences about your own team, then say them out loud.',
         'https://www.youtube.com/watch?v=5qI6meJ2kpc', 'Watch on YouTube'),
        ('video', 'compare', 'Video Lesson',
         'How to compare things in English -- Easy English Conversations, BBC Learning English',
         'A short real conversation where two people compare options and choose one. '
         'Connection to Lesson 12: the same moves as your role-play, in an everyday situation.',
         'Tip: listen once without pausing, then write down every comparison you heard.',
         'https://www.youtube.com/watch?v=5VGtCbFclgk', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
