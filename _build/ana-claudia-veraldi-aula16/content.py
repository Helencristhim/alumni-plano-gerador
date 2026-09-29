# -*- coding: utf-8 -*-
"""Aula 16 -- It Must Be... (modals of deduction).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
Sotaques (CURRICULO V3, linha 16 do hub): frances (listening 1 + dialogo) + britanico (listening 2).
Callback da aula 15: third conditional + hindsight, a close call, a blessing in disguise...
Veiculo: deduzir a partir de pistas (os vizinhos novos, o garcom que nao sorri, a loja
fechada) -- e a armadilha intercultural: deduzir com as regras da PROPRIA cultura.
Nao usa objetos de restauro (reservado para a aula 18).
"""

LESSON = {
    'n': 16,
    'model': 'reading',
    'menu_title': 'It Must Be...',
    'menu_desc': 'A moving truck, a waiter who does not smile and a shop that is closed on a Tuesday. Tonight, '
                 'must, might and can&rsquo;t -- and why a deduction that works in Brazil can be wrong in Paris',
    'grammar_point': 'modals of deduction must, might and cannot, present and past',
    'chapter_tag': 'Reading the Clues',
    'title_html': 'It Must <span class="accent">Be...</span>',
    'title_sub': 'We guess things about people all day long. English has three small words for how sure we are.',
    'phases': ['First Words', 'The Words of Your World', 'The Story', 'The Code',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, the Past <span class="accent">That Did Not Happen</span>',
        'callback': 'One sentence with if + had done and one word from last week: hindsight, in retrospect, a '
                    'close call, to dwell on, a blessing in disguise, water under the bridge.',
        'question': 'Then: a new family moves into your street. What clues would tell you something about them?',
    },
    'framing': {
        'heading': 'Three Words for <span class="accent">How Sure You Are</span>',
        'steps': [('The Words', 'a clue, a hunch, to jump to conclusions...'),
                  ('The Story', 'a text about reading clues, and reading them wrong'),
                  ('The Code', 'must, might and can&rsquo;t &mdash; now and in the past')],
        'note': 'The lights are on next door. <strong>They must be home.</strong> The car is not there. '
                '<strong>They might be out.</strong> It is four in the morning. <strong>They can&rsquo;t be having '
                'a party.</strong> Same house, three levels of certainty &mdash; and none of them is a fact.',
    },
    'hook': {
        'label': 'One Small Mystery',
        'heading': 'Who Just <span class="accent">Moved In?</span>',
        'line1': 'A moving truck stops in front of the empty house on your street. Out come a piano, three '
                 'surfboards, a baby&rsquo;s crib and forty boxes of books.',
        'line2': 'What can you say about the new neighbors? How sure are you?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">Guessing Well</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'A clue', 'icon': 'key',
         'def': 'A piece of information that helps you understand something',
         'ex': 'The surfboards were a clue: they must like the sea.',
         'match': 'a piece of information that helps you understand something'},
        {'word': 'Evidence', 'icon': 'book',
         'def': 'Facts that show something is true',
         'ex': 'There is no evidence that he is angry. He is just quiet.',
         'match': 'facts that show something is true'},
        {'word': 'A hunch', 'icon': 'zap',
         'def': 'A feeling that something is true, without real proof',
         'ex': 'I had a hunch that the shop was closed, so I called first.',
         'match': 'a feeling that something is true, without proof'},
        {'word': 'To assume', 'icon': 'help',
         'def': 'To believe something is true without checking',
         'ex': 'I assumed he was French, but he was from Belgium.',
         'match': 'to believe something is true without checking'},
        {'word': 'To figure something out', 'icon': 'compass',
         'def': 'To understand or solve something by thinking about it',
         'ex': 'It took me a week to figure out why the neighbors never used the front door.',
         'match': 'to understand or solve something by thinking'},
        {'word': 'To give something away', 'icon': 'eye',
         'def': 'To show something that somebody wanted to hide, often by accident',
         'ex': 'She said she was fine, but her face gave it away.',
         'match': 'to show something hidden, often by accident'},
        {'word': 'Obvious', 'icon': 'sun',
         'def': 'Very easy to see or understand',
         'ex': 'It was obvious that they had a baby. There was a crib in the truck.',
         'match': 'very easy to see or understand'},
        {'word': 'Puzzled', 'icon': 'cloud',
         'def': 'Confused because you cannot understand something',
         'ex': 'I was puzzled when the waiter did not smile back.',
         'match': 'confused because you cannot understand something'},
        {'word': 'Suspicious', 'icon': 'shield',
         'def': 'Feeling that something is wrong, or making people feel that',
         'ex': 'A car parked outside all night looked suspicious.',
         'match': 'feeling that something is wrong'},
        {'word': 'To jump to conclusions', 'icon': 'bolt', 'expr': True,
         'def': 'To decide something too quickly, before you know the facts',
         'ex': 'Do not jump to conclusions. He might just be tired.',
         'match': 'to decide too quickly, before you know the facts'},
        {'word': 'To put two and two together', 'icon': 'link', 'expr': True,
         'def': 'To understand something by connecting the things you know',
         'ex': 'I saw the crib and the tiny shoes and put two and two together.',
         'match': 'to understand by connecting the things you know'},
        {'word': 'To read between the lines', 'icon': 'message', 'expr': True,
         'def': 'To understand what somebody means but does not say directly',
         'ex': 'If you read between the lines, her message says no.',
         'match': 'to understand what somebody means but does not say'},
    ],
    'vocabnote': 'Look at the difference between <strong>evidence</strong> and <strong>a hunch</strong>. With '
                 'evidence, you say <em>it must be</em>. With a hunch, you say <em>it might be</em>. And when you '
                 'say <em>must</em> with only a hunch, you are <strong>jumping to conclusions</strong>.',
    'pron': [
        'Suspicious',
        'Puzzled',
        'Evidence',
        "She must have been tired. She can't have slept at all.",
    ],
    'gapfill': [
        ('"The surfboards were ', 'a clue', ': they must like the sea."'),
        ('"There is no ', 'evidence', ' that he is angry. He is just quiet."'),
        ('"It was ', 'obvious', ' that they had a baby. There was a crib in the truck."'),
        ('"I was ', 'puzzled', ' when the waiter did not smile back."'),
        ('"A car parked outside all night looked ', 'suspicious', '."'),
        ('"I had ', 'a hunch', ' that the shop was closed, so I called first."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Story)
    'ch3': {
        'heading': 'Reading the Clues, <span class="accent">and Reading Them Wrong</span>',
        'sub': 'A short text, then a French woman and an Englishman tell their side',
    },
    'reading': {
        'heading': 'The Waiter Who <span class="accent">Did Not Smile</span>',
        'rtitle': 'Reading the Clues, and Reading Them Wrong',
        'paras': [
            'We are all detectives. A neighbor carries a yoga mat, so she <strong>must</strong> do yoga. A man '
            'looks at his phone every minute, so he <strong>might</strong> be waiting for news. Most of the time '
            'these small deductions are useful, and most of the time we never check them.',
            'The problem starts when we travel. A Brazilian in Paris orders a coffee, and the waiter does not smile. '
            'The obvious conclusion is <em>he must be annoyed with me</em>. But in France a serious face is simply '
            'professional, and a waiter who smiled all the time would look a little strange. The clue was real; '
            'the conclusion was Brazilian.',
            'It works the other way too. A French visitor in Sao Paulo is puzzled when strangers smile and '
            'chat in the elevator. <em>They can&rsquo;t be this friendly with everybody</em>, she thinks. <em>They '
            'must want something.</em> They do not. It is just how people behave there.',
            'English gives us three small words for this: <strong>must</strong> when we are almost sure it is true, '
            '<strong>can&rsquo;t</strong> when we are almost sure it is not, and <strong>might</strong> when we '
            'honestly do not know. In another culture, the safest word is often the smallest one. Before you say '
            '<em>he must be angry</em>, try <em>he might just be French</em>.',
        ],
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist_choices': [
            ('French waiters are unfriendly to tourists', False),
            ('Our deductions come from our own culture, so abroad it is safer to be less sure', True),
            ('How to become a good detective in ten steps', False),
        ],
        'tf': [
            ('The text says most of our small deductions are checked.', 'f',
             'It says the opposite: most of the time we never check them.'),
            ('In France, a waiter with a serious face is probably annoyed.', 'f',
             'A serious face is simply professional there.'),
            ('A French visitor may think friendly strangers in Brazil want something.', 't',
             'She thinks: they must want something. They do not.'),
            ('Can&rsquo;t is used when we are almost sure something is NOT true.', 't',
             'Must = almost sure it is true; can&rsquo;t = almost sure it is not; might = we do not know.'),
            ('The text recommends using must more often when you travel.', 'f',
             'It says the safest word abroad is often the smallest one: might.'),
        ],
    },
    'listenings': [
        {
            'file': 'a16_listening_elodie.mp3',
            'voice': 'french_f',
            'label': 'Listening 1 &middot; France',
            'title': 'Why Is Everybody <span class="accent">Smiling?</span>',
            'blurb': 'A French woman on her first month in New York. Sound first &mdash; no text.',
            'text': 'My name is Elodie, and I am from Lyon. When I moved to New York, I was puzzled all the time. '
                    'The first week, a woman in the supermarket smiled at me and said, I love your scarf. In France, '
                    'a stranger does not say that. So I thought, she must be selling something, or she must think I '
                    'am somebody else. I did not answer. Then the man at the coffee shop asked me, how is your day '
                    'going? I thought, he can not really want to know. He must say this to every customer. And yes, '
                    'he did. But that was the point. It was not a real question, and it was not fake either. It was '
                    'just friendly. Now, after two years, when a stranger smiles at me, I smile back. When I go home '
                    'to Lyon, my mother says I must have become American.',
            'qs': [
                ('What did the woman in the supermarket say to Elodie, and what did Elodie think?',
                 'She said: I love your scarf. Elodie thought she must be selling something or thought she was somebody else.'),
                ('What did the man at the coffee shop ask her?',
                 'How is your day going?'),
                ('What does Elodie&rsquo;s mother say when she goes home to Lyon?',
                 'That she must have become American.'),
            ],
        },
        {
            'file': 'a16_listening_oliver.mp3',
            'voice': 'british_m',
            'label': 'Listening 2 &middot; United Kingdom',
            'title': 'The Shop That <span class="accent">Was Always Closed</span>',
            'blurb': 'An Englishman on holiday in a French village. Sound first &mdash; no text.',
            'text': 'I am Oliver, from Brighton. A few summers ago, my wife and I rented a house in a tiny village '
                    'in Provence. On the first day, we walked to the village shop at about half past one. It was '
                    'closed. We looked at each other and said, it must have gone out of business. The next day we '
                    'went at two. Closed again. By the third day, I had a theory. The owner must be ill, I said, or '
                    'he might be on holiday himself. Then an old lady walking past put two and two together, looked '
                    'at our faces and laughed. It is lunch, she said. Every day, from twelve to three. Of course. In '
                    'England, a shop that closes for three hours in the middle of the day would not survive a week. '
                    'In Provence, it is the most obvious thing in the world. We had jumped to conclusions three days '
                    'in a row.',
            'qs': [
                ('What did Oliver and his wife think when the shop was closed the first day?',
                 'That it must have gone out of business.'),
                ('What was Oliver&rsquo;s theory on the third day?',
                 'The owner must be ill, or he might be on holiday himself.'),
                ('Why was the shop really closed?',
                 'It was lunch. The shop closes every day from twelve to three.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4 (The Code)
    'ch4': {
        'heading': 'How Sure <span class="accent">Are You?</span>',
        'sub': 'must &middot; might &middot; can&rsquo;t &mdash; and must have, for the past',
    },
    'grammar': {
        'heading': 'Almost Sure, <span class="accent">Not Sure, Almost Sure Not</span>',
        'examples': [
            'The lights are on. They <span style="color:#c2410c;font-weight:700">must be</span> home.',
            'The car is not there. They <span style="color:#1d4ed8;font-weight:700">might be</span> at the beach.',
            'It is four in the morning. They <span style="color:#7c3aed;font-weight:700">can\'t be</span> having a party.',
            'The grass is wet. It <span style="color:#15803d;font-weight:700">must have rained</span> last night.',
        ],
        'prompt': 'None of these sentences is a fact &mdash; they are all guesses from a clue. Which one is the most '
                  'sure? Which one is the least sure? And look at the last one: what changes when the guess is '
                  'about the PAST?',
        'rule_rows': [
            ('must + verb', 'Almost sure it IS true (from evidence).', 'They <strong>must be</strong> home.'),
            ('might / may / could + verb', 'Possible. You do not know.', 'They <strong>might be</strong> at the beach.'),
            ('can&rsquo;t + verb', 'Almost sure it is NOT true.', 'They <strong>can&rsquo;t be</strong> asleep.'),
            ('must have + past participle', 'Almost sure about the PAST.', 'It <strong>must have rained</strong>.'),
            ('might have / can&rsquo;t have + p.p.', 'Possible / impossible in the past.', 'She <strong>can&rsquo;t have seen</strong> us.'),
            ('never mustn&rsquo;t here', 'Mustn&rsquo;t means it is forbidden. For a negative guess, use can&rsquo;t.',
             'never: <em>they mustn&rsquo;t be home</em>'),
        ],
        'oneliner': 'must = almost sure yes, can&rsquo;t = almost sure no, might = maybe &mdash; add have for the past.',
    },
    'practice_heading': 'How Sure Are <span class="accent">You?</span>',
    'practice_fill': [
        ('"The lights are on. They ', 'must', ' be home." (almost sure yes)'),
        ('"The car is not there. They ', 'might', ' be at the beach." (maybe)'),
        ('"It is four in the morning. They ', 'can&rsquo;t', ' be having a party." (almost sure no)'),
        ('"The grass is wet. It must ', 'have rained', ' last night." (rain &mdash; the past)'),
        ('"She did not say hello. She ', 'might not have seen', ' us." (see &mdash; maybe, the past)'),
        ('"He has lived in Paris for ten years. He ', 'must speak', ' French." (speak &mdash; almost sure)'),
    ],
    'dialogue': {
        'heading': 'The New <span class="accent">Neighbors</span>',
        'guest_name': 'Julien',
        'guest_key': 'julien',
        'guest_voice': 'french_m',
        'lines': [
            ('julien', 'Ana, did you see the truck at number fourteen? Somebody must be moving in.'),
            ('ana', 'Yes! There was a piano and three surfboards. They must love the sea.'),
            ('julien', 'Or they might just like surfing on holiday. Let\'s not <span class="vocab-highlight">jump to conclusions</span>.'),
            ('ana', 'There was a crib too. They must have a baby.'),
            ('julien', 'That is a good <span class="vocab-highlight">clue</span>. But the man did not say hello to me. He can not be very friendly.'),
            ('ana', 'He might not have seen you. He was carrying a piano!'),
            ('julien', 'Ha, true. In France, we do not say hello to strangers in the street. Maybe he is French.'),
            ('ana', 'Now you are <span class="vocab-highlight">putting two and two together</span>. I will take them a cake tomorrow, the Brazilian way.'),
        ],
        'comp': [
            ('What does Julien say when Ana thinks the neighbors must love the sea?',
             'That they might just like surfing on holiday, and they should not jump to conclusions.'),
            ('What does Julien first think about the man, and why?',
             'That he can not be very friendly, because he did not say hello.'),
            ('What does Julien say about strangers in France?',
             'That in France people do not say hello to strangers in the street.'),
        ],
    },
    'artifact': {
        'heading': 'What the Truck <span class="accent">Gives Away</span>',
        'title': 'DELIVERY NOTE &mdash; HOUSE NUMBER 14',
        'subtitle': 'Copy left in Ana Claudia Veraldi&rsquo;s mailbox by mistake',
        'corner': 'Arrival<br>Saturday 9:00',
        'label_width': '120px',
        'rows': [
            ('Origin', 'Florianopolis &mdash; 1,100 km'),
            ('Large items', '1 upright piano &middot; 3 surfboards &middot; 1 baby crib'),
            ('Boxes', '42 boxes, 40 marked BOOKS &mdash; FRAGILE'),
            ('Special request', 'Please do not ring the bell before 10 a.m.'),
            ('Contact', 'Dr. M. Almeida &mdash; mobile only, no calls at night'),
        ],
        'comp': [
            ('Where do the new neighbors come from, and what does that tell you?',
             '"They come from Florianopolis. They must love the beach &mdash; that explains the surfboards."'),
            ('Make one guess with might and one with can&rsquo;t.',
             '"One of them might be a doctor. They can&rsquo;t be very quiet people if they have a baby!"'),
            ('Why do they ask you not to ring before 10? Guess, and say how sure you are.',
             '"The baby might sleep late, or they must work at night. I can&rsquo;t be sure."'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('He can&rsquo;t to be French. He has a Spanish name.', 'He can&rsquo;t be French. He has a Spanish name.'),
        ('The lights are off. They mustn&rsquo;t be home.', 'The lights are off. They can&rsquo;t be home.'),
        ('The grass is wet. It must rained last night.', 'The grass is wet. It must have rained last night.'),
        ('The shop is dark. It might is closed.', 'The shop is dark. It might be closed.'),
    ],
    'quickfire': [
        {'situation': 'Your friend has not answered your messages all day. Make a guess, but do not jump to conclusions.',
         'tips': ['She might be busy, or her phone might be dead.',
                  'Might: you honestly do not know.']},
        {'situation': 'Your neighbor has a new car, a new boat and a new pool. Say what you are almost sure about.',
         'tips': ['He must have a very good job.',
                  'Must: almost sure, from evidence.']},
        {'situation': 'Somebody says the train from Sao Paulo to Rio takes twenty minutes. React.',
         'tips': ['That can&rsquo;t be right. It must take at least five hours by car.',
                  'Can&rsquo;t: almost sure it is NOT true.']},
        {'situation': 'You come home and the kitchen floor is wet and there is a broken glass. Guess what happened.',
         'tips': ['Somebody must have dropped a glass of water.',
                  'Must have + past participle: a guess about the past.']},
        {'situation': 'A French waiter does not smile at you. What do you think now, after tonight?',
         'tips': ['He is not annoyed. He might just be professional.',
                  'The cultural trap: your own rules are not his rules.']},
        {'situation': 'Your friend did not come to your party and did not call. Make two guesses about the past.',
         'tips': ['She might have forgotten, or she can&rsquo;t have got my message.',
                  'Might have / can&rsquo;t have + past participle.']},
    ],
    'speaking': [
        ('Look at me. What can you guess about my day today?',
         'You must have had a long day, because you look a little tired. You might have taught many classes.'),
        ('Tell me about a time you jumped to conclusions.',
         'Once I thought a colleague was angry with me, but she must have been tired. She was very nice the next day.'),
        ('What clues tell you that somebody is not from Brazil?',
         'If somebody does not kiss on the cheek, they might be from another country. If they say hello with a handshake, they must be foreign.'),
        ('What can people guess about you from your house?',
         'They might think I am an artist, because there are old things everywhere. They can&rsquo;t think I am tidy!'),
    ],
    'building': [
        ('the lights / be on / they / must / be home (almost sure)',
         'The lights are on. They must be home.'),
        ('it / be four in the morning / they / can&rsquo;t / be awake (almost sure no)',
         'It is four in the morning. They can&rsquo;t be awake.'),
        ('the grass / be wet / it / must / rain / last night (past)',
         'The grass is wet. It must have rained last night.'),
        ('she / not say hello / she / might / not see / us (past, maybe)',
         'She did not say hello. She might not have seen us.'),
    ],
    'answerkey_heading': 'Must, Might, Can&rsquo;t in <span class="accent">Eight Lines</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        '<strong>must + verb</strong> = almost sure it IS true: They must be home.',
        '<strong>might / may / could + verb</strong> = possible: They might be at the beach.',
        '<strong>can&rsquo;t + verb</strong> = almost sure it is NOT true: They can&rsquo;t be asleep.',
        'The past: <strong>must have / might have / can&rsquo;t have + past participle</strong>: It must have rained.',
        'No to after modals: never can&rsquo;t to be &middot; never might is.',
        'Mustn&rsquo;t is for rules, not guesses: they can&rsquo;t be home, never they mustn&rsquo;t be home.',
        'Evidence = must. A hunch = might. Must with only a hunch = jumping to conclusions.',
        'And the one that is not grammar: our clues come from our own culture. A serious waiter in Paris, a smiling stranger in New York &mdash; abroad, might is the safest word.',
    ],
    'rp_chapter_heading': 'Detectives in <span class="accent">Three Countries</span>',
    'roleplays': [
        {'heading': 'The French <span class="accent">Neighbor</span>',
         'scenario': 'You are talking to Julien, your French neighbor. He shows you the delivery note from number '
                     'fourteen. Make three guesses about the new neighbors: one you are almost sure about, one '
                     'that is possible and one that is impossible.',
         'chips': ['They must', 'They might', 'They can&rsquo;t']},
        {'heading': 'The Englishman in <span class="accent">Provence</span>',
         'scenario': 'You are Oliver&rsquo;s friend. He tells you about the closed shop in Provence. Guess why it '
                     'was closed, three times, using the past. Then tell him about a time you misread a clue in '
                     'another culture.',
         'chips': ['It must have', 'He might have', 'jump to conclusions']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'Describe a person you saw recently but do not know &mdash; on the street, on a bus, in a '
                     'shop. What did you notice? What can you guess about them, and how sure are you?',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'Guess Well, <span class="accent">and Check</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Good Guesses</span>',
    'survival': [
        'The lights are on. They must be home.',
        'They might be at the beach.',
        "That can't be right.",
        'It must have rained last night.',
        'Let\'s not jump to conclusions.',
    ],
    'checklist': [
        'I use must when I am almost sure something is true.',
        'I use might, may or could when something is possible.',
        'I use can&rsquo;t, not mustn&rsquo;t, when I am almost sure something is not true.',
        'I use must have, might have and can&rsquo;t have for guesses about the past.',
        'I know the words: a clue, evidence, a hunch, to jump to conclusions, to put two and two together.',
    ],
    'badge': {
        'name': 'Good Detective',
        'text': 'You read the clues tonight, Ana &mdash; and you know that abroad, might is often the smartest word.',
        'next': 'What Should I Do?',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'we become detectives.&quot; O recorte: deduzir a partir de pistas (must, might, can&apos;t) e a '
                 'armadilha intercultural &mdash; deduzir com as regras da propria cultura (o garcom frances que nao '
                 'sorri NAO esta bravo).',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 15: UMA frase com if + had done e '
                  'uma palavra da aula passada (hindsight, in retrospect, a close call, to dwell on, a blessing in '
                  'disguise, water under the bridge). PONTE (REGRA 27B): &quot;That was the past. Now, a mystery in '
                  'the present.&quot; e a pergunta do slide. ZERO correcao. Anote se ela diz &quot;they mustn&apos;t '
                  'be&quot; &mdash; e o diagnostico de hoje.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos e as tres frases da nota: a mesma '
                   'casa, tres niveis de certeza. So plante &mdash; a regra vem no capitulo 4.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela deduzir sobre os vizinhos novos. NAO corrija. '
                'Anote as frases &mdash; o artefato do capitulo 4 e exatamente esse caminhao.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for guessing well. Three '
                       'of them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> CCQ evidence x a hunch: &quot;Which one has proof? '
                  '(Evidence.)&quot; CCQ to assume: &quot;Did you check? (Nao.)&quot; CCQ to give something away: '
                  '&quot;Did she want to show it? (Nao, foi sem querer.)&quot; Peca um exemplo da vida dela.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ puzzled: &quot;Do you understand? (Nao.)&quot; '
                  'CCQ to jump to conclusions: &quot;Too fast or too slow? (Rapido demais.)&quot; CCQ to put two and '
                  'two together: &quot;Do you connect the clues? (Sim.)&quot; CCQ to read between the lines: '
                  '&quot;Is it written? (Nao, esta implicito.)&quot;',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'evidence pede must; a hunch pede might.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> sus-PI-cious (/su-SPI-shus/), PUZ-zled (/PAZ-ld/, uma '
                'silaba e meia), EV-i-dence (forca no EV). Na frase inteira: &quot;must have been&quot; vira '
                '/MUST-uv-bin/ e o t de &quot;can&apos;t&quot; quase some antes de &quot;have&quot;. 2 repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas estao '
                   'no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao leitura (1 min):</strong> Diga: &quot;A short text about reading clues, and '
                     'then two people who read them wrong.&quot;',
        'reading': '<strong>Leitura + gist (6 min):</strong> Primeira leitura RAPIDA (90 segundos) so para a ideia '
                   'central, depois o gist. Segunda leitura com calma. Pergunte: &quot;Has this ever happened to '
                   'you, in Brazil or abroad?&quot;',
        'tf': '<strong>True or False (4 min):</strong> Ana decide e JUSTIFICA com o texto antes de revelar. A 4a e a '
              'regra escondida no texto &mdash; destaque, mas explique so no capitulo 4.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque FRANCES: o h nao soa (&quot;how&quot; vira '
                      '&quot;ow&quot;), o r e de garganta, forca no fim das palavras. Toque 2 vezes. No fim: '
                      '&quot;Was the woman in the supermarket selling something?&quot; (Nao.)',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'BRITANICO do sul: o r final nao soa, &quot;half&quot; com a longo /hahf/. Toque 2 vezes. '
                      'Pergunte: &quot;How many times did Oliver jump to conclusions?&quot; (Tres.)',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. Three small words for '
                     'how sure you are.&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases (toque o audio). Pergunte: '
                   '&quot;Which one is the most sure? The least sure? Which one says it is NOT true?&quot; Depois: '
                   '&quot;Look at the last one. What changes for the past?&quot; (must have + participio.) So entao '
                   '&quot;Reveal the Rule&quot;. CCQs: &quot;They can&apos;t be home &mdash; are they home? (Quase '
                   'certeza que nao.)&quot; &quot;They mustn&apos;t be home &mdash; is this a guess? (Nao, seria uma '
                   'proibicao.)&quot; Volte as frases do hook e corrija junto.',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a forma ORALMENTE antes de clicar. Itens 4 e 5 sao '
                    'passado (have + participio).',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Julien, vizinho frances. Clique &quot;Next '
                    'Line&quot; e toque o audio. Nas falas da Ana, peca que ELA fale primeiro. PRAGMATICA: o Julien '
                    'deduz que o homem &quot;can&apos;t be very friendly&quot; porque nao disse ola &mdash; e depois '
                    'percebe que na Franca ninguem cumprimenta estranho na rua. A Ana fecha com o jeito brasileiro '
                    '(o bolo).',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o JULIEN, nunca sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar.',
        'artifact': '<strong>Artefato (5 min):</strong> A nota de entrega que caiu na caixa de correio dela. Peca que '
                    'faca uma deducao por linha, dizendo o grau de certeza (must / might / can&apos;t). Depois as 3 '
                    'perguntas &mdash; ela responde antes de revelar.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick guesses, '
                     'and your own answers.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 4 erros classicos: to '
                     'depois do modal, mustn&apos;t no lugar de can&apos;t, must sem have no passado, e is depois do '
                     'modal.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 5a volta ao garcom frances &mdash; veja se ela usa might.',
        'speaking': '<strong>Speaking (5 min):</strong> A 1a e divertida: ela deduz coisas sobre VOCE. Espere '
                    'respostas completas com must, might e can&apos;t. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica '
                    'para comparar. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so no fim, para conferir. A ultima linha e a '
                     'pragmatica da noite.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Detectives in '
                     'three countries.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o Julien, frances, um pouco cetico. Para cada '
               'deducao dela, pergunte: &quot;How sure are you?&quot; Corrija SO a forma (sem to depois do modal, '
               'can&apos;t e nao mustn&apos;t).',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e o Oliver. Conte a historia da loja fechada em 3 '
               'frases e deixe ela adivinhar no passado (must have / might have). Depois ela conta a propria '
               'historia de uma pista mal lida.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. NAO corrija durante. Conte '
               'quantos must, might e can&apos;t ela usa. Anote qualquer mustn&apos;t de deducao para o feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Must, might, '
                    'can&apos;t, must have e a expressao da noite.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Sixteen lessons in, and tonight you guessed '
                 'well &mdash; and carefully.&quot; Homework (oralmente, opcional): observar uma pessoa desconhecida '
                 'esta semana e gravar um audio de um minuto com cinco deducoes (must, might, can&apos;t). Proxima '
                 'aula: What Should I Do? &mdash; conselho e obrigacao, e como soam em cada cultura.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'It Must Be... -- Guessing From the Clues',
        'desc': 'A moving truck, a waiter who does not smile and a shop closed on a Tuesday: must, might and can&rsquo;t for guesses, now and in the past.',
        'context_paras': [
            'On Saturday, a moving truck stopped at number fourteen, next to Ana&rsquo;s house. Out came a piano, '
            'three surfboards and a crib. &quot;They <strong>must have</strong> a baby,&quot; Ana said. It was '
            '<strong>obvious</strong>. Her French neighbor, Julien, was more careful. &quot;They <strong>might '
            'be</strong> surfers, or they <strong>might</strong> just like the beach. Let\'s not <strong>jump to '
            'conclusions</strong>.&quot;',
            'The man carrying the piano did not say hello. &quot;He <strong>can&rsquo;t be</strong> very '
            'friendly,&quot; said Julien. Ana laughed. &quot;He <strong>might not have seen</strong> you. He was '
            'carrying a piano!&quot; Then Julien <strong>put two and two together</strong>: in France, people do '
            'not say hello to strangers in the street. The new neighbor <strong>might be</strong> French too.',
            'A delivery note gave the rest away. They came from Florianopolis, and forty boxes were full of books. '
            '&quot;They <strong>must love</strong> reading,&quot; Ana said. This time she had real '
            '<strong>evidence</strong>, not just <strong>a hunch</strong>.',
        ],
        'context_quiz': [
            ('"They must have a baby," Ana said. Why is she almost sure?',
             [('Because she saw the baby.', False),
              ('Because there was a crib in the truck.', True),
              ('Because Julien told her.', False)]),
            ('"He can&rsquo;t be very friendly." What does can&rsquo;t mean here?',
             [('Julien is almost sure the man is NOT friendly.', True),
              ('The man is not allowed to be friendly.', False),
              ('The man cannot speak.', False)]),
            ('Why did the man not say hello, according to Julien in the end?',
             [('Because he was angry.', False),
              ('Because he was carrying a piano.', False),
              ('Because in France people do not say hello to strangers in the street.', True)]),
        ],
        'tip_title': 'Modals of Deduction',
        'tip_sub': 'Three small words for how sure you are &mdash; and have + past participle for the past.',
        'tip_rows': [
            ('must + verb', 'Almost sure it is true', 'They <strong>must be</strong> home.'),
            ('might / may / could + verb', 'Possible', 'They <strong>might be</strong> at the beach.'),
            ('can&rsquo;t + verb', 'Almost sure it is not true', 'They <strong>can&rsquo;t be</strong> asleep.'),
            ('must have + past participle', 'Almost sure about the past', 'It <strong>must have rained</strong>.'),
            ('might have / can&rsquo;t have', 'Possible / impossible in the past', 'She <strong>might not have seen</strong> us.'),
        ],
        'tip_never': 'He can&rsquo;t to be French &middot; they mustn&rsquo;t be home (for a guess) &middot; it '
                     'must rained last night &middot; it might is closed. After a modal, always the base form, and '
                     'have + past participle for the past.',
        'fills': [
            ('The lights are on. They ', 'must', ' be home.',
             'one word -- almost sure it is true'),
            ('The car is not there. They ', 'might', ' be at the beach.',
             'one word -- possible, you do not know'),
            ('It is four in the morning. They ', 'can\'t', ' be having a party.',
             'one word with an apostrophe -- almost sure it is not true'),
            ('The grass is wet. It must ', 'have rained', ' last night.',
             'rain -- two words, a guess about the past'),
            ('He has lived in Paris for ten years. He ', 'must speak', ' French.',
             'speak -- two words, almost sure'),
            ('There is no ', 'evidence', ' that he is angry. He is just quiet.',
             'one word -- facts that show something is true'),
        ],
        'order_intro': 'Ana and Julien see a moving truck on their street. Put the conversation in order.',
        'order': [
            'Ana, did you see the truck? Somebody must be moving in.',
            'Yes! There was a piano and three surfboards. They must love the sea.',
            'Or they might just like surfing on holiday. Let\'s not jump to conclusions.',
            'There was a crib too. They must have a baby.',
            'But the man did not say hello to me. He can not be very friendly.',
            'He might not have seen you. He was carrying a piano!',
        ],
        'quiz': [
            ('Your friend has not answered your messages all day. The best guess is:',
             [('"She must be dead."', False),
              ('"She might be busy."', True),
              ('"She mustn\'t be at home."', False)]),
            ('The lights are off and the car is gone. You are almost sure nobody is home. You say:',
             [('"They mustn\'t be home."', False),
              ('"They can\'t be home."', True),
              ('"They can\'t to be home."', False)]),
            ('The street is wet this morning. You say:',
             [('"It must have rained last night."', True),
              ('"It must rained last night."', False),
              ('"It must to rain last night."', False)]),
            ('A French waiter does not smile at you. After tonight, the best reaction is:',
             [('"He must hate tourists."', False),
              ('"He can\'t be a real waiter."', False),
              ('"He might just be professional. That is normal in France."', True)]),
        ],
        'think': 'Think about a person you saw this week but do not know: on the street, in a shop or on a bus. '
                 'Describe them and make five guesses about their life. Use must, might and can&rsquo;t at least '
                 'once each, and one guess about the past with must have or might have.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Series',
         'title': 'Sherlock &mdash; Sherlock and John&rsquo;s First Meeting (A Study in Pink, BBC)',
         'desc': 'The most famous detective in English meets Dr. Watson and, in two minutes, figures out where he '
                 'has been from a few small clues. Fast British English and the best example of evidence, not a '
                 'hunch.',
         'tip': 'watch it once for fun. Then pause after each deduction and say it with must: he must have been...',
         'url': 'https://www.youtube.com/watch?v=VaT7IYQgyqo', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; How Others See You',
         'desc': 'A psychologist explains why we are so bad at guessing what other people think of us after a first '
                 'conversation &mdash; our deductions about ourselves are often wrong too.',
         'tip': 'listen for might and must. Notice how often the guest says what people might think, not what they '
                'must think.',
         'url': 'https://www.hiddenbrain.org/podcast/mind-reading-how-others-see-you/', 'cta': 'Listen on Hidden Brain'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'YouTube',
         'title': 'Why Do Americans Smile So Much? &mdash; The Atlantic',
         'desc': 'A short video on why smiling at strangers is normal in the United States and not in many other '
                 'countries &mdash; the other side of Elodie&rsquo;s story in tonight&rsquo;s listening.',
         'tip': 'after watching, make three guesses about a smiling stranger in New York and a serious waiter in '
                'Paris, using must, might and can&rsquo;t.',
         'url': 'https://www.youtube.com/watch?v=ojbJrdkPhGg', 'cta': 'Watch on YouTube'},
    ],
}
