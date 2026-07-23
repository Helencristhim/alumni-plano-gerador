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

# (classe do alvo escondido, classes possiveis do card clicavel que o contem)
FAMILIAS = [
    ('vocab-back', ('vocab-card-ic', 'vocab-card')),   # a PALAVRA (Vocabulary Reveal)
    ('q-answer', ('comp-q',)),                          # a RESPOSTA (comprehension)
    ('error-fix', ('error-card',)),                     # a CORRECAO (Spot the Error)
]

# nasce escondido: um dos tres jeitos de esconder via style inline.
_HIDE = r'(?:display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d]))'


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
    falhas = []
    for alvo, pais in FAMILIAS:
        rx = re.compile(r'class="%s"[^>]*\bstyle="[^"]*%s' % (re.escape(alvo), _HIDE),
                        re.IGNORECASE)
        quebrados = 0
        for m in rx.finditer(html):
            # amarra ESTA instancia ao card clicavel que a contem
            k = -1
            for pai in pais:
                p = html.rfind('<div class="%s' % pai, 0, m.start())
                if p > k:
                    k = p
            onclick = ''
            if k != -1:
                tag = html[k:html.find('>', k) + 1]
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
