#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 4 nos hubs prof+aluno de vanessa-giuriati (ADITIVO).
Anexa: card do menu IN CLASS (so prof), stamp4, accordion ex-lesson-4, complementares
aula4, entradas de audioMap, e ajusta totalLessons 3->4. Idempotente."""
import re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()
N = 5
PREV = N - 1

def block(label_start):
    lines = SNIP.splitlines(keepends=True)
    out, capturing = [], False
    for ln in lines:
        if ln.startswith(label_start):
            capturing = True
            continue
        if capturing and ln.startswith('<!-- '):
            break
        if capturing:
            out.append(ln)
    return ''.join(out).strip('\n')

menu_card = block('<!-- 1.')
stamp = block('<!-- 2.')
accordion = block('<!-- 3. ')
complement = block('<!-- 3b.')
am_raw = block('<!-- 4.')
am_entries = am_raw.replace('<script>', '').replace('</script>', '').strip('\n')

def insert(path, base_href):
    s = open(path, encoding='utf-8').read()
    if f'id="ex-lesson-{N}"' in s:
        print(f'  SKIP (already has aula{N}): {path}')
        return
    n = s
    has_inclass = '<!-- ========== TAB 3: IN CLASS' in n

    # 1. menu card — only in prof hub (aluno hub has no IN CLASS tab, REGRA 3)
    if has_inclass:
        m = re.search(r'(<a href="' + re.escape(base_href) + r'vanessa-giuriati-aula' + str(PREV) + r'\.html\?autostart=1".*?</a>)', n, re.S)
        assert m, f'menu aula{PREV} card not found in {path}'
        n = n[:m.end()] + '\n' + menu_card + n[m.end():]

    # 2. stamp — after previous stamp
    m = re.search(r'(<div class="stamp" id="stamp' + str(PREV) + r'".*?></div>)', n, re.S)
    assert m, f'stamp{PREV} not found in {path}'
    n = n[:m.end()] + '\n' + stamp + n[m.end():]

    # 3. accordion — before close of #tab-exercises
    marker = '</div><!-- /tab-exercises -->'
    idx = n.find(marker)
    assert idx != -1, f'/tab-exercises marker not found in {path}'
    pre = n[:idx]
    assert pre.rfind(f'id="ex-lesson-{PREV}"') != -1
    n = pre + accordion + '\n' + n[idx:]

    # 3b. complementares — before /tab-complementary
    m = re.search(r'(</div><!-- /tab-complementary -->)', n)
    assert m, f'/tab-complementary marker not found in {path}'
    n = n[:m.start()] + complement + '\n' + n[m.start():]

    # 4. audioMap entries
    m = re.search(r'(audioMap = \{\s*\n)', n)
    assert m, f'audioMap open not found in {path}'
    n = n[:m.end()] + am_entries + '\n' + n[m.end():]

    # 5. totalLessons PREV -> N
    n2 = re.sub(r'var totalLessons=' + str(PREV) + r';', f'var totalLessons={N};', n)
    assert n2 != n, f'totalLessons={PREV} not found in {path}'
    n = n2

    open(path, 'w', encoding='utf-8').write(n)
    print(f'  OK: {path}')

insert(os.path.join(ROOT, 'public/professor/vanessa-giuriati.html'), '/professor/')
insert(os.path.join(ROOT, 'public/aluno/vanessa-giuriati.html'), '/aluno/')
print('done')
