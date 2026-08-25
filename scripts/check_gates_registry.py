#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""META-GATE — todo gate declara o que cobre.

POR QUE ISTO EXISTE (06/08/2026)
--------------------------------
O repo tem 28 gates. Levantando-os um a um apareceram duas coisas:

  1. `check_ppp_lesson.py` e `check_contrato_aula.py` se declaravam OS DOIS "GATE 12",
     no mesmo arquivo de CI. Ninguem percebeu porque nada conferia.
  2. Gates de ANATOMIA rodavam no repo inteiro. Enquanto so existia um molde isso era
     inofensivo. Com um molde novo entrando, deixa de ser: uma regra escrita para a
     forma da helen-mendes passa a reprovar material que nunca teve aquela forma — e a
     saida obvia (afrouxar o gate) contamina os 1.221 arquivos que dependem dele.

A ordem do Dan (06/08/2026):

    "precisa garantir que os gates funcionem pras versoes especificas que foram criados,
     a nao ser os gates que se encaixem em ambos"

Este meta-gate transforma essa ordem de INTENCAO em IMPOSSIBILIDADE.

A REGRA QUE ELE COBRA
---------------------
    anatomia e sequencia  -> SEMPRE escopados (framework ou marcador)
    integridade, autorizacao, regressao, processo -> valem para todos os moldes

A divisao nao e arbitraria: botao morto, MP3 podre, contraste ilegivel e HTML truncado
sao defeito em QUALQUER molde. Ja "tem 7 capitulos na ordem X" so faz sentido para quem
tem esses capitulos.

O QUE ELE REPROVA
-----------------
  1. `check_*.py` (ou .mjs) que existe no disco e nao esta em scripts/gates.json
  2. entrada no registro cujo arquivo nao existe mais
  3. dois gates reivindicando o mesmo numero
  4. gate de anatomia/sequencia com escopo "repo"
  5. escopo por framework citando id que nao existe em public/data/frameworks.json
  6. tipo fora da lista de tipos declarada no proprio registro

USO:
    python3 scripts/check_gates_registry.py             # confere
    python3 scripts/check_gates_registry.py --selftest  # prova que ainda morde
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRO = os.path.join(RAIZ, "scripts", "gates.json")
FRAMEWORKS = os.path.join(RAIZ, "public", "data", "frameworks.json")

SEMPRE_ESCOPADOS = {"anatomia", "sequencia"}
NUNCA_ESCOPADOS = {"integridade", "autorizacao", "regressao", "processo"}

# Arquivos check_* que NAO sao gates (ferramenta de conserto, gerador, etc.).
NAO_E_GATE = set()


def carrega():
    with open(REGISTRO, encoding="utf-8") as fh:
        reg = json.load(fh)
    with open(FRAMEWORKS, encoding="utf-8") as fh:
        fw = json.load(fh)
    ids = {f["id"] for c in fw["categorias"] for f in c["frameworks"]}
    return reg, ids


def gates_no_disco():
    achados = {}
    # scripts/consultivo e a pasta do molde consultivo. Ela entra AQUI, e nao so no
    # gates.json, porque a checagem 1 (gate no disco sem entrada no registro) so alcanca o
    # que esta nesta lista: uma pasta nova fora dela abriria exatamente o buraco que este
    # meta-gate existe para fechar -- gate que roda no CI e que ninguem declarou.
    for pasta in ("scripts", os.path.join("scripts", "consultivo"), os.path.join("_build", "model")):
        d = os.path.join(RAIZ, pasta)
        # NUNCA `continue` em silencio. Renomear a pasta de um molde (private-black ->
        # consultivo, 25/08/2026) fazia este laco pular ela caladinho, e a checagem 1
        # (gate no disco sem entrada no registro) deixava de alcancar os gates que moram
        # la -- verde, medindo menos. E o buraco que o proprio meta-gate existe para
        # fechar. Pasta declarada que sumiu e erro, nao ausencia.
        if not os.path.isdir(d):
            raise SystemExit(
                f"check_gates_registry: a pasta declarada {pasta!r} nao existe. Se ela foi "
                f"renomeada, atualize a lista em gates_no_disco() -- senao os gates que "
                f"moram nela deixam de ser conferidos, em silencio.")
        for nome in sorted(os.listdir(d)):
            if not nome.startswith("check_"):
                continue
            if not (nome.endswith(".py") or nome.endswith(".mjs")):
                continue
            if nome in NAO_E_GATE:
                continue
            achados.setdefault(nome, pasta)
    return achados


