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
    t = t.replace("&rsquo;", "'").replace("&middot;", "\u00b7").replace("&ndash;", "\u2013")
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
    h = re.search(r'<div class="section-header-row"><h4>(?:(\d+)\s*&middot;\s*)?(.*?)</h4>', s)
    if h:
        if h.group(1):
            d["n"] = int(h.group(1))
        d["titulo"] = des(h.group(2))
    bd = re.search(r'<span class="badge badge-open">(.*?)</span>', s)
    if bd:
        d["badge"] = des(bd.group(1))
    abertura = []
    # O `task-instr` de DENTRO do quiz-item e o prompt do item, nao instrucao da seccao --
    # quem o emite e o `escolha`. Varrer sem tirar isto o poria na abertura, e a pergunta
    # apareceria ANTES do audio que ela cobra.
    s = re.sub(r'(<div class="quiz-item">)\s*<p class="task-instr">.*?</p>', r"\1", s,
               flags=re.S)
    # Uma varredura so, na ORDEM do arquivo, com o tipo explicito em cada item. Ler cada
    # peca como lista separada perderia a ordem entre elas -- e no molde a tabela vem antes
    # do callout, e o documento fica no meio das instrucoes.
    padrao = (r'<p class="task-instr">(.*?)</p>'
              r'|<div class="callout rule-box doc-block">\s*(?:<strong>(.*?)</strong><br>\s*)?'
              r'(.*?)\s*</div>'
              r'|<div class="callout rule-box">\s*<span class="callout-title">(.*?)</span>\s*'
              r'(.*?)\s*</div>'
              r'|<div class="tbl-wrap">\s*<table class="data" style="min-width:([^"]+)">\s*'
              r'(?:<thead>(.*?)</thead>\s*)?<tbody>\s*(.*?)\s*</tbody>'
              r'|<ul style="([^"]*)">\s*(.*?)\s*</ul>'
              r'|<div class="rec-bar">\s*<button class="audio-btn-sm" id="([^"]+)-start" '
              r'onclick="rcStart\(\'[^\']+\'\)">&#9679; (.*?)</button>'
              r'|<label class="mail-label" for="([^"]+)-subject">(.*?)</label>\s*'
              r'<input class="mail-subject"[^>]*oninput="save\(\'([^\']+)_subject\'[^>]*>\s*'
              r'<label class="mail-label"[^>]*>(.*?)</label>\s*'
              r'<textarea class="writebox"[^>]*style="min-height:([^"]+)"'
              r'|<div style="display:flex;gap:var\(--space-2h\);flex-wrap:wrap;'
              r'align-items:center;margin:var\(--space-3h\) 0" data-audgrupo="([^"]*)">(.*?)</div>'
              r'|<div class="res-card">\s*<h5>(.*?)</h5>\s*<span class="res-src">(.*?)</span>'
              r'\s*<p>(.*?)</p>\s*<a class="res-link" href="([^"]+)"[^>]*>(.*?)\s*&rarr;</a>')
    for m in re.finditer(padrao, s, re.S):
        if m.group(1) is not None:
            abertura.append(des(m.group(1)))
        elif m.group(3) is not None:
            d0 = {"texto": m.group(3).strip()}
            if m.group(2) is not None:
                d0["titulo"] = des(m.group(2))
            abertura.append({"doc": d0})
        elif m.group(4) is not None:
            abertura.append({"callout": {"titulo": des(m.group(4)),
                                         "texto": m.group(5).strip()}})
        elif m.group(9) is not None:
            abertura.append({"lista": [x.strip() for x in
                                       re.findall(r"<li>(.*?)</li>", m.group(10), re.S)],
                             "estilo": m.group(9)})
        elif m.group(11) is not None:
            abertura.append({"gravador": m.group(11),
                             "rotulo_gravar": des(m.group(12))})
        elif m.group(13) is not None:
            abertura.append({"escrita": {"id": m.group(13), "chave": m.group(15),
                                         "rotulo_assunto": des(m.group(14)),
                                         "rotulo_corpo": des(m.group(16)),
                                         "altura": m.group(17)}})
        elif m.group(18) is not None:
            # A barra de audio tem DUAS formas na mesma aula: a simples (um Play) e a de
            # velocidade (Normal/Slower, e o Play passa a chamar `audMain`). Por isso o
            # padrao captura o CORPO da barra e a leitura acontece aqui -- tentar cobrir as
            # duas na alternacao dava dois ramos quase iguais, e o segundo nunca casava.
            corpo = m.group(19)
            ops = re.findall(r'class="audio-btn-sm ghost aud-op" onclick="sayAs\(\'(.*?)\','
                             r'([\d.]+),\'([fm])\'\)"[^>]*>(.*?)</button>', corpo, re.S)
            if ops:
                au = {"grupo": m.group(18), "texto": ops[0][0], "voz": ops[0][2],
                      "velocidades": [[des(r), v] for t, v, _, r in ops]}
            else:
                u = re.search(r'class="audio-btn-sm" onclick="sayAs\(\'(.*?)\','
                              r'([\d.]+),\'([fm])\'\)"', corpo, re.S)
                if not u:
                    return {}
                au = {"grupo": m.group(18), "texto": u.group(1),
                      "rate": u.group(2), "voz": u.group(3)}
            abertura.append({"audio": au})
        elif m.group(20) is not None:
            abertura.append({"recurso": {"titulo": des(m.group(20)),
                                         "fonte": des(m.group(21)),
                                         "texto": m.group(22).strip(),
                                         "url": m.group(23), "cta": des(m.group(24))}})
        else:
            linhas, larg, cab = [], None, None
            if m.group(7):
                ths = re.findall(r"<th([^>]*)>(.*?)</th>", m.group(7), re.S)
                cab = [des(t) for _, t in ths]
                w = re.search(r'width:([^";]+)', ths[0][0]) if ths else None
                larg = w.group(1) if w else None
            for tr in re.findall(r"<tr>(.*?)</tr>", m.group(8), re.S):
                tds = re.findall(r"<td([^>]*)>(.*?)</td>", tr, re.S)
                if len(tds) < 2:
                    return {}
                if not linhas and not cab:
                    w = re.search(r'width:([^";]+)', tds[0][0])
                    larg = w.group(1) if w else None
                rot = re.sub(r"</?strong>", "", tds[0][1]).strip()
                linhas.append([des(rot)] + [c[1].strip() for c in tds[1:]])
            t = {"tabela": linhas, "min_width": m.group(6)}
            if cab:
                t["cabecalho"] = cab
            if larg:
                t["largura_rotulo"] = larg
            abertura.append(t)
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
    pr = re.search(r'<div class="quiz-item">\s*<p class="task-instr">(.*?)</p>', s, re.S)
    if pr:
        d["prompt"] = des(pr.group(1))
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
        def _campo(m):
            w = re.search(r"min-width:([^\";]+)", m.group(0))
            larg = w.group(1) if w else "170px"
            return "\x00" + m.group(1) + ("" if larg == "170px" else "|" + larg) + "\x01"
        marcado = re.sub(r'<input class="blank-input" data-ok="([^"]*)"[^>]*>', _campo, linha)
        itens.append(des(marcado).replace("\x00", "{").replace("\x01", "}"))
    sub = re.search(r'<p class="subprompt">(.*?)\s*((?:<em>.*?</em>\s*(?:&middot;)?\s*)+)</p>',
                    s, re.S)
    d = {"kind": "lacuna", "id": out.group(1) if out else "cz", "itens": itens}
    if sub:
        d["rotulo_banco"] = des(sub.group(1))
        d["banco"] = [des(x) for x in re.findall(r"<em>(.*?)</em>", sub.group(2), re.S)]
    return d


