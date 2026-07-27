#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 14 — aula do framework TASK-BASED (TBLT com priming leve).

Terceiro gate escopado a um framework. É o mais opinativo dos três, porque o TBL é o
que mais se parece com os outros por fora e o que mais diverge por dentro. O documento
pedagógico é explícito sobre a inversão:

    "a linguagem-alvo é EXPOSTA antes da tarefa (priming receptivo), mas NÃO é ensinada
     explicitamente antes dela. A descoberta e o refinamento da forma acontecem [...] no
     Focus on Form diferido, que vem DEPOIS da produção — esta é a inversão que
     distingue o TBLT do PPP."

O que ele cobra:

  1. 6 a 10 slides (1 por stage, com 1-2 no Input e 1-2 no Task Cycle).
  2. Os 6 stages na ORDEM: Warm-up & Priming, Input & Pre-task, Language for the Task,
     Task Cycle, Focus on Form, Wrap-up.
  3. FOCUS ON FORM EXISTE E VEM DEPOIS DO TASK CYCLE. Se sumir ou trocar de lugar, não
     é TBL — virou PPP com outros rótulos. É a regra central deste gate.
  4. O Task Cycle tem DUAS tasks (o documento pede 2 tipos diferentes; a 1 obrigatória,
     a 2 contingente ao tempo).
  5. NÃO existe stage de "Practice" entre a linguagem e a tarefa. O documento é
     categórico: "Não há stage de practice controlada antes da tarefa — o aluno vai
     direto ao ciclo com a linguagem disponível como recurso."
  6. Gramática explícita não entra (igual PPP e Communicative).

APLICA-SE SÓ a arquivos com <meta name="alumni-framework" content="task-based">.

USO:
    python3 scripts/check_tbl_lesson.py                 # repo inteiro
    python3 scripts/check_tbl_lesson.py A.html          # só este
    python3 scripts/check_tbl_lesson.py --selftest      # prova que morde
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGES = ["Warm-up & Priming", "Input & Pre-task", "Language for the Task",
          "Task Cycle", "Focus on Form", "Wrap-up"]
MIN_SLIDES, MAX_SLIDES = 6, 10

RE_FW = re.compile(r'<meta name="alumni-framework" content="([^"]*)"')
RE_SLIDE = re.compile(r'data-slide="\d+"')
RE_CHAPTER = re.compile(r'<div class="chapter-label"[^>]*>([^<]*)<')
RE_AULA = re.compile(r'-aula\d+\.html$')
RE_GRAMATICA = re.compile(
    r'class="[^"]*grammar-table|onclick="[^"]*revealGrammar|Grammar Tip|Grammar Discovery|data-grammar=')
RE_STYLE = re.compile(r'<style\b.*?</style>', re.S | re.I)
RE_SCRIPT = re.compile(r'<script\b.*?</script>', re.S | re.I)


def so_conteudo(html):
    return RE_SCRIPT.sub(' ', RE_STYLE.sub(' ', html))


def _norm(s):
    """Compara rótulos ignorando a forma do &amp; (o HTML escapa, o autor não)."""
    return s.replace('&amp;', '&').strip()


