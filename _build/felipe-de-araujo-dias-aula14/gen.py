#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 14 do Felipe de Araujo Dias — If the Container Is Late.
First conditional (if / unless / as soon as). Modelo de LEITURA (aula PAR, REGRA 29).
Tema: risco e consequencia — o container atrasado que pode derrubar a colecao de verao.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 14

IMG_TITLE = 'https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Container', 'a large metal box used to send goods by ship, train or truck',
     'The container with the summer collection is still in Singapore.'),
    ('Freight', 'goods that are transported, or the service of transporting them',
     'Air freight is ten times more expensive than sea freight.'),
    ('Collection', 'a group of clothes designed and sold for one season',
     'If the container is late, the summer collection will arrive after Black Friday.'),
    ('To be stuck', 'to be unable to move or to continue',
     'The ship has been stuck outside the port for four days.'),
    ('Knock-on effect', 'an indirect result that one problem causes in other areas',
     'One late container has a knock-on effect on forty stores.'),
    ('Contingency plan', 'a plan you prepare in case something goes wrong',
     'We need a contingency plan before Friday, not after.'),
    ('Buffer stock', 'extra stock that you keep in case of delays or problems',
     'If we have enough buffer stock, the stores will not notice.'),
    ('To reroute', 'to send something by a different way than planned',
     'If we reroute the container through another port, we will lose two more days.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Container', 'd'], ['2', 'Freight', 'g'], ['3', 'Collection', 'a'],
                   ['4', 'To be stuck', 'h'], ['5', 'Knock-on effect', 'b'],
                   ['6', 'Contingency plan', 'f'], ['7', 'Buffer stock', 'c'],
                   ['8', 'To reroute', 'e']],
         'defs': [['a', 'A group of clothes designed and sold for one season'],
                  ['b', 'An indirect result that one problem causes in other areas'],
                  ['c', 'Extra stock that you keep in case of delays or problems'],
                  ['d', 'A large metal box used to send goods by ship, train or truck'],
                  ['e', 'To send something by a different way than planned'],
                  ['f', 'A plan you prepare in case something goes wrong'],
                  ['g', 'Goods that are transported, or the service of transporting them'],
                  ['h', 'To be unable to move or to continue']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: buffer stock protects you before the problem, and a '
                  'contingency plan tells you what to do after it starts. Good operations '
                  'teams have both.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['The ', ['1', 'container'], ' with the summer ', ['2', 'collection'],
                   ' has been ', ['3', 'stuck'],
                   ' in Singapore for four days. If it does not leave this week, the ',
                   ['4', 'knock-on effect'],
                   ' will reach forty stores in November. We have some ', ['5', 'buffer stock'],
                   ', but not enough for Black Friday. Our ', ['6', 'contingency plan'],
                   ' has two options. We can ', ['7', 'reroute'],
                   ' the container through another port, or we can pay for air ',
                   ['8', 'freight'], ' for the best-selling items only.'],
         'bank': ['container', 'collection', 'stuck', 'knock-on effect', 'buffer stock',
                  'contingency plan', 'reroute', 'freight']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The Delay That Brings Down a Collection',
         'paras': [
             'A summer collection is planned eighteen months before it reaches a store. The '
             'fabric is chosen, the factories are booked, the advertising is paid for, and the '
             'date of the launch is fixed. Then all of it travels in a few metal boxes across '
             'the ocean, and for five weeks nobody in the company can touch it. If one of '
             'those containers is late, the problem does not stay in the port. It moves '
             'through the whole business.',
             'The knock-on effect is easy to describe and hard to stop. If the container misses '
             'its ship, it will wait a week for the next one. If it arrives a week late, the '
             'distribution center will receive it in the busiest week of the year. If the '
             'stores get it after Black Friday, the advertising will sell clothes that are not '
             'there. The best operations teams do not try to predict every delay. They decide, '
             'in advance, what they will do when it happens: how much buffer stock they need, '
             'which items deserve air freight, and who makes the call. Unless that decision '
             'exists before the delay, it will be made in a panic.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why sea freight is always slower than air freight', False],
                     ['b', 'Plan for the delay before it happens', True],
                     ['c', 'How a summer collection is designed', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['A summer collection is planned about a year and a half before the launch.', 't',
             'It says a collection is planned eighteen months before it reaches a store.'],
            ['If a container misses its ship, it will wait a day for the next one.', 'f',
             'It will wait a week for the next one.'],
            ['The text says the best teams try to predict every delay.', 'f',
             'They do not try to predict every delay. They decide in advance what they will do.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'A container with the summer collection is a week late. Tell your '
                           'director what will happen if it arrives after the 20th, and what '
                           'you will do.'],
            ['Scenario 2', 'Your team is going on a long weekend. Explain what will happen if '
                           'something breaks at the distribution center, and who people should '
                           'call.'],
            ['Scenario 3', 'Talk about a trip you have planned. What will you do if the flight '
                           'is late, if it rains, or if the hotel is full?'],
        ]},
        {'kind': 'rephrase',
         'title': 'Join the two ideas into one sentence with the word the cue asks for.',
         'items': [['The ship leaves tomorrow. We arrive on the 18th.', 'if'],
                   ['We pay for air freight. The stores will not have it.', 'unless'],
                   ['The container arrives. I will call you.', 'as soon as'],
                   ['It is late again. We will not use this supplier next year.', 'if']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'Your director asks what will happen if the container is a week late.',
             'tips': ['If + present, then will. Never if it will be.',
                      'Give the knock-on effect, not just the delay.']},
            {'situation': 'A store manager asks if the summer collection will arrive on time.',
             'tips': ['Be honest: it will, unless...',
                      'Say when you will know for sure.']},
            {'situation': 'The forwarder says the ship might leave tomorrow, or might not.',
             'tips': ['Two sentences: if it leaves... / if it does not leave...',
                      'Finish with your decision for each case.']},
            {'situation': 'Finance asks why you want to pay for air freight.',
             'tips': ['If we do not pay now, we will lose more in November.',
                      'Put a number on the knock-on effect.']},
            {'situation': 'A colleague asks when you will update the team.',
             'tips': ['As soon as + present: as soon as I hear from Bram.',
                      'Not as soon as I will hear.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['If the ship leaves tomorrow, we will arrive on the 18th.',
                  'Unless we pay for air freight, the stores will not have it.',
                  'I will call you as soon as the container arrives.',
                  'If it is late again, we will not use this supplier next year.'],
         'note': ('After if, unless and as soon as, use the present, even when you are talking '
                  'about the future. The will goes in the other half of the sentence.')},
    ],
}

