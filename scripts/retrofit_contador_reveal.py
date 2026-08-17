#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conserta os contadores de reveal que MATAM o exercicio ou mostram o numero errado.

DOIS DEFEITOS, UMA CAUSA: o handler escreve num elemento que pode nao existir, e escolhe
esse elemento com um ternario de dois ramos.

1. SEM GUARDA -> `document.getElementById('x').textContent = ...` com o `<span>` ausente
   lanca `TypeError: Cannot set properties of null` NO PRIMEIRO CLIQUE. O card para de
   abrir. O exercicio morre.
2. TERNARIO DE DOIS RAMOS -> `grid.id === 'vocabGrid1' ? 'vocabCount1' : 'vocabCount2'`.
   Com TRES grids, o terceiro cai no else e escreve no contador do SEGUNDO: o segundo passa
   a mostrar o total do terceiro, e o terceiro fica parado em 0 para sempre.

Nada disso aparece em gate estatico: a classe esta certa, o handler existe, o HTML e
valido. So aparece CLICANDO — foi assim que os dois foram achados (aula 3 do Samuel e
aula 3 da Sophia, 17/08/2026).

POR QUE NAO CASAR O CORPO INTEIRO DA FUNCAO. Ha pelo menos tres formatacoes no repo: a do
shell atual, uma MINIFICADA (daniela-feitoza-v2) e uma LOCALIZADA em espanhol
(daniel-bastos, "palabras reveladas"). Casar o corpo exato pegava so a primeira e deixava
13 de 84 arquivos de fora. Entao a transformacao e cirurgica DENTRO das duas funcoes:

  a) o ternario de dois ramos  -> id derivado do grid
  b) getElementById(X).textContent = Y  -> var _e=getElementById(X); if(_e) _e.textContent=Y

IDEMPOTENTE: um arquivo ja consertado nao casa mais nenhum dos dois padroes.

ESCOPO: so os arquivos da lista — os MEDIDOS NO NAVEGADOR como QUEBRA ou CONTADOR-ERRADO.

    python3 scripts/retrofit_contador_reveal.py lista.txt [--dry-run]
"""
import re
import sys

FUNCS = ('revealVocab', 'revealError')

# ternario de dois ramos, com ou sem espacos
TERN = re.compile(r"grid\.id\s*===\s*'vocabGrid1'\s*\?\s*'vocabCount1'\s*:\s*'vocabCount2'")
# escrita sem guarda: captura o argumento do getElementById e a expressao atribuida
ESCR = re.compile(r"document\.getElementById\(([^)]+)\)\.textContent\s*=\s*([^;]+);")


def corpo_da_funcao(js, fn):
    """(inicio, fim) do CORPO de `function fn(...) { ... }`, por contagem de chaves."""
    m = re.search(r'function\s+' + fn + r'\s*\([^)]*\)\s*\{', js)
    if not m:
        return None
    i = m.end()
    nivel = 1
    while i < len(js) and nivel:
        if js[i] == '{':
            nivel += 1
        elif js[i] == '}':
            nivel -= 1
        i += 1
    return (m.end(), i - 1)


def conserta(js):
    mudou = []
    for fn in FUNCS:
        pos = corpo_da_funcao(js, fn)
        if not pos:
            continue
        a, b = pos
        corpo = js[a:b]
        novo = corpo
        if TERN.search(novo):
            novo = TERN.sub("grid.id.replace('vocabGrid', 'vocabCount')", novo)
            mudou.append(fn + ':ternario')
        if ESCR.search(novo):
            n = 0

            def guarda(m):
                nonlocal n
                n += 1
                var = '_ctr%d' % n
                return ('var %s = document.getElementById(%s); if (%s) %s.textContent = %s;'
                        % (var, m.group(1), var, var, m.group(2)))
            novo = ESCR.sub(guarda, novo)
            mudou.append(fn + ':guarda')
        if novo != corpo:
            js = js[:a] + novo + js[b:]
    return js, mudou


def main(argv):
    dry = '--dry-run' in argv
    lista = [x for x in argv[1:] if not x.startswith('--')][0]
    paths = [l.strip() for l in open(lista) if l.strip()]
    ok, nada = 0, []
    from collections import Counter
    what = Counter()
    for p in paths:
        h = open(p, encoding='utf-8').read()
        novo, mudou = conserta(h)
        if novo == h:
            nada.append(p)
            continue
        ok += 1
        for m in mudou:
            what[m] += 1
        if not dry:
            open(p, 'w', encoding='utf-8').write(novo)
    print('%s: %d arquivo(s)' % ('casariam' if dry else 'corrigidos', ok))
    for k, v in sorted(what.items()):
        print('   %-24s %d' % (k, v))
    if nada:
        print('SEM NENHUM DOS DOIS PADROES (%d) — nao tocados:' % len(nada))
        for p in nada[:15]:
            print('   ' + p)
        if len(nada) > 15:
            print('   ... e %d outros' % (len(nada) - 15))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
