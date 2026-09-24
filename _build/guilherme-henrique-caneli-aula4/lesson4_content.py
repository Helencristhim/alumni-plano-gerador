#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo do deck IN CLASS da Aula 4, em formato de prova (CPE).

Mesmas duas travas da aula 3: nada aqui pode aparecer na PRE-CLASS desta aula
(ela ja foi refeita e tem texto, compreensao, word formation, transformations e
listen+choose proprios), e o lexico e o grammar_point sao do specs/aula4.py, que
continua sendo o dono deles.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'guilherme-henrique-caneli', 'specs'))
import aula4 as SPEC  # noqa: E402

L = next(v for k, v in vars(SPEC).items() if isinstance(v, dict) and 'pc' in v)

VOCAB = [(v['word'], v['def'], v['ex']) for v in L['vocab']]
SPEECH_PHRASES = L['survival']
GRAMMAR_ROWS = [(a, b, c) for a, b, c in L['grammar']['rule_rows']]
VOCAB_CARDS_1 = VOCAB[:5]
VOCAB_CARDS_2 = VOCAB[5:10]

MATCH_OPTS = [
    'the obligation that only becomes real if something specific happens',
    'the event nobody could have prevented, and it is narrower than people think',
    'the protection that lets old contracts continue under the old rules',
    'the claim the operator files when the arithmetic has been broken from outside',
    'the failure serious enough to let the other side act',
    'the power an official has to decide how a rule is applied',
]
MATCH_ROWS = [
    ('A contingent liability', 'the obligation that only becomes real if something specific happens'),
    ('Force majeure', 'the event nobody could have prevented, and it is narrower than people think'),
    ('A grandfathering clause', 'the protection that lets old contracts continue under the old rules'),
    ('A rebalancing claim', 'the claim the operator files when the arithmetic has been broken from outside'),
    ('A material breach', 'the failure serious enough to let the other side act'),
    ('Administrative discretion', 'the power an official has to decide how a rule is applied'),
]

COLLOC_BANK = ['file a rebalancing claim', 'trigger a step-in right', 'run a public consultation',
               'carry out due diligence', 'declare force majeure', 'breach a material obligation']
COLLOC_OPTS = ['file', 'trigger', 'run', 'carry', 'declare', 'breach']
COLLOC_ROWS = [
    ('The operator has thirty days to ____ .', 'file a rebalancing claim'),
    ('Only a sustained default will ____ .', 'trigger a step-in right'),
    ('The agency is required to ____ before it issues the licence.', 'run a public consultation'),
    ('No lender will sign before its advisers ____ .', 'carry out due diligence'),
    ('You cannot ____ for something you could have foreseen.', 'declare force majeure'),
    ('To ____ is not the same as to miss a deadline.', 'breach a material obligation'),
]

CLOZE_BANK = ['a regulatory sandbox', 'a tariff review', 'a fiscal framework', 'environmental licensing',
              'a termination payment', 'a step-in right', 'due diligence', 'a public consultation']
CLOZE_ITEMS = [
    dict(before='1. The ceiling on how many contingent obligations a government may carry at once belongs '
                'in ', after='.', answer='a fiscal framework', alt='fiscal framework',
         hint='Three words, with the article.'),
    dict(before='2. When the state ends the contract for reasons of its own, what it owes is ',
         after=', and the formula was agreed years earlier.',
         answer='a termination payment', alt='termination payment', hint='Three words, with the article.'),
    dict(before='3. A defined space where a few operators may test something under relaxed conditions is ',
         after='.', answer='a regulatory sandbox', alt='regulatory sandbox',
         hint='Three words, with the article.'),
    dict(before='4. If the concessionaire fails badly enough, the authority may exercise ',
         after=' and operate the asset itself.',
         answer='a step-in right', alt='step-in right', hint='Three words, with the article.'),
    dict(before='5. The slowest part of the timetable is almost always ', after='.',
         answer='environmental licensing', hint='Two words. Nothing to do with the tariff.'),
    dict(before='6. The price the operator may charge is recalculated at ', after='.',
         answer='a tariff review', alt='tariff review', hint='Three words, with the article.'),
    dict(before='7. No lender signs before its advisers have finished ', after='.',
         answer='due diligence', hint='Two words, no article.'),
]
CLOZE_NOT_NEEDED = 'a public consultation'

