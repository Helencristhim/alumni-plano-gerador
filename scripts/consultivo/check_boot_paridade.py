#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 58 — o boot do ALUNO nao esquece construtor que o do PROFESSOR tem.

O INCIDENTE QUE CRIOU ESTE GATE (03/09/2026)
---------------------------------------------
O "Reset my answers" nao limpava nada na tela, nos SEIS materiais da anatomia. A causa:

    `preResetGo` so restaura `if(_preSnap[n]!==undefined)`, e o boot do ALUNO nunca chamou
    `preSnap()`.

No arquivo da aluna o mapa ficava vazio, a condicao era falsa, e o botao saia sem tocar numa
classe. Ele APAGAVA o armazenamento — entao a limpeza era real e invisivel — e as
alternativas conferidas seguiam verdes. Clicar em Check de novo "consertava", porque o
`classList.toggle('correct', sel&&ok)` recalculava sem `.sel`. Zero erro no console, todos os
gates verdes, e ninguem tinha como ver.

POR QUE ELE PODE ACONTECER DE NOVO
-----------------------------------
`deriva_aluno()` NAO filtra o boot do professor: ele o SUBSTITUI inteiro pela constante
`BOOT_ALUNO`, escrita a mao em `extrai_shell.py`. Sao DUAS LISTAS INDEPENDENTES de
construtores, e nada compara uma com a outra. Quem conserta o boot do professor nao e levado
a olhar o do aluno — e o do aluno e justamente o unico arquivo que o aluno abre.

O QUE ESTE GATE MEDE
--------------------
Toda funcao chamada no boot do professor tem de estar TAMBEM no `BOOT_ALUNO`, ou constar da
lista `SO_DO_PROFESSOR` abaixo, com o motivo escrito. Diferenca nao declarada REPROVA.

    A lista e o ponto: ela obriga a DECLARAR que a ausencia e proposital, em vez de deixar
    "esqueci" e "de proposito" com a mesma aparencia.

USO:
    python3 scripts/consultivo/check_boot_paridade.py
    python3 scripts/consultivo/check_boot_paridade.py --selftest
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHELL = os.path.join(RAIZ, "_build", "model", "shells", "consultivo.html")
EXTRATOR = os.path.join(RAIZ, "scripts", "consultivo", "extrai_shell.py")
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# Ausencias LEGITIMAS, cada uma com o motivo. Quem tirar algo do boot do aluno tem de
# escrever aqui POR QUE — e e essa frase que o proximo leitor vai cobrar.
SO_DO_PROFESSOR = {
    "deckInit":     "o deck (slides do in-class) nao existe no arquivo do aluno",
    "snapInit":     "copia dos slides; sem deck, nada a copiar",
    "lessonsPaint": "repinta o percurso e as etapas do cartao da aula, area docente",
    "akBuild":      "o painel de Answer Key e do professor (data-view=professor)",
    "avalBuild":    "a escala de avaliacao do aluno e preenchida PELO professor",
    "closeBuild":   "o recap e a escala de confianca sao construidos no deck",
    "tgModoAplica": "o modo Teacher's Guide nao existe na visao do aluno",
    "setView":      "no build do aluno a visao e CONSTANTE (P3 §3): nao se promove papel",
}
# palavras-chave da linguagem que a regex de chamada pega por engano
RUIDO = {"for", "if", "while", "switch", "catch", "function", "return"}


def chamadas(texto):
    return {m.group(1) for m in re.finditer(r"^\s*([A-Za-z_$][\w$]*)\(", texto, re.M)} - RUIDO


def boot_professor(shell):
    i = shell.index("document.addEventListener('DOMContentLoaded',function(){\n  deckInit(")
    return shell[i:shell.index("\n});", i) + 4]


def boot_aluno(extrator):
    return re.search(r'BOOT_ALUNO = """(.*?)"""', extrator, re.S).group(1)


def confere(shell, extrator):
    prof = chamadas(boot_professor(shell))
    aluno = chamadas(boot_aluno(extrator))
    faltando = sorted(prof - aluno - set(SO_DO_PROFESSOR))
    # declarado como so-do-professor mas presente no aluno: a lista mentiu, e mentira em
    # lista de excecao e pior que ausencia — ela AUTORIZA o proximo esquecimento.
    mentira = sorted((set(SO_DO_PROFESSOR) & aluno))
    return faltando, mentira


def main():
    if "--selftest" in sys.argv:
        return selftest()
    shell = io.open(SHELL, encoding="utf-8").read()
    extrator = io.open(EXTRATOR, encoding="utf-8").read()
    faltando, mentira = confere(shell, extrator)
    print("=== GATE 58 — o boot do aluno nao esquece construtor do professor ===")
    if not faltando and not mentira:
        print(f"{VERDE}GATE 58 OK{ZERA} — os dois boots batem, e toda diferenca esta declarada.")
        return 0
    for f in faltando:
        print(f"  {VERMELHO}FAIL{ZERA}  `{f}()` roda no boot do PROFESSOR e nao no do ALUNO.")
        print(f"          Se a ausencia e proposital, declare em SO_DO_PROFESSOR com o motivo.")
        print(f"          Se nao e, o arquivo do aluno esta sem esse construtor — em silencio.")
    for f in mentira:
        print(f"  {VERMELHO}FAIL{ZERA}  `{f}()` esta em SO_DO_PROFESSOR mas TAMBEM roda no boot do aluno.")
        print(f"          A lista de excecao esta mentindo; corrija-a ou tire a chamada.")
    return 1


def selftest():
    """Prova que o gate morde: tirar preSnap do boot do aluno tem de reprovar."""
    shell = io.open(SHELL, encoding="utf-8").read()
    extrator = io.open(EXTRATOR, encoding="utf-8").read()
    assert confere(shell, extrator) == ([], []), "a base ja esta divergente"
    quebrado = extrator.replace("  preSnap();\n", "", 1)
    faltando, _ = confere(shell, quebrado)
    assert "preSnap" in faltando, f"nao mordeu: {faltando}"
    # e o outro lado: excecao que mente
    mentiroso = extrator.replace("  preKeys();", "  preKeys();\n  akBuild();", 1)
    _, mentira = confere(shell, mentiroso)
    assert "akBuild" in mentira, f"nao pegou a excecao mentirosa: {mentira}"
    print("GATE 58 selftest OK — pega o construtor esquecido E a excecao que mente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
