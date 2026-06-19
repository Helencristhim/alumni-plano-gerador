#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 18 nos hubs (prof + aluno) de victor-malvezi-paschotto
de forma ADITIVA. Prof tem cards IN CLASS (<a> ?autostart=1); aluno NAO tem cards
IN CLASS (so stamp + accordion + complementares + audioMap). Aulas 1-17 intactas.
Idempotente."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card = between('prof e aluno c/ /aluno/) -->\n', '\n\n<!-- 2. STAMP')
stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4. ENTRADAS')
amap_entries = between('<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>\n', '</script>').strip('\n')


def div_end(s, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced div from %d' % start)


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-18"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 18 ja integrada)')
        return
    orig = len(s)

    # 1. stamp18 apos stamp17
    m = re.search(r'<div class="stamp" id="stamp17"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-18 apos o fim do ex-lesson-17
    st = s.index('<div class="lesson-card" id="ex-lesson-17">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l17 apos o ultimo wrapper l16 (l17-youtube)
    yi = s.index('data-media="l17-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lancamento IN CLASS da aula 18 (SO no prof; aluno nao tem cards IN CLASS)
    if is_prof:
        a16 = list(re.finditer(r'<a href="/professor/victor-malvezi-paschotto-aula17\.html\?autostart=1".*?</a>', s, flags=re.S))
        if not a16:
            raise RuntimeError('card IN CLASS da aula 17 nao encontrado no prof')
        target = a16[-1]
        s = s[:target.end()] + '\n' + card + s[target.end():]

    # 5. entradas de audioMap (logo apos a abertura do objeto)
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + s[am.end():]

    # 6. totalLessons -> 17 (TOTAL_AULAS fica 24, intacto)
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=18', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'victor-malvezi-paschotto.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'victor-malvezi-paschotto.html'), False)
print('OK')
