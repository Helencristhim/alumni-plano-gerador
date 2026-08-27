#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 24 — o syllabus do ciclo: dez campos por aula, e o declarado bate com o gerado.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
Duas falhas medidas no mesmo dia, no molde guided-discovery:

  1. A aba "Syllabus 20 aulas" do hub tinha 135 bytes — a frase de esqueleto do shell.
     ZERO aula. E a falha 2.4 da instrucao corretiva na forma extrema: a interface
     anunciava 20 e apresentava nenhuma.
  2. `estado.json -> mecanicas_gastas` estava VAZIO depois de quatro aulas geradas, e
     nada no repo escrevia nele. O docx §5 pede um estado acumulativo e diz por que: "o
     gerador nao deve depender de memoria narrativa presumida". Sem isso, a regra "nao
     repetir a mesma combinacao dentro do bloco" (03 §4.2) so existia como intencao.

O QUE ELE COBRA
---------------
  (a) o syllabus tem tantas aulas quanto declara (`aulas_do_ciclo`), numeradas 1..N;
  (b) CADA aula preenche os DEZ campos do docx §3.1 e a ficha `spec` do prompt
      controlador (04 §3) — inclusive as provisorias. Provisorio nao autoriza campo
      vazio: um syllabus provisorio E a intencao contra a qual o checkpoint decide;
  (c) cada mecanica declara os CINCO subcampos que o 03 §4.2 exige (mecanica, funcao,
      operacao cognitiva, controle, evidencia), com o controle dentro dos tres graus
      do §4.1;
  (d) o cruzamento com `estado.json`: nenhuma mecanica MEDIDA na aula gerada sem
      declaracao no syllabus, nenhuma DECLARADA que a aula nao usa (salvo as marcadas
      `sem_widget`, que acontecem na conducao e nao num componente);
  (e) a aula listada como `produzida` tem arquivo em public/professor/, e o que tem
      arquivo esta listado. Aula que existe e nao esta no syllabus e aula fora do plano.

ESCOPO — sequencia, por marcador
--------------------------------
So o aluno que TEM `_build/{slug}/syllabus.json`. O eixo CICLO (20 aulas, 5 blocos,
checkpoint na 4) e do programa Private Black Adults; um aluno de pacote antigo nao tem
ciclo declarado e nao e medido por aqui.

USO:
    python3 scripts/check_syllabus_ciclo.py                 # todo aluno com syllabus.json
    python3 scripts/check_syllabus_ciclo.py stephanie-vicente
    python3 scripts/check_syllabus_ciclo.py --selftest      # prova que morde
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMPOS = ['bloco', 'framework', 'posicao_na_rotacao', 'titulo', 'objetivo_comunicativo',
          'relacao_com_o_perfil', 'operacao_nova', 'input', 'linguagem', 'microciclo',
          'produto', 'criterios_de_sucesso', 'evidencia_a_registrar', 'mecanicas',
          'avaliacao', 'spec']
SPEC = ['necessidade', 'framework_justificativa', 'origem', 'conteudo_recuperado',
        'conteudo_excluido', 'retask']
MICRO = ['evidencia_inicial', 'operacao_cognitiva', 'formulacao_hipotese',
         'verificacao_pratica', 'clarificacao_didatica', 'aplicacao_real']
MEC = ['mecanica', 'funcao', 'operacao', 'controle', 'evidencia']
CONTROLES = ('controlado', 'semiaberto', 'aberto')


