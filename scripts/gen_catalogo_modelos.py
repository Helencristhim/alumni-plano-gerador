#!/usr/bin/env python3
"""Gera public/data/modelos-aulas.json — o catalogo de AULAS MODELO, por aluno.

POR QUE ISTO EXISTE
-------------------
O catalogo ja mostrava MODELO (o molde) e FRAMEWORK (o metodo). Faltava a camada do
meio, que e onde a duvida mora: *dentro do mesmo aluno modelo, quais aulas sao
diferentes entre si?* A Helen tem 5 aulas — as 2 primeiras nao tem a camada de blocos
B2 que as 3 seguintes tem. O Tiago tem 5 aulas e cada uma usa um metodo diferente
(rodizio). Sem ver isso lado a lado, "aula modelo" vira uma lista de links.

TUDO O QUE ESTE ARQUIVO ESCREVE E MEDIDO NO HTML, nunca digitado:
  - titulo (<title>), n de slides, capitulos (.phase-label)
  - framework (<meta name="alumni-framework">)
  - componentes de IN CLASS presentes (classes reais, so dentro do slides-wrapper)

O unico texto humano e o ROSTER abaixo: quem e a persona. Aula nova do mesmo aluno
aparece sozinha; persona nova = uma linha no ROSTER.

Uso:  python3 scripts/gen_catalogo_modelos.py [--check]
      --check falha (exit 1) se o JSON no disco estiver desatualizado (usado no CI).
"""

import argparse
import html as htmllib
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "public" / "data" / "modelos-aulas.json"
FRAMEWORKS = RAIZ / "public" / "data" / "frameworks.json"

# ── QUEM E CADA PERSONA (unico texto humano deste arquivo) ────────────────────
ROSTER = [
    {
        "slug": "helen-mendes",
        "nome": "Helen Mendes",
        "modelo": "adulto",
        "papel": "O molde. Layout, CSS e JS de todo material adulto saem daqui.",
        "destaque": True,
    },
    {
        "slug": "helen-mendes-v4",
        "nome": "Helen Mendes (V4)",
        "modelo": "adulto",
        "papel": "Mesma persona, piloto do documento V4 (PPP): aula mais curta, "
                 "uma skill receptiva principal, Pre-class flipped.",
    },
    {
        "slug": "mock-rodizio-tiago",
        "nome": "Tiago",
        "modelo": "adulto",
        "papel": "Mock do rodízio de frameworks: o método alterna a cada aula "
                 "(PPP → Communicative → Task-Based → PPP → Communicative).",
        "destaque": True,
    },
    {
        "slug": "mock-ppp-lara",
        "nome": "Lara",
        "modelo": "adulto",
        "papel": "Mock do framework PPP.",
    },
    {
        "slug": "mock-cla-vitor",
        "nome": "Vitor",
        "modelo": "adulto",
        "papel": "Mock do framework Communicative Approach.",
    },
    {
        "slug": "mock-tbl-ines",
        "nome": "Inês",
        "modelo": "adulto",
        "papel": "Mock do framework Task-Based (TBL).",
    },
    {
        "slug": "bento",
        "nome": "Bento",
        "modelo": "kids",
        "papel": "Persona do modelo Kids: aventura lúdica, bilíngue, ilustração 3D.",
    },
    {
        "slug": "theo",
        "nome": "Théo",
        "modelo": "teens",
        "papel": "Persona do modelo Teens: missão gamificada com Word Arena embutido.",
    },
]

MODELOS = {
    "adulto": {"label": "Adulto", "accent": "#1e6f8f"},
    "kids": {"label": "Kids", "accent": "#1e9e5f"},
    "teens": {"label": "Teens", "accent": "#6C5CE7"},
}

