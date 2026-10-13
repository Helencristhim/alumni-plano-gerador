#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 16 do Felipe de Araujo Dias — The City That Surprised Me.
Oracoes relativas definidoras (who, which, that, where). Modelo de LEITURA (aula PAR,
REGRA 29). Tema: cultura e viagem — Napoles, a cidade que ninguem recomenda e que muda a
opiniao de quem vai. Listening 2 com sotaque italiano (Giulia, a mesma da aula 11).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 16

IMG_TITLE = 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=1400&q=80'
IMG_READ = 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Reputation', 'what most people think about a person or a place',
     'Naples has a reputation that is much worse than the city.'),
    ('Stereotype', 'a fixed, simple idea about a group or a place, and it is often wrong',
     'The stereotype says the city is dangerous and dirty.'),
    ('Neighborhood', 'an area of a city where people live',
     'We stayed in a neighborhood where only locals eat out.'),
    ('Crowded', 'full of people, with very little space',
     'The streets were crowded, noisy and full of scooters.'),
    ('Local', 'a person who lives in a place, not a tourist',
     'The best restaurant was one that a local showed us.'),
    ('To wander', 'to walk slowly around a place, with no fixed plan',
     'On Sunday we just wandered around the old city.'),
    ('Breathtaking', 'so beautiful that it surprises you',
     'The view of the bay from the hill was breathtaking.'),
    ('Hidden gem', 'a very good place that not many people know about',
     'The pizzeria was a hidden gem with six tables and no menu.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Reputation', 'g'], ['2', 'Stereotype', 'c'], ['3', 'Neighborhood', 'h'],
                   ['4', 'Crowded', 'a'], ['5', 'Local', 'f'], ['6', 'To wander', 'b'],
                   ['7', 'Breathtaking', 'e'], ['8', 'Hidden gem', 'd']],
         'defs': [['a', 'Full of people, with very little space'],
                  ['b', 'To walk slowly around a place, with no fixed plan'],
                  ['c', 'A fixed, simple idea about a group or a place, and it is often wrong'],
                  ['d', 'A very good place that not many people know about'],
                  ['e', 'So beautiful that it surprises you'],
                  ['f', 'A person who lives in a place, not a tourist'],
                  ['g', 'What most people think about a person or a place'],
                  ['h', 'An area of a city where people live']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a reputation can be true or false, but a stereotype is '
                  'almost always too simple. The way to test both is the same: wander, and talk '
                  'to a local.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Before the trip, everybody told me about the ', ['1', 'reputation'],
                   ' of the city: dirty, dangerous, chaotic. It is the ', ['2', 'stereotype'],
                   ' that every tourist hears. The streets were ', ['3', 'crowded'],
                   ', yes, and very loud. But we stayed in a ', ['4', 'neighborhood'],
                   ' where people still sit outside at night. On Sunday we just ',
                   ['5', 'wander'], 'ed with no plan. A ', ['6', 'local'],
                   ' showed us a ', ['7', 'hidden gem'],
                   ' with six tables, and the view from the hill was ', ['8', 'breathtaking'],
                   '.'],
         'bank': ['reputation', 'stereotype', 'crowded', 'neighborhood', 'wander', 'local',
                  'hidden gem', 'breathtaking']},
    ],
    'reading': [
        {'kind': 'reading', 'rtitle': 'The City Nobody Recommends',
         'paras': [
             'Ask ten people who have never been to Naples, and nine will tell you the same '
             'thing: it is dirty, it is dangerous, and you should only stay one night on your '
             'way to the Amalfi Coast. It is a reputation that the city has had for more than a '
             'hundred years, and it is the reason many travelers never get out of the train '
             'station. The ones who do stay often say the same sentence when they come home: '
             'nobody told me.',
             'What surprises visitors is not the monuments, which are many, but the street '
             'life. Naples is a city where people still live on the sidewalk: grandmothers who '
             'talk from one balcony to another, men who play cards outside the bar, and small '
             'shops that have belonged to the same family for four generations. The streets are '
             'crowded and loud, and the traffic is a show of its own. But the city has a warmth '
             'which is hard to find in places that are cleaner and more organized. The '
             'stereotype is not completely false. It is just the smallest part of the story.'],
         'source': 'Adapted for class'},
        {'kind': 'gist', 'prompt': 'What is the best title for this text?',
         'choices': [['a', 'Why you should only stay one night in Naples on your way to the coast',
                      False],
                     ['b', 'A city that is better than its reputation', True],
                     ['c', 'The monuments of southern Italy', False]]},
    ],
    'tf': [
        {'kind': 'tf', 'items': [
            ['The text says the bad reputation of Naples is very recent.', 'f',
             'It says the city has had this reputation for more than a hundred years.'],
            ['According to the text, what surprises visitors most is the street life.', 't',
             'It says it is not the monuments, but the street life.'],
            ['The text says the stereotype is completely false.', 'f',
             'It says the stereotype is not completely false, just the smallest part of the '
             'story.'],
        ]},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'Tell a colleague about a city that surprised you. Describe one '
                           'person you met, one place where you ate, and one thing which was '
                           'different from what you expected.'],
            ['Scenario 2', 'A supplier from abroad is visiting São Paulo for two days. '
                           'Recommend a neighborhood where he should stay and a restaurant that '
                           'only locals know.'],
            ['Scenario 3', 'Describe the city where you grew up to someone who has never been '
                           'there. What is the stereotype, and what is the truth?'],
        ]},
        {'kind': 'rephrase',
         'title': 'Join the two sentences into one, with the word the cue asks for.',
         'items': [['We met a taxi driver. He told us about the city.', 'who'],
                   ['We ate at a small restaurant. It had no menu.', 'which'],
                   ['This is the street. Giulia grew up there.', 'where'],
                   ['Naples is a city. It surprises everybody.', 'that']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'A colleague asks about the best place you have ever traveled to.',
             'tips': ['It is a city that... / It is the place where...',
                      'Give one detail that nobody expects.']},
            {'situation': 'A visitor asks you where to eat in São Paulo, like a local.',
             'tips': ['There is a restaurant where...',
                      'Say who goes there: people who...']},
            {'situation': 'Someone says a city you love is dangerous and dirty.',
             'tips': ['That is the stereotype, but...',
                      'Describe one neighborhood where the reality is different.']},
            {'situation': 'Describe a person who helped you on a trip.',
             'tips': ['He was a man who... / She was the woman who...',
                      'Who for people, never which.']},
            {'situation': 'Recommend a hidden gem in the city where you live.',
             'tips': ['It is a place which / that...',
                      'Say why tourists never find it.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['We met a taxi driver who told us about the city.',
                  'We ate at a small restaurant which had no menu.',
                  'This is the street where Giulia grew up.',
                  'Naples is a city that surprises everybody.'],
         'note': ('Who is for people, which is for things, and where is for places. That works '
                  'for people and things, and it is the most common in conversation. The '
                  'relative word replaces the second he, it or there, so do not repeat them.')},
    ],
}