ARTICLE_TITLE = "The Clause Nobody Reads Until It Matters"
ARTICLE_STANDFIRST = "Adapted from a comment essay on regulated infrastructure &middot; ~600 words"
ARTICLE = [
    ("Every long contract contains a paragraph that nobody reads at signing and everybody reads at three "
     "in the morning four years later. In regulated infrastructure that paragraph is usually the one "
     "governing what happens when the arrangement stops working.", 1,
     " The signature is the easy part; the machinery for unwinding it is where the money actually sits."),

    ("Begin with the asymmetry. A state can change the rules and an operator cannot, and every instrument "
     "in this field exists to price that fact rather than to abolish it. <b>A grandfathering clause</b> "
     "protects contracts signed under the old regime; <b>a rebalancing claim</b> is the route back to the "
     "original arithmetic when something outside the operator&rsquo;s control has broken it.", 2, ""),

    ("It matters enormously how narrowly those doors are drawn. <b>Force majeure</b> is the narrowest of "
     "them, and it is routinely misunderstood: it covers what nobody could have prevented, not what "
     "nobody happened to expect.", 3,
     " A currency collapse is foreseeable in the sense that everybody knows it can happen, and that is "
     "usually enough to keep it outside the clause."),

    ("The state has instruments of its own. <b>A step-in right</b> lets the authority take over operation "
     "when the concessionaire has committed <b>a material breach</b> &mdash; a failure serious enough to "
     "justify it, and the definition of serious enough is negotiated line by line.", 4,
     " Neither side expects to use these provisions, which is exactly why they are drafted carelessly more "
     "often than they should be."),

    ("Off the balance sheet, the picture is quieter and larger. <b>A contingent liability</b> only becomes "
     "real if a specified event occurs, which makes it attractive to a finance ministry and dangerous to a "
     "country.", 5,
     " Where a serious <b>fiscal framework</b> exists, it caps the total the state may carry, and the cap "
     "is the only thing standing between a guarantee programme and a fiscal event."),

    ("Procedure carries more weight here than outsiders expect. <b>Environmental licensing</b> takes as "
     "long as it takes, and <b>a public consultation</b> that changes nothing must still be conducted "
     "properly.", 6,
     " Newer rules increasingly arrive through <b>a regulatory sandbox</b>, which lets the regulator watch "
     "a few operators before it writes anything binding."),

    ("What survives all of it is the oldest question in the field, and it is not a legal question. Read the "
     "verbs. A contract in which the regulator <i>shall</i> publish within sixty days is a different asset "
     "from one in which it <i>may</i> publish in due course, and no amount of <b>due diligence</b> repairs "
     "the second. Where the drafting leaves room for <b>administrative discretion</b>, somebody will "
     "eventually exercise it, and their incentives will not be yours. That is not cynicism. It is the "
     "price of the paragraph nobody read.", None, ""),
]
GAP_OPTIONS = [
    ('A', 'The distinction is not academic: it decides who absorbs a loss that has already happened.'),
    ('B', 'Governments like it for the same reason auditors dislike it, which is that it does not appear '
          'anywhere until it does.'),
    ('C', 'What a lender is really buying, in other words, is not the asset but the rules around it.'),
    ('D', 'Most disputes in the sector are settled privately, and the terms are almost never published.'),
    ('E', 'Neither instrument gives the operator a veto; both give it a route back to a number.'),
    ('F', 'A badly run consultation is the commonest reason a licence is later set aside by a court.'),
    ('G', 'The result is a clause that both parties sign in the belief that it will never be read.'),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "G"), ("5", "B"), ("6", "F")]
