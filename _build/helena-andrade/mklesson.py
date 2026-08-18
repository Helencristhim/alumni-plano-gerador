#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mklesson.py — AUTORIA das aulas da Helena Andrade (PS-ASON, B2, reading-driven).

NAO substitui o builder. Ele emite exatamente os arquivos de CONTEUDO que se
escreveriam a mao (slides.html / preclass.html / complementary.html / config.json)
em _build/helena-andrade-aula{N}/, a partir de uma ficha por aula em specs/aulaN.json.
Depois disso o fluxo e o de sempre:

    python3 _build/model/build_from_model.py _build/helena-andrade-aula{N}/config.json

POR QUE EXISTE. Sao 10 aulas com a MESMA forma (o exame e sempre o mesmo: 10 questoes
de leitura, distratores parafraseados). Escrever 10x o mesmo esqueleto a mao e a receita
para a REGRA 11 item 9 (uniformidade) quebrar na aula 6. Aqui a forma e uma so; o que
varia por aula e o conteudo da ficha.

USO:  python3 _build/helena-andrade/mklesson.py 1
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

SLUG = 'helena-andrade'
STUDENT = 'Helena Andrade'
FIRST = 'Helena'
TOTAL_AULAS = 38
ACCENT = '#16325c'
ACCENT_LIGHT = '#4e86c7'
IMG = 'https://images.unsplash.com/photo-'

SPEAK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
         '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen')


def esc(t):
    """Texto para dentro de ATRIBUTO HTML. Aspas duplas nunca entram (REGRA 7.1: o
    texto vai no atributo, e ali a aspa dupla e o unico caractere que fecha)."""
    return (t.replace('&', '&amp;').replace('"', '&quot;')
             .replace('<', '&lt;').replace('>', '&gt;'))


def audio_btn(text, small=True):
    cls = 'audio-btn-sm' if small else 'audio-btn'
    return (f'<button class="{cls}" data-speak="{esc(text)}" '
            f'onclick="speakText(this.dataset.speak,this)">{SPEAK}</button>')


def bgimg(pid, dark='rgba(8,18,36,.80)', dark2='rgba(8,18,36,.92)'):
    return (f'background-image:linear-gradient({dark},{dark2}),'
            f"url('{IMG}{pid}?w=1400&q=80');background-size:cover;background-position:center")


# ─────────────────────────────────────────────────────────────────────────────
# SLIDES (IN CLASS)
# ─────────────────────────────────────────────────────────────────────────────
def slide(n, phase, cls, teacher, inner, style=''):
    st = f' style="{style}"' if style else ''
    return (f'<div class="slide {cls}" data-slide="{n}" data-phase="{phase}" '
            f'data-teacher="{esc(teacher)}"{st}>\n  <div class="slide-inner">\n'
            f'{inner}\n  </div>\n</div>\n')


def slide_c(n, phase, cls, teacher, inner, style=''):
    """igual, mas com slide-inner centralizado (capa / transicao / dark)."""
    st = f' style="{style}"' if style else ''
    return (f'<div class="slide {cls}" data-slide="{n}" data-phase="{phase}" '
            f'data-teacher="{esc(teacher)}"{st}>\n  <div class="slide-inner" style="text-align:center">\n'
            f'{inner}\n  </div>\n</div>\n')


VOCAB_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8">'
    '<path d="M3 18h18"/><path d="M5 18l-2-6h18l-2 6"/><path d="M12 12V4"/>'
    '<path d="M12 4l6 3-6 3"/></svg>')

# A PISTA DO CARD E TEXTO BRANCO SOBRE O GRADIENTE. Os dez pares abaixo foram
# escolhidos com o parada mais CLARA ainda escura o bastante para dar >= 4.5:1 com
# branco (WCAG AA). O gradiente do molde nao passa nesse criterio (mede 1.3-1.7), e a
# pista e justamente o texto que a aluna le antes de revelar a palavra.
GRADS = ['#0f2f5e,#2f5f9e', '#0b3d3a,#1f6f68', '#4a1533,#8a2f60', '#4a3208,#8a6014',
         '#22245c,#4a4d9c', '#0d3a1f,#1f6b3a', '#4a1418,#8a2c34', '#0e3243,#2a6a86',
         '#2c1a4a,#573290', '#3a2a0a,#6f5418']


