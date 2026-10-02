# -*- coding: utf-8 -*-
"""Helpers das abas suplementares (copiados das abas da Joyce Michalczuk).

Pedidos dela na consultoria de 29/09/2026: 'me fala o que fazer, shadow 30 minutos, ler uma hora'
(direcao em minutos), 4 a 6 horas de estudo por dia, e a dor central: explicar ICMS, VAT e a
reforma tributaria ao time global. Tudo em ingles na tela (B1). So chama funcoes que ja existem
no hub (toggleLesson, speakText, speakPhrase, startRecording, stopRecording,
startFreeRecording, stopFreeRecording). Sem fill-in, matching nem quiz: nada que o loadState
restaure por texto e possa colidir com as aulas."""
import html as H
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def q(s):
    return s.replace('"', '&quot;')


def card_open(cid, img, num, title, desc):
    return (f'<div class="lesson-card" id="{cid}">\n  <div class="lesson-header" onclick="toggleLesson(this)">\n'
            f'    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/{img}?w=600&q=80\')"></div>\n'
            f'    <div class="lesson-header-content">\n      <div class="lesson-number">{num}</div>\n      <h3>{title}</h3>\n'
            f'      <div class="lesson-desc">{desc}</div>\n    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n  <div class="lesson-body">\n')


CARD_CLOSE = '  </div>\n</div>\n'


def section(title, badge_cls, badge, instr, body):
    return (f'\n    <div class="exercise-section">\n      <div class="section-header-row"><h4>{title}</h4><span class="badge {badge_cls}">{badge}</span></div>\n'
            f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{instr}</p>\n{body}    </div>\n')


def speech(p):
    return (f'      <div class="speech-card" data-phrase="{q(p)}">\n        <div class="speech-phrase">{p}</div>\n'
            '        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
            '        <div class="speech-result"></div>\n      </div>\n')


def free(rid, prompt):
    return (f'      <div class="think-card">\n        <div class="think-question">{prompt}</div>\n'
            '        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>'
            '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>\n'
            f'        <div id="{rid}"></div>\n      </div>\n')


def listen_btn(text, accent):
    return (f'      <button class="audio-btn" data-accent="{accent}" data-speak="{q(text)}" onclick="speakText(this.dataset.speak,this)" '
            'style="margin-bottom:1rem">Listen</button>\n')


def transcript(text):
    return ('      <details style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:.7rem 1rem;margin-bottom:.8rem">'
            '<summary style="cursor:pointer;font-size:.85rem;font-weight:600;color:var(--accent)">Transcript</summary>'
            f'<p style="font-size:.9rem;line-height:1.7;margin-top:.6rem">{text}</p></details>\n')


def tab(slot, title, intro, body):
    return (f'<!-- ========== EXTRAS: {title.upper()} (aditivo) ========== -->\n<div class="tab-content" id="tab-{slot}">\n'
            f'<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">{title}</h3>\n'
            f'<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem">{intro}</p>\n{body}</div><!-- /tab-{slot} -->\n')


def rule_box(label, text):
    return (f'<div style="margin:.2rem 0 1.2rem;padding:.9rem 1.1rem;background:var(--accent-dim);border-left:3px solid var(--accent);'
            f'border-radius:0 8px 8px 0;font-size:.85rem;line-height:1.65;color:var(--text-mid)"><strong style="color:var(--accent)">{label}</strong> {text}</div>\n')


def table(head, rows):
    th = ''.join(f'<th style="text-align:left;padding:.6rem .7rem">{h}</th>' for h in head)
    tr = ''
    for r in rows:
        tds = ''.join(f'<td style="padding:.6rem .7rem;border-top:1px solid var(--border){";font-weight:600;white-space:nowrap" if i == 0 else ""}'
                      f'{";white-space:nowrap;color:var(--accent);font-weight:600" if i == len(r) - 1 else ""}">{c}</td>' for i, c in enumerate(r))
        tr += f'      <tr>{tds}</tr>\n'
    return ('<div style="overflow-x:auto;margin-bottom:1.5rem">\n<table style="width:100%;min-width:520px;border-collapse:collapse;font-size:.86rem;'
            f'background:var(--bg-card);border:1px solid var(--border);border-radius:8px">\n      <tr>{th}</tr>\n{tr}</table>\n</div>\n')


def bullets(title, items):
    li = ''.join(f'        <li style="margin-bottom:.45rem">{i}</li>\n' for i in items)
    return (f'<div class="exercise-section">\n  <div class="section-header-row"><h4>{title}</h4></div>\n'
            f'  <ul style="font-size:.88rem;line-height:1.6;color:var(--text-mid);padding-left:1.2rem;margin:0">\n{li}  </ul>\n</div>\n')


