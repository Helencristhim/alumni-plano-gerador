#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 10 nos hubs prof+aluno da Andreia (aditivo).
Cada substituicao usa ancora unica + assert de contagem == 1 (seguranca).
Hubs passados nao sao tocados; so adiciona a aula nova."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = os.path.join(os.path.dirname(__file__), 'hub_snippets.html')
PROF = os.path.join(ROOT, 'public', 'professor', 'andreia-heins.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'andreia-heins.html')

snip = open(SNIP, encoding='utf-8').read()

def section(start_marker, end_marker):
    i = snip.index(start_marker)
    j = snip.index(end_marker, i)
    return snip[i + len(start_marker):j].strip('\n')

menu_card   = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->\n', '\n\n<!-- 2.')
stamp_html  = section('inserir na stamps-row do header) -->\n', '\n\n<!-- 3.')
accordion   = section('após o ex-lesson anterior, prof E aluno) -->\n', '\n\n<!-- 3b.')
complement  = section('inserir na tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4.')

# audioMap entries (linhas entre <script> e </script> da secao 4) + [order-l10]
amap_block = section('mesclar no audioMap do hub, prof E aluno) -->\n<script>\n', '\n</script>')
amap_lines = amap_block + '\n  "[order-l10]": "/audio/andreia-heins/a10_order_presentation.mp3",'

def repl(s, anchor, new, label):
    assert s.count(anchor) == 1, f'{label}: ancora encontrada {s.count(anchor)}x (esperado 1)'
    return s.replace(anchor, new)

# ---- anchors ----
A_STAMP = '<div class="stamp" id="stamp9" data-label="Inquiry" style="background-image:url(\'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=200&q=80\')"></div>'
A_MENU  = ('      <div><div style="font-weight:600;font-size:.95rem">Asking Smart Questions in Meetings</div>'
           '<div style="font-size:.8rem;color:var(--text-dim)">Question forms in every tense: leading the meeting Q&amp;A -- 28 slides</div></div>\n    </a>')
A_EXED  = '</div><!-- /tab-exercises -->'
A_COMP  = '</div><!-- /tab-complementary -->'
A_AMAP  = '  "[order-l9]": "/audio/andreia-heins/a9_order_questions.mp3",'
A_TOTAL = 'var totalLessons=9;'

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    s = repl(s, A_STAMP, A_STAMP + '\n' + stamp_html, 'stamp')
    if is_prof:
        s = repl(s, A_MENU, A_MENU + '\n' + menu_card, 'menu card')
    s = repl(s, A_EXED, accordion + '\n' + A_EXED, 'accordion')
    s = repl(s, A_COMP, complement + '\n' + A_COMP, 'complementary')
    s = repl(s, A_AMAP, A_AMAP + '\n' + amap_lines, 'audioMap')
    s = repl(s, A_TOTAL, 'var totalLessons=10;', 'totalLessons')
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)}')

print('== prof hub =='); patch(PROF, True)
print('== aluno hub =='); patch(ALUNO, False)
print('OK')
