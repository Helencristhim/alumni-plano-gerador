#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 20 nos hubs (prof + aluno) de graziele-dias de forma ADITIVA.
Aulas 1-19 intactas. Idempotente: se ex-lesson-20 ja existe, aborta."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

# entrada extra de audioMap p/ o listen do ordering (extra_audio nao entra no snippet)
ORDER_AMAP = '  "[order-l20]": "/audio/graziele-dias/pc20_order_l20.mp3",'


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card_prof = between('prof e aluno c/ /aluno/) -->\n', '\n<!-- 2. STAMP')
stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '\n</script>').strip('\n')

assert card_prof and stamp and accordion and comp and amap_entries, 'snippet parse falhou'


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
    if 'id="ex-lesson-20"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 20 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp20 apos stamp19
    m = re.search(r'<div class="stamp" id="stamp19"[^>]*></div>', s)
    assert m, f'{path}: stamp19 nao encontrado'
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-20 apos ex-lesson-19
    st = s.index('<div class="lesson-card" id="ex-lesson-19">')
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l18 apos o ultimo wrapper l17
    yi = s.index('data-media="l19-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('graziele-dias-aula19.html?autostart=1')
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l20]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 18
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=20', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'graziele-dias.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'graziele-dias.html'), False)
print('OK')
