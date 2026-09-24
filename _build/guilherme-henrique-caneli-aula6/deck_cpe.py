#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os slides IN CLASS da Aula 6 no formato de prova e grava slides.html.

Mesmo caminho da aula 2. O que e generico (envelope do slide, cartoes, escolhas,
pareamento, players, gabarito) vive em ../guilherme-henrique-caneli/cpe_deck.py,
copiado verbatim do builder da aula 2. O que e desta aula -- a prosa, a ordem, a
nota ao professor -- e so o que esta aqui.

USO (da raiz): python3 _build/guilherme-henrique-caneli-aula3/deck_cpe.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'guilherme-henrique-caneli'))
import cpe_deck as D                                                   # noqa: E402
from cpe_deck import (slide, head, card, choices, matching, reveal,    # noqa: E402
                      player, player_mini, vocab_grid, checklist, roleplay, AUDIO)
import lesson6_content as C                                            # noqa: E402

# As sete imagens dos divisores. Os specs nao usam as mesmas chaves em todas as
# aulas (umas tem ch3, outras ch4, outras ch7), entao pega-se o que existe, na
# ordem, sem 'pc' (que e a miniatura da pre-class) e completa-se ciclando. Assim
# nenhuma aula quebra por uma chave que o spec dela nao declarou.
_imgs = [v for k, v in C.L['imgs'].items() if k != 'pc']
IMG = {i: _imgs[(i - 1) % len(_imgs)] for i in range(1, 8)}
PHASES = ['Lead-in', 'The Lexis', 'Reading: Parts 6 &amp; 5', 'Use of English',
          'Listening: Parts 2 &amp; 4', 'What Binds', 'Speaking &amp; Wrap']


def divisor(n, num, titulo, accent, sub):
    slide(n, '<div class="chapter-label">Chapter %d</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             '%s<br><span class="accent">%s</span></h1>'
             '<p class="subtitle">%s</p>' % (num, titulo, accent, sub),
          'Divisor (10 seg).', kind='image', bg=IMG[n])


