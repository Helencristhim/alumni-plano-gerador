#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 72 -- a atividade de ORDENAR e uma ordem que da para montar, conferir e desfazer.

O DEFEITO QUE ELE EXISTE PARA IMPEDIR
-------------------------------------
O componente nasceu em 11/09/2026, de um pedido da professora na revisao da aula 20 da
Gabriela: a ordenacao era um `classificar` com as opcoes `1st`..`6th` -- seis dropdowns
para uma tarefa so. Componente novo entra no repo com tolerancia zero (no alumni-black nao
ha legado e nao ha alvara), e componente que nasce sem gate volta a nascer quebrado: este
repo ja teve "324 botoes mortos" que nenhum gate viu, "handler que escreve num id que nao
existe" e "tres gates verdes sem medir nada".

O QUE ELE MEDE, no HTML PUBLICADO
---------------------------------
1. O HANDLER ACHA O ALVO. Todo `.ordbox` tem `id`, e existem `{id}-out` e um botao cujo
   `soCheck(this,'{id}')` cita esse id. Sem isso o Check e um clique que nao faz nada --
   e `if(!box)return` nao da erro em lugar nenhum.
2. O ID E UNICO no arquivo (o GATE 60 ja mede isso no repo inteiro; aqui a checagem e
   local porque um `ordbox` duplicado quebra ESTE componente de um jeito proprio: o
   `getElementById` devolve o primeiro e o segundo fica inerte).
3. EXISTE O CAMINHO SEM ARRASTO. Duas coisas, porque sao dois caminhos diferentes:
   toda coluna tem um `.sortdrop` focalizavel (e o destino do teclado e do toque), e toda
   linha tem as duas setas (e o unico jeito de REORDENAR sem arrastar). `draggable` sozinho
   nao e acessibilidade: em toque e no teclado ele simplesmente nao existe.
4. O GABARITO E FECHADO E COMPLETO: os `data-ok` das N linhas sao exatamente 1..N, uma vez
   cada. Repetido ou faltando, ha posicao que nenhuma resposta ocupa e a conferencia mente.
5. A ORDEM EMITIDA NAO E A ORDEM DA RESPOSTA -- nem ela de tras para frente, nem com metade
   das linhas ja no proprio lugar. E a PRO-009 do catalogo do auditor aplicada a este
   componente: exercicio que ja vem resolvido nao mede nada.
6. A COLUNA DE DESTINO NASCE VAZIA e todas as linhas nascem na de origem. Uma linha ja
   posta e uma resposta dada.

O QUE ELE NAO MEDE
------------------
Se a sequencia declarada e a sequencia certa da conversa -- isso e conteudo, e de quem
escreve a aula. E nao mede COMPORTAMENTO: arrastar, clicar e conferir se medem no
navegador, e quem faz isso e o GATE 42 (que dispara todo `[onclick]` do arquivo).

ESCOPO: os materiais publicados que carregam o carimbo `alumni-anatomia=consultivo`.
Sem baseline, por decisao do Dan: no alumni-black nao existe legado.

USO:
    python3 scripts/consultivo/check_ordenar_arrastando.py
    python3 scripts/consultivo/check_ordenar_arrastando.py public/professor/x.html
    python3 scripts/consultivo/check_ordenar_arrastando.py --selftest
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"
MARCA = 'name="alumni-anatomia" content="consultivo"'


def caixas(t):
    """Cada `.ordbox` e o seu corpo, pelo BALANCO de <div> -- nunca ate o primeiro </div>.

    E a licao que o proprio GATE 41 pagou: o laco do `quiz-options` lia ate o primeiro
    fechamento, o corpo terminava na primeira opcao, e a regra nunca disparou. Aqui o corpo
    tem duas colunas e N linhas aninhadas; ler por regex preguicoso seria medir a primeira
    coluna e chamar isso de medir a atividade."""
    for m in re.finditer(r'<div class="sortbox ordbox" id="([^"]+)">', t):
        nivel, i, fechou = 1, m.end(), False
        for d in re.finditer(r"<div\b|</div>", t[m.end():]):
            nivel += 1 if d.group(0) == "<div" else -1
            if nivel == 0:
                i, fechou = m.end() + d.start(), True
                break
        yield m.group(1), t[m.end():i], fechou


def _por_balanco(corpo, abertura):
    """Todo bloco que casa `abertura`, com o corpo delimitado pelo balanco de <div>.

    Uma funcao so para colunas e linhas: as duas aninham (a coluna contem linhas, a linha
    contem o `.item-why`), e ler qualquer uma das duas ate o primeiro `</div>` daria a
    resposta errada -- que e exatamente o defeito que este gate herdou de ver no GATE 41."""
    for m in re.finditer(abertura, corpo):
        nivel, i = 1, m.end()
        for d in re.finditer(r"<div\b|</div>", corpo[m.end():]):
            nivel += 1 if d.group(0) == "<div" else -1
            if nivel == 0:
                i = m.end() + d.start()
                break
        yield m.groups(), corpo[m.end():i]


