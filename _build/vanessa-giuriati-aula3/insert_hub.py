#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 3 nos hubs prof+aluno de vanessa-giuriati (ADITIVO).
Anexa: card do menu IN CLASS, stamp3, accordion ex-lesson-3, complementares aula3,
entradas de audioMap, e ajusta totalLessons 2->3. Idempotente (aborta se ex-lesson-3 ja existe)."""
import re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

def block(label_start, label_end=None):
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
# audioMap entries: strip <script> wrapper
am_raw = block('<!-- 4.')
am_entries = am_raw.replace('<script>', '').replace('</script>', '').strip('\n')

def insert(path, base_href):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-3"' in s:
        print(f'  SKIP (already has aula3): {path}')
        return
    n = s

    has_inclass = '<!-- ========== TAB 3: IN CLASS' in n

    # 1. menu card — only in prof hub (aluno hub has no IN CLASS tab, REGRA 3)
    if has_inclass:
        mc = menu_card
        m = re.search(r'(<a href="' + re.escape(base_href) + r'vanessa-giuriati-aula2\.html\?autostart=1".*?</a>)', n, re.S)
        assert m, f'menu aula2 card not found in {path}'
        n = n[:m.end()] + '\n' + mc + n[m.end():]

    # 2. stamp — after stamp2
    m = re.search(r'(<div class="stamp" id="stamp2".*?></div>)', n, re.S)
    assert m, f'stamp2 not found in {path}'
    n = n[:m.end()] + '\n' + stamp + n[m.end():]

    # 3. accordion — after the close of ex-lesson-2 card. ex-lesson-2 div closes right before tab-inclass/complementary.
    # Find ex-lesson-2 start, then match balanced... simpler: insert before the closing </div> of #tab-exercises.
    # The accordion lives inside tab-exercises. Insert right before '</div><!-- /tab-exercises' marker if present,
    # else before the tab-inclass comment. We anchor on the survival-card END of lesson 2 + its two closing divs.
    # Robust anchor: the menu IN CLASS section comment.
    marker = '</div><!-- /tab-exercises -->'
    idx = n.find(marker)
    assert idx != -1, f'/tab-exercises marker not found in {path}'
    pre = n[:idx]
    assert pre.rfind('id="ex-lesson-2"') != -1
    n = pre + accordion + '\n' + n[idx:]

    # 3b. complementares — before </div><!-- /tab-complementary -->
    m = re.search(r'(</div><!-- /tab-complementary -->)', n)
    assert m, f'/tab-complementary marker not found in {path}'
    n = n[:m.start()] + complement + '\n' + n[m.start():]

    # 4. audioMap — insert entries right after 'audioMap = {'
    m = re.search(r'(audioMap = \{\s*\n)', n)
    assert m, f'audioMap open not found in {path}'
    n = n[:m.end()] + am_entries + '\n' + n[m.end():]

    # 5. totalLessons 2 -> 3
    n2 = re.sub(r'var totalLessons=2;', 'var totalLessons=3;', n)
    assert n2 != n, f'totalLessons=2 not found in {path}'
    n = n2

    open(path, 'w', encoding='utf-8').write(n)
    print(f'  OK: {path}')

insert(os.path.join(ROOT, 'public/professor/vanessa-giuriati.html'), '/professor/')
insert(os.path.join(ROOT, 'public/aluno/vanessa-giuriati.html'), '/aluno/')
print('done')
