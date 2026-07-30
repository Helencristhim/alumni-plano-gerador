# -*- coding: utf-8 -*-
"""Aula 7 -- The House I'm Restoring (passive voice em contexto real).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques do listening (CURRICULO V3): holandes + australiano.
Callback da aula 6: a decisao de sair de SP -- a casa e o que veio DEPOIS daquela terca.
"""

LESSON = {
    'n': 7,
    'menu_title': "The House I'm Restoring",
    'menu_desc': 'The house that came after the decision -- talking about work that was done, '
                 'is being done and still has to be done, without ever naming who did it',
    'grammar_point': 'passive voice',
    'chapter_tag': 'The Work of the House',
    'title_html': 'The House <span class="accent">I&rsquo;m Restoring</span>',
    'title_sub': 'A house tells you what was done to it long before anybody tells you who did it.',
    'phases': ['First Words', 'The Words of the House', 'What Was Done',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],

    # ---------------------------------------------------------------- chapter 1
    'warmup': {
        'heading': 'The House Was Already <span class="accent">There</span>',
        'callback': 'Last time you told us about the Tuesday: the traffic, the last straw, '
                    'the notice you handed in. This house is what that Tuesday turned into. '
                    'It was standing there long before you were, and other people had already '
                    'been working on it for a century.',
        'question': 'What is the first thing that was done to the house after you got the keys?',
    },
    'framing': {
        'heading': 'The Work, and Then <span class="accent">the Worker</span>',
        'steps': [('The Words', 'plaster, beams, damp, sagging, a quote...'),
                  ('The House', 'two people who took one on, and what it cost them'),
                  ('Your Rooms', 'the tour, in English, with no notes')],
        'note': 'Anybody can say <strong>a builder replaced the roof in 2019</strong>. Tonight you say '
                '<strong>the roof was replaced in 2019</strong> &mdash; and the sentence stops being about '
                'a builder you never met and starts being about your house.',
    },
    'hook': {
        'label': 'Who Did It?',
        'heading': 'Nobody Asks <span class="accent">Who</span>',
        'line1': 'When somebody walks into an old house, they never ask who plastered the wall. '
                 'They ask what has been done and what is still waiting.',
        'line2': 'Tell me one room. What has been finished, and what has not been touched since '
                 'the day you arrived?',
    },

    # ---------------------------------------------------------------- chapter 2
    'vocab_heading': 'The Language of <span class="accent">an Old House</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'To strip back', 'icon': 'brush',
         'def': 'To take the old paint or paper off until only the bare surface is left',
         'ex': 'Every wall in the back room had to be stripped back to the brick.',
         'match': 'to take the old paint or paper off down to the bare surface'},
        {'word': 'To gut', 'icon': 'tool',
         'def': 'To empty a room completely, until only the walls and the floor are left',
         'ex': 'The kitchen was gutted in a single weekend.',
         'match': 'to empty a room completely, leaving only walls and floor'},
        {'word': 'To rewire', 'icon': 'bolt',
         'def': 'To replace all the old electrical wiring in a building',
         'ex': 'The ground floor is being rewired at the moment.',
         'match': 'to replace all the old electrical wiring in a building'},
        {'word': 'Damp', 'icon': 'wave',
         'def': 'The wet that gets into old walls and slowly ruins them from inside',
         'ex': 'There was damp coming up through the kitchen wall.',
         'match': 'the wet that gets into old walls and ruins them slowly'},
        {'word': 'Beam', 'icon': 'layers',
         'def': 'A long, thick piece of wood that holds a roof or a ceiling up',
         'ex': 'One beam under the roof had to be replaced completely.',
         'match': 'a long thick piece of wood that holds a roof or a ceiling up'},
        {'word': 'Plaster', 'icon': 'grid',
         'def': 'The smooth grey layer that goes on a wall before any paint does',
         'ex': 'The old plaster came off the wall in sheets.',
         'match': 'the smooth layer that goes on a wall before any paint'},
        {'word': 'Sagging', 'icon': 'scale',
         'def': 'Bending down in the middle because it is old or badly supported',
         'ex': 'The ceiling in the back room is sagging in the middle.',
         'match': 'bending down in the middle from age or poor support'},
        {'word': 'Sturdy', 'icon': 'shield',
         'def': 'Strong, solid and unlikely to break or move',
         'ex': 'The beams are a hundred and forty years old and still completely sturdy.',
         'match': 'strong and solid, unlikely to break or move'},
        {'word': 'A quote', 'icon': 'doc',
         'def': 'The written price a builder gives you before any work starts',
         'ex': 'The first quote we got was almost twice the second one.',
         'match': 'the written price a builder gives you before starting'},
        {'word': 'To take something on', 'icon': 'anchor',
         'def': 'To accept a difficult job knowing how much it is going to demand',
         'ex': 'Everyone asked why I took on a house nobody else wanted.',
         'match': 'to accept a difficult job knowing what it will demand'},
        {'word': 'To cut corners', 'icon': 'arrow', 'expr': True,
         'def': 'To do a job faster and cheaper by skipping the steps that matter',
         'ex': 'The previous owner cut corners everywhere, and we are still paying for it.',
         'match': 'to do a job cheaply by skipping the steps that matter'},
        {'word': 'A money pit', 'icon': 'home', 'expr': True,
         'def': 'A building that keeps swallowing money long after you expected it to stop',
         'ex': 'Everybody warned me the place would turn into a money pit.',
         'match': 'a building that keeps swallowing money with no end'},
    ],
    'vocabnote': "Two of tonight's twelve are whole expressions, not single words: to cut corners "
                 'and a money pit. Keep them intact. Somebody who drops a money pit into a '
                 'conversation about a house sounds like a person who has actually owned one.',
    'pron': ['Plaster', 'Sturdy', 'A money pit',
             'The whole ground floor is being rewired.'],
    'gapfill': [
        {'before': 'There was ', 'answer': 'damp', 'after': ' coming up through the kitchen wall.'},
        {'before': 'The old ', 'answer': 'plaster', 'after': ' came off the wall in sheets.'},
        {'before': 'The ceiling in the back room is ', 'answer': 'sagging', 'after': ' in the middle.'},
        {'before': 'These beams are a hundred and forty years old and still completely ',
         'answer': 'sturdy', 'after': '.'},
        {'before': 'The previous owner ', 'answer': 'cut corners',
         'after': ' everywhere, and we are still paying for it.'},
        {'before': 'Everybody warned me the place would turn into a ',
         'answer': 'money pit', 'after': '.'},
    ],

    # ---------------------------------------------------------------- chapter 3
    'ch3_heading': 'Two People Who <span class="accent">Took One On</span>',
    'ch3_sub': 'A conversation, then a voice from Rotterdam',
    'dialogue': {
        'name': 'Maddie', 'cls': 'maddie', 'initial': 'M', 'voice': 'australian_f',
        'heading': 'She Bought One <span class="accent">Too</span>',
        'lines': [
            {'who': 'maddie', 'text': 'Ana, someone told me you bought an old place in the interior. '
                                      'Ours is a hundred and ten years old and I am starting to think it is '
                                      'a <span class="vocab-highlight">money pit</span>.'},
            {'who': 'ana', 'text': 'Everybody said that to me too. How much has actually been done so far?'},
            {'who': 'maddie', 'text': 'The kitchen was <span class="vocab-highlight">gutted</span> in January, '
                                      'and the whole back of the house is being '
                                      '<span class="vocab-highlight">rewired</span> right now. '
                                      'The rest has not been touched.'},
            {'who': 'ana', 'text': 'Has anything been done about the '
                                   '<span class="vocab-highlight">damp</span>? That is the one thing '
                                   'you cannot leave.'},
            {'who': 'maddie', 'text': 'Not yet. Two <span class="vocab-highlight">quotes</span> have been sent to '
                                      'us and both of them are terrifying.'},
            {'who': 'ana', 'text': 'Take the expensive one. Mine was done cheaply by somebody who '
                                   '<span class="vocab-highlight">cut corners</span>, and the whole wall '
                                   'had to be <span class="vocab-highlight">stripped back</span> again '
                                   'eighteen months later.'},
            {'who': 'maddie', 'text': 'That is exactly what I was afraid of. Were your '
                                      '<span class="vocab-highlight">beams</span> all right?'},
            {'who': 'ana', 'text': 'One was <span class="vocab-highlight">sagging</span> and had to be replaced. '
                                   'The other six are original and still completely '
                                   '<span class="vocab-highlight">sturdy</span>. I have no idea why '
                                   'I <span class="vocab-highlight">took it on</span>, and I would do it again.'},
        ],
        'comp': [
            ('What has already been done to Maddie&rsquo;s house, and what is being done right now?',
             'The kitchen was gutted in January, and the whole back of the house is being rewired '
             'at this moment. Everything else has not been touched.'),
            ('What is stopping Maddie from dealing with the damp?',
             'The price. Two quotes have been sent to her and, in her words, both of them are terrifying.'),
            ('What does Ana warn her about, and what happened to Ana because of it?',
             'She warns her not to take the cheap option. Ana&rsquo;s own damp work was done by somebody '
             'who cut corners, and the wall had to be stripped back again eighteen months later.'),
        ],
    },
    'listenings': [
        {'voice': 'dutch_m',
         'heading': 'Nothing Had Been Done <span class="accent">Since 1974</span>',
         'intro': 'A Dutch man on the house he bought in Rotterdam. Sound first &mdash; no text.',
         'text': "I will be honest with you, the house was in a terrible state and I knew it. Nothing "
                 "had been done to it since about nineteen seventy four. You could see it from the "
                 "street. But the price was very low, and the reason the price was very low is that "
                 "everybody else had walked away. The roof was fine, actually, which surprised me. "
                 "The beams were inspected before I made the offer and they were declared completely "
                 "sound, which is the only reason I went ahead. Everything else was wrong. The whole "
                 "of the ground floor had to be rewired because the wiring was original, and I mean "
                 "original. The kitchen was gutted in one weekend by four friends and a lot of beer. "
                 "And then the damp. The damp is what nobody warns you about. Two walls were stripped "
                 "back to the brick and left open for a month, and I lived with plastic sheeting for "
                 "the whole of that winter. People ask me if I regret it. No. But I would never tell "
                 "anybody it was cheap.",
         'comp': [
             ('What condition was the house in when he bought it, and why was the price so low?',
              'Nothing had been done to it since about nineteen seventy four, and it showed from the '
              'street. The price was low because everybody else had walked away.'),
             ('What was the one thing that made him go ahead with the purchase?',
              'The beams. They were inspected before he made the offer and declared completely sound. '
              'The roof was fine too, which surprised him.'),
             ('What does he say nobody warns you about, and what did it cost him?',
              'The damp. Two walls were stripped back to the brick and left open for a month, and he '
              'lived with plastic sheeting for a whole winter.'),
         ]},
        {'voice': 'australian_m',
         'heading': 'Everything I Was <span class="accent">Told to Skip</span>',
         'intro': 'An Australian builder on the corners people ask him to cut. Sound first &mdash; no text.',
         'text': "I have been doing this for twenty six years and I get asked the same question every "
                 "single week. Can we skip that bit. And the honest answer is yes, you can skip almost "
                 "any of it, and almost all of it will come back. Damp is the classic. I am asked to "
                 "paint over damp maybe twice a month, and I say no, because in eight months that wall "
                 "will be exactly where it was, only now there is a coat of paint on it that has to be "
                 "removed as well. Plaster is another one. Plaster has to be left to dry properly and "
                 "nobody wants to hear that, because it means three more weeks of living in a building "
                 "site. The one thing I will never let anybody skip is anything structural. If a beam is "
                 "sagging it gets replaced, and I will walk off a job over that. Here is the thing "
                 "people find hard. A house that has been done properly does not look any better on the "
                 "day it is finished. It only looks better in ten years.",
         'comp': [
             ('What question is he asked every week, and what is his honest answer?',
              'People ask him if a step can be skipped. He says almost any of it can be skipped, and '
              'almost all of it will come back.'),
             ('Why does he refuse to paint over damp?',
              'Because in eight months the wall will be exactly where it was, only now with a coat of '
              'paint on it that has to be removed as well.'),
             ('What will he never let anybody skip, and what does he say about a house that has been '
              'done properly?',
              'Anything structural &mdash; a sagging beam gets replaced and he will walk off a job over '
              'it. A house done properly does not look better on the day it is finished; it only looks '
              'better in ten years.'),
         ]},
    ],

    # ---------------------------------------------------------------- chapter 4
    'grammar': {
        'ch_heading': 'The Work Comes <span class="accent">First</span>',
        'ch_sub': 'was replaced &middot; is being rewired &middot; has been repaired &mdash; and no builder anywhere',
        'heading': 'Where Is the <span class="accent">Person</span>?',
        'examples': [
            'The roof was replaced two years before I bought the house.',
            'The whole ground floor is being rewired at the moment.',
            'That wall has been plastered three times, and it is still not flat.',
            'These beams were cut by hand, about a hundred and forty years ago.',
        ],
        'prompt': 'Somebody replaced the roof. Somebody is rewiring the floor. In all four sentences, '
                  'where is that somebody? And ask yourself the better question: does the house care?',
        'table': [
            ('be + past participle', 'The general shape. The <strong>thing done</strong> matters more than '
                                     'who did it.', 'The roof <strong>was replaced</strong>.'),
            ('present simple passive', 'How it normally is, or how it is normally done.',
             'Old floors <strong>are sanded</strong> before they are sealed.'),
            ('present continuous passive', 'Happening <strong>right now</strong>.',
             'The kitchen <strong>is being rewired</strong> this week.'),
            ('present perfect passive', 'Finished, with a result you can <strong>still see</strong>.',
             'That wall <strong>has been plastered</strong> twice.'),
            ('past simple passive', 'Finished, at a known moment in the past.',
             'The beams <strong>were cut</strong> by hand.'),
            ('by + person', 'Only when who did it is <strong>the news</strong>. Usually you leave it out.',
             'It was built <strong>by a Portuguese carpenter</strong>.'),
            ('get + past participle', 'The spoken, everyday version. Common in speech, rare in writing.',
             'A window <strong>got broken</strong> in the storm.'),
        ],
        'oneliner': 'the passive puts the work first and the worker last &mdash; or nowhere at all.',
    },
    'mistakes': [
        ('The house was build in 1948.', 'The house was built in 1948.'),
        ('The kitchen is rewiring this week.', 'The kitchen is being rewired this week.'),
        ('The floors have sanded already.', 'The floors have already been sanded.'),
        ('The fire was happened in the old kitchen.', 'The fire happened in the old kitchen.'),
    ],
    'mistake_note': 'Three of these four are the same habit: the little verb <strong>be</strong> goes '
                    'missing, or the participle turns back into an infinitive. The fourth is the '
                    'opposite problem &mdash; <strong>happen</strong> has no passive at all, because '
                    'nobody happens anything.',
    'gpractice_heading': 'Which <span class="accent">Passive?</span>',
    'gpractice': [
        {'before': 'The roof ', 'answer': 'was replaced',
         'after': ' two years before I bought the place.', 'cue': 'replace &mdash; finished, known moment'},
        {'before': 'The whole ground floor ', 'answer': 'is being rewired',
         'after': ' at the moment.', 'cue': 'rewire &mdash; happening right now'},
        {'before': 'That wall ', 'answer': 'has been plastered',
         'after': ' three times, and it is still not flat.', 'cue': 'plaster &mdash; finished, result still visible'},
        {'before': 'Nothing ', 'answer': 'has been done',
         'after': ' to this house since 1998.', 'cue': 'do &mdash; careful with the participle'},
        {'before': 'Old floors ', 'answer': 'are sanded',
         'after': ' before they are sealed.', 'cue': 'sand &mdash; how it is normally done'},
    ],
    'artifact': {
        'heading': 'The Builder&rsquo;s <span class="accent">Quote</span>',
        'doc_title': 'QUOTE &mdash; A. VERALDI',
        'doc_sub': 'Ref 0714 &middot; valid for 30 days',
        'doc_right': 'Page 1 of 1<br>Not a contract',
        'rows': [
            ('Item 01', 'Existing plaster stripped back to the brick, all four walls of the back room'),
            ('Item 02', 'Roof beams inspected; one sagging beam replaced, the rest treated and left'),
            ('Item 03', 'Ground floor rewired; the original fuse box removed and taken away'),
            ('Item 04', 'Damp treated along the kitchen wall, then left open for three weeks'),
            ('Item 05', 'Walls replastered and left to dry for 21 days before any paint is applied'),
            ('Not included', 'Floors, windows and chimney. A separate quote will be sent next week.'),
        ],
        'comp': [
            ('Say item 02 as one full sentence. Which two passives does it need?',
             '"The roof beams were inspected, one sagging beam was replaced, and the rest were treated '
             'and left." Past simple passive throughout &mdash; the work is finished and the date is known.'),
            ('Say item 05 in the present, as the builder would describe his method.',
             '"The walls are replastered and left to dry for twenty one days before any paint is applied." '
             'Present simple passive &mdash; this is how it is always done, not one particular wall.'),
            ('Read the last line. Why is <em>a separate quote will be sent</em> better here than '
             '<em>we will send you a separate quote</em>?',
             'Because the company is not the point and everybody already knows who is sending it. The '
             'passive keeps the quote itself in the position of importance &mdash; which is also why it '
             'sounds more formal and more careful.'),
        ],
    },

    # ---------------------------------------------------------------- chapter 5
    'detective': [
        ('The house was build in 1948.', 'The house was built in 1948.'),
        ('The kitchen is rewiring this week.', 'The kitchen is being rewired this week.'),
        ('The floors have sanded already.', 'The floors have already been sanded.'),
        ('The fire was happened in the old kitchen.', 'The fire happened in the old kitchen.'),
    ],
    'quickfire': [
        {'situation': 'A visitor walks into the back room and asks what has been done in there so far. '
                      'Answer with two finished things and one thing still in progress.',
         'tips': ['The plaster has been stripped back and the wiring has been replaced.',
                  'The ceiling is being repaired at the moment.']},
        {'situation': 'Somebody asks who did the work on your kitchen. You have no idea what the man '
                      'was called. Answer anyway, without inventing a name.',
         'tips': ['It was done before I bought the place.',
                  'You do not need by somebody when you do not know, or do not care, who.']},
        {'situation': 'A builder offers to paint straight over the damp because it is faster. Refuse, '
                      'and say why.',
         'tips': ['I would rather not. The wall was painted over once already.',
                  'If corners are cut there, the whole thing has to be done again in a year.']},
        {'situation': 'A friend asks whether the house was a good decision, financially. Be honest '
                      'rather than positive.',
         'tips': ['It has turned into a bit of a money pit, if I am honest.',
                  'More has been spent on it than I planned. I would still take it on again.']},
        {'situation': 'Your builder asks whether to replace a sagging beam or treat it. Give him your '
                      'answer and your reason.',
         'tips': ['Replace it. Nothing structural gets skipped in this house.',
                  'A beam that is sagging now will be worse in five years.']},
        {'situation': 'Somebody asks what still has not been touched since you moved in. Name two '
                      'things and say when you expect them to be dealt with.',
         'tips': ['The windows have not been touched at all.',
                  'The chimney is going to be looked at next winter.']},
    ],
    'speaking': [
        ('What had already been done to the house before you bought it?',
         'Almost nothing. The roof had been replaced at some point, and the rest had not been touched in decades.'),
        ('What is being done right now?',
         'The back room is being replastered, and the ground floor is being rewired a section at a time.'),
        ('Has anything in the house been done badly and had to be done again?',
         'Yes. The damp was treated cheaply by somebody who cut corners, and the whole wall had to be stripped back again.'),
        ('What has not been touched since the day you got the keys?',
         'The windows and the chimney. Nothing has been done to either of them, and I am in no hurry.'),
    ],
    'build': [
        ('the roof / replace + two years before I bought it (finished, known date)',
         'The roof was replaced two years before I bought it.'),
        ('the ground floor / rewire + right now (in progress)',
         'The ground floor is being rewired right now.'),
        ('that wall / plaster + three times (finished, result still visible)',
         'That wall has been plastered three times.'),
        ('nothing / do + to this house since 1998 (negative, result still visible)',
         'Nothing has been done to this house since 1998.'),
    ],
    'answerkey_heading': 'Every Passive on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole passive key',
    'answerkey': [
        'be + past participle = the general shape: the work first, the worker last or nowhere',
        'past simple passive = finished, at a known moment: the roof was replaced in 2019',
        'present simple passive = how it is normally done: old floors are sanded before they are sealed',
        'present continuous passive = happening now: the kitchen is being rewired this week',
        'present perfect passive = finished, result still visible: that wall has been plastered twice',
        'by + person = ONLY when who did it is the news: it was built by a Portuguese carpenter',
        'get + past participle = the spoken version: a window got broken in the storm',
        'NEVER: was build &middot; is rewiring (when you mean is being rewired) &middot; have sanded '
        '(when you mean have been sanded) &middot; was happened',
    ],

    # ---------------------------------------------------------------- chapter 6
    'rp_ch_heading': 'Show Me <span class="accent">the House</span>',
    'roleplay': {
        'guided': {
            'heading': 'The Builder on <span class="accent">the Phone</span>',
            'scenario': 'I am a builder you have never met, calling about the quote. I ask three things: '
                        'what has already been done, what is being done at the moment, and what has not '
                        'been touched at all. Answer each one with a passive.',
            'chips': ['has been stripped back', 'is being rewired', 'has not been touched'],
        },
        'semi': {
            'heading': 'Maddie Asks You <span class="accent">What to Do</span>',
            'scenario': 'I am Maddie again, and I have two quotes for the damp: one cheap, one that '
                        'frightens me. Ask me two questions about my house before you give me any '
                        'opinion &mdash; then tell me what was done to yours and what it cost you.',
            'chips': ['cut corners', 'stripped back again', 'a money pit'],
        },
        'free': {
            'heading': 'Two Minutes, <span class="accent">Room by Room</span>',
            'scenario': 'Walk me through the house one room at a time. In each room tell me what was '
                        'done before you arrived, what has been done since, what is being done now, and '
                        'what you have decided to leave exactly as it is.',
        },
    },

    # ---------------------------------------------------------------- chapter 7
    'wrap_heading': 'The Work, <span class="accent">Not the Worker</span>',
    'survival_heading': 'Five Phrases for <span class="accent">an Old House</span>',
    'survival': [
        'Nothing had been done to it since the seventies.',
        'The ground floor is being rewired at the moment.',
        'That wall has been plastered three times already.',
        'The damp was treated by somebody who cut corners.',
        'The windows have not been touched, and I am in no hurry.',
    ],
    'checklist': [
        'I can say what was done to a place without naming who did it.',
        'I use is being done for the work that is happening right now.',
        'I use has been done when the result is still there in front of me.',
        'I never say was build, is rewiring or was happened.',
        'I know the words: plaster, beams, damp, sagging, sturdy, a quote, to cut corners, a money pit.',
    ],
    'closing': {
        'badge': 'The Restorer Badge <span class="accent">Earned!</span>',
        'text': 'You walked a stranger through a hundred year old house in English tonight, Ana, and '
                'not once did you have to invent the name of a builder to do it.',
        'next': 'Checkpoint &mdash; Block 1',
    },

    # ---------------------------------------------------------------- pre-class
    'pc_title': "The House I'm Restoring -- What Was Done, and What Is Still Waiting",
    'pc_desc': 'Talking about an old house without naming who did the work. Key words: to strip back, '
               'to gut, to rewire, damp, beam, plaster, sagging, sturdy, a quote, to take something on, '
               'to cut corners, a money pit. Structure: the passive voice -- was done, is being done, '
               'has been done.',
    'pc_context': {
        'paras': [
            'The house <strong>was built</strong> in 1912 and almost nothing <strong>had been done</strong> '
            'to it since the seventies. The <strong>plaster</strong> was falling off the walls, there was '
            '<strong>damp</strong> in the kitchen, and one ceiling was visibly <strong>sagging</strong>.',
            'Two <strong>quotes</strong> <strong>were sent</strong> to Ana before she chose a builder. The '
            'cheaper one <strong>was rejected</strong>, because the man who wrote it wanted to paint '
            'straight over the damp. That is exactly how the previous owner <strong>cut corners</strong>, '
            'and the same wall had to <strong>be stripped back</strong> twice.',
            'Today the back room <strong>is being replastered</strong> and the ground floor '
            '<strong>is being rewired</strong>. The <strong>beams</strong> <strong>were inspected</strong> '
            'before anything else started: one <strong>was replaced</strong>, the other six '
            '<strong>were declared</strong> completely <strong>sturdy</strong>. The windows '
            '<strong>have not been touched</strong>. Ana knew what she '
            '<strong>was taking on</strong>, and she still calls the place <strong>a money pit</strong>, '
            'affectionately.',
        ],
        'quiz': [
            {'q': 'Why does the text say "the house was built in 1912" and not "somebody built the house in 1912"?',
             'opts': [('Because the builder is unknown, irrelevant, or both &mdash; the house is the subject.', True),
                      ('Because the passive is always more polite than the active.', False),
                      ('Because English avoids dates in active sentences.', False)]},
            {'q': '"The back room is being replastered." What does this form tell you?',
             'opts': [('That the work is planned but has not started.', False),
                      ('That the work is in progress right now, unfinished.', True),
                      ('That the work was finished a long time ago.', False)]},
            {'q': '"The windows have not been touched." Why the present perfect passive here?',
             'opts': [('Because the result is still true today: they are untouched as you read this.', True),
                      ('Because the windows do not exist yet.', False),
                      ('Because the sentence is about a specific date in the past.', False)]},
        ],
    },
    'pc_tip': {
        'title': 'The Passive Voice',
        'lead': 'The work goes first. The worker goes last, or nowhere at all.',
        'table': [
            ('be + past participle', 'The general shape of every passive',
             'The roof <strong>was replaced</strong>.'),
            ('present simple passive', 'How it is normally done',
             'Old floors <strong>are sanded</strong> before they are sealed.'),
            ('present continuous passive', 'Happening right now',
             'The kitchen <strong>is being rewired</strong>.'),
            ('present perfect passive', 'Finished, result still visible',
             'That wall <strong>has been plastered</strong> twice.'),
            ('past simple passive', 'Finished, at a known moment',
             'The beams <strong>were cut</strong> by hand.'),
            ('by + person', 'Only when who did it is the news',
             'It was built <strong>by a Portuguese carpenter</strong>.'),
            ('get + past participle', 'The spoken, everyday version',
             'A window <strong>got broken</strong> in the storm.'),
        ],
        'never': 'The house was build &middot; the kitchen is rewiring &middot; the floors have sanded '
                 '&middot; the fire was happened. Two of those lose the verb be, one loses the participle, '
                 'and the last one makes a passive out of a verb that cannot have one.',
    },
    'pc_blanks': [
        {'before': 'The house ', 'answer': 'was built', 'after': ' in 1912, and the beams are original.',
         'hint': 'Hint: build -- finished, at a known moment in the past'},
        {'before': 'The ground floor ', 'answer': 'is being rewired', 'after': ' at the moment.',
         'hint': 'Hint: rewire -- the work is happening right now, three words'},
        {'before': 'That wall ', 'answer': 'has been plastered', 'after': ' three times already.',
         'hint': 'Hint: plaster -- finished, and the result is still there'},
        {'before': 'Nothing ', 'answer': 'has been done', 'after': ' to this house since 1998.',
         'hint': 'Hint: do -- careful with the participle'},
        {'before': 'The damp was treated by somebody who ', 'answer': 'cut corners',
         'after': ', and we are still paying for it.',
         'hint': 'Hint: to do a job cheaply by skipping the steps that matter'},
        {'before': 'Everybody warned me the place would turn into a ', 'answer': 'money pit',
         'after': '.', 'hint': 'Hint: a building that keeps swallowing money, two words'},
    ],
    'pc_order_lead': 'Somebody asks Ana about the house. Put the exchange in a logical order.',
    'pc_order': [
        'So what state was it in when you got the keys?',
        'Terrible. Nothing had been done to it since the seventies.',
        'And what is happening now?',
        'The back room is being replastered and the ground floor is being rewired.',
        'Is there anything you have decided to leave alone?',
        'The windows. They have not been touched, and I am in no hurry.',
    ],
    'order_voice': 'arthur',
    'pc_squiz': [
        {'q': 'A visitor asks what has been done to the back room. You answer:',
         'opts': [('"The plaster has been stripped back and the ceiling is being repaired."', True),
                  ('"Somebody has stripped the plaster and somebody repairs the ceiling."', False),
                  ('"The plaster has stripped back and the ceiling is repairing."', False)]},
        {'q': 'You want to say the wiring work is happening at this moment. The natural version is:',
         'opts': [('"The ground floor is rewiring this week."', False),
                  ('"The ground floor is being rewired this week."', True),
                  ('"The ground floor was rewiring this week."', False)]},
        {'q': 'A builder offers to paint over the damp. You refuse politely:',
         'opts': [('"No. You are trying to cheat me like the last one."', False),
                  ('"I would rather not. That wall was painted over once already, and it had to be stripped back."', True),
                  ('"The wall was happened before, so no."', False)]},
        {'q': 'Somebody asks who replastered the walls. You have no idea. The natural answer is:',
         'opts': [('"It was done before I bought the place."', True),
                  ('"It was done by somebody, I think by a man."', False),
                  ('"Nobody was plastered the walls."', False)]},
    ],
    'pc_think': 'Describe one room of a place you have lived in, using the passive at least four times. '
                'Say what had been done before you arrived, what has been done since, what is being done '
                'now, and what you have decided to leave exactly as it is.',

    # ------------------------------------------------------------ complementares
    'media': [
        {'id': 'series', 'thumb': 'doc', 'type': 'Documentary',
         'title': 'One Year of Renovating an Abandoned 500 Year Old Cottage (Cotswolds, England)',
         'desc': 'A couple buy a cottage that has not been lived in for years and spend a year on it. '
                 'Beams, damp, plaster, structural work, and every conversation you are about to have '
                 'with your own builder &mdash; in a broad English accent, at natural speed.',
         'tip': 'Tip: the whole film is people describing work that was done to a building. Watch ten '
                'minutes and write down every passive you hear. You will fill a page.',
         'url': 'https://www.youtube.com/watch?v=461NRE6LOeE', 'cta': 'Watch on YouTube'},
        {'id': 'podcast', 'thumb': 'podcast', 'type': 'Podcast',
         'title': '99% Invisible &mdash; The House That Came in the Mail',
         'desc': 'For thirty years you could order an entire house from a catalogue in the United States: '
                 'it arrived on a train in thousands of numbered pieces, and you built it yourself. The '
                 'episode is about who built the houses people live in, and how little of it was decided '
                 'by an architect.',
         'tip': 'Tip: this show is famous for how clearly it is narrated. Listen once without stopping, '
                'then again with the transcript on the page, which is free.',
         'url': 'https://99percentinvisible.org/episode/the-house-that-came-in-the-mail/',
         'cta': 'Listen on 99% Invisible'},
        {'id': 'youtube', 'thumb': 'video', 'type': 'Talk',
         'title': 'Architecture for the people by the people &mdash; Alastair Parvin, TED (13 min)',
         'desc': 'A British architect argues that almost every building in the world was designed by '
                 'somebody who was never an architect, and asks what happens when ordinary people get '
                 'the tools. It is the intellectual version of what you are doing to your own house.',
         'tip': 'Tip: he speaks fast and with a strong English accent. Try it once with no subtitles and '
                'aim only for the main argument &mdash; then turn them on and check how much you had.',
         'url': 'https://www.ted.com/talks/alastair_parvin_architecture_for_the_people_by_the_people',
         'cta': 'Watch on TED'},
    ],

    # ------------------------------------------------------------------ teacher
    'teacher': {
        'open': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A) &mdash; voce ja '
                'cumprimentou ao vivo. Va direto: "Tonight, one house." O recorte: na aula 6 ela contou a '
                'DECISAO de sair de Sao Paulo. Hoje ela fala do que veio depois &mdash; a casa em restauro '
                '&mdash; e falar de uma casa velha em ingles e falar no PASSIVO quase o tempo todo, que e o '
                'alvo da noite.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 6: a terca no transito, o '
                  'last straw, o handed in my notice. Faca a PONTE (REGRA 27B): "That Tuesday turned into a '
                  'house. Show me the house." Deixe falar livre, ZERO correcao. ANOTE se ela usa passivo '
                  'espontaneamente ou se resolve tudo com "they did" / "the man did" &mdash; e o diagnostico '
                  'do capitulo 4.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre o mapa em 3 passos. Deixe claro o alvo: nao '
                   'e "o passivo" como tabela, e a escolha de deixar a PESSOA de fora quando ela nao importa. '
                   'Nao de a regra ainda.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> Ela vai querer contar a historia da compra. Segure: '
                'a pergunta e sobre UM comodo, o que ficou pronto e o que nao foi tocado. Se ela responder com '
                '"the man came and he...", nao corrija ainda &mdash; so guarde a frase para usar no slide de '
                'Grammar Discovery.',
        'tr_vocab': '<strong>Transicao vocab (1 min):</strong> Diga: "Twelve words for an old house. Click each '
                    'card to reveal." Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta a palavra, revele. CCQ '
                  '"to strip back": "Do I take off the paint, or the wall? (So a camada de cima, ate a '
                  'superficie nua.)" CCQ "to gut": "Is anything left? (So parede e chao.)" CCQ "damp": "Is it '
                  'water on the floor? (Nao &mdash; e a umidade DENTRO da parede, que sobe e estraga devagar.)" '
                  'Peca um exemplo da casa dela em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ "sagging": "Is it broken? '
                  '(Ainda nao &mdash; esta cedendo no meio.)" CCQ "a quote": "Is it the final bill? (Nao &mdash; '
                  'e o preco por escrito ANTES da obra.)" CCQ "to cut corners": "Is it faster and better, or '
                  'faster and worse? (Mais rapido e pior &mdash; pulou o que importava.)" Marque que "a money '
                  'pit" e afetuoso e ironico: quem diz isso normalmente ama a casa.',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica: toca a '
                    'palavra, toca o significado. Certo fica verde, errado balanca em vermelho, e clicar num '
                    'par feito DESFAZ. Use o vocab-note no fim como ponte para o dialogo.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> Foque em: "plaster" (PLAS-ter, A curto; ela vai '
                'querer dizer "plaster" com A longo por influencia de "plastico"), "sturdy" (STER-di, o U e '
                'schwa, nunca "stiur"), "a money pit" (MA-ni pit, o O soa como U curto), e a frase inteira, '
                'onde "is being" cola e vira /iz-bi-in/. Peca 2 repeticoes de cada.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a palavra que falta '
                   'ANTES de clicar. As candidatas estao no banco embaixo, fora de ordem &mdash; ela ESCOLHE, '
                   'nao adivinha. Se travar, aponte duas do banco e pergunte qual das duas cabe. Clicar de novo '
                   'fecha (REGRA 27E).',
        'tr_ch3': '<strong>Transicao (1 min):</strong> Diga: "Two people who bought a house nobody else wanted. '
                  'First a conversation, then a man in Rotterdam." Passe ao proximo.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e a Maddie, AUSTRALIANA, que comprou uma casa de 110 '
                    'anos e esta assustada. Clique "Next Line" para cada fala e toque o audio de cada uma. Para '
                    'cada fala da Ana, peca que ELA fale primeiro. PRAGMATICA: repare que a Maddie abre com '
                    'auto-ironia ("I am starting to think it is a money pit") em vez de pedir ajuda &mdash; e '
                    'assim que se pede conselho em ingles australiano, e a Ana precisa saber LER isso como um '
                    'pedido de ajuda, nao como piada.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre a MADDIE, nao sobre a Ana '
                         '(REGRA 27F). Ana responde ANTES de voce clicar para revelar. Na 1a, exija que ela '
                         'separe o que JA FOI FEITO do que ESTA SENDO FEITO &mdash; e a distincao da noite '
                         'inteira, aparecendo aqui pela primeira vez, ainda sem regra.',
        'listen1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de '
                   'tocar &mdash; elas ja estao visiveis na tela. Este e um HOLANDES falando ingles: vogais '
                   'muito longas, V que tende a F, ritmo mais lento e consoante final bem marcada. Avise ANTES: '
                   '"This is a Dutch man, not an American." Toque 2 vezes, 0.75x se ela pedir. Depois pergunte '
                   'QUANTAS vezes ele disse quem fez o trabalho (resposta: praticamente nenhuma).',
        'tr_grammar': '<strong>Transicao gramatica (1 min):</strong> Diga: "Four sentences you have already '
                      'heard tonight. All four are about work. Now find the worker." Passe ao proximo.',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Pergunte: "Somebody replaced the roof. Where is '
                   'that somebody in the sentence?" Espere ela chegar sozinha em "nao esta la". Depois a '
                   'pergunta melhor: "Does the house care who did it?" So entao clique "Reveal the Rule". CCQ: '
                   '"The kitchen is being rewired &mdash; is it finished? (Nao, esta acontecendo agora.)" "That '
                   'wall has been plastered &mdash; can I see the result? (Sim, e por isso o present perfect.)" '
                   'NAO de a regra antes.',
        'mistake': '<strong>Common mistake (4 min):</strong> Os quatro que voltam sempre: (1) "was build" '
                   '&mdash; o participio virou infinitivo; (2) "is rewiring" no lugar de "is being rewired" '
                   '&mdash; some o being e a frase diz que a cozinha esta refazendo a fiacao de alguem; (3) '
                   '"have sanded" no lugar de "have been sanded"; (4) "was happened" &mdash; happen nao tem '
                   'passiva em lugar nenhum, e o portugues ajuda no erro ("foi acontecido" nao existe, mas '
                   '"aconteceu-se" quase). Mostre certo (verde) vs errado (vermelho) e peca que ela leia as '
                   'versoes certas 2 vezes cada.',
        'gpractice': '<strong>Practice (4 min):</strong> Leia cada frase. Ana escolhe ORALMENTE antes de clicar. '
                     'Se travar, faca a pergunta-chave: "Is it finished, is it happening now, or is it how it '
                     'is always done?" As tres respostas dao tres formas diferentes.',
        'listen2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de '
                   'tocar. Este e um AUSTRALIANO: vogais bem diferentes do americano (o "a" de "ask" e longo, '
                   'o "i" de "nice" quase vira "oi"), entonacao que sobe no fim de frases afirmativas. Avise '
                   'ANTES. Este audio existe por um motivo pedagogico especifico: a Ana descreveu na consultoria '
                   'o ciclo ansiedade-travamento diante do que nao entende. Aqui o homem diz que quase tudo pode '
                   'ser pulado e quase tudo volta &mdash; e uma frase sobre obra, e nao e so sobre obra. Deixe '
                   'pousar antes de passar.',
        'artifact': '<strong>Artefato (5 min):</strong> E o orcamento do pedreiro, escrito como orcamento real: '
                    'linhas sem verbo conjugado. Peca que ela transforme CADA linha numa frase completa, '
                    'escolhendo a forma passiva certa. So depois as 3 perguntas. Este e o melhor termometro da '
                    'aula &mdash; se ela transformar as seis linhas sozinha, o passivo esta consolidado.',
        'tr_practice': '<strong>Transicao practice (1 min):</strong> Diga: "Now we train: detective, quick fire, '
                       'and building." Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. Pergunte "What is wrong '
                     'here?". Ana corrige ANTES de clicar. Sao exatamente os quatro erros do slide de Common '
                     'Mistake &mdash; se ela acertar os quatro sem ajuda, a forma esta consolidada.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao ABERTA por vez. Ana responde em voz alta '
                     'ANTES de abrir as Tips &mdash; as Tips sao apoio, nao gabarito. Use Previous/Next para '
                     'navegar. Repare na 3a e na 5a: as duas exigem RECUSAR alguma coisa educadamente, que e '
                     'exatamente o que ela evita fazer em ingles por medo de soar grossa.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija '
                    'pelo menos um passivo em cada resposta. Se ela responder tudo no ativo ("the man came and '
                    'he fixed"), devolva: "And if you did not know his name?" As respostas modelo sao SUGESTOES '
                    '&mdash; a casa real da Ana e sempre melhor material.',
        'build': '<strong>Sentence Building (4 min):</strong> Mostre as keywords e a indicacao entre parenteses. '
                 'Ana monta a frase COMPLETA em voz alta, depois clica para comparar. Toggle: clicar de novo '
                 'fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO depois que ela '
                     'tentou tudo. E o resumo da aula inteira &mdash; peca que ela fotografe a tela, e o '
                     'material de estudo da semana.',
        'tr_roleplay': '<strong>Transicao role-play (1 min):</strong> Diga: "Now you show me the house. Three '
                       'steps, and the last one has no help at all." Passe ao proximo.',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e um pedreiro que ela nunca viu, ligando sobre o '
               'orcamento. Registro DIRETO e pratico. Faca as tres perguntas na ordem: o que ja foi feito, o que '
               'esta sendo feito, o que nao foi tocado. Ana responde com os chips. Corrija SO a escolha da forma '
               'passiva, nada mais.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e a Maddie de novo, com dois orcamentos na '
               'mao e genuinamente insegura. Ana precisa PERGUNTAR antes de opinar. Se ela comecar com "You '
               'should...", interrompa e peca de novo: "Ask me about my house first." E a competencia mais '
               'dificil da noite, e a mesma da aula 6: responder com a propria experiencia em vez de conselho.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO corrija '
               'durante. CONTE quantas passivas ela usa e diga o numero a ela no fim &mdash; medir e o que faz a '
               'forma virar habito. Meta: pelo menos seis, e pelo menos duas formas diferentes.',
        'tr_wrap': '<strong>Transicao wrap-up (1 min):</strong> Diga: "You just gave a stranger a tour of a '
                   'hundred year old house in English, and you never once had to invent the name of a builder."',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a Ana '
                    'repita. Cada uma cobre uma forma diferente: past perfect passive, present continuous '
                    'passive, present perfect passive, past simple passive com by, e a negativa.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: "Click each item if you feel confident." Leia '
                     'cada item. Todos os 5 checks = aula completa e a aula 7 registrada como concluida no '
                     'passaporte.',
        'closing': '<strong>Encerramento (2 min):</strong> Diga: "Seven lessons in, Ana, and tonight you '
                   'described a building site to an Australian and a Dutchman without once losing the thread." '
                   'Homework (oralmente, opcional): gravar dois minutos de tour pela casa, sem notas, e ouvir a '
                   'propria gravacao contando quantas passivas apareceram. Proxima aula: Checkpoint &mdash; '
                   'Block 1, revisao das aulas 1 a 7 e o benchmark de fala.',
    },
}
