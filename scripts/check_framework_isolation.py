#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 11 — ISOLAMENTO DE FRAMEWORK.

Ordem do Dan (27/07/2026):

    "nao quero que NADA DE ALUNOS JA ATUAIS utilize os frameworks que vamos inserir
     agora [...] gerar alunos mock, validar, pra so depois implementar"

Este gate e o que transforma essa ordem de INTENCAO em IMPOSSIBILIDADE. Sem ele,
basta alguem (ou um agente distraido) trocar uma linha de config pra um aluno real
receber uma aula de framework experimental — e ninguem ve ate a aula estar no ar.

COMO FUNCIONA
-------------
Toda aula nascida do builder carrega a etiqueta:

    <meta name="alumni-model"     content="adulto|kids|teens">   (categoria, ja existia)
    <meta name="alumni-framework" content="imersivo-prototipo">  (framework, novo)

A fonte da verdade e `public/data/frameworks.json` — quais frameworks existem em
cada categoria, e a lista `mocks` de quais slugs podem receber framework que ainda
nao e de producao.

REGRAS (as tres, todas bloqueantes)
-----------------------------------
1. FRAMEWORK DESCONHECIDO — a etiqueta declara um framework que nao existe no JSON
   daquela categoria. Erro de digitacao ou framework que ninguem cadastrou.
2. FRAMEWORK EXPERIMENTAL EM ALUNO REAL — framework com status != "producao" num
   slug que NAO esta em `mocks`. E a regra que o Dan pediu.
3. TROCA NAO DECLARADA — o mesmo aluno com aulas de frameworks diferentes SEM uma
   migracao escrita em `migracoes`.

   Esta regra nasceu como "um aluno nunca mistura frameworks" e foi CORRIGIDA pelo Dan
   em 27/07/2026: proibir a troca impedia tambem a troca INTENCIONAL (migrar um aluno
   do Imersivo para outro metodo a partir da aula N), que e um caso legitimo. O que
   precisa ser barrado nao e a troca — e a troca ACIDENTAL, do tipo "alguem mexeu no
   config e ninguem viu".

   Entao: a troca passa quando esta DECLARADA, e o gate ainda confere que as aulas
   respeitam o corte declarado (antes da aula N = framework "de"; da N em diante =
   framework "para"). Declarar sem cumprir tambem e erro.

4. PACOTE INCONSISTENTE — aulas do mesmo aluno declarando `TOTAL_AULAS` diferentes.

   Esta e a garantia FINANCEIRA (pedido do Dan, 27/07/2026): trocar de framework nao
   pode mexer no progresso do pacote que o aluno comprou. A barra do header e
   `aulas concluidas / TOTAL_AULAS` — se duas aulas do mesmo aluno declaram totais
   diferentes, ele ve percentuais diferentes conforme a aula que abrir.

   O progresso em si e IMUNE ao framework por construcao: `lesson_progress` grava
   (student_slug, lesson_number, inclass_done) — nao ha coluna de framework nem de
   estrutura. A aula 13 conta como a 13a do pacote tenha ela nascido em qualquer
   metodo. O que precisa ser vigiado e o DENOMINADOR, e e o que esta regra faz.

   Medicao de 27/07/2026: 9 alunos JA tem esse defeito no legado (nilo 40 vs 96,
   simone 12 vs 48, natalie 5/6/26...) — anterior a tudo isto e sem relacao com
   framework. Por isso a regra so olha aulas ETIQUETADAS: nasce em 0 e nao cobra
   retrofit de ninguem (REGRA 30).

LEGADO-TOLERANTE (REGRA 30/31)
------------------------------
Aula SEM a etiqueta `alumni-framework` e IGNORADA. As ~1.240 aulas anteriores a este
gate nao tem a etiqueta e NAO serao tocadas pra ganhar uma: elas ja sao identificaveis
pela estrutura (7 capitulos) e "aula que ja foi dada nao se mexe".

  Excecao conhecida e registrada: `sandra-hayasaki-aula5` foi refeita em PPP antes
  desta conversa. Sem etiqueta => o gate nao a ve. Isso e proposital — ela e legado,
  nao um caso novo. Esta documentada em _build/model/FRAMEWORKS.md.

USO
---
    python3 scripts/check_framework_isolation.py              # repo inteiro
    python3 scripts/check_framework_isolation.py A.html B.html  # so estes
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, 'public', 'data', 'frameworks.json')
DEFAULT = 'imersivo-prototipo'

RE_FW = re.compile(r'<meta name="alumni-framework" content="([^"]*)"')
RE_CAT = re.compile(r'<meta name="alumni-model" content="([^"]*)"')
RE_SLUG = re.compile(r'^(.*?)(?:-aula\d+)?\.html$')
RE_AULA = re.compile(r'-aula(\d+)\.html$')
RE_TOTAL = re.compile(r'TOTAL_AULAS\s*=\s*(\d+)')


def carrega_catalogo():
    with open(JSON_PATH, encoding='utf-8') as f:
        data = json.load(f)
    por_categoria = {}
    status = {}
    for cat in data['categorias']:
        por_categoria[cat['id']] = {fw['id'] for fw in cat['frameworks']}
        for fw in cat['frameworks']:
            # Se o mesmo framework aparece em 2 categorias com status diferente,
            # vale o MAIS restritivo (basta nao ser producao em uma pra exigir mock).
            if status.get(fw['id']) != 'nao-producao':
                status[fw['id']] = 'producao' if fw['status'] == 'producao' else 'nao-producao'
    mocks = {k: set(v) for k, v in data.get('mocks', {}).items()}
    migracoes = {m['slug']: m for m in data.get('migracoes', [])}
    return por_categoria, status, mocks, migracoes


