#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RETROFIT — Spot the Error com o gabarito morto (autorizado pelo Dan em 30/07/2026).

O DEFEITO
---------
O card usa `.fill-answer` (a classe do gap-fill) como alvo do reveal dentro de um
`.error-card`. Nao existe regra `.error-card.revealed .fill-answer` no stylesheet, entao o
`display:none` INLINE nunca sai: o card ganha `.revealed`, o contador sobe ate "4 / 4
errors found" e a correcao NUNCA aparece. Junto, o `line-through` nasce baked num
`<span style=...>` — a frase ja entra riscada e entrega de graca qual e o erro que a aluna
deveria achar.

Medido em walyson-aula8 (#1710) e fabiana-aula5 (#1730), os dois reportados pelo Dan.

O CONSERTO
----------
A marcacao do modelo (helen-mendes), que o proprio stylesheet de TODO arquivo afetado ja
suporta: `.error-sentence` + `.error-fix`, sem style inline. O risco passa a vir da regra
`.error-card.revealed .error-sentence` — ou seja, so DEPOIS do clique.

    <div class="error-card" onclick="revealError(this)">
      <div class="error-sentence">"frase com o erro"</div>
      <div class="error-fix">"frase <strong>corrigida</strong>"</div>
    </div>

POR QUE ISTO E SEGURO (REGRA 30 — o legado nao se mexe por capricho)
--------------------------------------------------------------------
Este script existe porque o Dan mandou varrer, depois de o mesmo defeito ser reportado
duas vezes em dois dias. As travas que o tornam uma reescrita medida, e nao um regex
guloso (o incidente que quase reescreveu 2.182 arquivos em vez de 48):

  1. So toca card que casa com O MOLDE INTEIRO (div > <p>frase</p> + <p class="fill-answer"
     escondido>gabarito</p>). Qualquer card fora do molde e PULADO e reportado, nunca
     "adaptado".
  2. So toca arquivo que JA TEM as 4 regras CSS de destino. Sem elas, converter deixaria o
     conteudo sem estilo — pior que o defeito.
  3. Prova de nao-dano: fora dos blocos substituidos, o arquivo tem de ficar BYTE A BYTE
     igual. Se sobrar qualquer diferenca, o arquivo e descartado inteiro.
  4. --dry-run por padrao. So escreve com --write.

    python3 scripts/retrofit_spot_the_error.py            # dry-run, relatorio
    python3 scripts/retrofit_spot_the_error.py --write    # aplica
    python3 scripts/retrofit_spot_the_error.py --selftest # prova que morde e que poupa
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# O MOLDE. Deliberadamente rigido no CONTEUDO (os dois <p>, nesta ordem, e o fill-answer
# escondido) e frouxo so no espaco em branco: metade do roster escreve o card em quatro
# linhas e a outra metade numa linha so (eduardo-chiba). Exigir \n deixava 18 arquivos
# para tras — o mesmo defeito, so que sem quebra de linha.
#
# `(?:(?!</?div\b).)*?` no lugar de `.*?` NAO e preciosismo. Com `.*?` puro o match
# ATRAVESSA A FRONTEIRA ENTRE CARDS: num card cujo 2o <p> nao e `.fill-answer`
# (rubens-tofolo usa `.error-correct`), o backtracking estica a frase por cima dos cards
# seguintes ate achar um `fill-answer` la na frente — e a substituicao comeria tudo no
# meio. E o regex guloso da REGRA 30. Aqui o match nao pode cruzar nenhum <div>/</div>.
CARD = re.compile(
    r'(?P<ind>[ \t]*)<div class="error-card"(?P<attrs>[^>]*?)>\s*'
    r'<p[^>]*>(?P<frase>(?:(?!</?div\b).)*?)</p>\s*'
    r'<p class="fill-answer"(?P<fixattrs>[^>]*?)>(?P<fix>(?:(?!</?div\b).)*?)</p>\s*'
    r'</div>', re.S)

ESCONDIDO = re.compile(r'display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d])')
SPAN_RISCO = re.compile(r'<span style="[^"]*line-through[^"]*">(.*?)</span>', re.S)
ONCLICK = re.compile(r'onclick="(?P<h>[^"]*)"')

# As 4 regras que o arquivo PRECISA ter para a marcacao de destino funcionar.
CSS_NECESSARIO = [
    ('.error-card .error-sentence', re.compile(r'\.error-card\s+\.error-sentence\s*\{')),
    ('.error-card .error-fix{display:none}',
     re.compile(r'\.error-card\s+\.error-fix\s*\{[^}]*display\s*:\s*none')),
    ('.error-card.revealed .error-fix{display:block}',
     re.compile(r'\.error-card\.revealed\s+\.error-fix\s*\{[^}]*display\s*:\s*block')),
    ('.error-card.revealed .error-sentence{line-through}',
     re.compile(r'\.error-card\.revealed\s+\.error-sentence\s*\{[^}]*line-through')),
]


def css_faltando(html):
    return [nome for nome, rx in CSS_NECESSARIO if not rx.search(html)]


def converter(html):
    """Devolve (novo_html, trocados, pulados). Nao decide nada sobre o arquivo."""
    trocados, pulados = [], []

    def troca(m):
        # so o card com o gabarito ESCONDIDO no style inline e o defeito.
        if not ESCONDIDO.search(m.group('fixattrs')):
            return m.group(0)
        oc = ONCLICK.search(m.group('attrs'))
        if not oc or 'revealError' not in oc.group('h'):
            pulados.append('onclick nao e revealError: %r' % m.group('attrs')[:60])
            return m.group(0)
        frase = SPAN_RISCO.sub(lambda s: s.group(1), m.group('frase')).strip()
        fix = m.group('fix').strip()
        # sobrou marcacao de risco fora do span? nao mexo — o autor fez algo diferente.
        if 'line-through' in frase:
            pulados.append('line-through fora do <span>: %r' % frase[:60])
            return m.group(0)
        if not frase or not fix:
            pulados.append('frase ou gabarito vazio')
            return m.group(0)
        ind = m.group('ind')
        trocados.append(frase)
        return ('%s<div class="error-card" onclick="%s">\n'
                '%s  <div class="error-sentence">%s</div>\n'
                '%s  <div class="error-fix">%s</div>\n'
                '%s</div>' % (ind, oc.group('h'), ind, frase, ind, fix, ind))

    return CARD.sub(troca, html), trocados, pulados


def prova_de_nao_dano(antes, depois):
    """Fora dos blocos de .error-card, os dois textos tem de ser IDENTICOS.

    Neutraliza todo bloco que casa com o molde nos dois lados e compara o resto byte a
    byte. Se o regex tiver comido qualquer coisa alem do card, isto acusa.
    """
    a = CARD.sub('\x00CARD\x00', antes)
    d = re.sub(r'[ \t]*<div class="error-card"[^>]*>\s*'
               r'<div class="error-sentence">.*?</div>\s*'
               r'<div class="error-fix">.*?</div>\s*'
               r'</div>', '\x00CARD\x00', depois, flags=re.S)
    d = CARD.sub('\x00CARD\x00', d)
    return a == d


def alvos(args):
    lista = [a for a in args if not a.startswith('--')]
    if lista:
        return lista
    out = []
    for sub in ('public/professor', 'public/aluno'):
        out += glob.glob(os.path.join(RAIZ, sub, '*.html'))
    return sorted(out)


def selftest():
    CSS = ('.error-card .error-sentence{flex:1}.error-card .error-fix{display:none}'
           '.error-card.revealed .error-fix{display:block}'
           '.error-card.revealed .error-sentence{text-decoration:line-through}')
    quebrado = (
        '      <div class="error-card" onclick="revealError(this)" style="padding:.9rem">\n'
        '        <p style="font-size:.9rem">"The shipment <span style="color:red;'
        'text-decoration:line-through;font-weight:600">was reroute</span> now."</p>\n'
        '        <p class="fill-answer" style="display:none;color:green">"The shipment '
        '<strong>was rerouted</strong> now."</p>\n'
        '      </div>')
    casos = []

    novo, tr, pu = converter(quebrado)
    casos.append(('converte o molde quebrado', len(tr) == 1 and not pu
                  and '<div class="error-sentence">"The shipment was reroute now."</div>' in novo
                  and '<div class="error-fix">"The shipment <strong>was rerouted</strong> now."</div>' in novo
                  and 'fill-answer' not in novo and 'line-through' not in novo))

    # ja no formato certo: nada a fazer
    certo = ('      <div class="error-card" onclick="revealError(this)">\n'
             '        <div class="error-sentence">"a"</div>\n'
             '        <div class="error-fix">"b"</div>\n'
             '      </div>')
    novo2, tr2, _ = converter(certo)
    casos.append(('poupa o card que ja esta certo', novo2 == certo and not tr2))

    # gabarito VISIVEL (nao e o defeito): nao mexe
    visivel = quebrado.replace('style="display:none;color:green"', 'style="color:green"')
    novo3, tr3, _ = converter(visivel)
    casos.append(('poupa gabarito que nasce visivel', novo3 == visivel and not tr3))

    # outro handler: pula e reporta
    outro = quebrado.replace('revealError(this)', 'abrirOutraCoisa(this)')
    novo4, tr4, pu4 = converter(outro)
    casos.append(('pula onclick que nao e revealError', novo4 == outro and not tr4 and len(pu4) == 1))

    # prova de nao-dano pega adulteracao fora do card
    _, _, _ = converter(quebrado)
    casos.append(('prova de nao-dano aceita a conversao correta',
                  prova_de_nao_dano('X\n' + quebrado + '\nY', 'X\n' + novo + '\nY')))
    casos.append(('prova de nao-dano ACUSA texto perdido fora do card',
                  not prova_de_nao_dano('X\n' + quebrado + '\nY', 'X\n' + novo + '\n')))

    # REGRESSAO: card vizinho com OUTRA classe de gabarito (.error-correct, rubens-tofolo).
    # Com `.*?` puro o match pulava a fronteira e engolia o card do meio.
    vizinhos = (
        '      <div class="error-card" onclick="revealError2(this)">\n'
        '        <p class="error-wrong">"He go always."</p>\n'
        '        <p class="error-correct" style="display:none">"He always goes."</p>\n'
        '      </div>\n' + quebrado)
    novo5, tr5, _ = converter(vizinhos)
    casos.append(('nao atravessa a fronteira entre cards',
                  len(tr5) == 1 and 'error-wrong' in novo5 and 'error-correct' in novo5
                  and novo5.count('<div class="error-card"') == 2))

    casos.append(('css_faltando acusa arquivo sem as regras', len(css_faltando('<style></style>')) == 4))
    casos.append(('css_faltando aceita arquivo com as regras', css_faltando(CSS) == []))

    ok = True
    for nome, passou in casos:
        print('  [%s] %s' % ('OK' if passou else 'ERRO', nome))
        ok = ok and passou
    print('SELFTEST:', 'passou (%d/%d)' % (sum(1 for _, p in casos if p), len(casos))
          if ok else 'FALHOU')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    escrever = '--write' in args
    tocados = cards = 0
    pulados_tot = []
    descartados = []
    for path in alvos(args):
        with open(path, encoding='utf-8') as f:
            antes = f.read()
        if 'fill-answer' not in antes or 'error-card' not in antes:
            continue
        depois, trocados, pulados = converter(antes)
        if not trocados:
            if pulados:
                pulados_tot += ['%s: %s' % (os.path.relpath(path, RAIZ), p) for p in pulados]
            continue
        falta = css_faltando(antes)
        if falta:
            descartados.append('%s: sem %s' % (os.path.relpath(path, RAIZ), falta[0]))
            continue
        if not prova_de_nao_dano(antes, depois):
            descartados.append('%s: prova de nao-dano FALHOU (arquivo intocado)'
                               % os.path.relpath(path, RAIZ))
            continue
        tocados += 1
        cards += len(trocados)
        pulados_tot += ['%s: %s' % (os.path.relpath(path, RAIZ), p) for p in pulados]
        if escrever:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(depois)
    print('%s: %d arquivo(s), %d card(s) do Spot the Error'
          % ('APLICADO' if escrever else 'DRY-RUN', tocados, cards))
    if pulados_tot:
        print('\ncards PULADOS (fora do molde — nao foram tocados): %d' % len(pulados_tot))
        for p in pulados_tot[:20]:
            print('  - ' + p)
    if descartados:
        print('\narquivos DESCARTADOS inteiros: %d' % len(descartados))
        for d in descartados[:20]:
            print('  ! ' + d)
    return 0


if __name__ == '__main__':
    sys.exit(main())
