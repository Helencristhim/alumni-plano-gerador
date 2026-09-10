#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aba EXPRESSIONS: o ingles falado que o americano usa de verdade no dia a dia.

O QUE A HELEN PEDIU (10/09/2026)
--------------------------------
"Uma aba so com expressions que americanos realmente usam no dia a dia", com
TEXTO, AUDIO e EXPLICACAO, no espirito do infografico "12 Idioms about TIME"
que ela mandou. Ela deu sete exemplos -- Sounds good, No rush, It's all good,
That checks out, I'd rather not, My bad, I'm beat -- e disse que eram exemplos.
Os sete estao aqui, cada um no grupo em que cabe, mais dezessete da mesma
familia: expressao curta, de conversa, que o Diego vai ouvir no corredor do
hospital e no supermercado, e que nao se aprende em lista de vocabulario.

Explicacao EM INGLES, por ordem dela e pela REGRA 13 (o Diego e B1: zero
portugues na tela).

DECISOES QUE NAO SE LEEM NO CODIGO
----------------------------------
1. CADA EXPRESSAO E UM `.vocab-card-pc`. Nao inventei componente: esse card ja
   existe no hub, ja tem o Listen de 44px, ja fica verde quando o aluno ouve,
   ja conta como unidade de progresso e o `loadState` ja o restaura pelo texto
   da palavra. Componente novo teria de trazer CSS novo -- e CSS vive no <head>,
   FORA das abas, onde o `insert_hub_extras` (com razao) nao deixa escrever.

2. DOIS AUDIOS POR CARD: a expressao sozinha e a expressao dentro da frase. E a
   diferenca entre saber o que "my bad" quer dizer e saber COMO soa quando
   alguem diz. Os dois em voz americana de verdade (ver gen_audio_extras.py, que
   para esta aba usa Arthur e Sarah, os dois com accent=american na ElevenLabs).

3. TUDO CONTRAIDO. "I'm beat", nunca "I am beat"; "It's all good", nunca "It is
   all good". As outras abas escrevem por extenso, e esta e a excecao de
   proposito: a aba inteira existe para ensinar como a frase SOA. O `data-alt`
   guarda a forma por extenso, entao quem digitar sem apostrofo tambem acerta.