def colunas(corpo):
    """As duas colunas da caixa."""
    for g, dentro in _por_balanco(corpo, r'<div class="sortcol" data-c="(\d+)"[^>]*>'):
        yield g[0], dentro


def linhas_da(corpo):
    """Cada linha movel: (data-i, data-ok, corpo da linha)."""
    for g, dentro in _por_balanco(
            corpo, r'<div class="ordrow" data-i="(\d+)" data-ok="(\d+)"[^>]*>'):
        yield g[0], g[1], dentro


def confere(caminho):
    t = open(caminho, encoding="utf-8", errors="replace").read()
    if MARCA not in t[:4000]:
        return [], 0
    rel = os.path.relpath(caminho, RAIZ)
    falhas, medidas = [], 0
    vistos = set()
    for ident, corpo, fechou in caixas(t):
        medidas += 1
        if not fechou:
            falhas.append(f"{rel}: a caixa '{ident}' nao fecha — o corpo lido dali e o resto "
                          f"do documento, e qualquer veredito sobre ela e falso.")
            continue
        if ident in vistos:
            falhas.append(f"{rel}: ha duas caixas com o id '{ident}'. `getElementById` "
                          f"devolve a primeira, e a segunda fica inerte — sem erro nenhum.")
        vistos.add(ident)

        # 1. o handler acha o alvo
        if f"soCheck(this,'{ident}')" not in t:
            falhas.append(f"{rel}: '{ident}' nao tem botao que chame "
                          f"soCheck(this,'{ident}') — a atividade nao tem como ser conferida.")
        if f'id="{ident}-out"' not in t:
            falhas.append(f"{rel}: '{ident}' nao tem onde escrever o resultado "
                          f"(falta id=\"{ident}-out\") — o Check confere e nao diz nada.")

        cols = dict(colunas(corpo))
        if sorted(cols) != ["0", "1"]:
            falhas.append(f"{rel}: '{ident}' tem as colunas {sorted(cols) or 'nenhuma'} e "
                          f"precisa de exatamente duas: a de origem (0) e a da ordem (1).")
            continue

        # 3. o caminho sem arrasto
        for c, corpo_col in cols.items():
            if 'class="sortdrop"' not in corpo_col:
                falhas.append(f"{rel}: a coluna {c} de '{ident}' nao tem o controle "
                              f"`.sortdrop` — com o card escolhido, o teclado nao tem como "
                              f"dizer o destino, e em toque nao ha arrasto que o substitua.")

        linhas = list(linhas_da(corpo))
        if not linhas:
            falhas.append(f"{rel}: '{ident}' nao tem linha nenhuma (`.ordrow`).")
            continue
        for di, _, resto in linhas:
            if resto.count('class="ordarrow"') != 2:
                falhas.append(f"{rel}: a linha {di} de '{ident}' nao tem o par de setas "
                              f"(`.ordarrow`) — sem elas nao existe caminho para REORDENAR "
                              f"que dispense o arrasto (REGRA 25).")

        # 4. gabarito fechado
        ok = [int(x) for _, x, _ in linhas]
        if sorted(ok) != list(range(1, len(ok) + 1)):
            falhas.append(f"{rel}: '{ident}' tem as posicoes {sorted(ok)} para "
                          f"{len(ok)} linha(s) — o gabarito precisa ser 1..{len(ok)}, uma "
                          f"vez cada, ou ha posicao que resposta nenhuma ocupa.")
        else:
            # 5. a ordem emitida nao e a ordem da resposta
            if ok == sorted(ok):
                falhas.append(f"{rel}: '{ident}' sai NA ORDEM DA RESPOSTA "
                              f"({' '.join(map(str, ok))}) — o exercicio ja vem resolvido.")
            elif ok == sorted(ok, reverse=True):
                falhas.append(f"{rel}: '{ident}' sai na ordem da resposta de tras para "
                              f"frente ({' '.join(map(str, ok))}) — se resolve tao rapido "
                              f"quanto a ordem certa.")
            else:
                fixos = sum(1 for i, n in enumerate(ok) if n == i + 1)
                if 2 * fixos >= len(ok):
                    falhas.append(f"{rel}: em '{ident}' {fixos} de {len(ok)} linhas ja estao "
                                  f"no proprio lugar ({' '.join(map(str, ok))}) — isso nao e "
                                  f"embaralhar, e empurrar duas frases.")

        # 6. a coluna de destino nasce vazia
        if 'class="ordrow"' in cols["1"]:
            falhas.append(f"{rel}: a coluna de destino de '{ident}' ja nasce com linha "
                          f"dentro — uma linha ja posta e uma resposta dada.")
        if len(re.findall(r'class="ordrow"', cols["0"])) != len(linhas):
            falhas.append(f"{rel}: '{ident}' nao comeca com todas as linhas na coluna de "
                          f"origem.")
    return falhas, medidas


