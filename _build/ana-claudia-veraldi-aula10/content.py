# -*- coding: utf-8 -*-
"""Aula 10 -- I Used to Live in the City (used to / would).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false, alem do dialogo.
Sotaques do listening (CURRICULO V3): nordico + britanico.
Callback da aula 9: ela passou a noite decodificando fala rapida; agora usa isso
para contar os habitos que ficaram para tras -- e a gramatica que a lingua reserva
so para isso.
"""

LESSON = {
    'n': 10,
    'menu_title': 'I Used to Live in the City',
    'menu_desc': 'The habits that stayed behind in Sao Paulo, and the two forms English keeps '
                 'exclusively for the life you no longer live',
    'grammar_point': 'used to and would for past habits',
    'chapter_tag': 'The Life Before',
    'title_html': 'I Used to Live <span class="accent">in the City</span>',
    'title_sub': 'English has a tense that exists only for the person you used to be.',
    'phases': ['First Words', 'The Words of Routine', 'The Life You Left',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],

    # ---------------------------------------------------------------- chapter 1
    'warmup': {
        'heading': 'You Spent Eleven Years <span class="accent">Doing the Same Thing</span>',
        'callback': 'Last time you found out that nobody actually says going to, and that the first '
                    'two minutes of a call go over everybody&rsquo;s head. You listened to a man '
                    'giving an update at full speed and you caught the headline.',
        'question': 'What did you do at exactly a quarter past seven, every weekday, for eleven years?',
    },
    'framing': {
        'heading': 'A Tense for the Person <span class="accent">You Used to Be</span>',
        'steps': [('The Words', 'a creature of habit, on autopilot, back then...'),
                  ('The Life', 'a text and two people who left a routine behind'),
                  ('The Two Forms', 'used to and would, and the one place would cannot go')],
        'note': 'Portuguese does this with the imperfect and nobody has to think about it. English '
                'built <strong>two separate structures</strong> for the same job, and put a rule '
                'between them that almost nobody teaches you.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'What Do You <span class="accent">Not Miss?</span>',
        'line1': 'Everybody asks what you miss about the city. It is the easy question, and the answer '
                 'is usually a restaurant.',
        'line2': 'The harder one: what did you do every single day for years that you have not thought '
                 'about once since you left?',
    },

    # ---------------------------------------------------------------- chapter 2
    'vocab_heading': 'The Language of <span class="accent">a Routine</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'To take something for granted', 'icon': 'gift',
         'def': 'To stop noticing something good because it is always there',
         'ex': 'I took the bakery on the corner completely for granted.',
         'match': 'to stop noticing something good because it is always there'},
        {'word': 'A creature of habit', 'icon': 'clock', 'expr': True,
         'def': 'Somebody who does the same things in the same order, every time',
         'ex': 'I am a creature of habit, and the move broke every routine I had.',
         'match': 'somebody who does the same things in the same order'},
        {'word': 'To fall into a routine', 'icon': 'compass',
         'def': 'To start doing the same thing every day without ever deciding to',
         'ex': 'Within a month I had fallen into a routine I never chose.',
         'match': 'to start doing the same thing daily without deciding to'},
        {'word': 'Second nature', 'icon': 'star', 'expr': True,
         'def': 'So familiar that you do it without thinking at all',
         'ex': 'By the third year that drive was second nature.',
         'match': 'so familiar that you do it without thinking at all'},
        {'word': 'On autopilot', 'icon': 'plane',
         'def': 'Doing something without paying any attention, from sheer repetition',
         'ex': 'I did that whole journey on autopilot, five days a week.',
         'match': 'doing something without attention, from sheer repetition'},
        {'word': 'To break a habit', 'icon': 'bolt',
         'def': 'To stop doing something you have done for years',
         'ex': 'Moving house is the fastest way to break a habit.',
         'match': 'to stop doing something you have done for years'},
        {'word': 'Back then', 'icon': 'moon',
         'def': 'At that time in the past, when things were different',
         'ex': 'Back then, nobody worked from home at all.',
         'match': 'at that time in the past, when things were different'},
        {'word': 'To miss out on something', 'icon': 'flag',
         'def': 'To lose the chance to have or do something good',
         'ex': 'I missed out on eleven years of evenings, sitting in that car.',
         'match': 'to lose the chance to have or do something good'},
        {'word': 'A regular', 'icon': 'people',
         'def': 'Somebody who goes to the same place so often that they are known there',
         'ex': 'I was a regular at that place for nine years and I never asked his name.',
         'match': 'somebody known at a place because they go there so often'},
        {'word': 'To wind down', 'icon': 'leaf',
         'def': 'To relax slowly at the end of a day or a period of work',
         'ex': 'It took me two hours to wind down after that commute.',
         'match': 'to relax slowly at the end of a day'},
        {'word': 'To dread', 'icon': 'lock',
         'def': 'To feel real fear about something that has not happened yet',
         'ex': 'I used to dread Sunday evenings more than Monday mornings.',
         'match': 'to feel real fear about something that is coming'},
        {'word': 'To look back on something', 'icon': 'map',
         'def': 'To think about a period of your life that is over',
         'ex': 'When I look back on those years I mostly remember being tired.',
         'match': 'to think about a period of your life that is over'},
    ],
    'vocabnote': "Two of tonight's twelve are whole expressions: a creature of habit and second "
                 'nature. Both of them describe the same thing from opposite sides &mdash; the person '
                 'who repeats, and the act that has been repeated so often it disappeared. Between '
                 'them, they are most of what a routine actually is.',
    'pron': ['On autopilot', 'To dread', 'A creature of habit',
             'I used to dread Sunday evenings more than Monday mornings.'],
    'gapfill': [
        {'before': 'It is very easy to ', 'answer': 'take something for granted',
         'after': ' when you have had it every day for years.'},
        {'before': 'I am a ', 'answer': 'creature of habit',
         'after': ', and the move broke every routine I had.'},
        {'before': 'By the third year, that drive was ', 'answer': 'second nature', 'after': '.'},
        {'before': 'I did that whole journey ', 'answer': 'on autopilot',
         'after': ', five days a week, for eleven years.'},
        {'before': '', 'answer': 'Back then',
         'after': ', nobody worked from home and nobody thought it was strange.'},
        {'before': 'I used to ', 'answer': 'dread',
         'after': ' Sunday evenings more than Monday mornings.'},
    ],

    # ---------------------------------------------------------------- chapter 3
    'ch3_heading': 'The Life You <span class="accent">Left Behind</span>',
    'ch3_sub': 'Read for the main idea, then a Londoner and a Norwegian',
    'reading_heading': 'The Eleven Years <span class="accent">Nobody Remembers</span>',
    'reading': {
        'rtitle': 'What a Routine Actually Costs',
        'paras': [
            'Ask somebody who has left a big city what they miss and they will name a restaurant, a '
            'cinema, a particular street. Ask what they do not miss and the answers get much longer, '
            'much faster, and much more precise. This is not nostalgia working badly. It is what '
            'habits do to memory.',
            'A routine, by definition, is something you stop noticing. The first week of a new commute '
            'is vivid: you see the buildings, you count the stops, you dread the traffic. By the third '
            'month it is second nature, and by the third year the entire journey happens on autopilot. '
            'You arrive without any memory of the drive. Eleven years of mornings compress into one '
            'generic morning, and everything that was inside them goes with it.',
            'The cost is not the time, although the time is enormous. The cost is that a life spent on '
            'autopilot leaves very little behind to look back on. People who moved away describe the '
            'same strange discovery: not that they wasted the years, but that the years are simply not '
            'there. They were a regular somewhere for a decade and never learnt the owner&rsquo;s name.',
            'This is also why leaving is such a violent thing to do to yourself, and why so many people '
            'describe the first months as exhausting rather than relaxing. Every small decision that '
            'used to be automatic has to be made again from the beginning. That exhaustion is not a '
            'sign that the move was wrong. It is the sound of a routine being broken, and it is '
            'temporary.',
        ],
        'source': 'Adapted for Lesson 10',
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist': [
            ['a', 'Big cities are worse for your health than small towns', False],
            ['b', 'A routine erases the years it fills, and breaking one is exhausting on purpose', True],
            ['c', 'People who move away almost always regret the decision later', False],
        ],
        'tf': [
            ['People find it easier to say what they miss than what they do not miss.', 'f',
             'The opposite. The list of what they do not miss gets longer, faster and more precise.'],
            ['The text says the first week of a commute is already automatic.', 'f',
             'The first week is vivid &mdash; you see the buildings and count the stops. It becomes '
             'second nature by about the third month.'],
            ['According to the text, the real cost of a routine is the time it takes.', 'f',
             'The time is enormous, but the cost named in the text is that the years leave nothing '
             'behind to look back on.'],
            ['People who move away often say the years are simply not there in their memory.', 't',
             'They describe it as a strange discovery: not that the years were wasted, but that they '
             'are missing.'],
            ['The exhaustion of the first months after a move means the move was a mistake.', 'f',
             'The text says the exact opposite: it is the sound of a routine being broken, and it is '
             'temporary.'],
        ],
    },
    'dialogue': {
        'name': 'Ingrid', 'cls': 'ingrid', 'initial': 'I', 'voice': 'nordic_f',
        'heading': 'She Left Oslo <span class="accent">Four Years Ago</span>',
        'lines': [
            {'who': 'ingrid', 'text': 'Ana, people keep asking me what I miss about Oslo, and honestly '
                                      'I have to invent something. What I really remember is what I '
                                      '<span class="vocab-highlight">used to dread</span>.'},
            {'who': 'ana', 'text': 'Which was?'},
            {'who': 'ingrid', 'text': 'Sunday evening. Every Sunday I '
                                      '<span class="vocab-highlight">would</span> start checking the '
                                      'calendar at about six and the whole evening was ruined. Did you '
                                      'have that?'},
            {'who': 'ana', 'text': 'For eleven years. And I never noticed, because I was '
                                   '<span class="vocab-highlight">a creature of habit</span> and it '
                                   'had become <span class="vocab-highlight">second nature</span>.'},
            {'who': 'ingrid', 'text': 'That is the part nobody warns you about. You '
                                      '<span class="vocab-highlight">fall into a routine</span> and '
                                      'then it disappears. There used to be a bakery under my flat and '
                                      'I could not tell you the man&rsquo;s name.'},
            {'who': 'ana', 'text': 'I was <span class="vocab-highlight">a regular</span> in the same '
                                   'place for nine years and I never asked either. I '
                                   '<span class="vocab-highlight">took it completely for granted</span>.'},
            {'who': 'ingrid', 'text': 'And now? Do you ever <span class="vocab-highlight">look back on'
                                      '</span> it and want any of it?'},
            {'who': 'ana', 'text': 'No. I <span class="vocab-highlight">missed out on</span> eleven '
                                   'years of evenings in that car. It took me two hours every night to '
                                   '<span class="vocab-highlight">wind down</span> from a journey I do '
                                   'not remember making.'},
        ],
        'comp': [
            ('What does Ingrid say happens when people ask her what she misses about Oslo?',
             'She has to invent something. What she actually remembers is not what she misses but what '
             'she used to dread.'),
            ('What was Ingrid&rsquo;s Sunday evening like, and when did it start?',
             'Every Sunday she would start checking the calendar at about six, and the whole evening '
             'was ruined from then on.'),
            ('What example does Ingrid give of something disappearing inside a routine?',
             'There used to be a bakery under her flat and she could not tell you the man&rsquo;s '
             'name, after years of going there.'),
        ],
    },
    'listenings': [
        {'voice': 'british_m',
         'heading': 'The 07:14 <span class="accent">Every Single Day</span>',
         'intro': 'A Londoner on eleven years of the same train. Sound first &mdash; no text.',
         'text': "I used to get the seven fourteen. Not the seven twelve, not the seven twenty, the "
                 "seven fourteen, and I would stand at exactly the same point on the platform because "
                 "that is where the doors opened. Every morning. For eleven years. And the thing that "
                 "genuinely disturbs me now is that I cannot remember a single one of them. Not one. I "
                 "can remember the first week, because the first week I was watching everything, and I "
                 "can remember the last day because I knew it was the last day. Everything in between "
                 "has gone. I used to buy a coffee from the same man at the same kiosk and I never "
                 "asked his name in eleven years, which sounds appalling when I say it out loud. My "
                 "wife says I did not waste those years, I just was not there for them, and I think "
                 "that is the more accurate way of putting it. What I would say to anybody is this. If "
                 "you cannot remember last Tuesday, that is not a memory problem.",
         'comp': [
             ('What exactly was his routine, and how long did it last?',
              'He got the seven fourteen train &mdash; not the twelve, not the twenty &mdash; and '
              'stood at the same point on the platform where the doors opened. Every morning, for '
              'eleven years.'),
             ('Which parts of those eleven years can he remember, and why those?',
              'The first week, because he was watching everything, and the last day, because he knew '
              'it was the last. Everything in between has gone.'),
             ('How does his wife describe what happened, and what does he say about it?',
              'She says he did not waste those years, he just was not there for them &mdash; and he '
              'thinks that is the more accurate way of putting it.'),
         ]},
        {'voice': 'nordic_m',
         'heading': 'Breaking It Was <span class="accent">Harder Than Living It</span>',
         'intro': 'A Norwegian on the first six months after leaving. Sound first &mdash; no text.',
         'text': "Nobody prepared me for how tiring the first months would be, and I want to be "
                 "specific about why, because I think the reason is interesting. It was not the "
                 "boxes and it was not the paperwork. It was that every single small thing had to be "
                 "decided again. Where do I buy bread now. What time do I leave now. Which way do I "
                 "walk. In the old life I did all of that on autopilot and it cost me nothing, and "
                 "suddenly I was making forty small decisions before nine in the morning. I remember "
                 "sitting down at about week three and thinking, honestly, that I had made a terrible "
                 "mistake. I had not. What I had done was break about two hundred habits at once, and "
                 "a habit is expensive to break and free to keep. That is the whole thing in one "
                 "sentence. It took about six months and then the new life became invisible too, which "
                 "is either wonderful or terrifying depending on the day you ask me.",
         'comp': [
             ('What was tiring about the first months, and what was not?',
              'Not the boxes and not the paperwork. It was that every small thing had to be decided '
              'again: where to buy bread, what time to leave, which way to walk.'),
             ('What did he think at about week three, and was he right?',
              'That he had made a terrible mistake. He had not &mdash; he had broken about two hundred '
              'habits at once.'),
             ('What is his one-sentence explanation, and what happened after six months?',
              'A habit is expensive to break and free to keep. After about six months the new life '
              'became invisible too, which he says is either wonderful or terrifying depending on the '
              'day.'),
         ]},
    ],

    # ---------------------------------------------------------------- chapter 4
    'grammar': {
        'ch_heading': 'Two Forms, <span class="accent">One Rule Between Them</span>',
        'ch_sub': 'used to &middot; would &mdash; and the one place would cannot go',
        'heading': 'Three Are Habits. <span class="accent">One Is Not.</span>',
        'examples': [
            'I used to leave the flat at ten past seven, every single morning.',
            'Every Monday I would sit in the same traffic, listening to the same radio.',
            'There used to be a bakery on the corner. It closed years ago.',
            'I did not use to notice the noise at all. I notice it now.',
        ],
        'prompt': 'Three of these four describe something repeated. One describes a situation that was '
                  'simply true. Find it &mdash; and then try to say that one with <em>would</em>. It '
                  'will not go.',
        'table': [
            ('used to + verb', 'A habit or a state that was true then and is not now.',
             'I <strong>used to live</strong> in Sao Paulo.'),
            ('would + verb', 'A <strong>repeated action</strong>, inside a memory or a story.',
             'Every Monday I <strong>would take</strong> the seven fourteen.'),
            ('STATES take used to only', 'be, have, know, like, live: <strong>would</strong> is '
                                         'impossible here.',
             'There <strong>used to be</strong> a bakery. (never: there would be)'),
            ('negative', 'did not <strong>use</strong> to &mdash; the d moves to did.',
             'I <strong>did not use to</strong> notice it.'),
            ('question', 'did you <strong>use</strong> to...?',
             '<strong>Did you use to</strong> walk to work?'),
            ('one finished event', 'A single event takes the past simple. Never used to.',
             'I <strong>moved</strong> in March. (never: I used to move)'),
            ('not the same as be used to', 'be / get used to + -ing is a different structure entirely.',
             "I <strong>am used to</strong> the quiet now &mdash; that is next week's lesson."),
        ],
        'oneliner': 'used to opens the door; would keeps the memory going once you are inside.',
    },
    'mistakes': [
        ('I use to live in Sao Paulo.', 'I used to live in Sao Paulo.'),
        ('I did not used to notice the noise.', 'I did not use to notice the noise.'),
        ('There would be a bakery on the corner.', 'There used to be a bakery on the corner.'),
        ('I used to move to the interior in March.', 'I moved to the interior in March.'),
    ],
    'mistake_note': 'The first two are the same <strong>d</strong>, in the wrong place: it belongs to '
                    '<em>used</em> in the affirmative and to <em>did</em> in the negative, never to '
                    'both. The third breaks the state rule &mdash; <em>be</em> never takes '
                    '<em>would</em>. The fourth is the commonest of all: <strong>one finished event '
                    'is past simple</strong>, no matter how important it was.',
    'gpractice_heading': 'Used To, Would, <span class="accent">or Neither?</span>',
    'gpractice': [
        {'before': 'I ', 'answer': 'used to live', 'after': ' in Sao Paulo for eleven years.',
         'cue': 'live &mdash; a state, not a repeated action'},
        {'before': 'Every Monday I ', 'answer': 'would take', 'after': ' the seven fourteen.',
         'cue': 'take &mdash; repeated action inside a memory'},
        {'before': 'There ', 'answer': 'used to be', 'after': ' a bakery on the corner.',
         'cue': 'be &mdash; careful, only one form works here'},
        {'before': 'I ', 'answer': 'did not use to notice', 'after': ' the noise at all.',
         'cue': 'not / notice &mdash; watch where the d goes'},
        {'before': 'I ', 'answer': 'moved', 'after': ' to the interior in March 2024.',
         'cue': 'move &mdash; one finished event with a date'},
    ],
    'artifact': {
        'heading': 'The Old <span class="accent">Weekday</span>',
        'doc_title': 'WEEKDAY &mdash; A. VERALDI',
        'doc_sub': 'Sao Paulo &middot; unchanged 2013 to 2024',
        'doc_right': 'Repeated<br>x 2,600',
        'rows': [
            ('05:50', 'alarm. Same one. Snoozed twice, every day, for eleven years'),
            ('07:10', 'leave the flat, same lift, same doorman, no conversation'),
            ('07:40', 'same avenue, same radio station, no memory of any of it'),
            ('08:40', 'coffee, same kiosk, same man, name never asked'),
            ('19:20', 'leave the office. Traffic again. Two hours to wind down afterwards'),
            ('Sunday 18:00', 'open the calendar. Evening over.'),
        ],
        'comp': [
            ('Say the 05:50 line as a full sentence, twice: once with used to and once with would.',
             '"I used to snooze the same alarm twice every morning." / "Every morning I would snooze '
             'it twice." Both work, because snoozing is a repeated action.'),
            ('Now say the 08:40 line with would, and then say what was really wrong with that.',
             '"Every morning I would buy a coffee from the same man." That is fine. But "I would never '
             'ask his name" is odd &mdash; a negative habit is much more natural with used to: "I '
             'never used to ask his name."'),
            ('The last line says the evening was over. Say it with used to, and explain why would '
             'would be strange.',
             '"Sunday evenings used to be ruined by six o&rsquo;clock." Would is impossible with '
             '<em>be</em>: it is a state, not an action, and states only take used to.'),
        ],
    },

    # ---------------------------------------------------------------- chapter 5
    'detective': [
        ('I use to live in Sao Paulo.', 'I used to live in Sao Paulo.'),
        ('I did not used to notice the noise.', 'I did not use to notice the noise.'),
        ('There would be a bakery on the corner.', 'There used to be a bakery on the corner.'),
        ('I used to move to the interior in March.', 'I moved to the interior in March.'),
    ],
    'quickfire': [
        {'situation': 'Somebody asks what your mornings were like in the city. Describe the routine, '
                      'not one particular morning.',
         'tips': ['I used to leave at ten past seven, every single day.',
                  'Every morning I would sit in the same traffic on the same avenue.']},
        {'situation': 'Somebody asks what has changed since you left. Give one thing that used to be '
                      'true and is not any more.',
         'tips': ['I used to dread Sunday evenings. I do not any more.',
                  'Use used to for the state, and the present simple for now.']},
        {'situation': 'Somebody asks when you moved. Careful &mdash; this one is a trap.',
         'tips': ['I moved in March 2024.',
                  'One finished event. Used to is impossible here, however big the event was.']},
        {'situation': 'A colleague says she is exhausted three weeks after moving and thinks she made a '
                      'mistake. Answer with what you know, not with encouragement.',
         'tips': ['That is two hundred habits breaking at once, not a mistake.',
                  'It took me about six months, and I would say the same thing to anybody.']},
        {'situation': 'Describe one thing that was completely automatic for you back then and is gone now.',
         'tips': ['That whole drive was second nature. I did it on autopilot for years.',
                  'I could not tell you a single thing about any of those mornings.']},
        {'situation': 'Somebody asks whether you miss the city. Answer honestly and precisely, without '
                      'either nostalgia or contempt.',
         'tips': ['I miss about four things and I do not miss the other eleven years.',
                  'Name the four. Vague answers here sound like you are hiding a regret.']},
    ],
    'speaking': [
        ('What did you use to do every single weekday, for years?',
         'I used to leave the flat at ten past seven and sit in the same traffic on the same avenue.'),
        ('What would happen every Sunday evening?',
         'I would open the calendar at about six, and after that the evening was over.'),
        ('What used to be on your street that is not there any more?',
         'There used to be a bakery on the corner. It closed while I was still living there and I '
         'barely noticed.'),
        ('What did you not use to notice back then, that you notice now?',
         'The noise. I did not use to hear it at all, and now two minutes of it exhausts me.'),
    ],
    'build': [
        ('I / live in Sao Paulo + eleven years (a state that is over)',
         'I used to live in Sao Paulo for eleven years.'),
        ('every Monday / I / take the seven fourteen (a repeated action in a memory)',
         'Every Monday I would take the seven fourteen.'),
        ('there / be a bakery on the corner (a state -- careful with the form)',
         'There used to be a bakery on the corner.'),
        ('I / not / notice the noise (negative -- watch where the d goes)',
         'I did not use to notice the noise.'),
    ],
    'answerkey_heading': 'Used To and Would on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole habit key',
    'answerkey': [
        'used to + verb = a habit OR a state that was true then and is not now: I used to live there',
        'would + verb = a repeated ACTION inside a memory: every Monday I would take the seven fourteen',
        'STATES (be, have, know, like, live) take used to ONLY: there used to be a bakery',
        'negative = did not USE to (the d moves to did): I did not use to notice it',
        'question = did you USE to...? : did you use to walk to work?',
        'one finished event = past simple, never used to: I moved in March',
        'be / get used to + -ing is a DIFFERENT structure (next lesson): I am used to the quiet now',
        'NEVER: I use to live &middot; I did not used to &middot; there would be a bakery &middot; '
        'I used to move in March',
    ],

    # ---------------------------------------------------------------- chapter 6
    'rp_ch_heading': 'The Person You <span class="accent">Used to Be</span>',
    'roleplay': {
        'guided': {
            'heading': 'The Colleague Who <span class="accent">Never Left</span>',
            'scenario': 'I still live in the city and I have never understood why anybody would leave. '
                        'I ask you three things: what your weekdays used to be like, what you would do '
                        'every Sunday evening, and what you did not use to notice back then. Answer '
                        'each in two sentences.',
            'chips': ['I used to', 'every Monday I would', 'I did not use to'],
        },
        'semi': {
            'heading': 'Ingrid Cannot Remember <span class="accent">Four Years</span>',
            'scenario': 'I am Ingrid, and I have just told you that I cannot remember four years of '
                        'Oslo mornings and it frightens me. Ask me two questions about that period '
                        'before you say anything about your own &mdash; then tell me what you found '
                        'when you looked back at yours.',
            'chips': ['on autopilot', 'a creature of habit', 'took it for granted'],
        },
        'free': {
            'heading': 'Two Minutes of <span class="accent">an Ordinary Tuesday</span>',
            'scenario': 'Describe one completely ordinary weekday from the life you no longer live, '
                        'from the alarm to the moment you finally wound down. Use used to for the '
                        'states and would for the repeated actions, and finish with the one thing from '
                        'it that you would genuinely take back.',
        },
    },

    # ---------------------------------------------------------------- chapter 7
    'wrap_heading': 'The Tense for <span class="accent">Who You Were</span>',
    'survival_heading': 'Five Phrases for <span class="accent">the Life Before</span>',
    'survival': [
        'I used to live in Sao Paulo for about eleven years.',
        'Every Monday I would sit in the same traffic on the same avenue.',
        'There used to be a bakery on the corner and I never learnt his name.',
        'I did not use to notice the noise at all.',
        'I did that whole journey on autopilot, five days a week.',
    ],
    'checklist': [
        'I use used to for habits and for states that are over.',
        'I use would only for repeated actions, never with be, have or know.',
        'I say did not use to, without the d, in the negative.',
        'I use the past simple for one finished event, however important it was.',
        'I know the words: a creature of habit, second nature, on autopilot, back then, to dread.',
    ],
    'closing': {
        'badge': 'The Life Before Badge <span class="accent">Earned!</span>',
        'text': 'You just described eleven years of mornings to a Norwegian, Ana, in a tense that '
                'exists in English for exactly one purpose: the person you no longer are.',
        'next': 'Getting Used to the Quiet',
    },

    # ---------------------------------------------------------------- pre-class
    'pc_title': 'I Used to Live in the City -- The Habits That Stayed Behind',
    'pc_desc': 'The routine of the life before, and the two forms English keeps for it. Key words: to '
               'take something for granted, a creature of habit, to fall into a routine, second '
               'nature, on autopilot, to break a habit, back then, to miss out on something, a '
               'regular, to wind down, to dread, to look back on something. Structure: used to and '
               'would for past habits.',
    'pc_context': {
        'paras': [
            'Ana <strong>used to live</strong> in Sao Paulo, and for eleven years her weekdays never '
            'changed. She <strong>would leave</strong> the flat at ten past seven, she '
            '<strong>would sit</strong> in the same traffic on the same avenue, and she '
            '<strong>would buy</strong> a coffee from the same man at the same kiosk. She never asked '
            'his name.',
            'There <strong>used to be</strong> a bakery on her corner, and it closed while she was '
            'still living there. She barely noticed, because by then the whole journey was '
            '<strong>second nature</strong> and she did it <strong>on autopilot</strong>. She was '
            '<strong>a creature of habit</strong> who had <strong>fallen into a routine</strong> she '
            'never chose, and she <strong>took every part of it for granted</strong>.',
            'She <strong>did not use to notice</strong> the noise. She <strong>used to dread</strong> '
            'Sunday evenings more than Monday mornings, and it took two hours to '
            '<strong>wind down</strong> after every commute. She <strong>moved</strong> to the '
            'interior in March 2024. When she <strong>looks back on</strong> those years now, what '
            'she mostly remembers is being tired.',
        ],
        'quiz': [
            {'q': 'Why "used to live" and not "would live" in the first line?',
             'opts': [('Because live is a state, and states only take used to.', True),
                      ('Because used to is more formal than would.', False),
                      ('Because would is only used in questions.', False)]},
            {'q': '"She would leave the flat at ten past seven." What does would tell you here?',
             'opts': [('That she left once and it was memorable.', False),
                      ('That it was a repeated action, part of a remembered routine.', True),
                      ('That she was planning to leave but did not.', False)]},
            {'q': 'Why "She moved to the interior in March 2024" and not "she used to move"?',
             'opts': [('Because it is one finished event with a date, which always takes past simple.', True),
                      ('Because moving is a state and states never take used to.', False),
                      ('Because the sentence is in the third person.', False)]},
        ],
    },
    'pc_tip': {
        'title': 'Used To and Would',
        'lead': 'Portuguese does this with one tense. English built two structures and a rule between them.',
        'table': [
            ('used to + verb', 'A habit or a state that was true then and is not now',
             'I <strong>used to live</strong> in Sao Paulo.'),
            ('would + verb', 'A repeated action, inside a memory',
             'Every Monday I <strong>would take</strong> the same train.'),
            ('states take used to only', 'be, have, know, like, live &mdash; would is impossible',
             'There <strong>used to be</strong> a bakery.'),
            ('negative', 'did not <strong>use</strong> to &mdash; the d moves to did',
             'I <strong>did not use to</strong> notice it.'),
            ('question', 'did you <strong>use</strong> to...?',
             '<strong>Did you use to</strong> walk to work?'),
            ('one finished event', 'Past simple. Never used to.',
             'I <strong>moved</strong> in March.'),
            ('not be used to', 'be / get used to + -ing is a different structure',
             'I <strong>am used to</strong> the quiet now.'),
        ],
        'never': 'I use to live &middot; I did not used to notice &middot; there would be a bakery '
                 '&middot; I used to move in March. Two of those put the d in the wrong place, one '
                 'breaks the state rule, and one turns a single event into a habit.',
    },
    'pc_blanks': [
        {'before': 'I ', 'answer': 'used to live', 'after': ' in Sao Paulo for eleven years.',
         'hint': 'Hint: live -- a state that was true then and is not now, three words'},
        {'before': 'Every Monday I ', 'answer': 'would take', 'after': ' the seven fourteen train.',
         'hint': 'Hint: take -- a repeated action inside a memory, two words'},
        {'before': 'There ', 'answer': 'used to be', 'after': ' a bakery on the corner.',
         'hint': 'Hint: be -- careful, only one of the two forms works with this verb'},
        {'before': 'I ', 'answer': 'did not use to notice', 'after': ' the noise at all.',
         'hint': 'Hint: not / notice -- watch where the d goes in the negative'},
        {'before': 'I ', 'answer': 'moved', 'after': ' to the interior in March 2024.',
         'hint': 'Hint: move -- one finished event with a date'},
        {'before': 'I did that whole journey ', 'answer': 'on autopilot',
         'after': ', five days a week, for eleven years.',
         'hint': 'Hint: two words -- doing something without any attention, from repetition'},
    ],
    'pc_order_lead': 'Ingrid and Ana compare the lives they left. Put the exchange in a logical order.',
    'pc_order': [
        'People keep asking me what I miss, and honestly I have to invent something.',
        'What do you actually remember, then?',
        'What I used to dread. Every Sunday I would open the calendar at six and the evening was over.',
        'I had exactly the same thing, for eleven years, and I never noticed it.',
        'There used to be a bakery under my flat and I could not tell you the man&rsquo;s name.',
        'Nor could I. I took the whole thing completely for granted.',
    ],
    'order_voice': 'arthur',
    'pc_squiz': [
        {'q': 'A colleague asks what your weekdays were like in the city. You answer:',
         'opts': [('"I used to leave at ten past seven and I would sit in the same traffic."', True),
                  ('"I use to leave at ten past seven and I was sitting in the same traffic."', False),
                  ('"I would be leaving at ten past seven every day."', False)]},
        {'q': 'You want to say a bakery existed on your corner and does not now. The natural version is:',
         'opts': [('"There would be a bakery on the corner."', False),
                  ('"There used to be a bakery on the corner."', True),
                  ('"There was being a bakery on the corner."', False)]},
        {'q': 'Somebody asks when you moved. The correct answer is:',
         'opts': [('"I used to move in March 2024."', False),
                  ('"I moved in March 2024."', True),
                  ('"I would move in March 2024."', False)]},
        {'q': 'You want to say you never noticed the noise back then. The correct negative is:',
         'opts': [('"I did not use to notice the noise."', True),
                  ('"I did not used to notice the noise."', False),
                  ('"I use not to notice the noise."', False)]},
    ],
    'pc_think': 'Describe one completely ordinary weekday from a period of your life that is over. Use '
                'used to at least three times for the states, would at least three times for the '
                'repeated actions, and finish with the past simple for the one event that ended it.',

    # ------------------------------------------------------------ complementares
    'media': [
        {'id': 'series', 'thumb': 'doc', 'type': 'Documentary',
         'title': 'Italy tackles rural exodus &mdash; DW Documentary (full film, 28 min)',
         'desc': 'Whole villages standing empty while the cities fill up, and the people going the '
                 'other way on purpose. Almost nobody in the film is a native speaker of English, '
                 'which is precisely the point: this is the English you actually meet.',
         'tip': 'Tip: listen for used to and would in the interviews. Everybody describing a village '
                'that emptied is describing a life that is over, and the grammar follows automatically.',
         'url': 'https://www.youtube.com/watch?v=b8F1jp05vsA', 'cta': 'Watch on YouTube'},
        {'id': 'podcast', 'thumb': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; Creatures of Habit',
         'desc': 'A psychologist who has spent her career on habits explains why about forty percent '
                 'of what you did today was not decided by you. The episode is the scientific version '
                 'of the text you read in class.',
         'tip': 'Tip: the host speaks slowly and the guest does not. Listen to five minutes of the '
                'guest with no transcript, then use the free transcript on the page to check.',
         'url': 'https://www.hiddenbrain.org/podcast/creatures-of-habit/',
         'cta': 'Listen on Hidden Brain'},
        {'id': 'youtube', 'thumb': 'video', 'type': 'Talk',
         'title': 'Try something new for 30 days &mdash; Matt Cutts, TED (3 min)',
         'desc': 'Three minutes on what happens when you deliberately break a routine for a month. '
                 'Short, fast, American, and the exact opposite of the eleven years you spent on '
                 'autopilot.',
         'tip': 'Tip: it is only three minutes, so watch it three times. First for the idea, then for '
                'the reductions from lesson 9, then just to enjoy it.',
         'url': 'https://www.ted.com/talks/matt_cutts_try_something_new_for_30_days',
         'cta': 'Watch on TED'},
    ],

    # ------------------------------------------------------------------ teacher
    'teacher': {
        'open': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: '
                '"Tonight, the person you used to be." O recorte: as aulas 1 e 2 falaram do lugar; '
                'esta fala do TEMPO. Ingles tem duas estruturas dedicadas a vida que acabou, e o '
                'portugues resolve tudo com o imperfeito &mdash; e exatamente por isso ela nunca '
                'precisou escolher.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 9: ela decodificou um '
                  'americano em velocidade real. PONTE (REGRA 27B): "You can hear the fast version now. '
                  'Tonight you tell the slow one -- your own." A pergunta e deliberadamente PRECISA '
                  '(um quarto para as sete): pergunta vaga sobre rotina produz resposta vaga. ZERO '
                  'correcao aqui.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase de baixo importa: '
                   'em portugues o imperfeito faz tudo e ela nunca teve de escolher. Aqui ha DUAS '
                   'formas e uma regra entre elas. Nao de a regra ainda.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> A primeira pergunta ("o que voce sente '
                'falta") e a facil e ela ja respondeu mil vezes. Segure e faca a segunda: o que ela '
                'fez todo dia por anos e nunca mais pensou. Se ela nao lembrar, e exatamente o ponto '
                'do texto do capitulo 3 &mdash; guarde a resposta dela para voltar la.',
        'tr_vocab': '<strong>Transicao vocab (1 min):</strong> Diga: "Twelve words for a routine. Click '
                    'each card to reveal." Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ "to '
                  'take for granted": "Is it a bad thing? (Nem sempre &mdash; e so o que acontece '
                  'quando algo bom vira paisagem.)" CCQ "second nature": "Am I good at it, or do I not '
                  'think about it? (Nao penso &mdash; e sobre automatismo, nao sobre talento.)" CCQ "on '
                  'autopilot": "Was I paying attention? (Zero.)" Peca um exemplo da vida de Sao Paulo '
                  'dela em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ "back then": "Is it '
                  'formal? (Nao, e conversa &mdash; e a forma mais natural de dizer naquela epoca.)" '
                  'CCQ "a regular": "Do they know my name? (Conhecem meu rosto. Talvez nao o nome '
                  '&mdash; e essa a ironia do dialogo.)" CCQ "to dread": "Is it worry, or fear? (E medo '
                  'real, e e sobre o que ainda vai acontecer.)"',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. '
                    'Certo fica verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note '
                    'como ponte para o texto: creature of habit e second nature sao os dois lados da '
                    'mesma coisa.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> "On autopilot" &mdash; o stress cai em '
                'AU, e o T final quase some. "To dread" &mdash; DRED, rima com bed, o EA nao e /i/. "A '
                'creature of habit" &mdash; CREE-cher, o T vira /tʃ/. Na frase inteira, "used to" cola '
                'e vira /YOOS-tu/, com S surdo, NUNCA /yoozd tu/. Esse ultimo ponto e o mais util da '
                'noite: e assim que se ouve used to em fala rapida.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a expressao que '
                   'falta ANTES de clicar. As candidatas estao no banco embaixo, fora de ordem. Se '
                   'travar, aponte duas e pergunte qual cabe. Clicar de novo fecha (REGRA 27E).',
        'tr_ch3': '<strong>Transicao (1 min):</strong> Diga: "A short text about what a routine costs. '
                  'Read for the main idea &mdash; do not stop at every word." Passe ao proximo.',
        'reading': '<strong>Leitura + Gist (6 min):</strong> De 3 minutos de leitura silenciosa. Depois '
                   'a pergunta de gist. Ana clica e o card certo fica verde. NAO peca traducao palavra '
                   'a palavra. O paragrafo 4 e o mais importante para ELA: o cansaco dos primeiros '
                   'meses nao e sinal de erro, e o som de uma rotina quebrando. Se ela reagir a isso, '
                   'pare e converse.',
        'tf': '<strong>True / False (4 min):</strong> Ana decide ANTES de clicar. Ao clicar, veredito e '
              'justificativa aparecem. Peca que ela aponte a linha do texto que prova cada resposta. A '
              '5a e a que vale a aula.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e a Ingrid, NORDICA, que saiu de Oslo ha '
                    'quatro anos. Clique "Next Line" e toque o audio de cada fala. Para cada fala da '
                    'Ana, peca que ELA fale primeiro. PRAGMATICA: repare que a Ingrid admite logo de '
                    'cara que INVENTA uma resposta quando perguntam do que sente falta &mdash; '
                    'honestidade desconfortavel e direta e muito nordica, e desarma a conversa social '
                    'em vez de aliment&aacute;-la. Comente no fim.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre a INGRID, nao sobre a '
                         'Ana (REGRA 27F). Ana responde ANTES de revelar. Na 2a, repare que a resposta '
                         'usa <em>would</em> naturalmente &mdash; e a primeira vez que a forma aparece '
                         'sem regra nenhuma, de proposito.',
        'listen1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES '
                   'de tocar. Este e um BRITANICO: vogais longas, T bem marcado, R final que some. '
                   'Avise ANTES. Ele usa <em>used to</em> e <em>would</em> alternadamente a aula '
                   'inteira &mdash; depois das perguntas, peca que ela cace UM exemplo de cada.',
        'tr_grammar': '<strong>Transicao gramatica (1 min):</strong> Diga: "Four sentences. Three of '
                      'them repeat. One of them simply was." Passe ao proximo.',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Peca que ela ache a frase que NAO e '
                   'acao repetida ("there used to be a bakery"). Depois peca que ela tente dizer essa '
                   'com <em>would</em> &mdash; ela vai sentir que nao vai, e esse desconforto e a '
                   'regra. So entao clique "Reveal the Rule". CCQ: "I used to live there &mdash; do I '
                   'live there now? (Nao. Used to sempre implica que acabou.)" "Every Monday I would '
                   'take the train &mdash; one Monday or many? (Muitas.)" NAO de a regra antes.',
        'mistake': '<strong>Common mistake (4 min):</strong> Os dois primeiros sao o mesmo D no lugar '
                   'errado: pertence a <em>used</em> no afirmativo e a <em>did</em> no negativo, nunca '
                   'aos dois. O terceiro quebra a regra dos estados. O quarto e o mais comum de todos '
                   'e o mais dificil de tirar: um evento unico e past simple, por mais importante que '
                   'seja. Peca 2 repeticoes das versoes certas.',
        'gpractice': '<strong>Practice (4 min):</strong> Ana escolhe ORALMENTE antes de clicar. Se '
                     'travar, faca a pergunta-chave: "Is it repeated, is it a state, or did it happen '
                     'once?" As tres respostas dao tres formas diferentes.',
        'listen2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA ANTES de tocar. '
                   'Este e um NORUEGUES: melodia que sobe e desce muito, W que tende a V, consoantes '
                   'finais claras. Avise ANTES. Este audio existe por um motivo pedagogico especifico: '
                   'a Ana tambem passou por uma mudanca radical, e este homem descreve o cansaco da '
                   'semana tres como PREVISIVEL, nao como fracasso. Deixe pousar antes de passar.',
        'artifact': '<strong>Artefato (5 min):</strong> E o dia util antigo dela, escrito como agenda. '
                    'Peca que ela transforme CADA linha em frase completa, escolhendo entre used to e '
                    'would. So depois as 3 perguntas. Este e o melhor termometro da aula &mdash; a '
                    'ultima linha (Sunday 18:00) e a armadilha: e estado, entao so used to serve.',
        'tr_practice': '<strong>Transicao practice (1 min):</strong> Diga: "Now we train: detective, '
                       'quick fire, and building." Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. "What is wrong '
                     'here?" Ana corrige ANTES de clicar. Sao os quatro do slide de Common Mistake.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez, resposta em voz alta '
                     'ANTES das Tips. A 3a e armadilha proposital (evento unico = past simple) &mdash; '
                     'se ela cair, e o erro que voce vai caçar no role-play 3.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. '
                    'Exija a forma certa em cada uma: a 1a pede used to ou would, a 2a pede would, a 3a '
                    'pede used to (estado) e a 4a pede o negativo sem o d. Se ela errar o negativo, '
                    'devolva a pergunta em vez de corrigir.',
        'build': '<strong>Sentence Building (4 min):</strong> Ana monta a frase COMPLETA em voz alta, '
                 'depois clica para comparar. Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO depois que '
                     'ela tentou tudo. A penultima linha e um SPOILER proposital da aula 11 (be/get '
                     'used to) &mdash; deixe ela ver que a confusao entre as duas ja tem data marcada.',
        'tr_roleplay': '<strong>Transicao role-play (1 min):</strong> Diga: "Now you tell somebody about '
                       'the person you used to be. Three steps, and the last one has no help."',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e um colega que nunca saiu da cidade e '
               'genuinamente nao entende por que alguem sairia. Registro curioso, nao hostil. Faca as '
               'tres perguntas na ordem. Corrija SO a escolha entre used to / would / past simple.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e a Ingrid, assustada por nao lembrar '
               'de quatro anos. Ana precisa PERGUNTAR antes de falar de si. Se ela comecar por si '
               'mesma, interrompa e peca de novo: "Ask me about mine first."',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO '
               'corrija durante. CONTE quantos <em>used to</em> e quantos <em>would</em> ela usa, e se '
               'ela acerta o past simple no evento final. Diga os numeros no fim. Meta: pelo menos tres '
               'de cada.',
        'tr_wrap': '<strong>Transicao wrap-up (1 min):</strong> Diga: "You just described eleven years '
                   'of mornings in a tense that exists for exactly one purpose."',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a '
                    'Ana repita. As cinco cobrem: used to com estado, would com acao repetida, used to '
                    'be, o negativo sem d, e uma frase so de vocabulario. Insista no /YOOS-tu/.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: "Click each item if you feel confident." '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 10 registrada como '
                     'concluida no passaporte.',
        'closing': '<strong>Encerramento (2 min):</strong> Diga: "Ten lessons in, Ana. A quarter of the '
                   'programme, and tonight you had a tense that Portuguese does not make you choose." '
                   'Homework (oralmente, opcional): gravar dois minutos descrevendo uma terca-feira '
                   'qualquer da vida antiga, e contar na propria gravacao quantos used to e quantos '
                   'would apareceram. Proxima aula: Getting Used to the Quiet &mdash; be used to e get '
                   'used to, que sao OUTRA estrutura, e a confusao mais comum que existe com a de hoje.',
    },
}