def le_recursos(s):
    cards = re.findall(r'<div class="res-card">\s*<h5>(.*?)</h5>\s*'
                       r'<span class="res-src">(.*?)</span>\s*<p>(.*?)</p>\s*'
                       r'<a class="res-link" href="([^"]+)"[^>]*>(.*?)\s*&rarr;</a>\s*</div>',
                       s, re.S)
    if not cards:
        return None
    # o card e a UNICA coisa da seccao? senao a forma e outra
    resto = re.sub(r'<div class="res-card">.*?</div>', "", s, flags=re.S)
    if re.search(r'<(table|input|textarea|button|ul)\b', resto):
        return None
    itens = [{"titulo": des(t), "fonte": des(f), "texto": x.strip(),
              "url": u, "cta": des(c)} for t, f, x, u, c in cards]
    return {"kind": "recursos", "id": "res", "itens": itens}


LEITORES = [le_classificar, le_escolha, le_par, le_lacuna, le_recursos]


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
    # SECCAO SO DE CONTEUDO. O "Lesson recap" do post-class nao tem exercicio -- e tabela
    # mais sintese --, e o acervo nao vira exercicio de proposito (ANA-013). Sem este caso o
    # conversor a chamava de "forma nao reconhecida" e a deixava em HTML para sempre.
    cab = cabecalho(s)
    # Campo de resposta descarta o caso "so conteudo". BOTAO, nao: o gravador tem tres
    # (gravar, parar, apagar) e ja e uma peca reconhecida da sequencia. O que importa e
    # sobrar botao que NINGUEM emite -- esse sim seria markup perdido na conversao.
    sem_pecas = re.sub(r"<button[^>]*onclick=\"(?:rc(?:Start|Stop|Apaga)|pwClear)\([^\"]*\""
                       r"[^>]*>.*?</button>", "", s, flags=re.S)
    if (cab.get("abertura")
            and not re.search(r"<(input|select)\b(?![^>]*class=\"mail-subject\")", s)
            and not re.search(r"<textarea\b(?![^>]*class=\"writebox\")", s)
            and not re.search(r"<button\b", sem_pecas)):
        return {"id": "conteudo", **cab}
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
        # A CHAVE TEM DE SER UNICA, e `sec{n}` so serve onde ha `n`.
        #
        # O post-class nao numera as seccoes, e a primeira versao caiu em
        # `sec{len(decl)+1}` -- que COLIDE com uma chave ja existente e a sobrescreve em
        # silencio. Rodando o conversor duas vezes no mesmo arquivo, ele comia o que ja
        # tinha migrado: o material encolheu 2 KB e so o `cmp` viu.
        base = f"sec{d['n']}" if d.get("n") else re.sub(
            r"[^a-z0-9]+", "", des(rot).lower())[:12] or "sec"
        chave, k = base, 2
        while chave in decl:
            chave, k = f"{base}{k}", k + 1
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
