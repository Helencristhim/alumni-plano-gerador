#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render.py -- emite os ARQUIVOS DE CONTEUDO de uma aula da Ana Claudia.

NAO e um builder alternativo (REGRA 20). O builder continua sendo
`_build/model/build_from_model.py`. Este script so escreve os INPUTS que o
builder consome (slides.html / preclass.html / complementary.html / config.json),
a partir de um `content.py` com o dicionario LESSON -- exatamente o papel que o
`content.py` da aula 10 ja tinha, agora com o render junto em vez de na mao.

Motivo: as 40 aulas do arco V3 tem a MESMA forma (36 slides, 7 capitulos,
5 etapas de Pre-class). Escrever a forma a mao 40 vezes e o caminho conhecido
para o defeito silencioso. Aqui a forma e UMA; o que muda por aula e so o
conteudo pedagogico.

USO (da raiz do repo):
  python3 _build/ana-claudia-veraldi-gen/render.py 11
  python3 _build/model/build_from_model.py _build/ana-claudia-veraldi-aula11/config.json
  python3 _build/model/insert_hub.py       _build/ana-claudia-veraldi-aula11/config.json
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

SLUG = 'ana-claudia-veraldi'

# ---------------------------------------------------------------- constantes
# IDs conferidos contra os configs ja publicados das aulas 1-9 (nao inventar voz nova:
# o gate cruza o audio_manifest com o data-voice declarado).
VOICES = {
    'arthur': 'sfJopaWaOtauCD3HKX6Q',
    'ellen': 'BIvP0GN1cAtSRTxNHnWS',
    'british_m': 'JBFqnCBsd6RMkjVDRZzb',
    'nordic_f': 'oVXQ3H21hRI9OtM4YH5K',
    'nordic_m': '6moWX0dfuSmryJkGegeK',
    'dutch_m': 'SVmtrm5iuquj8zKn5ZMg',
    'french_f': 'dTmTLshIypwp08eftJH6',
    'french_m': '1a6onbE6zC5AwIN3pEp0',
    'italian_f': 'NeTWyxKL7qMefrZEowed',
    'italian_m': 'vsxj8mTkgBSaMoGnPGc9',
    'german_f': 'e08a4DxAw2gRDHs73Vg0',
    'indian_f': 'fBJDfBxPazPKo9oZ1P8t',
    'australian_f': 'IwFADcBfc7Yo8KGhxTR5',
    'australian_m': 'Ziqfyey5k3R3GRC5abi8',
}

PALETTE = {'accent': '#0891b2', 'accent_light': '#22d3ee'}

HEADER = ['B2 (Intermedi&#225;rio)', 'Interior de S&#227;o Paulo', '46 anos', '60 min &middot; Online']

