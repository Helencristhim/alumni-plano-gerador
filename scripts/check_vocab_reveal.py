#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE 10 — RESPOSTA/PALAVRA QUE NASCE ESCONDIDA NUM REVEAL POR STYLESHEET.

O DEFEITO
---------
Varios componentes de aula escondem algo (a PALAVRA, a RESPOSTA, a CORRECAO) e
mostram no clique. Existem DOIS mecanismos, e a diferenca decide se um
`style="display:none"` inline e correto ou e um bug:

  A) REVEAL POR STYLESHEET — o handler so faz `classList.add/toggle('revealed')`
     e quem mostra e uma REGRA CSS (`.comp-q.revealed .q-answer{display:block}`).
     Se o alvo nasce com display:none INLINE, o inline VENCE a stylesheet e o
     conteudo NUNCA aparece. BUG.

  B) REVEAL POR JS — o handler faz `alvo.style.display=''` (ou 'block'). Isso
     REMOVE o inline em runtime -> aparece. Aqui o display:none inicial e o estado
     escondido CORRETO. NAO e bug.

Casos reais que motivaram o gate: luiz-bressane (aulas 7/8) e eduarda-gabriel x2
(.vocab-back); karina-macedo (.q-answer, resposta de compreensao); milton-sayegh e
juliana-marques (.error-fix, correcao do Spot the Error).

POR QUE A CHECAGEM E POR INSTANCIA, NAO POR ARQUIVO
---------------------------------------------------
Um mesmo arquivo pode ter varios handlers (revealError, revealError1, revealError7,
handler inline...). Checar "o arquivo tem revealError que seta display?" da FALSO
POSITIVO e FALSO NEGATIVO. Aqui cada alvo escondido e amarrado ao onclick do SEU
proprio card. Foi essa checagem que inocentou elaine-mieko-pinho (revealError7 seta
display) e tuca-dias (handler inline seta display), que a checagem por arquivo
acusava por engano.

    python3 scripts/check_vocab_reveal.py                 # varre o repo (CI)
    python3 scripts/check_vocab_reveal.py a.html b.html   # so estes arquivos
    python3 scripts/check_vocab_reveal.py --selftest      # prova que o gate morde
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (classe do alvo escondido, classes possiveis do card clicavel que o contem, so_gen_nova)
#
# `so_gen_nova` restringe a familia as aulas com <meta name="alumni-gen"> (geracao nova).
# Use quando a divida de legado for grande demais para caber num conserto (REGRA 30: aula
# publicada nao se mexe) — o gate entao serve para impedir que o defeito NASCA de novo.
FAMILIAS = [
    ('vocab-back', ('vocab-card-ic', 'vocab-card'), False),  # a PALAVRA (Vocabulary Reveal)
    ('q-answer', ('comp-q',), False),                        # a RESPOSTA (comprehension)
    ('error-fix', ('error-card',), False),                   # a CORRECAO (Spot the Error)
    # MESMO defeito do .error-fix, com a classe ERRADA no alvo: o conteudo usa
    # `.fill-answer` (a classe do gap-fill) dentro de um `.error-card`. Nao existe regra
    # `.error-card.revealed .fill-answer` no stylesheet, entao o display:none inline nunca
    # sai: o contador sobe a cada clique e a correcao NUNCA aparece. Medido no navegador em
    # walyson-ginaldo-silva-aula8 (4 de 4 cards mortos, reportado pelo Dan em 29/07/2026).
    # `.fill-item` entra pelo mesmo motivo: a regra base e `.fill-item.revealed
    # .fill-answer{display:inline}`, que o inline vence. NAO vale para `.comp-question`,
    # onde a regra do stylesheet usa !important e portanto ganha do inline.
    #
    # NASCEU escopada (so_gen_nova=True) porque havia 708 arquivos publicados com a mesma
    # forma morta e a REGRA 30 nao deixa mexer no legado por capricho. Em 30/07/2026 o Dan
    # mandou varrer: `scripts/retrofit_spot_the_error.py` converteu os 708 (2.832 cards)
    # para a marcacao do modelo e a divida do SPOT THE ERROR foi a ZERO — por isso a linha
    # do `error-card` perdeu o escopo e agora vale para o repo INTEIRO, legado inclusive.
    # O defeito nao tem mais por onde voltar: nem em aula nova, nem numa edicao manual de
    # aula antiga.
    ('fill-answer', ('error-card',), False),
    # O gap-fill segue ESCOPADO: sobrou 1 arquivo legado (public/professor/juliana-marques
    # .html, 5 cards) que a varredura nao cobriu de proposito — e outro componente, nao era
    # o que o Dan mandou varrer. Desescopar esta linha antes de consertar aquele arquivo
    # travaria o CI do repo inteiro por um defeito que ninguem autorizou tocar.
    ('fill-answer', ('fill-item',), True),
]

