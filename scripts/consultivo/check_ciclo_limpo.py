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
import json
import html
import io
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


# As abas onde citar OUTRA aula e o trabalho, nao o defeito.
#
# O `tab-planning` guarda o HISTORICO PEDAGOGICO -- "Aula 2 dominado, sustentou explicacoes
# complexas" -- e o INT-010 EXIGE que ele diga a origem de cada item. O `tab-syllabus`
# guarda o mapa das vinte aulas do ciclo ("o mapa inteiro esta aqui; so o bloco vigente e
# produzido", 02 §1).
#
# Medido no artefato do Marcos, que a auditora usou: com estas duas abas dentro, a regra
# acusou SEIS citacoes legitimas do historico. O INT-002 fala em referencia "sem
# identificacao explicita" -- e uma tabela de historico e identificacao explicita.
#
# O defeito real que originou este gate vivia no `tab-feedback`, que e do ALUNO -- e ali a
# regra e OUTRA, mais apertada: a aba do aluno mostra as aulas que ele TEM, nao o mapa do
# ciclo. `Lesson 19` num material de ciclo 1 estava DENTRO do ciclo (1-20) e mesmo assim era
# defeito, porque as aulas construidas eram 1 a 4.
#
#     mapa e historico  -> abas do professor -> pode citar o ciclo inteiro
#     o que o aluno tem -> abas do aluno     -> so as aulas construidas
#
# Foi testando contra os artefatos da auditora que as duas regras se separaram. Com uma
# regra so, ou ela perdia o defeito real (comparando com o ciclo) ou acusava seis citacoes
# legitimas do historico (comparando com as construidas).
ABAS_DE_TRABALHO = ("tab-planning", "tab-syllabus")
# E os CARTOES da aba In-class, que sao o painel do professor sobre o bloco: eles mostram as
# quatro aulas do bloco, com as ainda nao produzidas marcadas como tal. Medido no artefato do
# Marcos: "Aula 21 · Bloco 1 · Grammar / G1 · Ainda nao produzida" -- o professor vendo o
# plano, que e o que o ANA-006 exige (produzir um bloco por vez). O DECK, que e o que a aula
# ve, continua dentro da regra.
# `block-card` entra junto: e o painel do BLOCO (as quatro aulas, com as ainda nao
# produzidas marcadas como tal). Existe nos dois -- 6 ocorrencias no shell e 6 no molde --
# e e onde o artefato do Marcos escreve "Aula 21 · Ainda nao produzida".
CARTOES = r'<div[^>]*class="[^"]*\b(?:lesson-card|block-card)\b[^"]*"[^>]*>' 


def sem_abas_de_trabalho(c):
    """Remove as regioes onde a referencia a outra aula e legitima."""
    while True:
        m = re.search(CARTOES, c)
        if not m:
            break
        prof = 0
        for t in re.finditer(r"<div\b[^>]*>|</div>", c[m.start():]):
            prof += 1 if t.group(0).startswith("<div") else -1
            if prof == 0:
                c = c[:m.start()] + " " + c[m.start() + t.end():]
                break
        else:
            break
    for ident in ABAS_DE_TRABALHO:
        m = re.search(r'<div[^>]*id="' + ident + r'"[^>]*>', c)
        if not m:
            continue
        prof = 0
        for t in re.finditer(r"<div\b[^>]*>|</div>", c[m.start():]):
            prof += 1 if t.group(0).startswith("<div") else -1
            if prof == 0:
                c = c[:m.start()] + " " + c[m.start() + t.end():]
                break
    return c


def na_tela(c):
    """O texto que chega ao olho: sem comentario, sem script, sem style, sem data-teacher.

    A ordem importa. Tirar as tags ANTES dos comentarios deixaria o conteudo do comentario
    solto no meio do texto, e ele voltaria a contar."""
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    c = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", c, flags=re.S | re.I)
    c = re.sub(r'\sdata-teacher="[^"]*"', " ", c)
    c = sem_abas_de_trabalho(c)
    return " ".join(re.sub(r"<[^>]+>", " ", c).split())


def construidas(c):
    """Os numeros de aula que este material de fato CONSTRUIU."""
    return sorted({int(n) for n in re.findall(r"\b(\d+)\s*:\s*\{\s*n\s*:\s*\1\b", c)})


