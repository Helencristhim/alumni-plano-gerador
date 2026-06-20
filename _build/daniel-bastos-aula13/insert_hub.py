#!/usr/bin/env python3
"""Inserção SÓ ADITIVA da aula 13 nos hubs prof e aluno de daniel-bastos.
Extrai as 5 seções do hub_snippets.html e as encaixa por âncora de string."""
import re, os, sys

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
audio_lines = re.search(r'<script>(.*?)</script>', audio_blk, re.S).group(1).strip('\n')

def insert_after(text, anchor, payload, label):
    assert anchor in text, f'ÂNCORA não encontrada ({label}): {anchor[:60]!r}'
    assert text.count(anchor) == 1, f'âncora AMBÍGUA ({label}): {anchor[:60]!r} aparece {text.count(anchor)}x'
    return text.replace(anchor, anchor + payload, 1)

KINDS = {'professor': 'public/professor/daniel-bastos.html',
         'aluno': 'public/aluno/daniel-bastos.html'}
only = sys.argv[1] if len(sys.argv) > 1 else None

for kind, path in KINDS.items():
    if only and kind != only:
        continue
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    n0 = len(t)

    # 1. MENU CARD -> só no PROFESSOR (aluno não tem aba IN CLASS / menu de aulas, REGRA 3)
    if kind == 'professor':
        aula12_link = '/professor/daniel-bastos-aula12.html?autostart=1'
        m = re.search(r'(<a href="' + re.escape(aula12_link) + r'".*?</a>)', t, re.S)
        assert m, f'card aula12 não encontrado ({kind})'
        a12_block = m.group(1)
        assert t.count(a12_block) == 1
        t = t.replace(a12_block, a12_block + '\n' + menu_card, 1)

    # 2. STAMP -> após stamp12
    stamp12 = '<div class="stamp" id="stamp12" data-label="Hacer Presentaciones" style="background-image:url(\'https://images.unsplash.com/photo-1531058020387-3be344556be6?w=200&q=80\')"></div>'
    t = insert_after(t, stamp12, '\n' + stamp, f'{kind} stamp')

    # 3. ACCORDION -> antes do fechamento da tab-exercises
    acc_anchor = '</div>\n</div>\n</div><!-- /tab-exercises -->'
    assert acc_anchor in t, f'âncora accordion não encontrada ({kind})'
    t = t.replace(acc_anchor, '</div>\n</div>\n\n' + accordion + '\n</div><!-- /tab-exercises -->', 1)

    # 4. COMPLEMENTARES -> antes do fechamento da tab-complementary
    compl_anchor = '</div><!-- /tab-complementary -->'
    assert compl_anchor in t, f'âncora complementary não encontrada ({kind})'
    t = t.replace(compl_anchor, '\n' + compl + '\n' + compl_anchor, 1)

    # 5. audioMap -> inserir as entradas logo após 'var audioMap = {'
    am_anchor = 'var audioMap = {'
    assert am_anchor in t, f'âncora audioMap não encontrada ({kind})'
    t = t.replace(am_anchor, am_anchor + '\n' + audio_lines, 1)

    # 6. totalLessons 12 -> 13 (TOTAL_AULAS fica 48)
    t2 = t.replace('var totalLessons=12;', 'var totalLessons=13;')
    assert t2 != t, f'totalLessons não atualizado ({kind})'
    t = t2

    open(full, 'w', encoding='utf-8').write(t)
    print(f'OK {kind}: +{len(t)-n0} bytes')

print('inserção concluída')
