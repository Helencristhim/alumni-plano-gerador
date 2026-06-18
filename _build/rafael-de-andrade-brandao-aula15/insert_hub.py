#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA da aula 15 nos hubs prof+aluno (passo 7 do pipeline do modelo).
NAO reconstroi o hub: so insere stamp15, accordion ex-lesson-15, card IN CLASS,
bloco de complementares l15- e entradas de audioMap (pc15_ + [order-l15]); seta totalLessons=15.
Aulas 1..14 ficam intactas.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'rafael-de-andrade-brandao'

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()
snippet = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# audioMap: so as entradas pc15_ (frases do hub/preclass) + [order-l15]
pc_lines = [ln for ln in snippet.splitlines() if 'pc15_' in ln and ln.strip().startswith('"')]
order_line = '  "[order-l15]": "/audio/%s/a15_order_qa.mp3",' % SLUG
audio_block = '\n'.join([order_line] + [ln.rstrip() for ln in pc_lines])

STAMP = ('<div class="stamp" id="stamp15" data-label="Q&amp;A" '
         'style="background-image:url(\'https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=200&q=80\')"></div>')

def card(view):
    return (
        '<a href="/%s/%s-aula15.html?autostart=1"  style="display:flex;align-items:center;gap:1rem;padding:1.2rem;'
        'background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);'
        'border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit"  '
        'onmouseover="this.style.borderColor=\'var(--accent)\'" '
        'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;'
        'align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">15</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Handling Questions -- The Q&amp;A</div>'
        '<div style="font-size:.8rem;color:var(--text-dim)">Boardroom Q&amp;A Simulation -- 27 slides</div></div>\n'
        '    </a>' % (view, SLUG))

def patch(path, view):
    s = open(path, encoding='utf-8').read()
    assert 'id="stamp15"' not in s, 'aula 15 ja inserida em ' + path
    # 1. stamp15 apos stamp14
    stamp14 = ('<div class="stamp" id="stamp14" data-label="Trends" '
               'style="background-image:url(\'https://images.unsplash.com/photo-1543286386-713bdd548da4?w=200&q=80\')"></div>')
    assert stamp14 in s, 'stamp14 nao encontrado em ' + path
    s = s.replace(stamp14, stamp14 + '\n' + STAMP, 1)
    # 2. accordion Pre-class antes de <!-- /tab-exercises -->
    s = s.replace('<!-- /tab-exercises -->', preclass + '\n<!-- /tab-exercises -->', 1)
    # 3. card IN CLASS apos o card da aula14 (so o hub do professor tem aba IN CLASS;
    #    o aluno tem 2 abas, sem IN CLASS — REGRA 3)
    aula14_card_end = ('<div style="font-size:.8rem;color:var(--text-dim)">Sales Trend Walkthrough -- 27 slides</div></div>\n'
                       '    </a>')
    if aula14_card_end in s:
        s = s.replace(aula14_card_end, aula14_card_end + '\n    ' + card(view), 1)
    # 4. complementares antes do </div><!-- /tab-complementary -->
    s = s.replace('</div><!-- /tab-complementary -->', complementary + '\n</div><!-- /tab-complementary -->', 1)
    # 5. audioMap
    s = s.replace('var audioMap = {', 'var audioMap = {\n' + audio_block, 1)
    # 6. totalLessons
    s = re.sub(r'var totalLessons = \d+', 'var totalLessons = 15', s)
    open(path, 'w', encoding='utf-8').write(s)
    print('patched', os.path.relpath(path, ROOT))

targets = sys.argv[1:] or ['professor', 'aluno']
for view in targets:
    patch(os.path.join(ROOT, 'public', view, SLUG + '.html'), view)
