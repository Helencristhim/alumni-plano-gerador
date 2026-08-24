#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva os DOIS shells da anatomia `private-black` DO ARTEFATO, por script.

POR QUE POR SCRIPT, E NAO A MAO
-------------------------------
O artefato (`_build/model/artefatos/marcos-private-black.html`) e a ESPECIFICACAO da
interface: dele se COPIA, classe por classe. O porte a mao ja foi feito uma vez neste
projeto, em 11/08/2026, e renomeou cada peca (`reveal-item` virou `ic-reveal`,
`blank-input` virou `ic-blank`...); o inventario catalogou a REESCRITA, e o gate passou a
comparar a copia consigo mesma -- verde para sempre, medindo coerencia interna e chamando
isso de fidelidade. Quatro pecas do artefato (`callout`, 23,8 usos/aula; `tbl-wrap`;
`quiz-option`; `rule-box`) simplesmente nunca existiram no molde, e ninguem viu por meses.

Um script torna a derivacao AUDITAVEL: qualquer pessoa roda de novo e ve que o shell e o
artefato menos o que esta declarado aqui embaixo. Nada foi reescrito no caminho.

DOIS SHELLS, PORQUE A ENTREGA E DE DUAS URLS
--------------------------------------------
Regra da Stephanie, 24/08/2026, ja incorporada ao 00, ao 04, ao P1, ao P2 e ao P3:

    "A producao final deve gerar duas URLs distintas. A URL do professor contem a visao
     docente e permite alternar para uma previa da visao do aluno. A URL do aluno contem
     exclusivamente o conteudo destinado ao aluno. Gabaritos, Teacher's Guide, registros
     internos, hipoteses pedagogicas, evidencias reservadas e controles docentes nao podem
     estar apenas ocultos no HTML do aluno: nao devem integrar o arquivo, payload ou estado
     entregue por essa URL."

O artefato e UM arquivo com alternador -- e legitimo, porque e protótipo (P1 §0) e uma
pagina do claude.ai nao tem duas URLs. Para producao, o alternador continua existindo na
URL do professor (como previa) e NAO existe na do aluno, porque nao ha o outro lado dentro
dela.

    shells/black.html        professor: as 6 abas, o deck, o guia, a previa do aluno

O BUILD DO ALUNO E O PROXIMO PASSO, E NAO ESTA AQUI DE PROPOSITO
----------------------------------------------------------------
Ele nao e "o mesmo arquivo com pedacos escondidos": e outro build. Tentei deriva-lo junto
com este e o GATE 35 mostrou por que ele merece PR proprio -- remover o deck faz o boot
morrer em `deckInit`, na primeira linha, levando junto TODOS os construtores seguintes
(P2 §25: "uma excecao no boot nao fica onde nasceu"). Sem navegador isso nao aparece: o
HTML e valido e todo gate estatico fica verde.