LISTENINGS = [
    {'file': 'a16_listening1.mp3', 'voice': 'ellen',
     'text': ("Hi Felipe, it's Laura from the events team, with the details for the Milan trade "
              "fair. The hotel that we booked is ten minutes from the fair, so you can walk. The "
              "colleague who organizes our stand is Paolo, and he will meet you at the hotel on "
              "Monday morning. The fair finishes on Friday at noon. You told me you wanted to "
              "stay for the weekend, so I found a train which leaves Milan at two and arrives in "
              "Naples at a quarter to seven. If you prefer Florence, which is closer, let me "
              "know before Wednesday.")},
    {'file': 'a16_listening2.mp3', 'voice': 'italian_f',
     'text': ("Felipe, it's Giulia. Laura told me you are going to Naples, and I am so happy, "
              "because it's the city where I grew up. Please don't listen to people who say it is "
              "dangerous. Three things. First, stay in the old center, which is where the life "
              "is. Second, there is a small pizzeria near my grandmother's street that has no "
              "menu. You sit down and they bring you the pizza that they made that day. Third, "
              "on Sunday, take the funicular, which is a little train that goes up the hill. The "
              "view of the bay from there is breathtaking. Send me a photo.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l16]', 'file': 'pc16_order_naples.mp3', 'voice': 'arthur',
     'text': ('First, Giulia asks Felipe how his weekend in Naples was. Then Felipe says it was '
              'the city that surprised him most. After that, he describes the neighborhood where '
              'they stayed. Next, he talks about a taxi driver who told them the history of the '
              'city. Finally, Giulia says the pizzeria they found is a hidden gem.')},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de LEITURA. O tema é viagem e cultura: uma '
    'cidade que tem fama ruim e surpreende quem vai. Diga o tema e siga.',
    'Chapter 1: Before You Go', 'The City That', 'Surprised Me',
    'A place with a bad reputation, and the people and streets that change your mind',
    IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 15 (3 min): na aula 15 ele defendeu uma mudança com if I could '
    'change one thing. Hoje a pergunta é sobre viagem. Peça que ele responda ao prompt e ESCUTE '
    'se sai the driver which ou the street where I lived there &mdash; são os erros do '
    'Detective. Não corrija ainda.',
    'You Imagined a Change.', 'Now Remember a Place',
    'Last lesson you defended an idea that is not real yet. Today it is the other way: a city '
    'that is real, and very different from what people say about it. To describe people and '
    'places in one long sentence, English has four small words.',
    'If you could go back to one city tomorrow, which one would it be, and why?'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): aula de leitura. Diga que o texto do meio é sobre Nápoles. Passe ao '
    'próximo.',
    ['Eight words for a city, its people and its reputation.',
     'Who, which, that and where: one sentence instead of two.',
     'Describe a city that surprised you, with people and places in every sentence.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'a Trip',
    '8 words for the city, the people and what you expected', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para stereotype: '
    'Is a stereotype usually complete and true? (Não &mdash; simples demais.) CCQ para crowded: '
    'Is a crowded street empty or full? (Cheia.) Pronúncia: neighborhood = NEI-bor-hood, sem o '
    'gh.',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para to wander: Do you have a map and a plan '
    'when you wander? (Não.) CCQ para hidden gem: Do many tourists know a hidden gem? (Não.) '
    'Pronúncia: wander rima com ponder, não com wonder.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta. Pergunte no fim: which city in your life had a reputation like this?',
    'Use the Words', 'One Weekend, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição leitura (1 min): diga: Read for the main idea first. Do not translate word by '
    'word.',
    'Chapter 3: Read the Story', 'The City', 'Nobody Recommends',
    'Read for the main idea', IMG_READ))

