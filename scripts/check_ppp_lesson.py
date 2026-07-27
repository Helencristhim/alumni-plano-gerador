#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 12 — aula do framework PPP.

O primeiro gate ESCOPADO A UM FRAMEWORK. Nasce com o primeiro mock de PPP, seguindo a
decisão do Dan (27/07/2026):

    "não precisa generalizar, apenas caso os frameworks compartilhem o mesmo tipo de
     exercício; do contrário os mocks novos de aulas baseadas nos frameworks extras
     gerarão gates diferentes futuros"

Generalizar o gate do Imersivo seria AFROUXÁ-LO — e afrouxar vale para as 1.221 aulas que
dependem dele. Então o `validate_lesson` foi ESCOPADO (as regras dele valem só para o
Imersivo) e o PPP ganhou este, com as regras DELE.

O que ele cobra (documento pedagógico §PPP B1-C1 + _build/model/V4-SPEC.md):

  1. 7 <= slides <= 15. O PPP é curto de propósito; 25-30 é a faixa do Imersivo.
  2. Os 7 capítulos na ORDEM: Let's Get Started, Packing Words, Brainstorming,
     Diving Deep, Practice, Your Turn, Wrap-up.
  3. Os estágios DUPLOS têm mesmo 2 slides: Packing Words (apresentar -> usar),
     Practice (Categoria A -> Categoria B) e Your Turn (Production -> Discussion).
  4. Answer key existe. Todo exercício fechado do PPP fecha com o gabarito em BLOCO
     SEPARADO — nunca a resposta ao lado do item.
  5. Gramática é IMPLÍCITA: nada de "Grammar Tip", tabela de regra ou revealGrammar.
     Isto é o coração da diferença entre PPP e Imersivo — se vazar, a aula virou Imersivo
     com outro nome.

APLICA-SE SÓ a arquivos com <meta name="alumni-framework" content="ppp">. Qualquer outra
aula (Imersivo, legado, outro framework) é ignorada — este gate não é dono dela.

USO:
    python3 scripts/check_ppp_lesson.py                 # repo inteiro
    python3 scripts/check_ppp_lesson.py A.html B.html   # só estes
    python3 scripts/check_ppp_lesson.py --selftest      # prova que o gate ainda morde
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAPITULOS = ["Let's Get Started", "Packing Words", "Brainstorming",
             "Diving Deep", "Practice", "Your Turn", "Wrap-up"]
DUPLOS = {"Packing Words": 2, "Practice": 2, "Your Turn": 2}
MIN_SLIDES, MAX_SLIDES = 7, 15

RE_FW = re.compile(r'<meta name="alumni-framework" content="([^"]*)"')
RE_SLIDE = re.compile(r'data-slide="\d+"')
RE_CHAPTER = re.compile(r'<div class="chapter-label"[^>]*>([^<]*)<')
RE_AULA = re.compile(r'-aula\d+\.html$')
# Marcas de gramática EXPLÍCITA — o que o PPP não pode ter.
# Procura USO, não definição: o shell (compartilhado com o Imersivo) traz `.grammar-table`
# no CSS e `revealGrammar` no JS, e isso é inofensivo — o PPP simplesmente não chama.
# Acusar a folha de estilo seria acusar o shell, não a aula. Por isso <style> e <script>
# saem antes da busca, e o que se procura é a CHAMADA/uso real.
RE_GRAMATICA = re.compile(
    r'class="[^"]*grammar-table|onclick="[^"]*revealGrammar|Grammar Tip|Grammar Discovery|data-grammar=')
RE_STYLE = re.compile(r'<style\b.*?</style>', re.S | re.I)
RE_SCRIPT = re.compile(r'<script\b.*?</script>', re.S | re.I)


def so_conteudo(html):
    """HTML sem CSS nem JS — o que a aula de fato mostra."""
    return RE_SCRIPT.sub(' ', RE_STYLE.sub(' ', html))


def checa(path, html):
    erros = []
    slides = len(RE_SLIDE.findall(html))
    if not (MIN_SLIDES <= slides <= MAX_SLIDES):
        erros.append(f'{slides} slides — o PPP pede entre {MIN_SLIDES} e {MAX_SLIDES} '
                     f'(25-30 é a faixa do Imersivo)')

    caps = [c.strip() for c in RE_CHAPTER.findall(html)]
    # Ordem: a 1a aparição de cada capítulo tem de seguir a sequência do documento.
    ordem_vista = []
    for c in caps:
        if c in CAPITULOS and c not in ordem_vista:
            ordem_vista.append(c)
    faltando = [c for c in CAPITULOS if c not in ordem_vista]
    if faltando:
        erros.append(f'capítulo(s) ausente(s): {", ".join(faltando)}')
    esperado = [c for c in CAPITULOS if c in ordem_vista]
    if ordem_vista != esperado:
        erros.append(f'capítulos fora de ordem: {" > ".join(ordem_vista)} '
                     f'(esperado: {" > ".join(esperado)})')

    for cap, n in DUPLOS.items():
        vistos = caps.count(cap)
        if 0 < vistos < n:
            erros.append(f'"{cap}" tem {vistos} slide(s); o documento pede {n} '
                         f'(tipos diferentes, do mais controlado ao menos)')

    if 'ic-answer' not in html and 'Answer key' not in html and 'answer key' not in html:
        erros.append('nenhum ANSWER KEY — no PPP todo exercício fechado fecha com o '
                     'gabarito em bloco separado')

    g = RE_GRAMATICA.search(so_conteudo(html))
    if g:
        erros.append(f'gramática EXPLÍCITA presente ("{g.group(0)}") — no PPP a gramática é '
                     f'implícita (Diving Deep); regra explícita é do Imersivo')
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
    """Prova que o gate MORDE. Um gate que nunca falha é decoração."""
    base = ('<meta name="alumni-framework" content="ppp">' +
            ''.join(f'<div class="chapter-label">{c}</div>' for c in CAPITULOS) +
            '<div class="chapter-label">Packing Words</div>'
            '<div class="chapter-label">Practice</div>'
            '<div class="chapter-label">Your Turn</div>' +
            ''.join(f'data-slide="{i}"' for i in range(1, 11)) + 'Answer key')
    casos = [
        ('aula PPP correta', base, 0),
        ('slides de menos (3)', base.replace(
            ''.join(f'data-slide="{i}"' for i in range(4, 11)), ''), 1),
        ('sem answer key', base.replace('Answer key', ''), 1),
        # USO real, como apareceria numa aula: o botão e a tabela do Imersivo.
        ('gramática explícita (botão)', base + '<button onclick="revealGrammar()">Reveal</button>', 1),
        ('gramática explícita (tabela)', base + '<div class="grammar-table">...</div>', 1),
        ('capítulo faltando', base.replace('<div class="chapter-label">Diving Deep</div>', '', 1), 1),
        # O shell traz .grammar-table no CSS e revealGrammar no JS: inofensivo, NÃO pode acusar
        ('CSS/JS do shell não conta',
         base + '<style>.grammar-table{width:100%}</style><script>function revealGrammar(){}</script>', 0),
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
        if not m or m.group(1).strip() != 'ppp':
            continue                       # não é aula PPP: este gate não é dono dela
        if not RE_AULA.search(os.path.basename(caminho)):
            continue                       # hub ({slug}.html) não é aula: não tem slides
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
    print(f'\n=== GATE 12 (PPP) — {total} aula(s) PPP, {falharam} com erro ===')
    return 1 if falharam else 0


if __name__ == '__main__':
    sys.exit(main())
