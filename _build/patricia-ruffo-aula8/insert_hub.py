#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA e IDEMPOTENTE dos snippets da aula 8 no hub existente
(prof + aluno). Aulas anteriores intactas. Re-rodavel apos rebase do hub.

Insere, se ainda nao existirem:
  - card IN CLASS (so prof) apos o card da aula 6
  - stamp8 apos stamp6 na stamps-row
  - accordion ex-lesson-8 apos ex-lesson-6 (prof e aluno)
  - bloco complementares l8 antes do </div><!-- /tab-complementary -->
  - entradas de audioMap (mescla no bloco var audioMap = {...})
  - totalLessons -> 8 ; window.TOTAL_AULAS mantido em 40
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def section(start_marker, end_marker=None):
    i = SNIP.index(start_marker)
    j = SNIP.index('\n', i) + 1
    if end_marker:
        k = SNIP.index(end_marker)
    else:
        k = len(SNIP)
    return SNIP[j:k].strip('\n')


CARD = section('<!-- 1. CARD', '<!-- 2. STAMP')
STAMP = section('<!-- 2. STAMP', '<!-- 3. ACCORDION')
ACCORDION = section('<!-- 3. ACCORDION', '<!-- 3b. COMPLEMENTARES')
COMP = section('<!-- 3b. COMPLEMENTARES', '<!-- 4. ENTRADAS')
# audioMap entries (between <script> and </script> in section 4)
amap_block = SNIP[SNIP.index('<!-- 4. ENTRADAS'):]
AMAP = amap_block[amap_block.index('<script>') + len('<script>'):amap_block.index('</script>')].strip('\n')


def insert_after_block(html, anchor_id, new_block, present_token):
    """Insere new_block depois do bloco <div ...id="anchor_id">...</div> (balanceado)."""
    if present_token in html:
        return html  # ja inserido
    start = html.index(f'id="{anchor_id}"')
    # recua ate o <div de abertura
    div_start = html.rindex('<div', 0, start)
    # acha o </div> que fecha esse div (contagem balanceada)
    depth = 0
    i = div_start
    while i < len(html):
        m = re.compile(r'<div\b|</div>').search(html, i)
        if not m:
            break
        if m.group() == '</div>':
            depth -= 1
            if depth == 0:
                end = m.end()
                break
        else:
            depth += 1
        i = m.end()
    return html[:end] + '\n' + new_block + '\n' + html[end:]


def patch(path, is_prof):
    html = open(path, encoding='utf-8').read()
    orig = html

    # ancora = a aula anterior MAIS RECENTE presente no hub (7 se ja existir, senao 6)
    prev = 7 if 'id="stamp7"' in html else 6

    # 1. stamp8 apos o stamp da aula anterior
    if 'id="stamp8"' not in html:
        anchor = f'<div class="stamp" id="stamp{prev}"'
        i = html.index(anchor)
        end = html.index('</div>', i) + len('</div>')
        html = html[:end] + '\n' + STAMP + html[end:]

    # 2. accordion ex-lesson-8 apos o ex-lesson anterior (balanceado)
    html = insert_after_block(html, f'ex-lesson-{prev}', ACCORDION, 'id="ex-lesson-8"')

    # 3. card IN CLASS so no prof, apos o card da aula anterior
    if is_prof and 'patricia-ruffo-aula8.html?autostart=1' not in html:
        anchor = f'<a href="/professor/patricia-ruffo-aula{prev}.html?autostart=1"'
        i = html.index(anchor)
        end = html.index('</a>', i) + len('</a>')
        html = html[:end] + '\n' + CARD + html[end:]

    # 4. complementares l8 antes do fim da tab-complementary
    if 'data-media="l8-' not in html:
        marker = '</div><!-- /tab-complementary -->'
        i = html.index(marker)
        html = html[:i] + COMP + '\n' + html[i:]

    # 5. audioMap entries (mescla logo apos 'var audioMap = {')
    if '/audio/patricia-ruffo/a8_' not in html and '/audio/patricia-ruffo/pc8_' not in html:
        marker = 'var audioMap = {'
        i = html.index(marker) + len(marker)
        html = html[:i] + '\n' + AMAP + html[i:]

    # 6. totalLessons = maior numero de aula presente (nunca rebaixa; outras aulas
    #    podem ja ter mergeado um numero mais alto, ex. aula 12)
    nums = [int(n) for n in re.findall(r'id="ex-lesson-(\d+)"', html)]
    hi = max(nums) if nums else 8
    html = re.sub(r'totalLessons\s*=\s*\d+', f'totalLessons={hi}', html)

    if html != orig:
        open(path, 'w', encoding='utf-8').write(html)
        print(f'  patched {os.path.relpath(path, ROOT)}')
    else:
        print(f'  no change {os.path.relpath(path, ROOT)} (ja tinha aula 8?)')


patch(os.path.join(ROOT, 'public', 'professor', 'patricia-ruffo.html'), is_prof=True)
patch(os.path.join(ROOT, 'public', 'aluno', 'patricia-ruffo.html'), is_prof=False)
print('done')
