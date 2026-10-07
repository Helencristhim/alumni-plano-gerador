#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 11 do Felipe de Araujo Dias — Rules and Policies.
Modais de obrigacao (must, have to, should, don't have to, mustn't).
Modelo de FALA (aula IMPAR, REGRA 29). Tema: prevencao de perdas — explicar a politica
de visitantes do CD a uma visitante italiana.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-de-araujo-dias-common'))
import dias_lib as L  # noqa: E402

SLUG = 'felipe-de-araujo-dias'
N = 11

IMG_TITLE = 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1400&q=80'
IMG_VOCAB = 'https://images.unsplash.com/photo-1553413077-190dd305871c?w=1400&q=80'
IMG_GRAM = 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80'
IMG_TOUR = 'https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?w=1400&q=80'
IMG_TURN = 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80'

VOCAB = [
    ('Policy', 'a set of rules that a company follows and expects everybody to follow',
     'Our policy is simple: every visitor has to sign in at the gate.'),
    ('Shrinkage', 'the stock a retailer loses through theft, damage or mistakes',
     'Shrinkage cost us almost two percent of sales last year.'),
    ('Shoplifting', 'stealing goods from a store while it is open',
     'Most shoplifting happens in the busiest hour of the day.'),
    ('Restricted area', 'a place where only authorized people can go',
     "You mustn't enter the restricted area without an escort."),
    ('To comply with', 'to follow a rule, a standard or an instruction',
     'Every supplier has to comply with our safety standards.'),
    ('Spot check', 'a quick inspection done at random, without warning',
     'We do a spot check on two trucks every week.'),
    ('To enforce', 'to make sure that people really obey a rule',
     "A rule nobody enforces isn't a rule. It's a suggestion."),
    ('To be allowed to', 'to have permission to do something',
     "Visitors aren't allowed to take photos inside the warehouse."),
]

INCLASS_BLOCKS = {
    'vocab': [
        {'kind': 'matching', 'title': 'Match each word to its meaning',
         'words': [['1', 'Policy', 'c'], ['2', 'Shrinkage', 'f'], ['3', 'Shoplifting', 'h'],
                   ['4', 'Restricted area', 'a'], ['5', 'To comply with', 'g'],
                   ['6', 'Spot check', 'b'], ['7', 'To enforce', 'e'],
                   ['8', 'To be allowed to', 'd']],
         'defs': [['a', 'A place where only authorized people can go'],
                  ['b', 'A quick inspection done at random, without warning'],
                  ['c', 'A set of rules that a company follows and expects everybody to follow'],
                  ['d', 'To have permission to do something'],
                  ['e', 'To make sure that people really obey a rule'],
                  ['f', 'The stock a retailer loses through theft, damage or mistakes'],
                  ['g', 'To follow a rule, a standard or an instruction'],
                  ['h', 'Stealing goods from a store while it is open']]},
        {'kind': 'vocabnote',
         'text': ('Notice the pair: shoplifting is one cause and shrinkage is the total. Theft, '
                  'damage and simple mistakes all end up in the same number at the end of the '
                  'year.')},
    ],
    'gapfill': [
        {'kind': 'gapfill',
         'parts': ['Welcome to the distribution center. Our ', ['1', 'policy'],
                   ' for visitors is short, but we ', ['2', 'enforce'],
                   ' it every day. Last year ', ['3', 'shrinkage'],
                   ' cost us almost two percent of sales, and only part of it was ', ['4', 'shoplifting'],
                   ' in the stores. The rest happens here. That is why you are not ', ['5', 'allowed to'],
                   ' take photos, and why you need an escort in any ', ['6', 'restricted area'],
                   '. Every truck has to ', ['7', 'comply with'],
                   ' the same rules, and twice a week we do a ', ['8', 'spot check'],
                   ' on two of them, without warning.'],
         'bank': ['policy', 'enforce', 'shrinkage', 'shoplifting', 'allowed to',
                  'restricted area', 'comply with', 'spot check']},
    ],
    'practice': [
        {'kind': 'scenarios', 'items': [
            ['Scenario 1', 'A visitor arrives at your distribution center. Explain three rules '
                           'they have to follow, one thing they must not do, and one thing they '
                           'do not have to worry about.'],
            ['Scenario 2', 'A new store manager asks why the staff bags are checked at the end '
                           'of every shift. Explain the rule and the reason behind it.'],
            ['Scenario 3', 'A supplier wants to skip the spot checks because they are a trusted '
                           'partner. Say no politely, and say what they should do instead.'],
        ]},
        {'kind': 'rephrase',
         'title': 'Say each rule again with the modal the cue asks for.',
         'items': [['wear a vest in the warehouse', 'obligation'],
                   ['take photos near the docks', 'prohibition'],
                   ['wear safety boots in the office', 'no obligation'],
                   ['keep your badge where people can see it', 'advice']]},
    ],
    'quickfire': [
        {'kind': 'quickfire', 'items': [
            {'situation': 'A visitor takes out a phone to photograph the loading docks. Stop '
                          'them, politely and clearly.',
             'tips': ["Prohibition is mustn't or not allowed to.",
                      'Give the reason in one short sentence, then offer an alternative.']},
            {'situation': 'The visitor asks whether she needs to wear safety boots in the office '
                          'area. She does not.',
             'tips': ["No obligation is don't have to, never mustn't.",
                      'Then say where she does need them.']},
            {'situation': 'A store manager asks why the company checks staff bags at the end of '
                          'every shift.',
             'tips': ['Start with the rule, then the number behind it.',
                      'Shrinkage and shoplifting are not the same thing. Use both.']},
            {'situation': 'A colleague asks for your advice: should he report a small breach '
                          'he saw in the warehouse?',
             'tips': ['Advice is should, not must.',
                      'Say what you would do and why.']},
            {'situation': 'A supplier asks if the spot checks are really necessary for a '
                          'partner of ten years.',
             'tips': ['Every supplier has to comply. No exceptions, no apology.',
                      'Finish with what they can do to make the check faster.']},
        ]},
    ],
    'answerkey': [
        {'kind': 'answer', 'title': 'Reveal the model answers',
         'list': ['You have to wear a vest in the warehouse.',
                  "You mustn't take photos near the docks.",
                  "You don't have to wear safety boots in the office.",
                  'You should keep your badge where people can see it.'],
         'note': ("Mustn't closes a door: it is forbidden. Don't have to opens one: you can, "
                  "but you are free not to. They look alike and mean almost the opposite.")},
    ],
}

