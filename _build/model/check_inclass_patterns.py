#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_inclass_patterns.py — gate anti-regressao dos 2 bugs sistemicos de IN CLASS.

Bug 1 (reveal quebrado): slides de Comprehension/Listening com
  <div class="comp-question" onclick="...toggle('revealed')"> + resposta em
  <p class="fill-answer" style="display:none"> MAS sem a regra CSS
  .comp-question.revealed .fill-answer{display:block} -> clicar nao revela nada.
  O padrao CORRETO do modelo e .comp-q/.q-answer. Aulas novas devem usar .comp-q,
  ou (se usarem .comp-question) ter a regra CSS de reveal.

Bug 2 (Common Mistake chapado): slide com <div class="mistake-item" style="...">
  cru (background inline) em vez das classes do modelo .mistake-wrong/.mistake-right.

USO: python3 _build/model/check_inclass_patterns.py public/professor/{slug}-aula{N}.html [...]
Sai != 0 (bloqueia) se algum arquivo tiver qualquer um dos padroes quebrados.
"""
import re
import sys


def check(path):
    s = open(path, encoding='utf-8').read()
    problems = []

    # Bug 1: comp-question sem a regra CSS de reveal
    if 'class="comp-question"' in s and '.comp-question.revealed' not in s:
        n = s.count('class="comp-question"')
        problems.append(
            f'{n}x <div class="comp-question"> SEM a regra CSS '
            f'.comp-question.revealed (reveal nao funciona). Use .comp-q/.q-answer '
            f'do modelo, ou adicione a regra .comp-question.revealed .fill-answer'
            f'{{display:block!important}}.')

    # Bug 2: mistake-item com background inline em vez de .mistake-wrong/.mistake-right
    bad_items = re.findall(r'<div class="mistake-item"\s+style="[^"]*(?:danger-bg|success-bg|background)[^"]*"', s)
    if bad_items:
        problems.append(
            f'{len(bad_items)}x <div class="mistake-item" style="...background..."> cru '
            f'(visual chapado). Use as classes do modelo: '
            f'<div class="mistake-item mistake-wrong"> / mistake-right.')

    return problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = 0
    for f in sys.argv[1:]:
        probs = check(f)
        if probs:
            total += len(probs)
            print(f'! {f}')
            for p in probs:
                print(f'    - {p}')
    if total:
        print(f'\nFALHOU: {total} problema(s) de padrao IN CLASS. Corrija antes do PR.')
        sys.exit(1)
    print(f'OK: {len(sys.argv) - 1} arquivo(s) sem padrao IN CLASS quebrado.')


if __name__ == '__main__':
    main()
