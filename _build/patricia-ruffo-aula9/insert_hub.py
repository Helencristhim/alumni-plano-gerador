#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inserção ADITIVA da aula 9 nos hubs prof+aluno da Patricia Ruffo.

Idempotente: se a aula 9 já está inserida, não duplica. Suporta o passo de
contenção de merge (rodar de novo após re-checkout do hub do origin/main).

Insere 4 peças extraídas de hub_snippets.html:
  1. CARD IN CLASS  -> só no hub PROFESSOR, no fim da lista de cards (.../aula6 -> .../aula9)
  2. STAMP9         -> após stamp6 (prof + aluno)
  3. ACCORDION Pre-class (ex-lesson-9) -> após o fim de ex-lesson-6 (prof + aluno)
  3b. COMPLEMENTARES l9 -> no fim da tab-complementary (prof + aluno)
  4. audioMap a9/pc9 -> antes do fechamento do bloco audioMap (prof + aluno)

NÃO mexe em aulas anteriores. NÃO altera totalLessons/TOTAL_AULAS (já = 40).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def section(start_marker, end_marker):
    i = SNIP.index(start_marker) + len(start_marker)
    j = SNIP.index(end_marker, i)
    return SNIP[i:j].strip()


CARD = section('<!-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->',
               '<!-- 2. STAMP')
STAMP = section('<!-- 2. STAMP (inserir na stamps-row do header) -->',
                '<!-- 3. ACCORDION')
ACCORDION = section('<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->',
                    '<!-- 3b. COMPLEMENTARES')
COMPL = section('<!-- 3b. COMPLEMENTARES da aula 9 (inserir na tab-complementary, prof E aluno) -->',
                '<!-- 4. ENTRADAS')
# audioMap entries: linhas dentro do <script> da seção 4
am_block = section('<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->',
                   '<!-- 5.')
AUDIO_LINES = am_block.replace('<script>', '').replace('</script>', '').strip()


def insert_after_block(html, block_start_re, label):
    """Insere ACCORDION após o FIM do lesson-card que começa em block_start_re
    (ex-lesson-6). O lesson-card fecha no </div> que casa a abertura."""
    m = re.search(block_start_re, html)
    if not m:
        raise SystemExit(f'[{label}] âncora não encontrada: {block_start_re}')
    # caminhar pelos <div>/</div> a partir da abertura do lesson-card
    # achar a posição do <div class="lesson-card" que contém o id
    open_pos = html.rfind('<div class="lesson-card"', 0, m.end())
    depth = 0
    i = open_pos
    for tok in re.finditer(r'<div\b|</div>', html[open_pos:]):
        if tok.group() == '</div>':
            depth -= 1
            if depth == 0:
                end = open_pos + tok.end()
                return html[:end] + '\n\n' + ACCORDION + '\n' + html[end:]
        else:
            depth += 1
    raise SystemExit(f'[{label}] não fechou o lesson-card')


def max_n(html, pattern):
    ns = [int(x) for x in re.findall(pattern, html)]
    return max(ns) if ns else None


def insert_after_last_complementary(html, n_last):
    """Insere COMPL após o último media-card-wrapper l{n}-youtube e seu fechamento."""
    m = re.search(rf'<div class="media-card-wrapper" data-media="l{n_last}-youtube">.*?</div>\s*</div>\s*</div>', html, re.S)
    if not m:
        raise SystemExit(f'complementares l{n_last} não encontradas')
    return html[:m.end()] + '\n' + COMPL + html[m.end():]


def process(path, is_prof):
    html = open(path, encoding='utf-8').read()
    orig = html

    # 2. STAMP9 (após o ÚLTIMO stamp existente) — idempotente
    if 'id="stamp9"' not in html:
        n = max_n(html, r'id="stamp(\d+)"')
        anchor = re.search(rf'<div class="stamp" id="stamp{n}"[^>]*></div>', html)
        if not anchor:
            raise SystemExit(f'{path}: stamp{n} não encontrado')
        html = html[:anchor.end()] + '\n' + STAMP + html[anchor.end():]

    # 3. ACCORDION ex-lesson-9 (após o ÚLTIMO accordion existente) — idempotente
    if 'id="ex-lesson-9"' not in html:
        n = max_n(html, r'id="ex-lesson-(\d+)"')
        html = insert_after_block(html, rf'id="ex-lesson-{n}"', 'accordion')

    # 1. CARD IN CLASS — só professor, após o ÚLTIMO card existente
    if is_prof and 'aula9.html?autostart' not in html:
        n = max_n(html, r'patricia-ruffo-aula(\d+)\.html\?autostart')
        m = re.search(rf'<a href="/professor/patricia-ruffo-aula{n}\.html\?autostart=1".*?</a>', html, re.S)
        if not m:
            raise SystemExit(f'{path}: card IN CLASS aula{n} não encontrado')
        html = html[:m.end()] + '\n' + CARD + html[m.end():]

    # 3b. COMPLEMENTARES l9 — após o ÚLTIMO bloco complementar, idempotente
    if 'data-media="l9-series"' not in html:
        n = max_n(html, r'data-media="l(\d+)-youtube"')
        html = insert_after_last_complementary(html, n)

    # 4. audioMap a9/pc9 — após a ÚLTIMA entrada do audioMap (qualquer aula), idempotente
    if '/audio/patricia-ruffo/pc9_clarify.mp3' not in html:
        anchors = list(re.finditer(r'"[^"]*": "/audio/patricia-ruffo/[a-z0-9_]+\.mp3",', html))
        if not anchors:
            raise SystemExit(f'{path}: nenhuma entrada audioMap encontrada')
        end = anchors[-1].end()
        html = html[:end] + '\n' + AUDIO_LINES + html[end:]

    # totalLessons: garantir que cobre a aula 9 (nunca DIMINUIR)
    m = re.search(r'var totalLessons=(\d+);', html)
    if m and int(m.group(1)) < 9:
        html = html.replace(m.group(0), 'var totalLessons=9;')

    if html != orig:
        open(path, 'w', encoding='utf-8').write(html)
        print(f'  updated {os.path.relpath(path, ROOT)}')
    else:
        print(f'  no-op  {os.path.relpath(path, ROOT)} (já inserido)')


process(os.path.join(ROOT, 'public', 'professor', 'patricia-ruffo.html'), True)
process(os.path.join(ROOT, 'public', 'aluno', 'patricia-ruffo.html'), False)
print('OK')
