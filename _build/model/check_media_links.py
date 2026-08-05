#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_media_links.py — o link do complementar aponta pro TITULO que o card anuncia?

    python3 _build/model/check_media_links.py public/professor/{slug}.html [...]
    python3 _build/model/check_media_links.py --aula public/professor/{slug}-aula3.html

POR QUE ISTO EXISTE
-------------------
Os gates estaticos ja cobrem tres coisas: todo media-card tem link (REGRA 17,
`validate_lesson`), link de BUSCA e barrado e conteudo pago/HBR e barrado
(`check_forbidden_patterns`). Nenhum deles sabe se o link leva ao que o card DIZ
que leva — e nao tem como saber, porque isso exige rede.

O buraco e real e foi levantado na geracao de 05/08/2026: **um ID de titulo colhido
de resultado de busca pode resolver para OUTRA obra no catalogo brasileiro**. O card
anuncia "Suits — Season 1, Episode 1", o link abre outra coisa, e nada no repo
reclama. O aluno clica e cai no lugar errado; ninguem fica sabendo.

Este script fecha isso: le o `<h5>` do card e o `href`, busca a pagina, extrai o
`og:title` (ou o `<title>`) e compara. **Nao e gate de CI** — depende de rede e de
sites que bloqueiam robo. E ferramenta de AUTORIA: rode antes de abrir o PR.

COMO LER A SAIDA
----------------
  OK          o titulo da pagina bate com o do card
  MISMATCH    a pagina existe mas anuncia OUTRA coisa  -> CONSERTE (exit 1)
  CONFIRA     catalogo que TRADUZ titulo (Netflix, Prime, Disney+): mostra o titulo
              brasileiro resolvido pra voce bater o olho. NAO falha — ver abaixo.
  SEM TITULO  respondeu, mas sem og:title/<title> legivel (comum em SPA)
  BLOQUEADO   403/429/anti-bot. NAO e defeito; confira a mao uma vez e siga.
  ERRO        DNS/timeout/404 -> link provavelmente morto, confira

So MISMATCH derruba o exit code. Tudo que e incerto vira aviso, de proposito: um
verificador que grita com falso positivo e desligado na primeira semana.