# ── COMPONENTES DE IN CLASS ───────────────────────────────────────────────────
# chave = classe/atributo REAL no HTML (o que o navegador ve), valor = rotulo humano.
# A ordem aqui e a ordem em que os chips aparecem no card.
COMPONENTES = [
    ("vocab-card", "vocab reveal"),
    ("ic-pair", "matching"),
    ("dialogue-line", "diálogo line-by-line"),
    ("ic-reading", "texto de leitura"),
    ("ic-tfrow", "true/false com justificativa"),
    ("lp-seekbar", "listening com player"),
    ("comp-q-task", "slide de tarefa"),
    ("ic-predict", "slide de predição"),
    ("fill-item", "gap-fill"),
    ("ic-bank", "banco de palavras"),
    ("error-card", "spot the error"),
    ("qf-card", "quick fire"),
    ("ic-scenario", "cenários"),
    ("ic-mod", "bloco de modais"),
    ("roleplay-scenario", "role-play"),
    ("word-arena", "Word Arena (jogo)"),
    ("voc-img", "ilustração 3D (kids)"),
]

# Familias usadas pra descrever a VARIANTE em uma linha (derivado, nao digitado).
FAMILIA = [
    ("dialogue-line", "diálogo"),
    ("ic-reading", "leitura"),
    ("lp-seekbar", "listening"),
    ("word-arena", "jogo"),
    ("ic-scenario", "blocos B2"),
    ("roleplay-scenario", "role-play"),
]


def texto(s):
    """Entidade HTML -> caractere, e colapsa espaco."""
    return re.sub(r"\s+", " ", htmllib.unescape(s or "")).strip()


def corpo_dos_slides(h):
    """So o que esta dentro do slides-wrapper: fora dele ha CSS e JS que citam as
    mesmas classes, e contar isso faria toda aula parecer ter todo componente."""
    i = h.find('class="slides-wrapper"')
    if i < 0:
        i = h.find("slides-wrapper")
    j = h.find("</body>")
    return h[i:j] if i >= 0 else h


def le_aula(caminho):
    h = caminho.read_text(encoding="utf-8", errors="replace")
    corpo = corpo_dos_slides(h)

    titulo = ""
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    if m:
        t = texto(m.group(1))
        # "Professor View -- Helen Mendes | Lesson 4 -- Reading the Numbers"
        if "|" in t:
            t = t.split("|", 1)[1].strip()
        t = re.sub(r"^(Lesson|Aula)\s*\d+\s*[-—–]+\s*", "", t).strip()
        titulo = t

    fw = None
    m = re.search(r'<meta\s+name="alumni-framework"\s+content="([^"]+)"', h)
    if m:
        fw = m.group(1)

    capitulos = []
    for c in re.findall(r'class="phase-label[^"]*"[^>]*>([^<]*)<', corpo):
        c = texto(c)
        if c and c not in capitulos:
            capitulos.append(c)

    comps = []
    for classe, rotulo in COMPONENTES:
        achou = (
            re.search(r'class="[^"]*\b' + re.escape(classe) + r'\b', corpo)
            or (classe.startswith("data-") and classe in corpo)
        )
        if achou:
            comps.append({"id": classe, "label": rotulo})

    return {
        "titulo": titulo,
        "slides": len(re.findall(r'class="slide[ "]', corpo)),
        "framework": fw,
        "capitulos": capitulos,
        "componentes": comps,
    }


def rotulo_variante(ids):
    """Uma linha que diz o que ESTA variante e — derivada dos componentes medidos."""
    partes = [rot for cid, rot in FAMILIA if cid in ids]
    return " + ".join(partes) if partes else "estrutura própria"


