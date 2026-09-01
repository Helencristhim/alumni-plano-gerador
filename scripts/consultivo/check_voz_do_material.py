#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 51 — o material fala DO ALUNO, nunca de si mesmo nem do processo que o produziu.

POR QUE ISTO EXISTE (01/09/2026)
--------------------------------
O Dan abriu a primeira pagina do material da Joice — a aba Perfil, que a professora le
antes da aula — e achou isto:

    "E o primeiro A1 desta anatomia: os quatro materiais anteriores sao B1+. O pacote
     normativo cobre A1 explicitamente e autoriza apoio em portugues neste nivel."

Isso nao descreve a aluna. Descreve o SISTEMA que produziu o arquivo, na pagina que existe
para descrever a aluna. Junto vieram os codigos internos das hipoteses (`H1`, `H2`, `H3`)
usados como se a professora soubesse o que sao, `checkpoint`, `estado pedagogico`,
`criterio N do ciclo`, e o material justificando o proprio desenho ("nao e escolha
tematica", "o bloco mede fala e interacao"). Num cartao de aula havia ate uma referencia a
hipotese "do bloco do Caio" — outro aluno.

    A regra: o vocabulario de PRODUCAO nao aparece na superficie de LEITURA.
    O conteudo pedagogico continua; muda a lingua em que ele e dito.

Nada disso e sutil, e nenhum gate via, porque todos os outros medem forma (etapas,
minutos, componentes, audio) e este mede a VOZ.

O QUE ELE MEDE, E ONDE
----------------------
So o que um humano LE no arquivo publicado da anatomia `consultivo`:

  - o texto visivel (fora de <script> e <style>);
  - as notas de tela (`data-teacher`), que e o que a professora abre durante a aula;
  - as strings do `var GUIDE` e dos cartoes, que sao o guia e o cartao de cada aula.

NAO mede o codigo do shell: `checkpoint` como nome de variavel ou classe CSS e outra
coisa, e acusa-lo daria falso positivo em todos os 12 arquivos (medido).

A DIVIDA ANTERIOR FICA CONGELADA
--------------------------------
`voz-baseline.json` guarda quantas ocorrencias cada arquivo JA tinha em 01/09/2026. O gate
so reprova o que PASSAR desse numero. Isso e deliberado: os materiais do Luiz, da Lucia e
da Stephanie sao anteriores a esta correcao e nao se mexe neles sem pedido (REGRA 30).
A baseline so pode CAIR — `--update` recongela depois de uma limpeza legitima.

USO:
    python3 scripts/consultivo/check_voz_do_material.py
    python3 scripts/consultivo/check_voz_do_material.py --update    # recongela a base
    python3 scripts/consultivo/check_voz_do_material.py --selftest  # prova que morde
"""
import glob
import html as _html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voz-baseline.json")
ANATOMIA = "consultivo"

VERM, VERDE, AMAR, ZERA = "\033[31m", "\033[32m", "\033[33m", "\033[0m"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voz  # noqa: E402  a MESMA lista que o BUILDER usa para recusar a geracao

REGRAS = voz.REGRAS
superficie = voz.superficie
shell_superficie = voz.shell_superficie
_janelas = voz.janelas


def config_do(caminho):
    """O config do material, para as regras que precisam do slug e do tratamento."""
    arq = os.path.basename(caminho)
    for cfg in sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*",
                                             "config.json"))):
        try:
            with open(cfg, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        if d.get("slug") and arq.startswith(d["slug"]):
            return d
    return {}


def mede(caminho):
    c = open(caminho, encoding="utf-8", errors="replace").read()
    if 'name="alumni-anatomia" content="%s"' % ANATOMIA not in c[:4000]:
        return None
    cfg = config_do(caminho)
    achados = voz.confere(c, slug=cfg.get("slug"),
                          tratamento=(cfg.get("professor") or {}).get("tratamento", ""))
    fora = {rid: 0 for rid, _, _ in REGRAS}
    fora["contaminacao-de-aluno"] = 0
    fora["genero-do-docente"] = 0
    for a in achados:
        if a.startswith("CONTAMINACAO DE ALUNO"):
            fora["contaminacao-de-aluno"] += 1
        elif a.startswith("GENERO DO DOCENTE"):
            fora["genero-do-docente"] += 1
        else:
            rid = a.split("(", 1)[1].split(",", 1)[0]
            fora[rid] = fora.get(rid, 0) + 1
    mede.ultimo = achados
    return fora


def alvos():
    for lado in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", lado, "*.html"))):
            yield p


def carrega():
    if not os.path.exists(BASE):
        return {}
    with open(BASE, encoding="utf-8") as f:
        return json.load(f).get("arquivos", {})


def main():
    if "--selftest" in sys.argv:
        return selftest()
    base = carrega()
    atual, fails, limpos, textos_extra = {}, [], 0, {}
    for p in alvos():
        m = mede(p)
        if m is None:
            continue
        rel = os.path.relpath(p, RAIZ)
        textos_extra[rel] = list(getattr(mede, "ultimo", []))
        atual[rel] = {k: v for k, v in m.items() if v}
        antes = base.get(rel, {})
        piorou = {k: (antes.get(k, 0), v) for k, v in m.items() if v > antes.get(k, 0)}
        if piorou:
            fails.append((rel, piorou))
        elif not atual[rel]:
            limpos += 1

    if "--update" in sys.argv:
        with open(BASE, "w", encoding="utf-8") as f:
            json.dump({
                "_leia": ("Quanta voz de PRODUCAO cada material publicado da anatomia "
                          "consultivo ainda carrega. NAO e uma lista de tarefas: e o "
                          "ALVARA do que ja existia em 01/09/2026 e que nao se mexe sem "
                          "pedido (REGRA 30). O gate reprova o que PASSAR desses numeros. "
                          "Recongelar (--update) so depois de uma limpeza legitima: a base "
                          "so pode CAIR."),
                "arquivos": {k: v for k, v in sorted(atual.items()) if v},
            }, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print(f"baseline recongelada: {sum(sum(v.values()) for v in atual.values())} "
              f"ocorrencia(s) em {len([1 for v in atual.values() if v])} arquivo(s).")
        return 0

    textos = {rid: t for rid, t, _ in REGRAS}
    print(f"=== GATE 51 — a voz do material (anatomia {ANATOMIA}) ===")
    for rel, piorou in fails:
        print(f"{VERM}FAIL{ZERA}  {rel}")
        for t in textos_extra.get(rel, []):
            print(f"        {t}")
    if fails:
        print(f"\n{VERM}GATE 51 — {len(fails)} arquivo(s) com voz de producao NOVA.{ZERA}")
        print("A pagina descreve o aluno. O vocabulario de quem produziu o material fica "
              "fora dela.")
        return 1
    divida = sum(sum(v.values()) for v in atual.values())
    print(f"{VERDE}GATE 51 OK{ZERA} — {len(atual)} arquivo(s) da anatomia; {limpos} sem "
          f"nenhuma ocorrencia.")
    if divida:
        print(f"  divida congelada: {divida} ocorrencia(s) anteriores a 01/09/2026 "
              f"(scripts/consultivo/voz-baseline.json). Nao e lista de tarefas.")
    return 0


def selftest():
    """Prova que morde, e que o BUILDER usa a mesma lista.

    O selftest do gate nao pode provar so o gate: o que impede o defeito de nascer e o
    assert do builder, e os dois so valem se lerem a MESMA fonte. Aqui se confere o
    objeto, e nao a intencao."""
    falhas = []
    amostras = {
        "codigo-de-hipotese": "e a hipótese H1, decidida depois",
        "checkpoint": "esta e a aula do checkpoint",
        "estado-pedagogico": "leia o estado pedagogico antes",
        "documento-normativo": "o pacote normativo cobre A1",
        "criterio-numerado": "e o criterio 2 do ciclo",
        "defeito": "o defeito tem forma precisa",
        "material-falando-de-si": "nao e escolha tematica",
    }
    carimbo = '<meta name="alumni-anatomia" content="consultivo">'
    for rid, _, rx in REGRAS:
        visivel = f"{carimbo}<p>{amostras[rid]}</p>"
        escondido = f'{carimbo}<script>var x = "{amostras[rid]}";</script>'
        if not re.findall(rx, superficie(visivel), re.I):
            falhas.append(f"{rid}: NAO viu o padrao no texto visivel")
        if re.findall(rx, superficie(escondido), re.I):
            falhas.append(f"{rid}: viu o padrao DENTRO de <script> (falso positivo)")

    # genero: a forma feminina sem declaracao reprova; a masculina, nao
    if not voz.confere(f"{carimbo}<p>a producao e sempre com a professora</p>"):
        falhas.append("genero: NAO viu a forma feminina sem declaracao")
    if voz.confere(f"{carimbo}<p>o professor conduz a etapa</p>"):
        falhas.append("genero: reprovou a forma padrao ('o professor') sem declaracao")

    # contaminacao de aluno, com um slug real da anatomia
    alunos = voz.alunos_da_anatomia()
    if len(alunos) >= 2:
        meu, outro = list(alunos)[0], list(alunos)[1]
        texto = f"{carimbo}<p>compare com o material do {alunos[outro].split()[0]}</p>"
        if not any("CONTAMINACAO DE ALUNO" in a for a in voz.confere(texto, slug=meu)):
            falhas.append("aluno: NAO viu o nome de outro aluno na tela")
        if any("CONTAMINACAO DE ALUNO" in a for a in voz.confere(texto, slug=outro)):
            falhas.append("aluno: acusou o material de nomear O PROPRIO aluno")

    # A FONTE E UMA SO: o builder tem de recusar exatamente o que o gate acusa
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "build_consultivo", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "build_consultivo.py"))
    b = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(b)
        if getattr(b, "voz", None) is not voz:
            falhas.append("o builder NAO usa este modulo — as listas podem divergir")
    except Exception as e:
        falhas.append(f"nao consegui carregar o builder para conferir a fonte: {e}")

    for f in falhas:
        print(f"{VERM}selftest FAIL{ZERA}  {f}")
    if falhas:
        return 1
    print(f"{VERDE}selftest OK{ZERA} — as {len(REGRAS)} regras veem o texto visivel e "
          f"ignoram o codigo; a do genero distingue forma marcada de padrao; a de aluno "
          f"poupa o proprio; e o BUILDER le esta mesma lista.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
