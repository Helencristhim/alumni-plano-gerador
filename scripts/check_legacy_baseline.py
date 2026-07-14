#!/usr/bin/env python3
"""
GATE 8 — O LEGADO NÃO PIORA. Varre o REPO INTEIRO, não só o diff.

POR QUE ISSO EXISTE
-------------------
Todos os gates do CI olham apenas os arquivos que o PR mudou. Consequência: um
arquivo que quebrou e que ninguém mais tocou NUNCA MAIS é olhado por ninguém. O
defeito fica lá, invisível, até alguém encostar naquele aluno — e aí "aparece",
como se tivesse nascido naquele dia. Não nasceu: já estava lá.

Este gate varre os 2.2 mil arquivos toda vez. Ele NÃO exige que o legado esteja
limpo (são 944 arquivos com dívida acumulada, 68 alunos — isso é campanha, não
gate). Ele exige uma coisa só, e é a que importa:

    NENHUM ARQUIVO GANHA UM DEFEITO QUE NÃO TINHA.

O legado vira um número conhecido, congelado em legacy-baseline.json, que só pode
CAIR. Conserte um arquivo e o baseline encolhe (rode --update). Quebre um arquivo
e o gate reprova, mesmo que o PR nem tenha tocado nele.

    python3 scripts/check_legacy_baseline.py            # CI: falha se piorou
    python3 scripts/check_legacy_baseline.py --update    # congela o estado atual
    python3 scripts/check_legacy_baseline.py --report     # o inventário da dívida
"""
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, 'scripts', 'legacy-baseline.json')

# Os dois auditores mais ricos. Ambos varrem lista de arquivos e imprimem
# "arquivo" + linhas de defeito; a diferença é só o formato.
FAIL_V = re.compile(r'^\s*❌ FAIL\s+(\S+)\s+\[(\w+)\]')
DEFE_V = re.compile(r'^\s*✗\s+(.*)$')
FILE_P = re.compile(r'^!\s+(public/\S+\.html)')
DEFE_P = re.compile(r'^\s+-\s+\d+x\s+(.*)$')


def categoria(msg):
    """A MENSAGEM não serve de chave: ela carrega contagens, exemplos e nomes de
    aluno, que variam. A CATEGORIA é a mensagem sem nada disso — é o TIPO do
    defeito. Sem essa normalização o baseline vira ruído e o gate, inútil."""
    m = re.sub(r'\(ex:.*', '', msg)
    m = re.sub(r'\(disponíveis.*', '', m)
    m = re.sub(r'"[^"]*"', '"…"', m)
    m = re.sub(r"'[^']*'", "'…'", m)
    m = re.sub(r'<[^>]*>', '<…>', m)
    m = re.sub(r'\d+', 'N', m)
    return ' '.join(m.split())[:120]


def arquivos():
    saida = subprocess.run(['git', 'ls-files', 'public/professor', 'public/aluno'],
                           cwd=RAIZ, capture_output=True, text=True).stdout
    pular = re.compile(r'backup|teste|test|-new-', re.I)
    return [l for l in saida.split('\n')
            if l.endswith('.html') and not pular.search(os.path.basename(l))]


def varrer(fs):
    """-> {caminho: {categoria: contagem}}"""
    achados = {}

    def add(caminho, msg):
        achados.setdefault(caminho, {})
        c = categoria(msg)
        achados[caminho][c] = achados[caminho].get(c, 0) + 1

    # validate_lesson: imprime o BASENAME + [prof|aluno]; reconstruo o caminho.
    r = subprocess.run([sys.executable, '_build/model/validate_lesson.py'] + fs,
                       cwd=RAIZ, capture_output=True, text=True)
    atual = None
    for linha in r.stdout.split('\n'):
        m = FAIL_V.match(linha)
        if m:
            sub = 'professor' if m.group(2).startswith('prof') else 'aluno'
            atual = f'public/{sub}/{m.group(1)}'
            continue
        if atual:
            d = DEFE_V.match(linha.strip())
            if d:
                add(atual, d.group(1))

    # check_inclass_patterns: imprime o caminho completo.
    r = subprocess.run([sys.executable, '_build/model/check_inclass_patterns.py'] + fs,
                       cwd=RAIZ, capture_output=True, text=True)
    atual = None
    for linha in r.stdout.split('\n'):
        m = FILE_P.match(linha)
        if m:
            atual = m.group(1)
            continue
        if atual:
            d = DEFE_P.match(linha)
            if d:
                add(atual, d.group(1))

    return achados


def main():
    fs = arquivos()
    atual = varrer(fs)

    if '--update' in sys.argv:
        json.dump(atual, open(BASE, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1, sort_keys=True)
        n = sum(sum(c.values()) for c in atual.values())
        print(f'baseline congelado: {len(atual)} arquivo(s), {n} defeito(s), {len(fs)} varridos')
        return 0

    if '--report' in sys.argv:
        cats = {}
        for c in atual.values():
            for k, v in c.items():
                cats[k] = cats.get(k, 0) + v
        print(f'{len(atual)} arquivo(s) com dívida, de {len(fs)} varridos\n')
        for k, v in sorted(cats.items(), key=lambda x: -x[1]):
            print(f'{v:5d}  {k}')
        return 0

    if not os.path.exists(BASE):
        sys.exit('legacy-baseline.json não existe. Rode --update uma vez.')
    base = json.load(open(BASE, encoding='utf-8'))

    # A PERGUNTA: algum arquivo ganhou defeito que não tinha?
    # (Arquivo NOVO tem baseline vazio -> tolerância zero, de graça.)
    piorou = []
    for caminho, cats in sorted(atual.items()):
        antes = base.get(caminho, {})
        for cat, n in sorted(cats.items()):
            if n > antes.get(cat, 0):
                piorou.append((caminho, cat, antes.get(cat, 0), n))

    melhorou = sum(max(0, base.get(f, {}).get(c, 0) - atual.get(f, {}).get(c, 0))
                   for f in base for c in base[f])

    if piorou:
        print('=' * 70)
        print(f'  GATE 8 — LEGADO PIOROU: {len(piorou)} defeito(s) NOVO(S)')
        print('=' * 70)
        for caminho, cat, a, d in piorou[:40]:
            print(f'  ✗ {caminho}')
            print(f'      {cat}   ({a} -> {d})')
        if len(piorou) > 40:
            print(f'  ... e mais {len(piorou) - 40}')
        print('\nO gate varre o REPO INTEIRO. Um arquivo que este PR nem tocou pode ter')
        print('quebrado por efeito colateral (builder, modelo, retrofit). Conserte.')
        print('Se o defeito é REAL e aceito, rode --update e justifique no PR.')
        return 1

    n = sum(sum(c.values()) for c in atual.values())
    print(f'✓ GATE 8 — nenhum defeito novo em {len(fs)} arquivos.')
    print(f'  dívida de legado: {n} defeito(s) em {len(atual)} arquivo(s)'
          + (f'  (−{melhorou} vs baseline ✨)' if melhorou else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
