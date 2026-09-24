#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 6, em formato de prova (CPE)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula6 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)
VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]
VOCAB_CARDS_1 = VOCAB[:5]
VOCAB_CARDS_2 = VOCAB[5:10]

MATCH_OPTS = [
    'the three sentences you keep in a drawer for the day something breaks',
    'the condition that nothing may appear before a stated hour',
    'usable but not attributable to the person who said it',
    'the dull paragraph at the foot that the lawyers fought over',
    'saying what you expect without promising it',
    'the first line, which decides whether anybody reads the second',
]
MATCH_ROWS = [
    ('A holding statement', 'the three sentences you keep in a drawer for the day something breaks'),
    ('An embargo', 'the condition that nothing may appear before a stated hour'),
    ('On background', 'usable but not attributable to the person who said it'),
    ('Boilerplate', 'the dull paragraph at the foot that the lawyers fought over'),
    ('Forward guidance', 'saying what you expect without promising it'),
    ('A lede', 'the first line, which decides whether anybody reads the second'),
]
COLLOC_BANK = ['break an embargo', 'issue a holding statement', 'speak on background',
               'meet disclosure obligations', 'agree a key message', 'bury the lede']
COLLOC_OPTS = ['break', 'issue', 'speak', 'meet', 'agree', 'bury']
COLLOC_ROWS = [
    ('Do it once and those fifteen journalists never trust you again: ____ .', 'break an embargo'),
    ('Something has broken and you are not ready, so you ____ .', 'issue a holding statement'),
    ('You may use this, but not with my name on it: ____ .', 'speak on background'),
    ('Publish promptly and to everybody at once, and you ____ .', 'meet disclosure obligations'),
    ('Before a word is drafted, the room has to ____ .', 'agree a key message'),
    ('Put the news in the fourth line and you ____ .', 'bury the lede'),
]
CLOZE_BANK = ['an embargo', 'a holding statement', 'material information', 'boilerplate',
              'forward guidance', 'a spokesperson', 'a joint statement', 'on the record']
CLOZE_ITEMS = [
    dict(before='1. Three sentences written months in advance and kept in a drawer are ', after='.',
         answer='a holding statement', alt='holding statement', hint='Three words, with the article.'),
    dict(before='2. Anything a reasonable investor would want to know before dealing is ', after='.',
         answer='material information', hint='Two words, no article.'),
    dict(before='3. The dull paragraph at the foot that the lawyers fought over is ', after='.',
         answer='boilerplate', hint='One word, no article.'),
    dict(before='4. Saying what you expect without promising it is ', after='.',
         answer='forward guidance', hint='Two words, no article.'),
    dict(before='5. Nothing may appear before the stated hour, because the material went out under ',
         after='.', answer='an embargo', alt='embargo', hint='Two words, with the article.'),
    dict(before='6. Say it ', after=' and it belongs to whoever wrote it down.',
         answer='on the record', hint='Three words.'),
    dict(before='7. Issued by several parties at once, and five times slower to agree, is ', after='.',
         answer='a joint statement', alt='joint statement', hint='Three words, with the article.'),
]
CLOZE_NOT_NEEDED = 'a spokesperson'

