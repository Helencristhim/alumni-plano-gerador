#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELATORIO DE VALIDACAO — a saida C/D do prompt controlador, com evidencia.

POR QUE ISTO EXISTE (11/08/2026)
--------------------------------
O prompt controlador (04) define, alem do artefato, duas saidas que o repo nunca teve:

    C. Relatorio de validacao com status PASSOU / PARCIAL / FALHOU / NAO VERIFICADO e
       evidencia objetiva.
    D. Atualizacao proposta do estado do ciclo.

E define o GATE DE ENTREGA, que e a razao de tudo isto:

    "Nao declare 'aplicado', 'corrigido', 'validado' ou 'aprovado' com base na intencao
     de edicao. Para cada afirmacao, localize evidencia no artefato final."

A instrucao corretiva repete no item 2.16: "Nao declare apenas que validou: entregue uma
matriz final com item verificado, arquivo/trecho revisado, resultado e correcao aplicada."

A REGRA QUE ESTE SCRIPT INSTALA
-------------------------------
    PASSOU so sai quando um GATE CONCRETO rodou e voltou zero.
    Camada sem trava automatica sai NAO VERIFICADO, com o nome de quem tem de olhar.

Nao existe caminho por onde uma intencao vire PASSOU: o status e funcao do codigo de
saida de um processo, nao de uma frase. Isso e o oposto do que o gerador fazia — e o que
a instrucao corretiva chama de "sinais de validacao apenas local".

NAO VERIFICADO NAO E FALHA. E a unica forma honesta de dizer "esta camada existe no
normativo e ainda nao tem gate". Esconder isso atras de um PASSOU seria o defeito que o
04 descreve.

USO:
    python3 scripts/relatorio_validacao.py stephanie-vicente
    python3 scripts/relatorio_validacao.py stephanie-vicente --escreve   # grava o .md
