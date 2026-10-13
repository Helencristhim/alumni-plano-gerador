# -*- coding: utf-8 -*-
"""Aula 17 -- What Should I Do? (modals of obligation and advice).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques (CURRICULO V3, linha 17 do hub): nordico (listening 1 + dialogo) + indiano (listening 2).
Callback da aula 16: must/might/can't de deducao + a clue, a hunch, to jump to conclusions...
Ponte: o MUST tem dois empregos -- na 16 era palpite, hoje e regra e conselho.
Eixo intercultural (fio 🌍): o mesmo conselho soa como ordem numa cultura e como carinho
noutra; o "you might want to" britanico pode ser uma REGRA. Veiculo: visitar uma casa na
Noruega no inverno. Nao usa as cachorras nem a casa em restauro (REGRA DO FATO UNICO;
o restauro e da aula 18).
"""

LESSON = {
    'n': 17,
    'model': 'speech',
    'menu_title': 'What Should I Do?',
    'menu_desc': 'Shoes at the door in Norway, an aunt in India who says you must eat more and an English '
                 'landlady who says you might want to. Tonight, have to, mustn&rsquo;t, should and had better '
                 '-- and how advice sounds in each culture',
    'grammar_point': 'modals of obligation and advice: have to, must, should and had better',
    'chapter_tag': 'House Rules',
    'title_html': 'What Should <span class="accent">I Do?</span>',
    'title_sub': 'A rule, a choice or a good idea? In English, five small words tell you which one.',
    'phases': ['First Words', 'The Words of Your World', 'The Code', 'Many Englishes',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1519681393784-d120267933ba?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, <span class="accent">Good Guesses</span>',
        'callback': 'Make one guess about me with must, might or can&rsquo;t, and use one word from last week: a '
                    'clue, a hunch, evidence, to assume, to jump to conclusions, to read between the lines.',
        'question': 'Then: what is one piece of advice somebody gave you that you still follow today?',
    },
    'framing': {
        'heading': 'Must Has <span class="accent">Two Jobs</span>',
        'steps': [('The Words', 'etiquette, a faux pas, when in Rome...'),
                  ('The Code', 'have to, don&rsquo;t have to, mustn&rsquo;t, should, had better'),
                  ('Many Englishes', 'a Norwegian and an Indian on rules and advice')],
        'note': 'Last week: <strong>They must be home</strong> &mdash; a guess. Tonight: <strong>You have to take '
                'your shoes off</strong> &mdash; a rule, and <strong>You should try the cheese</strong> &mdash; a '
                'good idea. Same small words, a different job. And in each culture, advice sounds a little '
                'different.',
    },
    'hook': {
        'label': 'The Best Advice',
        'heading': 'Who Told You <span class="accent">What to Do?</span>',
        'line1': 'Everybody has one piece of advice they never forgot &mdash; from a grandmother, a teacher, or a '
                 'stranger on a bus.',
        'line2': 'Tell me yours. Who said it, how did they say it, and did you follow it?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">Rules and Advice</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'Etiquette', 'icon': 'book',
         'def': 'The rules of polite behavior in a place or a group',
         'ex': 'In Japan, there is a lot of etiquette around giving gifts.',
         'match': 'the rules of polite behavior in a place or a group'},
        {'word': 'Mandatory', 'icon': 'lock',
         'def': 'Required by a rule, so you have no choice',
         'ex': 'Wearing a seat belt is mandatory in Brazil.',
         'match': 'required by a rule, so you have no choice'},
        {'word': 'Optional', 'icon': 'key',
         'def': 'Not required, so you can choose',
         'ex': 'Dessert is optional, but nobody says no to it.',
         'match': 'not required, so you can choose'},
        {'word': 'To be expected to', 'icon': 'users',
         'def': 'To be supposed to do something because everybody thinks it is normal',
         'ex': 'At a Norwegian dinner, guests are expected to arrive on time.',
         'match': 'to be supposed to do something because it is normal'},
        {'word': 'A faux pas', 'icon': 'alert',
         'def': 'A small social mistake that makes you feel embarrassed',
         'ex': 'I walked into her living room with my shoes on. What a faux pas!',
         'match': 'a small social mistake that makes you feel embarrassed'},
        {'word': 'To frown upon something', 'icon': 'eye',
         'def': 'To think that something is not acceptable',
         'ex': 'In many countries, talking loudly on the train is frowned upon.',
         'match': 'to think that something is not acceptable'},
        {'word': 'Well-meaning', 'icon': 'heart',
         'def': 'Trying to help, even if the result is not perfect',
         'ex': 'My aunt is well-meaning, but her advice is sometimes too much.',
         'match': 'trying to help, even if the result is not perfect'},
        {'word': 'Unwritten rules', 'icon': 'map',
         'def': 'Rules that everybody follows but nobody writes down',
         'ex': 'Every small town has its unwritten rules.',
         'match': 'rules that everybody follows but nobody writes down'},
        {'word': 'To speak your mind', 'icon': 'message',
         'def': 'To say exactly what you think',
         'ex': 'She always speaks her mind, even when it is not easy to hear.',
         'match': 'to say exactly what you think'},
        {'word': 'A rule of thumb', 'icon': 'tool', 'expr': True,
         'def': 'A simple, practical rule that is not exact but usually works',
         'ex': 'As a rule of thumb, arrive five minutes early for dinner in Norway.',
         'match': 'a simple, practical rule that usually works'},
        {'word': 'When in Rome', 'icon': 'globe', 'expr': True,
         'def': 'When you are in another place, follow the customs of that place',
         'ex': 'Dinner at six? Fine. When in Rome, do as the Romans do.',
         'match': 'in another place, follow the customs of that place'},
        {'word': 'To take something the wrong way', 'icon': 'refresh', 'expr': True,
         'def': 'To feel offended by something that was not meant badly',
         'ex': 'Please do not take this the wrong way, but your coat is too thin for Oslo.',
         'match': 'to feel offended by something that was not meant badly'},
    ],
    'vocabnote': 'Three of tonight&rsquo;s words are whole expressions: <strong>a rule of thumb</strong>, '
                 '<strong>when in Rome</strong> and <strong>to take something the wrong way</strong>. Notice the pair '
                 '<strong>mandatory</strong> and <strong>optional</strong>: they are the formal cousins of tonight&rsquo;s '
                 'grammar &mdash; <em>you have to</em> and <em>you don&rsquo;t have to</em>.',
    'pron': [
        'Etiquette',
        'A faux pas',
        'Mandatory',
        'You\'d better bring warm socks.',
    ],
    'gapfill': [
        ('"Taking your shoes off is not ', 'optional', ' in a Norwegian home."'),
        ('"In Japan, there is a lot of ', 'etiquette', ' around giving gifts."'),
        ('"Wearing a seat belt is ', 'mandatory', ' in Brazil."'),
        ('"I walked into her living room with my shoes on. What ', 'a faux pas', '!"'),
        ('"My aunt is ', 'well-meaning', ', but her advice is sometimes too much."'),
        ('"As ', 'a rule of thumb', ', arrive five minutes early for dinner in Norway."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Code)
    'ch3': {
        'heading': 'A Rule, a Choice <span class="accent">or a Good Idea?</span>',
        'sub': 'have to &middot; don&rsquo;t have to &middot; mustn&rsquo;t &middot; should &middot; had better',
    },
    'grammar': {
        'heading': 'Necessary, Not Necessary, <span class="accent">Forbidden, Wise</span>',
        'examples': [
            'In Norway, you <span style="color:#c2410c;font-weight:700">have to</span> take your shoes off at the door.',
            'It is a small dinner. You <span style="color:#1d4ed8;font-weight:700">don\'t have to</span> bring a gift.',
            'You <span style="color:#7c3aed;font-weight:700">mustn\'t</span> smoke inside the house.',
            'It is minus ten tonight. You<span style="color:#15803d;font-weight:700">\'d better</span> bring warm socks.',
        ],
        'prompt': 'Which sentence is a rule? Which one is a choice? Which one is forbidden? Which one is a warning? '
                  'And look at <em>don&rsquo;t have to</em> and <em>mustn&rsquo;t</em>: do they mean the same thing?',
        'rule_rows': [
            ('have to / must + verb', 'Necessary. Have to = a rule from outside. Must = the speaker feels it.',
             'You <strong>have to</strong> take your shoes off.'),
            ('don&rsquo;t have to', 'NOT necessary. You can choose.', 'You <strong>don&rsquo;t have to</strong> bring a gift.'),
            ('mustn&rsquo;t', 'Forbidden. Do not do it.', 'You <strong>mustn&rsquo;t</strong> smoke inside.'),
            ('should / ought to', 'Advice: it is a good idea.', 'You <strong>should</strong> try the brown cheese.'),
            ('had better (&rsquo;d better)', 'Strong advice with a warning: or something bad happens.',
             'You<strong>&rsquo;d better</strong> bring warm socks.'),
            ('past of must and have to', 'Must has no past. Use had to.', 'Last winter I <strong>had to</strong> buy new boots.'),
        ],
        'oneliner': 'have to = necessary, don&rsquo;t have to = you choose, mustn&rsquo;t = forbidden, should = a '
                    'good idea, had better = or else.',
    },
    'practice_heading': 'Rule, Choice <span class="accent">or Advice?</span>',
    'practice_fill': [
        ('"In Norway, you ', 'have to', ' take your shoes off at the door." (a rule)'),
        ('"It is a small dinner. You ', 'don&rsquo;t have to', ' bring a gift." (not necessary)'),
        ('"You ', 'mustn&rsquo;t', ' smoke inside the house." (forbidden)'),
        ('"You ', 'should', ' try the brown cheese. It is delicious." (advice)'),
        ('"It is minus ten tonight. You ', 'had better', ' bring warm socks." (a warning)'),
        ('"Last winter I ', 'had to', ' buy new boots." (careful &mdash; the past)'),
    ],

    # ------------------------------------------------------------ chapter 4 (Many Englishes)
    'ch4': {
        'heading': 'A Norwegian and an Indian <span class="accent">Give Advice</span>',
        'sub': 'Norwegian and Indian English &mdash; and why the same words can be a rule or a hug',
    },
    'dialogue': {
        'heading': 'Packing for <span class="accent">Oslo</span>',
        'guest_name': 'Lars',
        'guest_key': 'lars',
        'guest_voice': 'nordic_m',
        'lines': [
            ('lars', 'So, Ana, you are really coming to Oslo in January? You are a brave woman.'),
            ('ana', 'I am! Tell me the truth. What should I pack?'),
            ('lars', 'Well, you might want to bring wool socks. Actually, you\'d better bring two pairs.'),
            ('ana', 'Two pairs? Is that a Norwegian <span class="vocab-highlight">rule of thumb</span>?'),
            ('lars', 'Sort of. And at my parents\' house you have to take your shoes off at the door. It is not <span class="vocab-highlight">optional</span>.'),
            ('ana', 'Do I have to bring a gift? In Brazil, you never arrive with empty hands.'),
            ('lars', 'You don\'t have to bring anything big. Flowers or chocolate is perfect. But you mustn\'t be late. Dinner at six means six.'),
            ('ana', 'Dinner at six? In Brazil we eat at nine! But okay, <span class="vocab-highlight">when in Rome</span>. I will be there at five to six.'),
        ],
        'comp': [
            ('What does Lars tell Ana to bring for the cold?',
             'Wool socks &mdash; actually two pairs.'),
            ('What is not optional at Lars&rsquo;s parents&rsquo; house?',
             'Taking your shoes off at the door.'),
            ('What does Lars say about the gift and about the time?',
             'She doesn&rsquo;t have to bring anything big &mdash; flowers or chocolate is perfect. But she '
             'mustn&rsquo;t be late: dinner at six means six.'),
        ],
    },
    'listenings': [
        {
            'file': 'a17_listening_ingrid.mp3',
            'voice': 'nordic_f',
            'label': 'Listening 1 &middot; Norway',
            'title': 'The Shoes at <span class="accent">the Door</span>',
            'blurb': 'A Norwegian woman on the unwritten rules of a home in Bergen. Sound first &mdash; no text.',
            'text': 'My name is Ingrid, and I live in Bergen, on the west coast of Norway. People always ask me '
                    'about the rules of a Norwegian home, so here they are. First, you have to take your shoes off '
                    'at the door. Nobody will tell you, but everybody will look at your feet. Second, you don\'t '
                    'have to bring a big present. A small thing is perfect, and something too expensive can make '
                    'people uncomfortable. Third, if dinner is at six, you should arrive at six. Not at ten past '
                    'six, and please, not at a quarter to. And one more thing. When a Norwegian gives you advice, '
                    'it sounds very soft. We say, maybe you could, or it might be an idea to. My Brazilian friend '
                    'Camila did not understand that at first. I told her, it might be an idea to bring a warmer '
                    'coat. She thought it was a small suggestion. It was minus twelve that week. She learned.',
            'qs': [
                ('What do you have to do at the door of a Norwegian home?',
                 'Take your shoes off. Nobody will tell you, but everybody will look at your feet.'),
                ('Why don&rsquo;t you have to bring a big present?',
                 'A small thing is perfect, and something too expensive can make people uncomfortable.'),
                ('What happened to Ingrid&rsquo;s friend Camila, and why?',
                 'She was cold, because Ingrid&rsquo;s advice about a warmer coat sounded soft, like a small '
                 'suggestion. It was minus twelve.'),
            ],
        },
        {
            'file': 'a17_listening_arjun.mp3',
            'voice': 'indian_m',
            'label': 'Listening 2 &middot; India',
            'title': 'You Must <span class="accent">Eat More</span>',
            'blurb': 'An Indian man on advice that sounds like an order &mdash; and an order that sounds like '
                     'advice. Sound first &mdash; no text.',
            'text': 'Hello, I am Arjun, from Pune, in India. In my family, advice is very direct. My aunt says, you '
                    'must eat more, you are too thin. You should call your mother every day. You have to come for '
                    'lunch on Sunday. For a foreigner, this sounds like orders. For us, it is love. If my aunt does '
                    'not tell me what to do, I think she is angry with me. Then I went to study in Manchester, in '
                    'England, and everything was upside down. In my first week, my landlady said, you might want to '
                    'put the bins out on Thursday night. I thought, okay, it is optional. I did not do it. On Friday '
                    'she knocked on my door, very politely, and said, the bins really must go out on Thursday. So '
                    'in India, must can be love. In England, might want to can be a rule. Now, when an English '
                    'person gives me soft advice, I always follow it.',
            'qs': [
                ('How does Arjun&rsquo;s aunt give advice, and what does it mean in his family?',
                 'Very directly: you must eat more, you should call your mother. In his family, it means love.'),
                ('What did Arjun&rsquo;s landlady in Manchester say in his first week?',
                 'You might want to put the bins out on Thursday night.'),
                ('What did Arjun learn about soft advice in England?',
                 'That it can be a rule. Now he always follows it.'),
            ],
        },
    ],
    'artifact': {
        'heading': 'The House <span class="accent">Rules</span>',
        'title': 'WELCOME TO FJORDHYTTA &mdash; HOUSE RULES',
        'subtitle': 'Guest: Ana Claudia Veraldi &middot; 14&ndash;18 January',
        'corner': 'Check-in<br>after 15:00',
        'label_width': '120px',
        'rows': [
            ('Shoes', 'Please leave all shoes in the entrance. Slippers are in the basket.'),
            ('Fireplace', 'Use only the dry wood in the shed. Never leave the fire alone.'),
            ('Quiet hours', '22:00 to 07:00. The neighbors live very close.'),
            ('Bed linen', 'Included. There is no need to bring your own.'),
            ('Check-out', 'By 11:00. Leave the key in the box by the door.'),
        ],
        'comp': [
            ('Read the rows about shoes and the fireplace. Say two rules with have to or mustn&rsquo;t.',
             '"You have to leave your shoes in the entrance. You mustn&rsquo;t leave the fire alone."'),
            ('What is not necessary? Say it with don&rsquo;t have to.',
             '"You don&rsquo;t have to bring your own bed linen. It is included."'),
            ('Give Ana one piece of advice for this trip, with should or had better.',
             '"She&rsquo;d better arrive before dark &mdash; in January it gets dark around half past three. And '
             'she should try the fireplace on the first night."'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('You don&rsquo;t have to smoke here. It is forbidden.', 'You mustn&rsquo;t smoke here. It is forbidden.'),
        ('You should to take off your shoes.', 'You should take off your shoes.'),
        ('Yesterday I must leave early.', 'Yesterday I had to leave early.'),
        ('You had better to bring a coat.', 'You had better bring a coat.'),
    ],
    'quickfire': [
        {'situation': 'A friend from abroad is staying at your house for the first time. Tell her one rule of the house.',
         'tips': ['You have to close the front gate. You don&rsquo;t have to take your shoes off.',
                  'Have to for a rule, don&rsquo;t have to for a choice.']},
        {'situation': 'A friend is going to Norway in January. Give her strong advice, with a warning.',
         'tips': ['You&rsquo;d better bring warm boots, or your feet will freeze.',
                  'Had better = advice + a warning. No to after it.']},
        {'situation': 'Explain the difference: you mustn&rsquo;t smoke here / you don&rsquo;t have to smoke here.',
         'tips': ['Mustn&rsquo;t = it is forbidden. Don&rsquo;t have to = you can choose. Very different!',
                  'This is the biggest trap of the lesson.']},
        {'situation': 'Tell me something you had to do last week. Careful with the past.',
         'tips': ['Last week I had to take my car to the mechanic.',
                  'Must has no past. Use had to.']},
        {'situation': 'A British friend says: you might want to bring an umbrella. What does she really mean?',
         'tips': ['She means: bring an umbrella! Soft advice can be a strong suggestion.',
                  'Remember Arjun and the bins.']},
        {'situation': 'Give a foreign visitor one piece of advice about Brazil.',
         'tips': ['You should try the cheese bread, and you&rsquo;d better not drive in Sao Paulo at six.',
                  'This one has no grammar target. Say the true thing.']},
    ],
    'speaking': [
        ('What is one unwritten rule in your town that a visitor would not know?',
         'You have to say good morning to everybody at the bakery. If you do not, people think you are rude.'),
        ('What advice would you give someone who is moving from a big city to a small town?',
         'You should learn the names of your neighbors. And you&rsquo;d better buy a good flashlight.'),
        ('Is there anything you had to learn the hard way when you traveled?',
         'In Lisbon I had to learn that dinner starts late. I arrived at seven and the restaurant was empty.'),
        ('When someone gives you very direct advice, do you take it the wrong way?',
         'Not usually. I like people who speak their mind, as long as they are kind.'),
    ],
    'building': [
        ('in Norway / you / have to / take off / your shoes',
         'In Norway, you have to take off your shoes.'),
        ('it / be / a small dinner / you / not have to / bring a gift',
         'It is a small dinner, so you don&rsquo;t have to bring a gift.'),
        ('you / mustn&rsquo;t / be late / dinner / start / at six',
         'You mustn&rsquo;t be late. Dinner starts at six.'),
        ('yesterday / I / must / leave early (careful: the past)',
         'Yesterday I had to leave early.'),
    ],
    'answerkey_heading': 'Rules and Advice on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        '<strong>have to</strong> + verb = necessary, often a rule from outside: You have to take your shoes off.',
        '<strong>must</strong> + verb = necessary, the speaker feels it: I must call my mother tonight.',
        '<strong>don&rsquo;t have to</strong> = not necessary, you choose: You don&rsquo;t have to bring a gift.',
        '<strong>mustn&rsquo;t</strong> = forbidden: You mustn&rsquo;t smoke inside. It is NOT the same as don&rsquo;t have to.',
        '<strong>should / ought to</strong> = advice: You should try the brown cheese.',
        '<strong>had better</strong> = strong advice + a warning: You&rsquo;d better bring warm socks.',
        'No to after must, should and had better. The past of must is <strong>had to</strong>.',
        'And the one that is not grammar: a direct you must can be love, and a soft you might want to can be a rule. Listen to who is speaking.',
    ],
    'rp_chapter_heading': 'Rules and Advice, <span class="accent">Out Loud</span>',
    'roleplays': [
        {'heading': 'Packing for <span class="accent">Oslo</span>',
         'scenario': 'You are talking to Lars, a Norwegian friend. You are going to visit his family in January. '
                     'Ask him three things: what you should pack, what you have to do in the house, and what you '
                     'don&rsquo;t have to worry about.',
         'chips': ['What should I', 'Do I have to', 'I&rsquo;d better']},
        {'heading': 'The Aunt Who <span class="accent">Gives Orders</span>',
         'scenario': 'Now you are having lunch with Arjun&rsquo;s aunt in Pune. She says you must eat more and you '
                     'should visit India every year. Answer warmly, accept one piece of advice, and politely say no '
                     'to another.',
         'chips': ['That is very kind, but', 'You are right, I should', 'I don&rsquo;t have to']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'A friend from abroad is coming to stay with you for a week. Tell them the house rules, what '
                     'they should see in your region, and one thing they had better not do.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'Rules, Choices <span class="accent">and Good Ideas</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Rules and Advice</span>',
    'survival': [
        'Do I have to bring anything?',
        'You don\'t have to, but it is a nice idea.',
        'You mustn\'t be late. Dinner is at six.',
        'You\'d better bring warm socks.',
        'When in Rome, do as the Romans do.',
    ],
    'checklist': [
        'I use have to for rules and don&rsquo;t have to when there is a choice.',
        'I know that mustn&rsquo;t means forbidden, not optional.',
        'I give advice with should and warnings with had better.',
        'I use had to for the past, never must.',
        'I know the words: etiquette, a faux pas, a rule of thumb, when in Rome, to take something the wrong way.',
    ],
    'badge': {
        'name': 'House Rules',
        'text': 'Tonight you learned the rules, the choices and the good ideas, Ana &mdash; and how they sound in '
                'Oslo, in Pune and in Manchester.',
        'next': 'The Story Behind the Object',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'rules and advice.&quot; Ponte com a aula 16: o MUST tem dois empregos &mdash; semana passada era '
                 'palpite (they must be home), hoje e regra e conselho. Eixo intercultural: o mesmo conselho soa '
                 'como ordem numa cultura e como carinho em outra.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 16: ELA faz um palpite sobre voce '
                  'com must, might ou can&apos;t e usa uma palavra da aula passada (a clue, a hunch, evidence, to '
                  'assume, to jump to conclusions, to read between the lines). Responda de verdade. PONTE (REGRA '
                  '27B): &quot;Good guess. Now, a different kind of must.&quot; e a pergunta do slide. ZERO '
                  'correcao. Anote se ela diz &quot;you must to&quot; ou &quot;I must&quot; no passado.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos e leia a nota: a mesma palavra, '
                   'must, com outro emprego. So plante a diferenca regra / escolha / conselho &mdash; a tabela vem '
                   'no capitulo 3.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela contar o conselho que nunca esqueceu. '
                'Pergunte COMO a pessoa falou: foi uma ordem ou uma sugestao? Anote a frase exata &mdash; ela volta '
                'no capitulo 3.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for rules and advice. '
                       'Three of them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> CCQ mandatory: &quot;Can you choose? (Nao.)&quot; CCQ '
                  'optional: &quot;Can you say no? (Sim.)&quot; CCQ a faux pas: &quot;Is it a crime? (Nao, so uma '
                  'gafe social.)&quot; CCQ to frown upon: &quot;Is it forbidden by law? (Nao, as pessoas nao '
                  'aprovam.)&quot; Peca um exemplo do Brasil em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ well-meaning: &quot;Does the person want to '
                  'help? (Sim.) Is the result always good? (Nao.)&quot; CCQ unwritten rules: &quot;Are they on a '
                  'sign? (Nao.)&quot; CCQ when in Rome: &quot;Whose customs do you follow? (Os do lugar.)&quot; CCQ '
                  'to take something the wrong way: &quot;Did the person want to offend you? (Nao.)&quot;',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'mandatory e optional sao os primos formais de have to e don&apos;t have to.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> ET-i-ket (forca no ET, o final &quot;-quette&quot; '
                'soa /ket/), a FOH PAH (o x e o s de faux pas NAO soam), MAN-da-to-ry (americano: MAN-da-tor-ee). '
                'Na frase: you&apos;d better = /YOOD BET-er/, o t vira quase d no americano. 2 repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas '
                   'estao no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. A rule, a choice or a '
                     'good idea?&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases (toque o audio). Pergunte: '
                   '&quot;Which one is a rule? A choice? Forbidden? A warning?&quot; O ponto central: don&apos;t '
                   'have to e mustn&apos;t NAO sao a mesma coisa (em PT os dois parecem &quot;nao precisa / nao '
                   'pode&quot;). So entao &quot;Reveal the Rule&quot;. CCQs: &quot;You don&apos;t have to bring a '
                   'gift &mdash; can I bring one? (Sim.)&quot; &quot;You mustn&apos;t smoke &mdash; can I? (Nao.)&quot; '
                   '&quot;You&apos;d better bring socks &mdash; what happens if I don&apos;t? (Frio.)&quot; Volte a '
                   'frase anotada no hook.',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a forma ORALMENTE antes de clicar. O item 6 e a '
                    'armadilha: passado de must = had to.',
        'ch4_trans': '<strong>Transicao Many Englishes (1 min):</strong> Diga: &quot;Two Norwegians and an Indian on '
                     'rules and advice.&quot; Avise os sotaques: noruegues (melodia que sobe e desce, vogais '
                     'longas) e indiano (r batido, ritmo silabico, t e d retroflexos).',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Lars, amigo noruegues. Clique &quot;Next Line&quot; '
                    'e toque o audio. Nas falas da Ana, peca que ELA fale primeiro. PRAGMATICA: o Lars comeca suave '
                    '(you might want to) e logo endurece (you&apos;d better) &mdash; o conselho noruegues e baixo, '
                    'mas e serio. Pergunte depois: &quot;In Brazil, would you say you might want to or you have '
                    'to?&quot;',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o LARS, nunca sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque NORUEGUES: a melodia sobe e desce dentro da frase, o r '
                      'e batido, vogais longas. Toque 2 vezes. No fim: &quot;Was Ingrid&apos;s advice a suggestion or a '
                      'rule?&quot; (Uma regra disfarcada.)',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'INDIANO: ritmo silabico (cada silaba com o mesmo peso), r batido, t e d com a lingua para tras. '
                      'Toque 2 vezes. Pergunte: &quot;Arjun&apos;s aunt and the landlady: who was more polite?&quot; '
                      '(As duas &mdash; cada uma do seu jeito.)',
        'artifact': '<strong>Artefato (5 min):</strong> As regras da cabana alugada na Noruega, em nome dela. Peca '
                    'que leia cada linha e transforme em frase com have to / mustn&apos;t / don&apos;t have to. '
                    'Depois as 3 perguntas &mdash; ela responde antes de revelar.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick answers, '
                     'and your own rules.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 4 erros classicos: '
                     'don&apos;t have to no lugar de mustn&apos;t, to depois de should, must no passado, to depois '
                     'de had better.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 3a e a armadilha principal (mustn&apos;t x don&apos;t have to).',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija pelo '
                    'menos um had to e um had better. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica para '
                    'comparar. O item 4 e passado: had to. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so no fim, para conferir. A linha 8 e a pragmatica: '
                     'vale uma pausa e uma pergunta sobre o Brasil.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Rules and '
                     'advice, three times.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o Lars. Responda as 3 perguntas dela com conselhos '
               'suaves que sao regras (you might want to...). Corrija SO a estrutura (should / have to / had better '
               '+ verbo, sem to).',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e a tia do Arjun: direta e carinhosa (you must eat '
               'more!). Ela aceita um conselho e recusa outro com educacao (callback da aula 14: tactful, to hedge). '
               'Se ela ficar sem saida, ensine &quot;That is very kind of you, but...&quot;.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. NAO corrija durante. Conte '
               'quantas formas diferentes ela usa (have to, don&apos;t have to, mustn&apos;t, should, had better) e '
               'diga o numero no fim. Anote qualquer &quot;should to&quot; para o feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Uma pergunta, '
                    'tres respostas (escolha, proibido, aviso) e a expressao da noite.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Now you know the rules &mdash; and how they '
                 'sound.&quot; Homework (oralmente, opcional): um audio de um minuto com as regras da casa dela para '
                 'um visitante estrangeiro: tres com have to / don&apos;t have to / mustn&apos;t e dois conselhos. '
                 'Proxima aula: The Story Behind the Object &mdash; relative clauses e a historia por tras de um '
                 'objeto.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'What Should I Do? -- Rules, Choices and Advice',
        'desc': 'Shoes at the door in Norway, an aunt in India and an English landlady: have to, don\'t have to, mustn\'t, should and had better.',
        'context_paras': [
            'When Camila, a Brazilian, visited her friend Ingrid in Bergen, she learned the <strong>unwritten '
            'rules</strong> fast. In a Norwegian home you <strong>have to</strong> take your shoes off at the door, '
            'and you <strong>don&rsquo;t have to</strong> bring an expensive present &mdash; a small one is better.',
            'Ingrid also gave her some soft advice: <em>it might be an idea to bring a warmer coat</em>. Camila '
            'thought it was <strong>optional</strong>. It was not. It was minus twelve. Ingrid laughed: <em>Next '
            'time, you <strong>had better</strong> listen when a Norwegian says maybe.</em>',
            'In India, Arjun&rsquo;s aunt gives advice the opposite way: <em>you <strong>must</strong> eat more, you '
            '<strong>should</strong> call your mother.</em> It sounds like an order, but it is love, and nobody '
            '<strong>takes</strong> it <strong>the wrong way</strong>. <strong>When in Rome</strong>, listen to how '
            'people give advice before you decide what it means.',
        ],
        'context_quiz': [
            ('"You don&rsquo;t have to bring an expensive present." What does it mean?',
             [('You can bring one, but it is not necessary.', True),
              ('It is forbidden to bring any present to a Norwegian home.', False),
              ('You must bring a present.', False)]),
            ('Why was Camila cold in Bergen?',
             [('Ingrid told her not to bring a coat because the house was warm.', False),
              ('She thought Ingrid&rsquo;s soft advice was optional.', True),
              ('The house had no heating.', False)]),
            ('How does Arjun&rsquo;s family understand his aunt&rsquo;s direct advice?',
             [('As an order that he has to obey or she gets angry.', False),
              ('As rude.', False),
              ('As love.', True)]),
        ],
        'tip_title': 'Rules, Choices and Advice',
        'tip_sub': 'Necessary, not necessary, forbidden, a good idea, a warning &mdash; five different jobs.',
        'tip_rows': [
            ('have to / must', 'Necessary', 'You <strong>have to</strong> take your shoes off.'),
            ('don&rsquo;t have to', 'Not necessary &mdash; you choose', 'You <strong>don&rsquo;t have to</strong> bring a gift.'),
            ('mustn&rsquo;t', 'Forbidden', 'You <strong>mustn&rsquo;t</strong> smoke inside.'),
            ('should / ought to', 'Advice', 'You <strong>should</strong> try the brown cheese.'),
            ('had better', 'Strong advice + a warning', 'You<strong>&rsquo;d better</strong> bring warm socks.'),
            ('had to', 'The past of must and have to', 'Last winter I <strong>had to</strong> buy boots.'),
        ],
        'tip_never': 'You should to go &middot; you had better to go &middot; yesterday I must leave &middot; you '
                     'don&rsquo;t have to smoke here (when you mean it is forbidden). After must, should and had '
                     'better: the base verb, no to. For the past of must, use had to.',
        'fills': [
            ('In Norway, you ', 'have to', ' take your shoes off at the door.',
             'a rule -- two words'),
            ('It is a small dinner. You ', 'don\'t have to', ' bring a gift.',
             'not necessary -- three words, one with an apostrophe'),
            ('You ', 'mustn\'t', ' smoke inside the house.',
             'forbidden -- one word with an apostrophe'),
            ('It is minus ten tonight. You had ', 'better', ' bring warm socks.',
             'one word -- strong advice with a warning'),
            ('Last winter I ', 'had to', ' buy new boots.',
             'two words -- the past of must'),
            ('Wearing a seat belt is ', 'mandatory', ' in Brazil.',
             'one word -- required by a rule, no choice'),
        ],
        'order_intro': 'Lars helps Ana get ready for a trip to Oslo. Put the conversation in order.',
        'order': [
            'So, Ana, you are really coming to Oslo in January?',
            'I am! Tell me the truth. What should I pack?',
            'You might want to bring wool socks. Actually, you\'d better bring two pairs.',
            'Do I have to bring a gift for your parents?',
            'You don\'t have to bring anything big. But you mustn\'t be late. Dinner at six means six.',
            'Dinner at six? Okay. When in Rome, I will be there at five to six.',
        ],
        'quiz': [
            ('A sign in a museum says you cannot use your phone. You tell a friend:',
             [('"You don\'t have to use your phone here."', False),
              ('"You mustn\'t use your phone here."', True),
              ('"You had better to use your phone here."', False)]),
            ('A friend asks if she needs to bring food to a barbecue. It is not necessary. You say:',
             [('"You mustn\'t bring anything."', False),
              ('"You don\'t have to bring anything, but drinks are always welcome."', True),
              ('"You must to bring something."', False)]),
            ('Your English neighbor says: you might want to move your car before the street is cleaned. She means:',
             [('Moving the car is a nice idea, but nothing will happen if you forget.', False),
              ('You really should move it.', True),
              ('She wants to borrow your car.', False)]),
            ('You wore shoes in a Norwegian living room and everybody looked at your feet. It was:',
             [('a faux pas', True),
              ('a rule of thumb that everybody in Norway follows at dinner', False),
              ('mandatory', False)]),
        ],
        'think': 'A friend from another country is coming to stay with you for a week. Record a short message for '
                 'them. Tell them three house rules (have to, don&rsquo;t have to, mustn&rsquo;t), give two pieces of '
                 'advice about your region (should, had better), and use one of tonight&rsquo;s expressions.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Film',
         'title': 'The Hundred-Foot Journey (2014) &mdash; official trailer',
         'desc': 'An Indian family opens a restaurant in a small French village, right across the street from a '
                 'very proud French chef. Two cultures, two sets of unwritten rules, and a lot of advice nobody asked '
                 'for.',
         'tip': 'watch the trailer, then say three rules of each restaurant with have to and mustn&rsquo;t.',
         'url': 'https://www.youtube.com/watch?v=sH9cr8wgULI', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'The Scandi Shift &mdash; Episode 21: Visiting Denmark: Culture Shocks, Unwritten Rules &amp; Survival Tips',
         'desc': 'Two people who live in Scandinavia explain the small rules a visitor does not see &mdash; and how '
                 'not to make a faux pas on your first visit.',
         'tip': 'write down every have to, should and don&rsquo;t have to you hear, then make your own list for Brazil.',
         'url': 'https://podcasts.apple.com/us/podcast/episode-21-visiting-denmark-culture-shocks-unwritten/id1864125206?i=1000792308859',
         'cta': 'Listen on Apple Podcasts'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'Cross cultural communication &mdash; Pellegrino Riccardi, TEDxBergen',
         'desc': 'An Italian who lives in Norway explains, with a lot of humor, why Norwegians and Italians drive, '
                 'queue and give advice in completely different ways.',
         'tip': 'pause after each story and say what a visitor should and shouldn&rsquo;t do in Norway.',
         'url': 'https://www.youtube.com/watch?v=YMyofREc5Jk', 'cta': 'Watch on YouTube'},
    ],
}
