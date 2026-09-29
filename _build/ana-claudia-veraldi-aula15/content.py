# -*- coding: utf-8 -*-
"""Aula 15 -- Looking Back (third conditional).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques (CURRICULO V3, linha 15 do hub): holandes (listening 1) + americano (listening 2 e dialogo).
Callback da aula 14: perguntas indiretas/educadas + blunt, tactful, straightforward, to hedge...
Fecha o trio das condicionais: 12 = real, 13 = irreal no presente, 15 = irreal no PASSADO.
Veiculo: o que ela mudaria e o que nao mudaria -- escolhas pequenas que viraram grandes.
A mudanca de SP (aula 6) aparece como UM exemplo, nunca como espinha (REGRA DO FATO UNICO).
"""

LESSON = {
    'n': 15,
    'model': 'speech',
    'menu_title': 'Looking Back',
    'menu_desc': 'A flat tire, a piano that was sold and a train that was never taken. Tonight, the third '
                 'conditional -- what would have happened, and why some things you would not change at all',
    'grammar_point': 'third conditional for unreal past situations',
    'chapter_tag': 'What If?',
    'title_html': 'Looking <span class="accent">Back</span>',
    'title_sub': 'The past cannot change. But English has a whole structure for imagining that it did.',
    'phases': ['First Words', 'The Words of Your World', 'The Code', 'Many Englishes',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1501139083538-0139583c060f?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1501139083538-0139583c060f?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, the Right <span class="accent">Amount of Polite</span>',
        'callback': 'Ask me one polite question about my week, using could you tell me or do you know if. Use one '
                    'word from last time: blunt, tactful, straightforward, pushy, to hedge, to get to the point.',
        'question': 'Then: think of one small decision in your life that turned out to be very big.',
    },
    'framing': {
        'heading': 'Three Conditionals, <span class="accent">One Family</span>',
        'steps': [('The Words', 'hindsight, a close call, a blessing in disguise...'),
                  ('The Code', 'if + had done, would have done'),
                  ('Many Englishes', 'a Dutchman and an American look back')],
        'note': '<strong>If it rains, I will stay home</strong> (it can happen). <strong>If I lived there, I would '
                'miss the noise</strong> (it is not true). Tonight, the third one: <strong>If I had taken that '
                'train, I would have met him</strong> &mdash; it did not happen, and it is too late.',
    },
    'hook': {
        'label': 'The Small Decision',
        'heading': 'What If You <span class="accent">Had Said No?</span>',
        'line1': 'A lot of the big things in our lives started with something very small: a party we almost did '
                 'not go to, a bus we almost missed, a message we almost did not send.',
        'line2': 'Tell me one. What happened? And what would your life look like if it had gone the other way?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">Looking Back</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'A regret', 'icon': 'cloud',
         'def': 'A feeling of sadness about something you did or did not do',
         'ex': 'My only regret is that I did not learn to play the piano.',
         'match': 'a feeling of sadness about something you did or did not do'},
        {'word': 'Hindsight', 'icon': 'eye',
         'def': 'Understanding a situation only after it has happened',
         'ex': 'With hindsight, I should have asked more questions before I bought the car.',
         'match': 'understanding a situation only after it has happened'},
        {'word': 'In retrospect', 'icon': 'refresh',
         'def': 'When you think about it now, after it happened',
         'ex': 'In retrospect, moving in the winter was not a good idea.',
         'match': 'when you think about it now, after it happened'},
        {'word': 'To turn out', 'icon': 'compass',
         'def': 'To happen in a particular way, often a surprising one',
         'ex': 'The trip I almost cancelled turned out to be the best one of my life.',
         'match': 'to happen in a particular way, often a surprising one'},
        {'word': 'A close call', 'icon': 'alert',
         'def': 'A situation where something bad very nearly happened',
         'ex': 'We missed the car by one meter. It was a close call.',
         'match': 'a situation where something bad very nearly happened'},
        {'word': 'Fortunate', 'icon': 'star',
         'def': 'Lucky, especially when things could have gone wrong',
         'ex': 'We were fortunate that the storm started after we got home.',
         'match': 'lucky, especially when things could have gone wrong'},
        {'word': 'To dwell on something', 'icon': 'anchor',
         'def': 'To keep thinking about something bad for too long',
         'ex': 'There is no point in dwelling on it. It is finished.',
         'match': 'to keep thinking about something bad for too long'},
        {'word': 'To take something for granted', 'icon': 'home',
         'def': 'To stop noticing how valuable something is because you always have it',
         'ex': 'I took my grandmother&rsquo;s stories for granted until she was gone.',
         'match': 'to stop noticing how valuable something is'},
        {'word': 'To make the most of something', 'icon': 'sun',
         'def': 'To use an opportunity as well as you can',
         'ex': 'We only had two days in Lisbon, so we made the most of them.',
         'match': 'to use an opportunity as well as you can'},
        {'word': 'A blessing in disguise', 'icon': 'gift', 'expr': True,
         'def': 'Something that seems bad at first but turns out to be good',
         'ex': 'Losing that apartment was a blessing in disguise. I found a much better one.',
         'match': 'something that seems bad at first but turns out to be good'},
        {'word': 'Water under the bridge', 'icon': 'leaf', 'expr': True,
         'def': 'Something from the past that is no longer important',
         'ex': 'We had a big argument years ago, but it is water under the bridge now.',
         'match': 'something from the past that is no longer important'},
        {'word': 'To have second thoughts', 'icon': 'help', 'expr': True,
         'def': 'To start to doubt a decision you have already made',
         'ex': 'I had second thoughts the night before the move.',
         'match': 'to start to doubt a decision you already made'},
    ],
    'vocabnote': 'Three of tonight&rsquo;s words are whole expressions: <strong>a blessing in disguise</strong>, '
                 '<strong>water under the bridge</strong> and <strong>to have second thoughts</strong>. Notice '
                 'that <strong>hindsight</strong> and <strong>in retrospect</strong> are the natural way to open a '
                 'third conditional: <em>In retrospect, if I had known...</em>',
    'pron': [
        'Hindsight',
        'In retrospect',
        'A blessing in disguise',
        'If I had known, I would have come earlier.',
    ],
    'gapfill': [
        ('"My only ', 'regret', ' is that I did not learn to play the piano."'),
        ('"With ', 'hindsight', ', I should have asked more questions."'),
        ('"We missed the car by one meter. It was ', 'a close call', '."'),
        ('"We were ', 'fortunate', ' that the storm started after we got home."'),
        ('"Losing that apartment was ', 'a blessing in disguise', '. I found a much better one."'),
        ('"We had a big argument years ago, but it is ', 'water under the bridge', ' now."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Code)
    'ch3': {
        'heading': 'The Past That <span class="accent">Did Not Happen</span>',
        'sub': 'if + had done &middot; would have done &middot; and the short forms you really hear',
    },
    'grammar': {
        'heading': 'It Did Not Happen, <span class="accent">and It Is Too Late</span>',
        'examples': [
            'If my bike <span style="color:#c2410c;font-weight:700">had not had</span> a flat tire, I <span style="color:#c2410c;font-weight:700">would have missed</span> the party.',
            'If I <span style="color:#1d4ed8;font-weight:700">had known</span> about the storm, I <span style="color:#1d4ed8;font-weight:700">would not have driven</span> to the coast.',
            'If we <span style="color:#7c3aed;font-weight:700">had left</span> ten minutes earlier, we <span style="color:#7c3aed;font-weight:700">might have caught</span> the train.',
            'If she <span style="color:#15803d;font-weight:700">had kept</span> the piano, her kids <span style="color:#15803d;font-weight:700">could have learned</span> to play.',
        ],
        'prompt': 'All four sentences are about the PAST. Did any of the colored things really happen? Look at '
                  'the two halves. What comes after <em>if</em>? And what comes in the other half?',
        'rule_rows': [
            ('if + had + past participle', 'An imagined past &mdash; the opposite of what happened.',
             'If I <strong>had known</strong>... (I did not know)'),
            ('would have + past participle', 'The imagined result in the past.',
             'I <strong>would have come</strong> earlier.'),
            ('could have / might have', 'A possible result, less certain.',
             'We <strong>might have caught</strong> the train.'),
            ('negatives', 'had not / would not have.',
             'If it <strong>had not rained</strong>, we <strong>would not have stayed</strong>.'),
            ('what you really hear', 'If I&rsquo;d known, I&rsquo;d have come. would have = /WOULD-uv/.',
             'If I<strong>&rsquo;d</strong> known, I<strong>&rsquo;d have</strong> come.'),
            ('never would after if', 'The same rule as the other two conditionals.',
             'never: <em>if I would have known</em>'),
        ],
        'oneliner': 'if + had done, would have done &mdash; for a past that did not happen.',
    },
    'practice_heading': 'Change the <span class="accent">Past</span>',
    'practice_fill': [
        ('"If I ', 'had known', ' about the party, I would have gone." (know &mdash; the if half)'),
        ('"If we had left earlier, we ', 'would have caught', ' the train." (catch &mdash; the result)'),
        ('"If it ', 'had not rained', ', we would have had a picnic." (rain, negative)'),
        ('"If she had kept the piano, her kids ', 'could have learned', ' to play." (learn &mdash; a possibility)'),
        ('"If I lived near the sea, I ', 'would swim', ' every day." (swim &mdash; careful, this one is NOW, not the past)'),
        ('"If he had asked me, I ', 'would have helped', ' him." (help &mdash; the result)'),
    ],

    # ------------------------------------------------------------ chapter 4 (Many Englishes)
    'ch4': {
        'heading': 'A Dutchman and an American <span class="accent">Look Back</span>',
        'sub': 'Dutch and American English &mdash; and two ways to talk about regret',
    },
    'dialogue': {
        'heading': 'Would You <span class="accent">Change It?</span>',
        'guest_name': 'Greg',
        'guest_key': 'greg',
        'guest_voice': 'arthur',
        'lines': [
            ('greg', 'So, Ana, do you ever think about Sao Paulo? If you had stayed, where would you be now?'),
            ('ana', 'Sometimes. If I had stayed, I would have saved more money. But I would not have found this house.'),
            ('greg', 'I know the feeling. I almost did not move to Portugal. I had <span class="vocab-highlight">second thoughts</span> the week before.'),
            ('ana', 'Really? What would you have done in Chicago?'),
            ('greg', 'The same job, the same apartment. <span class="vocab-highlight">In retrospect</span>, it was the best decision I ever made.'),
            ('ana', 'For me, the first year was hard. I <span class="vocab-highlight">took</span> the city <span class="vocab-highlight">for granted</span>. I missed the cinemas and the restaurants.'),
            ('greg', 'Sure, but you do not <span class="vocab-highlight">dwell on</span> it, right? That is the American way. No regrets, move on.'),
            ('ana', 'Not really. And honestly? If I had not left, I would never have learned to restore anything.'),
        ],
        'comp': [
            ('Where did Greg move, and where did he live before?',
             'He moved to Portugal. Before that he lived in Chicago.'),
            ('What happened the week before Greg moved?',
             'He had second thoughts &mdash; he almost did not move.'),
            ('What does Greg call the American way of looking back?',
             'No regrets, move on.'),
        ],
    },
    'listenings': [
        {
            'file': 'a15_listening_bram.mp3',
            'voice': 'dutch_m',
            'label': 'Listening 1 &middot; The Netherlands',
            'title': 'The Flat <span class="accent">Tire</span>',
            'blurb': 'A Dutchman on the worst evening that turned out to be the best. Sound first &mdash; no text.',
            'text': 'My name is Bram, and I live in Utrecht, where everybody goes everywhere by bike. Twelve years '
                    'ago, on a Friday evening, I was cycling to the train station. I was going to Amsterdam for a '
                    'concert, and I had the ticket in my pocket. Then my back tire went flat. I had no tools, it '
                    'started to rain, and I missed the train. I was so angry. Instead, I walked to a small party at '
                    'a friend\'s apartment around the corner, just to get out of the rain. That is where I met '
                    'Sanne, who is now my wife. We have two kids. If my tire had not gone flat, I would have been '
                    'at that concert, and I would never have met her. So I tell my children that a bad evening can '
                    'be a blessing in disguise. They think it is a boring story. I think it is the most important '
                    'flat tire in history.',
            'qs': [
                ('Where was Bram going that Friday evening, and why?',
                 'To Amsterdam, for a concert. He had the ticket in his pocket.'),
                ('Why did he go to the party at his friend&rsquo;s apartment?',
                 'He missed the train, it started to rain, and he wanted to get out of the rain.'),
                ('What would have happened if his tire had not gone flat?',
                 'He would have been at the concert and he would never have met Sanne, his wife.'),
            ],
        },
        {
            'file': 'a15_listening_megan.mp3',
            'voice': 'sarah',
            'label': 'Listening 2 &middot; United States',
            'title': 'The Piano <span class="accent">We Sold</span>',
            'blurb': 'An American on the one thing she would change. Sound first &mdash; no text.',
            'text': 'Hi, I am Megan, and I grew up in Ohio. When my grandmother died, my parents sold her old piano. '
                    'It was heavy, it was out of tune, and nobody in the family played. It seemed like the sensible '
                    'thing to do. I was nineteen and I did not really care. Now I have two daughters, and last year '
                    'the younger one started piano lessons at school. She loves it. And every time she practices, I '
                    'think about that piano. If we had kept it, she could have learned on her great-grandmother\'s '
                    'instrument. My mom says it is water under the bridge, and she is right. I do not dwell on it. '
                    'But if somebody asked me for one thing I would change, that would be it. We took it for '
                    'granted because it was always there.',
            'qs': [
                ('Why did Megan&rsquo;s parents sell the piano?',
                 'It was heavy, it was out of tune, and nobody in the family played.'),
                ('What happened last year with Megan&rsquo;s younger daughter?',
                 'She started piano lessons at school, and she loves it.'),
                ('What does Megan&rsquo;s mom say about the piano, and does Megan agree?',
                 'She says it is water under the bridge. Megan agrees and does not dwell on it, but it is the one thing she would change.'),
            ],
        },
    ],
    'artifact': {
        'heading': 'The Train That <span class="accent">Never Left</span>',
        'title': 'TRAVEL UPDATE &mdash; UTRECHT CENTRAAL TO AMSTERDAM',
        'subtitle': 'Sent to: Ana Claudia Veraldi &middot; booking AV-7715',
        'corner': 'Friday<br>18:42',
        'label_width': '120px',
        'rows': [
            ('Your train', 'Intercity 3548, departure 18:42, platform 5'),
            ('Status', 'CANCELLED &mdash; problem with the overhead power line'),
            ('Next option', 'Intercity 3550 at 19:12. Expected delay: 30 minutes'),
            ('Your event', 'Canal boat tour, starts 19:45. Check-in closes at 19:35'),
            ('Refund', 'Request online within 7 days'),
        ],
        'comp': [
            ('Ana took the 19:12 train. Did she make the boat tour? Say it with the third conditional.',
             '"No. If the first train had not been cancelled, she would have made the boat tour."'),
            ('What could she have done differently?',
             '"If she had taken an earlier train, she could have arrived in time." Could have = a possibility.'),
            ('Imagine the evening turned out well anyway. Say it with an expression from today.',
             '"She met a nice couple at the station and had dinner with them. It was a blessing in disguise."'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('If I would have known, I would have come.', 'If I had known, I would have come.'),
        ('If I had knew about the party, I would have gone.', 'If I had known about the party, I would have gone.'),
        ('If we had left earlier, we would caught the train.', 'If we had left earlier, we would have caught the train.'),
        ('If I had studied more, I would pass the exam last year.', 'If I had studied more, I would have passed the exam last year.'),
    ],
    'quickfire': [
        {'situation': 'You missed a friend&rsquo;s party because nobody told you about it. Say it with the third conditional.',
         'tips': ['If I had known about the party, I would have gone.',
                  'if + had + past participle, would have + past participle.']},
        {'situation': 'You got caught in the rain without an umbrella. Say what you would have done differently.',
         'tips': ['If I had checked the forecast, I would have taken an umbrella.',
                  'In speech: If I&rsquo;d checked, I&rsquo;d have taken...']},
        {'situation': 'Something bad that turned out to be good. Tell me about it in one sentence.',
         'tips': ['Missing that flight was a blessing in disguise.',
                  'A blessing in disguise: bad at first, good in the end.']},
        {'situation': 'A friend keeps talking about an old argument. Tell her kindly to move on.',
         'tips': ['It is water under the bridge now. Try not to dwell on it.',
                  'Water under the bridge + to dwell on.']},
        {'situation': 'Careful: this one is NOT the past. Say what you would do if you had a piano now.',
         'tips': ['If I had a piano, I would take lessons.',
                  'Present and unreal: second conditional, from lesson 13.']},
        {'situation': 'Say one thing you would not change about your life, and why.',
         'tips': ['I would not change the move. If I had stayed, I would never have found this house.',
                  'This one has no grammar target. Say the true thing.']},
    ],
    'speaking': [
        ('What is one small decision that turned out to be very big for you?',
         'Going to a friend&rsquo;s barbecue. If I had not gone, I would never have met my best friend.'),
        ('What is one thing you would change if you could go back?',
         'If I had started English earlier, I would have traveled more when I was younger.'),
        ('Tell me about a close call you had.',
         'Once I almost missed a flight. If the taxi had arrived five minutes later, I would have missed it.'),
        ('Is there anything you took for granted when you were younger?',
         'I took my free time for granted. If I had known how busy life would get, I would have made the most of it.'),
    ],
    'building': [
        ('I / know / about the storm / not drive / to the coast',
         'If I had known about the storm, I would not have driven to the coast.'),
        ('we / leave / ten minutes earlier / might / catch the train',
         'If we had left ten minutes earlier, we might have caught the train.'),
        ('she / keep / the piano / her kids / could / learn to play',
         'If she had kept the piano, her kids could have learned to play.'),
        ('I / live / near the sea / swim every day (careful: NOW, not the past)',
         'If I lived near the sea, I would swim every day.'),
    ],
    'answerkey_heading': 'All Three Conditionals on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        'THIRD conditional: if + <strong>had + past participle</strong>, <strong>would have + past participle</strong> = a past that did not happen.',
        'If I <strong>had known</strong>, I <strong>would have come</strong>. (I did not know, and I did not come.)',
        'Softer results: <strong>could have</strong> (it was possible) and <strong>might have</strong> (maybe).',
        'Negatives: If it <strong>had not rained</strong>, we <strong>would not have stayed</strong> home.',
        'What you hear: If I&rsquo;d known, I&rsquo;d have come &mdash; would have sounds like /WOULD-uv/.',
        'Never would after if: never if I would have known.',
        'The family: FIRST if it rains, I will (can happen) &middot; SECOND if I lived there, I would (not true now) &middot; THIRD if I had known, I would have (not true in the past).',
        'And the one that is not grammar: the American no regrets, move on is one way to look back. Other cultures talk about regret more openly. Neither is wrong.',
    ],
    'rp_chapter_heading': 'Looking Back, <span class="accent">Out Loud</span>',
    'roleplays': [
        {'heading': 'The American Who <span class="accent">Has No Regrets</span>',
         'scenario': 'You are talking to Greg, an American who moved to Portugal. He asks you three things: one '
                     'decision that changed your life, what would have happened if you had decided differently, and '
                     'whether you have any regrets.',
         'chips': ['If I had not', 'I would have', 'in retrospect']},
        {'heading': 'The Dutch Friend and <span class="accent">the Flat Tire</span>',
         'scenario': 'Now you are talking to Bram, from Utrecht. He tells you about the flat tire. Ask him two '
                     'polite questions about it, then tell him your own story of a bad day that turned out to be '
                     'good.',
         'chips': ['a blessing in disguise', 'If it had not been for', 'Do you ever wonder if']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'Tell me about one moment in your life you would change, and one you would never change. For '
                     'each one, say what would have happened if it had gone the other way.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'What You Would Change, <span class="accent">and What You Would Not</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Looking Back</span>',
    'survival': [
        'If I had known, I would have come earlier.',
        'If we had left earlier, we might have caught the train.',
        'In retrospect, it was the best decision I ever made.',
        'It was a blessing in disguise.',
        'It is water under the bridge now.',
    ],
    'checklist': [
        'I use if + had + past participle for a past that did not happen.',
        'I use would have, could have or might have in the result.',
        'I never use would in the if half of any conditional.',
        'I can choose between the first, second and third conditionals.',
        'I know the words: hindsight, in retrospect, a close call, a blessing in disguise, water under the bridge.',
    ],
    'badge': {
        'name': 'Looking Back',
        'text': 'You changed the past three times tonight, Ana &mdash; and said which parts you would keep exactly '
                'as they are.',
        'next': 'It Must Be...',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'the past that did not happen.&quot; E a terceira e ultima condicional: fecha o trio (12 real, 13 '
                 'irreal no presente, 15 irreal no passado). Ela disse na consultoria que o condicional &quot;nao '
                 'entra na cabeca&quot; &mdash; hoje ela ve a familia inteira.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 14: ELA te faz uma pergunta '
                  'educada (could you tell me / do you know if) e usa uma palavra da aula passada (blunt, tactful, '
                  'straightforward, pushy, to hedge, to get to the point). Responda de verdade. PONTE (REGRA 27B): '
                  '&quot;Now let me ask YOU something about the past.&quot; e a pergunta do slide. ZERO correcao. '
                  'Anote se ela diz &quot;if I would have&quot;.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos e as tres frases da nota: sao as '
                   'tres condicionais, em ordem. So plante &mdash; a regra vem no capitulo 3.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela contar a historia da pequena decisao. NAO '
                'corrija. Anote a frase exata &mdash; ela volta corrigida no capitulo 3 e no role-play 3.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for looking back. Three '
                       'of them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> CCQ hindsight: &quot;Did you understand it at the '
                  'time? (Nao, so depois.)&quot; CCQ a close call: &quot;Did the bad thing happen? (Nao, quase.)&quot; '
                  'CCQ to turn out: &quot;Did you know the result at the start? (Nao.)&quot; Peca um exemplo da vida '
                  'dela em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ to dwell on: &quot;Is it good for you? (Nao, '
                  'e pensar demais.)&quot; CCQ a blessing in disguise: &quot;Was it bad at the start? (Sim.) And at '
                  'the end? (Bom.)&quot; CCQ water under the bridge: &quot;Is it still important? (Nao.)&quot; CCQ to '
                  'have second thoughts: &quot;Had you already decided? (Sim.)&quot;',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'hindsight e in retrospect abrem a terceira condicional com naturalidade.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> HIND-sight (forca no HIND, i longo /ai/), in '
                'RET-ro-spect, a BLESS-ing in dis-GUISE. Na frase inteira: &quot;would have&quot; vira '
                '/WOULD-uv/ &mdash; o h some. Mostre tambem a forma curta: &quot;If I&apos;d known, I&apos;d have '
                'come.&quot; 2 repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas '
                   'estao no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. The past that did not '
                     'happen.&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases (toque o audio). Pergunte: &quot;Did '
                   'the tire go flat? Did he miss the party?&quot; Mostre que a frase diz o OPOSTO do que '
                   'aconteceu. Depois: &quot;What comes after if? And in the other half?&quot; Espere ela achar had + '
                   'participio e would have + participio. So entao &quot;Reveal the Rule&quot;. CCQs: &quot;If I had '
                   'known &mdash; did I know? (Nao.)&quot; &quot;We might have caught the train &mdash; are we sure? '
                   '(Nao, talvez.)&quot; Volte a frase anotada no hook e corrija junto.',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a forma ORALMENTE antes de clicar. O item 5 e a '
                    'armadilha: e AGORA (segunda condicional, aula 13), nao passado.',
        'ch4_trans': '<strong>Transicao Many Englishes (1 min):</strong> Diga: &quot;A Dutchman and two Americans '
                     'look back.&quot; Avise os sotaques: holandes (g aspirado na garganta, v que soa quase f) e '
                     'americano do meio-oeste.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Greg, americano de Chicago que mora em Portugal. '
                    'Clique &quot;Next Line&quot; e toque o audio. Nas falas da Ana, peca que ELA fale primeiro. '
                    'PRAGMATICA: o Greg representa o &quot;no regrets, move on&quot; americano; a Ana responde com '
                    'mais nuance (&quot;Not really&quot;). Pergunte depois: &quot;In Brazil, do people talk about '
                    'regret?&quot;',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o GREG, nunca sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque HOLANDES: o g e aspirado, o v soa quase f, frases '
                      'diretas e sem rodeio. Toque 2 vezes. No fim: &quot;Would Bram change that evening?&quot; '
                      '(Nunca &mdash; e o ponto.)',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'AMERICANO do meio-oeste (Ohio): r bem marcado, t entre vogais vira quase d (&quot;daughter&quot;, '
                      '&quot;water&quot;). Toque 2 vezes. Pergunte: &quot;Is Megan sad? Does she dwell on it?&quot;',
        'artifact': '<strong>Artefato (5 min):</strong> Um aviso real de trem cancelado na Holanda, em nome dela. '
                    'Peca que leia cada linha e depois responda as 3 perguntas com a terceira condicional. A 3a usa '
                    'a expressao da noite. Ela responde antes de revelar.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick answers, '
                     'and your own stories.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 4 erros classicos: would '
                     'depois do if, had + passado simples (knew), would sem have, e a metade do resultado sem '
                     'passado (would pass).',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 5a e a armadilha (e agora: segunda condicional).',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija pelo '
                    'menos uma resposta com might have ou could have. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica para '
                    'comparar. O item 4 e agora, nao passado. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so no fim, para conferir. A linha 7 mostra a familia '
                     'das tres condicionais lado a lado &mdash; vale uma pausa.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Your own '
                     'story, three times.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o Greg, americano, otimista. Faca as 3 perguntas '
               'do cenario, uma por vez. Corrija SO a estrutura (had + participio / would have + participio).',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e o Bram. Conte a historia do pneu em 3 frases. '
               'Ela faz duas perguntas EDUCADAS (callback da aula 14) e depois conta a historia dela. Ensine '
               '&quot;If it had not been for...&quot; se ela precisar.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. NAO corrija durante. Conte '
               'quantas terceiras condicionais ela usa e diga o numero no fim. Anote qualquer &quot;if I would '
               'have&quot; para o feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Duas frases de '
                    'estrutura, uma de abertura (in retrospect) e duas expressoes.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Fifteen lessons in, and you now have all three '
                 'conditionals.&quot; Homework (oralmente, opcional): um audio de um minuto sobre UMA coisa que ela '
                 'mudaria e UMA que nunca mudaria, com a terceira condicional. Proxima aula: It Must Be... &mdash; '
                 'deduzir e supor com must, might e can&apos;t.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'Looking Back -- What You Would Change and What You Would Not',
        'desc': 'A flat tire, a piano that was sold and a train that was cancelled: the third conditional for a past that did not happen.',
        'context_paras': [
            'Twelve years ago, Bram was cycling to the station in Utrecht when his tire went flat. He missed his '
            'train and went to a small party instead, where he met his future wife. <strong>If his tire had not '
            'gone flat, he would have gone</strong> to the concert and he <strong>would never have met</strong> '
            'her. For Bram, it was <strong>a blessing in disguise</strong>.',
            'Megan, from Ohio, has a different story. Her family sold her grandmother&rsquo;s piano because nobody '
            'played. Now her daughter loves the piano. <strong>If they had kept it</strong>, her daughter '
            '<strong>could have learned</strong> on it. Megan does not <strong>dwell on</strong> it &mdash; it is '
            '<strong>water under the bridge</strong> &mdash; but <strong>in retrospect</strong>, they '
            '<strong>took</strong> it <strong>for granted</strong>.',
            'Ana thinks about her own decisions too. <strong>If she had stayed</strong> in Sao Paulo, she '
            '<strong>would have saved</strong> more money. But she <strong>would not have found</strong> her house. '
            'With <strong>hindsight</strong>, she would not change a thing.',
        ],
        'context_quiz': [
            ('"If his tire had not gone flat, he would have gone to the concert." Did Bram go to the concert?',
             [('Yes, he went to the concert.', False),
              ('No. The sentence imagines the opposite of what happened.', True),
              ('We do not know.', False)]),
            ('"If they had kept it, her daughter could have learned on it." What does could have show?',
             [('A possibility in the past that did not happen.', True),
              ('Something her daughter does every day.', False),
              ('A plan for next year.', False)]),
            ('Why does Ana not regret leaving Sao Paulo?',
             [('Because she saved more money.', False),
              ('Because she found her house.', True),
              ('Because she never lived there.', False)]),
        ],
        'tip_title': 'The Third Conditional',
        'tip_sub': 'For a past that did not happen &mdash; and it is too late to change it.',
        'tip_rows': [
            ('if + had + past participle', 'An imagined past', 'If I <strong>had known</strong>...'),
            ('would have + past participle', 'The imagined result', '...I <strong>would have come</strong>.'),
            ('could have / might have', 'A possible result', 'We <strong>might have caught</strong> the train.'),
            ('negatives', 'had not / would not have', 'If it <strong>had not rained</strong>, we <strong>would not have stayed</strong>.'),
            ('short forms', 'Very common in speech', 'If I<strong>&rsquo;d</strong> known, I<strong>&rsquo;d have</strong> come.'),
            ('question', 'What would you have done?', 'What <strong>would you have done</strong> if you had stayed?'),
        ],
        'tip_never': 'If I would have known &middot; if I had knew &middot; we would caught the train &middot; if I '
                     'had studied, I would pass last year. Both halves need their full form: had + past participle, '
                     'and would have + past participle.',
        'fills': [
            ('If I ', 'had known', ' about the party, I would have gone.',
             'know -- two words: had + past participle'),
            ('If we had left earlier, we ', 'would have caught', ' the train.',
             'catch -- three words: would + have + past participle'),
            ('If it ', 'had not rained', ', we would have had a picnic.',
             'rain -- three words, negative'),
            ('If she had kept the piano, her kids ', 'could have learned', ' to play.',
             'learn -- three words, a possibility'),
            ('If I lived near the sea, I ', 'would swim', ' every day.',
             'swim -- careful, this one is NOW, not the past'),
            ('With ', 'hindsight', ', I should have asked more questions.',
             'one word -- understanding something only after it happened'),
        ],
        'order_intro': 'Greg asks Ana about her move from Sao Paulo. Put the conversation in order.',
        'order': [
            'So, Ana, if you had stayed in Sao Paulo, where would you be now?',
            'If I had stayed, I would have saved more money. But I would not have found this house.',
            'I know the feeling. I almost did not move to Portugal.',
            'Really? What would you have done in Chicago?',
            'The same job, the same apartment. In retrospect, it was the best decision I ever made.',
            'For me too. If I had not left, I would never have learned to restore anything.',
        ],
        'quiz': [
            ('You missed a friend&rsquo;s party because you did not know about it. You say:',
             [('"If I had known, I would have gone."', True),
              ('"If I would have known, I would have gone."', False),
              ('"If I knew, I would have went."', False)]),
            ('You lost your apartment, but you found a much better one. You say:',
             [('"It was water under the bridge."', False),
              ('"It was a blessing in disguise."', True),
              ('"It was a close call."', False)]),
            ('A friend keeps talking about an old argument. You tell her kindly:',
             [('"It is water under the bridge. Try not to dwell on it."', True),
              ('"It is a blessing in disguise. Dwell on it."', False),
              ('"You took it for granted."', False)]),
            ('Which sentence is about NOW, not the past?',
             [('"If I had had a piano, I would have played."', False),
              ('"If I had a piano, I would play every day."', True),
              ('"If I had known, I would have played."', False)]),
        ],
        'think': 'Think about one moment in your life you would change and one you would never change. For each '
                 'one, say what happened and what would have happened if it had gone the other way. Use the third '
                 'conditional at least four times, and one of tonight&rsquo;s expressions.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Film',
         'title': 'Sliding Doors (1998) &mdash; official trailer',
         'desc': 'A woman in London runs for a train. In one version of her life she catches it; in the other, the '
                 'doors close in her face. The whole film is a third conditional: what would have happened if she '
                 'had caught that train?',
         'tip': 'watch the trailer, then say three sentences about her two lives: if she had caught the train, '
                'she would have...',
         'url': 'https://www.youtube.com/watch?v=Da-Mizk86AE', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'You Are Not So Smart &mdash; 228. The Power of Regret, with Daniel H. Pink',
         'desc': 'An American writer who collected thousands of regrets from people all over the world talks about '
                 'what they have in common, and why looking back can help us move forward.',
         'tip': 'listen for would have and could have. Every time you hear one, write the whole sentence down.',
         'url': 'https://podcasts.apple.com/us/podcast/228-the-power-of-regret-daniel-h-pink/id521594713?i=1000554562286',
         'cta': 'Listen on Apple Podcasts'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'Don&rsquo;t regret regret &mdash; Kathryn Schulz, TED',
         'desc': 'A funny and honest talk about regret, starting with a tattoo the speaker regretted almost '
                 'immediately. Clear American English, and a kind way of looking back.',
         'tip': 'pause after each story and say what would have happened if she had decided differently.',
         'url': 'https://www.ted.com/talks/kathryn_schulz_don_t_regret_regret', 'cta': 'Watch on TED'},
    ],
}
