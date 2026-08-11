#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 21 — a interface gerada e a do ARTEFATO.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
O artefato de referencia (`_build/model/artefatos/erica-professor-view.html`, o Professor
View da Erica escrito pela Stephanie) e a ESPECIFICACAO DA INTERFACE. Decisao do Dan, textual:

    "SE AS AULAS NAO ESTAO IDENTICAS AO ARTEFATO, NO QUESITO INTERFACE, ENTAO ESTA ERRADO"
    "pq que eu colocaria esse artefato se nao fosse pra vc imitar ele?"

O porte de 07/08 nao imitou: RENOMEOU e REIMPLEMENTOU cada peca (reveal-item -> ic-reveal,
blank-input -> ic-blank, conf-btn -> ic-self, writebox -> ic-write...) e deixou quatro pecas
de fora — callout (23,8 usos/aula no artefato, a MAIS usada), tbl-wrap, quiz-option e
rule-box, todas com ZERO ocorrencia no molde.

E ninguem viu, porque no mesmo dia o inventario (`anatomias.json`) catalogou os nomes NOVOS e
mandou o GATE 20 conferir o shell contra ELE, "e NUNCA contra o artefato". O gate passou a
comparar a copia consigo mesma: verde para sempre, medindo nada.

Este gate faz a pergunta que faltava: **o que o artefato tem e o gerado nao tem?**

O QUE ELE MEDE
--------------
  A. classes usadas DENTRO de .slide no artefato e ausentes do CSS do shell   (peca nao portada)
  B. classes ic-* do shell sem contrapartida no artefato                      (reescrita orfa)
  C. classes declaradas em anatomias.json que nao existem no artefato         (inventario paralelo)

COMO ELE NAO VIRA UM MURO
-------------------------
A paridade total nao cabe num PR (130 regras de CSS, 27 kinds do builder, 4 aulas a regerar).
Entao o gate trabalha como o GATE 8: congela a divergencia de HOJE em
`scripts/artefato-paridade-baseline.json` e exige que ela so CAIA. Divergencia nova = FALHA
imediata; divergencia velha = tolerada ate o PR que a remove. Quando o baseline chegar a zero,
o `--update` deixa de ser necessario e o gate vira paridade exata.

ESCOPO: so a anatomia guided-discovery (o shell dela e as aulas com <meta alumni-framework>
dos 4 frameworks dessa anatomia). O resto do repo nao e acusado — gate novo nasce escopado.

USO:
    python3 scripts/check_artefato_paridade.py
    python3 scripts/check_artefato_paridade.py --selftest
    python3 scripts/check_artefato_paridade.py --update    # so quando a divergencia CAIU
