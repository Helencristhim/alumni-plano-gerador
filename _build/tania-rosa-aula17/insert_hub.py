#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 17 da Tania Rosa nos hubs
monoliticos (inline) prof/aluno. NAO toca aulas 1-16. Adiciona: card IN CLASS (so
prof, link para o standalone com ?autostart=1), stamp17, accordion Pre-class, bloco
Complementares, entradas audioMap (+ [goals-l17]) e ajusta totalLessons 16->17.
TOTAL_AULAS ja esta em 20 (milestone do roster) — nao mexe.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AUDIO_BASE = '/audio/tania-rosa/'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# --- audioMap entries do snippet (parte 4) ---
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>(.*?)</script>', snip, re.S)
amap_lines = [l for l in m.group(1).splitlines() if l.strip()]
# o snippet nao inclui a chave [goals-l17] (usada no card "ordem" do Pre-class) — adicionar
amap_lines.append(f'  "[goals-l17]": "{AUDIO_BASE}pc17_dream_goals.mp3",')
amap_block = '\n'.join(amap_lines)

# Complementares como bloco no padrao do hub da Tania (hr + h3 + media-grid)
COMP_BLOCK = (
    '\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n'
    '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:.5rem">'
    'Materiais Complementares &mdash; Aula 17</h3>\n'
    '<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: falar sobre o futuro e os sonhos &mdash; '
    'contar a um amigo o que voc&ecirc; gostaria de fazer, onde adoraria ir e o que espera conquistar. '
    'Foco: would like to / hope to / would love to + verbo (I would like to live abroad / I hope to become fluent) '
    'e vocabul&aacute;rio de sonhos e objetivos (dream, goal, abroad, bucket list, achieve). '
    'Marque como conclu&iacute;do ao terminar.</p>\n'
    '<div class="media-grid">\n' + complementary + '\n</div>\n')

# Card IN CLASS (so prof): link para o standalone, formato identico aos cards da Tania (accent)
CARD17 = (
    '    <a href="/professor/tania-rosa-aula17.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">17</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Talking About the Future &amp; Dreams</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">would like to &amp; hope to &mdash; 28 slides</div></div>\n'
    '    </a>')

STAMP16 = ('<div class="stamp" id="stamp16" data-label="Opinions &amp; Tips" style="background-image:url(\''
           'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>')
STAMP17 = ('\n<div class="stamp" id="stamp17" data-label="Dreams &amp; Goals" style="background-image:url(\''
           'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=200&q=80\')"></div>')

# anchor da ultima IN CLASS card (aula 16, Giving Opinions & Recommendations) no prof
CARD16_TAIL = (
    '<div style="font-weight:600;font-size:.95rem">Giving Opinions &amp; Recommendations</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">so/such a &amp; would recommend &mdash; 28 slides</div></div>\n'
    '    </a>')

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

    # 2. stamp17
    assert s.count(STAMP16) == 1, f'{path}: ancora stamp16 nao unica'
    s = s.replace(STAMP16, STAMP16 + STAMP17, 1); n += 1

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

    # 5. totalLessons 16 -> 17
    assert 'var totalLessons=16;' in s, f'{path}: totalLessons=16 nao encontrado'
    s = s.replace('var totalLessons=16;', 'var totalLessons=17;', 1); n += 1

    # 6. TOTAL_AULAS ja em 20 (nao mexe)
    assert 'window.TOTAL_AULAS=20;' in s, f'{path}: TOTAL_AULAS=20 nao encontrado'

    # 7. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD16_TAIL) == 1, f'{path}: ancora card 16 nao unica'
        s = s.replace(CARD16_TAIL, CARD16_TAIL + '\n' + CARD17, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'tania-rosa.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'tania-rosa.html'), False)
print('hubs atualizados (aditivo, aula 17).')