S.append(L.s_blocks(
    10, 3,
    'Reading + Gist (5 min): dois minutos de leitura silenciosa. Depois a pergunta de gist. Não '
    'peça tradução. Pergunte no fim se ele já teve a experiência do nobody told me.',
    'Read for the Main Idea', 'The City', 'Nobody Recommends', ['reading']))

S.append(L.s_blocks(
    11, 3,
    'True / False (4 min): ele decide TRUE ou FALSE ANTES de clicar. Ao clicar aparecem o '
    'veredito e a justificativa. Volte ao texto para conferir cada uma.',
    'Check Understanding', 'True or', 'False?', ['tf'],
    'Decide first, then tap to reveal the answer and why'))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): a Laura, do time de eventos, americana, com a logística da feira em '
    'Milão e do fim de semana. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Muitos '
    'horários &mdash; peça que ele anote só os do trem. Toque duas vezes.',
    1, 'The Fair and', 'the Weekend',
    'A colleague from the events team sends the plan. Sound first, no text.',
    'a16_listening1.mp3', SLUG,
    [('Who is Paolo?',
      'The colleague who organizes their stand. He will meet Felipe at the hotel.'),
     ('When does the train to Naples leave, and when does it arrive?',
      'It leaves Milan at two and arrives at a quarter to seven.'),
     ('What is the other city Laura offers?',
      'Florence, which is closer.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição gramática (1 min): diga: In the listening, Laura said the hotel that we booked. '
    'Two ideas, one sentence. How? Passe ao próximo.',
    'Chapter 4: Who, Which, That, Where', 'Two Sentences,', 'One Idea',
    'Defining relative clauses', IMG_GRAM))

