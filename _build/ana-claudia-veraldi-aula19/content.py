# -*- coding: utf-8 -*-
"""Aula 19 -- Small Talk: What's Safe to Ask Where (ANCORA intercultural).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques (CURRICULO V3, linha 19): holandes (listening 1), indiano (listening 2), americano (dialogo).
Ancora (a cada 5): o ponto nao e so gramatica -- e a ESCALA do que e seguro perguntar em cada
cultura. O Discovery descobre a FUNCAO de cada conector/filler (ganhar tempo, explicar, mudar de
assunto, ligar ao assunto anterior, voltar). O Spot the Error inclui um erro que NAO e de lingua
(perguntar salario a um americano que acabou de conhecer).
Callback da aula 18: relative clauses + an heirloom, a flea market, vintage, to haggle...
Veiculo: uma aula de culinaria em Lisboa (social, ZERO profissional). Nao usa as cachorras nem a casa.
Vocab de aulas anteriores que NAO pode voltar como novo: filler words, come to think of it,
off the top of my head, awkward, nosy, chatty, blunt, tactful.
"""

LESSON = {
    'n': 19,
    'model': 'speech',
    'menu_title': 'Small Talk -- What&rsquo;s Safe to Ask Where',
    'menu_desc': 'A Dutchman who answers how are you honestly, an Indian auntie who asks about your salary and an '
                 'American at a cooking class in Lisbon. Tonight, the little words that keep small talk going '
                 '-- and the questions that are safe in each culture',
    'grammar_point': 'connectors and fluency fillers for small talk: well, I mean, actually, by the way, speaking of and anyway',
    'chapter_tag': 'Intercultural Anchor',
    'title_html': 'Small Talk &mdash; <span class="accent">What&rsquo;s Safe to Ask Where</span>',
    'title_sub': 'The weather is safe everywhere. Your salary is not. And a few small words keep the conversation alive.',
    'phases': ['First Words', 'The Words of Your World', 'The Code', 'Many Englishes',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, <span class="accent">Old Things</span>',
        'callback': 'Tell me about one object in your house with a relative clause, and use one word from last '
                    'week: an heirloom, a flea market, vintage, sentimental value, to haggle.',
        'question': 'Then: when you meet a stranger at a party, what is the first thing you usually say?',
    },
    'framing': {
        'heading': 'The Talk Before <span class="accent">the Talk</span>',
        'steps': [('The Words', 'small talk, to break the ice, common ground...'),
                  ('The Code', 'well, I mean, actually, by the way, speaking of, anyway'),
                  ('Many Englishes', 'a Dutchman, an Indian and an American on small talk')],
        'note': 'Last week, objects with a story. Tonight, the five minutes before any real conversation: '
                '<strong>small talk</strong>. Two things make it work. The right <strong>topic</strong> &mdash; '
                'and that changes from culture to culture. And the small <strong>words</strong> that connect what '
                'you say: <em>well, by the way, anyway</em>.',
    },
    'hook': {
        'label': 'Safe or Not?',
        'heading': 'What Would You <span class="accent">Never Ask?</span>',
        'line1': 'In Brazil, people ask about your family in the first five minutes. In other countries, '
                 'that is a little too much.',
        'line2': 'Is there a question you would never ask a stranger? And one that a foreigner asked you that '
                 'surprised you?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">Small Talk</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'Small talk', 'icon': 'message',
         'def': 'Light, friendly conversation about easy topics, often with people you do not know well',
         'ex': 'We made small talk about the weather while we waited for the bus.',
         'match': 'light, friendly conversation about easy topics'},
        {'word': 'Off-limits', 'icon': 'lock',
         'def': 'Not allowed; a topic you should not talk about',
         'ex': 'In many countries, money is off-limits when you meet someone new.',
         'match': 'not allowed; a topic you should not talk about'},
        {'word': 'Intrusive', 'icon': 'eye',
         'def': 'Asking about things that are too private',
         'ex': 'Asking a stranger about her age can feel intrusive.',
         'match': 'asking about things that are too private'},
        {'word': 'Harmless', 'icon': 'shield',
         'def': 'Not able to hurt or offend anybody',
         'ex': 'A question about the weather is completely harmless.',
         'match': 'not able to hurt or offend anybody'},
        {'word': 'To pry', 'icon': 'help',
         'def': 'To try to find out about somebody&rsquo;s private life',
         'ex': 'I do not want to pry, but are you two related?',
         'match': 'to try to find out about somebody\'s private life'},
        {'word': 'Common ground', 'icon': 'link',
         'def': 'Interests or experiences that two people share',
         'ex': 'We found some common ground: we both love old houses.',
         'match': 'interests or experiences that two people share'},
        {'word': 'Rapport', 'icon': 'heart',
         'def': 'A friendly feeling of understanding between two people',
         'ex': 'After ten minutes of chatting, there was a nice rapport between us.',
         'match': 'a friendly feeling of understanding between two people'},
        {'word': 'A lull', 'icon': 'moon',
         'def': 'A short, quiet moment when nobody is talking',
         'ex': 'When there was a lull in the conversation, she asked about the food.',
         'match': 'a short, quiet moment when nobody is talking'},
        {'word': 'To mingle', 'icon': 'users',
         'def': 'To move around a party and talk to different people',
         'ex': 'Before dinner, the guests had time to mingle in the garden.',
         'match': 'to move around a party and talk to different people'},
        {'word': 'To break the ice', 'icon': 'zap', 'expr': True,
         'def': 'To say or do something that makes people feel relaxed at the start',
         'ex': 'A joke about the rain helped to break the ice.',
         'match': 'to make people feel relaxed at the start'},
        {'word': 'To keep the ball rolling', 'icon': 'refresh', 'expr': True,
         'def': 'To keep a conversation or an activity going',
         'ex': 'She asked another question to keep the ball rolling.',
         'match': 'to keep a conversation going'},
        {'word': 'To touch a nerve', 'icon': 'alert', 'expr': True,
         'def': 'To talk about something that upsets a person',
         'ex': 'I asked about his job, and I think I touched a nerve.',
         'match': 'to talk about something that upsets a person'},
    ],
    'vocabnote': 'Three of tonight&rsquo;s words are whole expressions: <strong>to break the ice</strong>, '
                 '<strong>to keep the ball rolling</strong> and <strong>to touch a nerve</strong>. Notice the pair '
                 '<strong>harmless</strong> and <strong>intrusive</strong>: every small-talk question sits somewhere '
                 'between them &mdash; and the line moves from country to country.',
    'pron': [
        'Rapport',
        'Intrusive',
        'Off-limits',
        'By the way, where are you from?',
    ],
    'gapfill': [
        ('"In many countries, money is ', 'off-limits', ' when you meet someone new."'),
        ('"A question about the weather is completely ', 'harmless', '."'),
        ('"We found some ', 'common ground', ': we both love old houses."'),
        ('"When there was ', 'a lull', ' in the conversation, she asked about the food."'),
        ('"Before dinner, the guests had time to ', 'mingle', ' in the garden."'),
        ('"A joke about the rain helped to ', 'break the ice', '."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Code)
    'ch3': {
        'heading': 'Small Words, <span class="accent">Big Jobs</span>',
        'sub': 'well &middot; I mean &middot; actually &middot; by the way &middot; speaking of &middot; anyway',
    },
    'grammar': {
        'heading': 'What Does Each <span class="accent">Little Word Do?</span>',
        'examples': [
            '<span style="color:#c2410c;font-weight:700">Well</span>, let me think... I&rsquo;d say Lisbon.',
            '<span style="color:#1d4ed8;font-weight:700">By the way</span>, where are you from?',
            '<span style="color:#7c3aed;font-weight:700">Speaking of</span> food, have you tried the custard tarts?',
            '<span style="color:#15803d;font-weight:700">Anyway</span>, as I was saying, the class starts at seven.',
        ],
        'prompt': 'Look at the colored words. Which one gives you a second to think? Which one opens a completely '
                  'new topic? Which one opens a new topic that is connected to the last one? And which one goes '
                  'back to the main topic?',
        'rule_rows': [
            ('well / let me see', 'Buys time. You need a second to think.', '<strong>Well</strong>, let me see... about ten years.'),
            ('I mean', 'Explains or corrects what you just said.', 'It&rsquo;s small. <strong>I mean</strong>, it&rsquo;s not tiny, but...'),
            ('actually', 'Adds a surprise, or politely says the opposite.', '<strong>Actually</strong>, I&rsquo;m from S&atilde;o Paulo, not Rio.'),
            ('by the way', 'Opens a new topic with no link to the last one.', '<strong>By the way</strong>, do you like football?'),
            ('speaking of + noun', 'Opens a new topic linked to the last word.', '<strong>Speaking of</strong> coffee, have you been to Brazil?'),
            ('anyway', 'Goes back to the main topic, or starts to close the chat.', '<strong>Anyway</strong>, it was nice talking to you.'),
        ],
        'oneliner': 'well = wait, I&rsquo;m thinking; I mean = let me explain; actually = a surprise; by the way = '
                    'new topic; speaking of = new topic, same thread; anyway = back, or goodbye.',
    },
    'practice_heading': 'Which <span class="accent">Little Word?</span>',
    'practice_fill': [
        ('"', 'Well', ', let me think... maybe fifteen years?" (buying time)'),
        ('"The town is quiet. ', 'I mean', ', there is a festival in June, but that&rsquo;s it." (explaining)'),
        ('"', 'By the way', ', do you know where the restroom is?" (a new topic, no link)'),
        ('"', 'Speaking of', ' festivals, have you been to the one in Parintins?" (a new topic, linked)'),
        ('"', 'Anyway', ', I think the chef is here. Nice to meet you!" (closing)'),
        ('"Everybody thinks I&rsquo;m from Rio. ', 'Actually', ', I&rsquo;m from the interior." (a surprise)'),
    ],

    # ------------------------------------------------------------ chapter 4 (Many Englishes)
    'ch4': {
        'heading': 'A Dutchman, an Indian <span class="accent">and an American</span>',
        'sub': 'Dutch, Indian and American English &mdash; and three ideas of what is safe to ask',
    },
    'dialogue': {
        'heading': 'Before the <span class="accent">Class Starts</span>',
        'guest_name': 'Mike',
        'guest_key': 'mike',
        'guest_voice': 'arthur',
        'lines': [
            ('mike', 'Hi! Is this the pastry class? I think I\'m a little early.'),
            ('ana', 'Me too. Well, at least we get the best seats. I\'m Ana, from Brazil.'),
            ('mike', 'Mike, from Ohio. So, what brings you to Lisbon?'),
            ('ana', 'A short vacation. I mean, it\'s mostly an excuse to eat. By the way, have you done a class like this before?'),
            ('mike', 'Never. My wife booked it. Speaking of food, have you tried the custard tarts yet?'),
            ('ana', 'Three times! We have something similar in Brazil, so we already have some <span class="vocab-highlight">common ground</span>.'),
            ('mike', 'Ha! That\'s a nice way to <span class="vocab-highlight">break the ice</span>. Anyway, I think the chef is here.'),
            ('ana', 'Perfect timing. It was nice talking to you, Mike. Let\'s sit together.'),
        ],
        'comp': [
            ('Where is Mike from, and why is he at the class?',
             'He is from Ohio. His wife booked the class.'),
            ('Which word does Mike use to change the topic to the custard tarts?',
             'Speaking of &mdash; &ldquo;Speaking of food, have you tried the custard tarts yet?&rdquo;'),
            ('How does Mike close the small talk?',
             'With anyway: &ldquo;Anyway, I think the chef is here.&rdquo;'),
        ],
    },
    'listenings': [
        {
            'file': 'a19_listening_pieter.mp3',
            'voice': 'dutch_m',
            'label': 'Listening 1 &middot; The Netherlands',
            'title': 'How Are You? <span class="accent">An Honest Answer</span>',
            'blurb': 'A Dutchman on why his small talk is short and very direct. Sound first &mdash; no text.',
            'text': 'Hi, I\'m Pieter, and I live in Utrecht, in the Netherlands. People say the Dutch are very '
                    'direct, and well, it\'s true. We are not great at small talk. At a party, I might ask you how '
                    'much you paid for your house, or why you don\'t have children. For us, these questions are '
                    'harmless. I mean, we are just curious. The first time I visited a friend in Texas, a woman at '
                    'the supermarket asked me, how are you doing? So I told her. My back hurt, my flight was late, '
                    'and I missed my wife. She just smiled and walked away. Actually, she did not want an answer at '
                    'all. It was just hello. By the way, the weather is the one topic that is safe everywhere, even '
                    'in Holland, because it is always bad. Anyway, now when an American asks me how I am, I say, '
                    'good, thanks, and you? Ten seconds. Done.',
            'qs': [
                ('What questions might Pieter ask at a party, and why does he think they are okay?',
                 'How much you paid for your house, or why you don&rsquo;t have children. For the Dutch, they are '
                 'harmless &mdash; people are just curious.'),
                ('What happened at the supermarket in Texas?',
                 'A woman asked how he was doing, and he told her everything. She just smiled and walked away: it '
                 'was only hello.'),
                ('Which topic is safe everywhere, according to Pieter, and why does he joke about Holland?',
                 'The weather. In Holland it is safe because it is always bad.'),
            ],
        },
        {
            'file': 'a19_listening_priya.mp3',
            'voice': 'indian_f',
            'label': 'Listening 2 &middot; India',
            'title': 'The Auntie <span class="accent">at the Wedding</span>',
            'blurb': 'An Indian woman in London on personal questions, the weather and the quiet moments in a '
                     'conversation. Sound first &mdash; no text.',
            'text': 'Hello, I\'m Priya. I grew up in Chennai, in the south of India, and now I live in London. In '
                    'India, small talk is very personal. An auntie you meet at a wedding will ask, are you married? '
                    'Why not? How much does your husband earn? It is not rude. It is a way of saying, I care about '
                    'you. In London, I learned that those questions are off-limits. You do not ask about money, age '
                    'or religion. So what do the British talk about? Well, the weather, the trains, and the weather '
                    'again. At first, I thought it was boring. I mean, who cares if it is raining? But then I '
                    'understood. The weather is common ground. Everybody has an opinion, and nobody gets hurt. '
                    'Actually, now I am the one who starts. When there is a lull in the conversation, I say, lovely '
                    'day, isn\'t it? Even when it isn\'t.',
            'qs': [
                ('What does an auntie at an Indian wedding ask, and what does it mean?',
                 'Are you married? Why not? How much does your husband earn? It means: I care about you.'),
                ('Which topics are off-limits in London?',
                 'Money, age and religion.'),
                ('What does Priya do now when there is a lull in the conversation?',
                 'She talks about the weather: &ldquo;Lovely day, isn&rsquo;t it?&rdquo; &mdash; even when it isn&rsquo;t.'),
            ],
        },
    ],
    'artifact': {
        'heading': 'Your <span class="accent">Class Card</span>',
        'title': 'PAST&Eacute;IS DE NATA MASTERCLASS &mdash; LISBON',
        'subtitle': 'Guest: Ana Claudia Veraldi &middot; Thursday, 18:45',
        'corner': 'Rua da<br>Prata, 112',
        'label_width': '120px',
        'rows': [
            ('Arrival', '18:45. Welcome drink and fifteen minutes to mingle before the class.'),
            ('Name tag', 'Write your first name and the country you are from.'),
            ('Talk about', 'Your favorite dish, your travels and what brought you to Lisbon.'),
            ('Please avoid', 'Politics and religion. This is a pastry class!'),
            ('Class', '19:00 to 21:30. Your tarts go home with you.'),
        ],
        'comp': [
            ('You have fifteen minutes to mingle. Start a conversation with a stranger, using one topic from the card.',
             '&ldquo;So, what brought you to Lisbon? I mean, apart from the custard tarts.&rdquo;'),
            ('The other person starts talking about politics. Change the topic politely.',
             '&ldquo;Speaking of Lisbon, have you been to Bel&eacute;m yet?&rdquo; or &ldquo;By the way, where are '
             'you from?&rdquo;'),
            ('It is 19:00 and the chef arrives. Close the conversation politely.',
             '&ldquo;Anyway, I think we&rsquo;re starting. It was nice talking to you!&rdquo;'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('Speaking of the weather, by the way, anyway, it is cold.', 'Speaking of the weather, it is cold today, isn&rsquo;t it?'),
        ('By the way of food, have you tried the tarts?', 'Speaking of food, have you tried the tarts?'),
        ('Actually it is very nice to meet you, actually.', 'It is very nice to meet you.'),
        ('So, how much do you earn? (to an American you just met)', 'So, what do you do for fun? (money is off-limits)'),
    ],
    'quickfire': [
        {'situation': 'You meet someone at a party and there is a lull. Say something to keep the ball rolling.',
         'tips': ['So, how do you know the host? / Have you tried the food? It&rsquo;s great.',
                  'An open, harmless question is the safest way back in.']},
        {'situation': 'Someone asks how old your house is. You are not sure. Buy some time and answer.',
         'tips': ['Well, let me see... about eighty years, I think.',
                  'Well and let me see give you a second to think.']},
        {'situation': 'You are talking about coffee. Move to a new topic that is connected to coffee.',
         'tips': ['Speaking of coffee, have you ever been to Brazil?',
                  'Speaking of + the last topic = a smooth bridge.']},
        {'situation': 'A Dutch friend asks how much you paid for your car. Answer politely without giving the number.',
         'tips': ['Well, more than I wanted to! Actually, that&rsquo;s a long story.',
                  'Humor + a soft change of topic. No need to be offended.']},
        {'situation': 'You have to leave the conversation. Close it politely.',
         'tips': ['Anyway, I should get going. It was really nice talking to you.',
                  'Anyway is the classic signal that the chat is ending.']},
        {'situation': 'Tell me one question that is harmless in Brazil but intrusive somewhere else.',
         'tips': ['In Brazil we ask, are you married? In England, that can feel intrusive.',
                  'This one has no grammar target. Say the true thing.']},
    ],
    'speaking': [
        ('What are three safe topics for small talk with a stranger in Brazil?',
         'Well, food, football and the traffic. Actually, the traffic is the best one &mdash; everybody has a story.'),
        ('Has anybody ever asked you a question that touched a nerve?',
         'Yes. A relative asked why I don&rsquo;t live in the city anymore. I mean, it was not rude, but it was too personal.'),
        ('Do you enjoy small talk, or do you prefer to go straight to a real conversation?',
         'It depends. With a stranger, I like it. It is a way to find common ground before the real conversation.'),
        ('What do you do when there is a lull in a conversation?',
         'I usually ask about food. Speaking of food, it always works with Brazilians.'),
    ],
    'building': [
        ('well / let me see / I / live there / about / ten years',
         'Well, let me see... I have lived there for about ten years.'),
        ('speaking of / travel / you / ever / be / to Portugal?',
         'Speaking of travel, have you ever been to Portugal?'),
        ('by the way / where / you / be / from?',
         'By the way, where are you from?'),
        ('anyway / it / be / nice / talk / to you',
         'Anyway, it was nice talking to you.'),
    ],
    'answerkey_heading': 'Small Talk on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        '<strong>well / let me see</strong> = I need a second to think: Well, let me see... about ten years.',
        '<strong>I mean</strong> = let me explain or correct: It&rsquo;s small. I mean, it&rsquo;s not tiny.',
        '<strong>actually</strong> = a surprise, or a polite &ldquo;no&rdquo;: Actually, I&rsquo;m from the interior.',
        '<strong>by the way</strong> = a new topic, no link: By the way, where are you from?',
        '<strong>speaking of + noun</strong> = a new topic, linked to the last one: Speaking of food...',
        '<strong>anyway</strong> = back to the main topic, or the signal that you are leaving.',
        'One or two of these per sentence is natural. Five in a row sounds nervous.',
        'And the one that is not grammar: weather, food and travel are safe almost everywhere; money, age, '
        'religion and family depend on WHERE you are. When in doubt, ask about the weather.',
    ],
    'rp_chapter_heading': 'Small Talk, <span class="accent">Out Loud</span>',
    'roleplays': [
        {'heading': 'Before the <span class="accent">Class Starts</span>',
         'scenario': 'You are at the pastry class in Lisbon. Mike, from Ohio, arrives early too. Break the ice, '
                     'find one piece of common ground, change the topic once, and close the chat when the chef '
                     'arrives.',
         'chips': ['Well,', 'By the way,', 'Anyway,']},
        {'heading': 'The Auntie <span class="accent">at the Wedding</span>',
         'scenario': 'Now you are at Priya&rsquo;s cousin&rsquo;s wedding in Chennai. Her auntie asks you about '
                     'your age, your family and your salary. Answer warmly, give what you are comfortable with, '
                     'and move the conversation to a safer topic.',
         'chips': ['Actually,', 'I mean,', 'Speaking of']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'You are at a party with people from five different countries. Start a conversation with a '
                     'stranger, keep the ball rolling for two minutes, and leave politely.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'Safe Topics <span class="accent">and Small Words</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Small Talk</span>',
    'survival': [
        'So, what brings you here?',
        'Well, let me think about that.',
        'By the way, where are you from?',
        'Speaking of food, have you tried the local dishes?',
        'Anyway, it was really nice talking to you.',
    ],
    'checklist': [
        'I use well and let me see to buy time.',
        'I use I mean to explain and actually for a surprise.',
        'I change topics with by the way and speaking of.',
        'I go back or close the chat with anyway.',
        'I know which topics are safe and which are off-limits in different cultures.',
    ],
    'badge': {
        'name': 'Ice Breaker',
        'text': 'Tonight you learned what is safe to ask where, Ana &mdash; and the small words that keep a '
                'conversation alive in Utrecht, in Chennai and in Lisbon.',
        'next': 'Telling It Like It Was',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'small talk.&quot; AULA-ANCORA (a cada 5): o ponto nao e so gramatica &mdash; e a ESCALA do que e '
                 'seguro perguntar em cada cultura (clima e comida = seguro; dinheiro, idade, familia = depende de '
                 'ONDE). A gramatica sao os conectores que mantem a conversa viva.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 18: ELA descreve um objeto da casa '
                  'com uma relative clause e uma palavra da aula passada (an heirloom, a flea market, vintage, '
                  'sentimental value, to haggle). Responda de verdade. PONTE (REGRA 27B): &quot;Nice story. And '
                  'when you meet a stranger, what is the first thing you say?&quot; ZERO correcao. Anote se ela usa '
                  'algum filler em portugues (tipo, entao, ne) &mdash; volta no capitulo 3.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos e leia a nota. So plante as duas '
                   'pecas: o TOPICO certo e as PALAVRINHAS que ligam. A tabela vem no capitulo 3.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela contar uma pergunta que nunca faria e uma que '
                'um estrangeiro fez e a surpreendeu. Pergunte: &quot;Was it rude, or just different?&quot; Anote a '
                'resposta &mdash; ela volta nos listenings.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for small talk. Three of '
                       'them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> CCQ small talk: &quot;Is it a serious conversation? '
                  '(Nao.)&quot; CCQ off-limits: &quot;Can you talk about it? (Melhor nao.)&quot; CCQ intrusive x '
                  'harmless: &quot;Asking about the weather &mdash; intrusive or harmless? (Harmless.)&quot; CCQ to '
                  'pry: &quot;Is it about public or private life? (Privada.)&quot; Peca um exemplo do Brasil em cada '
                  'card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ rapport: &quot;Is it a feeling or a topic? '
                  '(Sentimento.)&quot; CCQ a lull: &quot;Is anybody talking? (Nao.) Is it long? (Nao, curto.)&quot; '
                  'CCQ to break the ice: &quot;At the start or at the end? (No inicio.)&quot; CCQ to touch a nerve: '
                  '&quot;Is the person happy after? (Nao, chateada.)&quot; Rapport: o t final NAO soa.',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'harmless e intrusive sao as duas pontas da escala da aula.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> ra-POR (o t final e mudo, forca no POR), in-TRU-siv '
                '(forca no TRU, u longo), off-LIM-its (forca no LIM). Na frase: &quot;by the way&quot; sai quase '
                'uma palavra so, /bai-dhe-WEI/. 2 repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas '
                   'estao no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. Small words, big '
                     'jobs.&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases (toque o audio). Pergunte: '
                   '&quot;Which word gives you time to think? Which one opens a new topic? Which new topic is '
                   'connected to the last one? Which one goes back?&quot; Nao e regra de forma, e de FUNCAO. So entao '
                   '&quot;Reveal the Rule&quot;. CCQs: &quot;By the way, do you like football? &mdash; was football '
                   'the topic before? (Nao.)&quot; &quot;Speaking of coffee... &mdash; was coffee the topic before? '
                   '(Sim.)&quot; &quot;Anyway, nice talking to you &mdash; is the chat starting or ending? '
                   '(Terminando.)&quot; Volte aos fillers em portugues anotados no warm-up: qual e o equivalente?',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a palavra ORALMENTE antes de clicar. Itens 3 e 4 sao '
                    'o par central: by the way (sem ligacao) x speaking of (com ligacao).',
        'ch4_trans': '<strong>Transicao Many Englishes (1 min):</strong> Diga: &quot;A Dutchman, an Indian and an '
                     'American on small talk.&quot; Avise os sotaques: holandes (g aspirado no fundo da garganta, '
                     'r forte, ritmo seco) e indiano (r batido, ritmo silabico, t e d retroflexos). O americano e o '
                     'do dialogo.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Mike, americano de Ohio, numa aula de culinaria em '
                    'Lisboa. Clique &quot;Next Line&quot; e toque o audio. Nas falas da Ana, peca que ELA fale '
                    'primeiro. PRAGMATICA: as perguntas do Mike sao todas seguras (de onde, o que traz voce aqui, '
                    'comida) &mdash; nenhuma sobre familia ou dinheiro. Conte com ela os conectores do dialogo: '
                    'well, I mean, by the way, speaking of, anyway.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o MIKE, nunca sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque HOLANDES: g raspado na garganta, r forte, frases '
                      'curtas e diretas. Toque 2 vezes. No fim: &quot;In Brazil, is how are you a real question or '
                      'just hello?&quot;',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'INDIANO: ritmo silabico (cada silaba com o mesmo peso), r batido, t e d com a lingua para tras. '
                      'Toque 2 vezes. Pergunte: &quot;Is the Brazilian auntie closer to Chennai or to London?&quot; '
                      'Volte a resposta anotada no hook.',
        'artifact': '<strong>Artefato (5 min):</strong> O cartao da aula de culinaria em Lisboa, em nome dela. Peca '
                    'que leia cada linha. Depois as 3 tarefas &mdash; ela responde ANTES de revelar e usa pelo menos '
                    'um conector em cada resposta.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick answers, '
                     'and your own small talk.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 3 primeiros sao de lingua '
                     '(conectores empilhados, &quot;by the way of&quot; no lugar de speaking of, actually repetido). '
                     'O 4o NAO e erro de lingua: a frase esta certa, mas perguntar salario a um americano que voce '
                     'acabou de conhecer e um tema off-limits. Discuta: no Brasil, seria?',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 4a e a mais dificil: recusar uma pergunta sem ofender.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija pelo '
                    'menos tres conectores diferentes por resposta. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica para '
                    'comparar. Item 1: present perfect com for (callback da aula 3). Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so no fim, para conferir. A linha 7 e o alerta de '
                     'excesso; a linha 8 e a escala de seguranca dos temas &mdash; vale uma pergunta sobre o Brasil.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Small talk, '
                     'three times.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o Mike. Responda com naturalidade e deixe ELA '
               'conduzir: quebrar o gelo, achar algo em comum, mudar de assunto uma vez e fechar com anyway. Corrija '
               'SO o uso dos conectores.',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e a tia da Priya: calorosa e MUITO direta (idade, '
               'marido, salario). Ela responde com simpatia, da so o que quiser e desvia com speaking of / actually '
               '(callback da aula 14: tactful, to hedge). Se travar, ensine &quot;Actually, that is a long story! '
               'Speaking of stories...&quot;.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. Faca perguntas de verdade para '
               'manter a conversa. NAO corrija durante. Conte quantos conectores diferentes ela usa e diga o numero '
               'no fim. Anote excesso de &quot;actually&quot; para o feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Abrir, ganhar '
                    'tempo, mudar de assunto, ligar e fechar: uma conversa inteira em cinco frases.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Now you can start a conversation anywhere &mdash; '
                 'and know what not to ask.&quot; Homework (oralmente, opcional): na proxima vez que conversar com um '
                 'desconhecido (em portugues mesmo), perceber quais temas apareceram e trazer um exemplo; e um audio '
                 'de um minuto de small talk imaginario com 4 conectores diferentes. Proxima aula: Telling It Like It '
                 'Was &mdash; reported speech, recontar o que alguem disse.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'Small Talk -- What\'s Safe to Ask Where',
        'desc': 'A Dutchman, an Indian auntie and an American in Lisbon: the small words that keep a conversation going, and the topics that are safe in each culture.',
        'context_paras': [
            'Pieter, from Utrecht, thinks <strong>small talk</strong> is a little strange. At a Dutch party he '
            'might ask how much you paid for your house. For him, it is a <strong>harmless</strong> question. '
            '<em><strong>Well</strong>, we are just curious</em>, he says. <em><strong>I mean</strong>, why not '
            'ask?</em>',
            'Priya grew up in Chennai, where an auntie at a wedding asks about your salary. In London, she learned '
            'that money is <strong>off-limits</strong>. <strong>Actually</strong>, she now loves British small '
            'talk: the weather is <strong>common ground</strong>, and nobody gets hurt.',
            'In a cooking class in Lisbon, Ana meets Mike from Ohio. They <strong>break the ice</strong> with the '
            'custard tarts. <em><strong>By the way</strong>, have you done a class like this before?</em> she asks. '
            '<em><strong>Speaking of</strong> food...</em>, he answers. When the chef arrives, Mike says, '
            '<em><strong>Anyway</strong>, I think we are starting.</em>',
        ],
        'context_quiz': [
            ('Why does Pieter ask about the price of a house?',
             [('Because in the Netherlands he thinks it is a harmless, curious question.', True),
              ('Because he wants to buy the house himself.', False),
              ('Because he does not like small talk about the weather and wants to be rude.', False)]),
            ('What did Priya learn in London?',
             [('That the British never talk about the weather at all.', False),
              ('That money is off-limits, and the weather is common ground.', True),
              ('That aunties ask about salaries.', False)]),
            ('What does Mike&rsquo;s &ldquo;Anyway, I think we are starting&rdquo; mean?',
             [('He wants to change the topic to the chef&rsquo;s life story.', False),
              ('He did not understand Ana.', False),
              ('The small talk is ending.', True)]),
        ],
        'tip_title': 'Small Words, Big Jobs',
        'tip_sub': 'Buy time, explain, surprise, change topic, link, close &mdash; six different jobs.',
        'tip_rows': [
            ('well / let me see', 'Buy time to think', '<strong>Well</strong>, let me see... ten years.'),
            ('I mean', 'Explain or correct', 'It&rsquo;s small. <strong>I mean</strong>, not tiny.'),
            ('actually', 'A surprise, or a polite no', '<strong>Actually</strong>, I&rsquo;m from the interior.'),
            ('by the way', 'A new topic, no link', '<strong>By the way</strong>, where are you from?'),
            ('speaking of + noun', 'A new topic, linked to the last one', '<strong>Speaking of</strong> food...'),
            ('anyway', 'Back to the topic, or goodbye', '<strong>Anyway</strong>, nice talking to you.'),
        ],
        'tip_never': 'By the way of food &middot; speaking about of &middot; five connectors in one sentence. '
                     'Speaking of is followed by a noun. One or two small words per sentence sounds natural; more '
                     'sounds nervous. And remember: weather and food are safe almost everywhere, money and age are not.',
        'fills': [
            ('', 'Well', ', let me see... I think about ten years.',
             'one word -- you need a second to think'),
            ('It\'s a small town. I ', 'mean', ', it\'s not tiny, but it\'s quiet.',
             'one word -- you explain what you just said'),
            ('By the ', 'way', ', where are you from?',
             'one word -- a new topic with no link'),
            ('Speaking ', 'of', ' food, have you tried the custard tarts?',
             'one small word -- a new topic linked to the last one'),
            ('', 'Anyway', ', it was really nice talking to you.',
             'one word -- the chat is ending'),
            ('In many countries, money is ', 'off-limits', ' when you meet someone new.',
             'one word with a hyphen -- a topic you should not talk about'),
        ],
        'order_intro': 'Ana meets Mike before a cooking class in Lisbon. Put the conversation in order.',
        'order': [
            'Hi! Is this the pastry class? I think I\'m a little early.',
            'Me too. Well, at least we get the best seats. I\'m Ana, from Brazil.',
            'Mike, from Ohio. So, what brings you to Lisbon?',
            'A short vacation. By the way, have you done a class like this before?',
            'Never. Speaking of food, have you tried the custard tarts yet?',
            'Three times! Anyway, I think the chef is here.',
        ],
        'quiz': [
            ('You are talking about coffee and want to ask about Brazil, which is connected. You say:',
             [('"By the way of coffee, have you been to Brazil?"', False),
              ('"Speaking of coffee, have you ever been to Brazil?"', True),
              ('"Anyway, coffee is something I drink every single morning before work."', False)]),
            ('Someone asks how long you have lived in your town. You need a second. You say:',
             [('"Well, let me see... about fifteen years."', True),
              ('"Anyway, fifteen years."', False),
              ('"By the way, fifteen years."', False)]),
            ('You meet an American at a party. Which question is the safest small talk?',
             [('"How much do you earn in a normal month at your job?"', False),
              ('"Why don\'t you have children?"', False),
              ('"So, how do you know the host?"', True)]),
            ('There is a short silence in the conversation. It is:',
             [('a lull', True),
              ('rapport, the friendly feeling between two people', False),
              ('common ground', False)]),
        ],
        'think': 'Imagine you are at a party abroad and you meet someone new. Record two minutes of small talk: '
                 'break the ice, ask two safe questions, change the topic once with by the way or speaking of, '
                 'and close politely with anyway. Use at least one of tonight&rsquo;s expressions.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Film',
         'title': 'Lost in Translation (2003) &mdash; official trailer',
         'desc': 'Two Americans meet in a hotel bar in Tokyo. Everything starts with small talk &mdash; and with a '
                 'lot of cultural moments where nobody is sure what the other person really means.',
         'tip': 'watch the trailer twice and write down every small-talk question you hear. Are they safe in Brazil?',
         'url': 'https://www.youtube.com/watch?v=W6iVPCRflQM', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; Relationships 2.0: The Power of Tiny Interactions',
         'desc': 'A psychologist explains why short conversations with strangers make us happier, and how to start, '
                 'keep and end them.',
         'tip': 'listen for well, I mean, actually and anyway. How many times do the speakers use each one?',
         'url': 'https://hiddenbrain.org/podcast/relationships-2-0-the-power-of-tiny-interactions/',
         'cta': 'Listen on Hidden Brain'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'Why you should talk to strangers &mdash; Kio Stark, TED',
         'desc': 'A short talk about the small moments with people we do not know &mdash; and why they matter more '
                 'than we think.',
         'tip': 'turn on English subtitles and notice how she opens and closes each story.',
         'url': 'https://www.ted.com/talks/kio_stark_why_you_should_talk_to_strangers', 'cta': 'Watch on TED'},
    ],
}