GAP_KEY = (
    "<b>1 C</b> &mdash; &ldquo;in other words&rdquo; restates the paragraph, and &ldquo;the rules around "
    "it&rdquo; is what the next sentence calls &ldquo;the machinery&rdquo;.<br>"
    "<b>2 E</b> &mdash; two instruments have just been named; &ldquo;Neither instrument&rdquo; needs both "
    "of them immediately before it.<br>"
    "<b>3 A</b> &mdash; &ldquo;The distinction&rdquo; points back to prevented versus expected, and the "
    "currency example that follows is the illustration.<br>"
    "<b>4 G</b> &mdash; &ldquo;Neither side expects to use these provisions&rdquo; only makes sense after "
    "a sentence that says they sign believing it will never be read.<br>"
    "<b>5 B</b> &mdash; &ldquo;attractive to a ministry and dangerous to a country&rdquo; is exactly what "
    "B expands, and &ldquo;Where a serious fiscal framework exists&rdquo; answers it.<br>"
    "<b>6 F</b> &mdash; &ldquo;must still be conducted properly&rdquo; needs the consequence of not doing "
    "so.<br>"
    "<b>D</b> is the distractor: true, on topic, and it answers no reference and completes no argument."
)

MCQ = [
    ("The writer opens with the paragraph read &ldquo;at three in the morning four years later&rdquo; in "
     "order to", [
         ("criticise lawyers for the length of their contracts.", False),
         ("locate the value of the contract in the part nobody negotiates hard.", True),
         ("explain why disputes take so long to resolve.", False),
         ("suggest that signing ceremonies are largely symbolic.", False)]),
    ("According to the second paragraph, what do these instruments do about the asymmetry between state "
     "and operator?", [
         ("They remove it, by binding the state to the original terms.", False),
         ("They price it, rather than attempt to abolish it.", True),
         ("They transfer it to the lenders.", False),
         ("They make it a matter for the courts.", False)]),
    ("What point is the writer making with the currency example?", [
         ("Currency risk should always be hedged.", False),
         ("Force majeure turns on what could have been prevented, not on what was expected.", True),
         ("Emerging markets are uninsurable.", False),
         ("Lenders underestimate how often currencies collapse.", False)]),
    ("Why does the writer say these provisions are drafted carelessly?", [
         ("Because they are usually copied from other contracts.", False),
         ("Because neither side expects them ever to be used.", True),
         ("Because regulators refuse to negotiate them.", False),
         ("Because they are agreed at the very end of the process.", False)]),
    ("What does the writer identify as the value of a fiscal framework?", [
         ("It makes contingent liabilities appear in the accounts.", False),
         ("It caps the total the state may carry, which is what prevents a fiscal event.", True),
         ("It requires every guarantee to be approved in public.", False),
         ("It transfers the liability to the operator.", False)]),
    ("In the final paragraph, the writer&rsquo;s advice amounts to", [
         ("avoiding jurisdictions where officials have discretion.", False),
         ("reading the contract for what is obligatory rather than for what is promised.", True),
         ("commissioning more thorough due diligence.", False),
         ("negotiating the termination clause before anything else.", False)]),
]
MCQ_KEY = (
    "<b>1 b</b> &middot; <b>2 b</b> &middot; <b>3 b</b> &middot; <b>4 b</b> &middot; <b>5 b</b> &middot; "
    "<b>6 b</b><br><i>Item 6 is the trap: (d) is excellent advice and is NOT what the paragraph says. The "
    "paragraph is about the verbs.</i>"
)

