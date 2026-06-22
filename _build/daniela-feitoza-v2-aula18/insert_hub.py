#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere ADITIVAMENTE os snippets da aula 18 (gerados pelo
build_from_model.py) nos hubs da Daniela Feitoza V2 (prof + aluno).

NAO toca aulas 1-17. So adiciona: stamp18, card do menu IN CLASS (aula 18),
accordion ex-lesson-18 (Pre-class), bloco de Complementares l18, entradas de
audioMap; ajusta o placeholder "Aulas 18-43" -> "Aulas 19-43" e
var totalLessons=17 -> 18. TOTAL_AULAS fica 43.

O hub V2 TEM cards de menu IN CLASS (enterSlideMode/href autostart) -> a seccao 1
(CARD) E inserida, com /professor/ no hub prof e /aluno/ no hub aluno.
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


CARD = section('<!-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->',
               '<!-- 2. STAMP')
STAMP = section('<!-- 2. STAMP (inserir na stamps-row do header) -->',
                '<!-- 3. ACCORDION')
ACCORDION = section('<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->',
                    '<!-- 3b. COMPLEMENTARES')
COMP = section('<!-- 3b. COMPLEMENTARES da aula 18 (inserir na tab-complementary, prof E aluno) -->',
               '<!-- 4. ENTRADAS')
# audioMap: conteudo entre <script> e </script> da seccao 4
m = re.search(r'<!-- 4\. ENTRADAS.*?-->\s*<script>(.*?)</script>', snip, re.S)
AUDIOMAP = m.group(1).strip('\n')

# --- anchors (verificados unicos no hub V2 atual, base origin/main com 17 aulas) ---
STAMP17 = ("<div class=\"stamp\" id=\"stamp17\" data-label=\"How Long\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1501139083538-0139583c060f?w=200&q=80')\"></div>")
# Pre-class: a accordion entra ANTES do placeholder "Lessons 8-43" (vem logo apos o
# ex-lesson-17). O placeholder e unico no hub aluno; no hub prof ha outros, por isso
# ancoramos no fechamento + placeholder juntos (sequencia unica).
PRECLASS_ANCHOR = '</div>\n</div>\n\n        <!-- Lessons 8-43 Placeholder -->'
PLACEHOLDER_TXT = 'Aulas 18&ndash;43'
INCLASS_ANCHOR = '</div><!-- /tab-inclass -->'
# complementares: inserimos o bloco l18 logo apos o fechamento do bloco l17-youtube,
# ancorando na media-tip unica da aula 17 + fechamentos.
COMP_ANCHOR = ('Dica: depois do v&iacute;deo, d&ecirc; um update de um projeto seu em 4 frases, '
               'usando for e since.</p>\n    </div>\n  </div>\n</div>')
AUDIOMAP_ANCHOR = 'var audioMap = {'
TOTAL_ANCHOR = 'var totalLessons=17;'


def patch(path, is_aluno):
    s = open(path, encoding='utf-8').read()
    orig = s
    n = 0

    # 0. card do menu IN CLASS (so o hub PROF tem tab-inclass; o hub ALUNO nao tem)
    if not is_aluno:
        assert s.count(INCLASS_ANCHOR) == 1, f'{path}: /tab-inclass anchor nao unico'
        s = s.replace(INCLASS_ANCHOR, CARD + '\n  ' + INCLASS_ANCHOR, 1); n += 1

    # 1. stamp18 (apos stamp17)
    assert s.count(STAMP17) == 1, f'{path}: stamp17 anchor nao unico'
    s = s.replace(STAMP17, STAMP17 + '\n            ' + STAMP, 1); n += 1

    # 2. accordion ex-lesson-18 (antes do placeholder Pre-class, apos ex-lesson-17)
    assert s.count(PRECLASS_ANCHOR) == 1, f'{path}: preclass accordion anchor nao unico ({s.count(PRECLASS_ANCHOR)})'
    s = s.replace(PRECLASS_ANCHOR,
                  '</div>\n</div>\n\n        ' + ACCORDION + '\n\n        <!-- Lessons 8-43 Placeholder -->', 1); n += 1

    # 3. placeholder texto 18->19
    assert s.count(PLACEHOLDER_TXT) == 1, f'{path}: placeholder txt nao unico'
    s = s.replace(PLACEHOLDER_TXT, 'Aulas 19&ndash;43', 1); n += 1

    # 4. complementares l18 (apos o bloco l17-youtube, dentro da media-grid)
    assert s.count(COMP_ANCHOR) == 1, f'{path}: comp anchor nao unico'
    s = s.replace(COMP_ANCHOR, COMP_ANCHOR + '\n\n' + COMP, 1); n += 1

    # 5. audioMap (apos abertura)
    assert s.count(AUDIOMAP_ANCHOR) == 1, f'{path}: audioMap anchor nao unico'
    s = s.replace(AUDIOMAP_ANCHOR,
                  AUDIOMAP_ANCHOR + '\n    // ===== Aula 18 (pc18_ Pre-class + a18_ slides) =====\n' + AUDIOMAP, 1); n += 1

    # 6. totalLessons 17->18
    assert s.count(TOTAL_ANCHOR) == 1, f'{path}: totalLessons=17 nao unico'
    s = s.replace(TOTAL_ANCHOR, 'var totalLessons=18;', 1); n += 1

    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({n} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza-v2.html'), is_aluno=False)
patch(os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza-v2.html'), is_aluno=True)
print('hubs V2 atualizados (aditivo, aula 18).')
