#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Converte os .docx normativos do Private Black para Markdown, sem dependencia externa.

POR QUE ISTO EXISTE
-------------------
Os documentos normativos da escola nascem em .docx, no Drive. Enquanto ficam la, eles nao
sao citaveis nem verificaveis: regra fora do repo nao entra em gate, nao entra em revisao e
nao entra em PR. Foi exatamente por isso que tres dos cinco normativos de agosto nunca
viraram nada -- viviam em ~/Downloads.

Trazer o texto na mao criaria a SEGUNDA COPIA, que diverge na primeira edicao do original.
Este conversor existe para que reimportar seja barato: documento atualizado no Drive volta
por aqui, e o diff mostra exatamente o que a escola mudou.

O QUE ELE PRESERVA
------------------
  - a hierarquia de titulos (w:pStyle Heading N -> #, ##, ###)
  - as tabelas, em Markdown (sao a forma em que metade das regras esta escrita)
  - listas (numeradas e nao numeradas)
  - negrito e italico dentro do paragrafo
  - a ordem do documento

O QUE ELE NAO FAZ: imagens, cor, caixa de texto, comentario de revisao. Nenhum dos
documentos normativos depende deles -- se um dia depender, o conversor cresce; a regra
nunca deve depender de algo que o conversor perde em silencio.

USO:
    python3 scripts/black/docx_to_md.py ENTRADA.docx SAIDA.md --titulo "00 - Guia de Uso"
    python3 scripts/black/docx_to_md.py --selftest
"""
import argparse
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _texto_run(r):
    """Texto de um run, com negrito/italico. Preserva quebra explicita (w:br) e tab."""
    partes = []
    for n in r.iter():
        tag = n.tag
        if tag == W + "t":
            partes.append(n.text or "")
        elif tag == W + "br":
            partes.append("\n")
        elif tag == W + "tab":
            partes.append(" ")
    txt = "".join(partes)
    if not txt.strip():
        return txt
    rpr = r.find(W + "rPr")
    if rpr is not None:
        # w:b sem w:val, ou com val diferente de 0/false, e negrito ligado
        def _ligado(nome):
            el = rpr.find(W + nome)
            if el is None:
                return False
            v = el.get(W + "val")
            return v not in ("0", "false", "none")
        pre = post = ""
        if _ligado("b"):
            pre, post = "**", "**"
        if _ligado("i"):
            pre, post = pre + "*", "*" + post
        if pre:
            # o marcador nao pode envolver o espaco das bordas, senao o Markdown quebra
            esq = len(txt) - len(txt.lstrip())
            dir_ = len(txt) - len(txt.rstrip())
            miolo = txt[esq:len(txt) - dir_] if dir_ else txt[esq:]
            txt = txt[:esq] + pre + miolo + post + (txt[len(txt) - dir_:] if dir_ else "")
    return txt


def _texto_par(p):
    return "".join(_texto_run(r) for r in p.findall(W + "r"))


def _nivel_titulo(p):
    ppr = p.find(W + "pPr")
    if ppr is None:
        return 0
    st = ppr.find(W + "pStyle")
    if st is None:
        return 0
    val = (st.get(W + "val") or "").lower()
    m = re.match(r"heading(\d)", val)
    if m:
        return int(m.group(1))
    if val in ("title",):
        return 1
    return 0


def _e_lista(p):
    ppr = p.find(W + "pPr")
    return ppr is not None and ppr.find(W + "numPr") is not None


def _tabela_md(tbl):
    linhas = []
    for tr in tbl.findall(W + "tr"):
        celulas = []
        for tc in tr.findall(W + "tc"):
            txt = " ".join(_texto_par(p) for p in tc.findall(W + "p"))
            txt = re.sub(r"\s+", " ", txt).strip().replace("|", "\\|")
            celulas.append(txt)
        if celulas:
            linhas.append(celulas)
    if not linhas:
        return ""
    n = max(len(l) for l in linhas)
    linhas = [l + [""] * (n - len(l)) for l in linhas]
    out = ["| " + " | ".join(linhas[0]) + " |",
           "|" + "|".join(["---"] * n) + "|"]
    for l in linhas[1:]:
        out.append("| " + " | ".join(l) + " |")
    return "\n".join(out)


def converte(caminho_docx):
    with zipfile.ZipFile(caminho_docx) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    body = root.find(W + "body")
    if body is None:
        raise SystemExit("docx sem body: " + caminho_docx)
    blocos = []
    for el in body:
        if el.tag == W + "p":
            txt = _texto_par(el).strip()
            if not txt:
                continue
            niv = _nivel_titulo(el)
            if niv:
                blocos.append("#" * min(niv + 1, 6) + " " + txt)
            elif _e_lista(el):
                blocos.append("- " + txt)
            else:
                blocos.append(txt)
        elif el.tag == W + "tbl":
            t = _tabela_md(el)
            if t:
                blocos.append(t)
    # listas coladas viram um bloco so
    saida, buf = [], []
    for b in blocos:
        if b.startswith("- "):
            buf.append(b)
            continue
        if buf:
            saida.append("\n".join(buf))
            buf = []
        saida.append(b)
    if buf:
        saida.append("\n".join(buf))
    return "\n\n".join(saida).rstrip() + "\n"


def cabecalho(titulo, origem, drive_id, modificado):
    return (
        f"> **Documento normativo importado do Drive — nao editar aqui.**\n"
        f"> Origem: `{origem}`\n"
        f"> Drive ID: `{drive_id}`\n"
        f"> Modificado no Drive: {modificado}\n"
        f"> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> "
        f"docs/private-black/{titulo}.md`\n"
        f"> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve "
        f"reimportando, nunca editando o .md.\n\n"
    )


def _selftest():
    """Prova que o conversor MORDE: um docx montado a mao com titulo, tabela e negrito."""
    import io
    doc = (
        '<?xml version="1.0"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Titulo</w:t></w:r></w:p>'
        "<w:p><w:r><w:t>texto </w:t></w:r>"
        "<w:r><w:rPr><w:b/></w:rPr><w:t>forte</w:t></w:r></w:p>"
        '<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/></w:numPr></w:pPr>'
        "<w:r><w:t>item</w:t></w:r></w:p>"
        "<w:tbl><w:tr><w:tc><w:p><w:r><w:t>A</w:t></w:r></w:p></w:tc>"
        "<w:tc><w:p><w:r><w:t>B</w:t></w:r></w:p></w:tc></w:tr>"
        "<w:tr><w:tc><w:p><w:r><w:t>1</w:t></w:r></w:p></w:tc>"
        "<w:tc><w:p><w:r><w:t>2</w:t></w:r></w:p></w:tc></w:tr></w:tbl>"
        "</w:body></w:document>"
    )
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml", doc)
    buf.seek(0)
    tmp = "/tmp/_docx_selftest.docx"
    with open(tmp, "wb") as fh:
        fh.write(buf.read())
    md = converte(tmp)
    os.remove(tmp)
    falhas = []
    if "## Titulo" not in md:
        falhas.append("titulo Heading1 nao virou '## '")
    if "texto **forte**" not in md:
        falhas.append("negrito perdido")
    if "- item" not in md:
        falhas.append("lista perdida")
    if "| A | B |" not in md or "| 1 | 2 |" not in md:
        falhas.append("tabela perdida")
    if falhas:
        for f in falhas:
            print("FALHA:", f)
        print(md)
        return 1
    print("OK — selftest: titulo, negrito, lista e tabela sobrevivem a conversao.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada", nargs="?")
    ap.add_argument("saida", nargs="?")
    ap.add_argument("--drive-id", default="")
    ap.add_argument("--modificado", default="")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()
    if not a.entrada or not a.saida:
        ap.error("entrada e saida sao obrigatorias")
    md = converte(a.entrada)
    nome = os.path.splitext(os.path.basename(a.saida))[0]
    cab = cabecalho(nome, os.path.basename(a.entrada), a.drive_id, a.modificado)
    with open(a.saida, "w", encoding="utf-8") as fh:
        fh.write(cab + md)
    print(f"{a.saida}  ({len(md)} bytes de texto)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
