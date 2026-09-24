#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 5, em formato de prova (CPE).

Mesmas duas travas das aulas 3 e 4: nada aqui pode aparecer na PRE-CLASS desta
aula, e o lexico e o grammar_point sao do specs/aula5.py, que continua sendo o
dono deles.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula5 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)
VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]
VOCAB_CARDS_1 = VOCAB[:5]
VOCAB_CARDS_2 = VOCAB[5:10]

MATCH_OPTS = [
    'answering a weaker version of the question than the one you were asked',
    'the qualification that eats the sentence it was attached to',
    'accepting the subject and changing the terms',
    'the answer that fits no question in the room',
    'the number or name you have decided in advance not to give',
    'putting an argument on the table without owning it',
]
MATCH_ROWS = [
    ('A straw man', 'answering a weaker version of the question than the one you were asked'),
    ('A caveat', 'the qualification that eats the sentence it was attached to'),
    ('To reframe', 'accepting the subject and changing the terms'),
    ('A non-answer', 'the answer that fits no question in the room'),
    ('A red line', 'the number or name you have decided in advance not to give'),
    ("To play devil's advocate", 'putting an argument on the table without owning it'),
]

COLLOC_BANK = ['push back on a premise', 'concede a point early', 'find common ground',
               'steer the discussion', 'take the heat out of it', 'sidestep a question openly']
COLLOC_OPTS = ['push', 'concede', 'find', 'steer', 'heat', 'sidestep']
COLLOC_ROWS = [
    ('You do not have to accept the question as asked: you can ____ .', 'push back on a premise'),
    ('It costs almost nothing to ____ and buys the right to hold the rest.', 'concede a point early'),
    ('Look for it before you need it, not when the room turns: ____ .', 'find common ground'),
    ('A good chair will ____ without anybody noticing.', 'steer the discussion'),
    ('Slow down when everyone speeds up, and you ____ .', 'take the heat out of it'),
    ('Say what you will not discuss and why, and you ____ .', 'sidestep a question openly'),
]

CLOZE_BANK = ['a talking point', 'a non-answer', 'a straw man', 'a caveat', 'a red line',
              'common ground', 'to reframe', 'to rein in']
CLOZE_ITEMS = [
    dict(before='1. A rehearsed sentence that does not fit the question becomes ', after='.',
         answer='a non-answer', alt='non-answer', hint='Three words, with the article.'),
    dict(before='2. Answering a weaker version of what you were asked is ', after='.',
         answer='a straw man', alt='straw man', hint='Three words, with the article.'),
    dict(before='3. The number you decided in advance not to give is ', after='.',
         answer='a red line', alt='red line', hint='Three words, with the article.'),
    dict(before='4. A qualification long enough to swallow the claim it was hung on is ', after='.',
         answer='a caveat', alt='caveat', hint='Two words, with the article.'),
    dict(before='5. Accepting the subject and changing the terms is ', after='.',
         answer='to reframe', alt='reframe', hint='Two words, with the infinitive marker.'),
    dict(before='6. When the temperature rises, you ', after=' the argument, not the person.',
         answer='rein in', hint='Two words, a phrasal verb.'),
    dict(before='7. What you look for before you need it, not when the room turns, is ', after='.',
         answer='common ground', hint='Two words, no article.'),
]
CLOZE_NOT_NEEDED = 'a talking point'

