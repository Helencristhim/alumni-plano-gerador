#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 7 do Felipe de Araujo Dias — Since I Joined the Company.
Present perfect vs past simple, com for e since. Modelo de FALA (aula IMPAR, REGRA 29).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 7

IMG_TITLE = 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_CALL = 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('To join', 'to start working at a company',
     'I joined the company in March 2016.'),
    ('Career path', 'the sequence of roles a person moves through over the years',
     'My career path did not start in operations. It started in a law firm.'),
    ('To be promoted', 'to move to a more senior role in the same company',
     'I was promoted twice, in 2018 and in 2021.'),
    ('To take over', 'to start being responsible for something that somebody else had',
     'I took over the fourth area three years ago.'),
    ('Scope', 'the range of things a role or a project covers',
     'The scope has doubled since the merger.'),
    ('Headcount', 'the number of people who work in a team or a company',
     'We have run the night shift with half the headcount since January.'),
    ('Milestone', 'an important point that marks real progress in a project or a career',
     'Opening the second distribution center was the milestone of my career.'),
    ('Track record', 'everything a person or a company has achieved so far, seen as proof',
     'Nobody asks for your opinion. They ask for your track record.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'To join', 'c'], ['2', 'Career path', 'f'],
                   ['3', 'To be promoted', 'a'], ['4', 'To take over', 'h'],
                   ['5', 'Scope', 'b'], ['6', 'Headcount', 'g'],
                   ['7', 'Milestone', 'd'], ['8', 'Track record', 'e']],
         'defs': [['a', 'To move to a more senior role in the same company'],
                  ['b', 'The range of things a role or a project covers'],
                  ['c', 'To start working at a company'],
                  ['d', 'An important point that marks real progress'],
                  ['e', 'Everything a person or a company has achieved so far, seen as proof'],
                  ['f', 'The sequence of roles a person moves through over the years'],
                  ['g', 'The number of people who work in a team or a company'],
                  ['h', 'To start being responsible for something that somebody else had']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a milestone is one point, a track record is all of them '
                  'together. Nobody is hired for a milestone.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['I ', ['1'], ' the company in 2016, and my ', ['2'],
                   ' since then has been faster than I expected. I ', ['3'],
                   ' twice, in 2018 and in 2021, and I ', ['4'],
                   ' the fourth area three years ago. The ', ['5'],
                   ' of the job has doubled since the merger, and the ', ['6'],
                   ' under me went from ninety people to three hundred and ten. The real ',
                   ['7'], ' was the second distribution center. That is the only thing on my ',
                   ['8'], ' that took two years and cost me every Saturday.'],
         'bank': ['joined', 'career path', 'was promoted', 'took over', 'scope',
                  'headcount', 'milestone', 'track record']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Somebody at an event asks how long you have been in your role and '
                           'what you did before. Answer in five sentences, and make sure the '
                           'finished parts and the unfinished parts use different tenses.'],
            ['Scenario 2', 'A colleague from another country asks what has changed in your '
                           'company since the merger. Give three changes, all still true today.'],
            ['Scenario 3', 'Somebody asks what the hardest year of your career was, and why. '
                           'Tell it as a finished story, and then say what you have not '
                           'repeated since.'],
        ]},
        {'kind': 'rephrase', 'title': 'Say each sentence again with the other word.',
         'items': [['I have worked here for ten years.', 'since'],
                   ['I have been a director since 2021.', 'for'],
                   ['I have known him since we opened the second center.', 'for'],
                   ['We have used this supplier for six months.', 'since']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'Somebody at a fair asks how long you have been in your role. Answer '
                          'and add what you did before.',
             'tips': ['Still true today, so have been plus since or for.',
                      'What you did before is finished, so it takes the past simple.']},
            {'situation': 'They ask why a lawyer runs a supply chain. Explain in three sentences.',
             'tips': ['Finished study, finished job: past simple.',
                      'What it gives you today: present perfect or present simple.']},
            {'situation': 'They ask what has changed since the merger.',
             'tips': ['Since the merger means the period is still open.',
                      'Give a number: the headcount, the scope, the number of sites.']},
            {'situation': 'They ask about the hardest thing you have done at work.',
             'tips': ['Name it in the present perfect, then tell the story in the past simple.',
                      'Finish with what you have not done since.']},
            {'situation': 'They ask where you see yourself in three years, and you would rather '
                          'talk about the track record you already have.',
             'tips': ['Answer briefly, then bring it back to what you have built.',
                      'Two sentences and stop. Silence is not your problem to fill.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['I have worked here since 2016.',
                  'I have been a director for five years.',
                  'I have known him for three years.',
                  'We have used this supplier since March.'],
         'note': ('for measures the length, since names the starting point. The verb does not '
                  'change at all; only the word after it does.')},
    ],
}