def verifica(slugs=None):
    fails, checados = [], 0
    padrao = os.path.join(RAIZ, '_build', '*', 'syllabus.json')
    for p in sorted(glob.glob(padrao)):
        slug = os.path.basename(os.path.dirname(p))
        if slugs and slug not in slugs:
            continue
        checados += 1
        with open(p, encoding='utf-8') as fh:
            d = json.load(fh)
        rel = os.path.relpath(p, RAIZ)
        aulas = d.get('aulas', [])
        alvo = d.get('aulas_do_ciclo')

        # (a)
        if alvo and len(aulas) != alvo:
            fails.append(f'{rel}: declara aulas_do_ciclo={alvo} e traz {len(aulas)} aula(s).')
        ns = [a.get('n') for a in aulas]
        # A numeracao do ciclo NAO comeca sempre em 1. Aluno que vem de outro material
        # continua a contagem dele: o ciclo 1 do consultivo do Luiz vai da aula 9 a 28,
        # porque ele fez oito no molde anterior e a Instrucao Operacional §3.2 e explicita
        # -- novo ciclo nao transforma aluno vigente em aluno novo. O gate exigia 1..N e
        # transformava essa decisao em erro.
        inicio = int(d.get('primeira', 1))
        if ns != list(range(inicio, inicio + len(aulas))):
            fails.append(f'{rel}: numeracao das aulas fora de '
                         f'{inicio}..{inicio + len(aulas) - 1}: {ns}')

        for a in aulas:
            n = a.get('n')
            # (b)
            for c in CAMPOS:
                if not a.get(c):
                    fails.append(f'{rel}: aula {n} sem o campo "{c}" (docx §3.1 / 04 §3). '
                                 f'Provisorio nao autoriza campo vazio.')
            for c in MICRO:
                if not (a.get('microciclo') or {}).get(c):
                    fails.append(f'{rel}: aula {n}, microciclo sem "{c}" — as seis operacoes '
                                 f'do guided discovery sao o campo 6 do §3.1.')
            for c in SPEC:
                if not (a.get('spec') or {}).get(c):
                    fails.append(f'{rel}: aula {n}, ficha de especificacao sem "{c}" '
                                 f'(prompt controlador, fase 1).')
            # (c)
            for m in a.get('mecanicas', []):
                for c in MEC:
                    if not m.get(c):
                        fails.append(f'{rel}: aula {n}, mecanica {m.get("mecanica","?")!r} sem '
                                     f'"{c}". O 03 §4.2 exige os cinco: mecanica, funcao, '
                                     f'operacao cognitiva, controle e evidencia.')
                if m.get('controle') and m['controle'] not in CONTROLES:
                    fails.append(f'{rel}: aula {n}, mecanica {m["mecanica"]!r} com controle '
                                 f'{m["controle"]!r} — o §4.1 tem tres graus: '
                                 f'{", ".join(CONTROLES)}.')

        # (d) cruzamento com o estado acumulativo
        est_p = os.path.join(os.path.dirname(p), 'estado.json')
        if os.path.exists(est_p):
            with open(est_p, encoding='utf-8') as fh:
                est = json.load(fh)
            for m in est.get('mecanicas_gastas', []):
                if m.get('sem_declaracao'):
                    fails.append(
                        f'{rel}: a aula {m["aula"]} USA {m["mecanica"]!r} ({m.get("kinds")}) e o '
                        f'syllabus nao a declara. Mecanica que ninguem registrou nao entra na '
                        f'conta da repeticao do bloco seguinte.')
                if m.get('nao_usada'):
                    fails.append(
                        f'{rel}: o syllabus declara {m["mecanica"]!r} na aula {m["aula"]} e a '
                        f'aula nao a usa. Se ela acontece na conducao e nao em componente, '
                        f'marque "sem_widget": true.')

        # (e) produzidas x arquivos no disco
        decl = set(d.get('produzidas', []))
        # A anatomia consultivo nao tem um arquivo por aula: entrega DUAS URLs, e as aulas
        # do ciclo vivem DENTRO do arquivo do professor, marcadas por data-lesson. E ela nao
        # mora so em `{slug}.html`: enquanto o aluno continua tendo aula no material antigo,
        # o ciclo novo nasce ao lado, em `{slug}-c{N}.html` (a `fase: "piloto"` do builder).
        #
        # QUANDO EXISTE MATERIAL CONSULTIVO, os `{slug}-aulaN.html` NAO contam. Eles sao da
        # outra anatomia -- o material antigo do aluno, que continua no ar e nunca estara no
        # syllabus deste ciclo. Contando os dois juntos, o gate acusava o syllabus do Luiz de
        # ter doze aulas "geradas fora do plano", e as doze eram as aulas antigas dele.
        consultivo = []
        for cand in ([os.path.join(RAIZ, 'public', 'professor', f'{slug}.html')]
                     + sorted(glob.glob(os.path.join(RAIZ, 'public', 'professor',
                                                     f'{slug}-c*.html')))):
            if not os.path.exists(cand):
                continue
            with open(cand, encoding='utf-8', errors='replace') as fh:
                conteudo = fh.read()
            if 'content="consultivo"' in conteudo[:4000]:
                consultivo.append(conteudo)

        no_disco = set()
        if consultivo:
            for conteudo in consultivo:
                no_disco |= {int(x) for x in re.findall(r'data-lesson="(\d+)"', conteudo)}
        else:
            for f in glob.glob(os.path.join(RAIZ, 'public', 'professor',
                                            f'{slug}-aula*.html')):
                m = re.search(r'-aula(\d+)\.html$', f)
                if m:
                    no_disco.add(int(m.group(1)))
        if decl - no_disco:
            fails.append(f'{rel}: aula(s) {sorted(decl - no_disco)} listada(s) como produzida(s) '
                         f'e sem arquivo em public/professor/.')
        if no_disco - decl:
            fails.append(f'{rel}: aula(s) {sorted(no_disco - decl)} existe(m) em '
                         f'public/professor/ e nao esta(o) em "produzidas". Aula gerada fora do '
                         f'syllabus e aula fora do plano.')
    return fails, checados


