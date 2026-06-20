#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 19 do Roberto Pires nos
hubs monoliticos (inline) prof/aluno. Nao toca aulas 1-18. Adiciona: card IN CLASS
(so prof), stamp19, accordion Pre-class, bloco Complementares, entradas audioMap
(+ [order-l19]) e ajusta var totalLessons=18 -> 19.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/roberto-pires/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l19] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l19]": "{AUDIO_BASE}pc19_arrival_steps.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), formato identico aos cards existentes do Roberto (accent) ---
CARD19 = (
    '    <a href="/professor/roberto-pires-aula19.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">19</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">On the Plane &amp; Arrival</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Flight and arrival language; ordering steps with when, after &amp; before &#8212; 28 slides</div></div>\n'
    '    </a>')

# stamp18 (ancora aditiva) — stamp19 entra logo depois
STAMP18 = ('<div class="stamp" id="stamp18" data-label="Boarding" style="background-image:url(\''
           'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=200&q=80\')"></div>')
STAMP19 = ('\n        <div class="stamp" id="stamp19" data-label="On the Plane" style="background-image:url(\''
           'https://images.unsplash.com/photo-1542296332-2e4473faf563?w=200&q=80\')"></div>')

# tail do card IN CLASS da aula 18 (At the Airport: Check-in & Boarding) — ancora aditiva
CARD18_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">At the Airport: Check-in &amp; Boarding</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Choosing your seat and boarding with have to and need to &#8212; 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp19
    assert s.count(STAMP18) == 1, f'{path}: ancora stamp18 nao unica'
    s = s.replace(STAMP18, STAMP18 + STAMP19, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=18' in s, f'{path}: totalLessons=18 nao encontrado'
    s = s.replace('var totalLessons=18', 'var totalLessons=19', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD18_TAIL) == 1, f'{path}: ancora card 18 nao unica'
        s = s.replace(CARD18_TAIL, CARD18_TAIL + '\n' + CARD19, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'roberto-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'roberto-pires.html'), False)
print('hubs atualizados (aditivo).')
