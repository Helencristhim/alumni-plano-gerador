#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dias_lib.py — biblioteca de autoria das aulas do Felipe de Araujo Dias (B1, Diretor
de Suprimentos na Riachuelo).

NAO substitui o builder. Emite APENAS os arquivos de CONTEUDO que o
_build/model/build_from_model.py declara como entrada:

    slides.html   preclass.html   complementary.html   config.json

O LAYOUT/CSS/JS/audioMap continuam vindo do modelo (helen-mendes) via builder. Aqui
mora so o conteudo do perfil 360 — e as travas que impedem os bugs que matam material:

  REGRA 7.1 (botao morto): NENHUM texto falavel entra no argumento string de um
            onclick. Todo texto viaja em ATRIBUTO (data-speak / data-phrase).
  REGRA 13 : B1 => ZERO portugues na tela do aluno. Portugues so em data-teacher e
            no Planejamento. `_no_pt()` varre o que vai para a tela.
  REGRA 4  : as 5 etapas + sub-etapas 1.1..1.5 sao montadas por `preclass()`.
  REGRA 24 : matching embaralhado (ordem distinta da ordem das palavras).
  REGRA 16 : survival card = 5 frases, sem .sp-pt (B1).

Modelos de aula (REGRA 29):
  ODD  (impar) = PADRAO/fala : dialogo line-by-line + 3 role-plays
  EVEN (par)   = LEITURA     : ic-reading + gist + true/false (+ dialogo curto)
