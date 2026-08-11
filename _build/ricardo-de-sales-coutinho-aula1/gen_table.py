#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a tabela curricular de 96 aulas do planning.html a partir de curriculo.py.

O /api/gerar-temas nao respondeu em 40 min (falha conhecida do endpoint), entao o
programa e AUTORAL — escrito em blocos, com progressao A0 -> B1 funcional ancorada na
abertura da operacao do Banco BS2 na Florida. Ver o cabecalho de curriculo.py.

USO: python3 _build/ricardo-de-sales-coutinho-aula1/gen_table.py
     (le planning.tpl.html, escreve planning.html — idempotente)
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from curriculo import CURRICULO  # noqa: E402

MARCOS = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 96}


def linha(n, tema, foco, ativ, hw):
    fundo = ('background:var(--accent-dim)' if n == 1
             else 'background:var(--bg-elevated)' if n % 2 == 0 else '')
    style = 'border-bottom:1px solid var(--border)' + (';' + fundo if fundo else '')
    fw = ';font-weight:700' if n in MARCOS else ''
    return (f'        <tr style="{style}">'
            f'<td style="padding:.5rem{fw}">{n}</td>'
            f'<td style="padding:.5rem{fw}">{tema}</td>'
            f'<td style="padding:.5rem">{foco}</td>'
            f'<td style="padding:.5rem">{ativ}</td>'
            f'<td style="padding:.5rem">{hw}</td></tr>')


def main():
    rows = [linha(i + 1, *CURRICULO[i]) for i in range(len(CURRICULO))]
    tpl = os.path.join(AQUI, 'planning.tpl.html')
    out = os.path.join(AQUI, 'planning.html')
    s = open(tpl, encoding='utf-8').read()
    if '<!--CURRICULO-->' not in s:
        raise SystemExit('planning.tpl.html sem o placeholder <!--CURRICULO-->')
    open(out, 'w', encoding='utf-8').write(s.replace('<!--CURRICULO-->', '\n'.join(rows)))
    print(f'tabela escrita: {len(rows)} aulas')


if __name__ == '__main__':
    main()
