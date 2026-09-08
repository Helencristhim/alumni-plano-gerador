#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 66 — o recurso aponta para UM item, nunca para o canal, a serie ou a home.

O DEFEITO
---------
A revisao da professora, na aula 4 da Vanessa (#2536), escreveu:

    "Reading e Listen & Watch apontavam para SERIES INTEIRAS -- English at Work (que nao e
     de...)."

Ela consertou aquelas duas. Medido em 09/09/2026 no resto da anatomia: **30 links** ainda
mandavam o aluno para uma porta, nao para o material -- sete canais do YouTube, duas home
pages, e o resto hubs de serie e paginas de topico:

    youtube.com/@bbclearningenglish        ecorner.stanford.edu/
    youtube.com/@TED                       world-education-blog.org/
    bbc.co.uk/.../features/6-minute-english        ted.com/topics/business
    acquired.fm/episodes                   learningenglish.voanews.com/z/1581

Concentrados no Caio (11) e na Joice (15) -- os dois alunos que nunca foram revisados -- e
na aula 1 da Vanessa, a unica dela que ficou de fora da revisao de recursos.

**Um cartao que promete "escute as duas maneiras de pedir para repetir" e leva a um canal
com mil videos nao e um recurso: e uma tarefa a mais.** O aluno que abre isso na quinta a
noite fecha a aba.

O QUE ELE MEDE, e por que sao estas tres formas
------------------------------------------------
Nao ha como uma maquina julgar se um link e "bom". Ha tres formas em que ele PROVADAMENTE
nao e um item, porque a propria URL diz:

 1. **canal do YouTube** -- `/@handle`, `/c/`, `/user/`, `/channel/` sem video nem playlist.
    Um `watch?v=`, um `youtu.be/`, um `/playlist?list=` ou um `/shorts/` sao um item e
    passam: playlist curada e uma escolha, canal e a ausencia de uma.
 2. **home page** -- caminho vazio. E a porta do site, nao um material.
 3. **indice conhecido** -- `/topics/`, `/episodes`, `/podcasts/` no fim do caminho, e as
    secoes `voanews.com/z/` e `/p/`, que sao listagens.

O que ele NAO tenta medir: se `bbc.co.uk/.../features/english-at-work` e uma serie ou um
episodio. Isso depende do site, e adivinhar produziria falso positivo. O que sobra ja
barra as tres formas que aparecem de verdade.

ESCOPO: os blocos `kind: "recursos"` dos fragmentos autorais do consultivo.

USO:
    python3 scripts/consultivo/check_recurso_e_um_item.py [dir ...]
    python3 scripts/consultivo/check_recurso_e_um_item.py --selftest
"""
import glob
import json
import os
import re
import sys
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# Um video, uma playlist, um short: sao itens. O resto do YouTube e porta.
RX_ITEM_YT = re.compile(r"(?:watch\?|[?&]v=|youtu\.be/|/playlist\?|/shorts/)")
RX_CANAL_YT = re.compile(r"^/(?:@|c/|user/|channel/)")

# Listagens que aparecem no acervo. Ancoradas no FIM do caminho: `/podcasts/510313/x` e um
# programa (ainda porta, mas outra forma), `/podcasts/` e o indice.
RX_INDICE = re.compile(r"/topics?/[^/]*$|/episodes/?$|/podcasts/?$|/playlists?/?$")
RX_SECAO_VOA = re.compile(r"^/(?:z|p)/\d+")


def porque_nao_e_item(url):
    """A razao pela qual esta URL nao e um material, ou None."""
    q = urlparse(url)
    caminho = q.path
    if "youtube.com" in q.netloc or "youtu.be" in q.netloc:
        if RX_ITEM_YT.search(url):
            return None
        if RX_CANAL_YT.match(caminho) or not caminho.rstrip("/"):
            return ("e um CANAL do YouTube. O aluno chega a uma lista e tem de achar o "
                    "video sozinho — escolha o video (watch?v=…) ou a playlist")
    if not caminho.rstrip("/"):
        return "e a HOME do site, nao um material"
    if RX_INDICE.search(caminho):
        return "e um INDICE (topico, episodios, podcasts), nao um material"
    if "voanews.com" in q.netloc and RX_SECAO_VOA.match(caminho):
        return "e uma SECAO da VOA (/z/ ou /p/), que lista materiais — aponte para o artigo"
    return None


def recursos(obj):
    if isinstance(obj, dict):
        if obj.get("kind") == "recursos":
            for r in obj.get("itens", []):
                yield r
        for v in obj.values():
            yield from recursos(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from recursos(v)


def confere(pasta):
    falhas = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "aula*", "blocos.json"))):
        try:
            dados = json.load(open(caminho, encoding="utf-8"))
        except Exception as e:
            falhas.append(f"{os.path.relpath(caminho, RAIZ)}: nao e JSON valido ({e}).")
            continue
        rel = os.path.relpath(caminho, RAIZ)
        for r in recursos(dados):
            url = r.get("url", "")
            motivo = porque_nao_e_item(url)
            if motivo:
                falhas.append(f"{rel}: o recurso {r.get('titulo', '?')!r} aponta para "
                              f"{url} — {motivo}.")
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
        print(f"\n{VERMELHO}GATE 66 REPROVOU{ZERA} — {len(falhas)} recurso(s) apontando "
              f"para uma porta em vez do material.")
        return 1
    print(f"{VERDE}GATE 66 OK{ZERA} — {medidos} material(is): todo recurso abre no proprio "
          f"material.")
    return 0


def selftest():
    def caso(url):
        return {"reading": [{"kind": "recursos", "itens": [
            {"titulo": "x", "fonte": "f", "texto": "t", "url": url, "cta": "c"}]}]}
    casos = [
        ("video do YouTube", False, "https://www.youtube.com/watch?v=abc123"),
        ("youtu.be", False, "https://youtu.be/abc123"),
        ("playlist do YouTube — e uma escolha", False,
         "https://www.youtube.com/playlist?list=PL123"),
        ("canal por @handle", True, "https://www.youtube.com/@bbclearningenglish"),
        ("canal por /c/", True, "https://www.youtube.com/c/TED"),
        ("home do site", True, "https://ecorner.stanford.edu/"),
        ("pagina de topico", True, "https://www.ted.com/topics/business"),
        ("indice de episodios", True, "https://www.acquired.fm/episodes"),
        ("secao da VOA", True, "https://learningenglish.voanews.com/z/1581"),
        ("artigo da VOA", False, "https://learningenglish.voanews.com/a/5794014.html"),
        ("talk do TED", False,
         "https://www.ted.com/talks/david_s_rose_on_pitching_to_vcs"),
        ("exercicio do British Council", False,
         "https://learnenglish.britishcouncil.org/skills/reading/a1-reading/business-cards"),
    ]
    import tempfile
    erros = 0
    for nome, deve, url in casos:
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "aula1"))
            with open(os.path.join(d, "aula1", "blocos.json"), "w", encoding="utf-8") as fh:
                json.dump(caso(url), fh)
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