S.append(L.s_discovery(
    14, 4,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: What comes '
    'before each orange word: a person, a thing or a place? Só DEPOIS clique em Reveal the Rule. '
    'CCQ: Can you say the driver which took us? (Não &mdash; pessoa é who ou that.) In the '
    'street where she grew up, do you need there at the end? (Não &mdash; o where já diz o '
    'lugar.)',
    'relative clauses',
    [('"We met a taxi driver <span class="accent" style="font-weight:700">who</span> told us '
      'the history of the city."',
      'We met a taxi driver who told us the history of the city.'),
     ('"We ate at a pizzeria <span class="accent" style="font-weight:700">which</span> has no '
      'menu."',
      'We ate at a pizzeria which has no menu.'),
     ('"It was the city <span class="accent" style="font-weight:700">that</span> surprised me '
      'most."',
      'It was the city that surprised me most.'),
     ('"This is the street <span class="accent" style="font-weight:700">where</span> Giulia grew '
      'up."',
      'This is the street where Giulia grew up.')],
    'rule16',
    ['Word', 'Use it for', 'Example'],
    [['who', 'People.',
      'the driver <strong>who</strong> took us to the hotel'],
     ['which', 'Things and animals.',
      'a pizzeria <strong>which</strong> has no menu'],
     ['that', 'People or things. Very common when you speak.',
      'the city <strong>that</strong> surprised me'],
     ['where', 'Places. It replaces there.',
      'the street <strong>where</strong> she grew up'],
     ['No relative word', 'When the next part has its own subject, you can drop it.',
      'the hotel (<strong>that</strong>) we booked']],
    ('The relative word replaces he, she, it or there. Never say both: the street where she '
     'lived there is one place too many.')))

S.append(L.s_oral(
    15, 4,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: person, thing or place? A resposta escolhe a palavra.',
    'Grammar Practice', 'Person, Thing', 'or Place?',
    'Say the full sentence, then click to compare',
    [('Giulia is the colleague ______ grew up in Naples.',
      'Giulia is the colleague who grew up in Naples.'),
     ('The funicular is a little train ______ goes up the hill.',
      'The funicular is a little train which goes up the hill.'),
     ('We stayed in a neighborhood ______ the locals eat out.',
      'We stayed in a neighborhood where the locals eat out.'),
     ('It was the trip ______ changed my opinion.',
      'It was the trip that changed my opinion.')]))

S.append(L.s_dialogue(
    16, 4,
    'Diálogo (6 min): Giulia, a mesma visitante italiana da aula 11, agora do outro lado: ela '
    'cresceu em Nápoles. Clique Next Line a cada fala. Nas falas do FELIPE, peça que ELE fale '
    'primeiro, com o texto tapado. Aponte a fala 6: uma frase só, com who, em vez de duas.',
    'So, How Was', 'Naples?',
    [('giulia', 'G', 'italian_f', 'Felipe! So, how was your weekend in Naples?'),
     ('felipe', 'F', 'arthur',
      'Honestly, it was the city that surprised me most this year.'),
     ('giulia', 'G', 'italian_f', 'I told you! What surprised you?'),
     ('felipe', 'F', 'arthur',
      'The street life. We stayed in a <span class="vocab-highlight">neighborhood</span> where '
      'people sit outside until midnight.'),
     ('giulia', 'G', 'italian_f', 'And the traffic?'),
     ('felipe', 'F', 'arthur',
      'Crazy. But we had a taxi driver who told us the history of every street.'),
     ('giulia', 'G', 'italian_f', 'Did you find the pizzeria that I told you about?'),
     ('felipe', 'F', 'arthur',
      'Yes, the one which has no menu. Six tables, and the best pizza of my life.'),
     ('giulia', 'G', 'italian_f',
      'That place is a <span class="vocab-highlight">hidden gem</span>. Even the people from '
      'Milan do not know it.'),
     ('felipe', 'F', 'arthur',
      'And the funicular was a great tip. The view was '
      '<span class="vocab-highlight">breathtaking</span>.'),
     ('giulia', 'G', 'italian_f', 'So the city is not what people say?'),
     ('felipe', 'F', 'arthur',
      'Not at all. The <span class="vocab-highlight">reputation</span> is the smallest part of '
      'the story.')]))

S.append(L.s_comprehension(
    17, 4,
    'Comprehension (3 min): as perguntas são sobre a GIULIA, não sobre ele. Ele responde de '
    'memória ANTES de clicar.',
    'Did You Catch It?', 'About', 'Giulia',
    [('What does Giulia ask about after the street life?',
      'The traffic.'),
     ('What does she say about the pizzeria?',
      'It is a hidden gem. Even the people from Milan do not know it.'),
     ('What is her last question?',
      'If the city is not what people say.')]))