def vocab_grid(words, gid, start):
    cards = ''
    for i, w in enumerate(words):
        grad = GRADS[(start + i) % len(GRADS)]
        cards += (
            f'      <div class="vocab-card" onclick="revealVocab(this)">\n'
            f'        <div class="card-icon" style="background:linear-gradient(135deg,{grad})">'
            f'{VOCAB_ICON}<div class="card-hint">{w["def"]}</div></div>\n'
            f'        <div class="card-body"><div class="card-word">{w["w"]}</div>'
            f'<div class="card-def">{w["def"]}</div>'
            f'<div class="card-example">&quot;{w["ex"]}&quot;</div>'
            f'<div class="card-audio">{audio_btn(w["w"])}</div></div>\n'
            f'      </div>\n')
    return (f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
            f'<span id="vocabCount{gid}">0 / {len(words)} words revealed</span></p>\n'
            f'    <div class="vocab-grid" id="vocabGrid{gid}">\n{cards}    </div>')


def chips(items, dark=True):
    if dark:
        st = ('background:rgba(255,255,255,.1);border:1px solid var(--accent-light);'
              'border-radius:20px;padding:.3rem .8rem;font-size:.82rem;color:#fff')
    else:
        st = ('background:var(--bg-card);border:1px solid var(--accent);'
              'border-radius:20px;padding:.3rem .7rem;font-size:.8rem')
    return ''.join(f'<span style="{st}">{c}</span>' for c in items)


def da(txt):
    """O `.accent` e var(--accent) -- um azul-marinho profundo. Sobre slide escuro ou
    foto ele fica INVISIVEL, e o contrast-guard NAO o salva: ele pula elemento cujo fundo
    e gradiente/imagem (nao ha como adivinhar a cor efetiva). Em fundo escuro o destaque
    tem de ser o accent-light. Medido no Chromium na 1a versao desta aula."""
    return (txt.replace('class="accent"', 'class="accent" style="color:var(--accent-light)"')
               .replace("class='accent'", "class='accent' style='color:var(--accent-light)'"))


def heading(txt, dark=False, size=None):
    st = []
    if size:
        st.append(f'font-size:{size}')
    if dark:
        st.append('color:#fff')
        txt = da(txt)
    s = f' style="{";".join(st)}"' if st else ''
    return f'<h2 class="slide-heading"{s}>{txt}</h2>'


def player(pid, src, qid, questions, waveform):
    bars = ''.join('<div class="bar"></div>' for _ in range(20))
    qs = ''.join(
        f'<div class="comp-q" onclick="revealComp(this)"><div class="q-text">{i+1}. {q}</div>'
        f'<div class="q-answer">{a}</div></div>' for i, (q, a) in enumerate(questions))
    return f'''    <div class="waveform waveform-paused" id="{waveform}">{bars}</div>
    <div class="mock-player" id="{pid}" data-src="{src}" data-waveform="{waveform}" data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">
      <div class="lp-seekbar" onclick="mpSeek(event,'{pid}')" style="width:100%;height:6px;background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative"><div class="lp-progress" id="progress-{pid}" style="width:0%;height:100%;background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>
      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem"><span id="time-current-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span><span id="time-total-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>
      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">
        <button class="lp-btn" onclick="mpSkip('{pid}',-5)" aria-label="Back 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>
        <button class="lp-btn lp-play" id="play-{pid}" onclick="mpToggle('{pid}')" aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:48px;height:48px;cursor:pointer"><svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg><svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none"><rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>
        <button class="lp-btn" onclick="mpSkip('{pid}',5)" aria-label="Forward 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>
      </div>
      <div style="display:flex;gap:.4rem;justify-content:center">
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',0.5,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.5x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',0.75,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.75x</button>
        <button class="lp-speed-btn lp-speed-active" onclick="mpSpeed('{pid}',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',1.25,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1.25x</button>
      </div>
    </div>
    <div class="comp-questions" id="{qid}" style="max-width:520px;margin:1.2rem auto 0">{qs}</div>'''


