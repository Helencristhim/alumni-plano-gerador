#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de INSUMO das aulas da Ana Claudia Veraldi (V3).

NAO substitui o builder (REGRA 20). Ele so emite os TRES arquivos de conteudo que o
`_build/model/build_from_model.py` consome (slides.html, preclass.html,
complementary.html) + o config.json, a partir de um `content.py` com o conteudo
PEDAGOGICO da aula (vocabulario, textos, dialogo, perguntas, midia).

Por que existir: as 14 aulas do lote 7-20 tem de ser estruturalmente IDENTICAS
(REGRA 11, item 9 -- uniformidade visual). Escrever 600 linhas de HTML a mao por
aula convida divergencia silenciosa entre a aula 7 e a aula 20. Aqui a FORMA e
uma so, e o que muda de aula para aula e so o CONTEUDO.

USO (da raiz do repo):
    python3 _build/ana-claudia-veraldi-gen.py 7
    -> le  _build/ana-claudia-veraldi-aula7/content.py  (dict `LESSON`)
    -> escreve slides.html / preclass.html / complementary.html / config.json
"""
import importlib.util
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'ana-claudia-veraldi'

VOICES = {
    'arthur': 'sfJopaWaOtauCD3HKX6Q',        # american male (neutro)
    'ellen': 'BIvP0GN1cAtSRTxNHnWS',         # american female (voz da Ana)
    'american_f': 'EXAVITQu4vr4xnSDxMaL',    # Sarah -- 2a americana
    'british_m': 'JBFqnCBsd6RMkjVDRZzb',     # George
    'british_f': 'Xb7hH8MSUJpSbSDYk0k2',     # Alice
    'australian_m': 'Ziqfyey5k3R3GRC5abi8',  # Steve
    'australian_f': 'IwFADcBfc7Yo8KGhxTR5',  # Zoe
    'dutch_m': 'SVmtrm5iuquj8zKn5ZMg',       # Accent NL - Will
    'german_f': 'e08a4DxAw2gRDHs73Vg0',      # Accent DE - Charlotte
    'french_f': 'dTmTLshIypwp08eftJH6',      # Accent FR - Sylvie
    'french_m': '1a6onbE6zC5AwIN3pEp0',      # Nicolas
    'italian_f': 'NeTWyxKL7qMefrZEowed',     # Accent IT - Silvia
    'italian_m': 'vsxj8mTkgBSaMoGnPGc9',     # Valentino
    'nordic_m': '6moWX0dfuSmryJkGegeK',      # Accent NO - Birk
    'nordic_f': 'oVXQ3H21hRI9OtM4YH5K',      # Accent NORDIC - Freya
    'indian_f': 'fBJDfBxPazPKo9oZ1P8t',      # Anya
}

STAMPS = [
    {"id": 1, "label": "First Words",
     "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=200&q=80"},
    {"id": 2, "label": "Your Story",
     "img": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=200&q=80"},
    {"id": 3, "label": "The Code",
     "img": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=200&q=80"},
    {"id": 4, "label": "Many Englishes",
     "img": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=200&q=80"},
    {"id": 5, "label": "Confident Voice",
     "img": "https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?w=200&q=80"},
]

# ---------------------------------------------------------------- primitivas
SPK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
       '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
       '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

# Icones SVG (lucide style) usados nos reveal cards. Chave = nome curto no content.
ICONS = {
    'arrow': '<path d="M4 20V9a3 3 0 013-3h9"/><polyline points="13 3 17 6 13 9"/>',
    'tool': '<path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.8-3.8a6 6 0 01-7.9 7.9l-6.9 6.9a2.1 2.1 0 01-3-3l6.9-6.9a6 6 0 017.9-7.9l-3.8 3.8z"/>',
    'brush': '<path d="M18 3a3 3 0 00-3 3v6H9V6a3 3 0 00-6 0v9a6 6 0 0012 0V6a3 3 0 00-3-3z"/>',
    'home': '<path d="M3 10l9-7 9 7v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'star': '<path d="M12 2l3 6.6 7.2.9-5.3 4.9 1.4 7.1L12 18l-6.3 3.5 1.4-7.1L1.8 9.5 9 8.6z"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'layers': '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'map': '<polygon points="1 6 8 3 16 6 23 3 23 18 16 21 8 18 1 21"/><line x1="8" y1="3" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="21"/>',
    'chat': '<path d="M21 11.5a8.4 8.4 0 01-9 8.4 8.5 8.5 0 01-3.8-.9L3 21l2-5.2A8.4 8.4 0 014.1 12a8.4 8.4 0 018.4-8.4h.5a8.4 8.4 0 018 8z"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    'key': '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.7 12.3L21 2"/><path d="M17 6l3 3"/>',
    'leaf': '<path d="M11 20A7 7 0 019.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.7 4.5-7"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="M4.9 4.9l1.4 1.4"/><path d="M17.7 17.7l1.4 1.4"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="M4.9 19.1l1.4-1.4"/><path d="M17.7 6.3l1.4-1.4"/>',
    'moon': '<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>',
    'compass': '<circle cx="12" cy="12" r="10"/><polygon points="16.2 7.8 14.1 14.1 7.8 16.2 9.9 9.9"/>',
    'anchor': '<circle cx="12" cy="5" r="3"/><line x1="12" y1="22" x2="12" y2="8"/><path d="M5 12H2a10 10 0 0020 0h-3"/>',
    'flag': '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    'gift': '<polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/>',
    'scale': '<path d="M12 3v18"/><path d="M5 7h14"/><path d="M7 7l-3 7h6z"/><path d="M17 7l-3 7h6z"/>',
    'wave': '<path d="M2 8c2.5 0 2.5 3 5 3s2.5-3 5-3 2.5 3 5 3 2.5-3 5-3"/><path d="M2 15c2.5 0 2.5 3 5 3s2.5-3 5-3 2.5 3 5 3 2.5-3 5-3"/>',
    'people': '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.9"/><path d="M16 3.1a4 4 0 010 7.8"/>',
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>',
    'bulb': '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a6 6 0 00-3.6 10.8c.6.5.9 1.2.9 1.9V15h5.4v-.3c0-.7.3-1.4.9-1.9A6 6 0 0012 2z"/>',
    'doc': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="14" x2="15" y2="14"/><line x1="9" y1="18" x2="13" y2="18"/>',
    'bridge': '<path d="M2 17h20"/><path d="M5 17V9"/><path d="M19 17V9"/><path d="M2 9h20"/><path d="M12 9V4"/>',
    'grid': '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/>',
    'plane': '<path d="M17.8 19.2L16 11l3.5-3.5a2.1 2.1 0 00-3-3L13 8 4.8 6.2a1 1 0 00-1 .3l-.9.9a1 1 0 00.3 1.6L9 12l-2 3H4l-1 2 4 1 1 4 2-1v-3l3-2 3.2 6.8a1 1 0 001.6.3l.9-.9a1 1 0 00.3-1z"/>',
    'ear': '<path d="M6 8.5a6.5 6.5 0 1113 0c0 6-6 6-6 10a3 3 0 01-6 0"/><path d="M9.5 8.5a3 3 0 013 3"/>',
}

GRADS = [
    '#0c4a6e,#0369a1', '#713f12,#a16207', '#450a0a,#b91c1c', '#1e293b,#475569',
    '#7c2d12,#ea580c', '#134e4a,#0d9488', '#4c1d95,#7c3aed', '#7f1d1d,#dc2626',
    '#1e3a8a,#3b82f6', '#14532d,#16a34a', '#78350f,#c2410c', '#312e81,#4f46e5',
]

# Fundos full-screen. Todos ja usados nas aulas 1-6 da propria aluna, portanto
# verificados 200 (REGRA: zero imagem externa quebrada).
BG_POOL = [
    '1416339306562-f3d12fefd36f', '1416879595882-3373a0480b5b', '1444723121867-7a241cacace9',
    '1449824913935-59a10b8d2000', '1449844908441-8829872d2607', '1449965408869-eaa3f722e40d',
    '1454165804606-c3d57bc86b40', '1470071459604-3b5ec3a7fe05', '1480714378408-67cf0d13bc1b',
    '1494526585095-c41746248156', '1500382017468-9049fed747ef', '1502672260266-1c1ef2d93688',
    '1502920917128-1aa500764cbd', '1503387762-592deb58ef4e', '1504148455328-c376907d081c',
    '1516156008625-3a9d6067fab5', '1518791841217-8f162f1e1131', '1519677100203-a0e668c92439',
    '1521737604893-d14cc237f11d', '1523413651479-597eb2da0ad6', '1526778548025-fa2f459cd5c1',
    '1543466835-00a7907e9de1', '1548199973-03cce0bbc87b', '1553531384-cc64ac80f931',
    '1587300003388-59208cc962cb',
]


def backgrounds(n, w=1400):
    """8 fundos por aula, rotacionando o pool -- nunca dois iguais na mesma aula."""
    k = (n * 3) % len(BG_POOL)
    ids = [BG_POOL[(k + i * 3) % len(BG_POOL)] for i in range(8)]
    return [f'https://images.unsplash.com/photo-{i}?w={w}&q=80' for i in ids]


def esc_attr(t):
    """Texto de conteudo -> atributo HTML. Aspa dupla vira entidade; apostrofo NAO
    (REGRA 7.1: o texto mora no atributo, apostrofo ali e caractere comum)."""
    return (t or '').replace('"', '&quot;')


def plain(t):
    """Texto sem tags, para data-speak/data-phrase."""
    return re.sub(r'<[^>]+>', '', t or '')


def listen_btn(text, stop=False):
    ev = 'event.stopPropagation();' if stop else ''
    return (f'<button class="audio-btn-sm" data-speak="{esc_attr(plain(text))}" '
            f'onclick="{ev}speakText(this.dataset.speak,this)">{SPK} Listen</button>')


def player(pid, src, wave, qid):
    return f'''<div class="waveform waveform-paused" id="{wave}">{'<div class="bar"></div>' * 20}</div>
    <div class="mock-player" id="{pid}" data-src="{src}" data-waveform="{wave}" data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">
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
    </div>'''


def comp_qs(items):
    return ''.join(
        f'<div class="comp-q" onclick="revealComp(this)"><div class="q-text">{i + 1}. {q}</div>'
        f'<div class="q-answer">{a}</div></div>'
        for i, (q, a) in enumerate(items))


def slide(n, cls, phase, teacher, inner, bg=None, center=False):
    style = ''
    if bg:
        style = (f' style="background-image:linear-gradient(rgba(8,18,28,.80),rgba(8,18,28,.92)),'
                 f'url(\'{bg}\');background-size:cover;background-position:center"')
    active = ' active' if n == 1 else ''
    ci = ' style="text-align:center"' if center else ''
    return (f'<div class="slide {cls}{active}" data-slide="{n}" data-phase="{phase}" '
            f'data-teacher="{esc_attr(teacher)}"{style}>\n  <div class="slide-inner"{ci}>\n{inner}\n  </div>\n</div>\n')


# ------------------------------------------------------------------- SLIDES
def build_slides(L):
    n = L['n']
    a = f'a{n}_'
    imgs = L['images']
    out = []
    s = [0]

    def nxt():
        s[0] += 1
        return s[0]

    # 1 TITLE
    out.append(slide(nxt(), 'slide-image', 1, L['teacher']['open'],
                     f'''    <div class="chapter-label">Lesson {n} &middot; {L['chapter_tag']}</div>
    <h1 class="slide-heading" style="font-size:2.5rem;color:#fff">{L['title_html']}</h1>
    <p style="color:rgba(255,255,255,.82);font-size:1.1rem;margin-top:1rem">{L['title_sub']}</p>''',
                     bg=imgs[0], center=True))

    # 2 WARM-UP + CALLBACK
    out.append(slide(nxt(), 'slide-dark', 1, L['teacher']['warmup'],
                     f'''    <div class="chapter-label">Chapter 1: {L['phases'][0]}</div>
    <h2 class="slide-heading" style="color:#fff">{L['warmup']['heading']}</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:1rem;max-width:640px;margin-left:auto;margin-right:auto">{L['warmup']['callback']}</p>
    <p style="color:var(--accent-light);font-size:.95rem;margin-top:1.4rem;font-weight:600">{L['warmup']['question']}</p>''',
                     bg=imgs[1], center=True))

    # 3 FRAMING
    steps = ''.join(
        f'<div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;'
        f'padding:.9rem;text-align:center"><p style="font-weight:700;font-size:.9rem">{i + 1}. {t}</p>'
        f'<p style="font-size:.78rem;color:var(--text-dim)">{d}</p></div>'
        for i, (t, d) in enumerate(L['framing']['steps']))
    out.append(slide(nxt(), 'slide-light', 1, L['teacher']['framing'],
                     f'''    <div class="chapter-label">Tonight&rsquo;s Goal</div>
    <h2 class="slide-heading">{L['framing']['heading']}</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;max-width:680px;margin:1.5rem auto 0">{steps}</div>
    <p style="text-align:center;font-size:.88rem;color:var(--text-dim);margin-top:1.2rem;max-width:600px;margin-left:auto;margin-right:auto">{L['framing']['note']}</p>'''))

    # 4 HOOK
    out.append(slide(nxt(), 'slide-light', 1, L['teacher']['hook'],
                     f'''    <div class="chapter-label">{L['hook']['label']}</div>
    <h2 class="slide-heading">{L['hook']['heading']}</h2>
    <div style="max-width:580px;margin:1.5rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem;text-align:center">
      <p style="font-size:1rem">{L['hook']['line1']}</p>
      <p style="font-size:.88rem;color:var(--text-dim);margin-top:.8rem">{L['hook']['line2']}</p>
    </div>'''))

    # 5 CH2 TRANSITION
    out.append(slide(nxt(), 'slide-image', 2, L['teacher']['tr_vocab'],
                     f'''    <div class="chapter-label">Chapter 2: {L['phases'][1]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{L['vocab_heading']}</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{L['vocab_sub']}</p>''',
                     bg=imgs[2], center=True))

    # 6/7 VOCAB
    def vocab_grid(items, gid, cid, offset):
        cards = ''
        for i, v in enumerate(items):
            g = GRADS[(offset + i) % len(GRADS)]
            ic = ICONS[v['icon']]
            d = ('EXPRESSION &mdash; ' + v['def']) if v.get('expr') else v['def']
            cards += (
                f'      <div class="vocab-card" onclick="revealVocab(this)">\n'
                f'        <div class="card-icon" style="background:linear-gradient(135deg,{g})">'
                f'<svg viewBox="0 0 24 24" fill="none" stroke="#fff">{ic}</svg>'
                f'<div class="card-hint">{d}</div></div>\n'
                f'        <div class="card-body"><div class="card-word">{v["word"]}</div>'
                f'<div class="card-def">{d}</div>'
                f'<div class="card-example">"{v["ex"]}"</div>'
                f'<div class="card-audio">{listen_btn(v["word"], stop=True)}</div></div>\n'
                f'      </div>\n')
        return (f'    <div class="chapter-label">Vocabulary</div>\n'
                f'    <h2 class="slide-heading">Words <span class="accent">{offset + 1}-{offset + len(items)}</span></h2>\n'
                f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">'
                f'<span id="{cid}">0 / {len(items)} words revealed</span></p>\n'
                f'    <div class="vocab-grid" id="{gid}">\n{cards}    </div>')

    voc = L['vocab']
    assert len(voc) == 12, 'a aula precisa de 12 itens de vocabulario (B2)'
    out.append(slide(nxt(), 'slide-light', 2, L['teacher']['vocab1'],
                     vocab_grid(voc[:6], 'vocabGrid1', 'vocabCount1', 0)))
    out.append(slide(nxt(), 'slide-light', 2, L['teacher']['vocab2'],
                     vocab_grid(voc[6:], 'vocabGrid2', 'vocabCount2', 6)))

    # 8 MATCHING (B2 block)
    out.append(slide(nxt(), 'slide-light', 2, L['teacher']['matching'],
                     '''    <div class="chapter-label">Consolidate</div>
    <h2 class="slide-heading">Match the <span class="accent">Meaning</span></h2>
    <!--IC-BLOCKS:vocab-->'''))

    # 9 PRONUNCIATION
    rows = ''.join(
        f'<div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;'
        f'padding:1rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
        f'<span style="font-size:1.05rem;font-weight:600">{p}</span>{listen_btn(p)}</div>'
        for p in L['pron'])
    out.append(slide(nxt(), 'slide-light', 2, L['teacher']['pron'],
                     f'''    <div class="chapter-label">Review</div>
    <h2 class="slide-heading">Say It <span class="accent">Clearly</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:560px;margin:1.2rem auto 0">{rows}</div>'''))

    # 10 VOCAB IN CONTEXT (gap-fill de vocabulario -- builder injeta o banco)
    items = ''.join(
        f'<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">'
        f'"{g["before"]}<span class="fill-blank">___</span><span class="fill-answer">{g["answer"]}</span>{g["after"]}"'
        f'</div></div>' for g in L['gapfill'])
    out.append(slide(nxt(), 'slide-light', 2, L['teacher']['gapfill'],
                     f'''    <div class="chapter-label">In Context</div>
    <h2 class="slide-heading">Fill the <span class="accent">Gap</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say the missing word first, then click to check</p>
    <div class="fill-grid">{items}</div>'''))

    # ---- CHAPTER 3
    out.append(slide(nxt(), 'slide-image', 3, L['teacher']['tr_ch3'],
                     f'''    <div class="chapter-label">Chapter 3: {L['phases'][2]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{L['ch3_heading']}</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{L['ch3_sub']}</p>''',
                     bg=imgs[3], center=True))

    if L.get('reading'):
        # modelo LEITURA (aula PAR): texto + gist, depois true/false
        out.append(slide(nxt(), 'slide-light', 3, L['teacher']['reading'],
                         f'''    <div class="chapter-label">Read for the Main Idea</div>
    <h2 class="slide-heading">{L['reading_heading']}</h2>
    <!--IC-BLOCKS:reading-->'''))
        out.append(slide(nxt(), 'slide-light', 3, L['teacher']['tf'],
                         '''    <div class="chapter-label">Check Understanding</div>
    <h2 class="slide-heading">True or <span class="accent">False?</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Decide first, then tap to reveal the answer and why</p>
    <!--IC-BLOCKS:tf-->'''))

    # DIALOGO (nos dois modelos)
    d = L['dialogue']
    lines = ''
    for i, ln in enumerate(d['lines']):
        who = 'ana' if ln['who'] == 'ana' else d['cls']
        voice = 'ellen' if ln['who'] == 'ana' else d['voice']
        av = 'A' if ln['who'] == 'ana' else d['initial']
        vis = ' visible' if i == 0 else ''
        lines += (f'      <div class="dialogue-line{vis}" data-line="{i + 1}" data-voice="{voice}">'
                  f'<div class="dialogue-avatar {who}">{av}</div>'
                  f'<div class="dialogue-bubble {who}-bubble">{ln["text"]}</div></div>\n')
    out.append(slide(nxt(), 'slide-dark', 3, L['teacher']['dialogue'],
                     f'''    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">{d['heading']}</h2>
    <div class="dialogue-box" id="dialogueBox">
{lines}    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>'''))

    out.append(slide(nxt(), 'slide-light', 3, L['teacher']['dialogue_comp'],
                     f'''    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">About <span class="accent">{d['name']}</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;max-width:540px;margin:1.2rem auto 0">{comp_qs(d['comp'])}</div>'''))

    # LISTENING 1
    l1 = L['listenings'][0]
    out.append(slide(nxt(), 'slide-dark', 3, L['teacher']['listen1'],
                     f'''    <div class="chapter-label">Listening</div>
    <h2 class="slide-heading" style="color:#fff">{l1['heading']}</h2>
    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{l1['intro']}</p>
    {player('mp-listen1', f'/audio/{SLUG}/{a}listening1.mp3', 'waveform1', 'listening1Qs')}
    <div class="comp-questions" id="listening1Qs" style="max-width:520px;margin:1.2rem auto 0">{comp_qs(l1['comp'])}</div>''',
                     center=True))

    # ---- CHAPTER 4: GRAMMAR
    out.append(slide(nxt(), 'slide-image', 4, L['teacher']['tr_grammar'],
                     f'''    <div class="chapter-label">Chapter 4: {L['phases'][3]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{L['grammar']['ch_heading']}</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{L['grammar']['ch_sub']}</p>''',
                     bg=imgs[4], center=True))

    ex = ''.join(
        f'<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
        f'padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
        f'<p style="font-size:.92rem">"{e}"</p>{listen_btn(e)}</div>'
        for e in L['grammar']['examples'])
    trows = ''
    for i, (form, does, samp) in enumerate(L['grammar']['table']):
        bg = 'background:var(--bg-elevated);' if i % 2 else ''
        trows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                  f'<td style="padding:.5rem;font-weight:600">{form}</td>'
                  f'<td style="padding:.5rem">{does}</td><td style="padding:.5rem">{samp}</td></tr>')
    out.append(slide(nxt(), 'slide-light', 4, L['teacher']['grammar'],
                     f'''    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">{L['grammar']['heading']}</h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:640px;margin:1rem auto 0">{ex}</div>
    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">{L['grammar']['prompt']}</p>
    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('rule1');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="rule1" style="display:none;max-width:660px;margin:1rem auto 0;overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Form</th><th style="padding:.6rem;text-align:left">What it does</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
        <tbody>{trows}</tbody>
      </table>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">In one line: <strong>{L['grammar']['oneliner']}</strong></p>
    </div>'''))

    # COMMON MISTAKE
    XS = ('<div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626">'
          '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/>'
          '<line x1="9" y1="9" x2="15" y2="15"/></svg></div>')
    OK = ('<div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a">'
          '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>'
          '<polyline points="22 4 12 14.01 9 11.01"/></svg></div>')
    mi = ''
    for w, r in L['mistakes']:
        mi += f'      <div class="mistake-item mistake-wrong">{XS}\n        "{w}"\n      </div>\n'
        mi += f'      <div class="mistake-item mistake-right">{OK}\n        "{r}"\n      </div>\n'
    out.append(slide(nxt(), 'slide-light', 4, L['teacher']['mistake'],
                     f'''    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>
    <div class="mistake-card">
{mi}    </div>
    <p style="text-align:center;margin-top:2rem;font-size:.9rem;color:var(--text-dim)">{L['mistake_note']}</p>'''))

    # GRAMMAR PRACTICE
    gp = ''.join(
        f'<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">'
        f'"{g["before"]}<span class="fill-blank">___</span><span class="fill-answer">{g["answer"]}</span>{g["after"]}" '
        f'({g["cue"]})</div></div>' for g in L['gpractice'])
    out.append(slide(nxt(), 'slide-light', 4, L['teacher']['gpractice'],
                     f'''    <div class="chapter-label">Practice</div>
    <h2 class="slide-heading">{L['gpractice_heading']}</h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say it first, then click to check</p>
    <div class="fill-grid">{gp}</div>'''))

    # LISTENING 2
    l2 = L['listenings'][1]
    out.append(slide(nxt(), 'slide-dark', 4, L['teacher']['listen2'],
                     f'''    <div class="chapter-label">Listening 2</div>
    <h2 class="slide-heading" style="color:#fff">{l2['heading']}</h2>
    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{l2['intro']}</p>
    {player('mp-listen2', f'/audio/{SLUG}/{a}listening2.mp3', 'waveform2', 'listening2Qs')}
    <div class="comp-questions" id="listening2Qs" style="max-width:520px;margin:1.2rem auto 0">{comp_qs(l2['comp'])}</div>''',
                     center=True))

    # ARTEFATO
    art = L['artifact']
    arows = ''.join(
        f'<div style="display:flex;padding:.5rem 0;{"" if i == len(art["rows"]) - 1 else "border-bottom:1px solid var(--border)"}">'
        f'<span style="flex:0 0 96px;font-weight:700;color:var(--accent)">{k}</span>'
        f'<span style="flex:1">{v}</span></div>'
        for i, (k, v) in enumerate(art['rows']))
    out.append(slide(nxt(), 'slide-light', 4, L['teacher']['artifact'],
                     f'''    <div class="chapter-label">Real Document</div>
    <h2 class="slide-heading">{art['heading']}</h2>
    <div style="max-width:540px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.06)">
      <div style="background:var(--accent);color:#fff;padding:.9rem 1.2rem;display:flex;justify-content:space-between;align-items:center">
        <div><div style="font-weight:700;font-size:.95rem">{art['doc_title']}</div><div style="font-size:.72rem;opacity:.92">{art['doc_sub']}</div></div>
        <div style="font-size:.72rem;text-align:right;line-height:1.4">{art['doc_right']}</div>
      </div>
      <div style="padding:1rem 1.2rem;font-size:.86rem">{arows}</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:540px;margin:1.2rem auto 0">{comp_qs(art['comp'])}</div>'''))

    # ---- CHAPTER 5: PRACTICE
    out.append(slide(nxt(), 'slide-image', 5, L['teacher']['tr_practice'],
                     f'''    <div class="chapter-label">Chapter 5: {L['phases'][4]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Train Like a <span class="accent">Pro</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Detective &middot; Quick Fire &middot; Building</p>''',
                     bg=imgs[5], center=True))

    det = ''.join(
        f'<div class="error-card" onclick="revealError(this)">'
        f'<div class="error-sentence">"{w}"</div><div class="error-fix">"{r}"</div></div>'
        for w, r in L['detective'])
    out.append(slide(nxt(), 'slide-light', 5, L['teacher']['detective'],
                     f'''    <div class="chapter-label">Detective</div>
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="errorScore">0 / {len(L['detective'])} errors found</span></p>
    <div class="error-grid" id="errorGrid">{det}</div>'''))

    out.append(slide(nxt(), 'slide-light', 5, L['teacher']['quickfire'],
                     '''    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Answer on the <span class="accent">Spot</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:500px">Read each situation. Answer out loud, then tap Tips for support language.</p>
    <!--IC-BLOCKS:quickfire-->'''))

    sp = ''.join(
        f'<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem">'
        f'<p style="font-size:.88rem;margin-bottom:.4rem"><strong>{i + 1}.</strong> "{q}"</p>'
        f'<p style="font-size:.82rem;color:var(--accent);cursor:pointer" data-t="Show Answer" '
        f'data-a="{esc_attr(ans)}" onclick="this.textContent=this.textContent===this.dataset.t?this.dataset.a:this.dataset.t">Show Answer</p></div>'
        for i, (q, ans) in enumerate(L['speaking']))
    out.append(slide(nxt(), 'slide-light', 5, L['teacher']['speaking'],
                     f'''    <div class="chapter-label">Speaking</div>
    <h2 class="slide-heading">Your Own <span class="accent">Answers</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:620px;margin:1.2rem auto 0">{sp}</div>'''))

    bl = ''.join(
        f'<div class="oral-item" onclick="this.classList.toggle(\'revealed\')">'
        f'<div class="oral-situation">{i + 1}. {sit}</div>'
        f'<div class="oral-model">"{mod}"</div></div>'
        for i, (sit, mod) in enumerate(L['build']))
    out.append(slide(nxt(), 'slide-light', 5, L['teacher']['build'],
                     f'''    <div class="chapter-label">Build</div>
    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say the full sentence, then click to compare</p>
    <div class="oral-grid">{bl}</div>'''))

    out.append(slide(nxt(), 'slide-light', 5, L['teacher']['answerkey'],
                     f'''    <div class="chapter-label">Check Your Work</div>
    <h2 class="slide-heading">{L['answerkey_heading']}</h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:480px">Try everything first. Open the key only to compare.</p>
    <div style="max-width:560px;margin:1rem auto 0">
      <!--IC-BLOCKS:answerkey-->
    </div>'''))

    # ---- CHAPTER 6: YOUR TURN
    out.append(slide(nxt(), 'slide-image', 6, L['teacher']['tr_roleplay'],
                     f'''    <div class="chapter-label">Chapter 6: {L['phases'][5]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{L['rp_ch_heading']}</h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Guided &gt; Semi-free &gt; Free</p>''',
                     bg=imgs[6], center=True))

    def rp(idx, label, heading, scen, chips, grad, teacher):
        ch = ''
        if chips:
            ch = ('<p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">Keyword chips:</p>'
                  '<div style="display:flex;flex-wrap:wrap;gap:.4rem">' + ''.join(
                      f'<span style="background:var(--bg-card);border:1px solid var(--accent);'
                      f'border-radius:20px;padding:.3rem .7rem;font-size:.8rem">{c}</span>' for c in chips)
                  + '</div>')
        else:
            ch = '<p style="font-size:.85rem;color:var(--text-dim);font-style:italic">No keywords, no notes, two minutes.</p>'
        return slide(nxt(), 'slide-light', 6, teacher, f'''    <div class="chapter-label">Role-Play {idx} of 3 &mdash; {label}</div>
    <h2 class="slide-heading">{heading}</h2>
    <div class="roleplay-body" style="max-width:520px;margin:1rem auto 0;background:linear-gradient(135deg,{grad});border:1px solid var(--accent);border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> {scen}</p>
      {ch}
    </div>''')

    g = L['roleplay']
    out.append(rp(1, 'Guided', g['guided']['heading'], g['guided']['scenario'], g['guided']['chips'],
                  'var(--accent-dim),rgba(8,145,178,.05)', L['teacher']['rp1']))
    out.append(rp(2, 'Semi-free', g['semi']['heading'], g['semi']['scenario'], g['semi']['chips'],
                  'rgba(8,145,178,.08),rgba(8,145,178,.02)', L['teacher']['rp2']))
    out.append(rp(3, 'Free', g['free']['heading'], g['free']['scenario'], None,
                  'rgba(8,145,178,.12),rgba(8,145,178,.03)', L['teacher']['rp3']))

    # ---- CHAPTER 7: WRAP-UP
    out.append(slide(nxt(), 'slide-image', 7, L['teacher']['tr_wrap'],
                     f'''    <div class="chapter-label">Chapter 7: {L['phases'][6]}</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{L['wrap_heading']}</h2>''',
                     bg=imgs[7], center=True))

    sv = ''.join(
        f'<div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;'
        f'padding:.9rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
        f'<span style="font-size:.92rem;color:#fff">{p}</span>{listen_btn(p)}</div>'
        for p in L['survival'])
    out.append(slide(nxt(), 'slide-dark', 7, L['teacher']['survival'],
                     f'''    <div class="chapter-label">Survival Card</div>
    <h2 class="slide-heading" style="color:#fff">{L['survival_heading']}</h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1.2rem auto 0;text-align:left">{sv}</div>''',
                     center=True))

    CHK = ('<div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>')
    ck = ''.join(f'<div class="check-item" onclick="toggleCheck(this)">{CHK}{c}</div>' for c in L['checklist'])
    out.append(slide(nxt(), 'slide-dark', 7, L['teacher']['checklist'],
                     f'''    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Can Do Now</span></h2>
    <div class="check-grid" style="max-width:560px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">{ck}</div>''',
                     center=True))

    out.append(slide(nxt(), 'slide-dark', 7, L['teacher']['closing'],
                     f'''    <div class="chapter-label">Lesson Complete</div>
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">{L['closing']['badge']}</h2>
      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">{L['closing']['text']}</p>
      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson {n} -- Complete.</p>
      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: {L['closing']['next']}</p>
    </div>''', center=True))

    return '\n'.join(out)


# ----------------------------------------------------------------- PRE-CLASS
def build_preclass(L):
    n = L['n']
    voc = L['vocab']

    cards = ''.join(
        f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
        f'<span class="vocab-card-word">{v["word"]}</span><span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{v["def"][0].lower() + v["def"][1:]}</span></div>'
        f'<div class="vocab-card-example">"{v["ex"]}"</div></div>'
        f'<button class="audio-btn" data-speak="{esc_attr(v["word"])}" '
        f'onclick="speakText(this.dataset.speak,this)">Listen</button></div>\n'
        for v in voc)

    # matching EMBARALHADO (REGRA 24), deterministico
    defs = [v['match'] for v in voc]
    assert len(set(defs)) == len(defs), 'definicoes de matching repetidas'
    rows = ''
    for i, v in enumerate(voc):
        rnd = random.Random(n * 1000 + i)
        opts = defs[:]
        while True:
            rnd.shuffle(opts)
            if opts.index(v['match']) != i:
                break
        options = '<option value="">Select...</option>' + ''.join(
            f'<option value="{o}">{o}</option>' for o in opts)
        rows += (f'        <div class="match-row" data-answer="{v["match"]}">'
                 f'<span class="match-word" style="flex:0 0 190px">{v["word"]}</span>'
                 f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{options}</select></div>\n')

    ctx = ''.join(f'<p{" style=\"margin-top:.6rem\"" if i else ""}>{p}</p>'
                  for i, p in enumerate(L['pc_context']['paras']))
    quiz = ''.join(
        f'<div class="quiz-item"><div class="quiz-question">{i + 1}. {q["q"]}</div><div class="quiz-options">'
        + ''.join(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
                  f'<span class="option-letter">{"ABC"[j]}</span> {t}</div>'
                  for j, (t, ok) in enumerate(q['opts']))
        + '</div></div>'
        for i, q in enumerate(L['pc_context']['quiz']))

    trows = ''
    for i, (form, does, samp) in enumerate(L['pc_tip']['table']):
        bg = 'background:var(--bg-elevated);' if i % 2 else ''
        trows += (f'<tr style="{bg}border-bottom:1px solid var(--border)">'
                  f'<td style="padding:.5rem;font-weight:600">{form}</td>'
                  f'<td style="padding:.5rem">{does}</td><td style="padding:.5rem">{samp}</td></tr>')

    blanks = ''
    for b in L['pc_blanks']:
        phrase = plain(b['before'] + b['answer'] + b['after'])
        blanks += (
            f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{b["before"]}'
            f'<input class="blank-input" data-answer="{esc_attr(b["answer"])}" '
            f'data-hint="{esc_attr(b["hint"])}" data-phrase="{esc_attr(phrase)}" placeholder="___">'
            f'{b["after"]}"</div>'
            f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')

    order = ''.join(
        f'        <div class="order-item" draggable="true" data-order="{i + 1}" '
        f'onclick="selectOrderItem(this,\'order-l{n}\')"><span class="order-num">?</span>'
        f'<span class="order-text">"{t}"</span><span class="order-arrows">'
        f'<button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{n}\')">&#9650;</button>'
        f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l{n}\')">&#9660;</button>'
        f'</span></div>\n' for i, t in enumerate(L['pc_order']))

    speech = ''.join(
        f'      <div class="speech-card" data-phrase="{esc_attr(p)}">\n'
        f'        <div class="speech-phrase">{p}</div>\n'
        f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
        f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
        f'<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
        f'        <div class="speech-result"></div>\n      </div>\n' for p in L['survival'])

    squiz = ''.join(
        f'      <div class="quiz-item"><div class="quiz-question">{q["q"]}</div><div class="quiz-options">'
        + ''.join(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{"true" if ok else "false"}">'
                  f'<span class="option-letter">{"ABC"[j]}</span> {t}</div>'
                  for j, (t, ok) in enumerate(q['opts']))
        + '</div></div>\n' for q in L['pc_squiz'])

    surv = ''.join(
        f'      <div class="survival-phrase"><span class="sp-num">{i + 1}</span>'
        f'<span class="sp-en">{p}</span>'
        f'<button class="audio-btn" data-speak="{esc_attr(p)}" '
        f'onclick="speakText(this.dataset.speak,this)">Listen</button></div>\n'
        for i, p in enumerate(L['survival']))

    return f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{L['images'][0].replace('w=1400', 'w=600')}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson {n:02d} -- Pre-class</div>
      <h3>{L['pc_title']}</h3>
      <div class="lesson-desc">{L['pc_desc']}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{cards}      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the meaning of each word.</p>
      <div class="match-grid" id="match-l{n}">
{rows}      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l{n}')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text, then answer the questions.</p>
      <div class="context-text" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem;font-size:.9rem;line-height:1.7;margin-bottom:1rem">
        {ctx}
      </div>
      {quiz}
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {L['pc_tip']['title']}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{L['pc_tip']['lead']}</p>
      <div style="overflow-x:auto">
        <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
          <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Form</th><th style="padding:.6rem;text-align:left">What it does</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
          <tbody>{trows}</tbody>
        </table>
      </div>
      <p style="font-size:.82rem;color:var(--danger);margin-top:.8rem"><strong>Never:</strong> {L['pc_tip']['never']}</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence, then check your answer.</p>
{blanks}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{L['pc_order_lead']}</p>
      <div class="order-container" id="order-l{n}">
{order}      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{n}')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen, then record yourself. You will get a word-by-word score.</p>
{speech}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the answer that a real speaker would give.</p>
{squiz}    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Think, then record your answer. There is no wrong answer here.</p>
      <div class="think-card">
        <div class="think-question">{L['pc_think']}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>
        <div id="think-result-l{n}"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson {n}</h4>
{surv}    </div>

  </div>
</div>
'''


# ------------------------------------------------------------- COMPLEMENTARES
THUMBS = {
    'video': '<path d="M22 8.5a3 3 0 00-2.1-2.1C18 6 12 6 12 6s-6 0-7.9.4A3 3 0 002 8.5 31 31 0 002 12a31 31 0 00.1 3.5 3 3 0 002.1 2.1C6 18 12 18 12 18s6 0 7.9-.4a3 3 0 002.1-2.1A31 31 0 0022 12a31 31 0 00-.1-3.5z"/><polygon points="10 9 15 12 10 15" fill="var(--accent)" stroke="none"/>',
    'podcast': '<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>',
    'doc': '<path d="M3 21h18"/><path d="M5 21V9l5-4v16"/><path d="M14 21V11l5 3v7"/>',
}


def build_complementary(L):
    n = L['n']
    out = [f'\n<h4 style="font-size:.95rem;margin-bottom:.8rem">Lesson {n} -- {L["menu_title"]}</h4>\n']
    for m in L['media']:
        out.append(f'''
<div class="media-card-wrapper" data-media="l{n}-{m['id']}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2">{THUMBS[m['thumb']]}</svg></div>
    <div class="media-info">
      <div class="media-type">{m['type']}</div>
      <h5>{m['title']}</h5>
      <p>{m['desc']}</p>
      <p class="media-tip">{m['tip']}</p>
      <a href="{m['url']}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">{m['cta']} &#8599;</a>
    </div>
  </div>
</div>
''')
    return ''.join(out)


# --------------------------------------------------------------------- CONFIG
def build_config(L, nslides):
    n = L['n']
    a = f'a{n}_'
    d = L['dialogue']
    used = {'arthur', 'ellen', d['voice']} | {l['voice'] for l in L['listenings']}
    voices = {k: VOICES[k] for k in ['arthur', 'ellen'] + sorted(used - {'arthur', 'ellen'})}
    listen = []
    for i, l in enumerate(L['listenings']):
        listen.append({'file': f'{a}listening{i + 1}.mp3', 'voice': l['voice'], 'text': l['text']})
    blocks = {
        'vocab': [
            {'kind': 'matching', 'title': 'Match each word to its meaning',
             'words': [[str(i + 1), v['word'], 'abcdef'[i]] for i, v in enumerate(L['vocab'][:6])],
             'defs': [['abcdef'[i], v['match'][0].upper() + v['match'][1:]]
                      for i, v in enumerate(L['vocab'][:6])]},
            {'kind': 'vocabnote', 'text': L['vocabnote']},
        ],
        'quickfire': [{'kind': 'quickfire', 'items': L['quickfire']}],
        'answerkey': [{'kind': 'answer', 'title': L['answerkey_title'], 'key': L['answerkey']}],
    }
    if L.get('reading'):
        blocks['reading'] = [
            {'kind': 'reading', 'rtitle': L['reading']['rtitle'], 'paras': L['reading']['paras'],
             'source': L['reading'].get('source', f'Adapted for Lesson {n}')},
            {'kind': 'gist', 'prompt': L['reading']['gist_prompt'], 'choices': L['reading']['gist']},
        ]
        blocks['tf'] = [{'kind': 'tf', 'items': L['reading']['tf']}]
    cfg = {
        'slug': SLUG,
        'student_name': 'Ana Claudia Veraldi',
        'first_name': 'Ana',
        'gender': 'f',
        'program': 'Ingl&#234;s Geral &amp; Intercultural -- Flu&#234;ncia e Autonomia',
        'total_aulas': 40,
        'palette': {'accent': '#0891b2', 'accent_light': '#22d3ee'},
        'header': ['B2 (Intermedi&#225;rio)', 'Interior de S&#227;o Paulo', '46 anos', '60 min &middot; Online'],
        'hub_subtitle': 'Ingl&#234;s para a vida real &mdash; falar, entender qualquer sotaque e ter autonomia no idioma',
        'voices': voices,
        'characters': {'ana': 'ellen', d['cls']: d['voice']},
        'stamps': STAMPS,
        'lesson': {
            'n': n,
            'menu_num': f'{n:02d}',
            'menu_title': L['menu_title'],
            'menu_desc': L['menu_desc'],
            'subtitle': f'Lesson {n} -- {L["menu_title"]}',
            'title_tag': f'Professor View -- Ana Claudia Veraldi | Lesson {n} -- {L["menu_title"]}',
            'phases': L['phases'],
            'listenings': listen,
            'extra_audio': [{'key': f'[order-l{n}]', 'file': f'pc_order_l{n}.mp3',
                             'voice': L.get('order_voice', 'arthur'),
                             'text': ' '.join(plain(t) for t in L['pc_order'])}],
            'inclass_blocks': blocks,
        },
        'hub': 'snippets',
    }
    if L.get('grammar_point'):
        cfg['lesson']['grammar_point'] = L['grammar_point']
    return cfg


# ----------------------------------------------------------------------- MAIN
def norm_vocab(w):
    w = re.sub(r'[^a-z ]', ' ', (w or '').lower())
    w = ' '.join(w.split())
    return re.sub(r'^(to be|to|a|an|the) ', '', w).strip()


def main():
    n = int(sys.argv[1])
    d = os.path.join(HERE, f'{SLUG}-aula{n}')
    spec = importlib.util.spec_from_file_location(f'content{n}', os.path.join(d, 'content.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    L = mod.LESSON
    assert L['n'] == n, 'content.py com numero de aula errado'
    L.setdefault('images', backgrounds(n))
    assert len(set(L['images'])) == 8, 'a aula precisa de 8 fundos distintos'

    # GATE local: toda resposta do gap-fill de vocab tem de ser palavra ensinada (REGRA 2.4)
    taught = {norm_vocab(v['word']) for v in L['vocab']}
    for g in L['gapfill']:
        assert norm_vocab(g['answer']) in taught, (
            f'gap-fill cobra "{g["answer"]}" que nenhum reveal card ensina')

    slides = build_slides(L)
    nslides = slides.count('<div class="slide ')
    assert nslides >= 25, f'apenas {nslides} slides (minimo 25)'

    open(os.path.join(d, 'slides.html'), 'w', encoding='utf-8').write(slides)
    open(os.path.join(d, 'preclass.html'), 'w', encoding='utf-8').write(build_preclass(L))
    open(os.path.join(d, 'complementary.html'), 'w', encoding='utf-8').write(build_complementary(L))
    json.dump(build_config(L, nslides), open(os.path.join(d, 'config.json'), 'w', encoding='utf-8'),
              indent=2, ensure_ascii=False)
    print(f'OK aula {n}: {nslides} slides autorados -> {d}')


if __name__ == '__main__':
    main()
