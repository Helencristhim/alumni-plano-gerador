#!/usr/bin/env python3
"""Guard de PR de aula: roda ANTES de abrir o PR (junto com validar_aula.py).

Garante as duas propriedades que evitam o incidente 6cd5b3b9 (aulas apagadas
por checkout defasado):

1. ESCOPO — o diff contra origin/main só pode tocar arquivos do aluno em
   questão (+ pipeline/_build, scripts/ e lesson-counts.json). Arquivo de outro
   aluno no diff = abortar.
2. NUNCA REGREDIR — em todo HTML modificado (qualquer aluno), a contagem de
   id="ex-lesson-" e id="stampN" não pode DIMINUIR, e o arquivo não pode
   encolher mais de 10%. Aula só nasce, não morre.

Uso: python3 scripts/check_pr_scope.py <slug-do-aluno> [base=origin/main]
Sai com código != 0 se algo violar.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALLOWED_GLOBAL = (
    'public/data/lesson-counts.json',
)
ALLOWED_PREFIXES = ('_build/', 'scripts/')


def sh(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def show(rev, path):
    try:
        return sh('git', 'show', f'{rev}:{path}')
    except subprocess.CalledProcessError:
        return ''  # arquivo novo


def counts(html):
    return (
        len(re.findall(r'id="ex-lesson-', html)),
        len(set(re.findall(r'id="(stamp\d+)"', html))),
    )


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    slug = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else 'origin/main'
    sh('git', 'fetch', '-q', 'origin', 'main')

    changed = [l for l in sh('git', 'diff', '--name-only', base).splitlines() if l]
    errors = []

    for path in changed:
        ok = (
            path in ALLOWED_GLOBAL
            or path.startswith(ALLOWED_PREFIXES)
            or re.match(rf'public/(professor|aluno)/{re.escape(slug)}(-aula\d+)?(\.html)', path)
            or path.startswith(f'public/audio/{slug}/')
        )
        if not ok:
            errors.append(f'FORA DE ESCOPO ({slug}): {path}')

    for path in changed:
        if not path.endswith('.html') or not path.startswith('public/'):
            continue
        old = show(base, path)
        if not old:
            continue  # arquivo novo, nada a regredir
        new = (ROOT / path).read_text(encoding='utf-8', errors='replace')
        old_ex, old_st = counts(old)
        new_ex, new_st = counts(new)
        if new_ex < old_ex:
            errors.append(f'REGRESSAO ex-lesson em {path}: {old_ex} -> {new_ex}')
        if new_st < old_st:
            errors.append(f'REGRESSAO stamps em {path}: {old_st} -> {new_st}')
        if len(old) > 50_000 and len(new) < len(old) * 0.9:
            errors.append(f'ENCOLHEU >10% {path}: {len(old)} -> {len(new)} bytes (aula apagada?)')

    if errors:
        print('\n'.join('  ✗ ' + e for e in errors))
        print(f'\n❌ check_pr_scope FALHOU ({len(errors)} violações) — NAO abrir PR')
        return 1
    print(f'✅ check_pr_scope OK — {len(changed)} arquivo(s), tudo no escopo de {slug}, sem regressão')
    return 0


if __name__ == '__main__':
    sys.exit(main())
