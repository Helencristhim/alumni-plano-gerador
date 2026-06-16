#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 7 nos hubs (prof + aluno) de erica-maria-machado-santarem
de forma ADITIVA. Aulas 1-6 intactas. Idempotente: se ex-lesson-7 ja existe, aborta.
Molde aula6: ancoras stamp6/ex-lesson-6/l6-youtube/aula6.html?autostart=1.
O hub re-onboardado ja tem stamps 1-7 no header, entao a insercao de stamp e GUARDADA
(so insere se id="stamp7" ainda nao existir)."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

# entrada extra de audioMap p/ o listen do ordering (extra_audio nao entra no snippet)
ORDER_AMAP = '  "[order-l7]": "/audio/erica-maria-machado-santarem/pc7_order_l7.mp3",'


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
    if 'id="ex-lesson-7"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 7 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp7 apos stamp6 — SO se ainda nao existir (re-onboard ja trouxe stamps 1-7)
    if 'id="stamp7"' not in s:
        m = re.search(r'<div class="stamp" id="stamp6"[^>]*></div>', s)
        s = s[:m.end()] + '\n' + stamp + s[m.end():]
    else:
        print(f'  (stamp7 ja existe em {os.path.basename(path)} — insercao de stamp pulada)')

    # 2. accordion ex-lesson-7 apos ex-lesson-6
    st = s.index('<div class="lesson-card" id="ex-lesson-6">')
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l7 apos o ultimo wrapper l6
    yi = s.index('data-media="l6-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('erica-maria-machado-santarem-aula6.html?autostart=1')
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l7]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 7
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=7', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'erica-maria-machado-santarem.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'erica-maria-machado-santarem.html'), False)
print('OK')
