#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_ordering.py — liga o arrastar-com-o-dedo no exercicio de ordenar (ver ordering.py).

O JS e o CSS moram no SHELL DO HUB, e o hub de cada aluno foi clonado do modelo no dia em
que ele nasceu. Por isso o conserto tem dois destinos:

  modelo  -> public/{professor,aluno}/helen-mendes.html   (hub NOVO ja nasce certo)
  aluno   -> public/{professor,aluno}/{slug}.html          (hub que JA existe)

USO
  dry-run:  python3 _build/model/apply_ordering.py helen-mendes ricardo-wertheim
  aplicar:  python3 _build/model/apply_ordering.py helen-mendes ricardo-wertheim --apply

Idempotente. Aluno sem exercicio de ordenar = no-op.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import ordering  # noqa: E402


def main(argv):
    slugs = [a for a in argv if not a.startswith('--')]
    aplicar = '--apply' in argv
    if not slugs:
        print(__doc__)
        return 2
    tot = 0
    for slug in slugs:
        for papel in ('professor', 'aluno'):
            fp = os.path.join(ROOT, 'public', papel, f'{slug}.html')
            if not os.path.exists(fp):
                print(f'  {slug}/{papel}: arquivo nao existe — pulado')
                continue
            with open(fp, encoding='utf-8') as f:
                s0 = f.read()
            s, n = ordering.upgrade(s0)
            if s == s0:
                print(f'  {slug}/{papel}: nada a fazer (ja tem)')
                continue
            tot += 1
            print(f'  {slug}/{papel}: +{n} alca(s) em {s.count("order-container")} exercicio(s)')
            if aplicar:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(s)
    print(f'\n{tot} arquivo(s).' + ('' if aplicar else '  [DRY-RUN — use --apply para gravar]'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
