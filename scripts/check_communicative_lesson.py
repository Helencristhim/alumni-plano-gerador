#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 13 — aula do framework COMMUNICATIVE APPROACH.

Segundo gate escopado a um framework (o primeiro foi o do PPP). Mesma filosofia:
"escopar, não generalizar" — o `validate_lesson` cobra o que é do Imersivo, e cada
framework traz o gate das regras DELE.

O que ele cobra (documento pedagógico §Communicative Approach B1-C1):

  1. 6 a 10 slides. O documento dá 1 slide por stage, com 1-3 no Exposure e 1-2 na Task.
  2. Os 6 stages na ORDEM: Warm-up, Check it out, Language for Communication,
     Pre-communicative, Communicative Task, Feedback.
  3. O NÚCLEO existe e é a tarefa. O Communicative não é uma aula de exercícios com uma
     conversa no fim: 25-30 dos 60 minutos são a Communicative Task.
  4. Answer key nos stages FECHADOS (3 e 4) — e a ausência dele nos ABERTOS (1 e 5) é
     característica, não esquecimento: o documento diz "sem answer key" para a discussão
     e para a tarefa.
  5. O Warm-up NÃO tem exercício controlado. É a regra mais fácil de violar sem perceber
     — basta o autor achar que "só um matchingzinho" ajuda. Ajuda a virar PPP.
  6. Gramática explícita não entra (igual PPP): a forma sai do input, em contexto.

APLICA-SE SÓ a arquivos com <meta name="alumni-framework" content="communicative">.

USO:
    python3 scripts/check_communicative_lesson.py                 # repo inteiro
    python3 scripts/check_communicative_lesson.py A.html          # só este
    python3 scripts/check_communicative_lesson.py --selftest      # prova que morde
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGES = ["Warm-up", "Check it out", "Language for Communication",
          "Pre-communicative", "Communicative Task", "Feedback"]
MIN_SLIDES, MAX_SLIDES = 6, 10

RE_FW = re.compile(r'<meta name="alumni-framework" content="([^"]*)"')
RE_SLIDE = re.compile(r'data-slide="\d+"')
RE_CHAPTER = re.compile(r'<div class="chapter-label"[^>]*>([^<]*)<')
RE_AULA = re.compile(r'-aula\d+\.html$')
RE_GRAMATICA = re.compile(
    r'class="[^"]*grammar-table|onclick="[^"]*revealGrammar|Grammar Tip|Grammar Discovery|data-grammar=')
RE_STYLE = re.compile(r'<style\b.*?</style>', re.S | re.I)
RE_SCRIPT = re.compile(r'<script\b.*?</script>', re.S | re.I)
# Exercício CONTROLADO: o que tem gabarito ou validação automática.
RE_CONTROLADO = re.compile(r'icPickMatch|icPickGist|icRevealTf|icToggleAnswer|checkBlank|selectQuiz')


def so_conteudo(html):
    return RE_SCRIPT.sub(' ', RE_STYLE.sub(' ', html))


def slide_do_stage(html, stage):
    """Devolve o HTML do primeiro slide cujo chapter-label é `stage`."""
    for bloco in re.split(r'(?=<div class="slide )', html):
        m = RE_CHAPTER.search(bloco)
        if m and m.group(1).strip() == stage:
            return bloco
    return None


def checa(path, html):
    erros = []
    corpo = so_conteudo(html)

    n = len(RE_SLIDE.findall(html))
    if not (MIN_SLIDES <= n <= MAX_SLIDES):
        erros.append(f'{n} slides — o Communicative pede entre {MIN_SLIDES} e {MAX_SLIDES} '
                     f'(1 por stage, com 1-3 no Exposure e 1-2 na Task)')

    caps = [c.strip() for c in RE_CHAPTER.findall(html)]
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

    # 3 — o núcleo existe
    if 'Communicative Task' not in caps:
        erros.append('sem Communicative Task — a tarefa É o núcleo deste framework, '
                     'não um extra no fim')

    # 4 — answer key nos stages fechados
    if 'ic-answer' not in html and 'Answer key' not in html:
        erros.append('nenhum ANSWER KEY — os stages fechados (Language, Pre-communicative) '
                     'fecham com gabarito em bloco separado')

    # 5 — Warm-up sem exercício controlado (a regra mais fácil de violar sem perceber)
    warm = slide_do_stage(html, 'Warm-up')
    if warm and RE_CONTROLADO.search(so_conteudo(warm)):
        achado = RE_CONTROLADO.search(so_conteudo(warm)).group(0)
        erros.append(f'Warm-up tem exercício CONTROLADO ("{achado}") — no Communicative o '
                     f'stage 1 é discussão aberta, sem answer key. Com exercício ali, virou PPP')

    # 6 — gramática explícita
    g = RE_GRAMATICA.search(corpo)
    if g:
        erros.append(f'gramática EXPLÍCITA ("{g.group(0)}") — no Communicative a forma sai do '
                     f'input, em contexto, nunca isolada')
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
    def mk(extra_warm='', extra=''):
        blocos = []
        for s in STAGES:
            corpo = extra_warm if s == 'Warm-up' else ''
            blocos.append(f'<div class="slide "><div class="chapter-label">{s}</div>{corpo}</div>')
        return ('<meta name="alumni-framework" content="communicative">' +
                ''.join(blocos) + slides + 'Answer key' + extra)
    casos = [
        ('aula Communicative correta', mk(), 0),
        ('Warm-up com exercício controlado', mk(extra_warm='<div onclick="icPickMatch(this)">x</div>'), 1),
        ('sem answer key', mk().replace('Answer key', ''), 1),
        ('gramática explícita', mk(extra='<button onclick="revealGrammar()">R</button>'), 1),
        ('stage faltando', mk().replace('<div class="chapter-label">Feedback</div>', '', 1), 1),
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
        if not m or m.group(1).strip() != 'communicative':
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
    print(f'\n=== GATE 13 (Communicative) — {total} aula(s), {falharam} com erro ===')
    return 1 if falharam else 0


if __name__ == '__main__':
    sys.exit(main())
