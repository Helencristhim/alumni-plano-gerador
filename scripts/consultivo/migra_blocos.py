#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Converte atividade escrita a mao em declaracao -- e so aceita se voltar IGUAL.

POR QUE UM CONVERSOR, E NAO transcrever a mao
-----------------------------------------------
O molde tem 48 `exercise-section` escritas em HTML. Transcrever uma a uma e trabalho
mecanico, demorado e -- pior -- e exatamente o tipo de trabalho em que se erra sem perceber:
uma opcao a menos, uma resposta trocada, uma aspa que vira outra coisa. Foi assim que o
porte de 11/08/2026 renomeou cada peca e ninguem viu por meses.

Este script faz a conversao e, para CADA atividade, renderiza a declaracao de volta e
compara com o HTML original. Diferiu um byte, ele RECUSA aquela atividade e diz onde.

    a garantia nao e "o conversor e bom".
    e "o que ele nao consegue provar, ele nao converte".

O QUE ELE NAO FAZ
-----------------
Adivinhar. Atividade cuja forma ele nao reconhece sai na lista de PENDENTES, com o motivo, e
continua em HTML -- que e o comportamento certo: `<!--BLOCOS-->` ausente e no-op, entao a
aula segue funcionando enquanto a migracao avanca um exercicio por vez.

USO:
    python3 scripts/consultivo/migra_blocos.py _build/consultivo/{slug}/aula{N}/preclass.html
    python3 scripts/consultivo/migra_blocos.py ... --escreve    # aplica de verdade