# nasce escondido: um dos tres jeitos de esconder via style inline.
_HIDE = r'(?:display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d]))'

# TODOS os cards clicaveis conhecidos disputam a proximidade, nao so os da familia. Sem
# isso, um `.fill-answer` dentro de `.comp-question` (que o stylesheet mostra com
# !important, logo NAO e bug) seria amarrado ao `.error-card` anterior do arquivo, que pode
# estar centenas de linhas acima — falso positivo.
CARDS = ('vocab-card-ic', 'vocab-card', 'comp-question', 'comp-q', 'error-card', 'fill-item')


def _gen(html):
    """<meta name="alumni-gen"> — 0 quando a aula e anterior ao builder (legado)."""
    m = re.search(r'<meta name="alumni-gen" content="(\d+)"', html)
    return int(m.group(1)) if m else 0


def card_que_contem(html, pos):
    """(classe, tag de abertura) do card clicavel conhecido mais proximo ANTES de pos."""
    melhor, classe = -1, None
    for c in CARDS:
        p = html.rfind('<div class="%s' % c, 0, pos)
        if p > melhor:
            melhor, classe = p, c
    if melhor == -1:
        return None, ''
    return classe, html[melhor:html.find('>', melhor) + 1]


def corpo_funcao(html, nome):
    """Corpo de `function <nome>(...) { ... }` por balanceamento de chaves."""
    m = re.search(r'function\s+%s\s*\([^)]*\)\s*\{' % re.escape(nome), html)
    if not m:
        return None
    i = m.end() - 1
    depth = 0
    for j in range(i, len(html)):
        if html[j] == '{':
            depth += 1
        elif html[j] == '}':
            depth -= 1
            if depth == 0:
                return html[i:j + 1]
    return html[i:]


def handler_desconde(html, onclick):
    """True se ESTE handler tira o alvo do escondido (seta .style.display)."""
    if not onclick:
        return False
    if '.style.display' in onclick:      # handler inline faz na mao
        return True
    m = re.match(r'\s*([A-Za-z0-9_$]+)\s*\(', onclick)
    if not m:
        return False
    corpo = corpo_funcao(html, m.group(1))
    return bool(corpo) and '.style.display' in corpo


