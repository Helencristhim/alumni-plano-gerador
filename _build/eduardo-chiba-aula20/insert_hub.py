#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 20 nos hubs (prof + aluno) de eduardo-chiba de forma
ADITIVA. Hub legado da Helen: ex-lesson 1-19 + aulas 5-19 como cards <a>
standalone (SO no prof). Aulas 1-19 ficam intactas. Idempotente.

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
    """Clona o card <a> da aula 19 (estilo legado da Helen, so no prof) e reescreve p/ aula 20."""
    m = re.search(r'<a href="/professor/eduardo-chiba-aula19\.html".*?</a>', s, flags=re.S)
    if not m:
        raise RuntimeError('card da aula 19 nao encontrado no prof')
    card = m.group(0)
    card = card.replace('eduardo-chiba-aula19.html', 'eduardo-chiba-aula20.html')
    card = card.replace('>19<', '>20<')
    card = card.replace('Digital Communication -- Slack &amp; WhatsApp',
                        'Block 4 Review -- The Communication Audit')
    card = card.replace('Short-form professional register: chat tone, brevity &amp; etiquette -- 27 slides',
                        'All Block 4 writing: audit every channel -- 27 slides')
    return card


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-20"' in s:
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

    # 3. complementares l20 apos o ultimo wrapper l19 (l19-podcast)
    yi = s.index('data-media="l19-podcast"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    # 4. card de lancamento da aula 20 (SO no prof; aluno nao tem cards IN CLASS)
    if is_prof:
        card = make_card(s)
        a19 = list(re.finditer(r'<a href="/professor/eduardo-chiba-aula19\.html".*?</a>', s, flags=re.S))
        target = a19[-1]
        s = s[:target.end()] + '\n\n' + card + s[target.end():]

    # 5. entradas de audioMap (logo apos a abertura do objeto)
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + s[am.end():]

    # 6. totalLessons -> 20
    s = re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons=20', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'eduardo-chiba.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'eduardo-chiba.html'), False)
print('OK')
