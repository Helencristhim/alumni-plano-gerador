#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva o shell da anatomia `story-quest` DO ARTEFATO, por script.

POR QUE POR SCRIPT, E NAO A MAO
-------------------------------
O artefato (_build/model/artefatos/dante-kids-professor-view.html) e a
ESPECIFICACAO da interface: dele se COPIA, classe por classe (ver o README da
pasta e a licao de 11/08/2026, quando o porte a mao renomeou cada peca e o
GATE 20 passou a comparar a copia consigo mesma). Um script torna a derivacao
AUDITAVEL: qualquer pessoa roda de novo e ve que o shell e o artefato menos o
que esta declarado aqui embaixo — nada foi reescrito no caminho.

O QUE O SHELL E: o artefato com a AULA 2 fora (o molde carrega UMA aula de
exemplo, como o da guided-discovery), com os literais do MODELO no lugar dos do
Dante (e o base_swaps do builder que troca por aluno) e com as camadas de
producao que uma pagina estatica do claude.ai nao tem.

    python3 _build/model/extrai_shell_story_quest.py [--check]

--check nao escreve: so confere que o shell no disco e igual ao que sairia hoje.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(RAIZ)
ARTEFATO = os.path.join(RAIZ, '_build', 'model', 'artefatos',
                        'dante-kids-professor-view.html')
SHELL = os.path.join(RAIZ, '_build', 'model', 'shells', 'story-quest.html')

# A paleta do artefato e a do Bento. O shell fala a paleta do MODELO porque o
# base_swaps() troca ESSES literais por aluno — mesma solucao do --mint no
# guided-discovery (artefatos/README.md). Nenhuma regra de CSS e editada: so o
# valor dentro dela.
PALETA = [
    ('#1E9E5F', '#BE123C'), ('#1e9e5f', '#be123c'),   # accent
    ('#3FD489', '#F43F5E'), ('#3fd489', '#f43f5e'),   # accent-light
    ('rgba(30,158,95', 'rgba(190,18,60'),
    ('rgba(30, 158, 95', 'rgba(190, 18, 60'),
]

# Nome e slug: o shell e do MODELO, e o builder troca por aluno.
NOMES = [
    ('dante-blecker-gregory', 'helen-mendes'),
    ('Dante Blecker Gregory', 'Helen Mendes'),
    ('Dante', 'Helen'),
    ('DANTE', 'HELEN'),
]


def fecha_tag(s, i, tag):
    """Indice logo APOS o fechamento da tag aberta em i. Por BALANCO, nunca pelo
    primeiro </div> — o primeiro fecha um filho."""
    depth = 0
    for m in re.finditer(r'<' + tag + r'\b|</' + tag + r'\s*>', s[i:]):
        depth += 1 if not m.group(0).startswith('</') else -1
        if depth == 0:
            return i + m.end()
    raise SystemExit(f'tag <{tag}> aberta em {i} nao fecha')


def remove(s, abertura_rx, tag, quantos=None):
    """Remove elementos inteiros cuja tag de abertura casa a regex."""
    n = 0
    while True:
        m = re.search(abertura_rx, s)
        if not m:
            break
        s = s[:m.start()] + s[fecha_tag(s, m.start(), tag):]
        n += 1
        if quantos and n >= quantos:
            break
    return s, n


