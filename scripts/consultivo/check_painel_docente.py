#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 65 — o painel do professor fala SOBRE o aluno, nunca COM ele.

O DEFEITO
---------
`PC_NOTAS` e o painel que so a URL do PROFESSOR abre: o "Por que" (`pq`) e o "Pode gerar
duvida" (`duvida`) de cada atividade do pre-class. Sao instrucoes de trabalho para quem vai
dar a aula. O aluno nao ve nada disso -- por desenho (GATE 49, duas URLs).

Medido em 09/09/2026, nos cinco materiais fora do molde: **61 desses campos estavam escritos
para o ALUNO**, em segunda pessoa.

    joice 10-1.duvida   "Voce nao precisa entender tudo. Precisa pegar quatro coisas..."
    caio  4-6.duvida    "Use a sua empresa de verdade."
    lucia 6-6.duvida    "Diga em voz alta com um relogio antes da aula."

Quem abre o painel le uma instrucao endereçada a outra pessoa, e tem de traduzi-la de
cabeca no meio da aula. Pior: "Diga em voz alta com um relogio" lido pelo professor vira
uma ordem para ELE fazer, que nao e o que a nota quer dizer.

A CORRECAO JA EXISTIA EM UM MATERIAL. A revisao da professora consertou isto na Vanessa em
#2509 (aula 1) e #2530 (aulas 2, 3 e 4) -- *"`PC_NOTAS` e painel do PROFESSOR e voltou a
falar com ele"* -- e nao alcancou os outros quatro, porque ninguem os revisou. O registro
certo e o dela: terceira pessoa para o aluno, imperativo para quem conduz.

    "Se ela perguntar a regra, nao de. Diga que e o que voces vao descobrir juntos."
    "Se ela marcar <em>is</em>, nao corrija com regra -- anote e leve para a etapa 4."

POR QUE ISTO NAO E O DETECTOR LEXICO QUE O A05 §10.2 PROIBE
-----------------------------------------------------------
O A05 §10.2 manda a suite REJEITAR um detector assim:

    "reprovar automaticamente toda ocorrencia de 'Do not' e confirmar que a suite rejeita
     esse detector lexical simplista"

O que ele proibe e julgar a QUALIDADE da linguagem por uma lista de expressoes -- decidir
que "Do not" e ruim sem olhar se a restricao era necessaria. Este gate nao julga qualidade
nenhuma: ele detecta o DESTINATARIO, que e uma classe gramatical FECHADA (os pronomes e
possessivos de 2a pessoa do singular do portugues) num painel cujo leitor e fixado pela
arquitetura. Nao ha contexto em que "voce" num painel que so o professor abre se refira ao
professor: se se referisse, a nota estaria mandando o PROFESSOR fazer o exercicio.

DUAS ISENCOES, e as duas tem razao estrutural
----------------------------------------------
1. **"voces" (plural) passa.** Inclui quem le. "Diga que e o que voces vao descobrir juntos"
   fala com o professor sobre o par professor-aluno, e esta certo.
2. **Texto entre aspas ou em `<em>` nao conta.** E lingua CITADA -- a frase que o professor
   vai dizer ao aluno, ou o enunciado que esta na tela. Citar "voce nao precisa entender
   tudo" como o que se diz ao aluno e diferente de escrever isso como instrucao.
   Medido: a isencao nao esconde nenhum dos 61 -- todos apareciam fora de citacao tambem.

ESCOPO: `_build/consultivo/{slug}/aula*/notas.json`, que e de onde o painel e emitido.

USO:
    python3 scripts/consultivo/check_painel_docente.py [dir ...]
    python3 scripts/consultivo/check_painel_docente.py --selftest
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# Os campos do painel. Sao os dois que o professor le; o resto da nota e do emissor.
CAMPOS = ("pq", "duvida")

# 2a pessoa do SINGULAR. `voces` fica de fora de proposito (ver isencao 1) -- por isso o
# `(?!s)` depois de `voce`, e nao um `\b` que casaria com o plural.
SEGUNDA_PESSOA = re.compile(r"\b(voc[eê](?!s)|seu|sua|seus|suas|teu|tua|teus|tuas)\b", re.I)

RX_CITACAO = (re.compile(r"<em>.*?</em>", re.S),
              re.compile(r"&ldquo;.*?&rdquo;", re.S),
              re.compile(r"“.*?”", re.S),
              re.compile(r'".*?"', re.S))


def fora_de_citacao(texto):
    """O texto sem a lingua CITADA — o que sobra e a instrucao propriamente dita."""
    for rx in RX_CITACAO:
        texto = rx.sub(" ", texto)
    return texto


def confere(pasta):
    falhas = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "aula*", "notas.json"))):
        try:
            notas = json.load(open(caminho, encoding="utf-8"))
        except Exception as e:
            falhas.append(f"{os.path.relpath(caminho, RAIZ)}: nao e JSON valido ({e}).")
            continue
        rel = os.path.relpath(caminho, RAIZ)
        for tela, dados in notas.items():
            if not isinstance(dados, dict):
                continue
            for campo in CAMPOS:
                texto = dados.get(campo) or ""
                m = SEGUNDA_PESSOA.search(fora_de_citacao(texto))
                if m:
                    falhas.append(
                        f"{rel}: {tela}.{campo} trata o ALUNO por {m.group(0)!r}. "
                        f"O painel e do professor — escreva sobre o aluno em terceira "
                        f"pessoa e com ele no imperativo. Trecho: {texto.strip()[:100]}")
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
        print(f"\n{VERMELHO}GATE 65 REPROVOU{ZERA} — {len(falhas)} campo(s) do painel do "
              f"professor endereçados ao aluno.")
        return 1
    print(f"{VERDE}GATE 65 OK{ZERA} — {medidos} material(is): o painel do professor fala "
          f"sobre o aluno, e com quem conduz.")
    return 0


def selftest():
    casos = [
        ("terceira pessoa — o registro certo", False,
         {"1-1": {"pq": "Ela tende a achar que precisa entender a frase inteira."}}),
        ("imperativo para quem conduz", False,
         {"1-1": {"duvida": "Se ela marcar <em>is</em>, nao corrija com regra — anote."}}),
        ("segunda pessoa na instrucao", True,
         {"1-1": {"duvida": "Voce nao precisa entender tudo."}}),
        ("possessivo de segunda pessoa", True,
         {"1-1": {"pq": "Use a sua empresa de verdade."}}),
        ("'voces' inclui quem le — passa", False,
         {"1-1": {"duvida": "Diga que e o que voces vao descobrir juntos."}}),
        ("lingua citada entre aspas — passa", False,
         {"1-1": {"pq": "Se ela travar, diga “voce nao precisa entender tudo” e siga."}}),
        ("lingua citada em <em> — passa", False,
         {"1-1": {"duvida": "<em>How do you spell your name?</em> resolve o impasse."}}),
        ("campo que nao e do painel nao e medido", False,
         {"1-1": {"pq": "Ela abre a tela.", "outro": "Voce faz o exercicio."}}),
    ]
    import tempfile
    erros = 0
    for nome, deve, notas in casos:
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "aula1"))
            with open(os.path.join(d, "aula1", "notas.json"), "w", encoding="utf-8") as fh:
                json.dump(notas, fh, ensure_ascii=False)
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
