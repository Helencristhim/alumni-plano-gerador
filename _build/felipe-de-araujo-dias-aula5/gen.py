#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 5 do Felipe de Araujo Dias — What Went Wrong at the DC.
Past continuous vs past simple. Modelo de FALA (aula IMPAR, REGRA 29).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 5

IMG_TITLE = 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1553413077-190dd305871c?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_CALL = 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Distribution center', 'the large building where goods are sorted before they go to the stores',
     'The distribution center loads trucks for forty-two stores every night.'),
    ('Pallet', 'the wooden base that goods are stacked on so a machine can move them',
     'Nine pallets were waiting at the door when the line stopped.'),
    ('Forklift', 'the small vehicle that lifts and moves heavy loads inside a building',
     'A forklift hit the sensor arm at ten past two.'),
    ('To break down', 'to stop working, usually a machine or a vehicle',
     'The conveyor broke down in the middle of the night shift.'),
    ('Downtime', 'the period when work stops because something is not working',
     'Four hours of downtime cost us nine trucks.'),
    ('Backlog', 'the work that piled up because it was not done on time',
     'We cleared the backlog by two in the afternoon.'),
    ('Root cause', 'the real reason behind a problem, not the first thing you see',
     'The forklift was the accident. The root cause was the missing guard.'),
    ('To escalate', 'to pass a problem to somebody more senior when you cannot solve it',
     'The supervisor escalated it to me at three in the morning.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Distribution center', 'e'], ['2', 'Pallet', 'b'],
                   ['3', 'Forklift', 'g'], ['4', 'To break down', 'a'],
                   ['5', 'Downtime', 'h'], ['6', 'Backlog', 'c'],
                   ['7', 'Root cause', 'd'], ['8', 'To escalate', 'f']],
         'defs': [['a', 'To stop working, usually a machine or a vehicle'],
                  ['b', 'The wooden base that goods are stacked on so a machine can move them'],
                  ['c', 'The work that piled up because it was not done on time'],
                  ['d', 'The real reason behind a problem, not the first thing you see'],
                  ['e', 'The large building where goods are sorted before they go to the stores'],
                  ['f', 'To pass a problem to somebody more senior when you cannot solve it'],
                  ['g', 'The small vehicle that lifts and moves heavy loads inside a building'],
                  ['h', 'The period when work stops because something is not working']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: downtime is what the clock lost, backlog is what the work '
                  'gained. Four hours of one always becomes nine trucks of the other.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['At ten past two the night shift was loading trucks at the ', ['1'],
                   ' when a ', ['2'], ' turned too fast and hit a sensor. The conveyor ',
                   ['3'], ' immediately, and thirty ', ['4'],
                   ' stopped where they were. We had four hours of ', ['5'],
                   ' and a ', ['6'], ' of nine trucks by morning. The supervisor ', ['7'],
                   ' it to me at three. The ', ['8'],
                   ' was not the driver: nobody had put the guard back after the layout change.'],
         'bank': ['distribution center', 'forklift', 'broke down', 'pallets', 'downtime',
                  'backlog', 'escalated', 'root cause']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Your manager calls at seven in the morning and asks what happened '
                           'during the night. Give the background first, then the event, then '
                           'the consequence. Ninety seconds.'],
            ['Scenario 2', 'A supplier asks why their delivery was refused at the door. '
                           'Explain what was happening at the time, without blaming their driver.'],
            ['Scenario 3', 'Somebody outside operations asks what a root cause is. Explain it '
                           'using the story of the sensor and the missing guard.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Join the two sentences. The long action goes in the continuous.',
         'items': [['The team loaded trucks. The conveyor stopped. (while)', 'one sentence'],
                   ['I talked to Marco. My phone died. (when)', 'one sentence'],
                   ['It rained hard. We closed the dock doors. (while)', 'one sentence'],
                   ['The engineer looked at the sensor. He found the real cause. (while)',
                    'one sentence']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'It is seven in the morning. Your manager asks: what happened last '
                          'night? You have thirty seconds.',
             'tips': ['Background first: the team was loading trucks for forty-two stores.',
                      'Then the event: at ten past two the conveyor broke down.']},
            {'situation': 'She asks why nobody called her before three in the morning.',
             'tips': ['Say what people were doing instead: the supervisor was trying to restart it.',
                      'Then the moment it changed: when it did not restart, he escalated it.']},
            {'situation': 'She asks how bad the backlog was and when it was clear.',
             'tips': ['Two numbers and one time. Nine trucks, four hours, clear by two.',
                      'Do not say more or less. Say the number you know.']},
            {'situation': 'She asks what the root cause was, and you know the first answer is '
                          'not the real one.',
             'tips': ['Separate the accident from the cause: the forklift hit it, but the guard '
                      'was missing.',
                      'Say when the guard disappeared: after the November layout change.']},
            {'situation': 'She asks what you are doing so that it does not happen again. Answer '
                          'in two sentences and stop.',
             'tips': ['One action, one date, one owner.',
                      'Finish and stop talking. Silence is not your problem to fill.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['While the team was loading trucks, the conveyor stopped.',
                  'I was talking to Marco when my phone died.',
                  'While it was raining hard, we closed the dock doors.',
                  'While the engineer was looking at the sensor, he found the real cause.'],
         'note': ('The continuous holds the door open and the simple walks through it. Swap '
                  'them and the story stops making sense.')},
    ],
}

