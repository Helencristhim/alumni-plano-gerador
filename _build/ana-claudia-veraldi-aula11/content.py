# -*- coding: utf-8 -*-
"""Aula 11 -- Getting Used to the Quiet (be used to / get used to).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques do listening (CURRICULO V3): indiano + americano.
Callback da aula 10: ela descreveu, com used to e would, os onze anos de manhas iguais.
Hoje a MESMA palavra muda de lado: nao a vida que acabou, mas a vida a que ela ja se
acostumou -- e o -ing obrigatorio que separa uma coisa da outra.
"""

LESSON = {
    'n': 11,
    'model': 'speech',
    'menu_title': 'Getting Used to the Quiet',
    'menu_desc': 'The months nobody warns you about, and the one letter that separates the life '
                 'that ended from the life you are already living',
    'grammar_point': 'be used to and get used to for familiarity and adaptation',
    'chapter_tag': 'The Quiet',
    'title_html': 'Getting Used <span class="accent">to the Quiet</span>',
    'title_sub': 'Last week: the life that ended. Tonight: the life you have already started living.',
    'phases': ['First Words', 'The Words of Adapting', 'Somebody Else&rsquo;s First Year',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1494526585095-c41746248156?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'The First Night <span class="accent">Was Too Quiet</span>',
        'callback': 'Last time you described eleven years of identical mornings, and you did it with two '
                    'structures that exist only for a life that is over: used to and would.',
        'question': 'What was the very first thing about the countryside that your body refused to accept?',
    },
    'framing': {
        'heading': 'The Same Three Words, <span class="accent">Pointing Forwards</span>',
        'steps': [('The Words', 'eerie, overwhelming, to crave, to find your feet...'),
                  ('The First Year', 'an Indian engineer and an American who both moved and both struggled'),
                  ('The Code', 'be used to and get used to, and the letters that change everything')],
        'note': 'You already own <strong>used to + verb</strong>. Tonight the same three words appear again with '
                'something else after them, and they stop describing the past entirely. The difference is one '
                'suffix, and almost every learner in the world gets it wrong for years.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'How Long Does <span class="accent">Adapting Take?</span>',
        'line1': 'People who move somewhere very different all report the same thing: the hard part is not the '
                 'first week. The first week is exciting.',
        'line2': 'The hard part arrives around month three, when the new place has stopped being a holiday and '
                 'has not yet become home. How long did that last for you?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'The Language of <span class="accent">Adapting</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'To adjust', 'icon': 'compass',
         'def': 'To slowly change your habits so a new situation stops feeling wrong',
         'ex': 'It took me a whole winter to adjust to the silence out here.',
         'match': 'to slowly change your habits so a new situation stops feeling wrong'},
        {'word': 'Culture shock', 'icon': 'globe',
         'def': 'The disorientation of arriving somewhere that works by different rules',
         'ex': 'Moving three hours from the city gave me a small dose of culture shock.',
         'match': 'the disorientation of arriving somewhere with different rules'},
        {'word': 'Overwhelming', 'icon': 'cloud',
         'def': 'So intense or so much at once that you cannot deal with it properly',
         'ex': 'The first month was overwhelming, and I had expected it to be restful.',
         'match': 'so intense or so much at once that you cannot deal with it'},
        {'word': 'Eerie', 'icon': 'moon',
         'def': 'Strange and slightly frightening in a way that is hard to explain',
         'ex': 'The silence at three in the morning here is genuinely eerie.',
         'match': 'strange and slightly frightening in a way hard to explain'},
        {'word': 'Homesick', 'icon': 'home',
         'def': 'Sad because you are away from the place you think of as home',
         'ex': 'I was never homesick for the traffic, only for two or three people.',
         'match': 'sad because you are away from the place you call home'},
        {'word': 'To crave', 'icon': 'heart',
         'def': 'To want something so strongly that it is almost physical',
         'ex': 'By week three I was craving noise, which shocked me completely.',
         'match': 'to want something so strongly that it is almost physical'},
        {'word': 'Solitude', 'icon': 'leaf',
         'def': 'Being alone on purpose, and finding it good rather than lonely',
         'ex': 'I moved here for the solitude and it still took months to enjoy it.',
         'match': 'being alone on purpose, and finding it good rather than lonely'},
        {'word': 'To find your feet', 'icon': 'anchor', 'expr': True,
         'def': 'To become confident in a new place after a period of not coping',
         'ex': 'It was about six months before I really found my feet here.',
         'match': 'to become confident in a new place after not coping'},
        {'word': 'A steep learning curve', 'icon': 'trending', 'expr': True,
         'def': 'A period when you have to learn a great deal very fast',
         'ex': 'Rural life is a steep learning curve if you arrive from a flat in the city.',
         'match': 'a period when you have to learn a great deal very fast'},
        {'word': 'Unsettling', 'icon': 'alert',
         'def': 'Making you feel uneasy, without any obvious reason for it',
         'ex': 'Having no neighbours within shouting distance was unsettling at first.',
         'match': 'making you feel uneasy, without any obvious reason'},
        {'word': 'To ease into something', 'icon': 'refresh',
         'def': 'To start doing something slowly and gently instead of all at once',
         'ex': 'Nobody eases into a move. You arrive and the whole life starts on day one.',
         'match': 'to start doing something slowly instead of all at once'},
        {'word': 'Deafening', 'icon': 'zap',
         'def': 'So loud that you cannot hear anything else &mdash; and, oddly, used about silence too',
         'ex': 'People say the silence out here is deafening, and now I understand why.',
         'match': 'so loud you cannot hear anything else, or a total silence'},
    ],
    'vocabnote': 'Two of tonight&rsquo;s twelve are whole expressions: <strong>to find your feet</strong> and '
                 '<strong>a steep learning curve</strong>. Notice that they describe the same six months from '
                 'opposite ends &mdash; the curve is what the period does to you, and finding your feet is what '
                 'you have done by the end of it.',
    'pron': [
        'Eerie',
        'Overwhelming',
        'A steep learning curve',
        'I am used to the silence now, but it took a whole winter.',
    ],
    'gapfill': [
        ('"The first three months were completely ', 'overwhelming', ', and I had expected them to be restful."'),
        ('"The silence at three in the morning is genuinely ', 'eerie', '."'),
        ('"By week three I had started to ', 'crave', ' the sound of a road."'),
        ('"The first year out here is ', 'a steep learning curve', ' if you arrive from a flat in the city."'),
        ('"Having no neighbours within shouting distance was ', 'unsettling', ' at first."'),
        ('"I moved here for the ', 'solitude', ', and it still took months to enjoy it."'),
    ],

    # ------------------------------------------------------------ chapter 3
    'ch3': {
        'heading': 'Somebody Else&rsquo;s <span class="accent">First Year</span>',
        'sub': 'Two people who moved a long way, and neither of them found it easy',
    },
    'dialogue': {
        'heading': 'He Moved to Vermont <span class="accent">and Nearly Left</span>',
        'guest_name': 'Wes',
        'guest_key': 'wes',
        'guest_voice': 'arthur',
        'lines': [
            ('wes', 'Ana, everyone told me the quiet would be the easy part. I was <span class="vocab-highlight">craving</span> noise by the third week.'),
            ('ana', 'That happened to me too, and I felt ridiculous about it.'),
            ('wes', 'It is not ridiculous. Your ears spent thirty years filtering a city and suddenly there is nothing to filter. People call it restful. I found it <span class="vocab-highlight">eerie</span>.'),
            ('ana', 'The first winter here was genuinely <span class="vocab-highlight">unsettling</span>. I am used to it now, but it took months.'),
            ('wes', 'How long, honestly? Because I am still not used to driving forty minutes for a pharmacy.'),
            ('ana', 'About a winter. And I never really <span class="vocab-highlight">eased into</span> it &mdash; you arrive and the whole life starts on day one.'),
            ('wes', 'That is exactly it. It was a <span class="vocab-highlight">steep learning curve</span> and nobody warned me. I was not <span class="vocab-highlight">homesick</span> for the city, just for knowing how things worked.'),
            ('ana', 'Give it a year. You will <span class="vocab-highlight">find your feet</span>, and then you will get used to the silence without noticing that you have.'),
        ],
        'comp': [
            ('What surprised Wes most about the quiet, and when did it happen?',
             'He had been told the quiet would be the easy part, and by the third week he was craving noise instead.'),
            ('How does Wes explain why the silence felt eerie rather than restful?',
             'His ears had spent thirty years filtering a city, and suddenly there was nothing left to filter.'),
            ('What is Wes still not used to, and what was he actually homesick for?',
             'He is still not used to driving forty minutes to a pharmacy, and he was homesick for knowing how things worked, not for the city itself.'),
        ],
    },
    'listenings': [
        {
            'voice': 'indian_f',
            'title': 'From Bangalore <span class="accent">to a Village of Eight Hundred</span>',
            'blurb': 'An Indian engineer on her first year in rural Ireland. Sound first &mdash; no text.',
            'text': 'The thing nobody tells you is that the difficulty is not the big stuff. I had expected the big '
                    'stuff. I had read about the weather and I had read about the food and I was completely prepared '
                    'to hate both, and honestly neither of them bothered me at all. What broke me, and I mean this '
                    'quite literally, was that the shop shut at half past five. That is it. That is the whole '
                    'tragedy. I grew up in a city of thirteen million people where you can buy anything at any hour, '
                    'and I am not used to planning a week in advance simply to have rice in the house. For about '
                    'four months I found the evenings genuinely eerie. There is a kind of silence in a village of '
                    'eight hundred people that a city person has never heard, and everyone kept telling me how '
                    'peaceful it was, and I kept thinking, this is not peaceful, this is empty. And then somewhere '
                    'around the following spring I noticed that I had stopped noticing. I am used to the quiet now. '
                    'I go back to Bangalore twice a year and I last about nine days before the noise exhausts me, '
                    'which my mother finds extremely funny and slightly insulting.',
            'qs': [
                ('What had she expected to find difficult, and what actually was difficult?',
                 'She had expected to hate the weather and the food and prepared for both. Neither bothered her. What broke her was that the shop shut at half past five.'),
                ('Why is planning a week ahead so strange for her?',
                 'She grew up in a city of thirteen million people where anything can be bought at any hour, so she is not used to planning in advance simply to have rice in the house.'),
                ('What happened around the following spring, and what happens when she visits Bangalore now?',
                 'She noticed that she had stopped noticing the silence. Now she lasts about nine days in Bangalore before the noise exhausts her, which her mother finds funny and slightly insulting.'),
            ],
        },
        {
            'voice': 'arthur',
            'title': 'Month Three <span class="accent">Is the One That Gets You</span>',
            'blurb': 'An American on why the third month is the hardest. Sound first &mdash; no text.',
            'text': 'I have moved five times in my adult life, twice across an ocean, and the shape of it is always '
                    'identical, which I find weirdly comforting now. Weeks one to four, everything is a holiday. You '
                    'photograph the bakery. You tell people the light is different. Weeks five to eight, still fine, '
                    'still interesting. And then month three arrives and the whole thing collapses, and it collapses '
                    'for a very specific reason: the novelty has worn off and the competence has not arrived yet. '
                    'You are no longer a tourist and you are not a local either, and there is nothing to be in '
                    'between. That is when people phone home and say they have made a terrible mistake. My rule, and '
                    'I have given this advice to about a dozen people now, is that you are not allowed to make any '
                    'decision about leaving until month seven. Not month six. Seven. Because somewhere in the sixth '
                    'month you stop translating the small things. You stop rehearsing the sentence before you walk '
                    'into the post office. You get used to the way things are done, and the day you notice that, the '
                    'hard part is genuinely behind you.',
            'qs': [
                ('What are weeks one to four like, according to him?',
                 'Everything is a holiday. You photograph the bakery and you tell people the light is different.'),
                ('Why exactly does month three collapse?',
                 'The novelty has worn off and the competence has not arrived yet. You are no longer a tourist and not a local either, and there is nothing to be in between.'),
                ('What is his rule, and what changes around the sixth month?',
                 'No decision about leaving before month seven, not six. Around the sixth month you stop translating the small things and stop rehearsing sentences before going into the post office.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4
    'grammar': {
        'chapter_heading': 'One Suffix, <span class="accent">Two Different Tenses</span>',
        'chapter_sub': 'used to &middot; be used to &middot; get used to',
        'heading': 'Three Of These Are <span class="accent">Not Last Week&rsquo;s Rule</span>',
        'examples': [
            'I used to live in a flat with traffic under the window.',
            'I am used to the silence now, but it took a whole winter.',
            'It took me about six months to get used to driving everywhere.',
            'I am still not used to planning a week ahead just to buy rice.',
        ],
        'prompt': 'The first one is last week&rsquo;s rule and it is finished business. In the other three, look at '
                  'what comes immediately after the word <em>to</em>. It is never a bare verb. Say what it is &mdash; '
                  'and then say whether those three describe the past or now.',
        'rule_rows': [
            ('used to + <strong>verb</strong>', 'A habit or state that is OVER. Last week&rsquo;s rule.',
             'I <strong>used to live</strong> in the city.'),
            ('be used to + <strong>-ing</strong> / noun', 'You are ALREADY familiar with it, now.',
             'I <strong>am used to the silence</strong>.'),
            ('get used to + <strong>-ing</strong> / noun', 'The PROCESS of becoming familiar. Takes time.',
             'I <strong>got used to driving</strong> everywhere.'),
            ('why -ing and not the verb', 'Here <em>to</em> is a preposition, and a preposition takes -ing.',
             'I am used to <strong>driving</strong>. (never: to drive)'),
            ('negative', 'be / get take a normal negative, and often <em>yet</em>.',
             'I am <strong>not used to</strong> the dark <strong>yet</strong>.'),
            ('any tense you like', 'Unlike used to, be / get used to move freely in time.',
             'You <strong>will get used to</strong> it.'),
            ('the test that always works', 'Swap in <em>accustomed to</em>. If it fits, you need be / get used to.',
             'I am <strong>accustomed to</strong> the quiet.'),
        ],
        'oneliner': 'used to looks back and stops; be used to and get used to look at now and keep going.',
    },
    'mistakes': [
        ('I am used to drive on unpaved roads.', 'I am used to driving on unpaved roads.'),
        ('I am getting used to wake up at five.', 'I am getting used to waking up at five.'),
        ('I used to the silence now.', 'I am used to the silence now.'),
        ('It took me six months to used to it.', 'It took me six months to get used to it.'),
    ],
    'mistake_note': 'The first two are the same mistake: after <em>used to</em> here, <em>to</em> is a preposition, '
                    'so the verb takes <strong>-ing</strong>. The third drops the verb <em>be</em> and turns a '
                    'present state into last week&rsquo;s past. The fourth forgets that the PROCESS needs '
                    '<strong>get</strong> &mdash; without it there is no verb in the sentence at all.',
    'practice_heading': 'Used To, Be Used To, <span class="accent">or Get Used To?</span>',
    'practice_fill': [
        ('"I ', 'used to live', ' in a flat with traffic under the window." (live &mdash; finished, last week&rsquo;s rule)'),
        ('"I ', 'am used to', ' the silence now, and I would not sleep in the city." (the state, right now)'),
        ('"It took me six months to ', 'get used to driving', ' everywhere." (drive &mdash; the process, and mind the suffix)'),
        ('"I am still not ', 'used to planning', ' a week ahead." (plan &mdash; not yet familiar)'),
        ('"You ', 'will get used to', ' it by about month seven." (the process, in the future)'),
    ],
    'artifact': {
        'heading': 'The Settling-In <span class="accent">Log</span>',
        'title': 'SETTLING-IN LOG &mdash; A. VERALDI',
        'subtitle': 'Interior of Sao Paulo &middot; first twelve months',
        'corner': 'Still<br>adjusting',
        'label_width': '110px',
        'rows': [
            ('Week 1', 'unpacking, everything exciting, photographed the road twice'),
            ('Week 3', 'craving noise. Slept badly. Told nobody'),
            ('Month 3', 'the silence at night still eerie. Forty minutes to a pharmacy'),
            ('Month 6', 'stopped rehearsing what to say at the shop'),
            ('Month 9', 'drove to the city, lasted a day and a half'),
            ('Month 12', 'the quiet is now the normal setting. Cannot sleep in a city'),
        ],
        'comp': [
            ('Say the Week 3 line as a full sentence about what was true then, not now.',
             '"I was not used to the silence at all &mdash; by week three I was craving noise." Was not used to, because we are describing a state in the past that has since changed.'),
            ('Say the Month 6 line using get used to, and explain why get and not be.',
             '"By month six I had got used to going into the shop without rehearsing the sentence first." Get, because the line records a CHANGE happening, not a state that already existed.'),
            ('Say the Month 12 line two ways: with be used to and with the past simple.',
             '"I am used to the quiet now." / "The quiet became normal at about a year." Both are correct; only the first says anything about how she is today.'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'quickfire': [
        {'situation': 'Somebody asks how the first weeks in the countryside felt. Answer with the state you were in, not with a story.',
         'tips': ['I was not used to the silence at all, and it frightened me a little.',
                  'Not used to, because you are describing how you were then and are not now.']},
        {'situation': 'Somebody asks whether you have adapted. Answer about right now, in one sentence.',
         'tips': ['I am used to it now. I would not sleep properly in a city any more.',
                  'Be used to for the state that is already true.']},
        {'situation': 'A friend is three months into a move and is talking about giving up. Tell her what happens next, using the process.',
         'tips': ['You will get used to it, but not before about month seven.',
                  'Get used to for the change that has not finished happening.']},
        {'situation': 'Name one thing about rural life that you have still not adapted to. Careful with the form.',
         'tips': ['I am still not used to driving forty minutes for a pharmacy.',
                  'After to, the verb takes -ing. Driving, never drive.']},
        {'situation': 'Somebody asks what you did every weekday in the city, years ago. Careful &mdash; this one is last week&rsquo;s grammar.',
         'tips': ['I used to leave the flat at ten past seven.',
                  'Used to + bare verb. No -ing anywhere near this sentence.']},
        {'situation': 'Describe the exact moment you realised you had adapted, without using the word happy.',
         'tips': ['I noticed that I had stopped noticing, which is how you know.',
                  'I went back to the city and lasted a day and a half.']},
    ],
    'speaking': [
        ('What were you not used to at all in your first month here?',
         'I was not used to the silence, and I was certainly not used to driving forty minutes for anything.'),
        ('What are you used to now that would have seemed impossible three years ago?',
         'I am used to going a whole day without hearing a car, and I am used to planning the week around one shop.'),
        ('How long did it take you to get used to living this far from a city?',
         'About a winter. I got used to the quiet long before I got used to the distances.'),
        ('What did you use to do on a weekday evening in the city, back then?',
         'I used to sit in traffic until half past eight and then spend two hours winding down.'),
    ],
    'building': [
        ('I / not / the silence / at first (a state in the past that has changed)',
         'I was not used to the silence at first.'),
        ('it took me / six months / drive everywhere (the process, and mind the suffix)',
         'It took me six months to get used to driving everywhere.'),
        ('I / the quiet / now (the state, right now)',
         'I am used to the quiet now.'),
        ('I / live in a flat with traffic under the window (finished business, last week&rsquo;s rule)',
         'I used to live in a flat with traffic under the window.'),
    ],
    'answerkey_heading': 'The Three Forms on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole adaptation key',
    'answerkey': [
        'used to + BARE VERB = a habit or state that is over: I used to live in the city',
        'be used to + -ING or NOUN = you are already familiar with it now: I am used to the silence',
        'get used to + -ING or NOUN = the process of becoming familiar: I got used to driving everywhere',
        'the to in be / get used to is a PREPOSITION, so the verb takes -ing, always',
        'negative takes not, and very often yet: I am not used to the dark yet',
        'be / get used to work in any tense: I will get used to it &middot; I had got used to it',
        'the test: if accustomed to fits, you need be / get used to &mdash; never plain used to',
        'NEVER: I am used to drive &middot; I used to the silence now &middot; to used to it',
    ],
    'rp_chapter_heading': 'The Year You <span class="accent">Have Already Survived</span>',
    'roleplays': [
        {'heading': 'The Friend Who Is <span class="accent">Three Months In</span>',
         'scenario': 'I have just moved somewhere very quiet and I am at month three, which means I am telling you '
                     'I have made a mistake. Ask me two questions, then tell me what you were not used to, what you '
                     'are used to now, and how long getting used to it took.',
         'chips': ['I was not used to', 'I am used to', 'it took me about']},
        {'heading': 'The Colleague in <span class="accent">Bangalore</span>',
         'scenario': 'I am an Indian colleague you have worked with for years and I am considering a move to a very '
                     'small European town. I am direct and I want specifics, not encouragement. Tell me what will be '
                     'a steep learning curve, what I will crave, and what I will get used to faster than I expect.',
         'chips': ['a steep learning curve', 'you will crave', 'you will get used to']},
        {'heading': 'Two Minutes on <span class="accent">Your First Winter</span>',
         'scenario': 'Describe your first winter in the countryside from the inside: what was overwhelming, what was '
                     'eerie, what you craved, and the exact moment you realised you had found your feet. Use be used '
                     'to for the states and get used to for the changes, and finish with the one thing you are still '
                     'not used to.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'The Life You <span class="accent">Are Living Now</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Adapting</span>',
    'survival': [
        'I am used to the silence now, but it took a whole winter.',
        'I was not used to driving forty minutes for a pharmacy.',
        'It took me about six months to get used to living this far out.',
        'I am still not used to planning a whole week in advance.',
        'You will get used to it, but probably not before month seven.',
    ],
    'checklist': [
        'I use be used to for a state I am already familiar with now.',
        'I use get used to for the process of becoming familiar with something.',
        'I put -ing on the verb after be and get used to, every time.',
        'I keep used to + bare verb for a habit that is finished and gone.',
        'I know the words: eerie, overwhelming, to crave, to find your feet, a steep learning curve.',
    ],
    'badge': {
        'name': 'The Quiet',
        'text': 'You have just explained a whole year of adapting to an American who is three months behind you, '
                'Ana, using three structures that look identical and mean completely different things.',
        'next': 'If I Have Time This Weekend',
    },

    # ------------------------------------------------------------ teacher (icone T)
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Last week, '
                 'the life that ended. Tonight, the life you are already living.&quot; O recorte da noite e '
                 'exatamente o contraste com a aula 10 -- nao repita a regra passada, use-a como contraste.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 10: ela contou onze anos de manhas '
                  'iguais com used to e would. PONTE (REGRA 27B): &quot;Those two forms only look backwards. Tonight '
                  'the same words point at your life right now.&quot; A pergunta e sobre o CORPO de proposito -- '
                  'adaptacao e fisica antes de ser emocional. ZERO correcao aqui.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase de baixo e a tese da noite: '
                   'a diferenca entre used to e be used to e um sufixo, e quase todo aluno erra por anos. Nao de a '
                   'regra ainda -- so plante que a diferenca existe.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> A ideia do mes tres volta duas vezes na aula (listening '
                '2 e role-play 1). Se a Ana disser um numero aqui, ANOTE -- voce vai comparar com o do americano '
                'depois, e a comparacao e o melhor momento pedagogico da noite.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for the first year '
                       'somewhere new. Click each card to reveal.&quot; Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ &quot;eerie&quot;: '
                  '&quot;Is it dangerous, or just strange? (So estranho -- o medo e vago, e essa vagueza e a '
                  'palavra.)&quot; CCQ &quot;overwhelming&quot;: &quot;Is it good or bad? (Pode ser os dois -- e '
                  'sobre QUANTIDADE, nao sobre valor.)&quot; CCQ &quot;to crave&quot;: &quot;Do I want it, or do I '
                  'need it? (Quase preciso -- e mais forte que want.)&quot; Peca um exemplo do primeiro ano dela em '
                  'cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ &quot;solitude&quot;: &quot;Is it '
                  'the same as loneliness? (NAO. Solitude e escolhida e boa; loneliness e sofrida.)&quot; CCQ &quot;to '
                  'find your feet&quot;: &quot;Am I confident at the start or at the end? (No fim -- a expressao '
                  'pressupoe um periodo ruim antes.)&quot; CCQ &quot;deafening&quot;: &quot;Can silence be deafening? '
                  '(Pode, e e o uso mais interessante da palavra.)&quot;',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. Certo fica '
                    'verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note como ponte: a curva e o '
                    'que o periodo faz com voce, e find your feet e o que sobrou no fim.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> &quot;Eerie&quot; -- IH-ree, duas silabas, NUNCA '
                'ee-REE. &quot;Overwhelming&quot; -- o stress cai em WHEL, e o H praticamente some. &quot;A steep '
                'learning curve&quot; -- curve termina em V, nao em F. Na frase inteira, &quot;used to&quot; cola e '
                'vira /YOOS-tu/ com S surdo, exatamente como na aula 10 -- vale lembrar que a pronuncia nao muda, so '
                'a gramatica.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a palavra que falta ANTES de '
                   'clicar. As candidatas estao no banco embaixo, fora de ordem. Se travar, aponte duas e pergunte '
                   'qual cabe. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao (1 min):</strong> Diga: &quot;Two people who moved a long way. Neither of '
                     'them found it easy, and both of them are further along than you think.&quot; Passe ao proximo.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Wes, AMERICANO, tres meses em Vermont. Clique '
                    '&quot;Next Line&quot; e toque o audio de cada fala. Para cada fala da Ana, peca que ELA fale '
                    'primeiro. PRAGMATICA: o Wes admite fraqueza de forma direta e sem constrangimento -- muito '
                    'americano, e o contrario do que a Ana provavelmente faria numa reuniao com europeus do norte, '
                    'onde a mesma admissao vem embrulhada. Comente no fim. Repare tambem que a gramatica da noite '
                    'aparece aqui SEM regra nenhuma, de proposito.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o WES, nao sobre a Ana (REGRA 27F). '
                         'Ana responde ANTES de revelar. Na 3a, repare que a resposta separa duas saudades '
                         'diferentes -- da cidade e de saber como as coisas funcionam. Essa distincao vai voltar no '
                         'role-play 2.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar. '
                      'Esta e uma INDIANA: ritmo silabico (cada silaba com peso parecido), T e D retroflexos, '
                      'entonacao que sobe no fim de frases afirmativas. Avise ANTES. Esta voz existe por um motivo '
                      'especifico: a Ana passou anos em reuniao com indianos e nunca treinou o sotaque fora do '
                      'trabalho. Depois das perguntas, peca que ela cace UM exemplo de not used to no audio.',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Four sentences. One of them is last '
                     'week. Three of them are tonight, and the difference is three letters.&quot; Passe ao proximo.',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Peca que ela leia as quatro e diga o que vem depois '
                   'de <em>to</em> em cada uma. NAO explique -- a descoberta e ver que tres delas nao tem verbo puro '
                   'depois do to. Depois pergunte: &quot;Which of these four is about a life that ended?&quot; So '
                   'entao clique &quot;Reveal the Rule&quot;. CCQ: &quot;I am used to the silence -- do I like it? '
                   '(Nao necessariamente. So estou acostumada.)&quot; &quot;I got used to it -- when? (Ao longo do '
                   'tempo, e o processo terminou.)&quot; O truque do <em>accustomed to</em> e o mais util: se cabe, '
                   'e be/get used to.',
        'mistake': '<strong>Common mistake (4 min):</strong> Os dois primeiros sao o MESMO erro e sao os mais comuns '
                   'do mundo: depois de be/get used to, o <em>to</em> e preposicao e o verbo leva -ing. O terceiro '
                   'derruba o verbo be e joga a frase de volta para a aula passada. O quarto esquece o get e deixa a '
                   'frase sem verbo. Peca 2 repeticoes das versoes certas, em voz alta.',
        'practice': '<strong>Practice (4 min):</strong> Ana escolhe ORALMENTE antes de clicar. Se travar, faca a '
                    'pergunta-chave: &quot;Is it over, is it true now, or is it still happening?&quot; As tres '
                    'respostas dao as tres formas.',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA ANTES de tocar. Este e um '
                      'AMERICANO em velocidade normal, com reducoes (aula 9): &quot;gonna&quot;, &quot;kinda&quot;, T '
                      'virando D em &quot;competence&quot;. Avise ANTES. O conteudo importa para ELA: a regra do mes '
                      'sete descreve exatamente o que ela viveu. Compare com o numero que ela deu no slide 4 -- se '
                      'bater, pare e comente.',
        'artifact': '<strong>Artefato (5 min):</strong> E o primeiro ano DELA, escrito como registro. Peca que ela '
                    'transforme CADA linha em frase completa, escolhendo entre was not used to, got used to e am '
                    'used to. So depois as 3 perguntas. A linha do Mes 6 e o melhor termometro: e mudanca, entao pede '
                    '<em>get</em>, e quase todo aluno responde <em>be</em>.',
        'ch5_trans': '<strong>Transicao practice (1 min):</strong> Diga: &quot;Now we train: detective, quick fire, '
                     'and building.&quot; Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. &quot;What is wrong here?&quot; '
                     'Ana corrige ANTES de clicar. Sao os quatro do slide de Common Mistake.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez, resposta em voz alta ANTES das Tips. '
                     'A 5a e armadilha proposital (volta para used to + verbo puro) -- se ela cair, e o erro que voce '
                     'vai cacar no role-play 3.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija a '
                    'forma certa: a 1a pede was not used to, a 2a pede am used to, a 3a pede got used to e a 4a volta '
                    'para used to + verbo puro. Se ela errar o -ing, devolva a pergunta em vez de corrigir.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase COMPLETA em voz alta, depois clica '
                    'para comparar. Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO depois que ela tentou '
                     'tudo. A linha do <em>accustomed to</em> e a que ela vai levar para a vida -- destaque.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;Now you are the one who is further '
                     'along. Three steps, and the last one has no help.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e uma amiga no mes tres, convencida de que errou. '
               'Registro exausto, nao dramatico. Ana precisa PERGUNTAR antes de aconselhar. Corrija SO a escolha '
               'entre was not used to / am used to / got used to.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e uma colega INDIANA, direta, que quer '
               'especificidade e nao encorajamento. PRAGMATICA: se a Ana suavizar demais (&quot;maybe you might find '
               'it a little difficult&quot;), interrompa e peca de novo -- neste registro o hedge soa evasivo, nao '
               'gentil. E o inverso exato do que ela vai treinar na aula 14.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO corrija '
               'durante. CONTE quantos <em>be used to</em> e quantos <em>get used to</em> ela usa, e se algum verbo '
               'saiu sem -ing. Diga os numeros no fim. Meta: pelo menos dois de cada e zero verbo sem -ing.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;You just described a whole year of '
                     'adapting, in the tense that only exists for people who are still there.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a Ana repita. '
                    'As cinco cobrem: be used to afirmativo, was not used to, get used to com -ing, not used to com '
                    '-ing, e will get used to. Insista no /YOOS-tu/ e no -ing audivel.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 11 registrada como concluida no '
                     'passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Eleven lessons, Ana. Tonight you separated two '
                 'structures that most people never separate at all.&quot; Homework (oralmente, opcional): gravar '
                 'dois minutos sobre uma coisa a que ela AINDA nao se acostumou, contando quantos -ing apareceram. '
                 'Proxima aula: If I Have Time This Weekend -- o primeiro condicional, e o comeco do bloco que ela '
                 'mesma pediu (&quot;o condicional nao entra na minha cabeca&quot;).',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'Getting Used to the Quiet -- The First Year Somewhere New',
        'desc': 'The months nobody warns you about, and the three structures English uses to talk about them.',
        'context_paras': [
            'Ana <strong>used to live</strong> in a flat with traffic under the window, and for eleven years she '
            'never once thought about the noise. When she moved to the countryside she expected the silence to be '
            'restful. It was not. For the first three months it was <strong>eerie</strong>, and by the third week '
            'she was <strong>craving</strong> the sound of a road.',
            'She <strong>was not used to</strong> the dark either, and she was certainly <strong>not used to '
            'driving</strong> forty minutes for a pharmacy. The whole first year was <strong>a steep learning '
            'curve</strong>: everything she knew about how a day works had been built for a city. It was '
            '<strong>overwhelming</strong> in a way she had not expected, because nobody warns you that the '
            'difficulty arrives in month three rather than week one.',
            'It took her about a winter to <strong>get used to</strong> the quiet, and rather longer to <strong>get '
            'used to planning</strong> a whole week in advance. Now she <strong>is used to</strong> both. She goes '
            'back to the city twice a year, lasts about a day and a half, and comes home. She <strong>found her '
            'feet</strong> somewhere around month seven, and like everybody else she only noticed months later.',
        ],
        'context_quiz': [
            ('Why "used to live" in the first line, but "is used to" in the last paragraph?',
             [('The first is a finished state in the past; the second is a state that is true now.', True),
              ('The first is formal and the second is informal.', False),
              ('There is no difference; both mean the same thing.', False)]),
            ('"She was not used to driving forty minutes." Why driving and not drive?',
             [('Because the sentence is in the past.', False),
              ('Because here to is a preposition, and a preposition is followed by -ing.', True),
              ('Because drive is an irregular verb.', False)]),
            ('Why "it took her a winter to get used to the quiet" and not "to be used to the quiet"?',
             [('Because get used to describes the process of becoming familiar, which is what took a winter.', True),
              ('Because be used to cannot be used with periods of time.', False),
              ('Because get is more polite than be in this context.', False)]),
        ],
        'tip_title': 'Used To, Be Used To and Get Used To',
        'tip_sub': 'Three structures that look almost identical. One looks back; two look at now.',
        'tip_rows': [
            ('used to + <strong>verb</strong>', 'A habit or state that is finished', 'I <strong>used to live</strong> in the city.'),
            ('be used to + <strong>-ing</strong> / noun', 'Already familiar with it, now', 'I <strong>am used to</strong> the silence.'),
            ('get used to + <strong>-ing</strong> / noun', 'The process of becoming familiar', 'I <strong>got used to driving</strong> everywhere.'),
            ('why -ing', 'Here <em>to</em> is a preposition, not an infinitive', 'used to <strong>driving</strong>, never to drive'),
            ('negative', 'Normal negative, very often with <em>yet</em>', 'I am <strong>not used to</strong> it <strong>yet</strong>.'),
            ('any tense', 'be / get used to move freely in time', 'You <strong>will get used to</strong> it.'),
            ('the test', 'If <em>accustomed to</em> fits, use be / get used to', 'I am <strong>accustomed to</strong> the quiet.'),
        ],
        'tip_never': 'I am used to drive &middot; I am getting used to wake up early &middot; I used to the silence now '
                     '&middot; it took me six months to used to it. Two of those forget that <em>to</em> is a '
                     'preposition here, one drops the verb <em>be</em>, and one drops <em>get</em> and leaves the '
                     'sentence without a verb.',
        'fills': [
            ('I ', 'used to live', ' in a flat with traffic under the window.',
             'live -- a finished state, three words, the rule from lesson 10'),
            ('I ', 'am used to', ' the silence now, and I would not sleep in a city.',
             'the state right now, three words, starting with the verb be'),
            ('It took me six months to ', 'get used to driving', ' everywhere.',
             'drive -- the process of becoming familiar, four words, mind the suffix'),
            ('I am still not ', 'used to planning', ' a whole week in advance.',
             'plan -- not yet familiar, three words after not'),
            ('You ', 'will get used to', ' it by about month seven.',
             'the process, in the future, four words'),
            ('The silence at three in the morning is genuinely ', 'eerie', '.',
             'one word -- strange and slightly frightening in a way that is hard to explain'),
        ],
        'order_intro': 'Wes has just moved to Vermont and Ana is a year ahead of him. Put the exchange in a logical order.',
        'order': [
            'Everyone told me the quiet would be the easy part. I was craving noise by the third week.',
            'That happened to me too, and I felt ridiculous about it.',
            'It is not ridiculous. Your ears spent thirty years filtering a city and suddenly there is nothing to filter.',
            'The first winter here was genuinely unsettling. I am used to it now, but it took months.',
            'How long, honestly? Because I am still not used to driving forty minutes for a pharmacy.',
            'Give it a year. You will find your feet, and then you will get used to the silence without noticing.',
        ],
        'quiz': [
            ('A colleague asks whether you have adapted to the countryside. You answer:',
             [('"I am used to it now, although the first winter was hard."', True),
              ('"I used to it now, although the first winter was hard."', False),
              ('"I am used to adapt now, although the first winter was hard."', False)]),
            ('You want to say that becoming familiar with the long distances took six months. You say:',
             [('"It took me six months to be used to drive everywhere."', False),
              ('"It took me six months to get used to driving everywhere."', True),
              ('"It took me six months to used to driving everywhere."', False)]),
            ('You want to say you have not yet adapted to planning a week ahead. The natural version is:',
             [('"I am not used to plan a week ahead yet."', False),
              ('"I do not use to plan a week ahead yet."', False),
              ('"I am not used to planning a week ahead yet."', True)]),
            ('Somebody asks what your evenings were like in the city eleven years ago. You answer:',
             [('"I used to sit in traffic until half past eight."', True),
              ('"I was used to sit in traffic until half past eight."', False),
              ('"I am used to sitting in traffic until half past eight."', False)]),
        ],
        'think': 'Describe one thing you are still not used to, three years after moving. Say what it was like at '
                 'the start, whether you have got used to any part of it since, and what you think would have to '
                 'happen for it to stop bothering you. Use be used to at least twice and get used to at least twice.',
    },

    # ------------------------------------------------------------ complementares
    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Documentary',
         'title': 'A Year in the Life of a Scottish Island &mdash; BBC Scotland (full film, 58 min)',
         'desc': 'Islanders and incomers on what a first year somewhere very small and very quiet actually does to '
                 'a person. Several of the speakers arrived from cities and describe exactly the month-three collapse.',
         'tip': 'count how many times somebody says get used to rather than used to. The islanders use the '
                'process form constantly, because for them adapting never quite finishes.',
         'url': 'https://www.youtube.com/watch?v=1KV1qEhVBFk', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; Why Nobody Feels Rich',
         'desc': 'A psychologist on hedonic adaptation: the machinery that makes any new situation, good or bad, '
                 'become normal within months. It is the science under everything you did in class tonight.',
         'tip': 'the guest speaks faster than the host. Listen to five minutes of the guest with no transcript, '
                'then use the free transcript on the page to check what you caught.',
         'url': 'https://hiddenbrain.org/podcast/why-nobody-feels-rich/', 'cta': 'Listen on Hidden Brain'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'The secrets of learning a new language &mdash; Lydia Machova, TED (10 min)',
         'desc': 'A Slovak speaker, in clear non-native English, on what actually makes an adult adapt to something '
                 'genuinely difficult. Her accent is a gift: this is the English you meet in real international rooms.',
         'tip': 'watch it twice. The first time for the argument; the second time only listening to how she '
                'pronounces her vowels, which are Slavic and completely unlike an American set.',
         'url': 'https://www.ted.com/talks/lydia_machova_the_secrets_of_learning_a_new_language',
         'cta': 'Watch on TED'},
    ],
}