S.append(L.s_artifact(
    18, 4,
    'Artefato (4 min): a lista que a Giulia mandaria para ele. Peça que ele LEIA em voz alta, '
    'transformando cada linha numa frase com who, which, that ou where. A terceira pergunta é '
    'produção: exija where sem there no fim.',
    'Real Document', 'A Local’s', 'List',
    'NAPLES &mdash; A LOCAL&rsquo;S LIST', 'FOR: FELIPE DIAS &middot; FROM: GIULIA',
    [('Old center', 'the area where the life is'),
     ('Spaccanapoli', 'the long street that cuts the old city in two'),
     ('Old pizzeria', 'the place which has no menu'),
     ('Sansevero Chapel', 'the chapel where the Veiled Christ is'),
     ('Funicular', 'the little train that goes up to Vomero'),
     ('Seafront', 'the place where people walk at sunset'),
     ('Taxi', 'ask for a driver who knows the old center'),
     ('Coffee', 'drink it standing at the bar, like a local')],
    [('What is Spaccanapoli?',
      'It is the long street that cuts the old city in two.'),
     ('What kind of driver should Felipe ask for?',
      'A driver who knows the old center.'),
     ('Describe the seafront in one sentence with where.',
      'The seafront is the place where people walk at sunset.')]))

S.append(L.s_listening(
    19, 4,
    'Listening 2 (5 min): sotaque italiano, a Giulia, ANTES da viagem, com três dicas. LEIA AS '
    'PERGUNTAS COM ELE ANTES do play. A mensagem tem cinco orações relativas &mdash; peça que '
    'ele repita uma no fim. Toque duas vezes.',
    2, 'Three Tips', 'from Giulia',
    'A voice message from someone who grew up there. Sound first, no text.',
    'a16_listening2.mp3', SLUG,
    [('Why is Giulia happy that Felipe is going to Naples?',
      'Because it is the city where she grew up.'),
     ('What is special about the pizzeria near her grandmother’s street?',
      'It has no menu. They bring you the pizza they made that day.'),
     ('What is the funicular?',
      'A little train that goes up the hill.')]))

S.append(L.s_blocks(
    20, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as Tips. '
    'Exija pelo menos UMA oração relativa em cada resposta. Se ele fizer duas frases curtas, '
    'peça: now make it one sentence.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    21, 6,
    'Transição prática (1 min): diga: Now you describe your city. Three rounds, less help each '
    'time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    22, 6,
    'Scenarios + Rephrase (5 min): nos cenários exija who, which e where pelo menos uma vez '
    'cada. No rephrase ele une as duas frases com a palavra entre parênteses. Sem gabarito na '
    'tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    23, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('The driver which took us to the hotel was very friendly.',
      'The driver who took us to the hotel was very friendly.'),
     ('This is the street where my grandmother lived there.',
      'This is the street where my grandmother lived.'),
     ('Naples is a city who surprises everybody.',
      'Naples is a city that surprises everybody.'),
     ('The pizzeria that we ate there was tiny.',
      'The pizzeria where we ate was tiny.')]))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 1 &mdash; guiado (4 min): você é a Giulia. Pergunte: so, how was the trip? Ele '
    'conta usando as chips, sobre uma cidade real que ele conhece.',
    'Role-Play 1 &mdash; Guided', 'So, How Was', 'the Trip?',
    'Situation',
    'A colleague asks about a city you visited. Say why it surprised you, describe a person you '
    'met and a place where you ate.',
    ['the city that', 'a man who', 'a place where', 'crowded', 'a hidden gem']))

S.append(L.s_roleplay(
    25, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é um fornecedor estrangeiro que chega a São '
    'Paulo com medo da fama da cidade. Insista: but is it safe? Ele tem de responder ao '
    'estereótipo e recomendar lugares.',
    'Role-Play 2 &mdash; Semi-Free', 'Is It', 'Safe?',
    'Situation',
    'A supplier from abroad is coming to São Paulo and is worried about its reputation. Answer '
    'the stereotype honestly, and recommend a neighborhood and a restaurant.',
    ['the stereotype', 'a neighborhood where', 'people who', 'like a local']))

S.append(L.s_roleplay(
    26, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos e conte quantas orações relativas ele produziu. Diga o número '
    'no fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Describe the city that surprised you most in your life: its reputation, the people you '
    'met, the places where you ate or walked, and what changed your mind. Ninety seconds, no '
    'notes.',
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
    'câmera. São as cinco frases da próxima conversa de viagem dele, no jantar depois de uma '
    'feira.',
    'Say It with', 'Confidence',
    ['It was the city that surprised me most.',
     'We stayed in a neighborhood where the locals eat out.',
     'We met a taxi driver who told us everything.',
     'It has a reputation which is not fair.',
     'The best places are the ones that tourists never find.']))

