#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os hub_snippets.html (saida oficial do build_from_model.py modo snippets)
nos hubs prof+aluno existentes, de forma ADITIVA. Idempotente-ish: aborta se o
stamp/card/accordion da aula ja existir. Nada de aula passada e tocado.

USO: python3 insert_snippets.py <slug> <N>   (rodar da raiz do repo)
"""
import re
import sys
import os

slug = sys.argv[1]
N = int(sys.argv[2])
ROOT = os.getcwd()
snip_path = f'_build/{slug}-aula{N}/hub_snippets.html'
snip = open(snip_path, encoding='utf-8').read()


def section(snip, start_marker, end_marker):
    i = snip.index(start_marker)
    i = snip.index('\n', i) + 1
    j = snip.index(end_marker)
    return snip[i:j].strip('\n')


# A secao "2. STAMP" so existe se o config tiver um stamp pra esta aula (id == N).
# Lições além do numero de stamps (ex: aula 6 num pacote de 5 stamps) nao a tem.
has_stamp_section = '<!-- 2. STAMP' in snip
card_end = '<!-- 2. STAMP' if has_stamp_section else '<!-- 3. ACCORDION'
card = section(snip, '<!-- 1. CARD', card_end)
stamp = section(snip, '<!-- 2. STAMP', '<!-- 3. ACCORDION') if has_stamp_section else ''
accordion = section(snip, '<!-- 3. ACCORDION', '<!-- 3b. COMPLEMENTARES')
comp = section(snip, '<!-- 3b. COMPLEMENTARES', '<!-- 4. ENTRADAS')
# audioMap entries: between <script> and </script> inside section 4
amap_block = section(snip, '<!-- 4. ENTRADAS', '<!-- 5. Ajustar')
amap_entries = amap_block.replace('<script>', '').replace('</script>', '').strip('\n')


def patch_hub(path, is_aluno):
    s = open(path, encoding='utf-8').read()
    assert f'id="ex-lesson-{N}"' not in s, f'{path}: ex-lesson-{N} ja existe — abortando'
    assert f'data-media="l{N}-' not in s, f'{path}: complementares l{N} ja existem — abortando'
    stamp_exists = f'id="stamp{N}"' in s  # header do hub "new" ja cria os 5 stamps

    # 1. CARD do menu IN CLASS: inserir ANTES do </div> que fecha a lista de cards.
    # A lista comeca em <div style="display:flex;flex-direction:column;gap:1rem"> dentro de #tab-inclass.
    # O hub do ALUNO NAO tem aba IN CLASS (so Pre-class + Complementares) -> pular o card.
    menu_marker = '<div style="display:flex;flex-direction:column;gap:1rem">'
    if menu_marker in s:
        this_card = card.replace('/professor/', '/aluno/') if is_aluno else card
        mi = s.index(menu_marker)
        close_idx = s.index('\n  </div>\n</div>', mi)
        s = s[:close_idx] + '\n' + this_card + s[close_idx:]

    # 2. STAMP: inserir ANTES do </div> que fecha a stamps-row (so se nao existir;
    # o hub "new" da aula 1 ja cria os 5 stamps no header)
    if stamp and not stamp_exists:
        sr = s.index('<div class="stamps-row">')
        sr_close = s.index('</div>', sr)
        s = s[:sr_close] + stamp + '\n' + s[sr_close:]

    # 3. ACCORDION Pre-class: inserir ANTES de </div><!-- /tab-exercises -->
    ex_close = s.index('</div><!-- /tab-exercises -->')
    s = s[:ex_close] + accordion + '\n' + s[ex_close:]

    # 3b. COMPLEMENTARES: inserir ANTES de </div><!-- /tab-complementary -->
    comp_close = s.index('</div><!-- /tab-complementary -->')
    s = s[:comp_close] + comp + '\n' + s[comp_close:]

    # 4. audioMap: inserir as entradas logo apos 'var audioMap = {'
    am = s.index('var audioMap = {')
    am_nl = s.index('\n', am) + 1
    s = s[:am_nl] + amap_entries + '\n' + s[am_nl:]

    # 5. totalLessons -> N (so aumenta)
    def bump(m):
        return f'var totalLessons={N}' if 'totalLessons=' in m.group(0) else m.group(0)
    s = re.sub(r'var totalLessons\s*=\s*\d+', f'var totalLessons={N}', s)
    # TOTAL_AULAS permanece (programa total, nao muda)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {path}')


patch_hub(f'public/professor/{slug}.html', is_aluno=False)
patch_hub(f'public/aluno/{slug}.html', is_aluno=True)
print('OK')
