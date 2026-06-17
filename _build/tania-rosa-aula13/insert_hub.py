#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 13 da Tania Rosa nos hubs
monoliticos (inline) prof/aluno. NAO toca aulas 1-12. Adiciona: card IN CLASS (so
prof, link para o standalone com ?autostart=1), stamp13, accordion Pre-class, bloco
Complementares, entradas audioMap (+ [order-l13]) e ajusta totalLessons 12->13.
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
# o snippet nao inclui a chave [order-l13] (usada no card "ordem" do Pre-class) — adicionar
amap_lines.append(f'  "[order-l13]": "{AUDIO_BASE}pc13_order_planning.mp3",')
amap_block = '\n'.join(amap_lines)

# Complementares como bloco no padrao do hub da Tania (hr + h3 + media-grid)
COMP_BLOCK = (
    '\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n'
    '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:.5rem">'
    'Materiais Complementares &mdash; Aula 13</h3>\n'
    '<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: fazer planos &mdash; '
    'falar sobre a pr&oacute;xima viagem com going to (planos) e will (decis&otilde;es de momento). '
    'Foco: futuro e vocabul&aacute;rio de planejamento (book, budget, packing list). '
    'Marque como conclu&iacute;do ao terminar.</p>\n'
    '<div class="media-grid">\n' + complementary + '\n</div>\n')

# Card IN CLASS (so prof): link para o standalone, formato identico aos cards da Tania (accent)
CARD13 = (
    '    <a href="/professor/tania-rosa-aula13.html?autostart=1" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" '
    'onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;'
    'display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">13</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Making Plans</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Future with going to &amp; will &mdash; 28 slides</div></div>\n'
    '    </a>')

STAMP12 = ('<div class="stamp" id="stamp12" data-label="Sharing Opinions" style="background-image:url(\''
           'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>')
STAMP13 = ('\n<div class="stamp" id="stamp13" data-label="Making Plans" style="background-image:url(\''
           'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>')

# anchor da ultima IN CLASS card (aula 12, Sharing Opinions) no prof, para inserir a card 13 depois
CARD12_TAIL = (
    '      <div><div style="font-weight:600;font-size:.95rem">Sharing Opinions</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Agreeing &amp; disagreeing &mdash; 28 slides</div></div>\n'
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

    # 2. stamp13
    assert s.count(STAMP12) == 1, f'{path}: ancora stamp12 nao unica'
    s = s.replace(STAMP12, STAMP12 + STAMP13, 1); n += 1

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

    # 5. totalLessons 12 -> 13
    assert 'var totalLessons=12;' in s, f'{path}: totalLessons=12 nao encontrado'
    s = s.replace('var totalLessons=12;', 'var totalLessons=13;', 1); n += 1

    # 6. TOTAL_AULAS ja em 20 (nao mexe)
    assert 'window.TOTAL_AULAS=20;' in s, f'{path}: TOTAL_AULAS=20 nao encontrado'

    # 7. card IN CLASS (so prof)
    if is_prof:
        assert s.count(CARD12_TAIL) == 1, f'{path}: ancora card 12 nao unica'
        s = s.replace(CARD12_TAIL, CARD12_TAIL + '\n' + CARD13, 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'tania-rosa.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'tania-rosa.html'), False)
print('hubs atualizados (aditivo, aula 13).')
