#!/usr/bin/env python3
import re

SNIP = open('_build/maria-claudia-curimbaba-aula19/hub_snippets.html', encoding='utf-8').read()

def section(start_marker, end_marker):
    s = SNIP.index(start_marker) + len(start_marker)
    e = SNIP.index(end_marker)
    return SNIP[s:e].strip('\n')

card_raw   = section('(inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
stamp_raw  = section('(inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
accord_raw = section('(inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
compl_raw  = section('(inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
am = SNIP.index('<!-- 4. ENTRADAS')
am_s = SNIP.index('<script>', am) + len('<script>')
am_e = SNIP.index('</script>', am_s)
audio_entries = SNIP[am_s:am_e].strip('\n')

def insert_before(html, anchor, block):
    idx = html.index(anchor)
    return html[:idx] + block + '\n' + html[idx:]

def process(path, is_prof):
    html = open(path, encoding='utf-8').read()
    orig = html

    # 1. IN CLASS card — PROF ONLY (aluno hub has no launch card)
    if is_prof:
        anchor = '<a href="/professor/maria-claudia-curimbaba-aula18.html?autostart=1"'
        card = card_raw.replace('aula19.html?autostart=1" ', 'aula19.html?autostart=1" target="_blank" ')
        assert anchor in html, f'{path}: IN CLASS aula18 anchor not found'
        html = insert_before(html, anchor, card.strip())

    # 2. stamp — before stamp18
    anchor = '<div class="stamp" id="stamp18"'
    assert anchor in html, f'{path}: stamp18 not found'
    html = insert_before(html, anchor, stamp_raw)

    # 3. accordion — before ex-lesson-18
    anchor = '<div class="lesson-card" id="ex-lesson-18">'
    assert anchor in html, f'{path}: ex-lesson-18 not found'
    html = insert_before(html, anchor, accord_raw)

    # 3b. complementary — before aula18 complementary header
    anchor = '<h4 style="font-family:\'Cormorant Garamond\',serif;font-size:1.1rem;color:var(--accent);margin-top:2rem;margin-bottom:.8rem">Aula 18 -- Decision-Making: I Suggest We...</h4>'
    assert anchor in html, f'{path}: complementary aula18 header not found'
    html = insert_before(html, anchor, compl_raw)

    # 4. audioMap entries — after first "var audioMap = {"
    m = re.search(r'var audioMap = \{', html)
    assert m, f'{path}: audioMap not found'
    pos = m.end()
    html = html[:pos] + '\n' + audio_entries + html[pos:]

    # 5. totalLessons 18 -> 19
    html, n = re.subn(r'totalLessons=18', 'totalLessons=19', html)
    assert n >= 1, f'{path}: totalLessons=18 not found'

    assert html != orig
    open(path, 'w', encoding='utf-8').write(html)
    print(f'OK {path} (+{len(html)-len(orig)} bytes)')

process('public/professor/maria-claudia-curimbaba.html', True)
process('public/aluno/maria-claudia-curimbaba.html', False)
