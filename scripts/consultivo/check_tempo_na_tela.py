#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 74 — o tempo de producao da aluna nao vai para a tela projetada.

A REGRA (A02 §3, e a revisao das aulas 19 e 20 da Gabriela Pires)
-----------------------------------------------------------------
    "Indicacoes de tempo para a producao oral do aluno pertencem ao Teacher's Guide e nao
     devem aparecer na superficie projetada ao aluno. [...] Validacao bloqueante: nenhum
     slide ou prompt dirigido ao aluno exibe 'three minutes', '2 min', 'you have X
     minutes' ou equivalente sem justificativa funcional registrada no Teacher's Guide."

As revisoes de 09/09 e 11/09/2026 tiraram da tela, uma a uma:

    aula 19, tela 2   "Someone asks you about a film. You have five seconds and one sentence."
    aula 20, tela 1   "When someone asks what you think, and you need three seconds [...]"
    aula 20, tela 8   "Three seconds are yours"

O QUE ELE MEDE — e por que nao e "numero + minutos"
---------------------------------------------------
A primeira sonda contou numero seguido de unidade de tempo em todo texto de instrucao das 28
aulas do consultivo: 57 achados. Uma boa parte nao era tempo de producao nenhum — "You watched
a class for fifty minutes" (a cena da aula 3 do molde), "a story you can guess in ten
minutes" (a resenha que a aluna le), "Ask a second question" (ordinal). Gate que acusa isso
ensina a declarar excecao por reflexo.

O que conta e o tempo PRESO A ACAO DA ALUNA, em cinco formas:

    you have / you need / you get  + N unidade        "You have five seconds"
    verbo de producao + (for|in) N unidade            "Talk for two minutes"
    N unidade + to + verbo de producao                "Fifteen seconds to decide"
    your N unidade                                    "Your two minutes"
    N unidade, sozinho na frase / "starting now" /
    "are yours"                                       "Sixty seconds." "Three seconds are yours"

Rodado com `--todas` sobre as 28 aulas (15/09/2026): 22 telas, 21 com tempo da aluna (pitch
de tres minutos, formato de exame, "One minute, starting now", "Talk for two minutes") e uma
que so cita um tempo ja produzido ("the same architecture as your three minutes in lesson 3").
Nenhuma cena, nenhum texto lido, nenhum ordinal. E os tres defeitos que a revisao da Gabriela
tirou sao pegos (selftest). `ask` saiu da lista de verbos depois da sonda: "They ask for ten
minutes" e o interlocutor pedindo, nao a aluna produzindo.

ONDE: so a tela PROJETADA — o deck (slides.html, com os blocos que ele declara, e o fecho do
close.json). O pre-class e o post-class nao sao projetados, e a aula exemplar mantem ali
"About 60 seconds" no gravador opcional, que e onde o normativo deixa.

A EXCECAO E DECLARADA, COMO O NORMATIVO PEDE
--------------------------------------------
Ha tempo que e parte autentica da tarefa: o formato cronometrado de um exame, os tres minutos
que o comprador deu. O A02 aceita — com a justificativa registrada no guia. Aqui isso e um
campo da entrada daquela tela em `guia_telas.json`:

    "7": { ..., "tempo_na_tela": "The exam gives 15 seconds to prepare; the timing is the task." }

O campo nao e emitido (o emissor ignora chave que nao conhece): ele existe para que a decisao
esteja escrita, e nao para a professora.

ESCOPO: aulas com `geracao.json` gen >= 1 (scripts/consultivo/geracao.py). As 28 anteriores a
15/09/2026 nao sao medidas — "nenhuma aula existente sera corrigida".

USO:
    python3 scripts/consultivo/check_tempo_na_tela.py [pasta-do-aluno ...]
    python3 scripts/consultivo/check_tempo_na_tela.py --todas     # ignora o carimbo (sonda)
    python3 scripts/consultivo/check_tempo_na_tela.py --selftest
