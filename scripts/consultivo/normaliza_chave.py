#!/usr/bin/env python3
"""Tira a previsibilidade da chave de um exercicio (PRO-009), sem tocar no conteudo.

O GATE 41 barra chave que se acerta pela POSICAO. Barrar so nao basta: quando eu mesmo
corrigi na mao, trocando "uma linha" de cada grade, uma grade de tres virou `b b b` -- todas
do mesmo lado, o defeito literal do catalogo. Corrigir isto a mao e como o autor escrever o
`data-ok` a mao: da certo ate nao dar.

Esta ferramenta faz a correcao SEM decidir nada de pedagogia:

- chave com ate DUAS respostas distintas (o classificar binario e o `par`): reordena os
  ITENS. Reordenar as opcoes nao adiantaria -- `A B A B` viraria `B A B A`, que alterna
  igual.
- chave com mais opcoes: reordena as OPCOES, procurando a ordem com menos pontos fixos.
  Os itens ficam onde estao, porque a ordem deles costuma ser a da conversa.

O padrao escolhido nunca e sorteado: a semente e o ID do exercicio. Sorteio deixaria o
build irreproduzivel, e um padrao fixo para todos e previsivel entre aulas -- quem decora na
aula 1 acerta na 4.

  python3 scripts/consultivo/normaliza_chave.py _build/consultivo/<slug> [--escreve]
"""
import glob
import itertools
import json
import os
import sys
import zlib


def padroes(n):
    """Ordens de dois valores que nao se adivinham: nem tudo igual, nem alternancia
    perfeita, nem tres seguidas, e equilibradas."""
    out = []
    for p in itertools.product([0, 1], repeat=n):
        if len(set(p)) == 1:
            continue
        if all(a != b for a, b in zip(p, p[1:])):
            continue
        if max(len(list(g)) for _, g in itertools.groupby(p)) > 2:
            continue
        if abs(sum(p) - n / 2) > 0.5:
            continue
        out.append(list(p))
    return out


def previsivel(seq):
    if len(seq) < 3:
        return False
    if len(set(seq)) == 1:
        return True
    if len(set(seq)) <= 2 and all(a != b for a, b in zip(seq, seq[1:])):
        return True
    if len(set(seq)) <= 2 and max(len(list(g)) for _, g in itertools.groupby(seq)) > 2:
        return True
    fixos = sum(1 for i, x in enumerate(seq) if x == i)
    return fixos >= 3 and fixos >= 2 * (len(seq) / max(len(set(seq)), 1))


def semente(ident, n):
    return zlib.crc32(ident.encode()) % max(n, 1)


def arruma(b):
    """Devolve True se mexeu. Nao toca em texto: so em ORDEM."""
    if b.get("kind") == "par":
        lados = [it["alts"].index(it["ok"]) for it in b["itens"]]
        if not previsivel(lados):
            return False
        pads = padroes(len(b["itens"]))
        if not pads:
            return False
        for it, q in zip(b["itens"], pads[semente(b["id"], len(pads))]):
            if it["alts"].index(it["ok"]) != q:
                it["alts"] = list(reversed(it["alts"]))
        return True

    if b.get("kind") == "completar":
        # Cada item tem os SEUS finais, entao nao ha lista comum a reordenar -- e por isso a
        # primeira versao desta ferramenta simplesmente desistia aqui. Errado: a chave de um
        # `completar` e a POSICAO do final certo dentro do proprio item, e ela pode ser
        # perfeitamente previsivel do mesmo jeito. Medido ao escrever a aula 9 do Luiz: as
        # quatro respostas certas eram a PRIMEIRA opcao, quatro vezes seguidas. O gate pegava
        # e a ferramenta mandava consertar a mao -- que e como nasceu o `b b b` que eu mesmo
        # produzi corrigindo pares no olho.
        seq = [it["alts"].index(it["ok"]) for it in b["itens"]]
        if not previsivel(seq):
            return False
        larguras = {len(it["alts"]) for it in b["itens"]}
        if larguras != {2} and larguras != {3}:
            return False
        n = larguras.pop()
        # Ordem alvo: a posicao do certo VARIA item a item, sem cair em ciclo obvio.
        alvo = [(zlib.crc32((b["id"] + str(i)).encode()) % n) for i in range(len(b["itens"]))]
        if len(set(alvo)) == 1:                      # semente infeliz: desloca um
            alvo[0] = (alvo[0] + 1) % n
        for it, q in zip(b["itens"], alvo):
            certo = it["ok"]
            resto = [x for x in it["alts"] if x != certo]
            it["alts"] = resto[:q] + [certo] + resto[q:]
        return True

    if b.get("kind") != "classificar":
        return False
    ops = b["opcoes"]
    seq = [ops.index(it["ok"]) for it in b["itens"]]
    if not previsivel(seq):
        return False

    if len(set(seq)) <= 2:
        # binario: reordena os ITENS para um padrao que nao se adivinha
        pads = padroes(len(b["itens"]))
        if not pads:
            return False
        alvo = pads[semente(b["id"], len(pads))]
        primeiro = seq[0]
        baldes = {0: [it for it in b["itens"] if ops.index(it["ok"]) == primeiro],
                  1: [it for it in b["itens"] if ops.index(it["ok"]) != primeiro]}
        if len(baldes[0]) != alvo.count(0) or len(baldes[1]) != alvo.count(1):
            alvo = next((p for p in pads if p.count(0) == len(baldes[0])), None)
            if alvo is None:
                return False
        b["itens"] = [baldes[q].pop(0) for q in alvo]
        return True

    # varias opcoes: reordena as OPCOES buscando zero ponto fixo
    melhor, nota = None, None
    for perm in itertools.islice(itertools.permutations(range(len(ops))), 5000):
        nova = [ops[i] for i in perm]
        s2 = [nova.index(it["ok"]) for it in b["itens"]]
        if previsivel(s2):
            continue
        f = sum(1 for i, x in enumerate(s2) if x == i)
        if nota is None or f < nota:
            melhor, nota = nova, f
        if f == 0:
            break
    if melhor is None:
        return False
    b["opcoes"] = melhor
    return True


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    escreve = "--escreve" in sys.argv
    raiz = argv[0] if argv else "."
    mudou = 0
    for p in sorted(glob.glob(os.path.join(raiz, "aula*", "blocos.json"))):
        d = json.load(open(p, encoding="utf-8"))
        toca = []
        for _, blocos in d.items():
            for b in blocos:
                if isinstance(b, dict) and arruma(b):
                    toca.append(b["id"])
        if toca:
            mudou += len(toca)
            print(f"  {os.path.basename(os.path.dirname(p))}: {', '.join(toca)}")
            if escreve:
                json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not mudou:
        print("  nenhuma chave previsivel.")
    elif not escreve:
        print("\n  (--escreve para aplicar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
