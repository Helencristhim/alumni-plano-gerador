#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 3, em formato de prova (CPE).

Mesmo caminho da aula 2, e pelo mesmo motivo: o professor Andre pediu tarefa de
prova internacional, com raciocinio, em vez de card com definicao e matching.

DUAS TRAVAS QUE VALEM PARA TODA AULA DAQUI PARA A FRENTE
--------------------------------------------------------
1. Nada aqui pode aparecer na PRE-CLASS desta aula. A pre-class ja foi refeita
   (PR #2842) e tem texto, compreensao, word formation, transformations e um
   listen+choose proprios. A pre-class PREPARA; o deck ENTREGA a prova.
2. O lexico (os 14 termos) e o grammar_point NAO mudam: sao a espinha do
   programa, e o `specs/aula3.py` e o dono deles. Este arquivo importa de la em
   vez de copiar, para que os dois nunca divirjam.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula3 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)

# ── 1. LEXICO -- o dono e o spec, aqui so se le ──────────────────────────────
VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]

# ── 2. VOCABULARIO: a DEFINICAO e a frente do card ───────────────────────────
# O aluno produz o termo e so entao revela. Para quem ja tem o vocabulario
# passivo, este e o unico uso util de um reveal.
VOCAB_CARDS_1 = [(w, d, ex) for w, d, ex in VOCAB[:5]]
VOCAB_CARDS_2 = [(w, d, ex) for w, d, ex in VOCAB[5:10]]

# ── 3. Qual e qual, exatamente (discriminacao, nao reconhecimento) ───────────
MATCH_OPTS = [
    'the sentence that tells the room how to hear what follows',
    'the turn that moves the room off the comfortable half of the argument',
    'the short opening that says what the week is about',
    'the informal on-stage interview',
    'the set piece one person delivers from the front',
    'the two minutes about microphones, timings and fire exits',
]
MATCH_ROWS = [
    ('A framing device', 'the sentence that tells the room how to hear what follows'),
    ('A rhetorical pivot', 'the turn that moves the room off the comfortable half of the argument'),
    ('A curtain-raiser', 'the short opening that says what the week is about'),
    ('A fireside chat', 'the informal on-stage interview'),
    ('A keynote', 'the set piece one person delivers from the front'),
    ('A housekeeping note', 'the two minutes about microphones, timings and fire exits'),
]

COLLOC_BANK = ['set the tone', 'open the floor', 'hand over to', 'convene a session',
               'coalesce around a view', 'call for a show of hands']
COLLOC_OPTS = ['tone', 'floor', 'over', 'convene', 'coalesce', 'hands']
COLLOC_ROWS = [
    ('The first two minutes ____ for everything that follows.', 'set the tone'),
    ('After the third speaker the chair will ____ to questions.', 'open the floor'),
    ('With that, let me ____ our first panellist.', 'hand over to'),
    ('The bank agreed to ____ the working group in March.', 'convene a session'),
    ('By the second day the room had begun to ____ .', 'coalesce around a view'),
    ('Rather than read the agenda, the chair decided to ____ .', 'call for a show of hands'),
]

CLOZE_BANK = ['a curtain-raiser', 'agenda-setting', 'a framing device', 'a rhetorical pivot',
              'an inflection point', 'a housekeeping note', 'a show of hands', 'a fireside chat']
CLOZE_ITEMS = [
    dict(before='1. Deciding who speaks, and who is never asked back, is ',
         after=' whether or not the organisers would use the word.',
         answer='agenda-setting', hint='Two words, with a hyphen. It is what a programme does.'),
    dict(before='2. &ldquo;Not since 2008&rdquo; is ', after=': it tells the room how to hear the number that follows.',
         answer='a framing device', alt='framing device', hint='Three words, with the article.'),
    dict(before='3. The turn at minute three, away from the comfortable half of the argument, is ',
         after='.', answer='a rhetorical pivot', alt='rhetorical pivot', hint='Three words, with the article.'),
    dict(before='4. Two minutes on microphones and fire exits is ', after=', and it belongs in one sentence.',
         answer='a housekeeping note', alt='housekeeping note', hint='Three words, with the article.'),
    dict(before='5. The sector calls it ', after=' when the direction of travel changes, not merely the speed.',
         answer='an inflection point', alt='inflection point', hint='Three words, with the article.'),
    dict(before='6. The session that opens the week and names the question is ', after='.',
         answer='a curtain-raiser', alt='curtain-raiser', hint='Three words, with the article.'),
    dict(before='7. Asking the room to raise their arms produces ',
         after=', which is a device for manufacturing the look of consensus.',
         answer='a show of hands', alt='show of hands', hint='Four words, with the article.'),
]
CLOZE_NOT_NEEDED = 'a fireside chat'

