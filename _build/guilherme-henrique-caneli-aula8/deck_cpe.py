#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os slides IN CLASS da Aula 8 no formato de prova e grava slides.html.

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
import lesson8_content as C                                            # noqa: E402

# As sete imagens dos divisores. Os specs nao usam as mesmas chaves em todas as
# aulas (umas tem ch3, outras ch4, outras ch7), entao pega-se o que existe, na
# ordem, sem 'pc' (que e a miniatura da pre-class) e completa-se ciclando. Assim
# nenhuma aula quebra por uma chave que o spec dela nao declarou.
_imgs = [v for k, v in C.L['imgs'].items() if k != 'pc']
IMG = {i: _imgs[(i - 1) % len(_imgs)] for i in range(1, 8)}
PHASES = ['Lead-in', 'The Lexis', 'Reading: Parts 6 &amp; 5', 'Use of English',
          'Listening: Parts 2 &amp; 4', 'Commitments', 'Speaking &amp; Wrap']


def divisor(n, num, titulo, accent, sub):
    slide(n, '<div class="chapter-label">Chapter %d</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             '%s<br><span class="accent">%s</span></h1>'
             '<p class="subtitle">%s</p>' % (num, titulo, accent, sub),
          'Divisor (10 seg).', kind='image', bg=IMG[n])


