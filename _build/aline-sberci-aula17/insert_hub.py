#!/usr/bin/env python3
# Insere os snippets da aula 17 nos hubs prof + aluno (SO ADITIVO).
import re

SNIP = open('_build/aline-sberci-aula17/hub_snippets.html', encoding='utf-8').read()

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
        anchor = '/professor/aline-sberci-aula16.html?autostart=1'
        i = h.index(anchor)
        close = h.index('</a>', i) + len('</a>')
        assert h.count('aline-sberci-aula17.html?autostart') == 0, 'aula17 card ja existe'
        h = h[:close] + '\n            ' + menu_card.strip() + h[close:]

    # --- 2. STAMP (after stamp16) ---
    si = h.index('id="stamp16"')
    sclose = h.index('</div>', si) + len('</div>')
    assert 'id="stamp17"' not in h, 'stamp17 ja existe'
    h = h[:sclose] + '\n        ' + stamp.strip() + h[sclose:]

    # --- 3. ACCORDION Pre-class (insere LOGO APOS o card ex-lesson-16, dentro do
    #     mesmo container tab-exercises). O ex-lesson-16 e o ultimo .lesson-card da
    #     aba; precisamos achar o </div> que fecha esse card (casando profundidade
    #     desde o <div ... id="ex-lesson-16">), e inserir o novo accordion logo apos.
    #     Inserir antes de tab-inclass/tab-complementary coloca o card FORA da aba
    #     (depth 2 em vez de 3 -> ORPHAN no audit). ---
    assert 'id="ex-lesson-17"' not in h, 'ex-lesson-17 ja existe'
    li = h.index('id="ex-lesson-16"')
    open_div = h.rindex('<div', 0, li)   # inicio da tag <div ... id="ex-lesson-16">
    depth = 0
    k = open_div
    import re as _re
    token = _re.compile(r'<div\b|</div>')
    end_card = None
    for mtok in token.finditer(h, open_div):
        depth += 1 if mtok.group().startswith('<div') else -1
        if depth == 0:
            end_card = mtok.end()   # posicao logo apos o </div> que fecha o card
            break
    assert end_card is not None, 'nao achei o fim do card ex-lesson-16'
    h = h[:end_card] + '\n\n' + accordion.strip() + h[end_card:]

    # --- 4. COMPLEMENTARY (after the l16 media-grid close, as a sibling inside tab-complementary) ---
    assert 'data-media="l17-' not in h, 'l17 complementary ja existe'
    ci = h.index('data-media="l16-podcast"')
    # the l16 media-grid closes with '</div>\n</div>\n' right after the last wrapper
    grid_close = h.index('</div>\n</div>\n', ci) + len('</div>\n</div>\n')
    h = h[:grid_close] + '\n' + comp + '\n' + h[grid_close:]

    # --- 5. audioMap merge ---
    am = re.search(r'(?:var|const)\s+audioMap\s*=\s*\{', h)
    pos = am.end()
    h = h[:pos] + '\n' + am_entries + h[pos:]

    # --- 6. totalLessons 16 -> 17 ---
    h2 = h.replace('var totalLessons=16;', 'var totalLessons=17;')
    assert h2 != h, 'totalLessons nao trocado'
    h = h2

    assert len(h) > orig_len, 'arquivo encolheu'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-orig_len} bytes)')

patch('public/professor/aline-sberci.html', True)
patch('public/aluno/aline-sberci.html', False)
