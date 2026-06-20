#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere ADITIVAMENTE os snippets da aula 18 (gerados pelo build_from_model.py)
nos hubs (prof + aluno) da Carolina. Molde carolina-aula17.

Aulas 1-17 intactas. Idempotente: se ex-lesson-18 ja existe, aborta.
So adiciona: card IN CLASS (so prof), stamp18, accordion Pre-class, bloco de
Complementares, entradas de audioMap (+ [order-l18]) e ajusta totalLessons=18.
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

# entrada extra de audioMap p/ o listen do ordering (extra_audio nao entra no amap do snippet)
ORDER_AMAP = '  "[order-l18]": "/audio/carolina-paludetto-rodrigues/pc18_order_sequence.mp3",'


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card_prof = between('prof e aluno c/ /aluno/) -->\n', '\n<!-- 2. STAMP')
stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '\n</script>').strip('\n')

assert '<a href' in card_prof[:20], card_prof[:60]
assert 'id="stamp18"' in stamp, stamp[:60]
assert 'id="ex-lesson-18"' in accordion, accordion[:60]
assert 'data-media="l18-youtube"' in comp, comp[:60]
assert amap_entries and 'a18_' in amap_entries


def div_end(s, start):
    """Index just after the </div> that closes the <div> at start."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-18"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 18 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp18 apos stamp17
    m = re.search(r'<div class="stamp" id="stamp17"[^>]*></div>', s)
    assert m, f'{path}: ancora stamp17 nao encontrada'
    s = s[:m.end()] + '\n        ' + stamp + s[m.end():]

    # 2. accordion ex-lesson-18 apos ex-lesson-17
    st = s.index('<div class="lesson-card" id="ex-lesson-17">')
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l18 apos o ultimo wrapper de l17
    yi = s.index('data-media="l17-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('carolina-paludetto-rodrigues-aula17.html?autostart=1')
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l18]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    assert am, f'{path}: var audioMap nao encontrado'
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 18
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=18', s)

    assert s != open(path, encoding='utf-8').read()
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'carolina-paludetto-rodrigues.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'carolina-paludetto-rodrigues.html'), False)
print('hubs atualizados (aditivo).')
