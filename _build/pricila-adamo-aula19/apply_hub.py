#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica ADITIVAMENTE os snippets da aula 19 aos hubs prof+aluno (REGRA 20 — hub
existente, só adiciona). Lê hub_snippets.html gerado pelo builder e insere:
stamp19, ex-lesson-19, complementares l19, audioMap, totalLessons 18->19, e o
card do menu IN CLASS (só prof). Aulas 1-18 ficam byte-idênticas exceto as adições."""
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
# inject [order-l19] manually (extract_phrases skips '[' prefix)
amap_lines.append('  "[order-l19]": "/audio/pricila-adamo/pc19_order_hobby.mp3",')
amap_inject = '\n'.join(amap_lines)


def apply(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s

    # --- stamp19 after stamp18 line ---
    m = re.search(r'(<div class="stamp" id="stamp18"[^\n]*</div>)\n', s)
    assert m, f'{path}: stamp18 não achado'
    indent = re.match(r'\s*', s[s.rfind('\n', 0, m.start())+1:m.start()]).group()
    s = s[:m.end()] + indent + stamp + '\n' + s[m.end():]

    # --- ex-lesson-19 after the FULL ex-lesson-18 card ---
    i18 = s.index('<div class="lesson-card" id="ex-lesson-18">')
    close_marker = '\n\n</div><!-- /tab-exercises -->'
    j18 = s.index(close_marker, i18)
    s = s[:j18] + '\n\n' + accordion + s[j18:]

    # --- menu card (só prof): after the aula18 IN CLASS link ---
    if is_prof:
        link18 = '<a href="/professor/pricila-adamo-aula18.html?autostart=1"'
        li = s.index(link18)
        ci = s.index('\n    </a>\n', li) + len('\n    </a>\n')
        s = s[:ci] + menu_card + '\n' + s[ci:]

    # --- complementares l19 after the l18-youtube wrapper, before /tab-complementary ---
    yi = s.index('data-media="l18-youtube"')
    tc = s.index('</div><!-- /tab-complementary -->', yi)
    s = s[:tc] + comp + '\n\n' + s[tc:]

    # --- audioMap entries: right after 'var audioMap = {' (plain insert) ---
    open_tag = 'var audioMap = {\n'
    oi = s.index(open_tag) + len(open_tag)
    s = s[:oi] + amap_inject + '\n' + s[oi:]

    # --- totalLessons 18 -> 19 ---
    s = s.replace('var totalLessons=18;', 'var totalLessons=19;')

    assert s != orig, f'{path}: nada mudou'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  applied -> {os.path.relpath(path, ROOT)}')


apply(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
apply(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('done')