def deck():
    D.reset()

    # ── FASE 1 — Lead-in ──────────────────────────────────────────────────────
    slide(1, '<div class="passport-badge">Lesson 8</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3.4rem;line-height:1.05;'
             'margin:.6rem 0">Full<br><span class="accent">Circle</span></h1>\n'
             '  <p class="subtitle">The three hundred and sixty-two days nobody measures, and the tense '
             'that puts a date on a promise</p>',
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
            ('Commitments', '7 min', 'Future perfect and future continuous: landing on a date, or running across a period.'),
            ('Speaking', '9 min', 'Long turn and follow-up, then two debates, and in the second you do not choose your side.'),
        ])
    slide(1, head('The Shape of Today', 'Every Task Is an', 'Exam Task') +
          card('Cambridge C2 Proficiency format, on your material', plan),
          'Plano (1 min): o formato e o mesmo da aula 2, entao nao reapresente -- diga so o que muda: '
          'hoje a gramatica e o tempo do compromisso, e ela vai ser cobrada no long turn: tres promessas, '
          'cada uma com um mes. E a ultima aula do pacote.')

    slide(1, head('Lead-in', 'Books', 'Closed') +
          card('Answer in full sentences, before any vocabulary appears',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, q)
                   for i, q in enumerate([
                       'Name a commitment you made in a meeting this year. Did it carry a date? What '
                       'happened to it?',
                       'Fourteen action items are agreed and photographed on a flipchart. What happens to '
                       'them, and why?',
                       'When did you last read a document that admitted something had failed? What did it '
                       'change?'], 1))),
          'Lead-in (5 min): ele responde os tres em voz alta. NAO corrija lingua aqui -- anote duas '
          'imprecisoes de LEXICO para cobrar na fase 2. A terceira pergunta e a semente do artigo.',
          kind='dark')

    slide(1, head('Ninety Seconds', 'Close the', 'Year') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;Close a three-day forum for me. '
          'Ninety seconds, and every promise you make has to carry a month.&rdquo;</div>'
          '<div class="ic-predict-q">Do it now, cold. We come back to this recording at the end of the '
          'lesson.</div></div>',
          'Diagnostico (3 min): grave mentalmente TRES coisas: quantos compromissos ele faz, quantos tem data, e se algum tem NOME de dono. Nao devolva nada agora -- isto volta no long turn, e e a ultima comparacao do pacote.', kind='dark')

    # ── FASE 2 — The Lexis ────────────────────────────────────────────────────
    divisor(2, 2, 'The Words of', 'the Year After', 'Fourteen terms you half know, separated by what each one does')

    slide(2, head('Collocation', 'Words That', 'Travel Together') +
          card('Say the whole chunk, never the single word',
               '<div class="ic-bank">%s</div>' % ''.join(
                   '<span class="ic-b">%s</span>' % c for c in C.COLLOC_BANK)),
          'Collocation (2 min): ele le em voz alta e diz, para cada uma, QUANDO no ano ela acontece. Chunk '
          'dito solto nao gruda; dito com o ponto do calendario, gruda.')

    slide(2, head('The Front of the Card', 'The Definition', 'Comes First') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vgrid-l8a', 'vcount-l8a', C.VOCAB_CARDS_1),
          'Vocabulario 1 (4 min): a DEFINICAO esta na frente. Ele PRODUZ o termo antes de revelar. Para '
          'quem ja tem o vocabulario passivo, reconhecer nao ensina nada; produzir, sim.')

    slide(2, head('Five More', 'Same Rule,', 'Harder Five') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vgrid-l8b', 'vcount-l8b', C.VOCAB_CARDS_2),
          'Vocabulario 2 (4 min): mesma rotina. Se ele travar, de a COLLOCATION como pista, nunca a '
          'primeira letra.')

    pares = [(str(i + 1), w, 'abcdefgh'[i], m) for i, (w, m) in enumerate(C.MATCH_ROWS)]
    slide(2, matching('Which One Is It, Exactly',
                      'Six terms, six distinctions. Two of them differ by one word.', pares),
          'Discriminacao (4 min): o par que importa e benchmark x milestone, e a confusao custa dinheiro. '
          'Um e dos outros, o outro e seu. Quem troca os dois bate todas as metas e perde mercado.')

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
                         'Nothing here needs <b>%s</b>. Every one of these seven names an instrument or a '
                         'measure; that one names the occasion where they are used.' % C.CLOZE_NOT_NEEDED)),
          'Cloze (5 min): ele diz a expressao INTEIRA, com artigo. Se disser so o substantivo, devolva a '
          'frase e peca de novo: na prova a lacuna aberta e digitada, e o artigo conta.')

    slide(2, choices('Which of these would somebody who runs the year after <b>not</b> say?', [
        ('A', 'We will circle back at ninety days on those three items.', False),
        ('B', 'The debrief is on Thursday, while people still remember it.', False),
        ('C', 'We set the benchmark ourselves at the start of the year.', True),
        ('D', 'Every action item on the roadmap has a name against it.', False)]) +
        reveal('Why C is the one',
               'You cannot set your own benchmark. A benchmark is external by definition: it is somebody '
               'else&rsquo;s performance, and that is the whole reason it is worth measuring against. What '
               'you set yourself is a milestone. Say (C) in a board meeting and you have announced, '
               'without meaning to, that you are marking your own work.'),
        'Registro (3 min): esta e a pergunta que separa quem sabe a palavra de quem sabe o uso. Se ele '
        'acertar de primeira, peca para reescrever (C) de um jeito que funcione.')

    # ── FASE 3 — Reading ──────────────────────────────────────────────────────
    divisor(3, 3, 'The Year Between', 'Two Conferences', 'Paper 1, Part 6: six sentences removed, seven on offer, one useless')

    slide(3, head('Before You Read', 'One Line, One', 'Prediction') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;The interesting part of an annual '
          'event is not the three days.&rdquo;</div>'
          '<div class="ic-predict-q">That is the first sentence. What is the writer about to say the '
          'interesting part IS?</div></div>',
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
          'Leitura (3 min): peca a ligacao entre os dois antes de virar. O terceiro e a GRAMATICA disfarcada '
          'de conselho; o quarto e o maquinario. Guarde as duas frases citadas: voltam na fase 6.')
    slide(3, head('The Text', 'Paragraphs Five and', 'Six') + artigo(C.ARTICLE[4:6], '5 and 6'),
          'Leitura (3 min): aqui entram benchmark x milestone e o retrospective. Se ele reconhecer isto do '
          'trabalho dele, otimo: a tarefa nao e entender o conteudo, e achar a frase que falta.')

    slide(3, head('Before the Last Paragraph', 'Predict, Then', 'Place') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;The test is crude and it '
          'works.&rdquo;</div>'
          '<div class="ic-predict-q">That is how the last paragraph opens, and it is the only one with no '
          'gap. Who does the writer say you should ask, and when?</div></div>'
          '<div class="ic-card" style="margin-top:1rem"><div class="ic-card-h3">Then the task you have '
          'been reading for</div>'
          '<div class="comp-q comp-q-task"><div class="q-text">Gap 1 -- which sentence belongs here?'
          '</div></div>'
          '<p style="font-size:.92rem;color:var(--text-mid);margin:.6rem 0 0">Six gaps, seven sentences, '
          'one of them useless. Decide each by what the text points back to, not by what sounds true.</p>'
          '</div>',
          'Tarefa (2 min): ele responde a predicao PRIMEIRO, em uma palavra. Depois diz de qual lacuna '
          'menos tem certeza. Anote: a 6 e a unica que se resolve por GRAMATICA -- o paragrafo termina '
          'em dois pontos, e so uma opcao completa a frase.',
          extra=' data-task-for="reading"')

    slide(3, head('The Text', 'The Last', 'Paragraph') + artigo(C.ARTICLE[6:], 'no gap') +
          '<p style="margin-top:.9rem;font-size:.95rem;color:var(--text-mid)">No gap here. Read it '
          'twice.</p>',
          'Fecho da leitura (2 min): sem lacuna de proposito. Peca que ele aplique o teste ao ultimo evento '
          'em que ele falou: quatro pessoas, duas semanas depois, diriam a mesma coisa?')

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
               reveal('Reveal 1 to 5', '1 measurable &middot; 2 achievement &middot; 3 commitment &middot; '
                                       '4 accountability &middot; 5 persistence')),
          'Word formation (4 min): ele fez em casa, com OUTROS itens. Aqui cobre a FAMILIA: de "commit", '
          'quantas palavras em dez segundos (commitment, committed, non-committal, committee)?')

    def kwt(items, ini):
        linhas = ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<br>'
            '<span style="font-size:.74rem;letter-spacing:.1em;font-weight:800;color:var(--accent)">%s'
            '</span><br>%s<span class="ic-blank">&nbsp;&nbsp;</span>%s</span></div>'
            % (ini + i, t['lead'], t['key'], t['before'], t['after']) for i, t in enumerate(items))
        return linhas

    slide(4, head('Part 4', 'Key-word', 'Transformations') +
          card('Three to eight words. Do not change the key word.', kwt(C.TRANSFORMATIONS[:3], 1)),
          'Transformations 1 (4 min): ele DIZ antes de escrever. Pergunte, em cada item, se a frase pousa '
          'NUMA data ou atravessa um PERIODO -- e isso, e nao a dificuldade, que escolhe a forma.')

    slide(4, head('Part 4', 'Three', 'More') +
          card('Same rule, harder three', kwt(C.TRANSFORMATIONS[3:], 4) +
               reveal('Reveal the answer key', C.TRANSFORM_KEY)),
          'Transformations 2 (4 min): o item 4 (SINCE) e o mais dificil do pacote inteiro -- futuro '
          'perfeito medindo um intervalo a partir de um ponto no futuro. Se travar, escreva a linha do '
          'tempo na tela.')

    slide(4, head('Application', 'The Year You', 'Closed Cold') +
          card('Take the closing you recorded ninety minutes ago',
               '<div class="ic-lf-list">'
               '<div class="ic-lf"><span class="ic-lbl">1</span><span>Say it again, exactly as you said '
               'it.</span></div>'
               '<div class="ic-lf"><span class="ic-lbl">2</span><span>Now say it again with exactly '
               'three commitments, each carrying a month and a name.</span></div>'
               '<div class="ic-lf"><span class="ic-lbl">3</span><span>Which of the three would you still '
               'be able to report on in a year? Cut the others.</span></div></div>'),
          'Aplicacao (4 min): este e o slide que fecha o pacote. A pergunta 3 e a que conta: quase sempre '
          'sobra um de tres, e reconhecer isso em voz alta vale mais do que a aula inteira.',
          kind='dark')

    # ── FASE 5 — Listening ────────────────────────────────────────────────────
    divisor(5, 5, 'Five Voices,', 'Two Tasks', 'Paper 3, Part 4: what each speaker is, and what each one is arguing')

    slide(5, head('Part 2 -- Checked', 'The Talk You Heard at', 'Home') +
          player('mp-l8-talk', AUDIO + C.TALK_FILE,
                 'Three minutes. He completed the eight sentences before the lesson.') +
          reveal('The eight answers',
                 '1 nothing happened &middot; 2 energised &middot; 3 flipchart &middot; 4 future '
                 '&middot; 5 day &middot; 6 seven &middot; 7 summary &middot; 8 market share'),
          'Checagem (4 min): NAO toque o audio inteiro de novo. Toque so os trechos dos itens que ele '
          'errou, e pergunte o que ele OUVIU em vez do que estava la. Em Part 2 o erro quase nunca e de '
          'compreensao: e de escrever o sinonimo em vez da palavra dita.',
          kind='dark')

    for s in C.SPEAKERS:
        slide(5, head('Speaker %d' % s['n'], 'Listen', 'Twice') +
              player('mp-l8-mm%d' % s['n'], AUDIO + s['file'],
                     'First pass: what is this person? Second pass: what is the argument?'),
              'Falante %d (2 min): toque duas vezes, sem texto. Na primeira, so a Task One. Na segunda, a '
              'Task Two. Nao deixe ele anotar as duas de uma vez -- a tarefa dupla e o que a prova mede.'
              % s['n'], kind='dark')

    t1 = {k: v for k, v in C.TASK1_OPTS}
    t2 = {k: v for k, v in C.TASK2_OPTS}
    tira = ''.join(player_mini('mp-l8-mmx%d' % sp['n'], AUDIO + sp['file'], 'Speaker %d' % sp['n'])
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
                 '1 C (&ldquo;I stopped <i>allowing</i> the flipchart&rdquo;) &middot; 2 F (&ldquo;I have '
                 'written eleven of them&rdquo;) &middot; 3 A (&ldquo;our chart&rdquo;, &ldquo;our '
                 'competitors&rdquo;) &middot; 4 D (&ldquo;I <i>sponsor</i> three of these a '
                 'year&rdquo;, &ldquo;I do not renew&rdquo;) &middot; 5 B (&ldquo;The <i>closing</i> is '
                 'the only part I rehearse&rdquo;).') +
          reveal('Task Two &mdash; key, and why the extra three are there',
                 '1 B &middot; 2 E &middot; 3 D &middot; 4 H &middot; 5 A. '
                 'The unused options (C, F, G) are all things these people might plausibly believe. None '
                 'of them is what any of them said. Speaker 4 is the trap: a sponsor sounds like somebody '
                 'who would say C, and it is the opposite of what he argues.'),
          'Correcao (5 min): a pista da Task One nunca e o assunto, e o PRONOME e o verbo -- faca ele '
          'apontar a palavra exata. Na Task Two, cobre a diferenca entre "o que ele diria" e "o que ele '
          'disse": as tres que sobram existem para pegar quem responde pelo perfil do falante.')

    # ── FASE 6 — The Inversion ────────────────────────────────────────────────
    divisor(6, 6, 'Landing on a Date,', 'or Running Across', 'Future perfect and future continuous, and which one a promise needs')

    def linhas(rs, base):
        return ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span><b>%s</b><br>'
            '<span style="font-size:.88rem;color:var(--text-mid)">%s</span><br>'
            '<span style="font-size:.9rem">%s</span></span></div>' % (base + i, a, b, c)
            for i, (a, b, c) in enumerate(rs))

    slide(6, head('The Forms', 'Two Futures,', 'One Choice') +
          '<div class="cpe-tight">%s</div>' % card(
              'Which one lands on a date, and which one runs across a period',
              linhas(C.GRAMMAR_ROWS[:4], 1)),
          'Formas 1 (3 min): nao explique a regra -- ele ja a tem. Pergunte, em cada linha, se a frase '
          'POUSA ou ATRAVESSA. Compromisso pousa; tranquilizacao atravessa.')

    slide(6, head('The Forms', 'Three', 'More') +
          card('And the two that look like commitments and are not',
               linhas(C.GRAMMAR_ROWS[4:], 5)),
          'Formas 2 (3 min): "we will be looking at" e "over the coming period" sao as duas frases que '
          'parecem compromisso e nao sao. Peca um exemplo do trabalho dele de cada uma, e o conserto.')

    for i, q in enumerate(C.GRAMMAR_QUIZ[:3], 1):
        slide(6, choices(q[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q[1])]),
              'Discriminacao %d (2 min): o erro util aqui e achar que as duas formas sao intercambiaveis. Se '
              'ele hesitar, pergunte: "could somebody hold you to that, and on what day?"' % i)

    slide(6, choices(C.GRAMMAR_QUIZ[3][0], [(k, t, ok) for k, (t, ok) in zip('abcd', C.GRAMMAR_QUIZ[3][1])]) +
          reveal('Why the answer is (b)',
                 'The continuous reassures: it says work is under way across a period. That is its job, '
                 'and it is the right form when you are telling a room that something continues. It is '
                 'the wrong form for a commitment, because nothing in it lands on a day anybody can hold '
                 'you to. A closing address needs both, and needs to know which is which.'),
          'Discriminacao 4 (3 min): este e o item que fecha o capitulo e o pacote. A resposta certa nao e '
          '"a continua e fraca": e que ela serve para OUTRA coisa. Peca a ele um exemplo de cada uso.')

    prod = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<span class="ic-blank">&nbsp;&nbsp;'
        '</span>%s</span></div>' % (i, it['before'], it['after'])
        for i, it in enumerate(C.GRAMMAR_PRODUCTION, 1))
    slide(6, head('Produce It', 'Put a Month', 'On It') +
          card('Say each one, then say the day or the period it lands on. If you cannot, the promise is not finished',
               prod + reveal('Reveal', '1 will have met &middot; 2 will be running &middot; 3 will have been '
                                       'circulated &middot; 4 will have been three years (the number is '
                                       'yours)')),
          'Producao (5 min): o item 4 e de proposito aberto -- o numero e dele. E o unico do conjunto em '
          'que ele tem de escolher o dado, e e ai que se ve se o tempo verbal ja e automatico.')

    # ── FASE 7 — Speaking & Wrap ──────────────────────────────────────────────
    divisor(7, 7, 'Your', 'Turn', 'The long turn, the follow-up, and two debates')

    slide(7, head('Role-play -- Guided', 'Two Minutes,', 'With Support') +
          roleplay(C.ROLEPLAY_SCENARIO, C.ROLEPLAY_CHIPS),
          C.ROLEPLAY_TEACHER)

    slide(7, head('Collaborative Task', 'Fourteen Down', 'to Three') + card('Four minutes, together',
          '<p style="font-size:.95rem;line-height:1.7">%s</p>' % C.COLLAB_TASK),
          'Collaborative (4 min): entre como PAR, nao como professor. Defenda dois itens que deveriam '
          'morrer. O que se mede e se ele corta em publico e poe NOME nos tres que ficam.')

    slide(7, head('Long Turn', 'Two Minutes,', 'Uninterrupted') +
          card('No notes. No apology at the start.',
               '<p style="font-size:.95rem;line-height:1.7">%s</p>' % C.LONG_TURN),
          'Long turn (3 min): NAO interrompa, nem para elogiar. E o ULTIMO long turn do pacote. Anote tres '
          'coisas: quantos compromissos tem mes, quantos tem dono, e a melhor frase dele. Compare com a '
          'gravacao do slide 4 e com a da aula 1, se voce ainda tiver.', kind='dark')

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
          'regra 3: compromisso sem tempo verbal que pouse numa data nao conta como compromisso.')

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
                   'I can make a commitment in a tense that somebody could hold me to.',
                   'I can close a year in public: what was promised, what was not, and what happens next.'])),
          'Autoavaliacao (2 min): e a ultima do pacote. Peca uma PROVA oral de cada item marcado, e o que '
          'ele nao marcar entra na conversa sobre o proximo ciclo.')

    slide(7, '<div class="chapter-label">Lesson Complete</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'Full Circle<br><span class="accent">Badge Earned</span></h1>'
             '<p class="subtitle">Eight lessons, and the only test that matters: what is different now</p>'
             '<p style="margin-top:1.2rem;font-size:.95rem;color:rgba(255,255,255,.8)">Homework: the '
             'closing note, 280 to 320 words. This is the last lesson of the programme.</p>',
          'Fechamento (3 min): e o fim do pacote. Devolva as tres anotacoes do long turn e depois faca a '
          'pergunta do proprio texto: daqui a duas semanas, o que ele vai estar fazendo diferente? Peca '
          'um mes e um nome. Termine pela melhor frase dele.', kind='image', bg=IMG[1])


if __name__ == '__main__':
    deck()
    # Nome proprio: o mklesson.py TAMBEM grava slides.html nesta pasta, a partir
    # do spec antigo. Se os dois usassem o mesmo nome, quem rodasse por ultimo venceria,
    # e o deck de prova sumiria sem erro nenhum.
    D.write(HERE, PHASES, 'slides_cpe.html')
