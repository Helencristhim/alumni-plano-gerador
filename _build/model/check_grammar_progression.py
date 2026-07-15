#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_grammar_progression.py — GATE da REGRA 22 aplicada à GRAMÁTICA.

O irmão gramatical do check_vocab_progression.py. Um ponto gramatical ensinado
como NOVO numa aula NUNCA pode ser reapresentado como novo numa aula posterior do
mesmo aluno. Pode ser revisado (aula de review/checkpoint), mas não voltar como
descoberta.

POR QUE ESTE GATE É CONFIÁVEL (e o extrator da tabela de gramática não seria):
  A tabela de Grammar Discovery é de CONTRASTE — lista a estrutura NOVA junto das já
  ensinadas (present simple vs present continuous vs present perfect...). Extrair o
  ponto da coluna "Form" daria falso-positivo em toda aula correta. A saída limpa é
  o BUILDER emitir UM marcador canônico por aula: data-grammar="<ponto>" no slide de
  Grammar Discovery (build_from_model.inject_grammar_marker). Este checker lê ESSE
  marcador — uniforme, um-por-aula — exatamente como o vocab lê vocab-card-word.

TOLERÂNCIA AO LEGADO (crítico, REGRA 30/31):
  Aula/slide SEM data-grammar é IGNORADA — o gate só compara aulas que TÊM o marcador.
  Aula legada (gerada antes deste marcador existir) não tem data-grammar, logo nunca
  dispara e nunca exige retrofit. Zero falso-positivo no legado, por construção.

Fontes aceitas (passe quantos arquivos quiser do MESMO aluno):
  - Standalone (public/professor/{slug}-aulaN.html): o data-grammar mora aqui, no
    slide de Grammar Discovery. Arquivo inteiro = aula N (ou o data-lesson do slide).
  - HUB (public/professor/{slug}.html): não carrega slides — contribui vazio e passa.
Aluno e nº da aula saem do nome do arquivo / dos atributos — nada de adivinhação.

EXCEÇÃO DE REVIEW: aula cujo TÍTULO contém review/checkpoint/consolidation é isenta
  (não conta como fonte nem como repetição) — igual à lógica de review da REGRA 29.
WHITELIST opcional: _build/model/grammar_allow_repeat.json
  { "{slug}": ["ponto a reensinar de propósito", ...] }  (case-insensitive)

USO:
  python3 _build/model/check_grammar_progression.py public/professor/danielle-moreira-aula*.html
  python3 _build/model/check_grammar_progression.py public/professor/joao-guilherme-da-costa-e-silva.html
Exit 1 se houver repetição não-autorizada.
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOW_PATH = os.path.join(HERE, 'grammar_allow_repeat.json')

# Título de aula de revisão/consolidação — isenta (REGRA 29 usa o mesmo critério).
REVIEW_RE = re.compile(r'\b(review|checkpoint|consolidation|consolida|revis\w*|recap)\b', re.I)
GRAMMAR_RE = re.compile(r'data-grammar="([^"]*)"')


def _full_tag(c, gpos):
    """Devolve a tag de abertura INTEIRA que contém a posição `gpos` (onde começa
    data-grammar=). Necessário porque o data-teacher do slide contém HTML
    ('<strong>...</strong>'), então um recorte por `[^>]*` pararia DENTRO do atributo
    e perderia o data-lesson que pode vir depois. Aqui achamos o '<' que abre a tag e
    o '>' que a fecha respeitando aspas."""
    lt = c.rfind('<', 0, gpos)
    if lt == -1:
        return ''
    i, q = lt + 1, None
    while i < len(c):
        ch = c[i]
        if q:
            if ch == q:
                q = None
        elif ch in '"\'':
            q = ch
        elif ch == '>':
            return c[lt:i + 1]
        i += 1
    return c[lt:]


def norm(g):
    g = re.sub(r'\s+', ' ', g).strip().lower()
    g = g.strip('.,;:!?"\'')
    return g


