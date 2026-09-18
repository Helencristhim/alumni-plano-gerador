#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cpe_lib.py — blocos de aula no formato de prova Cambridge (CPE/CAE) para o
material do Guilherme Henrique Caneli.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
O professor (Andre Marinho) deu o feedback de 18/09/2026: para um aluno C1+ que
"poderia dar aula de ingles", card de vocabulario com definicao e matching
palavra->definicao e RECONHECIMENTO, nao raciocinio. Ele mandou dois modelos
(cpe-infrastructure-finance-lesson_12.html e w11_l11e.html) em que toda tarefa e
uma tarefa de prova: gapped text (Part 6), multiple choice (Part 5), word
formation (Part 3), key-word transformation (Part 4), sentence completion
(Listening Part 2) e multiple matching com duas tarefas (Listening Part 4).

O QUE ESTE ARQUIVO NAO FAZ
--------------------------
Nao inventa mecanica nova. Cada tarefa de prova e montada sobre uma PRIMITIVA que
ja existe no hub deste aluno e que o CI ja conhece:

    gapped text / multiple matching / cloze  ->  .match-row + checkMatch()
    multiple choice                          ->  .quiz-item + selectQuiz()
    word formation / transformation / gaps   ->  .blank-input + checkBlank()
    transcript, gabarito, comentario         ->  .comp-q + revealComp()
    audio                                    ->  .lp + togglePlayer()/initPlayer()
    fala do aluno                            ->  .speech-card / .think-card

Isso mantem TRES coisas que quebrariam se a mecanica fosse nova: o calculo de
progresso (updateProgress conta .match-row.correct, .blank-input.correct,
.quiz-item, .speech-card, .think-card), o GATE 7b (handler nao pode chamar funcao
indefinida) e o GATE 10 (reveal por stylesheet nao pode nascer com display:none
inline). O que muda e o DESENHO da tarefa, que e exatamente o que o professor
pediu.

