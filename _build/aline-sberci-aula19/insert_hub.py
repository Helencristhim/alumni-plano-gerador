#!/usr/bin/env python3
# Insere os snippets da aula 19 nos hubs prof + aluno (SO ADITIVO).
import re

SNIP = open('_build/aline-sberci-aula19/hub_snippets.html', encoding='utf-8').read()

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
        anchor = '/professor/aline-sberci-aula18.html?autostart=1'
        i = h.index(anchor)
        close = h.index('</a>', i) + len('</a>')
        assert h.count('aline-sberci-aula19.html?autostart') == 0, 'aula19 card ja existe'
        h = h[:close] + '\n            ' + menu_card.strip() + h[close:]

    # --- 2. STAMP (after stamp18) ---
    si = h.index('id="stamp18"')
    sclose = h.index('</div>', si) + len('</div>')
    assert 'id="stamp19"' not in h, 'stamp19 ja existe'
    h = h[:sclose] + '\n        ' + stamp.strip() + h[sclose:]

    # --- 3. ACCORDION Pre-class (insert as a sibling lesson-card right AFTER
    #        ex-lesson-18's lesson-card closes, but BEFORE the tab-content </div>
    #        that closes the Pre-class tab — so the new card stays inside the tab) ---
    assert 'id="ex-lesson-19"' not in h, 'ex-lesson-19 ja existe'
    i = h.index('id="ex-lesson-18"')
    start = h.rfind('<div', 0, i)  # opening <div class="lesson-card" ...>
    depth = 0
    card_end = None
    for m in re.finditer(r'<div\b|</div>', h[start:]):
        if m.group().startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                card_end = start + m.end()
                break
    assert card_end is not None, 'nao achei o fim do card ex-lesson-18'
    h = h[:card_end] + '\n' + accordion.strip() + h[card_end:]

    # --- 4. COMPLEMENTARY (after the l18 media-grid close, as a sibling inside tab-complementary) ---
    assert 'data-media="l19-' not in h, 'l19 complementary ja existe'
    ci = h.index('data-media="l18-podcast"')
    grid_close = h.index('</div>\n</div>\n', ci) + len('</div>\n</div>\n')
    h = h[:grid_close] + '\n' + comp + '\n' + h[grid_close:]

    # --- 5. audioMap merge ---
    am = re.search(r'(?:var|const)\s+audioMap\s*=\s*\{', h)
    pos = am.end()
    h = h[:pos] + '\n' + am_entries + h[pos:]

    # --- 6. totalLessons 18 -> 19 ---
    h2 = h.replace('var totalLessons=18;', 'var totalLessons=19;')
    assert h2 != h, 'totalLessons nao trocado'
    h = h2

    assert len(h) > orig_len, 'arquivo encolheu'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-orig_len} bytes)')

patch('public/professor/aline-sberci.html', True)
patch('public/aluno/aline-sberci.html', False)
