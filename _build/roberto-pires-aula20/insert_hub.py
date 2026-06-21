#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 20 (CAPSTONE) do Roberto
Pires nos hubs monoliticos (inline) prof/aluno. Nao toca aulas 1-19. Adiciona: card
IN CLASS (so prof), stamp20, accordion Pre-class, bloco Complementares, entradas
audioMap (+ [order-l20]) e ajusta var totalLessons=19 -> 20.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/roberto-pires/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l20] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l20]": "{AUDIO_BASE}pc20_hotel_steps.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), formato identico aos cards existentes do Roberto (accent) ---
CARD20 = (
    '    <a href="/professor/roberto-pires-aula20.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">20</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">At the Destination: Hotel Check-in &amp; Getting Around</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Checking in and getting around; polite requests and offers &#8212; 28 slides</div></div>\n'
    '    </a>')

# stamp19 (ancora aditiva) — stamp20 entra logo depois
STAMP19 = ('<div class="stamp" id="stamp19" data-label="On the Plane" style="background-image:url(\''
           'https://images.unsplash.com/photo-1542296332-2e4473faf563?w=200&q=80\')"></div>')
STAMP20 = ('\n        <div class="stamp" id="stamp20" data-label="Destination" style="background-image:url(\''
           'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=200&q=80\')"></div>')

# tail do card IN CLASS da aula 19 (On the Plane & Arrival) — ancora aditiva
# inclui o </a> de fechamento do card 19 para que o CARD20 entre DEPOIS dele
CARD19_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">On the Plane &amp; Arrival</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Flight and arrival language; ordering steps with when, after &amp; before &#8212; 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp20
    assert s.count(STAMP19) == 1, f'{path}: ancora stamp19 nao unica'
    s = s.replace(STAMP19, STAMP19 + STAMP20, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=19' in s, f'{path}: totalLessons=19 nao encontrado'
    s = s.replace('var totalLessons=19', 'var totalLessons=20', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD19_TAIL) == 1, f'{path}: ancora card 19 nao unica'
        s = s.replace(CARD19_TAIL, CARD19_TAIL + '\n' + CARD20, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'roberto-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'roberto-pires.html'), False)
print('hubs atualizados (aditivo).')
