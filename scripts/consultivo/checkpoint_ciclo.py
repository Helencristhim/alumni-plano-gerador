#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""As aulas do painel de checkpoint, numa fonte so -- lida pelo builder, pela voz e pelo gate.

O painel de checkpoint do Registro pos-aula saiu do artefato do Marcos com os numeros do
ciclo DELE escritos em texto: "Checkpoint da aula 22", "Decisao sobre as aulas 23-38", "as
aulas 19 a 22 continuam registradas". O JS ja derivava a aula do checkpoint de `CICLO`
(`cpAula()`), entao o painel liberava na aula certa e anunciava a errada. Na Adriana (bloco
4-7, ciclo 4-23) a professora decidia sobre "as aulas 23-38", quinze delas fora do contrato.

O shell agora traz MARCADORES no lugar dos numeros (`extrai_shell.CORRECOES`,
`checkpoint-*`), e quem os preenche e o builder, com a mesma conta do `cpAula()`:

    {{CP_PRIMEIRA}}  primeira aula do ciclo (= primeira do bloco 1)
    {{CP_AULA}}      ultima aula do bloco 1, a do checkpoint
    {{CP_RESTO}}     primeira aula depois do checkpoint
    {{CP_FIM}}       ultima aula do ciclo

Modulo proprio porque sao tres leitores: o builder preenche, o `voz.py` precisa do shell
preenchido para separar o rotulo do shell do texto do autor, e o GATE confere o publicado.
Tres copias da conta divergiriam na primeira edicao.
"""
import re

MARCADORES = ("{{CP_PRIMEIRA}}", "{{CP_AULA}}", "{{CP_RESTO}}", "{{CP_FIM}}")


def intervalo(ciclo):
    """(primeira, aula do checkpoint, primeira depois dele, ultima do ciclo), mensagem de
    recusa). Nada tem default: sem o dado, o painel diria um numero inventado."""
    ciclo = ciclo or {}
    faltam = [k for k in ("primeira", "porBloco", "aulas")
              if not isinstance(ciclo.get(k), int) or isinstance(ciclo.get(k), bool)
              or ciclo.get(k) < 1]
    if faltam:
        return None, (f"config: `ciclo` sem {faltam} (inteiro >= 1). O painel de checkpoint "
                      f"escreve a aula do checkpoint e o intervalo das aulas seguintes a "
                      f"partir de `ciclo.primeira`, `ciclo.porBloco` e `ciclo.aulas`; sem "
                      f"eles nao ha numero certo para escrever.")
    pri, blo, tot = ciclo["primeira"], ciclo["porBloco"], ciclo["aulas"]
    if blo >= tot:
        return None, (f"config: `ciclo.porBloco` ({blo}) nao e menor que `ciclo.aulas` "
                      f"({tot}). Nao ha aulas depois do checkpoint para o painel decidir.")
    cp = pri + blo - 1
    return (pri, cp, cp + 1, pri + tot - 1), None


def preenche(html, ciclo, exige_marcadores=True):
    """Troca os marcadores pelos numeros do ciclo. Devolve (html, erros)."""
    valores, erro = intervalo(ciclo)
    if erro:
        return html, [erro]
    ausentes = [m for m in MARCADORES if m not in html]
    if ausentes and exige_marcadores:
        raise SystemExit(f"o shell nao tem {ausentes}. O painel de checkpoint voltaria com os "
                         f"numeros do artefato -- rode scripts/consultivo/extrai_shell.py.")
    for marcador, valor in zip(MARCADORES, valores):
        html = html.replace(marcador, str(valor))
    return html, []


def ciclo_do_material(html):
    """O `var CICLO` que o builder escreveu no material, como dict -- ou None."""
    m = re.search(r"var CICLO=\{([^}]*)\}", html)
    if not m:
        return None
    campos = {}
    for chave in ("primeira", "porBloco", "aulas"):
        v = re.search(r"\b" + chave + r":(\d+)", m.group(1))
        if v:
            campos[chave] = int(v.group(1))
    return campos