# ── USE OF ENGLISH ───────────────────────────────────────────────────────────
# Itens diferentes dos da pre-class (ENFORCE, DISCREET, FIND, REGRET, PROTECT,
# CLASSIFY, MEANING). Nenhuma dessas raizes volta aqui.
WORD_FORMATION = [
    dict(before="The operator's ", after=" with the reporting rules was never in doubt. (COMPLY)",
         answer="compliance", hint="Noun from the verb."),
    dict(before="Contingent ", after=" do not appear anywhere until they do. (LIABLE)",
         answer="liabilities", hint="Plural noun from the adjective."),
    dict(before="The step-in was legally ", after=" and commercially catastrophic. (JUSTIFY)",
         answer="justifiable", hint="-able adjective. Watch the internal change."),
    dict(before="A currency collapse is ", after=", which is why it sits outside the clause. (FORESEE)",
         answer="foreseeable", hint="-able adjective from the verb."),
    dict(before="The dispute went to ", after=" rather than to court. (ARBITRATE)",
         answer="arbitration", hint="Noun from the verb."),
    dict(before="The agency was praised, unusually, for its ", after=". (TRANSPARENT)",
         answer="transparency", hint="Abstract noun from the adjective."),
    dict(before="The ", after=" of &ldquo;material&rdquo; is where the whole argument lives. (DEFINE)",
         answer="definition", hint="Noun from the verb."),
    dict(before="", after=", the consultation changed nothing at all. (EXPECT)",
         answer="Unexpectedly", hint="Negative prefix + adverb, capital letter, comma after it."),
]

# Palavras-chave DIFERENTES das da pre-class (RULED, ADVISED, INSISTED,
# APOLOGISED, ANNOUNCED, WARNED), na mesma gramatica: discurso indireto e verbos
# de relato na comunicacao regulatoria.
TRANSFORMATIONS = [
    dict(lead="&ldquo;It was not our decision.&rdquo; (the operator)", key="DENIED",
         before="The operator ", after=" their decision.",
         answer="denied that it had been", alt="denied it had been",
         hint="deny + that clause, with backshift."),
    dict(lead="&ldquo;Yes, we missed the filing deadline.&rdquo; (the director)", key="ADMITTED",
         before="The director ", after=" the filing deadline.",
         answer="admitted to missing", alt="admitted missing",
         hint="admit to + -ing."),
    dict(lead="&ldquo;You really must publish the methodology.&rdquo; (the adviser)", key="URGED",
         before="The adviser ", after=" the methodology.",
         answer="urged them to publish", alt="urged us to publish",
         hint="urge + object + to + infinitive."),
    dict(lead="&ldquo;The ministry leaked the draft.&rdquo; (the consortium)", key="ACCUSED",
         before="The consortium ", after=" the draft.",
         answer="accused the ministry of leaking",
         hint="accuse + object + of + -ing."),
    dict(lead="&ldquo;No, I will not comment on an open case.&rdquo; (the spokesperson)", key="REFUSED",
         before="The spokesperson ", after=" an open case.",
         answer="refused to comment on",
         hint="refuse + to + infinitive."),
    dict(lead="&ldquo;Why not run the consultation online?&rdquo; (the regulator)", key="SUGGESTED",
         before="The regulator ", after=" the consultation online.",
         answer="suggested running", alt="suggested that they run",
         hint="suggest + -ing. Never &ldquo;suggested to run&rdquo;."),
]
TRANSFORM_KEY = (
    "<b>1</b> denied that it had been &middot; denied it had been<br>"
    "<b>2</b> admitted to missing &middot; admitted missing<br>"
    "<b>3</b> urged them to publish &middot; urged us to publish<br>"
    "<b>4</b> accused the ministry of leaking<br>"
    "<b>5</b> refused to comment on<br>"
    "<b>6</b> suggested running &middot; suggested that they run<br>"
    "<i>Item 6 is the one that catches fluent speakers: SUGGEST never takes an infinitive.</i>"
)

