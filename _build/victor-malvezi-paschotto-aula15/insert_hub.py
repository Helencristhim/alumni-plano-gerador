#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 15 da Gabriela nos hubs (prof + aluno) de forma ADITIVA.
Aulas passadas intactas. Idempotente: se ex-lesson-15 ja existe, aborta.

Ambos os hubs (prof e aluno) ja tem a aula 14 como ultima aula (ex-lesson-14,
stamp14, l14). Por isso AMBOS ancoram em last_n=14."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()


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


def patch(path, is_prof, last_n):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-15"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 15 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp15 apos o ultimo stamp existente
    m = re.search(r'<div class="stamp" id="stamp%d"[^>]*></div>' % last_n, s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-15 apos o ultimo ex-lesson existente
    st = s.index('<div class="lesson-card" id="ex-lesson-%d">' % last_n)
    en = div_end(s, st)
    s = s[:en] + '\n' + accordion + s[en:]

    # 3. complementares l15 apos o ultimo wrapper l{last_n}
    yi = s.index('data-media="l%d-youtube"' % last_n)
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card IN CLASS (so prof; aluno nao tem aba inclass)
    if is_prof:
        ci = s.index('victor-malvezi-paschotto-aula%d.html?autostart=1' % last_n)
        ce = s.index('</a>', ci) + len('</a>')
        s = s[:ce] + '\n' + card_prof + s[ce:]

    # 5. entradas de audioMap (logo apos a abertura do objeto)
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + s[am.end():]

    # 6. totalLessons -> 15
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=15', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'victor-malvezi-paschotto.html'), True, 14)
patch(os.path.join(ROOT, 'public', 'aluno', 'victor-malvezi-paschotto.html'), False, 14)
print('OK')