def selftest():
    import copy
    import tempfile
    base = {
        'aulas_do_ciclo': 1, 'produzidas': [],
        'aulas': [dict(n=1, bloco='1', framework='reading-into-speaking',
                       posicao_na_rotacao='1 de 4', titulo='T', objetivo_comunicativo='O',
                       relacao_com_o_perfil='R', operacao_nova='N',
                       input={'material': 'M', 'autenticidade': 'A'}, linguagem='L',
                       microciclo={k: 'x' for k in MICRO}, produto='P',
                       criterios_de_sucesso=['c'], evidencia_a_registrar=['e'],
                       mecanicas=[{'mecanica': 'Sorting', 'funcao': 'f', 'operacao': 'o',
                                   'controle': 'controlado', 'evidencia': 'ev'}],
                       avaliacao='A', spec={k: 'x' for k in SPEC})]}

    def caso(rotulo, muda, deve_falhar):
        d = copy.deepcopy(base)
        muda(d)
        tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmp, '_build', 'zz-mock'), exist_ok=True)
        with open(os.path.join(tmp, '_build', 'zz-mock', 'syllabus.json'), 'w',
                  encoding='utf-8') as fh:
            json.dump(d, fh)
        global RAIZ
        velho, RAIZ = RAIZ, tmp
        try:
            fails, _ = verifica()
        finally:
            RAIZ = velho
        ok = bool(fails) == deve_falhar
        print(f"  {'OK  ' if ok else 'FALHA'}  {rotulo}")
        return not ok

    falhou = False
    falhou |= caso('syllabus completo', lambda d: None, False)
    falhou |= caso('campo do §3.1 vazio',
                   lambda d: d['aulas'][0].__setitem__('operacao_nova', ''), True)
    falhou |= caso('ficha sem retask',
                   lambda d: d['aulas'][0]['spec'].__setitem__('retask', ''), True)
    falhou |= caso('microciclo incompleto',
                   lambda d: d['aulas'][0]['microciclo'].__setitem__('aplicacao_real', ''), True)
    falhou |= caso('mecanica sem controle',
                   lambda d: d['aulas'][0]['mecanicas'][0].__setitem__('controle', ''), True)
    falhou |= caso('grau de controle inventado',
                   lambda d: d['aulas'][0]['mecanicas'][0].__setitem__('controle', 'medio'), True)
    falhou |= caso('conta de aulas nao bate',
                   lambda d: d.__setitem__('aulas_do_ciclo', 20), True)
    falhou |= caso('produzida sem arquivo',
                   lambda d: d.__setitem__('produzidas', [1]), True)
    if falhou:
        print('\nSELFTEST FALHOU — o gate parou de morder.')
        return 1
    print('\nSELFTEST OK — os 8 casos.')
    return 0


def main():
    if '--selftest' in sys.argv:
        return selftest()
    slugs = [a for a in sys.argv[1:] if not a.startswith('--')] or None
    fails, checados = verifica(slugs)
    for f in fails:
        print(f'  FAIL  {f}')
    if fails:
        print(f'\n{len(fails)} problema(s) em {checados} syllabus de ciclo.')
        return 1
    print(f'OK — {checados} syllabus de ciclo: dez campos por aula, ficha de especificacao '
          f'completa, mecanicas declaradas e batendo com o que a aula gastou.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
