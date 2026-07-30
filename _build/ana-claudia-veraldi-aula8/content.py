# -*- coding: utf-8 -*-
"""Aula 8 -- Checkpoint, Block 1 (revisao das aulas 1-7 + benchmark de fala).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false, alem do dialogo.
Sotaques do listening (CURRICULO V3): mistura de todos -- indiano + italiano.

O vocabulario NOVO da noite e deliberadamente de ESTRATEGIA DE FALA (ganhar tempo,
reformular, admitir que travou). Um checkpoint que so revisa nao ensina nada; este
entrega as ferramentas que permitem a Ana FALAR por dez minutos sem parar -- que e
exatamente o benchmark. A gramatica das aulas 1-7 e revisada nos exercicios, nao
reapresentada como novidade (REGRA 22).
"""

LESSON = {
    'n': 8,
    'menu_title': 'Checkpoint -- Block 1',
    'menu_desc': 'Everything from lessons 1 to 7 in one night, plus the language that keeps you '
                 'talking when the word you need refuses to come',
    'chapter_tag': 'Checkpoint',
    'title_html': 'Checkpoint <span class="accent">Block 1</span>',
    'title_sub': 'Seven lessons in. Tonight nothing new is taught and everything is used.',
    'phases': ['First Words', 'Keeping Going', 'What Fluency Is Not',
               'The Seven Codes', 'Practice', 'Your Turn', 'Wrap-Up'],

    # ---------------------------------------------------------------- chapter 1
    'warmup': {
        'heading': 'Seven Lessons <span class="accent">Ago</span>',
        'callback': 'Last time you walked a stranger through a hundred year old house: what had been '
                    'stripped back, what was being rewired, what nobody had touched. Before that, the '
                    'Tuesday in the traffic. Before that, the dogs, the town, the restoring, the '
                    'listening.',
        'question': 'Without preparing anything: what can you say in English now that you could not '
                    'say in April?',
    },
    'framing': {
        'heading': 'Nothing New. <span class="accent">Everything Used.</span>',
        'steps': [('Keeping Going', 'the phrases that buy you time'),
                  ('The Seven Codes', 'every structure from lessons 1 to 7'),
                  ('Ten Minutes', 'you talk, I time it, nobody interrupts')],
        'note': 'A checkpoint is not a test. It is the night you find out that things you fought for '
                'in April now come out without you choosing them &mdash; and that the ones that still '
                'do not come are <strong>four</strong>, not forty.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'What Happens When the <span class="accent">Word Will Not Come?</span>',
        'line1': 'Everybody loses a word mid-sentence, in every language, several times a day. '
                 'Fluent speakers lose them too. The difference is what happens in the next second.',
        'line2': 'In Portuguese you have twenty ways to fill that second. Tonight you get them in '
                 'English, because the silence is what makes you panic, not the missing word.',
    },

    # ---------------------------------------------------------------- chapter 2
    'vocab_heading': 'The Language of <span class="accent">Not Stopping</span>',
    'vocab_sub': 'Twelve items for the second after the word disappears',
    'vocab': [
        {'word': 'Off the top of my head', 'icon': 'bulb', 'expr': True,
         'def': 'From memory, without checking, and not exactly',
         'ex': 'Off the top of my head, I would say about eleven years.',
         'match': 'from memory, without checking, and not exactly'},
        {'word': 'To draw a blank', 'icon': 'moon',
         'def': 'To reach for something in your memory and find nothing there',
         'ex': 'I asked her for the name and she completely drew a blank.',
         'match': 'to reach into your memory and find nothing there'},
        {'word': 'Bear with me', 'icon': 'clock',
         'def': 'A polite way of asking somebody to wait while you find the words',
         'ex': 'Bear with me, I am trying to remember the English for this.',
         'match': 'a polite way of asking somebody to wait a moment'},
        {'word': 'To put it another way', 'icon': 'compass',
         'def': 'To say the same thing again in different words, because the first way failed',
         'ex': 'To put it another way, the house is older than the town.',
         'match': 'to say the same thing again in different words'},
        {'word': 'To get your point across', 'icon': 'target',
         'def': 'To make somebody understand what you actually mean',
         'ex': 'My grammar was terrible and I still got my point across.',
         'match': 'to make somebody understand what you actually mean'},
        {'word': 'To go off on a tangent', 'icon': 'map',
         'def': 'To start talking about something unrelated and never come back',
         'ex': 'Sorry, I went off on a tangent. Where was I?',
         'match': 'to start on something unrelated and never come back'},
        {'word': 'In a nutshell', 'icon': 'key', 'expr': True,
         'def': 'The whole thing said in very few words',
         'ex': 'In a nutshell, I left the city and I have not looked back.',
         'match': 'the whole thing said in very few words'},
        {'word': 'It slipped my mind', 'icon': 'wave',
         'def': 'I forgot it completely, and I did not mean to',
         'ex': 'I was going to call the builder and it completely slipped my mind.',
         'match': 'I forgot it completely and I did not mean to'},
        {'word': 'To be at a loss for words', 'icon': 'lock',
         'def': 'To have nothing to say, because of surprise or emotion rather than language',
         'ex': 'When they handed me the keys I was at a loss for words.',
         'match': 'to have nothing to say from surprise or emotion'},
        {'word': 'To struggle with something', 'icon': 'scale',
         'def': 'To find something hard and keep going at it anyway',
         'ex': 'I still struggle with conditionals, and I use them every day.',
         'match': 'to find something hard and keep going at it anyway'},
        {'word': 'To backtrack', 'icon': 'arrow',
         'def': 'To go back and correct something you have just said',
         'ex': 'Let me backtrack. I said Tuesday, and it was actually Wednesday.',
         'match': 'to go back and correct what you have just said'},
        {'word': 'To wing it', 'icon': 'plane',
         'def': 'To do something with no preparation at all and hope it works',
         'ex': 'I had no notes for that meeting. I completely winged it.',
         'match': 'to do something with no preparation and hope it works'},
    ],
    'vocabnote': "Two of tonight's twelve are whole expressions: off the top of my head and in a "
                 'nutshell. Notice what they have in common with the other ten &mdash; every single '
                 'one of them buys you two or three seconds while your brain finds the word. That is '
                 'not a trick. That is what fluent speakers are doing all day long.',
    'pron': ['Off the top of my head', 'In a nutshell', 'Bear with me',
             'To put it another way, nothing has been done since 1974.'],
    'gapfill': [
        {'before': 'I do not have the exact figure. ', 'answer': 'Off the top of my head',
         'after': ', about eleven years.'},
        {'before': 'Every time somebody asks me that name, I completely ',
         'answer': 'draw a blank', 'after': '.'},
        {'before': 'Stop me if I start to ', 'answer': 'go off on a tangent',
         'after': ', because I always do.'},
        {'before': 'Even when the grammar goes wrong, you can still ',
         'answer': 'get your point across', 'after': '.'},
        {'before': 'There were no notes and no slides, so I had to ',
         'answer': 'wing it', 'after': ' completely.'},
        {'before': '', 'answer': 'In a nutshell',
         'after': ', I left the city and I have not looked back.'},
    ],

    # ---------------------------------------------------------------- chapter 3
    'ch3_heading': 'What Fluency <span class="accent">Actually Is</span>',
    'ch3_sub': 'Read for the main idea, then two voices who are not native either',
    'reading_heading': 'The Myth of the <span class="accent">Silent Pause</span>',
    'reading': {
        'rtitle': 'Nobody Speaks Without Stopping',
        'paras': [
            'There is a belief, very common among adults who have studied English for years, that a '
            'fluent speaker produces language in a continuous line. Under that belief, every pause is '
            'evidence of failure. People who hold it tend to describe themselves as stuck, and a '
            'surprising number of them have been stuck for a decade.',
            'The recordings say something else entirely. Native speakers hesitate roughly every eight '
            'words. They repeat themselves, they backtrack, they go off on a tangent and come back, '
            'and they use an enormous number of small phrases whose only job is to occupy the second '
            'in which the next idea is being assembled. Off the top of my head. What I mean is. Bear '
            'with me.',
            'The difference between a fluent speaker and a blocked one is therefore not the number of '
            'pauses. It is what the pause is filled with. A fluent speaker fills it with language and '
            'keeps the floor. A blocked speaker fills it with silence, and the silence is read by '
            'everybody in the room, including the speaker, as failure. Panic arrives, and the panic '
            'is what removes the word, not the other way round.',
            'This has a practical consequence that is worth more than any grammar lesson. If you can '
            'be taught eight phrases that fill two seconds each, you have not been taught vocabulary. '
            'You have been given back sixteen seconds in every conversation, and in sixteen seconds '
            'almost anybody can find almost any word.',
        ],
        'source': 'Adapted for Lesson 8',
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist': [
            ['a', 'Native speakers are faster than learners and always will be', False],
            ['b', 'Fluency is not the absence of pauses, but what you put inside them', True],
            ['c', 'Grammar matters less than vocabulary when you are learning a language', False],
        ],
        'tf': [
            ['Fluent native speakers rarely hesitate when they talk.', 'f',
             'They hesitate roughly every eight words, and they repeat and backtrack constantly.'],
            ['The text says the pause itself is the problem.', 'f',
             'The pause is not the problem &mdash; what the pause is filled with is. Language keeps '
             'the floor; silence gets read as failure.'],
            ['According to the text, panic comes after the word disappears.', 'f',
             'The opposite order. The silence brings the panic, and the panic is what removes the word.'],
            ['Learning a handful of time-buying phrases has an effect out of proportion to its size.',
             't',
             'Eight phrases at two seconds each give back sixteen seconds per conversation, and that '
             'is usually enough to find any word.'],
            ['People who believe fluency means never stopping often stay blocked for years.', 't',
             'The text says a surprising number of them have been stuck for a decade.'],
        ],
    },
    'dialogue': {
        'name': 'Lars', 'cls': 'lars', 'initial': 'L', 'voice': 'nordic_m',
        'heading': 'He Has Been Stuck <span class="accent">Longer Than You</span>',
        'lines': [
            {'who': 'lars', 'text': 'Ana, can I ask you something? You have been doing these lessons '
                                    'for a while. Do you still <span class="vocab-highlight">struggle '
                                    'with</span> speaking, or is that over?'},
            {'who': 'ana', 'text': 'It is not over. But something has changed. '
                                   '<span class="vocab-highlight">In a nutshell</span>, I stopped going '
                                   'silent when I lose a word.'},
            {'who': 'lars', 'text': 'That is exactly my problem. I '
                                    '<span class="vocab-highlight">draw a blank</span> and then there '
                                    'is this terrible silence and everybody waits.'},
            {'who': 'ana', 'text': 'So fill it. Say <span class="vocab-highlight">bear with me</span>, '
                                   'or <span class="vocab-highlight">off the top of my head</span>, and '
                                   'keep the floor while you look for it.'},
            {'who': 'lars', 'text': 'Does that not sound like you are inventing time?'},
            {'who': 'ana', 'text': 'You are inventing time. So is everybody else. I '
                                   '<span class="vocab-highlight">went off on a tangent</span> twice in '
                                   'this conversation and you did not notice.'},
            {'who': 'lars', 'text': 'I did not, actually. And your grammar was not perfect either, '
                                    'but I understood every word.'},
            {'who': 'ana', 'text': 'That is the whole point. I '
                                   '<span class="vocab-highlight">got my point across</span>. Two years '
                                   'ago I would have said nothing and gone home furious with myself.'},
        ],
        'comp': [
            ('What does Lars describe as his problem?',
             'He draws a blank, and then there is a terrible silence while everybody waits for him.'),
            ('What is Lars worried about when Ana gives him the phrases?',
             'That using them sounds like inventing time &mdash; as though it were cheating rather '
             'than speaking.'),
            ('What does Lars admit at the end, and why does it matter?',
             'That he did not notice Ana going off on a tangent, and that her grammar was not perfect '
             'but he understood every word. It matters because it proves her point: getting the point '
             'across is not the same as being correct.'),
        ],
    },
    'listenings': [
        {'voice': 'indian_f',
         'heading': 'I Was Fluent Before I Was <span class="accent">Correct</span>',
         'intro': 'An Indian woman on the year she stopped apologising. Sound first &mdash; no text.',
         'text': "For a very long time I believed that I had to be correct before I was allowed to be "
                 "fluent, and I have since decided that this belief cost me about six years. I would "
                 "prepare a sentence in my head, check it twice, and by the time it was ready the "
                 "conversation had moved on. Everybody thought I was quiet. I was not quiet. I was "
                 "editing. What changed was a colleague, an Australian, who told me something quite "
                 "blunt over lunch. She said, nobody in this office has ever once noticed your grammar, "
                 "and all of us have noticed that you do not speak. That was not kind and it was "
                 "completely true. So I made a rule for myself. I would say the sentence first and "
                 "repair it afterwards if it needed repairing. In a nutshell, I gave myself permission "
                 "to backtrack out loud. And here is the strange part. Within about four months my "
                 "grammar improved as well, which is not what I expected at all. It turns out you "
                 "cannot correct a sentence you never said.",
         'comp': [
             ('What did she believe for years, and what did it cost her?',
              'That she had to be correct before she was allowed to be fluent. She reckons the belief '
              'cost her about six years.'),
             ('Why did people think she was quiet?',
              'Because she was preparing and checking every sentence in her head, and by the time it '
              'was ready the conversation had moved on. She was not quiet, she was editing.'),
             ('What rule did she make, and what surprised her about the result?',
              'To say the sentence first and repair it afterwards &mdash; to backtrack out loud. What '
              'surprised her is that her grammar improved too: you cannot correct a sentence you '
              'never said.'),
         ]},
        {'voice': 'italian_m',
         'heading': 'The Meeting Where I <span class="accent">Winged It</span>',
         'intro': 'An Italian man on the day he had no notes at all. Sound first &mdash; no text.',
         'text': "I want to tell you about the worst prepared meeting of my career, because it went "
                 "better than the ones I prepare. I was asked to present something with about ninety "
                 "seconds of warning. No slides, no notes, nothing. I completely winged it. And what I "
                 "noticed afterwards, listening back, was that I used about fifteen phrases that were "
                 "not really content at all. Let me put it another way. So, in a nutshell. Bear with "
                 "me a second. Off the top of my head, roughly forty percent. Those phrases were doing "
                 "the work that my preparation normally does, which is to give me somewhere to stand "
                 "while I think. The prepared version of me sounds better and says less, because the "
                 "prepared version is reading. My advice, and I give it to everybody in my team now, "
                 "is to learn the connective phrases before you learn more vocabulary. You will sound "
                 "twice as fluent with the same number of words.",
         'comp': [
             ('What happened at the meeting he describes?',
              'He was asked to present with about ninety seconds of warning &mdash; no slides, no '
              'notes &mdash; so he completely winged it, and it went better than his prepared meetings.'),
             ('What did he notice when he listened back to himself?',
              'That he used about fifteen phrases that were not content at all: let me put it another '
              'way, in a nutshell, bear with me, off the top of my head.'),
             ('What is his advice, and what reason does he give for it?',
              'Learn the connective phrases before learning more vocabulary, because you will sound '
              'twice as fluent with the same number of words. The prepared version of him sounds '
              'better and says less, because it is reading.'),
         ]},
    ],

    # ---------------------------------------------------------------- chapter 4
    'grammar': {
        'label': 'Grammar Review',
        'ch_heading': 'The Seven <span class="accent">Codes</span>',
        'ch_sub': 'One sentence per lesson &mdash; name the form before you look at the table',
        'heading': 'Which Lesson Does <span class="accent">Each One Come From?</span>',
        'examples': [
            'I have lived here for two years, and I moved in the March before that.',
            'It is far quieter here, and by far the best decision I have made.',
            'I have been restoring this house since the day I got the keys.',
            'The ground floor is being rewired, and nothing had been done since 1974.',
        ],
        'prompt': 'Four sentences, four different structures, and every one of them came out of a '
                  'lesson you have already had. Name the form in each before you open the table. If '
                  'you can name three of the four, this block is done.',
        'table': [
            ('Lesson 1 &mdash; present perfect vs past simple',
             'Experience with no date, against a finished moment with one.',
             'I <strong>have lived</strong> here for two years. I <strong>moved</strong> in March.'),
            ('Lesson 2 &mdash; comparatives and superlatives',
             'Two things measured, or one thing at the extreme, with the intensifier doing the work.',
             'It is <strong>far quieter</strong> &middot; <strong>by far the best</strong> decision.'),
            ('Lesson 3 &mdash; present perfect continuous',
             'How long something unfinished has been going on.',
             'I <strong>have been restoring</strong> it <strong>since</strong> March.'),
            ('Lesson 4 &mdash; asking for clarification',
             'The register scale, from blunt to careful.',
             '<strong>Sorry, I did not catch that</strong> &middot; <strong>Would you mind repeating?</strong>'),
            ('Lesson 5 &mdash; adjective order and -ed/-ing',
             'Opinion before fact, and the difference between what you feel and what a thing is.',
             'A <strong>lovely old wooden</strong> door &middot; I am <strong>exhausted</strong>, '
             'the walk is <strong>exhausting</strong>.'),
            ('Lesson 6 &mdash; past simple vs past continuous',
             'The scene that was already running, then the event that landed inside it.',
             'I <strong>was sitting</strong> in traffic <strong>when</strong> it <strong>happened</strong>.'),
            ('Lesson 7 &mdash; the passive',
             'The work first, the worker last or nowhere at all.',
             'The floor <strong>is being rewired</strong> &middot; nothing <strong>had been done</strong>.'),
        ],
        'oneliner': 'seven forms, and you now use six of them without deciding to.',
    },
    'mistakes': [
        ('I am living here since two years.', 'I have lived here for two years.'),
        ('It is more quiet than Sao Paulo and the most good decision.',
         'It is far quieter than Sao Paulo and by far the best decision.'),
        ('I was knowing it was the last straw.', 'I knew it was the last straw.'),
        ('The kitchen is rewiring this week.', 'The kitchen is being rewired this week.'),
    ],
    'mistake_note': 'One from lesson 1, one from lesson 2, one from lesson 6 and one from lesson 7. '
                    'These four are the ones that came back most often across the block &mdash; and '
                    'three of them are the same instinct: taking the Portuguese structure and putting '
                    'English words in it.',
    'gpractice_heading': 'One From <span class="accent">Each Lesson</span>',
    'gpractice': [
        {'before': 'I ', 'answer': 'have lived', 'after': ' here for two years now.',
         'cue': 'live &mdash; unfinished, still true (lesson 1)'},
        {'before': 'The town is ', 'answer': 'far quieter', 'after': ' than anywhere I have lived.',
         'cue': 'quiet &mdash; comparative with an intensifier (lesson 2)'},
        {'before': 'I ', 'answer': 'have been restoring', 'after': ' this house since March.',
         'cue': 'restore &mdash; how long, still going (lesson 3)'},
        {'before': 'I ', 'answer': 'was sitting', 'after': ' in traffic when it happened.',
         'cue': 'sit &mdash; the background scene (lesson 6)'},
        {'before': 'Nothing ', 'answer': 'has been done', 'after': ' to this house since 1998.',
         'cue': 'do &mdash; passive, result still visible (lesson 7)'},
    ],
    'artifact': {
        'heading': 'Your Own <span class="accent">Benchmark</span>',
        'doc_title': 'SPEAKING BENCHMARK &mdash; A. VERALDI',
        'doc_sub': 'Block 1 &middot; lessons 1 to 7',
        'doc_right': 'Ten minutes<br>No notes',
        'rows': [
            ('Part 1', 'Two minutes: where you live now and how it compares to where you lived before'),
            ('Part 2', 'Two minutes: the house, what has been done to it and what has not'),
            ('Part 3', 'Two minutes: the day you decided, with the scene before the event'),
            ('Part 4', 'Two minutes: what you have been working on since March, and for how long'),
            ('Part 5', 'Two minutes: one thing you still find hard in English, and what you do about it'),
            ('Rule', 'No notes. If a word disappears, use a phrase from tonight and keep talking.'),
        ],
        'comp': [
            ('Which structure does Part 1 almost force you to use, and why?',
             'Comparatives and superlatives. The moment you compare where you live now with where you '
             'lived before, you need far quieter, much smaller, by far the best.'),
            ('Part 3 needs two tenses, not one. Which two, and in what order?',
             'Past continuous for the scene that was already running, then past simple for the event '
             'that landed inside it. Scene first, event second &mdash; the other order kills the story.'),
            ('Part 4 asks how long. Which form, and what is the trap?',
             'Present perfect continuous: I have been working on it since March. The trap is the '
             'Portuguese structure, which gives I am working on it since March.'),
        ],
    },

    # ---------------------------------------------------------------- chapter 5
    'detective': [
        ('I am living here since two years.', 'I have lived here for two years.'),
        ('It is more quiet than Sao Paulo and the most good decision.',
         'It is far quieter than Sao Paulo and by far the best decision.'),
        ('I was knowing it was the last straw.', 'I knew it was the last straw.'),
        ('The kitchen is rewiring this week.', 'The kitchen is being rewired this week.'),
    ],
    'quickfire': [
        {'situation': 'You are asked a number you do not know precisely, and you are not going to look '
                      'it up. Answer anyway.',
         'tips': ['Off the top of my head, about eleven years.',
                  'Give the approximate number and move on. Do not apologise for it.']},
        {'situation': 'The word you need has simply disappeared. Buy yourself three seconds without '
                      'going silent.',
         'tips': ['Bear with me a second, I am looking for the word.',
                  'Keep the floor. Silence is what makes it worse, not the missing word.']},
        {'situation': 'You have just said something that came out wrong and you can hear it. Repair it '
                      'out loud.',
         'tips': ['Let me put it another way.', 'Sorry, let me backtrack. What I meant was...']},
        {'situation': 'You realise you have been talking about something completely different for a '
                      'minute. Get back without embarrassment.',
         'tips': ['Sorry, I went off on a tangent. Where was I?',
                  'Native speakers do this constantly and repair it in four words.']},
        {'situation': 'Somebody asks you to summarise ten minutes of talking in one sentence.',
         'tips': ['In a nutshell, I left the city and I have not looked back.',
                  'One sentence. Resist the temptation to explain it again.']},
        {'situation': 'You are asked what you still find hard in English. Answer without either '
                      'apologising or pretending.',
         'tips': ['I still struggle with conditionals, and I use them every day anyway.',
                  'Naming it precisely is what a B2 speaker does. Vague apology is what a beginner does.']},
    ],
    'speaking': [
        ('What can you say in English now that you could not say six months ago?',
         'I can tell a whole story with the scene first and the event afterwards, and I can talk about '
         'the house without naming a single builder.'),
        ('What still makes you go silent, and what are you going to do about it instead?',
         'When a word disappears I still freeze. From now on I say bear with me and keep the floor '
         'while I look for it.'),
        ('Somebody asks how long you have been restoring the house. Answer with the exact structure.',
         'I have been restoring it since the day I got the keys, so that is about two years now.'),
        ('In one sentence: what has this block actually changed?',
         'In a nutshell, I stopped editing before speaking, and I get my point across even when the '
         'grammar is not perfect.'),
    ],
    'build': [
        ('I / live here + two years (unfinished, still true)',
         'I have lived here for two years.'),
        ('this town / quiet + than Sao Paulo (comparative with an intensifier)',
         'This town is far quieter than Sao Paulo.'),
        ('I / restore the house + since March (how long, still going)',
         'I have been restoring the house since March.'),
        ('nothing / do + to the place since 1998 (passive, result still visible)',
         'Nothing has been done to the place since 1998.'),
    ],
    'answerkey_heading': 'The Whole Block on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole Block 1 key',
    'answerkey': [
        'Lesson 1 = present perfect (experience, no date) vs past simple (finished, with a date)',
        'Lesson 2 = comparatives and superlatives, with the intensifier: far quieter, by far the best',
        'Lesson 3 = present perfect continuous for how long something unfinished has been going on',
        'Lesson 4 = the register scale of asking again: sorry, what? / would you mind repeating that?',
        'Lesson 5 = adjective order (opinion before fact) and -ed vs -ing: exhausted / exhausting',
        'Lesson 6 = past continuous for the scene, past simple for the event that lands inside it',
        'Lesson 7 = the passive: was done, is being done, has been done, had been done',
        'And tonight: the eight phrases that fill the second in which you are looking for a word',
    ],

    # ---------------------------------------------------------------- chapter 6
    'rp_ch_heading': 'Ten Minutes, <span class="accent">No Notes</span>',
    'roleplay': {
        'guided': {
            'heading': 'The Colleague Who <span class="accent">Asks Everything</span>',
            'scenario': 'I am a new colleague on a video call and I ask you five short questions, one '
                        'from each lesson of this block: where you live, how it compares, how long you '
                        'have been restoring, what happened on the Tuesday, and what has been done to '
                        'the house. Answer each in two sentences.',
            'chips': ['I have lived', 'far quieter', 'have been restoring'],
        },
        'semi': {
            'heading': 'Lars Is Still <span class="accent">Editing</span>',
            'scenario': 'I am Lars, and I have just admitted that I prepare every sentence in my head '
                        'before I say it. Ask me two questions about how that feels, then tell me what '
                        'you did about the same problem &mdash; using at least three of tonight&rsquo;s '
                        'phrases while you do it.',
            'chips': ['bear with me', 'to put it another way', 'get your point across'],
        },
        'free': {
            'heading': 'The <span class="accent">Benchmark</span>',
            'scenario': 'Ten minutes, five parts, no notes and no interruptions. Where you live and how '
                        'it compares. The house and what has been done to it. The day you decided. What '
                        'you have been working on since March. And one thing you still find hard, with '
                        'what you now do about it.',
        },
    },

    # ---------------------------------------------------------------- chapter 7
    'wrap_heading': 'Seven Down, <span class="accent">Thirty-Three to Go</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Not Stopping</span>',
    'survival': [
        'Bear with me, I am looking for the word.',
        'Off the top of my head, about eleven years.',
        'Let me put it another way.',
        'Sorry, I went off on a tangent. Where was I?',
        'In a nutshell, I left the city and I have not looked back.',
    ],
    'checklist': [
        'I can fill a pause with language instead of silence.',
        'I can repair a sentence out loud without apologising for it.',
        'I can name which structure each of the seven lessons taught me.',
        'I spoke for ten minutes tonight with no notes at all.',
        'I know the phrases: bear with me, off the top of my head, in a nutshell, to backtrack.',
    ],
    'closing': {
        'badge': 'Block 1 Badge <span class="accent">Earned!</span>',
        'text': 'Ten minutes, no notes, two people who are not native speakers, and seven structures '
                'that were not there in April. Whatever you thought you could not do, Ana, you just '
                'did it out loud.',
        'next': 'Understanding Fast English',
    },

    # ---------------------------------------------------------------- pre-class
    'pc_title': 'Checkpoint Block 1 -- Everything from Lessons 1 to 7',
    'pc_desc': 'Reviewing the whole block and learning the phrases that keep you talking when a word '
               'disappears. Key phrases: off the top of my head, to draw a blank, bear with me, to put '
               'it another way, to get your point across, to go off on a tangent, in a nutshell, it '
               'slipped my mind, to be at a loss for words, to struggle with something, to backtrack, '
               'to wing it. Structures: all seven from lessons 1 to 7.',
    'pc_context': {
        'paras': [
            'Ana <strong>has lived</strong> in the interior for two years, and she '
            '<strong>moved</strong> there in March. The town is <strong>far quieter</strong> than '
            'Sao Paulo and, in her words, <strong>by far the best</strong> decision she has made. '
            'She <strong>has been restoring</strong> the same house <strong>since</strong> the day '
            'she got the keys.',
            'On the Tuesday it happened, she <strong>was sitting</strong> in traffic and nothing '
            '<strong>was moving</strong>, and then something <strong>snapped</strong>. Today the '
            'ground floor of the house <strong>is being rewired</strong>, and nothing '
            '<strong>had been done</strong> to the place since 1974.',
            'What she notices is not the grammar. It is that she no longer stops. When a word '
            'disappears she says <strong>bear with me</strong>, or gives an approximate figure '
            '<strong>off the top of her head</strong>, or <strong>puts it another way</strong>. She '
            'still <strong>struggles with</strong> conditionals. She <strong>gets her point across</strong> '
            'anyway, which two years ago she did not.',
        ],
        'quiz': [
            {'q': 'Why "has lived" in the first sentence and "moved" in the second?',
             'opts': [('Because the two years are unfinished, and March is a finished moment with a date.', True),
                      ('Because the present perfect is more formal than the past simple.', False),
                      ('Because English never uses the past simple with places.', False)]},
            {'q': '"She has been restoring the same house since the day she got the keys." What does '
                  'this form add that "she has restored" would not?',
             'opts': [('That the restoring is finished and the house is ready.', False),
                      ('That it is still going on, and the focus is on how long.', True),
                      ('That she restored it once and then stopped.', False)]},
            {'q': 'What does the third paragraph say has actually changed for her?',
             'opts': [('Her grammar became perfect.', False),
                      ('She stopped going silent when a word disappears, and gets her point across anyway.', True),
                      ('She no longer finds any part of English difficult.', False)]},
        ],
    },
    'pc_tip': {
        'title': 'The Seven Structures of Block 1',
        'lead': 'Nothing new here. One line per lesson, so you can see the whole block at once.',
        'table': [
            ('Lesson 1', 'Present perfect (no date) vs past simple (with one)',
             'I <strong>have lived</strong> here for two years. I <strong>moved</strong> in March.'),
            ('Lesson 2', 'Comparatives and superlatives, with intensifiers',
             'It is <strong>far quieter</strong> &middot; <strong>by far the best</strong> decision.'),
            ('Lesson 3', 'Present perfect continuous: how long, still going',
             'I <strong>have been restoring</strong> it <strong>since</strong> March.'),
            ('Lesson 4', 'Asking again, on a scale from blunt to careful',
             '<strong>Sorry, what?</strong> &middot; <strong>Would you mind repeating that?</strong>'),
            ('Lesson 5', 'Adjective order, and -ed vs -ing adjectives',
             'A <strong>lovely old wooden</strong> door &middot; I am <strong>exhausted</strong>.'),
            ('Lesson 6', 'Past continuous for the scene, past simple for the event',
             'I <strong>was sitting</strong> in traffic <strong>when</strong> it <strong>happened</strong>.'),
            ('Lesson 7', 'The passive: the work first, the worker last or nowhere',
             'The floor <strong>is being rewired</strong> &middot; nothing <strong>had been done</strong>.'),
        ],
        'never': 'I am living here since two years &middot; the most good decision &middot; I was '
                 'knowing &middot; the kitchen is rewiring. All four take a Portuguese structure and '
                 'put English words inside it.',
    },
    'pc_blanks': [
        {'before': '', 'answer': 'Bear with me', 'after': ', I am looking for the word.',
         'hint': 'Hint: three words -- ask somebody politely to wait a moment'},
        {'before': 'I do not have the exact figure. ', 'answer': 'Off the top of my head',
         'after': ', about eleven years.',
         'hint': 'Hint: six words -- from memory, without checking, and not exactly'},
        {'before': 'Sorry, I ', 'answer': 'went off on a tangent', 'after': '. Where was I?',
         'hint': 'Hint: you started on something unrelated and did not come back'},
        {'before': '', 'answer': 'In a nutshell', 'after': ', I left the city and I have not looked back.',
         'hint': 'Hint: three words -- the whole thing said in very few words'},
        {'before': 'I ', 'answer': 'have been restoring', 'after': ' this house since March.',
         'hint': 'Hint: restore -- how long, and it is still going on (lesson 3)'},
        {'before': 'Nothing ', 'answer': 'has been done', 'after': ' to the place since 1998.',
         'hint': 'Hint: do -- passive, and the result is still there (lesson 7)'},
    ],
    'pc_order_lead': 'Lars asks Ana whether speaking is still hard. Put the exchange in a logical order.',
    'pc_order': [
        'Do you still struggle with speaking, or is that over?',
        'It is not over. But I stopped going silent when I lose a word.',
        'That is exactly my problem. There is this terrible silence and everybody waits.',
        'So fill it. Say bear with me, and keep talking while you look for the word.',
        'Does that not sound like you are inventing time?',
        'You are inventing time. So is everybody else, in every language.',
    ],
    'order_voice': 'arthur',
    'pc_squiz': [
        {'q': 'You are asked for a number you do not know exactly. The natural answer is:',
         'opts': [('"Off the top of my head, about eleven years."', True),
                  ('"I am sorry, I cannot answer that question."', False),
                  ('"In my head from the top, eleven years more or less."', False)]},
        {'q': 'The word you need has disappeared mid-sentence. You:',
         'opts': [('Stop talking and wait until it comes back.', False),
                  ('Say "bear with me a second" and keep the floor while you look for it.', True),
                  ('Apologise for your English and change the subject.', False)]},
        {'q': 'You have just said something that came out wrong. The natural repair is:',
         'opts': [('"Sorry, my English is very bad, forget it."', False),
                  ('"Let me put it another way."', True),
                  ('"I am at a loss for words about this."', False)]},
        {'q': 'A colleague asks how long you have been restoring the house. You answer:',
         'opts': [('"I have been restoring it since March."', True),
                  ('"I am restoring it since March."', False),
                  ('"I restore it since March."', False)]},
    ],
    'pc_think': 'Talk for two minutes about what has changed in your English since April. Use the '
                'present perfect at least twice, one comparative, and at least two of the phrases '
                'from this lesson. If a word disappears, say bear with me out loud and keep going '
                'instead of stopping the recording.',

    # ------------------------------------------------------------ complementares
    'media': [
        {'id': 'series', 'thumb': 'doc', 'type': 'Talk',
         'title': "Don't insist on English! &mdash; Patricia Ryan, TED (11 min)",
         'desc': 'A teacher who spent thirty years in the Gulf argues that the world lost enormous '
                 'amounts of thinking to the belief that ideas only count once they are said in '
                 'correct English. It is the same argument you had with yourself for a decade, made '
                 'by somebody who taught the language for a living.',
         'tip': 'Tip: she speaks slowly and structures everything. Listen once for the argument, then '
                'again and write down every phrase she uses to move from one point to the next.',
         'url': 'https://www.ted.com/talks/patricia_ryan_don_t_insist_on_english',
         'cta': 'Watch on TED'},
        {'id': 'podcast', 'thumb': 'podcast', 'type': 'Podcast',
         'title': 'The Allusionist &mdash; a show about the English language, by Helen Zaltzman',
         'desc': 'Short episodes about where words come from and what people actually do with them. '
                 'The host is British, the guests are from everywhere, and nobody in it speaks in the '
                 'clean continuous line you were told fluency sounds like.',
         'tip': 'Tip: every episode has a free transcript on the site. Listen first, then read, then '
                'listen again. That order matters &mdash; reading first ruins the exercise.',
         'url': 'https://theallusionist.org/allusionist',
         'cta': 'Listen on The Allusionist'},
        {'id': 'youtube', 'thumb': 'video', 'type': 'Talk',
         'title': 'The benefits of a bilingual brain &mdash; TED-Ed (5 min)',
         'desc': 'Five minutes on what actually happens in a brain that runs two languages, including '
                 'why the second one feels slower even when it is not. Short enough to watch three '
                 'times in one sitting.',
         'tip': 'Tip: TED-Ed narration is fast and dense. Watch at 0.75x first, then at normal speed '
                'once you know what is coming.',
         'url': 'https://www.youtube.com/watch?v=MMmOLN5zBLY',
         'cta': 'Watch on YouTube'},
    ],

    # ------------------------------------------------------------------ teacher
    'teacher': {
        'open': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: '
                '"Tonight nothing new is taught and everything is used." Deixe claro o formato: e '
                'checkpoint, nao prova. O unico item realmente novo da noite e o vocabulario de '
                'ESTRATEGIA (ganhar tempo, reformular) &mdash; e ele existe para viabilizar o '
                'benchmark de 10 minutos no capitulo 6.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 7: a casa, o que foi '
                  'feito, o que esta sendo feito. Depois a PONTE (REGRA 27B): "Seven lessons. What can '
                  'you say now that you could not say in April?" Deixe falar livre, ZERO correcao. '
                  'ANOTE tudo: esta e a primeira metade do benchmark, e voce vai comparar com o '
                  'capitulo 6 no fim da aula.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. Insista na ultima '
                   'frase do slide: o que ainda nao sai sao QUATRO coisas, nao quarenta. A Ana '
                   'descreveu na consultoria o ciclo ansiedade-travamento; um checkpoint mal '
                   'enquadrado alimenta exatamente esse ciclo. Enquadre como INVENTARIO, nunca como '
                   'avaliacao.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> Este slide e o coracao da noite. Pergunte: '
                '"What do you do, right now, in the second after a word disappears?" Se ela disser '
                'que trava e fica em silencio, NAO console &mdash; diga que e exatamente isso que a '
                'aula vai resolver, e passe.',
        'tr_vocab': '<strong>Transicao vocab (1 min):</strong> Diga: "Twelve phrases for the second '
                    'after the word disappears. Click each card." Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ '
                  '"off the top of my head": "Am I sure of the number? (Nao &mdash; e aproximado, e '
                  'todo mundo entende que e.)" CCQ "to draw a blank": "Did I forget it, or can I not '
                  'reach it now? (Nao alcanco AGORA &mdash; e diferente de esquecer.)" CCQ "bear with '
                  'me": "Is it rude? (Ao contrario &mdash; e educado e compra tempo.)" Peca que ela '
                  'diga cada uma em voz alta 2 vezes: estas sao para USAR hoje, nao para reconhecer.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ "in a nutshell": '
                  '"Long or short? (Curtissimo &mdash; e um resumo, nao uma introducao.)" CCQ "to '
                  'backtrack": "Am I saying I was wrong? (Estou corrigindo em voz alta, que e o que '
                  'nativo faz o tempo todo.)" CCQ "to wing it": "Did I prepare? (Zero.)" Marque que '
                  '"to be at a loss for words" e sobre EMOCAO, nao sobre idioma &mdash; e o unico da '
                  'lista que nao serve de muleta linguistica.',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. '
                    'Certo fica verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note '
                    'como ponte: as doze existem para comprar dois ou tres segundos.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> Foque no RITMO, nao nos fonemas: estas '
                'frases precisam sair AUTOMATICAS, sem pensar. "Off the top of my head" cola tudo e '
                'vira /oftha-TOPu-vmy-hed/. "In a nutshell" tem o stress em NUT. "Bear with me" &mdash; '
                'BEAR rima com "air", nunca com "beer" (erro classico de brasileiro). Peca 3 '
                'repeticoes de cada, cada vez mais rapido.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a expressao que '
                   'falta ANTES de clicar. As candidatas estao no banco embaixo, fora de ordem. Se '
                   'travar, aponte duas do banco e pergunte qual das duas cabe. Clicar de novo fecha '
                   '(REGRA 27E).',
        'tr_ch3': '<strong>Transicao (1 min):</strong> Diga: "A short text about what fluency is not. '
                  'Read for the main idea &mdash; do not stop at every word." Passe ao proximo.',
        'reading': '<strong>Leitura + Gist (6 min):</strong> De 3 minutos de leitura silenciosa. Depois '
                   'a pergunta de gist: "What is the best title?" Ana clica e o card certo fica verde. '
                   'NAO peca traducao palavra a palavra. Este texto foi escrito para ELA: o paragrafo 3 '
                   'descreve exatamente o ciclo que ela relatou na consultoria (silencio, panico, '
                   'palavra some). Deixe pousar.',
        'tf': '<strong>True / False (4 min):</strong> Ana decide TRUE ou FALSE ANTES de clicar. Ao '
              'clicar, veredito e justificativa aparecem. Peca que ela aponte a linha do texto que '
              'prova cada resposta. A 3a e a mais importante: a ordem e silencio -> panico -> palavra '
              'some, e nao o contrario.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Lars, NORDICO, que trava exatamente '
                    'como ela travava. Clique "Next Line" e toque o audio de cada fala. Para cada fala '
                    'da Ana, peca que ELA fale primeiro. INVERSAO PROPOSITAL: aqui a Ana e quem tem a '
                    'resposta e o outro e quem esta travado. Ela nunca esteve nesse lugar em ingles. '
                    'Nao explique isso a ela &mdash; deixe acontecer.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o LARS, nao sobre a '
                         'Ana (REGRA 27F). Ana responde ANTES de revelar. Na 3a, puxe a conclusao: o '
                         'Lars nao percebeu os erros dela porque entendeu tudo. Getting the point '
                         'across nao e o mesmo que estar correto &mdash; e a tese da noite.',
        'listen1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES '
                   'de tocar. Esta e uma INDIANA falando ingles: ritmo silabico, T e D retroflexos, '
                   'entonacao que sobe no meio da frase. Avise ANTES. Este audio existe por um motivo '
                   'especifico: a frase final ("you cannot correct a sentence you never said") e a '
                   'resposta direta ao habito da Ana de editar antes de falar. Pergunte a ela se '
                   'reconhece o comportamento.',
        'tr_grammar': '<strong>Transicao gramatica (1 min):</strong> Diga: "Four sentences. Every one '
                      'came out of a lesson you have already had. Name the form." Passe ao proximo.',
        'grammar': '<strong>Grammar review (7 min):</strong> Este slide NAO e discovery &mdash; e '
                   'inventario. Peca que a Ana NOMEIE a forma de cada uma das quatro frases ANTES de '
                   'abrir a tabela. Se ela acertar tres das quatro, o bloco esta consolidado e voce '
                   'pode acelerar. Se acertar uma ou nenhuma, ANOTE quais faltaram: e o que entra na '
                   'revisao do Bloco 2. So depois clique "Reveal the Rule" e leia a tabela linha por '
                   'linha, uma aula por linha.',
        'mistake': '<strong>Common mistake (4 min):</strong> Os quatro erros que mais voltaram no bloco, '
                   'um de cada aula-chave: (1) "am living since" &mdash; estrutura do portugues; (2) '
                   '"more quiet / most good" &mdash; comparativo regular onde e irregular; (3) "was '
                   'knowing" &mdash; verbo de estado com -ing; (4) "is rewiring" no lugar de "is being '
                   'rewired". Mostre certo vs errado e peca 2 repeticoes das versoes certas.',
        'gpractice': '<strong>Practice (4 min):</strong> Uma frase por aula. Ana escolhe ORALMENTE antes '
                     'de clicar. Se travar, pergunte de qual AULA aquela frase veio &mdash; lembrar do '
                     'contexto costuma trazer a forma junto.',
        'listen2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES '
                   'de tocar. Este e um ITALIANO falando ingles: vogais finais alongadas, H inicial '
                   'quase mudo, ritmo muito melodico. Avise ANTES. O conselho final dele ("learn the '
                   'connective phrases before you learn more vocabulary") e literalmente a justificativa '
                   'do vocabulario desta aula. Aponte isso depois que ela responder.',
        'artifact': '<strong>Artefato (5 min):</strong> E o roteiro do benchmark que ela vai fazer no '
                    'capitulo 6. MOSTRE ANTES de cobrar: ela precisa saber o que vem. As 3 perguntas '
                    'fazem ela identificar QUAL estrutura cada parte exige &mdash; e isso que impede o '
                    'benchmark de virar cinco minutos de present simple. Se ela acertar as tres, ela '
                    'entra no capitulo 6 sabendo o que vai usar.',
        'tr_practice': '<strong>Transicao practice (1 min):</strong> Diga: "Now we train: detective, '
                       'quick fire, and building." Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. "What is wrong '
                     'here?" Ana corrige ANTES de clicar. Sao os mesmos quatro do slide de Common '
                     'Mistake. Acertar os quatro sozinha = bloco consolidado.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez. Ana responde em voz '
                     'alta ANTES de abrir as Tips. Estas seis sao TODAS de estrategia, nao de conteudo '
                     '&mdash; o objetivo e que a resposta saia em menos de dois segundos. Se ela pensar '
                     'antes de responder, o exercicio falhou: peca de novo, mais rapido.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. '
                    'A 2a e a mais importante da aula: ela tem de declarar em voz alta o que vai fazer '
                    'no lugar de travar. Faca ela dizer a frase concreta ("I say bear with me"), nunca '
                    'a intencao vaga ("I try to continue").',
        'build': '<strong>Sentence Building (4 min):</strong> Uma frase por aula do bloco. Ana monta a '
                 'frase COMPLETA em voz alta, depois clica para comparar. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO no fim. '
                     'Sao as 7 aulas em 7 linhas mais a de hoje &mdash; peca que ela fotografe: e o '
                     'mapa do bloco inteiro.',
        'tr_roleplay': '<strong>Transicao role-play (1 min):</strong> Diga: "Now ten minutes, five '
                       'parts, and the last one has no help at all." Passe ao proximo.',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e um colega novo numa call. Faca as '
               'CINCO perguntas na ordem, uma por aula do bloco. Ana responde em duas frases cada. '
               'Corrija SO a escolha de estrutura, nada mais. Isto e o aquecimento do benchmark.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e o Lars, que acabou de admitir que '
               'edita cada frase na cabeca antes de falar. Ana precisa PERGUNTAR antes de aconselhar, e '
               'usar pelo menos tres das frases da noite enquanto fala. CONTE quantas ela usa e diga o '
               'numero no fim.',
        'rp3': '<strong>BENCHMARK (10 min):</strong> Dez minutos, cinco partes, sem notas e sem '
               'interrupcao. NAO corrija NADA durante. Cronometre de verdade. ANOTE: (a) quantas vezes '
               'ela ficou em silencio mais de 3 segundos, (b) quantas frases-muleta da noite ela usou, '
               '(c) quais das 7 estruturas apareceram espontaneamente. No fim, diga os TRES numeros a '
               'ela. Compare com o que ela disse no warm-up. Este registro e a linha de base do Bloco 2 '
               '&mdash; guarde no controle de aulas.',
        'tr_wrap': '<strong>Transicao wrap-up (1 min):</strong> Diga: "Ten minutes, no notes, and seven '
                   'structures that were not there in April."',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a '
                    'Ana repita ate sair sem pensar. Estas cinco sao as unicas da aula que ela precisa '
                    'ter na ponta da lingua ANTES da proxima aula &mdash; a aula 9 e sobre entender '
                    'ingles rapido, e ela vai precisar delas.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: "Click each item if you feel confident." '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 8 registrada como '
                     'concluida no passaporte.',
        'closing': '<strong>Encerramento (2 min):</strong> Diga os tres numeros do benchmark em voz alta '
                   'e diga o que eles significam &mdash; sem suavizar e sem dramatizar. Homework '
                   '(oralmente, opcional): repetir o benchmark de 10 minutos sozinha, gravado, e '
                   'comparar com a gravacao de hoje. Proxima aula: Understanding Fast English &mdash; '
                   'connected speech, gonna, wanna, e por que o ingles falado nao tem espacos entre as '
                   'palavras.',
    },
}