LISTENINGS = [
    {'file': 'a11_listening1.mp3', 'voice': 'ellen',
     'text': ("Hi Felipe, this is Karen Walsh from loss prevention in Dallas. You asked how we "
              "handle staff bags, so here is our policy in one minute. Every employee has to "
              "leave personal bags in a locker before the shift. You don't have to lock it, but "
              "you should, because we are not responsible for what is inside. At the end of the "
              "shift, the supervisor does a spot check on three people at random. Nobody is "
              "allowed to refuse, and that includes me. The point is not to catch anybody. The "
              "point is that everybody knows it can happen. Since we started, shrinkage in the "
              "warehouse has gone down by almost a third.")},
    {'file': 'a11_listening2.mp3', 'voice': 'italian_f',
     'text': ("Felipe, it's Giulia. Thank you again for the visit. I wrote everything down, and "
              "I have to say, your gate is stricter than ours. In Milan visitors don't have to "
              "sign anything. They just show an ID. I think we should change that. One question "
              "for you. At the docks you said nobody is allowed to stand behind a truck. Is that "
              "a safety rule or a security rule? My director will ask me, and I must give him "
              "the right answer. Also, could you send me a copy of the visitor card? We have to "
              "present a new policy in November, and I would like to copy the good parts.")},
]

EXTRA_AUDIO = [
    {'key': '[order-l11]', 'file': 'pc11_order_visit.mp3', 'voice': 'arthur',
     'text': ("First, Felipe tells Giulia that every visitor has to sign in at the gate. Then he "
              "explains that she has to wear a vest in the warehouse. After that, Giulia asks if "
              "she must wear safety boots, and he says she doesn't have to. Next, he warns her "
              "that she mustn't take photos near the docks. Finally, he gives her some advice: "
              "she should keep her badge where people can see it.")},
]

S = []
S.append(L.s_title(
    1,
    'Abertura (1 min): sem saudação scriptada. Aula de FALA. Hoje ele está do lado de quem '
    'FAZ a regra: prevenção de perdas é uma das quatro áreas dele. Diga o tema e siga.',
    'Chapter 1: The Visitor Policy', 'Rules and', 'Policies',
    'Explaining the rules of your own building to somebody from abroad', IMG_TITLE))

