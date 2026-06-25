#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica ADITIVAMENTE os snippets da aula 20 aos hubs prof+aluno (REGRA 20 — hub
existente, só adiciona). Lê hub_snippets.html gerado pelo builder e insere:
stamp20, ex-lesson-20, complementares l20, audioMap, totalLessons 19->20, e o
card do menu IN CLASS (só prof). Aulas 1-19 ficam byte-idênticas exceto as adições."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()


def between(s, a, b):
    i = s.index(a)
    j = s.index(b, i + len(a))
    return s[i:j].rstrip()


# 1. menu card (só prof)
menu_card = between(snip, '<!-- 1. CARD', '<!-- 2. STAMP')
menu_card = menu_card.split('-->', 1)[1].strip('\n')
# 2. stamp
stamp = between(snip, '<!-- 2. STAMP', '<!-- 3. ACCORDION').split('-->', 1)[1].strip()
# 3. accordion Pre-class
accordion = between(snip, '<!-- 3. ACCORDION', '<!-- 3b. COMPLEMENTARES').split('-->', 1)[1].strip('\n')
# 3b. complementares
comp = between(snip, '<!-- 3b. COMPLEMENTARES', '<!-- 4. ENTRADAS').split('-->', 1)[1].strip('\n')
# 4. audioMap entries
amap_block = between(snip, '<!-- 4. ENTRADAS', '<!-- 5. Ajustar')
amap_lines = [ln for ln in amap_block.split('\n') if ln.strip().startswith('"')]
# inject [order-l20] manually (extract_phrases skips '[' prefix)
amap_lines.append('  "[order-l20]": "/audio/pricila-adamo/pc20_order_settle.mp3",')
amap_inject = '\n'.join(amap_lines)


def apply(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s

    # --- stamp20 after stamp19 line ---
    m = re.search(r'(<div class="stamp" id="stamp19"[^\n]*</div>)\n', s)
    assert m, f'{path}: stamp19 não achado'
    indent = re.match(r'\s*', s[s.rfind('\n', 0, m.start())+1:m.start()]).group()
    s = s[:m.end()] + indent + stamp + '\n' + s[m.end():]

    # --- ex-lesson-20 after the FULL ex-lesson-19 card ---
    i19 = s.index('<div class="lesson-card" id="ex-lesson-19">')
    close_marker = '\n\n</div><!-- /tab-exercises -->'
    j19 = s.index(close_marker, i19)
    s = s[:j19] + '\n\n' + accordion + s[j19:]

    # --- menu card (só prof): after the aula19 IN CLASS link ---
    if is_prof:
        link19 = '<a href="/professor/pricila-adamo-aula19.html?autostart=1"'
        li = s.index(link19)
        ci = s.index('\n    </a>\n', li) + len('\n    </a>\n')
        s = s[:ci] + menu_card + '\n' + s[ci:]

    # --- complementares l20 after the l19-youtube wrapper, before /tab-complementary ---
    yi = s.index('data-media="l19-youtube"')
    tc = s.index('</div><!-- /tab-complementary -->', yi)
    s = s[:tc] + comp + '\n\n' + s[tc:]

    # --- audioMap entries: right after 'var audioMap = {' (plain insert) ---
    open_tag = 'var audioMap = {\n'
    oi = s.index(open_tag) + len(open_tag)
    s = s[:oi] + amap_inject + '\n' + s[oi:]

    # --- totalLessons 19 -> 20 ---
    s = s.replace('var totalLessons=19;', 'var totalLessons=20;')

    assert s != orig, f'{path}: nada mudou'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  applied -> {os.path.relpath(path, ROOT)}')


apply(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
apply(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('done')