def build_slides(s):
    n = s['n']
    out = []
    T = s['teacher']
    ch = s['chapters']          # 7 nomes
    im = s['images']            # 7 ids: capa + 6 transicoes

    # ── FASE 1 ──────────────────────────────────────────────────────────────
    out.append(slide_c(1, 1, 'slide-image active', T['s1'],
        f'    <div class="chapter-label">Lesson {n:02d} &middot; {ch[0]}</div>\n'
        f'    <h1 class="slide-heading" style="font-size:2.4rem;color:#fff">{da(s["title_html"])}</h1>\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:1rem;max-width:640px;'
        f'margin-left:auto;margin-right:auto">{s["hero_line"]}</p>',
        bgimg(im[0], 'rgba(8,18,36,.72)', 'rgba(8,18,36,.90)')))

    out.append(slide_c(2, 1, 'slide-dark', T['s2'],
        f'    <div class="chapter-label">Chapter 1: {ch[0]}</div>\n'
        f'    {heading(s["warmup"]["h"], dark=True)}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:1rem;max-width:600px;'
        f'margin-left:auto;margin-right:auto">{s["warmup"]["p"]}</p>\n'
        f'    <div style="display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center;margin-top:1.2rem">'
        f'{chips(s["warmup"]["chips"])}</div>',
        bgimg(im[0], 'rgba(8,18,36,.84)', 'rgba(8,18,36,.94)')))

    out.append(slide(3, 1, 'slide-light', T['s3'],
        f'    <div class="chapter-label">The Exam</div>\n'
        f'    {heading(s["provoke"]["h"])}\n'
        f'    <div style="max-width:640px;margin:1.4rem auto 0;background:var(--accent-dim);'
        f'border:1px solid var(--accent);border-left:5px solid var(--accent);border-radius:10px;padding:1.4rem">\n'
        f'      <p style="font-size:1rem;line-height:1.7;font-style:italic">&quot;{s["provoke"]["quote"]}&quot;</p>\n'
        f'      <p style="font-size:.78rem;color:var(--text-dim);margin-top:.7rem">{s["provoke"]["src"]}</p>\n'
        f'    </div>\n'
        f'    <p style="text-align:center;font-size:.9rem;color:var(--text-dim);margin-top:1.2rem;'
        f'max-width:600px;margin-left:auto;margin-right:auto">{s["provoke"]["task"]}</p>'))

    goals = ''.join(
        f'<div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;'
        f'padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">{i+1}. {g[0]}</p>'
        f'<p style="font-size:.78rem;color:var(--text-dim)">{g[1]}</p></div>'
        for i, g in enumerate(s['goals']))
    out.append(slide(4, 1, 'slide-light', T['s4'],
        f'    <div class="chapter-label">Today&#39;s Goal</div>\n'
        f'    {heading("Three <span class=\'accent\'>Missions</span>")}\n'
        f'    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));'
        f'gap:.8rem;max-width:700px;margin:1.5rem auto 0">{goals}</div>'))

    # ── FASE 2 — vocabulario ────────────────────────────────────────────────
    out.append(slide_c(5, 2, 'slide-image', T['s5'],
        f'    <div class="chapter-label">Chapter 2: {ch[1]}</div>\n'
        f'    {heading(s["vocab_head"], dark=True, size="2rem")}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:.5rem">'
        f'{len(s["vocab"])} words the exam expects you to already own</p>',
        bgimg(im[1])))

    # QUATRO CARDS POR TELA E O TETO. Com cinco, o quinto nasce cortado embaixo dos
    # 100vh do slide (medido no Chromium). Dez palavras => 4 + 3 + 3.
    for gi, (a, b) in enumerate(((0, 4), (4, 7), (7, 10))):
        out.append(slide(6 + gi, 2, 'slide-light', T[f's{6+gi}'],
            f'    <div class="chapter-label">Vocabulary</div>\n'
            f'''    {heading(f"Words <span class='accent'>{a+1}-{b}</span>")}\n'''
            + vocab_grid(s['vocab'][a:b], gi + 1, a)))

    out.append(slide(9, 2, 'slide-light', T['s9'],
        f'    <div class="chapter-label">Consolidate</div>\n'
        f'    {heading("Word to <span class=\'accent\'>Meaning</span>")}\n'
        f'    <!--IC-BLOCKS:vocab-->'))

    # ── FASE 3 — o texto ────────────────────────────────────────────────────
    out.append(slide_c(10, 3, 'slide-image', T['s10'],
        f'    <div class="chapter-label">Chapter 3: {ch[2]}</div>\n'
        f'    {heading(s["reading_head"], dark=True, size="2rem")}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:.5rem">'
        f'{s["reading_sub"]}</p>', bgimg(im[2])))

    out.append(slide(11, 3, 'slide-light', T['s11'],
        f'    <div class="chapter-label">Reading</div>\n'
        f'    {heading(s["reading_title_html"])}\n'
        f'    <!--IC-BLOCKS:reading-->'))
    out.append(slide(12, 3, 'slide-light', T['s12'],
        f'    <div class="chapter-label">Main Idea</div>\n'
        f'    {heading("What Is the Text <span class=\'accent\'>Really Saying?</span>")}\n'
        f'    <!--IC-BLOCKS:gist-->'))
    out.append(slide(13, 3, 'slide-light', T['s13'],
        f'    <div class="chapter-label">Detail</div>\n'
        f'    {heading("True or <span class=\'accent\'>False?</span>")}\n'
        f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
        f'Not one of these sentences uses the words the text uses.</p>\n'
        f'    <!--IC-BLOCKS:tf-->'))

    # ── FASE 4 — gramatica ──────────────────────────────────────────────────
    out.append(slide_c(14, 4, 'slide-image', T['s14'],
        f'    <div class="chapter-label">Chapter 4: {ch[3]}</div>\n'
        f'    {heading(s["grammar_head"], dark=True, size="2rem")}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:.5rem">'
        f'{s["grammar_sub"]}</p>', bgimg(im[3])))

    ex = ''
    for e in s['grammar_examples']:
        ex += (f'<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
               f'padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
               f'<p style="font-size:.92rem">&quot;{e["html"]}&quot;</p>{audio_btn(e["say"])}</div>')
    rows = ''
    for i, r in enumerate(s['grammar_rows']):
        bg = 'background:var(--bg-elevated);' if i % 2 else ''
        if len(r) == 2:
            rows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                     f'<td style="padding:.5rem;font-weight:600">{r[0]}</td>'
                     f'<td style="padding:.5rem" colspan="2">{r[1]}</td></tr>')
        else:
            rows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                     f'<td style="padding:.5rem;font-weight:600">{r[0]}</td>'
                     f'<td style="padding:.5rem">{r[1]}</td>'
                     f'<td style="padding:.5rem">{r[2]}</td></tr>')
    rid = f'rule{n}'
    out.append(slide(15, 4, 'slide-light', T['s15'],
        f'    <div class="chapter-label">Grammar Discovery</div>\n'
        f'    {heading(s["grammar_discovery_h"])}\n'
        f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:640px;margin:1rem auto 0">{ex}</div>\n'
        f'    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">'
        f'{s["grammar_question"]}</p>\n'
        f'    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);'
        f'color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;'
        f'cursor:pointer" onclick="var t=document.getElementById(\'{rid}\');'
        f't.style.display=(t.style.display===\'none\'||!t.style.display)?\'block\':\'none\'">Reveal the Rule</button>\n'
        f'    <div id="{rid}" style="display:none;max-width:640px;margin:1rem auto 0;overflow-x:auto">\n'
        f'      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);'
        f'border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
        f'        <thead><tr style="background:var(--accent);color:#fff">'
        f'<th style="padding:.6rem;text-align:left">Form</th>'
        f'<th style="padding:.6rem;text-align:left">What it does</th>'
        f'<th style="padding:.6rem;text-align:left">Example</th></tr></thead>\n'
        f'        <tbody>{rows}</tbody>\n      </table>\n'
        f'      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">'
        f'{s["grammar_insight"]}</p>\n    </div>'))

    fills = ''.join(
        f'<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">'
        f'&quot;{f[0]}<span class="fill-blank">___</span><span class="fill-answer">{f[1]}</span>'
        f'{f[2]}&quot;</div></div>' for f in s['grammar_practice'])
    out.append(slide(16, 4, 'slide-light', T['s16'],
        f'    <div class="chapter-label">Practice</div>\n'
        f'    {heading("Which Form, <span class=\'accent\'>Which Meaning?</span>")}\n'
        f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
        f'Say it first, then click to check</p>\n'
        f'    <div class="fill-grid">{fills}</div>'))

    errs = ''.join(
        f'<div class="error-card" onclick="revealError(this)">'
        f'<div class="error-sentence">&quot;{e[0]}&quot;</div>'
        f'<div class="error-fix">&quot;{e[1]}&quot;</div></div>' for e in s['spot'])
    out.append(slide(17, 4, 'slide-light', T['s17'],
        f'    <div class="chapter-label">Detective</div>\n'
        f'    {heading("Spot the <span class=\'accent\'>Error</span>")}\n'
        f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
        f'<span id="errorScore">0 / {len(s["spot"])} errors found</span></p>\n'
        f'    <div class="error-grid" id="errorGrid">{errs}</div>'))

    # ── FASE 5 — equivalencia semantica ─────────────────────────────────────
    out.append(slide_c(18, 5, 'slide-image', T['s18'],
        f'    <div class="chapter-label">Chapter 5: {ch[4]}</div>\n'
        f'    {heading("Same Fact, <span class=\'accent\'>Other Words</span>", dark=True, size="2rem")}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:.5rem">'
        f'The exam never repeats the word the text used</p>', bgimg(im[4])))

    lf = ''.join(
        f'<div class="ic-lf"><span class="ic-lbl">{i+1}</span><span>The text says '
        f'<span class="ic-mod">{p[0]}</span> &mdash; the question says '
        f'<span class="ic-mod ic-strong">{p[1]}</span>.</span></div>'
        for i, p in enumerate(s['lf_pairs']))
    out.append(slide(19, 5, 'slide-light', T['s19'],
        f'    <div class="chapter-label">How the Exam Hides It</div>\n'
        f'    {heading("The Distractor Never <span class=\'accent\'>Repeats the Word</span>")}\n'
        f'    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin:.6rem auto 1rem;'
        f'max-width:620px">{s["lf_lead"]}</p>\n'
        f'    <div class="ic-lf-list">{lf}</div>'))

    out.append(slide(20, 5, 'slide-light', T['s20'],
        f'    <div class="chapter-label">Equivalence</div>\n'
        f'    {heading("Plain English to <span class=\'accent\'>Exam Register</span>")}\n'
        f'    <!--IC-BLOCKS:equiv-->'))

    out.append(slide(21, 5, 'slide-light', T['s21'],
        f'    <div class="chapter-label">Complete</div>\n'
        f'    {heading("Put the Register <span class=\'accent\'>Back In</span>")}\n'
        f'    <!--IC-BLOCKS:gap-->'))

    out.append(slide(22, 5, 'slide-light', T['s22'],
        f'    <div class="chapter-label">Quick Fire</div>\n'
        f'    {heading("One Question at <span class=\'accent\'>a Time</span>")}\n'
        f'    <!--IC-BLOCKS:quickfire-->'))

    # ── FASE 6 — escuta + producao ──────────────────────────────────────────
    out.append(slide_c(23, 6, 'slide-image', T['s23'],
        f'    <div class="chapter-label">Chapter 6: {ch[5]}</div>\n'
        f'    {heading(s["prod_head"], dark=True, size="2rem")}\n'
        f'    <p style="color:rgba(255,255,255,.85);font-size:1rem;margin-top:.5rem">'
        f'{s["prod_sub"]}</p>', bgimg(im[5])))

    for k, ls in enumerate(s['listenings']):
        pid = f'mp-listen{k+1}'
        out.append(slide_c(24 + k, 6, 'slide-dark', T[f's{24+k}'],
            f'    <div class="chapter-label">Listening {k+1}</div>\n'
            f'    {heading(ls["h"], dark=True)}\n'
            f'    <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem">'
            f'{ls["sub"]}</p>\n'
            + player(pid, f'/audio/{SLUG}/a{n}_listening{k+1}.mp3', f'listening{k+1}Qs',
                     ls['questions'], f'waveform{k+1}')))

    grads_rp = ['var(--accent-dim),rgba(22,50,92,.05)',
                'rgba(22,50,92,.08),rgba(22,50,92,.02)',
                'rgba(22,50,92,.12),rgba(22,50,92,.03)']
    for k, rp in enumerate(s['roleplays']):
        chip_html = (f'<p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Support:</p>'
                     f'<div style="display:flex;flex-wrap:wrap;gap:.4rem">{chips(rp["chips"], dark=False)}</div>'
                     if rp.get('chips') else
                     f'<p style="font-size:.85rem;color:var(--text-dim);font-style:italic">{rp["note"]}</p>')
        out.append(slide(26 + k, 6, 'slide-light', T[f's{26+k}'],
            f'    <div class="chapter-label">{rp["label"]}</div>\n'
            f'    {heading(rp["h"])}\n'
            f'    <div class="roleplay-body" style="max-width:540px;margin:1rem auto 0;'
            f'background:linear-gradient(135deg,{grads_rp[k]});border:1px solid var(--accent);'
            f'border-radius:12px;padding:1.5rem">\n'
            f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem">'
            f'<strong>Task:</strong> {rp["scenario"]}</p>\n      {chip_html}\n    </div>'))

    # ── FASE 7 — fecho ──────────────────────────────────────────────────────
    out.append(slide_c(29, 7, 'slide-image', T['s29'],
        f'    <div class="chapter-label">Chapter 7: {ch[6]}</div>\n'
        f'    {heading(s["wrap_head"], dark=True, size="2rem")}', bgimg(im[6])))

    surv = ''.join(
        f'<div class="survival-item-ic" style="background:rgba(255,255,255,.08);border:1px solid var(--border);'
        f'border-radius:10px;padding:.9rem;display:flex;justify-content:space-between;align-items:center;'
        f'gap:.6rem"><span style="font-size:.92rem">{p}</span>{audio_btn(p)}</div>'
        for p in s['survival'])
    out.append(slide_c(30, 7, 'slide-dark', T['s30'],
        f'    <div class="chapter-label">Survival Card</div>\n'
        f'    {heading("Five Sentences from <span class=\'accent\'>Today&#39;s Text</span>", dark=True)}\n'
        f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1.2rem auto 0;'
        f'text-align:left">{surv}</div>'))

    checks = ''.join(
        f'<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">'
        f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        f'<polyline points="20 6 9 17 4 12"/></svg></div>{c}</div>' for c in s['checklist'])
    out.append(slide_c(31, 7, 'slide-dark', T['s31'],
        f'    <div class="chapter-label">Self-Assessment</div>\n'
        f'    {heading("What I <span class=\'accent\'>Can Do Now</span>", dark=True)}\n'
        f'    <div class="check-grid" id="checklist-{n}" style="max-width:580px;margin:1.2rem auto 0;'
        f'display:flex;flex-direction:column;gap:.5rem;text-align:left">{checks}</div>'))

    out.append(slide_c(32, 7, 'slide-dark', T['s32'],
        f'    <div class="chapter-label">Lesson Complete</div>\n'
        f'    <div class="badge-card">\n'
        f'      <div class="badge-icon">\n'
        f'        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/>'
        f'</svg></div>\n'
        f'        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div>'
        f'<div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div>'
        f'<div class="sparkle"></div></div>\n      </div>\n'
        f'      {heading(s["badge"] + " <span class=\'accent\'>Earned!</span>", dark=True)}\n'
        f'      <p style="color:rgba(255,255,255,.8);font-size:1rem;margin-top:.5rem">{s["badge_line"]}</p>\n'
        f'      <p style="color:rgba(255,255,255,.85);font-size:.85rem;margin-top:1.5rem">'
        f'Lesson {n} -- Complete.</p>\n'
        f'      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: '
        f'{s["next_preview"]}</p>\n    </div>'))

    return '\n'.join(out)