def deriva():
    with open(ARTEFATO, encoding='utf-8') as fh:
        s = fh.read()
    rel = {}

    # 1. FORA A AULA 2 — o molde carrega UMA aula de exemplo.
    for nome, rx, tag in [
        ('slides',        r'<div class="slide[^"]*"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('phase-bar',     r'<div class="phase-bar"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('phase-labels',  r'<div class="phase-labels"[^>]*data-lesson="2"[^>]*>', 'div'),
        ('plano',         r'<div class="pv-plan"[^>]*data-plan-body="2"[^>]*>', 'div'),
        ('percurso',      r'<div class="pv-post"[^>]*data-post-body="2"[^>]*>', 'div'),
        ('pill',          r'<button class="pv-pill"[^>]*data-plan="2"[^>]*>', 'button'),
        ('card-inclass',  r'<button class="pv-card"[^>]*data-aula="2"[^>]*>', 'button'),
        ('card-postclass', r'<button class="pv-card"[^>]*data-post="2"[^>]*>', 'button'),
    ]:
        s, n = remove(s, rx, tag)
        rel[f'aula2/{nome}'] = n

    # O DADO da aula 2 tambem sai. O deck e data-driven: LESSONS['N'] = {hubLabel,
    # story, frame, build, imageQuiz, reset} alimenta as 10 telas. Deixar o objeto
    # da aula 2 num shell sem os slides dela e carregar conteudo do Dante para
    # dentro do molde — e o base_swaps nao tem como saber que aquilo e conteudo.
    m = re.search(r"LESSONS\['2'\]\s*=\s*\{", s)
    if m:
        depth, j = 0, m.end() - 1
        for t in re.finditer(r'\{|\}', s[j:]):
            depth += 1 if t.group(0) == '{' else -1
            if depth == 0:
                fim = j + t.end()
                break
        while fim < len(s) and s[fim] in ';\n\r\t ':
            fim += 1
        s = s[:m.start()] + s[fim:]
        rel['aula2/LESSONS'] = 1

    # O payload do percurso 2 sai do PV_POSTS pela CHAVE, nao por corte de texto.
    i = s.index('var PV_POSTS = ')
    import json
    obj, fim = json.JSONDecoder().raw_decode(s[i + len('var PV_POSTS = '):])
    obj.pop('2', None)
    s = (s[:i] + 'var PV_POSTS = ' + json.dumps(obj, ensure_ascii=False)
         + s[i + len('var PV_POSTS = ') + fim:])
    rel['aula2/payload'] = 1

    # 2. LITERAIS DO MODELO no lugar dos do Dante.
    for velho, novo in PALETA + NOMES:
        antes = s.count(velho)
        s = s.replace(velho, novo)
        rel[f'swap/{velho}'] = antes

    # 3. MARCADORES DE FECHO que o replace_between do builder ancora. O artefato
    #    fecha as abas com </div> mudo; sem o comentario o builder pega o </div>
    #    do primeiro filho (e o mesmo motivo do fim_da_aba no insert_hub).
    for tab in ('planning', 'inclass', 'postclass'):
        m = re.search(r'<div class="tab-content[^"]*" id="tab-' + tab + r'">', s)
        j = fecha_tag(s, m.start(), 'div')
        s = s[:j] + f'<!-- /tab-{tab} -->' + s[j:]
        rel[f'marcador/tab-{tab}'] = 1
    m = re.search(r'<div class="slides-container" id="slidesContainer">', s)
    j = fecha_tag(s, m.start(), 'div')
    s = s[:j] + '<!-- /slides-container -->' + s[j:]
    rel['marcador/slides-container'] = 1

    return s, rel


def main():
    s, rel = deriva()
    checando = '--check' in sys.argv
    if checando:
        if not os.path.exists(SHELL):
            print(f'FALTA {SHELL}')
            return 1
        with open(SHELL, encoding='utf-8') as fh:
            atual = fh.read()
        if atual != s:
            print('DIVERGE: o shell no disco nao e o que a derivacao produz hoje.')
            print('  (alguem editou o shell a mao, ou o artefato mudou)')
            return 1
        print('OK — o shell no disco e exatamente o artefato menos a aula 2, '
              'com os literais do modelo.')
        return 0
    os.makedirs(os.path.dirname(SHELL), exist_ok=True)
    with open(SHELL, 'w', encoding='utf-8') as fh:
        fh.write(s)
    print(f'escrito {os.path.relpath(SHELL, RAIZ)} ({len(s)/1024:.0f} KB)')
    for k, v in rel.items():
        print(f'  {k:34} {v}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
