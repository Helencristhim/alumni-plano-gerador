#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 50 — o MOLDE reconstroi dos proprios fragmentos, e o publicado e o que sai dali.

POR QUE ISTO EXISTE
-------------------
Em 28/08/2026 o Dan pediu uma coisa simples: *"preciso que o molde seja capaz de incorporar
o conserto desses erros pro futuro"*. Ao ir aplicar, descobri que o molde **nao reconstruia**
-- e ja nao reconstruia havia dias, sem que nada acusasse:

    cz1: gap-fill de GRAMATICA com banco de palavras.

Uma trava do emissor, correta na intencao, classificava como gramatica um gap-fill de
EXPRESSOES e recusava o banco declarado. O material publicado da Stephanie continuava no ar,
bonito e funcionando; o que tinha morrido era o CAMINHO de volta ate ele.

E isso e pior do que parece, porque o molde e por onde toda correcao entra no sistema. Sete
correcoes de plataforma feitas nesse mesmo dia -- o Check fora da visao do professor, o banco
do gap-fill, a explicacao que abre mesmo com erro, uma aula por vez -- chegaram ao aluno real
e NAO chegaram ao molde. A proxima aula gerada a partir dele nasceria com os defeitos que
tinham acabado de ser corrigidos, e ninguem veria: cada arquivo, isolado, passa em tudo.

    Molde que nao reconstroi nao e molde: e um arquivo antigo que parece um.

O QUE ELE MEDE
--------------
Duas coisas, e as duas sao necessarias:

  1. O builder ACEITA os fragmentos do molde (nenhum assert recusa a geracao).
  2. O que ele produz e BYTE A BYTE o que esta publicado.

A segunda e o que pega a divergencia silenciosa: publicado editado a mao, publicado vindo de
um build antigo, fragmento corrigido que ninguem reconstruiu. Sem ela, o gate diria "o molde
constroi" enquanto o arquivo no ar e outro.

O QUE ELE NAO MEDE
------------------
Conteudo, pedagogia, nivel. Ele nao sabe se a aula e boa -- sabe se ela e REPRODUZIVEL. Os
outros gates cuidam do resto, e todos eles ja rodam sobre o publicado do molde.

USO:
    python3 scripts/consultivo/check_molde_reconstroi.py
    python3 scripts/consultivo/check_molde_reconstroi.py --selftest
