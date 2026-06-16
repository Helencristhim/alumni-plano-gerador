#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 14 no hub prof + aluno de patricia-ruffo.
Idempotente: aborta se a aula 14 ja estiver presente. Nao toca aulas anteriores."""
import re, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()

def block(after_marker, end_marker):
    i = SNIP.index(after_marker) + len(after_marker)
    j = SNIP.index(end_marker, i)
    return SNIP[i:j].strip('\n')

CARD   = block('-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
STAMP  = block('-- 2. STAMP (inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACCORD = block('-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
COMP   = block('-- 3b. COMPLEMENTARES da aula 14 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am_i = SNIP.index('<!-- 4. ENTRADAS')
am_start = SNIP.index('<script>', am_i) + len('<script>')
am_end = SNIP.index('</script>', am_start)
AUDIO = SNIP[am_start:am_end].strip('\n')

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-14"' not in s, f'{path}: aula 14 JA presente -- abortando'
    # 1. STAMP after stamp12
    anchor = '<div class="stamp" id="stamp12" data-label="Data Storyteller" style="background-image:url(\'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80\')"></div>'
    assert anchor in s, f'{path}: anchor stamp12 nao encontrado'
    s = s.replace(anchor, anchor + '\n' + STAMP, 1)
    # 2. ACCORDION before /tab-exercises
    ex_close = '</div><!-- /tab-exercises -->'
    assert ex_close in s, f'{path}: /tab-exercises nao encontrado'
    s = s.replace(ex_close, ACCORD + '\n\n' + ex_close, 1)
    # 3. IN CLASS card (so prof) -- apos o card da aula12
    if is_prof:
        card12_end = 'Describing Data, Trends & Charts</div><div style="font-size:.8rem;color:var(--text-dim)">Reading the data story: comparatives and trend language to describe charts, increases, declines and peaks -- 30 slides</div></div>\n    </a>'
        assert card12_end in s, f'{path}: card IN CLASS aula12 nao encontrado'
        s = s.replace(card12_end, card12_end + '\n' + CARD, 1)
    # 4. COMPLEMENTARES before /tab-complementary
    comp_close = '</div><!-- /tab-complementary -->'
    assert comp_close in s, f'{path}: /tab-complementary nao encontrado'
    s = s.replace(comp_close, COMP + '\n' + comp_close, 1)
    # 5. audioMap entries after `var audioMap = {`
    am_anchor = 'var audioMap = {'
    assert am_anchor in s, f'{path}: var audioMap nao encontrado'
    s = s.replace(am_anchor, am_anchor + '\n' + AUDIO, 1)
    # 6. totalLessons -> 14 (nunca rebaixar; hub esta em 12)
    m = re.search(r'var totalLessons=(\d+);', s)
    assert m, f'{path}: totalLessons nao encontrado'
    cur = int(m.group(1))
    new = max(cur, 14)
    s = re.sub(r'var totalLessons=\d+;', f'var totalLessons={new};', s, count=1)
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} (totalLessons {cur}->{new})')

if __name__ == '__main__':
    patch(os.path.join(ROOT, 'public/professor/patricia-ruffo.html'), is_prof=True)
    patch(os.path.join(ROOT, 'public/aluno/patricia-ruffo.html'), is_prof=False)
    print('OK')
