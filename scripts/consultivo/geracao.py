#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O CARIMBO DE GERACAO de uma aula do consultivo — de que regra ela ja nasceu sabendo.

POR QUE ISTO EXISTE (15/09/2026)
--------------------------------
As aulas 19, 20 e 21 da Gabriela Pires foram revisadas pela professora e o Dan as tomou como
exemplo. As regras MEDIVEIS que essas revisoes estabeleceram viram gate. A ordem que veio
junto e literal: "vc nao vai corrigir mais nada" — nenhuma aula existente, de nenhum aluno.

Gate que nasce valendo para tudo acusa, no primeiro minuto, aula que foi escrita antes de a
regra existir (ver a memoria `gate-novo-nasce-escopado`). No imersivo o escopo e o
`<meta name="alumni-gen">` que o builder poe no arquivo publicado. No consultivo isso nao
serve: o GATE 50 reconstroi TODO material a partir dos fragmentos a cada PR, entao o que o
arquivo publicado carrega tem de sair do fragmento — e um meta novo mudaria os bytes dos
seis materiais que ja estao no ar.

Entao o carimbo mora no FRAGMENTO, por AULA, num arquivo que o emissor nao le:

    _build/consultivo/{slug}/aula{N}/geracao.json      {"gen": 1}

POR AULA, E NAO POR ALUNO: a aula 23 da Gabriela, quando for escrita, nasce sob os gates de
hoje; a 19 nao. Um carimbo no config.json nao separaria as duas.

A AUSENCIA NAO PODE SER UM JEITO DE ESCAPAR
--------------------------------------------
Se "sem carimbo" valesse "passado", toda aula nova que esquecesse o arquivo sairia do alcance
dos gates em silencio — que e exatamente o defeito que o carimbo existe para impedir. Por
isso a lista das aulas que JA EXISTIAM quando o carimbo nasceu esta congelada aqui
(`ANTERIORES`), e o builder RECUSA qualquer outra aula sem `geracao.json`. A lista nao
cresce: aula nova nao entra nela, entra com o carimbo.

    gen 0 = aula anterior a 15/09/2026 (esta na lista, nao tem arquivo). Nenhum gate novo.
    gen 1 = gates de 15/09/2026: tempo na tela (GATE 74), cartoes encostados (GATE 75),
            deck declarado (GATE 76).

`GEN_ATUAL` sobe SO quando entra invariante nova que nao pode valer para o que ja existe —
nunca por mudanca cosmetica. Gate novo escopa com `gen(pasta) >= N` na PRIMEIRA linha.
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(RAIZ, "_build", "consultivo")
ARQUIVO = "geracao.json"
GEN_ATUAL = 1

# As aulas que existiam em origin/main em 15/09/2026 (8db2aac99), menos as quatro do molde,
# reescritas no mesmo dia com `geracao.json` (PRs #2677, #2684, #2688 e o da aula 4, que tira as quatro desta lista). Congelada: so pode
# CAIR — quando uma aula dessas for reescrita e ganhar `geracao.json`, o arquivo vale e a
# entrada pode sair. Aula nova nunca entra aqui.
ANTERIORES = frozenset({
    "caio-de-souza-amante/aula1", "caio-de-souza-amante/aula2",
    "caio-de-souza-amante/aula3", "caio-de-souza-amante/aula4",
    "gabriela-pires/aula19", "gabriela-pires/aula20",
    "gabriela-pires/aula21", "gabriela-pires/aula22",
    "joice-lopes-leite/aula9", "joice-lopes-leite/aula10",
    "joice-lopes-leite/aula11", "joice-lopes-leite/aula12",
    "lucia-nishiyama-serra/aula3", "lucia-nishiyama-serra/aula4",
    "lucia-nishiyama-serra/aula5", "lucia-nishiyama-serra/aula6",
    "luiz-bressane/aula9", "luiz-bressane/aula10",
    "luiz-bressane/aula11", "luiz-bressane/aula12",
    "vanessa-aparecida/aula1", "vanessa-aparecida/aula2",
    "vanessa-aparecida/aula3", "vanessa-aparecida/aula4",
})


def chave(pasta):
    """`{slug}/aula{N}` a partir do caminho da pasta da aula."""
    pasta = os.path.normpath(pasta)
    return os.path.basename(os.path.dirname(pasta)) + "/" + os.path.basename(pasta)


def le(pasta):
    """(gen, erro). `erro` e None quando o carimbo esta certo — ou quando a aula e anterior
    a ele e esta na lista congelada."""
    caminho = os.path.join(pasta, ARQUIVO)
    if not os.path.exists(caminho):
        if chave(pasta) in ANTERIORES:
            return 0, None
        return 0, (f"{chave(pasta)}: falta `{ARQUIVO}`. Toda aula escrita depois de "
                   f"15/09/2026 declara de que geracao e: {{\"gen\": {GEN_ATUAL}}}. Sem o "
                   f"carimbo ela ficaria fora dos gates que so valem para material novo — "
                   f"e e por isso que a ausencia recusa, em vez de valer 'passado'.")
    try:
        with open(caminho, encoding="utf-8") as fh:
            dado = json.load(fh)
    except Exception as e:                                             # noqa: BLE001
        return 0, f"{chave(pasta)}: `{ARQUIVO}` nao e JSON valido ({e})."
    g = dado.get("gen") if isinstance(dado, dict) else None
    if not isinstance(g, int) or isinstance(g, bool) or not 1 <= g <= GEN_ATUAL:
        return 0, (f"{chave(pasta)}: `{ARQUIVO}` declara gen={g!r}. O valor e um inteiro "
                   f"de 1 a {GEN_ATUAL} (o 0 e das aulas anteriores ao carimbo, que nao "
                   f"tem o arquivo).")
    return g, None


def gen(pasta):
    """A geracao da aula. Carimbo invalido ou ausente fora da lista conta como a ATUAL:
    para os gates, duvida e material novo — nunca passado."""
    g, erro = le(pasta)
    return GEN_ATUAL if erro else g


def aulas(alvos=None):
    """As pastas de aula dos materiais do consultivo (so os que tem config.json)."""
    import glob
    bases = [a.rstrip("/") for a in alvos] if alvos else sorted(
        os.path.dirname(p) for p in glob.glob(os.path.join(BASE, "*", "config.json")))
    saida = []
    for b in bases:
        saida += sorted(glob.glob(os.path.join(b, "aula*")),
                        key=lambda p: int("".join(c for c in os.path.basename(p)
                                                  if c.isdigit()) or 0))
    return [p for p in saida if os.path.isdir(p)]
