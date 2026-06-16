#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 16 no hub prof + aluno de patricia-ruffo.
Idempotente: aborta se a aula 16 ja estiver presente. NAO toca aulas anteriores.
Anchors estaveis (independem da ordem das aulas 13/14/15 que podem entrar em paralelo):
- stamp e card sao inseridos logo apos a ABERTURA do container (prepend), nunca depois de um stamp/card especifico.
- accordion antes de /tab-exercises; complementares antes de /tab-complementary.
- audioMap apos `var audioMap = {`; totalLessons elevado p/ max(atual, 16); TOTAL_AULAS intacto (40)."""
import re, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

def block(after_marker, end_marker):
    i = SNIP.index(after_marker) + len(after_marker)
    j = SNIP.index(end_marker, i)
    return SNIP[i:j].strip('\n')

CARD     = block('-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
STAMP    = block('-- 2. STAMP (inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACCORD   = block('-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
COMP     = block('-- 3b. COMPLEMENTARES da aula 16 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_i = SNIP.index('<!-- 4. ENTRADAS')
am_start = SNIP.index('<script>', am_i) + len('<script>')
am_end = SNIP.index('</script>', am_start)
AUDIO = SNIP[am_start:am_end].strip('\n')

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-16"' not in s, f'{path}: aula 16 JA presente — abortando'

    # 1. STAMP — logo apos a abertura da stamps-row (prepend, order-independent)
    stamp_anchor = '<div class="stamps-row">'
    assert stamp_anchor in s, f'{path}: stamps-row nao encontrado'
    s = s.replace(stamp_anchor, stamp_anchor + '\n' + STAMP, 1)

    # 2. ACCORDION — antes do fechamento de /tab-exercises
    ex_close = '</div><!-- /tab-exercises -->'
    assert ex_close in s, f'{path}: /tab-exercises nao encontrado'
    s = s.replace(ex_close, ACCORD + '\n\n' + ex_close, 1)

    # 3. IN CLASS card (so prof) — prepend na lista de cards da tab-inclass
    if is_prof:
        card_list_anchor = '<div class="tab-content" id="tab-inclass">\n  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS -- Select Lesson</h3>\n  <div style="display:flex;flex-direction:column;gap:1rem">'
        assert card_list_anchor in s, f'{path}: container de cards IN CLASS nao encontrado'
        s = s.replace(card_list_anchor, card_list_anchor + '\n' + CARD, 1)

    # 4. COMPLEMENTARES — antes de /tab-complementary
    comp_close = '</div><!-- /tab-complementary -->'
    assert comp_close in s, f'{path}: /tab-complementary nao encontrado'
    s = s.replace(comp_close, COMP + '\n' + comp_close, 1)

    # 5. audioMap entries apos `var audioMap = {`
    am_anchor = 'var audioMap = {'
    assert am_anchor in s, f'{path}: var audioMap nao encontrado'
    s = s.replace(am_anchor, am_anchor + '\n' + AUDIO, 1)

    # 6. totalLessons -> max(atual, 16); NUNCA rebaixar
    m = re.search(r'var totalLessons=(\d+);', s)
    assert m, f'{path}: totalLessons nao encontrado'
    cur = int(m.group(1))
    newv = max(cur, 16)
    s = re.sub(r'var totalLessons=\d+;', f'var totalLessons={newv};', s, count=1)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} (totalLessons={newv})')

patch(os.path.join(ROOT, 'public/professor/patricia-ruffo.html'), is_prof=True)
patch(os.path.join(ROOT, 'public/aluno/patricia-ruffo.html'), is_prof=False)
print('OK')
