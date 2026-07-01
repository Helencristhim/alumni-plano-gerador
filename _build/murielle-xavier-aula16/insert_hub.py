#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula N no hub existente da Murielle (prof + aluno), aditivo.
O card da aula N entra logo apos o card da aula N-1 (ordem correta no menu)."""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
N = 16
PREV = N - 1
SNIP = os.path.join(ROOT, f'_build/murielle-xavier-aula{N}/hub_snippets.html')

snip = open(SNIP, encoding='utf-8').read()


def section(start_marker, end_marker):
    i = snip.index(start_marker) + len(start_marker)
    j = snip.index(end_marker)
    return snip[i:j].strip()


_card_end = '<!-- 2. STAMP' if '<!-- 2. STAMP' in snip else '<!-- 3. ACCORDION'
card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', _card_end)
stamp = section('inserir na stamps-row do header) -->', '<!-- 3. ACCORDION') if '<!-- 2. STAMP' in snip else ''
accordion = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
comp = section(f'COMPLEMENTARES da aula {N} (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>') + len('<script>'):am_block.index('</script>')].strip()


def process(path, href_prefix):
    s = open(path, encoding='utf-8').read()
    orig = s
    this_card = card.replace(f'/professor/murielle-xavier-aula{N}.html', f'{href_prefix}/murielle-xavier-aula{N}.html')

    anchor_prev = f'<a href="{href_prefix}/murielle-xavier-aula{PREV}.html?autostart=1"'
    if anchor_prev in s:
        ia = s.index(anchor_prev)
        close_a = s.index('</a>', ia) + len('</a>')
        s = s[:close_a] + '\n' + this_card + s[close_a:]

    marker = '</div><!-- /tab-exercises -->'
    im = s.index(marker)
    s = s[:im] + accordion + '\n\n' + s[im:]

    cmarker = '</div><!-- /tab-complementary -->'
    ic = s.index(cmarker)
    s = s[:ic] + comp + '\n\n' + s[ic:]

    am_anchor = 'var audioMap = {'
    iam = s.index(am_anchor) + len(am_anchor)
    s = s[:iam] + '\n' + am_inner + s[iam:]

    s = s.replace(f'var totalLessons={PREV};', f'var totalLessons={N};', 1)

    if stamp and f'id="stamp{N}"' not in s:
        anchor = f'id="stamp{PREV}"'
        ip = s.index(anchor)
        close = s.index('</div>', ip) + len('</div>')
        s = s[:close] + '\n        ' + stamp + s[close:]

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')


process(os.path.join(ROOT, 'public/professor/murielle-xavier.html'), '/professor')
process(os.path.join(ROOT, 'public/aluno/murielle-xavier.html'), '/aluno')
print('done')