LISTENINGS = [
    {'file': 'a7_listening1.mp3', 'voice': 'ellen',
     'text': ('Felipe, this is Nadia from people development. I am calling about the '
              'international assignment program. Applications have been open since Monday and '
              'they close on the fifteenth. You have been with the company for ten years and '
              'you have led four areas since the merger, so you have exactly the track record '
              'they are asking for. Two things you should know. The whole application is in '
              'English, and there is a twenty minute interview in English in April. You do not '
              'need your manager to sign anything. If you have not decided by Friday, call me '
              'and we will talk it through.')},
    {'file': 'a7_listening2.mp3', 'voice': 'dutch_m',
     'text': ('Felipe, this is Bram. Good to meet you this morning. I have been thinking about '
              'what you said about the guards on the sensors. We have had the same problem in '
              'Rotterdam since we changed the layout in 2023, and nobody has solved it '
              'properly. I have worked in this business for twenty-two years and I have never '
              'seen anybody share that kind of detail at a fair. So, two proposals. I send you '
              'our incident numbers for the last three years and you send me yours. And if you '
              'come to Europe in the autumn, come to Rotterdam for a day. We have run the night '
              'shift with half the headcount since January and it is working. Let me know.')},
]

EXTRA_AUDIO = [
    {'key': '[order-l7]', 'file': 'pc7_order_career.mp3', 'voice': 'arthur',
     'text': ('First, Felipe says that he joined the company in 2016, as facilities manager. '
              'Then he explains that he studied law and worked in a law firm for two years '
              'before that. After that, he says he was promoted twice, in 2018 and in 2021. '
              'Next, he says that the scope has doubled since the merger and the headcount has '
              'tripled. Finally, he says that the hardest year was the first one, and that he '
              'has not worked like that since.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem sauda&ccedil;&atilde;o scriptada. O tema &eacute; a carreira dele, '
    'contada a um desconhecido. Este slide s&oacute; abre a tela.',
    'Chapter 1: Ten Years in Two Minutes', 'Since I Joined', 'the Company',
    'Your own career, told to somebody who has never heard of you', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 6 (3 min): na aula 6 ele aprendeu experi&ecirc;ncia SEM data. '
    'Hoje entra a dura&ccedil;&atilde;o: for e since. Pe&ccedil;a que ele responda ao prompt e '
    'ESCUTE se ele diz I am here since 2016 &mdash; &eacute; o erro que quase todo brasileiro '
    'faz. N&atilde;o corrija ainda. Anote e volte a isso no slide 12.',
    'You Have Done It.', 'For How Long?',
    'Last time you said what you have done, with no dates. Now somebody wants the length of it. '
    'Ten years, since the merger, for six months. Portuguese uses the present here and English '
    'refuses to, and that single difference is what marks a Brazilian in the first minute.',
    'How long have you been in your current role? Answer in one full sentence.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as tr&ecirc;s miss&otilde;es. Diga que no fim ele conta dez anos '
    'de carreira em noventa segundos, sem apoio. Passe ao pr&oacute;ximo.',
    ['Eight words for talking about a career instead of a job title.',
     'Split what is finished from what is still running, with for and since.',
     'Tell ten years of your own career to a stranger, in ninety seconds.']))

S.append(L.s_chapter(
    4, 2,
    'Transi&ccedil;&atilde;o vocab (1 min): pista em ingl&ecirc;s primeiro, ele tenta a palavra, '
    's&oacute; ent&atilde;o clique.',
    'Chapter 2: Your Words', 'The Words of a', 'Career',
    '8 words that turn a job title into a story', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, s&oacute; ent&atilde;o clique. CCQ para '
    'to join: Do I join a company or a job? (A empresa.) CCQ para to be promoted: Do I change '
    'company when I am promoted? (N&atilde;o.) Pron&uacute;ncia: promoted tem tr&ecirc;s '
    's&iacute;labas (pro-MO-tid), com o -ed soando id.',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma din&acirc;mica. CCQ para scope: Is scope how much work or '
    'what kind of work? (O alcance: quais assuntos.) CCQ para track record: Is a track record '
    'one achievement or all of them? (Todas.) Estas duas palavras s&atilde;o exatamente o que '
    'ele precisa numa entrevista em ingl&ecirc;s.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balan&ccedil;a. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabul&aacute;rio (4 min): banco de palavras na tela. Ele escolhe e L&Ecirc; O '
    'PAR&Aacute;GRAFO INTEIRO em voz alta. Este par&aacute;grafo &eacute; a carreira dele de '
    'verdade &mdash; ele vai reus&aacute;-la tr&ecirc;s vezes hoje.',
    'Use the Words', 'Ten Years in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transi&ccedil;&atilde;o gram&aacute;tica (1 min): diga: Two periods, two tenses. One '
    'finished and one still running. Passe ao pr&oacute;ximo.',
    'Chapter 3: Finished or Still Running', 'For, Since,', 'and the Line Between',
    'The period that is over, and the period that is not', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os &aacute;udios. Pergunte: Two '
    'of these are still true today and two are over. Which are which, and what does the verb do '
    'about it? S&oacute; DEPOIS clique em Reveal the Rule. CCQ: In I ran that team for two '
    'years, do I still run it? (N&atilde;o.) In I have run four areas for five years, do I still '
    'run them? (Sim.)',
    'present perfect vs past simple with for and since',
    [('"I <span class="accent" style="font-weight:700">have been</span> at this company <span class="accent" style="font-weight:700">since</span> 2016."',
      'I have been at this company since 2016.'),
     ('"I <span class="accent" style="font-weight:700">joined</span> the company in 2016."',
      'I joined the company in 2016.'),
     ('"I <span class="accent" style="font-weight:700">have run</span> four areas <span class="accent" style="font-weight:700">for</span> five years."',
      'I have run four areas for five years.'),
     ('"I <span class="accent" style="font-weight:700">ran</span> the maintenance team for two years, and then I stopped."',
      'I ran the maintenance team for two years, and then I stopped.')],
    'rule7',
    ['Form', 'Use it for', 'Example'],
    [['have / has + participle + <strong>for</strong>',
      'A period that is still going. for + how long it has lasted.',
      'I <strong>have worked</strong> here <strong>for</strong> ten years.'],
     ['have / has + participle + <strong>since</strong>',
      'A period that is still going. since + the point where it started.',
      'I <strong>have been</strong> a director <strong>since</strong> 2021.'],
     ['Past simple', 'A period that is over. It has an end, so it takes a date.',
      'I <strong>ran</strong> that team <strong>for</strong> two years, and then I left.'],
     ['for or since', 'for + a length (six months, ten years). since + a start (March, 2016, '
      'the merger, I joined).',
      '<strong>for</strong> six months &middot; <strong>since</strong> March'],
     ['Never the present simple',
      'A period that started in the past cannot sit in the present simple. <em>I am here since '
      '2016</em> is wrong in every register.',
      'I <strong>have been</strong> here since 2016.']],
    ('for and since describe the same period from two ends. What decides the tense is not which '
     'word you use, it is whether the period has finished.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e s&oacute; depois clica. '
    'Toggle: clicar de novo fecha. Em cada item pergunte primeiro: is this period over? A '
    'resposta escolhe o tempo verbal sozinha.',
    'Grammar Practice', 'Over, or Still', 'Running?',
    'Say the full sentence, then click to compare',
    [('I ______ (work) here since 2016, and I am still here.',
      'I have worked here since 2016, and I am still here.'),
     ('I ______ (work) in a law firm for two years, and then I left.',
      'I worked in a law firm for two years, and then I left.'),
     ('The scope ______ (double) since the merger.',
      'The scope has doubled since the merger.'),
     ('How long ______ you ______ (be) in your current role?',
      'How long have you been in your current role?')]))

S.append(L.s_mistake(
    12, 3,
    'Common mistake (3 min): o primeiro &eacute; O erro do brasileiro em ingl&ecirc;s de '
    'trabalho, e ele vai fazer de novo hoje. Volte ao que voc&ecirc; anotou no warm-up e mostre '
    'para ele. Pe&ccedil;a que leia as vers&otilde;es CERTAS tr&ecirc;s vezes cada.',
    [('I am at this company since 2016.', 'I have been at this company since 2016.'),
     ('I work in operations for ten years.', 'I have worked in operations for ten years.'),
     ('I have joined the company in March 2016.', 'I joined the company in March 2016.')],
    ('If the period is still open, English uses have or has plus the participle, never the '
     'present. And a fixed date closes the period, so it goes back to the past simple.')))

S.append(L.s_listening(
    13, 3,
    'Listening 1 (5 min): ingl&ecirc;s americano, RH interno. LEIA AS PERGUNTAS EM VOZ ALTA COM '
    'ELE ANTES de tocar. O &aacute;udio tem quatro for/since seguidos &mdash; pergunte no fim '
    'quantos ele contou. Toque duas vezes.',
    1, 'The Call from', 'People Development',
    'A voicemail about an international assignment program. Sound first, no text.',
    'a7_listening1.mp3', SLUG,
    [('Since when have applications been open, and when do they close?',
      'Since Monday. They close on the fifteenth.'),
     ('Why does Nadia say he has the track record?',
      'He has been with the company for ten years and has led four areas since the merger.'),
     ('What are the two things about English that he should know?',
      'The application is in English, and there is a twenty minute interview in English in April.')]))

S.append(L.s_chapter(
    14, 4,
    'Transi&ccedil;&atilde;o di&aacute;logo (1 min): diga: Now the conversation itself. You are '
    'you. Bram runs operations for a Dutch retail group and you met him at the fair. Passe ao '
    'pr&oacute;ximo.',
    'Chapter 4: Telling It to a Stranger', 'Two Directors,', 'One Coffee',
    'Somebody who has never heard of you asks for ten years', IMG_CALL))

S.append(L.s_dialogue(
    15, 4,
    'Di&aacute;logo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, pe&ccedil;a que '
    'ELE fale primeiro, com o texto tapado &mdash; s&atilde;o literalmente as respostas dele '
    'numa entrevista. Bram tem sotaque holand&ecirc;s. Aponte a fala 12: ele responde a pergunta '
    'dif&iacute;cil com uma hist&oacute;ria, n&atilde;o com um adjetivo.',
    'Two Directors,', 'One Coffee',
    [('bram', 'B', 'dutch_m',
      'So, Felipe, you have the whole supply chain. How long have you been in that role?'),
     ('felipe', 'F', 'arthur',
      'Since 2021. I <span class="vocab-highlight">joined</span> the company in 2016 and I '
      '<span class="vocab-highlight">took over</span> the fourth area three years ago.'),
     ('bram', 'B', 'dutch_m', 'That is fast. What did you do before?'),
     ('felipe', 'F', 'arthur',
      'I studied law and I worked in a law firm for two years. I did not enjoy it, so I moved '
      'to operations.'),
     ('bram', 'B', 'dutch_m',
      'A lawyer in a distribution center. I have not heard that one before.'),
     ('felipe', 'F', 'arthur',
      'It helps more than people expect. I have read every supplier contract we have signed '
      'since I joined.'),
     ('bram', 'B', 'dutch_m',
      'I believe you. And the <span class="vocab-highlight">scope</span>, has it changed since 2021?'),
     ('felipe', 'F', 'arthur',
      'It has. I had two areas then. I have had four since the merger, and the '
      '<span class="vocab-highlight">headcount</span> has tripled.'),
     ('bram', 'B', 'dutch_m',
      'We have been through a merger too. What has been the hardest part for you?'),
     ('felipe', 'F', 'arthur',
      'The first year. I have never worked so many Saturdays, and I have not repeated that since.'),
     ('bram', 'B', 'dutch_m',
      'Good answer. Most people say the systems. It is never the systems.'),
     ('felipe', 'F', 'arthur',
      'It is never the systems. And you? How long have you been in Rotterdam?'),
     ('bram', 'B', 'dutch_m',
      'Twenty-two years, in three companies. I have not left the city since I started.')]))

S.append(L.s_comprehension(
    16, 4,
    'Comprehension (3 min): as perguntas s&atilde;o sobre o BRAM, n&atilde;o sobre ele. Ele '
    'responde de mem&oacute;ria ANTES de clicar. Se errar, volte ao di&aacute;logo e toque a fala.',
    'Did You Catch It?', 'About', 'Bram',
    [('How long has Bram been in Rotterdam, and in how many companies?',
      'Twenty-two years, in three companies.'),
     ('What has his company also been through?', 'A merger.'),
     ('What does he say most people answer, and what does he think of it?',
      'Most people say the systems, and he says it is never the systems.')]))

S.append(L.s_artifact(
    17, 4,
    'Artefato (4 min): o perfil interno dele. Pe&ccedil;a que ele LEIA em voz alta e depois '
    'responda. A terceira pergunta &eacute; a produ&ccedil;&atilde;o: ele TEM de dizer as '
    'tr&ecirc;s frases, n&atilde;o descrev&ecirc;-las.',
    'Real Document', 'The People', 'Profile',
    'PEOPLE PROFILE', 'INTERNAL',
    [('Name', 'Felipe de Ara&uacute;jo Dias'),
     ('Joined', 'March 2016 &middot; Facilities Manager'),
     ('Promoted', '2018 &middot; Operations Manager'),
     ('Promoted', '2021 &middot; Supply Chain Director'),
     ('Scope today', 'Supply, facilities, maintenance, loss prevention'),
     ('Headcount', '4 managers &middot; 310 people'),
     ('Milestone', '2 distribution centers opened since 2021'),
     ('Reports to', 'Chief Financial Officer')],
    [('How long has he been with the company, and how long has he been a director?',
      'He has been with the company since March 2016, and a director since 2021.'),
     ('Which lines take the past simple, and which take the present perfect?',
      'The two promotions are finished moments, so past simple. Joined in 2016 and still here, '
      'so has been with since.'),
     ('Say the whole profile in three sentences, out loud.',
      'I joined in 2016 as facilities manager. I was promoted twice, in 2018 and 2021. I have '
      'been supply chain director since then, and we have opened two distribution centers.')]))

S.append(L.s_listening(
    18, 4,
    'Listening 2 (5 min): sotaque holand&ecirc;s, o mesmo Bram do di&aacute;logo. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. Repare que Bram traz de volta o problema da aula 5 &mdash; '
    'pergunte no fim se ele reconheceu. Toque duas vezes.',
    2, 'Bram Follows', 'It Up',
    'A message left the same evening, from the other side of the fair. Sound first, no text.',
    'a7_listening2.mp3', SLUG,
    [('What problem has Rotterdam had, and since when?',
      'The same problem with the guards, since they changed the layout in 2023.'),
     ('What does Bram propose that the two of them exchange?',
      'Their incident numbers for the last three years.'),
     ('What has changed in Rotterdam since January?',
      'They have run the night shift with half the headcount, and it is working.')]))

S.append(L.s_blocks(
    19, 5,
    'Quick Fire (6 min): uma situa&ccedil;&atilde;o por vez, todas na mesma conversa de '
    'evento. Ele responde EM VOZ ALTA antes de abrir as Tips. Na &uacute;ltima, exija duas '
    'frases e sil&ecirc;ncio depois &mdash; ele tende a se explicar demais.',
    'Chapter 5: Real Talk', 'Ten Years on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    20, 6,
    'Transi&ccedil;&atilde;o pr&aacute;tica (1 min): diga: Now you tell it. Three rounds, less '
    'help each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    21, 6,
    'Scenarios + Rephrase (5 min): nos cen&aacute;rios, exija que ele misture os dois tempos '
    'numa mesma resposta. No rephrase, ele troca for por since e vice-versa, refazendo a conta. '
    'Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    22, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. A quarta &eacute; a pergunta que ELE vai ouvir num evento &mdash; '
    'garanta que ele saiba fazer.',
    [('I am here since 2016.', 'I have been here since 2016.'),
     ('I work in operations for ten years.', 'I have worked in operations for ten years.'),
     ('I have taken over the fourth area in 2023.', 'I took over the fourth area in 2023.'),
     ('How long do you work here?', 'How long have you worked here?')]))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 1 &mdash; guiado (4 min): voc&ecirc; &eacute; o Bram. Fa&ccedil;a as tr&ecirc;s '
    'perguntas na ordem e mais nada. Corrija apenas for/since e o present perfect; o resto anote.',
    'Role-Play 1 &mdash; Guided', 'The Three', 'Questions',
    'Situation',
    'A director you have just met asks three things: how long you have been in your role, what '
    'you did before, and what has changed since the merger. Answer all three in full sentences.',
    ['since 2021', 'for two years', 'I joined', 'I was promoted', 'the scope has doubled']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 2 &mdash; semi-livre (4 min): voc&ecirc; &eacute; a entrevistadora do programa '
    'internacional, vinte minutos, tudo em ingl&ecirc;s. Pergunte a coisa dif&iacute;cil: What '
    'has been your biggest failure? e espere. N&atilde;o resgate o sil&ecirc;ncio.',
    'Role-Play 2 &mdash; Semi-Free', 'The Twenty Minute', 'Interview',
    'Situation',
    'You are in the English interview for the international assignment program. Tell your career '
    'in four sentences, name one milestone, and answer one hard question about something that '
    'did not work.',
    ['track record', 'milestone', 'since the merger']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 3 &mdash; livre (5 min): a miss&atilde;o da aula. ZERO pistas na tela. N&atilde;o '
    'interrompa. Cronometre noventa segundos e conte quantas vezes ele acerta for/since. Diga o '
    'n&uacute;mero no fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Tell ten years of your career to somebody who has never heard of your company: where you '
    'started, what you left behind, how the scope has changed, one milestone, and one thing you '
    'have not repeated since. Ninety seconds, no notes.',
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
    '&atilde;o olhando para a c&acirc;mera. S&atilde;o as cinco frases da carreira dele em '
    'ingl&ecirc;s.',
    'Say It with', 'Confidence',
    ['I have been with the company since 2016.',
     'I have been supply chain director for five years.',
     'Before that I worked in a law firm for two years.',
     'The scope has doubled since the merger.',
     'The hardest year was the first one, and I have not repeated it since.']))

