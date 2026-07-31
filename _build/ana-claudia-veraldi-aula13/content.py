# -*- coding: utf-8 -*-
"""Aula 13 -- If I Lived in the Middle of Nowhere (second conditional).

Modelo FALA (aula IMPAR, REGRA 29): dialogo line-by-line + 3 role-plays, sem ic-reading.
Sotaques do listening (CURRICULO V3): italiano + britanico.
Callback da aula 12: ela planejou um sabado inteiro com condicoes reais. Hoje o mesmo
formato de frase muda de tempo e passa a descrever o que NAO e verdade -- e o erro
numero quatro da aula passada (would no lugar de will) vira a regra de hoje.
"""

LESSON = {
    'n': 13,
    'model': 'speech',
    'menu_title': 'If I Lived in the Middle of Nowhere',
    'menu_desc': 'The land next door, the horses she does not have and the life she keeps almost '
                 'deciding on -- and the tense English reserves for none of it being true',
    'grammar_point': 'second conditional for unreal and hypothetical situations',
    'chapter_tag': 'The Life Not Chosen',
    'title_html': 'If I Lived in the <span class="accent">Middle of Nowhere</span>',
    'title_sub': 'Last week the condition was real. Tonight none of it is true, and English changes tense to say so.',
    'phases': ['First Words', 'The Words of Supposing', 'Two People Who Almost Did It',
               'The Code', 'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1487215078519-e21cc028cb29?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'The Land Next Door <span class="accent">Is for Sale</span>',
        'callback': 'Last time you planned a whole Saturday out loud, with the condition attached to every job, '
                    'and every one of those conditions could genuinely happen.',
        'question': 'If the field next to your house came up for sale tomorrow, what would you actually do with it?',
    },
    'framing': {
        'heading': 'The Same Sentence, <span class="accent">One Tense Further Back</span>',
        'steps': [('The Words', 'far-fetched, feasible, a long shot, wishful thinking...'),
                  ('Two People', 'an Italian who did it and an Englishman who did not'),
                  ('The Code', 'the past tense that is not about the past at all')],
        'note': 'Last week you said <em>if it rains, I will work inside</em>, and it might really rain. Tonight the '
                'sentence looks almost identical and means the opposite: <strong>none of it is true</strong>. '
                'English marks that with a past tense, and the past has nothing to do with time here.',
    },
    'hook': {
        'label': 'The Real Question',
        'heading': 'What Is Actually <span class="accent">Stopping You?</span>',
        'line1': 'Everybody has one version of their life that they can describe in complete detail and have never '
                 'moved a single step towards.',
        'line2': 'The interesting part is never the dream. It is the one sentence that starts with <em>but</em> '
                 'immediately after it.',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'The Language of <span class="accent">Supposing</span>',
    'vocab_sub': 'Twelve items &mdash; ten of them plain, two of them whole expressions',
    'vocab': [
        {'word': 'Far-fetched', 'icon': 'globe',
         'def': 'So unlikely that it is difficult to take seriously',
         'ex': 'Keeping horses out here is not far-fetched at all, it is just expensive.',
         'match': 'so unlikely that it is difficult to take seriously'},
        {'word': 'To daydream', 'icon': 'cloud',
         'def': 'To imagine something pleasant while you should be doing something else',
         'ex': 'I daydream about that field every time I drive past it.',
         'match': 'to imagine something pleasant instead of concentrating'},
        {'word': 'A long shot', 'icon': 'target', 'expr': True,
         'def': 'Something with a very small chance of working, but worth trying',
         'ex': 'Buying the land is a long shot, but I have asked the price twice.',
         'match': 'something with a small chance of working, but worth trying'},
        {'word': 'Feasible', 'icon': 'tool',
         'def': 'Possible to do in practice, with the money and time you actually have',
         'ex': 'Two horses would be feasible. Six would not.',
         'match': 'possible to do in practice with the time and money you have'},
        {'word': 'Hypothetically', 'icon': 'help',
         'def': 'Used to introduce a situation that is imagined rather than real',
         'ex': 'Hypothetically, if the field were mine, the first thing would be a fence.',
         'match': 'used to introduce a situation that is imagined, not real'},
        {'word': 'To picture something', 'icon': 'eye',
         'def': 'To form a clear image of something in your mind',
         'ex': 'I can picture the whole thing: the fence, the gate, the two horses.',
         'match': 'to form a clear image of something in your mind'},
        {'word': 'Wishful thinking', 'icon': 'star', 'expr': True,
         'def': 'Believing something because you want it, not because it is likely',
         'ex': 'Saying the price will drop is wishful thinking and I know it.',
         'match': 'believing something because you want it, not because it is likely'},
        {'word': 'To weigh something up', 'icon': 'scale',
         'def': 'To consider the good and bad sides carefully before deciding',
         'ex': 'I have been weighing it up for two years and I am no closer.',
         'match': 'to consider the good and bad sides carefully before deciding'},
        {'word': 'Tempting', 'icon': 'heart',
         'def': 'Attractive enough to make you want it, even against your better judgement',
         'ex': 'The price is tempting, which is exactly what worries me.',
         'match': 'attractive enough to make you want it against your judgement'},
        {'word': 'Plausible', 'icon': 'shield',
         'def': 'Believable, whether or not it turns out to be true',
         'ex': 'His explanation was plausible, but I would still check it.',
         'match': 'believable, whether or not it turns out to be true'},
        {'word': 'To be inclined to', 'icon': 'compass',
         'def': 'To have a mild tendency towards a choice, without having decided',
         'ex': 'I am inclined to leave it and see whether anybody else buys it.',
         'match': 'to have a mild tendency towards a choice, without deciding'},
        {'word': 'To settle for something', 'icon': 'anchor',
         'def': 'To accept something smaller than what you originally wanted',
         'ex': 'I would rather wait than settle for half the field.',
         'match': 'to accept something smaller than what you originally wanted'},
    ],
    'vocabnote': 'Two of tonight&rsquo;s twelve are whole expressions: <strong>a long shot</strong> and '
                 '<strong>wishful thinking</strong>. They mark the two ends of the same road. A long shot is '
                 'unlikely but honest and worth attempting; wishful thinking is when you have quietly stopped '
                 'checking whether it is true.',
    'pron': [
        'Far-fetched',
        'Plausible',
        'Wishful thinking',
        'If I had ten more hectares, I would keep two horses.',
    ],
    'gapfill': [
        ('"Keeping horses out here is not ', 'far-fetched', ' at all, it is just expensive."'),
        ('"Buying the land is ', 'a long shot', ', but I have asked the price twice."'),
        ('"Two horses would be ', 'feasible', '. Six would not."'),
        ('"Saying the price will drop is ', 'wishful thinking', ' and I know it."'),
        ('"The price is ', 'tempting', ', which is exactly what worries me."'),
        ('"His explanation was ', 'plausible', ', but I would still check it."'),
    ],

    # ------------------------------------------------------------ chapter 3
    'ch3': {
        'heading': 'Two People Who <span class="accent">Almost Did It</span>',
        'sub': 'One of them bought the land. The other one is still describing it.',
    },
    'dialogue': {
        'heading': 'Marco Bought <span class="accent">the Field</span>',
        'guest_name': 'Marco',
        'guest_key': 'marco',
        'guest_voice': 'italian_m',
        'lines': [
            ('marco', 'So the field is still for sale. If I were you, I would go and offer them something this week.'),
            ('ana', 'I have been <span class="vocab-highlight">weighing it up</span> for two years, Marco.'),
            ('marco', 'Two years. And in two years, has the price ever gone down?'),
            ('ana', 'No. Saying it will is <span class="vocab-highlight">wishful thinking</span> and I know it. But if I bought it, I would have nothing left for the roof.'),
            ('marco', 'Then buy half. Or is that <span class="vocab-highlight">settling for</span> something you would resent?'),
            ('ana', 'Honestly, yes. If I had the whole field, I would <span class="vocab-highlight">picture</span> the fence and the two horses. Half a field is just grass.'),
            ('marco', 'That is not <span class="vocab-highlight">far-fetched</span>, you know. Two horses on that land would be completely <span class="vocab-highlight">feasible</span>. I did the same thing in Umbria and I was terrified for a year.'),
            ('ana', 'And if it had gone wrong? What would you have done?'),
        ],
        'comp': [
            ('What does Marco advise at the very start, and how does he phrase it?',
             'He tells her to go and offer them something this week, and he phrases it as advice: "If I were you, I would go and offer them something."'),
            ('What is the argument Marco uses about the two years?',
             'That in two years the price has never gone down, so waiting for it to drop is not a plan.'),
            ('What did Marco do himself, and how did he feel about it?',
             'He bought land in Umbria and did the same thing she is considering. He says he was terrified for a whole year.'),
        ],
    },
    'listenings': [
        {
            'voice': 'italian_f',
            'title': 'I Would Have Said <span class="accent">It Was Impossible</span>',
            'blurb': 'An Italian on the year she stopped describing the plan and started it. Sound first &mdash; no text.',
            'text': 'For about six years I had a very detailed answer ready for a question nobody had asked me. If '
                    'somebody said, what would you do if you could do anything, I had the whole thing: the piece of '
                    'land, the number of olive trees, even the colour of the shutters. I could describe it in more '
                    'detail than my actual flat. And then a friend of mine, who is not a kind person, asked me a '
                    'different question. She said, what would have to be true for you to do it this year. Not '
                    'someday. This year. And I discovered, sitting there, that I did not have an answer ready for '
                    'that one, because I had never once done the arithmetic. I had done the daydreaming for six '
                    'years and the arithmetic for zero hours. So I did it that weekend, on paper, and it turned out '
                    'that the thing I had been calling impossible was expensive and difficult and completely '
                    'possible. It took another two years. But the two years started that weekend, and not one of the '
                    'six years before it counted for anything at all.',
            'qs': [
                ('What did she have ready for six years, and how detailed was it?',
                 'A complete answer to a question nobody had asked: the piece of land, the number of olive trees, even the colour of the shutters. She could describe it in more detail than her actual flat.'),
                ('What was the different question her friend asked?',
                 'What would have to be true for her to do it THIS year, not someday.'),
                ('What did she discover when she finally did the arithmetic?',
                 'That the thing she had been calling impossible was expensive and difficult and completely possible. It still took two years, but the six years before counted for nothing.'),
            ],
        },
        {
            'voice': 'british_m',
            'title': 'The Question <span class="accent">Nobody Asks Back</span>',
            'blurb': 'An Englishman on the difference between a dream and a decision. Sound first &mdash; no text.',
            'text': 'I have a theory about this and it is not a comfortable one. When somebody tells you what they '
                    'would do if they had the money, or the time, or the land, they are almost never telling you '
                    'about the future. They are telling you about a decision they have already made and do not want '
                    'to admit to. Because the honest version of most of these sentences is not, I would move to the '
                    'coast if I could. It is, I could move to the coast and I have decided not to, and here are '
                    'eleven reasons that all sound like obstacles. And I say this as somebody who did exactly that '
                    'for nine years about a boat. Nine years of describing this boat. My wife could draw it. And '
                    'then one evening she asked me, very gently, whether I actually wanted the boat or whether I '
                    'wanted the conversation about the boat, and I have thought about that question probably once a '
                    'week ever since. I never bought the boat, by the way. But I did stop talking about it, and I '
                    'would say that was the more honest outcome of the two.',
            'qs': [
                ('What is his uncomfortable theory about people who say what they would do?',
                 'That they are almost never talking about the future. They are describing a decision they have already made and do not want to admit to.'),
                ('What is the honest version of most of those sentences, according to him?',
                 'Not "I would move to the coast if I could", but "I could move to the coast and I have decided not to, and here are eleven reasons that sound like obstacles."'),
                ('What did his wife ask him, and what happened in the end?',
                 'Whether he actually wanted the boat or wanted the conversation about the boat. He never bought it, but he stopped talking about it, which he says was the more honest outcome.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4
    'grammar': {
        'chapter_heading': 'A Past Tense With <span class="accent">Nothing to Do With Time</span>',
        'chapter_sub': 'if + past &middot; would &middot; and the were that survives in every person',
        'heading': 'None of These <span class="accent">Is True</span>',
        'examples': [
            'If I had ten more hectares, I would keep two horses.',
            'If I were you, I would offer them something this week.',
            'I would move to the coast tomorrow if it were not for the dogs.',
            'If I won that field at auction, I might sell the far end of it.',
        ],
        'prompt': 'Every one of these describes something that is <strong>not the case</strong>. Look at the verb '
                  'after <em>if</em>: it is in the past. Now ask the only question that matters &mdash; is any of '
                  'this about the past?',
        'rule_rows': [
            ('if + past simple, would + verb', 'An unreal or imaginary present or future.',
             '<strong>If I had</strong> more land, I <strong>would keep</strong> horses.'),
            ('the past is not past', 'It marks DISTANCE from reality, not distance in time.',
             '<strong>If I lived</strong> there... (I do not live there)'),
            ('were, in every person', 'Standard in this structure, including <em>I</em> and <em>she</em>.',
             '<strong>If I were</strong> you &middot; if it <strong>were not</strong> for the dogs'),
            ('would / could / might', 'The result half can soften exactly as it did last week.',
             'I <strong>might</strong> sell the far end.'),
            ('never would after if', 'The same rule as the first conditional, one tense down.',
             'never: <em>if I would have more land</em>'),
            ('first vs second', 'First: it may really happen. Second: it is not the case.',
             'If it <strong>rains</strong>... vs If I <strong>won</strong> the lottery...'),
            ('If I were to...', 'A more remote, slightly formal way of proposing a hypothesis.',
             '<strong>If I were to sell</strong>, where would I go?'),
        ],
        'oneliner': 'the past tense here means not real, and it never once means yesterday.',
    },
    'mistakes': [
        ('If I would have more land, I would keep horses.', 'If I had more land, I would keep horses.'),
        ('If I was you, I would not sell it.', 'If I were you, I would not sell it.'),
        ('If I have more time, I would restore the whole house.', 'If I had more time, I would restore the whole house.'),
        ('If I lived closer, I will visit every week.', 'If I lived closer, I would visit every week.'),
    ],
    'mistake_note': 'The first is <em>would</em> in the condition, which is forbidden in every conditional there is. '
                    'The second is the one native speakers argue about, and in this structure <strong>were</strong> '
                    'is the safe answer in every person. The third and fourth are the same crime from opposite '
                    'sides: they mix a real condition with an unreal result, or the reverse. Both halves have to '
                    'agree on whether this is happening or not.',
    'practice_heading': 'Real or <span class="accent">Unreal?</span>',
    'practice_fill': [
        ('"If I ', 'had', ' ten more hectares, I would keep two horses." (have &mdash; unreal, so mind the tense)'),
        ('"If I ', 'were', ' you, I would offer them something this week." (be &mdash; the form that survives here)'),
        ('"I would move to the coast tomorrow if it ', 'were not', ' for the dogs." (be, negative)'),
        ('"If it ', 'rains', ' on Saturday, I will work inside." (rain &mdash; careful, this one is REAL)'),
        ('"If I won that field at auction, I ', 'might sell', ' the far end." (sell &mdash; soften the result)'),
    ],
    'artifact': {
        'heading': 'The Field <span class="accent">Next Door</span>',
        'title': 'LAND FOR SALE &mdash; LOT 7, ADJOINING A. VERALDI',
        'subtitle': 'Two hectares &middot; on the market for 26 months',
        'corner': 'Price<br>unchanged',
        'label_width': '120px',
        'rows': [
            ('Size', 'two hectares, flat, one side already fenced'),
            ('Water', 'a well, working, tested in March'),
            ('Access', 'shares the entrance with the house. No new gate needed'),
            ('Condition', 'grass and nine old trees. Nothing to demolish'),
            ('Time on market', '26 months. Two offers, both withdrawn'),
            ('Asking price', 'unchanged since the day it was listed'),
        ],
        'comp': [
            ('Say what you would do first if the field were yours tomorrow.',
             '"If the field were mine, the first thing I would do is fence the open side." Past tense in the condition, would in the result, and none of it is true yet.'),
            ('Use the well and the shared entrance to say why this is not far-fetched.',
             '"If the water did not work, it would be a different conversation. As it is, I would not have to dig a well or build an entrance." Notice the second sentence is real, so it drops out of the conditional entirely.'),
            ('Now give yourself advice, out loud, in the form Marco used.',
             '"If I were you, I would offer them something below the asking price and see what happens." If I were you is the single most useful second conditional in the language.'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'quickfire': [
        {'situation': 'Somebody asks what you would do with the field if you bought it. Answer with the whole sentence, not just the second half.',
         'tips': ['If I bought it, I would fence the open side first and worry about the rest later.',
                  'Past tense after if, would in the result.']},
        {'situation': 'A friend is hesitating about the same kind of decision. Give her advice in the classic form.',
         'tips': ['If I were you, I would go and ask the price before anybody else does.',
                  'If I were you, never if I was you, in this structure.']},
        {'situation': 'Somebody asks whether you are painting the veranda on Saturday. Careful &mdash; this one is real.',
         'tips': ['If it is dry by ten, I will get the first coat on.',
                  'Real condition, so present tense and will. Last week&rsquo;s grammar, on purpose.']},
        {'situation': 'Say what would stop you, using the structure that names the single obstacle.',
         'tips': ['I would move to the coast tomorrow if it were not for the dogs.',
                  'If it were not for X is how English names one obstacle and dismisses all the others.']},
        {'situation': 'Soften a hypothetical result so it does not sound like a promise.',
         'tips': ['If I won that field at auction, I might sell the far end of it.',
                  'Might and could work exactly as they did in the first conditional.']},
        {'situation': 'Answer the Englishman&rsquo;s question honestly: is there something you talk about more than you pursue?',
         'tips': ['If I am honest, I have been describing that field for two years and doing the arithmetic for none.',
                  'This one has no grammar target. Say the true thing.']},
    ],
    'speaking': [
        ('What would you do if the field next door were yours tomorrow?',
         'If it were mine, I would fence the open side, plant along the road, and keep two horses within a year.'),
        ('What advice would you give somebody who has been hesitating for two years?',
         'If I were them, I would make one low offer and let the answer decide it, instead of waiting for a price that never moves.'),
        ('What is the one thing that would have to change for you to do it?',
         'I would do it tomorrow if it were not for the roof, which has to happen first and eats the same money.'),
        ('And what will you do this Saturday, in the real world?',
         'If the rain holds off, I will paint the veranda. That one is not hypothetical at all.'),
    ],
    'building': [
        ('I / have ten more hectares / keep two horses (not true)',
         'If I had ten more hectares, I would keep two horses.'),
        ('I / be you / offer them something this week (advice)',
         'If I were you, I would offer them something this week.'),
        ('I / move to the coast tomorrow / not be for the dogs (one obstacle)',
         'I would move to the coast tomorrow if it were not for the dogs.'),
        ('it / rain on Saturday / I / work inside (careful: this one is real)',
         'If it rains on Saturday, I will work inside.'),
    ],
    'answerkey_heading': 'Real and Unreal on <span class="accent">One Screen</span>',
    'answerkey_title': 'Reveal the whole conditional key',
    'answerkey': [
        'SECOND: if + PAST SIMPLE, would + verb = not true, now or in general: if I had more land, I would keep horses',
        'the past tense marks DISTANCE FROM REALITY, never time. If I lived there = I do not live there',
        'were survives in every person in this structure: if I were you, if it were not for the dogs',
        'the result can soften with could or might, exactly as in the first conditional',
        'WOULD NEVER GOES AFTER IF. Not in the first conditional, not in this one, not in any of them',
        'FIRST: if + present, will = it may genuinely happen this Saturday. The two never mix halves',
        'if I were to + verb = the same idea, more remote and slightly more formal',
        'NEVER: if I would have &middot; if I was you (here) &middot; if I have more time I would &middot; if I lived closer I will',
    ],
    'rp_chapter_heading': 'The Life You <span class="accent">Keep Describing</span>',
    'roleplays': [
        {'heading': 'The Neighbour Selling <span class="accent">the Field</span>',
         'scenario': 'I own the field and I have had it on the market for twenty six months. I ask you three '
                     'things: what you would do with it, what you would change first, and what would stop you. '
                     'Answer each one in full sentences, and do not make me an offer yet.',
         'chips': ['if it were mine', 'I would', 'if it were not for']},
        {'heading': 'The Friend Who Has Heard It <span class="accent">Before</span>',
         'scenario': 'I am an old friend and I have heard about this field for two years. I am going to ask you '
                     'the unkind question from the listening: what would have to be true for you to do it this '
                     'year? Then give me advice about a decision of mine, in the same structure.',
         'chips': ['what would have to be true', 'if I were you', 'I would be inclined to']},
        {'heading': 'Two Minutes on <span class="accent">the Life You Did Not Pick</span>',
         'scenario': 'Describe, in detail, one version of your life that is not happening: where you would live, '
                     'what you would keep, what your day would look like. Then say the honest sentence at the end '
                     '&mdash; whether you actually want it, or whether you want the conversation about it.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'The Tense for <span class="accent">What Is Not True</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Supposing</span>',
    'survival': [
        'If I had ten more hectares, I would keep two horses.',
        'If I were you, I would offer them something this week.',
        'I would move to the coast tomorrow if it were not for the dogs.',
        'If I won that field at auction, I might sell the far end.',
        'Hypothetically, if the field were mine, the first thing would be a fence.',
    ],
    'checklist': [
        'I use the past simple after if when the situation is not true.',
        'I use would, could or might in the result half, never after if.',
        'I say if I were you, in every person, for advice and for hypotheses.',
        'I keep the first conditional for what may genuinely happen, and never mix the halves.',
        'I know the words: far-fetched, feasible, a long shot, wishful thinking, to weigh something up.',
    ],
    'badge': {
        'name': 'The Life Not Chosen',
        'text': 'You have just described a life that is not happening, in complete detail, in a tense that exists '
                'for exactly that purpose &mdash; and then told an Italian and an Englishman the truth about it.',
        'next': 'Asking Nicely, and Who You Are Asking',
    },

    # ------------------------------------------------------------ teacher (icone T)
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Last week '
                 'the condition could really happen. Tonight none of it is true.&quot; O recorte da noite e o '
                 'CONTRASTE com a aula 12 -- e o erro numero 4 daquele slide de Common Mistake (would no lugar de '
                 'will) vira a regra de hoje. Se ela lembrar disso sozinha, otimo sinal.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 12: ela planejou um sabado inteiro '
                  'com condicoes reais. PONTE (REGRA 27B): &quot;Every one of those could happen. Tonight, none of '
                  'them can.&quot; A pergunta do campo vizinho e a espinha da aula inteira -- ANOTE tudo que ela '
                  'disser, porque o artefato do capitulo 4 e exatamente esse campo. ZERO correcao aqui.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos. A frase de baixo e a tese: a frase '
                   'parece quase igual a da semana passada e significa o oposto. Diga que o passado aqui nao tem '
                   'nada a ver com tempo -- e so plante, nao explique.',
        'hook': '<strong>Pergunta-gatilho (2 min):</strong> O ponto e a frase que comeca com <em>but</em>. Peca a '
                'versao dela e NAO discuta o merito -- guarde para o role-play 2 e para o listening 2, que atacam '
                'exatamente isso. Se ela ficar desconfortavel, e sinal de que a aula acertou o alvo.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for talking about '
                       'something that is not happening. Click each card to reveal.&quot; Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista, Ana tenta, revele. CCQ '
                  '&quot;far-fetched&quot;: &quot;Is it impossible, or just very unlikely? (Improvavel a ponto de '
                  'ser dificil levar a serio -- nao e impossivel.)&quot; CCQ &quot;a long shot&quot;: &quot;Would I '
                  'try it? (Sim -- e improvavel MAS vale tentar, e essa segunda metade e a expressao inteira.)&quot; '
                  'CCQ &quot;feasible&quot;: &quot;Is it about believing, or about doing? (Fazer -- com o dinheiro e '
                  'o tempo que existem de verdade.)&quot;',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. CCQ &quot;wishful thinking&quot;: '
                  '&quot;Am I lying to somebody else, or to myself? (A mim mesma -- e o auto-engano educado.)&quot; '
                  'CCQ &quot;plausible&quot;: &quot;Is it true? (Nao sei. E CRIVEL, que e outra coisa -- e o '
                  'contraste com feasible vale ser feito em voz alta.)&quot; CCQ &quot;to settle for&quot;: '
                  '&quot;Am I happy? (Nao muito -- ha renuncia dentro da palavra.)&quot;',
        'matching': '<strong>Consolidate (4 min):</strong> Ana diz o par em voz alta e SO DEPOIS clica. Certo fica '
                    'verde, errado balanca, clicar num par feito DESFAZ. Use o vocab-note como ponte: a long shot e '
                    'honesto, wishful thinking e quando voce parou de conferir.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> &quot;Far-fetched&quot; -- as duas palavras colam e o '
                'R e mudo em ingles britanico, leve em americano. &quot;Plausible&quot; -- PLAW-zuh-bul, o S soa '
                'como Z. &quot;Wishful thinking&quot; -- os dois TH sao surdos e a lingua sai entre os dentes; e o '
                'som mais dificil da noite para brasileiro. Na frase inteira, &quot;would&quot; reduz para /wud/ e '
                'quase sempre vira <em>I&rsquo;d</em> na fala real -- avise, porque no listening ela vai ouvir a '
                'forma contraida e nao a do slide.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Leia cada frase. Ana diz a palavra que falta ANTES de '
                   'clicar. As candidatas estao no banco embaixo, fora de ordem. Se travar, aponte duas e pergunte '
                   'qual cabe. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao (1 min):</strong> Diga: &quot;Two people. One of them bought the land. The '
                     'other one is still describing it.&quot; Passe ao proximo.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e o Marco, ITALIANO, que ja fez o que a Ana esta '
                    'adiando. Clique &quot;Next Line&quot; e toque o audio de cada fala. Para cada fala da Ana, '
                    'peca que ELA fale primeiro. PRAGMATICA: o Marco pressiona com PERGUNTAS, nao com conselhos '
                    '(&quot;has the price ever gone down?&quot;) -- e uma forma de insistir que soa calorosa em '
                    'italiano e invasiva em cultura nordica. Comente no fim. A ultima fala da Ana usa a TERCEIRA '
                    'condicional de proposito: nao explique, so registre que ela existe.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre o MARCO, nao sobre a Ana (REGRA '
                         '27F). Ana responde ANTES de revelar. A 1a resposta ja entrega a estrutura da noite '
                         '(&quot;if I were you&quot;) sem regra nenhuma, de proposito.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de '
                      'tocar. Esta e uma ITALIANA: vogais muito abertas e puras, consoantes duplas marcadas, ritmo '
                      'silabico. Avise ANTES. O conteudo e o coracao da aula: seis anos de sonho e zero hora de '
                      'conta. Se a Ana ficar quieta depois, NAO preencha o silencio.',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Four sentences in the past tense. '
                     'Not one of them is about the past.&quot; Passe ao proximo.',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Peca que ela leia as quatro e responda: &quot;When '
                   'did these happen?&quot; A resposta certa e &quot;nunca&quot;, e e essa a descoberta. Depois '
                   'pergunte por que o ingles usaria passado para algo que nao aconteceu. So entao clique '
                   '&quot;Reveal the Rule&quot;. CCQ: &quot;If I had more land -- do I have more land? (Nao.)&quot; '
                   '&quot;If I were you -- am I you? (Nao, e nunca serei: por isso a forma mais irreal de todas.)'
                   '&quot; &quot;If it rains on Saturday -- might it rain? (Pode. E por isso NAO e esta '
                   'gramatica.)&quot;',
        'mistake': '<strong>Common mistake (4 min):</strong> O primeiro e would depois de if, proibido em toda '
                   'condicional. O segundo e o was/were: em ingles falado moderno &quot;if I was you&quot; existe, '
                   'mas nesta estrutura <em>were</em> e a resposta segura e a que ela vai ouvir em qualquer material '
                   'de exame. O terceiro e o quarto sao o MESMO crime por lados opostos -- metade real com metade '
                   'irreal. Peca 2 repeticoes das versoes certas.',
        'practice': '<strong>Practice (4 min):</strong> Ana escolhe ORALMENTE antes de clicar. A QUARTA e armadilha '
                    'proposital: e a primeira condicional da aula passada no meio das irreais. Se ela colocar '
                    '&quot;rained&quot;, pergunte: &quot;Might it actually rain on Saturday?&quot; e ela se corrige '
                    'sozinha.',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA ANTES de tocar. Este e '
                      'um BRITANICO: vogais longas, R final que some, T bem marcado. Avise ANTES. Este audio e o '
                      'mais duro da aula de proposito: a tese e que quem diz &quot;eu faria se pudesse&quot; quase '
                      'sempre ja decidiu que nao. Deixe pousar. Se ela reagir, pare e converse -- vale mais que o '
                      'proximo slide.',
        'artifact': '<strong>Artefato (5 min):</strong> E o campo vizinho, escrito como anuncio. Peca que ela '
                    'transforme CADA linha numa frase da segunda condicional. So depois as 3 perguntas. A 2a e a '
                    'mais fina: parte do anuncio e REAL (o poco funciona), entao aquela metade sai da condicional. '
                    'Se ela mantiver tudo no irreal, aponte a linha do poco.',
        'ch5_trans': '<strong>Transicao practice (1 min):</strong> Diga: &quot;Now we train: detective, quick fire, '
                     'and building.&quot; Passe ao proximo.',
        'detective': '<strong>Detective (4 min):</strong> Leia cada frase com erro. &quot;What is wrong here?&quot; '
                     'Ana corrige ANTES de clicar. Sao os quatro do slide de Common Mistake.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> Uma situacao por vez, resposta em voz alta ANTES das '
                     'Tips. A 3a e armadilha proposital (o sabado e real, entao e a gramatica da aula passada) e a '
                     '6a nao tem alvo gramatical nenhum: e a pergunta honesta do listening 2. Nao corrija a 6a.',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija a '
                    'forma certa: as tres primeiras pedem segunda condicional, a QUARTA volta para a primeira. Se '
                    'ela usar would na quarta, devolva a pergunta em vez de corrigir.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase COMPLETA em voz alta, depois '
                    'clica para comparar. A quarta e real de proposito. Toggle: clicar de novo fecha (REGRA 27E).',
        'answerkey': '<strong>Answer key (3 min):</strong> O accordion nasce fechado. Abra SO depois que ela tentou '
                     'tudo. As duas linhas em maiusculas sao as unicas que nao podem ser esquecidas: o passado '
                     'marca irrealidade, e would nunca entra depois de if.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;Now you describe a life that is not '
                     'happening. Three steps, and the last one has no help.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e o dono do campo. Registro neutro, quase burocratico '
               '-- nao venda nada. Faca as tres perguntas na ordem. Corrija SO a estrutura condicional.',
        'rp2': '<strong>Role-play Semi-free (4 min):</strong> Voce e a amiga antiga que ja ouviu essa historia. Faca '
               'a pergunta do listening 1 (&quot;what would have to be true for you to do it THIS year?&quot;) e '
               'NAO aceite resposta vaga. Depois inverta: peca conselho sobre uma decisao SUA, para forcar o &quot;'
               'if I were you&quot; na producao dela.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem anotacao, sem interrupcao. NAO corrija '
               'durante. CONTE quantas segundas condicionais completas ela produz e quantas vezes o if-clause '
               'escorrega para o presente. Diga os numeros no fim. Meta: pelo menos quatro completas e zero would '
               'depois de if.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;You just spent two minutes in a life '
                     'you do not have, in the only tense English keeps for it.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Leia cada frase e toque o audio. Peca que a Ana repita. '
                    'As cinco cobrem: if + past com would, if I were you, if it were not for, might no resultado, e '
                    'hypothetically abrindo a frase. Insista no /wud/ reduzido.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Leia cada item. Todos os 5 checks = aula completa e a aula 13 registrada como concluida no '
                     'passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Thirteen lessons, Ana. Two conditionals down, '
                 'and you can already hear the difference between what might happen and what will not.&quot; '
                 'Homework (oralmente, opcional): gravar um minuto respondendo a pergunta da italiana -- o que '
                 'precisaria ser verdade para acontecer ESTE ano. Proxima aula: Asking Nicely, and Who You Are '
                 'Asking -- perguntas indiretas e a escala de diretividade entre culturas, que e o eixo '
                 'intercultural do bloco.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'If I Lived in the Middle of Nowhere -- Dreams, Hypotheses and What Is Not True',
        'desc': 'The field next door, the horses she does not have, and the tense English keeps for none of it being true.',
        'context_paras': [
            'The field next to Ana&rsquo;s house has been for sale for twenty six months and she has been '
            '<strong>weighing it up</strong> for two years. <strong>If she bought it</strong>, she '
            '<strong>would fence</strong> the open side first, and <strong>if the money went further</strong> than '
            'she thinks, she <strong>would keep</strong> two horses within a year. She can '
            '<strong>picture</strong> the whole thing: the fence, the gate, the nine old trees.',
            'None of it is <strong>far-fetched</strong>. Two horses on two hectares would be entirely '
            '<strong>feasible</strong>, and the well already works. The problem is the roof, which needs the same '
            'money in the same year. <strong>If it were not for</strong> the roof, she says, she '
            '<strong>would have made</strong> an offer already. Buying half the field would be '
            '<strong>settling for</strong> something she would resent, so she is '
            '<strong>inclined to</strong> wait.',
            'Her neighbour Marco is blunter about it. <strong>If he were her</strong>, he says, he '
            '<strong>would offer</strong> something below the asking price this week and let the answer decide it. '
            'Waiting for the price to drop after twenty six months is <strong>wishful thinking</strong>, and '
            'everybody involved knows it. It is <strong>a long shot</strong>, certainly. It is also the only move '
            'on the board.',
        ],
        'context_quiz': [
            ('"If she bought it, she would fence the open side." Why bought and not buys?',
             [('Because she has not bought it: the past tense marks that the situation is not real.', True),
              ('Because the purchase happened in the past.', False),
              ('Because bought is more formal than buys.', False)]),
            ('"If it were not for the roof, she would have made an offer already." What does if it were not for do here?',
             [('It names the single obstacle and dismisses all the others.', True),
              ('It states that the roof has already been repaired.', False),
              ('It softens a request so it sounds more polite.', False)]),
            ('"If he were her, he would offer something below the asking price." Why were and not was?',
             [('Because in this structure were is used with every person, and it is the safe form.', True),
              ('Because he is talking about more than one person.', False),
              ('Because the sentence is in the plural.', False)]),
        ],
        'tip_title': 'The Second Conditional',
        'tip_sub': 'A past tense that has nothing to do with the past. It marks distance from reality.',
        'tip_rows': [
            ('if + past simple, would + verb', 'An unreal present or future', '<strong>If I had</strong> more land, I <strong>would keep</strong> horses.'),
            ('the past is not past', 'It marks distance from REALITY, not time', '<strong>If I lived</strong> there... (I do not)'),
            ('were, in every person', 'Standard here, including I and she', '<strong>If I were</strong> you...'),
            ('would / could / might', 'The result half can soften', 'I <strong>might</strong> sell the far end.'),
            ('never would after if', 'The same rule as the first conditional', 'never: <em>if I would have</em>'),
            ('first vs second', 'First may happen; second is not the case', 'If it <strong>rains</strong>... vs If I <strong>won</strong>...'),
            ('if I were to...', 'A more remote, slightly formal hypothesis', '<strong>If I were to sell</strong>, where would I go?'),
        ],
        'tip_never': 'If I would have more land &middot; if I was you (in this structure) &middot; if I have more '
                     'time I would restore it &middot; if I lived closer I will visit. The first puts would in the '
                     'condition, the second uses the form that exams do not accept here, and the last two mix a '
                     'real half with an unreal one.',
        'fills': [
            ('If I ', 'had', ' ten more hectares, I would keep two horses.',
             'have -- the situation is not real, so the tense moves back'),
            ('If I ', 'were', ' you, I would offer them something this week.',
             'be -- one word, and it is the form that survives in every person here'),
            ('I would move to the coast tomorrow if it ', 'were not', ' for the dogs.',
             'be, negative, two words -- the structure that names one single obstacle'),
            ('If it ', 'rains', ' on Saturday, I will work inside.',
             'rain -- careful, this condition is REAL and belongs to lesson 12'),
            ('If I won that field at auction, I ', 'might sell', ' the far end of it.',
             'sell -- two words, and the result is softened rather than promised'),
            ('Keeping horses out here is not ', 'far-fetched', ' at all, it is just expensive.',
             'one word, hyphenated -- so unlikely that it is hard to take seriously'),
        ],
        'order_intro': 'Marco thinks Ana should make an offer on the field. Put the exchange in a logical order.',
        'order': [
            'So the field is still for sale. If I were you, I would go and offer them something this week.',
            'I have been weighing it up for two years, Marco.',
            'Two years. And in two years, has the price ever gone down?',
            'No. Saying it will is wishful thinking and I know it.',
            'Then buy half. Or is that settling for something you would resent?',
            'Honestly, yes. If I had the whole field, I would picture the fence and the two horses.',
        ],
        'quiz': [
            ('A friend asks what you would do with the land if you owned it. You answer:',
             [('"If I owned it, I would fence the open side first."', True),
              ('"If I would own it, I would fence the open side first."', False),
              ('"If I own it, I would fence the open side first."', False)]),
            ('You want to give somebody advice about a decision. The most natural version is:',
             [('"If I was you, I would make an offer."', False),
              ('"If I were you, I would make an offer."', True),
              ('"If I would be you, I would make an offer."', False)]),
            ('You want to name the one thing stopping you. You say:',
             [('"I would move tomorrow if it was not because of the dogs."', False),
              ('"I would move tomorrow unless the dogs."', False),
              ('"I would move tomorrow if it were not for the dogs."', True)]),
            ('Somebody asks what you are doing on Saturday if the weather is good. You answer:',
             [('"If it were dry, I would paint the veranda."', False),
              ('"If it is dry, I will paint the veranda."', True),
              ('"If it was dry, I will paint the veranda."', False)]),
        ],
        'think': 'Describe one version of your life that is not happening: where you would live, what you would '
                 'keep, and what an ordinary day would look like. Then answer the hard question honestly: what '
                 'would have to be true for you to start it this year? Use the second conditional at least four '
                 'times, and if I were you at least once when you give yourself advice.',
    },

    # ------------------------------------------------------------ complementares
    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Documentary',
         'title': 'The Biggest Little Farm &mdash; official full film on the National Geographic channel (91 min)',
         'desc': 'A couple with no experience buy two hundred acres of dead soil and spend eight years finding out '
                 'what was feasible and what was wishful thinking. It is your field, multiplied by a hundred.',
         'tip': 'listen for how often they say would in the first twenty minutes, while the farm is still '
                'imaginary, and how the word almost disappears once the work starts.',
         'url': 'https://www.youtube.com/watch?v=E1vaCXeoCcA', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'Hidden Brain &mdash; The Ventilator (on the decisions we describe but never make)',
         'desc': 'On the distance between what people say they would do and what they do. The episode is the '
                 'research behind the Englishman in tonight&rsquo;s second listening.',
         'tip': 'the guest uses would constantly, always about situations that are not real. Count five of them '
                'and write down the whole sentence each time.',
         'url': 'https://hiddenbrain.org/podcast/the-ventilator/', 'cta': 'Listen on Hidden Brain'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Talk',
         'title': 'The psychology of your future self &mdash; Dan Gilbert, TED (7 min)',
         'desc': 'Seven minutes on why the person you imagine being in ten years is almost never the person you '
                 'become. Clear, slow American English and very funny.',
         'tip': 'watch it once, then again and pause every time he describes a hypothetical. Almost every '
                'sentence in the talk is built the way tonight&rsquo;s grammar is built.',
         'url': 'https://www.ted.com/talks/dan_gilbert_the_psychology_of_your_future_self',
         'cta': 'Watch on TED'},
    ],
}
