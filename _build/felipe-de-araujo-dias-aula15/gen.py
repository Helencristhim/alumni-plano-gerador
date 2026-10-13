#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 15 do Felipe de Araujo Dias — If I Could Change One Thing.
Second conditional (if + past, would / could / might; if I were you). Modelo de FALA
(aula IMPAR, REGRA 29). Tema: defender uma mudanca que ele faria na empresa — tirar as
tres aprovacoes de cada conserto pequeno das lojas.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 15

IMG_TITLE = 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_MEET = 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Approval', 'official permission to do something',
     'Every small repair in the stores needs three approvals.'),
    ('Paperwork', 'the forms and documents you have to fill in for a process',
     'If we had less paperwork, the repairs would be faster.'),
    ('To streamline', 'to make a process simpler and faster',
     'I would streamline the approval process for small repairs.'),
    ('To empower', 'to give people the authority to make decisions themselves',
     'If we empowered store managers, they would solve small problems in a day.'),
    ('Feasible', 'possible and practical to do',
     'The idea is feasible, and it would not cost anything.'),
    ('Pilot', 'a small test of a new idea before you use it everywhere',
     'We could run a pilot in twenty stores for three months.'),
    ('Buy-in', 'agreement and support for an idea from the people involved',
     'Without buy-in from finance, the change would never happen.'),
    ('Drawback', 'a disadvantage, or a problem that comes with something good',
     'The main drawback is that we would have less control over spending.'),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Approval', 'f'], ['2', 'Paperwork', 'c'], ['3', 'To streamline', 'h'],
                   ['4', 'To empower', 'a'], ['5', 'Feasible', 'g'], ['6', 'Pilot', 'b'],
                   ['7', 'Buy-in', 'e'], ['8', 'Drawback', 'd']],
         'defs': [['a', 'To give people the authority to make decisions themselves'],
                  ['b', 'A small test of a new idea before you use it everywhere'],
                  ['c', 'The forms and documents you have to fill in for a process'],
                  ['d', 'A disadvantage, or a problem that comes with something good'],
                  ['e', 'Agreement and support for an idea from the people involved'],
                  ['f', 'Official permission to do something'],
                  ['g', 'Possible and practical to do'],
                  ['h', 'To make a process simpler and faster']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: a pilot tests the idea, and buy-in gets people behind it. '
                  'A change with a good pilot and no buy-in still dies in the next meeting.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Today, every small repair in our stores needs three ', ['1', 'approval'],
                   's, and the store manager fills in the same ', ['2', 'paperwork'],
                   ' three times. I would ', ['3', 'streamline'],
                   ' the process and ', ['4', 'empower'],
                   ' store managers to approve repairs below two thousand reais. The idea is ',
                   ['5', 'feasible'], ', and it costs nothing. We could start with a ',
                   ['6', 'pilot'], ' in twenty stores. We would need ', ['7', 'buy-in'],
                   ' from finance, of course. The only ', ['8', 'drawback'],
                   ' is a little less control over spending.'],
         'bank': ['approval', 'paperwork', 'streamline', 'empower', 'feasible', 'pilot',
                  'buy-in', 'drawback']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'The CEO asks: if you could change one process in your areas '
                           'tomorrow, what would you change? Say what, why, and what would '
                           'happen after.'],
            ['Scenario 2', 'A new store manager asks for advice about a supplier who is always '
                           'late. Start with if I were you, and give two pieces of advice.'],
            ['Scenario 3', 'Imagine you had a free year, with no work and no money problems. '
                           'Where would you live, and what would you do every day?'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each sentence again as an imaginary situation, with the word the cue asks '
                  'for.',
         'items': [['We have three approvals, so repairs are slow.', 'if we had'],
                   ['My advice: talk to finance first.', 'if I were you'],
                   ['The stores do not have the authority, so they wait.', 'would'],
                   ['Maybe we can test it in twenty stores.', 'could']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'The CEO asks what you would change first if you had a bigger budget.',
             'tips': ['If I had a bigger budget, I would...',
                      'Say the change, then the result.']},
            {'situation': 'A colleague asks your advice: should he accept a job in another city?',
             'tips': ['If I were you, I would...',
                      'Give one reason, then one risk.']},
            {'situation': 'Finance says your idea is not feasible. Defend it in two sentences.',
             'tips': ['It would cost..., and it would save...',
                      'Offer a pilot: we could start with...']},
            {'situation': 'Someone asks what you would do if you were not in supply chain.',
             'tips': ['If I were not..., I would...',
                      'Add one thing you would miss.']},
            {'situation': 'Your director asks for the main drawback of your idea.',
             'tips': ['Be honest: the main drawback would be...',
                      'Then say how you would control it.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['If we had fewer approvals, repairs would be faster.',
                  'If I were you, I would talk to finance first.',
                  'If the stores had the authority, they would not wait.',
                  'We could test it in twenty stores.'],
         'note': ('The second conditional is about a situation that is not real now: if + past, '
                  'then would, could or might. The past here is not about the past. It is about '
                  'distance from reality.')},
    ],
}

