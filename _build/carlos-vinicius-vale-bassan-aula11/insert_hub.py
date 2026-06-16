#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inserção ADITIVA da aula 11 do Carlos nos hubs (prof + aluno).
Só ADICIONA: stamp11, accordion Pre-class (ex-lesson-11), card IN CLASS (só prof),
bloco Complementares (l11), entradas de audioMap, e totalLessons 10->11.
NÃO toca em nada das aulas 1-10. Cada âncora é validada (exatamente 1 ocorrência)."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'carlos-vinicius-vale-bassan'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

preclass = read(os.path.join(HERE, 'preclass.html')).strip()
complementary = read(os.path.join(HERE, 'complementary.html')).strip()

# audioMap entries (part 4 do hub_snippets), exatamente as linhas de entrada
snip = read(os.path.join(HERE, 'hub_snippets.html'))
amap_lines = [l for l in snip.splitlines() if re.match(r'\s*"[^"]+":\s*"/audio/' + SLUG + r'/.*\.mp3",\s*$', l)]
assert amap_lines, 'nenhuma entrada de audioMap encontrada no hub_snippets'
amap_block = '\n'.join('  ' + l.strip() for l in amap_lines)

STAMP11 = ('        <div class="stamp" id="stamp11" data-label="Integration" '
           "style=\"background-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80')\"></div>")

INCLASS_CARD = (
    '<a href="/professor/' + SLUG + '-aula11.html#slides" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">11</div>\n'
    '  <div><div style="font-weight:600;font-size:.95rem">Block 2 &#8212; Closing the Deal &amp; Integration</div><div style="font-size:.8rem;color:var(--text-dim)">From the signed contract to the 100-day integration plan &#8212; 27 slides</div></div>\n'
    '</a>\n')

def sub_once(s, anchor, repl, label):
    n = s.count(anchor)
    assert n == 1, f'{label}: âncora encontrada {n}x (esperado 1): {anchor[:60]!r}'
    return s.replace(anchor, repl, 1)

def integrate(path, is_prof):
    s = read(path)
    assert 'id="ex-lesson-11"' not in s, f'{path}: aula 11 já integrada'
    # 1. stamp11 após stamp10
    stamp10 = ('        <div class="stamp" id="stamp10" data-label="Deal Structure" '
               "style=\"background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80')\"></div>")
    s = sub_once(s, stamp10, stamp10 + '\n' + STAMP11, 'stamp')
    # 2. accordion antes do fim do Pre-class
    s = sub_once(s, '</div><!-- /tab-exercises -->',
                 '\n' + preclass + '\n\n</div><!-- /tab-exercises -->', 'preclass')
    # 3. card IN CLASS (só prof)
    if is_prof:
        s = sub_once(s, '</a>\n</div>\n</div><!-- /tab-inclass -->',
                     '</a>\n' + INCLASS_CARD + '</div>\n</div><!-- /tab-inclass -->', 'inclass')
    # 4. complementares antes do fim
    s = sub_once(s, '</div><!-- /tab-complementary -->',
                 '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 'complementary')
    # 5. totalLessons
    s = sub_once(s, '  var totalLessons=10;', '  var totalLessons=11;', 'totalLessons')
    # 6. audioMap entries
    s = sub_once(s, 'var audioMap = {', 'var audioMap = {\n' + amap_block, 'audioMap')
    write(path, s)
    print('  ok', os.path.relpath(path, ROOT))

integrate(os.path.join(ROOT, 'public', 'professor', SLUG + '.html'), True)
integrate(os.path.join(ROOT, 'public', 'aluno', SLUG + '.html'), False)
print('done')
