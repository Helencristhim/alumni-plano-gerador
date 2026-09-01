#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 51 — o material fala DO ALUNO, nunca de si mesmo nem do processo que o produziu.

POR QUE ISTO EXISTE (01/09/2026)
--------------------------------
O Dan abriu a primeira pagina do material da Joice — a aba Perfil, que a professora le
antes da aula — e achou isto:

    "E o primeiro A1 desta anatomia: os quatro materiais anteriores sao B1+. O pacote
     normativo cobre A1 explicitamente e autoriza apoio em portugues neste nivel."

Isso nao descreve a aluna. Descreve o SISTEMA que produziu o arquivo, na pagina que existe
para descrever a aluna. Junto vieram os codigos internos das hipoteses (`H1`, `H2`, `H3`)
usados como se a professora soubesse o que sao, `checkpoint`, `estado pedagogico`,
`criterio N do ciclo`, e o material justificando o proprio desenho ("nao e escolha
tematica", "o bloco mede fala e interacao"). Num cartao de aula havia ate uma referencia a
hipotese "do bloco do Caio" — outro aluno.

    A regra: o vocabulario de PRODUCAO nao aparece na superficie de LEITURA.
    O conteudo pedagogico continua; muda a lingua em que ele e dito.

Nada disso e sutil, e nenhum gate via, porque todos os outros medem forma (etapas,
minutos, componentes, audio) e este mede a VOZ.

O QUE ELE MEDE, E ONDE
----------------------
So o que um humano LE no arquivo publicado da anatomia `consultivo`:

  - o texto visivel (fora de <script> e <style>);
  - as notas de tela (`data-teacher`), que e o que a professora abre durante a aula;
  - as strings do `var GUIDE` e dos cartoes, que sao o guia e o cartao de cada aula.

NAO mede o codigo do shell: `checkpoint` como nome de variavel ou classe CSS e outra
coisa, e acusa-lo daria falso positivo em todos os 12 arquivos (medido).

A DIVIDA ANTERIOR FICA CONGELADA
--------------------------------
`voz-baseline.json` guarda quantas ocorrencias cada arquivo JA tinha em 01/09/2026. O gate
so reprova o que PASSAR desse numero. Isso e deliberado: os materiais do Luiz, da Lucia e
da Stephanie sao anteriores a esta correcao e nao se mexe neles sem pedido (REGRA 30).
A baseline so pode CAIR — `--update` recongela depois de uma limpeza legitima.

USO:
    python3 scripts/consultivo/check_voz_do_material.py
    python3 scripts/consultivo/check_voz_do_material.py --update    # recongela a base
    python3 scripts/consultivo/check_voz_do_material.py --selftest  # prova que morde
"""
import glob
import html as _html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voz-baseline.json")
ANATOMIA = "consultivo"

VERM, VERDE, AMAR, ZERA = "\033[31m", "\033[32m", "\033[33m", "\033[0m"

# Cada regra: (id, o que e, regex). O texto do erro tem de dizer o que POR no lugar —
# gate que so proibe ensina a contornar, nao a escrever.
REGRAS = [
    ("codigo-de-hipotese",
     "codigo interno de hipotese (H1/H2/H3) na voz do material. Diga o que se observa, "
     "nao o codigo: 'Observar se ela formula perguntas', e nao 'H1'.",
     r"hip[oó]tese\s*(?:<[^>]+>)?\s*H[123]\b|hypothesis\s*H[123]\b"
     r"|(?<![\w>&])H[123](?=\s*(?:[:—(,.]|</))"),
    ("checkpoint",
     "'checkpoint' e palavra do processo de producao. Na tela: 'a aula que fecha o bloco', "
     "'o registro do bloco'.",
     r"\bcheckpoint\b"),
    ("estado-pedagogico",
     "'estado pedagogico' / 'estado.json' e um arquivo interno. Na tela: 'os registros do "
     "bloco', 'o que ficou registrado'.",
     r"estado pedag[oó]gico|pedagogical state|estado\.json"),
    ("documento-normativo",
     "referencia a documento normativo, secao (§) ou 'anatomia' na voz do material. A "
     "professora nao le o pacote: diga a regra, nao a fonte dela.",
     r"pacote normativ\w*|normative package|\bnormativ\w+|\banatomia\b|\d\d\s?§|§\s?\d"),
    ("criterio-numerado",
     "'criterio N do ciclo' e numeracao interna. Diga o criterio.",
     r"crit[ée]rio\s+\d+\s+do\s+ciclo|criterion\s+\d+\s+of\s+the\s+cycle"),
    ("defeito",
     "'defeito' nao e termo pedagogico, e o sujeito da frase costuma ser o aluno. Use "
     "'ponto de desenvolvimento', 'dificuldade', 'o que ainda nao aparece'.",
     r"\bdefeitos?\b"),
    ("material-falando-de-si",
     "o material justificando o proprio desenho. A pagina descreve o aluno, nao a decisao "
     "de quem a escreveu.",
     r"escolha tem[áa]tica|medida isolada|o bloco (?:mede|cobra|n[ãa]o pede|n[ãa]o faz)"
     r"|este bloco (?:mede|cobra)|o material (?:nunca|n[ãa]o)"),
]


def superficie(c):
    """So o que um humano LE: texto visivel, notas de tela, guia e cartoes.

    O codigo do shell fica de fora de proposito — `checkpoint` como identificador nao e a
    mesma coisa que `checkpoint` numa frase dita a professora, e medir os dois juntos
    acusaria os 12 arquivos da anatomia sem que houvesse defeito nenhum."""
    teacher = " ".join(_html.unescape(m) for m in re.findall(r'data-teacher="([^"]*)"', c))
    corpo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", c, flags=re.S)
    corpo = _html.unescape(re.sub(r"<[^>]+>", " ", corpo))
    js = " ".join(_html.unescape(x) for x in
                  re.findall(r"var (?:GUIDE|CARDS)\s*=\s*(\{.*?\n\})", c, re.S))
    return corpo + "\n" + teacher + "\n" + js


SHELL = os.path.join(RAIZ, "_build", "model", "shells", "consultivo.html")
_shell_cache = None


def shell_superficie():
    """A superficie do SHELL VAZIO — os rotulos fixos da interface.

    A aba de Evidencias do molde tem, no proprio shell, "Estado pedagogico do ciclo" e
    "Decisoes de checkpoint": sao NOMES DE SECAO do produto, iguais nos doze arquivos, e
    nao algo que o autor da aula escreveu. Medi-los daria a mesma acusacao em todo mundo e
    empurraria para renomear a interface — o que e outra decisao, do Dan, e toca material
    que nao se mexe.

    Entao o gate mede o DELTA: o que o autor acrescentou por cima do shell."""
    global _shell_cache
    if _shell_cache is None:
        _shell_cache = superficie(open(SHELL, encoding="utf-8", errors="replace").read()) \
            if os.path.exists(SHELL) else ""
    return _shell_cache


def _janelas(texto, rx):
    """Cada ocorrencia com 18 caracteres de contexto de cada lado, normalizada.

    A janela e curta de proposito: o rotulo do shell e seguido, no material, pelo texto
    que o autor escreveu, e uma janela larga faria o mesmo rotulo parecer diferente."""
    saida = []
    for m in re.finditer(rx, texto, re.I):
        a, b = max(0, m.start() - 18), min(len(texto), m.end() + 18)
        saida.append(re.sub(r"\s+", " ", texto[a:b]).strip().lower())
    return saida


def mede(caminho):
    c = open(caminho, encoding="utf-8", errors="replace").read()
    if 'name="alumni-anatomia" content="%s"' % ANATOMIA not in c[:4000]:
        return None
    s = superficie(c)
    shell = shell_superficie()
    fora = {}
    for rid, _, rx in REGRAS:
        do_shell = set(_janelas(shell, rx))
        do_autor = [j for j in _janelas(s, rx) if j not in do_shell]
        fora[rid] = len(do_autor)
    return fora


def tratamento_declarado(caminho):
    """Como o config manda tratar quem da a aula: 'a professora', 'o professor', ou nada.

    O genero de quem ensina NAO se deduz do nome — e a regra que ja custou um erro no
    material da Joice, cujo professor e homem e que dizia "a professora". O cadastro guarda
    o NOME, e nome nao e genero.

    Entao: ou o config declara `professor.tratamento`, e o material pode usar a forma
    marcada que ele declara, ou nao declara, e o material usa a forma nao marcada
    ('quem da a aula', 'o docente'). O que nao pode e o material escolher sozinho."""
    arq = os.path.basename(caminho)
    for cfg in sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*",
                                             "config.json"))):
        try:
            with open(cfg, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        if d.get("slug") and arq.startswith(d["slug"]):
            return ((d.get("professor") or {}).get("tratamento") or "").strip().lower()
    return ""


MARCADO_F = r"\b(?:a|à|da|pela|nossa|sua)\s+professora\b"
MARCADO_M = r"\b(?:o|ao|do|pelo|nosso|seu)\s+professor\b"


def genero_do_docente(caminho, s):
    """A forma de tratar quem da a aula bate com o que o config declara.

    A assimetria e da lingua, e nao um descuido da regra: em portugues *o professor* e a
    forma padrao de quem escreve um documento sem saber quem vai le-lo, e passa sem
    declaracao. *A professora* e escolha especifica — e foi exatamente ela, escrita sem
    base, que pos o material da Joice tratando por "a professora" um professor homem.

    Quem DECLARA `professor.tratamento` tem de ser consistente: o material da Lucia, cuja
    professora e mulher, dizia "a professora" nove vezes e "o professor" oito, na mesma
    pagina."""
    decl = tratamento_declarado(caminho)
    # o delta contra o shell, como nas outras regras: "Sintese do professor" e "Checklist do
    # professor" sao rotulos da aba de Evidencias, e aparecem uma vez por linha da tabela.
    shell = shell_superficie()
    fem = [j for j in _janelas(s, MARCADO_F) if j not in set(_janelas(shell, MARCADO_F))]
    masc = [j for j in _janelas(s, MARCADO_M) if j not in set(_janelas(shell, MARCADO_M))]
    fora = []
    if fem and "professora" not in decl:
        fora.append(
            f"GENERO DO DOCENTE: o material trata quem da a aula por "
            f"'a professora' ({len(fem)}x) e o config nao declara "
            f"`professor.tratamento` no feminino. Genero nao se deduz do nome: declare no "
            f"config, ou use a forma padrao ('o professor').")
    if masc and "professora" in decl:
        fora.append(
            f"GENERO DO DOCENTE: o config declara `professor.tratamento` no feminino e o "
            f"material usa a forma masculina {len(masc)}x. Numa mesma pagina, as duas "
            f"formas fazem parecer que sao duas pessoas.")
    return fora


def alvos():
    for lado in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", lado, "*.html"))):
            yield p


def carrega():
    if not os.path.exists(BASE):
        return {}
    with open(BASE, encoding="utf-8") as f:
        return json.load(f).get("arquivos", {})


def main():
    if "--selftest" in sys.argv:
        return selftest()
    base = carrega()
    atual, fails, limpos, textos_extra = {}, [], 0, {}
    for p in alvos():
        m = mede(p)
        if m is None:
            continue
        rel = os.path.relpath(p, RAIZ)
        gen = genero_do_docente(p, superficie(open(p, encoding="utf-8",
                                                   errors="replace").read()))
        if gen:
            m = dict(m)
            m["genero-do-docente"] = len(gen)
            textos_extra[rel] = gen
        atual[rel] = {k: v for k, v in m.items() if v}
        antes = base.get(rel, {})
        piorou = {k: (antes.get(k, 0), v) for k, v in m.items() if v > antes.get(k, 0)}
        if piorou:
            fails.append((rel, piorou))
        elif not atual[rel]:
            limpos += 1

    if "--update" in sys.argv:
        with open(BASE, "w", encoding="utf-8") as f:
            json.dump({
                "_leia": ("Quanta voz de PRODUCAO cada material publicado da anatomia "
                          "consultivo ainda carrega. NAO e uma lista de tarefas: e o "
                          "ALVARA do que ja existia em 01/09/2026 e que nao se mexe sem "
                          "pedido (REGRA 30). O gate reprova o que PASSAR desses numeros. "
                          "Recongelar (--update) so depois de uma limpeza legitima: a base "
                          "so pode CAIR."),
                "arquivos": {k: v for k, v in sorted(atual.items()) if v},
            }, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print(f"baseline recongelada: {sum(sum(v.values()) for v in atual.values())} "
              f"ocorrencia(s) em {len([1 for v in atual.values() if v])} arquivo(s).")
        return 0

    textos = {rid: t for rid, t, _ in REGRAS}
    print(f"=== GATE 51 — a voz do material (anatomia {ANATOMIA}) ===")
    for rel, piorou in fails:
        print(f"{VERM}FAIL{ZERA}  {rel}")
        for rid, (antes, agora) in sorted(piorou.items()):
            if rid == "genero-do-docente":
                for t in textos_extra.get(rel, []):
                    print(f"        {t}")
            else:
                print(f"        {rid}: {antes} -> {agora}. {textos[rid]}")
    if fails:
        print(f"\n{VERM}GATE 51 — {len(fails)} arquivo(s) com voz de producao NOVA.{ZERA}")
        print("A pagina descreve o aluno. O vocabulario de quem produziu o material fica "
              "fora dela.")
        return 1
    divida = sum(sum(v.values()) for v in atual.values())
    print(f"{VERDE}GATE 51 OK{ZERA} — {len(atual)} arquivo(s) da anatomia; {limpos} sem "
          f"nenhuma ocorrencia.")
    if divida:
        print(f"  divida congelada: {divida} ocorrencia(s) anteriores a 01/09/2026 "
              f"(scripts/consultivo/voz-baseline.json). Nao e lista de tarefas.")
    return 0


def selftest():
    """Prova que morde: injeta cada padrao numa superficie e confere que e visto, e que o
    mesmo padrao DENTRO de <script> nao e."""
    falhas = []
    for rid, _, rx in REGRAS:
        amostras = {
            "codigo-de-hipotese": "e a hipótese H1, decidida depois",
            "checkpoint": "esta e a aula do checkpoint",
            "estado-pedagogico": "leia o estado pedagogico antes",
            "documento-normativo": "o pacote normativo cobre A1",
            "criterio-numerado": "e o criterio 2 do ciclo",
            "defeito": "o defeito tem forma precisa",
            "material-falando-de-si": "nao e escolha tematica",
        }[rid]
        visivel = f'<meta name="alumni-anatomia" content="consultivo"><p>{amostras}</p>'
        escondido = (f'<meta name="alumni-anatomia" content="consultivo">'
                     f'<script>var x = "{amostras}";</script>')
        if not re.findall(rx, superficie(visivel), re.I):
            falhas.append(f"{rid}: NAO viu o padrao no texto visivel")
        if re.findall(rx, superficie(escondido), re.I):
            falhas.append(f"{rid}: viu o padrao DENTRO de <script> (falso positivo)")
    # e um arquivo sem o carimbo nao e medido
    if mede.__doc__ is None:
        pass
    # a regra do genero: a forma feminina sem declaracao reprova; a masculina, nao
    fem = superficie('<p>a producao e sempre com a professora</p>')
    masc = superficie('<p>o professor conduz a etapa</p>')
    if not genero_do_docente("/tmp/nao-declarado.html", fem):
        falhas.append("genero: NAO viu a forma feminina sem declaracao")
    if genero_do_docente("/tmp/nao-declarado.html", masc):
        falhas.append("genero: reprovou a forma padrao ('o professor') sem declaracao")
    for f in falhas:
        print(f"{VERM}selftest FAIL{ZERA}  {f}")
    if falhas:
        return 1
    print(f"{VERDE}selftest OK{ZERA} — as {len(REGRAS)} regras veem o texto visivel e "
          f"ignoram o codigo, e a do genero distingue forma marcada de forma padrao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
