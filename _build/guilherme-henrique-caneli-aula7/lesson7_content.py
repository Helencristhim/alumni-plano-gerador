#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 7, em formato de prova (CPE)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula7 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)
VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]
VOCAB_CARDS_1 = VOCAB[:5]
VOCAB_CARDS_2 = VOCAB[5:10]

MATCH_OPTS = [
    'one question put to everybody in turn, sixty seconds each',
    'the person whose defined job is to write down what was said',
    'who may be quoted, and who may ask what, agreed in the first two minutes',
    'twenty people in a room small enough that silence is uncomfortable',
    'the single sentence the session was convened to produce',
    'the list built so the disagreements in the room appear on the floor',
]
MATCH_ROWS = [
    ('A lightning round', 'one question put to everybody in turn, sixty seconds each'),
    ('A rapporteur', 'the person whose defined job is to write down what was said'),
    ('Ground rules', 'who may be quoted, and who may ask what, agreed in the first two minutes'),
    ('A breakout session', 'twenty people in a room small enough that silence is uncomfortable'),
    ('A consensus statement', 'the single sentence the session was convened to produce'),
    ('A lineup', 'the list built so the disagreements in the room appear on the floor'),
]
COLLOC_BANK = ['set the ground rules', 'time-box an intervention', 'take a follow-up question',
               'run a lightning round', 'draft a consensus statement', 'wrap up on time']
COLLOC_OPTS = ['set', 'time-box', 'take', 'run', 'draft', 'wrap']
COLLOC_ROWS = [
    ('Two minutes at the start save an hour later: ____ .', 'set the ground rules'),
    ('Say the number out loud and the delegate keeps to it: ____ .', 'time-box an intervention'),
    ('Only the chair may ____ in this format.', 'take a follow-up question'),
    ('Sixty seconds each, everybody in turn: ____ .', 'run a lightning round'),
    ('Put it on the screen imperfect and let them fix it: ____ .', 'draft a consensus statement'),
    ('The discipline that separates a good chair from an enthusiastic one is to ____ .', 'wrap up on time'),
]
CLOZE_BANK = ['simultaneous interpretation', 'a speaking slot', 'a parting thought', 'a closing round',
              'a rapporteur', 'ground rules', 'a breakout session', 'a lineup']
CLOZE_ITEMS = [
    dict(before='1. Everything in the room slows by eight seconds once there is ', after='.',
         answer='simultaneous interpretation', hint='Two words, no article.'),
    dict(before='2. Say the number out loud and the delegate keeps to it: that is the point of ',
         after='.', answer='a speaking slot', alt='speaking slot', hint='Three words, with the article.'),
    dict(before='3. Pleasant, unanimous and entirely unwritable, ', after=' produces nothing.',
         answer='a closing round', alt='closing round', hint='Three words, with the article.'),
    dict(before='4. Who may be quoted and who may ask what belongs in ', after=', in the first two minutes.',
         answer='ground rules', hint='Two words, no article.'),
    dict(before='5. Twenty people in a room small enough for silence to be uncomfortable is ', after='.',
         answer='a breakout session', alt='breakout session', hint='Three words, with the article.'),
    dict(before='6. Writing down what was said is a defined job, and the person doing it is ', after='.',
         answer='a rapporteur', alt='rapporteur', hint='Two words, with the article.'),
    dict(before='7. Built so the disagreements already in the room appear on the floor, ',
         after=' is not a list of the most senior people available.',
         answer='a lineup', alt='lineup', hint='Two words, with the article.'),
]
CLOZE_NOT_NEEDED = 'a parting thought'

