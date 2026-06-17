#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 14 nos hubs (prof + aluno) de eduardo-chiba de forma
ADITIVA. Hub legado da Helen: ex-lesson 1-13 + aulas 5-13 como cards <a>
standalone (SO no prof). Aulas 1-13 ficam intactas. Idempotente.

Aluno tem 2 abas (Pre-class + Complementares) e NAO tem card de lancamento IN CLASS:
no aluno inserimos stamp + accordion + complementares + audioMap + totalLessons,
mas NUNCA um card <a> de slides."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(__file__)
SN = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


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
    """Clona o card <a> da aula 13 (estilo legado da Helen, so no prof) e reescreve p/ aula 14."""
    m = re.search(r'<a href="/professor/eduardo-chiba-aula13\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 13 nao encontrado no prof')
    card = m.group(0)
    card = card.replace('eduardo-chiba-aula13.html', 'eduardo-chiba-aula14.html')
    card = card.replace('>13<', '>14<')
    card = card.replace('Q&amp;A Under Fire -- Thinking on Your Feet',
                        'Product Demo -- Showing the Platform')
    card = card.replace('Question forms &amp; hedging language -- 27 slides',
                        'Passive voice &amp; cause-and-effect -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-14"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 14 ja integrada)')
        return
    orig = len(s)

    # 1. stamp14 apos stamp13
    m = re.search(r'<div class="stamp" id="stamp13"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. accordion ex-lesson-14 apos o fim do ex-lesson-13
    st = s.index('<div class="lesson-card" id="ex-lesson-13">')
    en = div_end(s, st)
    s = s[:en] + '\n\n' + accordion + s[en:]

    # 3. complementares l14 apos o ultimo wrapper l13 (l13-podcast)
    yi = s.index('data-media="l13-podcast"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lancamento da aula 14 (SO no prof; aluno nao tem cards IN CLASS)
    if is_prof:
        card = make_card(s)
        a13 = list(re.finditer(r'<a href="/professor/eduardo-chiba-aula13\.html".*?</a>', s, flags=re.S))
        target = a13[-1]
        s = s[:target.end()] + '\n\n' + card + s[target.end():]

    # 5. entradas de audioMap (logo apos a abertura do objeto)
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + s[am.end():]

    # 6. totalLessons -> 14
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=14', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'eduardo-chiba.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'eduardo-chiba.html'), False)
print('OK')