def checa(path, html):
    erros = []
    caps = [_norm(c) for c in RE_CHAPTER.findall(html)]

    n = len(RE_SLIDE.findall(html))
    if not (MIN_SLIDES <= n <= MAX_SLIDES):
        erros.append(f'{n} slides — o TBL pede entre {MIN_SLIDES} e {MAX_SLIDES}')

    ordem = []
    for c in caps:
        if c in STAGES and c not in ordem:
            ordem.append(c)
    falta = [s for s in STAGES if s not in ordem]
    if falta:
        erros.append(f'stage(s) ausente(s): {", ".join(falta)}')
    esperado = [s for s in STAGES if s in ordem]
    if ordem != esperado:
        erros.append(f'stages fora de ordem: {" > ".join(ordem)} (esperado: {" > ".join(esperado)})')

    # 3 — A REGRA CENTRAL: Focus on Form existe e vem DEPOIS do Task Cycle
    if 'Focus on Form' not in caps:
        erros.append('sem Focus on Form — é o stage que DEFINE o TBL: a forma vem depois '
                     'da produção. Sem ele, isto é PPP com outros rótulos')
    elif 'Task Cycle' in caps:
        if caps.index('Focus on Form') < caps.index('Task Cycle'):
            erros.append('Focus on Form vem ANTES do Task Cycle — a inversão do TBL é '
                         'exatamente o contrário: produzir primeiro, refinar a forma depois')

    # 4 — o Task Cycle tem duas tasks
    n_task = caps.count('Task Cycle')
    if 0 < n_task < 2:
        erros.append(f'Task Cycle em {n_task} slide — o documento pede DUAS tasks de tipos '
                     f'diferentes (a 1ª obrigatória, a 2ª contingente ao tempo)')

    # 5 — sem practice controlada entre a linguagem e a tarefa
    if any(c == 'Practice' for c in caps):
        erros.append('há um stage "Practice" — o documento é categórico: no TBL NÃO existe '
                     'practice controlada antes da tarefa; a língua é recurso, não conteúdo')

    # 6 — gramática explícita
    g = RE_GRAMATICA.search(so_conteudo(html))
    if g:
        erros.append(f'gramática EXPLÍCITA ("{g.group(0)}") — no TBL a forma é refinada no '
                     f'Focus on Form, a partir do que o aluno produziu')
    return erros


def alvos(argv):
    if argv:
        return [a for a in argv if a.endswith('.html')]
    out = []
    for sub in ('professor', 'aluno'):
        d = os.path.join(ROOT, 'public', sub)
        if os.path.isdir(d):
            out += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith('.html')]
    return out


def selftest():
    slides = ''.join(f'data-slide="{i}"' for i in range(1, 9))
    def mk(stages=None, extra=''):
        st = stages if stages is not None else STAGES[:3] + ['Task Cycle', 'Task Cycle'] + STAGES[4:]
        return ('<meta name="alumni-framework" content="task-based">' +
                ''.join(f'<div class="slide "><div class="chapter-label">{s}</div></div>' for s in st) +
                slides + extra)
    casos = [
        ('aula TBL correta', mk(), 0),
        ('sem Focus on Form',
         mk(STAGES[:3] + ['Task Cycle', 'Task Cycle', 'Wrap-up']), 1),
        ('Focus on Form ANTES do Task Cycle',
         mk(STAGES[:3] + ['Focus on Form', 'Task Cycle', 'Task Cycle', 'Wrap-up']), 1),
        ('só uma task', mk(STAGES[:3] + ['Task Cycle'] + STAGES[4:]), 1),
        ('tem stage Practice (virou PPP)',
         mk(STAGES[:3] + ['Practice', 'Task Cycle', 'Task Cycle'] + STAGES[4:]), 1),
        ('gramática explícita', mk(extra='<button onclick="revealGrammar()">R</button>'), 1),
        ('CSS/JS do shell não conta',
         mk(extra='<style>.grammar-table{}</style><script>function revealGrammar(){}</script>'), 0),
    ]
    ruim = 0
    for nome, html, esperado in casos:
        n = len(checa('selftest', html))
        ok = (n > 0) == (esperado > 0)
        ruim += not ok
        print(f'  {"OK  " if ok else "FALHOU"} {nome}: {n} erro(s)')
    print('\nselftest: ' + ('✅ o gate morde' if not ruim else f'❌ {ruim} caso(s) errado(s)'))
    return 1 if ruim else 0


def main():
    if '--selftest' in sys.argv:
        return selftest()
    total = falharam = 0
    for caminho in alvos(sys.argv[1:]):
        try:
            with open(caminho, encoding='utf-8') as f:
                html = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        m = RE_FW.search(html)
        if not m or m.group(1).strip() != 'task-based':
            continue
        if not RE_AULA.search(os.path.basename(caminho)):
            continue
        total += 1
        erros = checa(caminho, html)
        rel = os.path.relpath(caminho, ROOT)
        if erros:
            falharam += 1
            print(f'❌ {rel}')
            for e in erros:
                print(f'     ✗ {e}')
        else:
            print(f'✅ {rel}')
    print(f'\n=== GATE 14 (Task-Based) — {total} aula(s), {falharam} com erro ===')
    return 1 if falharam else 0


if __name__ == '__main__':
    sys.exit(main())