S.append(L.s_checklist(
    29,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 16.',
    16,
    ['I can describe a city that surprised me, with people and places.',
     'I use who for people, which for things and where for places.',
     'I use that for people and things when I speak.',
     'I never say the street where she lived there.',
     'I know the words: reputation, stereotype, neighborhood, crowded, local, to wander, '
     'breathtaking, hidden gem.']))

S.append(L.s_badge(
    30,
    'Encerramento (2 min): diga: Lesson 16 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos sobre a cidade que mais surpreendeu ele, com pelo menos '
    'cinco orações relativas, e mandar no WhatsApp. Próxima aula: What He Said in the Meeting.',
    16, 'The City That Surprised Me',
    'You told the story of a city today, Felipe, and every person and place came with a '
    'sentence around it.',
    'What He Said in the Meeting'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'The City That Surprised Me -- Culture and Travel',
    'short_title': 'The City That Surprised Me',
    'menu_desc': ('Reading lesson: a city with a bad reputation, the people and streets that '
                  'change your mind, and who, which, that and where'),
    'grammar_point': 'relative clauses',
    'characters': {'felipe': 'arthur', 'giulia': 'italian_f'},
    'phases': ['Before You Go', 'Your Words', 'Read the Story', 'Who, Which, That, Where',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=600&q=80',
    'desc': ('The words of a trip: reputation, stereotype, neighborhood, crowded, local, to '
             'wander, breathtaking, hidden gem. Structure: defining relative clauses with who, '
             'which, that and where. Mission: describe a city that surprised you.'),
    'context_paras': [
        'Naples was the city <strong>that</strong> surprised me most this year. We stayed in a '
        'neighborhood <strong>where</strong> people sit outside until midnight. On the first '
        'night we met a taxi driver <strong>who</strong> told us the history of every street. '
        'On Saturday we found a small pizzeria <strong>which</strong> has no menu, and on Sunday '
        'we took the funicular, a little train <strong>that</strong> goes up the hill.',
        'Look at the small words in bold. Each one joins two ideas in one sentence and replaces '
        'a word: <em>who</em> replaces a person, <em>which</em> a thing, <em>where</em> a place. '
        '<em>That</em> can replace a person or a thing, and it is the most common when you '
        'speak. Because the relative word already does the job, you never repeat <em>he</em>, '
        '<em>it</em> or <em>there</em> after it.'],
    'context_quiz': [
        ('Why does the text say <em>a taxi driver who</em> and not <em>a taxi driver which</em>?',
         [('Because the taxi driver was the only man in the text who knew the history.', False),
          ('Because a taxi driver is a person.', True),
          ('Because who is more formal than which.', False)]),
        ('What does <em>where</em> replace in <em>a neighborhood where people sit outside</em>?',
         [('A place: in that neighborhood.', True),
          ('A person: the people who live there and sit outside every night of the week.', False),
          ('A time: at midnight.', False)]),
        ('What is the funicular, according to the text?',
         [('A small pizzeria near the old center of the city, which has no menu.', False),
          ('A little train that goes up the hill.', True),
          ('A taxi.', False)]),
    ],
    'tip_title': 'Defining Relative Clauses',
    'tip_intro': ('Two ideas, one sentence. A small word joins them and tells you what you are '
                  'talking about: a person, a thing or a place.'),
    'tip_rows': [
        ['who', 'People.', 'a driver <strong>who</strong> told us the history'],
        ['which', 'Things and animals.', 'a pizzeria <strong>which</strong> has no menu'],
        ['that', 'People or things. The most common when you speak.',
         'the city <strong>that</strong> surprised me'],
        ['where', 'Places. It replaces there.',
         'the street <strong>where</strong> she grew up'],
        ['No relative word', 'When the next part has its own subject.',
         'the hotel (<strong>that</strong>) we booked'],
        ['No repetition', 'Do not repeat he, it or there.',
         'the street where she lived, <strong>not</strong> where she lived there'],
    ],
    'tip_note': ('The most common mistake is which for people. A person always takes who or '
                 'that: <em>the driver who took us</em>, never <em>the driver which took us</em>.'),
    'blanks': [
        ('We met a taxi driver ', 'who', 'Hint: one word. For a person.',
         'We met a taxi driver who told us everything.', ' told us everything.'),
        ('We stayed in a neighborhood ', 'where', 'Hint: one word. For a place.',
         'We stayed in a neighborhood where the locals eat out.', ' the locals eat out.'),
        ('We ate at a pizzeria ', 'which', 'Hint: one word. For a thing. Not that.',
         'We ate at a pizzeria which has no menu.', ' has no menu.'),
        ('It has a ', 'reputation', 'Hint: one word. What most people think about it.',
         'It has a reputation which is not fair.', ' which is not fair.'),
        ('The pizzeria was a ', 'hidden gem',
         'Hint: two words. A great place that few people know.',
         'The pizzeria was a hidden gem with six tables.', ' with six tables.'),
        ('The view from the hill was ', 'breathtaking',
         'Hint: one word. So beautiful that it surprises you.',
         'The view from the hill was breathtaking.', '.'),
    ],
    'order_title': 'Put the Conversation in Order',
    'order_intro': 'Listen first, then put the five parts of the conversation in the order you '
                   'hear them.',
    'order': [
        (3, 'After that, he describes the neighborhood where they stayed.'),
        (5, 'Finally, Giulia says the pizzeria they found is a hidden gem.'),
        (1, 'First, Giulia asks Felipe how his weekend in Naples was.'),
        (4, 'Next, he talks about a taxi driver who told them the history of the city.'),
        (2, 'Then Felipe says it was the city that surprised him most.'),
    ],
    'speech': [
        'It was the city that surprised me most.',
        'We stayed in a neighborhood where the locals eat out.',
        'We met a taxi driver who told us everything.',
        'It has a reputation which is not fair.',
        'The best places are the ones that tourists never find.',
    ],
    'quiz_intro': 'You are telling a colleague about a trip. Choose the best thing to say.',
    'quiz': [
        ('You want to talk about the taxi driver. You say:',
         [('We had a taxi driver which told us the history of every street in the city.', False),
          ('We had a taxi driver who told us everything.', True),
          ('We had a taxi driver who he told us everything.', False)]),
        ('You want to describe the area of your hotel. You say:',
         [('We stayed in a neighborhood where the locals eat out.', True),
          ('We stayed in a neighborhood where the locals eat out there every night of the week.',
           False),
          ('We stayed in a neighborhood which the locals eat out.', False)]),
        ('You want to describe the pizzeria. You say:',
         [('It was a small pizzeria who has no menu and only six tables near the church.', False),
          ('It was a small pizzeria which has no menu.', True),
          ('It was a small pizzeria where has no menu.', False)]),
        ('You want to say which city surprised you. You say:',
         [('Naples was the city what surprised me most, more than Milan or Florence.', False),
          ('Naples was the city where surprised me most.', False),
          ('Naples was the city that surprised me most.', True)]),
    ],
    'think': ('Think about the city that surprised you most in your life, in Brazil or abroad. '
              'Record about ninety seconds. Start with its reputation: what people told you '
              'before you went. Then describe one person who you met there, one place where you '
              'ate or walked, and one thing which was different from what you expected. Finish '
              'with a hidden gem that you would recommend to a friend. Use who, which, that and '
              'where at least once each, and at least four words from this lesson. Do not stop '
              'to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'Defining relative clauses -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on who, which, that and where, and when you can drop them. Connection to '
         'Lesson 16: every sentence about the people and places of your trip.',
         'Tip: pause after each example and make the same sentence about a city you know.',
         'https://www.youtube.com/watch?v=1iC_rULeuZc', 'Watch on YouTube'),
        ('youtube', 'gameshow', 'Grammar Video',
         'Relative clauses -- The Grammar Gameshow, BBC Learning English',
         'A quick quiz show on relative clauses, with the mistakes everybody makes. Connection '
         'to Lesson 16: the driver which and the street where she lived there.',
         'Tip: play along. Answer each question out loud before the contestants do.',
         'https://www.youtube.com/watch?v=bpYTihB4bqc', 'Watch on YouTube'),
        ('series', 'naples', 'Travel Show',
         "Naples and Pompeii -- Rick Steves' Europe",
         'A full episode about the street life, the markets and the traffic of Naples. '
         'Connection to Lesson 16: the city from the reading, and the places on Giulia’s '
         'list.',
         'Tip: watch with English subtitles and count the sentences with who, which or where '
         'that you hear.',
         'https://www.youtube.com/watch?v=mgxD4JgdMYY', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
