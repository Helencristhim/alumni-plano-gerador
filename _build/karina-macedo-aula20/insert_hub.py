#!/usr/bin/env python3
"""Insere a aula 20 nos hubs prof e aluno da Karina -- SO ADITIVO.
Anchors por string unica. Falha alto se algo nao bater (nunca insere as cegas).
Pre-requisito: as aulas 17, 18 e 19 ja estao no hub (stamp19/ex-lesson-19/aula19)."""
import re, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB_PROF = os.path.join(ROOT, '..', '..', 'public', 'professor', 'karina-macedo.html')
HUB_ALUNO = os.path.join(ROOT, '..', '..', 'public', 'aluno', 'karina-macedo.html')
SNIP = os.path.join(ROOT, 'hub_snippets.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

snip = read(SNIP)

def section(label_start, label_end=None):
    i = snip.index(label_start)
    body_start = snip.index('\n', i) + 1
    if label_end:
        end = snip.index(label_end)
    else:
        end = snip.index('<!--', body_start)
    return snip[body_start:end].strip('\n')

card = section('<!-- 1. CARD')
stamp = section('<!-- 2. STAMP')
accordion = section('<!-- 3. ACCORDION')
comp = section('<!-- 3b. COMPLEMENTARES')
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip('\n')

def assert_once(hay, needle, ctx):
    n = hay.count(needle)
    assert n == 1, f'esperava 1 ocorrencia de {ctx!r}, achei {n}'

def insert_after(hay, anchor, payload, ctx):
    assert_once(hay, anchor, ctx)
    idx = hay.index(anchor) + len(anchor)
    return hay[:idx] + '\n' + payload + hay[idx:]

def patch_hub(path, is_prof):
    s = read(path)
    n0 = len(s)
    assert 'ex-lesson-20' not in s, 'aula 20 JA esta no hub -- abortando (idempotencia)'

    # 1. STAMP -- apos o stamp19
    stamp19 = '<div class="stamp" id="stamp19"'
    end19 = s.index('</div>', s.index(stamp19)) + len('</div>')
    s = s[:end19] + '\n' + stamp + s[end19:]

    # 2. ACCORDION Pre-class -- apos o fechamento do ex-lesson-19
    anchor19 = '<div class="lesson-card" id="ex-lesson-19">'
    p19 = s.index(anchor19)
    nxt = s.find('<div class="lesson-card"', p19 + len(anchor19))
    tab_end = s.find('</div><!-- /tab-exercises -->', p19)
    if nxt == -1 or (tab_end != -1 and tab_end < nxt):
        ins_at = tab_end
    else:
        ins_at = nxt
    assert ins_at != -1, 'nao achei ponto de insercao do accordion'
    s = s[:ins_at] + accordion + '\n' + s[ins_at:]

    # 3. COMPLEMENTARES -- apos o ultimo card l19 (l19-youtube wrapper)
    yt = '<div class="media-card-wrapper" data-media="l19-youtube">'
    pyt = s.index(yt)
    comp_tab_end = s.find('</div><!-- /tab-complementary -->', pyt)
    if comp_tab_end != -1:
        s = s[:comp_tab_end] + comp + '\n' + s[comp_tab_end:]
    else:
        m = re.search(re.escape(yt) + r'.*?</div>\s*</div>\s*</div>', s[pyt:], re.S)
        assert m, 'nao achei fim do wrapper l19-youtube'
        end = pyt + m.end()
        s = s[:end] + '\n' + comp + s[end:]

    # 4. audioMap -- apos 'var audioMap = {'
    s = insert_after(s, 'var audioMap = {', am_inner, 'var audioMap = {')

    # 5. totalLessons 19 -> 20
    assert 'var totalLessons=19' in s, 'nao achei var totalLessons=19'
    s = s.replace('var totalLessons=19', 'var totalLessons=20')

    # 6 (so prof). IN CLASS card -- apos o card da aula 19
    if is_prof:
        card_anchor = '/professor/karina-macedo-aula19.html?autostart=1'
        pc = s.index(card_anchor)
        a_end = s.index('</a>', pc) + len('</a>')
        s = s[:a_end] + '\n' + card + s[a_end:]

    assert 'ex-lesson-20' in s and 'stamp20' in s and 'l20-series' in s, 'pos-condicao falhou'
    assert 'var totalLessons=20' in s
    if is_prof:
        assert 'karina-macedo-aula20.html?autostart=1' in s
    write(path, s)
    print(f'OK {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}: {n0} -> {len(s)} bytes (+{len(s)-n0})')

patch_hub(HUB_PROF, is_prof=True)
patch_hub(HUB_ALUNO, is_prof=False)
print('done')