# ── LISTENING ────────────────────────────────────────────────────────────────
TALK_FILE = "a4_cpe_talk_what_the_file_says.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "I spent nineteen years on the other side of this table, at the agency, and then I crossed over. So "
    "let me tell you what an official is actually doing when you meet one. "
    "First, understand what is on the file. Everything I said to you in that meeting will be written down "
    "by somebody, and in three years a different person will read that note without me in the room. So I "
    "do not say we will approve it. I say the application appears to meet the criteria. You hear "
    "encouragement. What is on the file is a description. "
    "Second, deadlines. Where the statute says sixty days, it means sixty days from a complete "
    "application, and the word doing the work there is complete. The clock does not start when you file. "
    "It starts when we stop asking for things, and we decide when that is. "
    "Third, and this is the one that costs money, consultations. People treat them as theatre. They are "
    "not. A consultation that is run badly is the single commonest reason a licence gets struck down "
    "afterwards, and it is struck down on procedure, not on the merits. You can win every argument and "
    "still lose the licence. "
    "The last thing is about discretion. Everybody wants a rule with no discretion in it. You do not, "
    "actually. A rule with no discretion cannot be applied to a project nobody imagined when it was "
    "written, and your project is always the one nobody imagined. What you want is discretion that is "
    "exercised in writing, with reasons. Reasons can be challenged. Silence cannot."
)
TALK_ITEMS = [
    dict(before="1. Everything said in the meeting is read later by somebody with the speaker ",
         after=".", answer="not in the room", alt="out of the room",
         hint="Four words. He says it almost in passing."),
    dict(before="2. Instead of promising approval, an official says the application appears to meet the ",
         after=".", answer="criteria", hint="One word."),
    dict(before="3. What the official puts on the file is not encouragement but a ", after=".",
         answer="description", hint="One word."),
    dict(before="4. The sixty days run from a ", after=" application.",
         answer="complete", hint="One word. He says it is the word doing the work."),
    dict(before="5. A licence struck down after a bad consultation is struck down on ", after=".",
         answer="procedure", hint="One word. Not 'the merits'."),
    dict(before="6. You can win every argument and still lose the ", after=".",
         answer="licence", alt="license", hint="One word."),
    dict(before="7. A rule with no discretion cannot be applied to a project ",
         after=" when it was written.", answer="nobody imagined",
         hint="Two words, and he repeats them in the next sentence."),
    dict(before="8. What you want is discretion exercised in writing, with ", after=".",
         answer="reasons", hint="One word, and it is the last word of the talk but one."),
]

SPEAKERS = [
    dict(n=1, file="a4_cpe_mm_speaker_1.mp3", voice="alice", task1="C", task2="B", text=(
        "My job is to say no early. Everyone here thinks legal exists to paper the deal after it is agreed, "
        "and by then it is far too late. The clause that will cost us in year seven is negotiated in week "
        "two, usually by somebody who wants the announcement more than the contract. I have started going "
        "to the commercial meetings uninvited.")),
    dict(n=2, file="a4_cpe_mm_speaker_2.mp3", voice="arthur", task1="F", task2="E", text=(
        "People assume we are slow because we are obstructive. We are slow because if I sign this and the "
        "process was defective, it is my name on the decision and a court will say so in public. I am not "
        "protecting the department. I am protecting the licence, which is the thing the applicant actually "
        "wants, whether or not they can see that in month four.")),
    dict(n=3, file="a4_cpe_mm_speaker_3.mp3", voice="matilda", task1="A", task2="D", text=(
        "We do not lend against assets and we never have. We lend against a set of promises made by parties "
        "with different abilities to keep them. So the only question that matters on my credit paper is "
        "which of those promises survives a change of government. Everything else, the engineering, the "
        "traffic, the tariff, is detail underneath that one question.")),
    dict(n=4, file="a4_cpe_mm_speaker_4.mp3", voice="george", task1="D", task2="A", text=(
        "What comes before me is almost never a disagreement about facts. Both sides know what happened. "
        "They are arguing about what the words in clause 34 were supposed to cover, and very often nobody "
        "in the room was present when clause 34 was written. I decide these cases on the drafting, because "
        "the drafting is all I am given.")),
    dict(n=5, file="a4_cpe_mm_speaker_5.mp3", voice="antonio", task1="E", task2="H", text=(
        "We put in a forty-page response and the licence was granted anyway, which everyone tells me proves "
        "the process is a formality. I disagree. Twelve of our points are now conditions on that licence. "
        "Nobody reported that, because it is not a story. But the road will be built differently because we "
        "turned up.")),
]
TASK1_OPTS = [
    ("A", "a lender's credit officer"),
    ("B", "a minister responsible for infrastructure"),
    ("C", "an operator's general counsel"),
    ("D", "an arbitrator"),
    ("E", "a campaigner who takes part in consultations"),
    ("F", "a civil servant in a licensing agency"),
    ("G", "an engineer on a concession project"),
    ("H", "a financial journalist"),
]
TASK2_OPTS = [
    ("A", "Disputes are settled on the drafting, not on the facts."),
    ("B", "The expensive terms are agreed long before the lawyers are asked."),
    ("C", "Regulators should publish the reasons for every decision they take."),
    ("D", "What is being financed is a set of promises, not a physical asset."),
    ("E", "Delay protects the decision from being overturned later."),
    ("F", "Consultations are a formality that ought to be abolished."),
    ("G", "Foreign operators are treated more harshly than domestic ones."),
    ("H", "Taking part changes the outcome even when the decision goes against you."),
]