LISTENINGS = [
    {'file': 'a15_listening1.mp3', 'voice': 'ellen',
     'text': ("Felipe, hi, it's Karen from the CEO's office. A quick message about the "
              "directors' offsite next Thursday. This year the format is different. Every "
              "director gets five minutes and one question: if you could change one thing in "
              "the company, what would it be? Not a plan for the whole year, just one change. "
              "Please say what you would change, what would happen if we did it, and what the "
              "main drawback would be. If the idea needs money, bring a number. And if I were "
              "you, I wouldn't use slides. The CEO prefers people who talk to the room.")},
    {'file': 'a15_listening2.mp3', 'voice': 'nordic_f',
     'text': ("Hi Felipe, it's Ingrid. I just wanted to say your talk at the offsite was one "
              "of the best. The CEO liked the idea of the store managers approving small "
              "repairs, and he wants a pilot. If you started in twenty stores, he would like "
              "to see the first results in ninety days. Finance has one condition: a limit "
              "for each store, every month. Oh, and one small thing about your English. You "
              "said, if I would have the budget. In English, it's if I had the budget. The "
              "would only goes in the other half of the sentence. Congratulations again.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l15]', 'file': 'pc15_order_change.mp3', 'voice': 'arthur',
     'text': ("First, Ingrid asks Felipe what he would change if he could change one thing. "
              "Then Felipe says he would cut the three approvals for small repairs. After that, "
              "he explains that store managers would solve problems in a day. Next, Ingrid asks "
              "about the main drawback. Finally, Felipe says they could start with a pilot in "
              "twenty stores.")},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de FALA. Hoje ele defende uma mudança que '
    'faria na empresa, como numa reunião de diretoria. Diga o tema e siga.',
    'Chapter 1: One Thing', 'If I Could Change', 'One Thing',
    'An idea for your company, defended out loud, with the drawback included', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 14 (3 min): na aula 14 ele falou de riscos REAIS, com if + '
    'presente e will (o container, o plano de contingência). Hoje a situação é imaginária. Peça '
    'que ele responda ao prompt e ESCUTE se sai if I would have &mdash; é o erro do Detective. '
    'Não corrija ainda.',
    'You Planned for a Real Risk.', 'Now Imagine a Change',
    'Last lesson the container was real, and the question was what will happen. Today nothing '
    'is real yet: it is an idea, a wish, a change you would make if you had the power. English '
    'uses a different structure for that, and you will hear it in every strategy meeting.',
    'If you were the CEO for one day, what is the first thing you would do?'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as três missões. Diga que no fim ele vai defender a mudança dele '
    'em noventa segundos, sem apoio. Passe ao próximo.',
    ['Eight words for approvals, paperwork and selling an idea.',
     'If + past, would: the structure for an imaginary situation.',
     'Defend one real change in your company, and answer the hard question.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'a Change',
    '8 words for the problem, the idea and the people you need', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para paperwork: '
    'Can you count paperwork, three paperworks? (Não &mdash; é incontável, como overtime na '
    'aula 13.) CCQ para to empower: If you empower a manager, who decides? (O gerente.) '
    'Pronúncia: streamline tem stress no STREAM.',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para pilot: Is a pilot the whole project or '
    'a small test? (Um teste pequeno.) CCQ para drawback: Is a drawback a reason to say no? '
    '(Não necessariamente &mdash; é o lado ruim de algo bom.) Pronúncia: feasible = FEE-zuh-bul.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta, como se estivesse na reunião de diretoria. Pergunte no fim: is this '
    'idea feasible in your company?',
    'Use the Words', 'One Idea, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição gramática (1 min): diga: Last lesson the problem was real. Today it is an idea. '
    'Watch what happens to the verb. Passe ao próximo.',
    'Chapter 3: Not Real, Not Yet', 'If I Had,', 'I Would',
    'The second conditional', IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: Is any of '
    'this real right now? And which verb looks like the past? Só DEPOIS clique em Reveal the '
    'Rule. CCQ: In If I had a bigger budget, do I have a bigger budget? (Não.) Is had about '
    'yesterday? (Não &mdash; é sobre agora, só que imaginário.) In If I were you, am I you? (Não '
    '&mdash; é conselho.)',
    'second conditional',
    [('"If I <span class="accent" style="font-weight:700">had</span> the budget, I '
      '<span class="accent" style="font-weight:700">would change</span> the process."',
      'If I had the budget, I would change the process.'),
     ('"If store managers <span class="accent" style="font-weight:700">approved</span> small '
      'repairs, they <span class="accent" style="font-weight:700">would save</span> a week."',
      'If store managers approved small repairs, they would save a week.'),
     ('"If I <span class="accent" style="font-weight:700">were</span> you, I '
      '<span class="accent" style="font-weight:700">would talk</span> to finance first."',
      'If I were you, I would talk to finance first.'),
     ('"We <span class="accent" style="font-weight:700">could</span> start with a pilot if the '
      'CEO <span class="accent" style="font-weight:700">agreed</span>."',
      'We could start with a pilot if the CEO agreed.')],
    'rule15',
    ['Form', 'Use it for', 'Example'],
    [['If + past, would + verb', 'An imaginary situation now, and its result.',
      'If I <strong>had</strong> the budget, I <strong>would change</strong> it.'],
     ['would + verb if + past', 'The same idea, result first. No comma.',
      'Repairs <strong>would be</strong> faster if we <strong>cut</strong> approvals.'],
     ['If I were you, I would...', 'Advice. Were for every person.',
      'If I <strong>were</strong> you, I <strong>would wait</strong>.'],
     ['could / might + verb', 'A possible result, less certain than would.',
      'We <strong>could</strong> start with a pilot.'],
     ['First vs second', 'Real possibility: if + present, will. Imagined: if + past, would.',
      'If it <strong>arrives</strong>, we <strong>will</strong>... / If I <strong>were</strong> '
      'CEO, I <strong>would</strong>...']],
    ('Never would after if. The if half is in the past, but it is not about the past: it is '
     'about a situation that is not real.')))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: is it real? Se não é, o if vai para o passado e o resultado leva '
    'would.',
    'Grammar Practice', 'Real or', 'Imagined?',
    'Say the full sentence, then click to compare',
    [('If we ______ (have) fewer approvals, the repairs ______ (be) faster.',
      'If we had fewer approvals, the repairs would be faster.'),
     ('If I ______ (be) you, I ______ (start) with a pilot.',
      'If I were you, I would start with a pilot.'),
     ('Store managers ______ (solve) problems in a day if they ______ (have) the authority.',
      'Store managers would solve problems in a day if they had the authority.'),
     ('If finance ______ (not agree), we ______ (could / try) it in ten stores.',
      "If finance didn't agree, we could try it in ten stores.")]))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): a Karen, do escritório do CEO, americana, explicando o formato do '
    'offsite de diretores. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Ela dá três '
    'instruções e um conselho com if I were you &mdash; peça que ele repita o conselho no fim. '
    'Toque duas vezes.',
    1, 'One Question for', 'Every Director',
    'A message from the office of the CEO about next week. Sound first, no text.',
    'a15_listening1.mp3', SLUG,
    [('How much time does every director get at the offsite?',
      'Five minutes, and one question.'),
     ('What three things should Felipe say about his change?',
      'What he would change, what would happen, and the main drawback.'),
     ('What is Karen’s advice about slides?',
      'If she were him, she would not use slides.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição diálogo (1 min): diga: Before the offsite, Ingrid, the consultant who is '
    'running it, wants to hear your idea. Passe ao próximo.',
    'Chapter 4: The Conversation', 'What Would You', 'Change?',
    'Testing the idea before the offsite', IMG_MEET))

