# -*- coding: utf-8 -*-
"""Insere os snippets da aula 8 nos hubs PROF e ALUNO da Simone (aditivo).
Adiciona o stamp8 (ainda nao existe no hub) e ajusta totalLessons para 8."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'simone-quiles-de-santana-marques'
AUDIO_BASE = f'/audio/{SLUG}/'
N = 8

accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().rstrip() + '\n'
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().rstrip() + '\n'

snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# audioMap entries (snippet section 4) + [order-l8]
m = re.search(r'4\. ENTRADAS.*?<script>\n(.*?)</script>', snip, re.S)
audio_lines = m.group(1).rstrip('\n')
audio_lines += f'\n  "[order-l8]": "{AUDIO_BASE}a8_order_sequence.mp3",'

# menu card (snippet section 1)
mc = re.search(r'1\. CARD.*?-->\n(.*?)\n\n<!-- 2\.', snip, re.S)
menu_card = mc.group(1).rstrip('\n')

# stamp8 (snippet section 2)
ms = re.search(r'2\. STAMP.*?-->\n(.*?)\n\n<!-- 3\.', snip, re.S)
stamp8 = ms.group(1).rstrip('\n')
assert 'id="stamp8"' in stamp8, 'stamp8 ausente no snippet (config tem stamp id 8?)'

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig_len = len(s)
    assert 'id="ex-lesson-8"' not in s, f'{path}: aula 8 ja inserida'
    assert 'id="stamp8"' not in s, f'{path}: stamp8 ja existe'

    # 1) audioMap entries
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + audio_lines, 1)

    # 2) accordion Pre-class antes do fim da tab-exercises
    marker_ex = '</div><!-- /tab-exercises -->'
    assert marker_ex in s, f'{path}: marker tab-exercises ausente'
    s = s.replace(marker_ex, accordion + marker_ex, 1)

    # 3) complementares antes do fim da tab-complementary
    marker_co = '</div><!-- /tab-complementary -->'
    assert marker_co in s, f'{path}: marker tab-complementary ausente'
    s = s.replace(marker_co, complementary + marker_co, 1)

    # 4) menu card IN CLASS (so prof)
    if is_prof:
        anchor = '\n  </div>\n</div>\n\n<!-- ========== TAB 4'
        assert anchor in s, f'{path}: anchor do menu IN CLASS ausente'
        s = s.replace(anchor, '\n' + menu_card + anchor, 1)

    # 5) stamp8 na stamps-row (apos stamp7)
    m7 = re.search(r'(<div class="stamp" id="stamp7"[^>]*></div>)', s)
    assert m7, f'{path}: stamp7 ausente na stamps-row'
    s = s.replace(m7.group(1), m7.group(1) + '\n' + stamp8, 1)

    # 6) totalLessons -> 8
    s = re.sub(r'totalLessons\s*=\s*\d+', 'totalLessons = 8', s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  {os.path.relpath(path, ROOT)}: {orig_len} -> {len(s)} bytes (+{len(s)-orig_len})')

patch(os.path.join(ROOT, 'public', 'professor', f'{SLUG}.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', f'{SLUG}.html'), False)
print('done')