4. O MATCHING NAO REPETE A EXPLICACAO DO CARD. Se repetisse, o exercicio seria
   copiar de cima. Entao a coluna da direita traz a SITUACAO ("Someone offers
   you more coffee and you do not want it") e o aluno escolhe a expressao.

5. O FILL-IN USA CONVERSA NOVA, nao a frase do card, e fecha com o proprio
   audio: `antes + data-answer + depois` normalizado da exatamente o
   `data-phrase` (regra do check_preclass_blanks).

6. TETO DE NIVEL B1 (aulas 1..10 dele): present simple/continuous, passiva,
   past simple, modais, relative clauses, past perfect, indirect questions,
   condicionais 0/1/2, will/going to. Nada fora disso.

USO: python3 build_expressions.py   (escreve expressions.html ao lado)
"""
import os
import re

from build_extras import (H3, INTRO, ITAL, esc, lesson_card, matching,
                          painel_aba, pronunciation, quiz, secao)

AQUI = os.path.dirname(os.path.abspath(__file__))

# O margin-bottom repete o 1.2rem do `.exercise-section`: a nota entra no MESMO
# ritmo vertical dos blocos de exercicio, em vez de encostar no de baixo.
NOTA = ('margin:.2rem 0 1.2rem;padding:.9rem 1.1rem;background:var(--accent-dim);'
        'border-left:3px solid var(--accent);border-radius:0 8px 8px 0;'
        'font-size:.82rem;line-height:1.65;color:var(--text-mid)')

# Botao pequeno para ouvir a FRASE do card. O Listen grande (`.audio-btn`) fica
# com a expressao; este e secundario de proposito -- mesma familia visual, peso
# menor, e ainda assim com area de toque de 44px.
BTN_EX = ('display:inline-flex;align-items:center;gap:6px;margin:.45rem 0 0;'
          'padding:8px 14px;min-height:44px;background:transparent;color:var(--accent);'
          'border:1px solid var(--accent);border-radius:8px;cursor:pointer;'
          'font:600 .72rem/1 "Inter",sans-serif')


def cartao(expr, sentido, exemplo):
    """Um `.vocab-card-pc` com a expressao, o sentido em ingles e a frase real."""
    return (
        '        <div class="vocab-card-pc">\n'
        '          <div class="vocab-card-content">\n'
        '            <div class="vocab-card-header"><span class="vocab-card-word">%s</span>'
        '<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">%s</span></div>\n'
        '            <div class="vocab-card-example">&ldquo;%s&rdquo;</div>\n'
        '            <button style="%s" data-speak="%s" onclick="speakText(this.dataset.speak,this)">'
        '&#9654;&nbsp;Hear it in a sentence</button>\n'
        '          </div>\n'
        '          <button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button>\n'
        '        </div>' % (esc(expr), esc(sentido), esc(exemplo), BTN_EX,
                            esc(exemplo), esc(expr)))


def bloco_cartoes(itens):
    return ('    <div class="exercise-section">\n'
            '      <div class="section-header-row"><h4>Stage 1: The expressions</h4>'
            '<span class="badge badge-vocab">Listen</span></div>\n'
            '      <p style="%s">Tap Listen to hear the expression on its own, then hear it '
            'inside a real sentence. The card turns green once you have listened.</p>\n'
            '      <div class="vocab-cards">\n%s\n      </div>\n'
            '    </div>' % (ITAL, '\n'.join(cartao(*i[:3]) for i in itens)))


def nota(texto):
    return ('    <div style="%s"><strong style="color:var(--accent)">Careful.</strong> %s</div>'
            % (NOTA, esc(texto)))


# A FALA DO OUTRO SAI DE DENTRO DA FRASE DO EXERCICIO.
#
# O `check_preclass_blanks` cobra que `texto na tela + data-answer` de EXATAMENTE
# o `data-phrase` -- e ele tem razao: o Listen tem de tocar o que esta escrito.
# Como aqui o exercicio e uma CONVERSA, a fala do interlocutor ficaria dentro da
# mesma `.fill-blank-sentence` e o audio teria de trazer as duas vozes numa so.
#
# Entao a fala do outro vira uma LINHA A PARTE, fora da frase do exercicio: a
# tela continua sendo o dialogo inteiro, e o `.fill-blank-sentence` fica com a
# resposta do Diego -- exatamente a frase que o MP3 toca.
QUEBRA_ANTES = re.compile(r'^(.*[.?!]")\s+(".*)$', re.S)
QUEBRA_DEPOIS = re.compile(r'^(.*?")\s+(".*)$', re.S)

FALA_OUTRO = ('font-size:.8rem;color:var(--text-dim);font-style:italic;'
              'margin:0 0 .4rem;line-height:1.5')


def fill_in_dialogo(itens):
    out = []
    for it in itens:
        antes, resp, depois, dica, frase = it[:5]
        alt = (' data-alt="%s"' % esc(it[5])) if len(it) > 5 else ''
        ctx_antes = ctx_depois = ''
        m = QUEBRA_ANTES.match(antes)
        if m:
            ctx_antes, antes = m.group(1), m.group(2)
        m = QUEBRA_DEPOIS.match(depois)
        if m:
            depois, ctx_depois = m.group(1), m.group(2)
        # As aspas ficam SO na fala do outro. A linha do exercicio e a fala do
        # Diego: sem aspas, o olho separa quem diz o que sem precisar de rotulo.
        antes = antes.lstrip('"')
        depois = depois.rstrip('"')
        linhas = []
        if ctx_antes:
            linhas.append('      <div style="%s">%s</div>' % (FALA_OUTRO, esc(ctx_antes)))
        linhas.append(
            '      <div class="fill-blank-sentence">%s'
            '<input class="blank-input" data-answer="%s"%s data-hint="%s" data-phrase="%s" placeholder="___">'
            '%s</div>' % (esc(antes), esc(resp), alt, esc(dica), esc(frase), esc(depois)))
        if ctx_depois:
            linhas.append('      <div style="%s">%s</div>' % (FALA_OUTRO, esc(ctx_depois)))
        out.append('      <div class="fill-blank-item">\n%s\n'
                   '      <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                   '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
                   % '\n'.join(linhas))
    return '\n'.join(out)


# ============================================================== O CONTEUDO
# Cada item: (expressao, sentido em ingles, frase de exemplo, situacao do matching)

G1 = [
    ('Sounds good',
     'you agree with the plan the other person just suggested',
     "Sounds good. I'll see you at the front desk at seven.",
     'Someone suggests a plan and you are happy with it'),
    ('Works for me',
     'the time or the plan fits your schedule too',
     'Thursday at two works for me, if it works for you.',
     'Someone offers a day for a meeting and you can make it'),
    ("I'd rather not",
     'a polite no to something you do not want to do',
     "I'd rather not drive at night, if that's all right.",
     'You are asked to do something you would prefer to avoid'),
    ("I'm good",
     'a soft no, thank you: you do not need anything more',
     "More coffee? I'm good, thanks.",
     'Someone offers you more coffee and you do not want it'),
    ('Let me get back to you',
     'you need time before you give your answer',
     'Let me get back to you after I check the schedule.',
     'You cannot answer yet and you want to check first'),
    ('No rush',
     'there is no hurry, so the other person can take their time',
     'No rush, send it to me whenever you finish.',
     'You ask for something and the deadline is soft'),
]

G2 = [
    ('My bad',
     'a light way to admit a small mistake that was yours',
     'My bad, I sent that message to the wrong group.',
     'You did something small wrong and you own it'),
    ("It's all good",
     'there is no problem, so the other person can relax',
     "It's all good, we still have time to fix it.",
     'Someone apologises to you and you want to close the subject'),
    ('No worries',
     'a friendly answer to sorry or to thank you',
     'No worries, it happens to everyone.',
     'A colleague thanks you for a small favour'),
    ('It happens',
     'mistakes like this are normal and nobody is in trouble',
     'You forgot the file? It happens.',
     'Someone feels bad about a mistake that is not serious'),
    ("I'm on it",
     'you are starting that task right now',
     "I'm on it. I'll call the lab in two minutes.",
     'Your boss asks for something and you start immediately'),
    ('Let me double-check',
     'you will confirm the detail before you say it for sure',
     'Let me double-check the dose before you give it.',
     'You are almost sure, but the detail is too important to guess'),
]

G3 = [
    ("I'm beat",
     'very tired, with no energy left at all',
     "I'm beat. That shift was twelve hours long.",
     'You finish a long shift and you are exhausted'),
    ("I'm swamped",
     'you have far too much work at the same time',
     "I'm swamped today. Can we talk tomorrow?",
     'Your day is full and you cannot take one more thing'),
    ('Long day?',
     'small talk to somebody who looks tired',
     'Long day? You look like you need a break.',
     'A colleague looks tired and you want to say something kind'),
    ('I could use a coffee',
     'a light way to say that you would like one',
     'I could use a coffee before rounds.',
     'You want a coffee and you are hinting, not asking'),
    ("How's it going?",
     'an everyday hello, not a real question about your life',
     "Hey, how's it going?",
     'You pass a colleague in the hallway and say hello'),
    ('Same here',
     'you feel the same way, or you did the same thing',
     'Same here, I slept badly too.',
     'Someone says something and it is true for you as well'),
]

G4 = [
    ('That checks out',
     'the information fits what you already know, so it makes sense',
     'The dates match the chart, so that checks out.',
     'The numbers agree with each other and nothing looks wrong'),
    ('Good call',
     'that was a smart decision',
     'Good call. That test saved us two days.',
     'Someone made a decision that turned out to be right'),
    ('A heads-up',
     'a warning in advance, so that nobody is surprised',
     'Just a heads-up: the clinic closes early on Friday.',
     'You tell people something before it happens'),
    ('Circle back',
     'come back to a subject later, when there is time for it',
     "Let's circle back to that after the meeting.",
     'A subject is important but this is not the moment'),
    ('Keep me posted',
     'tell me the news as soon as you have it',
     'Keep me posted if anything changes overnight.',
     'You want to be told when the situation changes'),
    ('Off the top of my head',
     'from memory, without checking, so it may not be exact',
     'Off the top of my head, I think it was three weeks ago.',
     'You answer from memory and you want to mark it as approximate'),
]

# --- fill-in: CONVERSAS NOVAS (antes, resposta, depois, hint, frase completa[, alt])
F1 = [
    ('"Let\'s meet at the cafe on the corner." "', 'Sounds good',
     '. See you there."',
     'Hint: two words, and the first one is a verb about how a plan seems',
     'Sounds good. See you there.'),
    ('"Can you send it tomorrow?" "Sure, that ', 'works for me',
     '."',
     'Hint: three words, and the first one is the verb to work',
     'Sure, that works for me.'),
    ('"Would you like to swap shifts?" "', "I'd rather not",
     ', but thanks for asking."',
     'Hint: three words, and the middle one is rather',
     "I'd rather not, but thanks for asking.",
     'I would rather not'),
    ('"Do you want a hand with that?" "', "I'm good",
     ', thanks."',
     'Hint: two words: I am, said as one short word, plus an adjective',
     "I'm good, thanks.",
     'I am good'),
    ('"When do you need the report?" "', 'No rush',
     ', any time this week."',
     'Hint: two words, and the second one means hurry',
     'No rush, any time this week.'),
    ('"I don\'t have an answer yet. ', 'Let me get back to you',
     ' this afternoon."',
     'Hint: five words that ask for time before you answer',
     "I don't have an answer yet. Let me get back to you this afternoon."),
]

F2 = [
    ('"', 'My bad', ', I wrote the wrong date on the form."',
     'Hint: two words, and the second one is the opposite of good',
     'My bad, I wrote the wrong date on the form.'),
    ('"Sorry I\'m late." "', "It's all good",
     ', we haven\'t started yet."',
     'Hint: three words, and the middle one is all',
     "It's all good, we haven't started yet.",
     'It is all good'),
    ('"Thanks for covering for me." "', 'No worries',
     ', you\'d do the same for me."',
     'Hint: two words, and the second one is the plural of worry',
     "No worries, you'd do the same for me."),
    ('"I forgot to sign it." "', 'It happens',
     '. Sign it now and we\'re fine."',
     'Hint: two words, present simple of the verb to happen',
     "It happens. Sign it now and we're fine."),
    ('"Could you call the pharmacy?" "', "I'm on it",
     '. I\'ll do it before lunch."',
     'Hint: three words: I am, said as one short word, plus on plus it',
     "I'm on it. I'll do it before lunch.",
     'I am on it'),
    ('"Are you sure about the dose?" "', 'Let me double-check',
     ' before you give it."',
     'Hint: three words, and the last one has a hyphen and means to check twice',
     'Let me double-check before you give it.'),
]

F3 = [
    ('"How was the night shift?" "', "I'm beat",
     '. I need eight hours of sleep."',
     'Hint: two words, and the second one is a one-syllable word for exhausted',
     "I'm beat. I need eight hours of sleep.",
     'I am beat'),
    ('"Can you look at this today?" "Sorry, ', "I'm swamped",
     '. Tomorrow morning?"',
     'Hint: two words, and the second one means covered with work',
     "Sorry, I'm swamped. Tomorrow morning?",
     'I am swamped'),
    ('"You look tired. ', 'Long day?',
     '" "The longest."',
     'Hint: two words and a question mark, and the first one is the opposite of short',
     'You look tired. Long day?'),
    ('"There\'s a coffee machine downstairs." "Good, ', 'I could use a coffee',
     '."',
     'Hint: five words that start with I could',
     "Good, I could use a coffee."),
    ('"Hey, ', "how's it going?", '" "Not bad, and you?"',
     'Hint: four words, and How is comes first, said as one short word',
     "Hey, how's it going?",
     'how is it going?'),
    ('"I\'m nervous about the exam." "', 'Same here',
     '. I\'ve been studying all week."',
     'Hint: two words, and the first one means not different',
     "Same here. I've been studying all week."),
]

F4 = [
    ('"The two reports say the same thing, so ', 'that checks out',
     '."',
     'Hint: three words, and the middle one is the verb to check',
     'The two reports say the same thing, so that checks out.'),
    ('"I asked for a second opinion." "', 'Good call',
     '. That was the right thing to do."',
     'Hint: two words, and the second one is a noun about a decision',
     'Good call. That was the right thing to do.'),
    ('"Just ', 'a heads-up', ': the lab closes at four today."',
     'Hint: three words, and the last one has a hyphen and means warning',
     'Just a heads-up: the lab closes at four today.'),
    ('"We\'re out of time, so let\'s ', 'circle back',
     ' to this on Monday."',
     'Hint: two words, and the first one is what a plane does over an airport',
     "We're out of time, so let's circle back to this on Monday."),
    ('"I\'ll call you when the results arrive." "Please do, and ', 'keep me posted',
     '."',
     'Hint: three words, and the last one is the past participle of to post',
     'Please do, and keep me posted.'),
    ('"How long ago was the surgery?" "', 'Off the top of my head',
     ', about a year."',
     'Hint: six words that start with Off the top',
     'Off the top of my head, about a year.'),
]

# --- quiz: escolher a resposta natural (o que um americano diria) ---
Q1 = [
    ('Your colleague says: "Let\'s start at eight instead of nine." You agree. '
     'What do you say?',
     [('Sounds good.', True), ("I'm good.", False),
      ('No rush.', False), ('Same here.', False)]),
    ('Someone offers you a second sandwich and you do not want it. '
     'What is the natural answer?',
     [("I'm good, thanks.", True), ("I'd rather not, thanks.", False),
      ('It happens.', False), ('Works for me.', False)]),
    ('A friend asks you to speak at an event and you really do not want to. '
     'What is polite?',
     [("I'd rather not, but thanks for asking.", True),
      ("I'm good.", False), ('No worries.', False), ('That checks out.', False)]),
    ('You need to check the schedule before you answer. What do you say?',
     [('Let me get back to you.', True), ('No rush.', False),
      ('Good call.', False), ('Same here.', False)]),
]

Q2 = [
    ('You sent a file to the wrong person. What do you say first?',
     [('My bad.', True), ('It happens.', False),
      ('No worries.', False), ('That checks out.', False)]),
    ('A colleague says "I\'m so sorry, I forgot to call you back." '
     'What do you answer?',
     [('No worries, it happens.', True), ('My bad.', False),
      ("I'm on it.", False), ('Long day?', False)]),
    ('Your boss asks you to call the lab right now. What shows that you are starting?',
     [("I'm on it.", True), ('Let me get back to you.', False),
      ('No rush.', False), ("I'm good.", False)]),
    ('The dose looks right, but you want to confirm it before it is given. '
     'What do you say?',
     [('Let me double-check.', True), ('That checks out.', False),
      ("It's all good.", False), ('Good call.', False)]),
]

Q3 = [
    ('You finished a twelve-hour shift and you have no energy left. What do you say?',
     [("I'm beat.", True), ("I'm swamped.", False),
      ('Same here.', False), ('No rush.', False)]),
    ('A colleague asks for one more task and your day is already full. What fits?',
     [("I'm swamped today.", True), ("I'm beat.", False),
      ('It happens.', False), ('Good call.', False)]),
    ('Somebody says "Hey, how\'s it going?" in the hallway. '
     'What is the normal answer?',
     [('Not bad, and you?', True),
      ("It's going to the second floor.", False),
      ("I'd rather not.", False), ('Let me double-check.', False)]),
    ('Your colleague says "I didn\'t sleep well either." '
     'What does Same here mean?',
     [('The same thing is true for me.', True),
      ("I'm in the same room.", False),
      ('I do not agree with you.', False), ('Say it again, please.', False)]),
]

Q4 = [
    ('The chart and the lab report agree with each other. What do you say?',
     [('That checks out.', True), ('Good call.', False),
      ('Keep me posted.', False), ('It happens.', False)]),
    ('You want your colleague to tell you if anything changes tonight. '
     'What do you say?',
     [('Keep me posted.', True), ('Circle back.', False),
      ('No rush.', False), ('My bad.', False)]),
    ('You want to warn the team that the clinic closes early. How do you start?',
     [('Just a heads-up:', True), ('Off the top of my head,', False),
      ("It's all good:", False), ('Same here:', False)]),
    ('You answer from memory and you are not completely sure. How do you mark that?',
     [('Off the top of my head,', True), ('That checks out,', False),
      ('Good call,', False), ("I'm on it,", False)]),
]

GRUPOS = [
    dict(id='ae-group-1', n=1, itens=G1, fills=F1, quiz=Q1, seed=5100,
         img='https://images.unsplash.com/photo-1543269865-cbf427effbad?w=600&q=80',
         numero='Everyday Expressions 01',
         titulo='Yes, No, and Not Right Now',
         desc='The six short answers you need every day: agreeing to a plan, turning '
              'something down without sounding rude, and buying yourself time before '
              'you answer.',
         nota='All six are informal and completely normal at work. The one to watch is '
              '"I\'m good": it means no, thank you, not "I am fine". If you want to '
              'accept, say "Yes, please".',
         fala=["Sounds good. I'll see you at the front desk at seven.",
               "I'd rather not drive at night, if that's all right.",
               'Let me get back to you after I check the schedule.',
               'No rush, send it to me whenever you finish.']),
    dict(id='ae-group-2', n=2, itens=G2, fills=F2, quiz=Q2, seed=5200,
         img='https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&q=80',
         numero='Everyday Expressions 02',
         titulo='When Something Goes Wrong',
         desc='How Americans admit a small mistake, and how they tell you to stop '
              'apologising. Short, light and said fast, so that the moment passes.',
         nota='"My bad" is for small mistakes between colleagues. If the mistake is '
              'serious, or you are talking to a patient or a family, say "I\'m sorry" '
              'or "I apologise" instead.',
         fala=['My bad, I sent that message to the wrong group.',
               'No worries, it happens to everyone.',
               "I'm on it. I'll call the lab in two minutes.",
               'Let me double-check the dose before you give it.']),
    dict(id='ae-group-3', n=3, itens=G3, fills=F3, quiz=Q3, seed=5300,
         img='https://images.unsplash.com/photo-1517502884422-41eaead166d4?w=600&q=80',
         numero='Everyday Expressions 03',
         titulo='How You Feel, and Small Talk',
         desc='The hallway conversation: how tired you are, how full your day is, and '
              'the two or three lines that answer a greeting without stopping to talk.',
         nota='"How\'s it going?" is a greeting, not a question about your life. Two '
              'or three words back is enough: "Good, you?" or "Not bad, and you?".',
         fala=["I'm beat. That shift was twelve hours long.",
               "I'm swamped today. Can we talk tomorrow?",
               'I could use a coffee before rounds.',
               'Same here, I slept badly too.']),
    dict(id='ae-group-4', n=4, itens=G4, fills=F4, quiz=Q4, seed=5400,
         img='https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80',
         numero='Everyday Expressions 04',
         titulo='Making Sense of Things at Work',
         desc='What people say when the information fits, when a decision was right and '
              'when a subject has to wait. These six carry a lot of the talk in a meeting.',
         nota='"Circle back" and "keep me posted" are office English, and hospitals use '
              'them too. They are neutral, so you can say them to your boss.',
         fala=['The dates match the chart, so that checks out.',
               'Just a heads-up: the clinic closes early on Friday.',
               'Keep me posted if anything changes overnight.',
               'Off the top of my head, I think it was three weeks ago.']),
]


def render():
    cards = []
    for g in GRUPOS:
        pares = [(e, situacao) for e, _, _, situacao in g['itens']]
        s1 = bloco_cartoes(g['itens'])
        s2 = nota(g['nota'])
        s3 = secao('Stage 2: Which one fits?', 'Vocabulary', 'badge-vocab',
                   'Read the situation and choose the expression an American would use.',
                   matching('match-ae%d' % g['n'], pares, seed=g['seed']))
        s4 = secao('Stage 3: Complete the conversation', 'Practice', 'badge-practice',
                   'These are new conversations. Listen first, then write the missing '
                   'expression and check it.',
                   fill_in_dialogo(g['fills']))
        s5 = secao('Stage 4: What would you say?', 'Quiz', 'badge-quiz',
                   'One answer sounds natural. The others are correct English that '
                   'nobody would say here.',
                   quiz(g['quiz']))
        s6 = secao('Stage 5: Say it out loud', 'Speaking', 'badge-speak',
                   'Listen, then record yourself. You will get a word-by-word score.',
                   pronunciation(g['fala']))
        cards.append(lesson_card(g['id'], g['img'], g['numero'], g['titulo'], g['desc'],
                                 [s1, s2, s3, s4, s5, s6]))

    return ('<!-- ========== TAB 6: EXPRESSIONS (aditivo, 10/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-expressions">\n'
            '<h3 style="%s">Everyday American Expressions</h3>\n'
            '<p style="%s">Twenty-four expressions Americans really use, in the four '
            'moments where they come up: agreeing and refusing, fixing a small mistake, '
            'small talk, and work. Each one comes with what it means, a real sentence, '
            'and the voice of an American saying both.</p>\n'
            '%s\n'
            '%s\n'
            '</div><!-- /tab-expressions -->\n'
            % (H3, INTRO, painel_aba('expressions', 'Your progress in Expressions'),
               '\n\n'.join(cards)))


def main():
    destino = os.path.join(AQUI, 'expressions.html')
    html = render()
    with open(destino, 'w', encoding='utf-8') as f:
        f.write(html)
    print('expressions.html  %6d bytes  |  %d grupos, %d expressoes'
          % (len(html.encode('utf-8')), len(GRUPOS), sum(len(g['itens']) for g in GRUPOS)))


if __name__ == '__main__':
    main()
