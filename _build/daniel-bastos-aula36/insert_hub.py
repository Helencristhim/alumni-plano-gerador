#!/usr/bin/env python3
"""Insercion SOLO ADITIVA de la aula 36 en los hubs prof y aluno de daniel-bastos (idempotente para este N: usar sobre el hub de la aula 35)."""
import re, os, sys, json

N, PREV = 36, 35
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
cfg = json.load(open(os.path.join(HERE, 'config.json'), encoding='utf-8'))


def section(start_marker, end_marker):
    a = snip.index(start_marker) + len(start_marker)
    b = snip.index(end_marker)
    return snip[a:b].strip('\n')


menu_card = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
stamp = section('inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
accordion = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
compl = section('inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
audio_blk = section('mesclar no audioMap do hub, prof E aluno) -->', '<!-- 5. Ajustar')
audio_lines = re.search(r'<script>(.*?)</script>', audio_blk, re.S).group(1).strip('\n')
# o snippet nao carrega as entradas extra_audio (chave entre colchetes)
for it in cfg['lesson'].get('extra_audio', []):
    if '"%s"' % it['key'] not in audio_lines:
        audio_lines += '\n  %s: "/audio/daniel-bastos/%s",' % (json.dumps(it['key'], ensure_ascii=False), it['file'])


def insert_after(text, anchor, payload, label):
    assert anchor in text, f'ANCORA no encontrada ({label}): {anchor[:60]!r}'
    assert text.count(anchor) == 1, f'ancora AMBIGUA ({label})'
    return text.replace(anchor, anchor + payload, 1)


KINDS = {'professor': 'public/professor/daniel-bastos.html', 'aluno': 'public/aluno/daniel-bastos.html'}
only = sys.argv[1] if len(sys.argv) > 1 else None
for kind, path in KINDS.items():
    if only and kind != only:
        continue
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    n0 = len(t)
    assert f'id="ex-lesson-{N}"' not in t, f'aula {N} ya esta en el hub ({kind}): restaurar el hub antes'
    if kind == 'professor':
        link = f'/professor/daniel-bastos-aula{PREV}.html?autostart=1'
        m = re.search(r'(<a href="' + re.escape(link) + r'".*?</a>)', t, re.S)
        assert m, f'card aula{PREV} no encontrado ({kind})'
        blk = m.group(1)
        assert t.count(blk) == 1
        t = t.replace(blk, blk + '\n' + menu_card, 1)
    m = re.search(r'<div class="stamp" id="stamp%d"[^>]*></div>' % PREV, t)
    assert m, 'stamp previo no encontrado'
    t = insert_after(t, m.group(0), '\n' + stamp, f'{kind} stamp')
    acc_anchor = '</div><!-- /tab-exercises -->'
    assert t.count(acc_anchor) == 1
    t = t.replace(acc_anchor, accordion + '\n\n' + acc_anchor, 1)
    compl_anchor = '</div><!-- /tab-complementary -->'
    assert compl_anchor in t
    t = t.replace(compl_anchor, '\n' + compl + '\n' + compl_anchor, 1)
    am_anchor = 'var audioMap = {'
    assert am_anchor in t
    t = t.replace(am_anchor, am_anchor + '\n' + audio_lines, 1)
    t2 = t.replace('var totalLessons=%d;' % PREV, 'var totalLessons=%d;' % N)
    assert t2 != t, 'totalLessons no actualizado'
    t = t2
    open(full, 'w', encoding='utf-8').write(t)
    print(f'OK {kind}: +{len(t)-n0} bytes')
print('insercion concluida')
