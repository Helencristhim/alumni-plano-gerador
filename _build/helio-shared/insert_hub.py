#!/usr/bin/env python3
"""Insere a aula N nos hubs prof e aluno do Helio Santana -- SO ADITIVO.
Uso: python3 insert_hub.py N
Anchors por string unica. Falha alto se algo nao bater (nunca insere as cegas).
- card IN CLASS: so no hub PROF (aluno nao tem aba IN CLASS)
- stamp: so se o snippet trouxer (aulas 2-5 tem stamp; aula 6 nao)
"""
import sys, os

if len(sys.argv) != 2:
    print(__doc__); sys.exit(2)
N = int(sys.argv[1])
PREV = N - 1

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB_PROF = os.path.join(ROOT, '..', '..', 'public', 'professor', 'helio-santana.html')
HUB_ALUNO = os.path.join(ROOT, '..', '..', 'public', 'aluno', 'helio-santana.html')
SNIP = os.path.join(ROOT, '..', f'helio-santana-aula{N}', 'hub_snippets.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

snip = read(SNIP)

def section(label_start):
    i = snip.index(label_start)
    body_start = snip.index('\n', i) + 1
    end = snip.index('<!--', body_start)
    return snip[body_start:end].strip('\n')

card = section('<!-- 1. CARD')
has_stamp = '<!-- 2. STAMP' in snip
stamp = section('<!-- 2. STAMP') if has_stamp else None
accordion = section('<!-- 3. ACCORDION')
comp = section('<!-- 3b. COMPLEMENTARES')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip('\n')

def assert_once(hay, needle, ctx):
    n = hay.count(needle)
    assert n == 1, f'esperava 1 ocorrencia de {ctx!r}, achei {n}'

def patch_hub(path, is_prof):
    s = read(path)
    n0 = len(s)
    assert f'ex-lesson-{N}' not in s, f'aula {N} JA esta no hub {path} -- abortando (idempotencia)'

    # 1. STAMP -- NAO inserir: o hub (hub:new da aula 1) ja renderiza stamp1..5
    #    no header (passport badges decorativos). Inserir duplicaria.

    # 2. ACCORDION Pre-class -- antes do fechamento da aba exercises
    tab_end = '</div><!-- /tab-exercises -->'
    assert_once(s, tab_end, 'tab-exercises end')
    ins = s.index(tab_end)
    s = s[:ins] + accordion + '\n' + s[ins:]

    # 3. COMPLEMENTARES -- antes do fechamento da aba complementary
    comp_end = '</div><!-- /tab-complementary -->'
    assert_once(s, comp_end, 'tab-complementary end')
    ins = s.index(comp_end)
    s = s[:ins] + comp + '\n' + s[ins:]

    # 4. audioMap -- apos 'var audioMap = {'
    am_anchor = 'var audioMap = {'
    assert_once(s, am_anchor, 'var audioMap')
    idx = s.index(am_anchor) + len(am_anchor)
    s = s[:idx] + '\n' + am_inner + s[idx:]

    # 5. totalLessons PREV -> N
    tl = f'var totalLessons={PREV};'
    assert tl in s, f'nao achei {tl}'
    s = s.replace(tl, f'var totalLessons={N};')

    # 6 (so prof). IN CLASS card -- apos </a> do card da aula PREV
    if is_prof:
        card_anchor = f'/professor/helio-santana-aula{PREV}.html?autostart=1'
        assert_once(s, card_anchor, f'card aula{PREV}')
        a_end = s.index('</a>', s.index(card_anchor)) + len('</a>')
        s = s[:a_end] + '\n' + card + s[a_end:]

    assert f'ex-lesson-{N}' in s and f'l{N}-serie' in s, 'pos-condicao falhou (accordion/comp)'
    assert f'var totalLessons={N};' in s
    if is_prof:
        assert f'helio-santana-aula{N}.html?autostart=1' in s
    write(path, s)
    print(f'OK {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}: {n0} -> {len(s)} bytes (+{len(s)-n0})')

patch_hub(HUB_PROF, is_prof=True)
patch_hub(HUB_ALUNO, is_prof=False)
print(f'done aula {N}')
