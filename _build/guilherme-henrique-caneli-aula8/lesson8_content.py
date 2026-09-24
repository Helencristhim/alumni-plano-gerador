#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 8, em formato de prova (CPE)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula8 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)
VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]
VOCAB_CARDS_1 = VOCAB[:5]
VOCAB_CARDS_2 = VOCAB[5:10]

MATCH_OPTS = [
    'a standard you are measured against, usually somebody else&rsquo;s performance',
    'a point on your own route, which you set yourself',
    'the document that says what did not work and sells nothing',
    'the argument running underneath a whole programme',
    'an owner, a date, and otherwise a wish',
    'the meeting within the week, before memory turns into preference',
]
MATCH_ROWS = [
    ('A benchmark', 'a standard you are measured against, usually somebody else&rsquo;s performance'),
    ('A milestone', 'a point on your own route, which you set yourself'),
    ('A retrospective', 'the document that says what did not work and sells nothing'),
    ('A through line', 'the argument running underneath a whole programme'),
    ('An action item', 'an owner, a date, and otherwise a wish'),
    ('A debrief', 'the meeting within the week, before memory turns into preference'),
]
COLLOC_BANK = ['take stock in public', 'follow through on a commitment', 'circle back at ninety days',
               'set a benchmark', 'publish a roadmap', 'run a debrief']
COLLOC_OPTS = ['stock', 'follow', 'circle', 'benchmark', 'roadmap', 'debrief']
COLLOC_ROWS = [
    ('The point of the last twenty minutes is to ____ .', 'take stock in public'),
    ('Agreeing is free; what costs is to ____ .', 'follow through on a commitment'),
    ('Put a date on it and ____ on the three that mattered.', 'circle back at ninety days'),
    ('You cannot ____ against yourself: it has to be somebody else.', 'set a benchmark'),
    ('Sequence the items so the room sees the blockage: ____ .', 'publish a roadmap'),
    ('Do it inside a week, while memory is still memory: ____ .', 'run a debrief'),
]
CLOZE_BANK = ['a call to action', 'a scorecard', 'a through line', 'an action item',
              'a retrospective', 'a closing address', 'a milestone', 'a benchmark']
CLOZE_ITEMS = [
    dict(before='1. Without a date attached, ', after=' is a goodbye with a verb in it.',
         answer='a call to action', alt='call to action', hint='Four words, with the article.'),
    dict(before='2. What you open at the next event to see how many survived the year is ', after='.',
         answer='a scorecard', alt='scorecard', hint='Two words, with the article.'),
    dict(before='3. The argument running underneath the whole programme, visible only from the end, is ',
         after='.', answer='a through line', alt='through line', hint='Three words, with the article.'),
    dict(before='4. An owner and a date: without both, ', after=' is a wish.',
         answer='an action item', alt='action item', hint='Three words, with the article.'),
    dict(before='5. The only document in the cycle that is not selling anything is ', after='.',
         answer='a retrospective', alt='retrospective', hint='Two words, with the article.'),
    dict(before='6. A point on your own route, set by you, is ', after='.',
         answer='a milestone', alt='milestone', hint='Two words, with the article.'),
    dict(before='7. A standard set by somebody else&rsquo;s performance is ', after='.',
         answer='a benchmark', alt='benchmark', hint='Two words, with the article.'),
]
CLOZE_NOT_NEEDED = 'a closing address'