S.append(L.s_checklist(
    28,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 7.',
    7,
    ['I can tell ten years of my career in ninety seconds.',
     'I never say I am here since. I say I have been here since.',
     'I use for for a length and since for a starting point.',
     'I switch to the past simple the moment the period is closed.',
     'I know the words: to join, career path, to be promoted, to take over, scope, headcount, '
     'milestone, track record.']))

S.append(L.s_badge(
    29,
    'Encerramento (2 min): diga: Lesson 7 complete, Felipe. Homework ORALMENTE, nunca escrito na '
    'tela: gravar noventa segundos com a carreira dele em ingl&ecirc;s e mandar no WhatsApp '
    'antes da pr&oacute;xima aula. Pr&oacute;xima aula: The Plan for Next Quarter.',
    7, 'Since I Joined the Company',
    'Ten years, two promotions and one bad first year, all in ninety seconds, Felipe.',
    'The Plan for Next Quarter'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Since I Joined the Company -- Telling Your Own Career',
    'short_title': 'Since I Joined the Company',
    'menu_desc': ('Speaking lesson: ten years told to a stranger, and the line between the '
                  'period that is over and the period that is not'),
    'grammar_point': 'present perfect vs past simple with for and since',
    'characters': {'felipe': 'arthur', 'bram': 'dutch_m'},
    'phases': ['Ten Years in Two Minutes', 'Your Words', 'Finished or Still Running',
               'Telling It to a Stranger', 'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&q=80',
    'desc': ('The words of a career instead of a job title: to join, career path, to be '
             'promoted, to take over, scope, headcount, milestone, track record. Structure: '
             'present perfect with for and since for what is still running, past simple for '
             'what is closed. Mission: tell ten years to somebody who has never heard of you.'),
    'context_paras': [
        'I <strong>joined</strong> this company in March 2016, as facilities manager. Before '
        'that I <strong>studied</strong> law and I <strong>worked</strong> in a law firm '
        '<strong>for</strong> two years. I <strong>did not enjoy</strong> it, so I '
        '<strong>left</strong>. All of that is over, and every verb in it is in the past simple.',
        'Now look at what is still true. I <strong>have been</strong> here '
        '<strong>since</strong> 2016. I <strong>have been</strong> supply chain director '
        '<strong>for</strong> five years. The scope <strong>has doubled</strong> '
        '<strong>since</strong> the merger, and the headcount <strong>has tripled</strong>. '
        'None of those periods has an end yet, so none of them can use the past simple. And '
        'notice what English never does: it never says <em>I am here since 2016</em>. The '
        'present simple cannot carry a period that started in the past.'],
    'context_quiz': [
        ('Why does the text say <em>I worked in a law firm for two years</em> in the past simple?',
         [('Because for always takes the past simple.', False),
          ('Because that period is closed. He left, so it has an end.', True),
          ('Because a law firm is not the current company.', False)]),
        ('Why is <em>I am here since 2016</em> wrong in English?',
         [('Because since cannot be used with the verb to be.', False),
          ('Because the present simple cannot carry a period that started in the past. English '
           'needs have been.', True),
          ('Because 2016 is too far away for the present.', False)]),
        ('What is the difference between <em>for</em> and <em>since</em> here?',
         [('for measures the length of the period, since names the point where it started.', True),
          ('for is for work and since is for study.', False),
          ('for is informal and since is formal.', False)]),
    ],
    'tip_title': 'Present Perfect with For and Since',
    'tip_intro': ('The same period, seen from two ends. What chooses the tense is not the word '
                  'for or since. It is whether the period has closed.'),
    'tip_rows': [
        ['have / has + participle + for',
         'A period still running, measured by its length.',
         'I <strong>have worked</strong> here <strong>for</strong> ten years.'],
        ['have / has + participle + since',
         'A period still running, named by its starting point.',
         'I <strong>have been</strong> a director <strong>since</strong> 2021.'],
        ['Past simple', 'A closed period. It ended, so it can take a date.',
         'I <strong>worked</strong> there <strong>for</strong> two years, and then I left.'],
        ['for + length',
         'six months, ten years, a while, ages. Never <em>since ten years</em>.'],
        ['since + starting point',
         'March, 2016, the merger, I joined, we opened the second center.'],
        ['The question',
         '<em>How long <strong>have</strong> you <strong>been</strong> in this role?</em> — '
         'never <em>How long do you work here?</em>'],
    ],
    'tip_note': ('Before you answer, ask one question: is this period over? If it is not, you '
                 'need have or has plus the participle, whatever the Portuguese wants to do.'),
    'blanks': [
        ('I ', 'have been', 'Hint: two words. The period is still open, so not the present.',
         'I have been with this company since 2016.', ' with this company since 2016.'),
        ('I have been a director ', 'for', 'Hint: three letters. It comes before a length of time.',
         'I have been a director for five years.', ' five years.'),
        ('I ', 'joined', 'Hint: a fixed date closes the period, so past simple.',
         'I joined the company in March 2016.', ' the company in March 2016.'),
        ('The scope has doubled ', 'since', 'Hint: five letters. It comes before a starting point.',
         'The scope has doubled since the merger.', ' the merger.'),
        ('The ', 'headcount', 'Hint: one word. The number of people in the team.',
         'The headcount has tripled since 2021.', ' has tripled since 2021.'),
        ('How long ', 'have', 'Hint: four letters. The question about an open period starts here.',
         'How long have you been in your current role?', ' you been in your current role?'),
    ],
    'order_title': 'Put the Career in Order',
    'order_intro': 'Listen first, then put the five parts of the story in the order you hear them.',
    'order': [
        (3, 'After that, he says he was promoted twice, in 2018 and in 2021.'),
        (1, 'First, Felipe says that he joined the company in 2016, as facilities manager.'),
        (5, 'Finally, he says that the hardest year was the first one, and that he has not '
            'worked like that since.'),
        (2, 'Then he explains that he studied law and worked in a law firm for two years before '
            'that.'),
        (4, 'Next, he says that the scope has doubled since the merger and the headcount has '
            'tripled.'),
    ],
    'speech': [
        'I have been with the company since 2016.',
        'I have been supply chain director for five years.',
        'Before that I worked in a law firm for two years.',
        'The scope has doubled since the merger.',
        'The hardest year was the first one, and I have not repeated it since.',
    ],
    'quiz_intro': 'Somebody wants to hear about your career. Choose the best thing to say.',
    'quiz': [
        ('You started at the company in 2016 and you are still there. You say:',
         [('I am in this company since 2016.', False),
          ('I have been with this company since 2016.', True),
          ('I am with this company for ten years.', False)]),
        ('You worked at a law firm from 2014 to 2016 and then left. You say:',
         [('I have worked in a law firm for two years.', False),
          ('I worked in a law firm for two years, and then I moved to operations.', True),
          ('I am working in a law firm for two years.', False)]),
        ('Somebody asks about the length of time in your current role. The correct question is:',
         [('How long are you in this role?', False),
          ('How long have you been in this role?', True),
          ('How long do you have this role?', False)]),
        ('You want to say the team grew from ninety to three hundred people and is still '
         'growing. You say:',
         [('The headcount has tripled since the merger.', True),
          ('The headcount tripled since the merger, and it still grows.', False),
          ('The headcount is tripled for the merger.', False)]),
    ],
    'think': ('Somebody who has never heard of your company asks about your career. Record about '
              'ninety seconds. Start with what is finished: what you studied, where you worked '
              'before, and how long, all in the past simple. Then move to what is still running: '
              'how long you have been at your current company, how long you have been in your '
              'role, and what has changed since the last big event there. Name one milestone and '
              'one thing you have not repeated since. Use at least four words from this lesson. '
              'Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         '"Present perfect with for and since" -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on the exact pair you practised today, with a quiz at the end that catches '
         'the mistake you almost made in the warm-up. Connection to Lesson 7: it separates for '
         'from since with examples you can copy straight into your own answer.',
         'Tip: before each example, decide out loud whether the period is over. Then check '
         'whether the speaker agrees with you.',
         'https://www.youtube.com/watch?v=sSZcAh42qtI', 'Watch on YouTube'),
        ('video', 'career', 'Video Lesson',
         'Professional English: how to talk about your career',
         'The vocabulary and structures for describing a career path in English, from the first '
         'job to the current scope. Connection to Lesson 7: it gives you five more ways to say '
         'what you built, without repeating I was responsible for.',
         'Tip: write your own version of each sentence she gives, with your real dates, and read '
         'it out loud twice.',
         'https://www.youtube.com/watch?v=sFp5LPJ69EI', 'Watch on YouTube'),
        ('video', 'intro', 'Video Lesson',
         'Tell me about yourself -- introduce yourself in English',
         'The two minute answer that every interview and every conference starts with, broken '
         'into parts. Connection to Lesson 7: it is the free role-play you just did, with a '
         'structure you can reuse.',
         'Tip: record yourself first, then watch. Compare the order of your sentences with hers, '
         'not the words.',
         'https://www.youtube.com/watch?v=Tj1w86bw4EM', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
