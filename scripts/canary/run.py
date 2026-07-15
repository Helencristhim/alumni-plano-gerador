#!/usr/bin/env python3
"""
CANARIO DOS GATES — o vigia que nao confia no verde do gate.

    python3 scripts/canary/run.py

Cada fixture em scripts/canary/fixtures/ carrega UM defeito de proposito. O gate
correspondente TEM que reprova-lo. Se o gate PASSAR um fixture, o gate morreu
(pulado, desligado, ou logica quebrada) — e o canario fica VERMELHO, na hora, em
vez de meses depois quando alguem abrir a aula.

Isto e o que faltava em 14/07/2026, quando os GATES 1-7 sairam 'skipped' e o CI
ficou verde sem checar nada. Um gate verde nao prova que o gate funciona. Este
canario prova — a cada PR — que o gate ainda MORDE.

Contrato de cada fixture (MANIFEST.tsv):  <arquivo>\t<substring esperada no FAIL>
O canario exige AS DUAS coisas: exit != 0 (reprovou) E a substring presente
(reprovou pelo MOTIVO CERTO, nao por acidente).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FIXTURES = os.path.join(HERE, 'fixtures')
VALIDATOR = os.path.join(ROOT, '_build', 'model', 'validate_lesson.py')


def carregar_manifest():
    p = os.path.join(FIXTURES, 'MANIFEST.tsv')
    if not os.path.exists(p):
        print('CANARIO QUEBRADO: MANIFEST.tsv nao existe. Rode build_fixtures.py.', file=sys.stderr)
        sys.exit(2)
    itens = []
    for linha in open(p, encoding='utf-8'):
        linha = linha.strip()
        if not linha:
            continue
        arquivo, esperado = linha.split('\t', 1)
        itens.append((arquivo, esperado))
    if not itens:
        print('CANARIO QUEBRADO: MANIFEST vazio.', file=sys.stderr)
        sys.exit(2)
    return itens


def main():
    itens = carregar_manifest()
    mortos = []   # gates que DEIXARAM PASSAR um defeito = gate dormindo
    print(f'Canario: {len(itens)} fixture(s), cada um deve ser REPROVADO pelo seu gate.\n')

    for arquivo, esperado in itens:
        caminho = os.path.join(FIXTURES, arquivo)
        if not os.path.exists(caminho):
            mortos.append(f'{arquivo}: fixture SUMIU do disco')
            print(f'  ✗ {arquivo}: fixture nao existe')
            continue

        r = subprocess.run([sys.executable, VALIDATOR, caminho],
                           capture_output=True, text=True)
        saida = r.stdout + r.stderr
        reprovou = r.returncode != 0
        motivo_certo = esperado in saida

        if reprovou and motivo_certo:
            print(f'  ✓ {arquivo}: reprovado com "{esperado}" — gate VIVO')
        elif reprovou and not motivo_certo:
            # reprovou, mas por OUTRO motivo — o gate-alvo pode estar morto e outra
            # coisa e que barrou. Trata como morte: nao provamos que o gate certo mordeu.
            mortos.append(f'{arquivo}: reprovou, mas SEM a marca "{esperado}" — '
                          f'o gate-alvo pode estar morto (barrou outra coisa)')
            print(f'  ✗ {arquivo}: reprovado por motivo ERRADO (falta "{esperado}")')
        else:
            mortos.append(f'{arquivo}: PASSOU — o gate de "{esperado}" esta DORMINDO')
            print(f'  ✗ {arquivo}: PASSOU no validador — GATE DE "{esperado}" DORMINDO')

    print()
    if mortos:
        print('=== CANARIO VERMELHO — gate(s) dormindo: ===')
        for m in mortos:
            print(f'  - {m}')
        print('\nUm defeito conhecido passou pelo gate. O gate morreu ou foi pulado.')
        print('NAO mergeie ate o gate voltar a reprovar o fixture.')
        sys.exit(1)
    print('=== CANARIO VERDE — todos os gates ainda mordem ===')
    sys.exit(0)


if __name__ == '__main__':
    main()
