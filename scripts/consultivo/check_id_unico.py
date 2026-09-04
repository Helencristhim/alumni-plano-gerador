#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 60 — dois elementos com o mesmo `id` no material.

DE ONDE ISTO VEIO (revisao da professora, 04/09/2026)
-----------------------------------------------------
    "Post-Class aulas 2, 3 e 4: ha o botao 'ver em portugues' no Lesson recap, mas nao ha
     o conteudo em portugues como na aula 1."

O conteudo estava la, nas quatro aulas. O que nao estava era o ENDERECO. O bloco de recap
declarava `"id": "conteudo"` nas quatro, e o emissor deriva dele o id do apoio em
portugues: quatro `<div id="conteudo-pt">` no MESMO documento. O botao chama
`toggleEl('conteudo-pt')`, `getElementById` devolve o PRIMEIRO, e o primeiro e o da aula 1
-- que esta noutra tela, escondida. Nas aulas 2, 3 e 4 o botao troca de rotulo e nada
aparece.

POR QUE NENHUM GATE VIU
-----------------------
O HTML e valido: id repetido nao e erro de sintaxe, e navegador nenhum reclama. O botao
compila (GATE 7 verde), o texto existe no arquivo (uma busca por ele acha), o contraste
esta certo, o portugues esta escrito. Cada gate olhou a peca que lhe cabia e todas estavam
la. O que faltava era a RELACAO entre duas delas.

E o mesmo erro de categoria que o proprio emissor ja tinha nomeado uma vez, no gravador
(`r_gravar`: "sem isso, dois gravadores na mesma aba comandam um ao outro"). A anatomia
inteira e UM documento, com todas as aulas dentro: id que o autor escreve por aula tem de
ser unico no ciclo, e nada obrigava.

O QUE ELE MEDE
--------------
No material publicado (`alumni-anatomia=consultivo`, professor e aluno): nenhum atributo
`id` de tag aparece duas vezes.

NO BLACK NAO HA ALVARA EM JSON (decisao do Dan, 03/09/2026)
-----------------------------------------------------------
    "se estamos no alumni-black, nao existe legado, tudo e corrigivel e PRECISA ser
     corrigido, nada vai ser entregue e ficar como esta simplesmente por darmos o nome de
     legado"

Entao nao ha arquivo de baseline. A unica excecao e a de baixo, escrita AQUI, com o caso e
a razao -- do mesmo jeito que o GATE 56 declara as dele.

A EXCECAO, E POR QUE ELA E TEMPORARIA
-------------------------------------
Quatro materiais emitem o gravador (ou a caixa de escrita) DUAS VEZES, com os mesmos ids:
o autor declarou o componente na `abertura` (`{"gravador": ...}` / `{"escrita": ...}`) num
bloco que JA e `kind: "gravar"` / `"escrever"` -- e o `kind` emite o componente de novo.
Sao duas rotas para a mesma peca, e usar as duas duplica.

Nao e cosmetico: o segundo par de botoes fica INERTE (o `rcStart` acha o primeiro), e na
Stephanie as duas caixas de escrita gravam em CHAVES DIFERENTES (`post_l1_writing` e
`post_pw1_writing`) -- a aluna escreve numa e o material guarda na outra.

Nao esta consertado aqui de proposito. O conserto exige decidir, POR MATERIAL, qual das
duas pecas fica: na Stephanie a `abertura` emite um e-mail (assunto + corpo) e o `kind`
emite uma caixa simples -- sao componentes DIFERENTES, e escolher entre eles e decisao de
conteudo em material que esta revisao nao pediu (REGRA 31). O caminho definitivo e o
emissor RECUSAR as duas rotas juntas, e ai esta lista morre.

USO:
    python3 scripts/consultivo/check_id_unico.py [arquivo.html ...]
    python3 scripts/consultivo/check_id_unico.py --selftest
