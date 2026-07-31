# -*- coding: utf-8 -*-
"""Aula 12 -- If I Have Time This Weekend (first conditional).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false, alem do dialogo.
Sotaques do listening (CURRICULO V3): alemao + australiano.
Callback da aula 11: ela descreveu um ano inteiro de adaptacao. Hoje o assunto sai do
passado e vai para o fim de semana que ainda nao aconteceu -- e para a estrutura que a
propria aluna nomeou como o buraco dela: "o condicional nao entra na minha cabeca".
"""

LESSON = {
    'n': 12,
    'model': 'reading',
    'menu_title': 'If I Have Time This Weekend',
    'menu_desc': 'The Saturday that depends on the sky, the delivery and the dogs -- and the first '
                 'of the four conditionals she has been avoiding for years',
    'grammar_point': 'first conditional for real future possibilities',
    'chapter_tag': 'The Weekend Ahead',
    'title_html': 'If I Have Time <span class="accent">This Weekend</span>',
    'title_sub': 'Every plan you make out here has a condition attached. English puts it in one sentence.',
    'phases': ['First Words', 'The Words of Planning', 'The Weekend You Planned',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1519692933481-e162a57d6721?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1416339306562-f3d12fefd36f?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1519692933481-e162a57d6721?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Saturday Has Not <span class="accent">Happened Yet</span>',
        'callback': 'Last time you described a whole year of adapting, and you separated three structures that '
                    'most people never separate at all: used to, be used to and get used to.',
        'question': 'What is the one job in that house you have moved from weekend to weekend for months?',
    },
    'framing': {
        'heading': 'The Structure That <span class="accent">Never Sticks</span>',
        'steps': [('The Words', 'weather permitting, to put off, to squeeze in, daunting...'),
                  ('The Weekend', 'a text on why the Saturday you planned never happens'),
                  ('The Code', 'if, unless, as long as &mdash; and the one word that must never appear')],
        'note': 'You said it yourself in the consultation: <em>the conditionals never stick.</em> There are four of '
                'them and tonight is the first, which is also the only one that describes something that might '
                '<strong>actually happen this Saturday</strong>. Everything after this is built on it.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'How Many Jobs Are <span class="accent">On That List?</span>',
        'line1': 'People restoring a house do not have a to-do list. They have a list of things that depend on '
                 'other things: the weather, a delivery, a tool, an hour of daylight.',
        'line2': 'So the honest question is not what you will do on Saturday. It is: what has to be true first?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'The Language of <span class="accent">a Plan With Conditions</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'To put something off', 'icon': 'calendar',
         'def': 'To move something to a later date, usually because you do not want to do it',
         'ex': 'I have put the shutters off for four weekends in a row.',
         'match': 'to move something to a later date, usually to avoid it'},
        {'word': 'A downpour', 'icon': 'cloud',
         'def': 'A sudden fall of very heavy rain that does not last long',
         'ex': 'There was a downpour at eleven and the whole plan collapsed.',
         'match': 'a sudden fall of very heavy rain, usually short'},
        {'word': 'To bother', 'icon': 'help',
         'def': 'To make the effort to do something &mdash; most often used in the negative',
         'ex': 'If it is raining at eight I will not even bother getting the ladder out.',
         'match': 'to make the effort to do something, usually in the negative'},
        {'word': 'Weather permitting', 'icon': 'sun', 'expr': True,
         'def': 'Only if the weather allows it &mdash; said at the end of a plan',
         'ex': 'We are painting the veranda on Sunday, weather permitting.',
         'match': 'only if the weather allows it, said at the end of a plan'},
        {'word': 'To squeeze something in', 'icon': 'clock', 'expr': True,
         'def': 'To find time for something in a schedule that is already full',
         'ex': 'If the delivery comes early I might squeeze the market in as well.',
         'match': 'to find time for something in an already full schedule'},
        {'word': 'To run errands', 'icon': 'map',
         'def': 'To do the small necessary jobs outside the house: post, bank, shop',
         'ex': 'Out here, running errands means one trip or none.',
         'match': 'to do small necessary jobs outside the house'},
        {'word': 'Provided that', 'icon': 'shield',
         'def': 'Only if this one condition is true &mdash; more explicit than plain if',
         'ex': 'I will finish the kitchen this weekend, provided that the tiles arrive.',
         'match': 'only if this one condition is true; stronger than plain if'},
        {'word': 'To call something off', 'icon': 'alert',
         'def': 'To cancel something that had already been arranged',
         'ex': 'If the forecast is that bad on Friday I will call the whole thing off.',
         'match': 'to cancel something that had already been arranged'},
        {'word': 'Daunting', 'icon': 'target',
         'def': 'Making you slightly afraid to start, because it is large or difficult',
         'ex': 'A whole wall of sanding is daunting until you divide it into three days.',
         'match': 'making you slightly afraid to start, being large or difficult'},
        {'word': 'A window', 'icon': 'eye',
         'def': 'A short period of time in which something is possible',
         'ex': 'There is a dry window on Saturday morning and nothing after that.',
         'match': 'a short period of time in which something is possible'},
        {'word': 'To hold off', 'icon': 'lock',
         'def': 'To not start yet &mdash; used about rain, and about a decision',
         'ex': 'If the rain holds off until noon I can get the first coat on.',
         'match': 'to not start yet; used about rain and about decisions'},
        {'word': 'Manageable', 'icon': 'scale',
         'def': 'Small enough or simple enough that you can actually deal with it',
         'ex': 'Two hours of sanding is manageable. Eight hours is a fantasy.',
         'match': 'small enough or simple enough that you can deal with it'},
    ],
    'vocabnote': 'Two of tonight&rsquo;s twelve are whole expressions: <strong>weather permitting</strong> and '
                 '<strong>to squeeze something in</strong>. Both of them are conditions in disguise. '
                 '<em>Weather permitting</em> is a complete if-clause folded into two words, and you can hear it at '
                 'the end of almost any English plan made outdoors.',
    'pron': [
        'A downpour',
        'Daunting',
        'Weather permitting',
        'If the rain holds off until noon, I will get the first coat on.',
    ],
    'gapfill': [
        ('"There was ', 'a downpour', ' at eleven and the whole plan collapsed."'),
        ('"We are painting the veranda on Sunday, ', 'weather permitting', '."'),
        ('"A whole wall of sanding is ', 'daunting', ' until you divide it into three days."'),
        ('"There is a dry ', 'window', ' on Saturday morning and nothing after that."'),
        ('"Two hours of sanding is ', 'manageable', '. Eight hours is a fantasy."'),
        ('"If it is raining at eight I will not even ', 'bother', ' getting the ladder out."'),
    ],

    # ------------------------------------------------------------ chapter 3
    'ch3': {
        'heading': 'The Weekend You Planned <span class="accent">and the One You Had</span>',
        'sub': 'Read for the main idea, then a German and an Australian who plan very differently',
    },
    'reading': {
        'heading': 'Why Saturday <span class="accent">Never Fits</span>',
        'rtitle': 'The Weekend You Planned and the Weekend You Had',
        'paras': [
            'Ask anybody on a Thursday what they are doing at the weekend and you will get a list. Ask the same '
            'person on the following Monday what they actually did and you will get about a third of that list, '
            'usually with an apology attached. This gap is so reliable that psychologists gave it a name in the '
            'nineteen seventies, and forty years of research has failed to make anybody any better at it.',
            'The reason is not laziness and it is not bad character. It is that when we plan, we imagine the job '
            'itself and nothing else. We picture the sanding. We do not picture the twenty minutes of finding the '
            'sandpaper, the trip to the shop because the grade is wrong, the phone call in the middle, or the fact '
            'that it might simply rain. Every one of those is a condition, and the plan quietly assumes that all of '
            'them will go the right way at once.',
            'People who restore old houses learn this faster than most, because their conditions are physical and '
            'they are visible from the window. You cannot paint wet wood. You cannot lay a floor that has not been '
            'delivered. The result is that anybody who has spent a year on a house starts speaking in a very '
            'particular way: almost nothing is announced flatly, and almost everything arrives with the condition '
            'attached to the end of it, out loud.',
            'That habit turns out to be a good one, and not only for houses. A plan with the condition stated is a '
            'plan that survives contact with a Saturday. A plan without it is a wish, and by Monday it will have '
            'become an apology.',
        ],
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist_choices': [
            ('People who make weekend plans are usually lazy about carrying them out', False),
            ('We plan the job and forget the conditions around it &mdash; and saying the condition out loud is what makes a plan survive', True),
            ('Restoring an old house is far more difficult than most people realise', False),
        ],
        'tf': [
            ('The gap between the planned weekend and the real one is a recent discovery.', 'f',
             'Psychologists named it in the nineteen seventies, and forty years of research has not made anybody better at it.'),
            ('The text says the main cause is laziness.', 'f',
             'It says explicitly that it is not laziness and not bad character &mdash; it is that we imagine the job itself and nothing else.'),
            ('When we plan, we tend to picture the job but not the twenty minutes of looking for the sandpaper.', 't',
             'That is the central claim: every small obstacle is a condition, and the plan assumes all of them go the right way at once.'),
            ('According to the text, people restoring houses learn this slowly.', 'f',
             'They learn it faster than most, because their conditions are physical and visible from the window.'),
            ('The text says a plan with the condition stated out loud is more likely to survive.', 't',
             'A plan with the condition survives contact with a Saturday; a plan without it is a wish that becomes an apology.'),
        ],
    },
    'dialogue': {
        'heading': 'Dave Has Never <span class="accent">Called Anything Off</span>',
        'guest_name': 'Dave',
        'guest_key': 'dave',
        'guest_voice': 'australian_m',
        'lines': [
            ('dave', 'So are you doing the veranda on Saturday or not? You have <span class="vocab-highlight">put it off</span> three times now.'),
            ('ana', 'If the rain <span class="vocab-highlight">holds off</span> until noon, I will get the first coat on.'),
            ('dave', 'And if it does not?'),
            ('ana', 'Then I will not even <span class="vocab-highlight">bother</span> getting the ladder out. Wet wood takes nothing.'),
            ('dave', 'Fair enough. I never <span class="vocab-highlight">call</span> anything <span class="vocab-highlight">off</span> though. I just start and see what happens.'),
            ('ana', 'That works until you are halfway up a ladder in <span class="vocab-highlight">a downpour</span>.'),
            ('dave', 'It has happened. Twice. Look, if you get a dry <span class="vocab-highlight">window</span> in the morning, do the veranda; if you do not, do the door inside. Either way the day is not wasted.'),
            ('ana', 'That is the whole trick, is it not? Two plans, one condition. I will do the market too, <span class="vocab-highlight">provided that</span> the delivery comes before ten.'),
        ],
        'comp': [
            ('What does Dave point out about the veranda at the start?',
             'That Ana has put it off three times already, and he wants to know whether it is actually happening on Saturday.'),
            ('How does Dave describe his own way of dealing with the weather?',
             'He never calls anything off. He just starts and sees what happens &mdash; which has left him halfway up a ladder in a downpour twice.'),
            ('What is the advice Dave gives at the end, and why does it work?',
             'Have two plans and one condition: veranda if there is a dry window, the door inside if not. Either way the day is not wasted.'),
        ],
    },
    'listenings': [
        {
            'voice': 'german_f',
            'title': 'A Saturday <span class="accent">Is Not an Improvisation</span>',
            'blurb': 'A German engineer on planning weekends, and on the year she stopped. Sound first &mdash; no text.',
            'text': 'I want to defend planning, because people make jokes about Germans and planning and the jokes '
                    'are not wrong but they are also not the whole story. Here is what a plan actually is. A plan is '
                    'a promise you make to the version of yourself who wakes up on Saturday tired. That person is '
                    'not going to make good decisions at eight in the morning, so I make them for her on Thursday '
                    'evening, and I write down the condition next to each one. If the delivery arrives before ten, '
                    'the kitchen. If it does not, the garden. That is it. That is the entire system. Then I spent a '
                    'year in Lisbon and I discovered something that genuinely upset me for about three months, which '
                    'is that nobody there does this and the weekends are somehow better. People would ring on '
                    'Saturday morning and say, are you coming, and I would say, coming where, and there was no '
                    'answer to that question because it had not been decided yet. I found it unbearable and then I '
                    'found it liberating, in that order, and now I do about sixty percent of what I used to. I still '
                    'write the conditions down. I just write fewer things next to them.',
            'qs': [
                ('How does she define what a plan actually is?',
                 'A promise you make to the version of yourself who wakes up on Saturday tired, because that person will not make good decisions at eight in the morning.'),
                ('What exactly does she write down on Thursday evening?',
                 'The decisions, with the condition next to each one: if the delivery arrives before ten, the kitchen; if it does not, the garden.'),
                ('What happened in Lisbon, and where did she end up?',
                 'Nobody planned and the weekends were somehow better. People rang on Saturday morning asking if she was coming, with no destination decided. She found it unbearable, then liberating, and now does about sixty percent of what she used to.'),
            ],
        },
        {
            'voice': 'australian_m',
            'title': 'Two Plans and <span class="accent">One Condition</span>',
            'blurb': 'An Australian builder on why he stopped promising anything. Sound first &mdash; no text.',
            'text': 'Twenty two years on the tools and I have never once told a client I will finish on a particular '
                    'day, and I will tell you exactly why, because it is not what people assume. It is not that I am '
                    'unreliable. It is that a house has about forty things that can hold you up and thirty nine of '
                    'them are not your fault. The timber comes late. It rains for six days. The bloke with the '
                    'scaffolding gets sick. So what I say now, every single time, is this: if the weather holds, we '
                    'will have the roof on by Friday, and if it does not, we will be inside doing the plasterboard '
                    'and you will not lose a day. Two plans, one condition, said out loud before anything starts. '
                    'And here is the thing that surprised me. Clients do not want certainty. They think they do. '
                    'What they actually want is to know that you have thought about the thing that might go wrong. '
                    'The bloke who promises Friday and misses it loses the job. The bloke who says it depends on the '
                    'rain and explains what happens if it rains gets called back for the next one.',
            'qs': [
                ('What has he never done in twenty two years, and what is the reason?',
                 'He has never told a client he will finish on a particular day. A house has about forty things that can hold you up, and thirty nine of them are not your fault.'),
                ('What is the exact sentence he uses with clients now?',
                 'If the weather holds, the roof will be on by Friday; and if it does not, they will be inside doing the plasterboard and the client will not lose a day.'),
                ('What surprised him about what clients actually want?',
                 'They do not want certainty, although they think they do. They want to know you have thought about what might go wrong. The one who promises Friday and misses it loses the job.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4
    'grammar': {
        'chapter_heading': 'One Sentence, <span class="accent">Two Halves, One Rule</span>',
        'chapter_sub': 'if &middot; unless &middot; as long as &middot; provided that',
        'heading': 'All Four Are About Saturday. <span class="accent">Where Is Will?</span>',
        'examples': [
            'If it rains on Saturday, I will work inside instead.',
            'I will not start the roof unless the forecast is clear.',
            'As long as the tiles arrive by ten, I can finish the kitchen.',
            'When the rain stops, I will take the dogs out.',
        ],
        'prompt': 'Every one of these is about a Saturday that has not happened. Look at the verb straight after '
                  '<em>if</em>, <em>unless</em>, <em>as long as</em> and <em>when</em>. What tense is it &mdash; and '
                  'which half of each sentence is allowed to have <em>will</em> in it?',
        'rule_rows': [
            ('if + present, will + verb', 'A real possibility in the future. The default.',
             '<strong>If it rains</strong>, I <strong>will work</strong> inside.'),
            ('never will after if', 'The condition takes the PRESENT, however future it feels.',
             'never: <em>if it will rain</em>'),
            ('unless', 'Means <em>if not</em>. Never add a second negative.',
             'I will not start <strong>unless</strong> it is dry.'),
            ('as long as / provided that', 'A stronger, more explicit condition than plain if.',
             '<strong>Provided that</strong> the tiles arrive, I can finish.'),
            ('the result is not only will', 'might, could, can, or an imperative all work.',
             'If it rains, I <strong>might</strong> just read.'),
            ('if vs when', '<em>if</em> = it may not happen. <em>when</em> = it certainly will, only the time is open.',
             '<strong>When</strong> the rain stops... (it will stop)'),
            ('present perfect in the condition', 'For <em>after this is finished</em>.',
             'If I <strong>have finished</strong> by four, I will go.'),
        ],
        'oneliner': 'the future goes in one half only &mdash; the condition always stays in the present.',
    },
    'mistakes': [
        ('If it will rain on Saturday, I will work inside.', 'If it rains on Saturday, I will work inside.'),
        ('Unless it does not stop raining, I will stay in.', 'Unless it stops raining, I will stay in.'),
        ('When it rains on Saturday, I will work inside.', 'If it rains on Saturday, I will work inside.'),
        ('If it rains on Saturday, I would work inside.', 'If it rains on Saturday, I will work inside.'),
    ],
    'mistake_note': 'The first is the commonest conditional mistake in the world: <em>will</em> cannot live in the '
                    'condition, however future it feels. The second forgets that <em>unless</em> already contains '
                    '<em>not</em>. The third promises rain that has not been promised &mdash; <em>when</em> is for '
                    'things that are certain. The fourth swaps the tense of a real Saturday for the tense of an '
                    'imaginary one, which is next week&rsquo;s lesson and a completely different meaning.',
    'practice_heading': 'If, Unless, <span class="accent">or When?</span>',
    'practice_fill': [
        ('"If it ', 'rains', ' on Saturday, I will work inside instead." (rain &mdash; the condition, mind the tense)'),
        ('"I will not start the roof ', 'unless', ' the forecast is clear." (one word meaning if not)'),
        ('"As long as the tiles arrive by ten, I ', 'can finish', ' the kitchen." (finish &mdash; the result, and it is not will)'),
        ('"', 'When', ' the rain stops, I will take the dogs out." (the rain will certainly stop)'),
        ('"If I ', 'have finished', ' the sanding by four, I will go to the market." (finish &mdash; after it is done)'),
    ],
    'artifact': {
        'heading': 'Saturday, <span class="accent">With Conditions</span>',
        'title': 'SATURDAY PLAN &mdash; A. VERALDI',
        'subtitle': 'Forecast: rain from about 13:00 &middot; delivery window 08:00 to 12:00',
        'corner': 'Two plans<br>one condition',
        'label_width': '110px',
        'rows': [
            ('08:00', 'tiles arrive? &mdash; if yes, kitchen floor; if no, sand the door inside'),
            ('10:00', 'dry so far? &mdash; first coat on the veranda, or nothing at all'),
            ('12:00', 'market, but only if the delivery is already done'),
            ('13:00', 'rain expected. Everything outdoors stops here'),
            ('15:00', 'shutters &mdash; put off since April. Indoors, so no condition'),
            ('18:00', 'dogs out, rain or no rain'),
        ],
        'comp': [
            ('Say the 08:00 line as one full sentence with two halves.',
             '"If the tiles arrive, I will lay the kitchen floor; if they do not, I will sand the door inside." Present in both conditions, will in both results.'),
            ('Say the 12:00 line using provided that, and then again using unless.',
             '"I will go to the market provided that the delivery is already done." / "I will not go to the market unless the delivery is already done." Notice that unless carries the not by itself.'),
            ('The 18:00 line has no condition at all. Say it, and then say why when is the right word for 13:00.',
             '"I will take the dogs out at six whatever the weather." And 13:00 takes when, not if, because the forecast says the rain is certain &mdash; only the exact time is open.'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'quickfire': [
        {'situation': 'Somebody asks whether you are painting the veranda on Saturday. Answer with the condition attached.',
         'tips': ['If the rain holds off until noon, I will get the first coat on.',
                  'Present after if, will in the other half.']},
        {'situation': 'Say the same thing again, but starting from the negative side, in one clause.',
         'tips': ['I will not start unless it is dry by ten.',
                  'Unless already means if not. Do not add another negative.']},
        {'situation': 'A friend asks what happens if the delivery is late. Give her the second plan, not an apology.',
         'tips': ['If it is late, I will sand the door inside instead, so the day is not wasted.',
                  'Two plans, one condition. That is the whole lesson.']},
        {'situation': 'The forecast is certain: it will rain at one o&rsquo;clock. Say what you will do then. Careful with the first word.',
         'tips': ['When the rain starts, I will move everything indoors.',
                  'When, not if. The rain is not in doubt; only the exact hour is.']},
        {'situation': 'Make the market trip depend on one single thing, using a phrase stronger than plain if.',
         'tips': ['I will go to the market, provided that the delivery is done before ten.',
                  'Provided that / as long as make the condition explicit and slightly formal.']},
        {'situation': 'Somebody asks about a job you have moved four times. Answer honestly and put a real condition on it.',
         'tips': ['I have put the shutters off since April. If it rains all Saturday, I will finally do them.',
                  'The rain is what makes an indoor job happen. Say that out loud.']},
    ],
    'speaking': [
        ('What will you do on Saturday if the weather is good?',
         'If it is dry by ten, I will get the first coat on the veranda and leave the inside jobs for Sunday.'),
        ('And what will you do if it rains all day?',
         'If it rains all day, I will finally do the shutters, which I have put off since April.'),
        ('Under what condition will you go to the market this weekend?',
         'I will go, provided that the delivery arrives before ten. Out here it is one trip or none.'),
        ('What will you do when the rain finally stops on Sunday evening?',
         'When it stops, I will take the dogs out, because by then they will have been indoors for two days.'),
    ],
    'building': [
        ('if / rain on Saturday / I / work inside (a real possibility)',
         'If it rains on Saturday, I will work inside.'),
        ('I / not start the roof / unless / the forecast / clear (one clause, one negative)',
         'I will not start the roof unless the forecast is clear.'),
        ('as long as / the tiles / arrive by ten / I / can finish the kitchen (the result is not will)',
         'As long as the tiles arrive by ten, I can finish the kitchen.'),
        ('the rain / stop / I / take the dogs out (it will certainly stop)',
         'When the rain stops, I will take the dogs out.'),
    ],
    'answerkey_heading': 'The First Conditional on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole conditional key',
    'answerkey': [
        'if + PRESENT SIMPLE, will + verb = a real possibility this Saturday: if it rains, I will work inside',
        'WILL NEVER GOES AFTER IF. The condition stays in the present, however future it feels',
        'unless = if not. One negative only: I will not start unless it is dry',
        'as long as / provided that = the same idea, stated more explicitly and slightly more formally',
        'the result half can take will, might, could, can, or an imperative: if it rains, take the ladder in',
        'if = it may not happen &middot; when = it certainly will, only the time is open',
        'the condition can take the present perfect for after this is finished: if I have finished by four...',
        'NEVER: if it will rain &middot; unless it does not rain &middot; if it rains I would work inside',
    ],
    'rp_chapter_heading': 'The Saturday You <span class="accent">Have Not Had Yet</span>',
    'roleplays': [
        {'heading': 'The Neighbour Who Wants <span class="accent">a Straight Answer</span>',
         'scenario': 'I am your neighbour and I want to borrow your ladder on Saturday, so I need to know whether '
                     'you are using it. I ask you three things: what you are doing outdoors, what happens if it '
                     'rains, and by what time you will know. Answer each with the condition attached.',
         'chips': ['if it holds off', 'unless it is dry by', 'I will know by']},
        {'heading': 'The German Colleague Who <span class="accent">Wants the Whole Plan</span>',
         'scenario': 'I am a German colleague and you have invited me for the weekend. I will ask exactly what we '
                     'are doing and I will not accept we will see &mdash; I want each activity with its condition '
                     'and its alternative. Give me the whole Saturday that way.',
         'chips': ['provided that', 'if it does not, we will', 'weather permitting']},
        {'heading': 'Two Minutes on <span class="accent">Next Saturday</span>',
         'scenario': 'Describe the Saturday coming up in the house: what you will do first, what each job depends on, '
                     'what the second plan is if the first falls through, and the one thing you will do whatever '
                     'happens. Every job must arrive with its condition attached, out loud, before you move on.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'The Plan That <span class="accent">Survives Saturday</span>',
    'survival_heading': 'Five Phrases for <span class="accent">a Plan With Conditions</span>',
    'survival': [
        'If the rain holds off until noon, I will get the first coat on.',
        'I will not start the roof unless the forecast is clear.',
        'As long as the tiles arrive by ten, I can finish the kitchen.',
        'We are painting the veranda on Sunday, weather permitting.',
        'When the rain stops, I will take the dogs out.',
    ],
    'checklist': [
        'I keep the present simple after if, unless, as long as and provided that.',
        'I never put will in the condition half of the sentence.',
        'I use unless for if not, with only one negative in the sentence.',
        'I use when for something certain and if for something that may not happen.',
        'I know the words: weather permitting, to hold off, a downpour, daunting, to squeeze in.',
    ],
    'badge': {
        'name': 'The Weekend Ahead',
        'text': 'You have just planned a whole Saturday out loud, with every condition attached, to an Australian '
                'who never plans anything and a German who plans everything.',
        'next': 'If I Lived in the Middle of Nowhere',
    },

    # ------------------------------------------------------------ teacher (icone T)
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'the Saturday that has not happened yet.&quot; Esta e a primeira das quatro condicionais e a aluna '
                 'DECLAROU na consultoria que o condicional nunca entra na cabeca dela -- diga isso em voz alta, '
                 'porque nomear o buraco derruba metade do medo.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 11: ela separou used to, be used to '
                  'e get used to. PONTE (REGRA 27B): &quot;All of that was about time that has already passed. '
                  'Tonight, nothing has happened yet.&quot; A pergunta e sobre a casa DELA e sobre uma tarefa '
                  'adiada -- a resposta ja e material para o artefato do capitulo 4. ANOTE o que ela disser.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase de baixo cita a propria '
                   'aluna: &quot;o condicional nao entra na minha cabeca&quot;. Diga que sao QUATRO e que hoje e a '
                   'unica que descreve algo que pode acontecer neste sabado. Nao de a regra ainda.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> A reformulacao e o ponto: nao &quot;o que voce vai '
                'fazer&quot;, mas &quot;o que precisa ser verdade antes&quot;. Se ela responder com uma lista '
                'simples, devolva: &quot;And what does each of those depend on?&quot; E ai que a gramatica da noite '
                'nasce sozinha.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for a plan that depends '
                       'on something. Click each card to reveal.&quot; Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ &quot;to put '
                  'something off&quot;: &quot;Did I forget, or did I decide? (Decidi -- tem escolha dentro, e quase '
                  'sempre culpa leve.)&quot; CCQ &quot;to bother&quot;: &quot;Is it common in the positive? (Quase '
                  'nunca -- vive no negativo: I will not bother.)&quot; CCQ &quot;weather permitting&quot;: '
                  '&quot;Where in the sentence does it go? (No FIM, sempre.)&quot; Peca um exemplo da casa dela em '
                  'cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ &quot;provided that&quot;: '
                  '&quot;Is it the same as if? (Quase -- mas e mais explicito e um pouco mais formal, e serve para '
                  'UMA condicao so.)&quot; CCQ &quot;to hold off&quot;: &quot;Who holds off, the rain or me? (Os '
                  'dois -- a chuva nao comeca, ou eu adio uma decisao.)&quot; CCQ &quot;a window&quot;: &quot;Is it '
                  'in the wall? (Nao. E tempo, e e curto.)&quot;',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. Certo fica '
                    'verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note como ponte para a leitura: '
                    '&quot;weather permitting&quot; e uma condicional inteira dobrada em duas palavras.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> &quot;A downpour&quot; -- o stress cai em DOWN, e '
                'pour rima com more. &quot;Daunting&quot; -- DAWN-ting, e o T no meio e claro (nao americano-mole '
                'aqui). &quot;Weather permitting&quot; -- as duas palavras colam e o T duplo vira um flap. Na frase '
                'inteira, &quot;holds off&quot; liga o D no O da palavra seguinte: /holdzOF/. E linking, exatamente '
                'o da aula 9.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a palavra que falta ANTES de '
                   'clicar. As candidatas estao no banco embaixo, fora de ordem. A ultima e separavel (put... off) e '
                   'e uma boa hora para comentar que o objeto entra no meio. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao (1 min):</strong> Diga: &quot;A short text about why Saturday never fits. '
                     'Read for the main idea -- do not stop at every word.&quot; Passe ao proximo.',
        'reading': '<strong>Leitura + Gist (6 min):</strong> De 3 minutos de leitura silenciosa. Depois a pergunta '
                   'de gist. Ana clica e o card certo fica verde. NAO peca traducao palavra a palavra. O paragrafo 3 '
                   'e o que fala DELA: quem restaura casa aprende isso mais rapido porque as condicoes sao fisicas e '
                   'visiveis da janela. Se ela reagir, pare e converse.',
        'tf': '<strong>True / False (4 min):</strong> Ana decide ANTES de clicar. Ao clicar, veredito e justificativa '
              'aparecem. Peca que ela aponte a linha do texto que prova cada resposta. A 5a e a tese da aula inteira.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Dave, AUSTRALIANO, que nunca cancela nada. Clique '
                    '&quot;Next Line&quot; e toque o audio de cada fala. Para cada fala da Ana, peca que ELA fale '
                    'primeiro. PRAGMATICA: o Dave e direto ao ponto da grosseria simpatica (&quot;you have put it '
                    'off three times now&quot;) -- num registro nordico ou japones a mesma frase seria impensavel. '
                    'Comente no fim. A gramatica da noite aparece aqui SEM regra nenhuma, de proposito.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o DAVE, nao sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar. A 3a resposta contem a frase que a aula inteira '
                         'persegue: dois planos, uma condicao.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar. '
                      'Esta e uma ALEMA: consoantes finais ensurdecidas (D vira T no fim), W tendendo a V, ritmo '
                      'muito regular. Avise ANTES. O conteudo vale pela PRAGMATICA: ela defende o planejamento e '
                      'depois admite que perdeu para Lisboa. Nao trate como piada de aleman -- e um retrato de duas '
                      'culturas de tempo, e a Ana vive entre as duas.',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Four sentences about Saturday. In '
                     'every one of them, half the sentence is forbidden to talk about the future.&quot; Passe ao '
                     'proximo.',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Peca que ela leia as quatro e diga QUAL METADE tem '
                   'will. Depois peca que ela tente dizer a primeira com &quot;if it will rain&quot; -- ela vai '
                   'sentir que soa errado sem saber por que, e esse desconforto e a regra. So entao clique '
                   '&quot;Reveal the Rule&quot;. CCQ: &quot;If it rains -- am I sure it will rain? (Nao.)&quot; '
                   '&quot;When the rain stops -- am I sure it will stop? (Sim. So nao sei a hora.)&quot; &quot;I '
                   'will not start unless it is dry -- do I start if it is wet? (Nao.)&quot;',
        'mistake': '<strong>Common mistake (4 min):</strong> O primeiro e o erro mais comum do mundo inteiro e o '
                   'que a Ana vai cometer hoje: will na condicao. O segundo e a dupla negativa com unless. O '
                   'terceiro promete chuva que ninguem prometeu. O QUARTO e proposital: e a segunda condicional '
                   'aparecendo no lugar errado, e e exatamente a aula que vem. Peca 2 repeticoes das versoes certas.',
        'practice': '<strong>Practice (4 min):</strong> Ana escolhe ORALMENTE antes de clicar. Se travar, faca a '
                    'pergunta-chave: &quot;Which half is the condition?&quot; A condicao NUNCA leva will, e o resto '
                    'se resolve sozinho.',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA ANTES de tocar. Este e um '
                      'AUSTRALIANO: vogais muito deslocadas (day soa quase como die), R final que some, e &quot;'
                      'bloke&quot; e &quot;on the tools&quot; sao girias de oficio. Avise ANTES. O conteudo e a '
                      'melhor defesa possivel da gramatica da noite: dizer a condicao em voz alta e o que faz o '
                      'cliente voltar. Deixe pousar.',
        'artifact': '<strong>Artefato (5 min):</strong> E o sabado DELA, com a previsao do tempo no cabecalho. Peca '
                    'que ela transforme CADA linha em frase condicional completa. So depois as 3 perguntas. A linha '
                    'das 13:00 e a armadilha: a chuva e CERTA na previsao, entao pede <em>when</em>, e quase todo '
                    'aluno responde <em>if</em>. A das 18:00 nao tem condicao nenhuma, de proposito.',
        'ch5_trans': '<strong>Transicao practice (1 min):</strong> Diga: &quot;Now we train: detective, quick fire, '
                     'and building.&quot; Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. &quot;What is wrong here?&quot; '
                     'Ana corrige ANTES de clicar. Sao os quatro do slide de Common Mistake.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez, resposta em voz alta ANTES das Tips. '
                     'A 4a e armadilha proposital (a chuva e certa, entao when e nao if) -- se ela cair, e o erro '
                     'que voce vai cacar no role-play 3.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija a '
                    'forma certa: a 1a e a 2a pedem if + presente, a 3a pede provided that, a 4a pede when. Se ela '
                    'puser will depois de if, devolva a pergunta em vez de corrigir.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase COMPLETA em voz alta, depois '
                    'clica para comparar. Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO depois que ela tentou '
                     'tudo. A segunda linha esta em maiusculas de proposito: e a unica coisa desta aula que nao pode '
                     'ser esquecida.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;Now you plan a whole Saturday out '
                     'loud. Three steps, and the last one has no help.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o vizinho que quer a escada emprestada. Registro '
               'pratico e um pouco apressado. Faca as tres perguntas na ordem. Corrija SO a estrutura condicional.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e a colega ALEMA e NAO aceita &quot;we will '
               'see&quot;. Toda vez que a Ana der uma resposta vaga, devolva: &quot;And if it rains?&quot; '
               'PRAGMATICA: e o oposto do Dave -- aqui a vagueza soa desorganizada, nao relaxada. A Ana vive entre '
               'os dois registros na vida real dela.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO corrija '
               'durante. CONTE quantas condicoes ela declara em voz alta e quantas vezes will aparece do lado '
               'errado. Diga os numeros no fim. Meta: pelo menos quatro condicoes e zero will depois de if.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;You just made a plan that will survive '
                     'contact with a Saturday.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a Ana repita. '
                    'As cinco cobrem: if afirmativo, unless, as long as com modal, weather permitting no fim, e '
                    'when. Insista no linking de &quot;holds off&quot; e em nao pronunciar will na condicao.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 12 registrada como concluida no '
                     'passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Twelve lessons, Ana. You just used the '
                 'structure you told us never sticks, for an entire Saturday.&quot; Homework (oralmente, opcional): '
                 'no domingo a noite, gravar um minuto comparando o sabado planejado com o sabado real, usando if em '
                 'cada linha que nao aconteceu. Proxima aula: If I Lived in the Middle of Nowhere -- a segunda '
                 'condicional, a irma imaginaria desta, e a que apareceu de proposito no erro numero quatro de hoje.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'If I Have Time This Weekend -- Plans With Conditions Attached',
        'desc': 'The Saturday that depends on the sky and the delivery, and the first conditional that carries it.',
        'context_paras': [
            'Ana has <strong>put</strong> the veranda <strong>off</strong> for four weekends in a row, and this '
            'time she has a plan with the condition written next to it. <strong>If the rain holds off</strong> '
            'until noon, <strong>she will get</strong> the first coat on. <strong>If it does not</strong>, she '
            '<strong>will not even bother</strong> getting the ladder out, because wet wood takes nothing.',
            'The tiles are supposed to arrive between eight and twelve. <strong>As long as they arrive</strong> by '
            'ten, she <strong>can finish</strong> the kitchen floor the same day. <strong>Provided that</strong> the '
            'delivery is done, she <strong>will squeeze</strong> the market in as well, because out here '
            '<strong>running errands</strong> means one trip or none. She <strong>will not go</strong> at all '
            '<strong>unless</strong> the morning is clear.',
            'The forecast says rain from one o&rsquo;clock, and the forecast is rarely wrong about that. So '
            '<strong>when the rain starts</strong>, everything outdoors stops, and the shutters finally happen: a '
            '<strong>daunting</strong> job indoors that has waited since April. At six, <strong>whatever the '
            'weather</strong>, the dogs go out. That is the only line on the whole list with no condition attached '
            'at all.',
        ],
        'context_quiz': [
            ('"If the rain holds off until noon, she will get the first coat on." Why holds and not will hold?',
             [('Because the verb after if stays in the present, however future the meaning is.', True),
              ('Because holds off is an expression that has no future form.', False),
              ('Because the sentence is about a habit rather than a plan.', False)]),
            ('"She will not go at all unless the morning is clear." What does unless mean here?',
             [('Even if the morning is clear.', False),
              ('If the morning is not clear.', True),
              ('Until the morning is clear.', False)]),
            ('Why "when the rain starts" and not "if the rain starts"?',
             [('Because when is more polite than if in a written plan.', False),
              ('Because the forecast makes the rain certain; only the exact time is open.', True),
              ('Because if cannot be used with the weather.', False)]),
        ],
        'tip_title': 'The First Conditional',
        'tip_sub': 'One sentence, two halves. Only one of them is allowed to talk about the future.',
        'tip_rows': [
            ('if + present, will + verb', 'A real possibility in the future', '<strong>If it rains</strong>, I <strong>will work</strong> inside.'),
            ('never will after if', 'The condition stays in the present', 'never: <em>if it will rain</em>'),
            ('unless', 'Means <em>if not</em>; only one negative', 'I will not start <strong>unless</strong> it is dry.'),
            ('as long as / provided that', 'A more explicit, slightly formal condition', '<strong>Provided that</strong> the tiles arrive...'),
            ('other results', 'might, could, can, or an imperative', 'If it rains, I <strong>might</strong> just read.'),
            ('if vs when', '<em>if</em> may not happen; <em>when</em> certainly will', '<strong>When</strong> the rain stops...'),
            ('present perfect condition', 'For <em>after this is finished</em>', 'If I <strong>have finished</strong> by four...'),
        ],
        'tip_never': 'If it will rain &middot; unless it does not rain &middot; if it rains I would work inside '
                     '&middot; when it rains on Saturday (when the rain is not certain). The first puts the future '
                     'in the wrong half, the second doubles a negative that <em>unless</em> already contains, the '
                     'third belongs to an imaginary Saturday, and the fourth promises weather nobody promised.',
        'fills': [
            ('If it ', 'rains', ' on Saturday, I will work inside instead.',
             'rain -- the condition half, and it is not the future tense'),
            ('I will not start the roof ', 'unless', ' the forecast is clear.',
             'one word meaning if not, with no second negative'),
            ('As long as the tiles arrive by ten, I ', 'can finish', ' the kitchen.',
             'finish -- the result half, two words, and it is not will'),
            ('', 'When', ' the rain stops, I will take the dogs out.',
             'one word for something that is certain to happen, capital letter'),
            ('If I ', 'have finished', ' the sanding by four, I will go to the market.',
             'finish -- after it is completely done, two words'),
            ('We are painting the veranda on Sunday, ', 'weather permitting', '.',
             'two words -- a whole condition folded up, and it always goes at the end'),
        ],
        'order_intro': 'Dave wants to borrow the ladder and Ana has a Saturday with conditions. Put the exchange in a logical order.',
        'order': [
            'So are you doing the veranda on Saturday or not? You have put it off three times now.',
            'If the rain holds off until noon, I will get the first coat on.',
            'And if it does not?',
            'Then I will not even bother getting the ladder out. Wet wood takes nothing.',
            'Fair enough. I never call anything off. I just start and see what happens.',
            'That works until you are halfway up a ladder in a downpour.',
        ],
        'quiz': [
            ('A neighbour asks whether you are painting on Saturday. You answer:',
             [('"If it will be dry, I will paint the veranda."', False),
              ('"If it is dry, I will paint the veranda."', True),
              ('"If it is dry, I would paint the veranda."', False)]),
            ('You want to say you will only start when the wood is completely dry. You say:',
             [('"I will not start unless the wood is dry."', True),
              ('"I will not start unless the wood is not dry."', False),
              ('"I will not start if the wood will be dry."', False)]),
            ('The forecast says the rain will certainly stop at four. You say:',
             [('"If the rain stops at four, I will go out."', False),
              ('"When the rain stops at four, I will go out."', True),
              ('"Unless the rain stops at four, I will go out."', False)]),
            ('You want to make the market trip depend on one explicit condition. The most natural version is:',
             [('"I will go to the market, provided that the delivery is done."', True),
              ('"I will go to the market, provided that the delivery will be done."', False),
              ('"I would go to the market, provided that the delivery is done."', False)]),
        ],
        'think': 'Describe the Saturday you have coming up. For every job, say what it depends on and what you will '
                 'do instead if that condition is not met. Finish with the one thing you will do whatever happens. '
                 'Use if at least three times, unless at least once, and when at least once for something certain.',
    },

    # ------------------------------------------------------------ complementares
    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Documentary',
         'title': 'The Repair Shop &mdash; full episode on BBC&rsquo;s channel (45 min)',
         'desc': 'Restorers in a Sussex barn taking apart objects that other people gave up on. Half of what they '
                 'say is conditional: if this joint holds, if the veneer lifts cleanly, if the part can be found.',
         'tip': 'listen for the moment each restorer explains what they will do IF the first approach fails. '
                'That is the second plan from tonight&rsquo;s lesson, said by professionals, all day long.',
         'url': 'https://www.youtube.com/watch?v=WUL9G8gEeIc', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; The Planning Fallacy (Work 2.0: Deep Work)',
         'desc': 'Why every project takes longer than the person doing it expects, and why knowing that changes '
                 'nothing. It is the research behind the text you read in class.',
         'tip': 'try predicting how long the episode will feel before you start, then check. You will be wrong '
                'in the same direction as everybody else, which is the whole point.',
         'url': 'https://hiddenbrain.org/podcast/deep-work/', 'cta': 'Listen on Hidden Brain'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'Inside the mind of a master procrastinator &mdash; Tim Urban, TED (14 min)',
         'desc': 'Fourteen very funny minutes on the gap between the weekend you planned and the weekend you had. '
                 'Fast American English with a lot of the reductions from lesson 9.',
         'tip': 'watch it once for the argument, then again with the English subtitles on, and count how many '
                'times he says gonna instead of going to.',
         'url': 'https://www.ted.com/talks/tim_urban_inside_the_mind_of_a_master_procrastinator',
         'cta': 'Watch on TED'},
    ],
}
