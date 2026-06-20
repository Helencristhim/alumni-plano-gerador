#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 17 nos hubs da
Daniela Feitoza (prof + aluno). Replica a aula 16. NAO toca aulas 1-16.
stamp17, ex-lesson-17, complementares l17, audioMap; "Aulas 17-43" ->
"Aulas 18-43" e var totalLessons=16 -> 17.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def section(start_marker, end_marker):
    s = snip.index(start_marker)
    e = snip.index(end_marker)
    return snip[s + len(start_marker):e].strip('\n')


STAMP = section('<!-- 2. STAMP (inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACCORDION = section('<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->',
                    '<!-- 3b. COMPLEMENTARES')
COMP = section('<!-- 3b. COMPLEMENTARES da aula 17 (inserir na tab-complementary, prof E aluno) -->',
               '<!-- 4. ENTRADAS')
m = re.search(r'<!-- 4\. ENTRADAS.*?-->\s*<script>(.*?)</script>', snip, re.S)
AUDIOMAP = m.group(1).strip('\n')

STAMP16 = ("<div class=\"stamp\" id=\"stamp16\" data-label=\"The Timeline\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=200&q=80')\"></div>")
PLACEHOLDER_ANCHOR = '<!-- Lessons 8-43 Placeholder -->'
PLACEHOLDER_TXT = 'Aulas 17&ndash;43'
RESET_ANCHOR = '\n\n        <button class="reset-btn" onclick="resetProgress()">Resetar todo o progresso</button>'
AUDIOMAP_ANCHOR = 'const audioMap = {'
TOTAL_ANCHOR = 'var totalLessons=16;'


def patch(path):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0
    assert s.count(STAMP16) == 1, f'{path}: stamp16 anchor nao unico'
    s = s.replace(STAMP16, STAMP16 + '\n            ' + STAMP, 1); n += 1
    assert s.count(PLACEHOLDER_ANCHOR) == 1, f'{path}: placeholder comment nao unico'
    s = s.replace(PLACEHOLDER_ANCHOR, ACCORDION + '\n\n        ' + PLACEHOLDER_ANCHOR, 1); n += 1
    assert s.count(PLACEHOLDER_TXT) == 1, f'{path}: placeholder txt nao unico'
    s = s.replace(PLACEHOLDER_TXT, 'Aulas 18&ndash;43', 1); n += 1
    assert s.count(RESET_ANCHOR) == 1, f'{path}: reset anchor nao unico'
    s = s.replace(RESET_ANCHOR, '\n\n' + COMP + RESET_ANCHOR, 1); n += 1
    assert s.count(AUDIOMAP_ANCHOR) == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace(AUDIOMAP_ANCHOR,
                  AUDIOMAP_ANCHOR + '\n    // ===== Aula 17 (pc17_ Pre-class + a17_ slides) =====\n' + AUDIOMAP, 1); n += 1
    assert s.count(TOTAL_ANCHOR) == 1, f'{path}: totalLessons=16 nao unico'
    s = s.replace(TOTAL_ANCHOR, 'var totalLessons=17;', 1); n += 1
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza.html'))
patch(os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza.html'))
print('hubs atualizados (aditivo, aula 17).')