"""
import html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import geracao  # noqa: E402

GEN = 1
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# "a second" fica de fora de proposito: e ordinal em "a second question", e "a second" como
# duracao ("give me a second") nao e instrucao de tela.
_NUM = (r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|"
        r"twenty|thirty|forty(?:[- ]five)?|fifty|sixty|ninety)")
_T = (r"(?:" + _NUM + r"[\s-]+(?:seconds?|secs?|minutes?|mins?)"
      r"|(?:a|half a|one)\s+minute)")
_ACAO = (r"(?:talk|speak|answer|say|tell|present|explain|take|prepare|write|decide|think|"
         r"record|choose|pitch|brief|argue|respond|reply|describe|summari[sz]e)(?:ing)?")
_PT_NUM = r"(?:\d+|um|uma|dois|duas|tr[eê]s|quatro|cinco|dez|quinze|vinte|trinta|sessenta|meio)"
_PT_T = _PT_NUM + r"\s+(?:segundos?|minutos?)"
_PT_ACAO = r"(?:fal\w+|respond\w+|escrev\w+|pens\w+|prepar\w+|decid\w+|grav\w+|apresent\w+)"
PADROES = [
    r"\byou(?:'ve|\s+have|\s+need|\s+get|\s+will\s+have)\s+(?:only\s+|just\s+|about\s+)?" + _T,
    r"\b" + _ACAO + r"\b[^.?!<]{0,30}?\b(?:for|in|within|under)\s+(?:about\s+|only\s+)?" + _T,
    r"\b" + _ACAO + r"\s+(?:about\s+)?" + _T + r"\b",
    r"\b" + _T + r"\s+(?:to|for)\s+" + _ACAO + r"\b",
    r"\byour\s+" + _T,
    r"\b" + _T + r",?\s+starting now",
    r"\b" + _T + r"\s+(?:is|are)\s+yours",
    r"(?:^|[.?!:]\s+)" + _T + r"\s*[.!]",
    r"\bvoc[eê]\s+tem\s+(?:s[oó]\s+|cerca de\s+)?" + _PT_T,
    r"\b" + _PT_ACAO + r"\b[^.?!<]{0,30}?\b(?:por|em)\s+(?:cerca de\s+)?" + _PT_T,
    r"\b" + _PT_T + r"\s+para\s+" + _PT_ACAO,
]
RX = re.compile("|".join(f"(?:{p})" for p in PADROES), re.I)
_FACHADA = {"", "-", "--", "—", "n/a", "na", "none"}


def telas(slides):
    ini = [m.start() for m in re.finditer(r'<div class="slide[\s"]', slides)]
    return [slides[a:b] for a, b in zip(ini, ini[1:] + [len(slides)])]


def _texto(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def _strings(v, fora=("id", "kind", "chave")):
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from _strings(x, fora)
    elif isinstance(v, dict):
        for k, x in v.items():
            if k not in fora and not k.startswith("_"):
                yield from _strings(x, fora)


def superficie_da_tela(tela, blocos, close):
    """O que a tela projeta: o texto visivel, os blocos que ela declara e, no fecho, o
    recap e a escala de confianca do close.json (que o shell escreve ali)."""
    partes = [_texto(re.sub(r'\sdata-teacher="[^"]*"', "", tela))]
    for bid in re.findall(r"<!--BLOCOS:([A-Za-z0-9_]+)-->", tela):
        partes += [_texto(s) for s in _strings(blocos.get(bid) or [])]
    if 'id="recapList' in tela and close:
        partes += [_texto(s) for s in _strings(close)]
    return " | ".join(p for p in partes if p)


def confere_aula(pasta, todas=False):
    if not todas and geracao.gen(pasta) < GEN:
        return []
    sp = os.path.join(pasta, "slides.html")
    if not os.path.exists(sp):
        return []

    def carrega(nome, padrao):
        p = os.path.join(pasta, nome)
        return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else padrao

    blocos, guia, close = carrega("blocos.json", {}), carrega("guia_telas.json", {}), \
        carrega("close.json", {})
    falhas = []
    for i, tela in enumerate(telas(open(sp, encoding="utf-8").read()), 1):
        just = str((guia.get(str(i)) or {}).get("tempo_na_tela", "")).strip()
        if just.lower() not in _FACHADA:
            continue
        s = superficie_da_tela(tela, blocos, close)
        achados = [s[max(0, m.start() - 30):m.end() + 12].strip() for m in RX.finditer(s)]
        if achados:
            falhas.append(
                f"{geracao.chave(pasta)} tela {i}: tempo de producao na tela projetada "
                f"({len(achados)}x) — “…{achados[0]}…”. O tempo vai no guia da tela; se ele "
                f"for parte autentica da tarefa (exame cronometrado, o tempo que o "
                f"interlocutor deu), declare o motivo em `tempo_na_tela` na entrada {i} do "
                f"guia_telas.json (A02 §3).")
    return falhas


def main(argv):
    todas = "--todas" in argv
    alvos = [a for a in argv if not a.startswith("--")]
    pastas = geracao.aulas(alvos or None)
    medidas = [p for p in pastas if todas or geracao.gen(p) >= GEN]
    falhas = []
    for p in pastas:
        falhas += confere_aula(p, todas)
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    if falhas:
        print(f"\n{VERMELHO}GATE 74 REPROVOU{ZERA} — {len(falhas)} tela(s) com o tempo da "
              f"aluna na superficie projetada.")
        return 1
    print(f"{VERDE}GATE 74 OK{ZERA} — {len(medidas)} aula(s) medida(s) (gen >= {GEN}) de "
          f"{len(pastas)}; nenhuma projeta o tempo de producao da aluna.")
    return 0


def selftest():
    import tempfile

    def roda(slides, gen=1, guia=None, blocos=None, close=None, nome="aluna-x/aula30"):
        with tempfile.TemporaryDirectory() as d:
            pasta = os.path.join(d, *nome.split("/"))
            os.makedirs(pasta)
            open(os.path.join(pasta, "slides.html"), "w", encoding="utf-8").write(slides)
            if gen is not None:
                json.dump({"gen": gen}, open(os.path.join(pasta, "geracao.json"), "w"))
            for arq, dado in (("guia_telas.json", guia), ("blocos.json", blocos),
                              ("close.json", close)):
                if dado is not None:
                    json.dump(dado, open(os.path.join(pasta, arq), "w", encoding="utf-8"))
            return bool(confere_aula(pasta))

    def tela(corpo, extra=""):
        return (f'<div class="slide slide-light" data-slide="1" data-stage="1" '
                f'data-teacher="Give her two minutes to prepare."{extra}><div class="slide-inner">'
                f'{corpo}</div></div>')

    casos = [
        ("aula 19, tela 2, antes da revisao", True,
         dict(slides=tela('<div class="doc-brief"><p class="doc-para">Someone asks you about '
                          'a film. You have five seconds and one sentence.</p></div>'))),
        ("aula 20, tela 1, antes da revisao", True,
         dict(slides=tela('<p class="slide-question">When someone asks what you think, and '
                          'you need three seconds &mdash; what do you say?</p>'))),
        ("aula 20, tela 8, antes da revisao", True,
         dict(slides=tela('<h2 class="slide-heading">Three seconds <span class="accent">are '
                          'yours</span></h2>'))),
        ("a mesma tela depois da revisao passa", False,
         dict(slides=tela('<h2 class="slide-heading">The time <span class="accent">is '
                          'yours</span></h2>'))),
        ("tempo num bloco declarado na tela", True,
         dict(slides=tela("<!--BLOCOS:x1-->"),
              blocos={"x1": [{"kind": "escolha", "abertura": ["Talk for two minutes."]}]})),
        ("tempo no recap do fecho", True,
         dict(slides=tela('<div id="recapList30"></div>'),
              close={"recap": ["Pitching my company in two minutes"], "conf": []})),
        ("excecao declarada no guia passa", False,
         dict(slides=tela('<h2 class="slide-heading">Fifteen seconds to decide</h2>'),
              guia={"1": {"tempo_na_tela": "The exam format gives 15 seconds; timing is the task."}})),
        ("excecao de fachada nao vale", True,
         dict(slides=tela('<h2 class="slide-heading">Fifteen seconds to decide</h2>'),
              guia={"1": {"tempo_na_tela": "N/A"}})),
        ("o tempo no data-teacher (guia) nao e tela", False,
         dict(slides=tela('<p class="slide-question">Tell her what you think.</p>'))),
        ("a resenha que a aluna le nao e instrucao", False,
         dict(slides=tela('<p class="doc-para">Two hours is a long time for a story you can '
                          'guess in ten minutes.</p>'))),
        ("a cena da aula nao e tempo de producao", False,
         dict(slides=tela('<p class="slide-lead">You watched a class for fifty minutes. Each '
                          'one speaks for thirty seconds.</p>'))),
        ("ordinal nao e duracao", False,
         dict(slides=tela('<div class="q-item">Ask a second question about the answer.</div>'))),
        ("aula anterior ao carimbo (gen 0, na lista) nao e medida", False,
         dict(slides=tela('<p class="slide-question">You have two minutes.</p>'), gen=None,
              nome="gabriela-pires/aula20")),
        ("aula SEM carimbo fora da lista e medida (duvida e material novo)", True,
         dict(slides=tela('<p class="slide-question">You have two minutes.</p>'), gen=None)),
        ("apoio em portugues tambem e tela", True,
         dict(slides=tela('<p class="slide-pt">Você tem dois minutos para falar.</p>'))),
    ]
    erros = 0
    for nome, deve, kw in casos:
        pegou = roda(**kw)
        ok = pegou == deve
        erros += not ok
        print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
              f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(sys.argv[1:]))
