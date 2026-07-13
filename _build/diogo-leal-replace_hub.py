#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""replace_hub (diogo-leal) — REGERACAO de uma aula que JA existe no hub.

O insert_hub.py e ADITIVO (aula nova depois da ultima). Aqui a aula N ja existe
e esta sendo REESCRITA: o hub tem de trocar a aula N nas 4 abas (REGRA 29), sem
tocar em nenhuma outra aula:

  1. Planejamento  — linha N da tabela curricular
  2. Pre-class     — bloco <div class="lesson-card" id="ex-lesson-N">
  3. IN CLASS      — card do menu (so no hub do professor)
  4. Complementares— <h4>Lesson N ...</h4> + <div class="media-grid"> da aula N
  5. Header        — data-label do stampN
  6. audioMap      — remove as chaves da aula N (a{N}_/pc{N}_) e insere as novas

USO (da raiz do repo):  python3 _build/diogo-leal-replace_hub.py N
Idempotente: rodar de novo com o mesmo build produz o mesmo hub.
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SLUG = 'diogo-leal'

N = int(sys.argv[1])
BUILD = os.path.join(ROOT, '_build', f'{SLUG}-aula{N}')
SN = open(os.path.join(BUILD, 'hub_snippets.html'), encoding='utf-8').read()
CFG = json.load(open(os.path.join(BUILD, 'config.json'), encoding='utf-8'))
L = CFG['lesson']


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card_prof = between('prof e aluno c/ /aluno/) -->\n', '\n<!-- 2. STAMP')
accordion = between('prof E aluno) -->\n', '\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n<!-- 4. ENTRADAS')
amap_entries = between('prof E aluno) -->\n<script>\n', '\n</script>').strip('\n')

# audio extra (order-lN) nao entra no snippet: vem do config
extra = ''.join(
    f'  {json.dumps(x["key"])}: "/audio/{SLUG}/{x["file"]}",\n' for x in L.get('extra_audio', []))


def div_end(s, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced div')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = len(s)

    # ---- 1. tabela curricular (Planejamento) — so o hub do professor tem a aba ----
    pr = L.get('plan_row')
    if pr and is_prof:
        row = (f'<tr><td>{N}</td><td>{pr["tema"]}</td><td>{pr["foco"]}</td>'
               f'<td>{pr["atividade"]}</td><td>{pr["homework"]}</td></tr>')
        s, n_sub = re.subn(rf'<tr[^>]*>\s*<td[^>]*>{N}</td>.*?</tr>', lambda _: row, s, count=1, flags=re.S)
        assert n_sub == 1, f'{path}: linha {N} da tabela curricular NAO encontrada'

    # ---- 2. Pre-class: troca o bloco ex-lesson-N inteiro ----
    st = s.index(f'<div class="lesson-card" id="ex-lesson-{N}">')
    en = div_end(s, st)
    s = s[:st] + accordion + s[en:]

    # ---- 3. IN CLASS: card do menu (so professor) ----
    if is_prof:
        i = s.index(f'{SLUG}-aula{N}.html?autostart=1')
        cs = s.rfind('<a ', 0, i)
        ce = s.index('</a>', i) + len('</a>')
        s = s[:cs] + card_prof.strip() + s[ce:]

    # ---- 4. Complementares: <h4> da aula N + media-grid ----
    ci = s.index(f'data-media="l{N}-')
    h4 = s.rfind('<h4', 0, ci)
    gi = s.index('<div class="media-grid"', h4)
    ge = div_end(s, gi)
    s = s[:h4] + comp + s[ge:]

    # ---- 5. stamp da aula N (label do config) ----
    stamp = next((x for x in CFG['stamps'] if x['id'] == N), None)
    if stamp:
        s = re.sub(rf'(<div class="stamp" id="stamp{N}" data-label=")[^"]*(")',
                   lambda m: m.group(1) + stamp['label'] + m.group(2), s, count=1)

    # ---- 6. audioMap: fora as chaves da aula N, dentro as novas ----
    am = re.search(r'var audioMap\s*=\s*\{', s)
    assert am, f'{path}: audioMap nao encontrado'
    body_start = am.end()
    body_end = s.index('\n};', body_start)
    body = s[body_start:body_end]
    keep = [ln for ln in body.split('\n')
            if not re.search(rf'"/audio/{SLUG}/(a{N}_|pc{N}_)', ln)]
    new_body = '\n' + amap_entries + '\n' + extra.rstrip('\n') + '\n'.join(keep)
    s = s[:body_start] + new_body + s[body_end:]

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  {os.path.relpath(path, ROOT)}: {orig} -> {len(s)} bytes ({len(s)-orig:+d})')


patch(os.path.join(ROOT, 'public', 'professor', f'{SLUG}.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', f'{SLUG}.html'), False)
print(f'OK — aula {N} trocada nas 4 abas (prof + aluno)')
