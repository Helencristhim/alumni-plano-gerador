#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a entrada `consultivo` do inventario (_build/model/anatomias.json) MEDINDO o artefato.

POR QUE GERADO, E NAO ESCRITO A MAO
-----------------------------------
O inventario existe para que nenhuma peca suma sem ninguem ver. Em 07/08/2026 ele foi
escrito a mao a partir da COPIA -- catalogou as classes `ic-*` que o porte tinha inventado --
e o GATE 20 passou a comparar a copia consigo mesma: verde para sempre, medindo coerencia
interna e chamando isso de fidelidade. Quatro pecas do artefato (callout, a mais usada,
23,8 usos/aula; tbl-wrap; quiz-option; rule-box) ficaram de fora e ninguem notou por meses.

    "um inventario construido a partir da copia valida qualquer copia"

Aqui o inventario e MEDIDO no artefato, por regiao, com contagem. Ninguem digita a lista,
entao ninguem pode digita-la errado -- e o `--check` no CI reprova se o arquivo no disco
deixar de ser o que sairia da medicao de hoje.

USO:
    python3 scripts/consultivo/gen_inventario.py            # escreve
    python3 scripts/consultivo/gen_inventario.py --check    # so confere
"""
import collections
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-consultivo.html")
INV = os.path.join(RAIZ, "_build", "model", "anatomias.json")

# Regiao -> como acha-la. A regiao importa: a mesma classe pode servir a dois lugares, e o
# que se perde numa nao se ve na outra.
REGIOES = [
    ("planning", r'<div class="tab-content[^>]*id="tab-planning"'),
    ("syllabus", r'<div class="tab-content[^>]*id="tab-syllabus"'),
    ("preclass", r'<div class="tab-content[^>]*id="tab-preclass"'),
    ("inclass", r'<div class="tab-content[^>]*id="tab-inclass"'),
    ("feedback", r'<div class="tab-content[^>]*id="tab-feedback"'),
    ("postclass", r'<div class="tab-content[^>]*id="tab-postclass"'),
    ("deck", r'<div class="slides-wrapper"'),
]

# Estado e utilitario de uma letra: nao sao componentes, e listar isso e ruido.
RUIDO = re.compile(r"^(active|current|open|done|on|off|sel|hidden|visible|n|num|sub|lead|"
                   r"data|accent|ghost|warn|go|mini|correct|wrong|disabled)$")


def mascara_script_style(s):
    out = list(s)
    for m in re.finditer(r"<(script|style)\b[^>]*>(.*?)</\1\s*>", s, re.S):
        for k in range(m.start(2), m.end(2)):
            if out[k] != "\n":
                out[k] = "."
    return "".join(out)


def fecha_tag(s, i, tag="div"):
    d = 0
    for m in re.finditer(r"<" + tag + r"\b|</" + tag + r"\s*>", s[i:]):
        d += 1 if not m.group(0).startswith("</") else -1
        if d == 0:
            return i + m.end()
    raise SystemExit("tag nao fecha em " + str(i))


def mede():
    h = open(ARTEFATO, encoding="utf-8").read()
    hm = mascara_script_style(h)
    por_regiao, todas = {}, collections.Counter()
    for nome, rx in REGIOES:
        m = re.search(rx, hm)
        if not m:
            raise SystemExit(f"regiao '{nome}' nao existe no artefato — ele mudou de forma")
        seg = h[m.start():fecha_tag(hm, m.start())]
        c = collections.Counter()
        for mm in re.finditer(r'class="([^"]+)"', seg):
            for cl in mm.group(1).split():
                if not RUIDO.match(cl):
                    c[cl] += 1
                    todas[cl] += 1
        por_regiao[nome] = dict(sorted(c.items(), key=lambda x: (-x[1], x[0])))
    return por_regiao, todas


SHELL_PROF = os.path.join(RAIZ, "_build", "model", "shells", "consultivo.html")
SHELL_ALU = os.path.join(RAIZ, "_build", "model", "shells", "consultivo-aluno.html")


def abas_de(caminho):
    if not os.path.exists(caminho):
        return []
    s = open(caminho, encoding="utf-8").read()
    return sorted(set(re.findall(r'<div class="tab-content[^>]*id="tab-(\w+)"', s)))


def monta():
    por_regiao, todas = mede()
    h = open(ARTEFATO, encoding="utf-8").read()
    return {
        "_o_que_e": ("A anatomia do molde adulto NOVO. O molde e stephanie-vicente; este "
                     "inventario descreve a FORMA que ele passa a ter. As classes sao "
                     "MEDIDAS no artefato por scripts/consultivo/gen_inventario.py -- nunca "
                     "digitadas, porque inventario escrito a mao a partir da copia valida "
                     "qualquer copia."),
        "artefato": "_build/model/artefatos/marcos-consultivo.html",
        "shell": "_build/model/shells/consultivo.html",
        "shell_aluno": "_build/model/shells/consultivo-aluno.html",
        "origem": ("Material do Marcos Mansour, escrito fora do sistema em agosto/2026 ja sob "
                   "o pacote normativo novo (docs/consultivo/). Duas aulas do bloco 1: "
                   "19 Listening into Interaction e 20 Reading into Speaking."),
        # As abas sao MEDIDAS nos dois builds, nao digitadas: o rotulo visivel ("Perfil",
        # "Planning") muda com a visao, e o que o gate consegue conferir e o identificador.
        # Escrever o rotulo aqui criaria uma segunda fonte que diverge na primeira edicao.
        "abas": abas_de(SHELL_PROF),
        "abas_aluno": abas_de(SHELL_ALU),
        "entrega": ("DUAS URLs. A do professor tem a visao docente e a previa da visao do "
                    "aluno; a do aluno nao tem alternador, rota de professor nem conteudo "
                    "docente no arquivo, payload ou estado (P1 §3.1/§3.2, P3 §3). Quem cobra "
                    "e o GATE 36."),
        "etapas": ("OITO por framework, com nomes, funcoes e ordem do Documento 03, e NUNCA "
                   "oito slides: uma etapa pode ocupar varias telas e duas etapas podem "
                   "dividir uma. O numero de telas deriva do conteudo (P2 §17)."),
        "telas_no_artefato": len(re.findall(r'data-slide="', h)),
        "componentes_por_regiao": por_regiao,
        "componentes": dict(sorted(todas.items(), key=lambda x: (-x[1], x[0]))),
        "_como_ler": ("componentes = classe -> quantas vezes aparece no artefato inteiro. "
                      "Peca que sumir do shell reprova no GATE 20; classe nova sem par no "
                      "artefato (uma reescrita) reprova no GATE 21."),
    }


def main():
    check = "--check" in sys.argv
    novo = monta()
    with open(INV, encoding="utf-8") as fh:
        inv = json.load(fh)
    atual = inv["anatomias"].get("consultivo")
    if check:
        if atual != novo:
            print("FALHOU — o inventario no disco nao e o que sairia do artefato hoje.")
            if atual is None:
                print("  (a entrada 'consultivo' nao existe)")
            else:
                a, b = set(atual.get("componentes", {})), set(novo["componentes"])
                if a - b:
                    print("  sobra no inventario:", sorted(a - b)[:12])
                if b - a:
                    print("  falta no inventario:", sorted(b - a)[:12])
            return 1
        print(f"OK — inventario consultivo bate com o artefato "
              f"({len(novo['componentes'])} componentes).")
        return 0
    inv["anatomias"]["consultivo"] = novo
    with open(INV, "w", encoding="utf-8") as fh:
        json.dump(inv, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"escrito: {len(novo['componentes'])} componentes, "
          f"{len(novo['componentes_por_regiao'])} regioes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
