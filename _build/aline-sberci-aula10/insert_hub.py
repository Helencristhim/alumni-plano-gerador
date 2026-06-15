#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 10 da Aline nos hubs prof+aluno (aditivo, idempotente)."""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()

# menu card (prof) — extrai da hub_snippets (seção 1)
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
menu_card = re.search(r'(<a href="/professor/aline-sberci-aula10\.html\?autostart=1".*?</a>)', snip, re.S).group(1)

stamp10 = '<div class="stamp" id="stamp10" data-label="Meetings" style="background-image:url(\'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80\')"></div>'
stamp9_re = re.compile(r'(<div class="stamp" id="stamp9"[^>]*></div>)')

# audioMap entries (seção 4 da hub_snippets)
amap_block = re.search(r'<!-- 4\. ENTRADAS de audioMap.*?-->\s*<script>\n(.*?)</script>', snip, re.S).group(1).rstrip('\n')


def close_index(s, open_idx):
    """índice do </div> que fecha a <div ...> que começa em open_idx."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[open_idx:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return open_idx + m.start()
    raise ValueError('div não fechada')


def patch(view):
    path = os.path.join(ROOT, 'public', view, 'aline-sberci.html')
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-10"' in s:
        print(f'  {view}: já tem aula 10 — pulando')
        return
    # 1. totalLessons
    s = re.sub(r'var totalLessons=9;', 'var totalLessons=10;', s)
    # 2. stamp10 após stamp9
    s = stamp9_re.sub(lambda m: m.group(1) + '\n        ' + stamp10, s, count=1)
    # 3. accordion antes do fim da tab-exercises
    s = s.replace('</div><!-- /tab-exercises -->',
                  preclass + '\n\n</div><!-- /tab-exercises -->', 1)
    # 4. complementary antes do fim da tab-complementary (depth match)
    oi = s.index('<div class="tab-content" id="tab-complementary">')
    ci = close_index(s, oi)
    s = s[:ci] + '\n' + complementary + '\n' + s[ci:]
    # 5. menu card (só prof — aluno não tem IN CLASS)
    if view == 'professor':
        anchor = '/professor/aline-sberci-aula9.html?autostart=1'
        ai = s.index(anchor)
        ae = s.index('</a>', ai) + len('</a>')
        s = s[:ae] + '\n' + menu_card + s[ae:]
    # 6. audioMap entries logo após abertura
    s = re.sub(r'(var audioMap = \{\n)', r'\1' + amap_block.replace('\\', r'\\') + '\n', s, count=1)
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  {view}: aula 10 inserida ({len(s)//1024} KB)')


for v in ('professor', 'aluno'):
    patch(v)
print('done')