"""
import collections
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARIMBO = '<meta name="alumni-anatomia" content="consultivo">'
VERDE, VERMELHO, AMARELO, ZERA = "\033[32m", "\033[31m", "\033[33m", "\033[0m"

# O componente emitido duas vezes (ver acima). Prefixo do id -> por que ele esta aqui.
# Cada entrada some quando o material for corrigido; nenhuma entra sem PR proprio.
PENDENTES = {
    "lucia-nishiyama-serra-c1": ("rec3", "rec4", "rec5", "rec6"),
    "luiz-bressane-ciclo1": ("rec10", "rec11", "rec12"),
    "stephanie-vicente": ("rec1", "rec2", "rec3", "rec4",
                          "pw1", "pw2", "pw3", "pw4"),
}
# Os sufixos que o gravador e a caixa de escrita penduram no id do bloco.
SUFIXOS = ("-start", "-stop", "-time", "-player", "-done", "-msg", "-body", "-count")

# So o atributo `id` de uma tag. `id` dentro de string de JS ou de JSON nao e elemento.
RX_ID = re.compile(r'<[a-zA-Z][^>]*?\sid="([^"]+)"')


def duplicados(html):
    """Os ids que aparecem mais de uma vez, e quantas vezes."""
    c = collections.Counter(RX_ID.findall(html))
    return {k: n for k, n in sorted(c.items()) if n > 1}


def tolerado(nome_do_arquivo, ident):
    """E uma das duplicatas do componente emitido duas vezes, naquele material?"""
    for prefixo in PENDENTES.get(nome_do_arquivo, ()):
        if any(ident == prefixo + s for s in SUFIXOS):
            return True
    return False


def materiais():
    fora = []
    for sub in ("professor", "aluno"):
        pasta = os.path.join(RAIZ, "public", sub)
        if not os.path.isdir(pasta):
            continue
        for nome in sorted(os.listdir(pasta)):
            if not nome.endswith(".html"):
                continue
            caminho = os.path.join(pasta, nome)
            with open(caminho, encoding="utf-8") as fh:
                if CARIMBO in fh.read(4000):
                    fora.append(caminho)
    return fora


def roda(alvos):
    fora, pendentes = [], 0
    for caminho in alvos:
        rel = os.path.relpath(caminho, RAIZ)
        base = os.path.basename(caminho)[:-5]
        with open(caminho, encoding="utf-8") as fh:
            dups = duplicados(fh.read())
        for ident, n in dups.items():
            if tolerado(base, ident):
                pendentes += 1
                continue
            fora.append(f"{rel}: id=\"{ident}\" aparece {n}x. `getElementById` devolve o "
                        f"primeiro — os outros ficam inertes.")
    if fora:
        print(f"{VERMELHO}GATE 60 — id repetido ({len(fora)}){ZERA}", file=sys.stderr)
        for linha in fora:
            print(f"  {linha}", file=sys.stderr)
        return 1
    print(f"{VERDE}GATE 60 OK{ZERA} — {len(alvos)} material(is), nenhum id repetido novo.")
    if pendentes:
        print(f"{AMARELO}  {pendentes} id(s) do componente emitido duas vezes seguem "
              f"pendentes em {len(PENDENTES)} material(is) — ver PENDENTES no cabecalho.{ZERA}")
    return 0


def selftest():
    falhas = []
    if duplicados('<div id="a"></div><p id="a"></p>') != {"a": 2}:
        falhas.append("nao viu o id repetido")
    if duplicados('<div id="a"></div><p id="b"></p>'):
        falhas.append("acusou ids distintos")
    if duplicados('<script>var id="a";var id="a";</script>'):
        falhas.append("confundiu string de JS com atributo")
    if duplicados('<div class="x" data-k="y" id="a"></div><span id="a"></span>') != {"a": 2}:
        falhas.append("nao achou o id depois de outros atributos")
    if not tolerado("stephanie-vicente", "pw1-body"):
        falhas.append("nao reconheceu a duplicata declarada em PENDENTES")
    if tolerado("stephanie-vicente", "conteudo-pt"):
        falhas.append("tolerou um id que nao e do componente pendente")
    if tolerado("vanessa-aparecida-ciclo1", "rec1-start"):
        falhas.append("aplicou a pendencia de um material a outro")
    if falhas:
        for f in falhas:
            print(f"{VERMELHO}selftest FALHOU{ZERA}: {f}", file=sys.stderr)
        return 1
    print(f"{VERDE}selftest OK{ZERA} — le o atributo de tag, poupa string de JS, e a "
          f"excecao vale so para o material e o componente que ela nomeia.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    args = [os.path.abspath(a) for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(roda(args or materiais()))
