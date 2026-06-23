#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula N no hub existente (prof + aluno), de forma ADITIVA.
Stamp já existe (stamps 1-5 presentes desde o onboarding) — não re-inserir."""
import os, re

ROOT = '/home/dan/dev/work/better/wt-marcos-a4'
N = 7
SNIP = os.path.join(ROOT, f'_build/marcos-mansour-aula{N}/hub_snippets.html')

snip = open(SNIP, encoding='utf-8').read()

def section(start_marker, end_marker):
    i = snip.index(start_marker) + len(start_marker)
    j = snip.index(end_marker)
    return snip[i:j].strip()

card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP') if '<!-- 2. STAMP' in snip else section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 3. ACCORDION')
accordion = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
comp = section(f'COMPLEMENTARES da aula {N} (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip()

def process(path, href_prefix):
    s = open(path, encoding='utf-8').read()
    orig = s
    this_card = card.replace('/professor/marcos-mansour-aula', f'{href_prefix}/marcos-mansour-aula')

    # 1. IN CLASS card: only the professor hub has a tab-inclass with aula cards.
    prev = N - 1
    anchor_prev = f'<a href="{href_prefix}/marcos-mansour-aula{prev}.html?autostart=1"'
    if anchor_prev in s:
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

    # 5. totalLessons prev -> N
    s = s.replace(f'var totalLessons={prev};', f'var totalLessons={N};', 1)

    # 6. stamp{N} no passaporte (REGRA 29): inserir logo após o último stamp existente.
    #    O config do aluno só declarou 5 stamps; a partir da aula 6 cada aula nova
    #    ganha o seu próprio stamp (convenção 1 stamp/aula dos demais alunos).
    stamp_html = (f'\n<div class="stamp" id="stamp{N}" data-label="Calm Answers" '
                  f"style=\"background-image:url('https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=200&q=80')\"></div>")
    last_stamp_anchor = f'id="stamp{prev}"'
    if last_stamp_anchor in s and f'id="stamp{N}"' not in s:
        ils = s.index(last_stamp_anchor)
        close_div = s.index('</div>', ils) + len('</div>')
        s = s[:close_div] + stamp_html + s[close_div:]

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')

process(os.path.join(ROOT, 'public/professor/marcos-mansour.html'), '/professor')
process(os.path.join(ROOT, 'public/aluno/marcos-mansour.html'), '/aluno')
print('done')