STAMPS = [
    {'id': 1, 'label': 'First Words', 'img': 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=200&q=80'},
    {'id': 2, 'label': 'Your Story', 'img': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=200&q=80'},
    {'id': 3, 'label': 'The Code', 'img': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=200&q=80'},
    {'id': 4, 'label': 'Many Englishes', 'img': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=200&q=80'},
    {'id': 5, 'label': 'Confident Voice', 'img': 'https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?w=200&q=80'},
]

SVG_LISTEN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

ICONS = {
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'star': '<path d="M12 2l3 6.6 7.2.9-5.3 4.9 1.4 7.1L12 18l-6.3 3.5 1.4-7.1L1.8 9.5 9 8.6z"/>',
    'compass': '<circle cx="12" cy="12" r="10"/><polygon points="16.2 7.8 14.1 14.1 7.8 16.2 9.9 9.9"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'moon': '<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>',
    'plane': ('<path d="M17.8 19.2L16 11l3.5-3.5a2.1 2.1 0 00-3-3L13 8 4.8 6.2a1 1 0 00-1 .3l-.9.9a1 1 0 '
              '00.3 1.6L9 12l-2 3H4l-1 2 4 1 1 4 2-1v-3l3-2 3.2 6.8a1 1 0 001.6.3l.9-.9a1 1 0 00.3-1z"/>'),
    'users': ('<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>'
              '<path d="M23 21v-2a4 4 0 00-3-3.9"/><path d="M16 3.1a4 4 0 010 7.8"/>'),
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>',
    'map': ('<polygon points="1 6 8 3 16 6 23 3 23 18 16 21 8 18 1 21"/><line x1="8" y1="3" x2="8" y2="18"/>'
            '<line x1="16" y1="6" x2="16" y2="21"/>'),
    'leaf': '<path d="M11 20A7 7 0 019.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.7 4.5-7"/>',
    'flag': '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    'gift': ('<polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/>'
             '<line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/>'
             '<path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/>'),
    'home': '<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'eye': '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    'heart': '<path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 00-7.8 7.8l1.1 1L12 21l7.7-7.6 1.1-1a5.5 5.5 0 000-7.8z"/>',
    'mic': ('<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/>'
            '<line x1="12" y1="19" x2="12" y2="23"/>'),
    'globe': ('<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/>'
              '<path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>'),
    'coffee': ('<path d="M18 8h1a4 4 0 010 8h-1"/><path d="M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4z"/>'
               '<line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>'),
    'tool': ('<path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 '
             '2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/>'),
    'sun': ('<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/>'
            '<line x1="4.2" y1="4.2" x2="5.6" y2="5.6"/><line x1="18.4" y1="18.4" x2="19.8" y2="19.8"/>'
            '<line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/>'
            '<line x1="4.2" y1="19.8" x2="5.6" y2="18.4"/><line x1="18.4" y1="5.6" x2="19.8" y2="4.2"/>'),
    'cloud': '<path d="M18 10h-1.26A8 8 0 109 20h9a5 5 0 000-10z"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    'message': ('<path d="M21 11.5a8.4 8.4 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.4 8.4 0 01-3.8-.9L3 21l1.9-5.7a8.4 8.4 '
                '0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.4 8.4 0 013.8-.9h.5a8.5 8.5 0 018 8z"/>'),
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    'calendar': ('<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/>'
                 '<line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>'),
    'scale': '<path d="M12 3v18"/><path d="M5 7h14"/><path d="M8 7l-4 7h8z"/><path d="M16 7l-4 7h8z"/>',
    'anchor': '<circle cx="12" cy="5" r="3"/><line x1="12" y1="22" x2="12" y2="8"/><path d="M5 12H2a10 10 0 0020 0h-3"/>',
    'alert': ('<path d="M10.3 3.9L1.8 18a2 2 0 001.7 3h17a2 2 0 001.7-3L14.7 3.9a2 2 0 00-3.4 0z"/>'
              '<line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    'help': ('<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 015.8 1c0 2-3 3-3 3"/>'
             '<line x1="12" y1="17" x2="12.01" y2="17"/>'),
    'key': '<path d="M21 2l-2 2"/><path d="M11.4 11.6a5 5 0 11-7.1 7.1 5 5 0 017.1-7.1z"/><path d="M15.5 7.5l3 3L22 7l-3-3z"/>',
    'layers': ('<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/>'
               '<polyline points="2 12 12 17 22 12"/>'),
    'refresh': ('<polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/>'
                '<path d="M3.5 9a9 9 0 0114.9-3.4L23 10"/><path d="M1 14l4.6 4.4A9 9 0 0020.5 15"/>'),
    'trending': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    'link': ('<path d="M10 13a5 5 0 007.5.5l3-3a5 5 0 00-7-7l-1.7 1.7"/>'
             '<path d="M14 11a5 5 0 00-7.5-.5l-3 3a5 5 0 007 7L12.3 19"/>'),
    'zap': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
}

GRADS = [
    '#0c4a6e,#0369a1', '#713f12,#a16207', '#450a0a,#b91c1c', '#1e293b,#475569',
    '#7c2d12,#ea580c', '#134e4a,#0d9488', '#4c1d95,#7c3aed', '#7f1d1d,#dc2626',
    '#1e3a8a,#3b82f6', '#14532d,#16a34a', '#78350f,#c2410c', '#312e81,#4f46e5',
]

DARK_BG = "linear-gradient(rgba(8,18,28,.80),rgba(8,18,28,.92))"


# ---------------------------------------------------------------- helpers
def esc(t):
    """Escapa aspas duplas para uso dentro de atributo HTML."""
    return str(t).replace('"', '&quot;')


def icon_svg(name, stroke='#fff'):
    path = ICONS.get(name)
    assert path, 'icone desconhecido no content.py: %r (disponiveis: %s)' % (name, ', '.join(sorted(ICONS)))
    return '<svg viewBox="0 0 24 24" fill="none" stroke="%s">%s</svg>' % (stroke, path)


def listen_btn(text, stop=False):
    pre = 'event.stopPropagation();' if stop else ''
    return ('<button class="audio-btn-sm" data-speak="%s" onclick="%sspeakText(this.dataset.speak,this)">%s Listen</button>'
            % (esc(text), pre, SVG_LISTEN))


def img_slide(n, phase, teacher, img, chapter, heading, sub=None, big=False):
    size = '2.5rem' if big else '2rem'
    tag = 'h1' if big else 'h2'
    out = ['<div class="slide slide-image%s" data-slide="%d" data-phase="%d" data-teacher="%s" '
           'style="background-image:%s,url(\'%s\');background-size:cover;background-position:center">'
           % (' active' if n == 1 else '', n, phase, esc(teacher), DARK_BG, img)]
    out.append('  <div class="slide-inner" style="text-align:center">')
    out.append('    <div class="chapter-label">%s</div>' % chapter)
    out.append('    <%s class="slide-heading" style="font-size:%s;color:#fff">%s</%s>' % (tag, size, heading, tag))
    if sub:
        out.append('    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">%s</p>' % sub)
    out.append('  </div>')
    out.append('</div>')
    return '\n'.join(out) + '\n'


def light_slide(n, phase, teacher, chapter, heading, body, note=None):
    out = ['<div class="slide slide-light" data-slide="%d" data-phase="%d" data-teacher="%s">' % (n, phase, esc(teacher))]
    out.append('  <div class="slide-inner">')
    out.append('    <div class="chapter-label">%s</div>' % chapter)
    out.append('    <h2 class="slide-heading">%s</h2>' % heading)
    if note:
        out.append('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">%s</p>' % note)
    out.append(body)
    out.append('  </div>')
    out.append('</div>')
    return '\n'.join(out) + '\n'


def player(pid, src, wf, qid, questions, title, sub, blurb, n, phase, teacher, chapter):
    bars = '<div class="bar"></div>' * 20
    qs = ''.join('<div class="comp-q" onclick="revealComp(this)"><div class="q-text">%d. %s</div>'
                 '<div class="q-answer">%s</div></div>' % (i + 1, q, a) for i, (q, a) in enumerate(questions))
    return '''<div class="slide slide-dark" data-slide="%(n)d" data-phase="%(phase)d" data-teacher="%(teacher)s">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">%(chapter)s</div>
    <h2 class="slide-heading" style="color:#fff">%(title)s</h2>
    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">%(blurb)s</p>
    <div class="waveform waveform-paused" id="%(wf)s">%(bars)s</div>
    <div class="mock-player" id="%(pid)s" data-src="%(src)s" data-waveform="%(wf)s" data-questions="%(qid)s" style="max-width:460px;margin:.8rem auto 0">
      <div class="lp-seekbar" onclick="mpSeek(event,'%(pid)s')" style="width:100%%;height:6px;background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative"><div class="lp-progress" id="progress-%(pid)s" style="width:0%%;height:100%%;background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>
      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem"><span id="time-current-%(pid)s" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span><span id="time-total-%(pid)s" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>
      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">
        <button class="lp-btn" onclick="mpSkip('%(pid)s',-5)" aria-label="Back 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>
        <button class="lp-btn lp-play" id="play-%(pid)s" onclick="mpToggle('%(pid)s')" aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%%;width:48px;height:48px;cursor:pointer"><svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg><svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none"><rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>
        <button class="lp-btn" onclick="mpSkip('%(pid)s',5)" aria-label="Forward 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>
      </div>
      <div style="display:flex;gap:.4rem;justify-content:center">
        <button class="lp-speed-btn" onclick="mpSpeed('%(pid)s',0.5,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.5x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('%(pid)s',0.75,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.75x</button>
        <button class="lp-speed-btn lp-speed-active" onclick="mpSpeed('%(pid)s',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('%(pid)s',1.25,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1.25x</button>
      </div>
    </div>
    <div class="comp-questions" id="%(qid)s" style="max-width:520px;margin:1.2rem auto 0">%(qs)s</div>
  </div>
</div>
''' % dict(n=n, phase=phase, teacher=esc(teacher), chapter=chapter, title=title, blurb=blurb,
           wf=wf, bars=bars, pid=pid, src=src, qid=qid, qs=qs)


def comp_block(items):
    return ('<div style="display:flex;flex-direction:column;gap:1rem;max-width:540px;margin:1.2rem auto 0">'
            + ''.join('<div class="comp-q" onclick="revealComp(this)"><div class="q-text">%d. %s</div>'
                      '<div class="q-answer">%s</div></div>' % (i + 1, q, a) for i, (q, a) in enumerate(items))
            + '</div>')


# ---------------------------------------------------------------- slides
def render_slides(L):
    n = L['n']
    imgs = L['imgs']
    T = L['teacher']
    reading = L.get('model') == 'reading'
    out = []
    s = 0

    def nxt():
        nonlocal s
        s += 1
        return s

    # ---- chapter 1
    out.append(img_slide(nxt(), 1, T['title'], imgs['hero'], 'Lesson %d &middot; %s' % (n, L['chapter_tag']),
                         L['title_html'], None, big=True).replace(
        '</h1>\n  </div>',
        '</h1>\n    <p style="color:rgba(255,255,255,.82);font-size:1.1rem;margin-top:1rem">%s</p>\n  </div>' % L['title_sub']))

    w = L['warmup']
    out.append('''<div class="slide slide-dark" data-slide="%d" data-phase="1" data-teacher="%s" style="background-image:%s,url('%s');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 1: %s</div>
    <h2 class="slide-heading" style="color:#fff">%s</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:1rem;max-width:640px;margin-left:auto;margin-right:auto">%s</p>
    <p style="color:var(--accent-light);font-size:.95rem;margin-top:1.4rem;font-weight:600">%s</p>
  </div>
</div>
''' % (nxt(), esc(T['warmup']), DARK_BG, imgs['warmup'], L['phases'][0], w['heading'], w['callback'], w['question']))

    f = L['framing']
    steps = ''.join('<div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;'
                    'padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">%d. %s</p>'
                    '<p style="font-size:.78rem;color:var(--text-dim)">%s</p></div>' % (i + 1, t, d)
                    for i, (t, d) in enumerate(f['steps']))
    body = ('    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;'
            'max-width:680px;margin:1.5rem auto 0">%s</div>\n'
            '    <p style="text-align:center;font-size:.88rem;color:var(--text-dim);margin-top:1.2rem;max-width:600px;'
            'margin-left:auto;margin-right:auto">%s</p>' % (steps, f['note']))
    out.append(light_slide(nxt(), 1, T['framing'], 'Tonight&rsquo;s Goal', f['heading'], body))

    h = L['hook']
    body = ('    <div style="max-width:580px;margin:1.5rem auto 0;background:var(--bg-card);border:1px solid var(--border);'
            'border-radius:12px;padding:1.5rem;text-align:center">\n'
            '      <p style="font-size:1rem">%s</p>\n'
            '      <p style="font-size:.88rem;color:var(--text-dim);margin-top:.8rem">%s</p>\n'
            '    </div>' % (h['line1'], h['line2']))
    out.append(light_slide(nxt(), 1, T['hook'], h['label'], h['heading'], body))

    # ---- chapter 2
    out.append(img_slide(nxt(), 2, T['vocab_trans'], imgs['vocab'], 'Chapter 2: %s' % L['phases'][1],
                         L['vocab_heading'], L['vocab_sub']))

    vocab = L['vocab']
    assert len(vocab) == 12, 'a aula precisa de 12 itens de vocab (B2), veio %d' % len(vocab)
    for grp in (0, 1):
        cards = []
        for i, v in enumerate(vocab[grp * 6:grp * 6 + 6]):
            grad = GRADS[(grp * 6 + i) % len(GRADS)]
            hint = ('EXPRESSION &mdash; ' if v.get('expr') else '') + v['def']
            cards.append('      <div class="vocab-card" onclick="revealVocab(this)">\n'
                         '        <div class="card-icon" style="background:linear-gradient(135deg,%s)">%s'
                         '<div class="card-hint">%s</div></div>\n'
                         '        <div class="card-body"><div class="card-word">%s</div><div class="card-def">%s</div>'
                         '<div class="card-example">"%s"</div><div class="card-audio">%s</div></div>\n'
                         '      </div>' % (grad, icon_svg(v['icon']), hint, v['word'], hint, v['ex'],
                                           listen_btn(v['word'], stop=True)))
        body = ('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
                '<span id="vocabCount%d">0 / 6 words revealed</span></p>\n'
                '    <div class="vocab-grid" id="vocabGrid%d">\n%s\n    </div>' % (grp + 1, grp + 1, '\n'.join(cards)))
        out.append(light_slide(nxt(), 2, T['vocab%d' % (grp + 1)], 'Vocabulary',
                               'Words <span class="accent">%s</span>' % ('1-6' if grp == 0 else '7-12'), body))

    out.append(light_slide(nxt(), 2, T['matching'], 'Consolidate', 'Match the <span class="accent">Meaning</span>',
                           '    <!--IC-BLOCKS:vocab-->'))

    rows = ''.join('<div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;'
                   'padding:1rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
                   '<span style="font-size:1.05rem;font-weight:600">%s</span>%s</div>' % (p, listen_btn(p))
                   for p in L['pron'])
    body = '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:560px;margin:1.2rem auto 0">%s</div>' % rows
    out.append(light_slide(nxt(), 2, T['pron'], 'Review', 'Say It <span class="accent">Clearly</span>', body))

    items = ''.join('<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">%s'
                    '<span class="fill-blank">___</span><span class="fill-answer">%s</span>%s</div></div>'
                    % (pre, ans, post) for pre, ans, post in L['gapfill'])
    body = '    <div class="fill-grid">%s</div>' % items
    out.append(light_slide(nxt(), 2, T['gapfill'], 'In Context', 'Fill the <span class="accent">Gap</span>', body,
                           note='Say the missing word first, then click to check'))

    # ---- chapter 3
    c3 = L['ch3']
    out.append(img_slide(nxt(), 3, T['ch3_trans'], imgs['ch3'], 'Chapter 3: %s' % L['phases'][2],
                         c3['heading'], c3['sub']))

    if reading:
        out.append(light_slide(nxt(), 3, T['reading'], 'Read for the Main Idea', L['reading']['heading'],
                               '    <!--IC-BLOCKS:reading-->'))
        out.append(light_slide(nxt(), 3, T['tf'], 'Check Understanding', 'True or <span class="accent">False?</span>',
                               '    <!--IC-BLOCKS:tf-->',
                               note='Decide first, then tap to reveal the answer and why'))

    d = L['dialogue']
    lines = []
    for i, (who, txt) in enumerate(d['lines']):
        cls = 'ana' if who == 'ana' else d['guest_key']
        voice = 'ellen' if who == 'ana' else d['guest_voice']
        initial = 'A' if who == 'ana' else d['guest_name'][0].upper()
        lines.append('      <div class="dialogue-line%s" data-line="%d" data-voice="%s">'
                     '<div class="dialogue-avatar %s">%s</div>'
                     '<div class="dialogue-bubble %s-bubble">%s</div></div>'
                     % (' visible' if i == 0 else '', i + 1, voice, cls, initial, cls, txt))
    out.append('''<div class="slide slide-dark" data-slide="%d" data-phase="3" data-teacher="%s">
  <div class="slide-inner">
    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">%s</h2>
    <div class="dialogue-box" id="dialogueBox">
%s
    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>
  </div>
</div>
''' % (nxt(), esc(T['dialogue']), d['heading'], '\n'.join(lines)))

    out.append(light_slide(nxt(), 3, T['dialogue_comp'], 'Comprehension',
                           'About <span class="accent">%s</span>' % d['guest_name'], comp_block(d['comp'])))

    l1 = L['listenings'][0]
    out.append(player('mp-listen1', '/audio/%s/a%d_listening1.mp3' % (SLUG, n), 'waveform1', 'listening1Qs',
                      l1['qs'], l1['title'], None, l1['blurb'], nxt(), 3, T['listening1'], 'Listening'))

    # ---- chapter 4
    g = L['grammar']
    out.append(img_slide(nxt(), 4, T['ch4_trans'], imgs['ch4'], 'Chapter 4: %s' % L['phases'][3],
                         g['chapter_heading'], g['chapter_sub']))

    exs = ''.join('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;'
                  'display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
                  '<p style="font-size:.92rem">"%s"</p>%s</div>' % (e, listen_btn(e)) for e in g['examples'])
    rule_rows = ''.join('<tr style="%sborder-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">%s</td>'
                        '<td style="padding:.5rem">%s</td><td style="padding:.5rem">%s</td></tr>'
                        % ('background:var(--bg-elevated);' if i % 2 else '', a, b, c)
                        for i, (a, b, c) in enumerate(g['rule_rows']))
    body = ('    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:640px;margin:1rem auto 0">%s</div>\n'
            '    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">%s</p>\n'
            '    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;'
            'border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" '
            'onclick="var t=document.getElementById(\'rule1\');t.style.display=(t.style.display===\'none\'||!t.style.display)?\'block\':\'none\'">Reveal the Rule</button>\n'
            '    <div id="rule1" style="display:none;max-width:660px;margin:1rem auto 0;overflow-x:auto">\n'
            '      <table style="width:100%%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);'
            'border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
            '        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Form</th>'
            '<th style="padding:.6rem;text-align:left">What it does</th>'
            '<th style="padding:.6rem;text-align:left">Example</th></tr></thead>\n'
            '        <tbody>%s</tbody>\n      </table>\n'
            '      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">In one line: '
            '<strong>%s</strong></p>\n    </div>' % (exs, g['prompt'], rule_rows, g['oneliner']))
    out.append(light_slide(nxt(), 4, T['grammar'], 'Grammar Discovery', g['heading'], body))

    svg_x = ('<svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><circle cx="12" cy="12" r="10"/>'
             '<line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>')
    svg_v = ('<svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>'
             '<polyline points="22 4 12 14.01 9 11.01"/></svg>')
    mi = []
    for wrong, right in L['mistakes']:
        mi.append('      <div class="mistake-item mistake-wrong"><div class="mistake-icon">%s</div>\n        "%s"\n      </div>'
                  % (svg_x, wrong))
        mi.append('      <div class="mistake-item mistake-right"><div class="mistake-icon">%s</div>\n        "%s"\n      </div>'
                  % (svg_v, right))
    body = ('    <div class="mistake-card">\n%s\n    </div>\n'
            '    <p style="text-align:center;margin-top:2rem;font-size:.9rem;color:var(--text-dim)">%s</p>'
            % ('\n'.join(mi), L['mistake_note']))
    out.append(light_slide(nxt(), 4, T['mistake'], 'Common Mistake', 'Right vs <span class="accent">Wrong</span>', body))

    items = ''.join('<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">%s'
                    '<span class="fill-blank">___</span><span class="fill-answer">%s</span>%s</div></div>'
                    % (pre, ans, post) for pre, ans, post in L['practice_fill'])
    out.append(light_slide(nxt(), 4, T['practice'], 'Practice', L['practice_heading'],
                           '    <div class="fill-grid">%s</div>' % items,
                           note='Say it first, then click to check'))

    l2 = L['listenings'][1]
    out.append(player('mp-listen2', '/audio/%s/a%d_listening2.mp3' % (SLUG, n), 'waveform2', 'listening2Qs',
                      l2['qs'], l2['title'], None, l2['blurb'], nxt(), 4, T['listening2'], 'Listening 2'))

    a = L['artifact']
    art_rows = ''.join('<div style="display:flex;padding:.5rem 0;%s"><span style="flex:0 0 %s;font-weight:700;'
                       'color:var(--accent)">%s</span><span style="flex:1">%s</span></div>'
                       % ('' if i == len(a['rows']) - 1 else 'border-bottom:1px solid var(--border)',
                          a.get('label_width', '96px'), k, v)
                       for i, (k, v) in enumerate(a['rows']))
    body = ('    <div style="max-width:540px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);'
            'border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.06)">\n'
            '      <div style="background:var(--accent);color:#fff;padding:.9rem 1.2rem;display:flex;'
            'justify-content:space-between;align-items:center">\n'
            '        <div><div style="font-weight:700;font-size:.95rem">%s</div>'
            '<div style="font-size:.72rem;opacity:.92">%s</div></div>\n'
            '        <div style="font-size:.72rem;text-align:right;line-height:1.4">%s</div>\n'
            '      </div>\n'
            '      <div style="padding:1rem 1.2rem;font-size:.86rem">%s</div>\n'
            '    </div>\n%s'
            % (a['title'], a['subtitle'], a['corner'], art_rows,
               comp_block(a['comp']).replace('gap:1rem', 'gap:.7rem').replace(
                   'display:flex;flex-direction:column', 'display:flex;flex-direction:column')))
    out.append(light_slide(nxt(), 4, T['artifact'], 'Real Document', a['heading'], body))

    # ---- chapter 5
    out.append(img_slide(nxt(), 5, T['ch5_trans'], imgs['ch5'], 'Chapter 5: %s' % L['phases'][4],
                         'Train Like a <span class="accent">Pro</span>', 'Detective &middot; Quick Fire &middot; Building'))

    cards = ''.join('<div class="error-card" onclick="revealError(this)"><div class="error-sentence">"%s"</div>'
                    '<div class="error-fix">"%s"</div></div>' % (w, r) for w, r in L['mistakes'])
    body = ('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
            '<span id="errorScore">0 / %d errors found</span></p>\n'
            '    <div class="error-grid" id="errorGrid">%s</div>' % (len(L['mistakes']), cards))
    out.append(light_slide(nxt(), 5, T['detective'], 'Detective', 'Spot the <span class="accent">Error</span>', body))

    out.append('''<div class="slide slide-light" data-slide="%d" data-phase="5" data-teacher="%s">
  <div class="slide-inner">
    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Answer on the <span class="accent">Spot</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:500px">Read each situation. Answer out loud, then tap Tips for support language.</p>
    <!--IC-BLOCKS:quickfire-->
  </div>
</div>
''' % (nxt(), esc(T['quickfire'])))

    qs = ''.join('<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem">'
                 '<p style="font-size:.88rem;margin-bottom:.4rem"><strong>%d.</strong> "%s"</p>'
                 '<p style="font-size:.82rem;color:var(--accent);cursor:pointer" data-t="Show Answer" data-a="%s" '
                 'onclick="this.textContent=this.textContent===this.dataset.t?this.dataset.a:this.dataset.t">Show Answer</p></div>'
                 % (i + 1, q, esc(ans)) for i, (q, ans) in enumerate(L['speaking']))
    body = '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:620px;margin:1.2rem auto 0">%s</div>' % qs
    out.append(light_slide(nxt(), 5, T['speaking'], 'Speaking', 'Your Own <span class="accent">Answers</span>', body))

    items = ''.join('<div class="oral-item" onclick="this.classList.toggle(\'revealed\')">'
                    '<div class="oral-situation">%d. %s</div><div class="oral-model">"%s"</div></div>'
                    % (i + 1, sit, mod) for i, (sit, mod) in enumerate(L['building']))
    out.append(light_slide(nxt(), 5, T['building'], 'Build', 'Sentence <span class="accent">Building</span>',
                           '    <div class="oral-grid">%s</div>' % items,
                           note='Say the full sentence, then click to compare'))

    out.append('''<div class="slide slide-light" data-slide="%d" data-phase="5" data-teacher="%s">
  <div class="slide-inner">
    <div class="chapter-label">Check Your Work</div>
    <h2 class="slide-heading">%s</h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:480px">Try everything first. Open the key only to compare.</p>
    <div style="max-width:560px;margin:1rem auto 0">
      <!--IC-BLOCKS:answerkey-->
    </div>
  </div>
</div>
''' % (nxt(), esc(T['answerkey']), L['answerkey_heading']))

    # ---- chapter 6
    rp = L['roleplays']
    out.append(img_slide(nxt(), 6, T['ch6_trans'], imgs['ch6'], 'Chapter 6: %s' % L['phases'][5],
                         L['rp_chapter_heading'], 'Guided &gt; Semi-free &gt; Free'))

    grads_rp = ['linear-gradient(135deg,var(--accent-dim),rgba(8,145,178,.05))',
                'linear-gradient(135deg,rgba(8,145,178,.08),rgba(8,145,178,.02))',
                'linear-gradient(135deg,rgba(8,145,178,.12),rgba(8,145,178,.03))']
    labels = ['Role-Play 1 of 3 &mdash; Guided', 'Role-Play 2 of 3 &mdash; Semi-free', 'Role-Play 3 of 3 &mdash; Free']
    for i, r in enumerate(rp):
        if r.get('chips'):
            chips = ('      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keyword chips:</p>'
                     '<div style="display:flex;flex-wrap:wrap;gap:.4rem">%s</div>'
                     % ''.join('<span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;'
                               'padding:.3rem .7rem;font-size:.8rem">%s</span>' % c for c in r['chips']))
        else:
            chips = '      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">%s</p>' % r['footer']
        body = ('    <div class="roleplay-body" style="max-width:520px;margin:1rem auto 0;background:%s;'
                'border:1px solid var(--accent);border-radius:12px;padding:1.5rem">\n'
                '      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> %s</p>\n'
                '%s\n    </div>' % (grads_rp[i], r['scenario'], chips))
        out.append(light_slide(nxt(), 6, T['rp%d' % (i + 1)], labels[i], r['heading'], body))

    # ---- chapter 7
    out.append(img_slide(nxt(), 7, T['ch7_trans'], imgs['ch7'], 'Chapter 7: %s' % L['phases'][6], L['wrap_heading']))

    rows = ''.join('<div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;'
                   'padding:.9rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
                   '<span style="font-size:.92rem;color:#fff">%s</span>%s</div>' % (p, listen_btn(p))
                   for p in L['survival'])
    out.append('''<div class="slide slide-dark" data-slide="%d" data-phase="7" data-teacher="%s">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Survival Card</div>
    <h2 class="slide-heading" style="color:#fff">%s</h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1.2rem auto 0;text-align:left">%s</div>
  </div>
</div>
''' % (nxt(), esc(T['survival']), L['survival_heading'], rows))

    checks = ''.join('<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">'
                     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
                     '<polyline points="20 6 9 17 4 12"/></svg></div>%s</div>' % c for c in L['checklist'])
    out.append('''<div class="slide slide-dark" data-slide="%d" data-phase="7" data-teacher="%s">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Can Do Now</span></h2>
    <div class="check-grid" style="max-width:560px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">%s</div>
  </div>
</div>
''' % (nxt(), esc(T['checklist']), checks))

    b = L['badge']
    out.append('''<div class="slide slide-dark" data-slide="%d" data-phase="7" data-teacher="%s">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Lesson Complete</div>
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">%s Badge <span class="accent">Earned!</span></h2>
      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">%s</p>
      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson %d -- Complete.</p>
      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: %s</p>
    </div>
  </div>
</div>
''' % (nxt(), esc(T['badge']), b['name'], b['text'], n, b['next']))

    return '\n'.join(out), s


# ---------------------------------------------------------------- pre-class
def shuffled(seq, seed):
    """Embaralho deterministico (REGRA 24: opcao nunca na mesma posicao da palavra)."""
    out = list(seq)
    k = len(out)
    st = seed * 2654435761 % 4294967296
    for i in range(k - 1, 0, -1):
        st = (st * 1103515245 + 12345) % 2147483648
        j = st % (i + 1)
        out[i], out[j] = out[j], out[i]
    return out


def render_preclass(L):
    n = L['n']
    p = L['pc']
    vocab = L['vocab']
    out = []
    out.append('<div class="lesson-card" id="ex-lesson-%d">' % n)
    out.append('  <div class="lesson-header" onclick="toggleLesson(this)">')
    out.append('    <div class="lesson-header-img" style="background-image:url(\'%s\')"></div>' % L['imgs']['card'])
    out.append('    <div class="lesson-header-content">')
    out.append('      <div class="lesson-number">Lesson %d -- Pre-class</div>' % n)
    out.append('      <h3>%s</h3>' % p['title'])
    out.append('      <div class="lesson-desc">%s Key words: %s. Structure: %s.</div>'
               % (p['desc'], ', '.join(v['word'].lower() for v in vocab), L['grammar_point']))
    out.append('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" '
               'data-lesson-progress="%d" style="width:0%%"></div></div>'
               '<span class="mini-percent" data-lesson-pct="%d">0%%</span></div>' % (n, n))
    out.append('    </div>')
    out.append('    <div class="expand-icon">&#9660;</div>')
    out.append('  </div>')
    out.append('  <div class="lesson-body">')
    out.append('')

    # 1.1 vocab cards
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4>'
               '<span class="badge badge-vocab">Vocabulary</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Listen to each word and read the example. Tap Listen to hear it.</p>')
    out.append('      <div class="vocab-cards">')
    for v in vocab:
        out.append('        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
                   '<span class="vocab-card-word">%s</span><span class="vocab-card-dot"> -- </span>'
                   '<span class="vocab-card-def">%s</span></div>'
                   '<div class="vocab-card-example">"%s"</div></div>'
                   '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
                   % (v['word'], v['def'][0].lower() + v['def'][1:], v['ex'], esc(v['word'])))
    out.append('      </div>')
    out.append('    </div>')
    out.append('')

    # 1.2 matching
    matches = [v['match'] for v in vocab]
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4>'
               '<span class="badge badge-practice">Practice</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Choose the meaning of each word.</p>')
    out.append('      <div class="match-grid" id="match-l%d">' % n)
    for i, v in enumerate(vocab):
        opts = ''.join('<option value="%s">%s</option>' % (esc(m), m) for m in shuffled(matches, n * 100 + i + 1))
        out.append('        <div class="match-row" data-answer="%s"><span class="match-word" style="flex:0 0 190px">%s</span>'
                   '<select style="flex:1;width:100%%" onchange="checkMatch(this)"><option value="">Select...</option>%s</select></div>'
                   % (esc(v['match']), v['word'], opts))
    out.append('      </div>')
    out.append('      <button class="verify-all-btn" onclick="verifyAllMatches(\'match-l%d\')">Check Answers</button>' % n)
    out.append('    </div>')
    out.append('')

    # 1.3 grammar in context
    paras = ''.join('<p%s>%s</p>' % ('' if i == 0 else ' style="margin-top:.6rem"', t)
                    for i, t in enumerate(p['context_paras']))
    quiz = ''.join(
        '<div class="quiz-item"><div class="quiz-question">%d. %s</div><div class="quiz-options">%s</div></div>'
        % (i + 1, q, ''.join('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s">'
                             '<span class="option-letter">%s</span> %s</div>'
                             % ('true' if ok else 'false', 'ABC'[j], txt) for j, (txt, ok) in enumerate(opts)))
        for i, (q, opts) in enumerate(p['context_quiz']))
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4>'
               '<span class="badge badge-vocab">GRAMMAR</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Read the text, then answer the questions.</p>')
    out.append('      <div class="context-text" style="background:var(--bg-card);border:1px solid var(--border);'
               'border-radius:10px;padding:1rem;font-size:.9rem;line-height:1.7;margin-bottom:1rem">')
    out.append('        %s' % paras)
    out.append('      </div>')
    out.append('      %s' % quiz)
    out.append('    </div>')
    out.append('')

    # 1.4 grammar tip
    rows = ''.join('<tr style="%sborder-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">%s</td>'
                   '<td style="padding:.5rem">%s</td><td style="padding:.5rem">%s</td></tr>'
                   % ('background:var(--bg-elevated);' if i % 2 else '', a, b, c)
                   for i, (a, b, c) in enumerate(p['tip_rows']))
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- %s</h4>'
               '<span class="badge badge-vocab">GRAMMAR</span></div>' % p['tip_title'])
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">%s</p>'
               % p['tip_sub'])
    out.append('      <div style="overflow-x:auto">')
    out.append('        <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);'
               'border:1px solid var(--border);border-radius:8px;overflow:hidden">')
    out.append('          <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Form</th>'
               '<th style="padding:.6rem;text-align:left">What it does</th>'
               '<th style="padding:.6rem;text-align:left">Example</th></tr></thead>')
    out.append('          <tbody>%s</tbody>' % rows)
    out.append('        </table>')
    out.append('      </div>')
    out.append('      <p style="font-size:.82rem;color:var(--danger);margin-top:.8rem"><strong>Never:</strong> %s</p>'
               % p['tip_never'])
    out.append('    </div>')
    out.append('')

    # 1.5 fill in the blank
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4>'
               '<span class="badge badge-practice">Practice</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Complete each sentence, then check your answer.</p>')
    for pre, ans, post, hint in p['fills']:
        phrase = ('%s%s%s' % (pre, ans, post)).replace('"', '').strip()
        out.append('      <div class="fill-blank-item"><div class="fill-blank-sentence">"%s<input class="blank-input" '
                   'data-answer="%s" data-hint="Hint: %s" data-phrase="%s" placeholder="___">%s"</div>'
                   '<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                   '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
                   % (pre, esc(ans), esc(hint), esc(phrase), post))
    out.append('    </div>')
    out.append('')

    # stage 2 ordering
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4>'
               '<span class="badge badge-order">Order</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">%s</p>'
               % p['order_intro'])
    out.append('      <div class="order-container" id="order-l%d">' % n)
    for i, txt in enumerate(p['order']):
        out.append('        <div class="order-item" draggable="true" data-order="%d" onclick="selectOrderItem(this,\'order-l%d\')">'
                   '<span class="order-num">?</span><span class="order-text">"%s"</span>'
                   '<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l%d\')">&#9650;</button>'
                   '<button class="arrow-btn" onclick="moveItem(this,1,\'order-l%d\')">&#9660;</button></span></div>'
                   % (i + 1, n, txt, n, n))
    out.append('      </div>')
    out.append('      <button class="verify-all-btn" onclick="checkOrder(\'order-l%d\')">Check Order</button>' % n)
    out.append('    </div>')
    out.append('')

    # stage 3 pronunciation
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4>'
               '<span class="badge badge-speak">Speaking</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Listen, then record yourself. You will get a word-by-word score.</p>')
    for phrase in L['survival']:
        out.append('      <div class="speech-card" data-phrase="%s">' % esc(phrase))
        out.append('        <div class="speech-phrase">%s</div>' % phrase)
        out.append('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
                   '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
                   '<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>')
        out.append('        <div class="speech-result"></div>')
        out.append('      </div>')
    out.append('    </div>')
    out.append('')

    # stage 4 situational quiz
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4>'
               '<span class="badge badge-quiz">Quiz</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Choose the answer that a real speaker would give.</p>')
    for q, opts in p['quiz']:
        o = ''.join('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s">'
                    '<span class="option-letter">%s</span> %s</div>'
                    % ('true' if ok else 'false', 'ABC'[j], txt) for j, (txt, ok) in enumerate(opts))
        out.append('      <div class="quiz-item"><div class="quiz-question">%s</div>'
                   '<div class="quiz-options">%s</div></div>' % (q, o))
    out.append('    </div>')
    out.append('')

    # stage 5 free production
    out.append('    <div class="exercise-section">')
    out.append('      <div class="section-header-row"><h4>Stage 5: Free Production</h4>'
               '<span class="badge badge-think">Reflection</span></div>')
    out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">'
               'Think, then record your answer. There is no wrong answer here.</p>')
    out.append('      <div class="think-card">')
    out.append('        <div class="think-question">%s</div>' % p['think'])
    out.append('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>'
               '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>')
    out.append('        <div id="think-result-l%d"></div>' % n)
    out.append('      </div>')
    out.append('    </div>')
    out.append('')

    # survival card
    out.append('    <div class="survival-card">')
    out.append('      <h4>Survival Card -- Lesson %d</h4>' % n)
    for i, phrase in enumerate(L['survival']):
        out.append('      <div class="survival-phrase"><span class="sp-num">%d</span><span class="sp-en">%s</span>'
                   '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
                   % (i + 1, phrase, esc(phrase)))
    out.append('    </div>')
    out.append('')
    out.append('  </div>')
    out.append('</div>')
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------- complementary
MEDIA_ICONS = {
    'video': ('<path d="M22 8.5a3 3 0 00-2.1-2.1C18 6 12 6 12 6s-6 0-7.9.4A3 3 0 002 8.5 31 31 0 002 12a31 31 0 00.1 '
              '3.5 3 3 0 002.1 2.1C6 18 12 18 12 18s6 0 7.9-.4a3 3 0 002.1-2.1A31 31 0 0022 12a31 31 0 00-.1-3.5z"/>'
              '<polygon points="10 9 15 12 10 15" fill="var(--accent)" stroke="none"/>'),
    'podcast': ('<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/>'
                '<line x1="12" y1="19" x2="12" y2="23"/>'),
    'film': '<path d="M3 21h18"/><path d="M5 21V9l5-4v16"/><path d="M14 21V11l5 3v7"/>',
}