# ─────────────────────────────────────────────────────────────────────────────
# PRE-CLASS
# ─────────────────────────────────────────────────────────────────────────────
def rotate(lst, k):
    """Rotacao NUNCA identidade: opcao na mesma ordem das palavras viola a REGRA 24."""
    k %= len(lst)
    if k == 0:
        k = 1
    return lst[k:] + lst[:k]


def build_preclass(s):
    n = s['n']
    vocab = s['vocab']
    cards = ''.join(
        f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
        f'<span class="vocab-card-word">{w["w"]}</span><span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{w["def"]}</span></div>'
        f'<div class="vocab-card-example">&quot;{w["ex"]}&quot;</div></div>'
        f'<button class="audio-btn" data-speak="{esc(w["w"])}" '
        f'onclick="speakText(this.dataset.speak,this)">Listen</button></div>\n'
        for w in vocab)

    defs = [w['def'] for w in vocab]
    rows = ''
    for i, w in enumerate(vocab):
        opts = rotate(defs, i * 3 + 1)
        assert opts != defs, 'matching: opcoes na ordem original (REGRA 24)'
        o = ''.join(f'<option value="{esc(d)}">{d}</option>' for d in opts)
        rows += (f'        <div class="match-row" data-answer="{esc(w["def"])}">'
                 f'<span class="match-word" style="flex:0 0 170px">{w["w"]}</span>'
                 f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
                 f'<option value="">Select...</option>{o}</select></div>\n')

    ctx_paras = ''.join(f'<p{" style=\"margin-top:.7rem\"" if i else ""}>{p}</p>'
                        for i, p in enumerate(s['pc_context']['paras']))
    ctx_quiz = ''
    for i, q in enumerate(s['pc_context']['quiz']):
        opts = ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(c).lower()}">'
            f'<span class="option-letter">{"ABC"[j]}</span> {t}</div>'
            for j, (t, c) in enumerate(q['opts']))
        ctx_quiz += (f'      <div class="quiz-item"><div class="quiz-question">{i+1}. {q["q"]}</div>'
                     f'<div class="quiz-options">{opts}</div></div>\n')

    grows = ''
    for i, r in enumerate(s['grammar_rows']):
        bg = 'background:var(--bg-elevated);' if i % 2 else ''
        if len(r) == 2:
            grows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                      f'<td style="padding:.6rem;font-weight:600">{r[0]}</td>'
                      f'<td style="padding:.6rem" colspan="2">{r[1]}</td></tr>')
        else:
            grows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                      f'<td style="padding:.6rem;font-weight:600">{r[0]}</td>'
                      f'<td style="padding:.6rem">{r[1]}</td>'
                      f'<td style="padding:.6rem">{r[2]}</td></tr>')

    blanks = ''
    for b in s['pc_blanks']:
        phrase = f'{b[0]}{b[1]}{b[2]}'
        blanks += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">&quot;{b[0]}'
                   f'<input class="blank-input" data-answer="{esc(b[1])}" data-hint="{esc(b[3])}" '
                   f'data-phrase="{esc(phrase)}" placeholder="___">{b[2]}&quot;</div>'
                   f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                   f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')

    order = ''
    for txt, pos in s['pc_order']:
        order += (f'        <div class="order-item" draggable="true" data-order="{pos}" '
                  f'onclick="selectOrderItem(this,\'order-l{n}\')"><span class="order-num">?</span>'
                  f'<span class="order-text">{txt}</span><span class="order-arrows">'
                  f'<button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{n}\')">&#9650;</button>'
                  f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l{n}\')">&#9660;</button>'
                  f'</span></div>\n')

    speech = ''.join(
        f'      <div class="speech-card" data-phrase="{esc(p)}">\n'
        f'        <div class="speech-phrase">{p}</div>\n'
        f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">'
        f'&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">'
        f'&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">'
        f'&#9632; Stop</button></div>\n        <div class="speech-result"></div>\n      </div>\n'
        for p in s['survival'])

    sit = ''
    for q in s['pc_exam_quiz']:
        opts = ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(c).lower()}">'
            f'<span class="option-letter">{"ABCDE"[j]}</span> {t}</div>'
            for j, (t, c) in enumerate(q['opts']))
        sit += (f'      <div class="quiz-item"><div class="quiz-question">{q["q"]}</div>'
                f'<div class="quiz-options">{opts}</div></div>\n')

    surv = ''.join(
        f'      <div class="survival-phrase"><span class="sp-num">{i+1}</span>'
        f'<span class="sp-en">{p}</span>'
        f'<button class="btn btn-listen" data-speak="{esc(p)}" '
        f'onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>\n'
        for i, p in enumerate(s['survival']))

    return f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{IMG}{s["images"][0]}?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson {n:02d} -- Pre-class</div>
      <h3>{s["title_plain"]}</h3>
      <div class="lesson-desc">{s["pc_desc"]}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read it inside a real sentence. These are the words the exam text will use.</p>
      <div class="vocab-cards">
{cards}      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with its definition in English.</p>
      <div class="match-grid" id="match-l{n}">
{rows}      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l{n}')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the passage, then answer the questions about how it is written.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:8px;padding:1rem;margin-bottom:1rem;font-size:.9rem;line-height:1.7">
        {ctx_paras}
      </div>
{ctx_quiz}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {s["grammar_tip_title"]}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{s["grammar_tip_lead"]}</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">What it does</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>{grows}</tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem">{s["grammar_insight"]}</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Write the missing word. Tap Listen to hear the full sentence.</p>
{blanks}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: {s["pc_order_title"]}</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{s["pc_order_lead"]}</p>
      <div class="order-container" id="order-l{n}">
{order}      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{n}')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read each sentence out loud. Saying the technical words is how you stop skipping them when you read.</p>
{speech}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Exam-Format Questions</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Same format as the exam. Every wrong option says something the text does not say -- in words the text never used.</p>
{sit}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record your answer. Saying the text back in your own words is the skill the exam measures.</p>
      <div class="think-card">
        <div class="think-question">{s["pc_think"]}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{n}"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson {n}</h4>
{surv}    </div>

  </div>