S.append(L.s_warmup(
    2,
    'Warm-up + callback da aula 10 (3 min): na aula 10 ele pediu coisas que ninguém era '
    'obrigado a dar. Hoje é o contrário: ele explica regras que ninguém pode negociar. Peça '
    'que ele responda ao prompt e ESCUTE se ele diz You must not need ou You don\'t must '
    '&mdash; são os erros do Detective (slide 21). Não corrija ainda.',
    'Last Time You Asked.', 'Today You Set the Rules',
    'Last lesson every request left the other person a door. A policy does not. Some doors are '
    'closed, some are open, and some are only a good idea. English has a different word for '
    'each one, and visitors listen for the difference.',
    'Tell me three rules everybody has to follow in your distribution center.'))

S.append(L.s_agenda(
    3,
    'Agenda (1 min): apresente as três missões. Diga que no fim ele vai receber uma visitante '
    'italiana no CD, ao vivo. Passe ao próximo.',
    ['Eight words for rules, theft and the people who check.',
     "Must, have to, should, and the trap between mustn't and don't have to.",
     'Walk a visitor through your building and explain every rule on the way.']))

S.append(L.s_chapter(
    4, 2,
    'Transição vocab (1 min): pista em inglês primeiro, ele tenta a palavra, só então clique.',
    'Chapter 2: Your Words', 'The Words of', 'Loss Prevention',
    '8 words for the rules, the losses and the checks', IMG_VOCAB))

S.append(L.s_vocab(
    5,
    'Vocab reveal 1-4 (4 min): leia a pista, ele tenta, só então clique. CCQ para shrinkage: '
    'Is shrinkage only theft? (Não &mdash; roubo, dano e erro.) CCQ para restricted area: Can '
    'a visitor enter alone? (Não.) Pronúncia: policy tem stress na primeira sílaba (PAH-li-see).',
    '1-4', VOCAB[:4], 1, 0))

S.append(L.s_vocab(
    6,
    'Vocab reveal 5-8 (4 min): mesma dinâmica. CCQ para spot check: Do people know the day of '
    'a spot check? (Não &mdash; é aleatório.) CCQ para to enforce: If a rule is written but '
    'nobody checks it, is it enforced? (Não.) Repare que comply pede WITH.',
    '5-8', VOCAB[4:], 2, 4))

S.append(L.s_blocks(
    7, 2,
    'Consolidar (3 min): ele diz o par em voz alta ANTES de clicar. Certo fica verde, errado '
    'balança. Use o vocab-note como ponte.',
    'Consolidate', 'Match the', 'Meaning', ['vocab']))

S.append(L.s_blocks(
    8, 2,
    'Gap-fill de vocabulário (4 min): banco de palavras na tela. Ele escolhe e LÊ O PARÁGRAFO '
    'INTEIRO em voz alta. É o discurso de boas-vindas do CD dele &mdash; pergunte no fim o que '
    'ele mudaria para ficar igual à realidade da Riachuelo.',
    'Use the Words', 'One Welcome, in', 'One Paragraph',
    ['gapfill'], 'Choose from the word bank, then read the whole paragraph out loud.'))

S.append(L.s_chapter(
    9, 3,
    'Transição gramática (1 min): diga: Some doors are closed, some are open, some are only a '
    'good idea. Passe ao próximo.',
    'Chapter 3: Closed, Open, or a Good Idea', 'Must, Have To,', 'Should',
    "Obligation, prohibition, advice, and the freedom of don't have to", IMG_GRAM))

