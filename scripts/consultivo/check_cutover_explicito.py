#!/usr/bin/env python3
"""GATE 47 -- trocar o molde de um aluno e decisao, nunca efeito colateral.

O PERIGO
--------
O molde novo vai ser implantado AOS POUCOS, primeiro em alunos de teste, enquanto os
demais continuam tendo aula no material antigo -- pelo link que ja usam. Nesse periodo o
jeito mais facil de estragar a vida de um aluno e trivial: rodar o builder do consultivo
com a `fase` errada (ou sem `fase`) e sobrescrever `public/aluno/{slug}.html`. O comando e
o mesmo, o resultado passa em todos os gates de anatomia -- porque o arquivo novo esta
CERTO --, e o aluno abre o link de sempre e o material dele sumiu, no meio do contrato.

Nenhum gate existente pega isso. Todos perguntam "este arquivo esta bem formado?". Este
pergunta outra coisa: "este arquivo MUDOU DE ANATOMIA, e alguem decidiu isso?"

A TRAVA
-------
Um arquivo publicado que era IMERSIVO na base e aparece CONSULTIVO no PR so passa se o PR
disser `[cutover]` numa mensagem de commit. E a mesma forma do `[remove-ok]` da guarda do
main: a marca nao existe para liberar burocracia, existe para que a troca seja um ATO --
alguem digitou aquilo sabendo o que significa.

Durante o piloto nao ha o que marcar: `fase: "piloto"` escreve em `{slug}-ciclo{N}.html`, que e
arquivo NOVO. Arquivo novo nao muda anatomia de ninguem e nao precisa de marca.

    python3 scripts/consultivo/check_cutover_explicito.py [--base origin/main]
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARCA = 'name="alumni-anatomia" content="consultivo"'
AUTORIZA = "[cutover]"


def git(*a):
    return subprocess.run(["git", "-C", RAIZ, *a], capture_output=True, text=True).stdout


def anatomia_consultivo(texto):
    return MARCA in texto[:6000]


def main():
    base = "origin/main"
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]
    if not git("rev-parse", "--verify", base).strip():
        print(f"GATE 47 — base {base!r} nao existe aqui. Sem base nao ha o que comparar, e "
              f"passar verde sem comparar seria pior que falhar.")
        return 1

    mudados = [x for x in git("diff", "--name-only", "--diff-filter=M", f"{base}...HEAD",
                              "--", "public/professor/*.html", "public/aluno/*.html").split()
               if x]
    viradas = []
    for caminho in mudados:
        antes = git("show", f"{base}:{caminho}")
        agora = ""
        p = os.path.join(RAIZ, caminho)
        if os.path.exists(p):
            agora = open(p, encoding="utf-8", errors="ignore").read(6000)
        if anatomia_consultivo(agora) and not anatomia_consultivo(antes):
            viradas.append(caminho)

    if not viradas:
        print(f"✓ GATE 47 — nenhum aluno mudou de molde neste PR ({len(mudados)} "
              f"arquivo(s) publicado(s) modificado(s)).")
        return 0

    mensagens = git("log", "--format=%B", f"{base}..HEAD")
    if AUTORIZA in mensagens:
        print(f"✓ GATE 47 — {len(viradas)} arquivo(s) mudaram para o molde consultivo, "
              f"e o commit diz {AUTORIZA}:")
        for v in viradas:
            print(f"    {v}")
        return 0

    print("GATE 47 — material publicado mudou de molde sem que ninguem tenha decidido "
          "isso.\n")
    for v in viradas:
        print(f"  {v}\n    era imersivo na base, esta consultivo neste PR.")
    print(f"\nO aluno abre o link de sempre e encontra outro material. Se ele ainda tem "
          f"aula no antigo, perdeu o material no meio do contrato.")
    print(f"\n  Era para ser PILOTO?  ponha \"fase\": \"piloto\" no config — o builder "
          f"escreve em {{slug}}-ciclo{{N}}.html, ao lado, sem encostar no atual.")
    print(f"  Era MESMO o cutover?  ponha {AUTORIZA} na mensagem do commit, e copie o hub "
          f"antigo para {{slug}}-anterior.html no MESMO PR, senao ele deixa de existir.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