ARTICLE_TITLE = "The Eight-Second Delay"
ARTICLE_STANDFIRST = "Adapted from a comment essay on multilingual meetings &middot; ~600 words"
ARTICLE = [
    ("Nobody who has not worked in one quite believes how much a room changes once it is running with "
     "<b>simultaneous interpretation</b>. The words are the same. Everything else is different.", 1, ""),
    ("Begin with the obvious. A joke lands twice, which kills it. An interruption arrives on top of "
     "somebody else&rsquo;s sentence, because the interrupter has heard the end of a thought the rest of "
     "the room has not reached.", 2,
     " A chair who has not planned for this spends the session apologising for collisions that nobody "
     "actually caused."),
    ("The structural answers are dull and they work. <b>Ground rules</b> stated in the first two minutes "
     "&mdash; who may be quoted, whether <b>a follow-up question</b> comes from the floor or only from the "
     "chair, how long <b>a speaking slot</b> runs &mdash; save the hour that is otherwise spent "
     "negotiating them one intervention at a time. To <b>time-box</b> an intervention and say the number "
     "out loud is worth more than any appeal for brevity.", 3, ""),
    ("Format does the rest. <b>A breakout session</b> moves twenty people into a room small enough that "
     "silence becomes uncomfortable, which is the only reliable way of making the quiet ones speak. "
     "<b>A lightning round</b> puts one question to everybody in turn, sixty seconds each.", 4,
     " <b>A rapporteur</b> writes down what was said, and it is a defined job rather than a favour asked "
     "of the youngest person present."),
    ("What none of this solves is the ending. <b>A closing round</b> in which everybody offers "
     "<b>a parting thought</b> is pleasant and produces nothing that can be written down afterwards.", 5,
     " If the session was convened to produce <b>a consensus statement</b>, somebody has to put a draft "
     "sentence on the screen before people begin gathering their coats, and the chair has to "
     "<b>wrap up</b> by reading it aloud."),
    ("Composition matters more than content. <b>A lineup</b> is not a list of the most senior people "
     "available; it is a list built so that the disagreements already in the room are represented on the "
     "floor.", 6,
     " <b>A multilateral development bank</b> will send four people to a session like this, and either "
     "all four leave with the same sentence or none of them does."),
    ("None of which is a complaint about interpretation. The interpreters are usually the most competent "
     "people in the building, and the delay is not their doing; it is physics. What the delay removes is "
     "every technique that depends on speed, leaving only the ones that depend on structure. Chairs who "
     "are excellent in a monolingual room are frequently mediocre in this one, and the reverse is true "
     "rather more often than the circuit likes to admit.", None, ""),
]
GAP_OPTIONS = [
    ('A', 'A delegate who knows she has four minutes takes four; one who does not takes eleven.'),
    ('B', 'People will not write a sentence together; they will cheerfully correct one.'),
    ('C', 'The delay is about eight seconds, and eight seconds is long enough to redesign a '
          'conversation.'),
    ('D', 'Interpreters normally work in pairs and change over roughly every thirty minutes.'),
    ('E', 'Experienced delegates learn to leave a beat that feels absurd from the inside and reads as '
          'courtesy from the outside.'),
    ('F', 'If everybody at the table would answer the question the same way, the session has failed '
          'before it opens.'),
    ('G', 'It is the fastest instrument available for finding out where a room actually is, rather than '
          'where its loudest three members are.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "G"), ("5", "B"), ("6", "F")]
GAP_KEY = (
    "<b>1 C</b> &mdash; &ldquo;Everything else is different&rdquo; demands the specific difference, and "
    "the next paragraph is entirely about what eight seconds does.<br>"
    "<b>2 E</b> &mdash; collisions have just been described; E is the remedy, and &ldquo;A chair who has "
    "not planned for this&rdquo; follows from delegates who have.<br>"
    "<b>3 A</b> &mdash; &ldquo;say the number out loud&rdquo; is only justified by what knowing the number "
    "does to behaviour.<br>"
    "<b>4 G</b> &mdash; &ldquo;It&rdquo; can only be the lightning round, and the rapporteur sentence then "
    "moves on.<br>"
    "<b>5 B</b> &mdash; &ldquo;produces nothing that can be written down&rdquo; is answered by how people "
    "will and will not produce a sentence.<br>"
    "<b>6 F</b> &mdash; the lineup has just been defined by disagreement; F states the failure case.<br>"
    "<b>D</b> is the distractor: true, on topic, and it answers no reference."
)
MCQ = [
    ("What does the writer say is the effect of the delay on a joke?", [
        ("It becomes harder for the interpreter to convey.", False),
        ("It arrives twice, which destroys it.", True),
        ("It is usually left out altogether.", False),
        ("It works better than in a monolingual room.", False)]),
    ("Why do interruptions collide in an interpreted room?", [
        ("Delegates are less disciplined than in other formats.", False),
        ("The interrupter has heard an ending the rest of the room has not reached.", True),
        ("The microphones are shared between several speakers.", False),
        ("Chairs allow too many interventions at once.", False)]),
    ("What does the writer say is worth more than appealing for brevity?", [
        ("Cutting the number of speakers.", False),
        ("Naming the time limit out loud.", True),
        ("Taking follow-up questions only from the chair.", False),
        ("Moving the discussion into breakout rooms.", False)]),
    ("Why does a breakout session make quiet delegates speak?", [
        ("They are given a specific question to answer.", False),
        ("The room is small enough for silence to become uncomfortable.", True),
        ("The session is not being interpreted.", False),
        ("The rapporteur is not present.", False)]),
    ("According to the fifth paragraph, why must a draft sentence go up early?", [
        ("The rapporteur needs it for the record.", False),
        ("People will correct a sentence but will not compose one together.", True),
        ("The closing round runs over time otherwise.", False),
        ("Delegates need to approve it before they leave.", False)]),
    ("In the final paragraph, the writer&rsquo;s point about chairs is that", [
        ("interpretation makes the chair&rsquo;s job easier.", False),
        ("skill in one kind of room does not transfer to the other.", True),
        ("multilingual sessions should be chaired by interpreters.", False),
        ("the best chairs avoid interpreted sessions.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 b</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br><i>Item 6 is the one to argue about: (d) is a reasonable inference and the text does "
    "not make it. Part 5 rewards what is on the page.</i>"
)
WORD_FORMATION = [
    dict(before="An ", after=" in this format lands on somebody else&rsquo;s sentence. (INTERRUPT)",
         answer="interruption", hint="Noun from the verb."),
    dict(before="Appeals for ", after=" achieve nothing; a stated number achieves everything. (BRIEF)",
         answer="brevity", hint="Abstract noun from the adjective."),
    dict(before="Nobody doubts the ", after=" of the interpreters. (COMPETENT)",
         answer="competence", hint="Abstract noun from the adjective."),
    dict(before="A ", after=" closing round is the commonest way to waste ten minutes. (LENGTH)",
         answer="lengthy", hint="Adjective from the noun."),
    dict(before="The answers are ", after=" rather than rhetorical. (STRUCTURE)",
         answer="structural", hint="Adjective from the noun."),
    dict(before="Wider ", after=" is not the same thing as a longer speaking list. (PARTICIPATE)",
         answer="participation", hint="Noun from the verb."),
    dict(before="The room has to be small enough for ", after=" to be uncomfortable. (SILENT)",
         answer="silence", hint="Noun from the adjective."),
    dict(before="", after=", the quiet ones speak once the room is small enough. (RELY)",
         answer="Reliably", hint="Adverb, capital letter, comma after it."),
]
TRANSFORMATIONS = [
    dict(lead="The chair carried a folder that was old, black and made of leather.", key="LEATHER",
         before="The chair carried ", after=" folder.",
         answer="an old black leather", hint="Age, then colour, then material."),
    dict(lead="They met in a building that was beautiful, Italian and nineteenth-century.", key="ITALIAN",
         before="They met in ", after=" building.",
         answer="a beautiful nineteenth-century Italian",
         hint="Opinion, then age, then origin."),
    dict(lead="The table was large, round and made of glass.", key="GLASS",
         before="It was ", after=" table.",
         answer="a large round glass", hint="Size, then shape, then material."),
    dict(lead="The final session was long and held in plenary.", key="PLENARY",
         before="It was ", after=" session.",
         answer="a long final plenary", hint="Size, then order, then classifier."),
    dict(lead="Two interpreters worked in the booth; they were young and French.", key="FRENCH",
         before="The booth held ", after=" interpreters.",
         answer="two young French", hint="Number, then age, then origin."),
    dict(lead="The lectern was narrow, grey and made of steel.", key="STEEL",
         before="She spoke from ", after=" lectern.",
         answer="a narrow grey steel", hint="Size, then colour, then material."),
]
TRANSFORM_KEY = (
    "<b>1</b> an old black leather<br><b>2</b> a beautiful nineteenth-century Italian<br>"
    "<b>3</b> a large round glass<br><b>4</b> a long final plenary<br><b>5</b> two young French<br>"
    "<b>6</b> a narrow grey steel<br><i>Every one of these follows the same order, and the order is not "
    "negotiable: opinion, size, age, shape, colour, origin, material, purpose. Item 4 is the one that "
    "feels wrong and is not: <i>final</i> is ordering, and ordering sits with age.</i>"
)
TALK_FILE = "a7_cpe_talk_the_room_you_cannot_hear.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "I have interpreted for about twenty-two years, mostly in these infrastructure and finance sessions, "
    "and I want to tell you what I can hear that the room cannot. "
    "First, I can hear who has not decided what they think. When somebody knows their point, the sentence "
    "arrives whole and I can stay eight seconds behind comfortably. When they are working it out while "
    "speaking, the sentence turns twice in the middle, and I have to wait, and then I am fourteen seconds "
    "behind, and the room feels that as hesitation from me. It is not. "
    "Second, the jokes. Please stop. I am not being humourless. A joke depends on the last word arriving "
    "at a particular moment, and in my channel it arrives later, so half the room laughs, then the other "
    "half laughs, and the speaker thinks they have died. They have not. The structure has. "
    "Third, and this is the useful one. Short sentences are not simpler. They are more precise, because a "
    "long sentence in English with three subordinate clauses has to be reordered entirely in Portuguese "
    "or in German, and the reordering is where meaning gets lost. If you give me short sentences I give "
    "the room your meaning. If you give me architecture I give the room my best guess. "
    "And the last thing. Say the numbers slowly and say them twice. Everything else I can recover. A "
    "number I cannot."
)
TALK_ITEMS = [
    dict(before="1. The speaker has interpreted for about ", after=" years.",
         answer="twenty-two", alt="22", hint="Written as one hyphenated word."),
    dict(before="2. When a speaker knows their point, the sentence arrives ", after=".",
         answer="whole", hint="One word."),
    dict(before="3. When a speaker is still deciding, the sentence turns ", after=" in the middle.",
         answer="twice", hint="One word."),
    dict(before="4. The room reads the extra delay as ", after=" from the interpreter.",
         answer="hesitation", hint="One word."),
    dict(before="5. A joke depends on the last word arriving at a particular ", after=".",
         answer="moment", hint="One word."),
    dict(before="6. She says short sentences are not simpler but more ", after=".",
         answer="precise", hint="One word."),
    dict(before="7. A long English sentence with three subordinate clauses has to be ",
         after=" entirely in another language.", answer="reordered", hint="One word."),
    dict(before="8. Everything else she can recover, but not ", after=".",
         answer="a number", alt="numbers", hint="Two words, with the article."),
]
SPEAKERS = [
    dict(n=1, file="a7_cpe_mm_speaker_1.mp3", voice="alice", task1="E", task2="C", text=(
        "The thing I got wrong for years was the lineup. I picked the four most senior people who would "
        "say yes, and the session was polite and useless. Now I pick for disagreement. Two of them have to "
        "be people who would not have lunch together. It is more uncomfortable to organise and it is the "
        "only thing that has ever worked.")),
    dict(n=2, file="a7_cpe_mm_speaker_2.mp3", voice="arthur", task1="A", task2="F", text=(
        "I am in the booth, so I hear everything twice, once in the original and once as I say it. What I "
        "would ask of every speaker is short sentences and slow numbers. People believe that speaking "
        "beautifully helps me. It does not. A complicated sentence in English has to be taken apart and "
        "rebuilt, and that is where things go missing.")),
    dict(n=3, file="a7_cpe_mm_speaker_3.mp3", voice="matilda", task1="C", task2="A", text=(
        "By the time it reaches me, everyone believes something has been agreed, and my job is to find out "
        "what. Usually four people have four different sentences in their heads. So I stopped writing "
        "afterwards and started writing during, on the screen, wrong on purpose. Somebody always corrects "
        "it within ten seconds, and that is the agreement.")),
    dict(n=4, file="a7_cpe_mm_speaker_4.mp3", voice="george", task1="D", task2="H", text=(
        "We send four people to these and I used to think that was three too many. Then I looked at what "
        "came back. Four different summaries, four different action points, and nothing in the system a "
        "month later. Now they are not allowed to travel unless they agree, in the taxi, on one sentence "
        "they will all repeat.")),
    dict(n=5, file="a7_cpe_mm_speaker_5.mp3", voice="antonio", task1="B", task2="E", text=(
        "I have sat through hundreds of these as a delegate and I will say the unpopular thing. The "
        "breakout sessions are the only part that works. The plenary is theatre with better lighting. In a "
        "room of twenty I have said things I would never say into a microphone, and so has everybody "
        "else.")),
]
TASK1_OPTS = [
    ("A", "a conference interpreter"),
    ("B", "a delegate who attends frequently"),
    ("C", "a rapporteur"),
    ("D", "a manager at a development bank"),
    ("E", "a conference producer"),
    ("F", "a venue technician"),
    ("G", "a chair of plenary sessions"),
    ("H", "a journalist covering the event"),
]
TASK2_OPTS = [
    ("A", "Agreement has to be drafted during the session, not written up afterwards."),
    ("B", "Sessions should be shorter and have fewer speakers."),
    ("C", "A lineup should be built around disagreement rather than seniority."),
    ("D", "Interpreters should be given the speeches in advance."),
    ("E", "The small-group format produces what the main room cannot."),
    ("F", "Elaborate sentences lose meaning in translation; short ones do not."),
    ("G", "Delegates rarely read the rapporteur&rsquo;s notes afterwards."),
    ("H", "Sending several people is worthless unless they leave with one sentence."),
]
GRAMMAR_QUIZ = [
    ("&ldquo;a <b>large round glass</b> table&rdquo;. Which order would a native speaker reject?", [
        ("a round large glass table", True),
        ("a large round glass table", False),
        ("a large glass round table", False),
        ("both (a) and (c)", False)]),
    ("In &ldquo;a long <b>final</b> plenary session&rdquo;, <i>final</i> occupies the slot normally taken "
     "by", [
         ("opinion.", False), ("age or ordering.", True), ("origin.", False), ("purpose.", False)]),
    ("Why does &ldquo;a <b>Brazilian young</b> delegate&rdquo; sound wrong to a native ear?", [
         ("Nationality adjectives cannot precede a noun directly.", False),
         ("Origin comes after age, not before it.", True),
         ("Two adjectives require a comma between them.", False),
         ("&ldquo;Young&rdquo; must follow the verb.", False)]),
    ("Which of these is the order a native speaker produces without thinking?", [
         ("a steel narrow grey lectern", False),
         ("a narrow grey steel lectern", True),
         ("a grey narrow steel lectern", False),
         ("a narrow steel grey lectern", False)]),
    ("Adjective order matters in executive writing mainly because", [
         ("it is tested in international examinations.", False),
         ("the wrong order makes a fluent speaker sound non-native in one word.", True),
         ("it changes the meaning of the noun phrase.", False),
         ("style guides in this sector require it.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="They met around ", after=" table in the basement.",
         answer="a large round glass", hint="Size, shape, material."),
    dict(before="The bank sent ", after=" delegation to the forum.",
         answer="a small senior technical", alt="a small senior technical",
         hint="Size, then opinion-adjacent rank, then classifier."),
    dict(before="She was ", after=" interpreter in the booth that morning.",
         answer="the only young Portuguese", alt="the only young Brazilian",
         hint="Determiner-adjacent, then age, then origin."),
    dict(before="He read from ", after=" note the rapporteur had passed him.",
         answer="a short handwritten yellow", alt="a short yellow handwritten",
         hint="Size, then two that argue with each other: say both aloud and choose."),
]
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> You are closing a session of sixty people in "
    "three languages. Answer this: <i>&ldquo;What did this room actually agree?&rdquo;</i> Give the "
    "sentence first, then the evidence. Short sentences, slow numbers, and at least three complex noun "
    "phrases with two or more adjectives in front of the noun."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "Say your consensus sentence again, slowly enough to be interpreted.",
    "You used two adjectives before a noun. Say that phrase again and tell me why that order.",
    "Somebody in the room says you have overstated the agreement. Concede, then hold.",
    "One sentence: who in this room would have written it differently, and how?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe reiniciar. A pergunta 1 e o teste de interpretacao: se ele nao consegue "
    "repetir devagar sem mudar a frase, a frase nao estava pronta. A 2 e a da gramatica, e ele tem de "
    "NOMEAR a ordem, nao so acertar."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> You are co-chairing a closed session of sixty people "
    "in three languages, and you have ten minutes left. Together, decide: the one sentence you will put on "
    "the screen, who reads it aloud, and what you will do if two delegates object. You have to agree on "
    "the sentence."
)
DEBATE_1_MOTION = (
    "This house believes that the plenary session should be abolished and replaced entirely by breakout "
    "groups."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you open with the strongest argument against yourself.",
    "Short sentences only. If a sentence could not be interpreted live, it does not count.",
]
DEBATE_2_MOTION = (
    "This house believes that a chair should choose a lineup for disagreement even when the sponsors want "
    "seniority."
)
DEBATE_2_RULES = [
    "The teacher gives you the side. You do not choose it.",
    "Before you answer, restate the strongest point the other side has made, in your own words, so that "
    "they accept your version of it.",
    "Only then do you respond. A turn that skips the concession does not count.",
]
DEBATE_2_TEACHER = (
    "Segundo debate (6 min): DE o lado a ele. O que se mede e CONCESSAO: ele tem de reformular o ponto "
    "mais forte do outro lado a ponto de voce aceitar a reformulacao. Se reformula uma versao fraca, e "
    "straw man, e a rodada nao conta."
)
WRITING_TASK = (
    "<b>Paper 2, Part 2 &mdash; a report, 280 to 320 words, for the next lesson.</b> You chaired a closed "
    "session of sixty people last week. Write the report your organisation will circulate: the sentence "
    "the room agreed, the two positions that did not converge, and what you would change about the format "
    "next time. Assume the reader was not there and will not read a second page."
)
WRITING_MODEL = (
    "Three things are being read for. The agreed sentence, quoted exactly and early. An honest account of "
    "what did NOT converge, named rather than softened. And one concrete change to the format, not to the "
    "people. A report that says the discussion was rich and wide-ranging has told the reader nothing they "
    "could act on."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura. Se ele pedir mais, devolva a "
    "pergunta: 'what would somebody DO differently at the next session?'."
)
ROLEPLAY_SCENARIO = (
    "Your teacher is a delegate who has just arrived from another session and missed the first hour. You "
    "have two minutes, in a corridor, to tell her what the room agreed and where it split. She will "
    "interrupt if she loses the thread."
)
ROLEPLAY_CHIPS = ['a consensus statement', 'a breakout session', 'a lightning round', 'to wrap up',
                  'a short handwritten note', 'the senior technical delegation']
ROLEPLAY_TEACHER = (
    "Role-play guiado (4 min): voce e a delegada atrasada, e interrompe assim que perder o fio -- e o "
    "substituto do interprete, que nao existe aqui. Cronometre os dois minutos. Degrau GUIADO, com chips "
    "na tela; o long turn a seguir e o mesmo conteudo sem apoio nenhum."
)
