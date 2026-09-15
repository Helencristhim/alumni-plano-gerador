#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo-fonte das 5 abas suplementares do Fernando + emissor dos snippets.

DE ONDE VEIO (consultoria da Helen com o aluno, 15/09/2026)
-----------------------------------------------------------
O Fernando (B2, CFO em busca de emprego, entrevistas com gente de fora) trouxe
tres queixas, e as tres batem com os dados:
  1. nao sabe o que fazer depois da aula nem como fixar vocabulario
     (o hub do aluno nao tem homework; `mediaChecks` vazio);
  2. quer series e filmes direcionados (o perfil ja listava Succession,
     Industry etc., e nada disso estava no material);
  3. o ouvido e o gargalo: fala emendada, sotaque de Nova York, e o resumo das
     aulas mostra palavras que ele nao entendeu e erros que se repetem.

As abas:
  studyweek  -- Your Study Week: o que fazer, quando e onde (5h em blocos de 20 min)
  wordreview -- Word Review: revisao espacada das aulas 1-3 + os erros dele
  realspeed  -- Real-Speed English: o que o entrevistador diz, no ritmo real
  accents    -- Accents: seis entrevistadores, seis sotaques (1 voz por MP3)
  screen     -- Series & Films: curadoria com tarefa de escuta e gravacao

REGRAS QUE ESTE ARQUIVO OBEDECE
-------------------------------
* ADITIVO PURO: as abas entram depois da ultima aba existente, pelo
  `_build/model/insert_hub_extras.py`. Nenhum byte do material atual muda.
* SEM JS NOVO: so funcoes que o hub ja define (checkMatch, verifyAllMatches,
  checkBlank, listenBlank, selectQuiz, speakPhrase, startRecording,
  stopRecording, startFreeRecording, stopFreeRecording, toggleLesson,
  toggleMediaDone, speakText). Nenhum `switchTab` dentro do conteudo: o do hub
  usa `event.currentTarget` e marcaria o botao errado como ativo.
* REGRA 7.1: texto no atributo (data-speak / data-phrase), nunca na string JS.
* IDS PROPRIOS: wr-review-N, rs-group-N, ac-voice-N, sf-title-N. Nunca
  ex-lesson-N, stampN, data-lesson-progress.
* REGRA 13 (B2): zero portugues na tela.
* TETO DE NIVEL: as aulas dadas em sala sao 1-3 (past simple x present perfect,
  third conditional, modal perfects), mais o nucleo que um B2 ja tem (present,
  past, will/going to, modais basicos, passiva vista em sala em 01/09). Nada de
  cleft, inversao, relative non-defining, past perfect, future perfect,
  used to, pergunta indireta, subjuntivo -- sao das aulas 4-13.
* COLISAO DE ESTADO: `loadState` restaura por texto em TODO o documento
  (data-answer do fill-in, match-word do matching, 30 chars da opcao certa do
  quiz, frase do speech card, 40 chars do think card, palavra do vocab card).
  `checa_colisoes()` compara tudo com o hub e ABORTA o build se bater.
* FILL-IN FECHA COM O AUDIO: antes + resposta + depois == data-phrase.
* REGRA 17: links exatos (IMDb do titulo, conferido em 15/09/2026).

Os helpers de HTML sao os do Diego (mesma aba suplementar, mesmo hub-modelo):
importados, nao copiados.

