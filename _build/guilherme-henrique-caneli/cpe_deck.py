#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biblioteca de renderizacao dos decks IN CLASS em formato de prova (CPE).

Extraida, sem mudar uma linha, do build_slides_cpe.py da AULA 2 -- que continua
existindo e continua sendo o dono do deck dela. Aqui ficam so os blocos que nao
tem nada de aula 2 dentro: o envelope do slide, os cartoes, as escolhas, o
pareamento, os players e o gabarito.

O que NAO mora aqui e a prosa: titulo de capitulo, nota ao professor, a ordem
dos slides. Isso e de cada aula, e vive no deck_cpe.py dela, porque e ali que
uma aula deixa de ser igual a outra.

So usa blocos que o deck ja sabe renderizar e validar:
    ic-choices + icPickGist   escolha com acerto/erro na hora
    ic-match   + icPickMatch  pareamento clicavel, com placar
    comp-q     + revealComp   gabarito e justificativa escondidos
    lp/mp*     + mpToggle     player de audio do deck
"""
import os

A = 'guilherme-henrique-caneli'
AUDIO = '/audio/%s/' % A


def reset():
    """Zera o contador entre dois decks gerados no mesmo processo."""
    _n[0] = 0
    del _slides[:]


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

def write(here, phases, nome='slides.html'):
    """Fecha o deck: barra de fases, rotulos e o container dos slides.

    Identico ao main() da aula 2. A barra tem 7 segmentos porque o CSS da casca
    tem 7; uma aula com menos fases deixa as ultimas vazias em vez de quebrar o
    seletor.
    """
    bar = '\n'.join('  <div class="phase-segment %s" data-phase="%d"></div>'
                    % ('current' if i == 1 else 'upcoming', i) for i in range(1, 8))
    labels = '\n'.join('  <span class="phase-label%s" data-phase="%d" data-name="%s">%s</span>'
                       % (' current' if i == 1 else '', i, p, p)
                       for i, p in enumerate(phases, 1))
    out = ('<div class="phase-bar" id="phaseBar">\n%s\n</div>\n'
           '<div class="phase-labels" id="phaseLabels">\n%s\n</div>\n\n'
           '<div class="slides-container" id="slidesContainer">\n%s\n</div>\n'
           % (bar, labels, '\n'.join(_slides)))
    open(os.path.join(here, nome), 'w', encoding='utf-8').write(out)
    print('  %s: %d slides, %d KB' % (nome, len(_slides), len(out) // 1024))
    return len(_slides)
