#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 67 — a etiqueta da atividade diz o que a atividade E.

O DEFEITO
---------
A revisao da professora, na aula 2 da Vanessa (#2526):

    "A atividade 3 era um `classificar` com badge **Listening**, sem audio."

Ela consertou aquela. Medido em 09/09/2026 no resto da anatomia, **duas continuavam**, as
duas na Lucia -- aluna que nunca foi revisada:

    aula4 `vg4`  badge "Listening"; a abertura e um `doc` com a pergunta ESCRITA
    aula6 `md6`  badge "Listening"; a abertura e um `doc`, e a propria instrucao diz
                 "You will hear one answer IN CLASS" -- ou seja, aqui nao ha o que ouvir

O aluno abre o pre-class, ve a etiqueta que promete escuta, e encontra um texto. A
etiqueta e a primeira coisa que ele le e a unica que resume a tarefa: quando ela mente, o
aluno acha que perdeu o audio.

A DISTINCAO QUE O MATERIAL JA FAZ
----------------------------------
O acervo tem DUAS etiquetas para escuta, e a diferenca entre elas e exatamente esta:

    "Listening"           a tarefa E ouvir -- e o audio esta na propria atividade
    "Before you listen"   a tarefa PREPARA a escuta, que acontece em aula

A segunda e usada nove vezes e esta sempre certa. Os dois blocos da Lucia foram para ela:
sao preparacao, e dizem isso. O terceiro bloco com "Listening" -- `gs10` do Luiz -- tem
dois `audio` na abertura e passa, porque ali a etiqueta e verdade.

POR QUE ISTO NAO E DETECTOR LEXICO (A05 §10.2)
-----------------------------------------------
Nao ha julgamento de linguagem aqui. `badge` e um campo DECLARADO do bloco, com um valor
que o proprio material usa como rotulo de tipo, e `audio` e um filho DECLARADO da abertura.
A regra e uma implicacao entre duas declaracoes do autor: se voce rotulou de escuta, tem de
haver o que ouvir. O A05 proibe reprovar uma EXPRESSAO por estar numa lista; aqui nao se
lê prosa nenhuma.

ESCOPO: os blocos dos fragmentos autorais do consultivo.

USO:
    python3 scripts/consultivo/check_etiqueta_verdadeira.py [dir ...]
    python3 scripts/consultivo/check_etiqueta_verdadeira.py --selftest
"""
import glob
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# A etiqueta que afirma que a tarefa E ouvir. "Before you listen" diz o contrario -- que a
# escuta vem depois -- e por isso nao entra aqui.
ETIQUETA_DE_ESCUTA = {"Listening"}
ALTERNATIVA = "Before you listen"


def tem_audio(bloco):
    """A abertura carrega um `audio`? E ali que o player e declarado."""
    def procura(o):
        if isinstance(o, dict):
            if "audio" in o:
                return True
            return any(procura(v) for v in o.values())
        if isinstance(o, list):
            return any(procura(v) for v in o)
        return False
    return procura(bloco.get("abertura", []))


def blocos(obj):
    if isinstance(obj, dict):
        if "kind" in obj:
            yield obj
        for v in obj.values():
            yield from blocos(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from blocos(v)


def confere(pasta):
    falhas = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "aula*", "blocos.json"))):
        try:
            dados = json.load(open(caminho, encoding="utf-8"))
        except Exception as e:
            falhas.append(f"{os.path.relpath(caminho, RAIZ)}: nao e JSON valido ({e}).")
            continue
        rel = os.path.relpath(caminho, RAIZ)
        for b in blocos(dados):
            if str(b.get("badge", "")) in ETIQUETA_DE_ESCUTA and not tem_audio(b):
                falhas.append(
                    f"{rel}: o bloco {b.get('id', '?')!r} ({b.get('kind', '?')}) tem a "
                    f"etiqueta {b['badge']!r} e nenhum `audio` na abertura. Ou o audio "
                    f"entra, ou a etiqueta e {ALTERNATIVA!r} — que e o que o material usa "
                    f"quando a escuta acontece em aula.")
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
        print(f"\n{VERMELHO}GATE 67 REPROVOU{ZERA} — {len(falhas)} atividade(s) rotuladas "
              f"como escuta sem nada para ouvir.")
        return 1
    print(f"{VERDE}GATE 67 OK{ZERA} — {medidos} material(is): toda atividade rotulada como "
          f"escuta tem o audio dentro dela.")
    return 0


def selftest():
    AUD = {"audio": {"grupo": "1", "voz": "f", "texto": "x"}}
    casos = [
        ("Listening com audio", False,
         {"kind": "escolha", "id": "a", "badge": "Listening", "abertura": ["t", AUD]}),
        ("Listening sem audio", True,
         {"kind": "escolha", "id": "a", "badge": "Listening",
          "abertura": [{"doc": {"titulo": "t", "texto": "x"}}, "Mark three."]}),
        ("Before you listen sem audio — e o certo", False,
         {"kind": "escolha", "id": "a", "badge": "Before you listen",
          "abertura": [{"doc": {"titulo": "t", "texto": "x"}}]}),
        ("Reading sem audio", False,
         {"kind": "classificar", "id": "a", "badge": "Reading", "abertura": ["t"]}),
        ("sem etiqueta", False, {"kind": "par", "id": "a", "abertura": ["t"]}),
        ("audio aninhado fundo na abertura", False,
         {"kind": "escolha", "id": "a", "badge": "Listening",
          "abertura": [{"grupo": [AUD]}]}),
    ]
    import tempfile
    erros = 0
    for nome, deve, bloco in casos:
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "aula1"))
            with open(os.path.join(d, "aula1", "blocos.json"), "w", encoding="utf-8") as fh:
                json.dump({"sec1": [bloco]}, fh)
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