# ── 4. READING (Paper 1, Part 6 e Part 5) ────────────────────────────────────
# Artigo NOVO. O da pre-class e outro ("The First Ninety Seconds"): la o aluno le
# para entender, aqui le para encaixar seis frases retiradas.
ARTICLE_TITLE = "Why the Room Still Matters"
ARTICLE_STANDFIRST = "Adapted from a comment essay on the conference economy &middot; ~600 words"
ARTICLE = [
    ("The prediction was confident and it was wrong. Once a video call could carry a face and a slide deck "
     "at no cost, the argument ran, the industry that flies four thousand people to a hotel for three days "
     "would quietly die.", 1,
     " The circuit is larger than it was, the tickets cost more, and the waiting lists are longer."),

    ("The explanation people offer first is networking, which is true and shallow.", 2,
     " A video call is a transaction with an agenda and an end time. A corridor is a place where somebody "
     "says the thing they would never put in writing, and where you discover, in four seconds of "
     "hesitation, that the deal everybody assumes is closed is not closed."),

    ("The second function is harder to admit. A conference is a machine for producing agreement. When an "
     "organisation decides to <b>convene</b> four hundred people, and then decides who will deliver "
     "<b>the keynote</b>, who will sit for <b>the fireside chat</b> and who will not be invited back, it is "
     "doing <b>agenda-setting</b> whether or not it would use the word.", 3, ""),

    ("That is why the opening carries so much weight. <b>A curtain-raiser</b> is not decoration. It is the "
     "moment the organisers&rsquo; private argument becomes the room&rsquo;s public one, and a chair who "
     "understands the job will <b>set the tone</b> by choosing the hardest version of the question rather "
     "than the most agreeable one. <b>A framing device</b> &mdash; a date, a number, a single contrast "
     "&mdash; does most of the work in the first minute, and <b>a rhetorical pivot</b> somewhere around the "
     "third moves the room off the comfortable half of the argument.", 4,
     " The rest of the programme then either answers that question or visibly avoids it, and both are "
     "informative."),

    ("None of this is free of theatre. <b>A show of hands</b> is a device for manufacturing the appearance "
     "of consensus, and an experienced audience knows it. <b>A housekeeping note</b> can be used to eat the "
     "two minutes a difficult speaker was going to use.", 5,
     " The instruments are neutral; what is not neutral is whose hand is on them."),

    ("What has genuinely changed is the cost of being wrong. When the sector could <b>coalesce around</b> a "
     "view slowly, over years, a bad view was survivable.", 6,
     " A position formed in a hotel ballroom in March is priced into the market by June, and the people who "
     "formed it are under no obligation to revisit it."),

    ("So the room survives, and it survives for a reason that flatters nobody: it is the cheapest "
     "mechanism available for finding out what a few hundred people who control a great deal of money have "
     "decided to believe this year. If the sector really is at <b>an inflection point</b>, the room will "
     "say so before the data does. And by the time the chair finally announces that it is time to "
     "<b>hand over to</b> the first speaker, the argument that matters has usually already been made.",
     None, ""),
]
GAP_OPTIONS = [
    ('A', 'The programme is an argument about what the sector ought to be worried about, and it is settled '
          'in a room nobody sees, months before the first delegate lands.'),
    ('B', 'Even the decision about when to <b>open the floor</b> is a decision about which questions will '
          'have time to be asked at all.'),
    ('C', 'What happened instead is the opposite of what the arithmetic predicted, and the reason has '
          'nothing to do with the quality of the technology.'),
    ('D', 'Organisers have responded by cutting the number of panels and lengthening the breaks between '
          'them.'),
    ('E', 'What a room actually supplies is the unscheduled conversation, and no platform has yet found a '
          'way to manufacture one.'),
    ('F', 'Done properly, it hands four hundred people a single sentence to disagree with for the next '
          'three days.'),
    ('G', 'Capital now moves faster than the conference calendar, which means the mistakes travel at the '
          'same speed.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "F"), ("5", "B"), ("6", "G")]
GAP_KEY = (
    "<b>1 C</b> &mdash; the paragraph has just given a prediction; &ldquo;what happened instead&rdquo; "
    "answers it, and the sentences after it are the evidence.<br>"
    "<b>2 E</b> &mdash; &ldquo;true and shallow&rdquo; demands the deeper version, and the corridor "
    "sentences that follow illustrate the <i>unscheduled</i> conversation.<br>"
    "<b>3 A</b> &mdash; &ldquo;whether or not it would use the word&rdquo; needs the word explained: the "
    "programme IS the argument.<br>"
    "<b>4 F</b> &mdash; &ldquo;Done properly&rdquo; refers back to the chair&rsquo;s choice, and &ldquo;a "
    "single sentence to disagree with&rdquo; is what the next sentence calls &ldquo;that question&rdquo;.<br>"
    "<b>5 B</b> &mdash; a third instrument in a list of two, and &ldquo;The instruments are neutral&rdquo; "
    "needs three of them to be worth the plural.<br>"
    "<b>6 G</b> &mdash; &ldquo;survivable&rdquo; in the past demands what changed; the next sentence "
    "(March to June) is the illustration of speed.<br>"
    "<b>D</b> is the distractor. It is true, it is on topic, and it answers no reference and completes no "
    "argument."
)

MCQ = [
    ("In the first paragraph, the writer describes the prediction as &ldquo;confident&rdquo; in order to", [
        ("explain why the technology was adopted so quickly.", False),
        ("set up the contrast with what actually happened.", True),
        ("criticise the people who made it.", False),
        ("suggest the prediction may still turn out to be right.", False)]),
    ("The writer calls the networking explanation &ldquo;true and shallow&rdquo; because", [
        ("networking is not in fact what delegates do.", False),
        ("it is accurate but stops short of what a room actually provides.", True),
        ("it is the explanation organisers give to sponsors.", False),
        ("it applies equally well to a video call.", False)]),
    ("The reference to &ldquo;four seconds of hesitation&rdquo; is used to make the point that", [
        ("corridors are more efficient than scheduled meetings.", False),
        ("information travels in a room that would never be written down.", True),
        ("deals in the sector are usually less advanced than they appear.", False),
        ("experienced delegates can read people quickly.", False)]),
    ("According to the fourth paragraph, what does a chair who understands the job do?", [
        ("Keeps the opening as short as the programme allows.", False),
        ("Chooses the hardest version of the question rather than the most agreeable.", True),
        ("Avoids taking a position before the first panel.", False),
        ("Uses a framing device rather than a rhetorical pivot.", False)]),
    ("What does the writer mean by &ldquo;the instruments are neutral&rdquo;?", [
        ("The devices are used equally by every chair.", False),
        ("The devices have no purpose of their own; what matters is who controls them.", True),
        ("A show of hands and a housekeeping note are equally harmless.", False),
        ("The theatre of a conference does no damage.", False)]),
    ("In the final paragraph, the writer&rsquo;s view of the conference is that it is", [
        ("an unjustifiable expense that the sector tolerates.", False),
        ("useful precisely because it exposes what a small group has decided to believe.", True),
        ("the most reliable source of data available to investors.", False),
        ("less important than the private conversations that precede it.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 b</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br>"
    "<i>In Part 5 at least one option in every item is TRUE and still wrong. Item 3 is the clearest: (a) "
    "and (d) are both defensible statements about corridors, and neither is what that sentence is doing.</i>"
)

# ── 5. USE OF ENGLISH (Paper 1, Part 3 e Part 4) ─────────────────────────────
# Itens diferentes dos da pre-class desta aula: la ela usa EMPHASIS, AGREE,
# PERSUADE, INTRODUCE, COMFORT, REPEAT e USUAL. Nenhum deles volta aqui.
WORD_FORMATION = [
    dict(before="The ", after=" had underestimated how long the queue for coffee would be. (ORGANISE)",
         answer="organisers", alt="organizers", hint="Plural noun for the people who run it."),
    dict(before="A programme is a series of ", after=" taken long before anybody arrives. (DECIDE)",
         answer="decisions", hint="Plural noun from the verb."),
    dict(before="Being left off the list is a quiet form of ", after=". (EXCLUDE)",
         answer="exclusion", hint="Noun from the verb. Watch the internal change."),
    dict(before="By the third afternoon nothing said on the platform was ", after=" any more. (CONTEST)",
         answer="contestable", hint="-able adjective: capable of being argued with."),
    dict(before="A show of hands manufactures the ", after=" of consensus. (APPEAR)",
         answer="appearance", hint="Noun from the verb."),
    dict(before="The chair ", after=" the opening by four minutes and lost the room. (LENGTH)",
         answer="lengthened", hint="Verb from the noun, past tense."),
    dict(before="The instruments are neutral; their ", after=" is exactly the point. (NEUTRAL)",
         answer="neutrality", hint="Abstract noun from the adjective."),
    dict(before="", after=", the panel that everybody skipped produced the only news. (IRONY)",
         answer="Ironically", hint="Sentence adverb, capital letter, comma after it."),
]

# Palavras-chave DIFERENTES das da pre-class (NEVER, ONLY, NOT, RARELY, SOONER,
# ONCE), na mesma gramatica: inversao negativa e limitante.
TRANSFORMATIONS = [
    dict(lead="The audience did not realise how much had been decided in advance.", key="LITTLE",
         before="", after=" how much had been decided in advance.",
         answer="Little did the audience realise", alt="Little did the audience know",
         hint="Little + inversion, for what the subject failed to notice."),
    dict(lead="The chair must not interrupt a speaker in any circumstances.", key="CIRCUMSTANCES",
         before="Under ", after=" a speaker.",
         answer="no circumstances should the chair interrupt",
         alt="no circumstances may the chair interrupt",
         hint="Under no circumstances + modal + subject + bare infinitive."),
    dict(lead="The room had barely settled when the first question came.", key="SCARCELY",
         before="", after=" the first question came.",
         answer="Scarcely had the room settled when",
         hint="Scarcely ... when ... Past perfect in the first half."),
    dict(lead="The opening was so blunt that nobody had expected it.", key="SUCH",
         before="", after=" nobody had expected it.",
         answer="Such was the bluntness of the opening that",
         alt="Such was the bluntness of the opening,",
         hint="Such + was + NOUN + that. You need the noun from the adjective."),
    dict(lead="The sponsors did not know, and the delegates did not know either.", key="NOR",
         before="The sponsors did not know, ", after=".",
         answer="nor did the delegates", alt="nor did the delegates know",
         hint="nor + auxiliary + subject, to add a second negative."),
    dict(lead="She understood the point of the session only at the very end.", key="UNTIL",
         before="", after=" understand the point of the session.",
         answer="Not until the very end did she",
         hint="Not until + time phrase + inversion in the main clause."),
]
TRANSFORM_KEY = (
    "<b>1</b> Little did the audience realise &middot; Little did the audience know<br>"
    "<b>2</b> no circumstances should the chair interrupt &middot; (also: may the chair interrupt)<br>"
    "<b>3</b> Scarcely had the room settled when<br>"
    "<b>4</b> Such was the bluntness of the opening that<br>"
    "<b>5</b> nor did the delegates &middot; nor did the delegates know<br>"
    "<b>6</b> Not until the very end did she<br>"
    "<i>Three to eight words, the key word untouched, no change of meaning. Anything outside this list is "
    "for the teacher to judge in class.</i>"
)

# ── 6. LISTENING Part A -- sentence completion (Paper 3, Part 2) ─────────────
# Audio NOVO. O da pre-class e outro (uma programme director, voz sarah_us);
# este e um organizador, voz daniel, e o aluno faz as oito lacunas EM CASA e
# chega na aula so para a correcao.
TALK_FILE = "a3_cpe_talk_building_a_programme.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "People assume a conference programme is assembled from whoever agrees to come. It is the other way "
    "round. We start with a single sentence, and everything else is built to test it. "
    "This year the sentence was: the money is no longer the constraint. That is a claim, and it is the "
    "kind of claim a room can argue with. Four years ago the sentence was about the cost of capital, and "
    "it was wrong by the second morning, which was uncomfortable but useful. "
    "Once you have the sentence, the programme is an argument. You need somebody who believes it, "
    "somebody whose business depends on it being false, and a third person who will not take a side and "
    "will keep both of them honest. That third chair is the hardest to fill and the one we spend longest "
    "on. "
    "We also decide, quite deliberately, what will not be discussed. Every year there are two or three "
    "subjects that would fill a room and produce nothing, because everybody already agrees. We leave them "
    "out and we take the complaints. "
    "The last thing, and the one nobody believes until they have run an event, is the seating. Where a "
    "delegate sits changes what a delegate says. We move name cards up to an hour before a session, and "
    "we have changed the whole shape of a discussion by moving two of them three places. "
    "And we measure it afterwards, which almost nobody does. Two weeks later we call twenty delegates and "
    "ask one question: what are you doing differently? If the answers do not converge, the programme "
    "failed, however good the week felt at the time."
)
TALK_ITEMS = [
    dict(before="1. A programme does not start with speakers; it starts with a single ", after=".",
         answer="sentence", hint="One word. The speaker comes back to it four times."),
    dict(before="2. This year the claim was that the money is no longer the ", after=".",
         answer="constraint", hint="One word, in the second paragraph."),
    dict(before="3. Four years ago the sentence was about the cost of ", after=".",
         answer="capital", hint="One word."),
    dict(before="4. The programme needs somebody whose business depends on the claim being ", after=".",
         answer="false", hint="One word. Not &ldquo;wrong&rdquo;: write what you hear."),
    dict(before="5. The hardest chair to fill is the one who will not take ", after=".",
         answer="a side", alt="sides", hint="Two words, with the article."),
    dict(before="6. Subjects everybody already agrees about are deliberately ", after=".",
         answer="left out", hint="Two words. A phrasal verb."),
    dict(before="7. The thing nobody believes until they have run an event is the ", after=".",
         answer="seating", hint="One word."),
    dict(before="8. Two weeks later the organisers ask delegates what they are doing ", after=".",
         answer="differently", hint="One word, an adverb."),
]

# ── 7. LISTENING Part B -- multiple matching, duas tarefas (Paper 3, Part 4) ──
# Cinco vozes diferentes, e nenhuma delas e a sarah_us da pre-class: o aluno nao
# pode chegar na aula tendo ouvido a mesma pessoa dizer as mesmas coisas.
SPEAKERS = [
    dict(n=1, file="a3_cpe_mm_speaker_1.mp3", voice="alice", task1="B", task2="A", text=(
        "People think we build the week around whoever says yes. We do not. We start with one claim, and "
        "then we go looking for the three people who will fight about it properly. By the time the doors "
        "open, the argument has already been had, in our office, in February. What happens on the stage is "
        "a performance of a decision we took months ago.")),
    dict(n=2, file="a3_cpe_mm_speaker_2.mp3", voice="arthur", task1="E", task2="C", text=(
        "I went for eleven years and last year I stopped. Not because it had got worse. Because I added it "
        "up. Three days, the flights, the hotel, the time out of the office, and then I asked myself what "
        "I actually came home with. A view I already held, and two business cards. At that price the "
        "arithmetic simply does not work any more, whatever the corridors are worth.")),
    dict(n=3, file="a3_cpe_mm_speaker_3.mp3", voice="matilda", task1="A", task2="D", text=(
        "Everyone asks what we get out of it and they expect me to talk about leads. Honestly, the content "
        "of the panels is almost irrelevant to us. What we are buying is that our name sits next to those "
        "names for three days. If our chief executive says something entirely unremarkable on the stage, "
        "that is fine. The point was that she was on the stage.")),
    dict(n=4, file="a3_cpe_mm_speaker_4.mp3", voice="george", task1="C", task2="B", text=(
        "I file four pieces a week from these events and almost none of them come out of the sessions. On "
        "the platform people give you the version that has been through their communications team. Then at "
        "eight in the evening somebody finally tells you what is actually happening with the pipeline. The "
        "stage is the press release. The bar is the story.")),
    dict(n=5, file="a3_cpe_mm_speaker_5.mp3", voice="antonio", task1="D", task2="H", text=(
        "I speak at a great many of these, and I am going to say the thing that never goes down well. The "
        "room believes it is where things get decided. It is not. It is where a few hundred people who "
        "broadly agree with one another confirm that they agree, and then describe that as the market "
        "view. The decisions I deal with are taken somewhere else entirely.")),
]
TASK1_OPTS = [
    ("A", "a sponsor's head of marketing"),
    ("B", "a conference organiser"),
    ("C", "a journalist who covers the sector"),
    ("D", "a government official who speaks at these events"),
    ("E", "a delegate who has stopped attending"),
    ("F", "an academic who studies professional networks"),
    ("G", "a venue manager"),
    ("H", "a professional moderator"),
]
TASK2_OPTS = [
    ("A", "What the week is about is settled long before anybody arrives."),
    ("B", "What is said publicly is the safe version; the useful talk happens elsewhere."),
    ("C", "The cost can no longer be justified against what is actually learned."),
    ("D", "Being visible at the event is worth more than anything said at it."),
    ("E", "The same small group sets the agenda year after year."),
    ("F", "Online formats have turned out to be a better substitute than expected."),
    ("G", "Regulation ought to be debated in public rather than in closed sessions."),
    ("H", "The sector overestimates how much its own collective opinion matters."),
]

# ── 8. GRAMATICA -- inversao negativa e limitante ────────────────────────────
# GRAMMAR_ROWS vem do spec (a tabela que a pre-class ja mostra). O que e novo
# aqui e a DISCRIMINACAO: nao como se forma, mas o que a forma faz.
GRAMMAR_QUIZ = [
    ("&ldquo;Not since 2008 has capital been this patient.&rdquo; Compared with &ldquo;Capital has not "
     "been this patient since 2008&rdquo;, the inverted version", [
         ("is more formal but otherwise identical in effect.", False),
         ("puts the time span first, so the room hears the scale before the claim.", True),
         ("is the only grammatically correct order.", False),
         ("suggests the speaker is less certain of the date.", False)]),
    ("&ldquo;Only by fixing the rules can we move the money.&rdquo; The inversion here signals that", [
         ("fixing the rules is one of several options.", False),
         ("fixing the rules is the single condition, and nothing else will do.", True),
         ("the speaker is addressing regulators rather than investors.", False),
         ("the money has already begun to move.", False)]),
    ("A chair opens with &ldquo;Rarely do we have the people who sign and the people who regulate in one "
     "room.&rdquo; The effect of the inversion is to", [
         ("apologise for the composition of the panel.", False),
         ("mark the occasion as unusual before saying what it is.", True),
         ("soften a claim the chair cannot support.", False),
         ("indicate that the session will run over time.", False)]),
    ("Inversion of this kind is <b>least</b> appropriate when", [
         ("opening a keynote in front of four hundred people.", False),
         ("answering a hostile question in a short exchange.", True),
         ("writing the first line of a published comment piece.", False),
         ("introducing the single number a report turns on.", False)]),
    ("&ldquo;Little did the sponsors realise how much had already been agreed.&rdquo; What the form adds "
     "is", [
         ("a judgement that the sponsors should have known.", True),
         ("a statement that the sponsors were formally excluded.", False),
         ("an indication that the agreement was improper.", False),
         ("a suggestion that the sponsors later objected.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="", after=" a programme been built around a single claim.",
         answer="Never before has", alt="Never before had",
         hint="Never before + auxiliary + subject."),
    dict(before="", after=" the room hear what the number is for.",
         answer="Only with a framing device can", alt="Only with a framing device will",
         hint="Only + prepositional phrase + modal + subject."),
    dict(before="", after=" the chair interrupt a speaker mid-answer.",
         answer="Under no circumstances should", alt="Under no circumstances may",
         hint="Under no circumstances + modal + subject."),
    dict(before="", after=" the room understand what the week had been about.",
         answer="Not until the closing session did",
         hint="Not until + time phrase + auxiliary + subject."),
]

# ── 9. SPEAKING & WRITING (Paper 5 / Paper 2) ────────────────────────────────
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> You are opening a session at a regional "
    "infrastructure forum. Answer this: <i>&ldquo;What is this sector no longer allowed to say out "
    "loud?&rdquo;</i> Open with a framing device, pivot once, and land on a question the room can "
    "disagree with. No notes, and no apology at the start."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "You opened with a number. Why that number and not the obvious one?",
    "Say your central claim again, this time with an inversion, and tell me what the inversion bought you.",
    "Somebody in the room has just told you the opposite is true. Concede one thing to them, out loud, "
    "and then hold your position.",
    "If you had thirty seconds instead of two minutes, which sentence survives?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe ele reiniciar. A pergunta 2 e a da gramatica: ele tem de PRODUZIR a "
    "inversao sob pressao e dizer o que ela fez pela frase, que e a diferenca entre saber a forma e usa-la. "
    "Na 3, o que se mede e a concessao, nao a defesa: se ele concede e ja emenda um 'mas', a concessao nao "
    "aconteceu."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> Your organisation has been asked to convene a "
    "closed-door session of twenty people on the region&rsquo;s pipeline. Together, decide: who is in the "
    "room, who is deliberately left out, and what single sentence the session exists to test. You have to "
    "agree on the sentence before the four minutes are up."
)
DEBATE_1_MOTION = (
    "This house believes that industry conferences are a mechanism for manufacturing consensus, not for "
    "testing it."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you have to open with the strongest argument against yourself.",
    "One inversion per turn, at least. If it sounds forced, it was.",
]
DEBATE_2_MOTION = (
    "This house believes that a chair who has an opinion should state it in the opening, rather than "
    "pretending to neutrality."
)
DEBATE_2_RULES = [
    "The teacher gives you the side. You do not choose it.",
    "Before you answer, restate the strongest point the other side has made, in your own words, so that "
    "they accept your version of it.",
    "Only then do you respond. A turn that skips the concession does not count.",
]
DEBATE_2_TEACHER = (
    "Segundo debate (6 min): DE o lado a ele, de preferencia o que ele nao defenderia. O que se mede aqui "
    "nao e argumento, e CONCESSAO: ele tem de reformular o ponto mais forte do outro lado a ponto de o "
    "outro lado aceitar a reformulacao. Se ele reformula uma versao fraca, e straw man, e a rodada nao "
    "conta."
)
WRITING_TASK = (
    "<b>Paper 2, Part 2 &mdash; a proposal, 280 to 320 words, for the next lesson.</b> Your board has "
    "asked whether the organisation should keep sponsoring the regional forum. Write a proposal that "
    "states what the sponsorship is actually for, what would have to be true for it to be worth "
    "continuing, and what you would measure two weeks after the event. Assume the reader is sceptical and "
    "short of time."
)
# Em INGLES: isto aparece na tela compartilhada, e a REGRA 13 proibe portugues
# la. O recado ao professor, em portugues, vai no data-teacher do slide.
WRITING_MODEL = (
    "Three things are being read for. A purpose stated in <b>one</b> sentence. A falsifiable criterion: "
    "what would have to be true for this to be worth continuing. And one measure with a date on it. "
    "Elegance is not being marked. If the proposal could have been written without attending the event, "
    "it has failed."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura -- a estrutura e parte do que se "
    "avalia. Diga so que o leitor e cetico e tem pressa. O reveal em ingles e o criterio; se ele pedir mais, "
    "devolva a pergunta: 'what would have to be true?'."
)
