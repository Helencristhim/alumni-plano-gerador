#!/usr/bin/env python3
"""LIBERA DISCO NO BUILD DA VERCEL — apaga o .git EFEMERO do container.

POR QUE ISTO EXISTE (21/09/2026)
--------------------------------
Os tres builds de preview de 21/09 morreram assim, todos depois de ~10 minutos:

    Error: ENOSPC: no space left on device, open '/vercel/output/config.json'
    1 files larger than 100 MB detected on disk:
      7700 MB : .git/objects/pack/pack-26e0de6f....pack
    Output files: 8060 MB

O container nao tem disco para as tres coisas ao mesmo tempo:

    clone (.git)      7,7 GB
    checkout          9,1 GB   (public/audio = 7,75 GB em 116.738 MP3)
    /vercel/output    8,1 GB   (copia de public/ que a Vercel monta no fim)

O build de producao de 18/09 ainda caiu dentro do disco; com o material que entrou
depois, nao cabe mais. O ENOSPC estoura na hora de escrever /vercel/output, ou seja
DEPOIS do buildCommand — e nessa altura o .git ja nao serve para nada, porque o
deploy publica o CONTEUDO DO DISCO, nao o repositorio.

NAO e problema de historico. Reescrever historico (BFG/filter-repo) nao devolveria
nada: o peso e o conteudo ATUAL do main, nao versoes antigas.

O QUE ISTO FAZ
--------------
Roda como ULTIMO passo do buildCommand (depois de todos os gates, para nao mudar o
comportamento de nenhum deles — `check_lesson_integrity.py` consulta `git ls-files`)
e apaga o diretorio .git do container, devolvendo ~7,7 GB antes da Vercel montar a
saida.

TRAVAS (este script NAO PODE apagar .git de lugar nenhum que nao seja o container)
---------------------------------------------------------------------------------
So age se as tres condicoes forem verdadeiras ao mesmo tempo:
  1. a variavel VERCEL esta definida (a Vercel define VERCEL=1 no build);
  2. o repositorio esta debaixo de /vercel (o container clona em /vercel/path0);
  3. o .git e um diretorio de verdade nesse caminho.
Fora disso: nao faz nada e diz por que. E NUNCA derruba o build (sai sempre 0) —
um passo de limpeza que reprova deploy legitimo seria pior que o problema.
"""
import os
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GIT_DIR = os.path.join(ROOT, ".git")


def out(msg):
    print(f"[libera-disco] {msg}", flush=True)


def gb(n):
    return f"{n / 1_073_741_824:.2f} GB"


def tamanho(caminho):
    total = 0
    for base, _, arquivos in os.walk(caminho):
        for a in arquivos:
            try:
                total += os.path.getsize(os.path.join(base, a))
            except OSError:
                pass
    return total


def main():
    if not os.environ.get("VERCEL"):
        out("fora da Vercel (VERCEL nao definida) — nao toco em nada.")
        return 0

    if not ROOT.startswith("/vercel"):
        out(f"repositorio fora de /vercel ({ROOT}) — nao toco em nada.")
        return 0

    if not os.path.isdir(GIT_DIR) or os.path.islink(GIT_DIR):
        out("sem .git no container — nada a liberar.")
        return 0

    livre_antes = shutil.disk_usage(ROOT).free
    peso = tamanho(GIT_DIR)
    out(f"livre antes: {gb(livre_antes)} | .git efemero: {gb(peso)}")

    try:
        shutil.rmtree(GIT_DIR)
    except Exception as e:
        out(f"nao consegui apagar o .git ({e.__class__.__name__}) — seguindo sem liberar.")
        return 0

    livre_depois = shutil.disk_usage(ROOT).free
    out(f"livre depois: {gb(livre_depois)} (+{gb(livre_depois - livre_antes)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
