#!/usr/bin/env python3
"""GATE 33 — código de aluno JAMAIS muda quando entra gente nova.

O aluno recebe o código uma vez e ele é distribuído. Se uma execução do gerador
renumerar quem já tem, todas as senhas na mão da equipe viram lixo silenciosamente:
ninguém percebe até um aluno não conseguir entrar.

Prova, num diretório de teste (não toca em nada real):
  1. aluno novo alfabeticamente ANTES de todos -> ninguém é renumerado
  2. material novo de aluno existente (-v2)    -> herda o código dele, ninguém muda
  3. sumiço em massa de materiais              -> ABORTA em vez de revogar

Uso: python3 scripts/test_senhas_estaveis.py
"""
import csv
import os
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GER = RAIZ / "scripts" / "gerar_senhas_alunos.py"


def roda(pasta_alunos: Path, home: Path, *args) -> subprocess.CompletedProcess:
    src = GER.read_text(encoding="utf-8")
    src = src.replace('ALUNOS = Path("public/aluno")', f'ALUNOS = Path({str(pasta_alunos)!r})')
    tmp = home / "_ger.py"
    tmp.write_text(src, encoding="utf-8")
    env = dict(os.environ, HOME=str(home))
    return subprocess.run([sys.executable, str(tmp), *args], capture_output=True, text=True, env=env)


def lista(home: Path) -> dict:
    f = home / "alumni-senhas" / "senhas-alunos.csv"
    if not f.exists():
        return {}
    with f.open(encoding="utf-8") as fh:
        return {r["slug"]: r["senha"] for r in csv.DictReader(fh)}


def main() -> int:
    falhas = 0
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        alunos = d / "aluno"; alunos.mkdir()
        home = d / "home"; home.mkdir()
        base = ["carlos-silva", "maria-souza", "rafael-teste", "zilda-final"]
        for s in base:
            (alunos / f"{s}.html").write_text("<html><h1>%s</h1></html>" % s, encoding="utf-8")

        roda(alunos, home)
        antes = lista(home)
        print(f"  base: {len(antes)} alunos -> {antes}")

        print("\n1) ALUNO NOVO alfabeticamente ANTES de todos")
        (alunos / "aaa-novato.html").write_text("<html><h1>Novato</h1></html>", encoding="utf-8")
        roda(alunos, home)
        dps = lista(home)
        mudou = {k for k in antes if dps.get(k) != antes[k]}
        ok = not mudou and "aaa-novato" in dps
        print(f"     {'ok   ' if ok else 'FALHA'}  novato={dps.get('aaa-novato')} | renumerados: {sorted(mudou) or 'nenhum'}")
        falhas += 0 if ok else 1

        print("\n2) MATERIAL NOVO de aluno existente (-v2)")
        antes2 = lista(home)
        (alunos / "maria-souza-v2.html").write_text("<html><h1>Maria V2</h1></html>", encoding="utf-8")
        roda(alunos, home)
        dps2 = lista(home)
        mudou2 = {k for k in antes2 if dps2.get(k) != antes2[k]}
        novo_codigo = "maria-souza-v2" in dps2
        ok = not mudou2 and not novo_codigo
        print(f"     {'ok   ' if ok else 'FALHA'}  maria={dps2.get('maria-souza')} | -v2 ganhou código próprio: {novo_codigo} | renumerados: {sorted(mudou2) or 'nenhum'}")
        falhas += 0 if ok else 1

        print("\n3) SUMIÇO EM MASSA (árvore errada) -> tem de ABORTAR")
        antes3 = lista(home)
        for s in base[:3]:
            (alunos / f"{s}.html").unlink()
        r = roda(alunos, home)
        dps3 = lista(home)
        ok = r.returncode != 0 and dps3 == antes3
        print(f"     {'ok   ' if ok else 'FALHA'}  saiu={r.returncode} | lista intacta: {dps3 == antes3}")
        if r.stderr.strip():
            print("       " + r.stderr.strip().splitlines()[0])
        falhas += 0 if ok else 1

    print("\nGATE 33 " + ("OK — código de aluno não muda com entrada de gente nova.\n"
                          if not falhas else f"FALHOU — {falhas} cenário(s).\n"))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
