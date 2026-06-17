#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inserção ADITIVA da aula 15 nos hubs prof + aluno do Rafael Pelizaro.
Nunca remove nada; só insere após âncoras únicas da aula 14. Idempotente: aborta
se a aula 15 já estiver presente."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# 3. accordion Pre-class: do <div class="lesson-card" id="ex-lesson-15"> até antes de 3b
ACCORDION = SNIP[SNIP.index('<div class="lesson-card" id="ex-lesson-15">'):SNIP.index('<!-- 3b.')].rstrip('\n')

# 3b. complementares
COMP = SNIP[SNIP.index('<h4', SNIP.index('<!-- 3b.')):SNIP.index('<!-- 4.')].rstrip('\n')

# 4. audioMap entries (linhas "...": "...",)
amap_block = SNIP[SNIP.index('<script>', SNIP.index('<!-- 4.'))+len('<script>'):SNIP.index('</script>', SNIP.index('<!-- 4.'))]
AUDIO_ENTRIES = amap_block.strip('\n')

STAMP = '<div class="stamp" id="stamp15" data-label="Interview" style="background-image:url(\'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=200&q=80\')"></div>'

def menu_card(base):
    return (
        '    <a href="/' + base + '/rafael-pelizaro-aula15.html#slides" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">15</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">The Job Interview -- Telling Your Story</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect + past simple -- 28 slides</div></div>\n'
        '    </a>')

def patch(path, base, has_inclass, preclass_end_anchor):
    s = open(path, encoding='utf-8').read()
    assert 'ex-lesson-15' not in s, f'{path}: aula 15 JÁ presente — abortando (idempotência)'

    # 1) MENU CARD IN CLASS (só prof — aluno não tem aba IN CLASS, REGRA 3)
    if has_inclass:
        a14_card_anchor = '<a href="/' + base + '/rafael-pelizaro-aula14.html#slides" target="_blank"'
        assert a14_card_anchor in s, f'{path}: card menu aula14 não encontrado'
        ci = s.index(a14_card_anchor)
        close = s.index('</a>', ci) + len('</a>')
        s = s[:close] + '\n' + menu_card(base) + s[close:]

    # 2) STAMP: após o fechamento </div> do stamp14
    assert 'id="stamp14"' in s, f'{path}: stamp14 não encontrado'
    stamp14_full_end = s.index('</div>', s.index('id="stamp14"')) + len('</div>')
    s = s[:stamp14_full_end] + '\n' + STAMP + s[stamp14_full_end:]

    # 3) ACCORDION Pre-class: antes do marcador que fecha a aba Pre-class
    assert preclass_end_anchor in s, f'{path}: âncora fim Pre-class não encontrada'
    s = s.replace(preclass_end_anchor, ACCORDION + '\n\n' + preclass_end_anchor, 1)

    # 3b) COMPLEMENTARES: antes do fechamento da tab-complementary
    s = s.replace('</div><!-- /tab-complementary -->',
                  COMP + '\n</div><!-- /tab-complementary -->', 1)

    # 4) audioMap: inserir entradas antes do fechamento "\n};" do primeiro audioMap
    am_start = s.index('var audioMap = {')
    am_end = s.index('\n};', am_start)
    s = s[:am_end] + '\n' + AUDIO_ENTRIES + s[am_end:]

    # 5) totalLessons 14 -> 15
    s2 = re.sub(r'var totalLessons\s*=\s*14', 'var totalLessons=15', s)
    assert s2 != s, f'{path}: totalLessons=14 não encontrado'
    s = s2

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)}')

patch(os.path.join(ROOT, 'public', 'professor', 'rafael-pelizaro.html'), 'professor',
      has_inclass=True, preclass_end_anchor='<!-- ========== TAB 3: IN CLASS ========== -->')
patch(os.path.join(ROOT, 'public', 'aluno', 'rafael-pelizaro.html'), 'aluno',
      has_inclass=False, preclass_end_anchor='<!-- ========== TAB 2: COMPLEMENTARES ========== -->')
print('hub patch OK (aditivo)')
