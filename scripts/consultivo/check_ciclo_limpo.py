#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 39 — o material fala SO das aulas do ciclo dele (INT-002 do catalogo do auditor).

O DEFEITO QUE ELE EXISTE PARA IMPEDIR
--------------------------------------
Ate 25/08/2026 o molde publicado trazia, na aba **Feedback**, os botoes `Lesson 19` e
`Lesson 20` e os titulos do artefato do Marcos ("Reading the room", "From evidence to a
briefing") -- num ciclo cujas aulas sao 1 a 4. Nos DOIS arquivos. E a aba e
`data-view="aluno"`: quem via as duas aulas inexistentes era o ALUNO.

    INT-002 · Contaminacao de ciclo · BLOCKER
    "Aparecem numeros de aula, bloco, checkpoint ou decisoes de outro ciclo sem
     identificacao explicita."

POR QUE NENHUM GATE VIU
------------------------
Porque todos olhavam para o que o builder EMITE. Este defeito e do que ele NAO emitia: o
builder refazia `tab-preclass` e `tab-postclass` e passava direto pela `tab-feedback`, que
tem a MESMA forma. A regiao ficou intacta, valida, bonita -- e de outro aluno.

E a licao que fica: **regiao nao tocada nao e regiao conferida.** Um gate que so verifica o
que foi escrito nunca encontra o que ficou. Por isso este aqui nao pergunta "o builder
emitiu certo?", e sim "o arquivo PUBLICADO fala de alguma aula que nao existe neste ciclo?"
-- pergunta que independe de quem escreveu a regiao.

O QUE ELE MEDE
--------------
O intervalo do ciclo sai do proprio arquivo (`var LESSONS`), nunca de numero digitado aqui.
Depois procura, no texto que chega a TELA, referencia a `Lesson N` / `Aula N` fora desse
intervalo.

O que NAO conta como contaminacao, e por que:

  - **comentario de HTML, CSS e JS.** O comentario explica o codigo e nao chega ao olho de
    ninguem. Reprova-lo ensina a apagar o comentario em vez do defeito -- e foi assim que,
    na auditoria de 25/08, "hipotese" e "auditoria" quase viraram dois defeitos inventados:
    as duas palavras estavam em comentario de CSS.
  - **`data-teacher`.** E a nota de conducao, do professor, e ela PODE citar a aula 12 de
    proposito ("retomar o que ficou da aula 12"). O catalogo pede referencia *qualificada*,
    nao ausencia de referencia.
  - **o total do ciclo.** "Lessons in this cycle: 20" nao e referencia a uma aula.

ESCOPO: o carimbo `alumni-anatomia=consultivo`. O artefato-prototipo nao e carimbado e
continua livre para ser o que e -- as aulas 19 e 20 do Marcos.

USO:
    python3 scripts/consultivo/check_ciclo_limpo.py [arquivo.html ...]
    python3 scripts/consultivo/check_ciclo_limpo.py --selftest
"""
import glob
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def na_tela(c):
    """O texto que chega ao olho: sem comentario, sem script, sem style, sem data-teacher.

    A ordem importa. Tirar as tags ANTES dos comentarios deixaria o conteudo do comentario
    solto no meio do texto, e ele voltaria a contar."""
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    c = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", c, flags=re.S | re.I)
    c = re.sub(r'\sdata-teacher="[^"]*"', " ", c)
    return " ".join(re.sub(r"<[^>]+>", " ", c).split())


def ciclo_do_arquivo(c):
    """Os numeros de aula que este material de fato tem, lidos do proprio arquivo."""
    return sorted({int(n) for n in re.findall(r"\b(\d+)\s*:\s*\{\s*n\s*:\s*\1\b", c)})


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []

    erros = []
    aulas = ciclo_do_arquivo(c)
    if not aulas:
        return True, ["SEM var LESSONS: nao da para saber de que aulas este material e."]

    tela = na_tela(c)
    fora = {}
    for m in re.finditer(r"\b(?:Lesson|Aula)\s+0*(\d{1,2})\b", tela):
        n = int(m.group(1))
        if n not in aulas:
            fora.setdefault(n, tela[max(0, m.start() - 70):m.start() + 50])

    for n in sorted(fora):
        erros.append(
            f'CONTAMINACAO DE CICLO (INT-002): a tela fala em "Lesson {n}", e este material '
            f'tem as aulas {aulas}. Contexto: "...{fora[n]}..."')
    return True, erros


def alvos_padrao():
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                    glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(p)
        except OSError:
            pass
    return fora


def _confere_texto(t):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(t)
        p = f.name
    try:
        return confere(p)
    finally:
        os.unlink(p)


def _selftest():
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo = open(base, encoding="utf-8").read()
    ok, erros = _confere_texto(limpo)
    if erros:
        print("SELFTEST INCONCLUSIVO — o molde JA esta reprovando:")
        for e in erros:
            print("   ", e)
        return 1

    casos = [
        ("aula de outro ciclo na tela",
         lambda s: s.replace("<h2 class=\"sec\">Feedback</h2>",
                             "<h2 class=\"sec\">Feedback</h2><p>Lesson 19 — Reading the room</p>", 1),
         "Lesson 19"),
        ("o defeito real de 25/08 (botao da aba Feedback)",
         lambda s: s.replace('onclick="fbSel(1)"', 'onclick="fbSel(19)"', 1)
                    .replace("Lesson 01", "Lesson 19", 1),
         "Lesson 19"),
        ("mesma citacao, mas em COMENTARIO — nao pode reprovar",
         lambda s: s.replace("</body>", "<!-- Lesson 19 era a do artefato -->\n</body>", 1),
         None),
        ("mesma citacao no data-teacher — nao pode reprovar",
         lambda s: s.replace("</body>",
                             '<div data-teacher="retomar o que ficou da Lesson 19"></div>\n</body>', 1),
         None),
    ]
    falhou = False
    for nome, muta, esperado in casos:
        _, errs = _confere_texto(muta(limpo))
        if esperado is None:
            bom = not errs
            motivo = "ignorado, como deve" if bom else f"REPROVOU indevidamente: {errs[0][:50]}"
        else:
            bom = any(esperado in e for e in errs)
            motivo = (errs[0][:66] if errs else "nao acusou nada")
        print(f"  {'OK  ' if bom else 'FALHA'}  {nome:46} {motivo}")
        if not bom:
            falhou = True
    print()
    if falhou:
        print("SELFTEST FALHOU — a regra parou de morder, ou passou a morder demais.")
        return 1
    print(f"SELFTEST OK — {len(casos)} casos: 2 defeitos pegos, 2 citacoes legitimas poupadas.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    print(f"=== GATE 39 — contaminacao de ciclo (anatomia {ANATOMIA}) ===")
    total = vistos = 0
    for a in alvos:
        if not os.path.exists(a):
            continue
        aplicou, erros = confere(a)
        if not aplicou:
            continue
        vistos += 1
        rel = os.path.relpath(a, RAIZ)
        if erros:
            total += len(erros)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in erros:
                print(f"        {e}")
        else:
            print(f"{VERDE}ok{ZERA}    {rel}")
    print()
    if total:
        print(f"{VERMELHO}GATE 39 — {total} contaminacao(oes) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 39 OK — {vistos} arquivo(s) falam so das aulas do proprio ciclo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