ARTICLE_TITLE = "The Year Between Two Conferences"
ARTICLE_STANDFIRST = "Adapted from a comment essay on convening &middot; ~600 words"
ARTICLE = [
    ("The interesting part of an annual event is not the three days. It is the three hundred and "
     "sixty-two that follow, and almost nobody measures them.", 1, ""),
    ("<b>A closing address</b> is where that year is supposed to be set in motion, and it is usually "
     "where it quietly is not. A speaker who lists the panels has produced a receipt. One who names "
     "<b>a through line</b> &mdash; the argument that ran underneath the whole programme &mdash; has at "
     "least told the room what it had been arguing about.", 2, ""),
    ("What changes Monday is a date. &ldquo;We will continue the conversation&rdquo; is <b>a call to "
     "action</b> in roughly the sense that a shrug is an answer. <i>By this time next year we will have "
     "published the framework</i>, and <i>between now and March the working group will be meeting "
     "monthly</i>: those are sentences somebody can be held to.", 3, ""),
    ("The apparatus is dull. <b>An action item</b> has an owner and a date and is otherwise a wish. "
     "<b>A roadmap</b> puts the items in sequence so that a room can see which one is blocking the rest. "
     "<b>A scorecard</b> is what you open at the next event.", 4,
     " <b>A debrief</b> within the week, while people still remember what was said rather than what they "
     "wish had been said, costs an hour and saves the year."),
    ("Two words get confused, and the confusion is expensive. <b>A benchmark</b> is a standard you are "
     "measured against, usually somebody else&rsquo;s performance. <b>A milestone</b> is a point on your "
     "own route.", 5,
     " A room that has not grasped the difference will applaud a chart showing every milestone met by an "
     "organisation falling further behind the benchmark each quarter."),
    ("The honest instrument is the least popular. <b>A retrospective</b> that says what did not work is "
     "read by almost nobody and changes almost everything, because it is the only document in the cycle "
     "that is not selling something. To <b>take stock</b> in public, to <b>recap</b> what was promised "
     "rather than what was achieved, and to <b>follow through on</b> three items rather than agreeing to "
     "<b>circle back</b> on fourteen:", 6, ""),
    ("The test is crude and it works. Two weeks after the event, ask four people who were there what is "
     "being done differently. If the four answers converge, the closing worked, whatever it sounded like "
     "on the day. If they do not, the week was a conference, which is a perfectly respectable thing to "
     "have been and is not what anybody said they were buying.", None, ""),
]
GAP_OPTIONS = [
    ('A', 'The grammar is doing real work there, because a commitment without a tense that lands on a '
          'date is only a sentiment.'),
    ('B', 'You can hit every one of the second and still be losing on the first.'),
    ('C', 'What gets measured instead is attendance, satisfaction and the number of sessions, none of '
          'which tells anybody whether something happened.'),
    ('D', 'Most organisers now publish the following year&rsquo;s programme six months in advance.'),
    ('E', 'Neither, by itself, changes what anybody does on Monday morning.'),
    ('F', 'that is the whole discipline, and it is why so few organisations manage it twice in a row.'),
    ('G', 'None of these instruments is clever, and that is precisely why they survive.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "G"), ("5", "B"), ("6", "F")]
GAP_KEY = (
    "<b>1 C</b> &mdash; &ldquo;almost nobody measures them&rdquo; demands what IS measured instead.<br>"
    "<b>2 E</b> &mdash; &ldquo;Neither&rdquo; needs the two speakers just contrasted, and &ldquo;What "
    "changes Monday&rdquo; picks up &ldquo;Monday morning&rdquo; directly.<br>"
    "<b>3 A</b> &mdash; two tensed sentences have just been quoted; only A explains why the TENSE is the "
    "point.<br>"
    "<b>4 G</b> &mdash; &ldquo;The apparatus is dull&rdquo; is answered by why dull survives, and the "
    "debrief sentence then continues the list.<br>"
    "<b>5 B</b> &mdash; &ldquo;the second&rdquo; and &ldquo;the first&rdquo; can only be milestone and "
    "benchmark, in that order.<br>"
    "<b>6 F</b> &mdash; the paragraph ends on a colon; only F completes the sentence grammatically.<br>"
    "<b>D</b> is the distractor: true, on topic, and it answers no reference."
)
MCQ = [
    ("What does the writer say is the interesting part of an annual event?", [
        ("The quality of the sessions themselves.", False),
        ("The rest of the year, which almost nobody measures.", True),
        ("The private conversations between delegates.", False),
        ("The choice of speakers.", False)]),
    ("What is the difference the writer draws between the two kinds of closing speaker?", [
        ("One is shorter than the other.", False),
        ("One produces a receipt; the other at least names the argument.", True),
        ("One thanks the sponsors and the other does not.", False),
        ("One uses notes and the other does not.", False)]),
    ("Why does the writer quote two sentences in the third paragraph?", [
        ("To show how commitments are worded in this sector.", False),
        ("Because the tense is what makes them enforceable.", True),
        ("To contrast a promise with a prediction.", False),
        ("Because both were made at the same event.", False)]),
    ("What does the writer say about the instruments in the fourth paragraph?", [
        ("They are used too rarely to judge.", False),
        ("They survive precisely because they are not clever.", True),
        ("They work only in large organisations.", False),
        ("They have been replaced by software.", False)]),
    ("What is the danger of confusing a benchmark with a milestone?", [
        ("Targets are set too low.", False),
        ("An organisation can meet all its own points while falling behind others.", True),
        ("Progress becomes impossible to report.", False),
        ("The roadmap has to be rewritten each quarter.", False)]),
    ("The writer&rsquo;s final test judges a closing address by", [
        ("how the room felt on the day.", False),
        ("whether four people, a fortnight later, describe the same change.", True),
        ("how many action items were agreed.", False),
        ("whether the retrospective was published.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 b</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br><i>Item 3 is the bridge into the grammar: the two quoted sentences are a future perfect "
    "and a future continuous, and the writer&rsquo;s claim is that the tense IS the commitment.</i>"
)
WORD_FORMATION = [
    dict(before="Almost nothing in the year that follows is ", after=". (MEASURE)",
         answer="measurable", hint="-able adjective from the verb."),
    dict(before="A recap of what was promised is more useful than a list of every ", after=". (ACHIEVE)",
         answer="achievement", hint="Noun from the verb."),
    dict(before="Without a date, a ", after=" is only a sentiment. (COMMIT)",
         answer="commitment", hint="Noun from the verb."),
    dict(before="An owner is what turns an item into ", after=". (ACCOUNT)",
         answer="accountability", hint="Abstract noun. Watch the internal change."),
    dict(before="What the cycle rewards is not brilliance but ", after=". (PERSIST)",
         answer="persistence", hint="Abstract noun from the verb."),
    dict(before="The organisations that manage it twice are unusually ", after=". (DISCIPLINE)",
         answer="disciplined", hint="Adjective from the noun."),
    dict(before="The test is whether the four answers show any ", after=". (CONVERGE)",
         answer="convergence", hint="Noun from the verb."),
    dict(before="", after=", the least popular document is the one that changes most. (NOTE)",
         answer="Notably", hint="Adverb, capital letter, comma after it."),
]
TRANSFORMATIONS = [
    dict(lead="The framework will be published before next December.", key="PUBLISHED",
         before="By next December the framework ", after=".",
         answer="will have been published",
         hint="Future perfect, passive: finished by a point in the future."),
    dict(lead="We will still be waiting for the licence in June.", key="WAITING",
         before="In June we ", after=" for the licence.",
         answer="will still be waiting",
         hint="Future continuous: an action in progress at a future moment."),
    dict(lead="The group will meet six times before the review.", key="MET",
         before="By the review the group ", after=" six times.",
         answer="will have met", hint="Future perfect, counting completed events."),
    dict(lead="Next month it is ten years since the first roadmap was agreed.", key="SINCE",
         before="Next month it ", after=" the first roadmap was agreed.",
         answer="will have been ten years since",
         hint="Future perfect with &ldquo;since&rdquo;."),
    dict(lead="The audit will finish before you arrive.", key="COMPLETED",
         before="The audit ", after=" by the time you arrive.",
         answer="will have been completed",
         hint="Future perfect, passive, with &ldquo;by the time&rdquo;."),
    dict(lead="At this hour next week I shall be on the plane home.", key="FLYING",
         before="This time next week I ", after=" home.",
         answer="will be flying", hint="Future continuous for a fixed future activity."),
]
TRANSFORM_KEY = (
    "<b>1</b> will have been published<br><b>2</b> will still be waiting<br><b>3</b> will have met<br>"
    "<b>4</b> will have been ten years since<br><b>5</b> will have been completed<br>"
    "<b>6</b> will be flying<br><i>Three of these are perfect and three are continuous, and the "
    "difference is not difficulty: it is whether the sentence lands ON a date or ACROSS a period. A "
    "commitment needs the first; a reassurance usually needs the second.</i>"
)
TALK_FILE = "a8_cpe_talk_the_three_hundred_and_sixty_two.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "My title is chief of staff, which in practice means I am the person who finds out, six months later, "
    "that nothing happened. So I have opinions about closings. "
    "Here is the pattern. The week goes well. Everybody is energised, which is a word I have learned to "
    "distrust. Fourteen action items are agreed in the last session and written on a flipchart. The "
    "flipchart is photographed. The photograph is circulated. And that is the entire lifecycle: nothing "
    "in that list has an owner, so nothing in that list has a future. "
    "What we do now is unglamorous. Three items. Not fourteen. Each one has a name against it, in the "
    "room, out loud, and a date that is not a quarter but a day. If nobody will put their name to it in "
    "front of forty people, it was never going to happen anyway, and we have just saved ourselves the "
    "embarrassment of pretending. "
    "The second change was the debrief. We used to do it after three weeks, when everybody was free. "
    "Now it is inside seven days, and the difference is enormous, because after ten days people no longer "
    "remember the session. They remember their own summary of the session, which is a different and much "
    "more flattering document. "
    "And the third. We separated two words that everybody in my organisation used to use "
    "interchangeably. A milestone is ours. A benchmark is somebody else's. We hit every milestone in the "
    "first year and lost four points of market share, and nobody could explain it, because the chart on "
    "the wall was all green."
)
TALK_ITEMS = [
    dict(before="1. The speaker is the person who finds out, six months later, that ", after=".",
         answer="nothing happened", hint="Two words."),
    dict(before="2. The word he has learned to distrust is ", after=".",
         answer="energised", alt="energized", hint="One word."),
    dict(before="3. The fourteen action items are written on a ", after=".",
         answer="flipchart", hint="One word."),
    dict(before="4. Nothing on that list has an owner, so nothing on it has a ", after=".",
         answer="future", hint="One word."),
    dict(before="5. Each item now has a date that is not a quarter but a ", after=".",
         answer="day", hint="One word."),
    dict(before="6. The debrief now happens inside ", after=" days.",
         answer="seven", hint="One word."),
    dict(before="7. After ten days people remember their own ", after=" of the session.",
         answer="summary", hint="One word."),
    dict(before="8. They hit every milestone and lost four points of ", after=".",
         answer="market share", hint="Two words."),
]
SPEAKERS = [
    dict(n=1, file="a8_cpe_mm_speaker_1.mp3", voice="alice", task1="C", task2="B", text=(
        "I stopped allowing the flipchart. It sounds petty and it changed everything. If an item cannot be "
        "said as a sentence with a name and a day in it, out loud, in front of the room, it does not go on "
        "the list. We went from fourteen items to three, and for the first time all three were closed.")),
    dict(n=2, file="a8_cpe_mm_speaker_2.mp3", voice="arthur", task1="F", task2="E", text=(
        "Everyone wants the retrospective to be balanced. I have written eleven of them and the balanced "
        "ones are worthless. The useful document is the one that says this did not work and here is why, "
        "and it is read by four people, and those four are the ones who decide next year&rsquo;s "
        "programme.")),
    dict(n=3, file="a8_cpe_mm_speaker_3.mp3", voice="matilda", task1="A", task2="D", text=(
        "We were very proud of our chart. Every target green, two years running. Then somebody asked what "
        "our competitors had done over the same period, and the room went quiet. We had been measuring "
        "ourselves against ourselves, which is a comfortable thing to do and tells you nothing at all.")),
    dict(n=4, file="a8_cpe_mm_speaker_4.mp3", voice="george", task1="D", task2="H", text=(
        "I sponsor three of these a year and I used to judge them on the room: who came, how it felt, "
        "whether my chief executive was happy. Now I ask one question of my own people a fortnight later. "
        "What are we doing differently? If I get four different answers, I do not renew.")),
    dict(n=5, file="a8_cpe_mm_speaker_5.mp3", voice="antonio", task1="B", task2="A", text=(
        "The closing is the only part I now rehearse, which would have astonished me ten years ago. Not "
        "the words. The dates. I will not say we will continue the conversation. I will say the working "
        "group meets on the fourteenth, and by June we will have published. If I cannot say a month, I do "
        "not say the sentence.")),
]
TASK1_OPTS = [
    ("A", "a strategy director"),
    ("B", "a conference chair"),
    ("C", "a chief of staff"),
    ("D", "a corporate sponsor"),
    ("E", "a management consultant"),
    ("F", "an evaluator who writes retrospectives"),
    ("G", "a delegate attending for the first time"),
    ("H", "a programme administrator"),
]
TASK2_OPTS = [
    ("A", "A commitment is only real once it carries a month."),
    ("B", "Fewer items, each with a name attached, close more often than many."),
    ("C", "Conferences should be judged on attendance as well as outcomes."),
    ("D", "Measuring yourself against your own targets tells you nothing."),
    ("E", "A balanced retrospective is worth less than an uncomfortable one."),
    ("F", "Debriefs should be held jointly with the organisers."),
    ("G", "Sponsors should have a say in the programme."),
    ("H", "The only useful test is what people are doing differently afterwards."),
]
GRAMMAR_QUIZ = [
    ("&ldquo;By June we <b>will have published</b> the framework.&rdquo; Compared with &ldquo;we will "
     "publish it in June&rdquo;, the perfect form", [
         ("is more formal but otherwise identical.", False),
         ("fixes a deadline the speaker can be held to, rather than a plan.", True),
         ("suggests the speaker is less certain.", False),
         ("implies somebody else will do the publishing.", False)]),
    ("&ldquo;Between now and March the group <b>will be meeting</b> monthly.&rdquo; The continuous form "
     "here reports", [
         ("an intention that has not been agreed.", False),
         ("an arrangement that runs across a period rather than landing on a date.", True),
         ("an obligation imposed from outside.", False),
         ("a prediction about what is likely.", False)]),
    ("Which of these is the weakest commitment?", [
         ("By the fourteenth we will have circulated the roadmap.", False),
         ("We will be looking at the roadmap over the coming period.", True),
         ("The roadmap will have been circulated before the next board.", False),
         ("We will circulate the roadmap on the fourteenth.", False)]),
    ("In a closing address, the future continuous is most useful for", [
         ("committing to a deliverable.", False),
         ("reassuring a room that work continues between now and then.", True),
         ("reporting what somebody else has promised.", False),
         ("setting a benchmark.", False)]),
    ("&ldquo;This time next year it <b>will have been</b> five years since the first roadmap.&rdquo; The "
     "form is being used to", [
         ("predict what will happen next year.", False),
         ("measure a span of time from a future vantage point.", True),
         ("report what was agreed five years ago.", False),
         ("express regret about the delay.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="By the time the board meets in June, the working group ",
         after=" four times.", answer="will have met", hint="Future perfect, counting completed events."),
    dict(before="Between now and March the review ", after=" alongside the consultation.",
         answer="will be running", alt="will be taking place",
         hint="Future continuous, for work that runs across a period."),
    dict(before="By the fourteenth the roadmap ", after=" to every delegate.",
         answer="will have been circulated", alt="will have been sent",
         hint="Future perfect, passive, landing on a date."),
    dict(before="This time next year it ", after=" since the first scorecard.",
         answer="will have been three years", alt="will have been two years",
         hint="Future perfect with a span of time. The number is yours to choose."),
]
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> You are closing a three-day forum. Answer this: "
    "<i>&ldquo;What will be different a year from now, and how will we know?&rdquo;</i> Name the through "
    "line, then give exactly three commitments. Every one of them has to carry a month, and at least one "
    "has to be a future continuous."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "Name the owner of your first commitment. Out loud, now.",
    "Say your second commitment again using the other future form, and tell me what changed.",
    "Somebody says three is too few and the room expected fourteen. Concede, then hold.",
    "One sentence: what will your retrospective admit next year?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe reiniciar. A pergunta 1 e a mais dura e a mais curta -- se ele hesitar "
    "no nome, o compromisso nao existe, e e exatamente o que o texto diz. A 2 e a da gramatica: a mesma "
    "informacao nas duas formas, e ele tem de NOMEAR a diferenca."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> You have the last ten minutes of a forum and "
    "fourteen suggested action items on a flipchart. Together, cut them to three, decide who owns each "
    "one, and agree the date you will circle back. You have to say all three out loud, as complete "
    "sentences, before the four minutes are up."
)
DEBATE_1_MOTION = (
    "This house believes that a closing address should contain no thanks at all, only commitments."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you open with the strongest argument against yourself.",
    "Every commitment you mention has to carry a tense that lands on a date.",
]
DEBATE_2_MOTION = (
    "This house believes that an organisation should publish its retrospective in full, including what "
    "failed."
)
DEBATE_2_RULES = [
    "The teacher gives you the side. You do not choose it.",
    "Before you answer, restate the strongest point the other side has made, in your own words, so that "
    "they accept your version of it.",
    "Only then do you respond. A turn that skips the concession does not count.",
]
DEBATE_2_TEACHER = (
    "Segundo debate (6 min): DE o lado a ele. O que se mede e CONCESSAO: ele tem de reformular o ponto "
    "mais forte do outro lado a ponto de voce aceitar a reformulacao. E a ultima aula do pacote -- se a "
    "concessao sair limpa aqui, o ciclo inteiro fechou."
)
WRITING_TASK = (
    "<b>Paper 2, Part 2 &mdash; a closing note, 280 to 320 words, for the next lesson.</b> Write the note "
    "you would circulate the morning after a forum you closed. Give the through line, the three "
    "commitments with owners and dates, and one honest sentence about what the week did not resolve. "
    "Assume it will be read a year from now, next to the scorecard."
)
WRITING_MODEL = (
    "Three things are being read for. A through line stated in one sentence, not a list of sessions. "
    "Three commitments, each with a name and a month, written in a tense that lands. And one admission "
    "that costs something. A note that a reader could not check against reality in twelve months has not "
    "closed anything."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura. Se ele pedir mais, devolva a "
    "pergunta: 'could somebody hold you to this in a year?'."
)
ROLEPLAY_SCENARIO = (
    "Your teacher is the sponsor who paid for the forum and is deciding whether to renew. She has two "
    "minutes in a corridor and one question: what will be different a year from now? She will ask for a "
    "name and a month on anything you say."
)
ROLEPLAY_CHIPS = ['a through line', 'an action item', 'to follow through on', 'a scorecard',
                  'by June we will have', 'the group will be meeting']
ROLEPLAY_TEACHER = (
    "Role-play guiado (4 min): voce e a patrocinadora, e pede NOME e MES em cada compromisso que ele "
    "citar. Cronometre os dois minutos. Degrau GUIADO, com chips na tela; o long turn a seguir e o mesmo "
    "conteudo sem apoio nenhum, e e o ultimo da serie."
)
