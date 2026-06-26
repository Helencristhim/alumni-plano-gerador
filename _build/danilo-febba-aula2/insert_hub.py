#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 2 no hub existente do Danilo (prof + aluno), de forma ADITIVA.
Stamp ja existe (stamp2 presente desde o hub 'new' da aula 1) — nao re-inserir."""
import os, re

ROOT = '/Users/helenmendes/alumni-plano-gerador'
SNIP = os.path.join(ROOT, '_build/danilo-febba-aula2/hub_snippets.html')
N = 2

snip = open(SNIP, encoding='utf-8').read()

def section(start_marker, end_marker):
    i = snip.index(start_marker) + len(start_marker)
    j = snip.index(end_marker)
    return snip[i:j].strip()

card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
accordion = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
comp = section(f'COMPLEMENTARES da aula {N} (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip()

def process(path, href_prefix):
    s = open(path, encoding='utf-8').read()
    orig = s
    this_card = card.replace('/professor/danilo-febba-aula2.html', f'{href_prefix}/danilo-febba-aula2.html')

    # 1. IN CLASS card: only the professor hub has a tab-inclass with aula cards.
    #    Aluno hub has no IN CLASS tab (REGRA: aluno sem tab-inclass).
    anchor_a1 = f'<a href="{href_prefix}/danilo-febba-aula1.html?autostart=1"'
    if anchor_a1 in s:
        ia = s.index(anchor_a1)
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

    # 5. totalLessons 1 -> 2
    s = s.replace('var totalLessons=1;', f'var totalLessons={N};', 1)

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')

process(os.path.join(ROOT, 'public/professor/danilo-febba.html'), '/professor')
process(os.path.join(ROOT, 'public/aluno/danilo-febba.html'), '/aluno')
print('done')