def deck():
    D.reset()

    # ── FASE 1 — Lead-in ──────────────────────────────────────────────────────
    slide(1, '<div class="passport-badge">Lesson 6</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3.4rem;line-height:1.05;'
             'margin:.6rem 0">The Executive<br><span class="accent">Pen</span></h1>\n'
             '  <p class="subtitle">What a statement commits you to, and the twenty minutes you actually '
             'control</p>',
          'Abertura (2 min): diga a moldura em uma frase -- "hoje tudo e tarefa de prova, e o texto e um '
          'que voce leria de verdade". Nao explique o formato ainda; o slide seguinte faz isso.',
          kind='image', bg=IMG[1])

    plan = ''.join(
        '<div style="display:grid;grid-template-columns:150px 70px 1fr;gap:.7rem;padding:.5rem 0;'
        'border-bottom:1px solid var(--border);font-size:.92rem;align-items:baseline">'
        '<b style="color:var(--accent)">%s</b><span style="color:var(--text-dim)">%s</span>'
        '<span>%s</span></div>' % r for r in [
            ('Lexis', '8 min', 'Discrimination, collocation, and a cloze with one item too many.'),
            ('Reading', '18 min', 'Gapped text (Paper 1, Part 6), then the two questions that separate C1 from C2.'),
            ('Use of English', '8 min', 'Word formation and key-word transformations, said aloud first.'),
            ('Listening', '14 min', 'Multiple matching: five speakers, two tasks at the same time.'),
            ('What Binds', '7 min', 'be to, be supposed to, have to, and the linkers that commit you to a claim.'),
            ('Speaking', '9 min', 'Long turn and follow-up, then two debates, and in the second you do not choose your side.'),
        ])
    slide(1, head('The Shape of Today', 'Every Task Is an', 'Exam Task') +
          card('Cambridge C2 Proficiency format, on your material', plan),
          'Plano (1 min): o formato e o mesmo da aula 2, entao nao reapresente -- diga so o que muda: '
          'hoje a gramatica e o que a frase COMPROMETE, e ela vai ser cobrada no holding statement que ele '
          'tem de dizer em voz alta.')

    slide(1, head('Lead-in', 'Books', 'Closed') +
          card('Answer in full sentences, before any vocabulary appears',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, q)
                   for i, q in enumerate([
                       'Your project is suspended and the first call comes in twenty minutes. What is the '
                       'first sentence you say out loud?',
                       'A statement says something &ldquo;is to&rdquo; happen. Who arranged it, and would '
                       'you put that in writing?',
                       'Name a press release you have read that committed to nothing. How could you tell?'], 1))),
          'Lead-in (5 min): ele responde os tres em voz alta. NAO corrija lingua aqui -- anote duas '
          'imprecisoes de LEXICO para cobrar na fase 2. A terceira pergunta e a semente do artigo.',
          kind='dark')

    slide(1, head('Ninety Seconds', 'Three Sentences,', 'Now') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;Something has just gone wrong. Give '
          'me three sentences, now, that you would be content to see printed.&rdquo;</div>'
          '<div class="ic-predict-q">Do it now, cold. We come back to this recording at the end of the '
          'lesson.</div></div>',
          'Diagnostico (3 min): grave mentalmente TRES coisas: se a primeira frase diz o que MUDOU, se ele promete alguma coisa sem perceber, e se as tres frases cabem numa respiracao. Nao devolva nada agora.', kind='dark')

    # ── FASE 2 — The Lexis ────────────────────────────────────────────────────
    divisor(2, 2, 'The Words of', 'the Release', 'Fourteen terms you half know, separated by what each one does')

    slide(2, head('Collocation', 'Words That', 'Travel Together') +
          card('Say the whole chunk, never the single word',
               '<div class="ic-bank">%s</div>' % ''.join(
                   '<span class="ic-b">%s</span>' % c for c in C.COLLOC_BANK)),
          'Collocation (2 min): ele le em voz alta e diz, para cada uma, QUEM a faz e a quem custa. Chunk '
          'dito solto nao gruda; dito com a consequencia, gruda.')

    slide(2, head('The Front of the Card', 'The Definition', 'Comes First') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vgrid-l6a', 'vcount-l6a', C.VOCAB_CARDS_1),
          'Vocabulario 1 (4 min): a DEFINICAO esta na frente. Ele PRODUZ o termo antes de revelar. Para '
          'quem ja tem o vocabulario passivo, reconhecer nao ensina nada; produzir, sim.')

    slide(2, head('Five More', 'Same Rule,', 'Harder Five') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vgrid-l6b', 'vcount-l6b', C.VOCAB_CARDS_2),
          'Vocabulario 2 (4 min): mesma rotina. Se ele travar, de a COLLOCATION como pista, nunca a '
          'primeira letra.')

    pares = [(str(i + 1), w, 'abcdefgh'[i], m) for i, (w, m) in enumerate(C.MATCH_ROWS)]
    slide(2, matching('Which One Is It, Exactly',
                      'Six terms, six distinctions. Two of them differ by one word.', pares),
          'Discriminacao (4 min): o par que importa e on background x on the record. Nao e formalidade: e '
          'quem fica com a frase depois. Quem confunde os dois ja perdeu a frase.')

    cloze_linhas = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<span class="ic-blank">&nbsp;&nbsp;'
        '</span>%s</span></div>' % (i, it['before'][3:], it['after'])
        for i, it in enumerate(C.CLOZE_ITEMS, 1))
    slide(2, '<div class="cpe-tight">%s</div>' % card('Put the Lexis to Work',
                  '<p style="font-size:.86rem;color:var(--text-mid);margin-bottom:.8rem">Seven gaps, '
                  'eight expressions. One is not needed.</p>' + cloze_linhas +
                  '<div class="ic-bank" style="margin-top:.9rem">%s</div>' % ''.join(
                      '<span class="ic-b">%s</span>' % b for b in C.CLOZE_BANK) +
                  reveal('Which one was not needed?',
                         'Nothing here needs <b>%s</b>. Every one of these seven names a DOCUMENT, a rule or a '
                         'convention; that one names a person.' % C.CLOZE_NOT_NEEDED)),
          'Cloze (5 min): ele diz a expressao INTEIRA, com artigo. Se disser so o substantivo, devolva a '
          'frase e peca de novo: na prova a lacuna aberta e digitada, e o artigo conta.')

    slide(2, choices('Which of these would a communications director <b>not</b> say?', [
        ('A', 'We will issue a holding statement within the hour.', False),
        ('B', 'That part was on background, so please do not attribute it.', False),
        ('C', 'Let me put the boilerplate on the record for you.', True),
        ('D', 'The guidance is specific enough to be useful and no more.', False)]) +
        reveal('Why C is the one',
               'Boilerplate is already public and already attributed: it is the fixed paragraph at the '
               'foot of every release. Putting it &ldquo;on the record&rdquo; is an offer of something the '
               'journalist already has. The collocation exists; the transaction does not, and offering it '
               'signals that you do not know which of your words are worth anything.'),
        'Registro (3 min): esta e a pergunta que separa quem sabe a palavra de quem sabe o uso. Se ele '
        'acertar de primeira, peca para reescrever (C) de um jeito que funcione.')

    # ── FASE 3 — Reading ──────────────────────────────────────────────────────
    divisor(3, 3, 'Everything Leaks,', 'and Timing Is the Message', 'Paper 1, Part 6: six sentences removed, seven on offer, one useless')

    slide(3, head('Before You Read', 'One Line, One', 'Prediction') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;Every organisation eventually '
          'discovers that it does not control when its news becomes public.&rdquo;</div>'
          '<div class="ic-predict-q">That is the first sentence. What is the writer about to say it DOES '
          'control?</div></div>',
          'Predicao (2 min): aceite QUALQUER palpite, nao confirme nem corrija. A predicao ativa o que '
          'ele ja sabe; o que importa e ele perceber depois que a frase monta um contraste.',
          kind='dark', extra=' data-task-for="reading"')

    frases = ''.join(
        '<div class="cpe-sent"><span class="cpe-sent-k">%s</span><span>%s</span></div>' % (k, v)
        for k, v in C.GAP_OPTIONS)
    slide(3, head('Paper 1, Part 6', 'The Seven', 'Sentences') +
          '<div class="ic-card cpe-sent-card"><div class="ic-card-h3">Six gaps, seven sentences. '
          'One of them fits nowhere.</div><div class="cpe-sents">%s</div>'
          '<p class="cpe-sent-foot">Keep these in front of you while you read. Decide each gap by what '
          'the text points back to, not by what sounds true.</p></div>' % frases,
          'ESTA e a tela da foto (1 min). Antes da leitura, peca que ele fotografe a tela: as sete frases '
          'ficam com ele enquanto o texto passa pagina a pagina. Nao discuta nenhuma delas aqui.')

    def artigo(paras, gaps):
        out = []
        for before, n, after in paras:
            if n:
                out.append('<p>%s<span class="ic-blank"><span class="ic-n">%d</span></span>%s</p>'
                           % (before, n, after))
            else:
                out.append('<p>%s</p>' % before)
        return ('<div class="ic-reading"><div class="ic-rtitle">%s</div>%s'
                '<div class="ic-src">%s &middot; gaps %s</div></div>'
                % (C.ARTICLE_TITLE, ''.join(out), C.ARTICLE_STANDFIRST, gaps))

    # Quatro telas, pelo mesmo motivo da aula 2: tres paragrafos por tela cortam
    # a ultima linha num projetor de 1280x800, e a ultima linha e a que conta.
    slide(3, head('The Text', 'Paragraphs One and', 'Two') + artigo(C.ARTICLE[:2], '1 and 2'),
          'Leitura (3 min): em SILENCIO, paragrafo a paragrafo, e ele diz em uma frase o que cada um faz '
          'no argumento. Nao deixe ir para as opcoes antes disso.')
    slide(3, head('The Text', 'Paragraphs Three and', 'Four') + artigo(C.ARTICLE[2:4], '3 and 4'),
          'Leitura (3 min): peca a ligacao entre os dois antes de virar. O terceiro e convencao; o quarto '
          'e LEI, e a virada entre os dois e o ponto.')
    slide(3, head('The Text', 'Paragraphs Five and', 'Six') + artigo(C.ARTICLE[4:6], '5 and 6'),
          'Leitura (3 min): aqui entram os instrumentos e o oficio. Se ele reconhecer isto do trabalho '
          'dele, otimo: a tarefa nao e entender o conteudo, e achar a frase que falta.')

    slide(3, head('Before the Last Paragraph', 'Predict, Then', 'Place') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;Underneath all of it sits one test, '
          'and it has not changed in thirty years.&rdquo;</div>'
          '<div class="ic-predict-q">That is how the last paragraph opens, and it is the only one with no '
          'gap. What kind of test is it about to be: legal, editorial, or human?</div></div>'
          '<div class="ic-card" style="margin-top:1rem"><div class="ic-card-h3">Then the task you have '
          'been reading for</div>'
          '<div class="comp-q comp-q-task"><div class="q-text">Gap 1 -- which sentence belongs here?'
          '</div></div>'
          '<p style="font-size:.92rem;color:var(--text-mid);margin:.6rem 0 0">Six gaps, seven sentences, '
          'one of them useless. Decide each by what the text points back to, not by what sounds true.</p>'
          '</div>',
          'Tarefa (2 min): ele responde a predicao PRIMEIRO, em uma palavra. Depois diz de qual lacuna '
          'menos tem certeza. Anote: quase sempre e a 4, que se resolve por UMA palavra citada.',
          extra=' data-task-for="reading"')

    slide(3, head('The Text', 'The Last', 'Paragraph') + artigo(C.ARTICLE[6:], 'no gap') +
          '<p style="margin-top:.9rem;font-size:.95rem;color:var(--text-mid)">No gap here. Read it '
          'twice.</p>',
          'Fecho da leitura (2 min): sem lacuna de proposito. Peca que ele leia em voz alta a ultima frase '
          'e diga a diferenca entre escrito e montado. E ela que volta no follow-up.')

    letras = {k: v for k, v in C.GAP_OPTIONS}
    for gap_n, right in C.GAP_ANSWERS:
        opts = [(k, letras[k], k == right) for k, _v in C.GAP_OPTIONS]
        slide(3, choices('Gap %s -- which sentence belongs here?' % gap_n, opts, cls='cpe-long'),
              'Gap %s (2 min): a resposta e %s. Exija a PROVA antes do clique: qual palavra da frase '
              'seguinte aponta para tras. Se ele acertar por eliminacao, pergunte por que cada descartada '
              'foi descartada.' % (gap_n, right))

    slide(3, choices('One sentence fits <b>no</b> gap at all. Which one, and what is wrong with it?', [
        ('A', letras['A'], False), ('D', letras['D'], True),
        ('F', letras['F'], False), ('G', letras['G'], False)], cls='cpe-long') +
        reveal('Why D is the distractor',
               'D is true, it is on topic, and it would sit comfortably in a conversation about this '
               'article. What it never does is answer a reference or complete an argument. That is the '
               'whole test: a gapped text is not asking what is true, it is asking what is '
               '<i>cohesive</i>.'),
        'O distrator (3 min): este e o slide que mais ensina. Faca ele TENTAR encaixar D em cada lacuna e '
        'dizer, em cada uma, o que quebra.')

    q3 = C.MCQ[2]
    slide(3, choices(q3[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q3[1])]) +
          reveal('The trap in (a) and (d)',
                 'Both are TRUE statements about corridors. They are still wrong, because the question '
                 'asks what the sentence is <i>for</i>, not what it contains. In Part 5, at least one '
                 'option in every item is true and irrelevant.'),
          'Discriminador 1 (4 min): se ele escolher (a), NAO diga que errou. Pergunte: "is that what the '
          'sentence says, or what the sentence is doing?". Essa distincao e a diferenca entre C1 e C2 em '
          'leitura.')

    q6 = C.MCQ[5]
    slide(3, choices(q6[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q6[1])]) +
          reveal('Why this matters today',
                 'The writer ends on what the room EXPOSES, not on what it decides. That is the bridge '
                 'into the grammar: an inversion does the same job in one sentence -- it puts the thing '
                 'you want noticed where it cannot be skipped.'),
          'Discriminador 2 (3 min): termine a leitura AQUI e deixe a frase no ar. O proximo capitulo '
          'devolve isso como gramatica.')

    # ── FASE 4 — Use of English ───────────────────────────────────────────────
    divisor(4, 4, 'Use of', 'English', 'Paper 1, Parts 3 and 4: the word family, and the same meaning in other words')

    wf_rows = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<span class="ic-blank">&nbsp;&nbsp;'
        '</span>%s</span></div>' % (i, it['before'], it['after'])
        for i, it in enumerate(C.WORD_FORMATION[:5], 1))
    slide(4, head('Part 3', 'Word', 'Formation') +
          card('Say the word before you write it', wf_rows +
               reveal('Reveal 1 to 5', '1 attributable &middot; 2 announcement &middot; 3 selective &middot; '
                                       '4 equality &middot; 5 correction')),
          'Word formation (4 min): ele fez em casa, com OUTROS itens. Aqui cobre a FAMILIA: de '
          '"attribute", quantas palavras em dez segundos (attribution, attributable, attributed)?')

    def kwt(items, ini):
        linhas = ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<br>'
            '<span style="font-size:.74rem;letter-spacing:.1em;font-weight:800;color:var(--accent)">%s'
            '</span><br>%s<span class="ic-blank">&nbsp;&nbsp;</span>%s</span></div>'
            % (ini + i, t['lead'], t['key'], t['before'], t['after']) for i, t in enumerate(items))
        return linhas

    slide(4, head('Part 4', 'Key-word', 'Transformations') +
          card('Three to eight words. Do not change the key word.', kwt(C.TRANSFORMATIONS[:3], 1)),
          'Transformations 1 (4 min): ele DIZ antes de escrever. Os itens 1 e 2 parecem iguais e nao sao: '
          'um e arranjo, o outro e obrigacao de fora. Pergunte QUEM impoe cada um.')

    slide(4, head('Part 4', 'Three', 'More') +
          card('Same rule, harder three', kwt(C.TRANSFORMATIONS[3:], 4) +
               reveal('Reveal the answer key', C.TRANSFORM_KEY)),
          'Transformations 2 (4 min): o item 5 (MEANT) e o que separa o C1 do C2 aqui -- "was meant to" '
          'carrega que NAO aconteceu, e quase todo mundo escreve como se fosse neutro.')

    slide(4, head('Application', 'Your Three', 'Sentences') +
          card('Take the three sentences you gave at the start of the lesson',
               '<div class="ic-lf-list">'
               '<div class="ic-lf"><span class="ic-lbl">1</span><span>Say it again, exactly as you said '
               'it.</span></div>'
               '<div class="ic-lf"><span class="ic-lbl">2</span><span>Now mark every word in them that '
               'commits you to something, and say who is imposing it.</span></div>'
               '<div class="ic-lf"><span class="ic-lbl">3</span><span>Which one would you still be content '
               'to have said in six months? Keep that one, cut the rest.</span></div></div>'),
          'Aplicacao (4 min): este e o slide que liga a gramatica ao risco dele. A pergunta 3 e a que '
          'conta -- e o teste de seis meses, e quase sempre sobra uma frase de tres.',
          kind='dark')

    # ── FASE 5 — Listening ────────────────────────────────────────────────────
    divisor(5, 5, 'Five Voices,', 'Two Tasks', 'Paper 3, Part 4: what each speaker is, and what each one is arguing')

    slide(5, head('Part 2 -- Checked', 'The Talk You Heard at', 'Home') +
          player('mp-l6-talk', AUDIO + C.TALK_FILE,
                 'Three minutes. He completed the eight sentences before the lesson.') +
          reveal('The eight answers',
                 '1 two &middot; 2 four hundred &middot; 3 business &middot; 4 forty &middot; '
                 '5 the hour &middot; 6 friends &middot; 7 commits &middot; 8 sentence'),
          'Checagem (4 min): NAO toque o audio inteiro de novo. Toque so os trechos dos itens que ele '
          'errou, e pergunte o que ele OUVIU em vez do que estava la. Em Part 2 o erro quase nunca e de '
          'compreensao: e de escrever o sinonimo em vez da palavra dita.',
          kind='dark')

    for s in C.SPEAKERS:
        slide(5, head('Speaker %d' % s['n'], 'Listen', 'Twice') +
              player('mp-l6-mm%d' % s['n'], AUDIO + s['file'],
                     'First pass: what is this person? Second pass: what is the argument?'),
              'Falante %d (2 min): toque duas vezes, sem texto. Na primeira, so a Task One. Na segunda, a '
              'Task Two. Nao deixe ele anotar as duas de uma vez -- a tarefa dupla e o que a prova mede.'
              % s['n'], kind='dark')

    t1 = {k: v for k, v in C.TASK1_OPTS}
    t2 = {k: v for k, v in C.TASK2_OPTS}
    tira = ''.join(player_mini('mp-l6-mmx%d' % sp['n'], AUDIO + sp['file'], 'Speaker %d' % sp['n'])
                   for sp in C.SPEAKERS)
    caixa1 = matching('Task One &mdash; what each speaker <b>is</b>',
                      'Three of the eight roles are not used.',
                      [(str(sp['n']), 'Speaker %d' % sp['n'], sp['task1'], t1[sp['task1']])
                       for sp in C.SPEAKERS], opts=C.TASK1_OPTS)
    caixa2 = matching('Task Two &mdash; the main point each one <b>makes</b>',
                      'Three of the eight points are not used.',
                      [(str(sp['n']), 'Speaker %d' % sp['n'], sp['task2'], t2[sp['task2']])
                       for sp in C.SPEAKERS], opts=C.TASK2_OPTS)
    slide(5, head('Paper 3, Part 4', 'Two Tasks,', 'One Page') +
          '<p class="cpe-exam-intro">Five speakers, heard twice. <b>Task One:</b> what each speaker '
          '<i>is</i>. <b>Task Two:</b> the main point each one <i>makes</i>. Three letters in each list '
          'are not used.</p>'
          '<div class="cpe-mini-row">%s</div><div class="cpe-two">%s%s</div>' % (tira, caixa1, caixa2),
          'A pagina inteira (8 min): toque os cinco seguidos, sem parar, com as duas listas na tela. Na '
          'primeira passada ele fecha a Task One; na segunda, a Task Two. Nao separe as tarefas em duas '
          'telas -- fazer as duas ao mesmo tempo E o que a Part 4 mede.')

    slide(5, head('Part 4', 'What Gave Each One', 'Away') +
          reveal('Task One &mdash; key, and the word that decides it',
                 '1 B (&ldquo;the meeting before the <i>writing</i>&rdquo;) &middot; 2 E (&ldquo;I have '
                 'been on the <i>receiving end</i>&rdquo;, &ldquo;somebody else writes the story&rdquo;) '
                 '&middot; 3 A (&ldquo;the brake on the release&rdquo;, &ldquo;we can still say it&rdquo;) '
                 '&middot; 4 F (&ldquo;we used to give one paper&rdquo;, &ldquo;we announced&rdquo;) '
                 '&middot; 5 C (&ldquo;The rules&rdquo;, &ldquo;gets companies into difficulty&rdquo;).') +
          reveal('Task Two &mdash; key, and why the extra three are there',
                 '1 D &middot; 2 A &middot; 3 F &middot; 4 B &middot; 5 H. '
                 'The unused options (C, E, G) are all things these people might plausibly believe. None '
                 'of them is what any of them said. Speaker 3 is the trap: a lawyer sounds like somebody '
                 'who wants everything vaguer, and she argues the opposite.'),
          'Correcao (5 min): a pista da Task One nunca e o assunto, e o PRONOME e o verbo -- faca ele '
          'apontar a palavra exata. Na Task Two, cobre a diferenca entre "o que ele diria" e "o que ele '
          'disse": as tres que sobram existem para pegar quem responde pelo perfil do falante.')

    # ── FASE 6 — The Inversion ────────────────────────────────────────────────
    divisor(6, 6, 'What the Sentence', 'Commits You To', 'be to, be supposed to, have to -- and who is imposing each of them')

    def linhas(rs, base):
        return ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span><b>%s</b><br>'
            '<span style="font-size:.88rem;color:var(--text-mid)">%s</span><br>'
            '<span style="font-size:.9rem">%s</span></span></div>' % (base + i, a, b, c)
            for i, (a, b, c) in enumerate(rs))

    slide(6, head('The Forms', 'Four That Look', 'Alike') +
          '<div class="cpe-tight">%s</div>' % card(
              'What each one commits you to, and who is imposing it',
              linhas(C.GRAMMAR_ROWS[:4], 1)),
          'Formas 1 (3 min): nao explique a regra -- ele ja a tem. Pergunte, em cada linha, QUEM impoe: '
          'voce, outra pessoa, ou a lei. E ai que as quatro deixam de parecer iguais.')

    slide(6, head('The Forms', 'Three', 'More') +
          card('The linkers, and which of them commits you to a claim',
               linhas(C.GRAMMAR_ROWS[4:], 5)),
          'Formas 2 (3 min): "given" e o unico da lista que afirma uma CAUSA. Os outros contrastam ou '
          'mudam de assunto. Peca um exemplo do trabalho dele com cada um.')

    for i, q in enumerate(C.GRAMMAR_QUIZ[:3], 1):
        slide(6, choices(q[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q[1])]),
              'Discriminacao %d (2 min): o erro util aqui e achar que sao variacoes de estilo. Se ele marcar '
              '"mais formal", pergunte quem ficaria responsavel se a frase nao se cumprisse.' % i)

    slide(6, choices(C.GRAMMAR_QUIZ[3][0], [(k, t, ok) for k, (t, ok) in zip('abcd', C.GRAMMAR_QUIZ[3][1])]) +
          reveal('Why the answer is (b)',
                 'GIVEN asserts a cause: it says the guidance is the reason. WHEREAS contrasts, '
                 'NOTWITHSTANDING concedes, and AS REGARDS merely changes the subject. Only one of the '
                 'four puts the writer behind a causal claim, and in a release that is where the exposure '
                 'sits.'),
          'Discriminacao 4 (3 min): este e o item que liga a gramatica ao risco. Se ele errar, devolva a '
          'pergunta: "which of these four would you have to defend if the cause turned out to be wrong?"')

    prod = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<span class="ic-blank">&nbsp;&nbsp;'
        '</span>%s</span></div>' % (i, it['before'], it['after'])
        for i, it in enumerate(C.GRAMMAR_PRODUCTION, 1))
    slide(6, head('Produce It', 'Say Who', 'Imposed It') +
          card('Say each one, then say WHO arranged or imposed it. If you cannot, the sentence is not finished',
               prod + reveal('Reveal', '1 is due to be issued &middot; 2 was supposed to reach &middot; '
                                       '3 Given the embargo, &middot; 4 provided that every party has')),
          'Producao (5 min): depois de cada uma, ele nomeia QUEM impos. O item 2 e o mais importante: '
          '"was supposed to" ja diz que nao aconteceu, e se ele nao ouvir isso, vai escrever promessas '
          'quebradas achando que sao neutras.')

    # ── FASE 7 — Speaking & Wrap ──────────────────────────────────────────────
    divisor(7, 7, 'Your', 'Turn', 'The long turn, the follow-up, and two debates')

    slide(7, head('Role-play -- Guided', 'Two Minutes,', 'With Support') +
          roleplay(C.ROLEPLAY_SCENARIO, C.ROLEPLAY_CHIPS),
          C.ROLEPLAY_TEACHER)

    slide(7, head('Collaborative Task', 'Three Sentences,', 'Ten Minutes') + card('Four minutes, together',
          '<p style="font-size:.95rem;line-height:1.7">%s</p>' % C.COLLAB_TASK),
          'Collaborative (4 min): entre como PAR, nao como professor. Defenda a quarta frase com forca. O '
          'que se mede e se ele corta sob pressao, que e exatamente o que o texto diz que ninguem faz.')

    slide(7, head('Long Turn', 'Two Minutes,', 'Uninterrupted') +
          card('No notes. No apology at the start.',
               '<p style="font-size:.95rem;line-height:1.7">%s</p>' % C.LONG_TURN),
          'Long turn (3 min): NAO interrompa, nem para elogiar. Anote tres coisas: se a primeira frase diz '
          'o que mudou, quantos linkers formais ele produz sem pensar, e a melhor frase dele. Compare com '
          'as tres frases do slide 4.', kind='dark')

    slide(7, head('Follow-up', 'Four Questions,', 'No Restarting') +
          card(C.FOLLOW_UP_INTRO,
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, q)
                   for i, q in enumerate(C.FOLLOW_UP, 1))),
          C.FOLLOW_UP_TEACHER)

    slide(7, head('Debate One', 'Defend the Side You', 'Disagree With') +
          card(C.DEBATE_1_MOTION,
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, r)
                   for i, r in enumerate(C.DEBATE_1_RULES, 1))),
          'Debate 1 (5 min): ele escolhe o lado, e abre pelo argumento mais forte CONTRA si mesmo. Cobre a '
          'regra 3: dois linkers formais por turno, e "however" so uma vez na rodada inteira.')

    slide(7, head('Debate Two', 'The Side You Were', 'Given') +
          card(C.DEBATE_2_MOTION,
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, r)
                   for i, r in enumerate(C.DEBATE_2_RULES, 1))),
          C.DEBATE_2_TEACHER)

    slide(7, head('Writing', 'The Proposal,', 'For Next Time') +
          card('Paper 2, Part 2',
               '<p style="font-size:.95rem;line-height:1.7">%s</p>' % C.WRITING_TASK +
               reveal('What the teacher will be reading for', C.WRITING_MODEL)),
          C.WRITING_TEACHER)

    sp = ''.join('<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, p)
                 for i, p in enumerate(C.SPEECH_PHRASES, 1))
    slide(7, head('Survival', 'Five Sentences for', 'the Front of a Room') +
          card('Say each one with the stress where it belongs', '<div class="ic-lf-list">%s</div>' % sp),
          'Survival (2 min): ele repete as cinco com a tonica no fim. Sao as mesmas da pre-class, de '
          'proposito: e a terceira exposicao, e a que ele leva para a sala de verdade.')

    slide(7, head('Self-Assessment', 'What I Can Do', 'Now') +
          card('Tick only what is true',
               checklist([
                   'I can read a gapped text and justify each choice by reference, not by topic.',
                   'I can spot the option that is true and still wrong.',
                   'I can hear five speakers and separate what they are from what they argue.',
                   'I can tell what a sentence commits me to, and say who is imposing it.',
                   'I can write three sentences I would still be content to have said in six months.'])),
          'Autoavaliacao (2 min): peca uma PROVA oral de cada item marcado. O que ele nao marcar entra '
          'como foco da aula 7.')

    slide(7, '<div class="chapter-label">Lesson Complete</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'The Executive Pen<br><span class="accent">Badge Earned</span></h1>'
             '<p class="subtitle">What the sentence commits you to, and the twenty minutes you control</p>'
             '<p style="margin-top:1.2rem;font-size:.95rem;color:rgba(255,255,255,.8)">Homework: the '
             'statement and the note, 280 to 320 words. Next lesson: The Full Room.</p>',
          'Fechamento (1 min): devolva as tres anotacoes do long turn, nessa ordem: lexico, promessa '
          'feita sem perceber, melhor frase. Termine pela melhor frase dele.', kind='image', bg=IMG[1])


if __name__ == '__main__':
    deck()
    # Nome proprio: o mklesson.py TAMBEM grava slides.html nesta pasta, a partir
    # do spec antigo. Se os dois usassem o mesmo nome, quem rodasse por ultimo venceria,
    # e o deck de prova sumiria sem erro nenhum.
    D.write(HERE, PHASES, 'slides_cpe.html')