"""
import html as _html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import render  # noqa: E402


def des(t):
    """HTML -> texto do autor. O inverso do `esc` do render."""
    t = re.sub(r"<strong>(.*?)</strong>", r"**\1**", t, flags=re.S)
    t = re.sub(r"<em>(.*?)</em>", r"*\1*", t, flags=re.S)
    t = t.replace("&ldquo;", '"').replace("&rdquo;", '"')
    t = t.replace("&mdash;", "--").replace("&hellip;", "...")
    t = t.replace("&rsquo;", "'")
    return _html.unescape(re.sub(r"<[^>]+>", "", t)).strip()


def seccoes(html):
    """Cada `exercise-section` inteira, com o offset onde comeca e termina."""
    fora = []
    for m in re.finditer(r'<div class="exercise-section">', html):
        prof = 0
        for t in re.finditer(r"<div\b[^>]*>|</div>", html[m.start():]):
            prof += 1 if t.group(0).startswith("<div") else -1
            if prof == 0:
                fora.append((m.start(), m.start() + t.end()))
                break
    return fora


def cabecalho(s):
    """n, titulo e a ABERTURA na ordem em que ela aparece.

    Ler `task-instr` e `doc-block` como listas separadas perde a ORDEM entre eles -- e no
    molde o documento fica no meio das instrucoes. Aqui a abertura e varrida uma vez, na
    ordem do arquivo."""
    d = {}
    h = re.search(r'<div class="section-header-row"><h4>(\d+)\s*&middot;\s*(.*?)</h4></div>', s)
    if h:
        d["n"] = int(h.group(1))
        d["titulo"] = des(h.group(2))
    abertura = []
    for m in re.finditer(r'<p class="task-instr">(.*?)</p>'
                         r'|<div class="callout rule-box doc-block">\s*<strong>(.*?)</strong>'
                         r'<br>\s*(.*?)\s*</div>', s, re.S):
        if m.group(1) is not None:
            abertura.append(des(m.group(1)))
        else:
            abertura.append({"titulo": des(m.group(2)), "texto": m.group(3).strip()})
    if abertura:
        d["abertura"] = abertura
    return d


def nota(s, ident):
    m = re.search(r'<div class="callout" id="' + re.escape(ident) +
                  r'-key" style="display:none">\s*<div class="callout-title">(.*?)</div>\s*'
                  r'(.*?)\s*</div>', s, re.S)
    if not m:
        return None
    return {"titulo": des(m.group(1)), "texto": m.group(2).strip()}


def le_classificar(s):
    g = re.search(r'<div class="match-grid" id="([^"]+)">', s)
    if not g:
        return None
    ident = g.group(1)
    linhas = re.findall(r'<div class="match-row"><span class="match-word">(.*?)</span>'
                        r'<select data-ok="([A-J])">(.*?)</select></div>', s, re.S)
    if not linhas:
        return None
    ops = [des(o) for o in re.findall(r'<option value="[A-J]">(.*?)</option>', linhas[0][2])]
    itens = [{"t": des(t), "ok": ops[render.LETRAS.index(ok)]} for t, ok, _ in linhas]
    return {"kind": "classificar", "id": ident, "opcoes": ops, "itens": itens}


def le_escolha(s):
    g = re.search(r'<div class="quiz-options" id="([^"]+)">', s)
    if not g:
        return None
    itens = [{"t": des(t), **({"ok": True} if ok == "1" else {})}
             for ok, t in re.findall(r'<div class="quiz-option" data-ok="([01])" '
                                     r'onclick="tog\(this\)"><span>(.*?)</span></div>', s, re.S)]
    if not itens:
        return None
    d = {"kind": "escolha", "id": g.group(1), "itens": itens}
    r = re.search(r'<div class="rationale">(.*?)</div>', s, re.S)
    if r:
        d["rationale"] = des(r.group(1))
    return d


def le_par(s):
    g = re.search(r'<div class="pair-grid" id="([^"]+)">', s)
    if not g:
        return None
    itens = []
    for bloco in re.findall(r'<div class="pair-row" data-ok="([ab])">(.*?)</div>\s*(?=<div|$)',
                            s, re.S):
        ok, corpo = bloco
        palavra = re.search(r'<span class="pair-word">(.*?)</span>', corpo, re.S)
        alts = [des(a) for a in re.findall(r'<button class="pair-opt"[^>]*>(.*?)</button>',
                                           corpo, re.S)]
        if not (palavra and len(alts) == 2):
            return None
        itens.append({"t": des(palavra.group(1)), "alts": alts, "ok": alts["ab".index(ok)]})
    return {"kind": "par", "id": g.group(1), "itens": itens} if itens else None


def le_lacuna(s):
    if "blank-input" not in s:
        return None
    out = re.search(r'<div class="score-out" id="([^"]+)-out">', s)
    itens = []
    for linha in re.findall(r'<p class="chunk-line">(.*?)</p>', s, re.S):
        marcado = re.sub(r'<input class="blank-input" data-ok="([^"]*)"[^>]*>',
                         lambda m: "\x00" + m.group(1) + "\x01", linha)
        itens.append(des(marcado).replace("\x00", "{").replace("\x01", "}"))
    sub = re.search(r'<p class="subprompt">(.*?)\s*((?:<em>.*?</em>\s*(?:&middot;)?\s*)+)</p>',
                    s, re.S)
    d = {"kind": "lacuna", "id": out.group(1) if out else "cz", "itens": itens}
    if sub:
        d["rotulo_banco"] = des(sub.group(1))
        d["banco"] = [des(x) for x in re.findall(r"<em>(.*?)</em>", sub.group(2), re.S)]
    return d


LEITORES = [le_classificar, le_escolha, le_par, le_lacuna]


def converte(s):
    """A declaracao de uma seccao, ou None se a forma nao for reconhecida."""
    for leitor in LEITORES:
        d = leitor(s)
        if d:
            d.update({k: v for k, v in cabecalho(s).items()})
            n = nota(s, d["id"])
            if n:
                d["nota"] = n
            return d
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    escreve = "--escreve" in sys.argv
    if not args:
        raise SystemExit(__doc__.strip().splitlines()[-2].strip())
    caminho = args[0]
    pasta = os.path.dirname(caminho)
    html = open(caminho, encoding="utf-8").read()

    decl_path = os.path.join(pasta, "blocos.json")
    decl = json.load(open(decl_path, encoding="utf-8")) if os.path.exists(decl_path) else {}

    convertidas, pendentes, novo = [], [], html
    for ini, fim in reversed(seccoes(html)):
        original = html[ini:fim]
        d = converte(original)
        rot = (re.search(r"<h4>(.*?)</h4>", original) or [None, "?"])[1]
        if not d:
            pendentes.append((rot, "forma nao reconhecida"))
            continue
        # A PROVA: renderiza de volta e compara. Diferiu, nao converte.
        volta = render.seccao(d, d.get("n", 1))
        if volta.strip() != original.strip():
            pendentes.append((rot, "o render nao devolve os mesmos bytes"))
            continue
        chave = f"sec{d.get('n', len(decl) + 1)}"
        decl[chave] = [d]
        convertidas.append((chave, rot))
        novo = novo[:ini] + f"<!--BLOCOS:{chave}-->" + novo[fim:]

    print(f"=== {os.path.relpath(caminho)}")
    for chave, rot in reversed(convertidas):
        print(f"  convertida   {chave:8} {des(rot)[:56]}")
    for rot, motivo in pendentes:
        print(f"  PENDENTE              {des(rot)[:44]:46} {motivo}")
    print(f"\n  {len(convertidas)} convertida(s), {len(pendentes)} pendente(s)")

    if escreve and convertidas:
        open(caminho, "w", encoding="utf-8").write(novo)
        with open(decl_path, "w", encoding="utf-8") as f:
            json.dump(decl, f, ensure_ascii=False, indent=1)
        print(f"  escrito: {os.path.relpath(decl_path)}")
    elif convertidas:
        print("  (--escreve para aplicar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
