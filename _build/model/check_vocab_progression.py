#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_vocab_progression.py — GATE da REGRA 22 (vocabulário não repete entre aulas).

Palavra ensinada como vocabulário NOVO (vocab card) numa aula NUNCA pode ser
reapresentada como NOVA numa aula posterior do mesmo aluno. Pode ser revisada
(warm-up, diálogo), mas não voltar como vocab card.

O checker extrai o conjunto de `vocab-card-word` de cada aula (N) e falha se uma
mesma palavra aparece como vocab card em 2+ aulas distintas — o sinal estrutural
de que foi "ensinada como nova" duas vezes.

Fontes aceitas (passe quantos arquivos quiser do MESMO aluno):
  - HUB inline (public/professor/{slug}.html): cada bloco id="ex-lesson-N" = aula N
  - Standalone (public/professor/{slug}-aulaN.html): o arquivo inteiro = aula N
Aluno e nº da aula saem do nome do arquivo / dos ids — nada de adivinhação.

Whitelist opcional: _build/model/vocab_allow_repeat.json
  { "{slug}": ["word a re-ensinar de propósito", ...] }  (case-insensitive)

USO:
  python3 _build/model/check_vocab_progression.py public/professor/gabriela-paulucci.html
  python3 _build/model/check_vocab_progression.py public/professor/nilo-*-aula*.html
Exit 1 se houver repetição não-autorizada.
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOW_PATH = os.path.join(HERE, 'vocab_allow_repeat.json')


def norm(word):
    w = re.sub(r'\s+', ' ', word).strip().lower()
    w = w.strip('.,;:!?"\'')
    return w


def words_in(blob):
    return {norm(m) for m in re.findall(r'vocab-card-word[^>]*>([^<]+)<', blob) if norm(m)}


def slug_of(path):
    p = path.replace('\\', '/')
    m = re.search(r'/(?:professor|aluno)/(.+?)(?:-aula\d+)?\.html$', p)
    return m.group(1) if m else os.path.basename(p)


def lessons_from_file(path):
    """-> dict {lesson_no: set(words)} a partir de UM arquivo."""
    c = open(path, encoding='utf-8').read()
    out = defaultdict(set)
    m = re.search(r'-aula(\d+)\.html$', path.replace('\\', '/'))
    if m:                                   # standalone: arquivo inteiro = aula N
        out[int(m.group(1))] |= words_in(c)
        return out
    ids = [(mm.start(), int(mm.group(1)))   # hub inline: bloco por ex-lesson-N
           for mm in re.finditer(r'id="ex-lesson-(\d+)"', c)]
    for i, (pos, n) in enumerate(ids):
        end = ids[i + 1][0] if i + 1 < len(ids) else len(c)
        out[n] |= words_in(c[pos:end])
    return out


def main():
    args = []
    for a in sys.argv[1:]:
        args.extend(sorted(glob.glob(a)) or [a])
    if not args:
        print(__doc__)
        sys.exit(2)

    allow = {}
    if os.path.exists(ALLOW_PATH):
        allow = {k.lower(): {norm(w) for w in v}
                 for k, v in json.load(open(ALLOW_PATH, encoding='utf-8')).items()}

    by_slug = defaultdict(lambda: defaultdict(set))
    for path in args:
        if not os.path.exists(path):
            print(f'❌ arquivo não existe: {path}')
            sys.exit(2)
        for n, ws in lessons_from_file(path).items():
            by_slug[slug_of(path)][n] |= ws

    any_fail = False
    for slug, lessons in sorted(by_slug.items()):
        ok_repeat = allow.get(slug.lower(), set())
        first_seen, repeats = {}, defaultdict(list)
        for n in sorted(lessons):
            for w in sorted(lessons[n]):
                if w in first_seen and first_seen[w] != n:
                    repeats[w].append(n)
                else:
                    first_seen.setdefault(w, n)
        repeats = {w: ns for w, ns in repeats.items() if w not in ok_repeat}
        nles = len(lessons)
        if not lessons:
            print(f'⚠ {slug}: nenhuma aula com vocab card encontrada')
            continue
        if repeats:
            any_fail = True
            print(f'❌ FAIL  {slug} ({nles} aula(s)): {len(repeats)} palavra(s) reensinada(s) (REGRA 22)')
            for w, ns in sorted(repeats.items()):
                print(f'     ✗ "{w}" ensinada como nova na aula {first_seen[w]} e de novo na(s) aula(s) {", ".join(map(str, ns))}')
        else:
            total = sum(len(v) for v in lessons.values())
            print(f'✅ PASS  {slug} ({nles} aula(s), {total} vocab cards): zero repetição como conteúdo novo')
    print('\n' + ('=== REGRA 22 VIOLADA — corrigir ou whitelist antes de mergear ===' if any_fail else '=== REGRA 22 OK ==='))
    sys.exit(1 if any_fail else 0)


if __name__ == '__main__':
    main()
