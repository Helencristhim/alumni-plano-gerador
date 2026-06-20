#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 20 nos hubs da
Daniela Feitoza (prof + aluno). Replica a aula 19. NAO toca aulas 1-19.
stamp20, ex-lesson-20, complementares l20, audioMap; "Aulas 20-43" ->
"Aulas 21-43" e var totalLessons=19 -> 20.
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
COMP = section('<!-- 3b. COMPLEMENTARES da aula 20 (inserir na tab-complementary, prof E aluno) -->',
               '<!-- 4. ENTRADAS')
m = re.search(r'<!-- 4\. ENTRADAS.*?-->\s*<script>(.*?)</script>', snip, re.S)
AUDIOMAP = m.group(1).strip('\n')

STAMP19 = ("<div class=\"stamp\" id=\"stamp19\" data-label=\"Diplomacy\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1521791136064-7986c2920216?w=200&q=80')\"></div>")
PLACEHOLDER_ANCHOR = '<!-- Lessons 8-43 Placeholder -->'
PLACEHOLDER_TXT = 'Aulas 20&ndash;43'
RESET_ANCHOR = '\n\n        <button class="reset-btn" onclick="resetProgress()">Resetar todo o progresso</button>'
AUDIOMAP_ANCHOR = 'const audioMap = {'
TOTAL_ANCHOR = 'var totalLessons=19;'


def patch(path):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0
    assert s.count(STAMP19) == 1, f'{path}: stamp19 anchor nao unico'
    s = s.replace(STAMP19, STAMP19 + '\n            ' + STAMP, 1); n += 1
    assert s.count(PLACEHOLDER_ANCHOR) == 1, f'{path}: placeholder comment nao unico'
    s = s.replace(PLACEHOLDER_ANCHOR, ACCORDION + '\n\n        ' + PLACEHOLDER_ANCHOR, 1); n += 1
    assert s.count(PLACEHOLDER_TXT) == 1, f'{path}: placeholder txt nao unico'
    s = s.replace(PLACEHOLDER_TXT, 'Aulas 21&ndash;43', 1); n += 1
    assert s.count(RESET_ANCHOR) == 1, f'{path}: reset anchor nao unico'
    s = s.replace(RESET_ANCHOR, '\n\n' + COMP + RESET_ANCHOR, 1); n += 1
    assert s.count(AUDIOMAP_ANCHOR) == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace(AUDIOMAP_ANCHOR,
                  AUDIOMAP_ANCHOR + '\n    // ===== Aula 20 (pc20_ Pre-class + a20_ slides) =====\n' + AUDIOMAP, 1); n += 1
    assert s.count(TOTAL_ANCHOR) == 1, f'{path}: totalLessons=19 nao unico'
    s = s.replace(TOTAL_ANCHOR, 'var totalLessons=20;', 1); n += 1
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza.html'))
patch(os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza.html'))
print('hubs atualizados (aditivo, aula 20).')
