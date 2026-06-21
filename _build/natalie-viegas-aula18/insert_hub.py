#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 18 nos hubs (prof + aluno) de natalie-viegas de forma
ADITIVA, respeitando o layout LEGADO dela. Aulas 1-17 ficam intactas. Idempotente.

Layout do hub da Natalie:
  - prof: ex-lesson-1..4 inline + cards <a target=_blank> standalone (aulas 5-17) na tab-inclass
  - aluno: SO Pre-class (accordion ex-lesson-N) + Complementares; NAO tem tab-inclass
    => o card do menu IN CLASS vai SO no prof; aluno recebe stamp + accordion + complementares.
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

ORDER_AMAP = '  "[order-l18]": "/audio/natalie-viegas/pc18_order_l18.mp3",'


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


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


def make_card(s):
    """Clona o card <a> da aula 17 (estilo legado standalone) e reescreve p/ aula 18 (so prof)."""
    m = re.search(r'<a href="/professor/natalie-viegas-aula17\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 17 nao encontrado no prof')
    card = m.group(0)
    card = card.replace('natalie-viegas-aula17.html', 'natalie-viegas-aula18.html')
    card = card.replace('>17<', '>18<')
    card = card.replace('Leading the Status Meeting -- Moderating &amp; Handling Questions',
                        'Persuading and Influencing -- Making a Recommendation')
    card = card.replace('Indirect questions -- 27 slides',
                        'Emphasis for persuasion -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-18"' in s or 'natalie-viegas-aula18.html' in s:
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

    # 3. complementares l18 apos o ultimo wrapper l17
    yi = s.index('data-media="l17-podcast"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lancamento da aula 18 (SO no prof — aluno nao tem tab-inclass)
    if is_prof:
        card = make_card(s)
        m17 = re.search(r'<a href="/professor/natalie-viegas-aula17\.html".*?</a>', s, flags=re.S)
        s = s[:m17.end()] + '\n\n' + card + s[m17.end():]

    # 5. entradas de audioMap (logo apos a abertura do objeto) + [order-l18]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 18
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=18', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'natalie-viegas.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'natalie-viegas.html'), False)
print('OK')
