#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 13 (gerados pelo
build_from_model.py) nos hubs da Daniela Feitoza (prof + aluno).

Replica EXATAMENTE o que a aula 12 fez. NAO toca aulas 1-12.
So adiciona: stamp13, accordion ex-lesson-13 (Pre-class), bloco de
Complementares l13, entradas de audioMap; ajusta o placeholder
"Aulas 13-43" -> "Aulas 14-43" e var totalLessons=12 -> 13.

Este hub NAO tem cards de menu IN CLASS (autostart) — igual aula 12,
a seccao 1 do snippet NAO e inserida.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def section(start_marker, end_marker):
    s = snip.index(start_marker)
    e = snip.index(end_marker)
    body = snip[s + len(start_marker):e]
    return body.strip('\n')


STAMP = section('<!-- 2. STAMP (inserir na stamps-row do header) -->',
                '<!-- 3. ACCORDION')
ACCORDION = section('<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->',
                    '<!-- 3b. COMPLEMENTARES')
COMP = section('<!-- 3b. COMPLEMENTARES da aula 13 (inserir na tab-complementary, prof E aluno) -->',
               '<!-- 4. ENTRADAS')
# audioMap: conteudo entre <script> e </script> da seccao 4
m = re.search(r'<!-- 4\. ENTRADAS.*?-->\s*<script>(.*?)</script>', snip, re.S)
AUDIOMAP = m.group(1).strip('\n')

# --- anchors (verificados unicos no hub) ---
STAMP12 = ("<div class=\"stamp\" id=\"stamp12\" data-label=\"Retail Tech\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80')\"></div>")
PLACEHOLDER_ANCHOR = '<!-- Lessons 8-43 Placeholder -->'
PLACEHOLDER_TXT = 'Aulas 13&ndash;43'
RESET_ANCHOR = '\n\n        <button class="reset-btn" onclick="resetProgress()">Resetar todo o progresso</button>'
AUDIOMAP_ANCHOR = 'const audioMap = {'
TOTAL_ANCHOR = 'var totalLessons=12;'


def patch(path):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. stamp13 (apos stamp12)
    assert s.count(STAMP12) == 1, f'{path}: stamp12 anchor nao unico'
    s = s.replace(STAMP12, STAMP12 + '\n            ' + STAMP, 1); n += 1

    # 2. accordion ex-lesson-13 (antes do placeholder Pre-class)
    assert s.count(PLACEHOLDER_ANCHOR) == 1, f'{path}: placeholder comment nao unico'
    s = s.replace(PLACEHOLDER_ANCHOR, ACCORDION + '\n\n        ' + PLACEHOLDER_ANCHOR, 1); n += 1

    # 3. placeholder texto 13->14
    assert s.count(PLACEHOLDER_TXT) == 1, f'{path}: placeholder txt nao unico'
    s = s.replace(PLACEHOLDER_TXT, 'Aulas 14&ndash;43', 1); n += 1

    # 4. complementares l13 (apos l12, antes do reset-btn)
    assert s.count(RESET_ANCHOR) == 1, f'{path}: reset anchor nao unico'
    s = s.replace(RESET_ANCHOR, '\n\n' + COMP + RESET_ANCHOR, 1); n += 1

    # 5. audioMap (apos abertura)
    assert s.count(AUDIOMAP_ANCHOR) == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace(AUDIOMAP_ANCHOR,
                  AUDIOMAP_ANCHOR + '\n    // ===== Aula 13 (pc13_ Pre-class + a13_ slides) =====\n' + AUDIOMAP, 1); n += 1

    # 6. totalLessons 12->13
    assert s.count(TOTAL_ANCHOR) == 1, f'{path}: totalLessons=12 nao unico'
    s = s.replace(TOTAL_ANCHOR, 'var totalLessons=13;', 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza.html'))
patch(os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza.html'))
print('hubs atualizados (aditivo, aula 13).')