def faixa_do_ciclo(c):
    """A faixa do CICLO declarado. Mantida porque descreve o contrato, e usada pelo GATE 41.

    NAO e o criterio desta regra -- ver o comentario de ABAS_DE_TRABALHO. A faixa LEGITIMA

    NAO e a lista das aulas construidas -- e o CICLO inteiro. O syllabus existe justamente
    para mostrar o mapa das vinte aulas ("o mapa inteiro esta aqui; so o bloco vigente e
    produzido", 02 §1), entao um material do bloco 1 citar a aula 12 na aba de planejamento
    e o comportamento CERTO.

    A primeira versao desta regra comparava com as construidas, e so nao acusou o molde por
    sorte: o syllabus dele escreve "aulas 5-20" (intervalo, minusculo) em vez de "Aula 5".
    Testando contra o artefato do Marcos -- ciclo 2, primeira aula 19 -- ela acusou NOVE
    citacoes legitimas de uma vez. Material da auditora, defeito do gate.

    Sem `var CICLO` nao ha faixa declarada, e o fallback e o bloco construido. A ausencia em
    si e outro defeito, e quem cobra e o GATE 41 (ANA-003)."""
    m = re.search(r"var CICLO=\{([^}]*)\}", c)
    if m:
        pri = re.search(r"primeira:(\d+)", m.group(1))
        tot = re.search(r"aulas:(\d+)", m.group(1))
        if pri and tot:
            p0 = int(pri.group(1))
            return list(range(p0, p0 + int(tot.group(1))))
    return construidas(c)


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []

    erros = []
    aulas = construidas(c)
    feitas = aulas
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
            f'CONTAMINACAO DE CICLO (INT-002): uma tela do ALUNO fala em "Lesson {n}", e '
            f'este material tem as aulas {feitas}. Contexto: "...{fora[n]}..."')

    # ---- CONTAMINACAO DE ALUNO: o material de um aluno citando OUTRO
    #
    # Em 01/09/2026, o cartao da aula 12 da Joice dizia "e a hipotese H3 do bloco do Caio".
    # A frase estava bem formada, o cartao valido, e nenhum gate via: o INT-002 acima mede
    # NUMERO de aula fora do ciclo, e o nome de outra pessoa nao e um numero.
    #
    # O material de um aluno nao tem por que nomear outro. Personagem inventado nao entra na
    # lista — ela vem dos configs, e sao os nomes dos ALUNOS REAIS da anatomia.
    erros += _contaminacao_de_aluno(caminho, c)
    return True, erros


def _alunos_da_anatomia():
    """Primeiro nome de cada aluno com material nesta anatomia, tirado dos configs.

    O primeiro nome basta e e o que aparece em prosa ("do Caio"). Sobrenome raramente
    aparece solto, e usar o nome inteiro deixaria passar exatamente o caso que originou
    esta regra."""
    saida = {}
    for cfg in sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*",
                                             "config.json"))):
        try:
            with open(cfg, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        slug = d.get("slug")
        nome = (d.get("aluno") or {}).get("nome", "").strip()
        if slug and nome:
            saida[slug] = nome
    return saida


def _contaminacao_de_aluno(caminho, c):
    """O nome de proprio de OUTRO aluno da anatomia, na superficie deste material."""
    alunos = _alunos_da_anatomia()
    arq = os.path.basename(caminho)
    meu = next((slug for slug in alunos if arq.startswith(slug)), None)
    tela = na_tela(c) + " " + " ".join(
        html.unescape(m) for m in re.findall(r'data-teacher="([^"]*)"', c))
    fora = []
    for slug, nome in alunos.items():
        if slug == meu:
            continue
        for m in re.finditer(r"\b" + re.escape(nome) + r"\b", tela):
            ctx = re.sub(r"\s+", " ", tela[max(0, m.start() - 70):m.end() + 50])
            fora.append(
                f'CONTAMINACAO DE ALUNO: este material nomeia "{nome}", que e outro aluno '
                f'desta anatomia ({slug}). Contexto: "...{ctx}...". Se e personagem, '
                f'escolha outro nome; se e observacao interna, ela nao vai para a tela.')
            break
    return fora


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


def _confere_texto(t, como="stephanie-vicente"):
    """O arquivo temporario nao carrega o nome do aluno, e e o nome que diz de quem e o
    material. Sem isto, o proprio molde reprova na regra de contaminacao de aluno: ele
    nomeia a Stephanie porque ele E o material dela."""
    d = tempfile.mkdtemp()
    p = os.path.join(d, f"{como}.html")
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(t)
    try:
        return confere(p)
    finally:
        os.unlink(p)
        os.rmdir(os.path.dirname(p))


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
        # o defeito real de 01/09: um cartao da Joice citava "o bloco do Caio"
        ("nome de OUTRO aluno na tela",
         lambda s: s.replace("<h2 class=\"sec\">Feedback</h2>",
                             "<h2 class=\"sec\">Feedback</h2><p>e a mesma leitura do bloco do Caio</p>", 1),
         "CONTAMINACAO DE ALUNO"),
        ("nome de outro aluno no data-teacher — tambem reprova, e o professor le",
         lambda s: s.replace("</body>",
                             '<div data-teacher="compare com o material do Caio"></div>\n</body>', 1),
         "CONTAMINACAO DE ALUNO"),
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
