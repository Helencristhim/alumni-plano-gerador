#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troca o card Pre-class de UMA aula nos dois hubs do Guilherme.

Generalizacao do patch_hub_l2.py da aula 2, pelo mesmo motivo: o
_build/model/insert_hub.py e ADITIVO por decisao (REGRA 20 -- o hub so cresce e
nunca toca aula anterior) e PULA o bloco que ja existe. Aqui as aulas EXISTEM e
precisam ser substituidas, a pedido do professor.

A troca e cirurgica e so na aula pedida: acha o lesson-card por id, anda por
BALANCO de <div> ate o </div> que o fecha (nunca por regex de fim, que pararia
no primeiro </div> aninhado), e troca so esse intervalo. As outras aulas, os
stamps, as abas e o audioMap ficam byte a byte como estavam.

USO (da raiz): python3 _build/guilherme-henrique-caneli/patch_hub_pc.py <n> [--check]
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
    m = re.search(r'<div class="lesson-card"[^>]*id="%s"[^>]*>' % re.escape(lesson_id), s)
    assert m, 'card %s nao encontrado' % lesson_id
    depth = 0
    for t in re.finditer(r'<div\b|</div\s*>', s[m.start():]):
        depth += 1 if t.group(0).startswith('<div') else -1
        if depth == 0:
            return m.start(), m.start() + t.end()
    raise AssertionError('card %s nao fecha' % lesson_id)


def main():
    n = int(sys.argv[1])
    check = '--check' in sys.argv
    novo = open(os.path.join(ROOT, '_build', '%s-aula%d' % (SLUG, n), 'preclass.html'),
                encoding='utf-8').read().strip()
    alvo = 'ex-lesson-%d' % n
    for path in HUBS:
        s = open(path, encoding='utf-8').read()
        ini, fim = bloco(s, alvo)
        if s[ini:fim].strip() == novo:
            print('  = %s ja esta no formato novo' % os.path.relpath(path, ROOT))
            continue
        out = s[:ini] + novo + s[fim:]

        def divs(x):
            return len(re.findall(r'<div\b', x)) - len(re.findall(r'</div\s*>', x))
        assert divs(out) == divs(s), 'balanco de <div> mudou: %s' % path
        # nenhum id pode colidir nem sumir, e nenhuma OUTRA aula pode mudar
        for k in ('id="ex-lesson-', 'id="stamp', 'data-slide="'):
            assert out.count(k) == s.count(k), 'contagem de %s mudou em %s' % (k, path)
        for m in re.finditer(r'id="(ex-lesson-\d+)"', s):
            outro = m.group(1)
            if outro == alvo:
                continue
            a, b = bloco(s, outro), bloco(out, outro)
            assert s[a[0]:a[1]] == out[b[0]:b[1]], 'a aula %s mudou, e nao devia' % outro
        fns = set(re.findall(r'function ([a-zA-Z0-9_]+)\(', out))
        usados = set(re.findall(r'on\w+="([a-zA-Z0-9_]+)\(', novo))
        assert usados <= fns, 'handler sem funcao no hub: %s' % sorted(usados - fns)
        if check:
            print('  ~ %s: trocaria %d -> %d bytes' % (os.path.relpath(path, ROOT), fim - ini, len(novo)))
            continue
        open(path, 'w', encoding='utf-8').write(out)
        print('  + %s: aula %d trocada (%d -> %d bytes)'
              % (os.path.relpath(path, ROOT), n, fim - ini, len(novo)))


if __name__ == '__main__':
    main()