"""
import json
import os
import random
import re

# ---------------------------------------------------------------- infra

SPEAKABLE = []   # so p/ relatorio; o builder reextrai as frases do HTML

VOL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
           '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
           '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

GRADIENTS = [
    ('#0a4d68', '#3d9dc4'), ('#b45309', '#f59e0b'), ('#15803d', '#4ade80'),
    ('#0e7490', '#22d3ee'), ('#7c3aed', '#a78bfa'), ('#b91c1c', '#f87171'),
    ('#0f766e', '#5eead4'), ('#9333ea', '#c084fc'), ('#1d4ed8', '#60a5fa'),
    ('#c2410c', '#fb923c'), ('#0369a1', '#38bdf8'), ('#4338ca', '#818cf8'),
]

ICONS = [
    '<rect x="1" y="3" width="15" height="13"/><path d="M16 8h4l3 3v5h-7z"/>'
    '<circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
    '<path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 '
    '001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/><path d="M3.27 6.96L12 12.01l8.73-5.05"/>'
    '<path d="M12 22.08V12"/>',
    '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    '<path d="M4 19V5a2 2 0 012-2h9l5 5v11a2 2 0 01-2 2H6a2 2 0 01-2-2z"/>'
    '<path d="M14 3v5h5"/><path d="M8 13h8M8 17h5"/>',
    '<path d="M3 21h18"/><path d="M5 21V7l8-4v18"/><path d="M19 21V11l-6-4"/>',
    '<circle cx="12" cy="12" r="3"/><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>',
    '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    '<path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>'
    '<path d="M22 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>',
    '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18"/><path d="M8 3v4M16 3v4"/>',
    '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    '<path d="M3 12h18"/><path d="M7 8l-4 4 4 4"/><path d="M17 8l4 4-4 4"/>',
    '<path d="M12 20V10"/><path d="M8 14l4-4 4 4"/><rect x="4" y="3" width="16" height="4" rx="1"/>',
]

# ---- REGRA 13: B1 = zero portugues na tela. Trava simples e barulhenta. -----------
PT_WORDS = re.compile(
    r'\b(voc[eê]|n[aã]o|com|para|pelo|pela|uma|dos|das|que|ele|ela|isso|aqui|ent[aã]o|'
    r'muito|mais|sobre|quando|porque|tamb[eé]m|fazer|dizer|frase|palavra|aula|professor|'
    r'aluno|exerc[ií]cio|resposta|pergunta|traduza|escolha|complete|ou[çc]a|leia|escreva)\b',
    re.I)


def _no_dq(text, where):
    assert '"' not in text, f'aspas duplas quebram o atributo ({where}): {text!r}'


def _no_pt(text, where):
    """REGRA 13 — tela do aluno em B1 nao tem portugues."""
    m = PT_WORDS.search(re.sub(r'<[^>]+>', ' ', text))
    assert not m, f'REGRA 13 (B1 = zero portugues) em {where}: {m.group(0)!r} -> {text[:90]!r}'


def speak_btn(text, cls='audio-btn-sm', label='Listen', stop_prop=False):
    """UNICO emissor de botao de audio. O texto vai em data-speak (ATRIBUTO).
    REGRA 7.1: jamais dentro da string do onclick."""
    _no_dq(text, 'speak_btn')
    SPEAKABLE.append(text)
    pre = 'event.stopPropagation();' if stop_prop else ''
    icon = VOL_SVG + ' ' if label == 'Listen' else ''
    return (f'<button class="{cls}" data-speak="{text}" '
            f'onclick="{pre}speakText(this.dataset.speak,this)">{icon}{label}</button>')


# ---------------------------------------------------------------- slides

def _slide(n, phase, kind, teacher, inner, bg=None):
    _no_dq(teacher, f'data-teacher slide {n}')
    style = ''
    if bg:
        style = (' style="background-image:linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88)),'
                 f"url('{bg}');background-size:cover;background-position:center\"")
    return (f'<!-- ========== SLIDE {n} ========== -->\n'
            f'<div class="slide {kind}" data-slide="{n}" data-phase="{phase}" '
            f'data-teacher="{teacher}"{style}>\n{inner}\n</div>\n')


def s_title(n, teacher, label, h_a, h_b, sub, img):
    _no_pt(h_a + h_b + sub, f'slide {n}')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading" style="font-size:2.3rem;color:#fff">{h_a} '
             f'<span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:.6rem">{sub}</p>\n'
             '  </div>')
    return _slide(n, 1, 'slide-image active', teacher, inner, img)


def s_chapter(n, phase, teacher, label, h_a, h_b, sub, img):
    _no_pt(h_a + h_b + sub, f'slide {n}')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             f'    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{h_a} '
             f'<span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{sub}</p>\n'
             '  </div>')
    return _slide(n, phase, 'slide-image', teacher, inner, img)


def s_warmup(n, teacher, h_a, h_b, body, prompt):
    """REGRA 27A: zero saudacao scriptada. REGRA 20: callback da aula anterior."""
    _no_pt(h_a + h_b + body + prompt, f'slide {n}')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             '    <div class="chapter-label">Warm-Up</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin:1rem auto 0;'
             f'max-width:560px">{body}</p>\n'
             f'    <p style="color:var(--accent-light);font-size:.95rem;margin-top:1.4rem">{prompt}</p>\n'
             '  </div>')
    return _slide(n, 1, 'slide-dark', teacher, inner)


def s_agenda(n, teacher, missions):
    assert len(missions) == 3, 'a agenda tem 3 missoes'
    cards = ''
    for i, m in enumerate(missions, 1):
        _no_pt(m, f'slide {n} mission {i}')
        cards += (
            '      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);'
            'border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem">'
            '<div style="width:34px;height:34px;border-radius:9px;background:var(--accent);color:#fff;'
            'display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">'
            f'{i}</div><p style="font-size:.95rem">{m}</p></div>\n')
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Today</div>\n'
             '    <h2 class="slide-heading">Three <span class="accent">Missions</span></h2>\n'
             '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:520px;'
             'margin:1.4rem auto 0">\n' + cards + '    </div>\n  </div>')
    return _slide(n, 1, 'slide-light', teacher, inner)


def s_vocab(n, teacher, h_b, vocab, grid_id, offset):
    """Reveal cards. O revealVocab do shell faz toggle (REGRA 27E)."""
    cards = []
    for i, (w, d, ex) in enumerate(vocab):
        g1, g2 = GRADIENTS[(offset + i) % len(GRADIENTS)]
        ico = ICONS[(offset + i) % len(ICONS)]
        _no_dq(d, 'vocab def')
        _no_dq(ex, 'vocab example')
        _no_pt(w + ' ' + d + ' ' + ex, f'slide {n} vocab')
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
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Vocabulary</div>\n'
             f'    <h2 class="slide-heading">Words <span class="accent">{h_b}</span></h2>\n'
             '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
             f'<span id="vocabCount{grid_id}">0 / {len(vocab)} words revealed</span></p>\n'
             f'    <div class="vocab-grid" id="vocabGrid{grid_id}">\n' + '\n'.join(cards) +
             '\n    </div>\n  </div>')
    return _slide(n, 2, 'slide-light', teacher, inner)


def s_blocks(n, phase, teacher, label, h_a, h_b, keys, sub=''):
    """Slide que hospeda blocos do builder (IC-BLOCKS)."""
    _no_pt(h_a + h_b + sub, f'slide {n}')
    ph = '\n'.join(f'    <!--IC-BLOCKS:{k}-->' for k in keys)
    sub_html = ('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);'
                f'margin:.3rem auto 0;max-width:520px">{sub}</p>\n' if sub else '')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             + sub_html + ph + '\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_discovery(n, phase, teacher, grammar_point, examples, rule_id, rule_head, rule_rows, rule_note):
    """Grammar discovery — a REGRA nunca vem primeiro. examples = [(html, speak)]"""
    exs = ''
    for h, sp in examples:
        _no_pt(re.sub(r'<[^>]+>', ' ', h), f'slide {n} example')
        exs += ('      <div style="background:var(--bg-card);border:1px solid var(--border);'
                'border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;'
                f'align-items:center;gap:.6rem"><p style="font-size:.92rem">{h}</p>'
                f'{speak_btn(sp)}</div>\n')
    rows = ''
    for i, cells in enumerate(rule_rows):
        style = 'background:var(--bg-elevated)' if i % 2 else 'border-bottom:1px solid var(--border)'
        tds = ''.join(f'<td style="padding:.5rem{";font-weight:600" if j == 0 else ""}">{c}</td>'
                      for j, c in enumerate(cells))
        rows += f'          <tr style="{style}">{tds}</tr>\n'
    ths = ''.join(f'<th style="padding:.6rem;text-align:left">{h}</th>' for h in rule_head)
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Grammar Discovery</div>\n'
             '    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>\n'
             '    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:580px;'
             'margin:1rem auto 0">\n' + exs + '    </div>\n'
             '    <button class="primary-btn" style="margin:1.2rem auto 0;display:block;'
             'background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;'
             'font-size:.9rem;font-weight:600;cursor:pointer" '
             f'onclick="var t=document.getElementById(\'{rule_id}\');'
             "t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'\">"
             'Reveal the Rule</button>\n'
             f'    <div id="{rule_id}" style="display:none;max-width:580px;margin:1rem auto 0;'
             'overflow-x:auto">\n'
             '      <table style="width:100%;border-collapse:collapse;font-size:.85rem;'
             'background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
             f'        <thead><tr style="background:var(--accent);color:#fff">{ths}</tr></thead>\n'
             '        <tbody>\n' + rows + '        </tbody>\n      </table>\n'
             '      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">'
             f'{rule_note}</p>\n    </div>\n  </div>')
    slide = _slide(n, phase, 'slide-light', teacher, inner)
    # data-grammar (REGRA 22 / check_grammar_progression) — o builder tambem injeta a
    # partir de lesson.grammar_point; aqui garantimos que o slide certo o carregue.
    return slide.replace(f'data-phase="{phase}"',
                         f'data-phase="{phase}" data-grammar="{grammar_point}"', 1)


def s_oral(n, phase, teacher, label, h_a, h_b, sub, items):
    """Grammar practice: oral-grid com toggle (REGRA 27E)."""
    _no_pt(h_a + h_b + sub, f'slide {n}')
    its = ''
    for i, (cue, model) in enumerate(items, 1):
        _no_pt(cue, f'slide {n} cue')
        its += ('      <div class="oral-item" onclick="this.classList.toggle(\'revealed\')">'
                f'<div class="oral-situation">{i}. {cue}</div>'
                f'<div class="oral-model">"{model}"</div></div>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">{sub}</p>\n'
             '    <div class="oral-grid">\n' + its + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


X_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><circle cx="12" cy="12" r="10"/>'
         '<line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>')
V_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#16a34a">'
         '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>')


def s_mistake(n, phase, teacher, pairs, note):
    """Common Mistake — .mistake-item mistake-wrong/right, texto DIRETO no div."""
    _no_pt(note, f'slide {n} note')
    items = ''
    for wrong, right in pairs:
        _no_pt(wrong + ' ' + right, f'slide {n} mistake')
        items += (f'      <div class="mistake-item mistake-wrong">\n'
                  f'        <div class="mistake-icon">{X_SVG}</div>\n        "{wrong}"\n      </div>\n'
                  f'      <div class="mistake-item mistake-right">\n'
                  f'        <div class="mistake-icon">{V_SVG}</div>\n        "{right}"\n      </div>\n')
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Common Mistake</div>\n'
             '    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>\n'
             '    <div class="mistake-card">\n' + items + '    </div>\n'
             '    <p style="text-align:center;margin-top:1.4rem;font-size:.88rem;color:var(--text-dim);'
             f'max-width:560px;margin-left:auto;margin-right:auto">{note}</p>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def _comp_qs(qs, n=0):
    out = ''
    for i, (q, a) in enumerate(qs, 1):
        _no_pt(q + ' ' + a, f'slide {n} comp')
        out += (f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">{i}. {q}</div>'
                f'<div class="q-answer">{a}</div></div>\n')
    return out


def s_listening(n, phase, teacher, idx, h_a, h_b, sub, mp3, slug, qs):
    """Listening sound-first, MP3 unico + player completo do shell.
    REGRA 2.1: .comp-questions NASCE VISIVEL (nunca display:none)."""
    _no_pt(h_a + h_b + sub, f'slide {n}')
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
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             '    <div class="chapter-label">Listening</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             f'    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{sub}</p>\n'
             f'    <div class="waveform waveform-paused" id="{wf}">{bars}</div>\n'
             f'    <div class="mock-player" id="{pid}" data-src="/audio/{slug}/{mp3}" data-waveform="{wf}" '
             f'data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">\n'
             f'      <div class="lp-seekbar" onclick="mpSeek(event,\'{pid}\')" style="width:100%;height:6px;'
             'background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative">'
             f'<div class="lp-progress" id="progress-{pid}" style="width:0%;height:100%;'
             'background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>\n'
             '      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem">'
             f'<span id="time-current-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span>'
             f'<span id="time-total-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>\n'
             '      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;'
             'margin-bottom:.6rem">\n'
             f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',-5)" aria-label="Back 5 seconds" '
             'style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;'
             'border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">'
             '-5s</button>\n'
             f'        <button class="lp-btn lp-play" id="play-{pid}" onclick="mpToggle(\'{pid}\')" '
             'aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;'
             'border-radius:50%;width:48px;height:48px;cursor:pointer">'
             '<svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18">'
             '<polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg>'
             '<svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none">'
             '<rect x="6" y="4" width="4" height="16" fill="currentColor"/>'
             '<rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>\n'
             f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',5)" aria-label="Forward 5 seconds" '
             'style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;'
             'border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">'
             '+5s</button>\n'
             '      </div>\n'
             f'      <div style="display:flex;gap:.4rem;justify-content:center">{spd}</div>\n'
             '    </div>\n'
             f'    <div class="comp-questions" id="{qid}" style="max-width:520px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs, n) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def s_dialogue(n, phase, teacher, h_a, h_b, lines):
    """Dialogo line-by-line. lines = [(char_class, initial, voice, body_html)]"""
    _no_pt(h_a + h_b, f'slide {n}')
    ls = ''
    for i, (char, ini, voice, body) in enumerate(lines, 1):
        _no_pt(re.sub(r'<[^>]+>', ' ', body), f'slide {n} dialogue line {i}')
        vis = ' visible' if i == 1 else ''
        ls += (f'      <div class="dialogue-line{vis}" data-line="{i}" data-voice="{voice}">'
               f'<div class="dialogue-avatar {char}">{ini}</div>'
               f'<div class="dialogue-bubble {char}-bubble">{body}</div></div>\n')
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Dialogue</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             '    <div class="dialogue-box" id="dialogueBox">\n' + ls + '    </div>\n'
             '    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" '
             'style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;'
             'border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">'
             'Next Line</button>\n  </div>')
    return _slide(n, phase, 'slide-dark', teacher, inner)


def s_comprehension(n, phase, teacher, label, h_a, h_b, qs):
    """REGRA 27F: as perguntas sao sobre o INTERLOCUTOR, nunca sobre o proprio aluno."""
    _no_pt(h_a + h_b, f'slide {n}')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             '    <div class="comp-questions" style="max-width:540px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs, n) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_artifact(n, phase, teacher, label, h_a, h_b, brand, brand_sub, rows, qs):
    """Artefato REAL em HTML/CSS (nunca imagem), com o nome do aluno."""
    _no_pt(h_a + h_b + brand + brand_sub, f'slide {n}')
    rs = ''
    for i, (k, v) in enumerate(rows):
        _no_pt(f'{k} {v}', f'slide {n} artifact row')
        last = ('' if i == len(rows) - 1
                else ';border-bottom:1px solid var(--border);padding-bottom:.6rem;margin-bottom:.6rem')
        rs += (f'        <div style="display:flex;justify-content:space-between;gap:1rem{last}">'
               f'<span style="font-size:.78rem;color:var(--text-dim)">{k}</span>'
               f'<span style="font-size:.85rem;font-weight:600;text-align:right">{v}</span></div>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             '    <div style="max-width:520px;margin:1.2rem auto 0;background:var(--bg-card);'
             'border:1px solid var(--border);border-radius:12px;overflow:hidden;'
             'box-shadow:0 4px 16px rgba(0,0,0,.08)">\n'
             '      <div style="background:var(--accent);color:#fff;padding:.9rem 1.2rem;display:flex;'
             'justify-content:space-between;align-items:center">'
             f'<span style="font-weight:700;font-size:.9rem;letter-spacing:.5px">{brand}</span>'
             f'<span style="font-size:.72rem">{brand_sub}</span></div>\n'
             '      <div style="padding:1.2rem">\n' + rs + '      </div>\n    </div>\n'
             '    <div class="comp-questions" style="max-width:520px;margin:1.2rem auto 0">\n'
             + _comp_qs(qs, n) + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_error(n, phase, teacher, items):
    """Spot the error — revealError do shell (toggle)."""
    cards = ''
    for w, r in items:
        _no_pt(w + ' ' + r, f'slide {n} error')
        cards += (f'      <div class="error-card" onclick="revealError(this)">'
                  f'<div class="error-sentence">"{w}"</div>'
                  f'<div class="error-fix">"{r}"</div></div>\n')
    inner = ('  <div class="slide-inner">\n    <div class="chapter-label">Detective</div>\n'
             '    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>\n'
             '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
             f'<span id="errorScore">0 / {len(items)} errors found</span></p>\n'
             '    <div class="error-grid" id="errorGrid">\n' + cards + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_roleplay(n, phase, teacher, label, h_a, h_b, scenario_label, scenario, keywords):
    """Role-play. Gradiente CSS + chips (NUNCA foto). keywords=[] => free."""
    _no_pt(h_a + h_b + scenario, f'slide {n} roleplay')
    if keywords:
        chips = ''.join(
            '        <span style="border:1px solid var(--accent);color:var(--accent);'
            f'border-radius:20px;padding:.3rem .9rem;font-size:.8rem;font-weight:600">{k}</span>\n'
            for k in keywords)
        kw = f'      <div style="display:flex;flex-wrap:wrap;gap:.5rem">\n{chips}      </div>\n'
    else:
        kw = ('      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">'
              'No keywords. The floor is yours.</p>\n')
    inner = (f'  <div class="slide-inner">\n    <div class="chapter-label">{label}</div>\n'
             f'    <h2 class="slide-heading">{h_a} <span class="accent">{h_b}</span></h2>\n'
             '    <div class="roleplay-body" style="max-width:520px;margin:1rem auto 0;'
             'background:linear-gradient(135deg,rgba(10,77,104,.12),rgba(10,77,104,.03));'
             'border:1px solid var(--accent);border-radius:12px;padding:1.5rem">\n'
             '      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem">'
             f'<strong>{scenario_label}:</strong> {scenario}</p>\n' + kw + '    </div>\n  </div>')
    return _slide(n, phase, 'slide-light', teacher, inner)


def s_survival(n, teacher, h_a, h_b, phrases):
    assert len(phrases) == 5, 'survival card = 5 frases (REGRA 16)'
    _no_pt(h_a + h_b, f'slide {n}')
    rows = ''
    for i, p in enumerate(phrases, 1):
        _no_pt(p, f'slide {n} survival')
        rows += ('      <div class="survival-item-ic">'
                 f'<div class="survival-num-ic">{i}</div>'
                 f'<div class="survival-text-ic">"{p}"</div>'
                 f'{speak_btn(p, label=VOL_SVG)}</div>\n')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             '    <div class="chapter-label">Survival Lines</div>\n'
             f'    <h2 class="slide-heading" style="color:#fff">{h_a} <span class="accent">{h_b}</span></h2>\n'
             '    <div class="survival-grid" style="max-width:560px;margin:1.5rem auto 0">\n'
             + rows + '    </div>\n  </div>')
    return _slide(n, 7, 'slide-dark', teacher, inner)


CHECK_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
             '<polyline points="20 6 9 17 4 12"/></svg>')


def s_checklist(n, teacher, lesson_n, items):
    """5 checks -> inclass_done no Supabase (REGRA 28)."""
    assert len(items) == 5, 'o checklist DEVE ter exatamente 5 itens (REGRA 28)'
    its = ''
    for t in items:
        _no_pt(t, f'slide {n} checklist')
        its += ('      <div class="check-item" onclick="toggleCheck(this)">'
                f'<div class="check-box">{CHECK_SVG}</div>{t}</div>\n')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             '    <div class="chapter-label">Self-Assessment</div>\n'
             '    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>\n'
             f'    <div class="check-grid" id="checklist-{lesson_n}" style="max-width:540px;'
             'margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">\n'
             + its + '    </div>\n  </div>')
    return _slide(n, 7, 'slide-dark', teacher, inner)


def s_badge(n, teacher, lesson_n, badge, line, next_title):
    _no_pt(badge + ' ' + line + ' ' + next_title, f'slide {n} badge')
    inner = ('  <div class="slide-inner" style="text-align:center">\n'
             '    <div class="chapter-label">Lesson Complete</div>\n'
             '    <div class="badge-card">\n      <div class="badge-icon">\n'
             '        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" '
             'stroke="currentColor" stroke-width="1.5"><path d="M9 11l3 3L22 4"/>'
             '<path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div>\n'
             '        <div class="sparkles">' + '<div class="sparkle"></div>' * 6 + '</div>\n'
             '      </div>\n'
             f'      <h2 class="slide-heading" style="color:#fff">{badge} '
             '<span class="accent">Badge Earned!</span></h2>\n'
             f'      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">{line}</p>\n'
             '      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">'
             f'Lesson {lesson_n} -- Complete.</p>\n'
             '      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">'
             f'Next lesson: {next_title}</p>\n    </div>\n  </div>')
    return _slide(n, 7, 'slide-dark', teacher, inner)


# ---------------------------------------------------------------- Pre-class (REGRA 4)

def preclass(spec):
    """Accordion ex-lesson-N com as 5 etapas + sub-etapas 1.1..1.5 (REGRA 4).
    B1 => tudo em ingles (REGRA 13). Falha alto se faltar bloco obrigatorio."""
    n = spec['n']
    v = spec['vocab']
    for key in ('vocab', 'blanks', 'speech', 'order', 'context_paras', 'context_quiz',
                'tip_title', 'tip_intro', 'tip_rows', 'tip_note', 'quiz', 'think'):
        assert spec.get(key), f'REGRA 4: aula {n} sem "{key}"'
    assert len(spec['speech']) == 5, 'survival card = 5 frases (REGRA 16)'

    rnd = random.Random(700 + n)
    defs = [d for _, d, _ in v]

    # 1.1 vocab cards
    cards = '\n'.join(
        '        <div class="vocab-card-pc"><div class="vocab-card-content">'
        f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
        '<span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{d}</span></div>'
        f'<div class="vocab-card-example">"{ex}"</div></div>'
        f'{speak_btn(w, cls="audio-btn", label="Listen")}</div>' for w, d, ex in v)

    # 1.2 matching — REGRA 24: ordem SEMPRE diferente da ordem das palavras
    rows = []
    for w, d, _ in v:
        opts = defs[:]
        while True:
            rnd.shuffle(opts)
            if opts != defs:
                break
        o = ''.join(f'<option value="{x}">{x}</option>' for x in opts)
        rows.append(f'        <div class="match-row" data-answer="{d}">'
                    f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
                    '<select style="flex:1;width:100%" onchange="checkMatch(this)">'
                    f'<option value="">Select...</option>{o}</select></div>')
    match_rows = '\n'.join(rows)

    # 1.3 grammar in context
    _mt = ' style="margin-top:.7rem"'
    ctx_paras = '\n'.join(
        '        <p%s>%s</p>' % (_mt if i else '', p)
        for i, p in enumerate(spec['context_paras']))
    ctx_quiz = '\n'.join(
        '      <div class="quiz-item"><div class="quiz-question">%d. %s</div>'
        '<div class="quiz-options">%s</div></div>'
        % (i, q, ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
            f'<span class="option-letter">{chr(65 + j)}</span> {opt}</div>'
            for j, (opt, ok) in enumerate(opts)))
        for i, (q, opts) in enumerate(spec['context_quiz'], 1))

    # 1.4 grammar tip
    tip_rows = ''
    for i, cells in enumerate(spec['tip_rows']):
        style = ('border-bottom:1px solid var(--border);background:var(--bg-elevated)' if i % 2
                 else 'border-bottom:1px solid var(--border)')
        if len(cells) == 3:
            tds = (f'<td style="padding:.6rem;font-weight:600">{cells[0]}</td>'
                   f'<td style="padding:.6rem">{cells[1]}</td>'
                   f'<td style="padding:.6rem">{cells[2]}</td>')
        else:
            tds = (f'<td style="padding:.6rem;font-weight:600">{cells[0]}</td>'
                   f'<td style="padding:.6rem" colspan="2">{cells[1]}</td>')
        tip_rows += f'          <tr style="{style}">{tds}</tr>\n'

    # 1.5 fill in the blank
    fills = []
    for pre, ans, hint, phrase, post in spec['blanks']:
        _no_dq(phrase, 'blank phrase')
        _no_pt(hint, 'blank hint')
        SPEAKABLE.append(phrase)
        fills.append(
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre}'
            f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" '
            f'data-phrase="{phrase}" placeholder="___">{post}"</div>'
            '<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
    fill_items = '\n'.join(fills)

    # 2 ordering
    oid = f'order-l{n}'
    order_items = '\n'.join(
        f'        <div class="order-item" draggable="true" data-order="{o}" '
        f'onclick="selectOrderItem(this,\'{oid}\')"><span class="order-num">?</span>'
        f'<span class="order-text">{t}</span><span class="order-arrows">'
        f'<button class="arrow-btn" onclick="moveItem(this,-1,\'{oid}\')">&#9650;</button>'
        f'<button class="arrow-btn" onclick="moveItem(this,1,\'{oid}\')">&#9660;</button>'
        '</span></div>' for o, t in spec['order'])

    # 3 pronunciation (B1: sem .speech-translation)
    sp = []
    for phrase in spec['speech']:
        _no_dq(phrase, 'speech phrase')
        _no_pt(phrase, 'speech phrase')
        SPEAKABLE.append(phrase)
        sp.append(
            f'      <div class="speech-card" data-phrase="{phrase}">\n'
            f'        <div class="speech-phrase">{phrase}</div>\n'
            '        <div class="speech-controls">'
            '<button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            '<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button>'
            '</div>\n        <div class="speech-result"></div>\n      </div>')
    speech_cards = '\n'.join(sp)

    # 4 situational quiz
    sit_quiz = '\n'.join(
        '      <div class="quiz-item"><div class="quiz-question">%s</div>'
        '<div class="quiz-options">%s</div></div>'
        % (q, ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
            f'<span class="option-letter">{chr(65 + j)}</span> {opt}</div>'
            for j, (opt, ok) in enumerate(opts)))
        for q, opts in spec['quiz'])

    # survival (B1: sem .sp-pt)
    survival = '\n'.join(
        f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
        f'<span class="sp-en">{en}</span>'
        f'{speak_btn(en, cls="btn btn-listen", label="&#9835;")}</div>'
        for i, en in enumerate(spec['speech'], 1))

    html = f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{spec['hub_img']}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson {n:02d} -- Pre-class</div>
      <h3>{spec['title']}</h3>
      <div class="lesson-desc">{spec['desc']}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l{n}">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l{n}')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text, then answer the questions.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:8px;padding:1rem;margin-bottom:1rem;font-size:.9rem;line-height:1.7">
{ctx_paras}
      </div>
{ctx_quiz}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {spec['tip_title']}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{spec['tip_intro']}</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
{tip_rows}        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem">{spec['tip_note']}</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Write the correct word. Tap Listen to hear the full sentence.</p>
{fill_items}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: {spec['order_title']}</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{spec['order_intro']}</p>
      <button class="btn btn-listen" data-speak="[order-l{n}]" onclick="speakText(this.dataset.speak, this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="{oid}">
{order_items}
      </div>
      <button class="verify-all-btn" onclick="checkOrder('{oid}')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen, then record yourself. You will see which words came through clearly.</p>
{speech_cards}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{spec['quiz_intro']}</p>
{sit_quiz}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">{spec['think']}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
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
    _no_pt(re.sub(r'data-teacher="[^"]*"', '', html), f'preclass aula {n}')
    return html


# ---------------------------------------------------------------- Complementares

MEDIA_SVG = {
    'youtube': ('<path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 '
                '2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72'
                '.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 '
                '00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/>'),
    'podcast': ('<path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 '
                '2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/>'),
    'video': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3l-4 4-4-4"/>',
    'series': ('<rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><path d="M7 2v20"/>'
               '<path d="M17 2v20"/><path d="M2 12h20"/><path d="M2 7h5"/><path d="M2 17h5"/>'
               '<path d="M17 17h5"/><path d="M17 7h5"/>'),
    'article': ('<path d="M4 19V5a2 2 0 012-2h9l5 5v11a2 2 0 01-2 2H6a2 2 0 01-2-2z"/>'
                '<path d="M14 3v5h5"/><path d="M8 13h8M8 17h5"/>'),
}


def complementary(spec):
    """Bloco de Complementares da AULA N (modo snippets). 3 recomendacoes (REGRA 17).
    B1 => tudo em ingles (REGRA 13). Link direto ao episodio, nunca busca, nunca pago."""
    n = spec['n']
    items = spec['media']
    assert len(items) == 3, 'REGRA 17: exatamente 3 recomendacoes por aula'
    out = []
    for icon, mid, kind, title, desc, tip, link, cta in items:
        assert link.startswith('https://'), f'link invalido: {link}'
        assert not re.search(r'(search|/results|\?q=|query=)', link), f'REGRA 17: link de busca: {link}'
        _no_pt(f'{kind} {title} {desc} {tip} {cta}', f'complementary l{n}')
        out.append(f'''<div class="media-card-wrapper" data-media="l{n}-{mid}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2">{MEDIA_SVG[icon]}</svg></div>
    <div class="media-info">
      <div class="media-type">{kind}</div>
      <h5>{title}</h5>
      <p>{desc}</p>
      <p class="media-tip">{tip}</p>
      <a href="{link}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">{cta} &#8599;</a>
    </div>
  </div>
</div>
''')
    return '\n'.join(out)


# ---------------------------------------------------------------- config

BASE_CONFIG = {
    "slug": "felipe-de-araujo-dias",
    "student_name": "Felipe de Ara&uacute;jo Dias",
    "first_name": "Felipe",
    "gender": "m",
    "program": "Business &amp; General English",
    "total_aulas": 80,
    "palette": {"accent": "#0a4d68", "accent_light": "#3d9dc4"},
    "header": ["B1", "S&#227;o Paulo, SP", "Diretor de Suprimentos &mdash; Riachuelo",
               "60 min &middot; Online"],
    "hub_subtitle": ("Ingl&ecirc;s corporativo e geral para conduzir a conversa sozinho "
                     "&mdash; reuni&otilde;es, fornecedores, eventos e viagem"),
    "stamps": [
        {"id": 1, "label": "What I Actually Do",
         "img": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80"},
        {"id": 2, "label": "A Week That Never Repeats",
         "img": "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=200&q=80"},
        {"id": 3, "label": "The Supplier Call",
         "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=200&q=80"},
        {"id": 4, "label": "The Trip to Chicago",
         "img": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=200&q=80"},
        {"id": 5, "label": "What Went Wrong",
         "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80"},
    ],
    "voices": {
        "arthur": "sfJopaWaOtauCD3HKX6Q",
        "ellen": "BIvP0GN1cAtSRTxNHnWS",
        "british_m": "JBFqnCBsd6RMkjVDRZzb",
        "indian_f": "fBJDfBxPazPKo9oZ1P8t",
        "nordic_f": "oVXQ3H21hRI9OtM4YH5K",
        "nordic_m": "6moWX0dfuSmryJkGegeK",
        "italian_m": "vsxj8mTkgBSaMoGnPGc9",
        "italian_f": "NeTWyxKL7qMefrZEowed",
        "french_f": "dTmTLshIypwp08eftJH6",
        "french_m": "1a6onbE6zC5AwIN3pEp0",
        "dutch_m": "SVmtrm5iuquj8zKn5ZMg",
    },
}


def config(spec, slide_count):
    c = json.loads(json.dumps(BASE_CONFIG))
    c['characters'] = spec['characters']
    n = spec['n']
    c['lesson'] = {
        'n': n,
        'menu_num': f'{n:02d}',
        'menu_title': spec['title'],
        'menu_desc': f'{spec["menu_desc"]} -- {slide_count} slides',
        'subtitle': f'Lesson {n} -- {spec["short_title"]}',
        'title_tag': (f'Professor View -- Felipe de Ara&uacute;jo Dias | '
                      f'Lesson {n} -- {spec["short_title"]}'),
        'grammar_point': spec['grammar_point'],
        'phases': spec['phases'],
        'inclass_blocks': spec['inclass_blocks'],
        'listenings': spec['listenings'],
        'extra_audio': spec['extra_audio'],
    }
    c['hub'] = 'snippets'
    return c


# ---------------------------------------------------------------- REGRA 22

SLUG = 'felipe-de-araujo-dias'


def assert_no_vocab_repeat(n, vocab, root):
    """REGRA 22: nenhuma palavra ja ensinada como vocab card em aula anterior."""
    seen = {}
    hub = os.path.join(root, 'public', 'professor', f'{SLUG}.html')
    if os.path.exists(hub):
        c = open(hub, encoding='utf-8').read()
        ids = [(m.start(), int(m.group(1))) for m in re.finditer(r'id="ex-lesson-(\d+)"', c)]
        for i, (pos, ln) in enumerate(ids):
            if ln >= n:
                continue
            end = ids[i + 1][0] if i + 1 < len(ids) else len(c)
            for w in re.findall(r'vocab-card-word[^>]*>([^<]+)<', c[pos:end]):
                seen[w.strip().lower()] = ln
    dupes = [(w, seen[w.lower()]) for w, _, _ in vocab if w.lower() in seen]
    assert not dupes, f'REGRA 22 violada — ja ensinadas: {dupes}'
    return len(seen)


# ---------------------------------------------------------------- escrita

def emit(spec, slides_html, root, outdir, slide_count=None):
    os.makedirs(outdir, exist_ok=True)
    n = spec['n']
    count = slide_count or len(re.findall(r'<div class="slide ', slides_html))
    assert count >= 25, f'REGRA 11.7: minimo 25 slides para 60 min (tem {count})'

    assert_no_vocab_repeat(n, spec['vocab'], root)

    # REGRA 2.1: as perguntas do listening NUNCA nascem escondidas
    assert not re.search(r'class="comp-questions"[^>]*display:\s*none', slides_html), \
        'REGRA 2.1: .comp-questions nasceu escondido'

    open(os.path.join(outdir, 'slides.html'), 'w', encoding='utf-8').write(slides_html)
    open(os.path.join(outdir, 'preclass.html'), 'w', encoding='utf-8').write(preclass(spec))
    open(os.path.join(outdir, 'complementary.html'), 'w', encoding='utf-8').write(complementary(spec))
    with open(os.path.join(outdir, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config(spec, count), f, ensure_ascii=False, indent=2)

    # trava final REGRA 7.1: nenhum texto dentro da string de um onclick
    for fn in ('slides.html', 'preclass.html', 'complementary.html'):
        blob = open(os.path.join(outdir, fn), encoding='utf-8').read()
        bad = re.findall(r"speakText\('[^']*'", blob)
        assert not bad, f'REGRA 7.1 violada em {fn}: texto dentro do onclick: {bad[:2]}'
    print(f'aula {n}: {count} slides, {len(spec["vocab"])} vocab, '
          f'{len(set(SPEAKABLE))} frases falaveis')
    return count