def verifica(reg, ids_framework, disco):
    erros = []
    tipos_validos = set(reg["_tipos"])
    entradas = reg["gates"]

    # 1 — gate no disco sem entrada no registro
    for nome, pasta in disco.items():
        if nome not in entradas:
            erros.append(
                f"{pasta}/{nome}: existe no disco e NAO esta em scripts/gates.json. "
                f"Gate novo nasce declarado — tipo, escopo e numero. Sem isso ninguem "
                f"consegue responder 'este gate vale para o molde novo?'."
            )

    # 2 — entrada apontando para arquivo que nao existe mais
    for nome, meta in entradas.items():
        if nome in disco:
            continue
        pasta = meta.get("caminho", "scripts")
        if os.path.exists(os.path.join(RAIZ, pasta, nome)):
            continue
        erros.append(f"gates.json cita '{nome}', que nao existe em {pasta}/. Entrada orfa.")

    # 3 — numero duplicado
    usados = {}
    for nome, meta in entradas.items():
        n = meta.get("gate")
        if n is None:
            continue
        usados.setdefault(str(n), []).append(nome)
    for n, donos in sorted(usados.items()):
        if len(donos) > 1:
            erros.append(
                f"GATE {n} reivindicado por {len(donos)} gates: {', '.join(sorted(donos))}. "
                f"Numero duplicado faz o CI mentir sobre o que passou."
            )

    for nome, meta in entradas.items():
        tipo = meta.get("tipo")
        escopo = meta.get("escopo")

        # 6 — tipo valido
        if tipo not in tipos_validos:
            erros.append(f"{nome}: tipo {tipo!r} nao existe em _tipos.")
            continue

        # 4 — anatomia/sequencia nao pode valer para o repo inteiro
        if tipo in SEMPRE_ESCOPADOS and escopo == "repo":
            erros.append(
                f"{nome}: tipo '{tipo}' com escopo 'repo'. Gate de {tipo} mede a FORMA de "
                f"um molde — rodando em tudo, ele reprova material que nunca teve aquela "
                f"forma. Declare framework ou marcador."
            )

        # 5 — framework citado tem que existir
        if isinstance(escopo, dict) and "framework" in escopo:
            for fid in escopo["framework"]:
                if fid not in ids_framework:
                    erros.append(
                        f"{nome}: escopo cita framework '{fid}', que nao existe em "
                        f"public/data/frameworks.json."
                    )
        if isinstance(escopo, dict) and not ({"framework", "marcador"} & set(escopo)):
            erros.append(f"{nome}: escopo {escopo!r} sem 'framework' nem 'marcador'.")

    return erros


def selftest():
    """Prova que o gate morde: injeta cada defeito e exige que ele seja pego."""
    reg, ids = carrega()
    disco = gates_no_disco()
    base = verifica(reg, ids, disco)
    if base:
        print("SELFTEST INCONCLUSIVO — o registro ja esta com erro:")
        for e in base:
            print("   -", e)
        return 1

    casos = []

    import copy

    d = copy.deepcopy(reg)
    d["gates"]["check_ppp_lesson.py"]["gate"] = 11
    casos.append(("numero duplicado", d, "reivindicado por"))

    d = copy.deepcopy(reg)
    d["gates"]["check_ppp_lesson.py"]["escopo"] = "repo"
    casos.append(("anatomia sem escopo", d, "com escopo 'repo'"))

    d = copy.deepcopy(reg)
    d["gates"]["check_ppp_lesson.py"]["escopo"] = {"framework": ["framework-que-nao-existe"]}
    casos.append(("framework inexistente", d, "nao existe em"))

    d = copy.deepcopy(reg)
    d["gates"]["check_ppp_lesson.py"]["tipo"] = "inventado"
    casos.append(("tipo invalido", d, "nao existe em _tipos"))

    d = copy.deepcopy(reg)
    del d["gates"]["check_ppp_lesson.py"]
    casos.append(("gate nao registrado", d, "NAO esta em scripts/gates.json"))

    falhou = False
    for rotulo, mutante, esperado in casos:
        erros = verifica(mutante, ids, disco)
        pegou = any(esperado in e for e in erros)
        print(f"  {'OK  ' if pegou else 'FALHA'}  {rotulo}")
        if not pegou:
            falhou = True
            print(f"         esperava mensagem contendo {esperado!r}; veio: {erros}")
    if falhou:
        print("\nSELFTEST FALHOU — o meta-gate parou de morder.")
        return 1
    print("\nSELFTEST OK — os 5 defeitos sao pegos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    reg, ids = carrega()
    disco = gates_no_disco()
    erros = verifica(reg, ids, disco)
    print("=== META-GATE — registro de gates ===")
    print(f"{len(reg['gates'])} gates registrados, {len(disco)} check_* no disco")

    # A LISTA E DERIVADA, nunca digitada. Um campo "vale_para_ambos" seria um segundo lugar
    # dizendo a mesma coisa — e dois lugares divergem. Aqui a resposta sai do ESCOPO, que e
    # o mesmo dado que o gate usa para decidir se morde.
    ambos, so_um = [], {}
    for nome, meta in reg["gates"].items():
        esc = meta.get("escopo")
        rot = f"{nome} [{meta.get('tipo')}]"
        if esc == "repo":
            ambos.append(rot)
        elif isinstance(esc, dict) and esc.get("framework"):
            for f in esc["framework"]:
                so_um.setdefault(f, []).append(rot)
        elif isinstance(esc, dict) and esc.get("marcador"):
            so_um.setdefault(f"(marcador: {esc['marcador']})", []).append(rot)
    print()
    print(f"VALEM PARA TODOS OS MOLDES — {len(ambos)}")
    print("  integridade, autorizacao, regressao e processo: botao morto e botao morto,")
    print("  MP3 podre e MP3 podre, em qualquer anatomia.")
    for g in sorted(ambos):
        print(f"    {g}")
    print()
    print("ESCOPADOS A UM MOLDE — anatomia e sequencia, que medem FORMA")
    for chave in sorted(so_um):
        print(f"  {chave}")
        for g in sorted(so_um[chave]):
            print(f"    {g}")
    print()
    if erros:
        for e in erros:
            print(f"  ERRO  {e}")
        print(f"\n{len(erros)} problema(s).")
        return 1
    print("OK — todo gate declara tipo, escopo e numero unico.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