</div>
'''


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEMENTARES
# ─────────────────────────────────────────────────────────────────────────────
THUMBS = {
    'video': ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" '
              'stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0'
              '-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 '
              '19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 '
              '29 0 00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>'),
    'series': ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" '
               'stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/>'
               '<path d="M16 3l-4 4-4-4"/></svg>'),
    'doc': ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" '
            'stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/>'
            '<path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>'),
}


def build_complementary(s):
    n = s['n']
    out = []
    for c in s['media']:
        out.append(f'''<div class="media-card-wrapper" data-media="l{n}-{c["id"]}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb">{THUMBS[c["thumb"]]}</div>
    <div class="media-info">
      <div class="media-type">{c["type"]}</div>
      <h5>{c["title"]}</h5>
      <p>{c["desc"]}</p>
      <p class="media-tip">Tip: {c["tip"]}</p>
      <a href="{c["url"]}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">{c["cta"]} &#8599;</a>
    </div>
  </div>
</div>''')
    return '\n\n'.join(out) + '\n'


# ─────────────────────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────────────────────
STAMPS = [
    {'id': 1, 'label': 'The Ship', 'img': f'{IMG}1546883737-da9c5102ed9c?w=200&q=80'},
    {'id': 2, 'label': 'The Rules', 'img': f'{IMG}1519709042477-8de6eaf1fdc5?w=200&q=80'},
    {'id': 3, 'label': 'The Cargo', 'img': f'{IMG}1597334948330-38795f25d05d?w=200&q=80'},
    {'id': 4, 'label': 'The Report', 'img': f'{IMG}1570187671278-2370524a1197?w=200&q=80'},
    {'id': 5, 'label': 'The Exam', 'img': f'{IMG}1532528425368-31e68a9665fe?w=200&q=80'},
]


def build_config(s):
    n = s['n']
    blocks = {
        'vocab': [{
            'kind': 'matching',
            'title': 'Match each term to its meaning',
            'words': [[str(i + 1), w['w'], 'abcdefghij'[i]] for i, w in enumerate(s['vocab'])],
            'defs': [['abcdefghij'[i], w['def']] for i, w in enumerate(s['vocab'])],
        }],
        'reading': [{
            'kind': 'reading',
            'rtitle': s['reading']['rtitle'],
            'paras': s['reading']['paras'],
            'source': s['reading']['source'],
        }],
        'gist': [{'kind': 'gist', 'prompt': s['gist']['prompt'], 'choices': s['gist']['choices']}],
        'tf': [{'kind': 'tf', 'items': s['tf']}],
        'equiv': [{
            'kind': 'matching',
            'title': 'Match the plain sentence to the sentence an exam question would use',
            'hint': 'Tap a plain sentence, then tap its exam-register twin',
            'words': [[str(i + 1), p[0], 'abcdefgh'[i]] for i, p in enumerate(s['equiv'])],
            'defs': [['abcdefgh'[i], p[1]] for i, p in enumerate(s['equiv'])],
        }],
        'gap': [{'kind': 'gapfill', 'parts': s['gap']['parts'], 'bank': s['gap']['bank']}],
        'quickfire': [{'kind': 'quickfire', 'items': s['quickfire']}],
    }
    # o matching embaralha as definicoes na coluna da direita (REGRA 24)
    for key in ('vocab', 'equiv'):
        d = blocks[key][0]['defs']
        blocks[key][0]['defs'] = rotate(d, 3)

    return {
        'slug': SLUG,
        'student_name': STUDENT,
        'first_name': FIRST,
        'gender': 'f',
        'program': 'Ingl&#234;s para o PS-ASON &mdash; Marinha Mercante',
        'total_aulas': TOTAL_AULAS,
        'palette': {'accent': ACCENT, 'accent_light': ACCENT_LIGHT},
        'header': ['B2', 'Marinha Mercante', 'PS-ASON &mdash; mar&#231;o/2027', '60 min / Online'],
        'characters': {'cadet': 'ellen', 'officer': 'arthur'},
        'hub_subtitle': ('Leitura t&#233;cnica em ingl&#234;s para o exame do PS-ASON '
                         '&mdash; vocabul&#225;rio mar&#237;timo, registro formal e '
                         'equival&#234;ncia sem&#226;ntica'),
        'stamps': STAMPS,
        'lesson': {
            'n': n,
            'menu_num': f'{n:02d}',
            'menu_title': s['title_html'],
            'menu_desc': s['menu_desc'],
            'subtitle': f'Lesson {n} -- {s["title_plain"]}',
            'title_tag': f'Professor View -- {STUDENT} | Lesson {n} -- {s["title_plain"]}',
            'grammar_point': s['grammar_point'],
            'phases': s['chapters'],
            'inclass_blocks': blocks,
            'listenings': [
                {'file': f'a{n}_listening{k+1}.mp3', 'voice': ls['voice'], 'text': ls['text']}
                for k, ls in enumerate(s['listenings'])],
        },
        'hub': s['hub'],
        'molde': 'helen-mendes',
        'voices': {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'},
    }


def main():
    n = int(sys.argv[1])
    spec = json.load(open(os.path.join(HERE, 'specs', f'aula{n}.json'), encoding='utf-8'))
    spec['n'] = n
    d = os.path.join(ROOT, '_build', f'{SLUG}-aula{n}')
    os.makedirs(d, exist_ok=True)

    open(os.path.join(d, 'slides.html'), 'w', encoding='utf-8').write(build_slides(spec))
    open(os.path.join(d, 'preclass.html'), 'w', encoding='utf-8').write(build_preclass(spec))
    open(os.path.join(d, 'complementary.html'), 'w', encoding='utf-8').write(build_complementary(spec))
    json.dump(build_config(spec), open(os.path.join(d, 'config.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # planning.html so na aula 1 (hub "new")
    src = os.path.join(HERE, 'planning.html')
    if spec['hub'] == 'new' and os.path.exists(src):
        open(os.path.join(d, 'planning.html'), 'w', encoding='utf-8').write(
            open(src, encoding='utf-8').read())

    # sanidade barata, antes de o builder rodar
    sl = open(os.path.join(d, 'slides.html'), encoding='utf-8').read()
    assert sl.count('<div') == sl.count('</div>'), 'slides.html: <div> desbalanceado'
    pc = open(os.path.join(d, 'preclass.html'), encoding='utf-8').read()
    assert pc.count('<div') == pc.count('</div>'), 'preclass.html: <div> desbalanceado'
    for b in spec['pc_blanks']:
        assert b[1] in f'{b[0]}{b[1]}{b[2]}'
    assert len(spec['vocab']) == 10, 'a aula tem 10 palavras novas'
    assert len(re.findall(r'data-slide=', sl)) == 32, 'esperados 32 slides autorais'
    print(f'  ok  _build/{SLUG}-aula{n}/  ({len(sl)//1024} KB de slides)')


if __name__ == '__main__':
    main()
