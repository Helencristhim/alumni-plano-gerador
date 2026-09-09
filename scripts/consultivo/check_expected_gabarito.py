#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 71 — o `Expected` do guia de tela e GABARITO, nao resumo.

O DEFEITO
---------
Revisao da professora sobre a aula 19 da Gabriela, 09/09/2026, sobre esta nota:

    Expected: True: both talk about the ending, Chris finds something good, Chris finds
    the story predictable. The other three are not in the text or say the opposite.

    > "nao apresenta o 'answer key' do exercicio efetivamente, e vago.
    >  Isso e recorrente para todos 'expected' nas notas dos teacher's guides."

Tres dos seis itens saem parafraseados e os outros tres viram "the other three". Quem esta
dando a aula tem a tela do exercicio na frente e a nota ao lado, e ainda assim precisa
resolver de cabeca qual item e qual — no meio da aula, com a aluna esperando.

Medido em 09/09/2026, antes deste gate, nas seis anatomias do consultivo:

    caio-de-souza-amante   0/8    joice-lopes-leite      0/9    luiz-bressane     0/8
    gabriela-pires         3/12   lucia-nishiyama-serra  0/9    vanessa-aparecida 0/8

    3 de 54 telas de atividade fechada tinham o gabarito inteiro. As tres sao as telas 5, 6
    e 7 da aula 19 da Gabriela, reescritas nessa revisao.

A REGRA
-------
Tela que declara atividade FECHADA (`escolha`, `classificar`, `par`, `completar`, `lacuna`)
tem de nomear, no `expected` do guia daquela tela, CADA item — e, quando a resposta e texto
(`classificar`, `par`, `completar`, `lacuna`), tambem cada resposta correta.

"Nomear" e citar, nao parafrasear: as cinco primeiras palavras do item (ou o item inteiro,
se for menor) tem de aparecer no `expected`. Cinco palavras deixam passar a citacao
encurtada de quem escreve bem —

    "Two hours is a long time…" — Chris

— e nao deixam passar a parafrase, que e o defeito: o item "Both reviews talk about the
ending." nao e satisfeito por "both talk about the ending".

O PAREADO E POR ID DE BLOCO, NUNCA POR POSICAO
-----------------------------------------------
A chave da baseline e `{aluno}/aula{N}:{ids dos blocos da tela}` e nao o ordinal da tela.
Inserir uma tela no meio do deck renumera todas as seguintes — foi exatamente o que a
propria revisao da aula 19 fez, ao dividir a etapa 7 em duas telas. Com chave posicional a
baseline teria passado a perdoar a tela errada, calada.

ESCOPO: as telas do IN CLASS das anatomias do consultivo. O pre-class nao entra: os blocos
`sec1..sec6` nao vivem em tela nenhuma e nao tem guia de tela.

A BASELINE E ALVARA, NAO TODO
------------------------------
`expected_gabarito_baseline.json` congela as 51 telas que ja existiam vagas em 09/09/2026.
Elas sao de aulas publicadas — REGRA 30 — e o gate as PULA. Ele existe para que nenhuma
tela NOVA nasca assim. A baseline so pode cair: `--update` regrava, e quem consertar uma
aula por pedido do Dan a encolhe.

USO:
    python3 scripts/consultivo/check_expected_gabarito.py [dir ...]
    python3 scripts/consultivo/check_expected_gabarito.py --update
    python3 scripts/consultivo/check_expected_gabarito.py --selftest
