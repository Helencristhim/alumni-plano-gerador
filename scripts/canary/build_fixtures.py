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
import importlib.util
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def _load_builder():
    """Importa build_from_model para reusar a FUNÇÃO REAL que emite data-grammar.
    Assim o fixture de gramática prova builder+gate juntos: se alguém quebrar
    inject_grammar_marker, o fixture nasce sem marcador e o sanity-check abaixo grita."""
    spec = importlib.util.spec_from_file_location(
        'build_from_model', os.path.join(ROOT, '_build', 'model', 'build_from_model.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
# Aula STANDALONE (slides IN CLASS): base dos fixtures de slide.
BASE = os.path.join(ROOT, 'public', 'professor', 'danielle-moreira-aula1.html')
# HUB (Pre-class com match-row): base do fixture de idioma. O matching do Pre-class
# vive no hub, nao no standalone — por isso o fixture de portugues precisa dele.
BASE_HUB = os.path.join(ROOT, 'public', 'professor', 'danielle-moreira.html')
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

def defeito_tarefa_ausente(html):
    # remove o PRIMEIRO slide de tarefa (data-task-for) — assim um dialogo/leitura
    # fica exposto SEM a tarefa antes. O gate 'TAREFA AUSENTE' tem que pegar.
    return re.sub(
        r'<div class="slide[^"]*"[^>]*data-task-for="[^"]*"[^>]*>.*?</div>\s*(?=<div class="slide)',
        '', html, count=1, flags=re.S)

def defeito_header_portugues(html):
    # devolve "Aula N" ao subtitle e ao <title> (o PT no header que o gate #1316
    # trava). A heuristica de acento NAO pega "Aula" — por isso o gate ancora na
    # estrutura (.subtitle / <title>), e o canario prova que ele ainda ancora.
    h = re.sub(r'(<p class="subtitle"[^>]*>)\s*Lesson(\s+\d)', r'\1Aula\2', html, count=1)
    h = re.sub(r'(<title>[^<]*?)Lesson(\s+\d)', r'\1Aula\2', h, count=1)
    return h

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

# (arquivo, funcao, marca esperada no FAIL, base). base='standalone' (slides) ou 'hub' (Pre-class).
DEFEITOS = [
    ('pergunta-escondida.html', defeito_pergunta_escondida, 'PERGUNTA ESCONDIDA', 'standalone'),
    ('sentence-sem-css.html',   defeito_sentence_sem_css,   'SEM ESTILO-BASE',    'standalone'),
    ('gabarito-vazado.html',    defeito_gabarito_no_reveal, 'VAZA o gabarito',    'standalone'),
    ('header-portugues.html',   defeito_header_portugues,   'HEADER em português', 'standalone'),
    ('tarefa-ausente.html',     defeito_tarefa_ausente,     'TAREFA AUSENTE',     'standalone'),
    # NOTA: o gate de PORTUGUES no Pre-class (A2+) le o HUB (public/professor/{slug}.html),
    # nao o arquivo passado — um fixture renomeado nunca satisfaz esse lookup, entao ele
    # nao vira fixture-arquivo. O canario cobre o CORACAO desse gate (pt_na_tela +
    # nivel_do_html) por asercao unitaria em run.py. E assim que ele morreria.
]


def main():
    for rotulo, caminho in [('standalone', BASE), ('hub', BASE_HUB)]:
        if not os.path.exists(caminho):
            print(f'FALHA: base {rotulo} {caminho} nao existe', file=sys.stderr)
            sys.exit(2)
    html_std = open(BASE, encoding='utf-8').read()
    html_hub = open(BASE_HUB, encoding='utf-8').read()
    os.makedirs(OUT, exist_ok=True)

    # sanidade: cada base tem que ter os alvos, senao a injecao vira no-op silencioso
    for marca in ('class="comp-questions"', '.oral-item', '.oral-model'):
        if marca not in html_std:
            print(f'FALHA: base standalone sem alvo "{marca}" — fixture invalido', file=sys.stderr)
            sys.exit(2)
    if 'match-row' not in html_hub:
        print('FALHA: base hub sem "match-row" — fixture de idioma invalido', file=sys.stderr)
        sys.exit(2)

    manifest = []
    for arquivo, fn, esperado, base in DEFEITOS:
        html = html_hub if base == 'hub' else html_std
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

    build_grammar_fixtures(html_std)


# ── Fixture de GRAMÁTICA (REGRA 22) ──────────────────────────────────────────
# Diferente dos fixtures acima: este NÃO passa pelo validate_lesson.py (que checa
# UM arquivo), e sim pelo check_grammar_progression.py, que compara VÁRIAS aulas do
# MESMO aluno. Por isso o par vive fora do MANIFEST.tsv e o run.py o roda à parte
# (como já faz com o check unitário do gate de idioma). O defeito injetado: DUAS
# aulas do mesmo aluno com o MESMO data-grammar — o gate tem que reprovar.
GRAMMAR_FIXTURES = ('grammar-repetida-aula1.html', 'grammar-repetida-aula2.html')
GRAMMAR_PONTO = 'past perfect'
GRAMMAR_MARCA = 'GRAMÁTICA REPETIDA'


def build_grammar_fixtures(html_std):
    B = _load_builder()
    # usa a FUNÇÃO REAL do builder para plantar o marcador — não um regex paralelo
    corrompido = B.inject_grammar_marker(html_std, GRAMMAR_PONTO)
    if 'data-grammar=' not in corrompido:
        print('FALHA: inject_grammar_marker não emitiu data-grammar — builder quebrado '
              'ou base sem slide de Grammar Discovery. Fixture de gramática inválido.',
              file=sys.stderr)
        sys.exit(2)
    for arquivo in GRAMMAR_FIXTURES:
        with open(os.path.join(OUT, arquivo), 'w', encoding='utf-8') as f:
            f.write(corrompido)
    print(f'  gerado par de gramática {GRAMMAR_FIXTURES[0]} + {GRAMMAR_FIXTURES[1]}  '
          f'(mesmo data-grammar="{GRAMMAR_PONTO}" em 2 aulas — deve reprovar com: '
          f'"{GRAMMAR_MARCA}")')


if __name__ == '__main__':
    main()
