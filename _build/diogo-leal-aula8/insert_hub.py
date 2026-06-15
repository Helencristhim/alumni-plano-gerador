#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 8 nos hubs (prof + aluno) de forma ADITIVA.
Aulas passadas intactas. Idempotente: se ex-lesson-8 ja existe, aborta."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

# entrada extra de audioMap p/ o listen do ordering (extra_audio nao entra no snippet)
ORDER_AMAP = '  "[order-l8]": "/audio/diogo-leal/a8_order_pilot.mp3",'


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card_prof = between('prof e aluno c/ /aluno/) -->\n', '\n<!-- 2. STAMP')
stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '\n</script>').strip('\n')


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
    if 'id="ex-lesson-8"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 8 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp8 apos stamp7
    m = re.search(r'<div class="stamp" id="stamp7"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-8 apos ex-lesson-7
    st = s.index('<div class="lesson-card" id="ex-lesson-7">')
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l8 apos o ultimo wrapper l7
    yi = s.index('data-media="l7-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('diogo-leal-aula7.html?autostart=1')
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l8]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 8
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=8', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'diogo-leal.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'diogo-leal.html'), False)
print('OK')
