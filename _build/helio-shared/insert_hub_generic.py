#!/usr/bin/env python3
"""Inserção SÓ ADITIVA de UMA aula N (12..16) nos hubs prof+aluno de helio-santana.
Sequencial: rode 12, depois 13, ... Cada N ancora no stamp(N-1)/aulaN-1/totalLessons N-1.
Uso: python3 insert_hub_generic.py N
NÃO toca aulas anteriores — só APPEND."""
import re, os, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
snip = open(os.path.join(ROOT, '_build', f'helio-santana-aula{N}', 'hub_snippets.html'), encoding='utf-8').read()

def section(start_marker, end_marker):
    a = snip.index(start_marker) + len(start_marker)
    b = snip.index(end_marker)
    return snip[a:b].strip('\n')

menu_card = section('c/ /aluno/) -->', '<!-- 2. STAMP')
stamp     = section('na stamps-row do header) -->', '<!-- 3. ACCORDION')
accordion = section('prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
compl     = section('inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
audio_blk = section('mesclar no audioMap do hub, prof E aluno) -->', '<!-- 5. Ajustar')
audio_lines = re.search(r'<script>(.*?)</script>', audio_blk, re.S).group(1).strip('\n')

KINDS = {'professor': f'public/professor/helio-santana.html',
         'aluno': f'public/aluno/helio-santana.html'}

for kind, path in KINDS.items():
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    n0 = len(t)

    # 1. MENU CARD -> só no PROFESSOR (aluno não tem aba IN CLASS)
    if kind == 'professor':
        prev_link = f'/professor/helio-santana-aula{N-1}.html?autostart=1'
        m = re.search(r'(<a href="' + re.escape(prev_link) + r'".*?</a>)', t, re.S)
        assert m, f'card aula{N-1} não encontrado ({kind})'
        block = m.group(1)
        assert t.count(block) == 1, f'card aula{N-1} ambíguo ({kind})'
        t = t.replace(block, block + '\n' + menu_card, 1)

    # 2. STAMP -> após stamp(N-1)
    m = re.search(r'(<div class="stamp" id="stamp' + str(N-1) + r'"[^>]*></div>)', t)
    assert m, f'âncora stamp{N-1} não encontrada ({kind})'
    pstamp = m.group(1)
    assert t.count(pstamp) == 1, f'stamp{N-1} ambíguo ({kind})'
    t = t.replace(pstamp, pstamp + '\n' + stamp, 1)

    # 3. ACCORDION -> antes do fechamento da tab-exercises
    acc_anchor = '</div><!-- /tab-exercises -->'
    assert t.count(acc_anchor) == 1, f'âncora accordion ({kind})'
    t = t.replace(acc_anchor, '\n' + accordion + '\n' + acc_anchor, 1)

    # 4. COMPLEMENTARES -> antes do fechamento da tab-complementary
    compl_anchor = '</div><!-- /tab-complementary -->'
    assert t.count(compl_anchor) == 1, f'âncora complementary ({kind})'
    t = t.replace(compl_anchor, '\n' + compl + '\n' + compl_anchor, 1)

    # 5. audioMap -> após 'var audioMap = {'
    am_anchor = 'var audioMap = {' if 'var audioMap = {' in t else 'var audioMap={'
    assert am_anchor in t, f'âncora audioMap ({kind})'
    t = t.replace(am_anchor, am_anchor + '\n' + audio_lines, 1)

    # 6. totalLessons (N-1) -> N
    t2 = t.replace(f'var totalLessons={N-1}', f'var totalLessons={N}')
    assert t2 != t, f'totalLessons não atualizado ({kind})'
    t = t2

    open(full, 'w', encoding='utf-8').write(t)
    print(f'OK {kind} aula{N}: +{len(t)-n0} bytes')
print(f'inserção aula{N} concluída')
