#!/usr/bin/env python3
"""Insere a aula 14 nos hubs prof e aluno da Karina — SÓ ADITIVO.
Anchors por string única. Falha alto se algo não bater (nunca insere às cegas)."""
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
    """Extrai bloco entre o comentário label_start e o próximo comentário <!-- (ou label_end)."""
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
# audioMap entries (entre <script> e </script> do snippet)
am_block = snip[snip.index('<!-- 4. ENTRADAS'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip('\n')

def assert_once(hay, needle, ctx):
    n = hay.count(needle)
    assert n == 1, f'esperava 1 ocorrência de {ctx!r}, achei {n}'

def insert_after(hay, anchor, payload, ctx):
    assert_once(hay, anchor, ctx)
    idx = hay.index(anchor) + len(anchor)
    return hay[:idx] + '\n' + payload + hay[idx:]

def patch_hub(path, is_prof):
    s = read(path)
    n0 = len(s)
    assert 'ex-lesson-14' not in s, 'aula 14 JÁ está no hub — abortando (idempotência)'

    # 1. STAMP — após o stamp13
    stamp13 = '<div class="stamp" id="stamp13"'
    end13 = s.index('</div>', s.index(stamp13)) + len('</div>')
    s = s[:end13] + '\n' + stamp + s[end13:]

    # 2. ACCORDION Pre-class — após o fechamento do ex-lesson-13
    # ex-lesson-13 é um lesson-card; fecha no </div> que casa. Inserimos antes do </div> que encerra a lista,
    # logo após o card 13. Achamos o início do card 13 e o próximo lesson-card OU o fim do container.
    anchor13 = '<div class="lesson-card" id="ex-lesson-13">'
    p13 = s.index(anchor13)
    # fim do card 13 = início do próximo 'lesson-card' depois dele, OU marcador de fim da aba.
    nxt = s.find('<div class="lesson-card"', p13 + len(anchor13))
    tab_end = s.find('</div><!-- /tab-exercises -->', p13)
    if nxt == -1 or (tab_end != -1 and tab_end < nxt):
        ins_at = tab_end
    else:
        ins_at = nxt
    assert ins_at != -1, 'não achei ponto de inserção do accordion'
    s = s[:ins_at] + accordion + '\n' + s[ins_at:]

    # 3. COMPLEMENTARES — após o último card l13 (l13-youtube wrapper)
    yt = '<div class="media-card-wrapper" data-media="l13-youtube">'
    pyt = s.index(yt)
    yt_end = s.index('</div>\n</div>', pyt)
    # fechar os 2 divs do wrapper: media-card + media-card-wrapper
    yt_close = s.index('</div>', s.index('</div>', s.index('class="media-info"', pyt)))
    # mais robusto: inserir antes do fechamento da tab-complementary
    comp_tab_end = s.find('</div><!-- /tab-complementary -->', pyt)
    if comp_tab_end != -1:
        s = s[:comp_tab_end] + comp + '\n' + s[comp_tab_end:]
    else:
        # fallback: após o wrapper l13-youtube inteiro (3 níveis de div)
        m = re.search(re.escape(yt) + r'.*?</div>\s*</div>\s*</div>', s[pyt:], re.S)
        assert m, 'não achei fim do wrapper l13-youtube'
        end = pyt + m.end()
        s = s[:end] + '\n' + comp + s[end:]

    # 4. audioMap — após 'var audioMap = {'
    s = insert_after(s, 'var audioMap = {', am_inner, 'var audioMap = {')

    # 5. totalLessons 13 -> 14
    assert 'var totalLessons=13' in s, 'não achei var totalLessons=13'
    s = s.replace('var totalLessons=13', 'var totalLessons=14')

    # 6 (só prof). IN CLASS card — após o card da aula 13
    if is_prof:
        card_anchor = '/professor/karina-macedo-aula13.html?autostart=1'
        pc = s.index(card_anchor)
        # fim do <a> da aula 13
        a_end = s.index('</a>', pc) + len('</a>')
        s = s[:a_end] + '\n' + card + s[a_end:]

    assert 'ex-lesson-14' in s and 'stamp14' in s and 'l14-series' in s, 'pós-condição falhou'
    assert 'var totalLessons=14' in s
    if is_prof:
        assert 'karina-macedo-aula14.html?autostart=1' in s
    write(path, s)
    print(f'OK {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}: {n0} -> {len(s)} bytes (+{len(s)-n0})')

patch_hub(HUB_PROF, is_prof=True)
patch_hub(HUB_ALUNO, is_prof=False)
print('done')
