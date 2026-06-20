#!/usr/bin/env python3
# Insere os snippets da aula 18 nos hubs prof + aluno (SO ADITIVO).
import re

SNIP = open('_build/aline-sberci-aula18/hub_snippets.html', encoding='utf-8').read()

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
        anchor = '/professor/aline-sberci-aula17.html?autostart=1'
        i = h.index(anchor)
        close = h.index('</a>', i) + len('</a>')
        assert h.count('aline-sberci-aula18.html?autostart') == 0, 'aula18 card ja existe'
        h = h[:close] + '\n            ' + menu_card.strip() + h[close:]

    # --- 2. STAMP (after stamp17) ---
    si = h.index('id="stamp17"')
    sclose = h.index('</div>', si) + len('</div>')
    assert 'id="stamp18"' not in h, 'stamp18 ja existe'
    h = h[:sclose] + '\n        ' + stamp.strip() + h[sclose:]

    # --- 3. ACCORDION Pre-class (insere LOGO APOS o card ex-lesson-17, dentro do
    #     mesmo container tab-exercises). Casa profundidade desde o <div ... id="ex-lesson-17">
    #     ate o </div> que o fecha e insere o novo accordion logo apos. ---
    assert 'id="ex-lesson-18"' not in h, 'ex-lesson-18 ja existe'
    li = h.index('id="ex-lesson-17"')
    open_div = h.rindex('<div', 0, li)
    depth = 0
    token = re.compile(r'<div\b|</div>')
    end_card = None
    for mtok in token.finditer(h, open_div):
        depth += 1 if mtok.group().startswith('<div') else -1
        if depth == 0:
            end_card = mtok.end()
            break
    assert end_card is not None, 'nao achei o fim do card ex-lesson-17'
    h = h[:end_card] + '\n\n' + accordion.strip() + h[end_card:]

    # --- 4. COMPLEMENTARY (after the l17 media-grid close, as a sibling inside tab-complementary) ---
    assert 'data-media="l18-' not in h, 'l18 complementary ja existe'
    ci = h.index('data-media="l17-podcast"')
    grid_close = h.index('</div>\n</div>\n', ci) + len('</div>\n</div>\n')
    h = h[:grid_close] + '\n' + comp + '\n' + h[grid_close:]

    # --- 5. audioMap merge ---
    am = re.search(r'(?:var|const)\s+audioMap\s*=\s*\{', h)
    pos = am.end()
    h = h[:pos] + '\n' + am_entries + h[pos:]

    # --- 6. totalLessons 17 -> 18 ---
    h2 = h.replace('var totalLessons=17;', 'var totalLessons=18;')
    assert h2 != h, 'totalLessons nao trocado'
    h = h2

    assert len(h) > orig_len, 'arquivo encolheu'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-orig_len} bytes)')

patch('public/professor/aline-sberci.html', True)
patch('public/aluno/aline-sberci.html', False)