"""
import glob
import html
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "expected_gabarito_baseline.json")
VERDE, VERMELHO, AMARELO, ZERA = "\033[32m", "\033[31m", "\033[33m", "\033[0m"

FECHADOS = ("escolha", "classificar", "par", "completar", "lacuna")
PALAVRAS = 5   # quantas palavras do item bastam para dizer que o guia CITOU o item


def norm(t):
    """O texto como o gate compara: sem marcacao, sem acento, sem tipografia."""
    t = html.unescape(str(t))
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("’", "'").replace("“", '"').replace("”", '"')
          .replace("—", "-").replace("–", "-").replace("…", "..."))
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9' ]+", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def citado(alvo, dentro):
    """O `alvo` foi CITADO em `dentro`? Cinco palavras bastam; parafrase nao passa."""
    a = norm(alvo)
    if not a:
        return True
    if a in dentro:
        return True
    p = a.split()
    return len(p) > PALAVRAS and " ".join(p[:PALAVRAS]) in dentro


def telas_do_deck(slides):
    """Ordinal da tela -> ids de bloco que ela declara. A ordem e a do `data-teacher`,
    que e a MESMA que o builder usa para casar o guia (`aplica_guia_de_tela`)."""
    inicios = [m.start() for m in
               re.finditer(r'<div class="slide[^"]*"[^>]*?\sdata-teacher="', slides)]
    fins = inicios[1:] + [len(slides)]
    return {i: re.findall(r"<!--BLOCOS:([a-zA-Z0-9_]+)-->", slides[a:b])
            for i, (a, b) in enumerate(zip(inicios, fins), 1)}


def confere(pasta, baseline=(), colher=False):
    """Devolve (falhas, chaves_medidas_com_defeito)."""
    falhas, vagas = [], []
    aluno = os.path.basename(pasta.rstrip("/"))
    for d in sorted(glob.glob(os.path.join(pasta, "aula*"))):
        gp, sp, bp = (os.path.join(d, x) for x in
                      ("guia_telas.json", "slides.html", "blocos.json"))
        if not all(os.path.exists(x) for x in (gp, sp, bp)):
            continue
        aula = os.path.basename(d)
        try:
            guia = json.load(open(gp, encoding="utf-8"))
            bl = json.load(open(bp, encoding="utf-8"))
        except Exception as e:
            falhas.append(f"{aluno}/{aula}: fragmento nao e JSON valido ({e}).")
            continue
        for i, ids in telas_do_deck(open(sp, encoding="utf-8").read()).items():
            itens, kinds = [], set()
            for bid in ids:
                for b in (bl.get(bid) or []):
                    if b.get("kind") in FECHADOS:
                        kinds.add(b["kind"])
                        itens += [it for it in (b.get("itens") or [])
                                  if isinstance(it, dict)]
            if not itens:
                continue
            chave = f"{aluno}/{aula}:{'+'.join(sorted(ids))}"
            exp = norm((guia.get(str(i)) or {}).get("expected", ""))
            faltam = [it["t"] for it in itens
                      if it.get("t") and not citado(it["t"], exp)]
            respostas = sorted({it["ok"] for it in itens
                                if isinstance(it.get("ok"), str) and it["ok"].strip()})
            sem_resp = [r for r in respostas if not citado(r, exp)]
            if not (faltam or sem_resp):
                continue
            vagas.append(chave)
            if chave in baseline or colher:
                continue
            det = []
            if faltam:
                det.append(f"{len(faltam)} de {len(itens)} item(ns) nao citado(s): "
                           + "; ".join(repr(t[:52]) for t in faltam[:3])
                           + (" ..." if len(faltam) > 3 else ""))
            if sem_resp:
                det.append("resposta(s) correta(s) fora do texto: "
                           + ", ".join(repr(r[:32]) for r in sem_resp[:4]))
            falhas.append(
                f"{aluno}/{aula} tela {i} ({'/'.join(sorted(kinds))}, blocos "
                f"{'+'.join(ids)}): o `Expected` nao e gabarito — " + " | ".join(det))
    return falhas, vagas


def alunos(alvos):
    if alvos:
        return [a.rstrip("/") for a in alvos]
    return sorted(os.path.dirname(p) for p in
                  glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json")))


def carrega_baseline():
    if not os.path.exists(BASELINE):
        return []
    return json.load(open(BASELINE, encoding="utf-8")).get("telas", [])


def main(argv):
    atualizar = "--update" in argv
    alvos = [a for a in argv if not a.startswith("--")]
    base = carrega_baseline()
    falhas, vagas = [], []
    for pasta in alunos(alvos):
        if not os.path.isdir(pasta):
            continue
        f, v = confere(pasta, base, colher=atualizar)
        falhas += f
        vagas += v

    if atualizar:
        antes, agora = len(base), len(vagas)
        # A PRIMEIRA gravacao e o alvara nascendo: nao ha o que "crescer" ainda. Depois
        # dela a baseline so cai -- e e por isso que o arquivo entra no repo no MESMO
        # commit que o gate, e nunca depois.
        primeira = not os.path.exists(BASELINE)
        if not alvos and not primeira and agora > antes:
            print(f"{VERMELHO}RECUSADO{ZERA} — a baseline so pode CAIR: {antes} -> {agora}. "
                  f"Tela nova nao entra no alvara; escreva o gabarito.")
            return 1
        json.dump({"_": "GATE 71 — telas cujo `Expected` ja era vago em 09/09/2026. "
                        "ALVARA, nao TODO: o gate as pula. So pode cair.",
                   "telas": sorted(set(vagas))},
                  open(BASELINE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{VERDE}baseline regravada{ZERA} — {antes} -> {len(set(vagas))} tela(s).")
        return 0

    curadas = sorted(set(base) - set(vagas))
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 71 REPROVOU{ZERA} — {len(falhas)} tela(s) de atividade "
              f"fechada cujo `Expected` nao resolve item por item.")
        return 1
    if curadas:
        print(f"{AMARELO}{len(curadas)} tela(s) da baseline ja tem gabarito{ZERA} — rode "
              f"--update para encolher o alvara.")
    print(f"{VERDE}GATE 71 OK{ZERA} — nenhuma tela nova com `Expected` vago "
          f"({len(base)} no alvara de 09/09/2026).")
    return 0


def selftest():
    import tempfile
    TELA = ('<div class="slide" data-slide="1" data-stage="1" data-teacher="">'
            '<!--BLOCOS:x1--></div>')

    def roda(blocos_, expected):
        with tempfile.TemporaryDirectory() as d:
            a = os.path.join(d, "aula1")
            os.makedirs(a)
            open(os.path.join(a, "slides.html"), "w", encoding="utf-8").write(TELA)
            json.dump(blocos_, open(os.path.join(a, "blocos.json"), "w", encoding="utf-8"),
                      ensure_ascii=False)
            json.dump({"1": {"expected": expected}},
                      open(os.path.join(a, "guia_telas.json"), "w", encoding="utf-8"),
                      ensure_ascii=False)
            return bool(confere(d)[0])

    TF = {"x1": [{"kind": "escolha", "id": "x1", "itens": [
        {"t": "Both reviews talk about the ending.", "ok": True},
        {"t": "Chris finds something good in the movie.", "ok": False}]}]}
    CL = {"x1": [{"kind": "classificar", "id": "x1", "opcoes": ["Maya", "Chris"], "itens": [
        {"t": "The ending stays with you for days.", "ok": "Maya"},
        {"t": "You can guess the story in ten minutes.", "ok": "Chris"}]}]}

    casos = [
        ("gabarito completo passa", False, TF,
         "True: Both reviews talk about the ending. False: Chris finds something good in "
         "the movie."),
        ("parafrase do defeito real reprova", True, TF,
         "True: both talk about the ending. The other one is not in the text."),
        ("item nao citado reprova", True, TF, "Both reviews talk about the ending."),
        ("citacao encurtada em 5 palavras passa", False, TF,
         "True: &ldquo;Both reviews talk about the&hellip;&rdquo; "
         "False: &ldquo;Chris finds something good in&hellip;&rdquo;"),
        ("classificar exige tambem a resposta", True, CL,
         "The ending stays with you for days. You can guess the story in ten minutes."),
        ("classificar com item e resposta passa", False, CL,
         "Maya: The ending stays with you for days. "
         "Chris: You can guess the story in ten minutes."),
        ("tela sem atividade fechada nao e medida", False,
         {"x1": [{"kind": "gravar", "id": "x1", "itens": [{"t": "z"}]}]}, ""),
        ("entidade e tipografia nao mudam o veredito", False, TF,
         "True: Both reviews talk about the ending&period; "
         "False: Chris finds something good in the movie."),
    ]
    erros = 0
    for nome, deve, bl, exp in casos:
        pegou = roda(bl, exp)
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(sys.argv[1:]))