ESCOPO: este arquivo e do material DESTE aluno. Nao e importado por nenhum outro.
"""
import html as _html
import re


def esc(s):
    return _html.escape(s, quote=True)


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


# ── moldura ────────────────────────────────────────────────────────────────────

def section(title, badge, badge_class, intro='', body='', rubric=''):
    """Uma etapa da aula: cabecalho + rubrica (a instrucao de prova) + corpo."""
    out = ['<div class="exercise-section">']
    # title/badge ja vem com entidade HTML de proposito (--, &middot;): escapar
    # aqui imprimia "--" na tela como texto.
    out.append('<div class="section-header-row"><h4>%s</h4><span class="badge %s">%s</span></div>'
               % (title, badge_class, badge))
    if intro:
        out.append('<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;'
                   'font-style:italic">%s</p>' % intro)
    if rubric:
        out.append('<div style="border-left:3px solid var(--accent);background:var(--accent-dim);'
                   'padding:.7rem .9rem;border-radius:0 8px 8px 0;margin-bottom:1rem;'
                   'font-size:.86rem;line-height:1.6">%s</div>' % rubric)
    out.append(body)
    out.append('</div>')
    return '\n'.join(out)


def paper_tag(text):
    """A etiqueta do papel da prova ("Paper 1 · Part 6 · 18 min")."""
    return ('<div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;'
            'color:var(--accent);font-weight:700;margin-bottom:.35rem">%s</div>' % text)


# ── vocabulario ────────────────────────────────────────────────────────────────

def vocab_cards(items):
    """items: (word, definition, example). O audio vem do audioMap pela palavra."""
    out = ['<div class="vocab-cards">']
    for w, d, ex in items:
        out.append(
            '<div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
            '<span class="vocab-card-word">%s</span><span class="vocab-card-dot"> -- </span>'
            '<span class="vocab-card-def">%s</span></div>'
            '<div class="vocab-card-example">&ldquo;%s&rdquo;</div></div>'
            '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
            % (esc(w), esc(d), esc(ex), esc(w)))
    out.append('</div>')
    return '\n'.join(out)


def collocation_bank(rows):
    """Bloco estatico: as combinacoes que andam juntas (o 'collocation bank')."""
    chips = []
    for r in rows:
        chips.append('<span style="display:inline-block;background:var(--bg-elevated);'
                     'border:1px solid var(--border);border-radius:999px;padding:.32rem .8rem;'
                     'margin:.2rem .25rem .2rem 0;font-size:.84rem">%s</span>' % r)
    return '<div style="margin:.4rem 0 .2rem">%s</div>' % ''.join(chips)


# ── match-row: gapped text, multiple matching, cloze, colocacao ───────────────

def match_grid(grid_id, rows, options, verify=True, left_style=''):
    """rows: (rotulo_esquerdo, resposta). options: [(value, label)] — iguais em toda linha.

    O value do <option> e o que checkMatch compara com data-answer da linha.
    """
    out = ['<div class="match-grid" id="%s">' % grid_id]
    for label, answer in rows:
        out.append('<div class="match-row" data-answer="%s">' % esc(answer))
        out.append('<span class="match-word"%s>%s</span>' % (left_style, label))
        out.append('<select onchange="checkMatch(this)">')
        out.append('<option value="">Select...</option>')
        for value, text in options:
            out.append('<option value="%s">%s</option>' % (esc(value), esc(text)))
        out.append('</select></div>')
    out.append('</div>')
    if verify:
        out.append('<button class="verify-all-btn" onclick="verifyAllMatches(\'%s\')">Check answers</button>' % grid_id)
    return '\n'.join(out)


# ── blank-input: word formation, transformation, sentence completion ──────────

def fill_items(items):
    """items: dict(before, after, answer, alt, hint, phrase).

    `phrase` SO pode ser preenchido quando existe MP3 daquela frase no audioMap:
    o botao Listen le o audioMap pelo texto. Em tarefa de LISTENING a frase nunca
    entra — ouvir a resposta e a tarefa.
    """
    out = []
    for it in items:
        attrs = ['class="blank-input"', 'data-answer="%s"' % esc(it['answer'])]
        if it.get('alt'):
            attrs.append('data-alt="%s"' % esc(it['alt']))
        if it.get('hint'):
            attrs.append('data-hint="%s"' % esc(it['hint']))
        if it.get('phrase'):
            attrs.append('data-phrase="%s"' % esc(it['phrase']))
        attrs.append('placeholder="___"')
        listen = ('<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                  if it.get('phrase') else '')
        out.append('<div class="fill-blank-item"><div class="fill-blank-sentence">%s<input %s>%s</div>'
                   '%s<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
                   % (it['before'], ' '.join(attrs), it.get('after', ''), listen))
    return '\n'.join(out)


# ── quiz-item: multiple choice ────────────────────────────────────────────────

def quiz(items):
    """items: (pergunta, [(texto, correta?)])."""
    out = []
    for n, (q, opts) in enumerate(items, 1):
        out.append('<div class="quiz-item"><div class="quiz-question">%d. %s</div><div class="quiz-options">' % (n, q))
        for i, (text, ok) in enumerate(opts):
            out.append('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s">'
                       '<span class="option-letter">%s</span> %s</div>'
                       % ('true' if ok else 'false', 'ABCD'[i], text))
        out.append('</div></div>')
    return '\n'.join(out)


# ── comp-q: gabarito, transcricao, comentario do professor ───────────────────

def reveal(label, content):
    """Reveal por STYLESHEET (.comp-q.revealed .q-answer) — o alvo NAO leva
    display:none inline, senao o inline vence a folha e nada aparece (GATE 10)."""
    return ('<div class="comp-q" onclick="revealComp(this)">'
            '<div class="q-text">%s</div><div class="q-answer">%s</div></div>' % (label, content))


# ── player de audio (usa as funcoes do proprio hub) ───────────────────────────

def player(pid, src, caption=''):
    cap = ('<div style="font-size:.78rem;color:var(--text-dim);margin-bottom:.5rem">%s</div>' % caption) if caption else ''
    # classe propria (cpe-lp) porque as regras .lp-* do hub foram escritas para
    # SLIDE ESCURO (texto branco). Dentro da aba Pre-class, que e clara, o player
    # sairia branco no branco. A classe .lp fica para o JS (#id .lp-play, .lp-speed-btn).
    return (cap + '<div class="lp cpe-lp" id="%s" data-src="%s" style="max-width:520px;margin:.4rem 0 1rem">'
            '<div class="lp-seekbar" onclick="seekAudio(event,\'%s\')"><div class="lp-progress" id="progress-%s"></div></div>'
            '<div class="lp-times"><span id="time-current-%s">0:00</span><span id="time-total-%s">0:00</span></div>'
            '<div class="lp-row">'
            '<button class="lp-btn" onclick="skipAudio(\'%s\',-5)" aria-label="Back 5 seconds">-5s</button>'
            '<button class="lp-btn lp-play" id="play-%s" onclick="togglePlayer(\'%s\')" aria-label="Play or pause">'
            '<svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18">'
            '<polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
            '<svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none">'
            '<rect x="6" y="4" width="4" height="16" fill="currentColor"/>'
            '<rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>'
            '<button class="lp-btn" onclick="skipAudio(\'%s\',5)" aria-label="Forward 5 seconds">+5s</button></div>'
            '<div class="lp-speeds">'
            '<button class="lp-speed-btn" onclick="setPlayerSpeed(\'%s\',0.85,this)">0.85x</button>'
            '<button class="lp-speed-btn active" onclick="setPlayerSpeed(\'%s\',1,this)">1x (exam pace)</button>'
            '<button class="lp-speed-btn" onclick="setPlayerSpeed(\'%s\',1.15,this)">1.15x</button></div></div>'
            % (pid, src, pid, pid, pid, pid, pid, pid, pid, pid, pid, pid, pid))


# ── fala ──────────────────────────────────────────────────────────────────────

def speech_cards(phrases):
    out = []
    for p in phrases:
        out.append('<div class="speech-card" data-phrase="%s"><div class="speech-phrase">%s</div>'
                   '<div class="speech-controls">'
                   '<button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
                   '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
                   '<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>'
                   '<div class="speech-result"></div></div>' % (esc(p), esc(p)))
    return '\n'.join(out)


def think_card(question, result_id):
    return ('<div class="think-card"><div class="think-question">%s</div>'
            '<div class="speech-controls">'
            '<button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>'
            '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>'
            '<div id="%s"></div></div>' % (question, result_id))


def gap(n):
    """A marca de lacuna dentro de um texto corrido."""
    return ('<span style="display:inline-block;min-width:2.1rem;text-align:center;'
            'background:var(--accent);color:#fff;border-radius:5px;font-weight:700;'
            'font-size:.78rem;padding:.05rem .35rem;margin:0 .15rem">%s</span>' % n)
