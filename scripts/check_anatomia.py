#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 20 — a anatomia tem o que ela declara ter.

POR QUE ISTO EXISTE (07/08/2026)
--------------------------------
A anatomia guided-discovery foi construida lendo um ARTEFATO de referencia, escrito fora do
sistema. Enquanto o porte acontecia, o artefato era a especificacao — e eu perdi peca duas
vezes por perguntar a coisa errada:

  - "a classe existe no shell?"   respondeu SIM para tudo, porque o shell e clone e carrega
                                  ate o CSS das pecas que a anatomia nao usa.
  - "eu preciso de componente novo?"  contei o que EU tinha usado, nao o que o artefato TEM.
                                  Resultado: dei duas aulas como prontas com um quadro de
                                  feedback que nao recebia texto.

Ordem do Dan (07/08/2026): "o artefato nao vai ser necessario quando o shell estiver
totalmente construido e completo".

Ele esta certo, e isso decide o desenho deste gate: ele confere o shell contra
`_build/model/anatomias.json` — a lista DECLARADA NO REPO — e NUNCA contra o artefato, que
mora fora do repo, nao existe no CI e cujo papel acabou. O artefato era ANDAIME.

O QUE ELE REPROVA
-----------------
  1. componente declarado cuja CLASSE sumiu do shell
  2. componente declarado cujo KIND sumiu do builder
  3. aba declarada que nao esta no shell (prof ou aluno)
  4. shell declarado que nao existe no disco

O que ele NAO faz: exigir que uma AULA use todos os componentes. Aula escolhe; anatomia
oferece. Perder a oferta e que e o defeito.

USO:
    python3 scripts/check_anatomia.py
    python3 scripts/check_anatomia.py --selftest
"""
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = os.path.join(RAIZ, "_build", "model", "anatomias.json")
BUILDER = os.path.join(RAIZ, "_build", "model", "build_from_model.py")


def le(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def verifica(inv, builder_src, ler=le):
    erros = []
    for nome, a in inv["anatomias"].items():
        arquivos = {}
        for chave in ("shell", "hub", "hub_aluno"):
            p = os.path.join(RAIZ, a[chave])
            if not os.path.exists(p):
                erros.append(f'{nome}: {chave} declarado nao existe no disco: {a[chave]}')
                continue
            arquivos[chave] = ler(p)

        shell = arquivos.get("shell", "")
        for comp, meta in a["componentes"].items():
            cls = meta["classe"]
            if not re.search(r'[.\'" ]' + re.escape(cls) + r'[\s{.,:\'"]', shell):
                erros.append(
                    f'{nome}: o componente "{comp}" e declarado ({meta["usos_no_artefato"]} usos '
                    f'na referencia) mas a classe .{cls} SUMIU do shell. '
                    f'Papel: {meta["papel"]}')
            kind = meta.get("kind")
            if kind and f"k == '{kind}'" not in builder_src:
                erros.append(
                    f'{nome}: o componente "{comp}" declara kind "{kind}", que nao existe no '
                    f'builder. O config poderia pedi-lo e o builder abortaria.')

        for aba in a.get("abas", []):
            if f'id="tab-{aba}"' not in arquivos.get("hub", ""):
                erros.append(f'{nome}: aba "{aba}" declarada e ausente do hub do professor.')
        for aba in a.get("abas_aluno", []):
            if f'id="tab-{aba}"' not in arquivos.get("hub_aluno", ""):
                erros.append(f'{nome}: aba "{aba}" declarada e ausente do hub do aluno.')
    return erros


def selftest():
    inv = json.loads(le(INV))
    builder = le(BUILDER)
    base = verifica(inv, builder)
    if base:
        print("SELFTEST INCONCLUSIVO — o inventario ja esta com erro:")
        for e in base:
            print("   -", e)
        return 1

    import copy
    falhou = False
    casos = []

    d = copy.deepcopy(inv)
    d["anatomias"]["guided-discovery"]["componentes"]["inventado"] = {
        "classe": "ic-nao-existe", "kind": "reveal", "usos_no_artefato": 1, "papel": "x"}
    casos.append(("classe sumida do shell", d, builder, "SUMIU do shell"))

    d = copy.deepcopy(inv)
    d["anatomias"]["guided-discovery"]["componentes"]["reveal"]["kind"] = "kind-que-nao-existe"
    casos.append(("kind sumido do builder", d, builder, "nao existe no\n     builder"
                  .replace("\n     ", " ")))

    d = copy.deepcopy(inv)
    d["anatomias"]["guided-discovery"]["abas"].append("aba-fantasma")
    casos.append(("aba declarada e ausente", d, builder, "ausente do hub do professor"))

    for rotulo, mut, bsrc, esperado in casos:
        erros = verifica(mut, bsrc)
        pegou = any(esperado in e for e in erros)
        print(f"  {'OK  ' if pegou else 'FALHA'}  {rotulo}")
        if not pegou:
            falhou = True
            print(f"         esperava {esperado!r}; veio: {erros[:2]}")

    # o gate tem de morder tambem quando a CLASSE some do shell de verdade
    real = le(os.path.join(RAIZ, inv["anatomias"]["guided-discovery"]["shell"]))
    def ler_mutante(p):
        s = le(p)
        return s.replace("ic-write", "xx-removida") if p.endswith("guided-discovery.html") else s
    erros = verifica(inv, builder, ler=ler_mutante)
    pegou = any("ic-write" in e for e in erros)
    print(f"  {'OK  ' if pegou else 'FALHA'}  componente removido do shell de verdade")
    falhou |= not pegou

    if falhou:
        print("\nSELFTEST FALHOU — o gate parou de morder.")
        return 1
    print("\nSELFTEST OK — os 4 casos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    inv = json.loads(le(INV))
    erros = verifica(inv, le(BUILDER))
    n = sum(len(a["componentes"]) for a in inv["anatomias"].values())
    print("=== GATE 20 — a anatomia tem o que declara ter ===")
    print(f"{len(inv['anatomias'])} anatomia(s), {n} componente(s) declarado(s)")
    if erros:
        for e in erros:
            print(f"  ERRO  {e}")
        return 1
    print("OK — nenhum componente declarado sumiu do shell ou do builder.")
    print("O artefato de referencia nao e mais consultado: a fonte e este inventario.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
