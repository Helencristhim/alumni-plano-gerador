#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Etiqueta as aulas de UM aluno com o framework delas — POR ALUNO, sob demanda.

Decisão do Dan (27/07/2026): as ~1.240 aulas antigas NÃO serão etiquetadas em varredura.
Etiqueta-se um aluno só quando for mexer no framework dele — 5 a 20 arquivos, num PR
daquele aluno. Duas razões:

  1. REGRA 30/31 — varredura em 1.221 arquivos é exatamente o que quase reescreveu 2.182
     arquivos por engano uma vez. Aula que já foi dada não se mexe sem motivo.
  2. Operacional — o repo tem dezenas de gerações rodando em paralelo o tempo todo. Um
     commit tocando 1.221 arquivos conflita com quase toda branch aberta.

Por que etiquetar então? Porque o GATE 11 só enxerga aula ETIQUETADA. Para declarar uma
migração ("fulano: imersivo até a 12, PPP da 13 em diante") o gate precisa saber o que as
aulas antigas dele são — senão não há como conferir que o corte foi respeitado.

USO (dry-run é o padrão — nada é escrito sem --write):

    python3 scripts/tag_framework.py --slug fulano
    python3 scripts/tag_framework.py --slug fulano --write
    python3 scripts/tag_framework.py --slug fulano --framework ppp --de 13 --write

A etiqueta entra logo após <meta name="viewport">, o mesmo lugar onde o builder a põe.
IDEMPOTENTE: arquivo que já tem a etiqueta é pulado (nunca duplica, nunca sobrescreve).
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_VIEWPORT = re.compile(r'(<meta name="viewport"[^>]*>)')
RE_JA_TEM = re.compile(r'<meta name="alumni-framework"')
RE_AULA = re.compile(r'-aula(\d+)\.html$')


def alvos(slug):
    """Aulas do aluno nos dois papéis. O hub ({slug}.html) NÃO entra: ele não é uma aula,
    e o gate raciocina por aula."""
    out = []
    for sub in ('professor', 'aluno'):
        d = os.path.join(ROOT, 'public', sub)
        if not os.path.isdir(d):
            continue
        for nome in sorted(os.listdir(d)):
            m = re.match(rf'^{re.escape(slug)}-aula(\d+)\.html$', nome)
            if m:
                out.append((int(m.group(1)), os.path.join(d, nome)))
    return sorted(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--slug', required=True, help='slug do aluno (ex: tania-rosa)')
    ap.add_argument('--framework', default='imersivo-prototipo',
                    help='framework a carimbar (padrão: imersivo-prototipo)')
    ap.add_argument('--de', type=int, default=None, metavar='N',
                    help='a partir da aula N usa --framework; as ANTERIORES ficam com '
                         '--framework-anterior. Sem isto, todas recebem --framework.')
    ap.add_argument('--framework-anterior', default='imersivo-prototipo',
                    help='framework das aulas anteriores a --de (padrão: imersivo-prototipo)')
    ap.add_argument('--write', action='store_true',
                    help='escreve de fato. SEM esta flag, só mostra o que faria.')
    args = ap.parse_args()

    arquivos = alvos(args.slug)
    if not arquivos:
        print(f'nenhuma aula encontrada para o slug "{args.slug}"', file=sys.stderr)
        return 2

    escritos = pulados = sem_viewport = 0
    for n, caminho in arquivos:
        rel = os.path.relpath(caminho, ROOT)
        with open(caminho, encoding='utf-8') as f:
            html = f.read()
        if RE_JA_TEM.search(html):
            pulados += 1
            print(f'  = {rel:58} já etiquetado')
            continue
        fw = args.framework if (args.de is None or n >= args.de) else args.framework_anterior
        if not RE_VIEWPORT.search(html):
            sem_viewport += 1
            print(f'  ! {rel:58} SEM <meta viewport> — pulado', file=sys.stderr)
            continue
        novo = RE_VIEWPORT.sub(
            lambda m: m.group(1) + f'\n    <meta name="alumni-framework" content="{fw}">',
            html, count=1)
        if args.write:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(novo)
        escritos += 1
        print(f'  {"+" if args.write else "~"} {rel:58} {fw}')

    print(f'\n{"ESCRITO" if args.write else "DRY-RUN (nada foi escrito — use --write)"}: '
          f'{escritos} etiqueta(s), {pulados} já tinha(m), {sem_viewport} sem viewport')
    if args.write:
        print('Agora rode: python3 scripts/check_framework_isolation.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