S.append(L.s_dialogue(
    14, 4,
    'Diálogo (6 min): Ingrid é consultora sueca, sotaque nórdico, e está preparando o offsite. '
    'Clique Next Line a cada fala. Nas falas do FELIPE, peça que ELE fale primeiro, com o texto '
    'tapado. Aponte a fala 10: ele admite o lado ruim ANTES de ser cobrado, e é isso que convence.',
    'What Would You', 'Change?',
    [('ingrid', 'I', 'nordic_f',
      'So, Felipe. If you could change one thing in the company, what would it be?'),
     ('felipe', 'F', 'arthur',
      'The <span class="vocab-highlight">approvals</span> for small repairs. Today every repair '
      'needs three.'),
     ('ingrid', 'I', 'nordic_f', 'Even a broken door?'),
     ('felipe', 'F', 'arthur',
      'Even a broken door. The store manager waits nine days, and fills in the same '
      '<span class="vocab-highlight">paperwork</span> three times.'),
     ('ingrid', 'I', 'nordic_f', 'And what would you do instead?'),
     ('felipe', 'F', 'arthur',
      'I would <span class="vocab-highlight">empower</span> the store managers. If they '
      'approved repairs below two thousand reais, they would solve most problems in a day.'),
     ('ingrid', 'I', 'nordic_f', 'Would it cost anything?'),
     ('felipe', 'F', 'arthur', 'Nothing. It would actually save money, and a lot of time.'),
     ('ingrid', 'I', 'nordic_f', 'What would finance say?'),
     ('felipe', 'F', 'arthur',
      'They would worry about control. That is the main '
      '<span class="vocab-highlight">drawback</span>, and I understand it.'),
     ('ingrid', 'I', 'nordic_f', 'So how would you get their buy-in?'),
     ('felipe', 'F', 'arthur',
      'With a <span class="vocab-highlight">pilot</span>. If we started in twenty stores, we '
      'would have real numbers in three months.')]))

