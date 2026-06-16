#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 8 nos hubs (prof + aluno) de natalie-viegas de forma
ADITIVA, respeitando o layout LEGADO dela (hub da Helen: ex-lesson 1-4 inline +
aulas 5-7 como cards <a> standalone). Aulas 1-7 ficam intactas. Idempotente."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

ORDER_AMAP = '  "[order-l8]": "/audio/natalie-viegas/pc8_order_l8.mp3",'


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


def make_card(s, is_prof):
    """Clona o card <a> da aula 7 (mantendo o estilo legado da Helen) e reescreve p/ aula 8."""
    who = 'professor' if is_prof else 'aluno'
    m = re.search(r'<a href="/' + who + r'/natalie-viegas-aula7\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 7 não encontrado em ' + who)
    card = m.group(0)
    card = card.replace('natalie-viegas-aula7.html', 'natalie-viegas-aula8.html')
    card = card.replace('>07<', '>08<')
    card = card.replace('Procurement &amp; Tenders -- Winning the Bid',
                        'Presenting to Leadership -- The Elevator Pitch')
    card = card.replace('First conditional + polite requests -- 27 slides',
                        'Present perfect + quantifiers -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-8"' in s or 'natalie-viegas-aula8.html' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 8 já integrada)')
        return
    orig = len(s)

    # 1. stamp8 após stamp7
    m = re.search(r'<div class="stamp" id="stamp7"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-8 após o fim do ex-lesson-7
    st = s.index('<div class="lesson-card" id="ex-lesson-7">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l8 após o último wrapper l7
    yi = s.index('data-media="l7-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lançamento da aula 8 (clone do card legado da aula 7)
    card = make_card(s, is_prof)
    a7 = list(re.finditer(r'<a href="/(?:professor|aluno)/natalie-viegas-aula7\.html".*?</a>', s, flags=re.S))
    target = a7[-1]  # prof: o último (tab-inclass); aluno: o único (tab-exercises)
    s = s[:target.end()] + '\n\n' + card + s[target.end():]

    # 5. entradas de audioMap (logo após a abertura do objeto) + [order-l8]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 8
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=8', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'natalie-viegas.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'natalie-viegas.html'), False)
print('OK')
