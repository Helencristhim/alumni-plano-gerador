#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troca o card Pre-class da Aula 2 nos DOIS hubs do Guilherme.

Por que nao usa o _build/model/insert_hub.py: aquele e ADITIVO por decisao
(REGRA 20 -- hub so cresce, nunca toca aula anterior) e pula o bloco que ja
existe. Aqui a aula 2 EXISTE e precisa ser SUBSTITUIDA, a pedido do professor.
Entao a troca e cirurgica e so nesta aula:

  - acha o <div class="lesson-card" ... id="ex-lesson-2"> e anda por BALANCO de
    <div> ate o </div> que o fecha (nunca por regex de fim, que erraria no
    primeiro </div> aninhado);
  - troca so esse intervalo;
  - confere, antes de gravar, que o balanco de <div> do arquivo inteiro nao
    mudou, que nenhum id colide e que nenhum handler ficou sem funcao.

Aula 1 e aulas 3 a 8, stamps, abas e audioMap ficam byte a byte como estavam.

USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/patch_hub_l2.py [--check]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'guilherme-henrique-caneli'
HUBS = [os.path.join(ROOT, 'public', 'professor', SLUG + '.html'),
        os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')]


def bloco(s, lesson_id):
    """(inicio, fim) do lesson-card, fechando por BALANCO de <div>."""
    m = re.search(r'<div class="lesson-card"[^>]*id="%s"[^>]*>' % re.escape(lesson_id), s)
    assert m, 'card %s nao encontrado' % lesson_id
    depth = 0
    for t in re.finditer(r'<div\b|</div\s*>', s[m.start():]):
        depth += 1 if t.group(0).startswith('<div') else -1
        if depth == 0:
            return m.start(), m.start() + t.end()
    raise AssertionError('card %s nao fecha' % lesson_id)


def main():
    novo = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
    check = '--check' in sys.argv
    for path in HUBS:
        s = open(path, encoding='utf-8').read()
        ini, fim = bloco(s, 'ex-lesson-2')
        antigo = s[ini:fim]
        if antigo.strip() == novo:
            print('  = %s ja esta no formato novo' % os.path.relpath(path, ROOT))
            continue
        out = s[:ini] + novo + s[fim:]

        # ── travas antes de gravar ────────────────────────────────────────────
        def divs(x):
            return len(re.findall(r'<div\b', x)) - len(re.findall(r'</div\s*>', x))
        assert divs(out) == divs(s), 'balanco de <div> mudou no arquivo: %s' % path
        for k in ('id="ex-lesson-', 'id="stamp', 'data-slide="'):
            assert out.count(k) == s.count(k), 'contagem de %s mudou em %s' % (k, path)
        assert len(out) > len(s) * 0.9, 'arquivo encolheu mais de 10%%: %s' % path
        ids = re.findall(r'id="([^"]+)"', out)
        dup = sorted({i for i in ids if ids.count(i) > 1})
        assert not dup, 'id duplicado apos o patch: %s' % dup
        fns = set(re.findall(r'function ([a-zA-Z0-9_]+)\(', out))
        usados = set(re.findall(r'on\w+="([a-zA-Z0-9_]+)\(', novo))
        assert usados <= fns, 'handler sem funcao no hub: %s' % sorted(usados - fns)

        if check:
            print('  ? %s: trocaria %d KB por %d KB (travas OK)'
                  % (os.path.relpath(path, ROOT), len(antigo) // 1024, len(novo) // 1024))
            continue
        open(path, 'w', encoding='utf-8').write(out)
        print('  + %s: %d KB -> %d KB' % (os.path.relpath(path, ROOT), len(s) // 1024, len(out) // 1024))


if __name__ == '__main__':
    main()
