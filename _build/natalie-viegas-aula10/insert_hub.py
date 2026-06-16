#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 10 nos hubs (prof + aluno) de natalie-viegas de forma
ADITIVA, respeitando o layout LEGADO dela (hub da Helen: ex-lesson 1-4 inline +
aulas 5-9 como cards <a> standalone). Aulas 1-9 ficam intactas. Idempotente."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

ORDER_AMAP = '  "[order-l10]": "/audio/natalie-viegas/pc10_order_l10.mp3",'


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
    """Clona o card <a> da aula 9 (mantendo o estilo legado da Helen) e reescreve p/ aula 10."""
    who = 'professor' if is_prof else 'aluno'
    m = re.search(r'<a href="/' + who + r'/natalie-viegas-aula9\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 9 não encontrado em ' + who)
    card = m.group(0)
    card = card.replace('natalie-viegas-aula9.html', 'natalie-viegas-aula10.html')
    card = card.replace('>09<', '>10<')
    card = card.replace('Agreeing and Disagreeing -- Professional Debates',
                        'Handling Difficult Conversations -- Giving and Receiving Feedback')
    card = card.replace('Linking words for contrast -- 27 slides',
                        'Reported speech -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-10"' in s or 'natalie-viegas-aula10.html' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 10 já integrada)')
        return
    orig = len(s)

    # 1. stamp10 após stamp9
    m = re.search(r'<div class="stamp" id="stamp9"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-10 após o fim do ex-lesson-9
    st = s.index('<div class="lesson-card" id="ex-lesson-9">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l10 após o último wrapper l9
    yi = s.index('data-media="l9-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lançamento da aula 10 (clone do card legado da aula 9)
    card = make_card(s, is_prof)
    a9 = list(re.finditer(r'<a href="/(?:professor|aluno)/natalie-viegas-aula9\.html".*?</a>', s, flags=re.S))
    target = a9[-1]  # prof: o último (tab-inclass); aluno: o único (tab-exercises)
    s = s[:target.end()] + '\n\n' + card + s[target.end():]

    # 5. entradas de audioMap (logo após a abertura do objeto) + [order-l10]
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + '\n' + ORDER_AMAP + s[am.end():]

    # 6. totalLessons -> 10
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=10', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'natalie-viegas.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'natalie-viegas.html'), False)
print('OK')
