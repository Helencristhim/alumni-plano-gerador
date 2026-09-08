#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 61 — o pre-class PREPARA a aula; nao ENTREGA o que ela vai fazer descobrir.

O CASO
------
Revisao da professora sobre a aula 2 da Vanessa (PR #2526), palavra por palavra:

    "A atividade 3 era um `classificar` com badge Listening, sem audio, e trazia as TRES
     perguntas do balcao escritas num documento -- o transcript inteiro, antes da aula. O
     guia geral dizia que o transcript fica fechado ate a etapa 5, e ele ja estava aberto
     no pre-class desde a vespera."

O `talk.json` da aula 2 tem tres falas. As tres estavam no pre-class, com o nome de quem
diz cada uma. A aluna chegava a aula tendo LIDO o que ia ter de ESCUTAR: o exercicio de
listening virava conferencia de leitura, que e outra habilidade.

Catalogo do auditor (04/09/2026):

    PRO-006  Transcript liberado cedo -- BLOCKER
             "Em listening contrast, transcript aparece antes da tentativa ou da escuta que
              precisa ser puramente auditiva."
    SEQ-002  Descoberta apos clarificacao -- MAJOR
             "A regra/MPF e apresentada antes da tentativa de noticing ou descoberta."

O QUE O GATE MEDE, E ONDE ELE PARA
-----------------------------------
A fonte e o `talk.json` -- as falas que viram MP3 e que a aluna ouve na aula. A superficie
medida e o pre-class: as seccoes que o `preclass.html` daquela aula injeta, e so elas. O
post-class carrega o transcript de proposito (a aula ja aconteceu, e a #2526 mandou escrever
as tres perguntas ali, "com quem faz cada uma"), entao medir o arquivo inteiro reprovaria
justamente a correcao.

REPROVA quando o pre-class carrega **o audio inteiro** -- todas as falas, ou tres ou mais.
NAO reprova UMA fala solta. A diferenca nao e de grau, e de funcao:

  - uma linha escrita no pre-class e ESTIMULO: a aula 4 da Lucia mostra a pergunta do Ray
    ("Is that a hard date...?") para ela analisar por que a pergunta e confusa. A aula da
    ela nao e decodificar aquela frase, e responder a ela;
  - o audio inteiro escrito e o TRANSCRIPT: nao sobra nada para escutar.

Contado nas 24 aulas: Lucia 1/3 e 1/2 (estimulo), Vanessa 3/3 antes da correcao
(transcript). O corte separa os dois casos sem ninguem ter de julgar conteudo.

O QUE ELE NAO MEDE
------------------
Vocabulario e chunks. A REGRA 29 EXIGE que o pre-class previeja o lexico da aula; um gate
que reprovasse repeticao de palavra brigaria com a regra. Por isso a comparacao e por FALA
INTEIRA (>= 4 palavras), normalizada, e nao por termo.

Tambem nao mede o texto que gera audio: `abertura[].audio.texto` alimenta o `sayAs`, nao a
tela. O pre-class da aula 2 da Stephanie TEM a fala escrita nessa chave -- e a aluna nunca
a le, ela a escuta ali mesmo.

O QUE JA FOI CONSERTADO POR CAUSA DELE
--------------------------------------
Ao nascer, o gate encontrou duas aulas com o transcript no pre-class: a aula 2 do Caio (doc
"The call -- transcript", 4 de 4 falas) e a aula 10 da Joice ("The two introductions --
transcript", 2 de 2). As duas foram reescritas no mesmo PR, com autorizacao do Dan: a
operacao de cada atividade ficou, o conteudo do audio saiu.

  Caio a2  o `classificar` passou a distinguir figure/condition/opinion/decision em linhas
           de OUTRO negocio, e o `escolha` seguinte deixou de cobrar o conteudo da call
           para cobrar QUANDO vale interromper.
  Joice a10 o `classificar` passou a identificar as quatro pecas que TODA apresentacao tem,
           com falas de outras pessoas, e o `escolha` seguinte virou a decisao de que
           pergunta e segura fazer.

Nao ha lista de excecao: a partir daqui, audio inteiro no pre-class reprova.

ESCOPO: os fragmentos autorais, `_build/consultivo/{slug}/aula{n}/`. E ali que o defeito e
escrito -- a mesma superficie que o #2544 escolheu para a acentuacao.

USO:
    python3 scripts/consultivo/check_preclass_nao_entrega.py [dir ...]
    python3 scripts/consultivo/check_preclass_nao_entrega.py --selftest
"""
import glob
import html
import json
import os
import re
import sys
import tempfile
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, AMARELO, ZERA = "\033[32m", "\033[31m", "\033[33m", "\033[0m"

# Chaves que NAO sao tela do pre-class: apoio em portugues, painel do professor, e o texto
# que so existe para gerar MP3.
FORA = ("nota", "nota_pt", "rationale", "rationale_pt", "pt", "ptt", "audio")

# Minimo de palavras para uma fala contar. Abaixo disso ("Thank you.") a coincidencia diz
# mais sobre a lingua do que sobre o material.
MIN_PALAVRAS = 4

# Quantas falas ja sao "o audio inteiro" quando o audio e longo.
TETO_ABSOLUTO = 3

# Sem excecao. As duas que existiam foram consertadas (ver o cabecalho); no Black a
# excecao se escreve em codigo, com o caso e a razao, e nao ha caso.
PENDENTES = {}


def normal(t):
    t = re.sub(r"<[^>]+>", " ", str(t))
    t = html.unescape(t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9' ]", " ", t.lower())
    return re.sub(r" +", " ", t).strip()


def textos(o, acc):
    """Todo texto que o autor escreveu para a TELA, sem apoio, nota nem audio."""
    if isinstance(o, str):
        acc.append(o)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in FORA:
                continue
            textos(v, acc)
    elif isinstance(o, list):
        for v in o:
            textos(v, acc)


def seccoes_do_preclass(pasta):
    p = os.path.join(pasta, "preclass.html")
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as fh:
        return set(re.findall(r"<!--BLOCOS:([a-z0-9]+)-->", fh.read()))


def falas(pasta):
    p = os.path.join(pasta, "talk.json")
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        dados = json.load(fh)
    out = []
    for linha in dados if isinstance(dados, list) else []:
        t = normal(linha.get("t", "")) if isinstance(linha, dict) else ""
        if len(t.split()) >= MIN_PALAVRAS:
            out.append(t)
    return out


def confere(pasta):
    fala = falas(pasta)
    if len(fala) < 2:
        # Uma fala so: nao ha "audio inteiro" a entregar, e a fala unica e estimulo.
        return None
    secs = seccoes_do_preclass(pasta)
    bl = os.path.join(pasta, "blocos.json")
    if not secs or not os.path.exists(bl):
        return None
    with open(bl, encoding="utf-8") as fh:
        dados = json.load(fh)
    acc = []
    for sec in secs:
        textos(dados.get(sec), acc)
    pre = normal(" ".join(acc))
    dentro = [f for f in fala if f in pre]
    if len(dentro) == len(fala) or len(dentro) >= TETO_ABSOLUTO:
        return dentro, fala
    return None


def aulas(alvos):
    if alvos:
        return [a.rstrip("/") for a in alvos]
    return sorted(os.path.dirname(p) for p in
                  glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                                         "blocos.json")))


def chave(pasta):
    partes = pasta.replace("\\", "/").split("/")
    return "/".join(partes[-2:])


def main(argv):
    alvos = aulas(argv)
    falhas, perdoados, medidos = [], [], 0
    for pasta in alvos:
        if not os.path.isdir(pasta):
            continue
        medidos += 1
        r = confere(pasta)
        if not r:
            continue
        dentro, fala = r
        k = chave(pasta)
        msg = (f"{k}: o pre-class carrega {len(dentro)} das {len(fala)} falas do audio da "
               f"aula. Isto e o transcript entregue na vespera (PRO-006). Primeira: "
               f'"{dentro[0][:70]}..."')
        (perdoados if k in PENDENTES else falhas).append((k, msg))
    for k, m in perdoados:
        print(f"{AMARELO}PENDENTE{ZERA} {m}\n         -> {PENDENTES[k]}")
    for _, m in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {m}")
    if falhas:
        print(f"\n{VERMELHO}GATE 61 REPROVOU{ZERA} — {len(falhas)} aula(s) com o audio "
              f"escrito no pre-class. Uma fala solta como estimulo pode ficar; o audio "
              f"inteiro tem de sair da vespera.")
        return 1
    print(f"{VERDE}GATE 61 OK{ZERA} — {medidos} aula(s): o pre-class prepara a escuta sem "
          f"entrega-la" + (f" ({len(perdoados)} pendente(s) declarado(s))" if perdoados else ""))
    return 0


def selftest():
    """Prova que morde: o defeito plantado e a aula 2 da Vanessa antes do #2526."""
    casos = [
        ("audio inteiro no pre-class", True,
         [{"t": "Good morning. What is your name, please?"},
          {"t": "Thank you. And how many nights?"},
          {"t": "Would you like breakfast in the morning?"}],
         {"sec3": [{"kind": "classificar", "id": "cl2p", "abertura": [
             {"doc": {"titulo": "At the desk", "texto":
                      "<strong>Emma:</strong> Good morning. What is your name, please?<br>"
                      "<strong>Emma:</strong> Thank you. And how many nights?<br>"
                      "<strong>Clara:</strong> Would you like breakfast in the morning?"}}]}]}),
        ("uma fala como estimulo", False,
         [{"t": "I want to come back to the December thing, is that a hard date?"},
          {"t": "Six weeks of engineering for a requirement nobody has published yet."},
          {"t": "Can I ask which of the three markets asked for it first, please?"}],
         {"sec3": [{"kind": "escolha", "id": "vg4", "abertura": [
             {"doc": {"titulo": "Ray's question", "texto":
                      "I want to come back to the December thing, is that a hard date?"}}]}]}),
        ("a fala so gera audio, nao vai para a tela", False,
         [{"t": "Right, the coursebook. Peter, you had the strongest view last time."},
          {"t": "So start us off, and then we can hear the other side of it."}],
         {"sec3": [{"kind": "escolha", "id": "l1a2", "abertura": [
             "One line from the call. Listen once.",
             {"audio": {"grupo": "1", "texto":
                        "Right, the coursebook. Peter, you had the strongest view last time."}},
             {"audio": {"grupo": "2", "texto":
                        "So start us off, and then we can hear the other side of it."}}]}]}),
        ("o transcript no POST-class nao conta", False,
         [{"t": "Good morning. What is your name, please?"},
          {"t": "Thank you. And how many nights?"},
          {"t": "Would you like breakfast in the morning?"}],
         {"ev2": [{"kind": "classificar", "id": "ev2", "itens": [
             {"t": "Good morning. What is your name, please?"},
             {"t": "Thank you. And how many nights?"},
             {"t": "Would you like breakfast in the morning?"}]}]}),
    ]
    erros = 0
    for nome, deve, talk, blocos in casos:
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "talk.json"), "w", encoding="utf-8") as fh:
                json.dump(talk, fh)
            with open(os.path.join(d, "blocos.json"), "w", encoding="utf-8") as fh:
                json.dump(blocos, fh)
            with open(os.path.join(d, "preclass.html"), "w", encoding="utf-8") as fh:
                # so `sec3` e pre-class; `ev2` fica de fora, como no material real
                fh.write('<div id="pc1"><!--BLOCOS:sec3--></div>')
            pegou = confere(d) is not None
        marca = VERDE + "ok" + ZERA if pegou == deve else VERMELHO + "ERRO" + ZERA
        if pegou != deve:
            erros += 1
        print(f"  {marca}  {nome}: esperado {'FALHA' if deve else 'passa'}, "
              f"deu {'FALHA' if pegou else 'passa'}")
    print(("selftest OK" if not erros else f"selftest com {erros} erro(s)"))
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
