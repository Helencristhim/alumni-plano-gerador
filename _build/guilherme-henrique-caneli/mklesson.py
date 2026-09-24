#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mklesson.py — AUTORIA das aulas do Guilherme Henrique Caneli (C1+, 8 aulas).

NAO substitui o builder (REGRA 20). Emite so os arquivos de CONTEUDO que se escreveriam a
mao em _build/guilherme-henrique-caneli-aula{N}/ (slides.html, preclass.html,
complementary.html, config.json e, na aula 1, planning.html), a partir de uma ficha por
aula em specs/aulaN.py. Depois o fluxo e o de sempre:

    python3 _build/model/build_from_model.py _build/guilherme-henrique-caneli-aula{N}/config.json

POR QUE EXISTE. As 8 aulas tem as MESMAS duas formas (aula impar = fala, com dialogo
line-by-line e role-play; aula par = leitura, com texto central, gist e true/false —
REGRA 29.2). A forma foi copiada das aulas da Veridiana Sterman Petrilli ja publicadas e
aprovadas pelos gates; o que muda por aula e so a ficha. Escrever 8 vezes o esqueleto a
mao e o caminho conhecido para a REGRA 11 item 9 (uniformidade) quebrar na aula 6.

USO:  python3 _build/guilherme-henrique-caneli/mklesson.py 1
"""
import importlib.util
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

SLUG = 'guilherme-henrique-caneli'
STUDENT = 'Guilherme Henrique Caneli'
FIRST = 'Guilherme'
TOTAL = 8
PALETTE = {'accent': '#1E4D5C', 'accent_light': '#6FB3C2'}
HEADER = ['C1+ (Avan&#231;ado)', '37 anos &middot; GRI Institute',
          'Infraestrutura &middot; Am&#233;rica Latina &middot; S&#227;o Paulo, SP',
          '60 min &middot; Online &middot; 2x por semana']
PROGRAM = 'Executive English'
HUB_SUBTITLE = ('Ingl&#234;s executivo para quem abre confer&#234;ncias e fala com CEOs de infraestrutura '
                '&mdash; vocabul&#225;rio de project finance, fala sem roteiro e um sotaque que todo mundo entende')
DARK = 'linear-gradient(rgba(12,30,38,.80),rgba(12,30,38,.92))'
VOICES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}

SVG_LISTEN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

ICONS = {
    'coin': '<circle cx="12" cy="12" r="9"/><path d="M14.5 9a2.5 2.5 0 00-2.5-1.5c-1.4 0-2.5.8-2.5 2s1.1 1.7 2.5 2 2.5.9 2.5 2-1.1 2-2.5 2A2.5 2.5 0 019.5 15"/><line x1="12" y1="6" x2="12" y2="18"/>',
    'road': '<path d="M4 21L9 3"/><path d="M20 21L15 3"/><line x1="12" y1="5" x2="12" y2="8"/><line x1="12" y1="11" x2="12" y2="14"/><line x1="12" y1="17" x2="12" y2="20"/>',
    'bridge': '<path d="M2 18h20"/><path d="M4 18v-6a8 8 0 0116 0v6"/><line x1="8" y1="18" x2="8" y2="11"/><line x1="12" y1="18" x2="12" y2="8"/><line x1="16" y1="18" x2="16" y2="11"/>',
    'scale': '<path d="M12 3v18"/><path d="M5 7h14"/><path d="M8 7l-4 7h8z"/><path d="M16 7l-4 7h8z"/>',
    'mic': '<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>',
    'users': '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.9"/><path d="M16 3.1a4 4 0 010 7.8"/>',
    'chart': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'globe': '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>',
    'doc': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/>',
    'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    'layers': '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    'key': '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.7 12.3L21 2"/><path d="M16 7l3 3"/><path d="M19 4l2 2"/>',
    'compass': '<circle cx="12" cy="12" r="10"/><polygon points="16.2 7.8 14.1 14.1 7.8 16.2 9.9 9.9"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/>',
    'message': '<path d="M21 11.5a8.4 8.4 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.4 8.4 0 01-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.4 8.4 0 013.8-.9h.5a8.5 8.5 0 018 8z"/>',
    'flag': '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    'link': '<path d="M10 13a5 5 0 007.5.5l3-3a5 5 0 00-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 00-7.5-.5l-3 3a5 5 0 007 7L12.3 19"/>',
    'zap': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    'eye': '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    'alert': '<path d="M10.3 3.9L1.8 18a2 2 0 001.7 3h17a2 2 0 001.7-3L14.7 3.9a2 2 0 00-3.4 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'refresh': '<polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.5 9a9 9 0 0114.9-3.4L23 10"/><path d="M1 14l4.6 4.4A9 9 0 0020.5 15"/>',
    'building': '<rect x="4" y="2" width="16" height="20" rx="1"/><line x1="9" y1="6" x2="9" y2="6.01"/><line x1="15" y1="6" x2="15" y2="6.01"/><line x1="9" y1="10" x2="9" y2="10.01"/><line x1="15" y1="10" x2="15" y2="10.01"/><line x1="9" y1="14" x2="9" y2="14.01"/><line x1="15" y1="14" x2="15" y2="14.01"/><path d="M10 22v-4h4v4"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    'star': '<path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/>',
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>',
    'pen': '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/>',
    'hand': '<path d="M18 11V6a2 2 0 00-4 0v5"/><path d="M14 10V4a2 2 0 00-4 0v6"/><path d="M10 10.5V6a2 2 0 00-4 0v8"/><path d="M18 8a2 2 0 014 0v6a8 8 0 01-8 8h-2c-2.8 0-4.5-.9-5.9-2.4L3.4 16.2a2 2 0 013-2.6L8 15"/>',
    'filter': '<polygon points="22 3 2 3 10 12.5 10 19 14 21 14 12.5 22 3"/>',
    'anchor': '<circle cx="12" cy="5" r="3"/><line x1="12" y1="22" x2="12" y2="8"/><path d="M5 12H2a10 10 0 0020 0h-3"/>',
    'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
}
GRADS = ['#1e3a5f,#2f6690', '#134e4a,#0f766e', '#4a044e,#a21caf', '#78350f,#b45309', '#422006,#a16207',
         '#14532d,#16a34a', '#164e63,#0e7490', '#3b0764,#6d28d9', '#7f1d1d,#b91c1c', '#7e4a0c,#d97706',
         '#1e293b,#475569', '#312e81,#4f46e5', '#0c4a6e,#0369a1', '#7c2d12,#ea580c', '#1f2937,#4b5563']


def esc(t):
    return str(t).replace('"', '&quot;')


def plain(h):
    import re
    return re.sub(r'<[^>]+>', '', h)


def listen(text, stop=False):
    pre = 'event.stopPropagation();' if stop else ''
    return ('<button class="audio-btn-sm" data-speak="%s" onclick="%sspeakText(this.dataset.speak,this)">%s Listen</button>'
            % (esc(text), pre, SVG_LISTEN))


def icon(name):
    assert name in ICONS, 'icone desconhecido: %r' % name
    return '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">%s</svg>' % ICONS[name]


class Deck:
    def __init__(self, L):
        self.L = L
        self.n = 0
        self.out = []

    def add(self, cls, phase, teacher, inner, bg=None, label=''):
        self.n += 1
        style = ''
        if bg:
            style = (' style="background-image:%s,url(\'%s\');background-size:cover;background-position:center"'
                     % (DARK, bg))
        active = ' active' if self.n == 1 else ''
        self.out.append('<!-- ========== SLIDE %d: %s ========== -->\n'
                        '<div class="slide %s%s" data-slide="%d" data-phase="%d" data-teacher="%s"%s>\n'
                        '  <div class="slide-inner"%s>\n%s\n  </div>\n</div>\n'
                        % (self.n, label, cls, active, self.n, phase, esc(teacher), style,
                           ' style="text-align:center"' if cls in ('slide-image', 'slide-dark') and 'NOCENTER' not in label else '',
                           inner))

    def html(self):
        return '\n'.join(self.out)


def chapter(D, phase, teacher, img, label, heading, sub):
    D.add('slide-image', phase, teacher,
          '    <div class="chapter-label">%s</div>\n'
          '    <h2 class="slide-heading" style="font-size:2rem;color:#fff">%s</h2>\n'
          '    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">%s</p>' % (label, heading, sub),
          bg=img, label='CHAPTER')


def comp_qs(items, max_w='560px', gap='1rem'):
    return ('    <div style="display:flex;flex-direction:column;gap:%s;max-width:%s;margin:1.2rem auto 0">\n%s\n    </div>'
            % (gap, max_w, '\n'.join('      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">%d. %s</div>'
                                    '<div class="q-answer">%s</div></div>' % (i + 1, q, a)
                                    for i, (q, a) in enumerate(items))))


def fill_grid(items, note):
    rows = '\n'.join('      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"%s<span class="fill-blank">___</span>'
                     '<span class="fill-answer">%s</span>%s"</div></div>' % (pre, ans, post) for pre, ans, post in items)
    return ('    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">%s</p>\n'
            '    <div class="fill-grid">\n%s\n    </div>' % (note, rows))


def render_slides(L):
    D = Deck(L)
    T = L['teacher']
    I = L['imgs']
    reading = L['model'] == 'reading'

    # ---- chapter 1
    D.add('slide-image', 1, T['opening'],
          '    <div class="chapter-label">Lesson %d</div>\n'
          '    <h1 class="slide-heading" style="font-size:2.5rem;color:#fff">%s</h1>\n'
          '    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:.6rem">%s</p>'
          % (L['n'], L['title_html'], L['hero_line']), bg=I['hero'], label='OPENING')
    w = L['warmup']
    D.add('slide-dark', 1, T['warmup'],
          '    <div class="chapter-label">Warm-up</div>\n'
          '    <h2 class="slide-heading" style="color:#fff">%s</h2>\n'
          '    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:1rem;max-width:640px;margin-left:auto;margin-right:auto">%s</p>'
          % (w['heading'], w['sub']), label='WARM-UP')
    tg = L['target']
    steps = '\n'.join('      <div style="background:var(--bg-card);border:1px solid var(--border);border-left:4px solid var(--accent);'
                      'border-radius:10px;padding:1rem"><p style="font-size:.95rem"><strong>%d.</strong> %s</p></div>' % (i + 1, s)
                      for i, s in enumerate(tg['steps']))
    D.add('slide-light', 1, T['target'],
          '    <div class="chapter-label">The Target</div>\n    <h2 class="slide-heading">%s</h2>\n'
          '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:600px;margin:1.4rem auto 0">\n%s\n    </div>'
          % (tg['heading'], steps), label='TARGET')
    dg = L['diagnostic']
    D.add('slide-light', 1, T['diagnostic'],
          '    <div class="chapter-label">Diagnostic</div>\n    <h2 class="slide-heading">%s</h2>\n'
          '    <div style="max-width:600px;margin:1.4rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.4rem">\n'
          '      <p style="font-size:1rem;line-height:1.7">%s</p>\n'
          '      <p style="font-size:.9rem;color:var(--text-mid);margin-top:.6rem">%s</p>\n    </div>'
          % (dg['heading'], dg['p1'], dg['p2']), label='DIAGNOSTIC')

    # ---- chapter 2: vocab
    c = L['ch2']
    chapter(D, 2, T['ch2'], I['ch2'], 'Chapter 2: %s' % L['phases'][1], c['heading'], c['sub'])
    V = L['vocab']
    per = 5
    groups = [V[i:i + per] for i in range(0, len(V), per)]
    for gi, grp in enumerate(groups):
        cards = []
        for i, v in enumerate(grp):
            grad = GRADS[(gi * per + i) % len(GRADS)]
            cards.append('      <div class="vocab-card" onclick="revealVocab(this)">\n'
                         '        <div class="card-icon" style="background:linear-gradient(135deg,%s)">%s<div class="card-hint">%s</div></div>\n'
                         '        <div class="card-body"><div class="card-word">%s</div><div class="card-def">%s</div>'
                         '<div class="card-example">"%s"</div><div class="card-audio">%s</div></div>\n      </div>'
                         % (grad, icon(v['icon']), v['def'], v['word'], v['def'], v['ex'], listen(v['word'], stop=True)))
        a, b = gi * per + 1, gi * per + len(grp)
        D.add('slide-light', 2, T['vocab%d' % (gi + 1)],
              '    <div class="chapter-label">Vocabulary</div>\n'
              '    <h2 class="slide-heading">Words <span class="accent">%d-%d</span></h2>\n'
              '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount%d">0 / %d words revealed</span></p>\n'
              '    <div class="vocab-grid" id="vocabGrid%d">\n%s\n    </div>'
              % (a, b, gi + 1, len(grp), gi + 1, '\n'.join(cards)), label='VOCAB %d-%d' % (a, b))
    rows = '\n'.join('      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem;display:flex;'
                     'justify-content:space-between;align-items:center;gap:.6rem"><span style="font-size:1.1rem;font-weight:600">%s</span>%s</div>'
                     % (p, listen(p)) for p in L['pron'])
    D.add('slide-light', 2, T['pron'],
          '    <div class="chapter-label">Say It Clearly</div>\n    <h2 class="slide-heading">%s</h2>\n'
          '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:600px;margin:1.2rem auto 0">\n%s\n    </div>'
          % (L['pron_heading'], rows), label='PRONUNCIATION')
    if reading:
        D.add('slide-light', 2, T['matching'],
              '    <div class="chapter-label">Check</div>\n    <h2 class="slide-heading">Word and <span class="accent">Meaning</span></h2>\n'
              '    <!--IC-BLOCKS:vocab-->', label='MATCHING')
    else:
        D.add('slide-light', 2, T['vocab_fill'],
              '    <div class="chapter-label">In Context</div>\n    <h2 class="slide-heading">Fill the <span class="accent">Gap</span></h2>\n'
              + fill_grid(L['vocab_fill'], 'Say the missing word first, then click to check'), label='VOCAB IN CONTEXT')

    def grammar_block(ph):
        g = L['grammar']
        c3 = L['ch_grammar']
        chapter(D, ph, T['ch_grammar'], I['ch_grammar'], 'Chapter %d: %s' % (ph, L['phases'][ph - 1]), c3['heading'], c3['sub'])
        exs = '\n'.join('      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;'
                        'justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">"%s"</p>%s</div>'
                        % (h, listen(plain(h))) for h in g['examples'])
        head = ''.join('<th style="padding:.6rem;text-align:left">%s</th>' % x for x in g['rule_head'])
        body = '\n'.join('          <tr style="%sborder-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">%s</td>'
                         '<td style="padding:.5rem">%s</td><td style="padding:.5rem">%s</td></tr>'
                         % ('background:var(--bg-elevated);' if i % 2 else '', a, b, cc) for i, (a, b, cc) in enumerate(g['rule_rows']))
        D.add('slide-light', ph, T['grammar'],
              '    <div class="chapter-label">Grammar Discovery</div>\n    <h2 class="slide-heading">%s</h2>\n'
              '    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:700px;margin:1rem auto 0">\n%s\n    </div>\n'
              '    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">%s</p>\n'
              '    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById(\'rule1\');t.style.display=(t.style.display===\'none\'||!t.style.display)?\'block\':\'none\'">Reveal the Rule</button>\n'
              '    <div id="rule1" style="display:none;max-width:720px;margin:1rem auto 0;overflow-x:auto">\n'
              '      <table style="width:100%%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
              '        <thead><tr style="background:var(--accent);color:#fff">%s</tr></thead>\n        <tbody>\n%s\n        </tbody>\n      </table>\n'
              '      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">In one line: <strong>%s</strong></p>\n    </div>'
              % (g['heading'], exs, g['prompt'], head, body, g['oneliner']), label='GRAMMAR DISCOVERY')
        gp = L['grammar_practice']
        D.add('slide-light', ph, T['grammar_practice'],
              '    <div class="chapter-label">Grammar Practice</div>\n    <h2 class="slide-heading">%s</h2>\n'
              % gp['heading'] + fill_grid(gp['items'], 'Say it first, then click to check'), label='GRAMMAR PRACTICE')

    def listening(ph, idx):
        li = L['listenings'][idx]
        qs = '\n'.join('      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">%d. %s</div><div class="q-answer">%s</div></div>'
                       % (i + 1, q, a) for i, (q, a) in enumerate(li['qs']))
        D.add('slide-dark', ph, T['listening%d' % (idx + 1)],
              '    <div class="chapter-label">%s</div>\n'
              '    <h2 class="slide-heading" style="color:#fff">%s</h2>\n'
              '    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">%s</p>\n'
              '    <div class="audio-player" id="mp-listen%d" data-src="/audio/%s/a%d_listening%d.mp3" data-questions="listening%dQs"></div>\n'
              '    <div class="comp-questions" id="listening%dQs" style="max-width:560px;margin:1.2rem auto 0">\n%s\n    </div>'
              % (li['label'], li['title'], li['blurb'], idx + 1, SLUG, L['n'], idx + 1, idx + 1, idx + 1, qs),
              label='LISTENING %d' % (idx + 1))

    def artifact(ph):
        a = L['artifact']
        rows = '\n'.join('        <div style="display:flex;justify-content:space-between;gap:1rem;padding:.5rem 0;%s"><span>%s</span>'
                         '<span style="font-weight:600;text-align:right%s">%s</span></div>'
                         % ('' if i == len(a['rows']) - 1 else 'border-bottom:1px solid var(--border)', k,
                            ';color:var(--accent)' if hl else '', v)
                         for i, (k, v, hl) in enumerate(a['rows']))
        D.add('slide-light', ph, T['artifact'],
              '    <div class="chapter-label">Real Document</div>\n    <h2 class="slide-heading">%s</h2>\n'
              '    <div style="max-width:580px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.06)">\n'
              '      <div style="background:var(--accent);color:#fff;padding:.9rem 1.2rem;text-align:center">\n'
              '        <div style="font-weight:700;font-size:1rem;letter-spacing:.06em">%s</div>\n'
              '        <div style="font-size:.75rem;opacity:.92;margin-top:.2rem">%s</div>\n      </div>\n'
              '      <div style="padding:1rem 1.2rem;font-size:.85rem">\n%s\n      </div>\n'
              '      <div style="padding:.7rem 1.2rem;background:var(--bg-elevated);font-size:.78rem;color:var(--text-mid);border-top:1px solid var(--border)">%s</div>\n'
              '    </div>\n%s'
              % (a['heading'], a['title'], a['subtitle'], rows, a['note'], comp_qs(a['qs'], gap='.7rem')), label='ARTIFACT')

    def detective(ph):
        cards = '\n'.join('      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"%s"</div>'
                          '<div class="error-fix">"%s"</div></div>' % (w, r) for w, r in L['detective'])
        D.add('slide-light', ph, T['detective'],
              '    <div class="chapter-label">Detective</div>\n    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>\n'
              '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="errorScore">0 / %d errors found</span></p>\n'
              '    <div class="error-grid" id="errorGrid">\n%s\n    </div>' % (len(L['detective']), cards), label='SPOT THE ERROR')

    def roleplays(ph):
        rp = L['roleplays']
        chapter(D, ph, T['ch_rp'], I['ch_rp'], 'Chapter %d: %s' % (ph, L['phases'][ph - 1]), rp['heading'], 'Guided &gt; Semi-free &gt; Free')
        bgs = ['linear-gradient(135deg,var(--accent-dim),rgba(30,77,92,.05))',
               'linear-gradient(135deg,rgba(30,77,92,.08),rgba(30,77,92,.02))',
               'linear-gradient(135deg,rgba(30,77,92,.12),rgba(30,77,92,.03))']
        labels = ['Role-Play 1 of 3 &mdash; Guided', 'Role-Play 2 of 3 &mdash; Semi-free', 'Role-Play 3 of 3 &mdash; Free']
        for i, r in enumerate(rp['items']):
            if r.get('chips'):
                extra = ('      <p style="font-size:.85rem;font-weight:600;margin-bottom:.5rem">%s</p>\n'
                         '      <div style="display:flex;flex-wrap:wrap;gap:.4rem">\n%s\n      </div>'
                         % ('Keyword chips:' if i == 0 else 'Keywords:',
                            '\n'.join('        <span style="background:var(--bg-card);border:1px solid var(--accent);border-radius:20px;padding:.3rem .7rem;font-size:.8rem">%s</span>' % ch
                                      for ch in r['chips'])))
            else:
                extra = '      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">%s</p>' % r['footer']
            D.add('slide-light', ph, T['rp%d' % (i + 1)],
                  '    <div class="chapter-label">%s</div>\n    <h2 class="slide-heading">%s</h2>\n'
                  '    <div class="roleplay-body" style="max-width:580px;margin:1rem auto 0;background:%s;border:1px solid var(--accent);border-radius:12px;padding:1.5rem">\n'
                  '      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> %s</p>\n%s\n    </div>'
                  % (labels[i], r['heading'], bgs[i], r['scenario'], extra), label='ROLE-PLAY %d' % (i + 1))

    if not reading:
        # ODD — speaking model (Veridiana aula 1)
        grammar_block(3)
        c4 = L['ch4']
        chapter(D, 4, T['ch4'], I['ch4'], 'Chapter 4: %s' % L['phases'][3], c4['heading'], c4['sub'])
        d = L['dialogue']
        lines = []
        for i, (who, txt) in enumerate(d['lines']):
            key = 'guilherme' if who == 'g' else L['guest_key']
            voice = 'arthur' if who == 'g' else L['guest_voice']
            ini = 'G' if who == 'g' else d['guest_initial']
            lines.append('      <div class="dialogue-line%s" data-line="%d" data-voice="%s"><div class="dialogue-avatar %s">%s</div>'
                         '<div class="dialogue-bubble %s-bubble">%s</div></div>'
                         % (' visible' if i == 0 else '', i + 1, voice, key, ini, key, txt))
        D.add('slide-dark', 4, T['dialogue'],
              '    <div class="chapter-label">Dialogue</div>\n    <h2 class="slide-heading" style="color:#fff">%s</h2>\n'
              '    <div class="dialogue-box" id="dialogueBox">\n%s\n    </div>\n'
              '    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>'
              % (d['heading'], '\n'.join(lines)), label='NOCENTER DIALOGUE')
        D.add('slide-light', 4, T['dialogue_comp'],
              '    <div class="chapter-label">Comprehension</div>\n    <h2 class="slide-heading">About <span class="accent">%s</span></h2>\n%s'
              % (d['guest_name'], comp_qs(d['comp'])), label='DIALOGUE COMPREHENSION')
        listening(4, 0)
        listening(4, 1)
        artifact(4)
        chapter(D, 5, T['ch5'], I['ch5'], 'Chapter 5: %s' % L['phases'][4], L['ch5']['heading'], L['ch5']['sub'])
        detective(5)
        qs = '\n'.join('      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem"><p style="font-size:.88rem;margin-bottom:.4rem"><strong>%d.</strong> "%s"</p>'
                       '<p style="font-size:.82rem;color:var(--accent);cursor:pointer" data-t="Show Answer" data-a="%s" onclick="this.textContent=this.textContent===this.dataset.t?this.dataset.a:this.dataset.t">Show Answer</p></div>'
                       % (i + 1, q, esc(a)) for i, (q, a) in enumerate(L['speaking']))
        D.add('slide-light', 5, T['speaking'],
              '    <div class="chapter-label">Speaking</div>\n    <h2 class="slide-heading">Your Own <span class="accent">Answers</span></h2>\n'
              '    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:640px;margin:1.2rem auto 0">\n%s\n    </div>' % qs,
              label='SPEAKING')
        items = '\n'.join('      <div class="oral-item" onclick="this.classList.toggle(\'revealed\')"><div class="oral-situation">%d. %s</div>'
                          '<div class="oral-model">"%s"</div></div>' % (i + 1, s, m) for i, (s, m) in enumerate(L['building']))
        D.add('slide-light', 5, T['building'],
              '    <div class="chapter-label">Build</div>\n    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>\n'
              '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say the full sentence, then click to compare</p>\n'
              '    <div class="oral-grid">\n%s\n    </div>' % items, label='BUILD')
        roleplays(6)
        chapter(D, 7, T['ch7'], I['ch7'], 'Chapter 7: %s' % L['phases'][6], L['ch7']['heading'], L['ch7']['sub'])
    else:
        # EVEN — reading model (Veridiana aula 2)
        c3 = L['ch3']
        chapter(D, 3, T['ch3'], I['ch3'], 'Chapter 3: %s' % L['phases'][2], c3['heading'], c3['sub'])
        D.add('slide-light', 3, T['reading'],
              '    <div class="chapter-label">Reading</div>\n    <h2 class="slide-heading">%s</h2>\n    <!--IC-BLOCKS:reading-->'
              % L['reading']['heading'], label='READING')
        D.add('slide-light', 3, T['gist'],
              '    <div class="chapter-label">Main Idea</div>\n    <h2 class="slide-heading">What Is the Text <span class="accent">Really Saying?</span></h2>\n    <!--IC-BLOCKS:gist-->',
              label='GIST')
        D.add('slide-light', 3, T['tf'],
              '    <div class="chapter-label">Detail</div>\n    <h2 class="slide-heading">True or <span class="accent">False?</span></h2>\n'
              '    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Say it, then read out the line that proves it.</p>\n    <!--IC-BLOCKS:tf-->',
              label='TRUE OR FALSE')
        artifact(3)
        grammar_block(4)
        detective(4)
        chapter(D, 5, T['ch5'], I['ch5'], 'Chapter 5: %s' % L['phases'][4], L['ch5']['heading'], L['ch5']['sub'])
        D.add('slide-light', 5, T['equiv'],
              '    <div class="chapter-label">Same Meaning</div>\n    <h2 class="slide-heading">%s</h2>\n    <!--IC-BLOCKS:equiv-->'
              % L['equiv_heading'], label='EQUIVALENCE')
        D.add('slide-light', 5, T['gap'],
              '    <div class="chapter-label">In Context</div>\n    <h2 class="slide-heading">%s</h2>\n    <!--IC-BLOCKS:gap-->'
              % L['gap_heading'], label='GAP-FILL')
        D.add('slide-light', 5, T['quickfire'],
              '    <div class="chapter-label">Quick Fire</div>\n    <h2 class="slide-heading">One Question at <span class="accent">a Time</span></h2>\n    <!--IC-BLOCKS:quickfire-->',
              label='QUICK FIRE')
        listening(5, 0)
        listening(5, 1)
        roleplays(6)

    # ---- chapter 7 wrap-up
    sv = '\n'.join('      <div style="background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:10px;padding:.9rem;display:flex;'
                   'justify-content:space-between;align-items:center;gap:.6rem"><span style="font-size:.92rem;color:#fff">%s</span>%s</div>'
                   % (p, listen(p)) for p in L['survival'])
    D.add('slide-dark', 7, T['survival'],
          '    <div class="chapter-label">Survival Card</div>\n    <h2 class="slide-heading" style="color:#fff">%s</h2>\n'
          '    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:680px;margin:1.2rem auto 0;text-align:left">\n%s\n    </div>'
          % (L['survival_heading'], sv), label='SURVIVAL CARD')
    ck = '\n'.join('      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>%s</div>'
                   % c_ for c_ in L['checklist'])
    D.add('slide-dark', 7, T['checklist'],
          '    <div class="chapter-label">Self-Assessment</div>\n    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Can Do Now</span></h2>\n'
          '    <div class="check-grid" style="max-width:620px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">\n%s\n    </div>' % ck,
          label='SELF-ASSESSMENT')
    b = L['badge']
    D.add('slide-dark', 7, T['complete'],
          '    <div class="chapter-label">Lesson Complete</div>\n    <div class="badge-card">\n      <div class="badge-icon">\n'
          '        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/></svg></div>\n'
          '        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>\n      </div>\n'
          '      <h2 class="slide-heading" style="color:#fff">%s Badge <span class="accent">Earned!</span></h2>\n'
          '      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">%s</p>\n'
          '      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson %d -- Complete.</p>\n'
          '      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">%s</p>\n    </div>'
          % (b['name'], b['line'], L['n'], b['next']), label='LESSON COMPLETE')
    return D.html()


# ---------------------------------------------------------------- pre-class
def render_preclass(L):
    n = L['n']
    P = L['pc']
    V = L['vocab']
    rnd = random.Random(1000 + n)
    out = []
    out.append('<div class="lesson-card" id="ex-lesson-%d">\n  <div class="lesson-header" onclick="toggleLesson(this)">\n'
               '    <div class="lesson-header-img" style="background-image:url(\'%s\')"></div>\n'
               '    <div class="lesson-header-content">\n      <div class="lesson-number">Lesson %02d -- Pre-class</div>\n'
               '      <h3>%s</h3>\n      <div class="lesson-desc">%s Key words: %s. Structure: %s.</div>\n'
               '      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="%d" style="width:0%%"></div></div><span class="mini-percent" data-lesson-pct="%d">0%%</span></div>\n'
               '    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n  <div class="lesson-body">\n'
               % (n, L['imgs']['pc'], n, P['title'], P['desc'], ', '.join(plain(v['word']) for v in V),
                  L['grammar_point'], n, n))

    def section(h4, badge_cls, badge, intro, body):
        out.append('    <div class="exercise-section">\n      <div class="section-header-row"><h4>%s</h4><span class="badge %s">%s</span></div>\n'
                   '      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">%s</p>\n%s\n    </div>\n'
                   % (h4, badge_cls, badge, intro, body))

    cards = '\n'.join('        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">%s</span>'
                      '<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">%s</span></div><div class="vocab-card-example">"%s"</div></div>'
                      '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
                      % (v['word'], v['def'][0].lower() + v['def'][1:], v['ex'], esc(v['word'])) for v in V)
    section('Stage 1.1: Vocabulary Cards', 'badge-vocab', 'Vocabulary', 'Listen to each word and read the example. Tap Listen to hear it.',
            '      <div class="vocab-cards">\n%s\n      </div>' % cards)

    idx = P['match_idx']
    defs = [V[i]['def'][0].lower() + V[i]['def'][1:] for i in idx]
    opts = defs[:]
    while True:
        rnd.shuffle(opts)
        if all(opts[i] != defs[i] for i in range(len(defs))):
            break
    rows = []
    for k, vi in enumerate(idx):
        o = '\n'.join('            <option value="%s">%s</option>' % (esc(d), d) for d in opts)
        rows.append('        <div class="match-row" data-answer="%s">\n          <span class="match-word">%s</span>\n'
                    '          <select onchange="checkMatch(this)">\n            <option value="">Select...</option>\n%s\n          </select>\n        </div>'
                    % (esc(defs[k]), V[vi]['word'], o))
    section('Stage 1.2: Matching', 'badge-practice', 'Practice', 'Choose the meaning of each word.',
            '      <div class="match-grid" id="match-l%d">\n%s\n      </div>\n      <button class="verify-all-btn" onclick="verifyAllMatches(\'match-l%d\')">Check Answers</button>'
            % (n, '\n'.join(rows), n))

    paras = '\n'.join('        <p%s>%s</p>' % ('' if i == 0 else ' style="margin-top:.6rem"', p) for i, p in enumerate(P['context']))
    qz = []
    for i, (q, opts_, right) in enumerate(P['context_quiz']):
        o = ''.join('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s"><span class="option-letter">%s</span> %s</div>'
                    % ('true' if j == right else 'false', 'ABC'[j], t) for j, t in enumerate(opts_))
        qz.append('      <div class="quiz-item"><div class="quiz-question">%d. %s</div><div class="quiz-options">%s</div></div>' % (i + 1, q, o))
    section('Stage 1.3: Grammar in Context', 'badge-vocab', 'GRAMMAR', 'Read the text, then answer the questions.',
            '      <div class="context-text" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem;font-size:.9rem;line-height:1.7;margin-bottom:1rem">\n%s\n      </div>\n%s'
            % (paras, '\n'.join(qz)))

    g = L['grammar']
    head = ''.join('<th style="padding:.6rem;text-align:left">%s</th>' % x for x in g['rule_head'])
    body = '\n'.join('            <tr style="%sborder-bottom:1px solid var(--border)"><td style="padding:.5rem;font-weight:600">%s</td><td style="padding:.5rem">%s</td><td style="padding:.5rem">%s</td></tr>'
                     % ('background:var(--bg-elevated);' if i % 2 else '', a, b, c) for i, (a, b, c) in enumerate(P['tip_rows']))
    section('Stage 1.4: Grammar Tip -- %s' % P['tip_title'], 'badge-vocab', 'GRAMMAR', P['tip_lead'],
            '      <div style="overflow-x:auto">\n        <table style="width:100%%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
            '          <thead><tr style="background:var(--accent);color:#fff">%s</tr></thead>\n          <tbody>\n%s\n          </tbody>\n        </table>\n      </div>\n'
            '      <p style="font-size:.82rem;color:var(--danger);margin-top:.8rem"><strong>Never:</strong> %s</p>' % (head, body, P['tip_never']))

    bl = []
    for pre, ans, post, hint, alt in P['blanks']:
        phrase = plain(pre + ans + post)
        bl.append('      <div class="fill-blank-item"><div class="fill-blank-sentence">"%s<input class="blank-input" data-answer="%s"%s data-hint="%s" data-phrase="%s" placeholder="___">%s"</div>'
                  '<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
                  % (pre, esc(ans), (' data-alt="%s"' % esc(alt)) if alt else '', esc(hint), esc(phrase), post))
    section('Stage 1.5: Fill in the Blank', 'badge-practice', 'Practice', 'Complete each sentence, then check your answer.', '\n'.join(bl))

    # ── Stages 1.6 a 1.9: a anatomia de preparacao de prova ───────────────────
    # Vieram da aula 2, depois do feedback do professor Andre em 22/09/2026. Sao
    # CONDICIONAIS: aula cujo spec ainda nao tem o conteudo continua gerando
    # exatamente como gerava, byte a byte.
    #
    # Nenhum item daqui pode existir no deck: a pre-class PREPARA a aula, nao a
    # repete. Vocabulario repete de proposito (REGRA 1); tarefa, nao.

    def fill_sem_audio(itens):
        """Igual ao Stage 1.5, MENOS o botao Listen.

        O botao Listen le o audioMap pelo texto da frase (data-phrase). Estas
        frases nao tem MP3, entao com o botao o aluno clicaria num botao mudo.
        """
        out_ = []
        for pre, ans, post, hint, alt in itens:
            out_.append('      <div class="fill-blank-item"><div class="fill-blank-sentence">%s'
                        '<input class="blank-input" data-answer="%s"%s data-hint="%s" placeholder="___">%s</div>'
                        '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
                        % (pre, esc(ans), (' data-alt="%s"' % esc(alt)) if alt else '', esc(hint), post))
        return '\n'.join(out_)

    def quiz_bloco(itens, letras='ABCD'):
        out_ = []
        for i, (q, opts_, right) in enumerate(itens, 1):
            o = ''.join('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s">'
                        '<span class="option-letter">%s</span> %s</div>'
                        % ('true' if j == right else 'false', letras[j], t)
                        for j, t in enumerate(opts_))
            out_.append('      <div class="quiz-item"><div class="quiz-question">%d. %s</div>'
                        '<div class="quiz-options">%s</div></div>' % (i, q, o))
        return '\n'.join(out_)

    if P.get('reading'):
        paras_r = '\n'.join('        <p%s>%s</p>' % ('' if i == 0 else ' style="margin-top:.8rem"', t)
                            for i, t in enumerate(P['reading']))
        section('Stage 1.6: Read and Understand', 'badge-quiz', 'Reading',
                'Read it once straight through, then read it again and answer. Every expression from '
                'Stage 1.1 is in here doing a job.',
                '      <div style="text-align:center;margin-bottom:.9rem">'
                '<div style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;font-weight:700">%s</div></div>\n'
                '      <div class="context-text" style="background:var(--bg-card);border:1px solid var(--border);'
                'border-radius:10px;padding:1rem;font-size:.9rem;line-height:1.8;margin-bottom:1rem">\n%s\n      </div>\n%s'
                % (P['reading_title'], paras_r, quiz_bloco(P['comprehension'])))

    if P.get('word_formation'):
        section('Stage 1.7: Word Formation', 'badge-grammar', 'Use of English',
                'Use the word in capitals to form a word that fits the gap. Watch for negative prefixes, '
                'for part of speech, and for the internal change some of these words make.',
                fill_sem_audio(P['word_formation']))

    if P.get('transformations'):
        itens_t = []
        for lead, key, pre, ans, post, hint, alt in P['transformations']:
            cab = ('<div style="font-size:.88rem;margin-bottom:.35rem">%s</div>'
                   '<div style="font-size:.74rem;letter-spacing:.1em;font-weight:800;color:var(--accent);'
                   'margin-bottom:.3rem">%s</div>' % (lead, key))
            itens_t.append((cab + pre, ans, post, hint, alt))
        section('Stage 1.8: Key-word Transformations', 'badge-grammar', 'Use of English',
                'Complete the second sentence so that it means the same as the first, using the word given. '
                '<b>Do not change that word.</b> Use between three and eight words.',
                fill_sem_audio(itens_t))

    if P.get('listen_choose'):
        li = P['listen']
        pid = 'lp-pc-l%d' % n
        player = ('      <div style="font-size:.78rem;color:var(--text-dim);margin-bottom:.5rem">%s</div>\n'
                  '      <div class="lp cpe-lp" id="%s" data-src="/audio/%s/%s" style="max-width:520px;margin:.4rem 0 1rem">'
                  '<div class="lp-seekbar" onclick="mpSeek(event,\'%s\')"><div class="lp-progress" id="progress-%s"></div></div>'
                  '<div class="lp-times"><span id="time-current-%s">0:00</span><span id="time-total-%s">0:00</span></div>'
                  '<div class="lp-row">'
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
                  % (li['caption'], pid, SLUG, li['file'], pid, pid, pid, pid, pid, pid, pid, pid, pid, pid, pid))
        section('Stage 1.9: Listen and Choose', 'badge-quiz', 'Listening',
                'One speaker, heard twice, and six questions. Play it a second time before you answer.',
                player + '\n' + quiz_bloco(P['listen_choose']))

    oi = '\n'.join('        <div class="order-item" draggable="true" data-order="%d" onclick="selectOrderItem(this,\'order-l%d\')"><span class="order-num">?</span>'
                   '<span class="order-text">"%s"</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l%d\')">&#9650;</button>'
                   '<button class="arrow-btn" onclick="moveItem(this,1,\'order-l%d\')">&#9660;</button></span></div>' % (i + 1, n, t, n, n)
                   for i, t in enumerate(P['order']))
    section('Stage 2: %s' % P['order_title'], 'badge-order', 'Order', P['order_lead'],
            '      <div class="order-container" id="order-l%d">\n%s\n      </div>\n      <button class="verify-all-btn" onclick="checkOrder(\'order-l%d\')">Check Order</button>' % (n, oi, n))

    sc = '\n'.join('      <div class="speech-card" data-phrase="%s">\n        <div class="speech-phrase">%s</div>\n'
                   '        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
                   '        <div class="speech-result"></div>\n      </div>' % (esc(p), p) for p in L['survival'])
    section('Stage 3: Pronunciation', 'badge-speak', 'Speaking', 'Listen, then record yourself. You will get a word-by-word score.', sc)

    qz = []
    for q, opts_, right in P['quiz']:
        o = ''.join('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s"><span class="option-letter">%s</span> "%s"</div>'
                    % ('true' if j == right else 'false', 'ABC'[j], t) for j, t in enumerate(opts_))
        qz.append('      <div class="quiz-item"><div class="quiz-question">%s</div><div class="quiz-options">%s</div></div>' % (q, o))
    section('Stage 4: Situational Quiz', 'badge-quiz', 'Quiz', 'Choose the answer a real speaker would give.', '\n'.join(qz))

    section('Stage 5: Free Production', 'badge-think', 'Reflection', 'Think, then record your answer. There is no wrong answer here.',
            '      <div class="think-card">\n        <div class="think-question">%s</div>\n'
            '        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>\n'
            '        <div id="think-result-l%d"></div>\n      </div>' % (P['think'], n))

    sp = '\n'.join('      <div class="survival-phrase"><span class="sp-num">%d</span><span class="sp-en">%s</span><button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
                   % (i + 1, p, esc(p)) for i, p in enumerate(L['survival']))
    out.append('    <div class="survival-card">\n      <h4>Survival Card -- Lesson %d</h4>\n%s\n    </div>\n\n  </div>\n</div>\n' % (n, sp))
    return ''.join(out)


MEDIA_SVG = {
    'Series': '<rect x="2" y="7" width="20" height="15" rx="2"/><polyline points="17 2 12 7 7 2"/>',
    'Film': '<rect x="2" y="7" width="20" height="15" rx="2"/><polyline points="17 2 12 7 7 2"/>',
    'Podcast': '<path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>',
    'Talk': '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>',
    'Video': '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>',
}


def render_complementary(L):
    n = L['n']
    out = ['<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">Complementary Activities</h3>\n'
           '<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem">Optional extras to enjoy outside class. Mark each one as done after you watch or listen to it.</p>\n']
    for m in L['media']:
        out.append('<div class="media-card-wrapper" data-media="l%d-%s">\n  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>\n'
                   '  <div class="media-card">\n    <div class="media-thumb"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2">%s</svg></div>\n'
                   '    <div class="media-info">\n      <div class="media-type">%s</div>\n      <h5>%s</h5>\n      <p>%s</p>\n      <p class="media-tip">%s</p>\n'
                   '      <a href="%s" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">%s &#8599;</a>\n'
                   '    </div>\n  </div>\n</div>\n'
                   % (n, m['id'], MEDIA_SVG[m['type']], m['type'], m['title'], m['desc'], m['tip'], m['url'], m['cta']))
    return '\n'.join(out)


def matching_block(title, pairs, hint=None):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words = [[str(i + 1), w, letters[i]] for i, (w, _) in enumerate(pairs)]
    defs = [[letters[i], d] for i, (_, d) in enumerate(pairs)]
    rnd = random.Random(len(pairs) * 7 + len(title))
    order = defs[:]
    while True:
        rnd.shuffle(order)
        if all(order[i][0] != defs[i][0] for i in range(len(defs))):
            break
    b = {'kind': 'matching', 'title': title, 'words': words, 'defs': order}
    if hint:
        b['hint'] = hint
    return b


def render_config(L):
    n = L['n']
    stamps = [{'id': s['id'], 'label': s['label'], 'img': s['img']} for s in STAMPS]
    lesson = {
        'n': n, 'menu_num': '%02d' % n, 'menu_title': L['title_html'].replace("class='accent'", 'class="accent"'),
        'menu_desc': '%s -- %d slides' % (L['menu_desc'].split(' -- ')[0], L['_slides']), 'subtitle': 'Lesson %d -- %s' % (n, plain(L['title_html'])),
        'title_tag': 'Professor View -- %s | Lesson %d -- %s' % (STUDENT, n, plain(L['title_html'])),
        'grammar_point': L['grammar_point'], 'phases': L['phases'],
        'listenings': [{'file': 'a%d_listening%d.mp3' % (n, i + 1), 'voice': li['voice'], 'text': li['text']}
                       for i, li in enumerate(L['listenings'])],
    }
    # O eixo de sotaque e POR ALUNO e por aula: o voices.json global so tem tres
    # vozes, e a Part 4 da prova precisa de cinco falantes distintos. Quem declara
    # o override e o spec; o voices.json global NAO e tocado, porque e de todo
    # mundo. (gen_audio e validate_lesson ja leem este campo.)
    if L['model'] == 'reading':
        R = L['reading']
        lesson['inclass_blocks'] = {
            'vocab': [matching_block('Match each word to its meaning', [(v['word'], v['def'][0].lower() + v['def'][1:]) for v in L['vocab'][:10]])],
            'reading': [{'kind': 'reading', 'rtitle': R['rtitle'], 'paras': R['paras'], 'source': R['source'], 'link': ''}],
            'gist': [{'kind': 'gist', 'prompt': L['gist']['prompt'], 'choices': L['gist']['choices']}],
            'tf': [{'kind': 'tf', 'items': L['tf']}],
            'equiv': [matching_block(L['equiv']['title'], L['equiv']['pairs'], L['equiv'].get('hint'))],
            'gap': [{'kind': 'gapfill', 'parts': L['gap']['parts'], 'bank': L['gap']['bank']}],
            'quickfire': [{'kind': 'quickfire', 'items': L['quickfire']}],
        }
    lesson['extra_audio'] = []
    cfg = {
        'slug': SLUG, 'molde': 'helen-mendes', 'student_name': STUDENT, 'first_name': FIRST, 'gender': 'm',
        'program': PROGRAM, 'total_aulas': TOTAL, 'palette': PALETTE, 'header': HEADER, 'hub_subtitle': HUB_SUBTITLE,
        'characters': {'guilherme': 'arthur', L['guest_key']: L['guest_voice']},
        'stamps': stamps, 'lesson': lesson, 'hub': 'new' if n == 1 else 'snippets',
    }
    # O eixo de sotaque e POR ALUNO e por aula, e mora no TOPO do config, que e
    # onde o gen_audio o procura. O voices.json global so tem tres vozes e a Part
    # 4 da prova precisa de cinco falantes distintos; ele NAO e tocado, porque e
    # compartilhado com todos os alunos.
    if L.get('voices'):
        cfg['voices'] = L['voices']
    return cfg


STAMPS = [
    {'id': 1, 'label': 'The Executive Voice', 'img': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=200&q=80'},
    {'id': 2, 'label': 'The Language of Capital', 'img': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80'},
    {'id': 3, 'label': 'The Art of the Opening', 'img': 'https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=200&q=80'},
    {'id': 4, 'label': 'The Rules of the Game', 'img': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=200&q=80'},
    {'id': 5, 'label': 'Holding the Room', 'img': 'https://images.unsplash.com/photo-1515169067868-5387ec356754?w=200&q=80'},
    {'id': 6, 'label': 'The Executive Pen', 'img': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=200&q=80'},
    {'id': 7, 'label': 'The Full Room', 'img': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=200&q=80'},
    {'id': 8, 'label': 'Full Circle', 'img': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=200&q=80'},
]


def load_spec(n):
    p = os.path.join(HERE, 'specs', 'aula%d.py' % n)
    spec = importlib.util.spec_from_file_location('aula%d' % n, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.L


def check_spec(L):
    V = L['vocab']
    assert 12 <= len(V) <= 15, 'C1+: 12-15 palavras por aula, veio %d' % len(V)
    words = [plain(v['word']).lower() for v in V]
    assert len(set(words)) == len(words), 'vocab repetido na propria aula'
    assert len(L['survival']) == 5 and len(L['checklist']) == 5
    assert len(L['roleplays']['items']) == 3
    assert len(L['listenings']) == 2
    assert len(L['pc']['blanks']) >= 5 and len(L['pc']['order']) >= 5 and len(L['pc']['quiz']) >= 3
    assert len(L['pc']['match_idx']) == 6
    if L['model'] == 'reading':
        g = L['gap']
        assert all(len(p) == 2 for p in g['parts'] if isinstance(p, list)), 'gapfill sem resposta (BUILDER_GEN 3)'
        ans = sorted(p[1] for p in g['parts'] if isinstance(p, list))
        assert ans == sorted(g['bank']), 'banco do gapfill != respostas: %r vs %r' % (ans, g['bank'])
    else:
        taught = {w.replace('to ', '', 1) if w.startswith('to ') else w for w in words}
        for pre, ans, post in L['vocab_fill']:
            a = ans.lower()
            assert a in words or a in taught or any(a in w or w.split(' ', 1)[-1] in a for w in words), \
                'vocab_fill cobra palavra nao ensinada: %r' % ans


def main():
    n = int(sys.argv[1])
    L = load_spec(n)
    L['n'] = n
    check_spec(L)
    d = os.path.join(ROOT, '_build', '%s-aula%d' % (SLUG, n))
    os.makedirs(d, exist_ok=True)

    def w(name, s):
        open(os.path.join(d, name), 'w', encoding='utf-8').write(s)
        print('  wrote', os.path.relpath(os.path.join(d, name), ROOT), len(s))
    slides = render_slides(L)
    # O builder injeta 3 slides nas duas formas: a tarefa antes do dialogo/leitura (2.2) e a
    # predicao antes de cada listening (2.3). A contagem do card do menu e a do arquivo final.
    L['_slides'] = slides.count('<div class="slide ') + 3
    w('slides.html', slides)
    w('preclass.html', render_preclass(L))
    w('complementary.html', render_complementary(L))
    w('config.json', json.dumps(render_config(L), ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
