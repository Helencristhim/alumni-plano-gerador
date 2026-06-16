#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 11 nos hubs (prof + aluno) de erica-maria-machado-santarem
de forma ADITIVA. Aulas 1-10 intactas. Idempotente: se ex-lesson-11 ja existe, aborta.
Molde aula10: ancoras stamp10/ex-lesson-10/l10-youtube/aula10.html?autostart=1.
A insercao de stamp e GUARDADA (so insere se id="stamp11" ainda nao existir)."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

# entrada extra de audioMap p/ o listen do ordering (extra_audio nao entra no snippet)
ORDER_AMAP = '  "[order-l11]": "/audio/erica-maria-machado-santarem/pc11_order_l11.mp3",'


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
    if 'id="ex-lesson-11"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 11 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp11 apos stamp10 — SO se ainda nao existir
    if 'id="stamp11"' not in s:
        m = re.search(r'<div class="stamp" id="stamp10"[^>]*></div>', s)
        s = s[:m.end()] + '\n' + stamp + s[m.end():]
    else:
        print(f'  (stamp11 ja existe em {os.path.basename(path)} — insercao de stamp pulada)')

    # 2. accordion ex-lesson-11 apos ex-lesson-10
    st = s.index('<div class="lesson-card" id="ex-lesson-10">')
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l11 apos o ultimo wrapper l10
    yi = s.index('data-media="l10-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('erica-maria-machado-santarem-aula10.html?autostart=1')
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l11]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 11
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=11', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'erica-maria-machado-santarem.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'erica-maria-machado-santarem.html'), False)
print('OK')