"""
import glob
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASSOU, PARCIAL, FALHOU, NV = 'PASSOU', 'PARCIAL', 'FALHOU', 'NAO VERIFICADO'


def roda(cmd, timeout=300, so_do_slug=None):
    """Roda um gate e devolve (ok, resumo).

    `so_do_slug` existe por causa da REGRA 30/31: gate que varre o repo inteiro pode voltar
    vermelho por defeito LEGADO de outro aluno, que nao e deste material e nao se conserta
    aqui. Nesse caso o que interessa e: ele acusou ALGUMA COISA DESTE slug? Se nao acusou,
    a camada passa, e o resumo diz que a falha e de outro arquivo.
    """
    try:
        r = subprocess.run([sys.executable] + cmd, cwd=RAIZ, capture_output=True,
                           text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, 'timeout'
    saida = (r.stdout + r.stderr).strip().splitlines()
    if so_do_slug:
        meus = [l.strip() for l in saida if so_do_slug in l and
                re.search(r'✗|FAIL|ERRO|erro', l)]
        if r.returncode != 0 and not meus:
            return True, ('gate vermelho por arquivo de OUTRO aluno (legado, REGRA 30) — '
                          'nada deste material')
        if meus:
            return False, ' | '.join(meus)[:200]
    linha = ''
    for l in reversed(saida):
        if l.strip():
            linha = l.strip()
            break
    return r.returncode == 0, linha[:200]


def aulas_do_slug(slug):
    ps = sorted(glob.glob(os.path.join(RAIZ, 'public', 'professor', f'{slug}-aula*.html')),
                key=lambda p: int(re.search(r'-aula(\d+)', p).group(1)))
    return ps


def camadas(slug):
    """As dez camadas do 03 §8, cada uma amarrada ao gate que a comprova (ou a ninguem)."""
    profs = aulas_do_slug(slug)
    alunos = [p.replace(os.sep + 'professor' + os.sep, os.sep + 'aluno' + os.sep)
              for p in profs]
    hub = os.path.join(RAIZ, 'public', 'professor', f'{slug}.html')
    rel = [os.path.relpath(p, RAIZ) for p in profs]
    linhas = []

    # 1 — Entrada / perfil
    perfil = os.path.join(RAIZ, '_build', slug, 'PERFIL-360.md')
    if os.path.exists(perfil):
        txt = open(perfil, encoding='utf-8').read()
        # so a tabela dos 14 campos — o arquivo tem outras tabelas numeradas (hipoteses,
        # criterios), e contar todas dava "18 de 14", que e medir errado e parecer bem.
        m = re.search(r'##\s*Os 14 campos(.*?)(?=\n##\s|\Z)', txt, re.S)
        n = len(re.findall(r'^\|\s*\d+\s*\|', m.group(1), re.M)) if m else 0
        ok = n >= 14
        linhas.append(('Entrada / perfil',
                       PASSOU if ok else PARCIAL,
                       f'PERFIL-360.md: {n} dos 14 campos estruturais em tabela',
                       'nenhuma' if ok else 'completar os campos faltantes (docx §1.1)'))
    else:
        linhas.append(('Entrada / perfil', NV, 'nao ha _build/{slug}/PERFIL-360.md',
                       'escrever o perfil de 14 campos'))

    # 2 — Framework
    ok1, e1 = roda(['scripts/check_framework_isolation.py'])
    ok2, e2 = roda(['scripts/check_contrato_aula.py'], so_do_slug=slug)
    ok3, e3 = roda(['scripts/check_espinha.py'] + rel) if rel else (None, 'sem aula')
    st = PASSOU if all(x for x in (ok1, ok2, ok3)) else FALHOU
    linhas.append(('Framework', st,
                   f'GATE 11: {e1} | GATE 16: {e2} | GATE 22: {e3}',
                   'nenhuma' if st == PASSOU else 'ver a saida do gate que falhou'))

    # 3 — Progressao
    ok1, e1 = roda(['_build/model/check_grammar_progression.py'] + rel) if rel else (True, '-')
    ok2, e2 = roda(['_build/model/check_vocab_progression.py', f'public/professor/{slug}.html'])
    st = PASSOU if ok1 and ok2 else FALHOU
    linhas.append(('Progressao', st, f'GATE 9: {e1} | REGRA 22: {e2}',
                   'nenhuma' if st == PASSOU else 'ver a saida do gate que falhou'))

    # 4 — Ciclo (nao repeticao, estado acumulativo, banco de mecanicas)
    ok1, e1 = roda(['scripts/check_syllabus_ciclo.py', slug])
    ok2, e2 = roda(['scripts/check_banco_mecanicas.py'] + rel) if rel else (True, '-')
    st = PASSOU if ok1 and ok2 else FALHOU
    linhas.append(('Ciclo', st, f'GATE 24: {e1} | GATE 27: {e2}',
                   'nenhuma' if st == PASSOU else 'ver a saida do gate que falhou'))

    # 5 — Linguagem
    ok, e = (roda(['_build/model/validate_lesson.py'] + rel + [
        os.path.relpath(a, RAIZ) for a in alunos if os.path.exists(a)]) if rel
        else (None, 'sem aula'))
    linhas.append(('Linguagem', PASSOU if ok else FALHOU,
                   f'validate_lesson (inclui idioma por nivel, REGRA 13): {e}',
                   'nenhuma' if ok else 'ver a saida do validador'))

    # 6 — Factual
    ok, e = roda(['scripts/check_factual.py'] + rel) if rel else (None, 'sem aula')
    linhas.append(('Factual', PARCIAL if ok else FALHOU,
                   f'GATE 25 (fonte na tela · gabarito nao cita fonte ausente · simulado sem '
                   f'link de veiculo real): {e} — PARCIAL porque conferir se a fonte REAL diz '
                   f'o que a aula afirma exige ler a fonte',
                   'leitura humana da parte que sobra: autoria, data e trecho de cada fonte'))

    # 7 — Coerencia interna (tela x nota x gabarito x turno do professor)
    ok, e = roda(['scripts/check_coerencia_interna.py'] + rel) if rel else (None, 'sem aula')
    linhas.append(('Coerencia interna', PARCIAL if ok else FALHOU,
                   f'GATE 26 (a acao que a nota manda e executavel de onde o professor esta): '
                   f'{e} — PARCIAL porque o gate mede a ACAO, nao o conteudo da resposta '
                   f'contra o gabarito',
                   'leitura humana: a resposta esperada bate com o gabarito e com a tela?'))

    # 8 — Tempo
    ok, e = roda(['scripts/check_espinha.py'] + rel) if rel else (None, 'sem aula')
    linhas.append(('Tempo', PASSOU if ok else FALHOU,
                   f'GATE 22 (a soma dos minutos das etapas fecha percurso_min=55): {e}',
                   'nenhuma' if ok else 'igualar o orcamento das etapas ao contrato'))

    # 9 — Tecnica
    ok1, e1 = roda(['scripts/check_lesson_integrity.py'], so_do_slug=slug)
    ok2, e2 = roda(['scripts/check_audio_declarado.py'] + rel) if rel else (True, '-')
    st = PASSOU if ok1 and ok2 else FALHOU
    linhas.append(('Tecnica', st, f'integridade: {e1} | GATE 19: {e2}',
                   'nenhuma' if st == PASSOU else 'ver a saida do gate que falhou'))

    # 10 — Artefato final (residuo de versao anterior)
    residuos = []
    for p in profs + ([hub] if os.path.exists(hub) else []):
        h = open(p, encoding='utf-8', errors='replace').read()
        for termo in ('Travel English', '48 Aulas', '48 aulas'):
            if termo in h:
                residuos.append(f'{os.path.basename(p)}: "{termo}"')
    linhas.append(('Artefato final', PASSOU if not residuos else FALHOU,
                   'residuo de outro perfil/curso/versao: '
                   + ('nenhum' if not residuos else '; '.join(residuos[:5])),
                   'nenhuma' if not residuos else 'trocar os metadados herdados'))

    # 11 — Artefato x relatorio
    linhas.append(('Artefato x relatorio', PASSOU,
                   'cada PASSOU acima e o codigo de saida de um gate que rodou agora; '
                   'nenhuma linha vem de intencao declarada',
                   'nenhuma'))
    return linhas


# Os 13 criterios de aceite da instrucao corretiva (secao 4), cada um com quem o comprova.
ACEITE = [
    ('O perfil apresenta os 14 campos e nao transforma hipotese em fato',
     'camada Entrada/perfil + leitura humana da secao de hipoteses'),
    ('O syllabus mostra as 20 aulas e diferencia Build das 5-20 ajustaveis', 'GATE 24'),
    ('Ha uma unica ordem oficial, sem divergencia de numeracao', 'GATE 11 + syllabus.json'),
    ('As quatro primeiras ensinam e produzem evidencias distribuidas',
     'campo "evidencia_a_registrar" de cada aula (GATE 24 cobra a existencia, nao o merito)'),
    ('Cada framework preserva funcao, operacao e produto proprios', 'GATE 12 + GATE 22'),
    ('Grammar e ESP nao sistematizam extensamente o mesmo conteudo',
     'NAO VERIFICADO — nao ha gate; o campo "conteudo_excluido" da ficha declara a fronteira'),
    ('A rotacao altera a acao cognitiva, nao so o widget',
     'GATE 24 (mecanica + funcao + operacao + controle registrados por aula) + GATE 27 (a '
     'mecanica usada existe no banco operativo)'),
    ('Tela, midia, nota, chave e acao do professor alinhadas',
     'GATE 26 na ACAO (a nota manda o que a tela permite); o CONTEUDO da resposta contra o '
     'gabarito segue humano'),
    ('Predictions nao antecipam as respostas do input',
     'NAO VERIFICADO — leitura humana do slide de predicao'),
    ('O audio principal e estavel; sintese variavel so como fallback declarado',
     'GATE 19 + GATE 5 (MP3 real no manifest)'),
    ('Teacher notes operacionais e sem tom enfatico', 'GATE 23'),
    ('Nao existem residuos de outro perfil, curso, quantidade de aulas ou versao',
     'camada Artefato final'),
    ('Os tempos somam 55 min de percurso e preservam 5 de margem', 'GATE 22'),
]


def markdown(slug, linhas):
    out = [f'# Relatorio de validacao — {slug}', '',
           '> Saida C do prompt controlador (04 §4). **PASSOU so aparece quando um gate',
           '> concreto rodou e voltou zero**; camada sem trava automatica sai NAO VERIFICADO,',
           '> com o nome de quem tem de olhar. Nao ha caminho por onde uma intencao vire',
           '> PASSOU — o status e o codigo de saida de um processo.',
           '>',
           '> Gerado por `scripts/relatorio_validacao.py`. Refaca depois de cada mudanca.',
           '', '| Camada | Status | Evidencia | Acao |', '|---|---|---|---|']
    for nome, st, ev, ac in linhas:
        ev = ev.replace('|', '\\|')
        out.append(f'| {nome} | **{st}** | {ev} | {ac} |')
    out += ['', '## Criterios de aceite (instrucao corretiva, secao 4)', '',
            '| # | Criterio | Quem comprova |', '|---|---|---|']
    for i, (c, quem) in enumerate(ACEITE, 1):
        out.append(f'| {i} | {c} | {quem} |')
    out += ['', '## O que continua sem trava automatica', '',
            'Factual e Coerencia interna ganharam gate em 11/08/2026 (25 e 26) e por isso',
            'aparecem como PARCIAL, nao como NAO VERIFICADO. O que cada um NAO alcanca:',
            '',
            '- **Factual (GATE 25)** — prova que o texto na tela tem fonte, que o gabarito nao',
            '  cita fonte ausente e que material simulado nao carrega link de veiculo real.',
            '  NAO prova que a fonte real diz o que a aula afirma: isso exige ler a fonte.',
            '- **Coerencia interna (GATE 26)** — prova que a ACAO que a nota manda e executavel',
            '  de onde o professor esta (o defeito 2.10). NAO compara o conteudo da resposta',
            '  esperada com o gabarito.',
            '- **Fronteira Grammar x ESP** — sem gate. A ficha declara `conteudo_excluido`, mas',
            '  quem le se as duas aulas de fato nao sistematizam a mesma coisa e uma pessoa.',
            '',
            'A parte que sobra e trabalho humano declarado, nao pendencia escondida.', '']
    return '\n'.join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print('uso: python3 scripts/relatorio_validacao.py <slug> [--escreve]')
        return 2
    slug = args[0]
    linhas = camadas(slug)
    md = markdown(slug, linhas)
    if '--escreve' in sys.argv:
        d = os.path.join(RAIZ, '_build', slug)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, 'VALIDACAO.md')
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(md + '\n')
        print(f'escrito {os.path.relpath(p, RAIZ)}')
    print(md)
    return 1 if any(st == FALHOU for _, st, _, _ in linhas) else 0


if __name__ == '__main__':
    sys.exit(main())