S.append(L.s_discovery(
    10, 3,
    'Grammar discovery (5 min): leia os quatro exemplos, toque os áudios. Pergunte: Which of '
    'these is forbidden, which is necessary, which is a good idea, and which is free? Só '
    'DEPOIS clique em Reveal the Rule. CCQ: In You don\'t have to wear boots in the office, '
    'can she wear boots if she wants? (Sim &mdash; não é proibido.) In You mustn\'t take '
    'photos, can she? (Não.) Este é o ponto da aula.',
    'modals of obligation',
    [('"Every visitor <span class="accent" style="font-weight:700">has to</span> sign in at the gate."',
      'Every visitor has to sign in at the gate.'),
     ('"You <span class="accent" style="font-weight:700">mustn\'t</span> take photos near the docks."',
      "You mustn't take photos near the docks."),
     ('"You <span class="accent" style="font-weight:700">don\'t have to</span> wear boots in the office."',
      "You don't have to wear boots in the office."),
     ('"You <span class="accent" style="font-weight:700">should</span> keep your badge where people can see it."',
      'You should keep your badge where people can see it.')],
    'rule11',
    ['Form', 'Use it for', 'Example'],
    [['have to / has to', 'A rule that comes from outside: the company, the law, the policy.',
      'Every visitor <strong>has to</strong> sign in.'],
     ['must', 'A strong obligation, often written, or one the speaker feels personally.',
      'I <strong>must</strong> give him the right answer.'],
     ["mustn't / not allowed to", 'Forbidden. The door is closed.',
      "You <strong>mustn't</strong> take photos near the docks."],
     ["don't have to", 'Not necessary. You are free to do it or not.',
      "You <strong>don't have to</strong> wear boots in the office."],
     ['should', 'Advice. A good idea, not a rule.',
      'You <strong>should</strong> keep your badge visible.'],
     ['Past and questions',
      'Must has no past: use had to. <strong>Do</strong> I <strong>have to</strong> sign? '
      'Yesterday I <strong>had to</strong> stay late.']],
    ("Mustn't and don't have to look like twins and mean almost the opposite. One closes the "
     "door, the other opens it.")))

S.append(L.s_oral(
    11, 3,
    'Grammar practice (4 min): ele diz a frase COMPLETA em voz alta e só depois clica. Em cada '
    'item pergunte primeiro: is it forbidden, necessary, free or a good idea? A resposta escolhe '
    'o modal sozinha.',
    'Grammar Practice', 'Closed, Open, or', 'a Good Idea?',
    'Say the full sentence, then click to compare',
    [('Visitors ______ wear a vest in the warehouse. It is the rule.',
      'Visitors have to wear a vest in the warehouse.'),
     ('You ______ stand behind a truck. It is forbidden.',
      "You mustn't stand behind a truck."),
     ('You ______ bring your own vest. We have plenty at the gate.',
      "You don't have to bring your own vest."),
     ('Yesterday the driver ______ wait two hours for the spot check.',
      'Yesterday the driver had to wait two hours for the spot check.')]))

S.append(L.s_listening(
    12, 3,
    'Listening 1 (5 min): a gerente de prevenção de perdas de Dallas, americana, explicando a '
    'política de bolsas dos funcionários. LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. '
    'Ela usa have to, don\'t have to, should e not allowed to em um minuto. Toque duas vezes.',
    1, 'The Bag', 'Policy',
    'A colleague in Dallas explains one rule and the number behind it. Sound first, no text.',
    'a11_listening1.mp3', SLUG,
    [('Where do employees have to leave their bags, and do they have to lock it?',
      "In a locker. They don't have to lock it, but they should."),
     ('What happens at the end of every shift?',
      'The supervisor does a spot check on three people at random.'),
     ('What has happened to shrinkage in the warehouse since they started?',
      'It has gone down by almost a third.')]))

S.append(L.s_chapter(
    13, 4,
    'Transição diálogo (1 min): diga: Now the visit. Giulia works for a retail group in Milan '
    'and she wants to see how your DC works. Passe ao próximo.',
    'Chapter 4: The Tour', 'From the Gate', 'to the Docks',
    'Walking a visitor through your own building', IMG_TOUR))

S.append(L.s_dialogue(
    14, 4,
    'Diálogo (6 min): clique Next Line a cada fala. Nas falas do FELIPE, peça que ELE fale '
    'primeiro, com o texto tapado. Giulia tem sotaque italiano. Aponte a fala 6: ela pergunta '
    'se TEM de usar botas, e a resposta é don\'t have to, não mustn\'t.',
    'From the Gate', 'to the Docks',
    [('felipe', 'F', 'arthur',
      'Welcome, Giulia. Before we go in, every visitor has to sign in here at the gate.'),
     ('giulia', 'G', 'italian_f', 'Of course. Do I have to show my passport?'),
     ('felipe', 'F', 'arthur',
      'Just an ID. And inside the warehouse you have to wear this vest. It is our '
      '<span class="vocab-highlight">policy</span> for everybody, including me.'),
     ('giulia', 'G', 'italian_f', 'No problem. It is a very bright yellow.'),
     ('felipe', 'F', 'arthur', 'That is the idea. The drivers have to see you from far away.'),
     ('giulia', 'G', 'italian_f', 'And the shoes? Must I wear safety boots?'),
     ('felipe', 'F', 'arthur',
      "In the office, you don't have to. In the warehouse, yes, and we have boots at the gate."),
     ('giulia', 'G', 'italian_f', 'Good. Can I take some photos for my director?'),
     ('felipe', 'F', 'arthur',
      "Not near the docks, I'm afraid. Visitors aren't "
      '<span class="vocab-highlight">allowed to</span> take photos in a '
      '<span class="vocab-highlight">restricted area</span>.'),
     ('giulia', 'G', 'italian_f', 'I understand. Why is it so strict?'),
     ('felipe', 'F', 'arthur',
      'Because most of our <span class="vocab-highlight">shrinkage</span> happens between the '
      'truck and the shelf, not in the stores.'),
     ('giulia', 'G', 'italian_f', 'That is the same in Milan. We just never wrote the rule down.')]))