ARTICLE_TITLE = "Everything Leaks, and the Timing Is the Message"
ARTICLE_STANDFIRST = "Adapted from a comment essay on corporate communication &middot; ~600 words"
ARTICLE = [
    ("Every organisation eventually discovers that it does not control when its news becomes public. It "
     "controls, at best, the twenty minutes before.", 1,
     " The instruments built around that gap are older than the internet, and they survive for a reason."),
    ("<b>An embargo</b> is the oldest of them: the material goes out in advance on the condition that "
     "nothing appears before a stated hour. It is held together by nothing except professional habit, "
     "which is precisely why a breach is punished socially rather than legally.", 2, ""),
    ("Below the embargo sit two conventions that outsiders confuse constantly. A remark made "
     "<b>on background</b> may be used but not attributed; a remark made <b>on the record</b> belongs to "
     "whoever wrote it down.", 3,
     " <b>A spokesperson</b> who is unclear about which is in play should not be in the conversation, and "
     "when it goes wrong the fault is almost never the journalist&rsquo;s."),
    ("Then there is the law, which cares nothing for any of this. <b>Disclosure obligations</b> require a "
     "listed company to publish <b>material information</b> &mdash; anything a reasonable investor would "
     "want to know before dealing &mdash; promptly, and to everybody at the same moment.", 4,
     " A selective briefing that would be ordinary practice in a private company is, in a listed one, a "
     "serious matter."),
    ("When something breaks before the organisation is ready, <b>a holding statement</b> buys the "
     "forty-eight hours in which the real one can be written. Where several parties are involved, "
     "<b>a joint statement</b> takes five times as long, because every clause has to survive "
     "<b>stakeholder alignment</b> before anybody outside reads a word of it.", 5, ""),
    ("The craft itself is small and unforgiving. <b>A lede</b> that buries the development in the fourth "
     "line will be rewritten by somebody whose version you will not enjoy. <b>Boilerplate</b> at the foot "
     "is not filler; it is the paragraph the lawyers fought over. <b>Forward guidance</b> has to be "
     "specific enough to be useful and vague enough to survive a bad quarter.", 6, ""),
    ("Underneath all of it sits one test, and it has not changed in thirty years. Before anything goes "
     "out, somebody has to be able to state <b>a key message</b> in a single sentence, out loud, without "
     "the document in front of them. <b>A press statement</b> that fails that test has not been written. "
     "It has been assembled, and it will read like it.", None, ""),
]
GAP_OPTIONS = [
    ('A', 'The distinction is agreed before the sentence is spoken, never afterwards.'),
    ('B', 'The compromise is usually visible in the finished text, and experienced readers go looking for '
          'it.'),
    ('C', 'What it is actually managing, therefore, is not secrecy but sequence.'),
    ('D', 'Most organisations now publish to their own channels as well as through the press.'),
    ('E', 'Lose the trust of the fifteen journalists who matter and no amount of legal drafting will '
          'replace it.'),
    ('F', 'Get that balance wrong in either direction and the next thing you issue is a correction.'),
    ('G', 'The word doing the work there is <i>everybody</i>: the obligation is about equality of access, '
          'not about speed for its own sake.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "G"), ("5", "B"), ("6", "F")]
GAP_KEY = (
    "<b>1 C</b> &mdash; &ldquo;therefore&rdquo; needs the twenty minutes before it, and &ldquo;that "
    "gap&rdquo; in the next sentence needs sequence.<br>"
    "<b>2 E</b> &mdash; &ldquo;punished socially rather than legally&rdquo; is only explained by what the "
    "social punishment costs.<br>"
    "<b>3 A</b> &mdash; two conventions have just been defined; &ldquo;The distinction&rdquo; needs both, "
    "and &ldquo;unclear about which is in play&rdquo; follows from agreeing it beforehand.<br>"
    "<b>4 G</b> &mdash; the sentence quotes a word from the paragraph before it and the sentence after it "
    "contrasts private with listed.<br>"
    "<b>5 B</b> &mdash; &ldquo;stakeholder alignment&rdquo; produces a compromise; nothing else in the "
    "paragraph does.<br>"
    "<b>6 F</b> &mdash; &ldquo;that balance&rdquo; can only point at specific-enough versus "
    "vague-enough.<br>"
    "<b>D</b> is the distractor: true, on topic, and it answers no reference."
)
MCQ = [
    ("What does the writer say an organisation actually controls?", [
        ("Which journalists receive the material first.", False),
        ("The order in which things become known, not whether they become known.", True),
        ("The legal consequences of a breach.", False),
        ("The wording of the first report.", False)]),
    ("Why is a breach of an embargo punished socially rather than legally?", [
        ("The convention has no legal force behind it.", True),
        ("The courts have refused to enforce embargoes.", False),
        ("Legal action would attract more attention to the story.", False),
        ("Most breaches are accidental.", False)]),
    ("Who does the writer blame when background and on the record are confused?", [
        ("The journalist, for failing to check.", False),
        ("Whoever was speaking, for not settling it beforehand.", True),
        ("The organisation&rsquo;s lawyers.", False),
        ("Nobody: the distinction is inherently unclear.", False)]),
    ("What does the writer identify as the point of the disclosure rules?", [
        ("Getting information out as quickly as possible.", False),
        ("Making sure nobody gets it before anybody else.", True),
        ("Preventing selective briefing of regulators.", False),
        ("Protecting the company from later claims.", False)]),
    ("What does the writer say about boilerplate?", [
        ("It can be cut when space is short.", False),
        ("It is the paragraph the lawyers fought over, and it is not filler.", True),
        ("It is the part journalists read first.", False),
        ("It should be rewritten for every release.", False)]),
    ("The distinction drawn in the final paragraph is between a statement that has been", [
        ("approved and one that has been drafted.", False),
        ("written and one that has merely been assembled.", True),
        ("published and one that has been held.", False),
        ("agreed by one party and one agreed by several.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 a</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br><i>Item 2 is the one where the true-and-wrong trap is weakest, which is why it is worth "
    "asking him to justify it: the answer is in the words &ldquo;nothing except professional habit&rdquo;.</i>"
)

WORD_FORMATION = [
    dict(before="A remark made on background is usable but not ", after=". (ATTRIBUTE)",
         answer="attributable", hint="-able adjective from the verb."),
    dict(before="The ", after=" was held until the markets had closed. (ANNOUNCE)",
         answer="announcement", hint="Noun from the verb."),
    dict(before="A ", after=" briefing is ordinary practice until the company lists. (SELECT)",
         answer="selective", hint="Adjective from SELECT."),
    dict(before="The obligation is about ", after=" of access, not about speed. (EQUAL)",
         answer="equality", hint="Abstract noun from the adjective."),
    dict(before="Get the guidance wrong and the next release is a ", after=". (CORRECT)",
         answer="correction", hint="Noun from the verb."),
    dict(before="What is being protected is not the share price but the ", after=". (REPUTE)",
         answer="reputation", hint="Noun. Watch the internal change."),
    dict(before="Disclosure ", after=" do not bend for a bad quarter. (OBLIGE)",
         answer="obligations", hint="Plural noun from the verb."),
    dict(before="", after=", the dullest paragraph is the one that was negotiated hardest. (DELIBERATE)",
         answer="Deliberately", hint="Adverb, capital letter, comma after it."),
]
TRANSFORMATIONS = [
    dict(lead="The statement will be released at noon, as arranged.", key="DUE",
         before="The statement ", after=" at noon.",
         answer="is due to be released", hint="be due to, for a scheduled arrangement."),
    dict(lead="It is a legal requirement for listed companies to disclose material information.",
         key="OBLIGED", before="Listed companies ", after=" material information.",
         answer="are obliged to disclose", hint="be obliged to, for an obligation imposed from outside."),
    dict(lead="The first draft was cautious; the second was not.", key="WHEREAS",
         before="The first draft was cautious, ", after=".",
         answer="whereas the second was not", hint="Formal contrastive linker."),
    dict(lead="Because the embargo is in force, nothing may be published before six.", key="GIVEN",
         before="", after=" nothing may be published before six.",
         answer="Given the embargo,", alt="Given that the embargo is in force,",
         hint="Formal causal linker followed by a noun phrase."),
    dict(lead="The spokesperson was expected to call at four, but did not.", key="MEANT",
         before="The spokesperson ", after=" at four, but did not.",
         answer="was meant to call", hint="be meant to, for an expectation that failed."),
    dict(lead="Publication is permitted only if every party has signed off.", key="PROVIDED",
         before="Publication is permitted ", after=" signed off.",
         answer="provided that every party has", alt="provided every party has",
         hint="provided that, as a formal conditional."),
]
TRANSFORM_KEY = (
    "<b>1</b> is due to be released<br><b>2</b> are obliged to disclose<br>"
    "<b>3</b> whereas the second was not<br><b>4</b> Given the embargo, &middot; Given that the embargo is "
    "in force,<br><b>5</b> was meant to call<br><b>6</b> provided that every party has &middot; provided "
    "every party has<br><i>Items 1, 2 and 5 are the same family: be + to-infinitive. What separates them "
    "is who is imposing the arrangement, and whether it held.</i>"
)

TALK_FILE = "a6_cpe_talk_twenty_minutes.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "I run a wire desk, which means I am usually the first person outside your building to read what you "
    "have written. Let me tell you what happens to it in the first ninety seconds. "
    "Somebody on my desk reads two lines. Two. If the development is in line four because you wanted to "
    "set the context first, they will write the story from line four, and the context you cared about "
    "will not appear anywhere. That is not laziness. It is arithmetic: we handle four hundred of these a "
    "day. "
    "Second thing. Embargoes. We keep them, and I want to be clear about why, because it is not virtue. "
    "We keep them because the day we break one is the day we stop being sent things early, and being sent "
    "things early is the entire business. So an embargo is safe with us and it is worth exactly nothing "
    "if you send it to forty people. "
    "Third, and this is where companies hurt themselves. If you brief one outlet properly and hand "
    "everybody else three sentences, we all know within the hour. The reporter who got the good version "
    "does not protect you. She tells her friends, because that is what having the good version is for. "
    "And the last one. When a statement has been through eleven people, I can tell. Not because the "
    "language is bad, but because no sentence in it commits to anything. The paragraphs are all "
    "load-bearing and none of them carries weight. When that lands on my desk I do not write the story "
    "you sent. I go and find somebody who will say a sentence."
)
TALK_ITEMS = [
    dict(before="1. Somebody on the desk reads ", after=" lines.", answer="two",
         hint="One word, and he says it twice."),
    dict(before="2. The desk handles ", after=" of these a day.", answer="four hundred",
         hint="Two words."),
    dict(before="3. The reason the desk keeps embargoes is not virtue but ", after=".",
         answer="business", alt="the business", hint="One word."),
    dict(before="4. An embargo is worth nothing if you send it to ", after=" people.",
         answer="forty", hint="One word."),
    dict(before="5. If one outlet is briefed properly, everybody knows within ", after=".",
         answer="the hour", alt="an hour", hint="Two words."),
    dict(before="6. The reporter with the good version tells her ", after=".",
         answer="friends", hint="One word."),
    dict(before="7. In a statement that has been through eleven people, no sentence ",
         after=" to anything.", answer="commits", hint="One word."),
    dict(before="8. When that lands on his desk, he goes and finds somebody who will say a ", after=".",
         answer="sentence", hint="One word, and it is the last word of the talk."),
]
SPEAKERS = [
    dict(n=1, file="a6_cpe_mm_speaker_1.mp3", voice="alice", task1="B", task2="D", text=(
        "The hardest part of my job is not writing. It is the meeting before the writing, where eleven "
        "people each add one careful word. Every one of those words is defensible on its own. Put them "
        "together and the sentence promises nothing at all. I have started asking people to say the "
        "sentence out loud before they may change it.")),
    dict(n=2, file="a6_cpe_mm_speaker_2.mp3", voice="arthur", task1="E", task2="A", text=(
        "I have been on the receiving end of a thousand of these. What I want is one line that tells me "
        "what changed. Not the context, not the history, not the chief executive's view of the sector. "
        "What changed, today. If I have to hunt for it, somebody else writes the story and you will not "
        "care for their version.")),
    dict(n=3, file="a6_cpe_mm_speaker_3.mp3", voice="matilda", task1="A", task2="F", text=(
        "People treat my role as the brake on the release, and I understand why. But I am not trying to "
        "make it vaguer. I am trying to make sure that whatever it says, we can still say it in six months "
        "when the quarter has gone badly. Half the corrections I have seen came from guidance that was "
        "perfectly honest and far too precise.")),
    dict(n=4, file="a6_cpe_mm_speaker_4.mp3", voice="george", task1="F", task2="B", text=(
        "We used to give one paper the proper version and everybody else the short one. It felt clever for "
        "about a year. Then it stopped working, because they all talk to each other, and now the short "
        "version is the story: not what we announced, but how we handled it. We give everybody the same "
        "thing at the same minute.")),
    dict(n=5, file="a6_cpe_mm_speaker_5.mp3", voice="antonio", task1="C", task2="H", text=(
        "The rules are not really about speed, whatever people tell you. You can be slow, as long as "
        "everybody is equally informed at the moment you speak. What gets companies into difficulty is "
        "almost never the delay. It is the phone call to one investor the afternoon before.")),
]
TASK1_OPTS = [
    ("A", "a company lawyer"),
    ("B", "a head of communications"),
    ("C", "a market regulator"),
    ("D", "a chief executive"),
    ("E", "a journalist on a news desk"),
    ("F", "an investor relations director"),
    ("G", "a printer of annual reports"),
    ("H", "an academic who studies disclosure"),
]
TASK2_OPTS = [
    ("A", "A statement should open with what has changed and nothing else."),
    ("B", "Treating outlets differently damages you more than the news itself."),
    ("C", "Embargoes no longer serve any real purpose."),
    ("D", "Drafting by committee removes the commitment from every sentence."),
    ("E", "Companies disclose far more than the rules actually require."),
    ("F", "Guidance fails more often by being too precise than by being too vague."),
    ("G", "Regulators should approve statements before they are issued."),
    ("H", "The rules are about equal access, not about speed."),
]
GRAMMAR_QUIZ = [
    ("&ldquo;The board <b>is to</b> meet on Thursday.&rdquo; Compared with &ldquo;will meet&rdquo;, the "
     "form tells the reader that", [
         ("the meeting is less certain than a plain future.", False),
         ("the meeting has been formally arranged by somebody.", True),
         ("the writer disapproves of the meeting.", False),
         ("the date may still change.", False)]),
    ("Which sentence reports an expectation that was <b>not</b> met?", [
         ("The statement had to be released at noon.", False),
         ("The statement was supposed to be released at noon.", True),
         ("The statement is due to be released at noon.", False),
         ("The statement is to be released at noon.", False)]),
    ("&ldquo;Listed companies <b>have to</b> disclose material information.&rdquo; The choice of "
     "<i>have to</i> rather than <i>must</i> signals that", [
         ("the obligation is imposed from outside, not by the writer.", True),
         ("the obligation is weaker than it appears.", False),
         ("the sentence is less formal than it should be.", False),
         ("the rule applies only in some jurisdictions.", False)]),
    ("In a release, which linker commits the writer to a <b>causal</b> claim?", [
         ("Whereas the first draft was cautious, ...", False),
         ("Given the revised guidance, ...", True),
         ("Notwithstanding the revised guidance, ...", False),
         ("As regards the revised guidance, ...", False)]),
    ("&ldquo;The spokesperson <b>was not to comment</b> before noon.&rdquo; This most naturally reports", [
         ("a prediction about what would happen.", False),
         ("an instruction that had been given.", True),
         ("a personal preference.", False),
         ("a legal prohibition.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="The joint statement ", after=" at seven tomorrow morning.",
         answer="is due to be issued", alt="is to be issued",
         hint="be due to / be to: a scheduled arrangement, in the passive."),
    dict(before="The draft ", after=" the lawyers before it went out, and it did not.",
         answer="was supposed to reach", alt="was meant to reach",
         hint="be supposed to / be meant to: an expectation that failed."),
    dict(before="", after=" no comment may be made before the hour named.",
         answer="Given the embargo,", alt="Given that the embargo is in force,",
         hint="Formal causal linker + noun phrase."),
    dict(before="Publication is permitted ", after=" cleared the wording.",
         answer="provided that every party has", alt="provided every party has",
         hint="Formal conditional, not &ldquo;if&rdquo;."),
]
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> Something has gone wrong at your organisation "
    "and the first call has come in. Answer this: <i>&ldquo;What are we saying, and what are we not saying "
    "yet?&rdquo;</i> Give the holding statement out loud, then justify each thing you left out. Use at "
    "least three formal linkers and one <i>be to</i> construction."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "Say your key message again, in one sentence, without the structure around it.",
    "You said something &ldquo;is to&rdquo; happen. Who arranged it, and would you write that down?",
    "A journalist tells you a rival has already been briefed. Respond, on the record.",
    "One sentence: what is the first thing you would put in writing tonight?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe reiniciar. A pergunta 1 e o teste do wire desk -- se ele nao consegue "
    "dizer a mensagem em UMA frase sem a estrutura em volta, a declaracao nao foi escrita, foi montada. A "
    "3 e a mais dura: veja se ele nega, se confirma, ou se produz um non-answer."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> You and your partner are the only two people "
    "available to sign off a holding statement in the next ten minutes. Together, agree the three "
    "sentences. One of you wants a fourth sentence; the other has to decide whether it survives. You have "
    "to agree on the final wording."
)
DEBATE_1_MOTION = (
    "This house believes that a statement which commits to nothing does more damage than saying nothing at "
    "all."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you open with the strongest argument against yourself.",
    "At least two formal linkers per turn, and no &ldquo;however&rdquo; twice.",
]
DEBATE_2_MOTION = (
    "This house believes that forward guidance should be abolished, because precision and honesty pull in "
    "opposite directions."
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
    "<b>Paper 2, Part 2 &mdash; a statement and a note, 280 to 320 words, for the next lesson.</b> Write "
    "the holding statement your organisation would issue if a project you are responsible for were "
    "suspended tomorrow. Then, underneath it, write the short note to your chief executive explaining what "
    "you deliberately left out and when you would say it."
)
WRITING_MODEL = (
    "Three things are being read for. A first line that says what has happened, not what the organisation "
    "feels. A visible decision about what is being withheld, with a date attached to it. And a statement "
    "short enough that somebody could read it aloud from memory. A holding statement that reads like a "
    "press release has failed at its only job, which is to buy time without spending credibility."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura. Se ele pedir mais, devolva a "
    "pergunta: 'what would you refuse to say tonight, and when will you say it?'."
)
ROLEPLAY_SCENARIO = (
    "Your teacher is a journalist on a wire desk who has forty seconds for you and four hundred stories "
    "today. A project of yours has been suspended. You have two minutes to give her something she can file "
    "without inventing the missing half."
)
ROLEPLAY_CHIPS = ['a holding statement', 'a key message', 'on background', 'material information',
                  'the statement is due to', 'given the circumstances']
ROLEPLAY_TEACHER = (
    "Role-play guiado (4 min): voce e a jornalista, impaciente e sem grosseria. Interrompa na primeira "
    "frase que nao disser o que mudou. Cronometre os dois minutos. Degrau GUIADO, com chips na tela; o "
    "long turn a seguir e o mesmo conteudo sem apoio nenhum."
)
