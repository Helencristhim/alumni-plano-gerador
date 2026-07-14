#!/usr/bin/env python3
"""
Gera os fixtures do canario a partir de uma aula LIMPA (que passa no validador),
injetando UM defeito em cada copia. Rodar quando o shell do modelo mudar, pra
os fixtures continuarem "quase certos, com um erro so".

    python3 scripts/canary/build_fixtures.py

Por que a partir de uma aula real, e nao um HTML inventado: o validate_lesson faz
DEZENAS de checagens antes de chegar nos 4 gates que o canario mira. Um HTML
minimo morreria por outro motivo (aula orfa, espelho faltando, etc.) e o canario
nao saberia dizer se foi o gate certo que reprovou. Partindo de uma aula que
PASSA, o unico FAIL que aparece e o defeito que injetamos — prova limpa.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BASE = os.path.join(ROOT, 'public', 'professor', 'danielle-moreira-aula1.html')
OUT = os.path.join(os.path.dirname(__file__), 'fixtures')

# Cada defeito: (nome do arquivo, funcao que injeta UM defeito, substring que o
# validador DEVE cuspir ao reprovar). O runner exige as duas coisas: exit != 0 E
# a substring presente. Assim o canario nao aceita um FAIL por motivo ERRADO.
def defeito_pergunta_escondida(html):
    # devolve o display:none que o retrofit removeu do listening
    return re.sub(
        r'(<div class="comp-questions"[^>]*style=")',
        r'\1display:none;',
        html, count=1)

def defeito_sentence_sem_css(html):
    # remove o estilo-base do .oral-item (o card do Sentence Building)
    return re.sub(
        r'\.oral-item\s*\{[^}]*\}',
        '.oral-item{cursor:pointer}',   # sobra sem background/border/padding
        html, count=1)

def defeito_gabarito_no_reveal(html):
    # faz TODA regra .oral-model que esconde (display:none) passar a mostrar
    # (display:block) — o gabarito vaza. Precisa pegar TODAS: o arquivo tem varias
    # regras .oral-model (uma crua e a real com margin/font/etc.), e o gate so
    # dispara se NENHUMA esconder. Virar so uma deixa o gate achar display:none na
    # outra e nao reprovar.
    return re.sub(
        r'(\.oral-model\b[^{]*\{[^}]*?display\s*:\s*)none',
        r'\1block',
        html)

DEFEITOS = [
    ('pergunta-escondida.html', defeito_pergunta_escondida, 'PERGUNTA ESCONDIDA'),
    ('sentence-sem-css.html',   defeito_sentence_sem_css,   'SEM ESTILO-BASE'),
    ('gabarito-vazado.html',    defeito_gabarito_no_reveal, 'VAZA o gabarito'),
]


def main():
    if not os.path.exists(BASE):
        print(f'FALHA: base {BASE} nao existe', file=sys.stderr)
        sys.exit(2)
    html = open(BASE, encoding='utf-8').read()
    os.makedirs(OUT, exist_ok=True)

    # sanidade: a base tem que ter os alvos, senao a injecao vira no-op silencioso
    alvos = {'comp-questions': 'class="comp-questions"',
             'oral-item CSS': '.oral-item',
             'oral-model': '.oral-model'}
    for nome, marca in alvos.items():
        if marca not in html:
            print(f'FALHA: base sem alvo "{nome}" ({marca}) — fixture invalido', file=sys.stderr)
            sys.exit(2)

    manifest = []
    for arquivo, fn, esperado in DEFEITOS:
        corrompido = fn(html)
        if corrompido == html:
            print(f'FALHA: injecao de {arquivo} NAO mudou nada (regex obsoleto?)', file=sys.stderr)
            sys.exit(2)
        destino = os.path.join(OUT, arquivo)
        with open(destino, 'w', encoding='utf-8') as f:
            f.write(corrompido)
        manifest.append(f'{arquivo}\t{esperado}')
        print(f'  gerado {arquivo}  (deve reprovar com: "{esperado}")')

    with open(os.path.join(OUT, 'MANIFEST.tsv'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(manifest) + '\n')
    print(f'\n{len(DEFEITOS)} fixtures + MANIFEST.tsv em {OUT}')


if __name__ == '__main__':
    main()
