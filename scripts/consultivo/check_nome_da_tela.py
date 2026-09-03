#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 56 — o menu do deck chama cada tela pelo nome que a propria tela usa.

DE ONDE ISTO VEIO (revisao da professora, 03/09/2026)
-----------------------------------------------------
    "o nome do slide mudou de 'Say the four' para 'One word, or a sentence' mas no botao
     slides que mostra o menu para acessar cada slide, o nome ainda esta 'Say the four'"

O nome de uma tela esta escrito em DOIS lugares que ninguem obriga a concordar:

  - a `.stage-pill` da propria tela (`slides.html`), que e o que se ve projetado;
  - o `nav:[...]` do `registro.js`, que alimenta o menu lateral (`smBuild` -> `navLabel`) E
    o titulo da nota do professor (`aplica_guia_de_tela` -> `render.nota_de_tela`).

Numa revisao anterior a tela 5 da aula 1 da Vanessa foi renomeada no pill e o `nav` ficou
como estava. Resultado: o menu leva a uma tela que se chama outra coisa, e a nota que a
professora abre naquela tela vem com o titulo antigo. Nada quebra, nada avisa -- o material
so passa a mentir sobre si mesmo, em dois lugares de uma vez.

POR QUE UM GATE, E NAO DERIVAR UM DO OUTRO
------------------------------------------
Derivar seria melhor em principio (uma fonte nao diverge de si mesma), e nao cabe aqui: o
`nav` nomeia as DEZ telas e so oito tem pill -- a de abertura e a de fecho nao tem -- e ha
telas legitimas cujo pill traz o nome da ETAPA, nao o da tela, porque a etapa ocupa duas
telas. Derivar apagaria esses nomes proprios. Entao o gate cobra o que de fato importa:
onde os dois existem, eles dizem a mesma coisa.

O ALVARA (`nome-da-tela-baseline.json`)
---------------------------------------
Medido o repo inteiro, seis materiais ja divergem -- inclusive um com o `nav` DESLOCADO uma
posicao da tela 3 em diante (`luiz-bressane` aula 12), que e o mesmo defeito em serie. Sao
aulas ja dadas, e a REGRA 30 vale: nao se conserta o passado por conta propria. O alvara
congela o que existe hoje, e a divergencia so pode CAIR: qualquer par novo reprova na hora.

ESCOPO: o carimbo `alumni-anatomia=consultivo`. Gate novo nasce escopado.

USO:
    python3 scripts/consultivo/check_nome_da_tela.py [arquivo.html ...]
    python3 scripts/consultivo/check_nome_da_tela.py --selftest
    python3 scripts/consultivo/check_nome_da_tela.py --update   # so quando a lista CAIU