LISTENINGS = [
    {'file': 'a14_listening1.mp3', 'voice': 'ellen',
     'text': ("Felipe, it's Jessica from planning. I know you are talking to the forwarder "
              "today, so here are the dates that matter. The summer collection launches in the "
              "stores on November 10th. To be ready, the distribution center needs the "
              "container by October 28th. If it arrives later than that, we will miss the "
              "launch in at least forty stores. The advertising starts on November 3rd, and we "
              "can't move it. We have buffer stock for about two weeks of the basic items, but "
              "not for the new prints. If you need to choose, the prints are the priority.")},
    {'file': 'a14_listening2.mp3', 'voice': 'dutch_m',
     'text': ("Felipe, Bram here, from the Rotterdam office. I have news about the container. "
              "The ship is still stuck in Singapore, but the port says it will probably leave on "
              "Thursday. If it leaves on Thursday, it will arrive in Santos on the 26th, so you "
              "will just make it. If it doesn't leave on Thursday, the next ship is a week "
              "later, and you will miss your date. I can reroute it through another port, but "
              "that adds two days and about fifteen percent to the freight. I will call you as "
              "soon as the port confirms. Unless I call, the plan stays the same.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l14]', 'file': 'pc14_order_container.mp3', 'voice': 'arthur',
     'text': ('First, Bram tells Felipe that the container is stuck in Singapore. Then he says '
              'that if the ship leaves on Thursday, it will arrive on the 26th. After that, '
              'Felipe asks what will happen if it does not leave. Next, Bram offers to reroute '
              'the container through another port. Finally, Felipe decides to send only the new '
              'prints by air freight.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de LEITURA. O tema é o pesadelo dele: o '
    'container atrasado às vésperas da coleção. Diga o tema e siga.',
    'Chapter 1: Five Weeks at Sea', 'If the Container', 'Is Late',
    'Risk, consequence, and the decision you make before the delay', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 13 (3 min): na aula 13 ele apresentou o mês que passou. Hoje '
    'fala do que PODE acontecer. Peça que ele responda ao prompt e ESCUTE se sai If it will '
    'arrive late &mdash; é o erro do Detective. Não corrija ainda.',
    'You Presented the Month.', 'Now Plan for the Risk',
    'Last lesson the numbers were already in. This time nothing has happened yet: a ship is '
    'late, a date is fixed, and forty stores are waiting. English has one structure for exactly '
    'this, and you will use it every week.',
    'What will happen in your area if a big delivery arrives one week late?'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Diga que o texto do meio é sobre a coleção de verão. '
    'Passe ao próximo.',
    ['Eight words for ships, delays and the plan you make in advance.',
     'If, unless and as soon as: the present that talks about the future.',
     'Explain a risk and its knock-on effect, and decide what you will do.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'a Delay',
    '8 words for the ship, the risk and the plan', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para freight: Is '
    'freight only the truck, or also the goods? (Os dois.) CCQ para collection: Is a collection '
    'one product or a group? (Um grupo, de uma estação.) Pronúncia: freight rima com eight.',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para knock-on effect: Is it the first '
    'problem or the next ones? (Os próximos.) CCQ para buffer stock: Do you use it every day? '
    '(Não &mdash; só quando algo atrasa.)',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta. Pergunte no fim qual das duas opções ele escolheria, e por quê.',
    'Use the Words', 'One Delay, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição leitura (1 min): diga: Read for the main idea first. Do not translate word by '
    'word.',
    'Chapter 3: Read the Story', 'One Box,', 'Forty Stores',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist. Não '
    'peça tradução. Pergunte no fim se a última frase do texto é verdade na empresa dele.',
    'Read for the Main Idea', 'The Delay That Brings', 'Down a Collection', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): a Jessica, do planejamento, americana, com as datas que importam. LEIA '
    'AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Três datas numa mensagem &mdash; peça que '
    'ele anote as três. Toque duas vezes.',
    1, 'The Dates', 'That Matter',
    'A colleague from planning explains the deadline. Sound first, no text.',
    'a14_listening1.mp3', SLUG,
    [('When does the distribution center need the container?',
      'By October 28th.'),
     ('What will happen if it arrives later than that?',
      'They will miss the launch in at least forty stores.'),
     ('If Felipe needs to choose, what is the priority?',
      'The new prints.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição gramática (1 min): diga: Nothing has happened yet. So why is the verb in the '
    'present? Passe ao próximo.',
    'Chapter 4: If, Unless, As Soon As', 'The Present That', 'Talks About Tomorrow',
    'The first conditional', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: All of these '
    'are about the future. Which verb is in the present, and which one has will? Só DEPOIS '
    'clique em Reveal the Rule. CCQ: In If it leaves on Thursday, has it left? (Não &mdash; '
    'ainda não sabemos.) In Unless I call, the plan stays the same, if I do not call, what '
    'happens? (Nada muda.)',
    'first conditional',
    [('"If the ship <span class="accent" style="font-weight:700">leaves</span> on Thursday, it '
      '<span class="accent" style="font-weight:700">will arrive</span> on the 26th."',
      'If the ship leaves on Thursday, it will arrive on the 26th.'),
     ('"If it <span class="accent" style="font-weight:700">doesn\'t leave</span>, you '
      '<span class="accent" style="font-weight:700">will miss</span> your date."',
      "If it doesn't leave, you will miss your date."),
     ('"<span class="accent" style="font-weight:700">Unless</span> I call, the plan stays the same."',
      'Unless I call, the plan stays the same.'),
     ('"I will call you <span class="accent" style="font-weight:700">as soon as</span> the port confirms."',
      'I will call you as soon as the port confirms.')],
    'rule14',
    ['Form', 'Use it for', 'Example'],
    [['If + present, will + verb', 'A real possibility in the future, and its result.',
      'If it <strong>leaves</strong> on Thursday, it <strong>will arrive</strong> on the 26th.'],
     ['will + verb + if + present', 'The same idea, result first. No comma.',
      'We <strong>will miss</strong> the launch if it <strong>arrives</strong> late.'],
     ['unless + present', 'If not. Only the exception.',
      '<strong>Unless</strong> I call, the plan stays the same.'],
     ['as soon as / when + present', 'The moment something happens.',
      'I will call you <strong>as soon as</strong> it <strong>arrives</strong>.'],
     ['might / can / imperative', 'Other results are possible too.',
      'If it is late, <strong>call</strong> me. If it rains, it <strong>might</strong> slow down.']],
    ('Never will after if. The if half is the condition, in the present. The will half is the '
     'result.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: which half is the condition? A resposta decide onde vai o will.',
    'Grammar Practice', 'Condition and', 'Result',
    'Say the full sentence, then click to compare',
    [('If the container ______ (arrive) after the 28th, we ______ (miss) the launch.',
      'If the container arrives after the 28th, we will miss the launch.'),
     ('______ we pay for air freight, the prints will not be in the stores.',
      'Unless we pay for air freight, the prints will not be in the stores.'),
     ('I ______ (call) you as soon as the port ______ (confirm).',
      'I will call you as soon as the port confirms.'),
     ('If we ______ (not have) enough buffer stock, the stores ______ (notice).',
      "If we don't have enough buffer stock, the stores will notice.")]))

S.append(L.s_dialogue(
    16, 4,
    'Diálogo (6 min): Bram, do escritório de Roterdã, holandês, o mesmo da aula 7. Clique Next '
    'Line a cada fala. Nas falas do FELIPE, peça que ELE fale primeiro, com o texto tapado. '
    'Aponte a fala 11: ele decide em voz alta, com a condição dentro da frase.',
    'Thursday,', 'or Next Week?',
    [('bram', 'B', 'dutch_m',
      'Felipe, the ship is still <span class="vocab-highlight">stuck</span> in Singapore.'),
     ('felipe', 'F', 'arthur', 'When will it leave?'),
     ('bram', 'B', 'dutch_m',
      'Probably on Thursday. If it leaves on Thursday, it will arrive on the 26th.'),
     ('felipe', 'F', 'arthur',
      'That is two days before our deadline. And if it does not leave on Thursday?'),
     ('bram', 'B', 'dutch_m', 'Then the next ship is a week later.'),
     ('felipe', 'F', 'arthur',
      'If it arrives a week later, we will miss the launch in forty stores.'),
     ('bram', 'B', 'dutch_m',
      'I understand. I can <span class="vocab-highlight">reroute</span> the container through '
      'another port.'),
     ('felipe', 'F', 'arthur', 'How much will that cost?'),
     ('bram', 'B', 'dutch_m', 'About fifteen percent more, and two more days.'),
     ('felipe', 'F', 'arthur',
      'Two more days does not help us. What about air '
      '<span class="vocab-highlight">freight</span> for part of it?'),
     ('bram', 'B', 'dutch_m', 'It is possible, but it is very expensive.'),
     ('felipe', 'F', 'arthur',
      'Then here is the plan. If it does not leave on Thursday, we will send only the new '
      'prints by air.')]))

S.append(L.s_comprehension(
    17, 4,
    'Comprehension (3 min): as perguntas são sobre o BRAM, não sobre ele. Ele responde de '
    'memória ANTES de clicar.',
    'Did You Catch It?', 'About', 'Bram',
    [('Where does Bram say the ship is?',
      'Still stuck in Singapore.'),
     ('What does he say will happen if the ship does not leave on Thursday?',
      'The next ship is a week later.'),
     ('How much more does the reroute cost, according to Bram?',
      'About fifteen percent more, and two more days.')]))

S.append(L.s_artifact(
    18, 4,
    'Artefato (4 min): o plano de contingência que ele mandaria ao diretor. Peça que ele LEIA em '
    'voz alta, transformando cada linha numa frase com if. A terceira pergunta é produção: exija '
    'a frase com unless.',
    'Real Document', 'The Contingency', 'Plan',
    'CONTINGENCY PLAN &mdash; SUMMER COLLECTION', 'OWNER: FELIPE DIAS',
    [('Deadline at the DC', 'October 28th'),
     ('Ship leaves Thursday', 'Arrives 26th &middot; no action'),
     ('Ship leaves next week', 'Arrives Nov 2nd &middot; launch at risk'),
     ('Action if late', 'New prints by air freight only'),
     ('Air freight cost', 'about 10x sea freight'),
     ('Basic items', 'Buffer stock for 2 weeks'),
     ('Reroute option', '+2 days &middot; +15% &middot; rejected'),
     ('Decision by', 'Thursday 6 p.m.')],
    [('What happens if the ship leaves on Thursday?',
      'It will arrive on the 26th, and they will not need to do anything.'),
     ('What will they do if the ship leaves next week?',
      'They will send only the new prints by air freight.'),
     ('Say the rule for the basic items with unless.',
      'Unless the delay is longer than two weeks, the buffer stock will cover the basic items.')]))

S.append(L.s_listening(
    19, 4,
    'Listening 2 (5 min): sotaque holandês, o mesmo Bram do diálogo, com a notícia do porto. '
    'LEIA AS PERGUNTAS COM ELE ANTES do play. A mensagem tem quatro condicionais &mdash; peça '
    'que ele repita uma inteira no fim. Toque duas vezes.',
    2, 'News from', 'Rotterdam',
    'The forwarder calls with two possible futures. Sound first, no text.',
    'a14_listening2.mp3', SLUG,
    [('If the ship leaves on Thursday, when will it arrive in Santos?',
      'On the 26th, so they will just make it.'),
     ('What does the reroute add?',
      'Two days, and about fifteen percent to the freight.'),
     ('What happens if Bram does not call?',
      'The plan stays the same.')]))

S.append(L.s_blocks(
    20, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as Tips. '
    'Exija a condição E a consequência em toda resposta, e pelo menos um knock-on effect.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    21, 6,
    'Transição prática (1 min): diga: Now you plan for the risk. Three rounds, less help each '
    'time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    22, 6,
    'Scenarios + Rephrase (5 min): nos cenários exija if, unless e as soon as. No rephrase ele '
    'une as duas ideias com a palavra entre parênteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    23, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('If the ship will leave on Thursday, it will arrive on the 26th.',
      'If the ship leaves on Thursday, it will arrive on the 26th.'),
     ('I will call you as soon as the port will confirm.',
      'I will call you as soon as the port confirms.'),
     ('Unless we don\'t pay for air freight, the stores won\'t have it.',
      "Unless we pay for air freight, the stores won't have it."),
     ('If it arrive late, we will miss the launch.',
      'If it arrives late, we will miss the launch.')]))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 1 &mdash; guiado (4 min): você é o diretor. Pergunte: what happens if it is '
    'late? Ele responde usando as chips, com datas.',
    'Role-Play 1 &mdash; Guided', 'What Happens', 'If It Is Late?',
    'Situation',
    'Your director asks about the late container. Explain the two possible dates, what will '
    'happen in each case, and what you will do.',
    ['if it leaves', 'it will arrive', 'if it does not', 'we will miss', 'as soon as']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é do financeiro e não quer pagar frete aéreo. '
    'Insista: it is ten times more expensive. Ele tem de defender a decisão com o knock-on '
    'effect.',
    'Role-Play 2 &mdash; Semi-Free', 'Ten Times More', 'Expensive',
    'Situation',
    'Finance does not want to pay for air freight. Explain what will happen if you do not, put '
    'a number on the knock-on effect, and propose the smallest option that protects the launch.',
    ['unless', 'knock-on effect', 'only the', 'if we wait']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos e conte quantas frases com if ele produziu. Diga o número no '
    'fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Choose a real risk in one of your areas: a late delivery, a machine that might break, a '
    'supplier that might fail. Explain what will happen if it goes wrong, the knock-on effect, '
    'and your contingency plan. Ninety seconds, no notes.',
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
    'câmera. São as cinco frases da próxima crise de abastecimento dele.',
    'Say It with', 'Confidence',
    ['If it leaves on Thursday, it will arrive on time.',
     'If it arrives late, we will miss the launch.',
     'Unless we pay for air freight, the stores will not have it.',
     'I will call you as soon as I hear from the port.',
     'We need a contingency plan before Friday.']))

S.append(L.s_checklist(
    29,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 14.',
    14,
    ['I can explain a risk and what will happen if it goes wrong.',
     'I use the present after if, and will in the result.',
     'I use unless when I mean if not.',
     'I never say as soon as it will arrive.',
     'I know the words: container, freight, collection, to be stuck, knock-on effect, '
     'contingency plan, buffer stock, to reroute.']))

S.append(L.s_badge(
    30,
    'Encerramento (2 min): diga: Lesson 14 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos sobre um risco real de uma área dele, com o plano de '
    'contingência, e mandar no WhatsApp. Próxima aula: If I Could Change One Thing.',
    14, 'If the Container Is Late',
    'You turned a late ship into a plan today, Felipe, before anybody had to panic.',
    'If I Could Change One Thing'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'If the Container Is Late -- Risk and Consequence',
    'short_title': 'If the Container Is Late',
    'menu_desc': ('Reading lesson: a container stuck at sea, a collection that cannot wait, and '
                  'the first conditional for every risk you plan for'),
    'grammar_point': 'first conditional',
    'characters': {'felipe': 'arthur', 'bram': 'dutch_m'},
    'phases': ['Five Weeks at Sea', 'Your Words', 'Read the Story', 'If, Unless, As Soon As',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=600&q=80',
    'desc': ('The words of a delay: container, freight, collection, to be stuck, knock-on '
             'effect, contingency plan, buffer stock, to reroute. Structure: the first '
             'conditional with if, unless and as soon as. Mission: explain a risk, its '
             'knock-on effect, and what you will do.'),
    'context_paras': [
        'The ship is still in Singapore. <strong>If it leaves</strong> on Thursday, it '
        '<strong>will arrive</strong> in Santos on the 26th, two days before our deadline. '
        '<strong>If it doesn\'t leave</strong>, the next ship is a week later, and we '
        '<strong>will miss</strong> the launch in forty stores. <strong>Unless</strong> we pay '
        'for air freight, the new prints <strong>won\'t</strong> be there for Black Friday. I '
        '<strong>will call</strong> the director <strong>as soon as</strong> the port '
        '<strong>confirms</strong>.',
        'Look at the verbs. Nothing has happened yet, but after <em>if</em>, <em>unless</em> and '
        '<em>as soon as</em> the verb is in the present: <em>leaves</em>, <em>pay</em>, '
        '<em>confirms</em>. The <strong>will</strong> lives in the other half of the sentence, '
        'the result. And <em>unless</em> already means <em>if not</em>, so it never takes a '
        'second negative.'],
    'context_quiz': [
        ('Why is it <em>If it leaves on Thursday</em> and not <em>If it will leave</em>?',
         [('Because after if, the condition takes the present, even about the future.', True),
          ('Because Thursday is very close, so the present is more natural there.', False),
          ('Because leave is irregular.', False)]),
        ('What does <em>Unless we pay for air freight</em> mean?',
         [('Because we are going to pay for air freight next week.', False),
          ('If we do not pay for air freight.', True),
          ('After we pay for air freight and the container finally arrives.', False)]),
        ('When will the writer call the director?',
         [('Tomorrow morning, before the port says anything.', False),
          ('On Thursday at six.', False),
          ('As soon as the port confirms.', True)]),
    ],
    'tip_title': 'The First Conditional',
    'tip_intro': ('A real possibility in the future, and what will happen because of it. The '
                  'condition takes the present; the result takes will.'),
    'tip_rows': [
        ['If + present, will + verb', 'Condition first, with a comma.',
         'If it <strong>leaves</strong> on Thursday, it <strong>will arrive</strong> on time.'],
        ['will + verb if + present', 'Result first, no comma.',
         'We <strong>will miss</strong> the launch if it <strong>arrives</strong> late.'],
        ['unless + present', 'If not. Never with a second negative.',
         '<strong>Unless</strong> we <strong>pay</strong> for air freight, the stores '
         'will not have it.'],
        ['as soon as / when + present', 'The moment something happens.',
         'I will call you <strong>as soon as</strong> the port <strong>confirms</strong>.'],
        ['Other results', 'might, can, should or an imperative also work.',
         'If it is late, <strong>call</strong> me.'],
        ['Negative', "If it <strong>doesn't</strong> leave, we <strong>won't</strong> make it."],
    ],
    'tip_note': ('The most common mistake is will in both halves. Only the result takes will: '
                 '<em>if it arrives</em>, never <em>if it will arrive</em>.'),
    'blanks': [
        ('If the ship ', 'leaves', 'Hint: one word. Present, third person, after if.',
         'If the ship leaves on Thursday, it will arrive on the 26th.',
         ' on Thursday, it will arrive on the 26th.'),
        ('If it arrives late, we ', 'will miss', 'Hint: two words. The result.',
         'If it arrives late, we will miss the launch.', ' the launch.'),
        ('', 'Unless', 'Hint: one word. It means if not.',
         'Unless we pay for air freight, the stores will not have it.',
         ' we pay for air freight, the stores will not have it.'),
        ('I will call you as soon as the port ', 'confirms',
         'Hint: one word. Present, after as soon as.',
         'I will call you as soon as the port confirms.', '.'),
        ('We need a ', 'contingency plan',
         'Hint: two words. A plan for when something goes wrong.',
         'We need a contingency plan before Friday.', ' before Friday.'),
        ('The ship has been ', 'stuck', 'Hint: one word. Unable to move.',
         'The ship has been stuck in Singapore for four days.', ' in Singapore for four days.'),
    ],
    'order_title': 'Put the Call in Order',
    'order_intro': 'Listen first, then put the five parts of the call in the order you hear '
                   'them.',
    'order': [
        (2, 'Then he says that if the ship leaves on Thursday, it will arrive on the 26th.'),
        (5, 'Finally, Felipe decides to send only the new prints by air freight.'),
        (3, 'After that, Felipe asks what will happen if it does not leave.'),
        (1, 'First, Bram tells Felipe that the container is stuck in Singapore.'),
        (4, 'Next, Bram offers to reroute the container through another port.'),
    ],
    'speech': [
        'If it leaves on Thursday, it will arrive on time.',
        'If it arrives late, we will miss the launch.',
        'Unless we pay for air freight, the stores will not have it.',
        'I will call you as soon as I hear from the port.',
        'We need a contingency plan before Friday.',
    ],
    'quiz_intro': 'A container is late and the launch is close. Choose the best thing to say.',
    'quiz': [
        ('Your director asks what happens if the container is late. You say:',
         [('If it will arrive late, we miss the launch.', False),
          ('If it arrives late, we will miss the launch in forty stores.', True),
          ('If it arrive late, we will missing the launch.', False)]),
        ('You want to say that air freight is the only way. You say:',
         [("Unless we don't pay for air freight, the stores won't have the new prints.", False),
          ("Unless we pay for air freight, they won't have it.", True),
          ('Unless we will pay for air freight, the stores will not have it.', False)]),
        ('A colleague asks when you will update the team. You say:',
         [('As soon as the port will confirm the date, I will send everybody a message.', False),
          ('I will update everybody as soon as the port confirms.', True),
          ('As soon as the port confirmed, I update.', False)]),
        ('You want to give an instruction for a possible problem. You say:',
         [('If you will hear from Bram, you call me immediately on my mobile phone.', False),
          ('If you heard from Bram, call me.', False),
          ('If you hear from Bram, call me.', True)]),
    ],
    'think': ('Think about one real risk in your areas this month: a delivery, a machine, a '
              'supplier or an event. Record about ninety seconds. Explain what will happen if it '
              'goes wrong, and then the knock-on effect: who else will feel it, and when. Then '
              'give your contingency plan with at least one unless and one as soon as. Finish '
              'with what will happen if everything goes well. Use at least four words from '
              'this lesson. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'The first conditional -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on if + present and will, with the common mistakes. Connection to Lesson '
         '14: every sentence of your contingency plan.',
         'Tip: pause after each example and make the same sentence about a delivery you are '
         'waiting for.',
         'https://www.youtube.com/watch?v=8VETylIxyhw', 'Watch on YouTube'),
        ('youtube', 'unless', 'Grammar Video',
         "'Unless' vs 'as long as' -- English In A Minute, BBC Learning English",
         'One minute on unless, and why it never takes a second negative. Connection to Lesson '
         '14: the sentence about the air freight.',
         'Tip: make two unless sentences about your week, then say them out loud.',
         'https://www.youtube.com/watch?v=Or_Zm7QdSgc', 'Watch on YouTube'),
        ('video', 'shipping', 'Documentary',
         "How ocean shipping works (and why it's broken) -- Wendover Productions",
         'A documentary about the ships, ports and containers behind every store. Connection to '
         'Lesson 14: the five weeks at sea in the reading, explained from the inside.',
         'Tip: watch with English subtitles and write down three if sentences you hear or can '
         'make about it.',
         'https://www.youtube.com/watch?v=8d5d_HXGeMA', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