"""
import importlib.util
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AQUI = os.path.dirname(os.path.abspath(__file__))
MOLDE = os.path.join(RAIZ, "_build", "consultivo", "stephanie-vicente", "config.json")

VERDE, VERMELHO, ZERO = "\033[32m", "\033[31m", "\033[0m"


def _builder():
    spec = importlib.util.spec_from_file_location(
        "build_consultivo", os.path.join(AQUI, "build_consultivo.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, AQUI)
    spec.loader.exec_module(mod)
    return mod


def confere(config=MOLDE):
    """(ok, mensagens). Monta o material do config e compara com o publicado."""
    build = _builder()
    cfg = json.load(io.open(config, encoding="utf-8"))
    base_frag = os.path.join(RAIZ, cfg["fragmentos"])
    msgs = []
    try:
        prof, _telas, erros = build.monta(cfg, base_frag)
    except SystemExit as e:
        return False, [f"o builder RECUSOU os fragmentos do molde: {e}"]
    if erros:
        return False, ["o builder recusou os fragmentos do molde:"] + [f"  {x}" for x in erros]

    aluno, _ = build.extrai_shell.deriva_aluno(prof)
    slug = cfg["slug"]
    # O NOME VEM DO CONFIG, pelo mesmo caminho do builder. Ter a regra escrita duas vezes
    # e o que fazia este gate conferir um arquivo e o builder escrever OUTRO: a Lucia foi
    # publicada como `-c1`, antes de o sufixo virar `-cicloN`, e um rebuild criava o
    # segundo arquivo deixando o primeiro no ar, desatualizado, que e o link que a
    # professora tem.
    nome = cfg.get("arquivo") or (f"{slug}-ciclo{cfg['ciclo']['numero']}"
                                  if cfg.get("fase") == "piloto" else slug)
    ok = True
    for papel, gerado in (("professor", prof), ("aluno", aluno)):
        caminho = os.path.join(RAIZ, "public", papel, f"{nome}.html")
        if not os.path.exists(caminho):
            msgs.append(f"{papel}: {nome}.html nao existe -- o molde nao esta publicado")
            ok = False
            continue
        publicado = io.open(caminho, encoding="utf-8").read()
        if publicado == gerado:
            msgs.append(f"{papel}: {len(gerado)}B, byte a byte")
        else:
            ok = False
            msgs.append(
                f"{papel}: o publicado tem {len(publicado)}B e o builder devolve "
                f"{len(gerado)}B. O arquivo no ar NAO e o que os fragmentos produzem "
                f"-- rode o builder e commite a saida.")
    return ok, msgs


def selftest():
    """Um fragmento quebrado tem de REPROVAR.

    A prova nao pode ser "o molde passa hoje": isso confunde gate vivo com gate mudo. Aqui o
    config aponta para uma copia dos fragmentos com uma aula sem `observar` no cartao -- o
    builder recusa, e o gate tem de dizer isso em vez de passar."""
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix="molde-selftest-")
    try:
        frag = os.path.join(tmp, "frag")
        shutil.copytree(os.path.join(RAIZ, "_build", "consultivo", "stephanie-vicente"), frag)
        cartao = os.path.join(frag, "aula1", "cartao.json")
        d = json.load(io.open(cartao, encoding="utf-8"))
        d.pop("observar", None)
        io.open(cartao, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False))
        cfg = json.load(io.open(MOLDE, encoding="utf-8"))
        cfg["fragmentos"] = os.path.relpath(frag, RAIZ)
        alvo = os.path.join(tmp, "config.json")
        io.open(alvo, "w", encoding="utf-8").write(json.dumps(cfg, ensure_ascii=False))
        ok, msgs = confere(alvo)
        if ok:
            print("SELFTEST FALHOU — o gate passou com o cartao sem `observar`.")
            return 1
        print("SELFTEST OK — fragmento quebrado reprova:")
        for m in msgs[:3]:
            print("  " + m)
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def configs():
    """Todo material da anatomia, com o molde primeiro.

    O gate nasceu medindo so o molde, porque a pergunta era "a correcao chega ao molde?".
    Ela vale para TODOS: um material de aluno que nao reconstroi tambem esta fora do
    alcance de qualquer correcao futura, e ninguem descobre ate tentar rebuildar. Medido
    em 01/09/2026: rebuildar material publicado antes desta data expos DOIS defeitos que
    so aparecem assim — um fragmento que o builder recusa (a barra `ao-topo` da Lucia) e
    um nome de arquivo divergente (o `-c1` dela)."""
    todos = sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json")))
    return [MOLDE] + [c for c in todos if c != MOLDE]


def main():
    if "--selftest" in sys.argv:
        return selftest()
    print("=== GATE 50 — todo material reconstroi dos proprios fragmentos ===")
    ok_geral = True
    for cfg_path in configs():
        rotulo = os.path.basename(os.path.dirname(cfg_path))
        if cfg_path == MOLDE:
            rotulo += " (molde)"
        ok, msgs = confere(cfg_path)
        ok_geral = ok_geral and ok
        for m in msgs:
            print(("  " + VERDE + "ok" + ZERO + "    ") if ok else
                  ("  " + VERMELHO + "FAIL" + ZERO + "  "), f"{rotulo} · {m}")
    if ok_geral:
        print("\nGATE 50 OK — todo material da anatomia reconstroi, e o publicado e o que o "
              "builder devolve.")
        return 0
    print(f"\n{VERMELHO}GATE 50 — ha material que nao reproduz.{ZERO} Enquanto isto durar, correcao "
          f"de plataforma NAO chega ao molde, e a proxima aula nasce com o defeito que ja "
          f"foi consertado no aluno.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
