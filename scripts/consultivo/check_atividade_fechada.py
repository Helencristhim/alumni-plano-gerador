#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 62 — a atividade fechada e uma ESCOLHA: ha o que errar, e a conta fecha.

OS CASOS (todos da revisao da professora sobre a Vanessa)
---------------------------------------------------------
1. Aula 1, tela 2 (PR #2509): "a lista tinha so as quatro respostas certas -- entraram tres
   que nao pertencem a uma reserva, para a pergunta voltar a ser uma pergunta." Marcar as
   corretas quando TODAS sao corretas nao mede nada.

2. Aula 4, atividade 4 (PR #2536): "cinco itens com a MESMA resposta (<em>Can I have</em>)
   nao e escolha, e repeticao do mesmo chunk."

3. Aula 1, atividade 6 (PR #2509): "Atividade 6 dizia 'your four sentences' com CINCO
   frases: saiu a quinta." O enunciado dizia `Complete the four sentences.` e havia cinco.
   Catalogo: **REG-001 Contagem divergente, BLOCKER** -- "titulo, lead, TG, gabarito ou
   conclusao declara quantidade diferente dos itens reais". O GATE 46 ja cobre o REG-001 no
   audio ("a tela promete N falas"); este cobre o enunciado x os itens.

4. Aula 4, atividade 3 (PR #2536): "as seis falas estavam na ordem cronologica exata da
   resposta. Embaralhadas." Catalogo: **PRO-009 Sorting nao embaralhado, MAJOR**.

O QUE MUDOU JUNTO COM ESTE GATE
--------------------------------
O caso 4 NAO virou regra para o autor lembrar -- virou `embaralha()` no emissor
(`render.py`): a ordem do banco de gap-fill e a dos itens de um `classificar` sao decididas
por codigo, com semente estavel (o `ident` do bloco), e por isso nunca saem na ordem da
resposta. Foi medido antes: DOZE bancos nas 24 aulas listavam as palavras na ordem exata das
lacunas, em cinco alunos diferentes. A REGRA 24 do imersivo ja mandava embaralhar desde
sempre; nao adiantou, porque dependia de alguem lembrar.

O gate confere o resultado -- na TELA, nao na declaracao. Se alguem tirar o embaralhamento
do emissor, ele acusa.

DUAS SUPERFICIES, E A RAZAO DE CADA UMA
----------------------------------------
  fragmento (`blocos.json`)  o que o AUTOR escreveu: contraste, resposta repetida, contagem
                             declarada, resposta fora do banco. Sao decisoes de autoria, e o
                             fragmento e onde elas cabem.
  HTML publicado             a ORDEM DO BANCO: o que a aluna ve. Depois do embaralhamento
                             a ordem do fragmento nao diz mais nada sobre a tela.

A ordem do `classificar` fica com o GATE 41, que ja a mede em quatro formas. Aqui so entra
o banco do gap-fill, que ele nao alcanca.

O QUE ELE NAO MEDE
------------------
Se a pergunta vale a pena, se o distrator e plausivel, se a categoria faz sentido. Isso e
julgamento e continua com quem escreve a aula. O gate so pergunta se ha ESTRUTURA de
escolha: alternativa errada existindo, respostas diferentes entre si, conta fechando.

ESCOPO: `_build/consultivo/{slug}/aula{n}/` (fragmento) e o material com carimbo
`alumni-anatomia=consultivo` (ordem).

USO:
    python3 scripts/consultivo/check_atividade_fechada.py [dir ou arquivo ...]
    python3 scripts/consultivo/check_atividade_fechada.py --selftest
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
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"
ANATOMIA = "consultivo"

NUMERO = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}
# O numeral so conta quando um VERBO de tarefa o governa. "One of the two was written by..."
# e prosa; "Mark the three statements" e a conta da atividade. Sem esta amarra o detector
# achava tres divergencias que nao existiam (Caio a3, Joice a9, Lucia a3).
CONTAGEM = re.compile(r"\b(mark|choose|select|complete|write|match|order|put)\s+"
                      r"(?:the\s+|these\s+|your\s+)?(" + "|".join(NUMERO) + r")\b")

FECHADAS = ("escolha", "par", "completar", "classificar", "lacuna")


def normal(t):
    t = re.sub(r"<[^>]+>", " ", str(t))
    t = html.unescape(t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9' ]", " ", t.lower())
    return re.sub(r" +", " ", t).strip()


def seccoes_do_preclass(pasta):
    p = os.path.join(pasta, "preclass.html")
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as fh:
        return set(re.findall(r"<!--BLOCOS:([a-z0-9]+)-->", fh.read()))


def respostas_da_lacuna(itens):
    out = []
    for x in itens:
        s = x if isinstance(x, str) else (x.get("t", "") if isinstance(x, dict) else "")
        out += re.findall(r"\{([^|}]+)[|}]", s)
    return out


def no_banco(resposta, banco):
    """O banco pode trazer a forma com reticencias ("According to...") -- e apoio, nao
    gabarito colavel. Casa por prefixo nos dois sentidos."""
    r = normal(resposta)
    for b in banco:
        nb = normal(b).rstrip(". ")
        if not nb:
            continue
        if r == nb or r.startswith(nb) or nb.startswith(r):
            return True
    return False


def confere_fragmento(pasta):
    """As regras de AUTORIA, no pre-class daquela aula."""
    falhas = []
    bl = os.path.join(pasta, "blocos.json")
    if not os.path.exists(bl):
        return falhas
    secs = seccoes_do_preclass(pasta)
    with open(bl, encoding="utf-8") as fh:
        dados = json.load(fh)
    for sec in sorted(secs):
        for b in (dados.get(sec) or []):
            if not isinstance(b, dict) or b.get("kind") not in FECHADAS:
                continue
            ident = f"{os.path.basename(os.path.dirname(pasta))}/{os.path.basename(pasta)}" \
                    f" {sec}/{b.get('id')}"
            itens = b.get("itens") or []
            kind = b["kind"]

            if kind == "escolha":
                oks = [bool(i.get("ok")) for i in itens if isinstance(i, dict)]
                if oks and (all(oks) or not any(oks)):
                    falhas.append(f"{ident}: 'marque as corretas' com {sum(oks)} de "
                                  f"{len(oks)} corretas. Sem alternativa errada nao ha "
                                  f"escolha -- a pergunta nao e uma pergunta.")

            if kind in ("par", "completar"):
                oks = [normal(i.get("ok")) for i in itens if isinstance(i, dict)]
                if len(oks) >= 3 and len(set(oks)) == 1:
                    falhas.append(f"{ident}: {len(oks)} itens com a MESMA resposta "
                                  f"({oks[0][:40]!r}). Isso e repetir um chunk, nao escolher.")

            if kind == "lacuna" and b.get("banco"):
                fora = [r for r in respostas_da_lacuna(itens)
                        if not no_banco(r, b["banco"])]
                if fora:
                    falhas.append(f"{ident}: resposta que o banco nao oferece: "
                                  f"{fora[:2]!r}. Com banco na tela, a palavra que falta "
                                  f"nele e a que a aluna nao tem como achar.")

            aber = [x for x in (b.get("abertura") or b.get("instr") or [])
                    if isinstance(x, str)]
            m = CONTAGEM.search(normal(" ".join(aber)))
            if m:
                declarado = NUMERO[m.group(2)]
                real = (sum(1 for i in itens if isinstance(i, dict) and i.get("ok"))
                        if kind == "escolha" else len(itens))
                if real != declarado:
                    falhas.append(f"{ident}: o enunciado diz \"{m.group(1)} {m.group(2)}\" "
                                  f"e a atividade tem {real} (REG-001).")
    return falhas


def confere_ordem(caminho):
    """As regras de ORDEM, no HTML publicado -- o que a aluna ve."""
    falhas = []
    with open(caminho, encoding="utf-8") as fh:
        doc = fh.read()
    if f'name="alumni-anatomia" content="{ANATOMIA}"' not in doc[:4000]:
        return falhas
    rel = os.path.relpath(caminho, RAIZ)

    # A ordem do `classificar` NAO se mede aqui. O GATE 41 (`check_catalogo_auditor`,
    # r_resposta_previsivel) ja cobre PRO-009 na match-grid, e com mais formas do que eu
    # tinha escrito: permutacao identidade, alternancia perfeita e tres seguidas da mesma
    # categoria, alem do agrupamento. Duas regras medindo a mesma coisa dao duas respostas
    # a manter alinhadas. O que este PR acrescentou ali foi do lado do EMISSOR: `embaralha`
    # recusa as quatro formas, entao a ordem previsivel nao chega a ser escrita.

    # gap-fill: a ordem do banco nao pode ser a ordem das lacunas.
    for m in re.finditer(r'<div class="word-bank">.*?</div>\s*<div class="fill-list" id="([^"]+)">(.*?)</div>',
                         doc, re.S):
        bloco = doc[m.start():m.end()]
        banco = [normal(x) for x in re.findall(r"<em>(.*?)</em>",
                                               bloco[:bloco.find("fill-list")])]
        gaps = [normal(x) for x in re.findall(r'class="blank-input" data-ok="([^"]*)"',
                                              m.group(2))]
        if len(banco) >= 2 and banco == gaps:
            falhas.append(f"{rel} #{m.group(1)}: o banco esta na ordem exata das lacunas "
                          f"— preenche-se 1->1 sem ler (PRO-009).")
    return falhas


def alvos_padrao():
    aulas = sorted(os.path.dirname(p) for p in
                   glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                                          "blocos.json")))
    htmls = sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                   glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html")))
    return aulas, htmls


def main(argv):
    if argv:
        aulas = [a.rstrip("/") for a in argv if os.path.isdir(a)]
        htmls = [a for a in argv if a.endswith(".html")]
    else:
        aulas, htmls = alvos_padrao()
    falhas = []
    for pasta in aulas:
        falhas += confere_fragmento(pasta)
    medidos = 0
    for h in htmls:
        antes = len(falhas)
        falhas += confere_ordem(h)
        medidos += 1 if (len(falhas) > antes or _e_consultivo(h)) else 0
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 62 REPROVOU{ZERA} — {len(falhas)} atividade(s) fechada(s) "
              f"sem estrutura de escolha.")
        return 1
    print(f"{VERDE}GATE 62 OK{ZERA} — {len(aulas)} aula(s) e {medidos} arquivo(s): toda "
          f"atividade fechada tem o que errar, e a conta fecha.")
    return 0


def _e_consultivo(caminho):
    try:
        with open(caminho, encoding="utf-8") as fh:
            return f'name="alumni-anatomia" content="{ANATOMIA}"' in fh.read(4000)
    except OSError:
        return False


def selftest():
    frag = [
        ("lista sem alternativa errada", True,
         {"sec1": [{"kind": "escolha", "id": "kd1", "itens": [
             {"t": "Your name", "ok": True}, {"t": "The city", "ok": True},
             {"t": "The dates", "ok": True}]}]}),
        ("lista com distrator", False,
         {"sec1": [{"kind": "escolha", "id": "kd1", "itens": [
             {"t": "Your name", "ok": True}, {"t": "The weather today", "ok": False},
             {"t": "The dates", "ok": True}]}]}),
        ("cinco itens, a mesma resposta", True,
         {"sec1": [{"kind": "completar", "id": "cn1", "itens": [
             {"t": "a room", "alts": ["Can I have", "I am"], "ok": "Can I have"},
             {"t": "the password", "alts": ["Can I have", "I am"], "ok": "Can I have"},
             {"t": "breakfast", "alts": ["Can I have", "I am"], "ok": "Can I have"}]}]}),
        ("enunciado diz four, ha cinco", True,
         {"sec1": [{"kind": "lacuna", "id": "cz1",
                    "abertura": ["Complete the four sentences."],
                    "itens": ["My name {is|60px} Vanessa.", "I {am|60px} in Lisbon.",
                              "It {is|60px} from 14 October.", "Breakfast {is|60px} included.",
                              "It {is|60px} a room for two."]}]}),
        ("'one of the two' e prosa, nao contagem", False,
         {"sec1": [{"kind": "escolha", "id": "kd3", "abertura": [
             "You are going to read the same argument twice. One of the two was written "
             "by someone who signalled the moves.", "Mark the three statements that are true."],
             "itens": [{"t": "a", "ok": True}, {"t": "b", "ok": False},
                       {"t": "c", "ok": True}, {"t": "d", "ok": False},
                       {"t": "e", "ok": True}, {"t": "f", "ok": False}]}]}),
        ("banco com reticencias cobre a resposta", False,
         {"sec1": [{"kind": "lacuna", "id": "cz1",
                    "banco": ["According to...", "The syllabus says..."],
                    "itens": ["\"{According to the plan} , week seven.\"",
                              "\"{The syllabus says} twenty hours.\""]}]}),
        ("resposta que o banco nao tem", True,
         {"sec1": [{"kind": "lacuna", "id": "cz1", "banco": ["so that", "in order to"],
                    "itens": ["We moved it {because of the launch|120px}."]}]}),
    ]
    erros = 0
    for nome, deve, blocos in frag:
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "blocos.json"), "w", encoding="utf-8") as fh:
                json.dump(blocos, fh)
            with open(os.path.join(d, "preclass.html"), "w", encoding="utf-8") as fh:
                fh.write('<div id="pc1"><!--BLOCOS:sec1--></div>')
            pegou = bool(confere_fragmento(d))
        if pegou != deve:
            erros += 1
        print(f"  {(VERDE + 'ok' + ZERA) if pegou == deve else (VERMELHO + 'ERRO' + ZERA)}  "
              f"{nome}: esperado {'FALHA' if deve else 'passa'}, deu "
              f"{'FALHA' if pegou else 'passa'}")

    cab = '<meta name="alumni-anatomia" content="consultivo">'
    ordem = [
        ("banco na ordem das lacunas", True, cab +
         '<div class="word-bank"><span class="wb-rot">Use</span> <em>alpha</em> &middot; <em>beta</em></div>'
         '<div class="fill-list" id="cz1">'
         '<p class="chunk-line"><input class="blank-input" data-ok="alpha" placeholder="..."></p>'
         '<p class="chunk-line"><input class="blank-input" data-ok="beta" placeholder="..."></p>'
         '</div>'),
        ("banco embaralhado", False, cab +
         '<div class="word-bank"><span class="wb-rot">Use</span> <em>beta</em> &middot; <em>alpha</em></div>'
         '<div class="fill-list" id="cz1">'
         '<p class="chunk-line"><input class="blank-input" data-ok="alpha" placeholder="..."></p>'
         '<p class="chunk-line"><input class="blank-input" data-ok="beta" placeholder="..."></p>'
         '</div>'),
    ]
    for nome, deve, doc in ordem:
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                         encoding="utf-8") as fh:
            fh.write(doc)
            p = fh.name
        pegou = bool(confere_ordem(p))
        os.unlink(p)
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
