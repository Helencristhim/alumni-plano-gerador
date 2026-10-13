# -*- coding: utf-8 -*-
"""Aula 18 -- The Story Behind the Object (defining and non-defining relative clauses).

Modelo LEITURA (aula PAR, REGRA 29): ic-reading + gist + true/false.
Sotaques (CURRICULO V3, linha 18 do hub): alemao (listening 1) + britanico (listening 2 e
dialogo -- britanico masculino no listening, britanica no dialogo).
Callback da aula 17: have to / mustn't / should / had better + etiquette, a faux pas, when in Rome...
Veiculo: OBJETOS que contam historia (feira de antiguidades, heranca de familia, a gaveta com
uma carta) -- o restauro aparece pelo lado do objeto, nao da casa dela (a casa ja foi espinha
das aulas 3 e 7: REGRA DO FATO UNICO).
Eixo intercultural: pechinchar -- normal no Flohmarkt alemao e na feira britanica, estranho
numa loja; e o valor sentimental que nenhuma etiqueta de preco mede.
"""

LESSON = {
    'n': 18,
    'model': 'reading',
    'menu_title': 'The Story Behind the Object',
    'menu_desc': 'A suitcase from a Hamburg flea market, a desk with a letter from 1916 and a clock that '
                 'everybody stops to look at. Tonight, who, which, that, whose and where -- and the commas that '
                 'change the meaning',
    'grammar_point': 'defining and non-defining relative clauses with who, which, that, whose and where',
    'chapter_tag': 'Objects With a Past',
    'title_html': 'The Story Behind <span class="accent">the Object</span>',
    'title_sub': 'Every old object has a biography. English tells it with five small words and two commas.',
    'phases': ['First Words', 'The Words of Your World', 'The Story', 'The Code',
               'Practice', 'Your Turn', 'Wrap-Up'],
    'imgs': {
        'hero': 'https://images.unsplash.com/photo-1505228395891-9a51e7e86bf6?w=1400&q=80',
        'warmup': 'https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=1400&q=80',
        'vocab': 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1400&q=80',
        'ch3': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1400&q=80',
        'ch4': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80',
        'ch5': 'https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1400&q=80',
        'ch6': 'https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=1400&q=80',
        'ch7': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1400&q=80',
        'card': 'https://images.unsplash.com/photo-1505228395891-9a51e7e86bf6?w=600&q=80',
    },

    # ------------------------------------------------------------ chapter 1
    'warmup': {
        'heading': 'Last Time, <span class="accent">House Rules</span>',
        'callback': 'Tell me one rule of a place you know, with have to or mustn&rsquo;t, and use one word from last '
                    'week: etiquette, mandatory, optional, a faux pas, a rule of thumb, when in Rome.',
        'question': 'Then: what is the oldest object in your home, and where did it come from?',
    },
    'framing': {
        'heading': 'Every Object Has <span class="accent">a Biography</span>',
        'steps': [('The Words', 'an heirloom, a flea market, patina, sentimental value...'),
                  ('The Story', 'a text about the lives of old things'),
                  ('The Code', 'who, which, that, whose, where &mdash; and two commas')],
        'note': '<strong>The clock that my grandfather bought</strong> &mdash; that tells you WHICH clock. '
                '<strong>My clock, which is ninety years old,</strong> &mdash; that only adds a detail. Same word '
                'family, a different job, and the commas show you which one.',
    },
    'hook': {
        'label': 'One Old Thing',
        'heading': 'If It Could Talk, <span class="accent">What Would It Say?</span>',
        'line1': 'A chair, a ring, a photo, a recipe book: some objects live longer than the people who made them.',
        'line2': 'Choose one object in your life. Who had it before you, and what has it seen?',
    },

    # ------------------------------------------------------------ chapter 2
    'vocab_heading': 'Words for <span class="accent">Old Things</span>',
    'vocab_sub': 'Twelve words &mdash; nine plain, three expressions',
    'vocab': [
        {'word': 'An heirloom', 'icon': 'gift',
         'def': 'A valuable object that a family keeps for many generations',
         'ex': 'This ring is an heirloom. It was my great-grandmother&rsquo;s.',
         'match': 'a valuable object that a family keeps for generations'},
        {'word': 'A flea market', 'icon': 'map',
         'def': 'An outdoor market that sells old and used things',
         'ex': 'I found this mirror at a flea market in Hamburg.',
         'match': 'an outdoor market that sells old and used things'},
        {'word': 'Vintage', 'icon': 'star',
         'def': 'Old, but of good quality and still valued today',
         'ex': 'She only wears vintage dresses from the 1960s.',
         'match': 'old, but of good quality and still valued today'},
        {'word': 'Second-hand', 'icon': 'refresh',
         'def': 'Owned by someone else before you',
         'ex': 'Most of our furniture is second-hand, and I love it.',
         'match': 'owned by someone else before you'},
        {'word': 'Craftsmanship', 'icon': 'tool',
         'def': 'The skill of making things carefully and beautifully by hand',
         'ex': 'Look at the craftsmanship in this drawer. There is not a single nail.',
         'match': 'the skill of making things carefully by hand'},
        {'word': 'Patina', 'icon': 'sun',
         'def': 'The soft shine that an old surface gets with time and use',
         'ex': 'Please do not polish the table. The patina is part of its story.',
         'match': 'the soft shine an old surface gets with time and use'},
        {'word': 'To pass something down', 'icon': 'users',
         'def': 'To give something to a younger person in your family',
         'ex': 'My grandmother passed the recipe book down to my mother.',
         'match': 'to give something to a younger person in your family'},
        {'word': 'Sentimental value', 'icon': 'heart',
         'def': 'Importance that comes from memories, not from money',
         'ex': 'The watch is not expensive, but it has a lot of sentimental value.',
         'match': 'importance that comes from memories, not from money'},
        {'word': 'To haggle', 'icon': 'scale',
         'def': 'To discuss the price with the seller to pay less',
         'ex': 'At a flea market, everybody haggles a little.',
         'match': 'to discuss the price with the seller to pay less'},
        {'word': 'A diamond in the rough', 'icon': 'zap', 'expr': True,
         'def': 'Something with great hidden value that needs some work to shine',
         'ex': 'The chair was dirty and broken, but it was a diamond in the rough.',
         'match': 'something with hidden value that needs work to shine'},
        {'word': 'Worth its weight in gold', 'icon': 'key', 'expr': True,
         'def': 'Extremely useful or valuable',
         'ex': 'A good carpenter is worth his weight in gold.',
         'match': 'extremely useful or valuable'},
        {'word': 'One man\'s trash is another man\'s treasure', 'icon': 'leaf', 'expr': True,
         'def': 'Something one person throws away can be precious to someone else',
         'ex': 'My neighbor threw the old door away, and I took it home. One man\'s trash is another man\'s treasure.',
         'match': 'what one person throws away can be precious to another'},
    ],
    'vocabnote': 'Three of tonight&rsquo;s words are whole expressions: <strong>a diamond in the rough</strong>, '
                 '<strong>worth its weight in gold</strong> and <strong>one man&rsquo;s trash is another man&rsquo;s '
                 'treasure</strong>. And notice <strong>an</strong> heirloom: the h is silent, so it sounds like '
                 '<em>an AIR-loom</em>.',
    'pron': [
        'An heirloom',
        'Craftsmanship',
        'Patina',
        'The clock that my grandfather bought still works.',
    ],
    'gapfill': [
        ('"This ring is ', 'an heirloom', '. It was my great-grandmother&rsquo;s."'),
        ('"I found this mirror at ', 'a flea market', ' in Hamburg."'),
        ('"Please do not polish the table. The ', 'patina', ' is part of its story."'),
        ('"Look at the ', 'craftsmanship', ' in this drawer. There is not a single nail."'),
        ('"The watch is not expensive, but it has a lot of ', 'sentimental value', '."'),
        ('"The chair was dirty and broken, but it was ', 'a diamond in the rough', '."'),
    ],

    # ------------------------------------------------------------ chapter 3 (The Story)
    'ch3': {
        'heading': 'The Lives of <span class="accent">Old Things</span>',
        'sub': 'A short text, then a German woman and an Englishman tell their stories',
    },
    'reading': {
        'heading': 'The Letter in <span class="accent">the Drawer</span>',
        'rtitle': 'Every Object Has a Biography',
        'paras': [
            'A new object has a price. An old object has a biography. The chair <strong>that</strong> you buy in a '
            'shop today knows nothing. The chair <strong>which</strong> you find at a flea market has already '
            'lived a whole life: the family <strong>who</strong> bought it, the kitchen <strong>where</strong> it '
            'stood, the children <strong>whose</strong> shoes scratched its legs.',
            'This is why restorers often say that the best part of their work is not the wood or the paint. It is '
            'the surprises. A restorer in York once opened a writing desk, <strong>which</strong> had been closed '
            'for decades, and found a letter <strong>that</strong> a soldier wrote to his mother in 1916. The '
            'desk, <strong>which</strong> was worth about two hundred pounds, suddenly had a value <strong>that</strong> '
            'no price tag could show.',
            'Different cultures treat old things in different ways. In Germany, almost every city has a Sunday '
            'flea market, <strong>where</strong> people haggle happily over a lamp or a suitcase. In many '
            'Brazilian families, old furniture was simply replaced by something new, and the past went to the '
            'street. Today that is changing, and second-hand is becoming a choice, not a necessity.',
            'So next time you see an old object, ask the question <strong>that</strong> collectors always ask: '
            'not <em>how much is it?</em> but <em>who had it before me?</em>',
        ],
        'gist_prompt': 'Read once, quickly. Which title fits the whole text best?',
        'gist_choices': [
            ('How to find cheap furniture at flea markets in Germany and Brazil', False),
            ('Old objects carry the stories of the people who owned them', True),
            ('Why restorers prefer wood to paint', False),
        ],
        'tf': [
            ('The text says a new chair from a shop already has a story.', 'f',
             'It says the new chair knows nothing; the old one has already lived a whole life.'),
            ('According to restorers, the best part of the work is the surprises.', 't',
             'Not the wood or the paint: the surprises.'),
            ('The letter in the desk was written by a mother to her son.', 'f',
             'A soldier wrote it to his mother, in 1916.'),
            ('In German flea markets, people often haggle.', 't',
             'People haggle happily over a lamp or a suitcase.'),
            ('In the sentence The desk, which was worth about two hundred pounds, the part between the commas tells you which desk.', 'f',
             'It only adds extra information. We already know which desk.'),
        ],
    },
    'listenings': [
        {
            'file': 'a18_listening_greta.mp3',
            'voice': 'german_f',
            'label': 'Listening 1 &middot; Germany',
            'title': 'The Suitcase From <span class="accent">the Flea Market</span>',
            'blurb': 'A German woman on an old suitcase and the family that owned it. Sound first &mdash; no text.',
            'text': 'My name is Greta, and I live in Hamburg. Every Sunday I go to the flea market, which is next to '
                    'the river. Three years ago I saw an old brown suitcase, which was covered with hotel labels '
                    'from the nineteen fifties: Rome, Lisbon, Cairo. The man who was selling it wanted forty euros. '
                    'We haggled for ten minutes, which is completely normal at a German flea market, and I paid '
                    'twenty-five. At home I opened it and found a name inside the lid: Hannelore Weiss. I was '
                    'curious, so I searched online, and I found a woman whose grandmother had that name. She lived '
                    'in a small town near Bremen. I wrote to her, and she cried on the phone. The suitcase was the '
                    'one that her grandmother took on her honeymoon. I gave it back to her. I did not ask for the '
                    'twenty-five euros. Some things have a value that you cannot put on a price tag.',
            'qs': [
                ('What was special about the suitcase that Greta saw?',
                 'It was covered with hotel labels from the 1950s: Rome, Lisbon, Cairo.'),
                ('How much did Greta pay, and how?',
                 'Twenty-five euros. The man wanted forty, and they haggled for ten minutes.'),
                ('Who did Greta find, and what was the suitcase?',
                 'A woman whose grandmother was Hannelore Weiss. It was the suitcase that her grandmother took on her honeymoon.'),
            ],
        },
        {
            'file': 'a18_listening_tom.mp3',
            'voice': 'british_m',
            'label': 'Listening 2 &middot; United Kingdom',
            'title': 'The Desk That <span class="accent">Kept a Secret</span>',
            'blurb': 'An English furniture restorer on the best surprise of his life. Sound first &mdash; no text.',
            'text': 'I am Tom, and I restore old furniture in a small workshop in York, which used to be a '
                    'bakery. People think my job is about wood and glue, but really it is about stories. A few '
                    'years ago, a lady brought me a writing desk that she had bought at an auction. One of the '
                    'drawers, which had been stuck for decades, would not open. When I finally got it open, I found '
                    'a letter. It was from a young soldier who was writing to his mother in nineteen sixteen. He '
                    'told her not to worry, and he asked her to save him some of her apple cake. We never found '
                    'out if he came home. The lady, whose own grandfather had been a soldier, decided not to sell '
                    'the desk. She framed the letter and put it on the wall, right above the desk. That desk was '
                    'worth about two hundred pounds. Now it is worth its weight in gold.',
            'qs': [
                ('What was Tom&rsquo;s workshop before it was a workshop?',
                 'A bakery.'),
                ('What did Tom find in the drawer that had been stuck for decades?',
                 'A letter from a young soldier who was writing to his mother in 1916.'),
                ('What did the lady decide to do, and why is it interesting?',
                 'She decided not to sell the desk and framed the letter. Her own grandfather had been a soldier.'),
            ],
        },
    ],

    # ------------------------------------------------------------ chapter 4 (The Code)
    'ch4': {
        'heading': 'Which One, <span class="accent">or One More Detail?</span>',
        'sub': 'who &middot; which &middot; that &middot; whose &middot; where &mdash; and the two commas',
    },
    'grammar': {
        'heading': 'Five Small Words <span class="accent">and Two Commas</span>',
        'examples': [
            'The clock <span style="color:#c2410c;font-weight:700">that</span> my grandfather bought still works.',
            'This is the man <span style="color:#1d4ed8;font-weight:700">who</span> sold me the chair.',
            'My grandmother\'s sewing machine<span style="color:#7c3aed;font-weight:700">, which</span> is almost a hundred years old<span style="color:#7c3aed;font-weight:700">,</span> still works.',
            'The woman <span style="color:#15803d;font-weight:700">whose</span> table I restored sent me a photo.',
        ],
        'prompt': 'Look at the colored words. In which sentences do they tell you WHICH clock, man or woman? In which '
                  'one do they only add an extra detail? And what do the two commas do?',
        'rule_rows': [
            ('who / that', 'For people.', 'the man <strong>who</strong> sold me the chair'),
            ('which / that', 'For things.', 'the clock <strong>that</strong> my grandfather bought'),
            ('whose', 'Possession: his, her, their.', 'the woman <strong>whose</strong> table I restored'),
            ('where', 'For places.', 'the market <strong>where</strong> I found it'),
            ('defining &mdash; no commas', 'Tells you WHICH one. Without it, the sentence is not clear.',
             'The chair <strong>that I found</strong> is from 1940.'),
            ('non-defining &mdash; commas', 'Only extra information. Never that. In speech: a small pause.',
             'My clock<strong>, which is very old,</strong> still works.'),
        ],
        'oneliner': 'No commas = which one (that is fine). Commas = one more detail (never that).',
    },
    'practice_heading': 'Which <span class="accent">Word?</span>',
    'practice_fill': [
        ('"This is the man ', 'who', ' sold me the chair." (a person)'),
        ('"The clock ', 'that', ' my grandfather bought still works." (a thing &mdash; which one)'),
        ('"The woman ', 'whose', ' table I restored sent me a photo." (her table)'),
        ('"This is the flea market ', 'where', ' I found the mirror." (a place)'),
        ('"My sewing machine, ', 'which', ' is almost a hundred years old, still works." (extra detail, commas)'),
        ('"Hamburg, ', 'where', ' Greta lives, has a famous flea market." (a place, extra detail)'),
    ],
    'dialogue': {
        'heading': 'The Clock <span class="accent">on the Stall</span>',
        'guest_name': 'Harriet',
        'guest_key': 'harriet',
        'guest_voice': 'british_f',
        'lines': [
            ('harriet', 'Good morning! That clock you are looking at is my favorite thing on the stall.'),
            ('ana', 'It is beautiful. Look at the <span class="vocab-highlight">patina</span> on the wood. How old is it?'),
            ('harriet', 'About a hundred years. It belonged to a family who lived in Bath. It was an <span class="vocab-highlight">heirloom</span>.'),
            ('ana', 'Really? So why did they sell it?'),
            ('harriet', 'The grandson, who lives in Canada now, had no space for it. He was very sad to let it go.'),
            ('ana', 'I understand. Some things have a <span class="vocab-highlight">sentimental value</span> that money cannot pay. How much is it?'),
            ('harriet', 'Eighty pounds. But it is the clock that everybody stops to look at.'),
            ('ana', 'In Brazil we always <span class="vocab-highlight">haggle</span> a little at a market. Would you take sixty?'),
        ],
        'comp': [
            ('Where did the clock come from, according to Harriet?',
             'From a family who lived in Bath. It was an heirloom.'),
            ('Why did the family sell it?',
             'The grandson, who lives in Canada now, had no space for it.'),
            ('How much does Harriet want, and what does she say about the clock?',
             'Eighty pounds. She says it is the clock that everybody stops to look at.'),
        ],
    },
    'artifact': {
        'heading': 'Lot 47 <span class="accent">Has a Past</span>',
        'title': 'ONLINE AUCTION &mdash; LOT 47: OAK SEWING TABLE',
        'subtitle': 'Watched by: Ana Claudia Veraldi &middot; ends Sunday 20:00',
        'corner': 'Current bid<br>&pound;45',
        'label_width': '120px',
        'rows': [
            ('Made by', 'A carpenter from Leeds whose workshop closed in 1938'),
            ('Date', 'Around 1925'),
            ('Provenance', 'A farmhouse in Yorkshire, where the same family lived for ninety years'),
            ('Condition', 'Original handles. Small scratches on the top, which add to its character'),
            ('Inside', 'A drawer that still has the first owner&rsquo;s initials: M.H.'),
        ],
        'comp': [
            ('Who made the table? Answer with whose.',
             '"A carpenter from Leeds whose workshop closed in 1938."'),
            ('Where did the table come from? Answer with where.',
             '"From a farmhouse in Yorkshire, where the same family lived for ninety years."'),
            ('Would you bid on it? Say why, with which or that.',
             '"Yes. It is a table that has a story, and the scratches, which show its age, make it more interesting."'),
        ],
    },

    # ------------------------------------------------------------ chapter 5
    'mistakes': [
        ('This is the man which sold me the chair.', 'This is the man who sold me the chair.'),
        ('My clock, that is very old, still works.', 'My clock, which is very old, still works.'),
        ('The woman who her table I restored sent me a photo.', 'The woman whose table I restored sent me a photo.'),
        ('This is the market where I found it there.', 'This is the market where I found it.'),
    ],
    'quickfire': [
        {'situation': 'Point to one object near you and say who gave it to you. Use who or that.',
         'tips': ['This is the lamp that my sister gave me.',
                  'Defining: it tells you WHICH lamp. No commas.']},
        {'situation': 'Add an extra detail about your town, with commas.',
         'tips': ['My town, which has about forty thousand people, is very quiet.',
                  'Non-defining: commas, and never that.']},
        {'situation': 'Describe a person by something that belongs to them. Use whose.',
         'tips': ['She is the neighbor whose garden is full of roses.',
                  'Whose = his, her, their.']},
        {'situation': 'Tell me about a place where you love to buy old or used things.',
         'tips': ['There is a small antiques shop where I always find something interesting.',
                  'Where for places. Do not add there at the end.']},
        {'situation': 'You are at a flea market and the price is too high. Haggle politely.',
         'tips': ['It is lovely, but it is a bit more than I wanted to spend. Would you take thirty?',
                  'Callback from lesson 14: polite and tactful.']},
        {'situation': 'Tell me about something that has sentimental value for you.',
         'tips': ['My father&rsquo;s old watch, which does not work anymore, has a lot of sentimental value.',
                  'This one has no grammar target. Say the true thing.']},
    ],
    'speaking': [
        ('Is there an heirloom in your family? Who passed it down?',
         'Yes, a ring that my grandmother passed down to my mother. One day it will be mine.'),
        ('Have you ever found a diamond in the rough?',
         'Yes, an old door that my neighbor threw away. I cleaned it, and now it is the door of my studio.'),
        ('Do you like to haggle, or does it make you uncomfortable?',
         'At a market, yes. In a shop, never. It feels like a faux pas.'),
        ('What is one object you would never sell, at any price?',
         'The photo album that my mother made for me, which has every birthday until I was eighteen.'),
    ],
    'building': [
        ('this / be / the clock / my grandfather / buy / in 1952 (which one)',
         'This is the clock that my grandfather bought in 1952.'),
        ('my sewing machine / be / almost a hundred years old / still work (extra detail)',
         'My sewing machine, which is almost a hundred years old, still works.'),
        ('the woman / her table / I / restore / send me a photo',
         'The woman whose table I restored sent me a photo.'),
        ('Hamburg / Greta / live / have / a famous flea market (extra detail)',
         'Hamburg, where Greta lives, has a famous flea market.'),
    ],
    'answerkey_heading': 'Five Words and Two Commas in <span class="accent">Eight Lines</span>',
    'answerkey_title': 'Reveal the answer key',
    'answerkey': [
        '<strong>who</strong> for people: the man <strong>who</strong> sold me the chair.',
        '<strong>which</strong> for things: the desk, <strong>which</strong> was stuck for decades.',
        '<strong>that</strong> for people or things, but ONLY without commas: the clock <strong>that</strong> my grandfather bought.',
        '<strong>whose</strong> for possession: the woman <strong>whose</strong> table I restored.',
        '<strong>where</strong> for places: the market <strong>where</strong> I found it (no there at the end).',
        'No commas = defining: it tells you WHICH one.',
        'Commas = non-defining: one more detail. Never that. In speech, a small pause before and after.',
        'And the one that is not grammar: haggling is normal at a flea market in Hamburg or London, but in a shop it can be a faux pas.',
    ],
    'rp_chapter_heading': 'Objects With a Past, <span class="accent">Out Loud</span>',
    'roleplays': [
        {'heading': 'The Clock <span class="accent">on the Stall</span>',
         'scenario': 'You are at Harriet&rsquo;s stall at a market in London. Ask her about an old object: who it '
                     'belonged to, where it came from, and why they sold it. Then haggle politely.',
         'chips': ['Who did it belong to', 'the family that', 'Would you take']},
        {'heading': 'Greta&rsquo;s <span class="accent">Suitcase</span>',
         'scenario': 'Now you are talking to Greta, from Hamburg. She shows you a photo of the suitcase. Ask her two '
                     'questions about it, then tell her about an object in your life that has a story.',
         'chips': ['the woman whose', 'which was', 'where I found it']},
        {'heading': 'Two Minutes, <span class="accent">No Notes</span>',
         'scenario': 'Choose one object in your home that has a story. Tell me who had it before you, where it '
                     'came from, and why it matters to you.',
         'footer': 'No keywords, no notes, two minutes.'},
    ],
    'wrap_heading': 'Who Had It <span class="accent">Before You?</span>',
    'survival_heading': 'Five Phrases for <span class="accent">Old Things</span>',
    'survival': [
        'This is the clock that my grandfather bought.',
        'It belonged to a family who lived in Bath.',
        'My sewing machine, which is very old, still works.',
        'It has a lot of sentimental value.',
        'One man\'s trash is another man\'s treasure.',
    ],
    'checklist': [
        'I use who for people, which for things and where for places.',
        'I use whose for possession: the woman whose table I restored.',
        'I use commas for an extra detail, and never that between commas.',
        'I can tell the story of an object and who had it before me.',
        'I know the words: an heirloom, patina, sentimental value, to haggle, a diamond in the rough.',
    ],
    'badge': {
        'name': 'Storyteller of Objects',
        'text': 'Tonight you gave old things their biography, Ana &mdash; who made them, who kept them and where '
                'they have been.',
        'next': 'Small Talk &mdash; What&rsquo;s Safe to Ask Where',
    },

    # ------------------------------------------------------------ teacher
    'teacher': {
        'title': '<strong>Abertura (2 min):</strong> Sem saudacao scriptada (REGRA 27A). Va direto: &quot;Tonight, '
                 'the story behind old objects.&quot; Esta e a aula do lado &quot;fucador&quot; dela pelo OBJETO, '
                 'nao pela casa (a casa ja foi tema das aulas 3 e 7). Gramatica: relative clauses, defining e '
                 'non-defining.',
        'warmup': '<strong>Warm-up + callback (4 min):</strong> CALLBACK da aula 17: ELA diz uma regra de um lugar '
                  'com have to ou mustn&apos;t e usa uma palavra da aula passada (etiquette, mandatory, optional, a '
                  'faux pas, a rule of thumb, when in Rome). Responda de verdade. PONTE (REGRA 27B): &quot;Rules are '
                  'about places. Tonight, objects.&quot; e a pergunta do slide. ZERO correcao. Anote se ela diz '
                  '&quot;the thing what&quot; ou &quot;the man which&quot;.',
        'framing': '<strong>Enquadramento (3 min):</strong> Mostre os 3 passos e leia a nota: uma frase diz QUAL '
                   'relogio, a outra so acrescenta um detalhe. So plante a ideia das virgulas &mdash; a regra vem no '
                   'capitulo 4.',
        'hook': '<strong>Pergunta-gatilho (3 min):</strong> Deixe ela escolher um objeto e contar quem teve antes. '
                'NAO corrija. Anote 1-2 frases exatas: elas voltam corrigidas no capitulo 4 e no role-play 3.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: &quot;Twelve words for old things. Three of '
                       'them are expressions. Click each card.&quot;',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> CCQ an heirloom: &quot;Do you buy it in a shop? (Nao, '
                  'vem da familia.)&quot; CCQ vintage: &quot;Is it new? (Nao.) Is it bad quality? (Nao.)&quot; CCQ '
                  'second-hand: &quot;Did someone own it before? (Sim.)&quot; CCQ patina: &quot;Should you polish it '
                  'away? (Nao.)&quot; Peca um objeto da vida dela em cada card.',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> CCQ sentimental value: &quot;Does it come from money? '
                  '(Nao, de memorias.)&quot; CCQ to haggle: &quot;Do you accept the first price? (Nao.)&quot; CCQ a '
                  'diamond in the rough: &quot;Is it perfect now? (Nao.) Can it be? (Sim, com trabalho.)&quot; CCQ '
                  'one man&apos;s trash...: &quot;Is the object valuable for everybody? (Nao, para alguem.)&quot;',
        'matching': '<strong>Matching (3 min):</strong> Ana liga cada palavra a definicao em voz alta. Leia a nota: '
                    'AN heirloom, porque o h nao soa.',
        'pron': '<strong>Pronunciation drill (3 min):</strong> an AIR-loom (h mudo), CRAFTS-man-ship (forca no '
                'CRAFTS, o s e o m quase grudam), PA-ti-na (forca no PA; americano tambem aceita pa-TEE-na). Na '
                'frase: &quot;the clock that my grandfather bought&quot; sai sem pausa &mdash; o that quase some '
                '(/thet/). 2 repeticoes.',
        'gapfill': '<strong>Vocab in context (3 min):</strong> Ana diz a palavra ANTES de clicar. As candidatas '
                   'estao no banco, fora de ordem &mdash; ela ESCOLHE. Clicar de novo fecha (REGRA 27E).',
        'ch3_trans': '<strong>Transicao leitura (1 min):</strong> Diga: &quot;A short text about the lives of old '
                     'things, and then two people who found one.&quot;',
        'reading': '<strong>Leitura + gist (6 min):</strong> Primeira leitura RAPIDA (90 segundos) so para a ideia '
                   'central, depois o gist. Segunda leitura com calma. Pergunte: &quot;In your family, did old '
                   'furniture go to the street too?&quot; (O paragrafo 3 fala do Brasil.)',
        'tf': '<strong>True or False (4 min):</strong> Ana decide e JUSTIFICA com o texto antes de revelar. A 5a e a '
              'regra escondida no texto (virgulas = detalhe extra) &mdash; destaque, mas explique so no capitulo 4.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM A ANA ANTES de tocar '
                      '&mdash; elas ja estao visiveis. Sotaque ALEMAO: w soa quase v, o th vira s ou z, consoantes '
                      'finais duras (&quot;old&quot; vira quase &quot;olt&quot;). Toque 2 vezes. No fim: &quot;Would '
                      'you give the suitcase back?&quot;',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELA ANTES de tocar. Sotaque '
                      'BRITANICO: r final nao soa (&quot;drawer&quot; = /DROR/), t bem marcado. Toque 2 vezes. '
                      'Pergunte: &quot;Why did the lady not sell the desk?&quot;',
        'ch4_trans': '<strong>Transicao gramatica (1 min):</strong> Diga: &quot;Now the code. Five small words and '
                     'two commas.&quot;',
        'grammar': '<strong>Grammar discovery (8 min):</strong> Leia as 4 frases (toque o audio). Pergunte: &quot;In '
                   'which sentences do the colored words tell you WHICH one? Which one only adds a detail?&quot; '
                   'Espere ela achar que a frase 3 tem virgulas. So entao &quot;Reveal the Rule&quot;. CCQs: &quot;The '
                   'clock that my grandfather bought &mdash; do I have more than one clock? (Talvez, e por isso '
                   'digo qual.)&quot; &quot;My sewing machine, which is old &mdash; how many sewing machines? '
                   '(Uma.)&quot; &quot;Can I use that between commas? (Nunca.)&quot; Volte as frases anotadas no hook.',
        'practice': '<strong>Practice (4 min):</strong> Ana diz a palavra ORALMENTE antes de clicar. Itens 5 e 6 tem '
                    'virgulas: detalhe extra, nunca that.',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e a Harriet, dona de uma banca numa feira de Londres. '
                    'Clique &quot;Next Line&quot; e toque o audio. Nas falas da Ana, peca que ELA fale primeiro. '
                    'PRAGMATICA: pechinchar numa feira e normal no Reino Unido e na Alemanha, mas com educacao '
                    '(&quot;Would you take sixty?&quot;, nunca &quot;Sixty. Final.&quot;). Pergunte: &quot;In Brazil, '
                    'where do you haggle, and where would it be a faux pas?&quot;',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre a HARRIET e o relogio, nunca sobre '
                         'a Ana (REGRA 27F). Ana responde ANTES de revelar.',
        'artifact': '<strong>Artefato (5 min):</strong> Um anuncio de leilao online que ela esta acompanhando. Peca '
                    'que leia cada linha e diga em voz alta qual palavra relativa aparece (whose, where, which, '
                    'that). Depois as 3 perguntas &mdash; ela responde antes de revelar.',
        'ch5_trans': '<strong>Transicao pratica (1 min):</strong> Diga: &quot;Now we train. Errors, quick answers, '
                     'and your own objects.&quot;',
        'detective': '<strong>Detective (4 min):</strong> Ana corrige ANTES de clicar. Os 4 erros classicos: which '
                     'para pessoa, that entre virgulas, who her no lugar de whose, e o there repetido depois de '
                     'where.',
        'quickfire': '<strong>Quick Fire (6 min):</strong> UMA situacao por tela. Ana responde EM VOZ ALTA antes de '
                     'abrir as dicas. A 5a retoma a aula 14 (pedir com tato).',
        'speaking': '<strong>Speaking (5 min):</strong> Faca cada pergunta e espere a resposta COMPLETA. Exija pelo '
                    'menos uma frase com virgulas (which) e uma com whose. As respostas modelo sao sugestoes.',
        'building': '<strong>Sentence Building (4 min):</strong> Ana monta a frase completa em voz alta e clica para '
                    'comparar. Os itens 2 e 4 tem virgulas. Toggle (REGRA 27E).',
        'answerkey': '<strong>Answer key (2 min):</strong> Abra so no fim, para conferir. A linha 8 e a pragmatica: '
                     'onde pechinchar e normal e onde e gafe.',
        'ch6_trans': '<strong>Transicao role-play (1 min):</strong> Diga: &quot;From guided to free. Objects with a '
                     'past, three times.&quot;',
        'rp1': '<strong>Role-play Guided (4 min):</strong> Voce e a Harriet. Invente a historia do objeto quando ela '
               'perguntar. Deixe ela pechinchar e aceite na segunda tentativa se for educada. Corrija SO a palavra '
               'relativa (who / which / that / whose / where).',
        'rp2': '<strong>Role-play Semi-free (5 min):</strong> Voce e a Greta. Mostre a mala e conte em 3 frases. Ela '
               'faz duas perguntas e depois conta a historia de um objeto dela. Ensine &quot;the one that&quot; se '
               'ela precisar.',
        'rp3': '<strong>Free Practice (6 min):</strong> Dois minutos, sem interrupcao. NAO corrija durante. Conte '
               'quantas relative clauses ela usa e diga o numero no fim. Anote qualquer &quot;that&quot; entre '
               'virgulas para o feedback.',
        'ch7_trans': '<strong>Transicao wrap-up (1 min):</strong> Diga: &quot;Let us close. Five phrases to '
                     'keep.&quot;',
        'survival': '<strong>Survival card (3 min):</strong> Toque cada frase e peca que ela repita. Na frase 3, '
                    'marque a pausa das virgulas com a mao.',
        'checklist': '<strong>Checklist (2 min):</strong> Diga: &quot;Click each item if you feel confident.&quot; '
                     'Todos os 5 checks = aula completa e stamp no passaporte.',
        'badge': '<strong>Encerramento (2 min):</strong> Diga: &quot;Every object has a biography, and now you can '
                 'tell it.&quot; Homework (oralmente, opcional): uma foto de um objeto antigo da casa dela e um '
                 'audio de um minuto contando a historia dele com pelo menos 4 relative clauses. Proxima aula: Small '
                 'Talk &mdash; o que e seguro perguntar em cada cultura antes de uma conversa.',
    },

    # ------------------------------------------------------------ pre-class
    'pc': {
        'title': 'The Story Behind the Object -- Who, Which, That, Whose, Where',
        'desc': 'A suitcase from Hamburg, a desk with a letter from 1916 and a clock on a market stall: relative clauses to tell the story of old things.',
        'context_paras': [
            'Greta lives in Hamburg, <strong>where</strong> there is a big flea market every Sunday. Three years '
            'ago she found an old suitcase <strong>that</strong> was covered with hotel labels. Inside, there was a '
            'name, and she found the woman <strong>whose</strong> grandmother had owned it. It was '
            '<strong>an heirloom</strong>, and Greta gave it back.',
            'Tom restores furniture in York. One day he opened a desk drawer, <strong>which</strong> had been stuck '
            'for decades, and found a letter from a soldier <strong>who</strong> was writing to his mother in '
            '1916. The desk was not expensive, but now it has enormous <strong>sentimental value</strong>.',
            'Ana loves objects like these. For her, the <strong>patina</strong> on an old table is not a problem to '
            'fix. It is the story of the people <strong>who</strong> used it.',
        ],
        'context_quiz': [
            ('"She found the woman whose grandmother had owned it." Whose shows:',
             [('a place where something happened', False),
              ('possession &mdash; the woman&rsquo;s grandmother', True),
              ('a question', False)]),
            ('"He opened a desk drawer, which had been stuck for decades." The part between commas:',
             [('tells you which drawer, out of many drawers in the workshop', False),
              ('adds an extra detail', True),
              ('is a mistake', False)]),
            ('Why does Ana not want to remove the patina?',
             [('It is part of the story of the people who used the table.', True),
              ('Because it is difficult and expensive to remove from old furniture.', False),
              ('Because the table is new.', False)]),
        ],
        'tip_title': 'Relative Clauses',
        'tip_sub': 'Who, which, that, whose, where &mdash; and the two commas that change the meaning.',
        'tip_rows': [
            ('who / that', 'People', 'the man <strong>who</strong> sold me the chair'),
            ('which / that', 'Things', 'the clock <strong>that</strong> my grandfather bought'),
            ('whose', 'Possession', 'the woman <strong>whose</strong> table I restored'),
            ('where', 'Places', 'the market <strong>where</strong> I found it'),
            ('no commas', 'Defining: tells you WHICH one', 'The chair <strong>that I found</strong> is from 1940.'),
            ('commas', 'Non-defining: an extra detail, never that', 'My clock<strong>, which is old,</strong> still works.'),
        ],
        'tip_never': 'The man which sold me the chair &middot; my clock, that is old, still works &middot; the woman '
                     'who her table... &middot; the market where I found it there. Who for people, whose for '
                     'possession, and never that between commas.',
        'fills': [
            ('This is the man ', 'who', ' sold me the chair.',
             'one word -- for a person'),
            ('The woman ', 'whose', ' table I restored sent me a photo.',
             'one word -- possession: her table'),
            ('This is the flea market ', 'where', ' I found the mirror.',
             'one word -- for a place'),
            ('My sewing machine, ', 'which', ' is almost a hundred years old, still works.',
             'one word -- a thing, with commas, so not that'),
            ('This ring is ', 'an heirloom', '. It was my great-grandmother\'s.',
             'two words -- a valuable object kept by a family'),
            ('At a flea market, everybody ', 'haggles', ' a little.',
             'one word -- discusses the price to pay less'),
        ],
        'order_intro': 'Ana finds an old clock at Harriet&rsquo;s market stall. Put the conversation in order.',
        'order': [
            'Good morning! That clock you are looking at is my favorite thing on the stall.',
            'It is beautiful. Look at the patina on the wood. How old is it?',
            'About a hundred years. It belonged to a family who lived in Bath.',
            'Really? So why did they sell it?',
            'The grandson, who lives in Canada now, had no space for it.',
            'I understand. How much is it? Would you take sixty?',
        ],
        'quiz': [
            ('You want to tell a friend which chair you restored. You say:',
             [('"This is the chair, that I restored."', False),
              ('"This is the chair that I restored last summer."', True),
              ('"This is the chair who I restored."', False)]),
            ('You want to add an extra detail about your town. You say:',
             [('"My town, which is very quiet, has a lovely market."', True),
              ('"My town, that is very quiet, has a lovely market."', False),
              ('"My town which very quiet has a market."', False)]),
            ('At a flea market in Hamburg, the seller asks forty euros. You think it is too much. You say:',
             [('"Forty? That is a faux pas."', False),
              ('"It is lovely, but would you take thirty?"', True),
              ('"I will pay forty-five, because the patina is beautiful and I love it."', False)]),
            ('Your neighbor threw away an old door, and you made it beautiful. You say:',
             [('"It is worth its weight in gold, because the neighbor paid a lot."', False),
              ('"One man\'s trash is another man\'s treasure."', True),
              ('"It is an heirloom."', False)]),
        ],
        'think': 'Choose one old object in your home. Record its biography: who made it or owned it, where it '
                 'came from, how it came to you and why it matters. Use who, which, that, whose and where at least '
                 'once each, one sentence with commas, and one of tonight&rsquo;s expressions.',
    },

    'complementary': [
        {'slot': 'series', 'icon': 'film', 'type': 'Series',
         'title': 'The Repair Shop &mdash; Season 1, Episode 1 (full episode)',
         'desc': 'In a barn in the English countryside, a team of experts restores old objects that people love: a '
                 'clock, a chair, a toy. Every object comes with a family story, told in clear British English.',
         'tip': 'after each object, say one sentence with who and one with which: the man who brought the clock...',
         'url': 'https://www.youtube.com/watch?v=rsdyFVmp9lE', 'cta': 'Watch on YouTube'},
        {'slot': 'podcast', 'icon': 'podcast', 'type': 'Podcast',
         'title': 'A History of the World in 100 Objects &mdash; Swimming Reindeer',
         'desc': 'The director of the British Museum tells the story of a 13,000-year-old carving of two reindeer '
                 '&mdash; who made it, where it was found and what it tells us about the people who lived then.',
         'tip': 'listen for who, which and where. Write down three sentences that describe the object.',
         'url': 'https://podcasts.apple.com/us/podcast/swimming-reindeer/id351096296?i=1000080299652',
         'cta': 'Listen on Apple Podcasts'},
        {'slot': 'youtube', 'icon': 'video', 'type': 'Video',
         'title': 'How one Antiques Roadshow appraisal changed a family&rsquo;s life forever (PBS)',
         'desc': 'An American family brings an old object to the famous TV show and discovers that it is worth much '
                 'more than they ever imagined &mdash; in money and in history.',
         'tip': 'pause after the story and retell it with whose and which: the family whose...',
         'url': 'https://www.youtube.com/watch?v=AB3NvYFPKAk', 'cta': 'Watch on YouTube'},
    ],
}
