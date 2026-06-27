#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets de UMA aula do Danilo no hub existente (prof + aluno), ADITIVO.
Uso: python3 _build/danilo-febba-insert_hub.py N
- Card IN CLASS -> apenas hub PROF (aluno nao tem tab-inclass).
- Accordion Pre-class -> prof E aluno (antes de </div><!-- /tab-exercises -->).
- Complementares da aula -> prof E aluno (antes de </div><!-- /tab-complementary -->).
- audioMap -> prof E aluno (logo apos 'var audioMap = {').
- totalLessons -> N (ambos).
- STAMP: NAO inserir (stamps 1-5 ja existem desde o hub 'new' da aula 1).
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
N = int(sys.argv[1])
SNIP = os.path.join(ROOT, f'_build/danilo-febba-aula{N}/hub_snippets.html')
snip = open(SNIP, encoding='utf-8').read()

def section(start_marker, end_marker):
    i = snip.index(start_marker) + len(start_marker)
    j = snip.index(end_marker, i)
    return snip[i:j].strip()

card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- ')
accordion = section('ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b.')
comp = section(f'COMPLEMENTARES da aula {N} (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>') + len('<script>'):am_block.index('</script>')].strip()

def process(path, href_prefix, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s

    # 1. IN CLASS card: only the professor hub has a tab-inclass with aula cards.
    if is_prof:
        this_card = card.replace('/professor/danilo-febba-aula', f'{href_prefix}/danilo-febba-aula')
        anchor_prev = f'<a href="{href_prefix}/danilo-febba-aula{N-1}.html?autostart=1"'
        ia = s.index(anchor_prev)
        close_a = s.index('</a>', ia) + len('</a>')
        s = s[:close_a] + '\n' + this_card + s[close_a:]

    # 2. Pre-class accordion: insert right before </div><!-- /tab-exercises -->
    marker = '</div><!-- /tab-exercises -->'
    im = s.index(marker)
    s = s[:im] + accordion + '\n\n' + s[im:]

    # 3. Complementary block: insert right before </div><!-- /tab-complementary -->
    cmarker = '</div><!-- /tab-complementary -->'
    ic = s.index(cmarker)
    s = s[:ic] + comp + '\n\n' + s[ic:]

    # 4. audioMap entries: insert right after 'var audioMap = {'
    am_anchor = 'var audioMap = {'
    iam = s.index(am_anchor) + len(am_anchor)
    s = s[:iam] + '\n' + am_inner + s[iam:]

    # 5. totalLessons N-1 -> N
    s = s.replace(f'var totalLessons={N-1};', f'var totalLessons={N};', 1)

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')

process(os.path.join(ROOT, 'public/professor/danilo-febba.html'), '/professor', True)
process(os.path.join(ROOT, 'public/aluno/danilo-febba.html'), '/aluno', False)
print('done')
