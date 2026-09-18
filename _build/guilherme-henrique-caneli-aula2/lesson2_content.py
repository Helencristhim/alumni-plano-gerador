#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo da Aula 2 -- The Language of Capital -- no formato de prova (CPE).

O LEXICO E A GRAMATICA NAO MUDARAM: sao os mesmos 14 termos e o mesmo
grammar_point (causative have/get x passiva) do programa, porque o audio, a
escada de nivel e as aulas vizinhas dependem deles. O que mudou e a TAREFA.
"""

# ── 1. Vocabulario: os 14 termos do programa ──────────────────────────────────
# A palavra e a CHAVE do audioMap (pc2_*.mp3) -- nao pode ser reescrita.
VOCAB = [
    ("A risk-adjusted return",
     "what an investment earns once the chance of not earning it has been priced in",
     "On a risk-adjusted return, the brownfield road beats the new port."),
    ("A leverage ratio",
     "the proportion of a project paid for with debt rather than with the sponsor's own money",
     "At a leverage ratio of seventy to thirty, a single bad year eats the equity."),
    ("Subordinated debt",
     "a loan that ranks behind the senior lenders and is repaid only once they are whole",
     "The subordinated tranche charges twelve percent for the privilege of waiting."),
    ("An equity stake",
     "an ownership share, which absorbs the losses first and collects the upside last",
     "The fund took a twenty-five percent equity stake and a seat on the board."),
    ("Blended finance",
     "the deliberate use of public or concessional money to make a deal acceptable to private investors",
     "Blended finance is measured by how much private capital it crowds in, not by how much public money it spends."),
    ("A de-risking mechanism",
     "any instrument that moves a specific danger onto a party better placed to carry it",
     "The partial guarantee was the de-risking mechanism that got the deal past the committee."),
    ("An off-take agreement",
     "a long contract under which a buyer commits in advance to purchase what the asset will produce",
     "With a twenty-year off-take agreement, the revenue exists before the plant does."),
    ("Credit enhancement",
     "anything added to a deal to improve its rating, and so the price at which it can borrow",
     "Credit enhancement moved the bond two notches and took eighty basis points off the coupon."),
    ("Concessional lending",
     "money lent below market terms, usually by a development bank, to bring private capital in behind it",
     "Concessional lending took the first five years, which is precisely the period the funds refuse."),
    ("Yield compression",
     "the fall in returns that follows when too much capital pursues the same scarce assets",
     "Yield compression has left the safe road earning less than it did a decade ago."),
    ("Fiduciary duty",
     "the obligation to act in the interest of the people whose money is being managed, not one's own",
     "Her fiduciary duty is owed to a schoolteacher who will retire in 2050."),
    ("Capital deployment",
     "the act of actually putting committed money to work, as opposed to having raised it",
     "The fund's problem is not fundraising but capital deployment: the pipeline is thin."),
    ("A currency hedge",
     "a contract that fixes the exchange rate, so a good year on the asset is not lost on the rate",
     "Without a currency hedge, a strong dollar can erase the whole return."),
    ("An anchor investor",
     "the first large commitment, whose signature makes it possible for other committees to say yes",
     "The other funds are waiting for an anchor investor to go in first."),
]

# ── 2. Matching que DISCRIMINA (nao e a definicao do card de volta) ───────────
MATCH_OPTS = [
    "ranks behind another lender and is paid only once that lender is whole",
    "makes an existing obligation cheaper to borrow against by improving how it is rated",
    "moves one specific danger onto a party better placed to carry it",
    "lends on terms deliberately worse than the market would give, in order to attract others",
    "returns fall because demand for the asset rose, not because the asset got worse",
    "the obligation that makes the safer option compulsory rather than merely sensible",
    "the commitment whose function is to make the next commitment defensible",
    "money that has stopped being a promise and started being spent",
]
MATCH_ROWS = [
    ("Subordinated debt", MATCH_OPTS[0]),
    ("Credit enhancement", MATCH_OPTS[1]),
    ("A de-risking mechanism", MATCH_OPTS[2]),
    ("Concessional lending", MATCH_OPTS[3]),
    ("Yield compression", MATCH_OPTS[4]),
    ("Fiduciary duty", MATCH_OPTS[5]),
    ("An anchor investor", MATCH_OPTS[6]),
    ("Capital deployment", MATCH_OPTS[7]),
]

# ── 3. Collocation bank + precisao de colocacao ───────────────────────────────
COLLOC_BANK = [
    "to <b>rank</b> behind the senior lenders",
    "to <b>take</b> the first loss",
    "to <b>crowd in</b> private capital",
    "a <b>bankable</b> project &middot; its <b>bankability</b>",
    "to <b>wrap</b> a bond with a guarantee",
    "yields <b>compressed</b> to single digits",
    "capital <b>committed</b> but not yet <b>deployed</b>",
    "to <b>ring-fence</b> the revenue",
    "a duty <b>owed to</b> the members",
    "to <b>sit</b> at the top of the waterfall",
]
COLLOC_OPTS = [
    "rank behind the senior lenders",
    "take the first loss",
    "crowd in private capital",
    "wrap the bond with a guarantee",
    "ring-fence the revenue",
    "compress the yields to single digits",
]
COLLOC_ROWS = [
    ("A first-loss guarantee exists to ___", "crowd in private capital"),
    ("The subordinated tranche will ___", "rank behind the senior lenders"),
    ("The lawyers will ___, so that it cannot be diverted to the parent company.",
     "ring-fence the revenue"),
    ("The monoline agreed to ___", "wrap the bond with a guarantee"),
    ("Somebody has to ___, or the pension funds will not come at all.", "take the first loss"),
    ("Too much money chasing the same operating roads will ___", "compress the yields to single digits"),
]

# ── 4. Cloze com um item a mais (o banco inteiro em cada lacuna) ──────────────
CLOZE_BANK = [
    "an off-take agreement", "credit enhancement", "concessional lending",
    "blended finance", "a currency hedge", "an anchor investor",
    "yield compression", "fiduciary duty", "capital deployment",
]
CLOZE_ITEMS = [
    dict(before='1. A fund that manages teachers\' pensions cannot simply buy the most exciting asset on '
                'the table: its ', after=' makes the defensible choice the compulsory one.',
         answer='fiduciary duty', hint='Two words. The obligation is owed to the members, not chosen by the fund.'),
    dict(before='2. Revenue that would otherwise depend on next year\'s spot price is fixed by ',
         after=', so that the buyer is committed before the plant exists.',
         answer='an off-take agreement', alt='off-take agreement',
         hint='Three words, with the article.'),
    dict(before='3. Exposure to the exchange rate is closed with ', after='.',
         answer='a currency hedge', alt='currency hedge', hint='Three words, with the article.'),
    dict(before='4. A development bank agrees to lend below market terms, and that ',
         after=' is not charity but arithmetic.',
         answer='concessional lending', hint='Two words. Not "blended finance": that is the structure, this is the money.'),
    dict(before='5. Public money on worse terms is what makes private money on ordinary terms possible, a '
                'structure the sector calls ', after='.',
         answer='blended finance', hint='Two words. The name of the whole arrangement.'),
    dict(before='6. A guarantee wrapped around the bond delivers ',
         after=', and the project borrows two notches cheaper.',
         answer='credit enhancement', hint='Two words. Not "de-risking mechanism": this one is about the rating.'),
    dict(before='7. What is still missing is the first signature: until ',
         after=' commits publicly, every other committee has a reason to wait.',
         answer='an anchor investor', alt='anchor investor', hint='Three words, with the article.'),
    dict(before='8. And when they all arrive at once, the market produces its familiar result, ',
         after=', which leaves the safe asset earning less than it did a decade ago.',
         answer='yield compression', hint='Two words.'),
]
CLOZE_NOT_NEEDED = 'capital deployment'



# ── 5. READING Part A -- gapped text (Paper 1, Part 6) ────────────────────────
# Seis frases foram retiradas; sete opcoes, uma sobra. O que resolve cada lacuna
# e COESAO (referencia, conector, linha do argumento), nunca uma palavra isolada.
ARTICLE_TITLE = "Who Gets Paid First"
ARTICLE_STANDFIRST = "Adapted from a comment essay on infrastructure capital &middot; ~650 words"
ARTICLE = [
    ("Ask an engineer what an infrastructure project is and you will hear about geology, spans and traffic "
     "forecasts. Ask an investor and you will hear about something considerably less photogenic: the order of a "
     "queue. Beneath the concrete, every large scheme is a hierarchy of promises, and almost all of the "
     "intelligence in financing one goes into deciding who stands where in that hierarchy. ", 1,
     " The answer sets the price of every dollar that goes in, and it explains behaviour that, from the outside, "
     "looks merely timid."),

    ("At the front stand the senior lenders. They advance the bulk of the money, they are repaid before anyone "
     "else, and they are famously unimaginative about risk. ", 2,
     " Behind them sits subordinated debt, repaid only once the senior banks have been made whole, and charging "
     "handsomely for the privilege of waiting. At the very back, collecting whatever survives, sits equity, which "
     "is to say the party that is paid last and blamed first."),

    ("This layering explains a great deal that would otherwise look irrational. A pension fund that turns down a "
     "road promising fifteen percent in favour of one offering nine is not being cowardly; it is reading the "
     "queue. ", 3,
     " What it is buying, in the second case, is not a return at all but a position: near the front, protected, "
     "and dull enough to survive a committee."),

    ("The arrangement has consequences for what actually gets built. The institutions with the deepest pockets "
     "are also the ones with the strictest mandates, and their money therefore flows towards assets that are "
     "already operating and already earning. ", 4,
     " The effect shows up first in the price. Too much capital pursuing too few operating assets has compressed "
     "yields across the sector, so that the safe road now pays less than it did a decade ago, while the unbuilt "
     "one still cannot find a lender at any price."),

    ("Hence the instruments designed to rearrange the queue itself. A development bank that agrees to take the "
     "first loss on a solar cluster is not being generous; it is buying private money, and it knows roughly what "
     "it is paying. Guarantees, first-loss tranches, political risk insurance and concessional lending all "
     "perform the same operation by different means: they move a specific danger from the party that cannot "
     "carry it to the party that can. ", 5,
     " Practitioners call the result blended finance, and they judge it not by how much public money is spent "
     "but by how much private money arrives behind it."),

    ("There is a subtler reason these structures matter, and it concerns the first investor rather than the "
     "largest. Funds are institutions, but they are staffed by people, and people are reluctant to be the only "
     "name on a page. ", 6,
     " After that the queue fills with surprising speed, and the same committees that hesitated for two years "
     "will complain that their allocation was too small."),

    ("All of which the language of the sector is beautifully designed to obscure. Deals are described as having "
     "been structured, risks as having been transferred, approvals as having been obtained, and the reader is "
     "left to work out who did the structuring, the transferring and the obtaining. Put that question to any term "
     "sheet and it becomes a far more interesting document than it first appears. In project finance the passive "
     "is not a stylistic tic. It is a negotiating position.", None, ""),
]

GAP_OPTIONS = [
    ("A", "Its obligation, after all, is not to make the boldest bet on the table but to pay a schoolteacher a "
          "predictable income in 2050."),
    ("B", "An anchor investor, by committing early and in public, converts a proposal into something that other "
          "investment committees can defend internally."),
    ("C", "The question that decides a deal is therefore not who is paid the most, but who is paid first and who "
          "agrees to wait."),
    ("D", "Sovereign wealth funds, by contrast, answer to a finance ministry rather than to a retiree, and their "
          "horizons are political as well as financial."),
    ("E", "Their caution is not temperament but arithmetic: because their upside is capped at an interest rate, "
          "the only variable they can usefully manage is the chance of not being repaid at all."),
    ("F", "Construction, with its geology, its strikes and its lawsuits, is left to somebody else, and "
          "increasingly that somebody is a development bank."),
    ("G", "None of this makes the project any safer; it changes who is holding the risk when the danger finally "
          "arrives."),
]
GAP_ANSWERS = [("1", "C"), ("2", "E"), ("3", "A"), ("4", "F"), ("5", "G"), ("6", "B")]
GAP_KEY = (
    "<b>1 C</b> -- the paragraph poses a hierarchy; C turns it into a question, and the next sentence answers "
    "it with &ldquo;The answer&rdquo;.<br>"
    "<b>2 E</b> -- &ldquo;Their caution&rdquo; needs the senior lenders in the sentence before, and &ldquo;Behind "
    "them&rdquo; needs the front of the queue still in view.<br>"
    "<b>3 A</b> -- &ldquo;Its obligation&rdquo; refers back to the fund; &ldquo;in the second case&rdquo; only "
    "works if the two options are still on the table.<br>"
    "<b>4 F</b> -- &ldquo;is left to somebody else&rdquo; explains why the money flows to operating assets, and "
    "sets up &ldquo;The effect shows up first in the price&rdquo;.<br>"
    "<b>5 G</b> -- &ldquo;None of this&rdquo; gathers up the list of instruments; the concession it makes is what "
    "&ldquo;Practitioners call the result&rdquo; then answers.<br>"
    "<b>6 B</b> -- &ldquo;the only name on a page&rdquo; is solved by the first public signature, and "
    "&ldquo;After that&rdquo; needs that signature to exist.<br>"
    "<b>D is the distractor</b> -- true, on topic, and plausible near paragraph three, but it answers no "
    "reference and completes no argument."
)

# ── 6. READING Part B -- multiple choice (Paper 1, Part 5) ────────────────────
MCQ = [
    ("The contrast between the engineer and the investor in the first paragraph serves to", [
        ("show that technical expertise has been overrated in modern infrastructure.", False),
        ("locate the substance of a deal in the ordering of claims rather than in what is built.", True),
        ("suggest that investors are indifferent to whether a project actually works.", False),
        ("criticise the industry's preference for jargon over plain description.", False)]),
    ("What does the writer suggest about the senior lenders' attitude to risk?", [
        ("It is a conservatism that has outlived the conditions that produced it.", False),
        ("It is imposed on them by regulators rather than chosen by them.", False),
        ("It follows from the asymmetry between what they stand to gain and what they stand to lose.", True),
        ("It is a posture adopted in order to extract better terms from sponsors.", False)]),
    ("The reference to a schoolteacher retiring in 2050 is used to make the point that", [
        ("pension funds are accountable to people who will never read a term sheet.", False),
        ("the fund's caution is compulsory rather than temperamental.", True),
        ("infrastructure returns are too distant to be forecast with any confidence.", False),
        ("the industry underestimates how long its assets are expected to last.", False)]),
    ("The writer presents yield compression as", [
        ("evidence that the market is now pricing infrastructure risk efficiently.", False),
        ("a temporary distortion that cheap money created and will reverse.", False),
        ("the collective and self-defeating result of individually sensible caution.", True),
        ("proof that operating assets were overvalued from the beginning.", False)]),
    ("The writer's view of a development bank taking the first loss is that it is", [
        ("a subsidy that private investors have learned to take for granted.", False),
        ("a calculated purchase whose price is broadly known in advance.", True),
        ("an admission that the project would not otherwise deserve to be built.", False),
        ("an intervention that distorts the proper price of risk.", False)]),
    ("In the final paragraph, the writer argues that the passive voice in project finance", [
        ("reflects the genuine complexity of deals with many parties.", False),
        ("is an inherited convention that nobody in the sector now defends.", False),
        ("is used because naming the agent would concede something in a negotiation.", True),
        ("makes documents harder to read than their authors ever intend.", False)]),
]
MCQ_KEY = (
    "<b>1 B</b> -- A and D are opinions the text never offers; C overstates &ldquo;less photogenic&rdquo;.<br>"
    "<b>2 C</b> -- &ldquo;not temperament but arithmetic&rdquo;. A and D read a criticism into a description.<br>"
    "<b>3 B</b> -- A is <i>true</i> and still wrong: it is a fact in the sentence, not the point the sentence "
    "is making. This is the item that separates a C1 reader from a C2 one.<br>"
    "<b>4 C</b> -- &ldquo;too much capital pursuing too few&rdquo;: the caution is sensible one fund at a time "
    "and ruinous in aggregate.<br>"
    "<b>5 B</b> -- &ldquo;not being generous; it is buying private money, and it knows roughly what it is "
    "paying&rdquo;.<br>"
    "<b>6 C</b> -- &ldquo;not a stylistic tic. It is a negotiating position.&rdquo; A and D explain the passive "
    "innocently, which is precisely what the writer rejects."
)


# ── 7. USE OF ENGLISH Part A -- word formation (Paper 1, Part 3) ──────────────
WORD_FORMATION = [
    dict(before="Investors will forgive a difficult geography, but never a government whose commitments turn out to be ",
         after=". (RELY)", answer="unreliable",
         hint="Negative prefix + adjective from RELY."),
    dict(before="The first-loss tranche exists to make an otherwise ",
         after=" project bankable. (INVEST)", answer="uninvestable", alt="un-investable",
         hint="Negative prefix + -able adjective from INVEST."),
    dict(before="The board released the money only after an ",
         after=" review of the traffic model. (DEPEND)", answer="independent",
         hint="Not the same as 'dependable'. The review was carried out by an outside party."),
    dict(before="",
         after=", the funds that most need long-dated income are the least willing to fund new building. (PARADOX)",
         answer="paradoxically", hint="Sentence adverb, capital letter, comma after it."),
    dict(before="The sponsor was accused of the systematic ",
         after=" of construction costs. (STATE)", answer="understatement",
         hint="Prefix + noun from STATE. Not 'statement' on its own."),
    dict(before="Concessional lending is defended on the grounds of its ",
         after=" effect on private capital. (CATALYSE)", answer="catalytic",
         hint="Adjective from CATALYSE. Watch the internal change."),
    dict(before="A currency hedge costs money, but it removes the ",
         after=" that kills a committee approval. (CERTAIN)", answer="uncertainty",
         hint="Negative prefix + noun."),
    dict(before="The minister's ",
         after=" to reopen the concession after the election unsettled the whole market. (WILLING)",
         answer="willingness", hint="Noun from the adjective."),
]

# ── 8. USE OF ENGLISH Part B -- key-word transformation (Paper 1, Part 4) ─────
# Entre tres e oito palavras, a palavra-chave INALTERADA. checkBlank aceita a
# resposta e UMA variante (data-alt); o gabarito abaixo registra as demais, que
# o professor valida na aula.
TRANSFORMATIONS = [
    dict(lead="An independent firm audited our financial model before the roadshow.", key="HAD",
         before="Before the roadshow, we ", after=" by an independent firm.",
         answer="had our financial model audited", alt="had the financial model audited",
         hint="have + object + past participle. You arranged the service; the firm did the work."),
    dict(lead="The operator persuaded the ministry to approve the tariff.", key="GOT",
         before="The operator ", after=" the tariff.",
         answer="got the ministry to approve", alt="got the ministry to finally approve",
         hint="get + person + to + infinitive. Somebody was persuaded to act."),
    dict(lead="We are arranging for a development bank to provide a partial guarantee.", key="HAVING",
         before="We ", after=" a partial guarantee.",
         answer="are having a development bank provide", alt="are having a development bank give",
         hint="have + person + bare infinitive, in the present continuous."),
    dict(lead="Nobody knows who decided to reopen the concession.", key="DECISION",
         before="It is not known who ", after=" reopen the concession.",
         answer="took the decision to", alt="made the decision to",
         hint="Fixed collocation with DECISION + infinitive."),
    dict(lead="The fund will not invest unless the currency risk is hedged.", key="PROVIDED",
         before="The fund will invest ", after=" hedged.",
         answer="provided the currency risk is", alt="provided that the currency risk is",
         hint="Conditional alternative to 'if'. Do not change PROVIDED."),
    dict(lead="Nobody was surprised when the concession was renegotiated after the election.", key="CAME",
         before="It ", after=" that the concession was renegotiated after the election.",
         answer="came as no surprise to anyone", alt="came as no surprise",
         hint="Fixed expression: it ___ as no surprise."),
]
TRANSFORM_KEY = (
    "<b>1</b> had our financial model audited &middot; had the financial model audited<br>"
    "<b>2</b> got the ministry to approve &middot; (also acceptable: got the ministry to sign off on)<br>"
    "<b>3</b> are having a development bank provide &middot; (also: are having a development bank put up)<br>"
    "<b>4</b> took the decision to &middot; made the decision to<br>"
    "<b>5</b> provided the currency risk is &middot; provided that the currency risk is<br>"
    "<b>6</b> came as no surprise to anyone &middot; came as no surprise to anybody<br>"
    "<i>Any answer outside these is for the teacher to judge in class: the rule is three to eight words, the key "
    "word untouched, and no change of meaning.</i>"
)

# ── 9. LISTENING Part A -- sentence completion (Paper 3, Part 2) ──────────────
TALK_FILE = "pc2_talk_who_gets_paid_first.mp3"
TALK_VOICE = "daniel"
TALK_TEXT = (
    "Thank you. I have been asked to explain, in ten minutes, how a project actually gets funded, and I want to "
    "begin by throwing out the word that everybody arrives with, which is return. In my world the return is the "
    "last thing we look at. The first is the queue. "
    "Every financing is a hierarchy. The senior lenders are repaid first, and because their upside is fixed at an "
    "interest rate, the only thing they can really manage is the probability of default. Behind them we place what "
    "we call subordinated debt, which is paid after them and priced accordingly. And at the very back, taking "
    "whatever survives, sits the equity. "
    "Now, why would a pension fund accept nine percent on a road that is already open when a new port is offering "
    "fifteen? Not because it is timid. Because it has a mandate, and that mandate is written in the language of "
    "obligation, not of ambition. What the fund is buying at nine percent is not a return at all. It is a position "
    "near the front of the queue. "
    "That preference has a price, and all of us are paying it. So much capital has arrived for operating assets "
    "that the returns on exactly those assets have fallen. The industry's term for this is yield compression. "
    "Meanwhile the projects a country most needs, the ones still to be built, cannot raise a dollar, because "
    "construction risk is the one risk our investors are least willing to take. "
    "So the real work of my job is not finding money. It is rearranging the queue. If a development bank agrees to "
    "take the first loss, the private lender sitting behind it is suddenly looking at a different instrument. If a "
    "guarantor wraps the bond, the rating improves and the coupon falls. If the offtaker signs a twenty-year "
    "contract, the revenue exists before the asset does. And if the sponsor buys a currency hedge, a good year on "
    "the road stops being erased by a bad year on the exchange rate. "
    "None of this makes the road any safer. It moves the danger to whoever is best able to carry it, and that is "
    "all de-risking has ever meant. "
    "One last point, and it is the one people underestimate. The hardest signature to obtain is not the biggest. "
    "It is the first. Committees are staffed by people, and people do not want to be alone on a page. Find an "
    "anchor investor, and the rest of the round becomes a formality. "
    "And if you remember one sentence tonight, let it be this. We are not paid to find the highest number. We are "
    "paid to know who gets paid first."
)
TALK_ITEMS = [
    dict(before="1. The speaker says that in his world the first thing they look at is not the return but ",
         after=".", answer="the queue", alt="queue", hint="Two words, exactly as he says them."),
    dict(before="2. Because their upside is fixed, senior lenders can really only manage the ",
         after=".", answer="probability of default", alt="the probability of default",
         hint="Three words."),
    dict(before="3. The debt that is paid after the senior lenders and priced accordingly is called ",
         after=".", answer="subordinated debt", hint="Two words."),
    dict(before="4. A pension fund's mandate, he says, is written in the language of ",
         after=", not of ambition.", answer="obligation", hint="One word."),
    dict(before="5. The industry's term for the fall in returns on operating assets is ",
         after=".", answer="yield compression", hint="Two words."),
    dict(before="6. The one risk investors are least willing to take is ",
         after=".", answer="construction risk", hint="Two words."),
    dict(before="7. When the offtaker signs a twenty-year contract, the ",
         after=" exists before the asset does.", answer="revenue", hint="One word."),
    dict(before="8. The hardest signature to obtain is not the biggest; it is ",
         after=".", answer="the first", alt="first", hint="Two words."),
]

# ── 10. LISTENING Part B -- multiple matching, duas tarefas (Paper 3, Part 4) ─
# Cinco extratos, cinco VOZES diferentes (1 MP3 = 1 voz, sem excecao).
SPEAKERS = [
    dict(n=1, file="pc2_mm_speaker_1.mp3", voice="alice", task1="B", task2="E", text=(
        "People assume our problem is finding good assets. It is not. Our problem is that every asset we are "
        "permitted to buy is being bought by eleven other funds working from the same rulebook, and the price "
        "reflects that. I sat on a committee last month that approved a road at a return none of us would have "
        "looked at six years ago, and we approved it because the alternative was to hold cash. That is not "
        "investing. That is queuing politely.")),
    dict(n=2, file="pc2_mm_speaker_2.mp3", voice="arthur", task1="D", task2="A", text=(
        "We are often described as subsidising these deals, and I would push back on that. When we take the first "
        "five years, we are not making a gift. We are buying something quite specific, which is the presence of "
        "commercial lenders in year six. If we put in one dollar and four dollars of private money follow it, that "
        "dollar has done work no grant could do. Judge us on what arrives behind us, not on what we spend.")),
    dict(n=3, file="pc2_mm_speaker_3.mp3", voice="antonio", task1="C", task2="D", text=(
        "Everybody wants the road after it is open. Nobody wants it while it is a hole in the ground with a labour "
        "dispute and a rock formation that nobody surveyed properly. So the risk that terrifies the funds is "
        "precisely the risk we are paid to hold, and frankly we are not paid enough to hold it. Until somebody "
        "prices the building years honestly, the pipeline will stay full of projects that get announced and never "
        "financed.")),
    dict(n=4, file="pc2_mm_speaker_4.mp3", voice="matilda", task1="A", task2="B", text=(
        "My job is a narrow one. I look at whether the cash flow survives a bad decade. What has changed is the "
        "sheer amount of engineering around that cash flow. A guarantee here, an offtake there, a hedge on the "
        "currency, and the same underlying road presents as a materially safer credit. I have no objection to any "
        "of it, provided everybody remembers that the structure moved the risk. It did not delete it.")),
    dict(n=5, file="pc2_mm_speaker_5.mp3", voice="george", task1="F", task2="C", text=(
        "The complaint I heard for four years was about returns. It was never really about returns. Investors "
        "would have accepted a lower number on the day they believed that the rules would still be the rules "
        "after the next election. We reopened one concession, for reasons I would still defend, and it cost us a "
        "decade of credibility and a great deal more money than it ever saved.")),
]
TASK1_OPTS = [
    ("A", "a credit ratings analyst"),
    ("B", "a pension fund trustee"),
    ("C", "a contractor's finance director"),
    ("D", "an officer at a development bank"),
    ("E", "a fund manager raising a new vehicle"),
    ("F", "a former government minister"),
    ("G", "an infrastructure lawyer"),
    ("H", "a financial journalist"),
]
TASK2_OPTS = [
    ("A", "Public money should be judged by the private capital that follows it."),
    ("B", "Structuring relocates risk rather than removing it."),
    ("C", "Predictability of the rules matters more to investors than the level of return."),
    ("D", "Those who carry construction risk are not paid enough to carry it."),
    ("E", "Competition between similarly constrained buyers has pushed prices past what the asset merits."),
    ("F", "Regulation ought to be harmonised across the region."),
    ("G", "Currency risk is the single obstacle that ends most negotiations."),
    ("H", "Retail investors should be given access to infrastructure."),
]


# ── 11. GRAMATICA -- agencia: causative x passiva ────────────────────────────
# Mesmo grammar_point do programa. O que muda e que ele deixa de ser explicado e
# passa a ser DISCRIMINADO: quatro formas que um C1 ja produz, separadas pelo que
# cada uma faz com o agente.
GRAMMAR_ROWS = [
    ("have + object + past participle",
     "You arranged it. Who performed it is irrelevant, or arrives late with <i>by</i>.",
     "We <b>had</b> the financial model <b>audited</b> before the roadshow."),
    ("get + object + past participle",
     "Same structure, but there was resistance, effort or delay. Never neutral.",
     "After nine months the operator finally <b>got</b> the tariff <b>approved</b>."),
    ("have / get + person + verb",
     "You name the party you caused to act. <i>have</i> + bare infinitive; <i>get</i> + <i>to</i>.",
     "We <b>had</b> the lawyers <b>redraft</b> it. &middot; We <b>got</b> a development bank <b>to provide</b> a guarantee."),
    ("have + object + past participle (adversative)",
     "Identical shape, opposite sense: it was done <i>to</i> the subject, who arranged nothing.",
     "The sponsor <b>had</b> its licence <b>revoked</b> three weeks before financial close."),
    ("passive, agent named",
     "The agent is kept and pushed to the end, where the voice falls and the room is listening.",
     "The first loss <b>was taken by</b> the development bank."),
    ("passive, agent deleted",
     "Unknown, obvious, or deliberately unavailable. In a term sheet, assume the third.",
     "Approvals <b>were obtained</b> and the risk <b>was transferred</b>."),
    ("perfect passive infinitive / gerund",
     "The register of the briefing note: an action reported, its author absent.",
     "Risks are described as <b>having been transferred</b> to the private partner."),
]
GRAMMAR_QUIZ = [
    ("&ldquo;After nine months the operator finally <b>got</b> the tariff approved.&rdquo; The choice of "
     "<i>got</i> rather than <i>had</i> tells the reader that", [
         ("the operator was instructed to obtain the approval by its shareholders.", False),
         ("the approval was routine and administrative.", False),
         ("the approval was resisted and had to be pushed through.", True),
         ("the operator approved the tariff itself.", False)]),
    ("&ldquo;The sponsor <b>had</b> its licence revoked.&rdquo; Here the causative", [
         ("means the sponsor arranged for the licence to be revoked.", False),
         ("reports something unwelcome done to the sponsor by an authority.", True),
         ("is a mistake for &ldquo;the sponsor revoked its licence&rdquo;.", False),
         ("suggests the sponsor was indifferent to the outcome.", False)]),
    ("A term sheet reads: &ldquo;The exposure was reviewed and the structure amended.&rdquo; Compared with "
     "&ldquo;We had the exposure reviewed&rdquo;, this version", [
         ("states that nobody in particular carried out the review.", False),
         ("leaves open who commissioned the review, and therefore who answers for it.", True),
         ("is more precise, because the passive is the formal register.", False),
         ("implies the review was carried out by a regulator.", False)]),
    ("&ldquo;We had an independent firm audit the model&rdquo; and &ldquo;We had the model audited by an "
     "independent firm&rdquo; differ mainly in", [
         ("meaning: the first arranges a service, the second reports an accident.", False),
         ("formality: only the second is acceptable in writing.", False),
         ("what the sentence ends on, and therefore what the listener remembers.", True),
         ("tense: the second is closer to a present perfect.", False)]),
    ("In a briefing note, the sentence &ldquo;Approvals were obtained&rdquo; is most usefully met with the "
     "question", [
         ("when were they obtained, and are they still valid?", False),
         ("who obtained them, and what was conceded in order to obtain them?", True),
         ("which authority issues that class of approval?", False),
         ("why is the passive being used instead of the active?", False)]),
]
# Producao: as quatro frases que JA TEM MP3 (o Listen continua valendo), com a
# lacuna agora sobre a estrutura inteira, nao sobre uma palavra solta.
GRAMMAR_PRODUCTION = [
    dict(before="Before the roadshow, we ", after=" by an independent firm.",
         answer="had the financial model audited",
         alt="had our financial model audited",
         hint="have + object + past participle. Four words after 'we'.",
         phrase="Before the roadshow, we had the financial model audited by an independent firm."),
    dict(before="After nine months, the operator finally ", after=".",
         answer="got the tariff approved",
         hint="get + object + past participle: there was resistance.",
         phrase="After nine months, the operator finally got the tariff approved."),
    dict(before="We ", after=" a partial guarantee.",
         answer="got a development bank to provide",
         hint="get + person + to + infinitive: name the party you caused to act.",
         phrase="We got a development bank to provide a partial guarantee."),
    dict(before="The lender with subordinated debt ", after=" the senior bank.",
         answer="is paid only after",
         hint="Passive, agent deleted, because who pays is obvious from the structure.",
         phrase="The lender with subordinated debt is paid only after the senior bank."),
]

# ── 12. SPEAKING & WRITING (Paper 5 / Paper 2) ────────────────────────────────
SPEECH_PHRASES = [
    "What a pension fund needs is a risk-adjusted return, not the highest number on the page.",
    "We had the financial model audited by an independent firm before the roadshow.",
    "The operator got the tariff approved, and that changed the risk profile overnight.",
    "Without a currency hedge, a bad year for the exchange rate can erase a good year on the road.",
    "The other funds are waiting for an anchor investor to go in first.",
]
LONG_TURN = (
    "<b>Long turn -- two minutes, uninterrupted.</b> You are opening a session at an investor roundtable. "
    "Answer this: <i>&ldquo;Whose risk is it, really?&rdquo;</i> Take a single project you know and walk the room "
    "down the queue: who is paid first, who waits, who arranged each protection, and which danger did not "
    "disappear but simply changed hands. Two minutes, no notes. Use at least two causatives and four terms from "
    "this lesson, and end on the word you most want the room to remember."
)
COLLAB_TASK = (
    "<b>Collaborative task.</b> A ministry has one hundred million dollars and four ways to spend it on a stalled "
    "solar cluster: a first-loss tranche, a currency guarantee, a twenty-year off-take contract, or simply taking "
    "an equity stake itself. Talk through what each one does to the queue, and to whom. Then decide: which single "
    "instrument brings in the most private capital per public dollar, and what does the ministry give up by "
    "choosing it? Disagree with your teacher at least once, and say why."
)
WRITING_TASK = (
    "<b>Writing -- a briefing note, 280&ndash;320 words.</b> A sovereign wealth fund has asked why its peers "
    "are not yet invested in your region's infrastructure. Write the note. Give the fund the real answer, not the "
    "diplomatic one: the sequence of claims, the risks nobody will price, and the two changes that would move the "
    "first deal. Formal register, no bullet points, and at least three of: <i>de-risking mechanism, concessional "
    "lending, yield compression, credit enhancement, off-take agreement, anchor investor</i>. Somewhere in the "
    "note, use a passive where you are deliberately not naming the agent, and be ready to say why."
)
WRITING_MODEL = (
    "<i>What a strong answer does, in this order:</i> names the real obstacle in the first two sentences rather "
    "than the third paragraph; explains the queue once, plainly, without teaching the reader their own trade; "
    "concedes the weakest point before the reader finds it (the renegotiation, the thin pipeline, the currency); "
    "attributes each protection to a party, so that the fund knows whose signature it is buying; and ends on a "
    "single request, not a summary. The passive with no agent belongs in exactly one place -- where naming "
    "the party would commit you to more than you can deliver. If it appears anywhere else, it is a habit, not a "
    "choice."
)

# ── 13. FOLLOW-UP E OS DOIS DEBATES (o que faltava do modelo do professor) ────
# O modelo w11_l11e.html do professor encadeia LONG TURN -> follow-up curto ->
# DOIS debates for/against. A primeira versao desta aula parou no long turn e num
# debate so. Estas tres pecas fecham a sequencia de fala do modelo.
#
# Nada aqui pede audio novo: sao tarefas de producao oral. O lexico e o mesmo da
# aula (nenhum termo novo) e a gramatica cobrada e a desta aula -- causative have
# / get contra a passiva, que e exatamente o que a pergunta 2 do follow-up expoe.

FOLLOW_UP_INTRO = (
    "The examiner does not thank you and move on. Immediately after the two minutes come four short "
    "questions, and they are the real test: not what you prepared, but whether you can be pushed off it "
    "and stay precise. Answer each in two or three sentences. No restarting the long turn."
)
FOLLOW_UP = [
    ("You told me the risk moved. If that party walked away tomorrow morning, who is holding it by the "
     "afternoon, and what does it cost by then?"),
    ("Twice you said something &ldquo;was arranged&rdquo;. Name the party you left out each time, and tell me "
     "whether leaving them out was a choice or a habit."),
    ("Which of the protections you described would you not be willing to defend to the schoolteacher whose "
     "pension is paying for it?"),
    ("Say the whole thing again in one sentence, for a minister who has never read a term sheet, and without "
     "using the word <i>risk</i>."),
]
FOLLOW_UP_TEACHER = (
    "Follow-up (3 min): faca as quatro na sequencia, sem elogiar entre uma e outra. A pergunta 2 e a da "
    "gramatica da aula: se ele nao souber dizer quem sumiu na propria frase, a passiva dele ainda e habito, "
    "nao escolha. A pergunta 4 e a mais dura e vale por ela mesma: quem depende do jargao nao sobrevive a ela."
)

# Dois debates, como no modelo. O primeiro cobra repertorio dos dois lados; o
# segundo cobra concessao, que e o que falta a quem e fluente e nunca precisou
# negociar em ingles.
DEBATE_1_MOTION = (
    "Public money should never take the first loss on a private infrastructure project."
)
DEBATE_1_RULES = (
    "Ninety seconds <b>for</b>. Then ninety seconds <b>against</b>. Same speaker, no notes, and no repeating "
    "an argument you have already used."
)
DEBATE_2_MOTION = (
    "A fiduciary duty is a reason to stay out of infrastructure, not a reason to go into it."
)
DEBATE_2_RULES = (
    "Your teacher gives you the side; you do not choose it. Ninety seconds. Then, before you close, you must "
    "concede out loud the single strongest point against you, name it accurately, and say why you are still "
    "not moved. A concession that misstates the other side does not count."
)
DEBATE_2_TEACHER = (
    "Segundo debate (4 min): de a ele o lado que ele NAO defenderia -- normalmente o \"stay out\", "
    "porque contraria o proprio trabalho dele. O alvo aqui nao e argumento, e concessao: exija que ele "
    "reformule o ponto mais forte do outro lado com as palavras do outro lado antes de responder. Se a "
    "concessao sair caricata (\"some people say it is risky\"), devolva e peca de novo. Esta e a "
    "linguagem que falta a quem negocia em ingles sem nunca ter cedido em ingles."
)
