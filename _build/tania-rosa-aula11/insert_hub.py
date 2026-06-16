#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 11 da Tania Rosa nos hubs
monoliticos (inline) prof/aluno. NAO toca aulas 1-10. Adiciona: card IN CLASS (so
prof, link para o standalone com ?autostart=1), stamp11, accordion Pre-class, bloco
Complementares, entradas audioMap (+ [order-l11]) e ajusta totalLessons 10->11 e
TOTAL_AULAS 10->20.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/tania-rosa/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) + [order-l11] ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
amap_lines.append(f'  "[order-l11]": "{AUDIO_BASE}pc11_order_smalltalk.mp3",')
amap_block = '\n'.join(amap_lines)

# Complementares como bloco no padrao do hub da Tania (hr + h3 + media-grid)
COMP_BLOCK = (
    '\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n'
    '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:.5rem">'
    'Materiais Complementares &mdash; Aula 11</h3>\n'
    '<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: small talk &mdash; '
    'conversar com desconhecidos durante as viagens. Foco: question forms e tag questions. '
    'Marque como conclu&iacute;do ao terminar.</p>\n'
    '<div class="media-grid">\n' + complementary + '\n</div>\n')

# Card IN CLASS (so prof): link para o standalone, formato identico aos cards da Tania (accent)
CARD11 = (
    '    <a href="/professor/tania-rosa-aula11.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">11</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Small Talk</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Question forms &amp; tag questions &mdash; 28 slides</div></div>\n'
    '    </a>')

STAMP10 = ('<div class="stamp" id="stamp10" data-label="Mastery" style="background-image:url(\''
           'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>')
STAMP11 = ('\n<div class="stamp" id="stamp11" data-label="Small Talk" style="background-image:url(\''
           'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=200&q=80\')"></div>')

# anchor da ultima IN CLASS card (aula 10) no prof, para inserir a card 11 depois
CARD10_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">Putting It All Together</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Review and Confidence &mdash; 37 slides</div></div>\n'
    '    </div>')

PROF_TAB3 = '<!-- ========== TAB 3: IN CLASS ========== -->'
PROF_SLIDES = '<!-- ============================== SLIDES WRAPPER (IN CLASS) ============================== -->'
ALUNO_TABCOMP = '<div class="tab-content" id="tab-complementary">'
ALUNO_SCRIPT = '<script>\nfunction switchTab(tabId){document.querySelectorAll(\'.tab-content\')'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. audioMap
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); n += 1

    # 2. stamp11
    assert s.count(STAMP10) == 1, f'{path}: ancora stamp10 nao unica'
    s = s.replace(STAMP10, STAMP10 + STAMP11, 1); n += 1

    # 3. accordion Pre-class
    if is_prof:
        assert s.count(PROF_TAB3) == 1, f'{path}: TAB 3 anchor nao unico'
        s = s.replace(PROF_TAB3, preclass + '\n\n' + PROF_TAB3, 1); n += 1
    else:
        assert s.count(ALUNO_TABCOMP) == 1, f'{path}: tab-complementary anchor nao unico'
        s = s.replace(ALUNO_TABCOMP, preclass + '\n\n' + ALUNO_TABCOMP, 1); n += 1

    # 4. complementares
    if is_prof:
        assert s.count(PROF_SLIDES) == 1, f'{path}: SLIDES WRAPPER anchor nao unico'
        s = s.replace(PROF_SLIDES, COMP_BLOCK + '\n' + PROF_SLIDES, 1); n += 1
    else:
        assert s.count(ALUNO_SCRIPT) == 1, f'{path}: aluno script anchor nao unico'
        s = s.replace(ALUNO_SCRIPT, COMP_BLOCK + '\n' + ALUNO_SCRIPT, 1); n += 1

    # 5. totalLessons 10 -> 11
    assert 'var totalLessons=10;' in s, f'{path}: totalLessons=10 nao encontrado'
    s = s.replace('var totalLessons=10;', 'var totalLessons=11;', 1); n += 1

    # 6. TOTAL_AULAS 10 -> 20 (milestone do roster)
    assert 'window.TOTAL_AULAS=10;' in s, f'{path}: TOTAL_AULAS=10 nao encontrado'
    s = s.replace('window.TOTAL_AULAS=10;', 'window.TOTAL_AULAS=20;', 1); n += 1

    # 7. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD10_TAIL) == 1, f'{path}: ancora card 10 nao unica'
        s = s.replace(CARD10_TAIL, CARD10_TAIL + '\n' + CARD11, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'tania-rosa.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'tania-rosa.html'), False)
print('hubs atualizados (aditivo).')
