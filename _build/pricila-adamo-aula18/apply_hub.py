#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica ADITIVAMENTE os snippets da aula 18 aos hubs prof+aluno (REGRA 20 — hub
existente, só adiciona). Lê hub_snippets.html gerado pelo builder e insere:
stamp18, ex-lesson-18, complementares l18, audioMap, totalLessons 17->18, e o
card do menu IN CLASS (só prof). Aulas 1-17 ficam byte-idênticas exceto as adições."""
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
# inject [order-l18] manually (extract_phrases skips '[' prefix)
amap_lines.append('  "[order-l18]": "/audio/pricila-adamo/pc18_order_misunderstanding.mp3",')
amap_inject = '\n'.join(amap_lines)


def apply(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s

    # --- stamp18 after stamp17 line ---
    m = re.search(r'(<div class="stamp" id="stamp17"[^\n]*</div>)\n', s)
    assert m, f'{path}: stamp17 não achado'
    indent = re.match(r'\s*', s[s.rfind('\n', 0, m.start())+1:m.start()]).group()
    s = s[:m.end()] + indent + stamp + '\n' + s[m.end():]

    # --- ex-lesson-18 after the FULL ex-lesson-17 card ---
    i17 = s.index('<div class="lesson-card" id="ex-lesson-17">')
    close_marker = '\n\n</div><!-- /tab-exercises -->'
    j17 = s.index(close_marker, i17)
    s = s[:j17] + '\n\n' + accordion + s[j17:]

    # --- menu card (só prof): after the aula17 IN CLASS link ---
    if is_prof:
        link17 = '<a href="/professor/pricila-adamo-aula17.html?autostart=1"'
        li = s.index(link17)
        ci = s.index('\n    </a>\n', li) + len('\n    </a>\n')
        s = s[:ci] + menu_card + '\n' + s[ci:]

    # --- complementares l18 after the l17-youtube wrapper, before /tab-complementary ---
    yi = s.index('data-media="l17-youtube"')
    tc = s.index('</div><!-- /tab-complementary -->', yi)
    s = s[:tc] + comp + '\n\n' + s[tc:]

    # --- audioMap entries: right after 'var audioMap = {' (plain insert) ---
    open_tag = 'var audioMap = {\n'
    oi = s.index(open_tag) + len(open_tag)
    s = s[:oi] + amap_inject + '\n' + s[oi:]

    # --- totalLessons 17 -> 18 ---
    s = s.replace('var totalLessons=17;', 'var totalLessons=18;')

    assert s != orig, f'{path}: nada mudou'
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  applied -> {os.path.relpath(path, ROOT)}')


apply(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
apply(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('done')
