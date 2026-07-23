#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE 10 — VOCAB REVEAL QUE NASCE ESCONDIDO NUM REVEAL 100% CSS.

O DEFEITO
---------
Os cards de "Vocabulary Reveal" (IN CLASS) escondem a PALAVRA num `.vocab-back` e
a mostram no clique. Existem DOIS mecanismos de reveal no roster, e a diferenca
entre eles decide se `style="display:none"` no back e correto ou e um bug:

  A) REVEAL 100% CSS  — `revealVocab()` so faz `card.classList.add('revealed')`;
     quem mostra o back e o CSS (`.revealed .vocab-back{opacity:1;max-height:300px}`).
     Se o back nasce com `display:none` INLINE, o CSS de opacity/max-height NAO
     vence `display:none` (regra de especificidade do inline) -> a palavra NUNCA
     aparece. BUG. (Foi o caso do luiz-bressane, aulas 7 e 8: o professor clicava
     e nada acontecia.)

  B) REVEAL POR JS    — `revealVocab()` faz `back.style.display=''` ao abrir.
     Isso REMOVE o `display:none` inline em runtime -> a palavra aparece. Aqui o
     `display:none` inicial e o estado escondido CORRETO. NAO e bug.

Este gate distingue os dois: so reprova o back nascido-escondido quando o reveal
daquele arquivo e 100% CSS (nao ha atribuicao a `.style.display` no corpo do
`revealVocab`). Assim os arquivos do mecanismo B (que tem `display:none` de
proposito e funcionam) passam, e so o padrao realmente quebrado — e sua
reintroducao futura — e barrado.

Por que "born hidden" cobre display:none / visibility:hidden / opacity:0
-----------------------------------------------------------------------
Num reveal 100% CSS, o `.revealed .vocab-back` so seta opacity/max-height. Um
inline `display:none` OU `visibility:hidden` OU `opacity:0` no back sobrevive ao
`.revealed` (inline vence stylesheet) e mantem a palavra escondida. Os tres sao,
portanto, o mesmo bug. (Espelha a filosofia da REGRA 2.1: tarefa/resposta nao
pode nascer escondida.)

    python3 scripts/check_vocab_reveal.py                 # varre o repo (CI)
    python3 scripts/check_vocab_reveal.py a.html b.html   # so estes arquivos
    python3 scripts/check_vocab_reveal.py --selftest      # prova que o gate morde
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# back nascido escondido: um dos tres jeitos de esconder via style inline.
RE_BACK_HIDDEN = re.compile(
    r'class="vocab-back"[^>]*\bstyle="[^"]*'
    r'(?:display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d]))',
    re.IGNORECASE,
)


def corpo_revealvocab(html):
    """Extrai o corpo de function revealVocab(...) por balanceamento de chaves.
    Retorna a string do corpo, ou None se a funcao nao existir no arquivo."""
    m = re.search(r'function\s+revealVocab\s*\([^)]*\)\s*\{', html)
    if not m:
        return None
    i = m.end() - 1  # aponta para o '{' de abertura
    depth = 0
    for j in range(i, len(html)):
        c = html[j]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return html[i:j + 1]
    return html[i:]  # sem fechamento (HTML corrompido) — devolve o resto


def reveal_e_css_puro(html):
    """True se o reveal deste arquivo e 100% CSS (revealVocab NAO seta display).
    False se ele seta .style.display (mecanismo B/hibrido) ou se nao ha reveal."""
    body = corpo_revealvocab(html)
    if body is None:
        return False  # sem revealVocab -> nao ha o defeito deste gate
    return re.search(r'\.style\.display', body) is None


def falhas_no_arquivo(path):
    """Lista de mensagens de falha para um arquivo (vazia = ok)."""
    with open(path, encoding='utf-8', errors='ignore') as f:
        html = f.read()
    if not reveal_e_css_puro(html):
        return []  # mecanismo B/hibrido, ou sem reveal — display:none e ok
    n = len(RE_BACK_HIDDEN.findall(html))
    if n:
        rel = os.path.relpath(path, RAIZ)
        return ['%s: %d card(s) .vocab-back nascem escondidos (display:none/'
                'visibility:hidden/opacity:0) num reveal 100%% CSS -> a palavra '
                'nunca aparece no clique' % (rel, n)]
    return []


def alvos(args):
    if args:
        return [a for a in args if not a.startswith('--')]
    out = []
    for sub in ('public/professor', 'public/aluno'):
        out += glob.glob(os.path.join(RAIZ, sub, '*.html'))
    return sorted(out)


def selftest():
    """Prova, em memoria, que o gate REPROVA o padrao quebrado e ACEITA o certo.
    Roda sem depender de nenhum arquivo do repo."""
    import tempfile
    quebrado = ('<script>function revealVocab(card){card.classList.add("revealed");}'
                '</script><div class="vocab-back" style="display:none">word</div>')
    css_ok = ('<script>function revealVocab(card){card.classList.add("revealed");}'
              '</script><div class="vocab-back">word</div>')
    js_ok = ('<script>function revealVocab(card){var b=card.querySelector(".vocab-back");'
             'b.style.display="";}</script><div class="vocab-back" style="display:none">w</div>')
    casos = [('quebrado (CSS puro + hidden)', quebrado, True),
             ('ok (CSS puro, back visivel)', css_ok, False),
             ('ok (JS seta display, hidden inicial)', js_ok, False)]
    ok = True
    for nome, html, espera_falha in casos:
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as tf:
            tf.write(html)
            tmp = tf.name
        teve_falha = bool(falhas_no_arquivo(tmp))
        os.unlink(tmp)
        marca = 'OK' if teve_falha == espera_falha else 'ERRO'
        if teve_falha != espera_falha:
            ok = False
        print('  [%s] %s (esperava falha=%s, obteve=%s)' % (marca, nome, espera_falha, teve_falha))
    print('SELFTEST:', 'passou' if ok else 'FALHOU')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    falhas = []
    arquivos = alvos(args)
    for p in arquivos:
        falhas += falhas_no_arquivo(p)
    if falhas:
        print('GATE 10 — FALHOU: vocab reveal nasce escondido num reveal 100%% CSS')
        for f in falhas:
            print('  ! ' + f)
        print('\nConserto: remova o style inline que esconde o .vocab-back (o CSS '
              '.revealed .vocab-back ja mostra a palavra). NUNCA "conserte" '
              'escondendo — a palavra tem de aparecer no clique.')
        return 1
    print('GATE 10 — OK: %d arquivo(s) checados, 0 vocab reveal nascido escondido '
          'em reveal 100%% CSS.' % len(arquivos))
    return 0


if __name__ == '__main__':
    sys.exit(main())