def coleta():
    fws = json.loads(FRAMEWORKS.read_text(encoding="utf-8"))
    fw_label = {}
    for cat in fws.get("categorias", []):
        for f in cat.get("frameworks", []):
            fw_label[f["id"]] = f.get("label", f["id"])

    personas = []
    for p in ROSTER:
        slug = p["slug"]
        arquivos = sorted(
            (RAIZ / "public" / "professor").glob(f"{slug}-aula*.html"),
            key=lambda f: int(re.search(r"-aula(\d+)\.html$", f.name).group(1)),
        )
        # glob de prefixo pega vizinho: helen-mendes-* traria helen-mendes-v4-*.
        arquivos = [
            f for f in arquivos
            if re.fullmatch(re.escape(slug) + r"-aula\d+\.html", f.name)
        ]
        if not arquivos:
            print(f"  aviso: {slug} nao tem aula em public/professor — pulando")
            continue

        aulas, assinaturas = [], {}
        for f in arquivos:
            n = int(re.search(r"-aula(\d+)\.html$", f.name).group(1))
            dados = le_aula(f)
            ids = tuple(c["id"] for c in dados["componentes"])
            # A VARIANTE agrupa pelo PERFIL da aula (metodo + familias de atividade),
            # nao por cada componente. Senao aula 4 e 5 da Helen viram "variantes"
            # diferentes porque uma tem banco de palavras e a outra tem modais — e a
            # pergunta que o catalogo responde ("quais aulas sao de outro tipo?")
            # afogaria em ruido. A diferenca fina continua visivel: os chips de cada
            # aula sao os componentes DAQUELA aula.
            familias = tuple(cid for cid, _ in FAMILIA if cid in ids)
            chave = (dados["framework"] or "", familias)
            if chave not in assinaturas:
                assinaturas[chave] = {
                    "id": chr(ord("A") + len(assinaturas)),
                    "framework": dados["framework"],
                    "framework_label": fw_label.get(dados["framework"] or ""),
                    "resumo": rotulo_variante(ids),
                    "componentes": list(dados["componentes"]),
                    "aulas": [],
                }
            else:
                vistos = {c["id"] for c in assinaturas[chave]["componentes"]}
                for c in dados["componentes"]:
                    if c["id"] not in vistos:
                        assinaturas[chave]["componentes"].append(c)
            assinaturas[chave]["aulas"].append(n)
            espelho = RAIZ / "public" / "aluno" / f.name
            aulas.append({
                "n": n,
                "variante": assinaturas[chave]["id"],
                "framework_label": fw_label.get(dados["framework"] or ""),
                "professor": f"/professor/{f.name}",
                "aluno": f"/aluno/{f.name}" if espelho.exists() else None,
                **dados,
            })

        hub = RAIZ / "public" / "professor" / f"{slug}.html"
        cab = {}
        if hub.exists():
            hh = hub.read_text(encoding="utf-8", errors="replace")
            spans = [texto(s) for s in re.findall(r"<span>([^<]{1,60})</span>", hh)]
            if spans:
                cab["nivel"] = spans[0]
            for s in spans[1:4]:
                if s and s.lower() not in ("progresso geral",) and "," not in s:
                    cab["perfil"] = s
                    break

        modelo = MODELOS[p["modelo"]]
        personas.append({
            "slug": slug,
            "nome": p["nome"],
            "papel": p["papel"],
            "destaque": bool(p.get("destaque")),
            "modelo": p["modelo"],
            "modelo_label": modelo["label"],
            "accent": modelo["accent"],
            "nivel": cab.get("nivel", ""),
            "perfil": cab.get("perfil", ""),
            "hub_professor": f"/professor/{slug}.html" if hub.exists() else None,
            "hub_aluno": f"/aluno/{slug}.html"
            if (RAIZ / "public" / "aluno" / f"{slug}.html").exists() else None,
            "variantes": list(assinaturas.values()),
            "aulas": aulas,
        })

    return {
        "_fonte": "GERADO por scripts/gen_catalogo_modelos.py — nao editar a mao. "
                  "Tudo aqui e medido no HTML da aula; o unico texto humano e o "
                  "ROSTER de personas dentro do script.",
        "version": 1,
        "componentes_legenda": {cid: rot for cid, rot in COMPONENTES},
        "personas": personas,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="falha se o JSON no disco estiver desatualizado")
    args = ap.parse_args()

    dados = coleta()
    texto_novo = json.dumps(dados, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        atual = SAIDA.read_text(encoding="utf-8") if SAIDA.exists() else ""
        if atual != texto_novo:
            print("modelos-aulas.json desatualizado — rode "
                  "python3 scripts/gen_catalogo_modelos.py", file=sys.stderr)
            return 1
        print("modelos-aulas.json em dia")
        return 0

    SAIDA.write_text(texto_novo, encoding="utf-8")
    n_aulas = sum(len(p["aulas"]) for p in dados["personas"])
    print(f"{SAIDA.relative_to(RAIZ)}: {len(dados['personas'])} personas, "
          f"{n_aulas} aulas modelo")
    for p in dados["personas"]:
        vs = "  ".join(
            f"{v['id']}=aulas {','.join(str(a) for a in v['aulas'])} ({v['resumo']})"
            for v in p["variantes"]
        )
        print(f"  {p['slug']:22} {len(p['aulas'])} aulas | {vs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
