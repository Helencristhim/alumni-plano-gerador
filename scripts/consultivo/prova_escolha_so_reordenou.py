#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A prova de que o embaralhamento do `escolha` REORDENOU e nao REESCREVEU.

POR QUE ISTO EXISTE
-------------------
O PR que ligou o embaralhamento (11/09/2026) reconstroi os 14 arquivos publicados dos 7
materiais da anatomia -- e nao so o do aluno cuja aula foi pedida. O `--retrofit` do Dan
depende de uma medicao, nao de uma promessa: `git diff` dos outros 6 mostra centenas de
linhas trocadas, e olhar para ele nao distingue "as mesmas frases em outra ordem" de "uma
frase reescrita".

Este script responde a UNICA pergunta que decide isso, arquivo por arquivo e bloco por
bloco: o CONJUNTO de itens de cada `escolha` continua o mesmo, e cada `data-ok` continua
colado no MESMO texto?

  - item que sumiu, item que apareceu    -> FALHA
  - texto alterado, mesmo que um caractere -> FALHA (o item vira "novo" e outro "sumido")
  - resposta que trocou de item          -> FALHA
  - os mesmos itens em outra ordem       -> passa, e e o que o PR faz

USO:
    python3 scripts/consultivo/prova_escolha_so_reordenou.py <ref-git>
    python3 scripts/consultivo/prova_escolha_so_reordenou.py origin/main
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"
MARCA = 'name="alumni-anatomia" content="consultivo"'


def blocos(t):
    """{id do quiz-options: {texto do item: data-ok}}, lido pelo BALANCO de <div>."""
    fora = {}
    for m in re.finditer(r'<div class="quiz-options" id="([^"]+)">', t):
        nivel, i = 1, m.end()
        for d in re.finditer(r"<div\b|</div>", t[m.end():]):
            nivel += 1 if d.group(0) == "<div" else -1
            if nivel == 0:
                i = m.end() + d.start()
                break
        corpo = t[m.end():i]
        itens = {}
        for o in re.finditer(r'<div class="quiz-option" data-ok="([01])" onclick="tog\(this\)">'
                             r'<span>(.*?)</span></div>', corpo, re.S):
            itens[o.group(2)] = o.group(1)
        fora[m.group(1)] = itens
    return fora


def main(ref):
    alvos = sorted(p for sub in ("professor", "aluno")
                   for p in __import__("glob").glob(
                       os.path.join(RAIZ, "public", sub, "*.html"))
                   if MARCA in open(p, encoding="utf-8", errors="replace").read(4000))
    ruim = 0
    for p in alvos:
        rel = os.path.relpath(p, RAIZ)
        antes = subprocess.run(["git", "-C", RAIZ, "show", f"{ref}:{rel}"],
                               capture_output=True, text=True)
        if antes.returncode:
            print(f"  {VERDE}novo{ZERA}   {rel} (nao existe em {ref})")
            continue
        a, b = blocos(antes.stdout), blocos(open(p, encoding="utf-8").read())
        sumiu = sorted(set(a) - set(b))
        nasceu = sorted(set(b) - set(a))
        linhas, movidos = [], 0
        for ident in sorted(set(a) & set(b)):
            if a[ident] != b[ident]:
                so_a = sorted(set(a[ident]) - set(b[ident]))
                so_b = sorted(set(b[ident]) - set(a[ident]))
                trocou = [k for k in set(a[ident]) & set(b[ident])
                          if a[ident][k] != b[ident][k]]
                linhas.append(f"    {ident}: item(ns) que sumiram={so_a} "
                              f"nasceram={so_b} resposta trocada={trocou}")
            elif list(a[ident]) != list(b[ident]):
                movidos += 1
        if sumiu or nasceu or linhas:
            ruim += 1
            print(f"  {VERMELHO}FALHA{ZERA}  {rel}")
            if sumiu or nasceu:
                print(f"    blocos que sumiram={sumiu} nasceram={nasceu}")
            print("\n".join(linhas))
        else:
            print(f"  {VERDE}ok{ZERA}     {rel}: {len(b)} bloco(s) escolha, {movidos} "
                  f"reordenado(s), 0 com texto ou resposta alterados")
    if ruim:
        print(f"\n{VERMELHO}A MUDANCA NAO E SO DE ORDEM{ZERA} — {ruim} arquivo(s).")
        return 1
    print(f"\n{VERDE}SO ORDEM{ZERA} — nos {len(alvos)} arquivos, todo `escolha` tem o MESMO "
          f"conjunto de itens e cada resposta continua colada ao mesmo texto.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "origin/main"))