ARTICLE_TITLE = "What a Hostile Room Is Actually Testing"
ARTICLE_STANDFIRST = "Adapted from a comment essay on public hearings &middot; ~600 words"
ARTICLE = [
    ("A public hearing is not a conversation, and it is a mistake to prepare for one as though it were. "
     "The questioner holds the floor, the clock and the last word; the person answering holds none of the "
     "three.", 1, " What is being tested is not knowledge."),

    ("Most preparation goes into <b>a talking point</b>, which is the least useful instrument in the room. "
     "A rehearsed sentence is audible as a rehearsed sentence, and if it does not fit the question it "
     "becomes <b>a non-answer</b>, which is the one failure a hearing never forgives.", 2, ""),

    ("The moves that work are unglamorous. To <b>sidestep a question</b> in the open, saying what you will "
     "not discuss and why, costs far less than pretending. To <b>concede a point</b> early buys the right "
     "to hold everything else. To <b>reframe</b> is to accept the subject and change the terms.", 3,
     " To <b>push back</b> is to disagree on the record, and a room that came for a fight will sometimes "
     "respect that more than it respects agreement."),

    ("There are two reliable traps. The first is <b>a straw man</b>: answering a weaker version of the "
     "question than the one that was asked.", 4,
     " The second is the unattached <b>caveat</b>, the qualification that eats the sentence it was hung "
     "on, until nobody in the room could state what was actually claimed."),

    ("What separates the people who survive these rooms is preparation of a different kind. They decide in "
     "advance where <b>a red line</b> really sits &mdash; which numbers, which names &mdash; and then they "
     "give everything else away freely.", 5,
     " They look for <b>common ground</b> before they need it, and they <b>steer the discussion</b> "
     "without appearing to."),

    ("The last skill is temperature. When an exchange heats up the instinct is to match it. The people who "
     "do this well <b>rein in</b> the argument rather than the person, slow down when everybody else "
     "speeds up, and <b>take the heat out of</b> the room without conceding the point.", 6,
     " Playing <b>devil&rsquo;s advocate</b> remains available, but once only, and never twice in the same "
     "hearing."),

    ("None of this is about winning. A hearing is not won. It is survived well enough that the question "
     "stops being about the person answering and goes back to being about the thing they were asked to "
     "explain, which is the only outcome worth preparing for.", None, ""),
]
GAP_OPTIONS = [
    ('A', 'None of these is evasion, provided the speaker says openly which one is being used.'),
    ('B', 'That is why they sound open rather than defensive: they are protecting three things, not '
          'everything.'),
    ('C', 'Everything that follows from that asymmetry is a question of what you do with forty seconds you '
          'did not choose.'),
    ('D', 'Most hearings are now broadcast in full, and the recordings remain available long afterwards.'),
    ('E', 'A room will forgive an admission, a refusal, even a flash of temper; what it will not forgive '
          'is the sound of somebody answering a different question.'),
    ('F', 'Volume is the cheapest signal in the room, and the only one that can be answered simply by '
          'turning it up.'),
    ('G', 'Everybody notices, beginning with the person who asked, and the credit lost is never recovered '
          'in that session.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "G"), ("5", "B"), ("6", "F")]
GAP_KEY = (
    "<b>1 C</b> &mdash; &ldquo;that asymmetry&rdquo; points back to the three things the questioner holds; "
    "&ldquo;forty seconds&rdquo; sets up &ldquo;not knowledge&rdquo;.<br>"
    "<b>2 E</b> &mdash; &ldquo;the one failure a hearing never forgives&rdquo; demands the list of what it "
    "DOES forgive.<br>"
    "<b>3 A</b> &mdash; three moves have just been named; &ldquo;None of these&rdquo; needs all three "
    "immediately before it.<br>"
    "<b>4 G</b> &mdash; &ldquo;Everybody notices&rdquo; can only follow the trap being described, and "
    "&ldquo;The second is&rdquo; then continues the pair.<br>"
    "<b>5 B</b> &mdash; &ldquo;give everything else away freely&rdquo; is explained by &ldquo;protecting "
    "three things, not everything&rdquo;.<br>"
    "<b>6 F</b> &mdash; &ldquo;slow down when everybody speeds up&rdquo; needs the sentence about volume "
    "before the devil&rsquo;s advocate line closes the paragraph.<br>"
    "<b>D</b> is the distractor: true, on topic, answers no reference and completes no argument."
)
MCQ = [
    ("The writer opens by listing what the questioner holds in order to", [
        ("explain why hearings take so long.", False),
        ("establish that the exchange is not symmetrical, and that preparation must reflect that.", True),
        ("criticise the way hearings are conducted.", False),
        ("argue that the person answering should refuse to attend.", False)]),
    ("Why is a talking point described as the least useful instrument?", [
        ("It takes too long to deliver under pressure.", False),
        ("It is audible as rehearsed, and useless if it does not fit the question.", True),
        ("It commits the speaker to a position they cannot leave.", False),
        ("It is usually written by somebody else.", False)]),
    ("What condition does the writer attach to the moves in the third paragraph?", [
        ("That they are used no more than once each.", False),
        ("That the speaker says openly which one is being used.", True),
        ("That they are agreed with the questioner in advance.", False),
        ("That they are used only when the question is unfair.", False)]),
    ("What does the writer say is lost when a speaker uses a straw man?", [
        ("The chance to answer the real question later.", False),
        ("Credit with the room, and it is not recovered in that session.", True),
        ("The support of the person who asked.", False),
        ("Control of the time remaining.", False)]),
    ("According to the fifth paragraph, why do the survivors sound open?", [
        ("They have rehearsed a response to every likely line of attack.", False),
        ("They are protecting three things rather than everything.", True),
        ("They agree with the questioner wherever possible.", False),
        ("They prepare more thoroughly than the others.", False)]),
    ("In the final paragraph, the writer&rsquo;s definition of a good outcome is that", [
        ("the speaker leaves with their reputation improved.", False),
        ("attention returns from the person to the subject they were asked about.", True),
        ("the questioner concedes the point.", False),
        ("the hearing finishes ahead of time.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 b</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br><i>Item 4: (a) and (d) are both plausible consequences and neither is in the text. "
    "Part 5 rewards reading the sentence, not the situation.</i>"
)

# ── USE OF ENGLISH ───────────────────────────────────────────────────────────
# Raizes diferentes das da pre-class (EVADE, REFUSE, EASY, PREDICT, MEANING,
# HANDLE, WISE).
WORD_FORMATION = [
    dict(before="The ", after=" of the room was obvious before the first question. (HOSTILE)",
         answer="hostility", hint="Abstract noun from the adjective."),
    dict(before="A plain ", after=" costs less than an hour of deflection. (ADMIT)",
         answer="admission", hint="Noun from the verb. Watch the internal change."),
    dict(before="What she was protecting was not the number but her ", after=". (CREDIBLE)",
         answer="credibility", hint="Abstract noun from the adjective."),
    dict(before="No amount of ", after=" removes the asymmetry of a hearing. (PREPARE)",
         answer="preparation", hint="Noun from the verb."),
    dict(before="He sounded ", after=" from the second question onwards. (DEFEND)",
         answer="defensive", hint="Adjective from DEFEND. Watch the internal change."),
    dict(before="The credit lost in that exchange was never ", after=". (RECOVER)",
         answer="recovered", hint="Past participle of the verb."),
    dict(before="An early ", after=" buys the right to hold everything else. (CONCEDE)",
         answer="concession", hint="Noun from the verb."),
    dict(before="", after=", everyone in the room raises their voice at the same moment. (INSTINCT)",
         answer="Instinctively", hint="Adverb, capital letter, comma after it."),
]
# Palavras-chave DIFERENTES das da pre-class (HAD, SHOULD, WERE, POSITION,
# QUITE, BEEN), na mesma gramatica: condicional invertida e parafrase diplomatica.
TRANSFORMATIONS = [
    dict(lead="If anyone needs the detail, it is in the annexe.", key="REQUIRE",
         before="", after=" it is in the annexe.",
         answer="Should anyone require the detail,",
         hint="First conditional without &ldquo;if&rdquo;: Should + subject + bare infinitive."),
    dict(lead="If the committee had asked earlier, we would have published it.", key="ASKED",
         before="", after=" we would have published it.",
         answer="Had the committee asked earlier,",
         hint="Third conditional without &ldquo;if&rdquo;: invert HAD and the subject."),
    dict(lead="If it were not for the confidentiality undertaking, I would tell you.", key="NOT",
         before="Were it ", after=" I would tell you.",
         answer="not for the confidentiality undertaking,",
         hint="Inverted form of &ldquo;if it were not for&rdquo;."),
    dict(lead="I disagree with that characterisation.", key="PUT",
         before="That is not how I ", after=" myself.",
         answer="would put it", alt="would have put it",
         hint="Diplomatic paraphrase: disagree without the word disagree."),
    dict(lead="I cannot answer that today.", key="STAGE",
         before="I am ", after=".",
         answer="not able to answer that at this stage",
         alt="not in a position to answer that at this stage",
         hint="Soften a refusal by putting a limit of TIME on it."),
    dict(lead="You are simplifying what I said.", key="FAIR",
         before="I am ", after=" what I said.",
         answer="not sure that is entirely fair to", alt="not sure that is quite fair to",
         hint="Push back on the premise without accusing anybody."),
]
TRANSFORM_KEY = (
    "<b>1</b> Should anyone require the detail,<br><b>2</b> Had the committee asked earlier,<br>"
    "<b>3</b> not for the confidentiality undertaking,<br><b>4</b> would put it &middot; would have put it"
    "<br><b>5</b> not able to answer that at this stage &middot; not in a position to ...<br>"
    "<b>6</b> not sure that is entirely fair to &middot; not sure that is quite fair to<br>"
    "<i>Items 4 to 6 are not grammar drills. They are the sentences that keep a room from hardening, and "
    "all three work by putting a limit on the refusal rather than on the questioner.</i>"
)

# ── LISTENING ────────────────────────────────────────────────────────────────
TALK_FILE = "a5_cpe_talk_forty_seconds.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "I clerked committees for twelve years, which means I watched roughly two thousand people answer "
    "questions they did not want. Let me tell you what actually separates them. "
    "It is not knowledge. The witnesses who come apart usually know more than the members questioning "
    "them. It is not confidence either, and I would go further: the confident ones are often the worst, "
    "because they treat the hearing as a debate they can win. You cannot win it. The member has the floor, "
    "the clock and the last word, and any attempt to take those back reads as arrogance. "
    "What separates them is preparation of a specific kind, and it is very boring. Before the hearing, the "
    "good ones write down the three things they will not say. Three. Not a briefing folder. Three specific "
    "numbers or names. Everything outside those three they then give away without hesitating, and that is "
    "why they sound open while protecting more effectively than the person who guards everything. "
    "The second thing is the pause. Everyone speeds up under pressure. The witness who takes one full "
    "beat before answering reads as somebody thinking. From the inside that pause feels like a collapse. "
    "From the outside it is the most credible thing in the room. "
    "And the third, which almost nobody does. Say which move you are making. I am not going to give you "
    "that figure, and here is why. That sentence, said plainly, has ended more difficult exchanges than "
    "any clever answer I have heard in twelve years. The members are not trying to trap you. They are "
    "trying to find out whether you are straight with them."
)
TALK_ITEMS = [
    dict(before="1. The speaker clerked committees for ", after=" years.",
         answer="twelve", hint="One word, and he repeats it at the end."),
    dict(before="2. The witnesses who come apart usually know more than the ", after=".",
         answer="members", alt="members questioning them", hint="One word."),
    dict(before="3. The confident ones treat the hearing as a debate they can ", after=".",
         answer="win", hint="One word."),
    dict(before="4. Before the hearing, the good ones write down the three things they ", after=".",
         answer="will not say", hint="Three words."),
    dict(before="5. Everything outside those three they give away without ", after=".",
         answer="hesitating", hint="One word, an -ing form."),
    dict(before="6. The witness who takes one full beat reads as somebody ", after=".",
         answer="thinking", hint="One word."),
    dict(before="7. From the inside, that pause feels like a ", after=".",
         answer="collapse", hint="One word."),
    dict(before="8. The members are trying to find out whether you are ", after=" with them.",
         answer="straight", hint="One word, and it is the last line of the talk."),
]
SPEAKERS = [
    dict(n=1, file="a5_cpe_mm_speaker_1.mp3", voice="alice", task1="D", task2="C", text=(
        "I have given evidence four times now and the first one was a disaster. I had a folder with an "
        "answer for everything, and the moment a question came that was not in the folder I could hear "
        "myself reaching for the nearest thing that was. Now I take one sheet of paper with three lines on "
        "it and I am a great deal better.")),
    dict(n=2, file="a5_cpe_mm_speaker_2.mp3", voice="arthur", task1="A", task2="E", text=(
        "People think we are trying to catch witnesses out. Honestly, most of us have neither the time nor "
        "the appetite. What I am doing with my six minutes is finding out whether the answers hold "
        "together, and a witness who tells me plainly that they will not answer something goes up in my "
        "estimation, not down.")),
    dict(n=3, file="a5_cpe_mm_speaker_3.mp3", voice="matilda", task1="C", task2="A", text=(
        "The single change that improves a client most is not a phrase. It is the silence before they "
        "speak. I make them count one beat, out loud, in rehearsal, until it stops feeling like failure. "
        "Everything else we do together, the bridging, the reframing, is worth perhaps a tenth of that one "
        "beat.")),
    dict(n=4, file="a5_cpe_mm_speaker_4.mp3", voice="george", task1="B", task2="H", text=(
        "I sit in the press seats and I will tell you what actually gets written up. Not the toughest "
        "question. The moment the witness stops sounding like a person and starts sounding like a "
        "document. That is the clip. Nobody has ever been damaged in my paper by saying I do not know.")),
    dict(n=5, file="a5_cpe_mm_speaker_5.mp3", voice="antonio", task1="F", task2="D", text=(
        "My job is the two hours before, and most of it is subtraction. Ministers arrive wanting to take "
        "twenty lines in. I take out seventeen. What is left has to be things they would say to a friend "
        "in a corridor, because that is the only register that survives forty seconds of pressure.")),
]
TASK1_OPTS = [
    ("A", "a member of the committee asking the questions"),
    ("B", "a journalist who reports on hearings"),
    ("C", "a media trainer"),
    ("D", "an executive who has given evidence"),
    ("E", "a lawyer advising witnesses"),
    ("F", "a civil servant who prepares ministers"),
    ("G", "an academic who studies political communication"),
    ("H", "a committee clerk"),
]
TASK2_OPTS = [
    ("A", "The pause before answering is worth more than any technique."),
    ("B", "Hearings should be shorter and less adversarial."),
    ("C", "Preparing an answer for everything makes you worse, not better."),
    ("D", "Preparation is mostly a matter of taking material away."),
    ("E", "A witness who openly refuses to answer gains credit rather than losing it."),
    ("F", "Witnesses are treated unfairly by the way the format is designed."),
    ("G", "The questions asked are rarely the ones that matter."),
    ("H", "What damages a witness is sounding like a document rather than a person."),
]

# ── GRAMATICA ────────────────────────────────────────────────────────────────
GRAMMAR_QUIZ = [
    ("&ldquo;<b>Had</b> the committee asked earlier, we would have published it.&rdquo; Compared with the "
     "version using <i>if</i>, the inverted form", [
         ("changes the meaning to a real possibility.", False),
         ("raises the register, which in a hearing reads as careful rather than evasive.", True),
         ("is the only correct form in formal English.", False),
         ("suggests the committee is being blamed.", False)]),
    ("&ldquo;I am not in a position to answer that <b>at this stage</b>.&rdquo; The phrase at the end is "
     "doing which job?", [
         ("Softening the refusal by making it sound temporary.", True),
         ("Indicating that somebody else will answer instead.", False),
         ("Suggesting the question was improper.", False),
         ("Making the refusal more formal without changing it.", False)]),
    ("Which of these pushes back on the <b>premise</b> rather than on the person?", [
         ("With respect, you have misunderstood the figures.", False),
         ("I am not sure that is entirely fair to what I said.", True),
         ("That is simply not correct.", False),
         ("I would rather not be drawn on that.", False)]),
    ("<b>Should</b> you require the detail, it is in the annexe.&rdquo; Using <i>should</i> here rather "
     "than <i>if</i>", [
         ("makes the condition less likely and the offer more courteous.", True),
         ("turns the sentence into an instruction.", False),
         ("is required after a negative main clause.", False),
         ("indicates that the annexe may not exist.", False)]),
    ("A witness answers: &ldquo;That is not how I would put it myself.&rdquo; What has she done?", [
         ("Conceded the point while appearing to resist.", False),
         ("Disagreed without accusing the questioner of anything.", True),
         ("Refused to answer the question.", False),
         ("Agreed with the substance and objected to the tone.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="", after=" we would have brought the figures with us.",
         answer="Had we known the question was coming,", alt="Had we known that was coming,",
         hint="Third conditional, inverted. No &ldquo;if&rdquo;."),
    dict(before="", after=" I am happy to write to the committee afterwards.",
         answer="Should you need the detail,", alt="Should you require the detail,",
         hint="First conditional, inverted."),
    dict(before="I am ", after=" at this stage.",
         answer="not able to give you that figure", alt="not in a position to give you that figure",
         hint="Refuse, and put a limit of TIME on the refusal."),
    dict(before="That is ", after=" it myself.",
         answer="not quite how I would put", alt="not how I would put",
         hint="Disagree with the wording, not with the person."),
]

# ── SPEAKING & WRITING ───────────────────────────────────────────────────────
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> You are before a committee that believes your "
    "sector has been over-rewarded for risk it never carried. Answer this: <i>&ldquo;What have you been "
    "paid for?&rdquo;</i> Name your three red lines out loud at the start, give everything else freely, "
    "and use at least two inverted conditionals."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "You named three red lines. Which of the three would you give up first, and why that one?",
    "Refuse my next question, out loud, and tell me why you are refusing it.",
    "I am going to restate your argument in its weakest form. Correct my version without telling me I am "
    "wrong.",
    "One sentence: what would change your mind?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe reiniciar. A pergunta 2 e a mais util -- ele tem de recusar EM VOZ ALTA "
    "e dizer por que, que e a coisa que quase ninguem treina. Na 3, monte de proposito um straw man do "
    "argumento dele e veja se ele corrige a SUA versao sem dizer que voce entendeu errado."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> You are both appearing before the same committee "
    "next week, on opposite sides of a disputed tariff decision. Together, agree the two things you will "
    "both concede in public, so that neither of you is ambushed with the other&rsquo;s concession. You "
    "have to agree on the wording of both."
)
DEBATE_1_MOTION = (
    "This house believes that in a hostile hearing, saying &ldquo;I do not know&rdquo; costs less than any "
    "prepared answer."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you open with the strongest argument against yourself.",
    "At least one inverted conditional per turn. If it sounds forced, it was.",
]
DEBATE_2_MOTION = (
    "This house believes that a witness who refuses to answer is more trustworthy than one who answers "
    "everything."
)
DEBATE_2_RULES = [
    "The teacher gives you the side. You do not choose it.",
    "Before you answer, restate the strongest point the other side has made, in your own words, so that "
    "they accept your version of it.",
    "Only then do you respond. A turn that skips the concession does not count.",
]
DEBATE_2_TEACHER = (
    "Segundo debate (6 min): DE o lado a ele, de preferencia o que ele nao defenderia. O que se mede e "
    "CONCESSAO: ele tem de reformular o ponto mais forte do outro lado a ponto de voce aceitar a "
    "reformulacao. Se ele reformula uma versao fraca, e straw man -- e a aula inteira foi sobre isso."
)
WRITING_TASK = (
    "<b>Paper 2, Part 2 &mdash; a briefing note, 280 to 320 words, for the next lesson.</b> A colleague "
    "is appearing before a regulator next month and has asked you what to prepare. Write the note. State "
    "what they should decide in advance, what they should give away freely, and what to say when they will "
    "not answer. Assume they have done this badly once already."
)
WRITING_MODEL = (
    "Three things are being read for. A specific instruction, not a principle: &ldquo;write down three "
    "numbers&rdquo; beats &ldquo;be prepared&rdquo;. A sentence they can actually say out loud when they "
    "refuse. And one honest warning about what will feel wrong while it is working. A note made of good "
    "advice nobody can act on has failed."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura. Se ele pedir mais, devolva a "
    "pergunta: 'what would your colleague DO differently on the morning?'."
)

# ── ROLE-PLAY GUIADO ─────────────────────────────────────────────────────────
# Exigido pelo contrato do framework e cobrado pelo GATE 16, que so roda no servidor.
ROLEPLAY_SCENARIO = (
    "Your teacher is a committee member who believes your sector has been paid for risk it never carried. "
    "She has six minutes and no interest in being persuaded. You have two minutes to answer without "
    "conceding the substance and without sounding like a document."
)
ROLEPLAY_CHIPS = ['a red line', 'to concede a point', 'to reframe', 'common ground',
                  'should you need', 'that is not how I would put it']
ROLEPLAY_TEACHER = (
    "Role-play guiado (4 min): voce e a parlamentar, e interrompe DUAS vezes, sem pedir licenca. "
    "Cronometre os dois minutos. Este e o degrau GUIADO, com chips na tela; o long turn a seguir e o mesmo "
    "conteudo sem apoio nenhum, e a diferenca entre os dois e o que voce devolve como feedback."
)