def render_complementary(L):
    n = L['n']
    out = ['', '<h4 style="font-size:.95rem;margin-bottom:.8rem">Lesson %d -- %s</h4>' % (n, L['menu_title']), '']
    for m in L['complementary']:
        out.append('<div class="media-card-wrapper" data-media="l%d-%s">' % (n, m['slot']))
        out.append('  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>')
        out.append('  <div class="media-card">')
        out.append('    <div class="media-thumb"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" '
                   'stroke="var(--accent)" stroke-width="2">%s</svg></div>' % MEDIA_ICONS[m['icon']])
        out.append('    <div class="media-info">')
        out.append('      <div class="media-type">%s</div>' % m['type'])
        out.append('      <h5>%s</h5>' % m['title'])
        out.append('      <p>%s</p>' % m['desc'])
        out.append('      <p class="media-tip">Tip: %s</p>' % m['tip'])
        out.append('      <a href="%s" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;'
                   'font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;'
                   'border-bottom:1px solid var(--accent)">%s &#8599;</a>' % (m['url'], m['cta']))
        out.append('    </div>')
        out.append('  </div>')
        out.append('</div>')
        out.append('')
    return '\n'.join(out)


# ---------------------------------------------------------------- config
def render_config(L, nslides):
    n = L['n']
    d = L['dialogue']
    voices = {'arthur': VOICES['arthur'], 'ellen': VOICES['ellen']}
    for key in [d['guest_voice']] + [x['voice'] for x in L['listenings']]:
        voices[key] = VOICES[key]
    chars = {'ana': 'ellen', d['guest_key']: d['guest_voice']}
    assert 'helen' not in json.dumps(chars).lower(), 'personagem nao pode conter "helen" (assert do builder)'

    # matching do IN CLASS: a letra de cada palavra aponta para a def certa, ja embaralhada
    order = [v['match'][0].upper() + v['match'][1:] for v in L['vocab'][:8]]
    shuf = shuffled(order, n * 7 + 3)
    blocks = {
        'vocab': [
            {'kind': 'matching', 'title': 'Match each word to its meaning',
             'words': [[str(i + 1), v['word'], 'abcdefgh'[shuf.index(order[i])]]
                       for i, v in enumerate(L['vocab'][:8])],
             'defs': [[c, m] for c, m in zip('abcdefgh', shuf)]},
            {'kind': 'vocabnote', 'text': L['vocabnote']},
        ],
        'quickfire': [{'kind': 'quickfire', 'items': L['quickfire']}],
        'answerkey': [{'kind': 'answer', 'title': L['answerkey_title'], 'key': L['answerkey']}],
    }

    if L.get('model') == 'reading':
        r = L['reading']
        blocks['reading'] = [
            {'kind': 'reading', 'rtitle': r['rtitle'], 'paras': r['paras'], 'source': 'Adapted for Lesson %d' % n},
            {'kind': 'gist', 'prompt': r['gist_prompt'],
             'choices': [[c, t, ok] for c, (t, ok) in zip('abc', r['gist_choices'])]},
        ]
        blocks['tf'] = [{'kind': 'tf', 'items': [[s, v, j] for s, v, j in r['tf']]}]

    cfg = {
        'slug': SLUG,
        'student_name': 'Ana Claudia Veraldi',
        'first_name': 'Ana',
        'gender': 'f',
        'program': 'Ingl&#234;s Geral &amp; Intercultural -- Flu&#234;ncia e Autonomia',
        'total_aulas': 40,
        'palette': PALETTE,
        'header': HEADER,
        'hub_subtitle': 'Ingl&#234;s para a vida real &mdash; falar, entender qualquer sotaque e ter autonomia no idioma',
        'voices': voices,
        'characters': chars,
        'stamps': STAMPS,
        'lesson': {
            'n': n,
            'menu_num': str(n),
            'menu_title': L['menu_title'],
            'menu_desc': '%s -- %d slides' % (L['menu_desc'], nslides),
            'subtitle': 'Lesson %d -- %s' % (n, L['menu_title']),
            'title_tag': 'Professor View -- Ana Claudia Veraldi | Lesson %d -- %s' % (n, L['menu_title']),
            'phases': L['phases'],
            'listenings': [{'file': 'a%d_listening%d.mp3' % (n, i + 1), 'voice': x['voice'], 'text': x['text']}
                           for i, x in enumerate(L['listenings'])],
            'extra_audio': [{'key': '[order-l%d]' % n, 'file': 'pc_order_l%d.mp3' % n, 'voice': 'arthur',
                             'text': ' '.join(L['pc']['order'])}],
            'inclass_blocks': blocks,
            'grammar_point': L['grammar_point'],
        },
        'hub': 'snippets',
    }
    return cfg


# ---------------------------------------------------------------- main
def main():
    n = int(sys.argv[1])
    d = os.path.join(ROOT, '_build', '%s-aula%d' % (SLUG, n))
    spec = importlib.util.spec_from_file_location('content%d' % n, os.path.join(d, 'content.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    L = mod.LESSON
    assert L['n'] == n
    assert (L.get('model') == 'reading') == (n % 2 == 0), \
        'REGRA 29: aula PAR = modelo leitura, aula IMPAR = modelo fala'

    slides, nslides = render_slides(L)
    open(os.path.join(d, 'slides.html'), 'w', encoding='utf-8').write(slides)
    open(os.path.join(d, 'preclass.html'), 'w', encoding='utf-8').write(render_preclass(L))
    open(os.path.join(d, 'complementary.html'), 'w', encoding='utf-8').write(render_complementary(L))
    cfg = render_config(L, nslides)
    open(os.path.join(d, 'config.json'), 'w', encoding='utf-8').write(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')
    print('OK aula %d: %d slides -> %s' % (n, nslides, os.path.relpath(d, ROOT)))


if __name__ == '__main__':
    main()
