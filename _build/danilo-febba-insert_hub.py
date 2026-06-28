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
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
N = int(sys.argv[1])
SNIP = os.path.join(ROOT, f'_build/danilo-febba-aula{N}/hub_snippets.html')
snip = open(SNIP, encoding='utf-8').read()

# Stamps 1-5 nasceram com o hub "new" da aula 1. Para N>=6 o stamp do milestone
# nao existe e o validador (REGRA 29) cobra stamp{N} no hub prof. Inserimos aqui,
# de forma idempotente, no fim da stamps-row (prof E aluno). Label = menu_title da
# aula; imagens decorativas (rotativas, known-good unsplash).
_cfg = json.load(open(os.path.join(ROOT, f'_build/danilo-febba-aula{N}/config.json'), encoding='utf-8'))
STAMP_IMGS = [
    'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=200&q=80',
    'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80',
    'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=200&q=80',
    'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=200&q=80',
    'https://images.unsplash.com/photo-1552664730-d307ca884978?w=200&q=80',
]
STAMP_LABEL = _cfg['lesson']['menu_title'][:18]
STAMP_IMG = STAMP_IMGS[(N - 6) % len(STAMP_IMGS)]
STAMP_DIV = (f'<div class="stamp" id="stamp{N}" data-label="{STAMP_LABEL}" '
             f"style=\"background-image:url('{STAMP_IMG}')\"></div>")

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

    # 6. STAMP do milestone (idempotente): se stamp{N} ainda nao existe, inserir no
    #    fim da stamps-row (apos o ultimo stamp). Prof E aluno.
    if f'id="stamp{N}"' not in s:
        last_stamp = list(re.finditer(r'<div class="stamp" id="stamp\d+"[^>]*></div>', s))
        if last_stamp:
            pos = last_stamp[-1].end()
            s = s[:pos] + STAMP_DIV + s[pos:]

    assert s != orig, f'no change in {path}'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'updated {os.path.relpath(path, ROOT)}')

process(os.path.join(ROOT, 'public/professor/danilo-febba.html'), '/professor', True)
process(os.path.join(ROOT, 'public/aluno/danilo-febba.html'), '/aluno', False)
print('done')
