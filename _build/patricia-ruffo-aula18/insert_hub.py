#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inserção ADITIVA dos snippets da aula 18 no hub prof + aluno de patricia-ruffo.
Idempotente: aborta se a aula 18 já estiver presente. Não toca aulas anteriores."""
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
COMP     = block('-- 3b. COMPLEMENTARES da aula 18 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
# audioMap entries: between <script> and </script>
am_i = SNIP.index('<!-- 4. ENTRADAS')
am_start = SNIP.index('<script>', am_i) + len('<script>')
am_end = SNIP.index('</script>', am_start)
AUDIO = SNIP[am_start:am_end].strip('\n')

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-18"' not in s, f'{path}: aula 18 JÁ presente — abortando'
    # 1. STAMP after stamp17
    anchor = '<div class="stamp" id="stamp17" data-label="Conference Networker" style="background-image:url(\'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=200&q=80\')"></div>'
    assert anchor in s, f'{path}: anchor stamp17 não encontrado'
    s = s.replace(anchor, anchor + '\n' + STAMP, 1)
    # 2. ACCORDION before /tab-exercises
    ex_close = '</div><!-- /tab-exercises -->'
    assert ex_close in s, f'{path}: /tab-exercises não encontrado'
    s = s.replace(ex_close, ACCORD + '\n\n' + ex_close, 1)
    # 3. IN CLASS card (só prof) — após o card da aula 17
    if is_prof:
        card17_end = '<div><div style="font-weight:600;font-size:.95rem">Networking at Conferences</div><div style="font-size:.8rem;color:var(--text-dim)">Professional small talk and the follow-up: starting conversations, building rapport and keeping in touch after a conference -- 30 slides</div></div>\n    </a>'
        assert card17_end in s, f'{path}: card IN CLASS aula17 não encontrado'
        s = s.replace(card17_end, card17_end + '\n' + CARD, 1)
    # 4. COMPLEMENTARES before /tab-complementary
    comp_close = '</div><!-- /tab-complementary -->'
    assert comp_close in s, f'{path}: /tab-complementary não encontrado'
    s = s.replace(comp_close, COMP + '\n' + comp_close, 1)
    # 5. audioMap entries after `var audioMap = {`
    am_anchor = 'var audioMap = {'
    assert am_anchor in s, f'{path}: var audioMap não encontrado'
    s = s.replace(am_anchor, am_anchor + '\n' + AUDIO, 1)
    # 6. totalLessons -> 18 (nunca rebaixar; maior nº presente)
    s2 = re.sub(r'var totalLessons=\d+;', 'var totalLessons=18;', s, count=1)
    assert s2 != s and 'var totalLessons=18;' in s2, f'{path}: totalLessons não encontrado'
    s = s2
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)}')

patch(os.path.join(ROOT, 'public/professor/patricia-ruffo.html'), is_prof=True)
patch(os.path.join(ROOT, 'public/aluno/patricia-ruffo.html'), is_prof=False)
print('OK')
