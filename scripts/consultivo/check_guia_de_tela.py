#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 53 — a nota de tela do professor E o guia de dez campos, em ingles.

O QUE ELE MEDE
--------------
Toda tela do deck carrega um `data-teacher`. O Documento 04 §8.2 diz o que tem de haver
dentro dele: DEZ campos, nomeados, na mesma ordem, em todas as telas -- Goal, Interaction,
Run it, Exact prompt (condicional), Expected, Conditional support, Challenge, Monitoring,
Evidence to record, Transition.

POR QUE ISTO PRECISOU DE UM GATE
--------------------------------
Porque a forma declarada existe desde 02/09/2026 (`guia_telas.json` + `render.nota_de_tela`)
e mesmo assim quase todo material continuou com a nota escrita a mao: prosa livre, em
portugues, com os campos que cada aula inventava para si ("Objetivo / Conduza / Atencao /
Siga quando"). Duas consequencias, e as duas foram encontradas por leitura humana:

  - o professor nao sabe o que esperar. Uma tela avisa o que observar, a seguinte nao, e nada
    diz se a informacao falta ou se aquela tela nao precisava dela;
  - a revisao de 02/09/2026 nao conseguiu avaliar a linguagem didatica do guia, porque o guia
    de uma escola de INGLES estava escrito em PORTUGUES: *"pelo teacher's guide estar em
    portugues, nao consigo avaliar se a linguagem usada e efetivamente didatica"*.

O emissor ja recusa guia declarado incompleto. O que ele nao pode fazer e obrigar alguem a
declarar: a aula que nunca cria o `guia_telas.json` passa por ele sem ser vista. E isto.

A DIVIDA E ALVARA, NAO LISTA DE TAREFAS (REGRA 30)
---------------------------------------------------
Materiais escritos antes da forma declarada continuam com a nota em prosa, e eles FUNCIONAM
-- ha aula sendo dada com eles. `guia_em_prosa.json` congela quantas telas de cada material
ainda estao assim. O gate NUNCA exige que esse numero caia; ele exige que **nao suba**.

    A migracao e uma aula por vez, quando o Dan pedir aquela aula.

Material que nao esta no arquivo comeca em zero: aula nova nasce com o guia declarado, de
graca. E o numero congelado so pode CAIR -- `--update` recongela depois de uma migracao
legitima, e recusa recongelar para cima.

ESCOPO: o carimbo `alumni-anatomia=consultivo`, e so o arquivo do PROFESSOR (o do aluno nao
tem `data-teacher` -- e o GATE 36 que garante isso).

USO:
    python3 scripts/consultivo/check_guia_de_tela.py [arquivo.html ...]
    python3 scripts/consultivo/check_guia_de_tela.py --update     # recongela a divida
    python3 scripts/consultivo/check_guia_de_tela.py --selftest
"""
import glob
import html as _html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guia_em_prosa.json")
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# Os dez do 04 §8.2, na ordem. `Exact prompt` e CONDICIONAL: a tela em que o professor nao
# precisa dizer nada que ja nao esteja projetado OMITE a chave -- e omitir e a unica forma
# correta de dizer que nao se aplica (o normativo proibe campo condicional vazio ou com
# "N/A"). Por isso ele nao entra na lista de obrigatorios.
CAMPOS = ["Goal", "Interaction", "Run it", "Expected", "Conditional support",
          "Challenge", "Monitoring", "Evidence to record", "Transition"]

# O guia e do professor brasileiro e, ate 31/08/2026, era escrito em portugues. A regra
# mudou: guia de escola de ingles se escreve em ingles, para que a linguagem didatica dele
# possa ser lida por quem revisa. Estas sao as marcas do portugues que a prosa antiga usava.
_RX_PT = re.compile(
    r"<strong>\s*(?:Objetivo|Conduza|Aten[cç][aã]o|Siga quando|Diga assim|Observe|"
    r"Homework \(oralmente|Pr[oó]xima aula|Registro p[oó]s-aula|CCQ)\b", re.I)


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def eh_professor(c):
    return 'id="tab-inclass"' in c


def notas(c):
    """Cada `data-teacher` do arquivo, ja desescapado (no HTML ele vem como entidade)."""
    return [_html.unescape(m) for m in re.findall(r'\sdata-teacher="([^"]*)"', c)]


def slug_de(caminho):
    return re.sub(r"\.html$", "", os.path.basename(caminho))


def em_prosa(nota):
    """A nota NAO e o guia declarado? Mede pelos campos, nunca pelo idioma.

    Idioma seria o criterio errado: uma nota em ingles com campos inventados continua sendo
    prosa livre, e e o campo que o professor procura na hora da aula."""
    return [c for c in CAMPOS if f"<strong>{c}:</strong>" not in nota]


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA or not eh_professor(c):
        return None
    todas = notas(c)
    prosa = [i for i, n in enumerate(todas, 1) if em_prosa(n)]
    # portugues numa nota QUE JA E o guia declarado e outro defeito: significa que alguem
    # escreveu o campo certo com o texto na lingua errada.
    pt_no_guia = [i for i, n in enumerate(todas, 1)
                  if not em_prosa(n) and _RX_PT.search(n)]
    return {"telas": len(todas), "prosa": len(prosa), "onde": prosa[:6],
            "pt_no_guia": pt_no_guia}


def baseline():
    if not os.path.exists(BASELINE):
        return {}
    return json.load(open(BASELINE, encoding="utf-8")).get("em_prosa", {})


def main(argv):
    alvos = [a for a in argv if not a.startswith("--")]
    if not alvos:
        alvos = sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")))
    base = baseline()
    print(f"=== GATE 53 — o guia de tela tem os dez campos (anatomia {ANATOMIA}) ===")
    atual, total, vistos = {}, 0, 0
    for f in alvos:
        r = confere(f)
        if r is None:
            continue
        vistos += 1
        slug = slug_de(f)
        atual[slug] = r["prosa"]
        teto = base.get(slug, 0)
        rel = os.path.relpath(f, RAIZ)
        if r["pt_no_guia"]:
            total += len(r["pt_no_guia"])
            print(f"  {VERMELHO}FAIL{ZERA}   {rel}: tela(s) {r['pt_no_guia'][:6]} tem o guia "
                  f"declarado com texto em PORTUGUES. O guia e do professor e continua sendo "
                  f"escrito em ingles — e o que permite avaliar a linguagem didatica dele.")
        if r["prosa"] > teto:
            total += 1
            print(f"  {VERMELHO}FAIL{ZERA}   {rel}: {r['prosa']} de {r['telas']} telas com a "
                  f"nota em prosa livre, e a divida congelada e {teto}. Tela(s) "
                  f"{r['onde']}. Declare o guia em `guia_telas.json` — os dez campos do "
                  f"04 §8.2, em ingles, iguais em todas as telas.")
        elif r["prosa"]:
            print(f"  {VERDE}ok{ZERA}     {rel}  ({r['telas'] - r['prosa']}/{r['telas']} "
                  f"declaradas · {r['prosa']} em prosa, dentro do congelado)")
        else:
            print(f"  {VERDE}ok{ZERA}     {rel}  ({r['telas']}/{r['telas']} declaradas)")

    if "--update" in argv:
        # ---- A PRIMEIRA CONGELADA E MEDICAO, NAO AUMENTO
        #
        # Gate novo nasce escopado: sem o arquivo, nao ha divida anterior contra a qual
        # comparar, e recusar o primeiro `--update` deixaria o gate impossivel de ligar.
        # Depois disso a regra vale inteira -- o numero so cai.
        primeira = not os.path.exists(BASELINE)
        sobe = [] if primeira else [s for s, n in atual.items() if n > base.get(s, 0)]
        if sobe:
            print(f"\n{VERMELHO}--update RECUSADO{ZERA}: {sobe} teriam a divida AUMENTADA. "
                  f"Este numero so pode cair.")
            return 1
        json.dump({"_o_que_e": "Telas do consultivo cuja nota de professor ainda e prosa "
                               "livre, e nao o guia declarado de dez campos (Doc 04 §8.2). "
                               "ALVARA, nunca lista de tarefas: o gate exige que o numero "
                               "NAO SUBA, e nunca que ele caia (REGRA 30). Migrar e uma "
                               "aula por vez, quando o Dan pedir aquela aula.",
                   "em_prosa": {k: v for k, v in sorted(atual.items()) if v}},
                  open(BASELINE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"\nrecongelado: {sum(atual.values())} tela(s) em prosa.")
        return 0

    if total:
        print(f"\n{VERMELHO}GATE 53 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    divida = sum(atual.values())
    print(f"\n{VERDE}GATE 53 OK{ZERA} — {vistos} arquivo(s).")
    if divida:
        print(f"  divida congelada: {divida} tela(s) ainda em prosa "
              f"(scripts/consultivo/guia_em_prosa.json). Nao e lista de tarefas.")
    return 0


def selftest():
    falhas = []
    carim = '<meta name="alumni-anatomia" content="consultivo"><div id="tab-inclass"></div>'
    cheia = "".join(f"<strong>{c}:</strong> x<br><br>" for c in CAMPOS)
    if em_prosa(cheia):
        falhas.append("nao reconheceu o guia completo como declarado")
    if not em_prosa(cheia.replace("<strong>Monitoring:</strong>", "<strong>Watch for:</strong>")):
        falhas.append("aceitou um guia com um campo trocado por outro nome")
    if not em_prosa("<strong>Objetivo:</strong> abrir a aula"):
        falhas.append("aceitou prosa livre em portugues como guia")
    # a nota do ALUNO nao existe: arquivo sem a aba in-class fica fora do escopo
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     encoding="utf-8") as fh:
        fh.write('<meta name="alumni-anatomia" content="consultivo"><p>sem deck</p>')
        p = fh.name
    if confere(p) is not None:
        falhas.append("mediu um arquivo sem a aba in-class (o do aluno)")
    os.unlink(p)
    # o campo CONDICIONAL nao pode ser exigido
    if "Exact prompt" in CAMPOS:
        falhas.append("`Exact prompt` esta na lista de obrigatorios, e ele e condicional")
    # portugues DENTRO do guia declarado e visto
    if not _RX_PT.search("<strong>Conduza:</strong> leia com ela"):
        falhas.append("a marca de prosa em portugues nao foi vista")
    if falhas:
        print(VERMELHO + "selftest FALHOU" + ZERA)
        for f in falhas:
            print("  -", f)
        return 1
    print(f"{VERDE}selftest OK{ZERA} — o gate ve campo trocado, prosa livre e portugues no "
          f"guia; ignora o arquivo do aluno; e nao exige o campo condicional.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv[1:]))
