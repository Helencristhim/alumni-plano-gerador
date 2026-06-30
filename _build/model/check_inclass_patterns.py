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

    # Bug A (template leitura): .ic-reading sem rolagem -> texto+alternativas estouram a tela
    if 'class="ic-reading"' in s and not re.search(r'\.ic-reading\s*\{[^}]*max-height', s):
        problems.append(
            '.ic-reading presente mas SEM max-height/overflow no CSS (texto longo + '
            'alternativas estouram os 100vh e ficam cortados). Adicione '
            '.ic-reading{max-height:42vh;overflow-y:auto}.')

    # Bug D (overlap): slide de leitura centraliza vertical -> conteudo alto transborda
    # pra cima e o titulo invade a barra de capitulos. Exige top-align nos slides de leitura.
    if 'class="ic-reading"' in s and 'ic-reading:not(.ic-collapsed)){align-items:flex-start' not in s:
        problems.append(
            '.ic-reading presente mas SEM a regra de top-align (slide alto transborda '
            'pra cima e o titulo colide com a barra de capitulos). Adicione '
            '.slide:has(.ic-reading:not(.ic-collapsed)){align-items:flex-start}.')

    # Bug B (parte 2): ic-tfrow sem data-answer -> True/False mostra os 2 veredictos
    rows = re.findall(r'<div class="ic-tfrow"([^>]*)>', s)
    missing = [r for r in rows if 'data-answer' not in r]
    if missing:
        problems.append(
            f'{len(missing)}x <div class="ic-tfrow"> SEM data-answer (True/False acende '
            f'TRUE e FALSE juntos). Marque data-answer="true|false" em cada linha.')

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