Medido no navegador, o build do aluno precisa de:

  - um BOOT proprio, que chame so o que e dele (persInit, preKeys, preInit, audBuild,
    hubPaint, sfBuild, snapInit) e nenhum construtor de deck;
  - a remocao dos DADOS docentes do JS entregue -- PC_NOTAS (os gabaritos do pre-class,
    5,4 KB), GUIDE, CP, EP_MAPA, ESCALA, e os textos que so o deck usa;
  - a remocao das ROTAS docentes -- `?mode=teacher-guide` e o caminho que promove papel
    (P3 §3: "a URL do aluno nao possui alternador, rota de professor ou elevacao de papel
    por query, hash, armazenamento, atributo ou chamada direta").

Nada disso e cosmetico, e por isso vai com gate proprio (isolamento), que le os BYTES do
arquivo entregue -- nao a folha de estilo.

AS DUAS AULAS DO ARTEFATO FICAM NOS DOIS SHELLS
-----------------------------------------------
Nao e descuido, e o conserto de um erro que este repo ja pagou. No porte da story-quest eu
tirei a segunda aula "porque o molde carrega uma aula de exemplo"; medindo depois, a aula 2
levava embora mecanica que a aula 1 nao tem. Aqui vale igual: a 19 e Listening e a 20 e
Reading, e elas nao usam as mesmas pecas. Anatomia e o que a forma OFERECE; a aula escolhe.
O builder troca o conteudo inteiro, entao duas aulas de exemplo nao custam nada na geracao.

USO:
    python3 scripts/black/extrai_shell.py            # escreve os dois shells
    python3 scripts/black/extrai_shell.py --check    # nao escreve: confere o disco
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTEFATO = os.path.join(RAIZ, "_build", "model", "artefatos", "marcos-private-black.html")
SHELLS = os.path.join(RAIZ, "_build", "model", "shells")
SHELL_PROF = os.path.join(SHELLS, "black.html")

CARIMBO = '<meta name="alumni-anatomia" content="private-black">'

# O shell fala os literais do MODELO (stephanie-vicente, a aluna-modelo do molde adulto).
# O builder troca por aluno. Trocar aqui e o mesmo que o base_swaps faz no imersivo.
NOMES = [
    ("Marcos Mansour", "Stephanie Vicente"),
    ("Mansour", "Vicente"),
    ("Marcos", "Stephanie"),
    ("marcos_pv_v1", "MODELO_STORE"),   # vira derivado do ARTEFATO.id, ver STORE_DERIVADO
]

# P1 §3: "dado pessoal em identificador tecnico vaza para fora da interface e sobrevive a
# toda troca de rotulo". O artefato guarda o estado em 'marcos_pv_v1' -- uma chave montada
# com o nome de uma pessoa. Isto NAO e divergencia do artefato: e o proprio P1 sendo
# obedecido onde o artefato, sendo pagina de uma pessoa so, nao precisou obedecer.
#
# A chave e LITERAL, montada no build, e nao 'pv_'+artefatoId()+'_v1' em tempo de execucao.
# Tentei a segunda forma primeiro e ela QUEBROU O BOOT INTEIRO: `var STORE` aparece na secao
# de persistencia, muito antes de `var ARTEFATO` ser declarado, entao artefatoId() rodava com
# ARTEFATO ainda undefined -- "Cannot read properties of undefined (reading 'id')". O HTML
# continuava valido, todo gate estatico continuava verde, e o boot morria na primeira linha
# levando junto TUDO o que vinha depois (P2 §25: a excecao no boot nao fica onde nasceu).
# Quem pegou foi o GATE 35, no navegador, comparando com o artefato -- que boota limpo.
MODELO_ID = "private-black-modelo"
STORE_DERIVADO = "var STORE='pv_" + MODELO_ID + "_v1';"


def fecha_tag(s, i, tag="div"):
    """Indice logo APOS o fechamento da tag aberta em i. Por BALANCO, nunca pelo primeiro
    </div> -- o primeiro fecha um filho (P2: 'nunca extrair bloco ate </div>')."""
    depth = 0
    for m in re.finditer(r"<" + tag + r"\b|</" + tag + r"\s*>", s[i:]):
        depth += 1 if not m.group(0).startswith("</") else -1
        if depth == 0:
            return i + m.end()
    raise SystemExit(f"tag <{tag}> aberta em {i} nao fecha")


def mascara_script_style(s):
    """Copia de s com o MIOLO de <script>/<style> neutralizado, mantendo os offsets.

    Sem isto, qualquer varredura por '<div' encontra '<div' dentro de string JS e de
    comentario CSS, e o balanco de tags passa a mentir."""
    out = list(s)
    for m in re.finditer(r"<(script|style)\b[^>]*>(.*?)</\1\s*>", s, re.S):
        for k in range(m.start(2), m.end(2)):
            if out[k] != "\n":
                out[k] = "."
    return "".join(out)


def corpo_do_artefato():
    """O documento REAL, sem a moldura do claude.ai.

    O .html que o navegador salva traz o frame-runtime do host: dois <script>, um <style>
    e um <body data-view="professor"> proprios. O documento do artefato comeca DEPOIS
    disso, e traz os proprios <meta>, <title> e <style> -- escritos como se fossem head,
    porque o host injeta tudo dentro do body."""
    with open(ARTEFATO, encoding="utf-8") as fh:
        h = fh.read()
    i = h.find('<body data-view="professor">')
    if i < 0:
        raise SystemExit("artefato sem <body data-view=...>: a moldura mudou de forma")
    ini = h.index(">", i) + 1
    fim = h.rindex("</body>")
    return h[ini:fim]


def monta_documento(corpo, lang="pt-BR", view="professor"):
    """Reconstroi um documento HTML de verdade: o que o artefato escreveu como se fosse
    head volta para o head."""
    # o head do artefato vai ate o fim do ULTIMO <style> antes do primeiro <div>
    prim_div = corpo.index("<div ")
    ult_style = corpo.rindex("</style>", 0, prim_div) + len("</style>")
    cabeca, resto = corpo[:ult_style], corpo[ult_style:]
    cabeca = cabeca.replace('<meta charset="UTF-8">', "", 1).strip()
    return (
        "<!DOCTYPE html>\n"
        f'<html lang="{lang}">\n<head>\n'
        '<meta charset="UTF-8">\n'
        f"{CARIMBO}\n"
        f"{cabeca}\n"
        f"</head>\n<body data-view=\"{view}\">\n"
        f"{resto.strip()}\n</body>\n</html>\n"
    )


def deriva_professor():
    rel = {}
    corpo = corpo_do_artefato()
    for velho, novo in NOMES:
        rel[f"swap/{velho}"] = corpo.count(velho)
        corpo = corpo.replace(velho, novo)
    # a chave de estado deixa de carregar nome de pessoa (P1 §3)
    antes = corpo
    corpo = re.sub(r"var STORE='MODELO_STORE';", STORE_DERIVADO, corpo)
    corpo = corpo.replace("localStorage.getItem('MODELO_STORE')",
                          "localStorage.getItem('pv_" + MODELO_ID + "_v1')")
    rel["store/derivado-do-artefato-id"] = 1 if corpo != antes else 0
    # o id tecnico do artefato passa a ser o do MODELO
    corpo, n = (re.subn(r"var ARTEFATO=\{id:'[^']*'\}",
                        "var ARTEFATO={id:'" + MODELO_ID + "'}", corpo))
    rel["artefato-id/modelo"] = n
    return monta_documento(corpo), rel


def escreve(caminho, conteudo, check):
    atual = None
    if os.path.exists(caminho):
        with open(caminho, encoding="utf-8") as fh:
            atual = fh.read()
    if check:
        return "IGUAL" if atual == conteudo else ("DIFERE" if atual is not None else "AUSENTE")
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(conteudo)
    return "escrito"


def main():
    check = "--check" in sys.argv
    prof, rel_p = deriva_professor()

    print("=== derivacao do artefato ===")
    for k, v in rel_p.items():
        print(f"  {k:44s} {v}")

    r1 = escreve(SHELL_PROF, prof, check)
    print(f"\n  {os.path.relpath(SHELL_PROF, RAIZ):46s} {len(prof):8d} bytes  {r1}")
    if check and r1 != "IGUAL":
        print("\nFALHOU — o shell no disco NAO e o que sairia do artefato hoje.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
