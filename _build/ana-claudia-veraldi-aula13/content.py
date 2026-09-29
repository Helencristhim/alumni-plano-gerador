# -*- coding: utf-8 -*-
"""Aula 13 -- If I Lived in the Middle of Nowhere (second conditional).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques (CURRICULO V3, linha 13 do hub): italiano (listening 1 + dialogo) + britanico (listening 2).
Callback da aula 12: planos reais com condicao (if + present / will). Hoje a mesma frase
recua um tempo e passa a falar do que NAO e verdade.
Veiculo: as casas de 1 euro nas vilas italianas e a vida "longe de tudo" -- hipoteses,
nenhum fato biografico unico vira espinha. O gosto dela por restaurar entra como detalhe.
Pragmatica: 'If I were you' -- conselho direto (italiano) x conselho amaciado (britanico).
"""

LESSON = {
    'n': 13,
    'model': 'speech',
    'menu_title': 'If I Lived in the Middle of Nowhere',
    'menu_desc': 'One-euro houses in Italian villages, a cottage with no signal and the life you can describe '
                 'in detail but have never started -- and the tense English keeps for things that are not true',
    'grammar_point': 'second conditional for unreal and hypothetical situations',
    'chapter_tag': 'Dreams and Hypotheses',
    'title_html': 'If I Lived in the <span class="accent">Middle of Nowhere</span>',
    'title_sub': 'Last week the condition could really happen. Tonight none of it is true, and English changes tense to say so.',
    'phases': ['First Words', 'The Words of Supposing', 'The Code', 'Many Englishes',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1487215078519-e21cc028cb29?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Week, Every Plan <span class="accent">Could Happen</span>',
        'callback': 'Two words from last week, in one sentence about your real weekend: tentative, a fallback, '
                    'to call off, to hinge on, iffy, to pencil something in, to play it by ear, to take a rain check.',
        'question': 'Then: if you could live anywhere in the world for one year, where would you go?',
    },
    'framing': {
        'heading': 'The Same Sentence, <span class="accent">One Tense Back</span>',
        'steps': [('The Words', 'far-fetched, feasible, a long shot, off the grid...'),
                  ('The Code', 'a past tense that is not about the past'),
                  ('Many Englishes', 'an Italian who did it and an Englishman who did not')],
        'note': 'Last week you said <em>if it rains, I will stay home</em>, and it might really rain. Tonight the '
                'sentence looks almost the same and means the opposite: <strong>none of it is true</strong>. '
                'English marks that with a past tense, and here the past has nothing to do with time.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'What Is Actually <span class="accent">Stopping You?</span>',
        'line1': 'Almost everybody has one version of their life that they can describe in complete detail and '
                 'have never taken a single step towards.',
        'line2': 'What is yours? And what is the sentence that comes right after it, the one that starts with '
                 '<em>but</em>?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'The Language of <span class="accent">Supposing</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'Far-fetched', 'icon': 'globe',
         'def': 'So unlikely that it is difficult to take seriously',
         'ex': 'Moving to a village in Italy is not far-fetched. People do it every year.',
         'match': 'so unlikely that it is difficult to take seriously'},
        {'word': 'Feasible', 'icon': 'tool',
         'def': 'Possible to do in practice, with the time and money you really have',
         'ex': 'Restoring one small room is feasible. Restoring the whole house is not.',
         'match': 'possible to do with the time and money you really have'},
        {'word': 'Remote', 'icon': 'map',
         'def': 'Far away from towns, roads and other people',
         'ex': 'The village is so remote that the bus comes twice a week.',
         'match': 'far away from towns, roads and other people'},
        {'word': 'Self-sufficient', 'icon': 'leaf',
         'def': 'Able to produce what you need without help from outside',
         'ex': 'If we grew our own vegetables, we would be almost self-sufficient.',
         'match': 'able to produce what you need without outside help'},
        {'word': 'Tempting', 'icon': 'heart',
         'def': 'Attractive enough to make you want it, even when it is not a good idea',
         'ex': 'A house for one euro is very tempting, until you read the small print.',
         'match': 'attractive enough to make you want it, even if it is a bad idea'},
        {'word': 'Hypothetically', 'icon': 'help',
         'def': 'Used to introduce a situation that is imagined, not real',
         'ex': 'Hypothetically, if you had a year off, what would you do with it?',
         'match': 'used to introduce a situation that is imagined, not real'},
        {'word': 'To picture something', 'icon': 'eye',
         'def': 'To form a clear image of something in your mind',
         'ex': 'I can picture the house: blue shutters, a fig tree and no neighbors.',
         'match': 'to form a clear image of something in your mind'},
        {'word': 'To weigh something up', 'icon': 'scale',
         'def': 'To think carefully about the good and bad sides before you decide',
         'ex': 'She weighed it up for months before she said no.',
         'match': 'to think about the good and bad sides before you decide'},
        {'word': 'To be cut off', 'icon': 'lock',
         'def': 'To be separated from other people, roads or communication',
         'ex': 'In winter the road floods and the whole village is cut off.',
         'match': 'to be separated from people, roads or communication'},
        {'word': 'Off the grid', 'icon': 'zap', 'expr': True,
         'def': 'Living without public electricity, water or internet',
         'ex': 'If I lived off the grid, I would miss the internet more than the electricity.',
         'match': 'living without public electricity, water or internet'},
        {'word': 'A long shot', 'icon': 'target', 'expr': True,
         'def': 'Something with a very small chance of working, but worth trying',
         'ex': 'Getting one of those houses is a long shot, but I sent an email anyway.',
         'match': 'something with a small chance of working, but worth trying'},
        {'word': 'Wishful thinking', 'icon': 'star', 'expr': True,
         'def': 'Believing something because you want it, not because it is likely',
         'ex': 'Thinking the renovation will cost nothing is wishful thinking.',
         'match': 'believing something because you want it, not because it is likely'},
    ],
    'vocabnote': 'Three of tonight&rsquo;s words are whole expressions: <strong>off the grid</strong>, '
                 '<strong>a long shot</strong> and <strong>wishful thinking</strong>. The last two sit at opposite '
                 'ends of the same road. A long shot is unlikely but honest; wishful thinking is when you have '
                 'stopped checking whether it is true.',
    'pron': [
        'Far-fetched',
        'Self-sufficient',
        'Hypothetically',
        'If I lived in the middle of nowhere, I would miss the noise.',
    ],
    'gapfill': [
        ('"Living abroad for a year is not ', 'far-fetched', '. People do it all the time."'),
        ('"One small room is ', 'feasible', '. The whole house is not."'),
        ('"The farm is so ', 'remote', ' that the nearest shop is forty minutes away."'),
        ('"With a well and a vegetable garden, they are almost ', 'self-sufficient', '."'),
        ('"A house for one euro sounds ', 'tempting', ', until you see the roof."'),
        ('"They have no electricity company and no internet. They live completely ', 'off the grid', '."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Code)
    'ch3': {
        'heading': 'A Past Tense With <span class="accent">Nothing to Do With Time</span>',
        'sub': 'if + past &middot; would &middot; and the were that works for every person',
    },
    'grammar': {
        'heading': 'None of These <span class="accent">Is True</span>',
        'examples': [
            'If I <span style="color:#c2410c;font-weight:700">lived</span> in a village, I <span style="color:#c2410c;font-weight:700">would miss</span> the noise.',
            'If I <span style="color:#1d4ed8;font-weight:700">were</span> you, I <span style="color:#1d4ed8;font-weight:700">would visit</span> the village first.',
            'If the house <span style="color:#7c3aed;font-weight:700">had</span> a good roof, I <span style="color:#7c3aed;font-weight:700">would buy</span> it tomorrow.',
            'If I <span style="color:#15803d;font-weight:700">won</span> the lottery, I <span style="color:#15803d;font-weight:700">might restore</span> a whole street.',
        ],
        'prompt': 'Every one of these sentences describes something that is <strong>not the case</strong>. Look at '
                  'the verb after <em>if</em>: it is in the past. Now the only question that matters &mdash; is '
                  'any of this about the past?',
        'rule_rows': [
            ('if + past simple, would + verb', 'An unreal or imaginary present or future.',
             '<strong>If I lived</strong> there, I <strong>would miss</strong> the noise.'),
            ('the past is not past', 'It marks distance from REALITY, not distance in time.',
             '<strong>If I had</strong> a year off... (I do not have one)'),
            ('were, for every person', 'The standard form here, even with I, he and she.',
             '<strong>If I were</strong> you &middot; if she <strong>were</strong> here'),
            ('would / could / might', 'The result can be softened.',
             'I <strong>might</strong> restore a whole street.'),
            ('never would after if', 'The same rule as the first conditional.',
             'never: <em>if I would have more time</em>'),
            ('first vs second', 'First: it can really happen. Second: it is not the case.',
             'If it <strong>rains</strong>... vs If I <strong>won</strong> the lottery...'),
        ],
        'oneliner': 'the past tense here means NOT REAL &mdash; it never means yesterday.',
    },
    'practice_heading': 'Real or <span class="accent">Unreal?</span>',
    'practice_fill': [
        ('"If I ', 'had', ' a year off, I would live in a village in Italy." (have &mdash; unreal, so mind the tense)'),
        ('"If I ', 'were', ' you, I would visit the village in winter first." (be &mdash; advice)'),
        ('"If the house had a good roof, I ', 'would buy', ' it tomorrow." (buy &mdash; the result)'),
        ('"If it ', 'rains', ' on Saturday, I will stay home." (rain &mdash; careful, this one is REAL)'),
        ('"If the village ', 'were not', ' so remote, more people would live there." (be, negative)'),
        ('"If I won the lottery, I ', 'might restore', ' a whole street." (restore &mdash; soften the result)'),
    ],

    # ------------------------------------------------------------ chapter 4 (Many Englishes)
    'ch4': {
        'heading': 'Somebody Who Did It, <span class="accent">Somebody Who Did Not</span>',
        'sub': 'Italian and British English &mdash; and two very different ways to give advice',
    },
    'dialogue': {
        'heading': 'Marco Bought <span class="accent">a One-Euro House</span>',
        'guest_name': 'Marco',
        'guest_key': 'marco',
        'guest_voice': 'italian_m',
        'lines': [
            ('marco', 'So you saw the one-euro houses in Abruzzo? If I were you, I would apply this week.'),
            ('ana', 'It is very <span class="vocab-highlight">tempting</span>. But if I bought one, I would have to restore it in three years.'),
            ('marco', 'Three years is <span class="vocab-highlight">feasible</span>. I did mine in two, and I knew nothing about roofs.'),
            ('ana', 'I know a little about restoring. But the village is so <span class="vocab-highlight">remote</span>. If I lived there, I would feel <span class="vocab-highlight">cut off</span>.'),
            ('marco', 'In January, yes. The road closes when it snows. But in May you would never want to leave.'),
            ('ana', 'Honestly? Moving there is <span class="vocab-highlight">a long shot</span>. I am only <span class="vocab-highlight">weighing it up</span>.'),
            ('marco', 'That is how everybody starts. If people only moved when they were sure, the village would be empty.'),
            ('ana', 'Okay. If I visited in winter and still liked it, I would send the application.'),
        ],
        'comp': [
            ('What advice does Marco give Ana at the start?',
             'He says: if I were you, I would apply this week.'),
            ('How long did Marco take to restore his house, and what did he know about roofs?',
             'Two years, and he knew nothing about roofs.'),
            ('What happens to Marco&rsquo;s village in January, and how does he describe May?',
             'The road closes when it snows. In May, he says, you would never want to leave.'),
        ],
    },
    'listenings': [
        {
            'file': 'a13_listening_giulia.mp3',
            'voice': 'italian_f',
            'label': 'Listening 1 &middot; Italy',
            'title': 'The Village With <span class="accent">Forty People</span>',
            'blurb': 'A woman from Milan on the house she almost bought. Sound first &mdash; no text.',
            'text': 'My name is Giulia, and I grew up in Milan, where nobody knows their neighbors. Three years ago '
                    'I visited a village in Sicily with forty people and a house for one euro. I fell in love in '
                    'about ten minutes. I could picture everything: a table under the fig tree, my friends from '
                    'Milan coming for the summer. Then an old man in the bar asked me a simple question. He said, '
                    'if you lived here, what would you do on a Tuesday in February? I had no answer. The shop '
                    'opens twice a week, there is no doctor, and the bus goes to the city at six in the morning. '
                    'I did not buy the house. But I did not forget the question either. Now, every time I have a '
                    'big dream, I ask myself about the Tuesday in February. If I had asked it earlier, I would have '
                    'saved a lot of daydreaming.',
            'qs': [
                ('Where did Giulia grow up, and what is it like there?',
                 'In Milan, where nobody knows their neighbors.'),
                ('What question did the old man in the bar ask her?',
                 'If you lived here, what would you do on a Tuesday in February?'),
                ('What does Giulia do now, every time she has a big dream?',
                 'She asks herself about the Tuesday in February.'),
            ],
        },
        {
            'file': 'a13_listening_simon.mp3',
            'voice': 'british_m',
            'label': 'Listening 2 &middot; United Kingdom',
            'title': 'The Cottage <span class="accent">With No Signal</span>',
            'blurb': 'An Englishman on the dream he talked about for ten years. Sound first &mdash; no text.',
            'text': 'I am Simon, and I live in Bristol. For about ten years I told everybody the same story. If I '
                    'had the money, I would buy a stone cottage in the Scottish Highlands, somewhere with no '
                    'phone signal, and I would live completely off the grid. Solar panels, a wood stove, '
                    'vegetables in the garden. My friends had heard it so many times that they could finish my '
                    'sentences. Then last year my sister asked me, quite gently, whether I actually wanted the '
                    'cottage or just the conversation about the cottage. That hurt a bit, to be honest. So I '
                    'rented one for two weeks in November. It rained for fourteen days, the stove smoked, and I '
                    'drove forty minutes every morning to find a signal. I loved it, and I would not live there. '
                    'Both of those things are true. And I have stopped telling the story, which my friends are '
                    'very happy about.',
            'qs': [
                ('What did Simon say he would do if he had the money?',
                 'Buy a stone cottage in the Scottish Highlands with no phone signal and live off the grid.'),
                ('What did his sister ask him?',
                 'Whether he actually wanted the cottage or just the conversation about the cottage.'),
                ('What happened when he rented a cottage for two weeks, and what did he decide?',
                 'It rained for fourteen days, the stove smoked, and he drove forty minutes to find a signal. He loved it, but he would not live there.'),
            ],
        },
    ],
    'artifact': {
        'heading': 'A House for <span class="accent">One Euro</span>',
        'title': 'HOUSE FOR 1 EURO &mdash; LOT 12, A HILL VILLAGE IN ABRUZZO',
        'subtitle': 'Prepared for Ana Claudia Veraldi &middot; information sheet',
        'corner': 'Deadline<br>30 November',
        'label_width': '130px',
        'rows': [
            ('Price', '1 euro. Notary and taxes: about 3,000 euros'),
            ('Condition', 'two floors, stone walls, the roof needs to be replaced'),
            ('Obligation', 'restoration must start in 1 year and finish in 3'),
            ('Deposit', '5,000 euros, returned when the work is finished'),
            ('Village', '210 residents, one bar, shop open on Tuesdays and Fridays'),
            ('Nearest hospital', '45 minutes by car. The road sometimes closes in snow'),
        ],
        'comp': [
            ('If this house were yours, what would you do first?',
             '"If the house were mine, I would replace the roof before anything else." Past tense after if, would in the result.'),
            ('Would it be feasible for you? Give one reason for and one against.',
             '"It would be feasible, because I know how to restore things. But if the hospital were closer, I would feel safer."'),
            ('Give a friend advice about this house, the way Marco did.',
             '"If I were you, I would visit the village in winter before you send the application."'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('If I would live in Italy, I would learn Italian.', 'If I lived in Italy, I would learn Italian.'),
        ('If I was you, I would visit in winter.', 'If I were you, I would visit in winter.'),
        ('If I have more time, I would restore the whole house.', 'If I had more time, I would restore the whole house.'),
        ('If I lived closer, I will visit you every week.', 'If I lived closer, I would visit you every week.'),
    ],
    'quickfire': [
        {'situation': 'A friend asks where you would live if you could choose any place in the world. Answer with the whole sentence.',
         'tips': ['If I could choose, I would live in a small town in the north of Italy.',
                  'Past tense after if, would in the result.']},
        {'situation': 'Your friend is thinking about buying an old house. Give her advice.',
         'tips': ['If I were you, I would ask a builder to look at the roof first.',
                  'If I were you &mdash; never if I would be you.']},
        {'situation': 'Somebody asks what you are doing on Saturday if the weather is good. Careful &mdash; this one is real.',
         'tips': ['If it is sunny, I will go for a walk by the lake.',
                  'A real condition: present and will. Last week&rsquo;s grammar.']},
        {'situation': 'Say what you would miss if you lived completely off the grid.',
         'tips': ['If I lived off the grid, I would miss hot showers more than the internet.',
                  'Off the grid: no public electricity, water or internet.']},
        {'situation': 'Soften a hypothetical result so it does not sound like a promise.',
         'tips': ['If I had a year off, I might travel around Europe.',
                  'Might and could make the result less certain.']},
        {'situation': 'A friend says she will find a house in Italy that needs no work at all. React honestly.',
         'tips': ['Honestly? That sounds like wishful thinking.',
                  'Wishful thinking: believing it because you want it.']},
    ],
    'speaking': [
        ('If you could live anywhere for one year, where would you go?',
         'If I could live anywhere, I would spend a year in a small village in Portugal, near the sea.'),
        ('What would you miss if you lived in a very remote place?',
         'If I lived somewhere very remote, I would miss my friends and a good hospital nearby.'),
        ('What would you do if you had a whole year with no work?',
         'If I had a year off, I would restore an old house from scratch and learn Italian.'),
        ('What advice would you give somebody who wants to live off the grid?',
         'If I were them, I would try it for two weeks in winter before they decide.'),
    ],
    'building': [
        ('I / live in a village / miss the noise (not true)',
         'If I lived in a village, I would miss the noise.'),
        ('I / be you / visit in winter first (advice)',
         'If I were you, I would visit in winter first.'),
        ('the house / have a good roof / I / buy it (not true)',
         'If the house had a good roof, I would buy it.'),
        ('it / rain on Saturday / I / stay home (careful: this one is real)',
         'If it rains on Saturday, I will stay home.'),
    ],
    'answerkey_heading': 'Real and Unreal on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        'SECOND conditional: if + PAST SIMPLE, would + verb = not true: If I <strong>lived</strong> there, I <strong>would miss</strong> the noise.',
        'The past tense means NOT REAL, never yesterday: if I had a year off = I do not have one.',
        'Were for every person: If I <strong>were</strong> you &middot; if the village <strong>were not</strong> so remote.',
        'Soften the result with could or might: I <strong>might</strong> restore a whole street.',
        'Never would after if &mdash; in the first conditional or in this one.',
        'FIRST conditional (if + present, will) = it can really happen: If it <strong>rains</strong>, I <strong>will</strong> stay home.',
        'Do not mix the halves: never if I have more time, I would &middot; never if I lived closer, I will.',
        'And the one that is not grammar: an Italian says if I were you, I would... very directly; a British speaker often softens it: if I were you, I might think about...',
    ],
    'rp_chapter_heading': 'The Life You <span class="accent">Keep Describing</span>',
    'roleplays': [
        {'heading': 'The Italian Who <span class="accent">Wants an Answer</span>',
         'scenario': 'You are talking to Marco, an Italian who lives in a one-euro house. He is direct and '
                     'enthusiastic. He asks you three things: what you would do with the house, what you would '
                     'change first, and what would stop you. Answer each one in full sentences.',
         'chips': ['If the house were mine', 'I would', 'If it were not so remote']},
        {'heading': 'The British Friend <span class="accent">Who Softens Everything</span>',
         'scenario': 'Now you talk to a British friend. She asks you: what would have to be true for you to do '
                     'it this year? Answer her. Then give her advice about her own dream of a cottage in '
                     'Scotland &mdash; politely, the British way.',
         'chips': ['What would have to be true', 'If I were you, I might', 'feasible']},
        {'heading': 'Two Minutes on <span class="accent">the Other Life</span>',
         'scenario': 'Describe one version of your life that is not happening: where you would live, what your '
                     'house would look like, and what you would do on a Tuesday in February. Then say the honest '
                     'sentence: do you really want it, or do you want the conversation about it?',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'The Tense for <span class="accent">What Is Not True</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Supposing</span>',
    'survival': [
        'If I lived in a village, I would miss the noise.',
        'If I were you, I would visit in winter first.',
        'If the house had a good roof, I would buy it tomorrow.',
        'If I had a year off, I might travel around Europe.',
        'Hypothetically, what would you do on a Tuesday in February?',
    ],
    'checklist': [
        'I use the past simple after if when the situation is not true.',
        'I use would, could or might in the result, and never would after if.',
        'I say if I were you when I give advice.',
        'I keep the first conditional for things that can really happen, and I never mix the halves.',
        'I know the words: far-fetched, feasible, remote, off the grid, a long shot, wishful thinking.',
    ],
    'badge': {
        'name': 'The Other Life',
        'text': 'You described a life that is not happening, in the tense that exists for exactly that &mdash; '
                'and you asked the Tuesday-in-February question.',
        'next': 'Asking Nicely -- and Who You Are Asking',
    },

    # ------------------------------------------------------------ teacher (icone T)
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Last week '
                 'the condition could really happen. Tonight, none of it is true.&quot; O recorte da aula: sonhos e '
                 'hipoteses (a outra vida que ela descreve e nunca comecou), com o veiculo das casas de 1 euro nas '
                 'vilas italianas. Contraste com a aula 12 e o fio da noite.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 12. Peca UMA frase sobre o fim de '
                  'semana REAL dela usando duas palavras da lista (tentative, a fallback, to call off, to hinge on, '
                  'iffy, to pencil in, to play it by ear, to take a rain check). PONTE (REGRA 27B): &quot;Those plans '
                  'could happen. Now, something that is not going to happen.&quot; e a pergunta do slide. Livre, '
                  'ZERO correcao. Anote se ela diz &quot;if I would live&quot; &mdash; e o diagnostico de hoje.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase de baixo e a tese: a frase '
                   'parece a da semana passada e significa o oposto. Diga que o passado aqui nao e tempo &mdash; so '
                   'plante, nao explique a regra.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela descrever a &quot;outra vida&quot; com '
                'detalhes. O ponto e a frase com <em>but</em> que vem depois. NAO corrija a forma aqui: anote as '
                'frases exatas &mdash; voltam corrigidas no capitulo 3 e no role-play 3.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for talking about '
                       'something that is not happening. Three of them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista em ingles, Ana tenta a palavra, revele. '
                  'CCQ far-fetched: &quot;Is it impossible, or just very unlikely? (Muito improvavel.)&quot; CCQ '
                  'feasible: &quot;Can you really do it with your time and money? (Sim.)&quot; CCQ self-sufficient: '
                  '&quot;Do you need the supermarket? (Nao.)&quot; Peca um exemplo da vida dela em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ to weigh something up: &quot;Have you decided '
                  'yet? (Nao, ainda esta pensando nos pros e contras.)&quot; CCQ a long shot x wishful thinking: '
                  '&quot;Which one is honest about the chances? (A long shot.)&quot; CCQ off the grid: &quot;Do you '
                  'pay an electricity bill? (Nao.)&quot; Pronuncia: off the grid liga tudo &mdash; /o-fthe-GRID/.',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta, depois voces '
                    'conferem juntas. Leia a nota embaixo: as tres expressoes da noite.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> far-FETCHED (forca na segunda parte), '
                'self-suf-FI-cient (forca no FI, o c soa /sh/), hy-po-THE-ti-cally (forca no THE). Na frase inteira, '
                '&quot;I would&quot; vira &quot;I&apos;d&quot; na fala natural &mdash; mostre as duas formas. 2 '
                'repeticoes de cada.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra que falta ANTES de clicar. As '
                   'candidatas estao no banco, fora de ordem &mdash; ela ESCOLHE, nao adivinha. Clicar de novo fecha '
                   '(REGRA 27E).',
        'ch3_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. A past tense that has '
                     'nothing to do with the past.&quot; Nao explique ainda.',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases com ela (toque o audio). Pergunte: '
                   '&quot;Is any of this true? Do I live in a village? Am I you? Did I win the lottery?&quot; (Nao.) '
                   'Depois: &quot;Look at the verb after if. What tense is it? Is it about the past?&quot; Espere '
                   'ela descobrir que o passado marca IRREALIDADE. So entao &quot;Reveal the Rule&quot;. CCQs: '
                   '&quot;If I had a year off &mdash; do I have a year off? (Nao.)&quot; &quot;If I were you &mdash; '
                   'why were and not was? (Forma padrao nesta estrutura, para todas as pessoas.)&quot; Contraste '
                   'com a 12: &quot;If it rains &mdash; can it really rain? (Sim, e real.)&quot;',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a forma ORALMENTE antes de clicar. O item 4 e a '
                    'armadilha: e REAL (first conditional), entao presente + will. Se ela usar o passado ali, '
                    'pergunte: &quot;Can it really rain on Saturday?&quot;',
        'ch4_trans': '<strong>Transicao Many Englishes (1 min):</strong> Diga: &quot;Now an Italian who did it and '
                     'an Englishman who did not.&quot; Avise que vai ouvir sotaque italiano (vogais abertas, '
                     'r vibrado, final de palavra com vogal extra: &quot;house-a&quot;) e britanico.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Marco, italiano, que comprou uma casa de 1 euro em '
                    'Abruzzo. Clique &quot;Next Line&quot; e toque o audio de cada fala. Nas falas da Ana, peca que '
                    'ELA fale primeiro. PRAGMATICA: o Marco da conselho de forma DIRETA (&quot;If I were you, I '
                    'would apply this week&quot;) &mdash; para um italiano isso e carinho, nao grosseria. Guarde '
                    'para o role-play 2, onde o britanico faz o oposto.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o MARCO, nunca sobre a Ana '
                         '(REGRA 27F). Ana responde ANTES de revelar. Na 1, puxe a forma: &quot;What structure does '
                         'he use for advice?&quot; (If I were you, I would...)',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de '
                      'tocar &mdash; elas ja estao visiveis. Sotaque ITALIANO: vogais bem abertas, ritmo cantado, '
                      'as vezes uma vogal extra no fim da palavra. Toque 2 vezes. No fim, pergunte: &quot;And you? '
                      'What would you do on a Tuesday in February?&quot; &mdash; e a pergunta que atravessa a aula.',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'BRITANICO: o r final nao soa (&quot;cottage&quot;, &quot;November&quot;), o t de &quot;quite&quot; '
                      'e bem marcado. Toque 2 vezes. Pragmatica: o Simon amacia tudo (&quot;quite gently&quot;, '
                      '&quot;to be honest&quot;, &quot;a bit&quot;). Pergunte: &quot;Is he sad or happy at the '
                      'end?&quot; (Os dois &mdash; e ele diz isso.)',
        'artifact': '<strong>Artefato (5 min):</strong> A ficha de uma casa de 1 euro, preparada para ela. Peca que '
                    'leia cada linha e diga UMA frase na segunda condicional (&quot;If I bought it, I would have to '
                    'start in one year&quot;). Use o gosto dela por restaurar: &quot;Would it be feasible for '
                    'you?&quot; Depois as 3 perguntas &mdash; ela responde antes de revelar.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick answers, '
                     'and your own sentences.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 4 erros classicos: would '
                     'depois do if, was em vez de were no conselho, e os dois que MISTURAM as metades (real com '
                     'irreal). Se ela achar os 4 sozinha, a forma esta consolidada.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 3a e a armadilha (e real &mdash; first conditional). As dicas sao modelos, '
                     'nao gabarito: se ela usar a vida dela, vale mais.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA (com a metade '
                    'do if). Exija pelo menos um &quot;If I were you&quot; e um &quot;might&quot;. As respostas '
                    'modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase COMPLETA em voz alta, depois clica '
                    'para comparar. O item 4 e real. Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so depois de tudo feito, para conferir. A ultima '
                     'linha nao e gramatica: e a diferenca de conselho direto (italiano) e amaciado (britanico).',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Three '
                     'conversations, three different people.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o Marco, italiano, direto e entusiasmado. Faca as 3 '
               'perguntas do cenario, uma por vez. Ana usa os chips. Corrija SO o would depois do if e o was/were.',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e uma amiga britanica. Pergunte: &quot;What would '
               'have to be true for you to do it this year?&quot; Depois ela te da conselho sobre o seu sonho do '
               'cottage na Escocia &mdash; o jeito britanico: &quot;If I were you, I might think about...&quot;. '
               'PRAGMATICA: compare com o Marco. Qual soa melhor para quem?',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO corrija '
               'durante. Conte quantas vezes ela usa a segunda condicional e diga o numero no fim. Anote qualquer '
               '&quot;if I would&quot; para o feedback final. A frase honesta do fim e o ponto alto &mdash; deixe '
               'ela terminar.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Cada uma cobre '
                    'uma engrenagem: a estrutura basica, o conselho, a condicao irreal sobre uma coisa, o resultado '
                    'suavizado com might e a pergunta hipotetica.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Leia cada item. Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Thirteen lessons in, and tonight you talked '
                 'about a life that is not happening &mdash; in the right tense.&quot; Homework (oralmente, '
                 'opcional): gravar um audio de um minuto respondendo a pergunta da Giulia &mdash; &quot;If you '
                 'lived in your dream place, what would you do on a Tuesday in February?&quot; Proxima aula: '
                 'Asking Nicely &mdash; perguntas indiretas e educadas, e como o grau de diretividade muda de um '
                 'pais para outro.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'If I Lived in the Middle of Nowhere -- Dreams, Hypotheses and What Is Not True',
        'desc': 'One-euro houses in Italy, a cottage with no signal and the tense English keeps for things that are not true.',
        'context_paras': [
            'Every year, small villages in Italy sell old houses for one euro. It sounds '
            '<strong>far-fetched</strong>, but it is real. The catch is that you must restore the house in three '
            'years. Ana has been <strong>weighing it up</strong>. <strong>If she bought</strong> one, she '
            '<strong>would replace</strong> the roof first, and <strong>if she had</strong> more time, she '
            '<strong>would restore</strong> the whole house herself.',
            'Her friend Marco lives in one of those villages. It is very <strong>remote</strong>: in January the '
            'road closes and the village is <strong>cut off</strong>. &quot;<strong>If I were you</strong>, I '
            '<strong>would visit</strong> in winter first,&quot; he says. He grows his own vegetables and is '
            'almost <strong>self-sufficient</strong>.',
            'Ana can <strong>picture</strong> the house very clearly, but she knows that thinking it will be easy '
            'is <strong>wishful thinking</strong>. <strong>If the village were not</strong> so far from a hospital, '
            'she <strong>would apply</strong> tomorrow. For now, it is <strong>a long shot</strong> &mdash; and a '
            'very <strong>tempting</strong> one.',
        ],
        'context_quiz': [
            ('"If she bought one, she would replace the roof first." Why bought and not buys?',
             [('Because she has not bought one: the past tense shows the situation is not real.', True),
              ('Because she bought the house last year.', False),
              ('Because bought is more polite than buys.', False)]),
            ('"If I were you, I would visit in winter first." What is Marco doing?',
             [('Telling a story about his past.', False),
              ('Giving Ana advice.', True),
              ('Making a promise.', False)]),
            ('Why does Ana not apply for the house tomorrow?',
             [('Because the house is too expensive.', False),
              ('Because Marco told her not to.', False),
              ('Because the village is far from a hospital.', True)]),
        ],
        'tip_title': 'The Second Conditional',
        'tip_sub': 'A past tense that has nothing to do with the past. It shows that something is not real.',
        'tip_rows': [
            ('if + past simple, would + verb', 'An unreal present or future', '<strong>If I lived</strong> there, I <strong>would miss</strong> the noise.'),
            ('the past is not past', 'It shows distance from reality, not time', '<strong>If I had</strong> a year off... (I do not)'),
            ('were, for every person', 'The standard form, even with I and she', '<strong>If I were</strong> you...'),
            ('would / could / might', 'The result can be softened', 'I <strong>might</strong> travel around Europe.'),
            ('question form', 'would + subject + verb', 'What <strong>would you do</strong> if you won?'),
            ('first vs second', 'First can happen; second is not true', 'If it <strong>rains</strong>... vs If I <strong>won</strong>...'),
        ],
        'tip_never': 'If I would live in Italy &middot; if I have more time, I would restore it &middot; if I '
                     'lived closer, I will visit. The first puts would after if; the other two mix a real half with '
                     'an unreal half.',
        'fills': [
            ('If I ', 'lived', ' in a village, I would miss the noise.',
             'live -- the situation is not real, so the tense moves back'),
            ('If I ', 'were', ' you, I would visit in winter first.',
             'be -- one word, the standard form for advice'),
            ('If the house had a good roof, I ', 'would buy', ' it tomorrow.',
             'buy -- two words, the result'),
            ('If it ', 'rains', ' on Saturday, I will stay home.',
             'rain -- careful, this condition is REAL'),
            ('If I had a year off, I ', 'might travel', ' around Europe.',
             'travel -- two words, a softer result'),
            ('Living abroad for a year is not ', 'far-fetched', '. People do it all the time.',
             'one word with a hyphen -- so unlikely that it is hard to take seriously'),
        ],
        'order_intro': 'Marco thinks Ana should buy a one-euro house. Put the conversation in order.',
        'order': [
            'So you saw the one-euro houses? If I were you, I would apply this week.',
            'It is very tempting. But if I bought one, I would have to restore it in three years.',
            'Three years is feasible. I did mine in two.',
            'But the village is so remote. If I lived there, I would feel cut off.',
            'In January, yes. But in May you would never want to leave.',
            'Okay. If I visited in winter and still liked it, I would send the application.',
        ],
        'quiz': [
            ('A friend asks where you would live if you could choose. You answer:',
             [('"If I could choose, I would live in a small village in Italy."', True),
              ('"If I would choose, I would live in a small village in Italy."', False),
              ('"If I can choose, I would live in a small village in Italy."', False)]),
            ('You want to give a friend advice about a house. The most natural version is:',
             [('"If I would be you, I would ask a builder."', False),
              ('"If I were you, I would ask a builder first."', True),
              ('"If I am you, I would ask a builder."', False)]),
            ('A British friend wants to buy a cottage with no signal. A soft, polite way to give advice is:',
             [('"You are wrong. Do not do it."', False),
              ('"If I were you, I might try it for two weeks first."', True),
              ('"If I will be you, I try it."', False)]),
            ('Somebody asks about your plans for Saturday if the weather is good. You answer:',
             [('"If it were sunny, I would go to the lake."', False),
              ('"If it is sunny, I will go to the lake."', True),
              ('"If it was sunny, I will go to the lake."', False)]),
        ],
        'think': 'Describe one version of your life that is not happening: where you would live, what your house '
                 'would look like and what you would do on a Tuesday in February. Then answer honestly: what would '
                 'have to be true for you to start it? Use the second conditional at least four times, and if I '
                 'were you at least once.',
    },

    # ------------------------------------------------------------ complementares (preenchido apos verificar links)
    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Documentary',
         'title': 'Italy&rsquo;s 1 Euro House Dream: The renovation reality &mdash; Foreign Correspondent, ABC (YouTube)',
         'desc': 'An Australian reporter follows foreigners who bought one-euro houses in an Italian town, and the '
                 'real cost of the renovation. It is Marco&rsquo;s story, told by the people living it, with Italian '
                 'and Australian accents side by side.',
         'tip': 'every time somebody describes the house before they bought it, say what YOU would do: if I bought '
                'that house, I would...',
         'url': 'https://www.youtube.com/watch?v=9umeNSIunak', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Stuff You Should Know &mdash; How Living Off the Grid Works',
         'desc': 'Fourteen minutes of relaxed American English on what it really takes to live without public '
                 'electricity and water: solar panels, wells, wood stoves and the bills you stop paying.',
         'tip': 'listen once for the gist. Then answer out loud: if you lived off the grid, what would you miss '
                'first?',
         'url': 'https://www.iheart.com/podcast/1119-stuff-you-should-know-26940277/episode/how-living-off-the-grid-works-29468204/',
         'cta': 'Listen on iHeart'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'The psychology of your future self &mdash; Dan Gilbert, TED',
         'desc': 'A short, funny talk on why the life we imagine for ourselves in ten years is almost never the life '
                 'we choose when we get there &mdash; the same idea as Simon and his cottage.',
         'tip': 'pause every time he describes a situation that is not real, and repeat his sentence. Many of them '
                'use would.',
         'url': 'https://www.ted.com/talks/dan_gilbert_the_psychology_of_your_future_self', 'cta': 'Watch on TED'},
    ],
}
