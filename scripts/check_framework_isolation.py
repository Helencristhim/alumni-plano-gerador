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

3b. RODIZIO NAO CUMPRIDO — a partir de 30/07/2026 um aluno pode ter os frameworks
   ALTERNANDO por posicao de aula (a nova estrategia do Black adulto: "intercalar a
   rodada de frameworks nas aulas"). Isso e outra TOPOLOGIA, nao um caso particular de
   migracao: migracao tem um corte e dois frameworks; rodizio tem N frameworks e nenhum
   corte. Declara-se em `rodizios` de frameworks.json:

       {"slug": "...", "desde_aula": 1, "ciclo": ["ppp", "communicative", "task-based"]}

   O framework esperado da aula N e ciclo[(N - desde_aula) % len(ciclo)], e o gate
   confere aula a aula — mesma severidade da regra 3. Slug com rodizio E migracao ao
   mesmo tempo e erro: nao ha resposta unica para "qual framework a aula N devia ter".

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
    rodizios = {r['slug']: r for r in data.get('rodizios', [])}
    return por_categoria, status, mocks, migracoes, rodizios


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


def selftest():
    """Prova que o gate MORDE — em especial a regra do rodízio, que é nova (30/07/2026).

    Exercita `checa_sequencia` direto: ela é pura, então o selftest não precisa de disco
    nem de HTML de mentira. Cada caso descreve uma situação real de geração.
    """
    st = {'ppp': 'nao-producao', 'communicative': 'nao-producao',
          'task-based': 'nao-producao', 'imersivo-prototipo': 'producao'}
    ciclo = ['ppp', 'communicative', 'task-based']
    rod = {'ciclo': ciclo, 'desde_aula': 1}
    certo = {1: 'ppp', 2: 'communicative', 3: 'task-based', 4: 'ppp', 5: 'communicative'}
    fws = lambda aulas: {fw: ['x.html'] for fw in set(aulas.values())}

    casos = [
        ('rodízio cumprido (5 aulas, ciclo de 3)', certo, rod, None, 0),
        ('aula 4 saiu em TBL (devia ser PPP)', {**certo, 4: 'task-based'}, rod, None, 1),
        ('aula 2 saiu em imersivo (fora do ciclo)', {**certo, 2: 'imersivo-prototipo'},
         rod, None, 1),
        ('rodízio de 1 framework só (declaração vazia de efeito)',
         {1: 'ppp', 2: 'ppp'}, {'ciclo': ['ppp'], 'desde_aula': 1}, None, 1),
        ('rodízio cita framework que não existe', certo,
         {'ciclo': ['ppp', 'ppppp'], 'desde_aula': 1}, None, 1),
        ('rodízio começa na aula 3 (1 e 2 são de antes)',
         {1: 'imersivo-prototipo', 2: 'imersivo-prototipo', 3: 'ppp', 4: 'communicative'},
         {'ciclo': ciclo, 'desde_aula': 3}, None, 0),
        ('rodízio + migração ao mesmo tempo', certo, rod,
         {'de': 'ppp', 'para': 'communicative', 'a_partir_da_aula': 3}, 1),
        # As regras que já existiam continuam mordendo — o rodízio não pode tê-las afrouxado.
        ('mistura SEM declaração nenhuma', {1: 'ppp', 2: 'communicative'}, None, None, 1),
        ('migração declarada e cumprida',
         {1: 'imersivo-prototipo', 2: 'imersivo-prototipo', 3: 'ppp'}, None,
         {'de': 'imersivo-prototipo', 'para': 'ppp', 'a_partir_da_aula': 3}, 0),
        ('migração declarada e NÃO cumprida',
         {1: 'ppp', 2: 'imersivo-prototipo', 3: 'ppp'}, None,
         {'de': 'imersivo-prototipo', 'para': 'ppp', 'a_partir_da_aula': 3}, 1),
    ]
    ruim = 0
    for nome, aulas, r, mig, esperado in casos:
        n = len(checa_sequencia('selftest', fws(aulas), aulas, mig, r, st))
        ok = (n > 0) == (esperado > 0)
        ruim += not ok
        print(f'  {"OK  " if ok else "FALHOU"} {nome}: {n} erro(s)')
    print('\nselftest: ' + ('✅ o gate morde' if not ruim else f'❌ {ruim} caso(s) errado(s)'))
    return 1 if ruim else 0


def main():
    if '--selftest' in sys.argv:
        return selftest()
    por_categoria, status, mocks, migracoes, rodizios = carrega_catalogo()
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
        erros.extend(checa_sequencia(slug, fws, aula_fw[slug], migracoes.get(slug),
                                     rodizios.get(slug), status))

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


def checa_sequencia(slug, fws, aulas, mig, rod, status):
    """As regras 3 / 3b: o aluno tem os frameworks que ALGUÉM DECLAROU que ele teria.

    `fws`   {framework: [arquivos]} — tudo que este slug tem etiquetado (hub inclusive)
    `aulas` {numero_da_aula: framework} — só arquivos {slug}-aulaN.html
    Função PURA (não lê disco) — é o que o --selftest exercita.
    """
    erros = []
    # RODIZIO — o método ALTERNA por posição de aula, para sempre (pedido do Dan,
    # 30/07/2026). É outra topologia, não um caso particular de migração: migração tem UM
    # corte e dois frameworks; rodízio tem N frameworks e nenhum corte. Espremer rodízio em
    # migracoes[] transformaria a declaração de migração em carta branca ("declarei, agora
    # vale qualquer coisa") — exatamente o buraco que a regra 3 fechou em 27/07.
    #
    # A severidade é a MESMA da regra 3: a pergunta continua sendo "esta aula tem o
    # framework que alguém declarou que ela teria?". Só muda quem responde — a sequência,
    # em vez do corte.
    if rod and mig:
        return [f'{slug}: tem rodízio E migração declarados ao mesmo tempo. São regras '
                f'incompatíveis (uma alterna para sempre, a outra corta uma vez); com as '
                f'duas, não há resposta única para "qual framework a aula N devia ter".']
    if rod:
        ciclo = rod.get('ciclo') or []
        desde = rod.get('desde_aula', 1)
        if len(ciclo) < 2:
            return [f'{slug}: rodízio declarado com ciclo de {len(ciclo)} framework(s) — '
                    f'rodízio exige pelo menos 2 (com um só é o framework do aluno, e a '
                    f'declaração não faria nada além de desligar a checagem de mistura).']
        desconhecidos = sorted({fw for fw in ciclo if fw not in status})
        if desconhecidos:
            return [f'{slug}: rodízio cita framework inexistente: '
                    f'{", ".join(desconhecidos)}.']
        # O HUB ({slug}.html, sem número) carrega a etiqueta da ÚLTIMA aula gerada — num
        # rodízio isso é ruído, não declaração: ele contém aulas de vários métodos. Por
        # isso a conferência é só sobre arquivos com número de aula.
        for n, fw in sorted(aulas.items()):
            if n < desde:
                continue  # antes de o rodízio começar: fora do alcance desta regra
            esperado = ciclo[(n - desde) % len(ciclo)]
            if fw != esperado:
                erros.append(
                    f'{slug}-aula{n}: framework "{fw}" contraria o rodízio declarado — o '
                    f'ciclo {" > ".join(ciclo)} (a partir da aula {desde}) pede '
                    f'"{esperado}" nesta posição.')
        return erros

    if not mig:
        if len(fws) > 1:
            detalhe = ' vs '.join(f'{k} ({len(v)} aula(s))' for k, v in sorted(fws.items()))
            erros.append(
                f'{slug}: aulas de frameworks DIFERENTES sem migração declarada -> '
                f'{detalhe}. Se a troca é intencional, declare em migracoes[] de '
                f'frameworks.json ({{"slug","de","para","a_partir_da_aula"}}); se alternam '
                f'de propósito, declare em rodizios[]; se não é nem um nem outro, alguém '
                f'trocou o framework deste aluno por engano.')
        return erros
    corte, de, para = mig.get('a_partir_da_aula'), mig.get('de'), mig.get('para')
    if not (corte and de and para):
        return [f'{slug}: migração declarada incompleta — exige "de", "para" e '
                f'"a_partir_da_aula".']
    fora = {fw for fw in fws if fw not in (de, para)}
    if fora:
        erros.append(f'{slug}: migração declara {de} -> {para}, mas há aula em '
                     f'{sorted(fora)}.')
    for n, fw in sorted(aulas.items()):
        esperado = de if n < corte else para
        if fw != esperado:
            erros.append(
                f'{slug}-aula{n}: framework "{fw}" contraria a migração declarada '
                f'({de} até a aula {corte - 1}, {para} da {corte} em diante).')
    return erros


if __name__ == '__main__':
    sys.exit(main())