POR QUE A NETFLIX NAO FALHA
---------------------------
Ela devolve o titulo LOCALIZADO: "Worth" vira "Quanto vale?", "The Lincoln Lawyer"
vira "O Poder e a Lei", "Drive to Survive" vira "F1: Dirigir para Viver". Comparar
por palavra acusa MISMATCH em todos — cinco de cinco na primeira rodada deste
script, todos corretos. Traducao nao se verifica por sobreposicao de tokens, entao
para esses hosts o script faz a UNICA coisa que consegue provar: mostra o titulo que
o ID realmente abre, e deixa a conferencia com quem escreveu o card. Isso ja resolve
o buraco original — um ID errado abre OUTRA obra, e o nome dela aparece aqui.
"""
import html as _html
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# Catalogos que devolvem o titulo TRADUZIDO. Comparar por palavra aqui e ruido puro
# (ver docstring). Para estes o script REPORTA o titulo resolvido e nao falha.
LOCALIZAM = ("netflix.com", "primevideo.com", "amazon.com", "disneyplus.com",
             "max.com", "globoplay.globo.com", "appletv.apple.com")

# Palavras que aparecem no card mas nunca no titulo da pagina — tirar antes de comparar
RUIDO = {
    "season", "episode", "temporada", "episodio", "ep", "s1", "s2", "part", "parte",
    "the", "a", "an", "of", "and", "or", "with", "for", "on", "in", "to", "de", "do",
    "da", "e", "o", "um", "uma", "any", "recent", "series", "podcast", "video",
    "youtube", "netflix", "spotify", "ted", "talk", "official", "full", "hd",
}


def norm(s):
    s = unicodedata.normalize("NFD", _html.unescape(s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return [w for w in re.sub(r"[^a-z0-9 ]", " ", s).split() if w not in RUIDO and len(w) > 2]


# oEmbed devolve o titulo REAL em JSON, sem depender de og:title renderizado. Resolve
# os dois casos que o scrape nao pega: YouTube (muitas paginas nao servem og:title pro
# robo) e Spotify (SPA — o <title> vem "Spotify – Web Player", generico, o que o
# comparador leria como MISMATCH em TODO link do host).
OEMBED = {
    "youtube.com": "https://www.youtube.com/oembed?format=json&url=",
    "youtu.be": "https://www.youtube.com/oembed?format=json&url=",
    "open.spotify.com": "https://open.spotify.com/oembed?url=",
    "vimeo.com": "https://vimeo.com/api/oembed.json?url=",
}


def _oembed(url):
    """Titulo via oEmbed, ou None se o host nao tem/nao respondeu."""
    base = next((v for k, v in OEMBED.items() if k in url), None)
    if not base:
        return None
    try:
        req = urllib.request.Request(base + urllib.parse.quote(url, safe=""),
                                     headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            t = json.load(r).get("title")
        return t.strip()[:160] if t else None
    except Exception:                                        # noqa: BLE001
        return None


def titulo_da_pagina(url):
    """(estado, titulo). Estado: ok | sem-titulo | bloqueado | erro."""
    t = _oembed(url)
    if t:
        return "ok", t
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read(400_000)
        enc = "utf-8"
        m = re.search(rb'charset=["\']?([\w-]+)', raw[:4000], re.I)
        if m:
            enc = m.group(1).decode("ascii", "ignore")
        txt = raw.decode(enc, "replace")
    except urllib.error.HTTPError as e:
        return ("bloqueado" if e.code in (401, 403, 429, 451) else "erro"), f"HTTP {e.code}"
    except Exception as e:                                   # noqa: BLE001
        return "erro", type(e).__name__
    for pat in (r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)',
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:title',
                r"<title[^>]*>(.*?)</title>"):
        m = re.search(pat, txt, re.I | re.S)
        if m and m.group(1).strip():
            return "ok", _html.unescape(m.group(1)).strip()[:160]
    return "sem-titulo", ""


def cards(doc):
    """(titulo_do_card, url) de cada media-card com link."""
    out = []
    for blk in re.findall(r'<div class="media-card-wrapper".*?(?=<div class="media-card-wrapper"|\Z)',
                          doc, re.S):
        t = re.search(r"<h5[^>]*>(.*?)</h5>", blk, re.S)
        a = re.search(r'<a[^>]+href="(https?://[^"]+)"', blk)
        if t and a:
            out.append((re.sub(r"<[^>]+>", "", t.group(1)).strip(), a.group(1)))
    return out


def main(argv):
    paths = [a for a in argv[1:] if not a.startswith("-")]
    if not paths:
        print(__doc__)
        return 2
    ruins = vistos = 0
    seen = set()
    for p in paths:
        try:
            doc = open(p, encoding="utf-8").read()
        except OSError as e:
            print(f"  ERRO ao abrir {p}: {e}")
            ruins += 1
            continue
        print(f"\n=== {p}")
        for titulo, url in cards(doc):
            if url in seen:
                continue
            seen.add(url)
            vistos += 1
            estado, achado = titulo_da_pagina(url)
            esperado = norm(titulo)
            if estado != "ok":
                rot = {"bloqueado": "BLOQUEADO", "sem-titulo": "SEM TITULO"}.get(estado, "ERRO")
                print(f"  {rot:10} {titulo[:52]:<52} {achado}")
                continue
            achados = norm(achado)
            # "any recent episode" aponta pro PROGRAMA, e o episodio do topo muda toda
            # semana — o titulo resolvido nunca vai bater com o do card, e nao deveria.
            # Verificamos o que da pra verificar: que o programa existe e abre.
            if re.search(r"any (recent )?episode|qualquer epis|episode of season",
                         titulo, re.I):
                print(f"  CONFIRA    {titulo[:52]:<52} -> programa abre: {achado[:52]}")
                continue
            if any(h in url for h in LOCALIZAM):
                # titulo traduzido: mostrar e deixar a conferencia com o humano
                print(f"  CONFIRA    {titulo[:52]:<52} -> abre: {achado[:60]}")
                continue
            # basta UMA palavra significativa em comum: titulos de catalogo variam muito
            # ("Suits" vs "Suits: Segunda Chance"), e exigir igualdade so gera ruido.
            if esperado and achados and not (set(esperado) & set(achados)):
                print(f"  MISMATCH   {titulo[:52]:<52} -> pagina diz: {achado[:60]}")
                ruins += 1
            else:
                print(f"  OK         {titulo[:52]:<52} ({achado[:44]})")
    print(f"\n=== {vistos} link(s) conferido(s) | {ruins} MISMATCH")
    if ruins:
        print("=== CONSERTE os MISMATCH antes do PR (REGRA 17: link vai ao recurso EXATO)")
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