def materiais(alvos):
    if alvos:
        return alvos
    fora = []
    for sub in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", sub, "*.html"))):
            with open(p, encoding="utf-8", errors="replace") as fh:
                if MARCA in fh.read(4000):
                    fora.append(p)
    return fora


def main(argv):
    falhas, caixas_vistas, arquivos = [], 0, 0
    for p in materiais(argv):
        if not os.path.exists(p):
            continue
        arquivos += 1
        f, n = confere(p)
        falhas += f
        caixas_vistas += n
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 72 REPROVOU{ZERA} — {len(falhas)} problema(s) em "
              f"atividade de ordenar.")
        return 1
    print(f"{VERDE}GATE 72 OK{ZERA} — {arquivos} material(is), {caixas_vistas} atividade(s) "
          f"de ordenar: gabarito fechado, ordem embaralhada, caminho sem arrasto em todas.")
    return 0


BOM = """<meta name="alumni-anatomia" content="consultivo">
<div class="sortbox ordbox" id="o1">
      <div class="sortcol" data-c="0" onclick="soCol(this,event)">
        <h5>A</h5>
        <div class="sortlist">
          <div class="ordrow" data-i="0" data-ok="3" draggable="true">
            <button type="button" class="sortitem">x</button>
            <span class="ordmove"><button class="ordarrow">u</button><button class="ordarrow">d</button></span>
          </div>
          <div class="ordrow" data-i="1" data-ok="1" draggable="true">
            <button type="button" class="sortitem">y</button>
            <span class="ordmove"><button class="ordarrow">u</button><button class="ordarrow">d</button></span>
          </div>
          <div class="ordrow" data-i="2" data-ok="2" draggable="true">
            <button type="button" class="sortitem">z</button>
            <span class="ordmove"><button class="ordarrow">u</button><button class="ordarrow">d</button></span>
          </div>
        </div>
        <button type="button" class="sortdrop">Move back here</button>
      </div>
      <div class="sortcol" data-c="1" onclick="soCol(this,event)">
        <h5>B</h5>
        <div class="sortlist"></div>
        <button type="button" class="sortdrop">Move here</button>
      </div>
    </div>
    <button class="verify-all-btn" onclick="soCheck(this,'o1')">Check</button>
    <div class="score-out" id="o1-out"></div>
"""


def selftest():
    import tempfile
    casos = [
        ("limpo", False, lambda s: s),
        ("ordem da resposta", True,
         lambda s: s.replace('data-ok="3"', 'data-ok="1"', 1)
                    .replace('data-i="1" data-ok="1"', 'data-i="1" data-ok="2"', 1)
                    .replace('data-i="2" data-ok="2"', 'data-i="2" data-ok="3"', 1)),
        ("gabarito repetido", True, lambda s: s.replace('data-ok="1"', 'data-ok="3"', 1)),
        ("sem botao de conferir", True,
         lambda s: s.replace("soCheck(this,'o1')", "soCheck(this,'outro')", 1)),
        ("sem lugar para o resultado", True, lambda s: s.replace('id="o1-out"', 'id="zz"', 1)),
        ("coluna sem o controle focalizavel", True,
         lambda s: s.replace('<button type="button" class="sortdrop">Move here</button>', "", 1)),
        ("linha sem as setas", True,
         lambda s: s.replace('<span class="ordmove"><button class="ordarrow">u</button>'
                             '<button class="ordarrow">d</button></span>', "", 1)),
        ("destino ja nasce com linha", True,
         lambda s: s.replace('<div class="sortlist"></div>',
                             '<div class="sortlist"><div class="ordrow" data-i="9" '
                             'data-ok="9"></div></div>', 1)),
        ("caixa que nao fecha", True,
         lambda s: s.replace('<div class="sortlist"></div>', '<div class="sortlist">', 1)),
    ]
    erros = 0
    for nome, deve, muta in casos:
        fd, cam = tempfile.mkstemp(suffix=".html")
        os.close(fd)
        try:
            open(cam, "w", encoding="utf-8").write(muta(BOM))
            pegou = bool(confere(cam)[0])
        finally:
            os.unlink(cam)
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(args))