S.append(L.s_comprehension(
    15, 4,
    'Comprehension (3 min): as perguntas são sobre a INGRID, não sobre ele. Ele responde de '
    'memória ANTES de clicar.',
    'Did You Catch It?', 'About', 'Ingrid',
    [('What is the first question Ingrid asks?',
      'If he could change one thing in the company, what it would be.'),
     ('What example of a small repair does she give?',
      'A broken door.'),
     ('What does she want to know about finance?',
      'What finance would say, and how he would get their buy-in.')]))

S.append(L.s_artifact(
    16, 4,
    'Artefato (4 min): a página única que ele levaria ao offsite. Peça que ele APRESENTE em voz '
    'alta, linha por linha, transformando cada linha numa frase com would ou could. A terceira '
    'pergunta é produção: exija a frase completa com if + passado.',
    'Real Document', 'The One-Page', 'Proposal',
    'CHANGE PROPOSAL &mdash; SMALL REPAIRS', 'PRESENTER: FELIPE DIAS',
    [('Today', '3 approvals for every repair'),
     ('Average wait', '9 days &middot; same form 3 times'),
     ('Proposal', 'Store managers approve below BRL 2,000'),
     ('Expected wait', '1 to 2 days'),
     ('Cost', 'zero &middot; less paperwork'),
     ('Main drawback', 'less control over spending'),
     ('Control', 'monthly limit for each store'),
     ('Pilot', '20 stores &middot; 90 days')],
    [('How long would a repair take with the new process?',
      'One to two days, instead of nine.'),
     ('What is the main drawback, and how would he control it?',
      'Less control over spending. There would be a monthly limit for each store.'),
     ('Say the main idea with if + past and would.',
      'If store managers approved small repairs, they would wait one or two days, not nine.')]))

