#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os slides IN CLASS da Aula 2 no formato de prova e grava slides.html.

Mesma fonte de conteudo da pre-class (lesson2_content.py): o artigo, as lacunas,
as multiplas escolhas, os cinco falantes e a gramatica sao OS MESMOS. E a REGRA 1
do sistema (pre-class PREPARA, in class ENTREGA, complementares REFORCAM: mesmo
vocabulario, mesma gramatica, mesmo tema) e tambem o que o professor pediu: ele
quer chegar na aula com a tarefa da prova ja na tela, nao com um resumo dela.

So usa blocos que o deck ja sabe renderizar e validar:
    ic-choices + icPickGist   escolha com acerto/erro na hora
    ic-match   + icPickMatch  pareamento clicavel, com placar
    ic-gaptext + ic-bank      lacuna com banco de palavras (conduzida pelo professor)
    comp-q     + revealComp   gabarito e justificativa escondidos
    lp/mp*     + mpToggle     player de audio do deck

USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/build_slides_cpe.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lesson2_content as C  # noqa: E402

A = 'guilherme-henrique-caneli'
AUDIO = '/audio/%s/' % A
IMG = {
    1: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1400&q=80',
    2: 'https://images.unsplash.com/photo-1560179707-f14e90ef3623?w=1400&q=80',
    3: 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1400&q=80',
    4: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1400&q=80',
    5: 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1400&q=80',
    6: 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1400&q=80',
}
PHASES = ['Lead-in', 'The Lexis', 'Reading: Parts 6 &amp; 5', 'Use of English',
          'Listening: Parts 2 &amp; 4', 'The Agent', 'Speaking &amp; Wrap']

_n = [0]
_slides = []


def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


def slide(phase, inner, teacher, kind='light', bg=None, extra=''):
    _n[0] += 1
    cls = {'light': 'slide slide-light', 'dark': 'slide slide-dark',
           'image': 'slide slide-image'}[kind]
    if _n[0] == 1:
        cls += ' active'
    style = ''
    if bg:
        style = (' style="background-image:linear-gradient(rgba(12,30,38,.80),rgba(12,30,38,.92)),'
                 "url('%s');background-size:cover;background-position:center\"" % bg)
    _slides.append(
        '<div class="%s" data-slide="%d" data-phase="%d" data-lesson="2"%s%s data-teacher="%s">\n'
        '  <div class="slide-inner">%s</div>\n</div>' % (cls, _n[0], phase, extra, style,
                                                         esc_attr(teacher), inner))


def head(label, title, accent=''):
    return ('<div class="chapter-label">%s</div>\n  <h2 class="slide-heading">%s '
            '<span class="accent">%s</span></h2>' % (label, title, accent))


def card(title, body):
    return '<div class="ic-card"><div class="ic-card-h3">%s</div>%s</div>' % (title, body)


def choices(question, opts, kind='gist', cls=''):
    """opts: (letra, texto, certa?) -- valida no clique, sem dizer qual antes.

    cls='cpe-long' aperta a lista para as sete frases da Part 6, que sao longas:
    no tamanho padrao, sete frases INTEIRAS cortam a ultima num projetor de
    1280x800 -- e frase cortada foi exatamente a reclamacao do professor.

    O modificador vai num ATRIBUTO do cartao, nunca numa classe a mais no
    .ic-choices: os gates (validate_lesson 751/1530, build_from_model 1180)
    procuram a string class="ic-choices" ao pe da letra, e uma segunda classe ali
    faz o slide deixar de ser visto como checagem -- sem erro, so um aviso novo.
    """
    rows = ''.join(
        '<div class="ic-choice" data-right="%s" onclick="icPickGist(this)">'
        '<span class="ic-opt">%s</span><span>%s</span>'
        '<span class="ic-badge">&#10003;</span></div>' % ('true' if ok else 'false', k, t)
        for k, t, ok in opts)
    return ('<div data-kind="%s" class="ic-card"%s><div class="ic-card-h3">%s</div>'
            '<div class="ic-choices">%s</div></div>'
            % (kind, ' data-dense="1"' if cls else '', question, rows))


def matching(title, hint, pairs, opts=None):
    """pairs: (n, esquerda, letra, direita) -- gabarito no data-match da esquerda.

    opts: a lista (letra, texto) COMPLETA, quando a tarefa tem distratores. Sem
    ela a coluna da direita desenha so as opcoes usadas -- que e o defeito que a
    Part 4 deste deck tinha: dizia "three of the eight are not used" e mostrava
    cinco. Os tres distratores existem no conteudo e estao na pre-class; eram os
    unicos que nunca chegavam a tela projetada.
    """
    words = ''.join(
        '<div class="ic-chip ic-word" role="button" tabindex="0" data-k="%s" data-match="%s" '
        'onclick="icPickMatch(this)"><span class="ic-k">%s</span><span>%s</span>'
        '<span class="ic-pair"></span></div>' % (n, k, n, left) for n, left, k, _r in pairs)
    lista = opts if opts is not None else [(k, r) for _n, _l, k, r in pairs]
    defs = ''.join(
        '<div class="ic-chip ic-def" role="button" tabindex="0" data-k="%s" '
        'onclick="icPickMatch(this)"><span class="ic-k">%s</span><span>%s</span>'
        '<span class="ic-pair"></span></div>' % (k, k, right) for k, right in lista)
    return ('<div data-kind="matching" class="ic-card"><div class="ic-card-h3">%s</div>'
            '<p class="ic-match-hint">%s</p><div class="ic-match-score">0 / %d matched</div>'
            '<div class="ic-match" data-interactive="1">'
            '<div class="ic-match-col"><h4>%s</h4>%s</div>'
            '<div class="ic-match-col"><h4>Meanings</h4>%s</div></div></div>'
            % (title, hint, len(pairs), 'Speakers' if 'Speaker' in pairs[0][1] else 'Words &amp; expressions',
               words, defs))


ICONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">'
         '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>')