S.append(L.s_comprehension(
    15, 4,
    'Comprehension (3 min): as perguntas são sobre a GIULIA, não sobre ele. Ele responde de '
    'memória ANTES de clicar. Se errar, volte ao diálogo e toque a fala.',
    'Did You Catch It?', 'About', 'Giulia',
    [('What does Giulia want to take for her director?',
      'Some photos of the distribution center.'),
     ('What does she ask about her shoes?',
      'Whether she must wear safety boots.'),
     ('What does she say about the rule in Milan?',
      'It is the same problem there, but they never wrote the rule down.')]))

S.append(L.s_artifact(
    16, 4,
    'Artefato (4 min): o cartão de regras que todo visitante recebe no portão. Peça que ele '
    'LEIA em voz alta, trocando os símbolos por modais. A terceira pergunta é produção: exija '
    'a frase inteira com don\'t have to.',
    'Real Document', 'The Visitor', 'Card',
    'VISITOR RULES &mdash; DC SAO PAULO', 'HOST: FELIPE DIAS',
    [('Gate', 'Sign in with an ID &middot; required'),
     ('Warehouse', 'Yellow vest and safety boots &middot; required'),
     ('Office area', 'Safety boots &middot; not necessary'),
     ('Docks', 'No photos &middot; no standing behind trucks'),
     ('Restricted areas', 'Only with an escort'),
     ('Badge', 'Keep it visible &middot; recommended'),
     ('Spot checks', 'Any vehicle, any day, without warning'),
     ('Questions', 'Ask your host')],
    [('What does every visitor have to do at the gate?',
      'Sign in with an ID.'),
     ('Which two things are forbidden at the docks?',
      'Taking photos and standing behind a truck.'),
     ('Say the rule for the office area with don\'t have to.',
      "You don't have to wear safety boots in the office area.")]))

S.append(L.s_listening(
    17, 4,
    'Listening 2 (5 min): sotaque italiano, a mesma Giulia do diálogo, depois da visita. LEIA '
    'AS PERGUNTAS COM ELE ANTES do play. Ela faz uma pergunta difícil no meio &mdash; peça que '
    'ele RESPONDA a pergunta dela no fim, em voz alta. Toque duas vezes.',
    2, 'Giulia Writes', 'It All Down',
    'A message left after the visit, with one hard question. Sound first, no text.',
    'a11_listening2.mp3', SLUG,
    [('How is the gate in Milan different?',
      "Visitors don't have to sign anything. They just show an ID."),
     ('What does Giulia want to know about the docks?',
      'Whether the rule about standing behind a truck is a safety rule or a security rule.'),
     ('Why does she want a copy of the visitor card?',
      'They have to present a new policy in November.')]))

S.append(L.s_blocks(
    18, 5,
    'Quick Fire (6 min): uma situação por vez. Ele responde EM VOZ ALTA antes de abrir as '
    'Tips. Exija a REGRA e o MOTIVO em toda resposta. Regra sem motivo soa como ordem; motivo '
    'sem regra não protege ninguém.',
    'Chapter 5: Real Talk', 'Answer on the', 'Spot', ['quickfire'],
    'Read each situation. Answer out loud first, then tap Tips for support language.'))

S.append(L.s_chapter(
    19, 6,
    'Transição prática (1 min): diga: Now you explain your own rules. Three rounds, less help '
    'each time.',
    'Chapter 6: Your Turn', 'From Guided to', 'Free',
    'Three rounds, less help each time', IMG_TURN))

