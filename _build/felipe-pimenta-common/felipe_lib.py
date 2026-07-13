#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""felipe_lib.py — biblioteca de autoria das aulas do Felipe Pimenta (B2, CFO fintech).

NAO substitui o builder. Emite APENAS os arquivos de CONTEUDO que o
_build/model/build_from_model.py declara como entrada:

    slides.html   preclass.html   complementary.html   config.json

O LAYOUT/CSS/JS/audioMap continuam vindo do modelo (helen-mendes) via builder.
Aqui mora so o conteudo do perfil 360 — e as travas que impedem os dois bugs
que matam material:

  REGRA 7.1 (botao morto): NENHUM texto falavel entra no argumento string de um
  onclick. Todo texto viaja em ATRIBUTO (data-speak / data-phrase), onde o
  apostrofo e caractere comum. Assim o ingles mantem a contracao natural
  (I've, don't, it's) SEM quebrar o handler inline. O `speak_btn()` e o UNICO
  jeito de emitir botao de audio, e ele assere isso.

  REGRA 4  : as 5 etapas + sub-etapas 1.1..1.5 sao montadas por `preclass()`,
             que falha se faltar qualquer bloco.
  REGRA 24 : matching embaralhado (ordem distinta da ordem das palavras).
  REGRA 22 : `assert_no_vocab_repeat()` cruza o vocab da aula com o das anteriores.

Modelos de aula (REGRA 29):
  ODD  (impar) = PADRAO/fala : dialogo line-by-line + role-play  -> 33 slides
  EVEN (par)   = LEITURA     : ic-reading + gist + true/false    -> 34 slides
"""
import json
import os
import random
import re

# ---------------------------------------------------------------- infra

# Pool de imagens de fundo VALIDADAS (200 OK) — herdadas da aula 1 aprovada.
IMG = {
    'title':   'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80',
    'hook':    'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1400&q=80',
    'vocab':   'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80',
    'code':    'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1400&q=80',
    'context': 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1400&q=80',
    'practice': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=1400&q=80',
    'turn':    'https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=1400&q=80',
    'wrap':    'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1400&q=80',
}

VOL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
           '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
           '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

# gradientes unicos por card de vocab (REGRA: cada palavra com cor propria)
GRADIENTS = [
    ('#0e7490', '#22d3ee'), ('#7c3aed', '#a78bfa'), ('#b45309', '#f59e0b'),
    ('#15803d', '#4ade80'), ('#1d4ed8', '#60a5fa'), ('#9f1239', '#fb7185'),
    ('#c2410c', '#fb923c'), ('#0d9488', '#2dd4bf'), ('#4338ca', '#818cf8'),
    ('#ca8a04', '#fde047'), ('#0369a1', '#38bdf8'), ('#374151', '#9ca3af'),
]

# icones SVG genericos (Lucide style) — 12, um por card
ICONS = [
    '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18"/><path d="M8 3v4M16 3v4"/>',
    '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h5M9.5 14.5h5"/>',
    '<path d="M3 21h18"/><path d="M6 21V8l6-4 6 4v13"/><path d="M10 21v-6h4v6"/>',
    '<path d="M3 12h18"/><path d="M7 8l-4 4 4 4"/><path d="M17 8l4 4-4 4"/>',
    '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20v-1a6 6 0 0112 0v1"/><path d="M15 20v-1a5 5 0 016-4.5"/>',
    '<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4M5 5l3 3M16 16l3 3M19 5l-3 3M8 16l-3 3"/>',
    '<circle cx="12" cy="12" r="3"/><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>',
    '<path d="M4 4h16v6H4z"/><path d="M4 14h16v6H4z"/><path d="M8 10v4M16 10v4"/>',
    '<path d="M12 20V10"/><path d="M8 14l4-4 4 4"/><rect x="4" y="3" width="16" height="4" rx="1"/>',
    '<path d="M4 19V5a2 2 0 012-2h9l5 5v11a2 2 0 01-2 2H6a2 2 0 01-2-2z"/><path d="M14 3v5h5"/><path d="M8 13h8M8 17h5"/>',
]

SPEAKABLE = []          # tudo que vira MP3 (so p/ relatorio; o builder reextrai do HTML)


def _no_dq(text, where):
    assert '"' not in text, f'aspas duplas quebram o atributo ({where}): {text!r}'


def speak_btn(text, cls='audio-btn-sm', label='Listen', stop_prop=False):
    """UNICO emissor de botao de audio. O texto vai em data-speak (ATRIBUTO).

    REGRA 7.1: jamais dentro da string do onclick. Em atributo o apostrofo e
    caractere comum — nao ha string JS para fechar, nao ha botao morto.
    """
    _no_dq(text, 'speak_btn')
    SPEAKABLE.append(text)
    pre = 'event.stopPropagation();' if stop_prop else ''
    icon = VOL_SVG + ' ' if label == 'Listen' else ''
    return (f'<button class="{cls}" data-speak="{text}" '
            f'onclick="{pre}speakText(this.dataset.speak,this)">{icon}{label}</button>')


def speak_inline(text):
    """Botao de audio inline do dialogo (icone so)."""
    _no_dq(text, 'speak_inline')
    SPEAKABLE.append(text)
    return (f'<span class="audio-inline" data-speak="{text}" '
            f'onclick="speakText(this.dataset.speak,this)">{VOL_SVG}</span>')


# ---------------------------------------------------------------- slides

def _slide(n, phase, kind, teacher, inner, bg=None):
    _no_dq(teacher, f'data-teacher slide {n}')
    style = ''
    if bg:
        style = (f' style="background-image:linear-gradient(rgba(15,15,30,.78),rgba(15,15,30,.9)),'
                 f"url('{bg}');background-size:cover;background-position:center\"")
    return (f'<!-- ===== SLIDE {n} ===== -->\n'
            f'<div class="slide {kind}" data-slide="{n}" data-phase="{phase}" '
            f'data-teacher="{teacher}"{style}>\n{inner}\n</div>\n')


def s_title(n, phase, teacher, label, h1_a, h1_b, sub):
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h1 class="slide-heading" style="font-size:2.5rem;color:#fff">{h1_a} '
             f'<span class="accent">{h1_b}</span></h1>\n'
             f'    <p style="color:rgba(255,255,255,.82);font-size:1.1rem;margin-top:1rem">{sub}</p>\n'
             f'  </div>')
    return _slide(n, phase, 'slide-image active', teacher, inner, IMG['title'])


def s_chapter(n, phase, teacher, label, h_a, h_b, sub, img):
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{h_a} '
             f'<span class="accent">{h_b}</span></h2>\n'
             + (f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{sub}</p>\n' if sub else '')
             + f'  </div>')
    return _slide(n, phase, 'slide-image', teacher, inner, img)


def s_hook(n, phase, teacher, label, h_a, h_b, sub):
    """Warm-up. REGRA 27A: zero saudacao scriptada — vai direto ao conteudo."""
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:1rem;max-width:580px;'
             f'margin-left:auto;margin-right:auto">{sub}</p>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner, IMG['hook'])


def s_cards3(n, phase, teacher, label, h_a, h_b, cards, foot=''):
    """Slide de 3 cards (reframe / goals)."""
    cs = ''.join(
        '<div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;'
        f'padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">{t}</p>'
        f'<p style="font-size:.78rem;color:var(--text-dim)">{d}</p></div>' for t, d in cards)
    foot_html = (f'    <p style="text-align:center;font-size:.88rem;color:var(--text-dim);margin-top:1.2rem;'
                 f'max-width:560px;margin-left:auto;margin-right:auto">{foot}</p>\n') if foot else ''
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));'
             f'gap:.8rem;max-width:680px;margin:1.5rem auto 0">{cs}</div>\n{foot_html}  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_vocab(n, phase, teacher, h_b, vocab, grid_id, offset):
    """Reveal cards (REGRA 27E: revealVocab do shell faz toggle)."""
    cards = []
    for i, (w, d, _pt, ex) in enumerate(vocab):
        g1, g2 = GRADIENTS[(offset + i) % len(GRADIENTS)]
        ico = ICONS[(offset + i) % len(ICONS)]
        _no_dq(d, 'vocab def')
        _no_dq(ex, 'vocab example')
        cards.append(
            '      <div class="vocab-card" onclick="revealVocab(this)">\n'
            f'        <div class="card-icon" style="background:linear-gradient(135deg,{g1},{g2})">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="#fff">{ico}</svg>'
            f'<div class="card-hint">{d}</div></div>\n'
            f'        <div class="card-body"><div class="card-word">{w}</div>'
            f'<div class="card-def">{d}</div>'
            f'<div class="card-example">"{ex}"</div>'
            f'<div class="card-audio">{speak_btn(w, stop_prop=True)}</div></div>\n'
            '      </div>')
    lo, hi = offset + 1, offset + len(vocab)
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Vocabulary</div>\n'
             f'    <h2 class="slide-heading">Words <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
             f'<span id="vocabCount{grid_id}">0 / {len(vocab)} words revealed</span></p>\n'
             f'    <div class="vocab-grid" id="vocabGrid{grid_id}">\n' + '\n'.join(cards) +
             f'\n    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_pron(n, phase, teacher, words):
    rows = ''.join(
        '      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
        'padding:1rem;display:flex;justify-content:space-between;align-items:center">'
        f'<span style="font-size:1.1rem;font-weight:600">{w}</span>{speak_btn(w)}</div>\n'
        for w in words)
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Pronunciation</div>\n'
             f'    <h2 class="slide-heading">Say It <span class="accent">Clearly</span></h2>\n'
             f'    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:500px;margin:1.2rem auto 0">\n'
             + rows + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_fill(n, phase, teacher, label, h_a, h_b, sub, items):
    """fill-grid clicavel (revealFill do shell). items = [(pre, answer, post)]"""
    its = ''.join(
        '      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">'
        f'"{pre}<span class="fill-blank">___</span><span class="fill-answer">{ans}</span>{post}"'
        '</div></div>\n' for pre, ans, post in items)
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">{sub}</p>\n'
             f'    <div class="fill-grid">\n' + its + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_discovery(n, phase, teacher, examples, question, rule_rows, rule_note, rule_id):
    """Grammar discovery (REGRA: regra NUNCA vem primeiro). examples = [(html, speak)]"""
    exs = ''.join(
        '      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
        'padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
        f'<p style="font-size:.92rem">{h}</p>{speak_btn(sp)}</div>\n' for h, sp in examples)
    rows = ''.join(
        f'          <tr style="{"background:var(--bg-elevated)" if i % 2 else "border-bottom:1px solid var(--border)"}">'
        f'<td style="padding:.5rem;font-weight:600">{a}</td><td style="padding:.5rem">{b}</td>'
        f'<td style="padding:.5rem">{c}</td></tr>\n' for i, (a, b, c) in enumerate(rule_rows))
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Grammar Discovery</div>\n'
             f'    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>\n'
             f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1rem auto 0">\n'
             + exs +
             f'    </div>\n'
             f'    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">{question}</p>\n'
             f'    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);'
             f'color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;'
             f'cursor:pointer" onclick="var t=document.getElementById(\'{rule_id}\');'
             f"t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'\">Reveal the Rule</button>\n"
             f'    <div id="{rule_id}" style="display:none;max-width:620px;margin:1rem auto 0;overflow-x:auto">\n'
             f'      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);'
             f'border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
             f'        <thead><tr style="background:var(--accent);color:#fff">'
             f'<th style="padding:.6rem;text-align:left">Form</th>'
             f'<th style="padding:.6rem;text-align:left">Use</th>'
             f'<th style="padding:.6rem;text-align:left">Example</th></tr></thead>\n'
             f'        <tbody>\n' + rows + '        </tbody>\n      </table>\n'
             f'      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">{rule_note}</p>\n'
             f'    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


X_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><circle cx="12" cy="12" r="10"/>'
         '<line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>')
V_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#16a34a">'
         '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>')


def s_mistake(n, phase, teacher, pairs, note):
    """Common Mistake. slide-light; texto DIRETO no div (nunca <p>/<strong> dentro
    do .mistake-item — o display:flex espalha inline)."""
    items = ''
    for wrong, right in pairs:
        items += (f'      <div class="mistake-item mistake-wrong">\n'
                  f'        <div class="mistake-icon">{X_SVG}</div>\n        "{wrong}"\n      </div>\n'
                  f'      <div class="mistake-item mistake-right">\n'
                  f'        <div class="mistake-icon">{V_SVG}</div>\n        "{right}"\n      </div>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Common Mistake</div>\n'
             f'    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>\n'
             f'    <div class="mistake-card">\n' + items + '    </div>\n'
             f'    <p style="text-align:center;margin-top:2rem;font-size:.9rem;color:var(--text-dim)">{note}</p>\n'
             f'  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_dialogue(n, phase, teacher, h_a, h_b, lines):
    """Dialogo line-by-line. lines = [(char, initial, voice, html, speak)]"""
    ls = ''
    for i, (char, ini, voice, body, speak) in enumerate(lines, 1):
        vis = ' visible' if i == 1 else ''
        ls += (f'      <div class="dialogue-line{vis}" data-line="{i}" data-voice="{voice}">'
               f'<div class="dialogue-avatar {char}">{ini}</div>'
               f'<div class="dialogue-bubble {char}-bubble">{body} {speak_inline(speak)}</div></div>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Dialogue</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div class="dialogue-box" id="dialogueBox">\n' + ls + '    </div>\n'
             f'    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" '
             f'style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;'
             f'border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">'
             f'Next Line</button>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def _comp_qs(qs):
    return ''.join(f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">{i}. {q}</div>'
                   f'<div class="q-answer">{a}</div></div>\n' for i, (q, a) in enumerate(qs, 1))


def s_comprehension(n, phase, teacher, h_a, h_b, qs):
    """REGRA 27F: pergunta sobre o INTERLOCUTOR, nunca sobre o proprio aluno."""
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Comprehension</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div style="display:flex;flex-direction:column;gap:1rem;max-width:520px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_listening(n, phase, teacher, idx, label, h_a, h_b, sub, mp3, slug, qs):
    """Listening sound-first, MP3 unico + player completo do shell (mpToggle/mpSeek/
    mpSkip/mpSpeed). Perguntas so aparecem quando o audio termina."""
    pid = f'mp-listen{idx}'
    wf = f'waveform{idx}'
    qid = f'listening{idx}Qs'
    bars = '<div class="bar"></div>' * 20
    spd = ''.join(
        f'<button class="lp-speed-btn{" lp-speed-active" if s == 1 else ""}" '
        f'onclick="mpSpeed(\'{pid}\',{s},this)" style="background:'
        + ('var(--accent);border:1px solid var(--accent);color:#fff' if s == 1
           else 'transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82)')
        + f';border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">{s}x</button>'
        for s in (0.5, 0.75, 1, 1.25))
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{sub}</p>\n'
             f'    <div class="waveform waveform-paused" id="{wf}">{bars}</div>\n'
             f'    <div class="mock-player" id="{pid}" data-src="/audio/{slug}/{mp3}" data-waveform="{wf}" '
             f'data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">\n'
             f'      <div class="lp-seekbar" onclick="mpSeek(event,\'{pid}\')" style="width:100%;height:6px;'
             f'background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative">'
             f'<div class="lp-progress" id="progress-{pid}" style="width:0%;height:100%;'
             f'background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>\n'
             f'      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem">'
             f'<span id="time-current-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span>'
             f'<span id="time-total-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>\n'
             f'      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">\n'
             f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',-5)" aria-label="Back 5 seconds" '
             f'style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;'
             f'width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>\n'
             f'        <button class="lp-btn lp-play" id="play-{pid}" onclick="mpToggle(\'{pid}\')" '
             f'aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%;'
             f'width:48px;height:48px;cursor:pointer">'
             f'<svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18">'
             f'<polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
             f'<svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none">'
             f'<rect x="6" y="4" width="4" height="16" fill="currentColor"/>'
             f'<rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>\n'
             f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',5)" aria-label="Forward 5 seconds" '
             f'style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;'
             f'width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>\n'
             f'      </div>\n'
             f'      <div style="display:flex;gap:.4rem;justify-content:center">{spd}</div>\n'
             f'    </div>\n'
             f'    <div class="comp-questions" id="{qid}" style="display:none;max-width:520px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def s_error(n, phase, teacher, items):
    """Spot the error (revealError do shell)."""
    cards = ''.join(
        f'      <div class="error-card" onclick="revealError(this)">'
        f'<div class="error-sentence">"{w}"</div><div class="error-fix">"{r}"</div></div>\n'
        for w, r in items)
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Detective</div>\n'
             f'    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>\n'
             f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
             f'<span id="errorScore">0 / {len(items)} errors found</span></p>\n'
             f'    <div class="error-grid" id="errorGrid">\n' + cards + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_artifact(n, phase, teacher, label, h_a, h_b, brand, brand_sub, rows, qs):
    """Artefato REAL em HTML/CSS (nunca imagem), com o nome do aluno."""
    rs = ''
    for i, (k, v) in enumerate(rows):
        last = ' ' if i == len(rows) - 1 else ';border-bottom:1px solid var(--border);padding-bottom:.6rem;margin-bottom:.6rem'
        rs += (f'        <div style="display:flex;justify-content:space-between{last}">'
               f'<span style="font-size:.78rem;color:var(--text-dim)">{k}</span>'
               f'<span style="font-size:.85rem;font-weight:600">{v}</span></div>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div style="max-width:520px;margin:1.2rem auto 0;background:var(--bg-card);'
             f'border:1px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,.08)">\n'
             f'      <div style="background:var(--accent);color:#fff;padding:.9rem 1.2rem;display:flex;'
             f'justify-content:space-between;align-items:center">'
             f'<span style="font-weight:700;font-size:.9rem;letter-spacing:.5px">{brand}</span>'
             f'<span style="font-size:.72rem;opacity:.85">{brand_sub}</span></div>\n'
             f'      <div style="padding:1.2rem">\n' + rs + '      </div>\n    </div>\n'
             f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:520px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_quickfire(n, phase, teacher, h_a, h_b):
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Quick Fire</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <!--IC-BLOCKS:quickfire-->\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_building(n, phase, teacher, items):
    """Sentence building — gabarito ESCONDIDO ate o clique (toggle, REGRA 27E)."""
    its = ''.join(
        f'      <div class="oral-item" onclick="this.classList.toggle(\'revealed\')">'
        f'<div class="oral-situation">{i}. {cue}</div>'
        f'<div class="oral-model">"{model}"</div></div>\n'
        for i, (cue, model) in enumerate(items, 1))
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Build</div>\n'
             f'    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>\n'
             f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
             f'Say the full sentence, then click to compare</p>\n'
             f'    <div class="oral-grid">\n' + its + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_roleplay(n, phase, teacher, h_a, h_b, scenario, keywords, tint='.08'):
    """Role-play. Gradiente CSS + chips (NUNCA foto). keywords=[] => free practice."""
    if keywords:
        chips = ''.join(
            '<span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;'
            f'padding:.3rem .7rem;font-size:.8rem">{k}</span>' for k in keywords)
        kw = ('      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keywords:</p>\n'
              f'      <div style="display:flex;flex-wrap:wrap;gap:.4rem">{chips}</div>\n')
    else:
        kw = ('      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">'
              'No keywords. The floor is yours.</p>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">Role-Play</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div class="roleplay-body" style="max-width:520px;margin:1rem auto 0;'
             f'background:linear-gradient(135deg,rgba(49,46,129,{tint}),rgba(49,46,129,.02));'
             f'border:1px solid var(--accent);border-radius:12px;padding:1.5rem">\n'
             f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem">'
             f'<strong>Scenario:</strong> {scenario}</p>\n' + kw + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_survival(n, phase, teacher, h_a, h_b, phrases):
    rows = ''.join(
        '      <div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;'
        'padding:.9rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
        f'<span style="font-size:.92rem;color:#fff">{p}</span>{speak_btn(p)}</div>\n' for p in phrases)
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">Survival Card</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:640px;margin:1.2rem auto 0;'
             f'text-align:left">\n' + rows + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


CHECK_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
             '<polyline points="20 6 9 17 4 12"/></svg>')


def s_checklist(n, phase, teacher, lesson_n, items):
    """5 checks -> inclass_done no Supabase (REGRA 28)."""
    assert len(items) == 5, 'o checklist DEVE ter exatamente 5 itens (REGRA 28)'
    its = ''.join(f'      <div class="check-item" onclick="toggleCheck(this)">'
                  f'<div class="check-box">{CHECK_SVG}</div>{t}</div>\n' for t in items)
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">Self-Assessment</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">What I Can Do <span class="accent">Now</span></h2>\n'
             f'    <div class="check-grid" id="checklist-{lesson_n}" style="max-width:560px;margin:1.2rem auto 0;'
             f'display:flex;flex-direction:column;gap:.5rem;text-align:left">\n' + its + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def s_complete(n, phase, teacher, lesson_n, badge, line, next_title):
    inner = (f'  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">Lesson Complete</div>\n'
             f'    <div class="badge-card">\n      <div class="badge-icon">\n'
             f'        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             f'stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/>'
             f'</svg></div>\n'
             f'        <div class="sparkles">' + '<div class="sparkle"></div>' * 6 + '</div>\n      </div>\n'
             f'      <h2 class="slide-heading" style="color:#fff">{badge} <span class="accent">Earned!</span></h2>\n'
             f'      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">{line}</p>\n'
             f'      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">'
             f'Lesson {lesson_n} -- Complete.</p>\n'
             f'      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">'
             f'Next lesson: {next_title}</p>\n    </div>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def s_blocks(n, phase, teacher, label, h_a, h_b, keys, sub=''):
    """Slide generico de blocos B2 (reading / gist / tf / guiding)."""
    ph = '\n'.join(f'    <!--IC-BLOCKS:{k}-->' for k in keys)
    sub_html = (f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">{sub}</p>\n'
                if sub else '')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             + sub_html + ph + '\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


# ---------------------------------------------------------------- Pre-class (REGRA 4)

def preclass(spec):
    """Monta o accordion ex-lesson-N com as 5 etapas + sub-etapas 1.1..1.5 (REGRA 4).
    Falha alto se qualquer bloco obrigatorio faltar."""
    n = spec['n']
    v = spec['vocab']
    for key in ('vocab', 'blanks', 'speech', 'order', 'context_text', 'context_quiz',
                'tip_title', 'tip_rows', 'tip_note', 'quiz', 'think', 'order_intro'):
        assert spec.get(key), f'REGRA 4: aula {n} sem "{key}"'
    assert len(spec['speech']) == 5, 'survival card = 5 frases (REGRA 16)'

    rnd = random.Random(100 + n)
    defs = [d for _, d, _, _ in v]

    # 1.1 vocab cards
    cards = '\n'.join(
        '        <div class="vocab-card-pc"><div class="vocab-card-content">'
        f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
        f'<span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{d} ({pt})</span></div>'
        f'<div class="vocab-card-example">"{ex}"</div></div>'
        f'{speak_btn(w, cls="audio-btn")}</div>' for w, d, pt, ex in v)

    # 1.2 matching — REGRA 24: ordem SEMPRE diferente da ordem das palavras
    rows = []
    for w, d, _, _ in v:
        opts = defs[:]
        while True:
            rnd.shuffle(opts)
            if opts != defs:
                break
        o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
        rows.append(f'        <div class="match-row" data-answer="{d}">'
                    f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
                    f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
                    f'<option value="">Select...</option>{o}</select></div>')
    match_rows = '\n'.join(rows)

    # 1.3 grammar in context
    ctx_quiz = '\n'.join(
        '      <div class="quiz-item"><div class="quiz-question">%d. %s</div><div class="quiz-options">%s</div></div>'
        % (i, q, ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
            f'<span class="option-letter">{chr(65 + j)}</span> {opt}</div>'
            for j, (opt, ok) in enumerate(opts)))
        for i, (q, opts) in enumerate(spec['context_quiz'], 1))

    # 1.4 grammar tip (bilingue)
    tip_rows = '\n'.join(
        f'          <tr style="{"border-bottom:1px solid var(--border);background:var(--bg-elevated)" if i % 2 else "border-bottom:1px solid var(--border)"}">'
        f'<td style="padding:.6rem;font-weight:600">{a}</td><td style="padding:.6rem">{b}</td>'
        f'<td style="padding:.6rem">{c}</td></tr>'
        for i, (a, b, c) in enumerate(spec['tip_rows']))

    # 1.5 fill in the blank
    fills = []
    for pre, ans, hint, phrase, post in spec['blanks']:
        _no_dq(phrase, 'blank phrase')
        SPEAKABLE.append(phrase)
        fills.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre} '
            f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
            f'data-phrase="{phrase}" placeholder="___"> {post}"</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    fill_items = '\n'.join(fills)

    # 2 ordering
    oid = f'order-l{n}'
    order_items = '\n'.join(
        f'        <div class="order-item" draggable="true" data-order="{o}" '
        f'onclick="selectOrderItem(this,\'{oid}\')"><span class="order-num">?</span>'
        f'<span class="order-text">{t}</span><span class="order-arrows">'
        f'<button class="arrow-btn" onclick="moveItem(this,-1,\'{oid}\')">&#9650;</button>'
        f'<button class="arrow-btn" onclick="moveItem(this,1,\'{oid}\')">&#9660;</button>'
        f'</span></div>' for o, t in spec['order'])

    # 3 pronunciation
    sp = []
    for phrase, pt in spec['speech']:
        _no_dq(phrase, 'speech phrase')
        SPEAKABLE.append(phrase)
        sp.append(
            f'      <div class="speech-card" data-phrase="{phrase}">\n'
            f'        <div class="speech-phrase">{phrase}</div>\n'
            f'        <div class="speech-translation">{pt}</div>\n'
            f'        <div class="speech-controls">'
            f'<button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            f'<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button>'
            f'</div>\n        <div class="speech-result"></div>\n      </div>')
    speech_cards = '\n'.join(sp)

    # 4 situational quiz
    sit_quiz = '\n'.join(
        '      <div class="quiz-item"><div class="quiz-question">%s</div><div class="quiz-options">%s</div></div>'
        % (q, ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
            f'<span class="option-letter">{chr(65 + j)}</span> {opt}</div>'
            for j, (opt, ok) in enumerate(opts)))
        for q, opts in spec['quiz'])

    # survival
    survival = '\n'.join(
        f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
        f'<span class="sp-en">{en}</span><span class="sp-pt">{pt}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
        for i, (en, pt) in enumerate(spec['speech'], 1))

    html = f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{spec['hub_img']}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula {n:02d} -- Pre-class</div>
      <h3>{spec['title']}</h3>
      <div class="lesson-desc">{spec['desc']}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{spec['vocab_intro']}</p>
      <div class="vocab-cards">
{cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada termo com a defini&#231;&#227;o correta.</p>
      <div class="match-grid" id="match-l{n}">
{match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>{spec['context_text']}</p>
      </div>
{ctx_quiz}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {spec['tip_title']}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{spec['tip_intro']}</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
{tip_rows}
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem">{spec['tip_note']}</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: {spec['order_title']}</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{spec['order_intro']}</p>
      <div class="order-container" id="{oid}">
{order_items}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('{oid}')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{spec['speech_intro']}</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada momento real da sua rotina de CFO.</p>
{sit_quiz}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesmo respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada &mdash; fale por 2 a 3 minutos, sem script.</p>
      <div class="think-card">
        <div class="think-question">{spec['think']}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{n}"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson {n}</h4>
{survival}
    </div>

  </div>
</div>
'''
    for must in ('Grammar in Context', 'Grammar Tip', 'vocab-card-pc', 'match-row',
                 'blank-input', 'speech-card', 'quiz-item', 'think-card', 'order-item'):
        assert must in html, f'REGRA 4/11: bloco obrigatorio ausente no Pre-class: {must}'
    return html


# ---------------------------------------------------------------- Complementares

MEDIA_SVG = {
    'Series': ('<rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><path d="M7 2v20"/>'
               '<path d="M17 2v20"/><path d="M2 12h20"/><path d="M2 7h5"/><path d="M2 17h5"/>'
               '<path d="M17 17h5"/><path d="M17 7h5"/>'),
    'Podcast': ('<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/>'
                '<path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>'
                '<line x1="8" y1="23" x2="16" y2="23"/>'),
    'YouTube': ('<path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 '
                '00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19c1.72.46 8.6.46 8.6.46s6.88 '
                '0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.33z"/>'
                '<polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/>'),
}


def complementary(spec):
    """Bloco de Complementares da AULA N (modo snippets). 3 recomendacoes (REGRA 17)."""
    n = spec['n']
    items = spec['media']
    assert len(items) == 3, 'REGRA 17: exatamente 3 recomendacoes por aula'
    out = [f'\n<h4 style="font-size:.95rem;margin-bottom:.8rem">Aula {n} -- {spec["short_title"]}</h4>\n']
    for kind, mid, title, desc, tip, link in items:
        svg = MEDIA_SVG[kind]
        out.append(f'''
<div class="media-card-wrapper" data-media="l{n}-{mid}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2">{svg}</svg></div>
    <div class="media-info">
      <div class="media-type">{kind}</div>
      <h5>{title}</h5>
      <p>{desc}</p>
      <p class="media-tip">{tip}</p>
      <a href="{link}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Open &#8599;</a>
    </div>
  </div>
</div>
''')
    return ''.join(out)


# ---------------------------------------------------------------- config

BASE_CONFIG = {
    "slug": "felipe-pimenta",
    "student_name": "Felipe Pimenta",
    "first_name": "Felipe",
    "gender": "m",
    "program": "Business English -- Finance &amp; Career",
    "total_aulas": 16,
    "palette": {"accent": "#312E81", "accent_light": "#5B54C7"},
    "header": [
        "B2 (Intermedi&#225;rio-Superior)",
        "S&#227;o Paulo, SP",
        "CFO &mdash; Fintech",
        "60 min &middot; Online",
    ],
    "hub_subtitle": "Business English para Finan&#231;as Corporativas, Entrevistas e Carreira Internacional",
    # stamps do header — MESMOS 5 da aula 1 (o hub ja existe; em modo "snippets" o
    # builder so precisa deles para montar o header do standalone).
    "stamps": [
        {"id": 1, "label": "Diagnostic",
         "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80"},
        {"id": 2, "label": "Hindsight",
         "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=200&q=80"},
        {"id": 3, "label": "Accountability",
         "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80"},
        {"id": 4, "label": "Difficult Talks",
         "img": "https://images.unsplash.com/photo-1521791136064-7986c2920216?w=200&q=80"},
        {"id": 5, "label": "The Boardroom",
         "img": "https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=200&q=80"},
    ],
}


def config(spec, slide_count):
    c = dict(BASE_CONFIG)
    c['characters'] = spec['characters']
    c['lesson'] = {
        'n': spec['n'],
        'menu_num': f"{spec['n']:02d}",
        'menu_title': spec['title'],
        'menu_desc': f"{spec['menu_desc']} -- {slide_count} slides",
        'subtitle': f"Aula {spec['n']} -- {spec['short_title']}",
        'title_tag': f"Professor View -- Felipe Pimenta | Aula {spec['n']} -- {spec['short_title']}",
        'phases': spec['phases'],
        'listenings': spec['listenings'],
        'inclass_blocks': spec['inclass_blocks'],
    }
    c['hub'] = 'snippets'
    return c


# ---------------------------------------------------------------- REGRA 22

def assert_no_vocab_repeat(n, vocab, root):
    """REGRA 22: nenhuma palavra ja ensinada como vocab card em aula anterior."""
    seen = {}
    hub = os.path.join(root, 'public', 'professor', 'felipe-pimenta.html')
    if os.path.exists(hub):
        c = open(hub, encoding='utf-8').read()
        ids = [(m.start(), int(m.group(1))) for m in re.finditer(r'id="ex-lesson-(\d+)"', c)]
        for i, (pos, ln) in enumerate(ids):
            if ln >= n:
                continue
            end = ids[i + 1][0] if i + 1 < len(ids) else len(c)
            for w in re.findall(r'vocab-card-word[^>]*>([^<]+)<', c[pos:end]):
                seen[w.strip().lower()] = ln
    dupes = [(w, seen[w.lower()]) for w, _, _, _ in vocab if w.lower() in seen]
    assert not dupes, f'REGRA 22 violada — ja ensinadas: {dupes}'
    return len(seen)


# ---------------------------------------------------------------- escrita

def emit(spec, slides_html, root, outdir):
    os.makedirs(outdir, exist_ok=True)
    n = spec['n']
    count = len(re.findall(r'<div class="slide ', slides_html))
    assert count >= 25, f'REGRA 11.7: minimo 25 slides para 60 min (tem {count})'

    assert_no_vocab_repeat(n, spec['vocab'], root)

    open(os.path.join(outdir, 'slides.html'), 'w', encoding='utf-8').write(slides_html)
    open(os.path.join(outdir, 'preclass.html'), 'w', encoding='utf-8').write(preclass(spec))
    open(os.path.join(outdir, 'complementary.html'), 'w', encoding='utf-8').write(complementary(spec))
    with open(os.path.join(outdir, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config(spec, count), f, ensure_ascii=False, indent=2)

    # ---- trava final REGRA 7.1: nenhum texto dentro da string de um onclick ----
    for fn in ('slides.html', 'preclass.html', 'complementary.html'):
        blob = open(os.path.join(outdir, fn), encoding='utf-8').read()
        bad = re.findall(r"speakText\('[^']*'", blob)
        assert not bad, f'REGRA 7.1 violada em {fn}: texto dentro do onclick: {bad[:2]}'
    print(f'aula {n}: {count} slides, {len(spec["vocab"])} vocab, '
          f'{len(set(SPEAKABLE))} frases falaveis')
    return count