# ── GRAMATICA ────────────────────────────────────────────────────────────────
GRAMMAR_QUIZ = [
    ("&ldquo;The minister <b>indicated</b> that the government had no current intention of revisiting the "
     "framework.&rdquo; Compared with &ldquo;promised&rdquo;, the choice of <i>indicated</i>", [
         ("is simply a more formal register for the same act.", False),
         ("records a signal rather than a commitment, and can be withdrawn.", True),
         ("suggests the minister was speaking off the record.", False),
         ("means the statement was made in writing.", False)]),
    ("Which of these reports the speaker as having <b>accepted fault</b>?", [
         ("The director explained that the deadline had been missed.", False),
         ("The director admitted to missing the deadline.", True),
         ("The director confirmed that the deadline had passed.", False),
         ("The director noted that the deadline was no longer relevant.", False)]),
    ("&ldquo;The agency <b>maintained</b> that the consultation had been properly run.&rdquo; The reporting "
     "verb tells the reader that", [
         ("the agency is correct.", False),
         ("the position was held against challenge, and the writer is not endorsing it.", True),
         ("the agency said this more than once.", False),
         ("the statement was made under oath.", False)]),
    ("In a board paper, which sentence commits the writer to the least?", [
         ("Counsel advised that the clause is unenforceable.", False),
         ("Counsel suggested that the clause may be unenforceable.", True),
         ("Counsel confirmed that the clause is unenforceable.", False),
         ("Counsel warned that the clause is unenforceable.", False)]),
    ("&ldquo;We were <b>given to understand</b> that the tariff would be revised.&rdquo; The construction "
     "is doing which job?", [
         ("Naming the source of the information precisely.", False),
         ("Reporting an impression while deleting whoever created it.", True),
         ("Indicating that the information was written down.", False),
         ("Showing that the speaker disagrees with the revision.", False)]),
]
GRAMMAR_PRODUCTION = [
    dict(before="The consortium ", after=" the draft to the press.",
         answer="accused the ministry of leaking",
         hint="accuse + object + of + -ing. Name the party."),
    dict(before="Counsel ", after=" before the board had seen the figures.",
         answer="advised us not to sign", alt="advised them not to sign",
         hint="advise + object + not to + infinitive."),
    dict(before="The regulator ", after=" the methodology alongside the decision.",
         answer="agreed to publish", alt="undertook to publish",
         hint="A reporting verb + to + infinitive, for a commitment given."),
    dict(before="Nothing in the minute says who ", after=" in the first place.",
         answer="raised the concern", alt="raised the concerns",
         hint="Active, with the agent named. This is the repair, not the problem."),
]