S.append(L.s_blocks(
    20, 6,
    'Scenarios + Rephrase (5 min): nos cenários, exija pelo menos um modal de cada tipo. No '
    'rephrase ele escolhe o modal pela pista entre parênteses. Sem gabarito na tela.',
    'Say It Yourself', 'Three Situations,', 'Full Answers', ['practice']))

S.append(L.s_error(
    21, 6,
    'Detective (4 min): leia cada frase errada e pergunte What is wrong here? Ele corrige EM '
    'VOZ ALTA antes de clicar. Score no topo.',
    [('Every visitor have to sign in at the gate.', 'Every visitor has to sign in at the gate.'),
     ('You must to wear a vest in the warehouse.', 'You must wear a vest in the warehouse.'),
     ('Last week we must stop two trucks.', 'Last week we had to stop two trucks.'),
     ('Do I must show my passport?', 'Do I have to show my passport?')]))

S.append(L.s_roleplay(
    22, 6,
    'Role-play 1 &mdash; guiado (4 min): você é um visitante no portão. Faça três perguntas: '
    'tenho de assinar? posso fotografar? preciso de bota no escritório? Ele responde usando as '
    'chips.',
    'Role-Play 1 &mdash; Guided', 'At the', 'Gate',
    'Situation',
    'A visitor arrives at your distribution center. Answer their questions about the rules: '
    'what they have to do, what they are not allowed to do, and what they do not need to worry '
    'about.',
    ['has to sign in', 'have to wear', "aren't allowed to", "don't have to", 'should keep']))

S.append(L.s_roleplay(
    23, 6,
    'Role-play 2 &mdash; semi-livre (4 min): você é um fornecedor antigo que acha a spot check '
    'uma ofensa. Insista duas vezes: but we have worked together for ten years. Ele tem de '
    'manter a regra sem perder o fornecedor.',
    'Role-Play 2 &mdash; Semi-Free', 'The Supplier Who', 'Wants an Exception',
    'Situation',
    'A supplier of ten years asks you to stop the spot checks on their trucks. Keep the rule, '
    'explain why everybody has to comply, and offer one thing that makes the check easier for '
    'them.',
    ['has to comply with', 'no exceptions', 'should', 'instead']))

S.append(L.s_roleplay(
    24, 6,
    'Role-play 3 &mdash; livre (5 min): a missão da aula. ZERO pistas na tela. Não interrompa. '
    'Cronometre noventa segundos e conte quantos modais DIFERENTES ele usou. Diga o número no '
    'fim. CELEBRE.',
    'Role-Play 3 &mdash; Free', 'Ninety Seconds,', 'No Help',
    'Scenario',
    'Take a visitor on a tour of one of your real buildings, from the gate to the most '
    'restricted area. On the way, explain what they have to do, what they must not do, what '
    'they do not have to do, and one piece of advice. Finish with the reason the rules exist. '
    'Ninety seconds, no notes.',
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
    'câmera. São as cinco frases da próxima visita que ele receber.',
    'Say It with', 'Confidence',
    ['Every visitor has to sign in at the gate.',
     'You have to wear a vest inside the warehouse.',
     "You don't have to wear safety boots in the office.",
     "I'm afraid visitors aren't allowed to take photos here.",
     'You should keep your badge where people can see it.']))

S.append(L.s_checklist(
    27,
    'Checklist (2 min): diga: Click each item if you feel confident. Leia cada item em voz '
    'alta. Os 5 checks marcados fecham a aula 11.',
    11,
    ['I can explain the rules of my building to a visitor, in English.',
     'I use have to for rules and should for advice.',
     "I never say mustn't when I mean don't have to.",
     'I use had to for an obligation in the past.',
     'I know the words: policy, shrinkage, shoplifting, restricted area, to comply with, spot '
     'check, to enforce, to be allowed to.']))

S.append(L.s_badge(
    28,
    'Encerramento (2 min): diga: Lesson 11 complete, Felipe. Homework ORALMENTE, nunca escrito '
    'na tela: gravar noventa segundos explicando as regras de um prédio real dele a um '
    'visitante e mandar no WhatsApp. Próxima aula: Two Suppliers, One Decision.',
    11, 'Rules and Policies',
    'You walked an Italian visitor from the gate to the docks today, Felipe, and every rule had '
    'a reason.',
    'Two Suppliers, One Decision'))

SLIDES = '\n'.join(S)