"""
import collections
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "erica-professor-view.html")
SHELL = os.path.join(RAIZ, "_build", "model", "shells", "guided-discovery.html")
INV = os.path.join(RAIZ, "_build", "model", "anatomias.json")
BASELINE = os.path.join(RAIZ, "scripts", "artefato-paridade-baseline.json")

# Classes que NAO sao interface de aula: utilitario generico do artefato, chrome do browser,
# ou nome de uma letra. Comparar isto so gera ruido.
IGNORAR = re.compile(r'^(fa|svg|icon)-|^(active|current|completed|upcoming|open|done|on|off'
                     r'|hidden|show|visible)$|^.$')


# ── O CHASSI ──────────────────────────────────────────────────────────────────────────
# Ate 11/08/2026 o chassi do guided-discovery era o do shell imersivo (helen-mendes), porque
# o shell nasceu clonado dele. Decisao do Dan naquele dia: "os dois moldes devem ser
# separados mesmo, em si" — o chassi do guided-discovery passa a sair do ARTEFATO, e o do
# imersivo NAO MUDA (nenhum aluno do molde antigo pode ser afetado).
#
# Estes seletores tem de bater com o artefato byte a byte. O GATE 18 nao pega isto: ele
# compara PRESENCA de funcao e de classe entre os dois shells, nao o VALOR das regras — um
# `max-width` revertido de 940 para 920 passaria por ele sem um pio.
CHASSI = [
    ".slide", ".slide.active", ".slide-inner",
    ".slide-light", ".slide-light .slide-inner",
    ".slide-dark", ".slide-dark .slide-inner",
    ".slide-image", ".slide-image::before", ".slide-image .slide-inner",
    ".chapter-label", ".slide-title", ".slide-subtitle", ".slide-heading", ".slide-lead",
    ".audio-btn-sm", ".audio-btn-sm:hover", ".roleplay-card", ".roleplay-kw", ".stage-pill",
]

# Onde o artefato fixa uma cor DA ERICA, o shell usa o equivalente parametrizado — o
# artefato e a pagina de UMA aluna, o shell e a forma dela (REGRA 10). Toda adaptacao vive
# AQUI, declarada: o que nao estiver nesta tabela e divergencia e reprova.
ADAPTACOES_DE_PALETA = {
    ".stage-pill": [("rgba(15,76,117,.14)", "rgba(190,18,60,.14)")],
    ".audio-btn-sm:hover": [("#0a3a5c", "var(--accent-light)")],
}


def _corpos(txt):
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", txt, re.S))
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    d = {}
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        sel = re.sub(r"\s+", " ", m.group(1)).strip()
        d.setdefault(sel, m.group(2).strip())
    return d


def medir_chassi(art, shell):
    """Seletores de chassi cujo corpo no shell NAO e o do artefato (pos-adaptacao)."""
    ra, rs = _corpos(art), _corpos(shell)
    fora = []
    for sel in CHASSI:
        a, s_ = ra.get(sel), rs.get(sel)
        if a is None or s_ is None:
            fora.append((sel, "ausente", "ausente" if s_ is None else "presente"))
            continue
        esperado = a
        for de, para in ADAPTACOES_DE_PALETA.get(sel, []):
            esperado = esperado.replace(de, para)
        norm = lambda x: re.sub(r"\s+", "", x).rstrip(";")
        if norm(esperado) != norm(s_):
            fora.append((sel, esperado[:70], s_[:70]))
    return fora


def le(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def css_classes(s):
    """Classes DEFINIDAS nos <style> do documento.

    COMENTARIO NAO E REGRA. Sem remover /* ... */ antes, um comentario que CITA o nome da
    peca ("portado do artefato (.reveal-item/.r-front/.r-back)") faz o gate acreditar que a
    peca existe — e ela nao existe. Foi assim que .r-front e .r-back passaram por "presentes"
    na primeira medicao: a unica ocorrencia delas no shell estava dentro de um comentario.
    Mesma familia do erro que este gate existe para pegar: ler o texto ESCRITO como se fosse
    o efeito PRODUZIDO.
    """
    out = set()
    for st in re.findall(r"<style[^>]*>(.*?)</style>", s, re.S):
        st = re.sub(r"/\*.*?\*/", "", st, flags=re.S)
        for m in re.finditer(r"\.([a-zA-Z][\w-]*)", st):
            out.add(m.group(1))
    return out


def classes_em_slide(s):
    """Classes usadas DENTRO de um <div class="slide ...">, com a contagem.

    A conta e por profundidade de <div>: entra ao abrir um .slide, sai ao fechar o mesmo.
    O chrome do Professor View (hub, menu, abas, syllabus) fica de fora de proposito — ele e
    outro shell (hub-guided-discovery.html) e outro trabalho.
    """
    usos = collections.Counter()
    pilha, dentro = [], 0
    for m in re.finditer(r"<(/?)(\w+)([^>]*)>", s):
        fechando, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if tag != "div":
            if not fechando and dentro:
                c = re.search(r'class="([^"]+)"', attrs)
                if c:
                    usos.update(c.group(1).split())
            continue
        if fechando:
            if pilha and pilha.pop():
                dentro = max(0, dentro - 1)
            continue
        c = re.search(r'class="([^"]+)"', attrs)
        eh_slide = bool(c and "slide" in c.group(1).split())
        if eh_slide:
            dentro += 1
        if c and dentro:
            usos.update(c.group(1).split())
        pilha.append(eh_slide)
    return usos


def medir(art, shell, inv):
    a_slide = classes_em_slide(art)
    a_css = css_classes(art)
    s_css = css_classes(shell)

    faltando = sorted(
        c for c in a_slide
        if c not in s_css and not IGNORAR.match(c) and c in a_css
    )
    orfas = sorted(
        c for c in s_css
        if c.startswith("ic-") and c not in a_css and len(c) > 3
    )
    gd = inv["anatomias"]["guided-discovery"]
    declaradas = [m["classe"] for m in gd["componentes"].values() if m.get("classe")]
    declaradas += [m["classe"] for m in (gd.get("estrutura", {}).get("pecas") or {}).values()
                   if m.get("classe")]
    # EQUIVALENCIA DECLARADA nao e divergencia: e renome com motivo escrito (ex.: a barra de
    # etapas se chama phase-* aqui porque reusa a mecanica que o shell base ja tinha; a
    # aparencia e a mesma). O que o gate persegue e o renome SILENCIOSO.
    equivalentes = {v["aqui"] for v in gd.get("equivalencias", {}).values()
                    if isinstance(v, dict) and v.get("aqui")}
    # PECAS PARADAS: kinds sem forma no artefato, aguardando decisao da autora. Continuam
    # contados nas orfas (nao viram divida invisivel), mas nao contam como declaracao
    # paralela — a declaracao delas E a pendencia.
    paradas = {c for it in (gd.get("_pendente_sem_forma_no_artefato", {}).get("itens") or [])
               for c in it.get("classes", [])}
    paralelas = sorted({c for c in declaradas
                        if c not in a_css and c not in equivalentes and c not in paradas})
    chassi = [sel for sel, _, _ in medir_chassi(art, shell)]
    return {"faltando": faltando, "orfas": orfas, "paralelas": paralelas,
            "chassi": chassi}, a_slide


def compara(atual, base):
    """Novidades = o que esta em `atual` e nao estava no baseline. So isso reprova."""
    novos = {}
    for k, v in atual.items():
        antigo = set(base.get(k, []))
        d = [x for x in v if x not in antigo]
        if d:
            novos[k] = d
    return novos


def relatorio(atual, base, a_slide):
    print("=== GATE 21 — a interface gerada e a do ARTEFATO ===")
    print(f"artefato: {os.path.relpath(ARTEFATO, RAIZ)}")
    rotulos = {
        "faltando": "peca do artefato AUSENTE do shell (nao portada)",
        "orfas": "classe ic-* do shell SEM par no artefato (reescrita orfa)",
        "paralelas": "classe declarada no anatomias.json que NAO existe no artefato",
        "chassi": "regra de CHASSI que nao e mais a do artefato",
    }
    for k, rot in rotulos.items():
        n, nb = len(atual[k]), len(base.get(k, []))
        seta = "=" if n == nb else ("v" if n < nb else "^")
        print(f"  {rot:58} {n:4}  (baseline {nb}) {seta}")
    top = [(a_slide[c], c) for c in atual["faltando"]]
    if top:
        print("\n  as 8 ausencias mais usadas no artefato (por aula, 4 aulas):")
        for n, c in sorted(top, reverse=True)[:8]:
            print(f"     .{c:22} {n/4:6.1f} usos/aula")


def selftest():
    art, shell = le(ARTEFATO), le(SHELL)
    inv = json.loads(le(INV))
    base = json.loads(le(BASELINE)) if os.path.exists(BASELINE) else {}
    atual, _ = medir(art, shell, inv)
    if compara(atual, base):
        print("SELFTEST INCONCLUSIVO — a base ja esta com divergencia nova:")
        print("  ", compara(atual, base))
        return 1

    falhou = False
    casos = []

    # 1. peca do artefato REMOVIDA do shell agora reprova
    shell_mut = shell.replace(".stage-pill", ".xx-removida")
    casos.append(("peca do artefato removida do shell", art, shell_mut, inv, "faltando"))

    # 2. classe ic-* NOVA no shell reprova
    shell_mut2 = shell.replace("</style>", ".ic-invencao-nova{color:red}</style>", 1)
    casos.append(("classe ic-* nova sem par no artefato", art, shell_mut2, inv, "orfas"))

    # 3. componente declarado com nome que nao existe no artefato reprova
    import copy
    inv_mut = copy.deepcopy(inv)
    inv_mut["anatomias"]["guided-discovery"]["componentes"]["reveal"]["classe"] = "zz-paralela"
    casos.append(("declaracao com nome paralelo", art, shell, inv_mut, "paralelas"))

    # 4. chassi revertido para o valor do shell imersivo reprova
    shell_mut3 = shell.replace("max-width:940px;width:100%;position:relative;margin:auto",
                               "max-width:920px;width:100%;position:relative")
    casos.append(("chassi revertido (slide-inner 940 -> 920)", art, shell_mut3, inv, "chassi"))

    for rotulo, a, s, i, chave in casos:
        at, _ = medir(a, s, i)
        pegou = chave in compara(at, base)
        print(f"  {'OK   ' if pegou else 'FALHA'} {rotulo}")
        if not pegou:
            falhou = True

    if falhou:
        print("\nSELFTEST FALHOU — o gate parou de morder.")
        return 1
    print(f"\nSELFTEST OK — {len(casos)} casos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    art, shell = le(ARTEFATO), le(SHELL)
    inv = json.loads(le(INV))
    atual, a_slide = medir(art, shell, inv)

    if "--update" in sys.argv:
        # BOOTSTRAP: sem baseline no disco, o primeiro --update CONGELA o estado de hoje.
        # Sem esta porta, o proprio gate impediria seu primeiro congelamento (tudo "subiu de
        # zero") e nao haveria como comecar a medir.
        primeira = not os.path.exists(BASELINE)
        base = {} if primeira else json.loads(le(BASELINE))
        for k, v in atual.items():
            if not primeira and len(v) > len(base.get(k, [])):
                print(f"RECUSADO: '{k}' subiu de {len(base.get(k, []))} para {len(v)}. "
                      f"O baseline so pode CAIR — conserte a divergencia nova primeiro.")
                return 1
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump(atual, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print(f"baseline {'CRIADO' if primeira else 'recongelado'}: "
              f"{ {k: len(v) for k, v in atual.items()} }")
        return 0

    base = json.loads(le(BASELINE)) if os.path.exists(BASELINE) else {}
    relatorio(atual, base, a_slide)
    novos = compara(atual, base)
    if novos:
        print("\n  DIVERGENCIA NOVA (nao estava no baseline) — isto reprova:")
        for k, v in novos.items():
            for c in v:
                print(f"     [{k}] .{c}")
        print("\n  O artefato e a especificacao da interface. Use a classe DELE, com o CSS")
        print("  dele (_build/model/artefatos/erica-professor-view.html). Se a diferenca for")
        print("  exigida por doutrina (REGRA 7 / 7.1 / 13), declare em artefatos/README.md.")
        return 1
    print("\nOK — nenhuma divergencia NOVA. A divida congelada so pode cair.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
