#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere ADITIVAMENTE os snippets de UMA aula (build_from_model.py modo snippets)
nos hubs monoliticos de fernando-varela (prof E aluno). NAO toca aulas anteriores.

Adiciona: card IN CLASS (so prof), accordion Pre-class (prof+aluno), bloco
Complementares (prof+aluno), entradas de audioMap (prof+aluno), STAMP do header
(prof+aluno) e ajusta var totalLessons {N-1}->{N}.

USO: python3 _build/_fernando_insert_hub.py N
"""
import os, re, sys

N = int(sys.argv[1])
PREV = N - 1
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SNIP = open(os.path.join(HERE, f'fernando-varela-aula{N}', 'hub_snippets.html'), encoding='utf-8').read()

# stamp header (label + imagem) por aula
STAMPS = {
    7:  ("Project Updates",     "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=200&q=80"),
    8:  ("Future Plans",        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=200&q=80"),
    9:  ("Professional Emails", "https://images.unsplash.com/photo-1526554850534-7c78330d5f90?w=200&q=80"),
    10: ("On the Call",         "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=200&q=80"),
    11: ("On the Global Stage", "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=200&q=80"),
}


def between(s, a, b):
    i = s.index(a) + len(a)
    j = s.index(b, i)
    return s[i:j].strip()


# menu card (so prof)
m = re.search(r'(<a href="/professor/fernando-varela-aula%d\.html\?autostart=1".*?</a>)' % N, SNIP, re.S)
card_prof = m.group(1)

accordion = between(SNIP, '(inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
complementary = between(SNIP, '(inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
amap_inner = between(SNIP, '<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>', '</script>')
amap_block = '\n'.join(l for l in amap_inner.splitlines() if l.strip())

label, img = STAMPS[N]
stamp_html = f'<div class="stamp" id="stamp{N}" data-label="{label}" style="background-image:url(\'{img}\')"></div>'


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    edits = 0
    # 1. audioMap (prof+aluno)
    assert s.count('var audioMap = {') == 1, f'{path}: audioMap anchor'
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + amap_block, 1); edits += 1
    # 2. accordion Pre-class (prof+aluno)
    assert s.count('</div><!-- /tab-exercises -->') == 1, f'{path}: tab-exercises anchor'
    s = s.replace('</div><!-- /tab-exercises -->', '\n' + accordion + '\n\n</div><!-- /tab-exercises -->', 1); edits += 1
    # 3. complementares (prof+aluno)
    assert s.count('</div><!-- /tab-complementary -->') == 1, f'{path}: tab-complementary anchor'
    s = s.replace('</div><!-- /tab-complementary -->', '\n' + complementary + '\n\n</div><!-- /tab-complementary -->', 1); edits += 1
    # 4. totalLessons {PREV}->{N}
    assert f'var totalLessons={PREV}' in s, f'{path}: totalLessons={PREV} nao encontrado'
    s = s.replace(f'var totalLessons={PREV}', f'var totalLessons={N}', 1); edits += 1
    # 5. stamp do header (prof+aluno) — apos stamp{PREV}
    sm = re.search(r'<div class="stamp" id="stamp%d"[^>]*></div>' % PREV, s)
    assert sm, f'{path}: stamp{PREV} anchor'
    pos = sm.end()
    s = s[:pos] + '\n' + stamp_html + s[pos:]; edits += 1
    # 6. menu card (so prof) — apos o </a> da card da aula anterior
    if is_prof:
        anchor_href = f'/professor/fernando-varela-aula{PREV}.html?autostart=1'
        idx = s.index(anchor_href)
        close = s.index('</a>', idx) + len('</a>')
        s = s[:close] + '\n' + card_prof + s[close:]; edits += 1
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} ({edits} edicoes, +{(len(s)-len(orig))//1024} KB)')


patch(os.path.join(ROOT, 'public', 'professor', 'fernando-varela.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'fernando-varela.html'), False)
print(f'aula {N}: hubs atualizados (aditivo).')