def vocab_grid(gid, cid, itens):
    """Reveal de vocabulario do shell (.vocab-card + revealVocab).

    Aqui ele nao e reconhecimento: a FRENTE do card e a definicao e a palavra e o
    que esta escondido. O aluno PRODUZ o termo e so entao revela para conferir --
    que e o uso util de um reveal para quem ja tem o vocabulario passivo.
    """
    cards = ''.join(
        '<div class="vocab-card" onclick="revealVocab(this)">'
        '<div class="card-icon" style="background:linear-gradient(135deg,#1e3a5f,#2f6690)">%s'
        '<div class="card-hint">%s</div></div>'
        '<div class="card-body"><div class="card-word">%s</div><div class="card-def">%s</div>'
        '<div class="card-example">&ldquo;%s&rdquo;</div><div class="card-audio">'
        '<button class="audio-btn-sm" data-speak="%s" '
        'onclick="event.stopPropagation();speakText(this.dataset.speak,this)">Listen</button>'
        '</div></div></div>' % (ICONE, d, w, d, ex, w) for w, d, ex in itens)
    return ('<p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
            '<span id="%s">0 / %d words revealed</span></p>'
            '<div class="vocab-grid" id="%s">%s</div>' % (cid, len(itens), gid, cards))


def roleplay(cenario, chips):
    chips_html = ''.join(
        '<span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;'
        'padding:.3rem .7rem;font-size:.8rem">%s</span>' % c for c in chips)
    return ('<div class="roleplay-body" style="max-width:620px;margin:1rem auto 0;'
            'background:linear-gradient(135deg,var(--accent-dim),rgba(30,77,92,.05));'
            'border:1px solid var(--accent);border-radius:12px;padding:1.5rem">'
            '<p class="roleplay-scenario" style="font-size:.95rem;margin-bottom:1rem">'
            '<strong>Scenario:</strong> %s</p>'
            '<p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keyword chips:</p>'
            '<div style="display:flex;flex-wrap:wrap;gap:.4rem">%s</div></div>' % (cenario, chips_html))


def checklist(itens):
    return ''.join(
        '<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<polyline points="20 6 9 17 4 12"/></svg></div>%s</div>' % t for t in itens)


def reveal(label, content):
    """Painel FORA do botao: o GATE 28 clica de verdade e descarta, de proposito,
    toda mudanca dentro do elemento clicado. Com o gabarito como filho, um reveal
    que funciona fica indistinguivel de um morto."""
    return ('<div class="cpe-reveal">'
            '<div class="comp-q" onclick="revealComp(this)"><div class="q-text">%s</div></div>'
            '<div class="cpe-key">%s</div></div>' % (label, content))


def player(pid, src, caption=''):
    cap = ('<div style="font-size:.8rem;color:var(--text-dim);margin-bottom:.4rem">%s</div>'
           % caption) if caption else ''
    return (cap + '<div class="mock-player lp" id="%s" data-src="%s" '
            'style="max-width:460px;margin:.8rem auto">'
            '<div class="lp-seekbar" onclick="mpSeek(event,\'%s\')">'
            '<div class="lp-progress" id="progress-%s"></div></div>'
            '<div class="lp-times"><span id="time-current-%s">0:00</span>'
            '<span id="time-total-%s">0:00</span></div><div class="lp-row">'
            '<button class="lp-btn" onclick="mpSkip(\'%s\',-5)" aria-label="Back 5 seconds">-5s</button>'
            '<button class="lp-btn lp-play" id="play-%s" onclick="mpToggle(\'%s\')" aria-label="Play or pause">'
            '<svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18">'
            '<polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
            '<svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none">'
            '<rect x="6" y="4" width="4" height="16" fill="currentColor"/>'
            '<rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>'
            '<button class="lp-btn" onclick="mpSkip(\'%s\',5)" aria-label="Forward 5 seconds">+5s</button></div>'
            '<div class="lp-speeds">'
            '<button class="lp-speed-btn" onclick="mpSpeed(\'%s\',0.85,this)">0.85x</button>'
            '<button class="lp-speed-btn lp-speed-active" onclick="mpSpeed(\'%s\',1,this)">1x</button>'
            '<button class="lp-speed-btn" onclick="mpSpeed(\'%s\',1.15,this)">1.15x</button></div></div>'
            % (pid, src, pid, pid, pid, pid, pid, pid, pid, pid, pid, pid, pid))


def player_mini(pid, src, rotulo):
    """Botao de play e so isso, para os cinco falantes caberem numa tira unica.

    Usa o MESMO mpToggle do player grande: ele so precisa do elemento com
    data-src e do botao play-<id> com os dois icones. O id e proprio
    (mp-l2-mmx<n>) porque os falantes ja tem player nos slides individuais, e id
    repetido faria mpIcon pintar sempre o primeiro do documento.
    """
    return ('<div class="cpe-mini lp" id="%s" data-src="%s">'
            '<button class="lp-btn lp-play cpe-mini-btn" id="play-%s" onclick="mpToggle(\'%s\')" '
            'aria-label="Play or pause %s">'
            '<svg class="lp-icon-play" viewBox="0 0 24 24" width="15" height="15">'
            '<polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
            '<svg class="lp-icon-pause" viewBox="0 0 24 24" width="15" height="15" style="display:none">'
            '<rect x="6" y="4" width="4" height="16" fill="currentColor"/>'
            '<rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>'
            '<span class="cpe-mini-lbl">%s</span></div>' % (pid, src, pid, pid, rotulo, rotulo))


# ══════════════════════════════════════════════════════════════════════════════
# O DECK
# ══════════════════════════════════════════════════════════════════════════════

