#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 17 do Roberto Pires nos
hubs monoliticos (inline) prof/aluno. Nao toca aulas 1-16. Adiciona: card IN CLASS
(so prof), stamp17, accordion Pre-class, bloco Complementares, entradas audioMap
(+ [order-l17]) e ajusta var totalLessons=16 -> 17.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/roberto-pires/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l17] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l17]": "{AUDIO_BASE}pc17_plan_steps.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), formato identico aos cards existentes do Roberto (accent) ---
CARD17 = (
    '    <a href="/professor/roberto-pires-aula17.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">17</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Future Travel Plans</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Talking about your next trip with going to and will &#8212; 28 slides</div></div>\n'
    '    </a>')

STAMP16 = ('<div class="stamp" id="stamp16" data-label="My Trip" style="background-image:url(\''
           'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=200&q=80\')"></div>')
STAMP17 = ('\n        <div class="stamp" id="stamp17" data-label="Next Trip" style="background-image:url(\''
           'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>')

# tail do card IN CLASS da aula 16 (Talking About Your Trip) — ancora aditiva
CARD16_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">Talking About Your Trip</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Sharing past travel experiences with the past simple &#8212; 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp17
    assert s.count(STAMP16) == 1, f'{path}: ancora stamp16 nao unica'
    s = s.replace(STAMP16, STAMP16 + STAMP17, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=16;' in s, f'{path}: totalLessons=16 nao encontrado'
    s = s.replace('var totalLessons=16;', 'var totalLessons=17;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD16_TAIL) == 1, f'{path}: ancora card 16 nao unica'
        s = s.replace(CARD16_TAIL, CARD16_TAIL + '\n' + CARD17, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'roberto-pires.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'roberto-pires.html'), False)
print('hubs atualizados (aditivo).')
