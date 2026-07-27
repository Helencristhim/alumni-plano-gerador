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
3. SLUG MISTURADO — o mesmo aluno com aulas de frameworks diferentes. Um aluno segue
   UM metodo; misturar no meio do curso confunde o aluno e a professora.

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
    return por_categoria, status, mocks


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
    por_categoria, status, mocks = carrega_catalogo()
    erros = []
    # slug -> {framework: [arquivos]}  (so entra quem TEM etiqueta)
    por_slug = defaultdict(lambda: defaultdict(list))
    vistos = 0

    for caminho in arquivos_alvo(sys.argv[1:]):
        try:
            with open(caminho, encoding='utf-8') as f:
                html = f.read(8192)  # a etiqueta vive no <head>
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

    # REGRA 3 — slug com mais de um framework
    for slug, fws in por_slug.items():
        if len(fws) > 1:
            detalhe = ' vs '.join(f'{k} ({len(v)} aula(s))' for k, v in sorted(fws.items()))
            erros.append(f'{slug}: aulas de frameworks DIFERENTES no mesmo aluno -> {detalhe}')

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
