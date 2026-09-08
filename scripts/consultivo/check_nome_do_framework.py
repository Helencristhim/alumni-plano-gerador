#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 64 — o quarto framework tem UM nome, e a sigla nao volta.

A REGRA, E DE ONDE ELA VEM
---------------------------
Relatorio de Alteracoes Normativas do pacote Private Black, consolidacao de 02/09/2026,
ajuste 22:

    "Quarto framework tinha nomes hibridos e sigla -> Nome exclusivo: Personalized
     Real-World English; arquitetura de oito etapas nao foi alterada."

E, na secao 5 (testes e mutacoes especificados):

    "Nomenclatura: ocorrencia residual da sigla ou de forma hibrida do quarto framework
     reprova o novo material."

O Documento 06 repete a ordem: *"Usar exclusivamente Personalized Real-World English como
nome do quarto framework. Nao exibir sigla ou forma hibrida. IDs tecnicos legados so
permanecem por compatibilidade e nao orientam novos materiais."*

O QUE ESTAVA NA TELA
--------------------
Medido em 08/09/2026, antes do conserto: os SEIS materiais da anatomia mostravam a sigla.

    registro.js   `mod:'ESP'`  -> a etiqueta curta da aula, renderizada como "ESP / E1"
    registro.js   `fwNome:'ESP — Real World'`  -> a forma HIBRIDA, em cinco dos seis
    syllabus.html "ESP · Real-World English", "ESP · Real World", e a lista das quatro
                  modalidades terminando em "e ESP"

Um deles ja estava certo: o `fwNome` da Stephanie, que e o molde. Os outros cinco tinham
ficado para tras — a correcao chegou ao molde e nao aos materiais gerados antes dela.

A DISTINCAO QUE O GATE FAZ, E POR QUE
--------------------------------------
O proprio 06 preserva os identificadores tecnicos legados. Por isso este gate NAO mede
codigo: a classe CSS `mod-esp`, a variavel `--mod-esp` e o id `esp-real-world` no
`gates.json` continuam validos, porque ninguem os le na tela. O que ele mede e TEXTO
VISIVEL.

  proibido, porque aparece    `mod`, `fwNome`, celula de tabela, titulo, prosa do syllabus
  permitido, porque nao       classe CSS, custom property, id de framework, nome de arquivo

`Real-World` sozinho, na etiqueta curta, e o encurtamento do nome oficial — o mesmo que
`Reading`, `Listening` e `Grammar` sao para os outros tres. Nao e sigla nem hibrido: e a
primeira parte do nome, na mesma forma das irmas. Hibrido e misturar as duas coisas
("ESP — Real World"), e e isso que reprova.

ESCOPO: os fragmentos autorais, `_build/consultivo/{slug}/`. E ali que o nome e escrito.

USO:
    python3 scripts/consultivo/check_nome_do_framework.py [dir ...]
    python3 scripts/consultivo/check_nome_do_framework.py --selftest
"""
import glob
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

OFICIAL = "Personalized Real-World English"

# A sigla como PALAVRA. `\b` de um lado so nao basta: `mod-esp` e `--mod-esp` casariam.
SIGLA = re.compile(r"(?<![\w-])ESP(?![\w-])")

# Onde o nome e escrito para ser lido. `registro.js` e fragmento autoral, nao codigo do
# shell: dele saem `mod` e `fwNome`, que a tela imprime.
# Cada fragmento autoral, sem excecao de forma. A primeira versao desta lista esquecia
# `preclass.html` e `postclass.html` — e era justamente ali que a sigla estava viva, no
# cabecalho "Aula 04 · ESP / E1" que so a visao do professor mostra. Gate que nomeia uma
# regiao e mede outra passa verde sobre o defeito.
ALVOS = ("syllabus.html", "perfil.html", "planning-aluno.html", "registro.js",
         "cartao.json", "guia_telas.json", "guide.js", "blocos.json", "slides.html",
         "notas.json", "close.json", "preclass.html", "postclass.html", "talk.json")

# Formas hibridas ja vistas, para dar mensagem util em vez de so apontar a sigla.
HIBRIDAS = ("ESP — Real World", "ESP · Real World", "ESP · Real-World English",
            "ESP - Real World", "ESP/Real-World")


def linhas_com_sigla(caminho):
    fora = []
    with open(caminho, encoding="utf-8", errors="replace") as fh:
        for i, linha in enumerate(fh, 1):
            if SIGLA.search(linha):
                trecho = linha.strip()
                hib = next((h for h in HIBRIDAS if h in linha), None)
                fora.append((i, hib, trecho[:110]))
    return fora


def confere(pasta):
    falhas = []
    for nome in ALVOS:
        for caminho in glob.glob(os.path.join(pasta, nome)) + \
                       glob.glob(os.path.join(pasta, "aula*", nome)):
            for i, hib, trecho in linhas_com_sigla(caminho):
                rel = os.path.relpath(caminho, RAIZ)
                if hib:
                    falhas.append(f"{rel}:{i}: forma HIBRIDA {hib!r}. O nome e "
                                  f"{OFICIAL!r}, inteiro. Trecho: {trecho}")
                else:
                    falhas.append(f"{rel}:{i}: a sigla ESP aparece em texto que a tela "
                                  f"mostra. Use {OFICIAL!r} por extenso, ou 'Real-World' "
                                  f"na etiqueta curta. Trecho: {trecho}")
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
        print(f"\n{VERMELHO}GATE 64 REPROVOU{ZERA} — {len(falhas)} ocorrencia(s) da sigla "
              f"ou de forma hibrida do quarto framework.")
        return 1
    print(f"{VERDE}GATE 64 OK{ZERA} — {medidos} material(is): o quarto framework aparece "
          f"so pelo nome que a norma fixou.")
    return 0


def selftest():
    casos = [
        ("nome oficial", False, "registro.js",
         "{n:4,bloco:1,mod:'Real-World',cod:'E1',fwNome:'Personalized Real-World English',"),
        ("forma hibrida", True, "registro.js",
         "{n:4,bloco:1,mod:'Real-World',cod:'E1',fwNome:'ESP — Real World',"),
        ("sigla na etiqueta", True, "registro.js", "{n:4,mod:'ESP',cod:'E1',"),
        ("sigla na prosa do syllabus", True, "syllabus.html",
         "<p>As aulas 1-4 cobrem Reading, Listening, Grammar e ESP.</p>"),
        ("classe CSS legada nao reprova", False, "slides.html",
         '<span class="mod-tag mod-esp">04</span> e a var --mod-esp:#6E0C6F'),
        ("nome oficial na tabela", False, "syllabus.html",
         "<td>Personalized Real-World English</td>"),
    ]
    erros = 0
    for nome, deve, arquivo, conteudo in casos:
        with tempfile.TemporaryDirectory() as d:
            alvo = os.path.join(d, "aula4") if arquivo != "syllabus.html" else d
            os.makedirs(alvo, exist_ok=True)
            with open(os.path.join(alvo, arquivo), "w", encoding="utf-8") as fh:
                fh.write(conteudo)
            pegou = bool(confere(d))
        if pegou != deve:
            erros += 1
        print(f"  {(VERDE + 'ok' + ZERA) if pegou == deve else (VERMELHO + 'ERRO' + ZERA)}  "
              f"{nome}: esperado {'FALHA' if deve else 'passa'}, deu "
              f"{'FALHA' if pegou else 'passa'}")
    print("selftest OK" if not erros else f"selftest com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