def deck():
    # ── FASE 1 — Lead-in ──────────────────────────────────────────────────────
    slide(1, '<div class="passport-badge">Lesson 2</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3.4rem;line-height:1.05;'
             'margin:.6rem 0">The Language of<br><span class="accent">Capital</span></h1>\n'
             '  <p class="subtitle">Who is paid first, who waits, and which sentence is hiding the '
             'person who made it happen</p>',
          'Abertura (2 min): diga a moldura da aula em uma frase -- "today every task is an exam task, '
          'and the text is one you would actually read". Nao explique o formato ainda; o slide seguinte faz isso.',
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
            ('The Agent', '7 min', 'Causative and passive: who is named, who is hidden, and why.'),
            ('Speaking', '9 min', 'Long turn and follow-up, then two debates, and in the second one you do not choose your side.'),
        ])
    slide(1, head('The Shape of Today', 'Every Task Is an', 'Exam Task') +
          card('Cambridge C2 Proficiency format, on your material', plan),
          'Plano (1 min): mostre que o formato mudou e por que -- ele pediu tarefa de prova, com '
          'critical thinking, e o material agora entrega isso. Nao peca desculpa pelo material antigo; '
          'apresente o novo.')

    slide(1, head('Lead-in', 'Books', 'Closed') +
          card('Answer in full sentences, before any vocabulary appears',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, q)
                   for i, q in enumerate([
                       'A fund manager calls your project "attractive but unbankable". What, precisely, has she said no to?',
                       'Your government guarantees a project\'s revenue. Whose risk has disappeared, and whose has merely moved?',
                       'A briefing note says you "were advised" to revise the tariff. Who advised you, and why does the sentence not say?'], 1))),
          'Lead-in (5 min): ele responde os tres em voz alta. NAO corrija lingua aqui -- anote duas '
          'imprecisoes de LEXICO para cobrar na fase 2. A terceira pergunta e a semente da gramatica '
          'da aula: guarde a resposta dele e volte a ela no slide do agente.')

    slide(1, head('Diagnostic', 'Ninety Seconds,', 'No Notes') +
          '<div class="ic-scenario"><div class="ic-who">A sovereign wealth fund manager, at your table</div>'
          '<p>"Your region has the projects and we have the money. So tell me honestly: why are we '
          'still not invested?"</p></div>'
          '<p style="margin-top:.9rem;font-size:.95rem;color:var(--text-mid)">Answer in ninety seconds. '
          'Then say which word you reached for and did not find.</p>',
          'Diagnostico (4 min): cronometre de verdade. O que interessa nao e o conteudo, e onde a '
          'fluencia dele TRAVA. Anote a palavra que faltou: ela provavelmente esta na lista de hoje, '
          'e voce vai devolve-la a ele no fim da aula.')

    # ── FASE 2 — The Lexis ────────────────────────────────────────────────────
    slide(2, '<div class="chapter-label">Chapter 2</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'The Lexis of the<br><span class="accent">Capital Stack</span></h1>'
             '<p class="subtitle">Fourteen terms, and the distinctions between the four that look alike</p>',
          'Divisor (10 seg): passe rapido.', kind='image', bg=IMG[2])

    slide(2, head('Collocation', 'Words That Travel', 'Together') +
          card('Read each one aloud. Then build a sentence with two of them.',
               '<div class="ic-bank ic-soft">%s</div>' % ''.join(
                   '<span class="ic-b">%s</span>' % c.replace('<b>', '').replace('</b>', '')
                   for c in C.COLLOC_BANK)),
          'Colocacao (3 min): elicite, nao ensine. Peca uma frase contrastando brownfield e greenfield '
          'usando "patient capital" e "construction risk". Se sair sem esforco, suba: exija "crowd in" '
          'e "bankability" na mesma frase.')

    slide(2, head('Produce It', 'The Definition Is the', 'Front of the Card') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vocabGrid1', 'vocabCount1', C.VOCAB[:5]),
          'Reveal 1-5 (4 min): a definicao esta na frente e a PALAVRA e o que esta escondido. Ele '
          'produz o termo em voz alta antes de revelar. Para quem ja tem o vocabulario passivo, o '
          'reveal so vale nesse sentido. CCQ de risk-adjusted return: "is fifteen percent always '
          'better than nine?".')

    slide(2, head('Produce It', 'Five', 'More') +
          '<div class="cpe-tight">%s</div>' % vocab_grid('vocabGrid2', 'vocabCount2', C.VOCAB[5:10]),
          'Reveal 6-10 (4 min): mesma rotina. As duas que costumam sair trocadas sao credit '
          'enhancement e de-risking mechanism: pergunte qual delas mexe no RATING.')

    pares = [(str(i + 1), w, 'abcdefgh'[i], m) for i, (w, m) in enumerate(C.MATCH_ROWS)]
    slide(2, head('Precision', 'Which One Is It,', 'Exactly') +
          '<div class="cpe-tight">%s</div>' % matching(
              'Match each term to the distinction it makes',
              'Tap a term, then tap its meaning. These are distinctions, not dictionary definitions.',
              pares),
          'Matching (5 min): ele fecha o par EM VOZ ALTA antes de clicar. As duplas que pegam sao '
          'credit enhancement x de-risking mechanism e concessional lending x blended finance. Se ele '
          'errar, nao de a resposta: peca a diferenca entre as duas opcoes que ele considerou.')

    # As oito frases do cloze, com a lacuna marcada. O banco fica a vista: na aula a
    # tarefa nao e lembrar a palavra, e justificar por que so uma serve.
    # DUAS telas, nao uma. Oito lacunas com o banco e o gabarito na mesma tela
    # cortavam 35px a 1280x800 mesmo com .cpe-tight, e apertar mais deixaria a
    # letra ilegivel num projetor. Quatro e quatro cabem, e a divisao ainda
    # ajuda: o professor cobra a justificativa de duas lacunas por vez.
    def cloze_bloco(itens, base):
        return ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s'
            '<span class="ic-blank">&nbsp;&nbsp;</span>%s</span></div>'
            % (base + i, re.sub(r'^\d+\.\s*', '', it['before']), it['after'])
            for i, it in enumerate(itens))

    banco = '<div class="ic-bank ic-soft">%s</div>' % ''.join(
        '<span class="ic-b">%s</span>' % b for b in C.CLOZE_BANK)

    slide(2, head('In Context', 'Put the Lexis to', 'Work') +
          '<div class="cpe-tight">%s</div>' % card(
              'One expression in the bank is not needed. Gaps 1 to 4.',
              '<div class="ic-lf-list">%s</div>%s' % (cloze_bloco(C.CLOZE_ITEMS[:4], 1), banco)),
          'Cloze 1 (2 min): ele ja digitou isto em casa. Aqui a tarefa e OUTRA: peca a JUSTIFICATIVA da '
          'lacuna 4 -- por que nao pode ser blended finance. O banco fica a vista de proposito.')

    slide(2, head('In Context', 'Gaps Five to', 'Eight') +
          '<div class="cpe-tight">%s</div>' % card(
              'Same bank. One expression is still not needed.',
              '<div class="ic-lf-list">%s</div>%s' % (cloze_bloco(C.CLOZE_ITEMS[4:], 5), banco) +
              reveal('Reveal the key',
                     '1 fiduciary duty &middot; 2 an off-take agreement &middot; 3 a currency hedge '
                     '&middot; 4 concessional lending &middot; 5 blended finance &middot; 6 credit '
                     'enhancement &middot; 7 an anchor investor &middot; 8 yield compression. '
                     '<b>Not needed:</b> %s.' % C.CLOZE_NOT_NEEDED)),
          'Cloze 2 (2 min): peca a justificativa da lacuna 6 -- por que nao pode ser de-risking '
          'mechanism. E peca que ele diga qual sobrou e POR QUE sobrou: e a unica pergunta do slide que '
          'nao tem resposta no banco.')

    slide(2, choices('Which of these would a native speaker in this sector <b>not</b> say?', [
        ('a', 'The tranche ranks behind the senior loan.', False),
        ('b', 'The guarantee crowded in four dollars of private money.', False),
        ('c', 'We compressed the yields deliberately to attract funds.', True),
        ('d', 'The revenue was ring-fenced at financial close.', False)]) +
        reveal('Why (c)', 'Yield compression is something that <i>happens to</i> a market, not something a '
                          'party does on purpose. The collocation exists; the agency does not. This is the '
                          'kind of error that survives fluency.'),
        'Registro (3 min): esta e a pergunta que separa quem sabe a palavra de quem sabe o uso. Se ele '
        'acertar de primeira, peca para reescrever (c) de um jeito que funcione.')

    # ── FASE 3 — Reading (Paper 1, Parts 6 e 5) ───────────────────────────────
    slide(3, '<div class="chapter-label">Chapter 3</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'Who Gets<br><span class="accent">Paid First</span></h1>'
             '<p class="subtitle">Paper 1, Part 6: six sentences removed, seven on offer, one of them useless</p>',
          'Divisor (10 seg).', kind='image', bg=IMG[3])

    slide(3, head('Before You Read', 'One Line, One', 'Prediction') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;Ask an engineer what an '
          'infrastructure project is and you will hear about geology, spans and traffic forecasts.&rdquo;</div>'
          '<div class="ic-predict-q">This is the first line. What is the second half of that sentence '
          'going to do?</div></div>',
          'Predicao (2 min): aceite QUALQUER palpite, nao confirme nem corrija. A predicao serve para '
          'ativar o que ele ja sabe. O que importa e ele perceber, depois, que a frase vira um contraste.',
          kind='dark', extra=' data-task-for="reading"')

    def artigo(paras, gaps):
        out = []
        for before, n, after in paras:
            if n:
                out.append('<p>%s<span class="ic-blank">&nbsp;<span class="ic-n">%d</span></span>%s</p>'
                           % (before, n, after))
            else:
                out.append('<p>%s</p>' % before)
        return ('<div class="ic-reading"><div class="ic-rtitle">%s</div>%s'
                '<div class="ic-src">%s &middot; gaps %s</div></div>'
                % (C.ARTICLE_TITLE, ''.join(out), C.ARTICLE_STANDFIRST, gaps))

    # ── A TELA DAS SETE FRASES ────────────────────────────────────────────────
    # Pedido do professor Andre, 21/09/2026: "tira uma foto dessas frases e nos
    # vamos lendo o texto incluindo; eu posso ir passando as paginas". O texto
    # continua paginado (ele disse que isso ele manobra); o que NAO pode ficar
    # espalhado sao as opcoes. Entao elas ganham uma tela so delas, inteiras,
    # ANTES do texto -- e e essa a tela que ele fotografa.
    #
    # Sem .comp-q e sem ic-choices de proposito: e uma tela de referencia, nao de
    # checagem. Com qualquer um dos dois ela seria lida como checagem do slide
    # anterior e a REGRA 2.2 passaria a cobrar um slide de tarefa antes dela.
    frases = ''.join(
        '<div class="cpe-sent"><span class="cpe-sent-k">%s</span><span>%s</span></div>' % (k, v)
        for k, v in C.GAP_OPTIONS)
    slide(3, head('Paper 1, Part 6', 'The Seven', 'Sentences') +
          '<div class="ic-card cpe-sent-card"><div class="ic-card-h3">Six gaps, seven sentences. '
          'One of them fits nowhere.</div><div class="cpe-sents">%s</div>'
          '<p class="cpe-sent-foot">Keep these in front of you while you read. Decide each gap by '
          'what the text points back to, not by what sounds true.</p></div>' % frases,
          'ESTA e a tela da foto (1 min). Antes de comecar a leitura, peca que ele fotografe a tela: '
          'as sete frases ficam com ele enquanto o texto passa pagina a pagina. Nao discuta nenhuma '
          'delas aqui -- so leia em voz alta a letra de cada uma e siga.')

    # O texto vai em QUATRO telas, nao em duas: medido no Chrome a 1400x900, dois
    # blocos de tres paragrafos cortavam a ultima linha -- e a ultima linha do
    # artigo ("It is a negotiating position") e a ponte para a gramatica da aula.
    slide(3, head('The Text', 'Paragraphs One and', 'Two') + artigo(C.ARTICLE[:2], '1 and 2'),
          'Leitura (3 min): ele le EM SILENCIO, paragrafo a paragrafo, e diz em uma frase o que cada '
          'um faz no argumento. Nao deixe partir para as opcoes antes disso: a coesao so aparece para '
          'quem ja entendeu a linha do texto.')

    slide(3, head('The Text', 'Paragraphs Three and', 'Four') + artigo(C.ARTICLE[2:4], '3 and 4'),
          'Leitura (3 min): mesma rotina. Peca a ligacao entre os dois paragrafos antes de virar: o '
          'terceiro explica um comportamento, o quarto mostra o preco dele.')

    slide(3, head('The Text', 'Paragraphs Five and', 'Six') + artigo(C.ARTICLE[4:6], '5 and 6'),
          'Leitura (3 min): aqui entram os instrumentos. Se ele ja souber tudo isso do trabalho, otimo: '
          'a tarefa nao e entender o conteudo, e achar a frase que falta.')

    # Slide de TAREFA antes da ultima tela de texto (REGRA 2.2, bloqueante). Ele tem
    # de trazer TRES coisas, e o gate cobra as tres:
    #   data-task-for="reading"  a marca de que e o slide de tarefa
    #   .ic-predict              o aluno arrisca antes de ser exposto
    #   a MESMA pergunta         que o slide de checagem seguinte vai cobrar,
    #                            em <div class="q-text">, e SEM a resposta
    # Fica de proposito sem .comp-q e sem ic-choices: com qualquer um dos dois ele
    # seria lido como slide de CHECAGEM do texto anterior, e a regra passaria a
    # cobrar uma tarefa antes daquele tambem, em cascata.
    slide(3, head('Before the Last Paragraph', 'Predict, Then', 'Place') +
          '<div class="ic-predict"><div class="ic-predict-line">&ldquo;All of which the language of '
          'the sector is beautifully designed to obscure.&rdquo;</div>'
          '<div class="ic-predict-q">That is how the last paragraph opens, and it is the only one with '
          'no gap in it. Does the writer end by summarising, by conceding, or by accusing?</div></div>'
          '<div class="ic-card" style="margin-top:1rem"><div class="ic-card-h3">Then the task you have '
          'been reading for</div>'
          '<div class="comp-q comp-q-task"><div class="q-text">Gap 1 -- which sentence belongs here?'
          '</div></div>'
          '<p style="font-size:.92rem;color:var(--text-mid);margin:.6rem 0 0">Six gaps, seven sentences, '
          'one of them useless. Decide each one by what the text points back to, not by what sounds '
          'true.</p></div>',
          'Tarefa (2 min): ele responde a predicao PRIMEIRO, em uma palavra -- summarise, concede ou '
          'accuse. Depois diz de qual lacuna menos tem certeza. Anote: quase sempre e a 6, e a ultima '
          'frase do artigo e o que resolve.',
          extra=' data-task-for="reading"')

    slide(3, head('The Text', 'The Last', 'Paragraph') + artigo(C.ARTICLE[6:], 'no gap') +
          '<p style="margin-top:.9rem;font-size:.95rem;color:var(--text-mid)">No gap here. Read it '
          'twice.</p>',
          'Fecho da leitura (2 min): sem lacuna de proposito. Peca que ele leia a ultima frase em voz '
          'alta e diga o que ela acusa. E dela que sai o capitulo da gramatica.')

    letras = {k: v for k, v in C.GAP_OPTIONS}

    # As sete frases vao INTEIRAS. Antes eram cortadas em 102 caracteres com
    # reticencias, e uma frase cortada nao e uma opcao: metade delas so se decide
    # pelo fim ("...a promise made in 1994", "...the same committees that
    # hesitated"). O professor pediu justamente isso -- as frases completas, e
    # todas na mesma imagem.
    for gap_n, right in C.GAP_ANSWERS:
        opts = [(k, letras[k], k == right) for k, _v in C.GAP_OPTIONS]
        slide(3, choices('Gap %s -- which sentence belongs here?' % gap_n, opts, cls='cpe-long'),
              'Gap %s (2 min): a resposta e %s. Exija a PROVA antes do clique: qual palavra da frase '
              'seguinte aponta para tras. Se ele acertar por eliminacao, pergunte por que cada '
              'descartada foi descartada.' % (gap_n, right))

    slide(3, choices('One sentence fits <b>no</b> gap at all. Which one, and what is wrong with it?', [
        ('A', letras['A'], False), ('B', letras['B'], False),
        ('D', letras['D'], True), ('G', letras['G'], False)], cls='cpe-long') +
        reveal('Why D is the distractor',
               'D is true, on topic, and would sit comfortably in a conversation about this article. '
               'What it never does is answer a reference or complete an argument. That is the whole '
               'test: a gapped text is not asking what is true, it is asking what is <i>cohesive</i>.'),
        'O distrator (3 min): este e o slide que mais ensina. Faca ele TENTAR encaixar D em cada lacuna '
        'e dizer, em cada uma, o que quebra. Se ele nao consegue verbalizar, mostre a lacuna 3: D fala '
        'de sovereign funds, mas o "Its obligation" seguinte precisa do pension fund.')

    q3 = C.MCQ[2]
    slide(3, choices(q3[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q3[1])]) +
          reveal('The trap in (a)',
                 '(a) is <b>true</b>. It is a fact stated in that very sentence. It is still the wrong '
                 'answer, because the question asks what the sentence is <i>for</i>, not what it '
                 'contains. In Part 5, at least one option in every item is true and irrelevant.'),
          'Discriminador 1 (4 min): se ele escolher (a), NAO diga que errou. Pergunte: "is that what '
          'the sentence says, or what the sentence is doing?". Esta distincao e a diferenca entre C1 e '
          'C2 em leitura, e e exatamente o que ele pediu quando falou de reading between the lines.')

    q6 = C.MCQ[5]
    slide(3, choices(q6[0], [(k, t, ok) for k, (t, ok) in zip('abcd', q6[1])]) +
          reveal('Why this matters today',
                 'The writer calls the passive "a negotiating position". That is the bridge into the '
                 'grammar of this lesson: the same structure can report a fact, or withhold a name. '
                 'Which one it is doing is a choice the writer made.'),
          'Discriminador 2 (3 min): termine a leitura AQUI e deixe a frase no ar. O proximo capitulo '
          'devolve isso como gramatica. Se ele disser que o passivo e so formalidade, guarde a frase '
          'dele e confronte no slide do term sheet.')

    # ── FASE 4 — Use of English ───────────────────────────────────────────────
    slide(4, '<div class="chapter-label">Chapter 4</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'Use of<br><span class="accent">English</span></h1>'
             '<p class="subtitle">Paper 1, Parts 3 and 4: the word family, and the same meaning in other words</p>',
          'Divisor (10 seg).', kind='image', bg=IMG[4])

    wf_rows = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<span class="ic-blank">&nbsp;&nbsp;'
        '</span>%s</span></div>' % (i, it['before'], it['after'])
        for i, it in enumerate(C.WORD_FORMATION[:5], 1))
    slide(4, head('Part 3', 'Word', 'Formation') +
          card('Say the word before you write it', wf_rows +
               reveal('Reveal 1 to 5', '1 unreliable &middot; 2 uninvestable &middot; 3 independent &middot; '
                                       '4 Paradoxically &middot; 5 understatement')),
          'Word formation (4 min): ele fez em casa. Na aula, cobre a FAMILIA: de "rely", quantas '
          'palavras ele produz em dez segundos (reliable, unreliable, reliability, reliance, reliant)? '
          'Item 2 e o que pega: "uninvestable" existe e e usado, mas ele tende a produzir "non-investable".')

    tr_rows = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<br>'
        '<span class="ic-rephrase-cue">%s</span> %s<span class="ic-blank">&nbsp;&nbsp;</span>%s</span></div>'
        % (i, t['lead'], t['key'], t['before'], t['after'])
        for i, t in enumerate(C.TRANSFORMATIONS[:3], 1))
    slide(4, head('Part 4', 'Key-word', 'Transformations') +
          card('Three to eight words. The key word does not change.', tr_rows +
               reveal('Reveal 1 to 3', '1 had our financial model audited &middot; '
                                       '2 got the ministry to approve &middot; '
                                       '3 are having a development bank provide')),
          'Transformacao (4 min): ele DIZ a resposta antes de ver. Conte as palavras em voz alta com '
          'ele -- passar de oito e o erro mais comum de quem e fluente, porque a parafrase natural dele '
          'e mais longa que a exigida.')

    tr_rows2 = ''.join(
        '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s<br>'
        '<span class="ic-rephrase-cue">%s</span> %s<span class="ic-blank">&nbsp;&nbsp;</span>%s</span></div>'
        % (i, t['lead'], t['key'], t['before'], t['after'])
        for i, t in enumerate(C.TRANSFORMATIONS[3:], 4))
    slide(4, head('Part 4', 'Three', 'More') +
          card('The last one is an idiom, not a structure', tr_rows2 +
               reveal('Reveal 4 to 6', '4 took the decision to &middot; 5 provided the currency risk is '
                                       '&middot; 6 came as no surprise to anyone')),
          'Transformacao (4 min): o item 6 e o unico idiomatico. Se ele produzir "was not a surprise '
          'for anyone", aceite o sentido e cobre a forma fixa: it came as no surprise TO.')

    slide(4, head('Real Document', 'The Term Sheet on', 'Your Desk') +
          '<div class="ic-reading"><div class="ic-rtitle">Term sheet summary &middot; Northeast Solar '
          'Cluster</div>'
          '<p><b>Equity offered:</b> 25% stake to one anchor investor. <b>Leverage:</b> 70% debt / 30% '
          'equity. <b>Debt:</b> senior loan (development bank) plus a subordinated tranche. '
          '<b>Revenue:</b> secured by a twenty-year off-take agreement. <b>Currency:</b> hedged to 2035. '
          '<b>Status:</b> approvals were obtained in March; the model was reviewed and the structure '
          'amended; the tariff was subsequently revised.</p></div>' +
          reveal('The three sentences that name nobody',
                 '<i>approvals were obtained</i> &middot; <i>the model was reviewed</i> &middot; '
                 '<i>the tariff was revised</i>. Three actions, three missing agents. Ask who, in each '
                 'case, and what they were given in exchange. That question is the lesson.'),
          'Caca ao agente (5 min): ele le o term sheet em voz alta e PARA em cada passivo sem agente. '
          'Tres perguntas por frase: quem fez, por que o documento nao diz, e o que voce perguntaria '
          'numa call. Este slide amarra leitura, lexico e gramatica num documento que ele recebe de verdade.')

    # ── FASE 5 — Listening (Paper 3, Parts 2 e 4) ─────────────────────────────
    slide(5, '<div class="chapter-label">Chapter 5</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'Five Voices,<br><span class="accent">Two Tasks</span></h1>'
             '<p class="subtitle">Paper 3, Part 4: what each speaker is, and what each one is arguing</p>',
          'Divisor (10 seg).', kind='image', bg=IMG[5])

    slide(5, head('Part 2 -- Checked', 'The Talk You Heard at', 'Home') +
          player('mp-l2-talk', AUDIO + C.TALK_FILE,
                 'Three minutes. He completed the eight sentences before the lesson.') +
          reveal('The eight answers',
                 '1 the queue &middot; 2 probability of default &middot; 3 subordinated debt &middot; '
                 '4 obligation &middot; 5 yield compression &middot; 6 construction risk &middot; '
                 '7 revenue &middot; 8 the first'),
          'Checagem (4 min): NAO toque o audio inteiro de novo. Toque so os trechos dos itens que ele '
          'errou, e pergunte o que ele ouviu em vez do que estava la. Em Part 2 o erro quase nunca e de '
          'compreensao: e de escrever o sinonimo em vez da palavra dita.',
          kind='dark')

    for s in C.SPEAKERS[:3]:
        slide(5, head('Speaker %d' % s['n'], 'Listen', 'Twice') +
              player('mp-l2-mm%d' % s['n'], AUDIO + s['file'],
                     'First pass: what is this person? Second pass: what is the argument?'),
              'Falante %d (2 min): toque duas vezes, sem texto. Na primeira, so a Task One. Na segunda, '
              'a Task Two. Nao deixe ele anotar as duas de uma vez -- a tarefa dupla e justamente o que '
              'a prova mede.' % s['n'], kind='dark')

    for s in C.SPEAKERS[3:]:
        slide(5, head('Speaker %d' % s['n'], 'Listen', 'Twice') +
              player('mp-l2-mm%d' % s['n'], AUDIO + s['file'],
                     'First pass: what is this person? Second pass: what is the argument?'),
              'Falante %d (2 min): mesma rotina. O falante 4 e o mais dificil de identificar pela funcao '
              'e o mais facil pelo argumento; o 5 e o contrario.' % s['n'], kind='dark')

    # ── A PAGINA DE PROVA DA PART 4 ───────────────────────────────────────────
    # Pedido do professor Andre, 21/09/2026: "e um audio e duas atividades ao
    # mesmo tempo; o aluno tem que ver TODAS as opcoes e escolher -- Speaker One
    # falou daquela categoria e B daquela outra. Se fica tudo espalhado (...)
    # essa parte das opcoes tem que estar tudo junto."
    #
    # Eram duas telas, uma por tarefa, e cada uma mostrava so as cinco opcoes
    # usadas. Agora e UMA tela: as oito da Task One, as oito da Task Two, os
    # cinco falantes com as duas respostas e os cinco audios na mesma tira. E a
    # imagem que ele fotografa, e e tambem como a pagina cai na prova de verdade.
    t1 = {k: v for k, v in C.TASK1_OPTS}
    t2 = {k: v for k, v in C.TASK2_OPTS}
    tira = ''.join(player_mini('mp-l2-mmx%d' % sp['n'], AUDIO + sp['file'], 'Speaker %d' % sp['n'])
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
          '<i>is</i>. <b>Task Two:</b> the main point each one <i>makes</i>. Three letters in each '
          'list are not used.</p>'
          '<div class="cpe-mini-row">%s</div><div class="cpe-two">%s%s</div>' % (tira, caixa1, caixa2),
          'A pagina inteira (8 min): toque os cinco seguidos, sem parar, com as duas listas na tela. '
          'Na primeira passada ele fecha a Task One; na segunda, a Task Two. Nao separe as tarefas em '
          'duas telas de novo -- fazer as duas ao mesmo tempo E o que a Part 4 mede.')

    slide(5, head('Part 4', 'What Gave Each One', 'Away') +
          reveal('Task One &mdash; key, and the word that decides it',
                 '1 B (&ldquo;every asset we are <i>permitted</i> to buy&rdquo; = a mandate) &middot; '
                 '2 D (&ldquo;when <i>we</i> take the first five years&rdquo;) &middot; '
                 '3 C (&ldquo;the risk <i>we</i> are paid to hold&rdquo;) &middot; '
                 '4 A (&ldquo;presents as a safer <i>credit</i>&rdquo;) &middot; '
                 '5 F (&ldquo;<i>we</i> reopened one concession&rdquo;).') +
          reveal('Task Two &mdash; key, and why the extra three are there',
                 '1 E &middot; 2 A &middot; 3 D &middot; 4 B &middot; 5 C. '
                 'The unused options (F, G, H) are all things these people might plausibly believe. '
                 'None of them is what any of them said.'),
          'Correcao (5 min): a pista da Task One nunca e o assunto, e o PRONOME e o verbo -- faca ele '
          'apontar a palavra exata. Na Task Two, cobre a diferenca entre "o que ele diria" e "o que ele '
          'disse": as tres opcoes que sobram existem para pegar quem responde pelo perfil do falante.')

    # ── FASE 6 — The Agent ────────────────────────────────────────────────────
    slide(6, '<div class="chapter-label">Chapter 6</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'Who Made It<br><span class="accent">Happen</span></h1>'
             '<p class="subtitle">Four ways to name the party who acted, and two ways to lose them</p>',
          'Divisor (10 seg).', kind='image', bg=IMG[6])

    # Sete formas num slide so estouram a tela projetada (medido: a linha 6 corta e a
    # 7 nao aparece). Duas telas, e a divisao e a propria licao: causativo primeiro,
    # passivo depois.
    def linhas(rs, base):
        return '<div class="ic-lf-list">%s</div>' % ''.join(
            '<div class="ic-lf"><span class="ic-lbl">%d</span><span><b>%s</b> -- %s<br>'
            '<span style="color:var(--text-mid)">%s</span></span></div>' % (i, f, w, ex)
            for i, (f, w, ex) in enumerate(rs, base))

    slide(6, head('The Analysis', 'The Causative', 'Family') +
          card('Four shapes. Three of them mean you arranged it. One means the opposite.',
               linhas(C.GRAMMAR_ROWS[:4], 1)),
          'Analise 1 (3 min): NAO explique formacao -- ele forma tudo isso. Explique EFEITO. A linha '
          'que surpreende quem e fluente e a quarta: "had its licence revoked" tem a forma do causativo '
          'e o sentido oposto. Peca um exemplo do trabalho dele para cada uma das quatro.')

    slide(6, head('The Analysis', 'The Passive, and What It', 'Leaves Out') +
          card('The same fact, with the agent kept, dropped, or buried in a report',
               linhas(C.GRAMMAR_ROWS[4:], 5)),
          'Analise 2 (3 min): volte ao term sheet do capitulo 4 e peca que ele classifique cada frase '
          'de la nestas tres. A ultima linha e a do briefing note que ele escreve de homework.')

    for i, (q, opts) in enumerate(C.GRAMMAR_QUIZ[:3], 1):
        slide(6, choices(q, [(k, t, ok) for k, (t, ok) in zip('abcd', opts)]),
              'Item %d (2 min): toda opcao e gramatical; so uma e o que a frase significa. Se ele '
              'hesitar, peca para ler as duas finalistas em voz alta e dizer que situacao cada uma '
              'descreve.' % i)

    slide(6, head('Production', 'Say It Both', 'Ways') +
          card('One fact, two sentences: one that names the agent, one that hides it',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, s)
                   for i, s in enumerate([
                       'An outside adviser reviewed the fund\'s exposure last quarter.',
                       'The ministry finally approved the revised tariff, after nine months of pressure.',
                       'The regulator withdrew the sponsor\'s licence three weeks before financial close.',
                       'We are arranging for a development bank to guarantee the first five years.'], 1)) +
               reveal('What to listen for',
                      'Naming: <i>we had the exposure reviewed by an outside adviser</i>. Hiding: <i>the '
                      'exposure was reviewed</i>. Item 3 is the trap: the natural causative is adversative '
                      '(<i>the sponsor had its licence withdrawn</i>), not arranged.')),
          'Producao (5 min): ele diz as duas versoes de cada fato e, em seguida, diz EM QUE SITUACAO '
          'escolheria cada uma. E aqui que a aula fecha: o passivo deixa de ser registro e vira decisao.')

    # ── FASE 7 — Speaking & Wrap ──────────────────────────────────────────────
    slide(7, head('Role-play -- Guided', 'Brief the Fund in', 'Two Minutes') +
          roleplay('A sovereign wealth fund manager has your term sheet in front of her and two minutes '
                   'before her next meeting. Walk her through what is offered, how the revenue is '
                   'secured, and who arranged each protection.',
                   ['an equity stake', 'subordinated debt', 'an off-take agreement', 'a currency hedge',
                    'we had it audited', 'we got them to approve']),
          'Role-play guiado (4 min): voce e a gestora do fundo, sem pressa de ser simpatica. Cronometre '
          'os dois minutos. Este e o degrau GUIADO: com chips na tela. O long turn logo a seguir e o '
          'mesmo conteudo sem apoio nenhum, e a diferenca entre os dois e o que voce devolve como '
          'feedback.')

    slide(7, head('Long Turn', 'Two Minutes,', 'Uninterrupted') +
          '<div class="ic-scenario"><div class="ic-who">Opening a session at an investor roundtable</div>'
          '<p>"Whose risk is it, really?"</p></div>'
          '<p style="margin-top:.8rem;font-size:.95rem">Take one project you know. Walk the room down '
          'the queue: who is paid first, who waits, who arranged each protection, and which danger did '
          'not disappear but simply changed hands. Two causatives, four terms from today, and end on '
          'the word you want remembered.</p>',
          'Long turn (5 min): DOIS minutos sem interromper, nem para corrigir. Anote tres coisas: um '
          'erro de lexico, um momento em que o agente sumiu sem intencao, e a melhor frase dele. '
          'Devolva as tres no fim, nessa ordem.')

    # O modelo do professor nao para no long turn: vem o follow-up, que e onde se
    # ve se ele so recitou o que preparou. Quatro perguntas, na ordem.
    slide(7, head('Follow-up', 'Four Questions,', 'No Restarting') +
          card('Straight after the two minutes, without praise in between',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s</span></div>' % (i, q)
                   for i, q in enumerate(C.FOLLOW_UP, 1))),
          C.FOLLOW_UP_TEACHER)

    slide(7, head('Collaborative Task', 'One Hundred Million,', 'Four Ways') +
          card('Talk it through, then decide',
               '<div class="ic-lf-list">%s</div>' % ''.join(
                   '<div class="ic-lf"><span class="ic-lbl">%s</span><span>%s</span></div>' % (k, v)
                   for k, v in [('A', 'A first-loss tranche'), ('B', 'A currency guarantee'),
                                ('C', 'A twenty-year off-take contract'),
                                ('D', 'The ministry simply takes an equity stake itself')]) +
               '<p style="margin-top:.8rem">Which single instrument brings in the most private capital '
               'per public dollar, and what does the ministry give up by choosing it?</p>'),
          'Tarefa colaborativa (5 min): participe de verdade, defendendo a opcao D (a mais fraca), e '
          'obrigue-o a te convencer. Exija linguagem de discordancia diplomatica -- e o que falta a '
          'quem e fluente e nunca precisou negociar em ingles.')

    slide(7, head('Debate I', 'Defend the Side You', 'Disagree With') +
          '<div class="ic-scenario"><div class="ic-who">Motion 1</div><p>"%s"</p></div>'
          '<p style="margin-top:.8rem;font-size:.95rem">%s</p>' % (C.DEBATE_1_MOTION, C.DEBATE_1_RULES),
          'Debate (4 min): esta e a tarefa que ele nao consegue improvisar. Obrigue a troca de lado: '
          'defender a posicao contraria e o que expoe o repertorio real. Se ele repetir argumento, '
          'interrompa e peca outro.')

    # Segundo debate, como no modelo. O primeiro cobra repertorio dos dois lados;
    # este cobra CONCESSAO, que e o que falta a quem e fluente e nunca precisou
    # ceder terreno em ingles.
    slide(7, head('Debate II', 'The Side You', 'Were Given') +
          '<div class="ic-scenario"><div class="ic-who">Motion 2</div><p>"%s"</p></div>'
          '<p style="margin-top:.8rem;font-size:.95rem">%s</p>' % (C.DEBATE_2_MOTION, C.DEBATE_2_RULES),
          C.DEBATE_2_TEACHER)

    slide(7, head('Survival', 'Five Sentences for the', 'Investor Table') +
          '<div class="ic-lf-list">%s</div>' % ''.join(
              '<div class="ic-lf"><span class="ic-lbl">%d</span><span>%s '
              '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">'
              'Listen</button></span></div>' % (i, p, p)
              for i, p in enumerate(C.SPEECH_PHRASES, 1)),
          'Survival (2 min): ele repete as cinco com a tonica no fim. Sao as mesmas frases da pre-class, '
          'de proposito: e a terceira exposicao, e a que ele leva para a reuniao.')

    slide(7, head('Self-Assessment', 'What I Can Do', 'Now') +
          card('Tick only what is true',
               checklist([
                   'I can read a gapped text and justify each choice by reference, not by topic.',
                   'I can spot the option that is true and still wrong.',
                   'I can hear five speakers and separate what they are from what they argue.',
                   'I choose between naming and hiding the agent, and I can say why I chose.',
                   'I can hold a two-minute turn on the capital stack without notes.'])),
          'Autoavaliacao (2 min): peca uma PROVA oral de cada item que ele marcar. O item que ele nao '
          'marcar entra como foco da aula 3.')

    slide(7, '<div class="chapter-label">Lesson Complete</div>\n'
             '  <h1 style="font-family:\'Cormorant Garamond\',serif;font-size:3rem;line-height:1.1">'
             'The Language of Capital<br><span class="accent">Badge Earned</span></h1>'
             '<p class="subtitle">Who is paid first, who waits, and who the sentence is hiding</p>'
             '<p style="margin-top:1.2rem;font-size:.95rem;color:rgba(255,255,255,.8)">Homework: the '
             'briefing note, 280 to 320 words. Next lesson: The Art of the Opening.</p>',
          'Fechamento (1 min): devolva as tres anotacoes do long turn, nessa ordem: lexico, agente '
          'perdido, melhor frase. Termine pela melhor frase dele.', kind='image', bg=IMG[1])

    return _slides


def main():
    s = deck()
    bar = '\n'.join('  <div class="phase-segment %s" data-phase="%d"></div>'
                    % ('current' if i == 1 else 'upcoming', i) for i in range(1, 8))
    labels = '\n'.join('  <span class="phase-label%s" data-phase="%d" data-name="%s">%s</span>'
                       % (' current' if i == 1 else '', i, p, p)
                       for i, p in enumerate(PHASES, 1))
    out = ('<div class="phase-bar" id="phaseBar">\n%s\n</div>\n'
           '<div class="phase-labels" id="phaseLabels">\n%s\n</div>\n\n'
           '<div class="slides-container" id="slidesContainer">\n%s\n</div>\n'
           % (bar, labels, '\n'.join(s)))
    open(os.path.join(HERE, 'slides.html'), 'w', encoding='utf-8').write(out)
    print('slides.html: %d slides, %d KB' % (len(s), len(out) // 1024))


if __name__ == '__main__':
    main()
