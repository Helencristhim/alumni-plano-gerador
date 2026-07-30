#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Propaga para o hub do ALUNO as edicoes de conteudo feitas no hub do PROFESSOR.

Por que nao regerar. O hub do aluno NAO e uma copia do professor: tem 2 abas em vez
de 4 (sem Planejamento, sem IN CLASS) e nasce sem data-teacher. Derivar um do outro
como se faz na aula standalone destruiria essa estrutura. Mas o Pre-class e os
Complementares -- que sao o conteudo que se edita -- existem nos dois, iguais.

Como funciona. Compara o hub do professor ANTES (git HEAD) e DEPOIS da edicao, linha
a linha. Cada linha que mudou vira um par (antiga -> nova). Se a linha antiga existe
no hub do aluno, e trocada pela nova. Linha que so existe no professor (as que tem
data-teacher, a aba Planejamento, o menu IN CLASS) simplesmente nao casa e e ignorada
-- e o comportamento correto, nao um erro.

USO: python3 _build/model/propagate_hub_aluno.py {slug}
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def main(slug):
    prof = ROOT / "public" / "professor" / f"{slug}.html"
    aluno = ROOT / "public" / "aluno" / f"{slug}.html"
    if not prof.exists() or not aluno.exists():
        print(f"faltando: prof={prof.exists()} aluno={aluno.exists()}")
        return 1

    old = subprocess.run(
        ["git", "show", f"HEAD:public/professor/{slug}.html"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    new = prof.read_text(encoding="utf-8")

    old_lines, new_lines = old.splitlines(), new.splitlines()
    if len(old_lines) != len(new_lines):
        print(f"AVISO: contagem de linhas mudou ({len(old_lines)} -> {len(new_lines)}); "
              "so pares de linhas alinhadas serao propagados")

    pairs = [(a, b) for a, b in zip(old_lines, new_lines) if a != b]
    if not pairs:
        print("nada mudou no hub do professor")
        return 0

    s = aluno.read_text(encoding="utf-8")
    hit = miss = 0
    for a, b in pairs:
        if a and a in s:
            s = s.replace(a, b)
            hit += 1
        else:
            miss += 1
    aluno.write_text(s, encoding="utf-8")
    print(f"{len(pairs)} linhas mudadas no professor -> {hit} propagadas ao aluno, "
          f"{miss} nao aplicaveis (so existem no professor)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
