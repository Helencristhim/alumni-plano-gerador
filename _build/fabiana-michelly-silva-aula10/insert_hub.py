#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 10 (gerados pelo builder) nos hubs prof+aluno existentes.
Passo documentado do modo 'snippets' (README): o builder NAO toca o hub; este merge insere
card IN CLASS (so prof), stamp, accordion Pre-class, bloco Complementares, entradas de audioMap
(DENTRO do bloco JS) e ajusta totalLessons. Idempotente: aborta se a aula 10 ja estiver no hub.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = os.path.dirname(os.path.abspath(__file__))

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

accordion = read(os.path.join(D, 'preclass.html')).rstrip('\n')
complementary = read(os.path.join(D, 'complementary.html')).rstrip('\n')

# audioMap entries from the generated snippet (already inside <script>..</script>)
snip = read(os.path.join(D, 'hub_snippets.html'))
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>\n(.*?)</script>', snip, re.S)
amap_entries = m.group(1).rstrip('\n')
# also wire the order-l10 listen button audio (extra_audio key, not auto-included in snippet)
amap_entries += '\n  "[order-l10]": "/audio/fabiana-michelly-silva/a10_order_sequence.mp3",'

CARD10 = (
'    <a href="/professor/fabiana-michelly-silva-aula10.html?autostart=1"  style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit"  onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">10</div>\n'
'      <div><div style="font-weight:600;font-size:.95rem">Projecting Forward</div><div style="font-size:.8rem;color:var(--text-dim)">Timelines, Forecasts, and Strategic Plans -- 28 slides</div></div>\n'
'    </a>')

STAMP10 = '<div class="stamp" id="stamp10" data-label="Projecting Forward" style="background-image:url(\'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=200&q=80\')"></div>'

STAMP9 = '<div class="stamp" id="stamp9" data-label="Processes That Evolved" style="background-image:url(\'https://images.unsplash.com/photo-1518186285589-2f7649de83e0?w=200&q=80\')"></div>'

CARD9_TAIL = (
'      <div><div style="font-weight:600;font-size:.95rem">The Way We Used to Work</div><div style="font-size:.8rem;color:var(--text-dim)">Habits, Changes, and Processes That Evolved -- 28 slides</div></div>\n'
'    </a>')

# l9-youtube media-tip + its closing tags (unique anchor; identical in both hubs)
L9_YT_TAIL = (
'      <p class="media-tip">After watching, record a 60-second comparison of an old and a new process at your work. Use at least four new words and three structures: one "used to", one "would" for a repeated past action, and one "get used to + -ing".</p>\n'
'    </div>\n'
'  </div>\n'
'</div>')

def replace_once(s, old, new, label):
    assert s.count(old) == 1, f'{label}: anchor encontrado {s.count(old)}x (esperado 1)'
    return s.replace(old, new, 1)

def patch(path, is_prof):
    s = read(path)
    assert 'id="ex-lesson-10"' not in s and 'stamp10' not in s, f'{path}: aula 10 ja presente'
    # audioMap (dentro do bloco JS)
    s = replace_once(s, 'var audioMap = {', 'var audioMap = {\n' + amap_entries, 'audioMap')
    # stamp
    s = replace_once(s, STAMP9, STAMP9 + '\n' + STAMP10, 'stamp')
    # accordion Pre-class antes do fechamento da tab-exercises
    s = replace_once(s, '</div><!-- /tab-exercises -->', accordion + '\n</div><!-- /tab-exercises -->', 'accordion')
    # complementares apos o bloco da aula 9
    s = replace_once(s, L9_YT_TAIL, L9_YT_TAIL + '\n' + complementary, 'complementary')
    # totalLessons
    s = replace_once(s, 'var totalLessons = 9;', 'var totalLessons = 10;', 'totalLessons')
    # card IN CLASS (so prof tem tab-inclass)
    if is_prof:
        s = replace_once(s, CARD9_TAIL, CARD9_TAIL + '\n' + CARD10, 'card')
    write(path, s)
    print(f'OK {os.path.relpath(path, ROOT)}')

patch(os.path.join(ROOT, 'public/professor/fabiana-michelly-silva.html'), True)
patch(os.path.join(ROOT, 'public/aluno/fabiana-michelly-silva.html'), False)
print('done')
