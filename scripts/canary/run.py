#!/usr/bin/env python3
"""
CANARIO DOS GATES — o vigia que nao confia no verde do gate.

    python3 scripts/canary/run.py

Cada fixture em scripts/canary/fixtures/ carrega UM defeito de proposito. O gate
correspondente TEM que reprova-lo. Se o gate PASSAR um fixture, o gate morreu
(pulado, desligado, ou logica quebrada) — e o canario fica VERMELHO, na hora, em
vez de meses depois quando alguem abrir a aula.

Isto e o que faltava em 14/07/2026, quando os GATES 1-7 sairam 'skipped' e o CI
ficou verde sem checar nada. Um gate verde nao prova que o gate funciona. Este
canario prova — a cada PR — que o gate ainda MORDE.

Contrato de cada fixture (MANIFEST.tsv):  <arquivo>\t<substring esperada no FAIL>
O canario exige AS DUAS coisas: exit != 0 (reprovou) E a substring presente
(reprovou pelo MOTIVO CERTO, nao por acidente).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FIXTURES = os.path.join(HERE, 'fixtures')
VALIDATOR = os.path.join(ROOT, '_build', 'model', 'validate_lesson.py')
GRAMMAR_GATE = os.path.join(ROOT, '_build', 'model', 'check_grammar_progression.py')
# Par de fixtures de gramática: 2 aulas do mesmo aluno com o MESMO data-grammar.
GRAMMAR_FIXTURES = ('grammar-repetida-aula1.html', 'grammar-repetida-aula2.html')
GRAMMAR_MARCA = 'GRAMÁTICA REPETIDA'


def carregar_manifest():
    p = os.path.join(FIXTURES, 'MANIFEST.tsv')
    if not os.path.exists(p):
        print('CANARIO QUEBRADO: MANIFEST.tsv nao existe. Rode build_fixtures.py.', file=sys.stderr)
        sys.exit(2)
    itens = []
    for linha in open(p, encoding='utf-8'):
        linha = linha.strip()
        if not linha:
            continue
        arquivo, esperado = linha.split('\t', 1)
        itens.append((arquivo, esperado))
    if not itens:
        print('CANARIO QUEBRADO: MANIFEST vazio.', file=sys.stderr)
        sys.exit(2)
    return itens


def unidade_gate_portugues():
    """O gate de PORTUGUES no Pre-class (A2+) le o HUB, nao o arquivo passado, entao
    nao vira fixture-arquivo limpo. Mas o CORACAO dele sao duas funcoes do validador:
    detectar PT na tela (pt_na_tela) e ler o nivel (nivel_do_html). Se qualquer uma
    for enfraquecida — que e como esse gate morreria em silencio — este check pega.

    Retorna lista de falhas (vazia = coracao do gate vivo).
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'validate_lesson', os.path.join(ROOT, '_build', 'model', 'validate_lesson.py'))
    V = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V)

    falhas = []
    # 1. detecta PT acentuado inequivoco (o defeito que o retrofit tirou)
    if not (hasattr(V, 'pt_na_tela') and V.pt_na_tela('<p>apresentação da rotina</p>')):
        falhas.append('pt_na_tela NAO detecta português acentuado — o gate de idioma esta cego')
    # 2. NAO acusa ingles puro (sem falso positivo — foi o bug do "travel")
    if hasattr(V, 'pt_na_tela') and V.pt_na_tela('<p>travel and available options</p>'):
        falhas.append('pt_na_tela acusa INGLES como português (falso positivo — quebraria aula correta)')
    # 3. le o nivel do header (sem isso o gate bidirecional nao sabe o que cobrar)
    hdr = '<div class="student-info"><span>B2 (x)</span><span>São Paulo</span></div>'
    if not (hasattr(V, 'nivel_do_html') and V.nivel_do_html(hdr) == 'B2'):
        falhas.append('nivel_do_html NAO le o CEFR do header — o gate de idioma nao roda')
    return falhas


