#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 15 — os MODOS DE PRODUCAO do IN CLASS (tabela do pedagogico, 28/07/2026).

A tabela que o Luiz e a Stephanie fecharam define QUAIS atividades podem ocupar a etapa
de producao, com que estrutura, e quantas por aula:

  | Modo                          | Estrutura                                      |
  |-------------------------------|------------------------------------------------|
  | Discutir opiniao/experiencia  | 5-10 perguntas                                 |
  | Comentar/analisar situacoes   | 3-5 cenarios + 3-5 perguntas + banco 8-12      |
  | Estudo de caso / problemas    | 3-5 casos + 3-5 perguntas + banco 8-12         |
  | Argumentar a favor/contra     | 2 situacoes divergentes + banco 8-12           |
  | Produzir/criar (projeto)      | instrucao com requisitos, teto de 10 min       |

  PELO MENOS 2 POR AULA.

ROLE-PLAY SAIU DO MENU (ordem do Dan, 28/07/2026). O motivo e o que o Luiz e a Stephanie
levantaram: em aula PARTICULAR o role-play poe o professor como interlocutor, e a fala do
aluno passa a depender da atuacao dele. Se o professor improvisa bem, a aula rende; se
nao, a producao encolhe. Nos outros modos o material esta na TELA e o professor instiga.

Por que um gate e nao so uma regra escrita: role-play e o formato mais facil de escrever e
o mais tentador — foi o que a producao da Lara era antes desta rodada. Regra que depende
de alguem lembrar nao e regra.

COMO SE DECLARA: `data-produce-mode="<modo>"` no slide de producao.

ESCOPO: aulas com <meta name="alumni-gen"> (geracao nova). Aula publicada nao se conserta
(REGRA 30) — e nenhuma delas declara modo, entao o gate as ignora por construcao.

USO:  python3 scripts/check_produce_modes.py [arquivo.html ...]
      sem argumentos, varre public/professor e public/aluno.
      --selftest  prova que o gate ainda morde.
"""
import glob
import os
import re
import sys

MODOS = {
    'discussion':      'Discutir opiniao/experiencia (5-10 perguntas)',
    'comment-analyse': 'Comentar/analisar situacoes (3-5 + 3-5 + banco 8-12)',
    'case-study':      'Estudo de caso / solucao de problemas (3-5 + 3-5 + banco 8-12)',
    'argue':           'Argumentar a favor/contra (2 situacoes + banco 8-12)',
    'project':         'Produzir/criar (projeto, teto de 10 min)',
}
# Removido do menu por decisao do pedagogico. Fica listado de proposito: o gate precisa
# dizer POR QUE recusa, senao quem escrever a proxima aula acha que foi esquecimento.
REMOVIDOS = {
    'role-play': ('role-play poe o professor como interlocutor, e em aula particular a '
                  'fala do aluno passa a depender da atuacao dele'),
}
MIN_POR_AULA = 2


def _gen(c):
    m = re.search(r'<meta name="alumni-gen" content="(\d+)"', c)
    return int(m.group(1)) if m else 0


def _slides(c):
    i, j = c.find('<div class="slides-container"'), c.find('</div><!-- /slides-container -->')
    if i < 0 or j < 0:
        return []
    return [p for p in re.split(r'(?=<div class="slide )', c[i:j]) if 'data-slide=' in p]


def checar(path):
    c = open(path, encoding='utf-8').read()
    if _gen(c) < 1:
        return None                      # legado: nao e comigo
    if not re.search(r'-aula\d+\.html$', os.path.basename(path)):
        return None                      # hub nao tem slides de aula
    erros = []
    por_aula = {}
    for ch in _slides(c):
        m = re.search(r'data-produce-mode="([^"]*)"', ch)
        if not m:
            continue
        modo = m.group(1).strip()
        n = (re.search(r'data-slide="(\d+)"', ch) or [None, '?'])[1]
        aula = (re.search(r'data-lesson="(\d+)"', ch) or [None, '1'])[1]
        if modo in REMOVIDOS:
            erros.append(f'slide {n}: modo "{modo}" foi REMOVIDO do menu — {REMOVIDOS[modo]}')
        elif modo not in MODOS:
            erros.append(f'slide {n}: modo "{modo}" nao existe. Validos: {", ".join(sorted(MODOS))}')
        else:
            por_aula.setdefault(aula, set()).add(modo)
    for aula, modos in sorted(por_aula.items()):
        if len(modos) < MIN_POR_AULA:
            erros.append(f'aula {aula}: so {len(modos)} modo(s) de producao ({", ".join(sorted(modos))}) '
                         f'— a tabela pede PELO MENOS {MIN_POR_AULA} por aula')
    if not por_aula and not erros:
        return None                      # aula sem etapa de producao declarada: fora do escopo
    return erros


def selftest():
    """Um gate que nunca falha nao e gate. Prova que ele morde nos dois casos."""
    base = ('<meta name="alumni-gen" content="1">'
            '<div class="slides-container">'
            '<div class="slide " data-slide="1" data-lesson="1" data-produce-mode="{a}"></div>'
            '<div class="slide " data-slide="2" data-lesson="1" data-produce-mode="{b}"></div>'
            '</div><!-- /slides-container -->')
    casos = [
        ('role-play barrado', base.format(a='role-play', b='discussion'), True),
        ('modo inexistente',  base.format(a='debate-livre', b='discussion'), True),
        ('so 1 modo na aula', base.format(a='case-study', b='case-study'), True),
        ('2 modos validos',   base.format(a='case-study', b='discussion'), False),
    ]
    tmp = os.path.join(os.path.dirname(__file__), '.produce_selftest-aula1.html')
    ok = True
    for nome, html, deve_falhar in casos:
        open(tmp, 'w', encoding='utf-8').write(html)
        erros = checar(tmp) or []
        falhou = bool(erros)
        marca = '✅' if falhou == deve_falhar else '❌'
        if falhou != deve_falhar:
            ok = False
        print(f'  {marca} {nome}: {"barrou" if falhou else "passou"} '
              f'(esperado: {"barrar" if deve_falhar else "passar"})')
        if erros:
            print(f'       {erros[0]}')
    os.remove(tmp)
    print('=== SELFTEST OK ===' if ok else '=== SELFTEST FALHOU ===')
    return 0 if ok else 1


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    alvos = args or sorted(glob.glob('public/professor/*.html') + glob.glob('public/aluno/*.html'))
    rc, vistos = 0, 0
    for p in alvos:
        erros = checar(p)
        if erros is None:
            continue
        vistos += 1
        if erros:
            rc = 1
            print(f'❌ {p}')
            for e in erros:
                print(f'     ✗ {e}')
        else:
            print(f'✅ {p}')
    print(f'\n=== GATE 15 (modos de producao) — {vistos} aula(s), '
          f'{"0" if rc == 0 else "com"} erro(s) ===')
    sys.exit(rc)


if __name__ == '__main__':
    main()