USO: python3 build_extras.py   (escreve os 5 snippets ao lado deste arquivo)
"""
import html as htmllib
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
SLUG = 'fernando-meneghelli-bottura'
sys.path.insert(0, os.path.join(RAIZ, '_build', 'diego-leonel-george-wached-extras'))

from build_extras import (H3, INTRO, ITAL, LINK_STYLE, barra_card, esc,  # noqa: E402
                          fill_in, lesson_card, matching, painel_aba,
                          pronunciation, quiz, secao, word_bank)
from build_expressions import BTN_EX, NOTA  # noqa: E402

IMG = {
    'career': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&q=80',
    'desk': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80',
    'board': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=600&q=80',
    'team': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80',
    'meeting': 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=600&q=80',
    'paper': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&q=80',
}

SVG_FILM = ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" '
            'stroke="var(--accent)" stroke-width="2"><rect x="2" y="3" width="20" height="18" rx="2"/>'
            '<path d="M7 3v18M17 3v18M2 8h5M2 16h5M17 8h5M17 16h5"/></svg>')


def emb(perguntas, seed):
    """Embaralha as opcoes de cada pergunta (seed fixa = build reproduzivel).
    Sem isto a certa cairia quase sempre na letra A, como foi escrita."""
    out = []
    for i, (q, opcoes) in enumerate(perguntas):
        opcoes = list(opcoes)
        random.Random(seed * 100 + i).shuffle(opcoes)
        out.append((q, opcoes))
    return out


def nota(rotulo, texto):
    return ('    <div style="%s"><strong style="color:var(--accent)">%s</strong> %s</div>'
            % (NOTA, esc(rotulo), esc(texto)))


def think(pergunta, rid):
    return ('      <div class="think-card">\n'
            '        <div class="think-question">%s</div>\n'
            '        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
            '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>\n'
            '        <div id="%s"></div>\n'
            '      </div>' % (esc(pergunta), rid))


# ================================================================ WORD REVIEW
# Revisao ESPACADA: cada Review e feita 1, 3 e 7 dias depois da aula (o roteiro
# esta na aba Study Week). Matching INVERTIDO de proposito: a linha e uma
# SITUACAO da carreira dele e a opcao e a palavra. Assim o aluno recupera a
# palavra (o que trava na entrevista), e a linha nunca tem o mesmo texto do
# matching do Pre-class -- que e o que o loadState usa para restaurar.

WR = [
    dict(n=1, img=IMG['career'], lesson='Lesson 1',
         titulo='Your Career Story Words',
         desc='The words from Lesson 1, in situations from a CFO career. Do this review one day after the class, again three days later, and the speaking stage again after a week.',
         pares=[('Ten years of results that anyone can check', 'track record'),
                ('The month the new system went live across the whole group', 'milestone'),
                ('You personally led the cost program from the first day', 'to spearhead'),
                ('A unit loses money for two years, then makes a profit again', 'turnaround'),
                ('A CFO with twenty years in the same industry', 'seasoned'),
                ('You still build the cash-flow model yourself', 'hands-on'),
                ('Moving from an advertising group to a manufacturing company', 'transition'),
                ('The skills and contacts only you can offer the new company', 'to bring to the table')],
         banco=['solid track record', 'personally spearheaded', 'at the helm', 'every stakeholder', 'steered', 'the groundwork'],
         fills=[('"Over twenty years I have built a ', 'solid track record', ' in cost control."',
                 'Hint: an adjective plus the Lesson 1 word, three words',
                 'Over twenty years I have built a solid track record in cost control.'),
                ('"In 2019 I ', 'personally spearheaded', ' the restructuring of the finance team."',
                 'Hint: two words, an adverb plus the past simple of to spearhead',
                 'In 2019 I personally spearheaded the restructuring of the finance team.'),
                ('"She was ', 'at the helm', ' of the finance function for six years."',
                 'Hint: three words, in the leading position',
                 'She was at the helm of the finance function for six years.'),
                ('"I kept ', 'every stakeholder', ' informed, from the banks to the auditors."',
                 'Hint: a word meaning each one, plus the Lesson 1 word',
                 'I kept every stakeholder informed, from the banks to the auditors.'),
                ('"We ', 'steered', ' the company through a very hard year."',
                 'Hint: past simple of to steer',
                 'We steered the company through a very hard year.'),
                ('"The first year was about laying ', 'the groundwork', ' for growth."',
                 'Hint: the article plus the Lesson 1 word',
                 'The first year was about laying the groundwork for growth.')],
         quiz=[('The interviewer asks: "What would you bring to the table?" What does she want to hear?',
                [('The value you offer that other candidates do not.', True),
                 ('The documents you are bringing to the meeting.', False),
                 ('The name of your last manager.', False),
                 ('The salary you expect.', False)]),
               ('You still work in finance today. Which sentence is right?',
                [('I worked in finance for twenty years, and I love it.', False),
                 ('I have worked in finance for twenty years.', True),
                 ('I am working in finance since twenty years.', False),
                 ('I work in finance for twenty years.', False)]),
               ('Which sentence uses "turnaround" correctly?',
                [('I turnaround the unit in 2020.', False),
                 ('The turnaround took eighteen months and saved the unit.', True),
                 ('It was a turnaround moment when I read the email.', False),
                 ('We made a turnaround of the budget meeting.', False)])],
         fala=['I have a strong track record in turnarounds.',
               'I spearheaded the transition to a shared finance team.',
               'As a seasoned CFO, I stay hands-on with the numbers.',
               'The groundwork we did in 2019 made the turnaround possible.']),

    dict(n=2, img=IMG['board'], lesson='Lesson 2',
         titulo='The Mandate Words',
         desc='The words from Lesson 2, used the way a board talks about a CFO. Same rhythm: one day, three days and seven days after the class.',
         pares=[('The board tells the new CFO to cut costs by 15% in two years', 'mandate'),
                ('Treasury, tax and reporting are all part of your job', 'remit'),
                ('Your six years as CFO of the same group', 'tenure'),
                ('You take over a team that the previous CFO hired', 'to inherit'),
                ('An old system that still runs but costs a fortune', 'legacy'),
                ('A finance team of eight people for a very large business', 'lean'),
                ('You hire twenty people in three months for a new contract', 'to ramp up'),
                ('Looking back, you now see a risk you missed at the time', 'hindsight')],
         banco=['inherited', 'scaled back', 'the backing', 'In hindsight', 'the turning point', 'ramped up'],
         fills=[('"When I joined, I ', 'inherited', ' a team of forty people."',
                 'Hint: past simple of to inherit',
                 'When I joined, I inherited a team of forty people.'),
                ('"We ', 'scaled back', ' the project after we lost the account."',
                 'Hint: past simple, two words, the opposite of ramp up',
                 'We scaled back the project after we lost the account.'),
                ('"Without ', 'the backing', ' of the board, the plan would have failed."',
                 'Hint: the article plus the Lesson 2 word for support',
                 'Without the backing of the board, the plan would have failed.'),
                ('"', 'In hindsight', ', I would have changed the system first."',
                 'Hint: two words, looking back',
                 'In hindsight, I would have changed the system first.'),
                ('"Losing the biggest client was ', 'the turning point', ' of my tenure."',
                 'Hint: the article plus a two-word Lesson 2 expression',
                 'Losing the biggest client was the turning point of my tenure.'),
                ('"We ', 'ramped up', ' production in only three months."',
                 'Hint: past simple, two words, increase quickly',
                 'We ramped up production in only three months.')],
         quiz=[('The interviewer asks: "What was your remit?" What do you talk about?',
                [('The areas you were responsible for, like treasury and tax.', True),
                 ('The money you sent to the head office.', False),
                 ('The reasons you left the company.', False),
                 ('The name of the company that paid you.', False)]),
               ('Which third conditional sentence is correct?',
                [('If we kept the legacy system, costs would have gone up.', False),
                 ('If we had kept the legacy system, costs would go up.', False),
                 ('If we had kept the legacy system, costs would have gone up.', True),
                 ('If we would have kept the legacy system, costs had gone up.', False)]),
               ('A company describes its finance team as "lean". What does that mean?',
                [('The team is small on purpose, to keep costs low.', True),
                 ('The team is weak and needs training.', False),
                 ('The team works only part-time.', False),
                 ('The team is new to the company.', False)])],
         fala=['My mandate was to bring the group back to profit.',
               'I inherited a legacy system and a very lean team.',
               'If I had had more backing, I would have moved faster.',
               'In hindsight, that was the turning point of my tenure.']),

    dict(n=3, img=IMG['meeting'], lesson='Lesson 3',
         titulo='Listening Under Pressure Words',
         desc='The words from Lesson 3: what you say when you did not catch the question, and what the interviewer does when she wants more.',
         pares=[('The interviewer keeps asking until she gets past your first answer', 'to probe'),
                ('You explain a complex deal one part at a time', 'to unpack'),
                ('From "costs went down" to the exact line in the P&L', 'to drill down'),
                ('You return to a question you skipped ten minutes earlier', 'to circle back'),
                ('You mention the IPO in one sentence and move on', 'to touch on'),
                ('You understood the main idea, but not every word', 'the gist'),
                ('You say her question again in your own words', 'to paraphrase'),
                ('You need five seconds to find the number in your notes', 'bear with me')],
         banco=['only got the gist', 'Just to clarify', 'Bear', 'probed', 'circle', 'driving'],
         fills=[('"Sorry, I ', 'only got the gist', '. Could you say that again?"',
                 'Hint: four words, you understood only the main idea',
                 'Sorry, I only got the gist. Could you say that again?'),
                ('"', 'Just to clarify', ', you mean the 2019 numbers?"',
                 'Hint: three words you say before you check what someone means',
                 'Just to clarify, you mean the 2019 numbers?'),
                ('"', 'Bear', ' with me, I want to find the exact figure."',
                 'Hint: one word, the first word of the expression',
                 'Bear with me, I want to find the exact figure.'),
                ('"She ', 'probed', ' every number I gave her."',
                 'Hint: past simple of to probe',
                 'She probed every number I gave her.'),
                ('"Can we ', 'circle', ' back to the question about your team?"',
                 'Hint: one word, return to a point',
                 'Can we circle back to the question about your team?'),
                ('"Sorry, what exactly are you ', 'driving', ' at?"',
                 'Hint: one word, -ing form',
                 'Sorry, what exactly are you driving at?')],
         quiz=[('You did not prepare the numbers, and the interview went badly. What do you tell a friend?',
                [('I must prepare the numbers.', False),
                 ('I should have prepared the numbers.', True),
                 ('I should prepared the numbers.', False),
                 ('I have should prepare the numbers.', False)]),
               ('The interviewer says: "Let\'s drill down into that." What happens next?',
                [('She changes the subject.', False),
                 ('She asks for specific details about the same point.', True),
                 ('She ends the interview.', False),
                 ('She asks you to speak more slowly.', False)]),
               ('You did not understand a long question. What is the best move?',
                [('Answer something close and hope for the best.', False),
                 ('Stay silent until she repeats it.', False),
                 ('Paraphrase it and check: "So, you mean the 2019 restructuring?"', True),
                 ('Say "yes" and wait for the next question.', False)])],
         fala=['Just to clarify, you mean the 2019 restructuring?',
               'Bear with me, I want to give you the exact figure.',
               'Let me unpack that in three parts.',
               'I think I might have misunderstood the question.']),

    dict(n=4, img=IMG['paper'], lesson='From your classes',
         titulo='The Words Your Classes Flagged',
         desc='This review comes from the summaries of your own classes: the words you did not understand, the ones that were hard to pronounce and the corrections your teacher made more than once.',
         pares=[('The money a company makes from sales, before costs', 'revenue'),
                ('The goods a company keeps in the warehouse', 'inventory'),
                ('A company that cannot pay its debts and has to close', 'bankruptcy'),
                ('How much profit a business makes compared to its size', 'profitability'),
                ('Changing with the time of year, like sales at Christmas', 'seasonal'),
                ('Your natural ability to learn or do something well', 'aptitude'),
                ('The way you think and behave toward other people', 'attitude'),
                ('The person who leads the meeting of the board', 'the chair')],
         banco=['people', 'has', 'directly to', 'Profitability', 'brink', 'Our revenue'],
         fills=[('"We hired two hundred ', 'people', ' in three years."',
                 'Hint: this word is already plural, so it never takes an s',
                 'We hired two hundred people in three years.'),
                ('"Korea ', 'has', ' always been a strong market for us."',
                 'Hint: one country is singular, so the verb takes the third person form',
                 'Korea has always been a strong market for us.'),
                ('"I reported ', 'directly to', ' the CEO and the board."',
                 'Hint: two words, an adverb plus the preposition',
                 'I reported directly to the CEO and the board.'),
                ('"', 'Profitability', ' was the problem, not the market."',
                 'Hint: the English word for how much profit a business makes',
                 'Profitability was the problem, not the market.'),
                ('"The unit was on the ', 'brink', ' of bankruptcy when I joined."',
                 'Hint: one word, on the edge of',
                 'The unit was on the brink of bankruptcy when I joined.'),
                ('"', 'Our revenue', ' grew twelve percent, but margins went down."',
                 'Hint: two words, a possessive plus the money from sales',
                 'Our revenue grew twelve percent, but margins went down.')],
         quiz=[('Which sentence is correct English?',
                [('Our rentability improved in 2021.', False),
                 ('Our profitability improved in 2021.', True),
                 ('Our rentabilities improved in 2021.', False),
                 ('Our profitable improved in 2021.', False)]),
               ('Which past form ends with an extra syllable, /id/?',
                [('faced', False), ('worked', False), ('inherited', True), ('probed', False)]),
               ('Which question has the right word order?',
                [('What the company decided in 2020?', False),
                 ('What did the company decide in 2020?', True),
                 ('What did the company decided in 2020?', False),
                 ('What decided the company in 2020?', False)]),
               ('A long recovery from losses back to profit is...',
                [('a turning point.', False), ('a turnaround.', True),
                 ('a transition.', False), ('a milestone.', False)])],
         fala=['Our revenue grew, but inventory costs grew faster.',
               'I faced a bankruptcy risk in my first year.',
               'I inherited a seasoned team and worked with them for six years.',
               'He led the project last year, and now I lead it.']),
]


def render_wordreview():
    cards = []
    for w in WR:
        s1 = secao('Stage 1: Which word is it?', 'Vocabulary', 'badge-vocab',
                   'Read the situation and choose the word. Try to say the word before you open the list.',
                   matching('match-wr%d' % w['n'], w['pares'], seed=7100 + w['n'] * 10))
        s2 = secao('Stage 2: Complete from memory', 'Practice', 'badge-practice',
                   'Use the word bank. Listen to the full sentence after you check it.',
                   word_bank(w['banco']) + '\n' + fill_in(w['fills']))
        s3 = secao('Stage 3: Check the meaning', 'Quiz', 'badge-quiz',
                   'Choose the best answer.', quiz(emb(w['quiz'], 71 + w['n'])))
        s4 = secao('Stage 4: Say it like an executive', 'Speaking', 'badge-speak',
                   'Listen, then record yourself. On day seven, do only this stage.',
                   pronunciation(w['fala']))
        cards.append(lesson_card('wr-review-%d' % w['n'], w['img'],
                                 'Word Review %02d -- %s' % (w['n'], w['lesson']),
                                 w['titulo'], w['desc'], [s1, s2, s3, s4]))
    return ('<!-- ========== EXTRAS: WORD REVIEW (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-wordreview">\n'
            '<h3 style="%s">Word Review</h3>\n'
            '<p style="%s">Words stay when you meet them again at the right time. Each review below '
            'goes with one class: do it one day after the class, repeat the mistakes three days later, '
            'and record the speaking stage again after a week. Review 04 is built from your own class summaries.</p>\n'
            '%s\n%s\n'
            '</div><!-- /tab-wordreview -->\n'
            % (H3, INTRO, painel_aba('wordreview', 'Your progress in Word Review'), '\n\n'.join(cards)))


# =========================================================== REAL-SPEED ENGLISH
# O que o entrevistador DIZ, e como SOA quando sai rapido. Card = expressao +
# sentido + "sounds like" (a fala emendada escrita do jeito que se ouve) + frase.
# O ditado cobra justamente o pedaco que embola. Contraido de proposito; o
# data-alt aceita a forma por extenso.

def cartao_som(expr, sentido, som, exemplo):
    return (
        '        <div class="vocab-card-pc">\n'
        '          <div class="vocab-card-content">\n'
        '            <div class="vocab-card-header"><span class="vocab-card-word">%s</span>'
        '<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">%s</span></div>\n'
        '            <div class="vocab-card-example" style="font-style:normal">Sounds like: <strong>%s</strong></div>\n'
        '            <div class="vocab-card-example">&ldquo;%s&rdquo;</div>\n'
        '            <button style="%s" data-speak="%s" onclick="speakText(this.dataset.speak,this)">'
        '&#9654;&nbsp;Hear it in a sentence</button>\n'
        '          </div>\n'
        '          <button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button>\n'
        '        </div>' % (esc(expr), esc(sentido), esc(som), esc(exemplo), BTN_EX,
                            esc(exemplo), esc(expr)))


RS = [
    dict(n=1, img=IMG['desk'], titulo='The First Two Minutes',
         desc='How an interviewer opens a call. These lines come fast, often before you are ready, and they set the tone.',
         itens=[('Thanks for making the time', 'thank you for finding time for this call', 'thanks-fer-making-the-time',
                 'Hi Fernando, thanks for making the time on a Friday.'),
                ('Can you hear me okay?', 'a quick check that the audio of the call works', 'k-nya-hear-me-okay',
                 'Can you hear me okay? The connection here is not great.'),
                ('Walk me through your background', 'tell your career story in order', 'walk-me-thru-yer-background',
                 'So, walk me through your background, starting wherever you like.'),
                ('What brings you here?', 'why you are interested in this job', 'wha-brings-ya-here',
                 'What brings you here? You had a great role at your last company.'),
                ('Tell me a bit about yourself', 'give a short introduction', 'tell-me-a-bit-a-bout-yer-self',
                 'Tell me a bit about yourself, the short version.'),
                ('Before we dive in', 'before the main part of the interview starts', 'b-for-we-dive-in',
                 'Before we dive in, let me explain how today is going to work.')],
         fills=[('"', 'Walk me through', ' your last two jobs, please."',
                 'Hint: three words, tell the story in order',
                 'Walk me through your last two jobs, please.'),
                ('"', "What brings you", ' to a company like ours?"',
                 'Hint: three words, a question about your reasons', 'What brings you to a company like ours?'),
                ('"Great, ', 'thanks for making', ' the time today."',
                 'Hint: three words, thank you for finding time', 'Great, thanks for making the time today.'),
                ('"', 'Before we dive', ' in, do you have a hard stop at eleven?"',
                 'Hint: three words, before the main part', 'Before we dive in, do you have a hard stop at eleven?'),
                ('"', 'Can you hear', ' me now? I switched to my headphones."',
                 'Hint: three words, the audio check', 'Can you hear me now? I switched to my headphones.')],
         quiz=[('The interviewer says "Walk me through your background." How long should your first answer be?',
                [('Two minutes, in order, with the main results.', True),
                 ('Ten minutes, with every job since university.', False),
                 ('One sentence with your current title.', False),
                 ('You should ask her to send the question by email.', False)]),
               ('"What brings you here?" is really a question about...',
                [('the way you travelled to the office.', False),
                 ('your reasons for wanting this job.', True),
                 ('the documents you brought.', False),
                 ('the city where you live.', False)]),
               ('You hear "k-nya-hear-me-okay". What did the interviewer say?',
                [('Can you hear me okay?', True), ('Can I hear you okay?', False),
                 ('Can you help me okay?', False), ('Do you hear me okay?', False)])],
         fala=['Thanks for making the time today.',
               'Sure. I have spent twenty years in finance, the last eight as a CFO.',
               'I am here because of the turnaround you are planning.']),

    dict(n=2, img=IMG['team'], titulo='Keeping the Conversation Moving',
         desc='The short reactions an interviewer uses while you talk. They tell you to continue, to stop, or to give more detail.',
         itens=[('Go on', 'please continue, I am listening', 'go-wan',
                 'Go on, what happened after the bank said no?'),
                ('Fair enough', 'I accept your point, even if I am not fully convinced', 'fair-a-nuff',
                 'Fair enough. It was a very hard market that year.'),
                ('Makes sense', 'I understand and I agree with your logic', 'make-sense',
                 'Makes sense. So you cut the costs before you hired again.'),
                ('Let me stop you there', 'I want to interrupt with a question', 'lemme-stop-ya-there',
                 'Let me stop you there. Who made that decision, you or the CEO?'),
                ('Say more about that', 'give more detail about the point you just made', 'say-more-a-bout-that',
                 'Say more about that. How big was the team?'),
                ('Got it', 'I understand', 'gah-dit',
                 'Got it. And the margin went back up the next year?')],
         fills=[('"', 'Let me stop', ' you there for a second."',
                 'Hint: three words, the interviewer wants to interrupt', 'Let me stop you there for a second.'),
                ('"', 'Fair enough', '. Tell me about the second year."',
                 'Hint: two words, I accept your point', 'Fair enough. Tell me about the second year.'),
                ('"', 'Say more', ' about the team you inherited."',
                 'Hint: two words, give more detail', 'Say more about the team you inherited.'),
                ('"', 'Got it', ', so the board approved the plan in March."',
                 'Hint: two words, I understand', 'Got it, so the board approved the plan in March.'),
                ('"Okay, ', 'go on', '. What did the auditors say?"',
                 'Hint: two words, please continue', 'Okay, go on. What did the auditors say?')],
         quiz=[('The interviewer says "Fair enough" after your answer. What does it tell you?',
                [('She accepts your answer and is ready to move on.', True),
                 ('She thinks your answer was unfair.', False),
                 ('She wants you to repeat the answer.', False),
                 ('She is angry about your salary question.', False)]),
               ('You are in the middle of a long answer and hear "Let me stop you there." What do you do?',
                [('Finish your story first, then listen.', False),
                 ('Stop, listen to her question, and answer that.', True),
                 ('Apologize and end the interview.', False),
                 ('Start the story again from the beginning.', False)]),
               ('You hear "gah-dit". What did the interviewer say?',
                [('Got it.', True), ('Good hit.', False), ('Get it.', False), ('God, it.', False)])],
         fala=['Let me stop you there. Who made that decision?',
               'Fair enough. It was a very hard market that year.',
               'Say more about that. How big was the team?']),

    dict(n=3, img=IMG['board'], titulo='The Hard Questions',
         desc='The questions that come quickly and cut words in half. You usually know the answer. The problem is catching the question.',
         itens=[("Why'd you leave?", 'why did you leave your last job', 'why-dja-leave',
                 "Why'd you leave after only two years?"),
                ("How'd that go?", 'how did that situation end', 'how-dthat-go',
                 "You presented the plan to the banks. How'd that go?"),
                ("What's your take on", 'what is your opinion about', 'wats-yer-take-on',
                 "What's your take on the new tax rules in Brazil?"),
                ('Give me a ballpark', 'give me an approximate number', 'gimme-a-ballpark',
                 "I don't need the exact figure, just give me a ballpark."),
                ('What would you have done differently?', 'looking back, what would you change', 'wud-ja-have-done-differently',
                 'The deal failed. What would you have done differently?'),
                ('Where do you see the risk?', 'which part worries you most', 'where-dya-see-the-risk',
                 'This plan looks good on paper. Where do you see the risk?')],
         fills=[('"So ', "why'd you", ' leave the agency?"',
                 'Hint: three words, a short form of why did you', "So why'd you leave the agency?", 'why did you'),
                ('"Okay, and ', "how'd that", ' go with the auditors?"',
                 'Hint: two words, a short form of how did that', "Okay, and how'd that go with the auditors?", 'how did that'),
                ('"', "What's your take", ' on our last results?"',
                 'Hint: three words, a question about your opinion', "What's your take on our last results?", 'what is your take'),
                ('"Just ', 'give me a ballpark', ' for the savings."',
                 'Hint: four words, an approximate number', 'Just give me a ballpark for the savings.'),
                ('"What ', 'would you have', ' done in my place?"',
                 'Hint: three words, third conditional question', 'What would you have done in my place?')],
         quiz=[('The interviewer asks "Give me a ballpark." What is a good answer?',
                [('"Around four million reais a year."', True),
                 ('"I need to check my files first."', False),
                 ('"Exactly 4,237,512 reais."', False),
                 ('"I prefer not to talk about baseball."', False)]),
               ('You hear "why-dja-leave". What was the full question?',
                [('Why do you live?', False), ('Why did you leave?', True),
                 ('Why did you lead?', False), ('Why do you leave?', False)]),
               ('"What\'s your take on the market?" asks for...',
                [('your opinion about the market.', True), ('a number from your report.', False),
                 ('the price you paid.', False), ('your plan for next week.', False)])],
         fala=["Why'd you leave after only two years?",
               'Give me a ballpark for the savings.',
               'What would you have done differently?']),

    dict(n=4, img=IMG['meeting'], titulo='Closing the Call',
         desc='The last minutes decide what you remember. These lines tell you the interview is ending and what comes next.',
         itens=[("We're running short on time", 'we have only a few minutes left', 'we-r-running-short-on-time',
                 "We're running short on time, so one last question."),
                ('Any questions for me?', 'your turn to ask the interviewer something', 'any-questions-fer-me',
                 'That covers my side. Any questions for me?'),
                ('What are the next steps?', 'what happens after this interview', 'wadder-the-next-steps',
                 'Thank you. What are the next steps in the process?'),
                ("We'll be in touch", 'we will contact you with an answer', 'will-be-in-touch',
                 "We'll be in touch by the end of next week."),
                ("I'll loop in", 'I will add another person to the conversation', 'all-loop-in',
                 "I'll loop in our CFO for the second round."),
                ("Let's circle back", 'let us return to this subject later', 'lets-circle-back',
                 "Let's circle back on the salary next week.")],
         fills=[('"Sorry, ', "we're running short", ' on time today."',
                 'Hint: three words, few minutes left', "Sorry, we're running short on time today.", 'we are running short'),
                ('"Do you have ', 'any questions for', ' me or for the team?"',
                 'Hint: three words, your turn to ask', 'Do you have any questions for me or for the team?'),
                ('"', "We'll be in", ' touch in about ten days."',
                 'Hint: three words, a short form of we will', "We'll be in touch in about ten days.", 'we will be in'),
                ('"', "I'll loop in", ' the head of HR."',
                 'Hint: three words, add a person to the conversation', "I'll loop in the head of HR.", 'i will loop in'),
                ('"Could you tell me ', 'the next steps', ', please?"',
                 'Hint: three words, what happens after today', 'Could you tell me the next steps, please?')],
         quiz=[('The interviewer says "We\'ll be in touch." What does it mean?',
                [('She will contact you later with news.', True),
                 ('She wants to touch base right now.', False),
                 ('You got the job.', False),
                 ('You should call her tomorrow.', False)]),
               ('You hear "We\'re running short on time." What is the best move?',
                [('Start a long story about your first job.', False),
                 ('Keep your next answer short and clear.', True),
                 ('Ask for ten more minutes.', False),
                 ('Say goodbye immediately.', False)]),
               ('"I\'ll loop in our CFO" means...',
                [('the CFO will join the next conversation.', True),
                 ('the CFO is not available.', False),
                 ('the CFO will call your references.', False),
                 ('the CFO wants to see your numbers again.', False)])],
         fala=['Thank you. What are the next steps in the process?',
               "We're running short on time, so one last question.",
               'Yes, I have two questions for you.']),
]


def render_realspeed():
    cards = []
    for g in RS:
        s1 = ('    <div class="exercise-section">\n'
              '      <div class="section-header-row"><h4>Stage 1: Hear it</h4>'
              '<span class="badge badge-vocab">Listen</span></div>\n'
              '      <p style="%s">Listen to the expression, then hear it inside a real sentence. '
              'Use the speed buttons at the top of the page: first 0.75x, then 1x.</p>\n'
              '      <div class="vocab-cards">\n%s\n      </div>\n'
              '    </div>' % (ITAL, '\n'.join(cartao_som(*i) for i in g['itens'])))
        s2 = secao('Stage 2: Catch the words', 'Practice', 'badge-practice',
                   'Press Listen first and write what you hear. This is where the words run together.',
                   fill_in(g['fills']))
        s3 = secao('Stage 3: What did they mean?', 'Quiz', 'badge-quiz',
                   'Choose the best answer.', quiz(emb(g['quiz'], 81 + g['n'])))
        s4 = secao('Stage 4: Shadow it', 'Speaking', 'badge-speak',
                   'Listen and repeat at the same speed, with the same rhythm. Speaking fast helps you hear fast.',
                   pronunciation(g['fala']))
        cards.append(lesson_card('rs-group-%d' % g['n'], g['img'],
                                 'Real-Speed English %02d' % g['n'], g['titulo'], g['desc'],
                                 [s1, s2, s3, s4]))
    return ('<!-- ========== EXTRAS: REAL-SPEED ENGLISH (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-realspeed">\n'
            '<h3 style="%s">Real-Speed English</h3>\n'
            '<p style="%s">In a real interview, words do not come one by one. "What did you" becomes '
            '"wha-dja", and your brain has to fill in the rest. It can only do that with sounds it already knows. '
            'These twenty-four lines are the ones interviewers use most, with how they really sound.</p>\n'
            '%s\n%s\n'
            '</div><!-- /tab-realspeed -->\n'
            % (H3, INTRO, painel_aba('realspeed', 'Your progress in Real-Speed English'), '\n\n'.join(cards)))


# ===================================================================== ACCENTS
# UM SOTAQUE POR MP3 (listening e monologo, README). O genero e sempre uma
# situacao de processo seletivo com dado literal -- nome, data, numero, pedido
# -- e toda pergunta tem a resposta escrita no audio (nada de inferencia).
# A voz vai em `data-accent`, que o gen_audio_extras.py deste diretorio le.
# NAO e `data-voice`: esse o validador resolve pelo voices.json global.
# As vozes vieram da conta compartilhada e AINDA NAO FORAM VALIDADAS DE OUVIDO.

AC = [
    dict(n=1, voz='ny_m', img=IMG['desk'], sotaque='American -- New York',
         titulo='The Recruiter in New York',
         quem='David Klein, a recruiter at Hudson Partners, leaves you a voice message.',
         texto=("Hi Fernando, it's David Klein from Hudson Partners in New York. Thanks for sending the updated resume. "
                "So here's the deal. The client is a packaging group, about nine hundred million dollars in revenue, "
                "and they need a CFO who has done a turnaround before. The first call is with their CEO, Laura Stein, "
                "next Tuesday at ten a.m. New York time. That's eleven in Sao Paulo. She's gonna ask about your track record, "
                "and she's gonna push on the numbers, so have your three big results ready. It's a thirty-minute video call. "
                "Can you confirm by Friday? Just call me back or drop me a line. Talk soon."),
         quiz=[('What does the client company make?',
                [('Packaging.', True), ('Cars.', False), ('Software.', False), ('Food.', False)]),
               ('Who is on the first call?',
                [('David Klein.', False), ('The CEO, Laura Stein.', True),
                 ('The head of HR.', False), ('The CFO of the group.', False)]),
               ('How long is the video call?',
                [('Ten minutes.', False), ('Thirty minutes.', True), ('One hour.', False), ('Ninety minutes.', False)]),
               ('By when does David need an answer?',
                [('By Tuesday.', False), ('By Monday.', False), ('By Friday.', True), ('Today.', False)])],
         eco="She's gonna push on the numbers, so have your three big results ready.",
         pensa='Record the three big results David asked for, in about sixty seconds.'),

    dict(n=2, voz='london_f', img=IMG['career'], sotaque='British -- London',
         titulo='The Talent Team in London',
         quem='Charlotte Hayes, head of talent at Northbridge Capital, calls about the next stages.',
         texto=("Good morning, Fernando. Charlotte Hayes here, from Northbridge Capital in London. "
                "I've just come off the phone with our finance director, and he'd like to meet you. "
                "The role covers Brazil, Chile and Colombia, and you'd report to him directly. There are two stages. "
                "First, a forty-five minute interview with me and a colleague from HR, on the twenty-third. "
                "Then a case study. We'll send you last year's accounts for our Chilean business, and you'll have a week "
                "to prepare a short presentation. If the twenty-third doesn't suit you, have a word with my assistant, Tom, "
                "and he'll sort out another date. Lovely to speak to you."),
         quiz=[('Which countries does the role cover?',
                [('Brazil, Chile and Colombia.', True), ('Brazil, Peru and Mexico.', False),
                 ('Chile and Argentina.', False), ('Only Brazil.', False)]),
               ('When is the first interview?',
                [('On the thirteenth.', False), ('On the twenty-third.', True),
                 ('Next Monday.', False), ('In a week.', False)]),
               ('What will they send for the case study?',
                [("Last year's accounts for the Chilean business.", True),
                 ('A list of questions from HR.', False),
                 ('The contract for the role.', False),
                 ('A presentation from the finance director.', False)]),
               ('Who can change the date?',
                [('The finance director.', False), ('Her assistant, Tom.', True),
                 ('A colleague from HR.', False), ('Nobody, the date is fixed.', False)])],
         eco="If the twenty-third doesn't suit you, have a word with my assistant, Tom.",
         pensa='Leave Charlotte a short message back: confirm the date and ask one question about the case study.'),

    dict(n=3, voz='india_m', img=IMG['team'], sotaque='Indian -- Bangalore',
         titulo='The Controller in Bangalore',
         quem='Rajesh Menon, finance controller at the group shared service center, calls before the panel.',
         texto=("Hello Fernando, good evening. This is Rajesh Menon, finance controller at our shared service center in Bangalore. "
                "I am calling because you will work very closely with my team if you join. We process the accounts "
                "for fourteen companies in the group, and we close the month in six working days. The CFO wants to bring that "
                "down to four. So in the panel interview on Thursday, I will ask you one practical question: have you "
                "shortened a closing process before, and how? Please keep your answer to two or three minutes, with real numbers. "
                "The panel starts at six thirty in the evening, India time, so it will be morning for you. See you on Thursday."),
         quiz=[('How many companies does the team process?',
                [('Four.', False), ('Six.', False), ('Fourteen.', True), ('Forty.', False)]),
               ('How many working days does the month-end close take today?',
                [('Four.', False), ('Six.', True), ('Two or three.', False), ('Fourteen.', False)]),
               ('What does the CFO want?',
                [('To close the month in four days.', True), ('To hire more people.', False),
                 ('To move the team to Brazil.', False), ('To cancel the panel.', False)]),
               ('How long should your answer be?',
                [('Thirty seconds.', False), ('Two or three minutes.', True),
                 ('Ten minutes.', False), ('As long as you need.', False)])],
         eco='Please keep your answer to two or three minutes, with real numbers.',
         pensa="Answer Rajesh's question in two minutes: a closing process you made faster, with the numbers."),

    dict(n=4, voz='sydney_f', img=IMG['meeting'], sotaque='Australian -- Sydney',
         titulo='The Second Round in Sydney',
         quem='Kate Donovan, from Southern Cross Resources, invites you to a second interview.',
         texto=("G'day Fernando, Kate Donovan from Southern Cross Resources in Sydney. Thanks heaps for your time on the phone "
                "last week. The team reckons you're a strong fit, so we'd like to go ahead with a second interview. "
                "This one's with our chairman, Peter Walsh, and it'll be a bit more relaxed. More of a chat, really. "
                "He'll want to hear about the time you managed a big currency loss, so have a think about that one. "
                "Heads up, though: Peter's quite direct, and he doesn't like long answers. We're looking at Monday the fourth, "
                "at eight a.m. Sydney time. No worries if that doesn't work, just flick me an email."),
         quiz=[('Who is the second interview with?',
                [('The chairman, Peter Walsh.', True), ('The CEO.', False),
                 ('Kate Donovan.', False), ('The finance team.', False)]),
               ('Which story does Peter want to hear?',
                [('A big currency loss you managed.', True), ('Your first job.', False),
                 ('A merger you led.', False), ('A new system you installed.', False)]),
               ('What does Peter not like?',
                [('Long answers.', True), ('Numbers.', False), ('Video calls.', False), ('Direct questions.', False)]),
               ('What does "flick me an email" mean?',
                [('Send me a quick email.', True), ('Delete my email.', False),
                 ('Call me instead.', False), ('Print the email.', False)])],
         eco="Heads up, though: Peter's quite direct, and he doesn't like long answers.",
         pensa='Tell Peter the currency loss story in under ninety seconds. Short sentences.'),

    dict(n=5, voz='brussels_f', img=IMG['board'], sotaque='French -- Brussels',
         titulo='The Final Stage in Brussels',
         quem='Isabelle Moreau, HR director at Valmont Logistics, calls with the plan for the final day.',
         texto=("Hello Fernando, this is Isabelle Moreau, HR director at Valmont Logistics in Brussels. I have good news. "
                "After our first conversation, the CEO has decided to invite you for the final stage. It will be in person, "
                "here in Brussels, on the ninth of October. We will pay for the flight and two nights at the hotel. "
                "The day has three parts. In the morning, a meeting with the CEO. At lunch, you meet the finance team. "
                "And in the afternoon, a presentation to two members of the board. For the presentation, please prepare "
                "fifteen minutes on one topic: your plan to reduce working capital in our Latin American business. "
                "I will send all the details by email today."),
         quiz=[('Where is the final stage?',
                [('On a video call.', False), ('In person, in Brussels.', True),
                 ('In Sao Paulo.', False), ('In Paris.', False)]),
               ('What will the company pay for?',
                [('The flight and two nights at the hotel.', True), ('Only the hotel.', False),
                 ('A week in Brussels.', False), ('Nothing.', False)]),
               ('Who do you meet at lunch?',
                [('The CEO.', False), ('The finance team.', True),
                 ('Two members of the board.', False), ('Isabelle Moreau.', False)]),
               ('What is the topic of the presentation?',
                [('Reducing working capital in Latin America.', True),
                 ('Your career story.', False),
                 ('The new tax rules in Belgium.', False),
                 ('Hiring a finance team.', False)])],
         eco='Please prepare fifteen minutes on one topic: your plan to reduce working capital.',
         pensa='Record the first minute of your presentation to the board: the headline and your three steps.'),

    dict(n=6, voz='rotterdam_m', img=IMG['paper'], sotaque='Dutch -- Rotterdam',
         titulo='The Direct Question in Rotterdam',
         quem='Joost van Dijk, CEO of a logistics group, asks you the hardest question of the interview.',
         texto=("Okay Fernando, let me be very direct, because that is how we work here in Rotterdam. Your CV is strong, "
                "but I have one concern. In your last company, the margin went down two years in a row. So my question is simple. "
                "What went wrong, and what should you have done differently? Take your time. I am not looking for a perfect story. "
                "I want to see that you can look at a bad result honestly. After that I have two more questions, one about your team "
                "and one about the bank covenants, and then we finish at a quarter past eleven."),
         quiz=[('What is his concern?',
                [('The margin went down two years in a row.', True),
                 ('Your CV is too long.', False),
                 ('You never worked in logistics.', False),
                 ('Your English is not strong enough.', False)]),
               ('What does he want to see?',
                [('That you can look at a bad result honestly.', True),
                 ('A perfect story.', False),
                 ('Your salary expectations.', False),
                 ('A list of your references.', False)]),
               ('What are the two other questions about?',
                [('Your team and the bank covenants.', True), ('Your family and your city.', False),
                 ('Tax and inventory.', False), ('The board and the auditors.', False)]),
               ('When does the interview finish?',
                [('At eleven.', False), ('At a quarter past eleven.', True),
                 ('At a quarter to eleven.', False), ('At half past eleven.', False)])],
         eco='What went wrong, and what should you have done differently?',
         pensa="Answer Joost in ninety seconds: what went wrong, and what you should have done differently."),
]


def render_accents():
    cards = []
    for a in AC:
        ouve = ('    <div class="exercise-section">\n'
                '      <div class="section-header-row"><h4>Stage 1: Read the questions, then listen</h4>'
                '<span class="badge badge-quiz">Listening</span></div>\n'
                '      <p style="%s">%s Read the four questions first, so you know what to listen for. '
                'Then press Listen. Play it again at 0.75x if you need to, but finish at 1x.</p>\n'
                '      <button class="audio-btn" data-accent="%s" data-speak="%s" '
                'onclick="speakText(this.dataset.speak,this)" style="margin-bottom:1rem">Listen</button>\n'
                '%s\n'
                '    </div>' % (ITAL, esc(a['quem']), a['voz'], esc(a['texto']), quiz(emb(a['quiz'], 91 + a['n']))))
        transcript = ('    <details style="margin:0 0 1.2rem;padding:.8rem 1.1rem;background:var(--bg-card);'
                      'border:1px solid var(--border);border-radius:8px">\n'
                      '      <summary style="cursor:pointer;font-size:.85rem;font-weight:600;color:var(--accent)">'
                      'Stage 2: Open the transcript only after you answer</summary>\n'
                      '      <p style="font-size:.85rem;line-height:1.7;color:var(--text-mid);margin-top:.7rem">%s</p>\n'
                      '    </details>' % esc(a['texto']))
        eco = secao('Stage 3: Copy the accent', 'Speaking', 'badge-speak',
                    'Listen to one line and repeat it. You do not need this accent. You need to hear it.',
                    pronunciation([a['eco']]))
        fala = secao('Stage 4: Answer', 'Reflection', 'badge-think',
                     'Record your answer, then listen to yourself.',
                     think(a['pensa'], 'think-result-ac%d' % a['n']))
        cards.append(lesson_card('ac-voice-%d' % a['n'], a['img'],
                                 'Accent %02d -- %s' % (a['n'], a['sotaque']), a['titulo'],
                                 a['quem'], [ouve, transcript, eco, fala]))
    return ('<!-- ========== EXTRAS: ACCENTS (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-accents">\n'
            '<h3 style="%s">Accents</h3>\n'
            '<p style="%s">Your interviewer may be in New York, London, Brussels or Bangalore. '
            'Each card is one person, one accent and one real step of a hiring process. The questions only ask '
            'for what the person says, never for guesses. Before a real interview, do the card with the closest accent.</p>\n'
            '%s\n%s\n'
            '</div><!-- /tab-accents -->\n'
            % (H3, INTRO, painel_aba('accents', 'Your progress in Accents'), '\n\n'.join(cards)))


# ============================================================== SERIES & FILMS
# REGRA 17: link exato. IMDb do titulo, conferido em 15/09/2026. Nada de citar
# fala do roteiro: a cena e descrita, e a tarefa e de escuta + gravacao.

SF = [
    dict(n=1, tipo='Film -- 2011', titulo='Margin Call', imdb='tt1615147',
         sobre='Twenty-four hours inside a New York investment bank at the start of the 2008 crisis.',
         porque='This is the sound of a New York trading floor: fast, clipped and full of numbers. '
                'The senior people keep asking for the short version, exactly like an interviewer does.',
         cena='Watch the late-night meeting after the CEO arrives by helicopter. First with English subtitles, then again without them.',
         pensa='After the meeting scene, explain the bank\'s problem in sixty seconds, as if you were talking to a CEO with no finance background.'),
    dict(n=2, tipo='Film -- 2015', titulo='The Big Short', imdb='tt1596363',
         sobre='A group of investors bets against the US housing market before the 2008 crash.',
         porque='The film stops several times to explain a financial product in plain English. '
                'That is the Lesson 3 skill: unpacking something complex so anyone can follow.',
         cena='Pick one of the scenes where a character turns to the camera to explain a financial term. Watch it twice.',
         pensa='Unpack one concept from your own career, like working capital or a covenant, in sixty seconds and in plain English.'),
    dict(n=3, tipo='Documentary -- 2010', titulo='Inside Job', imdb='tt1645089',
         sobre='A documentary about the causes of the 2008 crisis, told through real interviews.',
         porque='Real bankers, economists and politicians from the United States, the United Kingdom and France, '
                'answering hard questions. It is accent practice with real people under pressure.',
         cena='Watch the first thirty minutes. Note two moments when a person does not really answer the question.',
         pensa='Choose one of those questions and record the answer that person should have given.'),
    dict(n=4, tipo='Series -- Season 1, Episode 1, "Induction"', titulo='Industry', imdb='tt7671070',
         sobre='Young graduates compete for permanent jobs at an investment bank in London.',
         porque='British accents, office English and very fast finance talk. '
                'Good training for a London interview panel.',
         cena='Watch the first episode with English subtitles. Write down five expressions you hear more than once.',
         pensa='Use three of your five expressions in a sixty-second story about your first months in a new job.'),
    dict(n=5, tipo='Series -- Season 1, Episode 1, "Pilot"', titulo='Billions', imdb='tt4270492',
         sobre='A New York hedge fund manager and a federal prosecutor fight each other.',
         porque='The fastest New York English on this list, with a lot of negotiation language. '
                'If you can follow this, a New York recruiter will sound slow.',
         cena='Choose one two-minute scene. Play it three times: subtitles on, subtitles off, then speak along with it.',
         pensa='Record thirty seconds of the scene from memory, at the same speed as the actors.'),
    dict(n=6, tipo='Series -- Season 1, Episode 1, "Celebration"', titulo='Succession', imdb='tt7660850',
         sobre='A family controls a global media company, and the father will not step down.',
         porque='Boardroom language: control, shareholders, the board, the deal. '
                'Useful for any company where a family still decides.',
         cena='Watch the first episode. Pause every time the board or the company\'s future comes up, and repeat the last sentence.',
         pensa='Record sixty seconds of advice for the CFO of a family-controlled company.'),
]


def render_screen():
    cards = []
    for s in SF:
        cards.append(
            '<div class="media-card-wrapper" data-media="sf-title-%d">\n'
            '  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>\n'
            '  <div class="media-card">\n'
            '    <div class="media-thumb">%s</div>\n'
            '    <div class="media-info">\n'
            '      <div class="media-type">%s</div>\n'
            '      <h5>%s</h5>\n'
            '      <p>%s</p>\n'
            '      <p><strong>Why it helps you:</strong> %s</p>\n'
            '      <p class="media-tip">Your task: %s</p>\n'
            '      <a href="https://www.imdb.com/title/%s/" target="_blank" rel="noopener" style="%s">See the title on IMDb &#8599;</a>\n'
            '%s\n'
            '%s\n'
            '    </div>\n'
            '  </div>\n'
            '</div>' % (s['n'], SVG_FILM, esc(s['tipo']), esc(s['titulo']), esc(s['sobre']),
                        esc(s['porque']), esc(s['cena']), s['imdb'], LINK_STYLE,
                        barra_card('sf-title-%d' % s['n']),
                        think(s['pensa'], 'think-result-sf%d' % s['n'])))
    return ('<!-- ========== EXTRAS: SERIES & FILMS (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-screen">\n'
            '<h3 style="%s">Series &amp; Films</h3>\n'
            '<p style="%s">Six titles from the world of finance, chosen for your ear. Watch in three passes: '
            'English subtitles, no subtitles, then one minute where you speak along with the actors. '
            'Each title has a recording task. Mark it as done when you finish both.</p>\n'
            '%s\n'
            '<div class="media-grid">\n%s\n</div>\n'
            '</div><!-- /tab-screen -->\n'
            % (H3, INTRO, painel_aba('screen', 'Your progress in Series & Films'), '\n\n'.join(cards)))


# ================================================================= STUDY WEEK
# Sem exercicio e sem barra: e o mapa. Tabela com rolagem propria no celular.

SEMANA = [
    ('Monday', 'Pre-class of Tuesday\'s lesson (Stages 1 and 2) &middot; one group of Real-Speed English', '40 min'),
    ('Tuesday', 'Class &middot; after class: open the class summary tab, then do the Word Review of that lesson', '20 min'),
    ('Wednesday', 'Pre-class of Thursday\'s lesson &middot; one Accent card &middot; one scene from Series &amp; Films', '60 min'),
    ('Thursday', 'Class &middot; after class: Word Review of that lesson', '20 min'),
    ('Friday', 'Word Review from three days ago (only your mistakes) &middot; one group of Real-Speed English', '40 min'),
    ('Saturday', 'One episode or film from Series &amp; Films, in three passes, plus the recording task', '80 min'),
    ('Sunday', 'Word Review from a week ago (speaking stage only) &middot; one Accent card', '40 min'),
]


def render_studyweek():
    linhas = '\n'.join(
        '      <tr><td style="padding:.6rem .7rem;border-top:1px solid var(--border);font-weight:600;white-space:nowrap">%s</td>'
        '<td style="padding:.6rem .7rem;border-top:1px solid var(--border)">%s</td>'
        '<td style="padding:.6rem .7rem;border-top:1px solid var(--border);white-space:nowrap;color:var(--accent);font-weight:600">%s</td></tr>'
        % d for d in SEMANA)
    tabela = ('    <div style="overflow-x:auto;margin-bottom:1.5rem">\n'
              '    <table style="width:100%%;min-width:520px;border-collapse:collapse;font-size:.88rem;'
              'background:var(--bg-card);border:1px solid var(--border);border-radius:8px">\n'
              '      <tr><th style="text-align:left;padding:.6rem .7rem">Day</th>'
              '<th style="text-align:left;padding:.6rem .7rem">What to do</th>'
              '<th style="text-align:left;padding:.6rem .7rem">Time</th></tr>\n'
              '%s\n    </table>\n    </div>' % linhas)

    def bloco(titulo, pontos):
        itens = '\n'.join('        <li style="margin-bottom:.45rem">%s</li>' % p for p in pontos)
        return ('    <div class="exercise-section">\n'
                '      <div class="section-header-row"><h4>%s</h4></div>\n'
                '      <ul style="font-size:.88rem;line-height:1.6;color:var(--text-mid);padding-left:1.2rem;margin:0">\n%s\n      </ul>\n'
                '    </div>' % (esc(titulo), itens))

    return ('<!-- ========== EXTRAS: YOUR STUDY WEEK (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-studyweek">\n'
            '<h3 style="%s">Your Study Week</h3>\n'
            '<p style="%s">Your plan for about five hours a week outside class, in blocks of twenty minutes. '
            'Every block has one clear job. If a day goes wrong, skip it and follow the next day. Do not try to catch up.</p>\n'
            '%s\n'
            '%s\n'
            '%s\n'
            '%s\n'
            '%s\n'
            '%s\n'
            '</div><!-- /tab-studyweek -->\n'
            % (H3, INTRO,
               nota('The one rule.', 'Do the Pre-class of a lesson BEFORE the class of that lesson. '
                    'The class then uses what you prepared, instead of starting from zero. '
                    'If you are not sure which lesson comes next, ask your teacher at the end of each class.'),
               tabela,
               bloco('After every class', [
                   'Open the <strong>class summary tab</strong> (the last tab at the top of this page). '
                   'Read three parts: the words you did not understand, pronunciation, and corrections.',
                   'Do the <strong>Word Review</strong> of that lesson on the same day or the next day.',
                   'Anything from the summary that is still hard goes into your next Word Review 04 session.']),
               bloco('How to keep new words', [
                   '<strong>Day 1:</strong> the full Word Review of the lesson.',
                   '<strong>Day 3:</strong> the same review again, only the items you got wrong.',
                   '<strong>Day 7:</strong> only the speaking stage. Say each sentence without reading it first.',
                   'Seeing a word at the right time works better than seeing it ten times in one day.']),
               bloco('How to train your ear', [
                   '<strong>Real-Speed English</strong> teaches the sounds an interviewer really makes. Start at 0.75x and always finish at 1x.',
                   '<strong>Accents</strong>: read the questions before you listen. Open the transcript only at the end.',
                   '<strong>Series &amp; Films</strong>: three passes, English subtitles, no subtitles, then speak along for one minute.',
                   'Your brain fills in the words it already knows. Every block here adds to that stock.']),
               bloco('The week of a real interview', [
                   'Two days before: the Accent card closest to your interviewer, twice.',
                   'The day before: Real-Speed English 01 and 04, then record your career story from Word Review 01.',
                   'One hour before: listen to one Accent card at 1x. No new words on the day.'])))


# ============================================================ COLISOES E EMISSAO

def _txt(s):
    return re.sub(r'\s+', ' ', htmllib.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def chaves_de_estado(src):
    """As chaves que o loadState do hub usa para restaurar, em todo o documento."""
    return {
        'blank': set(htmllib.unescape(a).lower().strip() for i in re.findall(r'<input[^>]*class="blank-input"[^>]*>', src)
                     for a in re.findall(r'data-answer="([^"]*)"', i)),
        'matchword': set(_txt(m) for m in re.findall(r'class="match-word"[^>]*>(.*?)</span>', src, re.S)),
        'quiz': set(_txt(t)[:30] for t in re.findall(
            r'<div class="quiz-option[^"]*"[^>]*data-correct="true"[^>]*>(.*?)</div>', src, re.S)),
        'speech': set(htmllib.unescape(p) for p in re.findall(r'<div class="speech-card"[^>]*?data-phrase="([^"]*)"', src)),
        'think': set(_txt(q)[:40] for q in re.findall(r'class="think-question"[^>]*>(.*?)</div>', src, re.S)),
        'vocab': set(_txt(w) for w in re.findall(r'class="vocab-card-word"[^>]*>(.*?)</span>', src, re.S)),
        'media': set(re.findall(r'data-media="([^"]+)"', src)),
    }


def checa_fill_in(snippet, nome):
    norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()  # noqa: E731
    for m in re.finditer(r'<div class="fill-blank-sentence">(.*?)<input[^>]*data-answer="([^"]*)"[^>]*'
                         r'data-phrase="([^"]*)"[^>]*>(.*?)</div>', snippet, re.S):
        antes, resp, frase, depois = (_txt(m.group(1)), htmllib.unescape(m.group(2)),
                                      htmllib.unescape(m.group(3)), _txt(m.group(4)))
        if norm(antes + ' ' + resp + ' ' + depois) != norm(frase):
            sys.exit('ERRO [%s]: fill-in nao fecha com o audio:\n  %s | %s | %s\n  != %s'
                     % (nome, antes, resp, depois, frase))


def checa_colisoes(snippets):
    existentes = None
    for visao in ('aluno', 'professor'):
        hub = open(os.path.join(RAIZ, 'public', visao, SLUG + '.html'), encoding='utf-8').read()
        # O hub pode ja ter as abas (rodada de --replace): as chaves DELAS nao contam.
        for slot, _, _ in snippets:
            hub = re.sub(r'<div class="tab-content" id="tab-%s">.*?</div><!-- /tab-%s -->' % (slot, slot), '', hub, flags=re.S)
        chaves = chaves_de_estado(hub)
        existentes = chaves if existentes is None else {k: existentes[k] | chaves[k] for k in chaves}
    minhas = {k: [] for k in existentes}
    for slot, html, _ in snippets:
        checa_fill_in(html, slot)
        for k, v in chaves_de_estado(html).items():
            minhas[k].extend(v)
    erros = []
    for k, lista in minhas.items():
        for item in set(lista):
            if item in existentes[k]:
                erros.append('%s colide com o material existente: %r' % (k, item))
        # dentro das abas novas tambem nao pode repetir (conta so as unicas por snippet)
    for k in ('blank', 'matchword', 'speech', 'think', 'vocab'):
        vistos = {}
        for slot, html, _ in snippets:
            for item in chaves_de_estado(html)[k]:
                if item in vistos and vistos[item] != slot:
                    erros.append('%s repetido entre abas %s e %s: %r' % (k, vistos[item], slot, item))
                vistos.setdefault(item, slot)
    if erros:
        sys.exit('ERRO: colisao de estado (loadState marcaria uma coisa ao acertar outra):\n  '
                 + '\n  '.join(sorted(erros)))


SNIPPETS = [('studyweek', render_studyweek, 'Your Study Week'),
            ('wordreview', render_wordreview, 'Word Review'),
            ('realspeed', render_realspeed, 'Real-Speed English'),
            ('accents', render_accents, 'Accents'),
            ('screen', render_screen, 'Series & Films')]


def main():
    prontos = [(slot, fn(), rot) for slot, fn, rot in SNIPPETS]
    checa_colisoes(prontos)
    for slot, html, _ in prontos:
        destino = os.path.join(AQUI, slot + '.html')
        with open(destino, 'w', encoding='utf-8') as f:
            f.write(html)
        print('%-16s %6d bytes' % (slot + '.html', len(html.encode('utf-8'))))
    print('colisoes: nenhuma')


if __name__ == '__main__':
    main()
