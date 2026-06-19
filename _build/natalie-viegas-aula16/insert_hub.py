#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 16 nos hubs (prof + aluno) de natalie-viegas de forma
ADITIVA, respeitando o layout LEGADO dela. Aulas 1-15 ficam intactas. Idempotente.

Layout do hub da Natalie:
  - prof: ex-lesson-1..4 inline + cards <a target=_blank> standalone (aulas 5-15) na tab-inclass
  - aluno: SÓ Pre-class (accordion ex-lesson-N) + Complementares; NÃO tem tab-inclass
    => o card do menu IN CLASS vai SÓ no prof; aluno recebe stamp + accordion + complementares.
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

ORDER_AMAP = '  "[order-l16]": "/audio/natalie-viegas/pc16_order_l16.mp3",'


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
    """Clona o card <a> da aula 15 (estilo legado standalone) e reescreve p/ aula 16 (só prof)."""
    m = re.search(r'<a href="/professor/natalie-viegas-aula15\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 15 não encontrado no prof')
    card = m.group(0)
    card = card.replace('natalie-viegas-aula15.html', 'natalie-viegas-aula16.html')
    card = card.replace('>15<', '>16<')
    card = card.replace('Project Kick-off -- Giving Updates',
                        'Project Updates -- Reporting Progress')
    card = card.replace('Future continuous -- 27 slides',
                        'Present perfect continuous -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-16"' in s or 'natalie-viegas-aula16.html' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 16 já integrada)')
        return
    orig = len(s)

    # 1. stamp16 após stamp15
    m = re.search(r'<div class="stamp" id="stamp15"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-16 após o fim do ex-lesson-15
    st = s.index('<div class="lesson-card" id="ex-lesson-15">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l16 após o último wrapper l15
    yi = s.index('data-media="l15-podcast"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lançamento da aula 16 (SÓ no prof — aluno não tem tab-inclass)
    if is_prof:
        card = make_card(s)
        m15 = re.search(r'<a href="/professor/natalie-viegas-aula15\.html".*?</a>', s, flags=re.S)
        s = s[:m15.end()] + '\n\n' + card + s[m15.end():]

    # 5. entradas de audioMap (logo após a abertura do objeto) + [order-l16]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 16
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=16', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'natalie-viegas.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'natalie-viegas.html'), False)
print('OK')
