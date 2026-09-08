#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 69 — o item de atividade fechada diz POR QUE, ou entrega o apoio que promete.

O DEFEITO
---------
O molde e o material do Luiz dao uma explicacao a CADA item de `escolha` e `classificar`:
67/67 e 106/106. Cem por cento, nos dois. Medido em 09/09/2026 no resto da anatomia:

    caio-de-souza-amante      0/109        joice-lopes-leite       0/113
    lucia-nishiyama-serra     0/117        vanessa-aparecida       0/109

O aluno marca, confere, ve verde ou vermelho, e nao fica sabendo POR QUE. Um distrator so
ensina quando alguem diz o que ele estava testando; sem isso ele e uma pegadinha que
acertou ou nao acertou.

Nao e questao de nivel: os dois que tinham sao B1 e B1+, e o Caio e a Lucia sao B1.

A EXCECAO, E ELA E DECLARADA
-----------------------------
A Vanessa e a unica com `apoio.bilingue` no config. O apoio por item dela e o PORTUGUES
(`ptt`, 151 itens), decidido na revisao de 02/09: ela e real-beginner, e uma explicacao em
ingles seria "uma linha que ela pula". Entao o gate aceita as DUAS formas -- `porque` ou
`ptt` -- e o material bilingue satisfaz pela segunda.

O que ele NAO aceita e nenhuma das duas.

POR QUE `par` E `completar` FICAM DE FORA
------------------------------------------
Medido: o molde e o Luiz nao explicam item de `par` (0/30 e 0/24) nem quase nenhum
`completar` (3/3 num, 0/16 no outro). Faz sentido -- no `par` a resposta e uma palavra do
proprio vocabulario da aula, e nao ha distrator para desfazer. Cobrar ali seria inventar
uma regra que os dois materiais de referencia nao seguem.

ESCOPO: os blocos `escolha` e `classificar` dos fragmentos autorais do consultivo.

USO:
    python3 scripts/consultivo/check_item_explica.py [dir ...]
    python3 scripts/consultivo/check_item_explica.py --selftest
"""
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

KINDS = ("escolha", "classificar")


def blocos(obj):
    if isinstance(obj, dict):
        if "kind" in obj:
            yield obj
        for v in obj.values():
            yield from blocos(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from blocos(v)


def bilingue(pasta):
    """O config declara o modo? So ele decide -- nunca o nivel, nunca o conteudo."""
    try:
        d = json.load(open(os.path.join(pasta, "config.json"), encoding="utf-8"))
    except Exception:
        return False
    return bool((d.get("apoio") or {}).get("bilingue"))


def confere(pasta):
    falhas = []
    apoio_pt = bilingue(pasta)
    for caminho in sorted(glob.glob(os.path.join(pasta, "aula*", "blocos.json"))):
        try:
            dados = json.load(open(caminho, encoding="utf-8"))
        except Exception as e:
            falhas.append(f"{os.path.relpath(caminho, RAIZ)}: nao e JSON valido ({e}).")
            continue
        rel = os.path.relpath(caminho, RAIZ)
        for b in blocos(dados):
            if b.get("kind") not in KINDS:
                continue
            mudos = [i for i, it in enumerate(b.get("itens") or [], 1)
                     if isinstance(it, dict)
                     and not it.get("porque")
                     and not (apoio_pt and it.get("ptt"))]
            if mudos:
                como = "`porque`, ou `ptt` (o material declara apoio bilingue)" if apoio_pt \
                    else "`porque`"
                falhas.append(
                    f"{rel}: o bloco {b.get('id', '?')!r} ({b['kind']}) tem "
                    f"{len(mudos)} item(ns) sem {como} — itens {mudos[:6]}. O aluno confere "
                    f"e nao fica sabendo por que.")
    return falhas


def alunos(alvos):
    if alvos:
        return [a.rstrip("/") for a in alvos]
    return sorted(os.path.dirname(p) for p in
                  glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json")))


def main(argv):
    falhas, medidos = [], 0
    for pasta in alunos(argv):
        if not os.path.isdir(pasta):
            continue
        medidos += 1
        falhas += confere(pasta)
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 69 REPROVOU{ZERA} — {len(falhas)} bloco(s) com item que "
              f"nao explica nada.")
        return 1
    print(f"{VERDE}GATE 69 OK{ZERA} — {medidos} material(is): todo item de escolha e de "
          f"classificar diz por que, ou entrega o apoio que o config promete.")
    return 0


def selftest():
    import tempfile
    casos = [
        ("todos com `porque`", False, False,
         {"sec1": [{"kind": "escolha", "id": "a", "itens": [
             {"t": "x", "ok": True, "porque": "Yes. Porque sim."},
             {"t": "y", "ok": False, "porque": "No &mdash; porque nao."}]}]}),
        ("um item mudo", True, False,
         {"sec1": [{"kind": "escolha", "id": "a", "itens": [
             {"t": "x", "ok": True, "porque": "Yes."}, {"t": "y", "ok": False}]}]}),
        ("`ptt` NAO basta sem o modo declarado", True, False,
         {"sec1": [{"kind": "classificar", "id": "a", "itens": [
             {"t": "x", "ok": "u", "ptt": "Traducao."}]}]}),
        ("`ptt` basta quando o config declara o modo", False, True,
         {"sec1": [{"kind": "classificar", "id": "a", "itens": [
             {"t": "x", "ok": "u", "ptt": "Traducao."}]}]}),
        ("`par` fica de fora, por medicao", False, False,
         {"sec1": [{"kind": "par", "id": "a", "itens": [{"t": "x", "ok": "u"}]}]}),
        ("`completar` fica de fora", False, False,
         {"sec1": [{"kind": "completar", "id": "a", "itens": [{"t": "x", "ok": "u"}]}]}),
    ]
    erros = 0
    for nome, deve, decl, blocos_ in casos:
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "aula1"))
            cfg = {"apoio": {"bilingue": True}} if decl else {}
            json.dump(cfg, open(os.path.join(d, "config.json"), "w", encoding="utf-8"))
            json.dump(blocos_, open(os.path.join(d, "aula1", "blocos.json"), "w",
                                    encoding="utf-8"), ensure_ascii=False)
            pegou = bool(confere(d))
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
