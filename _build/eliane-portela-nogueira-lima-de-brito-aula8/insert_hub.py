#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 8 (review/checkpoint) no hub existente da Eliane
(prof + aluno), aditivo. Aula de revis&atilde;o reusa vocabul&aacute;rio de propósito, ent&atilde;o
o audioMap dedup (fix #1183) compara SÓ contra as chaves j&aacute; presentes no bloco
audioMap do hub: frases repetidas de aulas anteriores mant&ecirc;m o &aacute;udio antigo,
apenas as frases NOVAS da aula 8 s&atilde;o inseridas.
Stamps 1-5 j&aacute; existem no hub desde o 'new' da aula 1 — NAO re-inserir esses."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SLUG = 'eliane-portela-nogueira-lima-de-brito'
N = 8
PREV = N - 1
SNIP = os.path.join(ROOT, f'_build/{SLUG}-aula{N}/hub_snippets.html')

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


def audiomap_keys(hub_html):
    """Chaves ja existentes SÓ dentro do bloco `var audioMap = { ... };` (fix #1183)."""
    m = re.search(r'var audioMap\s*=\s*\{', hub_html)
    start = m.end()
    depth = 1
    i = start
    while i < len(hub_html) and depth > 0:
        if hub_html[i] == '{':
            depth += 1
        elif hub_html[i] == '}':
            depth -= 1
        i += 1
    block = hub_html[start:i]
    return set(re.findall(r'"((?:[^"\\]|\\.)*)"\s*:', block))


def process(path, href_prefix):
    s = open(path, encoding='utf-8').read()
    orig = s
    this_card = card.replace(f'/professor/{SLUG}-aula{N}.html', f'{href_prefix}/{SLUG}-aula{N}.html')

    # 1. IN CLASS card: only professor hub has the tab-inclass aula cards.
    anchor_prev = f'<a href="{href_prefix}/{SLUG}-aula{PREV}.html?autostart=1"'
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

    # 4. audioMap entries: dedup por CHAVE contra o bloco audioMap existente (fix #1183).
    existing = audiomap_keys(s)
    kept = []
    for line in am_inner.splitlines():
        km = re.match(r'\s*"((?:[^"\\]|\\.)*)"\s*:', line)
        if km and km.group(1) in existing:
            continue  # frase ja tem audio no hub (aula anterior) — nao duplicar chave
        kept.append(line)
    if kept:
        am_anchor = 'var audioMap = {'
        iam = s.index(am_anchor) + len(am_anchor)
        s = s[:iam] + '\n' + '\n'.join(kept) + s[iam:]

    # 5. totalLessons PREV -> N
    s = s.replace(f'var totalLessons={PREV};', f'var totalLessons={N};', 1)

    # 6. STAMP: insert stampN right after the stamp{PREV} div in the stamps-row
    if stamp and f'id="stamp{N}"' not in s:
        anchor = f'id="stamp{PREV}"'
        ip = s.index(anchor)
        close = s.index('</div>', ip) + len('</div>')
        s = s[:close] + '\n        ' + stamp + s[close:]

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')


process(os.path.join(ROOT, f'public/professor/{SLUG}.html'), '/professor')
process(os.path.join(ROOT, f'public/aluno/{SLUG}.html'), '/aluno')
print('done')
