#!/usr/bin/env python3
# Insere os snippets da aula 19 nos hubs prof + aluno do roberto-rezende (SO ADITIVO).
# Legado: hub aluno tem buracos (ex-lesson 7-9, stamps 7-11 faltando), PRE-EXISTENTE.
# NAO consertamos: so anexamos a aula 19 apos o ULTIMO stamp/ex-lesson presente em CADA arquivo.
import re

SNIP = open('_build/roberto-rezende-aula19/hub_snippets.html', encoding='utf-8').read()

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


def end_of_wrapper(h, start_idx):
    """Given index inside a media-card-wrapper, return index just after its matching </div>."""
    open_div = h.rfind('<div', 0, start_idx)
    i = open_div
    depth = 0
    tag_re = re.compile(r'<(/?)div\b[^>]*>')
    while True:
        m = tag_re.search(h, i)
        if not m:
            raise AssertionError('matching </div> not found')
        if m.group(1) == '/':
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
        i = m.end()


def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    orig_len = len(h)

    # --- 1. MENU CARD (prof only) — apos o card da aula 18 ---
    if is_prof:
        anchor = '/professor/roberto-rezende-aula18.html?autostart=1'
        assert h.count('roberto-rezende-aula19.html?autostart') == 0, 'aula19 card ja existe'
        i = h.index(anchor)
        close = h.index('</a>', i) + len('</a>')
        h = h[:close] + '\n            ' + menu_card.strip() + h[close:]

    # --- 2. STAMP (apos o ULTIMO stamp presente; difere prof vs aluno) ---
    assert 'id="stamp19"' not in h, 'stamp19 ja existe'
    last_stamp = [m.start() for m in re.finditer(r'id="stamp\d+"', h)][-1]
    sclose = h.index('</div>', last_stamp) + len('</div>')
    h = h[:sclose] + '\n        ' + stamp.strip() + h[sclose:]

    # --- 3. ACCORDION Pre-class (DENTRO de tab-exercises, logo apos o FIM do
    #        card ex-lesson-18) ---
    assert 'id="ex-lesson-19"' not in h, 'ex-lesson-19 ja existe'
    li = h.index('id="ex-lesson-18"')
    card_end = end_of_wrapper(h, li)
    h = h[:card_end] + '\n' + accordion.strip() + '\n' + h[card_end:]

    # --- 4. COMPLEMENTARY (apos o ULTIMO wrapper l18, dentro de tab-complementary) ---
    assert 'data-media="l19-' not in h, 'l19 complementary ja existe'
    last_l18 = [m.start() for m in re.finditer(r'data-media="l18-', h)][-1]
    wrap_end = end_of_wrapper(h, last_l18)
    h = h[:wrap_end] + '\n' + comp + '\n' + h[wrap_end:]

    # --- 5. audioMap merge ---
    am = re.search(r'(?:var|const)\s+audioMap\s*=\s*\{', h)
    pos = am.end()
    h = h[:pos] + '\n' + am_entries + h[pos:]

    # --- 6. totalLessons 18 -> 19 (ADITIVO) ---
    h2 = re.sub(r'var totalLessons ?= ?18', 'var totalLessons=19', h)
    assert h2 != h, 'totalLessons nao trocado'
    h = h2

    assert len(h) > orig_len, 'arquivo encolheu'
    open(path, 'w', encoding='utf-8').write(h)
    print(f'OK {path}  (+{len(h)-orig_len} bytes)')


patch('public/professor/roberto-rezende.html', True)
patch('public/aluno/roberto-rezende.html', False)
