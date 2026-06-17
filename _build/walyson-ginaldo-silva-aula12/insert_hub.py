#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 12 (Making Presentations) nos hubs prof + aluno de
walyson-ginaldo-silva de forma ADITIVA e idempotente. Hub do modelo (cards <a>
IN CLASS com ?autostart=1, ex-lesson accordions, stamps, complementares).

Aulas 1-11 ficam intactas. Prof recebe card IN CLASS + stamp + accordion +
complementares + audioMap + totalLessons. Aluno (2 abas) recebe stamp + accordion
+ complementares + audioMap + totalLessons, mas NUNCA card <a> de slides."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'walyson-ginaldo-silva.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'walyson-ginaldo-silva.html')
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card = between('prof e aluno c/ /aluno/) -->\n', '\n\n<!-- 2. STAMP')
stamp = between('stamps-row do header) -->\n', '\n\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '</script>').strip('\n')


def div_end(s, start):
    """Retorna o índice logo após o </div> que fecha a <div> que começa em start."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced div from %d' % start)


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-12"' in s or 'data-media="l12-' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 12 ja integrada)')
        return
    orig = len(s)

    # 1. CARD IN CLASS (só prof) — após o </a> da aula 11
    if is_prof:
        anchor = '/professor/walyson-ginaldo-silva-aula11.html?autostart=1'
        i = s.index(anchor)
        close = s.index('</a>', i) + len('</a>')
        s = s[:close] + '\n' + card + s[close:]

    # 2. STAMP — após o stamp11
    m = re.search(r'<div class="stamp" id="stamp11"[^>]*></div>', s)
    assert m, 'stamp11 nao encontrado em ' + path
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 3. ACCORDION Pre-class — após o lesson-card ex-lesson-11 (div balanceada)
    j = s.index('id="ex-lesson-11"')
    card_start = s.rindex('<div', 0, j)
    end = div_end(s, card_start)
    s = s[:end] + '\n' + accordion + s[end:]

    # 3b. COMPLEMENTARES — após o wrapper l11-youtube (div balanceada)
    k = s.index('data-media="l11-youtube"')
    comp_start = s.rindex('<div', 0, k)
    comp_e = div_end(s, comp_start)
    s = s[:comp_e] + '\n' + comp + s[comp_e:]

    # 4. audioMap — mesclar entradas no objeto audioMap do hub
    am = s.index('var audioMap = {')
    brace = s.index('{', am)
    s = s[:brace + 1] + '\n' + amap_entries + '\n' + s[brace + 1:]

    # 5. totalLessons 11 -> 12
    s, n = re.subn(r'totalLessons=11\b', 'totalLessons=12', s)
    assert n >= 1, 'totalLessons=11 nao encontrado em ' + path

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  OK {os.path.basename(path)} (+{len(s)-orig} bytes)')


patch(PROF, is_prof=True)
patch(ALUNO, is_prof=False)
print('Hubs atualizados (aditivo).')