"""
import glob
import html as _html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "nome-da-tela-baseline.json")
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


RX_ENTRADA = re.compile(r"\n\s*(\d+):\{n:\1,bloco:")


def nomes_do_nav(js, n):
    """Os rotulos do menu daquela aula, do `nav:[...]` dentro da entrada `n:` de LESSONS.

    A entrada vai do proprio cabecalho ate o da PROXIMA aula (ou o fim do texto). Recortar
    assim, e nao por um fechamento de chave, e o que faz o gate valer para o material de uma
    aula so e para o de vinte, sem contar delimitador dentro de string."""
    ini = [(int(m.group(1)), m.start()) for m in RX_ENTRADA.finditer(js)]
    for k, (num, pos) in enumerate(ini):
        if num != n:
            continue
        fim = ini[k + 1][1] if k + 1 < len(ini) else len(js)
        nav = re.search(r"nav:\[(.*?)\]", js[pos:fim], re.S)
        return re.findall(r"'([^']*)'", nav.group(1)) if nav else []
    return []


def pills_por_tela(c, n):
    """(indice da tela na aula, nome no pill) — so as telas que TEM pill."""
    fora = []
    blocos = re.split(r'(?=<div class="slide[^"]*"\s+data-slide=")', c)
    i = 0
    for b in blocos:
        m = re.match(r'<div class="slide[^"]*"\s+data-slide="\d+"[^>]*data-lesson="(\d+)"', b)
        if not m or int(m.group(1)) != n:
            continue
        p = re.search(r'class="stage-pill">([^<]*)<', b)
        if p:
            txt = _html.unescape(p.group(1))
            fora.append((i, txt.split("\u00b7", 1)[-1].strip()))
        i += 1
    return fora


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return None
    fora = []
    for n in sorted(int(m.group(1)) for m in RX_ENTRADA.finditer(c)):
        nav = nomes_do_nav(c, n)
        if not nav:
            fora.append((f"aula {n}", "", "o `nav` do registro nao foi encontrado"))
            continue
        for i, pill in pills_por_tela(c, n):
            alvo = nav[i] if i < len(nav) else ""
            if pill != alvo:
                fora.append((f"aula {n} tela {i + 1}", pill, alvo))
    return fora


def chave(rel, onde, pill, nav):
    return f"{rel}|{onde}|{pill}|{nav}"


def main(argv):
    atualiza = "--update" in argv
    alvos = [a for a in argv if not a.startswith("--")]
    if not alvos:
        alvos = sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                       glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html")))
    velho = set()
    if os.path.exists(BASELINE):
        velho = set(json.load(open(BASELINE, encoding="utf-8"))["toleradas"])
    print(f"=== GATE 56 — o menu chama a tela pelo nome dela (anatomia {ANATOMIA}) ===")
    achado, vistos = set(), 0
    detalhe = {}
    for f in alvos:
        r = confere(f)
        if r is None:
            continue
        vistos += 1
        rel = os.path.relpath(f, RAIZ)
        for onde, pill, nav in r:
            k = chave(rel, onde, pill, nav)
            achado.add(k)
            detalhe[k] = (rel, onde, pill, nav)
    if atualiza:
        json.dump({"_o_que_e": "GATE 56: divergencias entre a `.stage-pill` da tela e o "
                               "`nav` do menu que ja existiam. E ALVARA, nao tarefa: so "
                               "pode CAIR (REGRA 30).",
                   "toleradas": sorted(achado)},
                  open(BASELINE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{VERDE}baseline atualizado{ZERA} — {len(achado)} divergencia(s) toleradas.")
        return 0
    novas = achado - velho
    for k in sorted(novas):
        rel, onde, pill, nav = detalhe[k]
        print(f"  {VERMELHO}FAIL{ZERA}   {rel}: {onde} se chama {pill!r} na tela e "
              f"{nav!r} no menu. O nome esta em dois lugares — mude nos dois.")
    curadas = velho - achado
    if novas:
        print(f"\n{VERMELHO}GATE 56 — {len(novas)} divergencia(s) NOVA(S) em {vistos} "
              f"arquivo(s).{ZERA}")
        return 1
    if curadas:
        print(f"  {len(curadas)} divergencia(s) do alvara sumiram. Rode --update para "
              f"recongelar a base — ela so pode cair.")
        return 1
    print(f"\n{VERDE}GATE 56 OK{ZERA} — {vistos} arquivo(s); "
          f"{len(velho)} divergencia(s) antigas toleradas, nenhuma nova.")
    return 0


def selftest():
    falhas = []
    cab = '<meta name="alumni-anatomia" content="consultivo">'
    corpo = (cab +
             '<div class="slide slide-open" data-slide="1" data-stage="1" data-lesson="1">'
             '<p class="chapter-label">Lesson 01</p></div>'
             '<div class="slide slide-light" data-slide="2" data-stage="1" data-lesson="1">'
             '<span class="stage-pill">1 &middot; The paper in your hand</span></div>'
             '<div class="slide slide-dark" data-slide="3" data-stage="2" data-lesson="1">'
             '<span class="stage-pill">2 &middot; Say the four</span></div>'
             "\n 1:{n:1,bloco:1,mod:'Reading',\n"
             "    nav:['Lesson opening','The paper in your hand','One word, or a sentence'],\n"
             "    stages:[]};")
    tmp = os.path.join(RAIZ, "_selftest_gate56.html")
    open(tmp, "w", encoding="utf-8").write(corpo)
    try:
        r = confere(tmp)
        if [x[1:] for x in r] != [("Say the four", "One word, or a sentence")]:
            falhas.append(f"nao apontou a tela renomeada so num lugar: {r}")
        if any("The paper" in x[1] for x in r):
            falhas.append("acusou a tela que concorda")
        # a tela de abertura nao tem pill e nao pode ser cobrada
        if any("tela 1" in x[0] for x in r):
            falhas.append("cobrou a tela de abertura, que nao tem pill")
    finally:
        os.remove(tmp)
    if not os.path.exists(BASELINE):
        falhas.append("o alvara nao existe — rode --update uma vez")
    if falhas:
        print(VERMELHO + "selftest FALHOU" + ZERA)
        for f in falhas:
            print("  -", f)
        return 1
    print(f"{VERDE}selftest OK{ZERA} — le o pill e o nav pela POSICAO da tela, aponta so a "
          f"que diverge e poupa a tela sem pill.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv[1:]))
