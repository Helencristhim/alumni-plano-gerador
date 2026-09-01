#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A VOZ DO MATERIAL, numa fonte só — lida pelo builder E pelo gate.

    o que se declara pode estar errado.
    o que nao se escreve nao pode.
    (render.py)

Este modulo existe pelo mesmo motivo que `audio_surface.py`: a lista tem de ser UMA. Se o
builder tivesse a sua copia e o gate a dele, as duas divergiriam na primeira edicao, e a
divergencia apareceria como material que passa no CI e carrega o defeito -- ou o contrario.

    O gate diz "isto esta errado". O builder diz "isto nao vai ser escrito".

A diferenca importa: enquanto a checagem so existia no CI, o defeito nascia, ia para o
disco, entrava no commit, subia no PR e so entao era pego -- e no meio disso alguem podia
mergear. Aqui a geracao PARA.

O QUE ESTA LISTA COBRE
----------------------
A superficie que um humano LE: texto visivel, notas de tela (`data-teacher`), guia e
cartoes. Nao o codigo do shell -- `checkpoint` como identificador nao e `checkpoint` numa
frase dita a professora.
"""
import glob
import html as _html
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHELL = os.path.join(RAIZ, "_build", "model", "shells", "consultivo.html")

# (id, o que por no lugar, regex). O texto do erro ENSINA: gate que so proibe ensina a
# contornar.
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

MARCADO_F = r"\b(?:a|à|da|pela|nossa|sua)\s+professora\b"
MARCADO_M = r"\b(?:o|ao|do|pelo|nosso|seu)\s+professor\b"

_shell_cache = None


def superficie(c):
    """So o que um humano LE: texto visivel, notas de tela, guia e cartoes."""
    teacher = " ".join(_html.unescape(m) for m in re.findall(r'data-teacher="([^"]*)"', c))
    corpo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", c, flags=re.S)
    corpo = _html.unescape(re.sub(r"<[^>]+>", " ", corpo))
    js = " ".join(_html.unescape(x) for x in
                  re.findall(r"var (?:GUIDE|CARDS)\s*=\s*(\{.*?\n\})", c, re.S))
    return corpo + "\n" + teacher + "\n" + js


def shell_superficie():
    """Os rotulos fixos da interface, que sao do molde e nao do autor da aula."""
    global _shell_cache
    if _shell_cache is None:
        _shell_cache = (superficie(open(SHELL, encoding="utf-8", errors="replace").read())
                        if os.path.exists(SHELL) else "")
    return _shell_cache


def janelas(texto, rx):
    """Cada ocorrencia com 18 caracteres de contexto de cada lado, normalizada.

    A janela e curta de proposito: o rotulo do shell e seguido, no material, pelo texto que
    o autor escreveu, e uma janela larga faria o mesmo rotulo parecer diferente."""
    saida = []
    for m in re.finditer(rx, texto, re.I):
        a, b = max(0, m.start() - 18), min(len(texto), m.end() + 18)
        saida.append(re.sub(r"\s+", " ", texto[a:b]).strip().lower())
    return saida


def do_autor(s, rx):
    """As ocorrencias que o AUTOR acrescentou, subtraindo o que ja vem do shell."""
    do_shell = set(janelas(shell_superficie(), rx))
    return [j for j in janelas(s, rx) if j not in do_shell]


def alunos_da_anatomia():
    """Primeiro nome de cada aluno com material na anatomia, tirado dos configs."""
    saida = {}
    for cfg in sorted(glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*",
                                             "config.json"))):
        try:
            with open(cfg, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        nome = (d.get("aluno") or {}).get("nome", "").strip()
        if d.get("slug") and nome:
            saida[d["slug"]] = nome
    return saida


def confere(html_do_material, slug=None, tratamento=""):
    """As tres familias, sobre o material ja montado. Devolve lista de mensagens.

    `slug` e `tratamento` vem do config: sem eles, a regra de aluno e a de genero nao tem
    contra o que medir e sao puladas."""
    s = superficie(html_do_material)
    fora = []

    for rid, texto, rx in REGRAS:
        achou = do_autor(s, rx)
        if achou:
            fora.append(f"VOZ DO MATERIAL ({rid}, {len(achou)}x): {texto} "
                        f"Primeira: “...{achou[0]}...”")

    if slug:
        alunos = alunos_da_anatomia()
        tela = s
        for outro, nome in alunos.items():
            if outro == slug:
                continue
            if re.search(r"\b" + re.escape(nome) + r"\b", tela):
                fora.append(
                    f"CONTAMINACAO DE ALUNO: o material nomeia “{nome}”, que e "
                    f"outro aluno da anatomia ({outro}). Se e personagem, escolha outro "
                    f"nome; se e observacao interna, ela nao vai para a tela.")

    decl = (tratamento or "").strip().lower()
    fem = do_autor(s, MARCADO_F)
    masc = do_autor(s, MARCADO_M)
    if fem and "professora" not in decl:
        fora.append(
            f"GENERO DO DOCENTE: o material trata quem da a aula no feminino ({len(fem)}x) "
            f"e o config nao declara `professor.tratamento` assim. Genero nao se deduz do "
            f"nome: declare no config, ou use a forma padrao ('o professor').")
    if masc and "professora" in decl:
        fora.append(
            f"GENERO DO DOCENTE: o config declara o tratamento no feminino e o material usa "
            f"a forma masculina {len(masc)}x. Numa mesma pagina, as duas formas fazem "
            f"parecer que sao duas pessoas.")
    return fora
