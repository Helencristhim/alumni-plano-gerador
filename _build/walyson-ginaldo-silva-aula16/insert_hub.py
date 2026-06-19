#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 16 do Walyson nos hubs
monoliticos (inline) prof/aluno. Nao toca aulas 1-15. Adiciona: card IN CLASS
(so prof), stamp16, accordion Pre-class, bloco Complementares, entradas audioMap
(+ [order-l16]) e ajusta var totalLessons=15 -> 16.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/walyson-ginaldo-silva/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l16] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l16]": "{AUDIO_BASE}pc16_order_negotiate_email_steps.mp3",')
amap_block = '\n'.join(amap_lines)

# --- card IN CLASS (so prof), formato identico aos cards existentes do Walyson (accent) ---
CARD16 = (
    '    <a href="/professor/walyson-ginaldo-silva-aula16.html?autostart=1"  '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">16</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Negotiating by Email</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Making and responding to written offers and counteroffers '
    '-- the second conditional -- 28 slides</div></div>\n'
    '    </a>')

STAMP15 = ('<div class="stamp" id="stamp15" data-label="Formal Writer" style="background-image:url(\''
           'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=200&q=80\')"></div>')
STAMP16 = ('\n<div class="stamp" id="stamp16" data-label="Deal Negotiator" style="background-image:url(\''
           'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=200&q=80\')"></div>')

# tail do card IN CLASS da aula 15 (Writing a Formal Email) — ancora aditiva (so prof)
CARD15_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">Writing a Formal Email</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Requesting and confirming contract terms in writing '
    '-- polite request and confirmation language -- 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp16
    assert s.count(STAMP15) == 1, f'{path}: ancora stamp15 nao unica'
    s = s.replace(STAMP15, STAMP15 + STAMP16, 1); n += 1

    # 3. accordion Pre-class
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises nao unico'
    s = s.replace('</div><!-- /tab-exercises -->',
                  '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 1); n += 1

    # 4. complementares
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary nao unico'
    s = s.replace('</div><!-- /tab-complementary -->',
                  '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); n += 1

    # 5. totalLessons
    assert 'var totalLessons=15;' in s, f'{path}: totalLessons=15 nao encontrado'
    s = s.replace('var totalLessons=15;', 'var totalLessons=16;', 1); n += 1

    # 6. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD15_TAIL) == 1, f'{path}: ancora card 15 nao unica'
        s = s.replace(CARD15_TAIL, CARD15_TAIL + '\n' + CARD16, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'walyson-ginaldo-silva.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'walyson-ginaldo-silva.html'), False)
print('hubs atualizados (aditivo).')