def falhas_no_arquivo(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        html = f.read()
    rel = os.path.relpath(path, RAIZ)
    gen = _gen(html)
    falhas = []
    for alvo, pais, so_gen_nova in FAMILIAS:
        if so_gen_nova and not gen:
            continue
        rx = re.compile(r'class="%s"[^>]*\bstyle="[^"]*%s' % (re.escape(alvo), _HIDE),
                        re.IGNORECASE)
        quebrados = 0
        for m in rx.finditer(html):
            # amarra ESTA instancia ao card clicavel que a contem
            classe, tag = card_que_contem(html, m.start())
            if classe is None or not any(classe.startswith(p) for p in pais):
                continue    # o alvo esta em OUTRO componente — nao e desta familia
            oc = re.search(r'onclick="([^"]*)"', tag)
            onclick = oc.group(1) if oc else ''
            if not handler_desconde(html, onclick):
                quebrados += 1
        if quebrados:
            falhas.append('%s: %d x .%s nasce escondido e o reveal e por stylesheet '
                          '-> o conteudo nunca aparece no clique' % (rel, quebrados, alvo))
    return falhas


def alvos(args):
    if args:
        return [a for a in args if not a.startswith('--')]
    out = []
    for sub in ('public/professor', 'public/aluno'):
        out += glob.glob(os.path.join(RAIZ, sub, '*.html'))
    return sorted(out)


def selftest():
    """Prova, em memoria, que o gate REPROVA o quebrado e ACEITA os certos."""
    import tempfile
    casos = [
        ('QUEBRADO: stylesheet reveal + alvo escondido',
         '<script>function revealComp(q){q.classList.toggle("revealed");}</script>'
         '<div class="comp-q" onclick="revealComp(this)">'
         '<div class="q-answer" style="display:none">resposta</div></div>', True),
        ('OK: alvo visivel (stylesheet base esconde)',
         '<script>function revealComp(q){q.classList.toggle("revealed");}</script>'
         '<div class="comp-q" onclick="revealComp(this)">'
         '<div class="q-answer">resposta</div></div>', False),
        ('OK: handler NOMEADO seta display',
         '<script>function revealError(c){c.querySelector(".error-fix").style.display="";}'
         '</script><div class="error-card" onclick="revealError(this)">'
         '<div class="error-fix" style="display:none">fix</div></div>', False),
        ('OK: handler INLINE seta display',
         '<div class="error-card" onclick="this.querySelector(\'.error-fix\').style.display=\'block\'">'
         '<div class="error-fix" style="display:none">fix</div></div>', False),
        ('QUEBRADO: vocab-back escondido, revealVocab so classList',
         '<script>function revealVocab(c){c.classList.add("revealed");}</script>'
         '<div class="vocab-card-ic" onclick="revealVocab(this)">'
         '<div class="vocab-back" style="display:none">word</div></div>', True),
        # o caso walyson-aula8: classe ERRADA no alvo (fill-answer dentro de error-card).
        ('QUEBRADO: fill-answer dentro de error-card (geracao nova)',
         '<meta name="alumni-gen" content="3">'
         '<script>function revealError(c){c.classList.toggle("revealed");}</script>'
         '<div class="error-card" onclick="revealError(this)">'
         '<p class="fill-answer" style="display:none">fix</p></div>', True),
        # Antes de 30/07/2026 este caso esperava False: a familia era escopada por causa
        # dos 708 legados. A varredura zerou a divida e o escopo caiu — agora o MESMO
        # defeito numa aula sem carimbo TEM de reprovar. E disso que vem o "nunca mais".
        ('QUEBRADO: fill-answer dentro de error-card em aula LEGADA (sem carimbo)',
         '<script>function revealError(c){c.classList.toggle("revealed");}</script>'
         '<div class="error-card" onclick="revealError(this)">'
         '<p class="fill-answer" style="display:none">fix</p></div>', True),
        # o mecanismo `so_gen_nova` continua vivo e testado — hoje quem usa e o gap-fill,
        # que ainda tem 1 arquivo legado por consertar (juliana-marques).
        ('OK: fill-answer dentro de fill-item em aula LEGADA (familia ainda escopada)',
         '<script>function revealFill(c){c.classList.toggle("revealed");}</script>'
         '<div class="fill-item" onclick="revealFill(this)">'
         '<span class="fill-answer" style="display:none">resposta</span></div>', False),
        ('QUEBRADO: o mesmo fill-item, agora em aula com carimbo',
         '<meta name="alumni-gen" content="3">'
         '<script>function revealFill(c){c.classList.toggle("revealed");}</script>'
         '<div class="fill-item" onclick="revealFill(this)">'
         '<span class="fill-answer" style="display:none">resposta</span></div>', True),
        ('OK: fill-answer dentro de comp-question (stylesheet usa !important)',
         '<meta name="alumni-gen" content="3">'
         '<div class="error-card" onclick="revealError(this)"><div class="error-fix">a</div></div>'
         '<div class="comp-question" onclick="this.classList.toggle(\'revealed\')">'
         '<p class="fill-answer" style="display:none">resposta</p></div>', False),
    ]
    ok = True
    for nome, html, espera in casos:
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as tf:
            tf.write(html)
            tmp = tf.name
        teve = bool(falhas_no_arquivo(tmp))
        os.unlink(tmp)
        if teve != espera:
            ok = False
        print('  [%s] %s' % ('OK' if teve == espera else 'ERRO', nome))
    print('SELFTEST:', 'passou' if ok else 'FALHOU')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    arquivos = alvos(args)
    falhas = []
    for p in arquivos:
        falhas += falhas_no_arquivo(p)
    if falhas:
        print('GATE 10 — FALHOU: conteudo de reveal nasce escondido')
        for f in falhas:
            print('  ! ' + f)
        print('\nConserto: remova o display:none INLINE do alvo. A regra base do '
              'stylesheet (.comp-q .q-answer{display:none}) ja o esconde, e a regra '
              '.revealed o mostra no clique. NUNCA "conserte" escondendo de novo.')
        return 1
    print('GATE 10 — OK: %d arquivo(s), 0 alvo de reveal nascido escondido.' % len(arquivos))
    return 0


if __name__ == '__main__':
    sys.exit(main())