def fixture_gate_gramatica():
    """O gate da REGRA 22 para GRAMÁTICA (check_grammar_progression.py) compara VÁRIAS
    aulas do mesmo aluno — não cabe no MANIFEST de arquivo-único rodado pelo
    validate_lesson. Aqui rodamos o gate no par de fixtures (2 aulas, MESMO
    data-grammar) e exigimos as duas coisas: exit != 0 E a marca "GRAMÁTICA REPETIDA"
    (reprovou pelo MOTIVO certo). É assim que esse gate morreria em silêncio — pulado,
    desligado, ou tolerando o legado a ponto de não ver a repetição real.

    Retorna lista de falhas (vazia = gate vivo)."""
    falhas = []
    caminhos = [os.path.join(FIXTURES, f) for f in GRAMMAR_FIXTURES]
    faltando = [f for f, p in zip(GRAMMAR_FIXTURES, caminhos) if not os.path.exists(p)]
    if faltando:
        return [f'fixture(s) de gramática sumiram do disco: {faltando} — rode build_fixtures.py']
    r = subprocess.run([sys.executable, GRAMMAR_GATE, *caminhos],
                       capture_output=True, text=True)
    saida = r.stdout + r.stderr
    if r.returncode == 0:
        falhas.append('gramática: o par com data-grammar REPETIDO PASSOU — '
                      'o gate de "GRAMÁTICA REPETIDA" está DORMINDO')
    elif GRAMMAR_MARCA not in saida:
        falhas.append(f'gramática: reprovou, mas SEM a marca "{GRAMMAR_MARCA}" — '
                      f'o gate-alvo pode estar morto (barrou outra coisa)')
    return falhas


def main():
    itens = carregar_manifest()
    mortos = []   # gates que DEIXARAM PASSAR um defeito = gate dormindo
    print(f'Canario: {len(itens)} fixture(s) + 1 check do gate de idioma + '
          f'1 check do gate de gramática.\n')

    for arquivo, esperado in itens:
        caminho = os.path.join(FIXTURES, arquivo)
        if not os.path.exists(caminho):
            mortos.append(f'{arquivo}: fixture SUMIU do disco')
            print(f'  ✗ {arquivo}: fixture nao existe')
            continue

        r = subprocess.run([sys.executable, VALIDATOR, caminho],
                           capture_output=True, text=True)
        saida = r.stdout + r.stderr
        reprovou = r.returncode != 0
        motivo_certo = esperado in saida

        if reprovou and motivo_certo:
            print(f'  ✓ {arquivo}: reprovado com "{esperado}" — gate VIVO')
        elif reprovou and not motivo_certo:
            # reprovou, mas por OUTRO motivo — o gate-alvo pode estar morto e outra
            # coisa e que barrou. Trata como morte: nao provamos que o gate certo mordeu.
            mortos.append(f'{arquivo}: reprovou, mas SEM a marca "{esperado}" — '
                          f'o gate-alvo pode estar morto (barrou outra coisa)')
            print(f'  ✗ {arquivo}: reprovado por motivo ERRADO (falta "{esperado}")')
        else:
            mortos.append(f'{arquivo}: PASSOU — o gate de "{esperado}" esta DORMINDO')
            print(f'  ✗ {arquivo}: PASSOU no validador — GATE DE "{esperado}" DORMINDO')

    # check unitario do gate de idioma (nao vira fixture-arquivo — ver build_fixtures.py)
    for f in unidade_gate_portugues():
        mortos.append(f'gate de idioma (unitario): {f}')
        print(f'  ✗ idioma: {f}')
    if not any('idioma' in m for m in mortos):
        print('  ✓ idioma: pt_na_tela detecta PT, ignora inglês, lê o nível — coração VIVO')

    # gate de GRAMÁTICA (REGRA 22): compara aulas do mesmo aluno, roda à parte do MANIFEST
    for f in fixture_gate_gramatica():
        mortos.append(f'gate de gramática: {f}')
        print(f'  ✗ gramática: {f}')
    if not any('gramática' in m for m in mortos):
        print(f'  ✓ gramática: par com data-grammar repetido reprovado com '
              f'"{GRAMMAR_MARCA}" — gate VIVO')

    print()
    if mortos:
        print('=== CANARIO VERMELHO — gate(s) dormindo: ===')
        for m in mortos:
            print(f'  - {m}')
        print('\nUm defeito conhecido passou pelo gate. O gate morreu ou foi pulado.')
        print('NAO mergeie ate o gate voltar a reprovar o fixture.')
        sys.exit(1)
    print('=== CANARIO VERDE — todos os gates ainda mordem ===')
    sys.exit(0)


if __name__ == '__main__':
    main()
