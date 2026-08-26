#!/usr/bin/env python3
"""GATE 45 -- a atividade e DECLARADA, nao escrita a mao.

O problema que este gate existe para fechar e o que a Helen descreveu em 25/08/2026: o
gerador "capta o essencial, mas deixa passar detalhe que e regra fixa e clara", e repete o
erro mesmo depois de o normativo ser reforcado. Gate que so barra no fim nao resolve isso
-- quando ele reprova, o defeito ja nasceu, e o autor volta a escrever o mesmo HTML.

A saida foi tirar o exercicio da mao de quem escreve: o autor DECLARA (`blocos.json`) e o
builder EMITE (`render.py`). O `data-ok` deixa de ser digitado -- o autor escreve o TEXTO da
resposta certa e a letra e derivada. As classes deixam de ser digitadas. A ordem dos
atributos deixa de ser digitada. Nao ha o que errar porque nao ha o que teclar.

Isto so continua verdade enquanto NINGUEM voltar a escrever exercicio direto no fragmento.
E o que este gate mede: fragmento de pre-class e post-class do consultivo nao contem HTML de
atividade -- so prosa e `<!--BLOCOS:chave-->`.

O que ele NAO mede: se a declaracao esta pedagogicamente certa. Isso e do GATE 44 e da
leitura humana. Aqui a pergunta e uma so, e de forma: o exercicio veio do emissor?

Escopo: os fragmentos do consultivo. NAO varre o repo -- o imersivo escreve HTML no
fragmento por construcao, e cobrar isto dele seria cobrar que ele fosse outro molde.
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# As marcas sao de FORMA, nao de palavra: cada uma so aparece em HTML de atividade que o
# render sabe emitir. Prosa que MENCIONE "match-grid" num paragrafo nao constroi grade
# nenhuma, entao a busca e pela tag/atributo, nunca pelo nome solto.
# `_do-artefato` fica de fora, e nao e comodidade. Aquilo nao e escrito por ninguem: e o
# que o `extrai_fragmentos.py` tira do artefato a cada rodada de CI, para o round-trip
# provar que o builder devolve o artefato. O artefato e o prototipo do claude.ai, e ali o
# HTML cru e legitimo -- e a origem, nao a saida.
#
# O que essa exclusao esconde, medido em 25/08/2026 para nao virar suposicao: das 24
# seccoes das aulas 19 e 20 do Marcos, o emissor reproduz 4 (normalizando entidade, porque
# o fragmento extraido vem decodificado). O molde da Stephanie esta em 48 de 48. Ou seja: o
# emissor cobre O MOLDE, ainda nao toda forma que os artefatos usam. Quando uma aula do
# Marcos virar material, ela passa pelo conversor como qualquer outra, e o que ele nao
# souber emitir vira forma nova no render -- nao excecao aqui.
FORA_DO_ALCANCE = os.sep + "_do-artefato" + os.sep

MARCAS = [
    (r'<div class="match-grid"', "grade de classificar/completar", "classificar / completar"),
    (r'<div class="quiz-options"', "lista de marcar", "escolha"),
    (r'<div class="pair-grid"', "grade de duas leituras", "par"),
    (r'<input class="blank-input"', "lacuna", "lacuna"),
    (r'<div class="res-card">', "cartao de acervo", "recursos / recurso"),
    (r'<textarea class="writebox"', "caixa de escrita", "escrita"),
    (r'onclick="sayAs\(', "barra de audio", "audio"),
    (r'<div class="chunk-line"|<p class="chunk-line"', "linha de frase", "frases"),
    (r'data-gravador=|onclick="recToggle\(', "gravador", "gravador"),
]


def main():
    alvos = sorted(p for p in
                   glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                                          "preclass.html")) +
                   glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "aula*",
                                          "postclass.html"))
                   if FORA_DO_ALCANCE not in p)
    if not alvos:
        raise SystemExit("GATE 45 — nenhum fragmento de pre/post-class do consultivo. "
                         "O gate nao tem o que medir, e isso e falha: ou o caminho mudou "
                         "ou o material sumiu.")
    faltas = []
    for p in alvos:
        s = open(p, encoding="utf-8").read()
        # Comentario de HTML nao chega ao olho de ninguem, e o marcador de bloco E um
        # comentario -- tirar os dois antes de medir evita acusar o proprio mecanismo.
        s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
        rel = os.path.relpath(p, RAIZ)
        for padrao, oque, kind in MARCAS:
            n = len(re.findall(padrao, s))
            if n:
                faltas.append(f"  {rel}: {n}x {oque} escrito a mao — declare como "
                              f"`kind: {kind}` no blocos.json e deixe o builder emitir.")
    if faltas:
        print("GATE 45 — atividade escrita a mao no fragmento do consultivo.\n")
        print("\n".join(faltas))
        print("\nO exercicio do consultivo e DECLARADO, nao teclado. Escrever o HTML direto")
        print("devolve ao autor o `data-ok`, as classes e a ordem dos atributos — que e")
        print("exatamente o que fazia o mesmo defeito voltar depois de corrigido.")
        print("\n  python3 scripts/consultivo/migra_blocos.py <fragmento> --escreve")
        print("\nO conversor so converte o que ele consegue re-emitir byte a byte; o que")
        print("sobrar pendente e forma que o render ainda nao sabe fazer — acrescente lá.")
        return 1
    print(f"✓ GATE 45 — {len(alvos)} fragmento(s): toda atividade vem do emissor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