S.append(L.s_listening(
    17, 4,
    'Listening 2 (5 min): sotaque nórdico, a mesma Ingrid do diálogo, depois do offsite. LEIA '
    'AS PERGUNTAS COM ELE ANTES do play. No fim ela corrige um erro do Felipe &mdash; peça que '
    'ele diga qual, e a forma certa. Toque duas vezes.',
    2, 'After the', 'Offsite',
    'A message the day after the talk, with one small correction. Sound first, no text.',
    'a15_listening2.mp3', SLUG,
    [('What does the CEO want to see?',
      'A pilot, with the first results in ninety days.'),
     ('What is the condition from finance?',
      'A limit for each store, every month.'),
     ('What small mistake does Ingrid correct?',
      'He said if I would have the budget. It should be if I had the budget.')]))

S.append(L.s_blocks(
    18, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as Tips. '
    'Exija as DUAS metades em toda resposta: a condição com o passado e o resultado com would. '
    'Se ele parar na primeira frase, pergunte: and then what would happen?',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    19, 6,
    'Transição prática (1 min): diga: Now you defend your idea. Three rounds, less help each '
    'time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    20, 6,
    'Scenarios + Rephrase (5 min): nos cenários exija if + passado, would e pelo menos um if I '
    'were you. No rephrase ele usa a pista entre parênteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    21, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM VOZ '
    'ALTA antes de clicar. Score no topo.',
    [('If I would have the budget, I would change the process.',
      'If I had the budget, I would change the process.'),
     ('If I was you, I would talk to finance first.',
      'If I were you, I would talk to finance first.'),
     ('If store managers approve small repairs, they would save a week.',
      'If store managers approved small repairs, they would save a week.'),
     ('We will start a pilot if the CEO agreed.',
      'We would start a pilot if the CEO agreed.')]))

S.append(L.s_roleplay(
    22, 6,
    'Role-play 1 &mdash; guiado (4 min): você é a Ingrid. Pergunte: if you could change one '
    'thing, what would it be? Ele responde usando as chips, com a mudança das aprovações ou '
    'outra dele.',
    'Role-Play 1 &mdash; Guided', 'One Change,', 'Three Sentences',
    'Situation',
    'A consultant asks what you would change in your company. Say what you would change, what '
    'would happen after, and what it would cost.',
    ['if I could', 'I would', 'it would save', 'feasible', 'a pilot']))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é o diretor financeiro e não gosta da ideia. '
    'Insista: we would lose control. Ele tem de admitir o drawback e propor o controle.',
    'Role-Play 2 &mdash; Semi-Free', 'We Would Lose', 'Control',
    'Situation',
    'The finance director thinks your idea is dangerous. Admit the main drawback, explain how '
    'you would control it, and ask for a small pilot.',
    ['the main drawback', 'if we had a limit', 'buy-in', 'we could start']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos, como no offsite. Conte quantas frases com would ele disse e '
    'depois faça UMA pergunta difícil. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'You are at the offsite. Defend one real change you would make in your areas: what you '
    'would change, what would happen, what it would cost, and the main drawback. Then answer '
    'one question from the CEO. Ninety seconds, no notes.',
    []))

S.append(L.s_blocks(
    25, 6,
    'Answer key (2 min): o accordion nasce fechado. Só abra depois que ele tentou as quatro do '
    'rephrase. Clicar de novo fecha.',
    'Check Your Work', 'Model', 'Answers', ['answerkey'],
    'Try the rephrase first. Reveal the key only to compare.'))

S.append(L.s_survival(
    26,
    'Survival lines (3 min): leia cada frase, toque o áudio, peça repetição olhando para a '
    'câmera. São as cinco frases da próxima vez que ele defender uma ideia na diretoria.',
    'Say It with', 'Confidence',
    ['If I could change one thing, it would be this.',
     'If we had fewer approvals, the stores would be faster.',
     'The main drawback would be less control.',
     'We could start with a pilot in twenty stores.',
     'If I were you, I would talk to finance first.']))

S.append(L.s_checklist(
    27,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz alta. '
    'Os 5 checks marcados fecham a aula 15.',
    15,
    ['I can defend a change I would make in my company.',
     'I use the past after if, and would in the result, for something that is not real.',
     'I say if I were you when I give advice.',
     'I know when to use will and when to use would.',
     'I know the words: approval, paperwork, to streamline, to empower, feasible, pilot, '
     'buy-in, drawback.']))