SPEC = {
    'n': N,
    'title': 'Rules and Policies -- Explaining the Rules',
    'short_title': 'Rules and Policies',
    'menu_desc': ('Speaking lesson: a visitor at the distribution center, the rules of the '
                  "building, and the trap between mustn't and don't have to"),
    'grammar_point': 'modals of obligation',
    'characters': {'felipe': 'arthur', 'giulia': 'italian_f'},
    'phases': ['The Visitor Policy', 'Your Words', 'Closed, Open, or a Good Idea', 'The Tour',
               'Real Talk', 'Your Turn', 'Wrap-Up'],
    'inclass_blocks': INCLASS_BLOCKS,
    'listenings': LISTENINGS,
    'extra_audio': EXTRA_AUDIO,
    'vocab': VOCAB,
    'hub_img': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=600&q=80',
    'desc': ('The words of loss prevention: policy, shrinkage, shoplifting, restricted area, to '
             'comply with, spot check, to enforce, to be allowed to. Structure: must, have to, '
             "should, mustn't and don't have to. Mission: walk a visitor through your building "
             'and explain every rule on the way.'),
    'context_paras': [
        'Welcome to the distribution center. Every visitor <strong>has to</strong> sign in at '
        'the gate, and inside the warehouse you <strong>have to</strong> wear a yellow vest. '
        'Those are not my rules. They are the policy, and they apply to everybody, including '
        'me. You <strong>mustn\'t</strong> take photos near the docks, and you '
        '<strong>mustn\'t</strong> stand behind a truck. Those two are closed doors.',
        'Other things are open. In the office area you <strong>don\'t have to</strong> wear '
        'safety boots: you can, but nobody will ask you to. And some things are only a good '
        'idea. You <strong>should</strong> keep your badge where people can see it, because the '
        'security team will stop you if they cannot. One more thing: <em>must</em> has no past. '
        'Last week a driver refused a spot check, and we <strong>had to</strong> stop his truck '
        'for two hours.'],
    'context_quiz': [
        ("What does <em>you don't have to wear safety boots</em> mean?",
         [('Nobody is allowed to wear safety boots in the office area, not even visitors.', False),
          ('Boots are not necessary in the office, but you are free to wear them.', True),
          ('You should wear boots in the office.', False)]),
        ('Which two things are forbidden near the docks?',
         [('Taking photos and standing behind a truck.', True),
          ('Wearing a vest and showing an ID.', False),
          ('Signing in and keeping the badge visible.', False)]),
        ('Why does the text say <em>we had to stop his truck</em> and not <em>we must stop</em>?',
         [('Because had to sounds more polite and more friendly when you talk to a visitor.', False),
          ('Because it was not really necessary.', False),
          ('Because must has no past form, so a past obligation takes had to.', True)]),
    ],
    'tip_title': 'Modals of Obligation',
    'tip_intro': ('Four kinds of door: closed, necessary, open, and only a good idea. Each one '
                  'has its own word, and visitors listen for the difference.'),
    'tip_rows': [
        ['have to / has to', 'A rule from outside: the company, the policy, the law.',
         'Every visitor <strong>has to</strong> sign in.'],
        ['must', 'A strong obligation, often written, or one the speaker feels personally.',
         'I <strong>must</strong> call him back today.'],
        ["mustn't / not allowed to", 'Forbidden. The door is closed.',
         "You <strong>mustn't</strong> take photos near the docks."],
        ["don't have to", 'Not necessary. You are free to do it or not.',
         "You <strong>don't have to</strong> wear boots in the office."],
        ['should', 'Advice. A good idea, not a rule.',
         'You <strong>should</strong> keep your badge visible.'],
        ['had to', 'The past of both must and have to.',
         'Last week we <strong>had to</strong> stop a truck.'],
    ],
    'tip_note': ("No to after must, mustn't or should: <em>you must wear</em>, never <em>you "
                 'must to wear</em>. And in questions, use have to: <em>Do I have to sign?</em>'),
    'blanks': [
        ('Every visitor ', 'has to', 'Hint: two words. A rule from the company, third person.',
         'Every visitor has to sign in at the gate.', ' sign in at the gate.'),
        ('You ', "mustn't", 'Hint: one word with an apostrophe. It is forbidden.',
         "You mustn't take photos near the docks.", ' take photos near the docks.'),
        ('You ', "don't have to", 'Hint: three words. Not necessary, but not forbidden.',
         "You don't have to wear safety boots in the office.",
         ' wear safety boots in the office.'),
        ('Last week we ', 'had to', 'Hint: two words. The past of must.',
         'Last week we had to stop a truck for two hours.', ' stop a truck for two hours.'),
        ('Twice a week we do a ', 'spot check',
         'Hint: two words. A quick inspection without warning.',
         'Twice a week we do a spot check on two trucks.', ' on two trucks.'),
        ('Every supplier has to ', 'comply with',
         'Hint: two words. To follow a rule or a standard.',
         'Every supplier has to comply with our safety standards.',
         ' our safety standards.'),
    ],
    'order_title': 'Put the Visit in Order',
    'order_intro': 'Listen first, then put the five parts of the visit in the order you hear '
                   'them.',
    'order': [
        (3, "After that, Giulia asks if she must wear safety boots, and he says she doesn't "
            'have to.'),
        (5, 'Finally, he gives her some advice: she should keep her badge where people can see '
            'it.'),
        (1, 'First, Felipe tells Giulia that every visitor has to sign in at the gate.'),
        (2, 'Then he explains that she has to wear a vest in the warehouse.'),
        (4, "Next, he warns her that she mustn't take photos near the docks."),
    ],
    'speech': [
        'Every visitor has to sign in at the gate.',
        'You have to wear a vest inside the warehouse.',
        "You don't have to wear safety boots in the office.",
        "I'm afraid visitors aren't allowed to take photos here.",
        'You should keep your badge where people can see it.',
    ],
    'quiz_intro': 'You are explaining the rules of your building to a visitor. Choose the best '
                  'thing to say.',
    'quiz': [
        ('A visitor asks if she needs safety boots in the office. She does not. You say:',
         [("You mustn't wear safety boots in the office, only in the warehouse area.", False),
          ('You must to wear safety boots only in the warehouse.', False),
          ("You don't have to wear them in the office, only in the warehouse.", True)]),
        ('A visitor starts taking photos of the docks. You say:',
         [("I'm afraid you aren't allowed to take photos here.", True),
          ("You don't have to take photos here, it is the policy of the company.", False),
          ('You should not to take photos here.', False)]),
        ('You want to talk about a rule you followed last week. You say:',
         [('Last week we must stop a truck.', False),
          ('Last week we had to stop a truck.', True),
          ('Last week we have to stop a truck.', False)]),
        ('A colleague asks for your opinion, not a rule. You say:',
         [('You have to talk to the supervisor.', False),
          ("You mustn't talk to the supervisor before you talk to me first.", False),
          ('You should talk to the supervisor first.', True)]),
    ],
    'think': ('Think about one real building you are responsible for: a store, the distribution '
              'center or the head office. Record about ninety seconds. Imagine a visitor who '
              'has never been there. Explain what they have to do when they arrive, two things '
              "they mustn't do, one thing they don't have to worry about, and one piece of "
              'advice. Then tell them one rule you had to enforce in the past, and why. Use at '
              'least four words from this lesson. Do not stop to correct yourself.'),
    'media': [
        ('youtube', 'grammar', 'Grammar Video',
         "'Have to' and 'must' -- 6 Minute Grammar, BBC Learning English",
         'Six minutes on the two obligations, where they come from and how they sound in real '
         'speech. Connection to Lesson 11: it is the core of the rules you explained to Giulia.',
         'Tip: pause after each example and say whether the rule comes from outside or from the '
         'speaker.',
         'https://www.youtube.com/watch?v=HUXXgVElADg', 'Watch on YouTube'),
        ('youtube', 'trap', 'Grammar Video',
         "Mustn't vs don't have to -- English In A Minute, BBC Learning English",
         'One minute on the trap of the lesson: the two forms that look alike and mean almost '
         'the opposite. Connection to Lesson 11: the safety boots question, in sixty seconds.',
         'Tip: watch it twice, then say one closed door and one open door from your own '
         'building.',
         'https://www.youtube.com/watch?v=tFirN40-6mY', 'Watch on YouTube'),
        ('video', 'safety', 'Video Lesson',
         'Health and safety -- English at Work, BBC Learning English',
         'A short office drama about rules nobody wants to follow, with the phrases people '
         'really use. Connection to Lesson 11: how to explain a rule without sounding like a '
         'policeman.',
         'Tip: write down every sentence with have to, must or should, and decide which kind of '
         'door it is.',
         'https://www.youtube.com/watch?v=zL4PI-pWfi8', 'Watch on YouTube'),
    ],
}


if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    L.emit(SPEC, SLIDES, ROOT, HERE, slide_count=count)