def arquivos_alvo(argv):
    if argv:
        return [a for a in argv if a.endswith('.html')]
    out = []
    for sub in ('professor', 'aluno'):
        d = os.path.join(ROOT, 'public', sub)
        if not os.path.isdir(d):
            continue
        for nome in os.listdir(d):
            if nome.endswith('.html'):
                out.append(os.path.join(d, nome))
    return out


def main():
    por_categoria, status, mocks, migracoes = carrega_catalogo()
    erros = []
    # slug -> {framework: [arquivos]}  (so entra quem TEM etiqueta)
    por_slug = defaultdict(lambda: defaultdict(list))
    # slug -> {numero_da_aula: framework}   e   slug -> {total_aulas: [arquivos]}
    aula_fw = defaultdict(dict)
    totais = defaultdict(lambda: defaultdict(list))
    vistos = 0

    for caminho in arquivos_alvo(sys.argv[1:]):
        try:
            with open(caminho, encoding='utf-8') as f:
                html = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        m = RE_FW.search(html)
        if not m:
            continue  # legado / sem etiqueta => ignorado de proposito
        vistos += 1
        fw = m.group(1).strip()
        cat = (RE_CAT.search(html).group(1).strip() if RE_CAT.search(html) else 'adulto')
        rel = os.path.relpath(caminho, ROOT)
        base = os.path.basename(caminho)
        slug = RE_SLUG.match(base).group(1)
        por_slug[slug][fw].append(rel)
        n_aula = RE_AULA.search(base)
        if n_aula:
            aula_fw[slug][int(n_aula.group(1))] = fw
        t = RE_TOTAL.search(html)
        if t:
            totais[slug][int(t.group(1))].append(rel)

        # REGRA 1 — framework existe nesta categoria?
        conhecidos = por_categoria.get(cat)
        if conhecidos is None:
            erros.append(f'{rel}: categoria "{cat}" nao existe em frameworks.json')
        elif fw not in conhecidos:
            erros.append(
                f'{rel}: framework "{fw}" nao esta cadastrado na categoria "{cat}". '
                f'Cadastre em public/data/frameworks.json ou corrija a etiqueta.')

        # REGRA 2 — experimental so em mock
        if status.get(fw) == 'nao-producao' and slug not in mocks.get(fw, set()):
            erros.append(
                f'{rel}: framework "{fw}" NAO e de producao e o slug "{slug}" nao esta '
                f'na lista mocks["{fw}"] de frameworks.json. Aluno real nao recebe '
                f'framework em validacao (ordem do Dan, 27/07/2026).')

    # REGRA 3 — troca de framework só passa se estiver DECLARADA e for cumprida.
    #
    # Os dois lados são checados SEPARADAMENTE, e de propósito:
    #   (a) mais de um framework sem declaração  -> troca acidental;
    #   (b) declaração existe -> o corte TEM de ser cumprido, mesmo que o aluno acabe com
    #       um framework só. Sem (b) havia um buraco: migrando TODAS as aulas (inclusive as
    #       anteriores ao corte), o slug volta a ter um único framework, a checagem de
    #       mistura não dispara, e a declaração passa a dizer uma coisa enquanto os
    #       arquivos fazem outra. Pego em teste, 27/07/2026.
    for slug, fws in por_slug.items():
        mig = migracoes.get(slug)
        if not mig:
            if len(fws) > 1:
                detalhe = ' vs '.join(f'{k} ({len(v)} aula(s))' for k, v in sorted(fws.items()))
                erros.append(
                    f'{slug}: aulas de frameworks DIFERENTES sem migração declarada -> '
                    f'{detalhe}. Se a troca é intencional, declare em migracoes[] de '
                    f'frameworks.json ({{"slug","de","para","a_partir_da_aula"}}); se não é, '
                    f'alguém trocou o framework deste aluno por engano.')
            continue
        corte, de, para = mig.get('a_partir_da_aula'), mig.get('de'), mig.get('para')
        if not (corte and de and para):
            erros.append(f'{slug}: migração declarada incompleta — exige "de", "para" e '
                         f'"a_partir_da_aula".')
            continue
        fora = {fw for fw in fws if fw not in (de, para)}
        if fora:
            erros.append(f'{slug}: migração declara {de} -> {para}, mas há aula em '
                         f'{sorted(fora)}.')
        for n, fw in sorted(aula_fw[slug].items()):
            esperado = de if n < corte else para
            if fw != esperado:
                erros.append(
                    f'{slug}-aula{n}: framework "{fw}" contraria a migração declarada '
                    f'({de} até a aula {corte - 1}, {para} da {corte} em diante).')

    # REGRA 4 — o pacote do aluno tem UM tamanho só (garantia financeira)
    for slug, vals in totais.items():
        if len(vals) > 1:
            detalhe = ' vs '.join(
                f'{n} (em {os.path.basename(v[0])}{"..." if len(v) > 1 else ""})'
                for n, v in sorted(vals.items()))
            erros.append(
                f'{slug}: TOTAL_AULAS divergente entre as aulas -> {detalhe}. A barra do '
                f'pacote é "concluídas / TOTAL_AULAS": com dois valores, o aluno vê '
                f'percentuais diferentes conforme a aula que abrir.')

    print(f'=== GATE 11 — isolamento de framework ===')
    print(f'arquivos com etiqueta: {vistos}  (sem etiqueta = legado, ignorado)')
    if erros:
        print(f'\n❌ {len(erros)} violacao(oes):\n')
        for e in erros:
            print(f'  ✗ {e}')
        return 1
    print('✅ OK — nenhum aluno real com framework experimental.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