LISTENINGS = [
    {'file': 'a5_listening1.mp3', 'voice': 'ellen',
     'text': ('Felipe, this is Karen, night supervisor. It is twenty past three and I am '
              'escalating this to you. At about ten past two the team was loading the trucks '
              'for the north stores when conveyor three stopped. A forklift was turning at the '
              'end of the aisle and it hit the sensor arm. Nobody was hurt. We tried to restart '
              'the line three times and it did not come back, so I called the engineer. We have '
              'thirty pallets sitting on the floor and nine trucks waiting outside. I am '
              'sending the drivers to the second dock while we wait. Call me when you see this.')},
    {'file': 'a5_listening2.mp3', 'voice': 'italian_m',
     'text': ('Felipe, Marco here, from the equipment team. I finished the inspection twenty '
              'minutes ago. The forklift did not break the sensor. The sensor was working '
              'perfectly. What broke was the arm that holds it, and that arm was standing there '
              'with no guard around it. When I checked the photos from November, the guard was '
              'in place. Somebody removed it during the layout change and nobody put it back. '
              'So the root cause is the process, not the driver. I am sending you the report '
              'today, and I can install two new guards on Friday if you confirm this morning.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l5]', 'file': 'pc5_order_incident.mp3', 'voice': 'arthur',
     'text': ('First, the night shift was loading the trucks for the north stores. Then a '
              'forklift turned at the end of the aisle and hit the sensor arm. After that, the '
              'supervisor tried to restart the line three times and it did not come back. Next, '
              'she escalated the problem to Felipe at twenty past three. Finally, the engineer '
              'inspected the machine and found that the guard was missing since November.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. Este slide abre a tela e '
    'd&aacute; o tema: contar um incidente de opera&ccedil;&atilde;o em noventa segundos, que '
    '&eacute; exatamente o que a chefia dele pede em ingl&ecirc;s.',
    'Chapter 1: The Call at Three in the Morning', 'What Went Wrong', 'at the DC',
    'Telling a problem in ninety seconds, in the right order', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 4 (3 min): na aula 4 ele contou uma viagem inteira no passado '
    'simples. Fa&ccedil;a a ponte: hoje o passado simples sozinho n&atilde;o basta. Pe&ccedil;a '
    'que ele conte o problema e ESCUTE se ele consegue separar o fundo do acontecimento. '
    'N&atilde;o corrija ainda &mdash; anote.',
    'A List Is Not', 'a Story',
    'Last time you told a trip with one tense and it worked. A problem is different. Somebody '
    'has to know what was already happening before the thing went wrong, or the story sounds '
    'like a list of facts with no cause.',
    'Think of one thing that went wrong at work this year. Tell me in four sentences.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as tr&ecirc;s miss&otilde;es. Diga que no fim ele conta o '
    'incidente inteiro sem apoio, cronometrado. Passe ao pr&oacute;ximo.',
    ['Eight words that only exist inside a distribution center.',
     'Separate the background from the event, with was doing and did.',
     'Report a real incident in ninety seconds: what, when, how bad, and why.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of a', 'Bad Night',
    '8 words you need when the line stops', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'pallet: Is the pallet the goods or the base under them? (A base.) CCQ para to break down: '
    'Does a person break down or a machine? (Aqui, a m&aacute;quina.) Pron&uacute;ncia: '
    'forklift tem stress na primeira s&iacute;laba (FORK-lift).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para root cause: If the forklift hit '
    'the sensor, is the forklift the root cause? (N&atilde;o &mdash; a falta da prote&ccedil;'
    '&atilde;o &eacute;.) CCQ para to escalate: Do I escalate to my team or to my manager? (Ao '
    'gestor.) Este par de palavras &eacute; o vocabul&aacute;rio de reuni&atilde;o de crise '
    'dele.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte para o gap-fill.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Este par&aacute;grafo &eacute; o incidente completo '
    '&mdash; ele vai reus&aacute;-lo tr&ecirc;s vezes hoje.',
    'Use the Words', 'Four Hours in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: Two tenses, two jobs. One holds the '
    'scene open, the other closes it. Passe ao pr&oacute;ximo.',
    'Chapter 3: The Background and the Event', 'What Was Happening', 'When It Happened',
    'Past continuous for the scene, past simple for the moment', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Two '
    'of these actions were long and two were instant. Which is which, and how does the verb '
    'show it? S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In While they were loading, the '
    'conveyor stopped &mdash; which action started first? (O carregamento.) Which one finished '
    'first? (A parada da esteira &eacute; instant&acirc;nea.)',
    'past continuous vs past simple',
    [('"At two in the morning the night shift <span class="accent" style="font-weight:700">was loading</span> trucks."',
      'At two in the morning the night shift was loading trucks.'),
     ('"While they <span class="accent" style="font-weight:700">were loading</span>, the conveyor <span class="accent" style="font-weight:700">stopped</span>."',
      'While they were loading, the conveyor stopped.'),
     ('"A forklift <span class="accent" style="font-weight:700">hit</span> the sensor arm."',
      'A forklift hit the sensor arm.'),
     ('"Nobody <span class="accent" style="font-weight:700">was watching</span> that corner."',
      'Nobody was watching that corner.')],
    'rule5',
    ['Form', 'Use it for', 'Example'],
    [['Past continuous: was / were + -ing',
      'The long action. The background. What was already in progress.',
      'The team <strong>was loading</strong> trucks.'],
     ['Past simple', 'The short action that interrupts, and the sequence after it.',
      'The conveyor <strong>stopped</strong>. A forklift <strong>hit</strong> the arm.'],
     ['while and when', 'while goes with the long action, when goes with the short one.',
      '<strong>While</strong> they were loading, the conveyor stopped.'],
     ['Two long actions', 'Both in the continuous, when they happened at the same time.',
      'While I <strong>was calling</strong> Marco, the team <strong>was clearing</strong> the aisle.'],
     ['Verbs with no -ing',
      'know, want, need, believe, understand describe a state, not an action. '
      '<em>I <strong>knew</strong> the cause at six</em>, never <em>I was knowing</em>.']],
    ('The continuous holds the door open and the simple walks through it. A report with only '
     'the simple is a list; a report with only the continuous never gets to the point.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. '
    'Toggle: clicar de novo fecha. Pergunte a cada item POR QUE cada verbo est&aacute; na forma '
    'que est&aacute; &mdash; a explica&ccedil;&atilde;o dele vale mais que o acerto.',
    'Grammar Practice', 'Background or', 'Event?',
    'Say the full sentence, then click to compare',
    [('While the team ______ (load) the trucks, the conveyor ______ (stop).',
      'While the team was loading the trucks, the conveyor stopped.'),
     ('The supervisor ______ (try) to restart the line when I ______ (call) her.',
      'The supervisor was trying to restart the line when I called her.'),
     ('Nobody ______ (watch) that corner at two in the morning.',
      'Nobody was watching that corner at two in the morning.'),
     ('I ______ (know) the root cause before the engineer ______ (send) the report.',
      'I knew the root cause before the engineer sent the report.')]))

S.append(L.s_mistake(
    12, 3,
    'Common mistake (3 min): os tr&ecirc;s erros que aparecem quando brasileiro conta incidente '
    'em ingl&ecirc;s. O terceiro &eacute; o mais teimoso: verbo de estado n&atilde;o vai para o '
    '-ing. Pe&ccedil;a que ele leia as vers&otilde;es CERTAS duas vezes cada.',
    [('While I was call Marco, the line stopped.',
      'While I was calling Marco, the line stopped.'),
     ('While the conveyor stopped, we were loading.',
      'While we were loading, the conveyor stopped.'),
     ('I was knowing the root cause at six.', 'I knew the root cause at six.')],
    ('Ask yourself which action was long. That one takes the -ing, and the other one does not, '
     'no matter which one you say first.')))

S.append(L.s_listening(
    13, 3,
    'Listening 1 (5 min): a supervisora do turno da noite, ingl&ecirc;s americano, falando com '
    'pressa. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. O &aacute;udio est&aacute; '
    'cheio de past continuous de prop&oacute;sito &mdash; n&atilde;o explique ainda, s&oacute; '
    'deixe ele ouvir. Toque duas vezes.',
    1, 'The Night Supervisor', 'Escalates',
    'A voicemail left at twenty past three in the morning. Sound first, no text.',
    'a5_listening1.mp3', SLUG,
    [('What was the team doing when the conveyor stopped?',
      'They were loading the trucks for the north stores.'),
     ('What did Karen try before she called the engineer?',
      'She tried to restart the line three times and it did not come back.'),
     ('What is waiting outside, and what is she doing about it?',
      'Nine trucks. She is sending the drivers to the second dock.')]))

S.append(L.s_chapter(
    14, 4,
    'Transi&ccedil;&atilde;o di&aacute;logo (1 min): diga: Now the engineer. You are you, and '
    'Marco flew in from Milan for the equipment contract. Passe ao pr&oacute;ximo.',
    'Chapter 4: Finding the Real Cause', 'It Was Never', 'the Driver',
    'The engineer walks you through what he found', IMG_CALL))

S.append(L.s_dialogue(
    15, 4,
    'Di&aacute;logo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, pe&ccedil;a que '
    'ELE fale primeiro, com o texto tapado. Marco tem sotaque italiano de prop&oacute;sito. '
    'Repare que a fala 7 do Felipe usa uma pergunta indireta da aula 3 &mdash; aponte isso.',
    'The Engineer and', 'the Sensor',
    [('felipe', 'F', 'arthur',
      'Marco, thank you for coming so early. What were you doing when the call came in?'),
     ('marco', 'M', 'italian_m',
      'I was driving to another site, so I turned around. I arrived at five and started the '
      'inspection.'),
     ('felipe', 'F', 'arthur',
      'And what did you find? Karen told me a '
      '<span class="vocab-highlight">forklift</span> hit the sensor.'),
     ('marco', 'M', 'italian_m',
      'The forklift hit the arm, not the sensor. The sensor was working perfectly when I tested it.'),
     ('felipe', 'F', 'arthur',
      'So the machine did not <span class="vocab-highlight">break down</span> by itself.'),
     ('marco', 'M', 'italian_m',
      'No. The arm was standing there with no guard around it. In the November photos the guard '
      'was in place.'),
     ('felipe', 'F', 'arthur',
      'I see. Could you tell me who removed it during the layout change?'),
     ('marco', 'M', 'italian_m',
      'I cannot. I only know that nobody put it back, and nobody checked. That is your '
      '<span class="vocab-highlight">root cause</span>.'),
     ('felipe', 'F', 'arthur',
      'Four hours of <span class="vocab-highlight">downtime</span> for a missing guard. What do '
      'you need from me?'),
     ('marco', 'M', 'italian_m',
      'A confirmation this morning. If you confirm, I install two new guards on Friday, while '
      'the line is off anyway.'),
     ('felipe', 'F', 'arthur',
      'You have it. Send me the report today and I will escalate the process part myself.'),
     ('marco', 'M', 'italian_m',
      'Good. And Felipe, the driver was not the problem. Please say that in the meeting.')]))

S.append(L.s_comprehension(
    16, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre o MARCO, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar. Se errar, volte ao di&aacute;logo e toque a fala.',
    'Did You Catch It?', 'About', 'Marco',
    [('What was Marco doing when the call came in?',
      'He was driving to another site, so he turned around.'),
     ('What exactly did the forklift hit, and what was still working?',
      'It hit the arm. The sensor itself was working perfectly.'),
     ('What does Marco need from Felipe, and by when?',
      'A confirmation this morning, so he can install two guards on Friday.')]))

S.append(L.s_artifact(
    17, 4,
    'Artefato (4 min): o relat&oacute;rio de incidente que ele escreveria de verdade. '
    'Pe&ccedil;a que ele LEIA em voz alta e depois responda. Na primeira pergunta exija a frase '
    'com while, n&atilde;o s&oacute; a informa&ccedil;&atilde;o.',
    'Real Document', 'The Incident', 'Report',
    'INCIDENT REPORT', 'DC-SP-0219',
    [('Site', 'Distribution center &mdash; Guarulhos'),
     ('Reported by', 'Felipe de Ara&uacute;jo Dias'),
     ('Date and time', 'February 19 &middot; 02:10'),
     ('Background', 'Night shift was loading trucks for 42 stores'),
     ('Event', 'Forklift hit the sensor arm on conveyor 3'),
     ('Downtime', '4 hours 20 minutes'),
     ('Backlog', '9 trucks &middot; cleared by 14:00'),
     ('Root cause', 'Sensor guard removed in November and never replaced'),
     ('Escalated to', 'Operations Director &middot; 03:20')],
    [('Say the Background and the Event as one sentence.',
      'While the night shift was loading trucks for forty-two stores, a forklift hit the sensor '
      'arm on conveyor three.'),
     ('Why is the forklift not the root cause?',
      'Because the guard was already missing. The forklift was the accident, not the reason.'),
     ('How long was the gap between the event and the escalation?',
      'One hour and ten minutes. It happened at 02:10 and reached the director at 03:20.')]))

S.append(L.s_listening(
    18, 4,
    'Listening 2 (5 min): sotaque italiano, o mesmo Marco do di&aacute;logo. LEIA AS PERGUNTAS '
    'COM ELE ANTES do play. Este &aacute;udio tem a mesma informa&ccedil;&atilde;o do '
    'di&aacute;logo em outra ordem &mdash; pergunte no fim o que ele ouviu de novo. Toque duas '
    'vezes.',
    2, 'The Inspection', 'Report',
    'The engineer sums up what he found, in one message. Sound first, no text.',
    'a5_listening2.mp3', SLUG,
    [('What was working perfectly, and what broke?',
      'The sensor was working perfectly. The arm that holds it broke.'),
     ('What did the November photos show?',
      'That the guard was in place before the layout change.'),
     ('What does Marco offer, and what does he need first?',
      'Two new guards on Friday, if Felipe confirms this morning.')]))

S.append(L.s_blocks(
    19, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez, e todas s&atilde;o a MESMA '
    'reuni&atilde;o, em sequ&ecirc;ncia. Ele responde EM VOZ ALTA antes de abrir as Tips. Na '
    '&uacute;ltima, exija que ele PARE de falar depois de duas frases &mdash; ele tende a '
    'preencher o sil&ecirc;ncio.',
    'Chapter 5: Real Talk', 'The Seven', 'A.M. Call', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    20, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you tell it. Three rounds, less '
    'help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    21, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija fundo, evento e '
    'consequ&ecirc;ncia nessa ordem. No rephrase ele junta as duas frases numa s&oacute;, com '
    'while ou when. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    22, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('The night shift was load the trucks.', 'The night shift was loading the trucks.'),
     ('We was working when it happened.', 'We were working when it happened.'),
     ('While the conveyor stopped, we were loading pallets.',
      'While we were loading pallets, the conveyor stopped.'),
     ('I was seeing the report at seven.', 'I saw the report at seven.')]))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; a diretora de opera&ccedil;&otilde;es '
    'e est&aacute; com pressa. Interrompa uma vez com So what actually happened? se ele '
    'come&ccedil;ar pelo detalhe t&eacute;cnico em vez do fundo.',
    'Role-Play 1 &mdash; Guided', 'The Seven', 'A.M. Report',
    'Situation',
    'Report the incident to your director in four sentences: what the team was doing, what '
    'happened, how bad it was, and what you are doing about it.',
    ['was loading', 'at ten past two', 'four hours of downtime', 'nine trucks',
     'root cause', 'escalated']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; o dono da transportadora e '
    'est&aacute; irritado. Pressione uma vez com My drivers waited four hours. Who pays for '
    'that? e observe se ele mant&eacute;m o passado contínuo no fundo da hist&oacute;ria.',
    'Role-Play 2 &mdash; Semi-Free', 'The Carrier', 'Wants Answers',
    'Situation',
    'The transport company complains that nine trucks waited all night. Explain what was '
    'happening, what went wrong, and what you changed. Do not blame the forklift driver.',
    ['while', 'nobody was hurt', 'what we changed']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa, nem para corrigir. Cronometre noventa segundos e anote os erros de tempo verbal '
    'para a pr&oacute;xima aula. CELEBRE no fim.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Tell the whole night to a colleague in another country who knows nothing about the site: '
    'what was happening, what went wrong, how long the line was down, what the real cause was, '
    'and what happens on Friday. Ninety seconds, no notes.',
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
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco frases da pr&oacute;xima '
    'reuni&atilde;o de crise dele.',
    'Say It with', 'Confidence',
    ['The team was loading trucks when the conveyor stopped.',
     'Nobody was hurt, and the line was down for four hours.',
     'The forklift was the accident. The root cause was the missing guard.',
     'We cleared the backlog by two in the afternoon.',
     'Let me give you the background first, and then the numbers.']))

S.append(L.s_checklist(
    28,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 5 e liberam o quinto stamp.',
    5,
    ['I can give the background before the event, without being asked.',
     'I use was doing for the long action and did for the short one.',
     'I never put a state verb like know or want in the -ing form.',
     'I can report an incident in ninety seconds and then stop talking.',
     'I know the words: distribution center, pallet, forklift, break down, downtime, backlog, '
     'root cause, escalate.']))

S.append(L.s_badge(
    29,
    'Encerramento (2 min): diga: Lesson 5 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar noventa segundos contando um problema real desta semana, come&ccedil;ando pelo '
    'fundo, e mandar no WhatsApp antes da pr&oacute;xima aula. Pr&oacute;xima aula: Have You '
    'Ever...?',
    5, 'What Went Wrong at the DC',
    'You told four hours of a bad night in ninety seconds, Felipe, and the order was right.',
    'Have You Ever...?'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'What Went Wrong at the DC -- Reporting a Problem',
    'short_title': 'What Went Wrong at the DC',
    'menu_desc': ('Speaking lesson: a conveyor stops at two in the morning, and the two tenses '
                  'that turn four hours of chaos into ninety seconds of report'),
    'grammar_point': 'past continuous vs past simple',
    'characters': {'felipe': 'arthur', 'marco': 'italian_m'},
    'phases': ['The Call at Three in the Morning', 'Your Words',
               'The Background and the Event', 'Finding the Real Cause', 'Real Talk',
               'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80',
    'desc': ('The words of a bad night in operations: distribution center, pallet, forklift, to '
             'break down, downtime, backlog, root cause, to escalate. Structure: past '
             'continuous for the background and past simple for the event. Mission: report a '
             'real incident in ninety seconds, in the right order.'),
    'context_paras': [
        'At ten past two the night shift <strong>was loading</strong> the trucks for the north '
        'stores. Two people <strong>were working</strong> at the end of the aisle and nobody '
        '<strong>was watching</strong> the corner. While they '
        '<strong>were loading</strong>, a forklift <strong>turned</strong> too fast and '
        '<strong>hit</strong> the sensor arm on conveyor three. The line '
        '<strong>stopped</strong> immediately.',
        'The supervisor <strong>tried</strong> to restart it three times. While she '
        '<strong>was trying</strong>, nine trucks <strong>arrived</strong> at the dock and '
        '<strong>waited</strong>. At twenty past three she <strong>escalated</strong> it. The '
        'engineer <strong>inspected</strong> the machine at five, and while he '
        '<strong>was checking</strong> the November photos he <strong>found</strong> the real '
        'cause: somebody <strong>removed</strong> a guard during the layout change and nobody '
        '<strong>put</strong> it back. I <strong>knew</strong> the answer before the report '
        'arrived, but I <strong>waited</strong> for it anyway.'],
    'context_quiz': [
        ('Why is it <em>while they were loading, a forklift turned</em> and not '
         '<em>while they loaded</em>?',
         [('Because loading is the long action that was already in progress. The forklift '
           'interrupts it.', True),
          ('Because load is an irregular verb and needs the -ing form.', False),
          ('Because the sentence starts with while, and while always takes -ing.', False)]),
        ('Why does the text say <em>I knew the answer</em> and not <em>I was knowing</em>?',
         [('Because know is a state, not an action, so it does not take the -ing form.', True),
          ('Because the sentence is in the first person.', False),
          ('Because knowing something is always short.', False)]),
        ('What does the continuous add that the simple alone would not?',
         [('It makes the sentence longer and more polite.', False),
          ('It shows what was already happening, so the reader understands the cause and not '
           'just the order of events.', True),
          ('It shows that the action never finished.', False)]),
    ],
    'tip_title': 'Past Continuous and Past Simple',
    'tip_intro': ('Two tenses, two jobs. One paints the scene and the other moves the story. A '
                  'good incident report needs both, in that order.'),
    'tip_rows': [
        ['was / were + -ing', 'The long action, already in progress when something happened.',
         'The team <strong>was loading</strong> trucks.'],
        ['Past simple', 'The short action that interrupts, and everything that follows it.',
         'A forklift <strong>hit</strong> the arm. The line <strong>stopped</strong>.'],
        ['while + continuous',
         'Marks the background. <em>While the team was loading, the conveyor stopped.</em>'],
        ['when + simple',
         'Marks the moment. <em>The supervisor was trying to restart it when I called.</em>'],
        ['Two continuous',
         'Two long actions at the same time: <em>While I was calling Marco, the team was '
         'clearing the aisle.</em>'],
        ['State verbs',
         'know, want, need, understand, believe never take -ing: <em>I <strong>knew</strong> '
         'the cause</em>, never <em>I was knowing</em>.'],
    ],
    'tip_note': ('Before you speak, ask which action was long. That one takes was doing. '
                 'Everything else takes the simple past, and the order you say them in does not '
                 'change that.'),
    'blanks': [
        ('At two in the morning the team ', 'was loading',
         'Hint: two words. The long action that was already in progress.',
         'At two in the morning the team was loading trucks.', ' trucks.'),
        ('While they were loading, the conveyor ', 'stopped',
         'Hint: the short action that interrupts, so past simple.',
         'While they were loading, the conveyor stopped.', '.'),
        ('The supervisor ', 'was trying',
         'Hint: two words. She was in the middle of it when the phone rang.',
         'The supervisor was trying to restart the line.', ' to restart the line.'),
        ('Four hours of ', 'downtime', 'Hint: one word. The time when work stops.',
         'Four hours of downtime cost us nine trucks.', ' cost us nine trucks.'),
        ('I ', 'knew', 'Hint: a state verb, so no -ing. The past of know.',
         'I knew the root cause before the report arrived.',
         ' the root cause before the report arrived.'),
        ('She ', 'escalated', 'Hint: regular verb, add -ed. To pass it to somebody more senior.',
         'She escalated the problem at twenty past three.',
         ' the problem at twenty past three.'),
    ],
    'order_title': 'Put the Night in Order',
    'order_intro': 'Listen first, then put the five parts of the night in the order you hear them.',
    'order': [
        (2, 'Then a forklift turned at the end of the aisle and hit the sensor arm.'),
        (5, 'Finally, the engineer inspected the machine and found that the guard was missing '
            'since November.'),
        (1, 'First, the night shift was loading the trucks for the north stores.'),
        (4, 'Next, she escalated the problem to Felipe at twenty past three.'),
        (3, 'After that, the supervisor tried to restart the line three times and it did not '
            'come back.'),
    ],
    'speech': [
        'The team was loading trucks when the conveyor stopped.',
        'Nobody was hurt, and the line was down for four hours.',
        'The forklift was the accident. The root cause was the missing guard.',
        'We cleared the backlog by two in the afternoon.',
        'Let me give you the background first, and then the numbers.',
    ],
    'quiz_intro': 'Something went wrong last night. Choose the best thing to say.',
    'quiz': [
        ('Your director asks what happened. The clearest first sentence is:',
         [('A forklift hit a sensor and everything stopped.', False),
          ('At two in the morning the team was loading trucks when the conveyor stopped.', True),
          ('While the conveyor stopped, the team was loading trucks.', False)]),
        ('She asks what the supervisor did before calling you. You say:',
         [('She was tried to restart the line three times.', False),
          ('She tried to restart the line three times, and then she escalated it.', True),
          ('She is trying to restart the line three times.', False)]),
        ('She asks when you understood the real cause. You say:',
         [('I was knowing it at six, before the report.', False),
          ('I knew it at six, before the report arrived.', True),
          ('I was known it at six.', False)]),
        ('The carrier asks why nine trucks waited. The most useful answer is:',
         [('It was not our fault. The forklift driver did it.', False),
          ('While we were clearing the line, the trucks arrived. We moved them to the second '
           'dock and cleared the backlog by two.', True),
          ('The trucks were waiting because they were waiting outside.', False)]),
    ],
    'think': ('Think about one real problem at work in the last six months. Record about ninety '
              'seconds. Start with the background: what was already happening, and who was '
              'doing what. Then say what went wrong, in the past simple, and how long it '
              'lasted. Then separate the accident from the root cause. Finish with one thing '
              'that changed afterwards. Use at least four words from this lesson, and at least '
              'two sentences with while. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"Past simple and past continuous" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on exactly the pair you practised today, including when to use while and '
         'when to use when. Connection to Lesson 5: it drills the choice you have to make in '
         'the first sentence of every incident report.',
         'Tip: after each example, say out loud which action was long. If you cannot answer, '
         'rewind ten seconds.',
         'https://www.youtube.com/watch?v=uTB5I8V9Eog', 'Watch on YouTube'),
        ('video', 'problems', 'Video Lesson',
         '"Talking about problems and difficulties" -- Derek Callan, Business English',
         'The vocabulary people actually use at work when something is not working, from a '
         'small hiccup to a full stop. Connection to Lesson 5: it gives you the ten phrases '
         'that sit between broke down and root cause.',
         'Tip: choose three phrases you do not have in Portuguese yet, and write one sentence '
         'about your own site with each.',
         'https://www.youtube.com/watch?v=Xhwebiqg4VQ', 'Watch on YouTube'),
        ('video', 'postmortem', 'Video Lesson',
         'How to run a project post-mortem meeting',
         'A short, practical walkthrough of the meeting that happens after something fails, and '
         'the questions that separate the accident from the cause. Connection to Lesson 5: this '
         'is the meeting where the English you practised today gets used.',
         'Tip: watch it thinking about the missing guard. Which of their questions would have '
         'found it in November?',
         'https://www.youtube.com/watch?v=foJR-UxEY4w', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
