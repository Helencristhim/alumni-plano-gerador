#!/usr/bin/env python3
"""Inserção SÓ ADITIVA da aula 7 nos hubs prof e aluno de helio-santana.
Extrai as 5 seções do hub_snippets.html e as encaixa por âncora de string.
NÃO toca nas aulas 1-6 — só APPEND."""
import re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

def section(start_marker, end_marker):
    a = snip.index(start_marker) + len(start_marker)
    b = snip.index(end_marker)
    return snip[a:b].strip('\n')

menu_card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
stamp     = section('inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
accordion = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
compl     = section('inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
audio_blk = section('mesclar no audioMap do hub, prof E aluno) -->', '<!-- 5. Ajustar')
audio_lines = re.search(r'<script>(.*?)</script>', audio_blk, re.S).group(1).strip('\n')

KINDS = {'professor': 'public/professor/helio-santana.html',
         'aluno': 'public/aluno/helio-santana.html'}
only = sys.argv[1] if len(sys.argv) > 1 else None

for kind, path in KINDS.items():
    if only and kind != only:
        continue
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    n0 = len(t)

    # 1. MENU CARD -> só no PROFESSOR (aluno não tem aba IN CLASS / menu de aulas, REGRA 3)
    if kind == 'professor':
        aula6_link = '/professor/helio-santana-aula6.html?autostart=1'
        m = re.search(r'(<a href="' + re.escape(aula6_link) + r'".*?</a>)', t, re.S)
        assert m, f'card aula6 não encontrado ({kind})'
        a6_block = m.group(1)
        assert t.count(a6_block) == 1, f'card aula6 ambíguo ({kind})'
        t = t.replace(a6_block, a6_block + '\n' + menu_card, 1)

    # 2. STAMP -> após stamp6
    stamp6 = '<div class="stamp" id="stamp6" data-label="El Acuerdo Final" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>'
    assert stamp6 in t, f'âncora stamp6 não encontrada ({kind})'
    assert t.count(stamp6) == 1, f'stamp6 ambíguo ({kind})'
    t = t.replace(stamp6, stamp6 + '\n' + stamp, 1)

    # 3. ACCORDION -> antes do fechamento da tab-exercises (após o ex-lesson-6)
    acc_anchor = '</div><!-- /tab-exercises -->'
    assert acc_anchor in t, f'âncora accordion não encontrada ({kind})'
    assert t.count(acc_anchor) == 1, f'âncora accordion ambígua ({kind})'
    t = t.replace(acc_anchor, '\n' + accordion + '\n' + acc_anchor, 1)

    # 4. COMPLEMENTARES -> antes do fechamento da tab-complementary
    compl_anchor = '</div><!-- /tab-complementary -->'
    assert compl_anchor in t, f'âncora complementary não encontrada ({kind})'
    assert t.count(compl_anchor) == 1, f'âncora complementary ambígua ({kind})'
    t = t.replace(compl_anchor, '\n' + compl + '\n' + compl_anchor, 1)

    # 5. audioMap -> inserir as entradas logo após 'var audioMap = {'
    am_anchor = 'var audioMap = {'
    assert am_anchor in t, f'âncora audioMap não encontrada ({kind})'
    t = t.replace(am_anchor, am_anchor + '\n' + audio_lines, 1)

    # 6. totalLessons 6 -> 7 (TOTAL_AULAS fica 50)
    t2 = t.replace('var totalLessons=6', 'var totalLessons=7')
    assert t2 != t, f'totalLessons não atualizado ({kind})'
    t = t2

    open(full, 'w', encoding='utf-8').write(t)
    print(f'OK {kind}: +{len(t)-n0} bytes')

print('inserção concluída')
