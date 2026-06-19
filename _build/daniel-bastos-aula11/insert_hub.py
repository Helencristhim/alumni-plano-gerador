#!/usr/bin/env python3
"""Inserção SÓ ADITIVA da aula 11 nos hubs prof e aluno de daniel-bastos.
Extrai as 5 seções do hub_snippets.html e as encaixa por âncora de string."""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

def section(start_marker, end_marker):
    a = snip.index(start_marker) + len(start_marker)
    b = snip.index(end_marker)
    return snip[a:b].strip('\n')

menu_card  = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
stamp      = section('inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
accordion  = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
compl      = section('inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
audio_blk  = section('mesclar no audioMap do hub, prof E aluno) -->', '<!-- 5. Ajustar')
# audio_blk vem com <script>...</script> em volta; extrair só as linhas de entrada
audio_lines = re.search(r'<script>(.*?)</script>', audio_blk, re.S).group(1).strip('\n')

def insert_after(text, anchor, payload, label):
    assert anchor in text, f'ÂNCORA não encontrada ({label}): {anchor[:60]!r}'
    assert text.count(anchor) == 1, f'âncora AMBÍGUA ({label}): {anchor[:60]!r} aparece {text.count(anchor)}x'
    return text.replace(anchor, anchor + payload, 1)

import sys as _sys
KINDS = {'professor': 'public/professor/daniel-bastos.html',
         'aluno': 'public/aluno/daniel-bastos.html'}
only = _sys.argv[1] if len(_sys.argv) > 1 else None

for kind, path in KINDS.items():
    if only and kind != only:
        continue
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    n0 = len(t)

    # 1. MENU CARD -> só no PROFESSOR (aluno não tem aba IN CLASS / menu de aulas, REGRA 3)
    if kind == 'professor':
        aula10_link = '/professor/daniel-bastos-aula10.html?autostart=1'
        m = re.search(r'(<a href="' + re.escape(aula10_link) + r'".*?</a>)', t, re.S)
        assert m, f'card aula10 não encontrado ({kind})'
        a10_block = m.group(1)
        assert t.count(a10_block) == 1
        t = t.replace(a10_block, a10_block + '\n' + menu_card, 1)

    # 2. STAMP -> após stamp10
    stamp10 = '<div class="stamp" id="stamp10" data-label="Reuniones Que Importan" style="background-image:url(\'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80\')"></div>'
    t = insert_after(t, stamp10, '\n' + stamp, f'{kind} stamp')

    # 3. ACCORDION -> após o fim do accordion ex-lesson-10. Âncora = bloco de fechamento único
    #    do tab-exercises, que vem logo após o ex-lesson-10. Inserir ANTES do fechamento da tab.
    acc_anchor = '</div>\n</div>\n</div><!-- /tab-exercises -->'
    assert acc_anchor in t, f'âncora accordion não encontrada ({kind})'
    t = t.replace(acc_anchor, '</div>\n</div>\n\n' + accordion + '\n</div><!-- /tab-exercises -->', 1)

    # 4. COMPLEMENTARES -> após o bloco l10-youtube, antes do fechamento da tab
    compl_anchor = '</div><!-- /tab-complementary -->'
    assert compl_anchor in t, f'âncora complementary não encontrada ({kind})'
    t = t.replace(compl_anchor, '\n' + compl + '\n' + compl_anchor, 1)

    # 5. audioMap -> inserir as entradas logo após 'var audioMap = {'
    am_anchor = 'var audioMap = {'
    assert am_anchor in t, f'âncora audioMap não encontrada ({kind})'
    t = t.replace(am_anchor, am_anchor + '\n' + audio_lines, 1)

    # 6. totalLessons 10 -> 11 (TOTAL_AULAS fica 48)
    t2 = t.replace('var totalLessons=10;', 'var totalLessons=11;')
    assert t2 != t, f'totalLessons não atualizado ({kind})'
    t = t2

    open(full, 'w', encoding='utf-8').write(t)
    print(f'OK {kind}: +{len(t)-n0} bytes')

print('inserção concluída')
