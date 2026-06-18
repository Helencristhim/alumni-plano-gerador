#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert aula 12 snippets ADITIVAMENTE no hub fabiana-michelly-silva (prof + aluno).
Não toca em nada das aulas 1-11. Apenas adiciona: IN CLASS card, stamp12,
ex-lesson-12 (após ex-lesson-11), complementares l12 (após l11), entradas de
audioMap, e totalLessons 11->12."""
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

    # 1. IN CLASS card: after aula11 card's closing </a> (PROF hub only;
    #    aluno hub has no IN CLASS card list).
    anchor11 = f'<a href="/{side}/fabiana-michelly-silva-aula11.html?autostart=1"'
    if anchor11 in h:
        idx = h.index(anchor11)
        close = h.index('</a>', idx) + len('</a>')
        cardside = card if side == 'professor' else card.replace('/professor/', '/aluno/')
        h = h[:close] + '\n' + cardside + h[close:]

    # 2. stamp after stamp11 line
    s11 = h.index('id="stamp11"')
    s11end = h.index('\n', s11) + 1
    h = h[:s11end] + stamp + '\n' + h[s11end:]

    # 3. ex-lesson-12 after ex-lesson-11 closes. ex-lesson-11 is the last pre-class
    #    card; it ends right before the close of the exercises tab.
    close_ex = h.index('</div><!-- /tab-exercises -->')
    h = h[:close_ex] + prec + '\n' + h[close_ex:]

    # 4. complementares after l11-youtube wrapper closes
    yt = h.index('data-media="l11-youtube"')
    # the wrapper closes at the </div> that matches media-card-wrapper; find the
    # block end: next occurrence of '</div>\n</div>\n</div>' style is fragile, so
    # find the start of the NEXT structural element after the youtube block.
    # The l11-youtube media-card-wrapper is the last l11 card; insert right after it.
    # Find its closing by locating the media-tip then the 3 closing divs.
    tip = h.index('</p>', h.index('media-tip', yt))
    # after tip: </div>(media-info) </div>(media-card) </div>(media-card-wrapper)
    seg = h[tip:]
    m = re.search(r'(</p>\s*</div>\s*</div>\s*</div>)', seg)
    end = tip + m.end()
    h = h[:end] + '\n' + compl + h[end:]

    # 5. audioMap: insert kv before the first '};' that closes the top audioMap
    am = h.index('var audioMap = {')
    amclose = h.index('};', am)
    h = h[:amclose] + audio_kv + '\n' + h[amclose:]

    # 6. totalLessons 11 -> 12
    h = h.replace('var totalLessons = 11;', 'var totalLessons = 12;')

    assert h != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-len(orig)} chars)')

process(os.path.join(ROOT, 'public', 'professor', 'fabiana-michelly-silva.html'), 'professor')
process(os.path.join(ROOT, 'public', 'aluno', 'fabiana-michelly-silva.html'), 'aluno')
