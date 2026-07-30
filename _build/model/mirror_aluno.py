#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regera o espelho ALUNO de uma aula standalone a partir do arquivo do PROFESSOR,
aplicando EXATAMENTE a mesma transformacao que o build_from_model.py faz no fim de
`build_lesson()` (busque por "espelho ALUNO (REGRA 34)").

Para que serve. Quando uma aula ja publicada precisa de conserto de CONTEUDO, editar
so o arquivo do professor deixa o do aluno para tras -- e os dois divergem em silencio,
porque nenhum gate compara o conteudo dos dois. Rodar o builder inteiro nao serve:
ele reconstroi a aula do config e joga fora a edicao manual.

A transformacao e mecanica e sem estado: tira o data-teacher, troca os rotulos de
Professor para Aluno, aponta o EXIT para o hub do aluno e troca a chave de
localStorage. O conteudo -- que e o que se esta consertando -- vem inteiro do professor.

USO: python3 _build/model/mirror_aluno.py public/professor/{slug}-aula{N}.html [...]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def mirror(prof_path: Path):
    m = re.match(r"(.+)-aula(\d+)\.html$", prof_path.name)
    if not m:
        return f"{prof_path.name}: nao e uma aula standalone (-aulaN.html)"
    slug, n = m.group(1), m.group(2)
    aluno_path = ROOT / "public" / "aluno" / prof_path.name
    if not aluno_path.exists():
        return f"{prof_path.name}: espelho do aluno nao existe -- nada a fazer"

    a = prof_path.read_text(encoding="utf-8")
    a = a.replace("<title>Professor View --", "<title>Aluno --")
    a = a.replace('<span class="prof-badge">Professor View</span>',
                  '<span class="prof-badge">Aluno</span>')
    a = a.replace(">PROFESSOR VIEW<", ">ALUNO<")
    a = re.sub(r'\sdata-teacher="(?:[^"\\]|\\.)*"', "", a)
    a = a.replace("</style>", ".teacher-t{display:none !important}\n</style>", 1)
    a = a.replace(f"window.location.href = '/professor/{slug}.html#inclass'",
                  f"window.location.href = '/aluno/{slug}.html#inclass'")
    a = a.replace(f"{slug}-aula{n}-professor", f"{slug}-aula{n}-aluno")

    old = aluno_path.read_text(encoding="utf-8")
    if old == a:
        return f"{prof_path.name}: espelho ja identico"
    aluno_path.write_text(a, encoding="utf-8")
    return (f"{prof_path.name}: espelho do aluno regerado "
            f"({len(old)} -> {len(a)} chars, data-teacher restantes: {a.count('data-teacher')})")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(mirror(Path(f).resolve()))
