#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 20 nos hubs (prof + aluno) de natalie-viegas de forma
ADITIVA, respeitando o layout LEGADO dela. Aulas 1-19 ficam intactas. Idempotente.

Layout do hub da Natalie:
  - prof: ex-lesson-1..4 inline + cards <a target=_blank> standalone (aulas 5-19) na tab-inclass
  - aluno: SO Pre-class (accordion ex-lesson-N) + Complementares; NAO tem tab-inclass
    => o card do menu IN CLASS vai SO no prof; aluno recebe stamp + accordion + complementares.
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

ORDER_AMAP = '  "[order-l20]": "/audio/natalie-viegas/pc20_order_l20.mp3",'


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card = between('prof e aluno c/ /aluno/) -->\n', '\n\n<!-- 2. STAMP')
stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n\n<!-- 3. ACCORDION')
accordion = between('prof E aluno) -->\n', '\n\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '</script>').strip('\n')


def div_end(s, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced div from %d' % start)


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-20"' in s or 'natalie-viegas-aula20.html' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 20 ja integrada)')
        return
    orig = len(s)

    # 1. stamp20 apos stamp19
    m = re.search(r'<div class="stamp" id="stamp19"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-20 apos o fim do ex-lesson-19
    st = s.index('<div class="lesson-card" id="ex-lesson-19">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l20 apos o ultimo wrapper l19
    yi = s.index('data-media="l19-podcast"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lancamento da aula 20 (SO no prof — aluno nao tem tab-inclass)
    if is_prof:
        m18 = re.search(r'<a href="/professor/natalie-viegas-aula19\.html[^"]*".*?</a>', s, flags=re.S)
        if not m18:
            raise RuntimeError('card da aula 19 nao encontrado no prof')
        s = s[:m18.end()] + '\n\n' + card + s[m18.end():]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l20]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 20
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=20', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'natalie-viegas.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'natalie-viegas.html'), False)
print('OK')
