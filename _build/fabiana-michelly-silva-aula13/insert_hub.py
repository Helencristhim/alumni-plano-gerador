#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert aula 13 snippets ADITIVAMENTE no hub fabiana-michelly-silva (prof + aluno).
Não toca em nada das aulas 1-12. Apenas adiciona: IN CLASS card, stamp13,
ex-lesson-13 (após ex-lesson-12), complementares l13 (após l12), entradas de
audioMap, e totalLessons 12->13."""
import re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

def get(a, b):
    i = SNIP.index(a); j = SNIP.index(b)
    return '\n'.join(SNIP[i:j].split('\n')[1:]).strip()

card  = get('<!-- 1.', '<!-- 2.')
stamp = get('<!-- 2.', '<!-- 3. ACCORDION')
prec  = get('<!-- 3. ACCORDION', '<!-- 3b.')
compl = get('<!-- 3b.', '<!-- 4.')
audio_block = get('<!-- 4.', '<!-- 5.')
# audio_block is <script> ...kv lines... </script> ; extract kv lines
audio_kv = re.sub(r'</?script>', '', audio_block).strip()

def process(path, side):
    h = open(path, encoding='utf-8').read()
    orig = h

    # 1. IN CLASS card: after aula12 card's closing </a> (PROF hub only;
    #    aluno hub has no IN CLASS card list).
    anchor12 = f'<a href="/{side}/fabiana-michelly-silva-aula12.html?autostart=1"'
    if anchor12 in h:
        idx = h.index(anchor12)
        close = h.index('</a>', idx) + len('</a>')
        cardside = card if side == 'professor' else card.replace('/professor/', '/aluno/')
        h = h[:close] + '\n' + cardside + h[close:]

    # 2. stamp after stamp12 line
    s12 = h.index('id="stamp12"')
    s12end = h.index('\n', s12) + 1
    h = h[:s12end] + stamp + '\n' + h[s12end:]

    # 3. ex-lesson-13 after ex-lesson-12 closes. ex-lesson-12 is the last pre-class
    #    card; it ends right before the close of the exercises tab.
    close_ex = h.index('</div><!-- /tab-exercises -->')
    h = h[:close_ex] + prec + '\n' + h[close_ex:]

    # 4. complementares after l12-youtube wrapper closes
    yt = h.index('data-media="l12-youtube"')
    tip = h.index('</p>', h.index('media-tip', yt))
    seg = h[tip:]
    m = re.search(r'(</p>\s*</div>\s*</div>\s*</div>)', seg)
    end = tip + m.end()
    h = h[:end] + '\n' + compl + h[end:]

    # 5. audioMap: insert kv before the first '};' that closes the top audioMap
    am = h.index('var audioMap = {')
    amclose = h.index('};', am)
    h = h[:amclose] + audio_kv + '\n' + h[amclose:]

    # 6. totalLessons 12 -> 13
    h = h.replace('var totalLessons = 12;', 'var totalLessons = 13;')

    assert h != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-len(orig)} chars)')

process(os.path.join(ROOT, 'public', 'professor', 'fabiana-michelly-silva.html'), 'professor')
process(os.path.join(ROOT, 'public', 'aluno', 'fabiana-michelly-silva.html'), 'aluno')