# ── SPEAKING & WRITING ───────────────────────────────────────────────────────
LONG_TURN = (
    "<b>Long turn &mdash; two minutes, uninterrupted.</b> You are briefing an investment committee that "
    "does not know this jurisdiction. Answer this: <i>&ldquo;What in this contract is a promise, and what "
    "is only a hope?&rdquo;</i> Take a real agreement you have read. Report what was said using at least "
    "four different reporting verbs, and be explicit about which of them commit anybody."
)
FOLLOW_UP_INTRO = (
    "Four examiner questions, straight after the two minutes. No restarting, and no preparation between "
    "them."
)
FOLLOW_UP = [
    "You used the word &ldquo;assured&rdquo;. Who assured whom, and in what form?",
    "Report the same undertaking twice: once so that it binds, and once so that it does not.",
    "Somebody on the committee says you are being pessimistic. Concede one thing, then hold the rest.",
    "One sentence: what would have to change in the drafting for your answer to change?",
]
FOLLOW_UP_TEACHER = (
    "Follow-up (4 min): nao deixe reiniciar. A pergunta 2 e a da gramatica -- ele tem de produzir a MESMA "
    "informacao com dois verbos de relato de forca diferente, sob pressao. Na 3, o que se mede e a "
    "concessao: se ele concede e emenda um 'mas' na mesma respiracao, a concessao nao aconteceu."
)
COLLAB_TASK = (
    "<b>Collaborative task &mdash; four minutes.</b> A ministry has offered your consortium a concession "
    "with a generous tariff and wide administrative discretion over how it is reviewed. Together, decide "
    "the single change you would demand before signing, and agree which of you takes that demand to the "
    "ministry and how it is phrased. You have to agree on the wording."
)
DEBATE_1_MOTION = (
    "This house believes that discretion in a regulator is worth more to an investor than certainty."
)
DEBATE_1_RULES = [
    "Ninety seconds each, alternating. No notes.",
    "You choose your side, and you open with the strongest argument against yourself.",
    "Every claim you attribute to somebody must carry a reporting verb that fits its strength.",
]
DEBATE_2_MOTION = (
    "This house believes that a public consultation which changes nothing is still worth running."
)
DEBATE_2_RULES = [
    "The teacher gives you the side. You do not choose it.",
    "Before you answer, restate the strongest point the other side has made, in your own words, so that "
    "they accept your version of it.",
    "Only then do you respond. A turn that skips the concession does not count.",
]
DEBATE_2_TEACHER = (
    "Segundo debate (6 min): DE o lado a ele, de preferencia o que ele nao defenderia. O que se mede e "
    "CONCESSAO: ele tem de reformular o ponto mais forte do outro lado a ponto de o outro lado aceitar a "
    "reformulacao. Se ele reformula uma versao fraca, e straw man, e a rodada nao conta."
)
WRITING_TASK = (
    "<b>Paper 2, Part 2 &mdash; a report, 280 to 320 words, for the next lesson.</b> Your committee has "
    "asked for a one-page note on a jurisdiction you know. Report what the authorities have said about "
    "future tariff treatment, distinguishing clearly between what was undertaken and what was merely "
    "indicated, and state what you would need in writing before recommending the investment."
)
WRITING_MODEL = (
    "Three things are being read for. Reporting verbs chosen for their <b>strength</b>, not for variety. "
    "A clear line between what binds and what does not. And one concrete request: what, in writing, would "
    "change your recommendation. A note that reports everything as though it were equally firm has failed, "
    "however well it is written."
)
WRITING_TEACHER = (
    "Writing (2 min): leia a tarefa em voz alta e pare. NAO de estrutura. O criterio em ingles esta no "
    "reveal; se ele pedir mais, devolva a pergunta: 'which of these actually binds anybody?'."
)

# ── ROLE-PLAY GUIADO ─────────────────────────────────────────────────────────
# Exigido pelo contrato do framework (imersivo-prototipo@1) e cobrado pelo
# GATE 16, que so roda no servidor.
ROLEPLAY_SCENARIO = (
    "Your teacher is a member of an investment committee who has never worked in this jurisdiction. You "
    "have two minutes to report what the regulator has told you about the next tariff review, making "
    "clear which parts of it would survive a change of government."
)
ROLEPLAY_CHIPS = ['a tariff review', 'administrative discretion', 'we were given to understand',
                  'the agency undertook to', 'the minister indicated that', 'nothing in writing']
ROLEPLAY_TEACHER = (
    "Role-play guiado (4 min): voce e a integrante do comite, e interrompe UMA vez, com a pergunta que "
    "importa: 'is that an undertaking or an impression?'. Cronometre os dois minutos. Este e o degrau "
    "GUIADO, com chips na tela; o long turn a seguir e o mesmo conteudo sem apoio nenhum."
)
