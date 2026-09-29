# -*- coding: utf-8 -*-
"""Aula 14 -- Asking Nicely, and Who You Are Asking (ANCORA intercultural).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
Sotaques (CURRICULO V3, linha 14 do hub): noruegues (listening 1), britanico (listening 2),
americano (dialogo).
Ancora (a cada 5): o ponto nao e so gramatica -- e a ESCALA de diretividade. O Discovery
descobre um escalonamento (direta -> indireta -> muito indireta) e a ordem das palavras
que muda junto. O Spot the Error inclui um erro que NAO e de lingua (pedido cru para um
britanico).
Callback da aula 13: second conditional + far-fetched, feasible, off the grid, a long shot...
"""

LESSON = {
    'n': 14,
    'model': 'reading',
    'menu_title': 'Asking Nicely -- and Who You Are Asking',
    'menu_desc': 'The same question is perfectly normal in Oslo and a little rude in London. Tonight, indirect '
                 'questions, and how to choose the right amount of politeness for the person in front of you',
    'grammar_point': 'indirect and polite questions on a directness scale',
    'chapter_tag': 'Intercultural Anchor',
    'title_html': 'Asking Nicely &mdash; and <span class="accent">Who You Are Asking</span>',
    'title_sub': 'A Norwegian, a British woman and an American ask for the same thing. Only the words around the question change.',
    'phases': ['First Words', 'The Words of Your World', 'The Story', 'The Code',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, a Life That <span class="accent">Is Not True</span>',
        'callback': 'One sentence with if + past and two words from last week: far-fetched, feasible, remote, '
                    'off the grid, a long shot, wishful thinking, to weigh something up.',
        'question': 'Then: when you need a favor from somebody you do not know well, how do you ask?',
    },
    'framing': {
        'heading': 'One Question, <span class="accent">Three Countries</span>',
        'steps': [('The Words', 'blunt, tactful, pushy, to beat around the bush...'),
                  ('The Story', 'a text about politeness in Oslo, London and New York'),
                  ('The Code', 'indirect questions and the word order that changes')],
        'note': '<strong>Where is the station?</strong> In Oslo that is a perfectly polite question. In London it '
                'can sound a little cold. The grammar of polite questions is not only about being nice: it is about '
                'choosing how much politeness THIS person expects.',
    },
    'hook': {
        'label': 'One Ordinary Favor',
        'heading': 'How Would You <span class="accent">Ask?</span>',
        'line1': 'You are staying in a small guesthouse. You need to use the kitchen after ten at night, and the '
                 'rules say it closes at nine.',
        'line2': 'What exactly do you say to the owner? Now imagine the owner is Norwegian. Then British. Does '
                 'your question change?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">How Direct You Are</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'Blunt', 'icon': 'alert',
         'def': 'Saying exactly what you think, without trying to be gentle',
         'ex': 'He is not rude, he is just blunt. He says what he thinks.',
         'match': 'saying exactly what you think, without being gentle'},
        {'word': 'Tactful', 'icon': 'heart',
         'def': 'Careful not to upset people when you say something difficult',
         'ex': 'She found a tactful way to say that the soup was too salty.',
         'match': 'careful not to upset people when you say something difficult'},
        {'word': 'Straightforward', 'icon': 'compass',
         'def': 'Honest and clear, with no hidden meaning',
         'ex': 'Norwegians are very straightforward. A question is just a question.',
         'match': 'honest and clear, with no hidden meaning'},
        {'word': 'Courteous', 'icon': 'users',
         'def': 'Polite and respectful, especially to people you do not know',
         'ex': 'The owner was courteous, even when we arrived two hours late.',
         'match': 'polite and respectful, especially to strangers'},
        {'word': 'Pushy', 'icon': 'bolt',
         'def': 'Trying too hard to make somebody do what you want',
         'ex': 'I did not want to sound pushy, so I asked only once.',
         'match': 'trying too hard to make somebody do what you want'},
        {'word': 'Awkward', 'icon': 'help',
         'def': 'Uncomfortable, and not sure what to say or do',
         'ex': 'There was an awkward silence after my question.',
         'match': 'uncomfortable, and not sure what to say or do'},
        {'word': 'To come across as', 'icon': 'eye',
         'def': 'To give other people a certain impression',
         'ex': 'Without please, a short question can come across as rude.',
         'match': 'to give other people a certain impression'},
        {'word': 'To impose on somebody', 'icon': 'lock',
         'def': 'To ask somebody for something that gives them extra work or trouble',
         'ex': 'I do not want to impose on you, but could I stay one more night?',
         'match': 'to give somebody extra work or trouble with a request'},
        {'word': 'To hedge', 'icon': 'shield',
         'def': 'To avoid a clear, direct answer or request, often to be polite',
         'ex': 'The British often hedge: I was just wondering if maybe...',
         'match': 'to avoid being clear and direct, often to be polite'},
        {'word': 'To beat around the bush', 'icon': 'leaf', 'expr': True,
         'def': 'To talk about other things and avoid the main point',
         'ex': 'Stop beating around the bush and tell me what you need.',
         'match': 'to talk about other things and avoid the main point'},
        {'word': 'To get to the point', 'icon': 'target', 'expr': True,
         'def': 'To start talking about the most important thing',
         'ex': 'In Oslo, people get to the point in the first sentence.',
         'match': 'to start talking about the most important thing'},
        {'word': 'To walk on eggshells', 'icon': 'alert', 'expr': True,
         'def': 'To be extremely careful about what you say, so you do not upset somebody',
         'ex': 'I felt I was walking on eggshells with my new landlady.',
         'match': 'to be very careful not to upset somebody'},
    ],
    'vocabnote': 'Look at how many of these words describe the SAME behavior from different sides: '
                 '<strong>blunt</strong> and <strong>straightforward</strong> can describe the same sentence. Which '
                 'word you choose depends on whether you liked it. The same is true of <strong>tactful</strong> and '
                 '<strong>beating around the bush</strong>.',
    'pron': [
        'Courteous',
        'Straightforward',
        'Awkward',
        'Could you tell me where the station is?',
    ],
    'gapfill': [
        ('"He is not rude, he is just ', 'blunt', '. He says what he thinks."'),
        ('"She found a ', 'tactful', ' way to say that the soup was too salty."'),
        ('"There was an ', 'awkward', ' silence after my question."'),
        ('"I did not want to sound ', 'pushy', ', so I asked only once."'),
        ('"The owner was ', 'courteous', ', even when we arrived two hours late."'),
        ('"A question in Oslo is just a question. People there are very ', 'straightforward', '."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Story)
    'ch3': {
        'heading': 'How Much Politeness <span class="accent">Is Too Much?</span>',
        'sub': 'A short text, then a Norwegian and a British woman tell their side',
    },
    'reading': {
        'heading': 'The Same Favor, <span class="accent">Three Ways</span>',
        'rtitle': 'How Much Politeness Is Too Much?',
        'paras': [
            'Imagine you need directions in a new city. In Oslo, <em>Where is the station?</em> is a perfectly '
            'normal question. Norwegians are famously <strong>straightforward</strong>: they get to the point, and '
            'a long, careful question can even sound strange to them, as if you were hiding something.',
            'Ask the same thing in London and it may come across as a little <strong>blunt</strong>. A British '
            'speaker is more likely to say <em>Sorry, could you tell me where the station is?</em> or even <em>I was '
            'just wondering if you knew where the station was</em>. The British tend to hedge, especially when they '
            'feel they are imposing on somebody.',
            'Americans usually sit somewhere in the middle. They are friendly and quick: <em>Hi! Do you know where '
            'the station is?</em> is courteous enough almost everywhere in the United States. Too much hedging can '
            'even sound awkward, as if the question were a bigger favor than it is.',
            'Notice what happens to the grammar as the question becomes more polite. <strong>Where is the '
            'station?</strong> becomes <strong>Could you tell me where the station is?</strong> The question '
            'moves to the front, and the second half goes back to the normal order of a statement. So the polite '
            'version is not only longer. It is built differently. And the skill at this level is not knowing one '
            'polite form, but choosing the right one for the person in front of you.',
        ],
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist_choices': [
            ('Why the British are more polite than Norwegians', False),
            ('How to find the station in three European cities', False),
            ('The right amount of politeness depends on who you ask, and polite questions have their own word order', True),
        ],
        'tf': [
            ('In Oslo, Where is the station? sounds rude.', 'f',
             'The text says it is a perfectly normal question there. Norwegians are straightforward.'),
            ('A British speaker often adds words like sorry or I was just wondering.', 't',
             'The British tend to hedge, especially when they feel they are imposing.'),
            ('Americans usually hedge more than the British.', 'f',
             'They sit in the middle. Too much hedging can even sound awkward in the United States.'),
            ('In a polite question, the second half has the word order of a statement.', 't',
             'Could you tell me where the station IS &mdash; not where is the station.'),
            ('The text says there is one correct polite form for every situation.', 'f',
             'The skill is choosing the right form for the person in front of you.'),
        ],
    },
    'listenings': [
        {
            'file': 'a14_listening_eirik.mp3',
            'voice': 'nordic_m',
            'label': 'Listening 1 &middot; Norway',
            'title': 'The Question <span class="accent">Nobody Asked</span>',
            'blurb': 'A Norwegian on his first month in England. Sound first &mdash; no text.',
            'text': 'My name is Eirik, and I am from Bergen, on the west coast of Norway. When I moved to '
                    'Manchester for my master\'s degree, I shared a house with an English guy called Tom. In '
                    'my second week, he said to me, I was just wondering if you might possibly be able to do the '
                    'dishes at some point. I said, no thank you, I am busy tonight. For me, that was an honest '
                    'answer to a question. He was asking if I was able to, and I was not. Tom did not speak to me '
                    'for two days. Later a friend explained that it was not a question at all. It was a request, '
                    'and quite an urgent one. In Norway we would just say, can you do the dishes, and nobody would '
                    'find that rude. Now I have learned to listen for the words wondering and possibly. When I hear '
                    'them, I know that something important is coming.',
            'qs': [
                ('Where is Eirik from, and where did he move?',
                 'He is from Bergen, in Norway, and he moved to Manchester for his master&rsquo;s degree.'),
                ('How did Eirik answer Tom&rsquo;s question about the dishes?',
                 'He said no thank you, he was busy that night.'),
                ('What does Eirik do now when he hears wondering and possibly?',
                 'He knows that something important is coming: it is a request, not a real question.'),
            ],
        },
        {
            'file': 'a14_listening_harriet.mp3',
            'voice': 'british_f',
            'label': 'Listening 2 &middot; United Kingdom',
            'title': 'Give Me <span class="accent">a Coffee</span>',
            'blurb': 'A British woman on her first morning in Oslo. Sound first &mdash; no text.',
            'text': 'I am Harriet, I am from Leeds, and three years ago I moved to Oslo with my husband. On my '
                    'first morning I went to a small café near our flat. The man in front of me said, one coffee, '
                    'black. No please, no thank you, no smile. I was quite shocked, to be honest. I thought, how '
                    'rude. Then the woman behind the counter smiled at him and said, of course, and they chatted '
                    'about the weather for a minute. Nobody was offended except me. When it was my turn, I said, '
                    'hello, sorry, I was wondering if I could possibly have a coffee, if it is not too much '
                    'trouble. She looked at me as if I had asked for something very complicated. Now, three years '
                    'later, I order my coffee in five words. But when I go home to Leeds, I have to remember to put '
                    'all the sorries back in.',
            'qs': [
                ('What did the man in front of Harriet say, and how did she feel?',
                 'He said one coffee, black, with no please or thank you. She was quite shocked and thought it was rude.'),
                ('How did the woman behind the counter react to him?',
                 'She smiled, said of course, and they chatted about the weather.'),
                ('What does Harriet have to remember when she goes home to Leeds?',
                 'To put all the sorries back in.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4 (The Code)
    'ch4': {
        'heading': 'The Question <span class="accent">Moves to the Front</span>',
        'sub': 'direct &middot; polite &middot; very polite &mdash; and the word order that changes',
    },
    'grammar': {
        'heading': 'From Direct to <span class="accent">Very Polite</span>',
        'examples': [
            'Where <span style="color:#c2410c;font-weight:700">is the station</span>?',
            'Could you tell me where <span style="color:#1d4ed8;font-weight:700">the station is</span>?',
            'Do you happen to know if <span style="color:#7c3aed;font-weight:700">the kitchen closes</span> at nine?',
            'I was wondering if <span style="color:#15803d;font-weight:700">you could</span> help me with my bags.',
        ],
        'prompt': 'These four questions go from the most direct to the most polite. Look at the colored words. '
                  'In the first one, the verb comes BEFORE the subject. What happens to the order in the other three? '
                  'And where did the word do go?',
        'rule_rows': [
            ('direct question', 'Verb before the subject. Fine with friends, and in Norway.',
             'Where <strong>is the station</strong>?'),
            ('Could you tell me + wh-word', 'Polite. The second half has statement order.',
             'Could you tell me where <strong>the station is</strong>?'),
            ('Do you know + if / whether', 'For yes/no questions. No do in the second half.',
             'Do you know <strong>if the kitchen closes</strong> at nine?'),
            ('Would you mind + -ing', 'A polite request. The answer no means yes, I will.',
             'Would you mind <strong>opening</strong> the window?'),
            ('I was wondering if + could', 'Very polite, typical in the UK. Past forms make it softer.',
             'I was wondering <strong>if you could</strong> help me.'),
            ('choose the level', 'The more you impose, and the more British the listener, the higher you go.',
             'a coffee in Oslo &ne; a favor in London'),
        ],
        'oneliner': 'the polite part goes to the front, and the question itself goes back to normal order.',
    },
    'practice_heading': 'Make It <span class="accent">Polite</span>',
    'practice_fill': [
        ('"Could you tell me where the station ', 'is', '?" (be &mdash; statement order at the end)'),
        ('"Do you know ', 'if', ' the kitchen closes at nine?" (a yes/no question inside)'),
        ('"Do you know what time the shop ', 'opens', '?" (open &mdash; no does in the second half)'),
        ('"Would you mind ', 'opening', ' the window?" (open &mdash; the form after mind)'),
        ('"I was wondering if you ', 'could', ' help me with my bags." (can &mdash; softer in the past)'),
        ('"Can you tell me how much this ', 'costs', '?" (cost &mdash; statement order)'),
    ],
    'dialogue': {
        'heading': 'Is It Okay <span class="accent">to Ask?</span>',
        'guest_name': 'Josh',
        'guest_key': 'josh',
        'guest_voice': 'arthur',
        'lines': [
            ('josh', 'Hi, Ana! Welcome to Vermont. Did you find the cabin okay?'),
            ('ana', 'Yes, thank you. Sorry to <span class="vocab-highlight">impose on</span> you, but could you tell me where the nearest supermarket is?'),
            ('josh', 'Sure, no problem! It is about ten minutes down the road. You are not imposing at all.'),
            ('ana', 'Great. And do you know if it is open on Sundays?'),
            ('josh', 'It opens at eight on Sundays. Anything else? Just ask. You do not need to <span class="vocab-highlight">beat around the bush</span> with me.'),
            ('ana', 'Okay, then I will <span class="vocab-highlight">get to the point</span>. Would you mind lending me a heater? The cabin is cold at night.'),
            ('josh', 'Not at all. I will bring one over in an hour. Americans love a <span class="vocab-highlight">straightforward</span> question.'),
            ('ana', 'Good to know. In Brazil I would ask about your family first!'),
        ],
        'comp': [
            ('How far is the supermarket, according to Josh?',
             'About ten minutes down the road.'),
            ('What time does the supermarket open on Sundays?',
             'At eight.'),
            ('What does Josh say about straightforward questions?',
             'That Americans love a straightforward question &mdash; she does not need to beat around the bush.'),
        ],
    },
    'artifact': {
        'heading': 'Three Messages, <span class="accent">One Request</span>',
        'title': 'MESSAGES TO ANA CLAUDIA VERALDI &mdash; GUESTHOUSE HOSTS',
        'subtitle': 'The same request: please do not use the kitchen after 10 p.m.',
        'corner': 'Norway &middot; UK<br>USA',
        'label_width': '110px',
        'rows': [
            ('Ingrid, Oslo', 'Kitchen closes at 10. Thanks.'),
            ('Margaret, York', 'So sorry to bother you! I was just wondering if you would mind not using the kitchen after ten, if that is okay? Thanks so much!'),
            ('Kayla, Denver', 'Hey Ana! Quick thing: could you please keep the kitchen use before 10 p.m.? Thanks!'),
        ],
        'comp': [
            ('Put the three messages in order, from the most direct to the most polite.',
             'Ingrid (Oslo), then Kayla (Denver), then Margaret (York).'),
            ('Is Ingrid being rude? Explain in one sentence.',
             '"No, she is being straightforward. In Norway a short message is perfectly courteous."'),
            ('Rewrite Ingrid&rsquo;s message the way Margaret would write it.',
             '"I was wondering if you could possibly finish in the kitchen by ten. Thank you so much!"'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('Could you tell me where is the station?', 'Could you tell me where the station is?'),
        ('Do you know what time does the shop open?', 'Do you know what time the shop opens?'),
        ('I was wondering if could you help me.', 'I was wondering if you could help me.'),
        ('Would you mind to open the window?', 'Would you mind opening the window?'),
        ('To your British landlady: Give me the key.', 'To your British landlady: Could I possibly have the key, please?'),
    ],
    'quickfire': [
        {'situation': 'You are in London and you need to find a pharmacy. Ask a stranger.',
         'tips': ['Sorry, could you tell me where the nearest pharmacy is?',
                  'Sorry + could you tell me + statement order.']},
        {'situation': 'In Oslo, you want to know the price of a sandwich. Ask the Norwegian way.',
         'tips': ['How much is this sandwich?',
                  'Direct is fine in Norway. Too much hedging sounds strange.']},
        {'situation': 'You want to know if the museum is open on Mondays. Ask politely.',
         'tips': ['Do you know if the museum is open on Mondays?',
                  'A yes/no question inside: if or whether.']},
        {'situation': 'You need your British host to turn down the music. Ask without sounding pushy.',
         'tips': ['I was wondering if you could turn the music down a little.',
                  'I was wondering if + could: very polite, very British.']},
        {'situation': 'On a train, ask the person next to you to move their bag.',
         'tips': ['Would you mind moving your bag, please?',
                  'Would you mind + -ing. If the answer is no, it means yes.']},
        {'situation': 'An American friend says: just ask, do not beat around the bush. Ask for a ride to the airport.',
         'tips': ['Could you give me a ride to the airport on Friday?',
                  'Could you is enough. No need for I was wondering here.']},
    ],
    'speaking': [
        ('How do you ask a neighbor for a favor in Brazil?',
         'In Brazil I would chat a little first, and then say: I was wondering if you could water my plants this weekend.'),
        ('Do you prefer people who are blunt or tactful? Why?',
         'I prefer tactful people, but in some situations a straightforward answer saves a lot of time.'),
        ('Tell me about a time a question came across the wrong way.',
         'Once I asked a colleague a very short question and it came across as rude. I did not mean it that way.'),
        ('Ask me something about my weekend, very politely.',
         'Do you mind if I ask what you did this weekend?'),
    ],
    'building': [
        ('could / you / tell me / where / the bus stop / be (polite)',
         'Could you tell me where the bus stop is?'),
        ('do / you / know / if / the bakery / open / on Sundays (polite, yes/no)',
         'Do you know if the bakery opens on Sundays?'),
        ('would / you / mind / close / the door (a request)',
         'Would you mind closing the door?'),
        ('I / wonder / if / you / can / help me / with this form (very polite, British)',
         'I was wondering if you could help me with this form.'),
    ],
    'answerkey_heading': 'The Politeness Scale in <span class="accent">Eight Lines</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        'Direct: <strong>Where is</strong> the station? Verb before subject. Normal in Norway and with friends.',
        'Polite: Could you tell me where <strong>the station is</strong>? The second half has statement order.',
        'No do in the second half: Do you know what time the shop <strong>opens</strong>? &middot; never what time does the shop open.',
        'Yes/no inside: Do you know <strong>if</strong> / <strong>whether</strong> the kitchen closes at nine?',
        'Would you mind <strong>+ -ing</strong>: Would you mind opening the window? No means yes, I will.',
        'Very polite: I was wondering if you <strong>could</strong>... The past makes it softer.',
        'The more you impose, the more polite you go. A coffee is not a favor.',
        'And the one that is not grammar: Norway is direct, the UK hedges, the US is in the middle. Choose the level for the listener, not for yourself.',
    ],
    'rp_chapter_heading': 'Three People, <span class="accent">Three Levels</span>',
    'roleplays': [
        {'heading': 'The British Landlady',
         'scenario': 'You are renting a room from Margaret, in York. She is kind but very British. Ask her three '
                     'things: if you can use the washing machine, where the nearest bus stop is, and if a friend can '
                     'visit on Saturday. Do not sound pushy.',
         'chips': ['I was wondering if', 'Could you tell me where', 'Would you mind if']},
        {'heading': 'The Norwegian <span class="accent">Neighbor</span>',
         'scenario': 'Now you are in a cabin near Bergen. Your Norwegian neighbor, Eirik, is straightforward. You '
                     'need firewood, the Wi-Fi password and a ride to the station tomorrow. Get to the point &mdash; '
                     'and notice how different it feels.',
         'chips': ['Can you', 'Do you know if', 'straightforward']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'Tell me about a situation where you had to ask a stranger for help, in Brazil or abroad. What '
                     'did you say? How did it come across? Then ask me two polite questions about a trip I took.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'The Right Question for <span class="accent">the Right Person</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Asking Nicely</span>',
    'survival': [
        'Could you tell me where the station is?',
        'Do you know if the kitchen closes at nine?',
        'Would you mind opening the window?',
        'I was wondering if you could help me with my bags.',
        'Sorry to impose on you, but could I ask a small favor?',
    ],
    'checklist': [
        'I put indirect questions in statement order: could you tell me where the station is.',
        'I do not use do or does in the second half of an indirect question.',
        'I use would you mind + -ing and I was wondering if + could.',
        'I choose how polite to be for the person in front of me: Norway, the UK or the US.',
        'I know the words: blunt, tactful, straightforward, pushy, to hedge, to beat around the bush, to get to the point.',
    ],
    'badge': {
        'name': 'Many Voices',
        'text': 'You asked the same favor three ways, Ana &mdash; and chose the right one for a Norwegian, a British '
                'woman and an American.',
        'next': 'Looking Back',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). AULA ANCORA intercultural '
                 '(a cada 5). Va direto: &quot;Tonight, the same question in three countries.&quot; O ponto nao e so '
                 'a gramatica das perguntas indiretas: e ESCOLHER o nivel de polidez para quem esta na frente. Ela '
                 'ja viveu isso na pele com colegas de varios paises &mdash; puxe essa experiencia, sem virar aula '
                 'de trabalho.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 13: UMA frase com if + passado e '
                  'duas palavras da lista (far-fetched, feasible, remote, off the grid, a long shot, wishful '
                  'thinking, to weigh something up). PONTE (REGRA 27B): &quot;Last week, a life that is not true. '
                  'Tonight, a very real problem: asking a stranger for help.&quot; Depois a pergunta do slide, livre. '
                  'Anote se ela diz &quot;could you tell me where is...&quot; &mdash; e o diagnostico de hoje.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. Plante a tese sem dar regra: a mesma '
                   'pergunta e normal em Oslo e um pouco fria em Londres. E a pergunta educada e CONSTRUIDA diferente, '
                   'nao so mais longa.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela formular o pedido para o dono da pousada. NAO '
                'corrija. Anote a frase exata. Depois pergunte se mudaria para um noruegues e para uma britanica. '
                'A frase anotada volta corrigida no capitulo 4.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for how direct people '
                       'are. Three of them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ blunt x '
                  'straightforward: &quot;Same behavior &mdash; which one is a compliment? (Straightforward.)&quot; '
                  'CCQ tactful: &quot;Does a tactful person say the difficult thing? (Sim, mas com cuidado.)&quot; '
                  'CCQ pushy: &quot;Is asking three times pushy? (Provavelmente.)&quot; Peca um exemplo da vida dela.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ to impose on somebody: &quot;Does it give the '
                  'other person extra work? (Sim.)&quot; CCQ to hedge: &quot;Is the request clear? (Nao, e '
                  'amaciada.)&quot; CCQ beat around the bush x get to the point: opostos. To walk on eggshells: '
                  '&quot;Are you relaxed? (Nao, com muito cuidado.)&quot;',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'blunt e straightforward podem descrever a MESMA frase &mdash; muda o julgamento.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> COUR-te-ous (/KUR-ti-us/, nunca /cou-RE-ous/), '
                'straight-FOR-ward (forca no FOR), AWK-ward (/OK-werd/, o w do meio some). Na frase inteira, a '
                'entonacao DESCE no fim de &quot;Could you tell me where the station is?&quot; de forma suave. 2 '
                'repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas estao '
                   'no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao leitura (1 min):</strong> Diga: &quot;A short text about politeness in three '
                     'cities, and then two people who lived it.&quot;',
        'reading': '<strong>Leitura + gist (6 min):</strong> Primeira leitura RAPIDA (90 segundos) so para a ideia '
                   'central, depois o gist. Segunda leitura com calma. Pergunte: &quot;Which city is closest to '
                   'Brazil?&quot; Nao ha resposta certa &mdash; puxe a experiencia dela.',
        'tf': '<strong>True or False (4 min):</strong> Ana decide e JUSTIFICA com o texto antes de revelar. A 4a e a '
              'regra gramatical escondida no texto &mdash; destaque, mas NAO explique ainda (o capitulo 4 faz isso).',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque NORUEGUES: entonacao que sobe e desce dentro da frase '
                      '(&quot;cantada&quot;), consoantes claras, o r um pouco vibrado. Toque 2 vezes. No fim: '
                      '&quot;Was Eirik rude? Was Tom?&quot; (Nenhum dos dois &mdash; e o ponto da aula.)',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'BRITANICO do norte (Leeds): o u de &quot;much&quot; e &quot;trouble&quot; soa mais fechado, '
                      'quase /u/. Toque 2 vezes. Pergunte: &quot;Which is closer to you: Harriet in Oslo, or the man '
                      'who said one coffee, black?&quot;',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. Why does the question '
                     'change order when it gets polite?&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 perguntas (toque o audio). ESCALA: da mais '
                   'direta a mais educada. Pergunte: &quot;In the first one, is comes before the station. What about '
                   'the second?&quot; Espere ela descobrir a ordem de afirmacao. Depois: &quot;Where is do in the '
                   'third?&quot; (Sumiu.) So entao &quot;Reveal the Rule&quot;. CCQs: &quot;Could you tell me where '
                   'the station is &mdash; is it a question? (Sim, mas a segunda metade e ordem de afirmacao.)&quot; '
                   '&quot;Would you mind opening the window? &mdash; if I say no, do I open it? (Sim, abre.)&quot; '
                   'Volte a frase anotada no hook e corrija junto.',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a forma ORALMENTE antes de clicar. Itens 3 e 6: sem '
                    'does/do na segunda metade, e o s da terceira pessoa volta (opens, costs).',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Josh, americano, dono de uma cabana em Vermont. '
                    'Clique &quot;Next Line&quot; e toque o audio. Nas falas da Ana, peca que ELA fale primeiro. '
                    'PRAGMATICA: a Ana comeca muito educada (&quot;sorry to impose&quot;) e o Josh diz que ela nao '
                    'precisa &mdash; o americano fica no MEIO da escala. A ultima fala dela e a ponte para o Brasil.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o JOSH, nunca sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar.',
        'artifact': '<strong>Artefato (5 min):</strong> Tres mensagens de anfitrioes com o MESMO pedido. Ana ordena '
                    'da mais direta a mais educada e depois reescreve a da Ingrid no estilo da Margaret. O ponto: a '
                    'Ingrid NAO e grosseira &mdash; e norueguesa.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick questions, '
                     'and your own answers.&quot;',
        'detective': '<strong>Detective (5 min):</strong> Ana corrige ANTES de clicar. Os 4 primeiros sao de '
                     'lingua (ordem, do/does, if could you, mind to). O 5o NAO e de lingua: a frase esta '
                     'gramaticalmente certa, mas para uma britanica soa como ordem. Esse e o erro de ancora da noite.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. Repare: nem toda situacao pede o nivel maximo &mdash; em Oslo, direto e o '
                     'certo.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. A 4a '
                    'inverte: ELA te pergunta. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica para '
                    'comparar. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so depois de tudo feito. A ultima linha e a ancora '
                     'intercultural da noite.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Two very '
                     'different hosts.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e a Margaret, britanica, gentil e indireta. Se a Ana '
               'for direta demais, reaja com um silencio educado (&quot;Oh... right.&quot;) e deixe ela perceber. '
               'Corrija so a ordem das palavras.',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e o Eirik, noruegues, direto. Se a Ana fizer muitos '
               'rodeios, pergunte: &quot;Sorry, what do you need?&quot; Depois, compare com ela: qual dos dois foi '
               'mais natural para ELA?',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. NAO corrija durante. Depois, '
               'ela te faz duas perguntas educadas. Anote &quot;where is&quot; dentro de pergunta indireta para o '
               'feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Da mais neutra '
                    '(could you tell me) a mais britanica (I was wondering if).',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Fourteen lessons in, and tonight you learned '
                 'that polite depends on who is listening.&quot; Homework (oralmente, opcional): mandar um audio '
                 'pedindo o mesmo favor duas vezes &mdash; uma para um noruegues, uma para uma britanica. Proxima '
                 'aula: Looking Back &mdash; a terceira condicional, o que ela mudaria e o que nao mudaria.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'Asking Nicely -- and Who You Are Asking',
        'desc': 'Indirect and polite questions, and how much politeness a Norwegian, a British and an American listener expects.',
        'context_paras': [
            'When Ana stayed in a guesthouse in Norway, her host Ingrid sent her a message: <em>Kitchen closes at '
            '10. Thanks.</em> At first it seemed <strong>blunt</strong>, but Ingrid was only being '
            '<strong>straightforward</strong>. Norwegians like to <strong>get to the point</strong>.',
            'In England it was different. Her landlady, Margaret, never said anything directly. She liked to '
            '<strong>hedge</strong>: <strong>I was wondering if you could</strong> close the window, or '
            '<strong>would you mind turning</strong> the music down? Ana sometimes felt she was '
            '<strong>walking on eggshells</strong>, because she did not want to come across as '
            '<strong>pushy</strong>.',
            'In the United States, her host Josh was friendly and quick. When Ana asked, <strong>Could you tell me '
            'where the supermarket is?</strong>, he laughed and said she did not need to <strong>beat around the '
            'bush</strong>. For Ana, the lesson was clear: the most <strong>courteous</strong> question is the one '
            'that fits the person you are asking.',
        ],
        'context_quiz': [
            ('Why did Ingrid write such a short message?',
             [('Because she was angry with Ana.', False),
              ('Because Norwegians are straightforward and like to get to the point.', True),
              ('Because she did not speak English well.', False)]),
            ('"Could you tell me where the supermarket is?" Why is not where is the supermarket?',
             [('Because in an indirect question the second half has statement order.', True),
              ('Because is must always go at the end of a sentence.', False),
              ('Because the question is in the past.', False)]),
            ('What is the main idea of the text?',
             [('English speakers are always very polite.', False),
              ('Ana did not like her hosts.', False),
              ('The right level of politeness depends on who you are asking.', True)]),
        ],
        'tip_title': 'Indirect and Polite Questions',
        'tip_sub': 'The polite part goes to the front. The question itself goes back to statement order.',
        'tip_rows': [
            ('direct question', 'Verb before the subject', 'Where <strong>is the station</strong>?'),
            ('Could you tell me + wh-word', 'Statement order at the end', 'Could you tell me where <strong>the station is</strong>?'),
            ('Do you know + if / whether', 'For yes/no questions, no do', 'Do you know <strong>if it opens</strong> on Sundays?'),
            ('Would you mind + -ing', 'A polite request', 'Would you mind <strong>closing</strong> the door?'),
            ('I was wondering if + could', 'Very polite, typical in the UK', 'I was wondering <strong>if you could</strong> help me.'),
        ],
        'tip_never': 'Could you tell me where is the station &middot; do you know what time does it open &middot; I '
                     'was wondering if could you &middot; would you mind to open. The second half of an indirect '
                     'question is never a question.',
        'fills': [
            ('Could you tell me where the station ', 'is', '?',
             'be -- one word, at the end, in statement order'),
            ('Do you know ', 'if', ' the kitchen closes at nine?',
             'one word -- for a yes/no question inside another question'),
            ('Do you know what time the shop ', 'opens', '?',
             'open -- no does here, so the verb takes the s'),
            ('Would you mind ', 'opening', ' the window?',
             'open -- the form that always follows mind'),
            ('I was wondering if you ', 'could', ' help me with my bags.',
             'can -- one word, softer in the past'),
            ('He is not rude, he is just ', 'blunt', '. He says what he thinks.',
             'one word -- saying what you think without being gentle'),
        ],
        'order_intro': 'Ana arrives at Josh&rsquo;s cabin in Vermont. Put the conversation in order.',
        'order': [
            'Hi, Ana! Welcome to Vermont. Did you find the cabin okay?',
            'Yes, thank you. Could you tell me where the nearest supermarket is?',
            'Sure! It is about ten minutes down the road.',
            'Great. And do you know if it is open on Sundays?',
            'It opens at eight on Sundays. Anything else? Just ask.',
            'Would you mind lending me a heater? The cabin is cold at night.',
        ],
        'quiz': [
            ('You are in London and you need directions. The most natural question is:',
             [('"Sorry, could you tell me where the museum is?"', True),
              ('"Sorry, could you tell me where is the museum?"', False),
              ('"Tell me where the museum is."', False)]),
            ('You want to know the opening time of a shop. You say:',
             [('"Do you know what time does the shop open?"', False),
              ('"Do you know what time the shop opens?"', True),
              ('"Do you know what time opens the shop?"', False)]),
            ('A Norwegian host sends you: "Breakfast at 8. No shoes inside." What does it mean?',
             [('She is angry with you.', False),
              ('She is being straightforward, which is normal in Norway.', True),
              ('She does not want you in the house.', False)]),
            ('You need your British neighbor to move his car. The best choice is:',
             [('"Move your car."', False),
              ('"I was wondering if you could move your car a little."', True),
              ('"I was wondering if could you move your car."', False)]),
        ],
        'think': 'Think about a time you had to ask a stranger or a new neighbor for something. What did you say, '
                 'and how did it come across? Now record the same request three times: for a Norwegian, for a '
                 'British person and for an American. Use at least one could you tell me, one do you know if and '
                 'one I was wondering if.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Video',
         'title': 'Norway culture shock &mdash; Asian in Norway (YouTube)',
         'desc': 'A YouTuber who moved to Norway talks about the things that surprised them most in everyday life. '
                 'English as a lingua franca again: a non-native speaker, speaking clearly, about a culture that is '
                 'not their own.',
         'tip': 'every time something sounds strange or rude, ask yourself: is it rude, or just straightforward? '
                'Then say it as a polite question: do you know why Norwegians...?',
         'url': 'https://www.youtube.com/watch?v=rOduD1fPyvo', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Luke&rsquo;s English Podcast &mdash; 541. What British People Say vs What They Mean',
         'desc': 'A British teacher goes through the polite phrases the British use and what they really mean '
                 '&mdash; the other side of Eirik&rsquo;s story about the dishes.',
         'tip': 'write down three phrases that hedge, like I was just wondering. Then say what a Norwegian would '
                'say instead.',
         'url': 'https://teacherluke.co.uk/2018/07/31/541-what-british-people-say-vs-what-they-mean/',
         'cta': 'Listen on the podcast website'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'YouTube',
         'title': 'What Brits Say vs What They Mean (Politeness Decoded) &mdash; Unlock English with Hannah',
         'desc': 'A short, clear video from a British teacher on politeness, understatement and the polite phrases '
                 'that confuse visitors. Standard British accent, good for listening practice.',
         'tip': 'pause after each phrase and turn it into an indirect question: could you tell me what... means?',
         'url': 'https://www.youtube.com/watch?v=Y91cWCKSf9s', 'cta': 'Watch on YouTube'},
    ],
}
