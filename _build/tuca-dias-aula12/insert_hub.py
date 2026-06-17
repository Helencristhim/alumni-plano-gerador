#!/usr/bin/env python3
# Insere os snippets da aula 12 nos hubs prof + aluno (SÓ ADITIVO).
import re, sys

SNIP = open('_build/tuca-dias-aula12/hub_snippets.html', encoding='utf-8').read()

def section(start_marker, end_marker):
    s = SNIP.index(start_marker)
    s = SNIP.index('\n', s) + 1
    e = SNIP.index(end_marker)
    return SNIP[s:e].strip('\n')

menu_card = section('<!-- 1. CARD', '<!-- 2. STAMP')
stamp = section('<!-- 2. STAMP', '<!-- 3. ACCORDION')
accordion = section('<!-- 3. ACCORDION', '<!-- 3b. COMPLEMENTAR')
comp = section('<!-- 3b. COMPLEMENTAR', '<!-- 4. ENTRADAS')
am_block = SNIP[SNIP.index('<!-- 4. ENTRADAS'):SNIP.index('<!-- 5.')]
am_entries = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip('\n')

def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    orig_len = len(h)

    # --- 1. MENU CARD (prof only) ---
    if is_prof:
        anchor = '/professor/tuca-dias-aula11.html?autostart=1'
        i = h.index(anchor)
        close = h.index('</a>', i) + len('</a>')
        assert h.count('tuca-dias-aula12.html?autostart') == 0, 'aula12 card já existe'
        h = h[:close] + '\n            ' + menu_card.strip() + h[close:]

    # --- 2. STAMP (after stamp11) ---
    si = h.index('id="stamp11"')
    sclose = h.index('</div>', si) + len('</div>')
    assert 'id="stamp12"' not in h, 'stamp12 já existe'
    h = h[:sclose] + '\n        ' + stamp.strip() + h[sclose:]

    # --- 3. ACCORDION Pre-class (after ex-lesson-11, before next major block) ---
    li = h.index('id="ex-lesson-11"')
    if is_prof:
        nxt = h.index('<div class="tab-content" id="tab-inclass">')
    else:
        nxt = h.index('<div class="tab-content" id="tab-complementary">', li)
    assert 'id="ex-lesson-12"' not in h, 'ex-lesson-12 já existe'
    h = h[:nxt] + accordion.strip() + '\n\n' + h[nxt:]

    # --- 4. COMPLEMENTARY (before /tab-complementary) ---
    ci = h.index('data-media="l11-youtube"')
    tc = h.index('</div><!-- /tab-complementary -->')
    assert 'data-media="l12-' not in h, 'l12 complementary já existe'
    h = h[:tc] + comp + '\n' + h[tc:]

    # --- 5. audioMap merge ---
    am = re.search(r'(?:var|const)\s+audioMap\s*=\s*\{', h)
    pos = am.end()
    h = h[:pos] + '\n' + am_entries + h[pos:]

    # --- 6. totalLessons 11 -> 12 ---
    h2 = h.replace('var totalLessons=11;', 'var totalLessons=12;')
    assert h2 != h, 'totalLessons não trocado'
    h = h2

    assert len(h) > orig_len, 'arquivo encolheu'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-orig_len} bytes)')

patch('public/professor/tuca-dias.html', True)
patch('public/aluno/tuca-dias.html', False)
