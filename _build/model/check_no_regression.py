#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_no_regression.py — GATE anti-regressão pra arquivo de aula MODIFICADO num PR.

Pra cada arquivo, compara com a versão do ref base (default origin/main):
  - contagem de id="ex-lesson-" não pode DIMINUIR (accordion Pre-class sumindo)
  - contagem de id="stamp"     não pode DIMINUIR (stamp sumindo)
  - contagem de data-slide=    não pode DIMINUIR (slides sumindo)
  - arquivo não pode ENCOLHER mais de 10% (overwrite com versão velha — incidente 6cd5b3b9)

Aula só nasce, não morre. USO:
  python3 _build/model/check_no_regression.py --base origin/main arquivo.html [...]
"""
import re
import subprocess
import sys


def counts(c):
    return {
        'ex-lesson': len(re.findall(r'id="ex-lesson-', c)),
        'stamp': len(re.findall(r'id="stamp\d', c)),
        'slides': len(re.findall(r'data-slide="', c)),
        'bytes': len(c),
    }


def main():
    args = sys.argv[1:]
    base = 'origin/main'
    if args and args[0] == '--base':
        base = args[1]
        args = args[2:]
    if not args:
        print(__doc__)
        sys.exit(2)
    rc = 0
    for path in args:
        cur = counts(open(path, encoding='utf-8').read())
        r = subprocess.run(['git', 'show', f'{base}:{path}'], capture_output=True, text=True)
        if r.returncode != 0:
            print(f'✅ {path}: novo no PR (sem base pra comparar)')
            continue
        old = counts(r.stdout)
        fails = []
        for k in ('ex-lesson', 'stamp', 'slides'):
            if cur[k] < old[k]:
                fails.append(f'{k} DIMINUIU: {old[k]} -> {cur[k]}')
        if old['bytes'] and cur['bytes'] < old['bytes'] * 0.9:
            fails.append(f'arquivo ENCOLHEU {100 - cur["bytes"]*100//old["bytes"]}% '
                         f'({old["bytes"]} -> {cur["bytes"]} bytes) — possível overwrite com versão velha')
        if fails:
            rc = 1
            print(f'❌ {path}:')
            for f in fails:
                print(f'   ✗ {f}')
        else:
            print(f'✅ {path}: sem regressão (ex-lesson {old["ex-lesson"]}->{cur["ex-lesson"]}, '
                  f'stamps {old["stamp"]}->{cur["stamp"]}, slides {old["slides"]}->{cur["slides"]})')
    sys.exit(rc)


if __name__ == '__main__':
    main()