def _attr(tag, name):
    m = re.search(r'\b' + re.escape(name) + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def slug_of(path):
    p = path.replace('\\', '/')
    m = re.search(r'/(?:professor|aluno)/(.+?)(?:-aula\d+)?\.html$', p)
    if m:
        return m.group(1)
    base = os.path.basename(p)
    base = re.sub(r'-aula\d+\.html$', '', base)
    return re.sub(r'\.html$', '', base)


def _enclosing_lesson(c, pos):
    """No HUB, o data-grammar (se algum dia existir ali) cairia dentro de um bloco
    id="ex-lesson-N". Retorna N do bloco que contém `pos`, ou None."""
    best = None
    for mm in re.finditer(r'id="ex-lesson-(\d+)"', c):
        if mm.start() <= pos:
            best = int(mm.group(1))
        else:
            break
    return best


def _title_text(c):
    """Texto onde procurar 'review/checkpoint': a IDENTIDADE da aula — <title> e
    subtitle. NÃO usa os chapter-label dos slides: toda aula normal tem um capítulo
    'Recap'/'Wrap-Up', o que marcaria QUALQUER aula como review (falso-positivo)."""
    bits = []
    for pat in (r'<title>([^<]*)</title>',
                r'<p class="subtitle"[^>]*>([^<]*)</p>'):
        bits += re.findall(pat, c)
    return ' '.join(bits)


def lessons_from_file(path):
    """-> (grammars: {aula: set(pontos)}, reviews: set(aula)) a partir de UM arquivo."""
    c = open(path, encoding='utf-8').read()
    grammars = defaultdict(set)
    reviews = set()
    file_aula = None
    m = re.search(r'-aula(\d+)\.html$', path.replace('\\', '/'))
    if m:
        file_aula = int(m.group(1))

    for tm in GRAMMAR_RE.finditer(c):
        g = norm(tm.group(1))
        if not g:
            continue
        dl = _attr(_full_tag(c, tm.start()), 'data-lesson')
        if dl and dl.isdigit():
            aula = int(dl)
        elif file_aula is not None:
            aula = file_aula
        else:
            aula = _enclosing_lesson(c, tm.start())
        if aula is not None:
            grammars[aula].add(g)

    # review: standalone = título do arquivo; hub = título de cada bloco ex-lesson-N
    if file_aula is not None:
        if REVIEW_RE.search(_title_text(c)):
            reviews.add(file_aula)
    else:
        ids = [(mm.start(), int(mm.group(1))) for mm in re.finditer(r'id="ex-lesson-(\d+)"', c)]
        for i, (pos, n) in enumerate(ids):
            end = ids[i + 1][0] if i + 1 < len(ids) else len(c)
            block = c[pos:end]
            htxt = ' '.join(re.findall(r'<h[23][^>]*>([^<]*)</h[23]>', block))
            if REVIEW_RE.search(htxt):
                reviews.add(n)
    return grammars, reviews


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
    review_by_slug = defaultdict(set)
    for path in args:
        if not os.path.exists(path):
            print(f'❌ arquivo não existe: {path}')
            sys.exit(2)
        grammars, reviews = lessons_from_file(path)
        for n, gs in grammars.items():
            by_slug[slug_of(path)][n] |= gs
        review_by_slug[slug_of(path)] |= reviews

    any_fail = False
    for slug, lessons in sorted(by_slug.items()):
        ok_repeat = allow.get(slug.lower(), set())
        reviews = review_by_slug.get(slug, set())
        # aula de review não conta — nem como fonte nem como repetição (REGRA 29)
        graded = {n: gs for n, gs in lessons.items() if n not in reviews}
        marked = {n: gs for n, gs in graded.items() if gs}
        if not marked:
            print(f'⚠ {slug}: nenhuma aula com data-grammar — nada a checar (legado tolerado)')
            continue
        first_seen, repeats = {}, defaultdict(list)
        for n in sorted(graded):
            for g in sorted(graded[n]):
                if g in first_seen and first_seen[g] != n:
                    repeats[g].append(n)
                else:
                    first_seen.setdefault(g, n)
        repeats = {g: ns for g, ns in repeats.items() if g not in ok_repeat}
        nmarked = len(marked)
        if repeats:
            any_fail = True
            print(f'❌ FAIL  {slug} ({nmarked} aula(s) com marcador): '
                  f'{len(repeats)} ponto(s) de GRAMÁTICA REPETIDA (REGRA 22)')
            for g, ns in sorted(repeats.items()):
                print(f'     ✗ "{g}" ensinado como novo na aula {first_seen[g]} '
                      f'e de novo na(s) aula(s) {", ".join(map(str, ns))}')
        else:
            total = sum(len(v) for v in marked.values())
            print(f'✅ PASS  {slug} ({nmarked} aula(s) com marcador, {total} ponto(s)): '
                  f'zero gramática reensinada como nova')
    print('\n' + ('=== REGRA 22 (GRAMÁTICA REPETIDA) — corrigir ou whitelist antes de mergear ==='
                  if any_fail else '=== REGRA 22 (gramática) OK ==='))
    sys.exit(1 if any_fail else 0)


if __name__ == '__main__':
    main()
