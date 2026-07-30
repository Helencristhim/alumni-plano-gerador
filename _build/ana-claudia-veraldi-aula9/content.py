# -*- coding: utf-8 -*-
"""Aula 9 -- Understanding Fast English (ancora intercultural, connected speech).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays.
Sotaques do listening (CURRICULO V3): americano RAPIDO + frances.
Callback da aula 8: as frases que compram tempo -- agora o problema nao e produzir,
e DECODIFICAR. E o gap que ela mesma nomeou: "a minha autonomia de compreensao
auditiva e muito ruim".
"""

LESSON = {
    'n': 9,
    'menu_title': 'Understanding Fast English',
    'menu_desc': 'Why fast English sounds like one long word, and what happens to the sounds that '
                 'disappear between going and to',
    'grammar_point': 'connected speech: reductions and weak forms',
    'chapter_tag': 'Many Englishes',
    'title_html': 'Understanding <span class="accent">Fast English</span>',
    'title_sub': 'The words are all there. They have simply stopped standing apart from each other.',
    'phases': ['First Words', 'The Words of Speed', 'Two Fast Voices',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],

    # ---------------------------------------------------------------- chapter 1
    'warmup': {
        'heading': 'You Can Speak. <span class="accent">Now Catch It.</span>',
        'callback': 'Last time you spoke for ten minutes with no notes, and when a word disappeared you '
                    'said bear with me and kept the floor. That solved the half of the problem where '
                    'you are the one talking.',
        'question': 'Think of the last time somebody said something in English and you caught nothing '
                    'at all. Was the person speaking quietly, or fast, or both?',
    },
    'framing': {
        'heading': 'Nothing Is Missing. <span class="accent">It Is All Joined.</span>',
        'steps': [('The Words', 'to slur, to mumble, to keep up, over your head...'),
                  ('Two Voices', 'a fast American and a French woman, twice each'),
                  ('The Sounds', 'gonna, wanna, didja, lotta &mdash; and why they exist')],
        'note': 'You were taught English with <strong>spaces between the words</strong>. Nobody speaks '
                'with spaces between the words. Tonight you stop hearing a wall of noise and start '
                'hearing four or five very ordinary reductions doing it to you over and over.',
    },
    'hook': {
        'label': 'The Real Problem',
        'heading': 'It Is Not the <span class="accent">Speed</span>',
        'line1': 'Everybody says fast English is the problem. It is not really the speed. It is that '
                 'at speed, English glues words together and throws sounds away.',
        'line2': 'Whaddaya gonna do about it? That is six words. Say it slowly and you already know '
                 'every single one of them.',
    },

    # ---------------------------------------------------------------- chapter 2
    'vocab_heading': 'The Language of <span class="accent">Speed and Noise</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'To slur', 'icon': 'wave',
         'def': 'To run words together so that their edges disappear',
         'ex': 'He was tired and started to slur everything.',
         'match': 'to run words together so their edges disappear'},
        {'word': 'To swallow a sound', 'icon': 'moon',
         'def': 'To leave out a sound that is written but never actually said',
         'ex': 'Americans swallow the t in twenty. It comes out as twenny.',
         'match': 'to leave out a sound that is written but not said'},
        {'word': 'A contraction', 'icon': 'key',
         'def': 'The short spoken form of two words: I am becomes I&rsquo;m',
         'ex': 'Almost every contraction is invisible to you until somebody writes it down.',
         'match': 'the short spoken form of two words'},
        {'word': 'Gonna', 'icon': 'plane',
         'def': 'What going to becomes in ordinary speech, in almost every sentence',
         'ex': 'I am gonna call the builder this afternoon.',
         'match': 'what going to becomes in ordinary speech'},
        {'word': 'To mumble', 'icon': 'lock',
         'def': 'To speak quietly and unclearly, with the mouth barely moving',
         'ex': 'He mumbled the price and I had to ask him twice.',
         'match': 'to speak quietly and unclearly, mouth barely moving'},
        {'word': 'To rattle off', 'icon': 'bolt',
         'def': 'To say something very fast, from memory, without a single pause',
         'ex': 'She rattled off six dates and I caught the first one.',
         'match': 'to say something very fast from memory, without pausing'},
        {'word': 'Word for word', 'icon': 'grid',
         'def': 'Trying to catch every single word instead of the meaning',
         'ex': 'I listen word for word and that is exactly why I lose everything.',
         'match': 'trying to catch every single word instead of the meaning'},
        {'word': 'To keep up', 'icon': 'clock',
         'def': 'To follow at the same speed and not fall behind',
         'ex': 'He was going so fast I could not keep up at all.',
         'match': 'to follow at the same speed and not fall behind'},
        {'word': 'Crystal clear', 'icon': 'sun', 'expr': True,
         'def': 'Completely easy to understand, with no effort at all',
         'ex': 'The second time she said it, it was crystal clear.',
         'match': 'completely easy to understand, with no effort at all'},
        {'word': 'To go over your head', 'icon': 'compass', 'expr': True,
         'def': 'To be too fast or too complex for you to follow at all',
         'ex': 'That whole first minute went completely over my head.',
         'match': 'to be too fast or too complex for you to follow'},
        {'word': 'To enunciate', 'icon': 'ear',
         'def': 'To pronounce every sound separately and very clearly',
         'ex': 'When she enunciates I understand everything. When she relaxes, I lose her.',
         'match': 'to pronounce every sound separately and very clearly'},
        {'word': 'A tongue twister', 'icon': 'chat',
         'def': 'A phrase built to be hard to say, usually for fun',
         'ex': 'Say it three times fast. It is a tongue twister.',
         'match': 'a phrase built to be hard to say, usually for fun'},
    ],
    'vocabnote': "Two of tonight's twelve are whole expressions: crystal clear and to go over your "
                 'head. They are opposites, and between them they describe every listening experience '
                 'you have ever had in English. Most of what happens in the middle has a name too, '
                 'and by the end of tonight it will have four.',
    'pron': ['To slur', 'Crystal clear', 'A tongue twister',
             'That whole first minute went completely over my head.'],
    'gapfill': [
        {'before': 'He was going so fast that I could not ', 'answer': 'keep up',
         'after': ' at all.'},
        {'before': 'He tends to ', 'answer': 'rattle off',
         'after': ' a whole list of dates without pausing once.'},
        {'before': 'If somebody talks that fast, the first minute will always ',
         'answer': 'go over your head', 'after': '.'},
        {'before': 'The second time she said it, it was absolutely ',
         'answer': 'crystal clear', 'after': '.'},
        {'before': 'I listen ', 'answer': 'word for word',
         'after': ' and that is exactly why I lose everything.'},
        {'before': 'Americans ', 'answer': 'swallow a sound',
         'after': ' in the middle of twenty. It comes out as twenny.'},
    ],

    # ---------------------------------------------------------------- chapter 3
    'ch3_heading': 'Two People Talking <span class="accent">Normally</span>',
    'ch3_sub': 'Nobody is going to slow down for you first',
    'dialogue': {
        'name': 'Marc', 'cls': 'marc', 'initial': 'M', 'voice': 'french_m',
        'heading': 'The Frenchman Who <span class="accent">Also Loses Them</span>',
        'lines': [
            {'who': 'marc', 'text': 'Ana, be honest with me. On those calls with the Americans, do you '
                                    'actually <span class="vocab-highlight">keep up</span>, or do you '
                                    'just wait for the email afterwards?'},
            {'who': 'ana', 'text': 'The first two minutes usually go completely '
                                   '<span class="vocab-highlight">over my head</span>. After that I get '
                                   'about half.'},
            {'who': 'marc', 'text': 'Same. And it is not the vocabulary. When they write it down it is '
                                    '<span class="vocab-highlight">crystal clear</span>. When they say '
                                    'it, everything is glued together.'},
            {'who': 'ana', 'text': 'Because they are not saying going to. They say gonna. And they '
                                   '<span class="vocab-highlight">swallow the sound</span> in the middle '
                                   'of twenty.'},
            {'who': 'marc', 'text': 'So it is not that they <span class="vocab-highlight">mumble</span>. '
                                    'It is that the sounds are genuinely not there.'},
            {'who': 'ana', 'text': 'Exactly. And I made it worse for years by listening '
                                   '<span class="vocab-highlight">word for word</span>. If I lose one '
                                   'word I stop, and then I lose the next twelve.'},
            {'who': 'marc', 'text': 'That is a very good description of my Monday mornings. So what do '
                                    'you do instead?'},
            {'who': 'ana', 'text': 'I let the small ones go. If somebody '
                                   '<span class="vocab-highlight">rattles off</span> a whole sentence I '
                                   'take the two words that carry the meaning and I keep going.'},
        ],
        'comp': [
            ('What does Marc admit about calls in English?',
             'That he is not sure he keeps up either &mdash; he asks Ana whether she actually follows '
             'or just waits for the email afterwards. It is his Monday mornings too.'),
            ('What is Marc&rsquo;s explanation for the problem, and what does Ana add to it?',
             'Marc says it is not the vocabulary, because written down it is crystal clear; everything '
             'is glued together in speech. Ana adds that the sounds are genuinely missing: gonna, and '
             'the swallowed t in twenty.'),
            ('What does Marc conclude at the end, in his own words?',
             'That the speakers are not mumbling &mdash; the sounds are genuinely not there. It is a '
             'different problem from bad pronunciation, and it needs a different solution.'),
        ],
    },
    'listenings': [
        {'voice': 'arthur',
         'heading': 'The Two Minutes You <span class="accent">Always Lose</span>',
         'intro': 'An American at ordinary speed &mdash; the speed nobody slows down from. Sound first.',
         'text': "Alright so quick update before we get into the numbers, and I'm gonna go fast because "
                 "we've got about eleven minutes. The install slipped a week, that's the headline, "
                 "nothing dramatic, it just slipped. Reason being, the parts were held at customs for "
                 "four days and there wasn't a lot we coulda done about that. Second thing, and this is "
                 "the one I want everybody to hear, the budget hasn't moved. It hasn't moved a dollar. "
                 "I keep getting asked and the answer's the same as it was in March. Third, we're gonna "
                 "need somebody on site Thursday, and I'd rather it wasn't me. If you wanna volunteer, "
                 "now's a great moment. Okay, that's the update. Anybody got anything before I hand "
                 "over?",
         'comp': [
             ('What is the headline of the update, and what caused it?',
              'The install slipped by a week. The parts were held at customs for four days and there '
              'was not much they could have done about it.'),
             ('What is the one thing he wants everybody to hear?',
              'That the budget has not moved. Not a dollar, and the answer is the same as it was in '
              'March.'),
             ('What does he ask for at the end, and how does he ask for it?',
              'Somebody on site on Thursday &mdash; and he says he would rather it was not him, then '
              'invites volunteers. Half a joke, and a real request.'),
         ]},
        {'voice': 'french_f',
         'heading': 'Twelve Years Before I <span class="accent">Heard It</span>',
         'intro': 'A French woman on the day the noise turned into words. Sound first &mdash; no text.',
         'text': "I had been studying English for about twelve years when somebody finally explained "
                 "the thing that changed everything, and I remain slightly angry that nobody said it "
                 "sooner. I could read anything. I could write reports. And on the telephone I "
                 "understood almost nothing, which made me believe my English was fake. Then a "
                 "colleague showed me a transcript of a recording while it was playing. Every word on "
                 "that page was a word I knew. Every single one. I simply had not heard them, because "
                 "they were not being said the way they are written. Going to was gonna. Did you was "
                 "didja. And a lot of was a lotta. Nobody had ever told me this. My teachers spoke "
                 "very slowly and very clearly, which was kind and which was useless. So my advice, "
                 "for whatever it is worth, is to listen to the fast version first and read the "
                 "transcript afterwards. The other order teaches you nothing at all.",
         'comp': [
             ('What could she do well, and what made her believe her English was fake?',
              'She could read anything and write reports, but on the telephone she understood almost '
              'nothing.'),
             ('What did the colleague do, and what did she discover?',
              'The colleague showed her a transcript while the recording played. Every word on the page '
              'was a word she already knew &mdash; she simply had not heard them, because they were '
              'not said the way they are written.'),
             ('What is her advice about order, and why?',
              'Listen to the fast version first and read the transcript afterwards. The other order '
              'teaches you nothing, and slow clear teachers were kind but useless.'),
         ]},
    ],

    # ---------------------------------------------------------------- chapter 4
    'grammar': {
        'label': 'Sound Discovery',
        'ch_heading': 'What Happened to <span class="accent">the Spaces?</span>',
        'ch_sub': 'gonna &middot; wanna &middot; didja &middot; lotta &mdash; four reductions, most of your problem',
        'heading': 'Say the Right-Hand Side <span class="accent">Out Loud</span>',
        'examples': [
            'What are you going to do? &mdash; Whaddaya gonna do?',
            'I want to talk to you about it. &mdash; I wanna talk to ya about it.',
            'Did you see the beams yet? &mdash; Didja see the beams yet?',
            'It is a lot of work. &mdash; It&rsquo;s a lotta work.',
        ],
        'prompt': 'Read the left-hand side. Now read the right-hand side out loud, fast. They are the '
                  'same sentence. Which sounds actually disappeared, and which ones only moved?',
        'table': [
            ('gonna / wanna / gotta', 'going to, want to and have got to, before a verb.',
             "I'm <strong>gonna</strong> call him &middot; I <strong>wanna</strong> see it."),
            ('of and to lose their vowel', 'They flatten to a single weak sound between words.',
             'a <strong>lotta</strong> work &middot; talk <strong>ta</strong> you'),
            ('linking consonant to vowel', 'A final consonant jumps onto the next word.',
             'an apple sounds like <strong>a napple</strong>'),
            ('weak forms', 'to, of, for, and, was, can all collapse to one dull sound.',
             'fish <strong>and</strong> chips sounds like <strong>fish&rsquo;n</strong> chips'),
            ('/d/ + /y/ becomes /j/', 'did you, would you, could you all fuse.',
             '<strong>didja</strong> &middot; <strong>wouldja</strong> &middot; <strong>couldja</strong>'),
            ('the disappearing t', 'Between vowels in American English it softens to a d, or vanishes.',
             'water sounds like <strong>wader</strong> &middot; twenty like <strong>twenny</strong>'),
            ('stressed words carry meaning', 'Nouns and main verbs are loud; everything else is quiet.',
             'the two loud words in a sentence are usually enough'),
        ],
        'oneliner': 'English is not written with the spaces it is spoken with.',
    },
    'mistakes': [
        ('I am going to gonna call him tomorrow.', 'I am gonna call him tomorrow.'),
        ('I wanna to see the house on Saturday.', 'I wanna see the house on Saturday.'),
        ('He gonna come at eight.', 'He is gonna come at eight.'),
        ('We gotta to leave in ten minutes.', 'We gotta leave in ten minutes.'),
    ],
    'mistake_note': 'Three of these four are the same error: <strong>gonna, wanna and gotta already '
                    'contain the to</strong>, so adding another one makes the sentence collapse. The '
                    'third is different &mdash; gonna replaces <em>going to</em>, never <em>is going '
                    'to</em>, so the verb <strong>be</strong> stays exactly where it was. And one '
                    'warning: these are <strong>spoken</strong> forms. Say them, hear them, and do not '
                    'write them in an email.',
    'gpractice_heading': 'Write What You <span class="accent">Hear</span>',
    'gpractice': [
        {'before': 'What ', 'answer': 'are you gonna', 'after': ' do about the roof?',
         'cue': 'are you going to &mdash; said as one word'},
        {'before': 'I ', 'answer': 'wanna', 'after': ' talk to you about the quote.',
         'cue': 'want to &mdash; one word in speech'},
        {'before': 'We ', 'answer': 'gotta', 'after': ' leave in ten minutes.',
         'cue': 'have got to &mdash; one word in speech'},
        {'before': 'Honestly, it is ', 'answer': 'a lotta', 'after': ' work for one weekend.',
         'cue': 'a lot of &mdash; the of loses its vowel'},
        {'before': '', 'answer': 'Didja', 'after': ' see the beams before they replaced them?',
         'cue': 'did you &mdash; the d and the y fuse into one sound'},
    ],
    'artifact': {
        'heading': 'The Voicemail, <span class="accent">As You Heard It</span>',
        'doc_title': 'VOICEMAIL &mdash; 07:52',
        'doc_sub': 'Transcribed exactly as spoken',
        'doc_right': 'Duration 0:34<br>Not edited',
        'rows': [
            ('0:00', 'Morning, s&rsquo;me again, sorry to call so early'),
            ('0:04', 'Listen, we&rsquo;re gonna hafta move Thursday'),
            ('0:08', 'The guy with the plaster can&rsquo;t make it til Friday'),
            ('0:13', 'Didja get the quote I sent ya on Monday?'),
            ('0:18', 'Cos there&rsquo;s a lotta stuff on there I wanna go through with ya'),
            ('0:26', 'Anyway, gimme a ring when you get a sec. Cheers.'),
        ],
        'comp': [
            ('Say the 0:04 line the way it is written in a book. What has been reduced?',
             '"We are going to have to move Thursday." Going to became gonna, have to became hafta, '
             'and we are became we&rsquo;re. Three reductions in six words.'),
            ('The 0:13 line has two reductions. Name both.',
             '"Did you get the quote I sent you on Monday?" Did you fused into didja, and you flattened '
             'to ya. Neither sound was lost &mdash; they were joined.'),
            ('What does gimme a ring mean, and what has happened to it?',
             '"Give me a call." Give me collapses into gimme, and a ring is simply British and '
             'Australian for a phone call. The reduction is the sound; the ring is the vocabulary.'),
        ],
    },

    # ---------------------------------------------------------------- chapter 5
    'detective': [
        ('I am going to gonna call him tomorrow.', 'I am gonna call him tomorrow.'),
        ('I wanna to see the house on Saturday.', 'I wanna see the house on Saturday.'),
        ('He gonna come at eight.', 'He is gonna come at eight.'),
        ('We gotta to leave in ten minutes.', 'We gotta leave in ten minutes.'),
    ],
    'quickfire': [
        {'situation': 'Somebody has just rattled off three dates and you caught none of them. Ask '
                      'again without apologising for your English.',
         'tips': ['Sorry, could you give me those dates again, a bit slower?',
                  'Ask for the DATES, not for the whole sentence. Be specific about what you missed.']},
        {'situation': 'You caught about half of what was said, and the half you caught is enough to '
                      'answer. Answer, and check the rest afterwards.',
         'tips': ['So Thursday is off and Friday is on &mdash; have I got that right?',
                  'Repeating back what you did catch is faster than asking for everything again.']},
        {'situation': 'An American colleague is speaking at full speed and you need him slower for '
                      'the next five minutes, not for one sentence.',
         'tips': ['Would you mind taking this bit a little slower? I want to get the detail right.',
                  'Give a reason. Slowing down for no stated reason feels like criticism.']},
        {'situation': 'A Norwegian colleague says something you miss. Ask again &mdash; and notice that '
                      'what? would land very differently here than it does with the American.',
         'tips': ['Sorry, I did not catch that.',
                  'Pardon? &mdash; short, soft, and neutral almost everywhere.']},
        {'situation': 'Somebody asks whether you followed all of that. You followed most of it. Say so '
                      'honestly.',
         'tips': ['Most of it. The first minute went over my head, the rest was fine.',
                  'Naming which part you lost is a B2 answer. Saying yes when you did not is not.']},
        {'situation': 'You want somebody to say something once more, and you already asked once. Ask '
                      'the second time.',
         'tips': ['Sorry, one more time &mdash; just the last part?',
                  'Narrow it. The second ask should be smaller than the first, never bigger.']},
    ],
    'speaking': [
        ('When somebody speaks fast in English, what actually happens in your head?',
         'I lose one word, I stop to look for it, and by the time I find it I have lost the next twelve.'),
        ('What have you been doing about it, and what are you going to do instead?',
         'I have been listening word for word. From now on I take the two words that carry the meaning '
         'and let the small ones go.'),
        ('Somebody asks whether you followed the whole call. Answer honestly and precisely.',
         'Most of it. The first two minutes went over my head, and after that it was fine.'),
        ('What did you not know before tonight about the way English is actually said?',
         'That the sounds are genuinely not there. I thought people were mumbling and it turns out '
         'going to is simply gonna.'),
    ],
    'build': [
        ('what / you / going to do about the roof (say it the way it is said)',
         'Whaddaya gonna do about the roof?'),
        ('I / want to / talk to you about the quote',
         'I wanna talk to you about the quote.'),
        ('did you / see the beams before they replaced them',
         'Didja see the beams before they replaced them?'),
        ('it is / a lot of work / for one weekend',
         "It's a lotta work for one weekend."),
    ],
    'answerkey_heading': 'Every Reduction on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole sound key',
    'answerkey': [
        'gonna = going to &middot; wanna = want to &middot; gotta = have got to (all three already contain the TO)',
        'lotta = a lot of &middot; kinda = kind of &middot; sorta = sort of (the OF loses its vowel)',
        'didja = did you &middot; wouldja = would you &middot; couldja = could you (the D and the Y fuse)',
        'hafta = have to &middot; gimme = give me &middot; lemme = let me',
        'ya = you, unstressed &middot; ta = to, unstressed &middot; n = and (fish&rsquo;n chips)',
        'the t between vowels goes soft or vanishes: water = wader, twenty = twenny',
        'a final consonant jumps to the next word: an apple = a napple',
        'STRATEGY: take the two loud words and let the quiet ones go. Word for word is what loses you '
        'the sentence, not the speed',
    ],

    # ---------------------------------------------------------------- chapter 6
    'rp_ch_heading': 'Ask Again, <span class="accent">Without Shrinking</span>',
    'roleplay': {
        'guided': {
            'heading': 'The American Who <span class="accent">Will Not Slow Down</span>',
            'scenario': 'I am giving you an update at full speed, exactly like the recording. Stop me '
                        'three times: once to get a date again, once to check something back, and once '
                        'to ask me to take a whole section more slowly. Do not apologise for your '
                        'English at any point.',
            'chips': ['could you give me that again', 'have I got that right', 'a little slower'],
        },
        'semi': {
            'heading': 'Marc Wants to Know <span class="accent">What You Do</span>',
            'scenario': 'I am Marc, and I have just admitted that the first two minutes of every call '
                        'go over my head. Ask me two questions about how I listen, then tell me exactly '
                        'what you have changed &mdash; not the theory, the thing you actually do.',
            'chips': ['word for word', 'keep up', 'the two words that carry it'],
        },
        'free': {
            'heading': 'Two Minutes, <span class="accent">No Notes</span>',
            'scenario': 'Explain to somebody who has never studied English why fast English is hard, '
                        'using yourself as the example. What you used to believe was happening, what is '
                        'actually happening, and what you now do in the second after you lose a word.',
        },
    },

    # ---------------------------------------------------------------- chapter 7
    'wrap_heading': 'The Sounds Were <span class="accent">Never There</span>',
    'survival_heading': 'Five Phrases for <span class="accent">the Moment You Lose It</span>',
    'survival': [
        'Sorry, that whole first part went over my head.',
        'Could you give me those dates again, a bit slower?',
        'So Thursday is off and Friday is on. Have I got that right?',
        'You were rattling it off and I could not keep up.',
        'Now that is crystal clear, thank you.',
    ],
    'checklist': [
        'I know that gonna, wanna and gotta already contain the word to.',
        'I can hear didja, lotta, hafta and gimme for what they are.',
        'I stopped listening word for word and started taking the two loud words.',
        'I can ask somebody to slow down without apologising for my English.',
        'I know the words: to slur, to mumble, to keep up, crystal clear, to go over your head.',
    ],
    'closing': {
        'badge': 'Many Englishes Badge <span class="accent">Earned!</span>',
        'text': 'For years you thought they were mumbling, Ana. Tonight you found out that going to '
                'has not been said out loud in that form since about 1940, and that you already knew '
                'every word you were missing.',
        'next': 'I Used to Live in the City',
    },

    # ---------------------------------------------------------------- pre-class
    'pc_title': 'Understanding Fast English -- The Sounds That Are Not There',
    'pc_desc': 'Why fast English sounds like one long word. Key words: to slur, to swallow a sound, a '
               'contraction, gonna, to mumble, to rattle something off, word for word, to keep up, '
               'crystal clear, to go over your head, to enunciate, a tongue twister. Focus: connected '
               'speech -- gonna, wanna, didja, lotta and the weak forms.',
    'pc_context': {
        'paras': [
            'For twelve years Ana believed people were <strong>mumbling</strong>. She could read '
            'anything and write anything, and on a call she caught almost nothing, which made her '
            'believe her English was somehow fake.',
            'Then somebody showed her a transcript while the recording played. Every word on the page '
            'was a word she already knew. She simply had not heard them. Nobody says <em>going to</em>; '
            'they say <strong>gonna</strong>. Nobody says <em>did you</em>; they say <strong>didja</strong>. '
            'Americans <strong>swallow the sound</strong> in the middle of twenty, and <em>a lot of</em> '
            'arrives as <strong>a lotta</strong>. The sounds are not hidden. They are genuinely not there.',
            'What made it worse was her own method. Listening <strong>word for word</strong>, she would '
            'lose one word, stop to look for it, and lose the next twelve. Now she takes the two words '
            'that carry the meaning and lets the small ones go. When somebody '
            '<strong>rattles something off</strong> and she cannot <strong>keep up</strong>, she says '
            'so. The first minute still goes <strong>over her head</strong>. The rest is now '
            '<strong>crystal clear</strong>.',
        ],
        'quiz': [
            {'q': 'Why did Ana believe her English was fake?',
             'opts': [('Because she could read and write well but understood almost nothing on a call.', True),
                      ('Because her vocabulary was too small for real conversations.', False),
                      ('Because she had never studied grammar properly.', False)]},
            {'q': 'What did the transcript prove?',
             'opts': [('That she needed to learn many more words.', False),
                      ('That every word was one she already knew, and she simply had not heard them.', True),
                      ('That the speakers were pronouncing the words incorrectly.', False)]},
            {'q': 'Why does listening word for word make things worse?',
             'opts': [('Because you lose one word, stop to look for it, and lose the next twelve.', True),
                      ('Because it is slower than reading a transcript.', False),
                      ('Because native speakers speak faster when they see you concentrating.', False)]},
        ],
    },
    'pc_tip': {
        'title': 'Connected Speech',
        'lead': 'You were taught English with spaces between the words. Nobody speaks with spaces.',
        'table': [
            ('gonna / wanna / gotta', 'going to, want to, have got to &mdash; all three already contain '
                                      'the to',
             "I'm <strong>gonna</strong> call him &middot; I <strong>wanna</strong> see it"),
            ('lotta / kinda / sorta', 'the of loses its vowel completely',
             'a <strong>lotta</strong> work &middot; <strong>kinda</strong> tired'),
            ('didja / wouldja / couldja', 'the d and the y fuse into one sound',
             '<strong>Didja</strong> see it?'),
            ('hafta / gimme / lemme', 'have to, give me, let me',
             '<strong>Gimme</strong> a ring when you can'),
            ('weak forms', 'to, of, for, and, was and can collapse to one dull sound',
             'fish <strong>and</strong> chips = <strong>fish&rsquo;n</strong> chips'),
            ('the disappearing t', 'between vowels in American English it softens or vanishes',
             'water = <strong>wader</strong> &middot; twenty = <strong>twenny</strong>'),
            ('linking', 'a final consonant jumps onto the next word',
             'an apple = <strong>a napple</strong>'),
        ],
        'never': 'I am going to gonna call &middot; I wanna to see it &middot; he gonna come &middot; '
                 'we gotta to leave. Three of those add a second to that is already inside the word, '
                 'and one drops the verb be, which never goes anywhere. And these are SPOKEN forms: '
                 'hear them, say them, do not write them in an email.',
    },
    'pc_blanks': [
        {'before': 'I am ', 'answer': 'gonna', 'after': ' call the builder this afternoon.',
         'hint': 'Hint: what going to becomes in speech, one word'},
        {'before': 'I ', 'answer': 'wanna', 'after': ' talk to you about the quote.',
         'hint': 'Hint: what want to becomes in speech, one word'},
        {'before': 'He was going so fast that I could not ', 'answer': 'keep up', 'after': ' at all.',
         'hint': 'Hint: two words -- to follow at the same speed and not fall behind'},
        {'before': 'That whole first minute went completely ', 'answer': 'over my head', 'after': '.',
         'hint': 'Hint: three words -- too fast or too complex for you to follow'},
        {'before': 'I listen ', 'answer': 'word for word',
         'after': ' and that is exactly why I lose everything.',
         'hint': 'Hint: catching every single word instead of the meaning'},
        {'before': 'The second time she said it, it was absolutely ', 'answer': 'crystal clear',
         'after': '.', 'hint': 'Hint: two words -- completely easy to understand'},
    ],
    'pc_order_lead': 'Ana and a colleague talk about calls in English. Put the exchange in a logical order.',
    'pc_order': [
        'Do you actually keep up on those calls, or do you wait for the email?',
        'The first two minutes usually go completely over my head.',
        'Same here. And it is not the vocabulary.',
        'No. It is that they say gonna, and they swallow the sound in the middle of twenty.',
        'So what do you do instead?',
        'I take the two words that carry the meaning and I let the small ones go.',
    ],
    'order_voice': 'arthur',
    'pc_squiz': [
        {'q': 'Somebody rattles off three dates and you catch none. The best thing to say is:',
         'opts': [('"Sorry, could you give me those dates again, a bit slower?"', True),
                  ('"Sorry, my English is very bad, please repeat everything."', False),
                  ('"I did not understand nothing of that."', False)]},
        {'q': 'You caught half, and the half you caught is enough to answer. You:',
         'opts': [('Say nothing and hope the rest arrives by email.', False),
                  ('Repeat back what you caught: "So Thursday is off and Friday is on -- right?"', True),
                  ('Ask them to repeat the whole thing from the beginning.', False)]},
        {'q': 'Which of these is the correct spoken form?',
         'opts': [('"He gonna come at eight."', False),
                  ('"He is gonna come at eight."', True),
                  ('"He is going to gonna come at eight."', False)]},
        {'q': 'Somebody asks whether you followed the whole call. You followed most of it. You say:',
         'opts': [('"Yes, everything, no problem." (and hope)', False),
                  ('"Most of it. The first minute went over my head, the rest was fine."', True),
                  ('"No, I never understand anything on calls."', False)]},
    ],
    'pc_think': 'Find any two minutes of English being spoken at natural speed -- a podcast, a video, '
                'anything with no subtitles. Listen twice. Then record yourself saying what you caught, '
                'what you lost, and which reductions you can now name. Do not translate. Describe.',

    # ------------------------------------------------------------ complementares
    'media': [
        {'id': 'series', 'thumb': 'video', 'type': 'Pronunciation',
         'title': "How to Pronounce 'Gonna' and 'Wanna' &mdash; Rachel's English (American)",
         'desc': 'Four minutes on the two reductions that account for a large slice of everything you '
                 'lose on an American call. She shows the mouth, slows the audio down, and then plays '
                 'it at real speed so you hear what you have been missing.',
         'tip': 'Tip: watch it once, then go back to any American recording you have and count how '
                'many times gonna appears. It will be more than you expect.',
         'url': 'https://www.youtube.com/watch?v=2EBBNmNzypY', 'cta': 'Watch on YouTube'},
        {'id': 'podcast', 'thumb': 'podcast', 'type': 'Podcast',
         'title': 'How I Built This &mdash; NPR (free, full episodes)',
         'desc': 'Long interviews with people telling the story of something they built, at the speed '
                 'Americans actually talk to each other. No teaching, no slowing down, and every '
                 'reduction from tonight, live.',
         'tip': 'Tip: this is the fast version. Listen to five minutes with no transcript, then open '
                'the transcript on the NPR page and read what you heard. That order, never the reverse.',
         'url': 'https://www.npr.org/podcasts/510313/how-i-built-this', 'cta': 'Listen on NPR'},
        {'id': 'youtube', 'thumb': 'video', 'type': 'Pronunciation',
         'title': "Tim's Pronunciation Workshop: Assimilation of /t/ and /p/ &mdash; BBC Learning English",
         'desc': 'The British version of the same phenomenon, in three minutes. Sounds do not just '
                 'disappear &mdash; they change into their neighbours. Once you have seen it named you '
                 'cannot unhear it.',
         'tip': 'Tip: compare this with the American video above. The rules are not identical, and '
                'knowing which accent you are hearing is half of understanding it.',
         'url': 'https://www.youtube.com/watch?v=i_ohrkQmzdQ', 'cta': 'Watch on YouTube'},
    ],

    # ------------------------------------------------------------------ teacher
    'teacher': {
        'open': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: '
                '"Tonight, the two minutes you always lose." Esta e uma aula-ANCORA do eixo '
                'intercultural/listening: e o gap que a propria Ana nomeou na consultoria ("a minha '
                'autonomia de compreensao auditiva e muito ruim"). Diga isso a ela com essas palavras.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 8: as frases que '
                  'compram tempo (bear with me, off the top of my head) resolveram a metade em que ELA '
                  'fala. PONTE (REGRA 27B): "That was you talking. Tonight is you listening." Deixe '
                  'responder livre, ZERO correcao. ANOTE se ela atribui o problema a velocidade ou a '
                  'propria capacidade &mdash; a segunda resposta e o alvo emocional da noite.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase que importa e a '
                   'de baixo: ela aprendeu ingles COM espacos entre as palavras, e ninguem fala assim. '
                   'Reenquadre o problema: nao e deficiencia dela, e informacao que nunca lhe deram.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> Escreva "Whaddaya gonna do about it?" e '
                'peca que ela leia em voz alta, rapido. Depois pergunte quantas palavras sao (seis). '
                'Ela conhece todas. Este e o momento em que a aula inteira faz sentido &mdash; nao '
                'passe rapido demais.',
        'tr_vocab': '<strong>Transicao vocab (1 min):</strong> Diga: "Twelve words for speed and noise. '
                    'Click each card." Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ "to '
                  'slur": "Is the person drunk? (Pode ser, mas normalmente e so cansaco ou velocidade '
                  '&mdash; as bordas das palavras somem.)" CCQ "to swallow a sound": "Is the sound '
                  'quiet, or absent? (AUSENTE. Essa e a diferenca que muda tudo.)" CCQ "gonna": "Is it '
                  'slang? (Nao &mdash; e como praticamente todo nativo diz going to, inclusive num '
                  'noticiario.)" Marque a diferenca entre mumble (a pessoa fala mal) e reduction (a '
                  'lingua funciona assim).',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ "word for word": '
                  '"Is it a good strategy? (E a que ela usa, e e a que a derruba.)" CCQ "crystal '
                  'clear" vs "to go over your head": pergunte por um exemplo real de cada uma da '
                  'semana dela. CCQ "to enunciate": "Do native speakers enunciate? (So quando estao '
                  'fazendo esforco por voce &mdash; e por isso que a professora e mais facil que o '
                  'colega.)"',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. '
                    'Certo fica verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note '
                    'como ponte: crystal clear e over your head sao os dois extremos, e o meio tem nome.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> "To slur" &mdash; o L e escuro e o R '
                'americano nao vibra. "Crystal clear" tem dois L escuros seguidos, e e proposital: e '
                'dificil de dizer e facil de ouvir. "A tongue twister" &mdash; o TH de tongue nao '
                'existe, e /t/+ /ʌ/. Na frase inteira, peca que ela COLE "went completely over" sem '
                'pausa. Peca 2 repeticoes de cada.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a expressao que '
                   'falta ANTES de clicar. As candidatas estao no banco embaixo, fora de ordem. Se '
                   'travar, aponte duas e pergunte qual cabe. Clicar de novo fecha (REGRA 27E).',
        'tr_ch3': '<strong>Transicao (1 min):</strong> Diga: "Two people who lose the first two minutes '
                  'of every call. One of them is French." Passe ao proximo.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Marc, FRANCES, colega que tem o mesmo '
                    'problema. Clique "Next Line" e toque o audio de cada fala. Para cada fala da Ana, '
                    'peca que ELA fale primeiro. PONTO PEDAGOGICO: a Ana e quem EXPLICA aqui. Ela '
                    'nunca ocupou esse lugar em ingles, e ocupa-lo e o que transforma conhecimento em '
                    'confianca. PRAGMATICA: o Marc abre com "be honest with me" &mdash; frances vai '
                    'direto ao ponto pessoal muito mais cedo que um britanico faria.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o MARC, nao sobre a '
                         'Ana (REGRA 27F). Ana responde ANTES de revelar. A 3a e a chave da aula: '
                         '"they are not mumbling, the sounds are genuinely not there". Se ela sair da '
                         'aula so com isso, ja valeu.',
        'listen1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES '
                   'de tocar. Este e um AMERICANO em velocidade NORMAL de reuniao &mdash; o audio mais '
                   'dificil que ela ja teve neste material, e isso e proposital. AVISE: "This one is '
                   'fast. You are not supposed to get all of it on the first play." Toque 3 vezes se '
                   'preciso, e use 0.75x na segunda. Depois peca que ela aponte UMA reducao que ouviu '
                   '(gonna, coulda, wanna, hasn&rsquo;t).',
        'tr_grammar': '<strong>Transicao (1 min):</strong> Diga: "Four sentences, twice each. Left is '
                      'how it is written. Right is how it is said." Passe ao proximo.',
        'grammar': '<strong>Sound discovery (7 min):</strong> Peca que ela leia o lado ESQUERDO devagar '
                   'e o DIREITO rapido, em voz alta, quatro vezes. Depois pergunte: "Which sounds '
                   'disappeared, and which ones only moved?" Espere ela perceber sozinha que quase '
                   'nada some &mdash; quase tudo se junta. So entao clique "Reveal the Rule". CCQ: '
                   '"gonna &mdash; where did the TO go? (Esta dentro. Por isso wanna to nao existe.)" '
                   'NAO de a regra antes.',
        'mistake': '<strong>Common mistake (4 min):</strong> Tres dos quatro sao o mesmo erro: gonna, '
                   'wanna e gotta JA CONTEM o to, e o aluno acrescenta outro. O terceiro e diferente: '
                   'gonna substitui "going to", nunca "is going to" &mdash; o verbo be fica. AVISO '
                   'IMPORTANTE que ela precisa ouvir de voce: estas formas sao FALADAS. Reconhecer e '
                   'obrigatorio, produzir e opcional, escrever em e-mail e erro.',
        'gpractice': '<strong>Practice (4 min):</strong> Aqui ela ESCREVE a forma reduzida, o que e '
                     'estranho de proposito: escrever "didja" uma vez fixa o som melhor do que ouvir '
                     'dez. Ana diz em voz alta antes de clicar. Se travar, diga a forma completa e peca '
                     'que ela acelere ate colar.',
        'listen2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA ANTES de tocar. '
                   'Esta e uma FRANCESA falando ingles: R uvular ocasional, H inicial que some, stress '
                   'mais uniforme, vogais puras. Avise ANTES. Este audio e o par emocional do listening '
                   '1: a mulher passou DOZE ANOS achando que o ingles dela era falso, pelo mesmo motivo '
                   'que a Ana acha. E o conselho final dela (rapido primeiro, transcript depois) e '
                   'exatamente o homework.',
        'artifact': '<strong>Artefato (5 min):</strong> E um recado de voz transcrito EXATAMENTE como '
                    'foi falado. Peca que a Ana leia cada linha em voz alta e depois diga a versao de '
                    'livro. Este e o melhor termometro da aula: se ela reconstruir as seis linhas, ela '
                    'consegue decodificar fala rapida. Se travar numa, e a reducao que ela precisa '
                    'treinar na semana.',
        'tr_practice': '<strong>Transicao practice (1 min):</strong> Diga: "Now we train: detective, '
                       'quick fire, and building." Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. "What is wrong '
                     'here?" Ana corrige ANTES de clicar. Sao os quatro do slide de Common Mistake.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez, resposta em voz alta '
                     'ANTES das Tips. INTERCULTURAL: compare a 3a com a 4a. Com o americano, um pedido '
                     'direto e normal; com o nordico, "what?" soa agressivo e "pardon" e o padrao. Ela '
                     'viveu isso na pele em anos de empresa indiana &mdash; puxe a experiencia dela.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. '
                    'A 2a e a mais importante: ela tem de declarar em voz alta a MUDANCA de metodo. '
                    'Exija a frase concreta, nunca a intencao vaga.',
        'build': '<strong>Sentence Building (4 min):</strong> Aqui ela produz a forma REDUZIDA em voz '
                 'alta. Nao aceite a versao lenta e correta &mdash; peca de novo, rapido, ate colar. '
                 'Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO no fim. '
                     'A ultima linha e a mais importante de todas: a estrategia, nao a lista. Peca que '
                     'ela fotografe a tela.',
        'tr_roleplay': '<strong>Transicao role-play (1 min):</strong> Diga: "Now you stop me. Three '
                       'times, and without apologising once." Passe ao proximo.',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce da um update em velocidade REAL, como o '
               'listening 1. Nao facilite. Ela tem de interromper TRES vezes, dos tres jeitos '
               'indicados. Se ela pedir desculpas pelo ingles dela, PARE e peca de novo sem o pedido de '
               'desculpas &mdash; e o habito mais caro que ela tem.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e o Marc de novo. Ana pergunta antes '
               'de aconselhar e depois conta o que MUDOU no metodo dela. Se ela der teoria, devolva: '
               '"What do you actually do, in the second after you lose a word?"',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO '
               'corrija durante. Peca especificamente que ela nomeie DUAS reducoes. Se ela conseguir '
               'explicar o fenomeno para um leigo, ela entendeu de verdade &mdash; explicar e o teste '
               'mais duro que existe.',
        'tr_wrap': '<strong>Transicao wrap-up (1 min):</strong> Diga: "You have just explained connected '
                   'speech to somebody, in English. Nine lessons ago you thought people were mumbling."',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a '
                    'Ana repita. As cinco cobrem o ciclo inteiro: admitir que perdeu, pedir de novo, '
                    'confirmar o que pegou, nomear o problema e fechar. Nenhuma delas pede desculpa '
                    'pelo ingles &mdash; aponte isso.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: "Click each item if you feel confident." '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 9 registrada como '
                     'concluida no passaporte.',
        'closing': '<strong>Encerramento (2 min):</strong> Diga: "Nine lessons in, Ana, and tonight you '
                   'stopped believing that people were mumbling at you." Homework (oralmente, '
                   'opcional): dois minutos de audio real sem legenda, duas escutas, depois o '
                   'transcript &mdash; NUNCA o transcript primeiro. Proxima aula: I Used to Live in the '
                   'City &mdash; used to e would, os habitos que ficaram para tras.',
    },
}
