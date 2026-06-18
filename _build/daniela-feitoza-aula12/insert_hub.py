#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 12 (gerados pelo
build_from_model.py) nos hubs da Daniela Feitoza (prof + aluno).

Replica EXATAMENTE o que a aula 11 fez. NAO toca aulas 1-11.
So adiciona: stamp12, accordion ex-lesson-12 (Pre-class), bloco de
Complementares l12, entradas de audioMap; ajusta o placeholder
"Aulas 12-43" -> "Aulas 13-43" e var totalLessons=11 -> 12.

Este hub NAO tem cards de menu IN CLASS (autostart) — igual aula 11,
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
COMP = section('<!-- 3b. COMPLEMENTARES da aula 12 (inserir na tab-complementary, prof E aluno) -->',
               '<!-- 4. ENTRADAS')
# audioMap: conteudo entre <script> e </script> da seccao 4
m = re.search(r'<!-- 4\. ENTRADAS.*?-->\s*<script>(.*?)</script>', snip, re.S)
AUDIOMAP = m.group(1).strip('\n')

# --- anchors (verificados unicos no hub) ---
STAMP11 = ("<div class=\"stamp\" id=\"stamp11\" data-label=\"Experience\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=200&q=80')\"></div>")
PLACEHOLDER_ANCHOR = '<!-- Lessons 8-43 Placeholder -->'
PLACEHOLDER_TXT = 'Aulas 12&ndash;43'
RESET_ANCHOR = '\n\n        <button class="reset-btn" onclick="resetProgress()">Resetar todo o progresso</button>'
AUDIOMAP_ANCHOR = 'const audioMap = {'
TOTAL_ANCHOR = 'var totalLessons=11;'


def patch(path):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 1. stamp12 (apos stamp11)
    assert s.count(STAMP11) == 1, f'{path}: stamp11 anchor nao unico'
    s = s.replace(STAMP11, STAMP11 + '\n            ' + STAMP, 1); n += 1

    # 2. accordion ex-lesson-12 (antes do placeholder Pre-class)
    assert s.count(PLACEHOLDER_ANCHOR) == 1, f'{path}: placeholder comment nao unico'
    s = s.replace(PLACEHOLDER_ANCHOR, ACCORDION + '\n\n        ' + PLACEHOLDER_ANCHOR, 1); n += 1

    # 3. placeholder texto 12->13
    assert s.count(PLACEHOLDER_TXT) == 1, f'{path}: placeholder txt nao unico'
    s = s.replace(PLACEHOLDER_TXT, 'Aulas 13&ndash;43', 1); n += 1

    # 4. complementares l12 (apos l11, antes do reset-btn)
    assert s.count(RESET_ANCHOR) == 1, f'{path}: reset anchor nao unico'
    s = s.replace(RESET_ANCHOR, '\n\n' + COMP + RESET_ANCHOR, 1); n += 1

    # 5. audioMap (apos abertura)
    assert s.count(AUDIOMAP_ANCHOR) == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace(AUDIOMAP_ANCHOR,
                  AUDIOMAP_ANCHOR + '\n    // ===== Aula 12 (pc12_ Pre-class + a12_ slides) =====\n' + AUDIOMAP, 1); n += 1

    # 6. totalLessons 11->12
    assert s.count(TOTAL_ANCHOR) == 1, f'{path}: totalLessons=11 nao unico'
    s = s.replace(TOTAL_ANCHOR, 'var totalLessons=12;', 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza.html'))
patch(os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza.html'))
print('hubs atualizados (aditivo, aula 12).')