S.append(L.s_badge(
    28,
    'Encerramento (2 min): diga: Lesson 15 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos defendendo UMA mudança real nas áreas dele, com o '
    'drawback, e mandar no WhatsApp. Próxima aula: The City That Surprised Me.',
    15, 'If I Could Change One Thing',
    'You defended a real change today, Felipe, and you said the drawback before anybody asked.',
    'The City That Surprised Me'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'If I Could Change One Thing -- Opinion and Hypothesis',
    'short_title': 'If I Could Change One Thing',
    'menu_desc': ('Speaking lesson: one change you would make in the company, defended out '
                  'loud, and the second conditional for every idea that is not real yet'),
    'grammar_point': 'second conditional',
    'characters': {'felipe': 'arthur', 'ingrid': 'nordic_f'},
    'phases': ['One Thing', 'Your Words', 'Not Real, Not Yet', 'The Conversation',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&q=80',
    'desc': ('The words of a change: approval, paperwork, to streamline, to empower, feasible, '
             'pilot, buy-in, drawback. Structure: the second conditional, with if + past, '
             'would, could and if I were you. Mission: defend one change you would make in '
             'your company.'),
    'context_paras': [
        'If I could change one thing in the company, it <strong>would be</strong> the approvals '
        'for small repairs. Today a broken door needs three signatures and nine days. If store '
        'managers <strong>approved</strong> repairs below two thousand reais, they '
        '<strong>would solve</strong> most problems in a day. It <strong>wouldn\'t cost</strong> '
        'anything. If finance <strong>were</strong> worried about control, we '
        '<strong>could</strong> start with a pilot in twenty stores.',
        'Look at the verbs after <em>if</em>: <em>approved</em>, <em>were</em>. They look like '
        'the past, but they are not about the past. They show that the situation is '
        '<strong>not real</strong> now: it is an idea. The result takes <em>would</em>, '
        '<em>could</em> or <em>might</em>. And to give advice, we say <em>If I '
        '<strong>were</strong> you</em>, never <em>if I would be you</em>.'],
    'context_quiz': [
        ('In <em>If store managers approved repairs</em>, is the writer talking about the past?',
         [('Yes, because approved is the past simple of approve, so it happened before.', False),
          ('No. It is an imaginary situation now.', True),
          ('Yes, because the managers approved repairs last year.', False)]),
        ('How much would the change cost, according to the text?',
         [('Two thousand reais for every store in the pilot, every single month.', False),
          ('Nothing.', True),
          ('Nine days.', False)]),
        ('What could they do if finance were worried about control?',
         [('Start with a pilot in twenty stores.', True),
          ('Cancel the whole idea and keep the three approvals and the paperwork.', False),
          ('Ask the store managers for more signatures.', False)]),
    ],
    'tip_title': 'The Second Conditional',
    'tip_intro': ('A situation that is not real now, and what would happen if it were. The '
                  'condition takes the past; the result takes would, could or might.'),
    'tip_rows': [
        ['If + past, would + verb', 'Condition first, with a comma.',
         'If I <strong>had</strong> the budget, I <strong>would change</strong> the process.'],
        ['would + verb if + past', 'Result first, no comma.',
         'Repairs <strong>would be</strong> faster if we <strong>cut</strong> approvals.'],
        ['If I were you, I would...', 'Advice. Use were with every person.',
         'If I <strong>were</strong> you, I <strong>would talk</strong> to finance.'],
        ['could / might', 'A possible result, less sure than would.',
         'We <strong>could</strong> start with a pilot.'],
        ['First or second?', 'Real possibility: if + present, will. Imagined: if + past, would.',
         'If it <strong>arrives</strong>, we <strong>will</strong> call. / If I <strong>were'
         '</strong> CEO, I <strong>would</strong> change it.'],
        ['Negative', "If we <strong>didn't</strong> have three approvals, it <strong>wouldn't"
         "</strong> take nine days."],
    ],
    'tip_note': ('The most common mistake is would in both halves. Only the result takes would: '
                 '<em>if I had</em>, never <em>if I would have</em>.'),
    'blanks': [
        ('If I ', 'had', 'Hint: one word. The past of have, after if.',
         'If I had the budget, I would change the process.',
         ' the budget, I would change the process.'),
        ('If I had the budget, I ', 'would change', 'Hint: two words. The result.',
         'If I had the budget, I would change the process.', ' the process.'),
        ('If I ', 'were', 'Hint: one word. Advice: if I ... you.',
         'If I were you, I would talk to finance first.',
         ' you, I would talk to finance first.'),
        ('We ', 'could', 'Hint: one word. A possible result, less sure than would.',
         'We could start with a pilot in twenty stores.', ' start with a pilot in twenty stores.'),
        ('The main ', 'drawback', 'Hint: one word. A disadvantage.',
         'The main drawback would be less control.', ' would be less control.'),
        ('Without ', 'buy-in', 'Hint: two parts with a hyphen. Support from the people involved.',
         'Without buy-in from finance, the change would never happen.',
         ' from finance, the change would never happen.'),
    ],
    'order_title': 'Put the Conversation in Order',
    'order_intro': 'Listen first, then put the five parts of the conversation in the order you '
                   'hear them.',
    'order': [
        (4, 'Next, Ingrid asks about the main drawback.'),
        (2, 'Then Felipe says he would cut the three approvals for small repairs.'),
        (5, 'Finally, Felipe says they could start with a pilot in twenty stores.'),
        (1, 'First, Ingrid asks Felipe what he would change if he could change one thing.'),
        (3, 'After that, he explains that store managers would solve problems in a day.'),
    ],
    'speech': [
        'If I could change one thing, it would be this.',
        'If we had fewer approvals, the stores would be faster.',
        'The main drawback would be less control.',
        'We could start with a pilot in twenty stores.',
        'If I were you, I would talk to finance first.',
    ],
    'quiz_intro': 'You are defending an idea in a directors’ meeting. Choose the best thing '
                  'to say.',
    'quiz': [
        ('The CEO asks what you would do with a bigger budget. You say:',
         [('If I would have a bigger budget, I would hire two more technicians.', False),
          ('If I had a bigger budget, I would hire two more technicians.', True),
          ('If I have a bigger budget, I would hire.', False)]),
        ('A new manager asks for your advice. You say:',
         [('If I was you, I will talk to finance first, before the meeting starts.', False),
          ('If I were you, I would talk to finance first.', True),
          ('If I am you, I talk to finance.', False)]),
        ('You want to offer a small test. You say:',
         [('We could start with a pilot in twenty stores.', True),
          ('We would started a pilot in twenty stores in the south of the country.', False),
          ('We can to start a pilot.', False)]),
        ('Finance asks about the risk. You say:',
         [('The main drawback will be less control, if we would do it in every store.', False),
          ('The main drawback would be less control.', True),
          ('The main drawback would being less control.', False)]),
    ],
    'think': ('Think about one real thing you would change in your four areas if you had the '
              'power. Record about ninety seconds. Say what you would change and why, what '
              'would happen after the change, and what it would cost. Then say the main '
              'drawback, and how you would control it. Finish with one piece of advice that '
              'starts with if I were you. Use at least four words from this lesson. Do not stop '
              'to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         'The second conditional -- 6 Minute Grammar, BBC Learning English',
         'Six minutes on if + past and would, with the common mistakes. Connection to Lesson '
         '15: every sentence of your offsite talk.',
         'Tip: pause after each example and make the same sentence about your own company.',
         'https://www.youtube.com/watch?v=3OuqzHxlrHc', 'Watch on YouTube'),
        ('youtube', 'first-second', 'Grammar Video',
         'The first and second conditional -- English Class, BBC Learning English',
         'A short class that puts the two structures side by side: the real risk and the '
         'imagined change. Connection to Lesson 15: the container from Lesson 14 against the '
         'idea you defended today.',
         'Tip: after watching, say one sentence with will and one with would about the same '
         'delivery.',
         'https://www.youtube.com/watch?v=HjzA0Z_ZyxE', 'Watch on YouTube'),
        ('video', 'ideas', 'TED Talk',
         'How to get your ideas to spread -- Seth Godin, TED',
         'A short talk about why some ideas win in a company and others are forgotten after the '
         'meeting. Connection to Lesson 15: buy-in, and how to sell a change.',
         'Tip: watch with English subtitles and write down one idea you would use at your '
         'next directors\u2019 meeting.',
         'https://www.youtube.com/watch?v=xBIVlM435Zg', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
