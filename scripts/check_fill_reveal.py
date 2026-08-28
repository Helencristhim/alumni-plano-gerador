#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE 49 — O QUE O CLIQUE PROMETE MOSTRAR TEM DE APARECER NA TELA.

O DEFEITO
---------
    <span class="fill-blank"><span class="fill-blank">___</span>
                             <span class="fill-answer">is</span></span>

O `.fill-answer` nasceu DENTRO do `.fill-blank`. O CSS do modelo esconde o
espaco em branco quando o item e revelado (`.fill-item.revealed .fill-blank
{display:none}`) — e a resposta, sendo FILHA dele, some junto. A professora
clica, o `___` desaparece, e NADA aparece no lugar. Os seis itens do slide
"Fill in the Word" morrem, em aula, ao vivo.

Aconteceu nas aulas 5 a 20 da patricia-yamaguti-shimada (32 arquivos, professor
e aluno). Nasceu assim: nunca funcionou.

POR QUE OS GATES DE REVEAL QUE JA EXISTEM PASSAM RETO
-----------------------------------------------------
O GATE 10 (check_vocab_reveal.py) le HTML como TEXTO e procura alvo escondido
por classe. Aqui nao ha nada escondido a mais: o `.fill-answer` tem o mesmo
`display:none` de sempre, e a regra `.fill-item.revealed .fill-answer
{display:inline}` existe e casa. Estaticamente o arquivo esta CERTO. O que
quebra e a ARVORE — quem e filho de quem — e isso nao esta em nenhuma classe.

O GATE 28 (check_reveal_clica.py) clica de verdade, mas (a) so em elemento cujo
texto comeca com "Reveal ", e (b) mede "ALGUMA COISA mudou de estilo". Aqui algo
MUDA — o `.fill-blank` vai para `display:none`. O gate 28 aprovaria.

A DIFERENCA DESTE GATE: ele nao pergunta "mudou?", pergunta "O ALVO APARECEU?".
Mede a caixa (getBoundingClientRect) do elemento que devia surgir, com o slide
de verdade aberto no Chromium. Caixa de largura ou altura zero = o aluno nao ve
= FAIL, seja qual for o mecanismo (display, visibility, opacity, ancestral
escondido, texto vazio).

USO
---
    python3 scripts/check_fill_reveal.py <arquivos.html>   # os arquivos do PR
    python3 scripts/check_fill_reveal.py --selftest        # prova que o gate morde
    python3 scripts/check_fill_reveal.py --varre           # repo inteiro (sweeper)
"""
import os
import pathlib
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (gatilho, alvo que TEM de aparecer). Um par so entra aqui depois de medido no
# molde: o gate roda em milhares de arquivos e par nao verificado vira ruido.
PARES = [
    ('.fill-item', '.fill-answer, .fill-a'),
]

# Abre cada slide de verdade (o CSS esconde slide inativo, e alvo dentro de
# ancestral escondido mede caixa zero — o que daria falso positivo em massa).
# Depois clica no gatilho e mede a caixa do alvo. Sem heuristica de mecanismo:
# ou o elemento ocupa espaco na tela, ou nao ocupa.
JS = r"""(pares) => {
  const out = [];
  const slides = [...document.querySelectorAll('.slide')];
  const alvos = document.body.classList.contains('slide-mode') || slides.length
    ? slides : [document.body];
  for (const slide of alvos) {
    const gatilhos = [];
    for (const [gsel, asel] of pares)
      for (const g of slide.querySelectorAll(gsel)) gatilhos.push([g, asel]);
    if (!gatilhos.length) continue;
    // Torna ESTE slide o visivel. Guarda e devolve o estado, para nao contaminar
    // a medicao do proximo.
    const antes = slides.map(s => s.className);
    slides.forEach(s => s.classList.remove('active'));
    slide.classList.add('active');
    for (const [g, asel] of gatilhos) {
      const alvo = g.querySelector(asel);
      const rotulo = (g.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60);
      if (!alvo) {
        out.push({slide: slide.dataset.slide || '?', rotulo,
                  motivo: 'o gatilho nao tem o elemento de resposta dentro'});
        continue;
      }
      try { g.click(); } catch (e) {
        out.push({slide: slide.dataset.slide || '?', rotulo,
                  motivo: 'clicar estourou: ' + String(e).slice(0, 60)});
        continue;
      }
      const cx = alvo.getBoundingClientRect();
      if (cx.width <= 0 || cx.height <= 0) {
        const cs = getComputedStyle(alvo);
        let pai = alvo.parentElement, escondido = null;
        while (pai && pai !== document.body) {
          if (getComputedStyle(pai).display === 'none') {
            escondido = pai.tagName.toLowerCase() + '.' + (pai.className || '').toString().slice(0, 30);
            break;
          }
          pai = pai.parentElement;
        }
        out.push({slide: slide.dataset.slide || '?', rotulo,
                  motivo: escondido
                    ? ('a resposta esta DENTRO de um ancestral escondido (' + escondido + ')')
                    : ('a resposta nao ocupa espaco (display=' + cs.display +
                       ', visibility=' + cs.visibility + ', texto=' +
                       JSON.stringify((alvo.textContent || '').slice(0, 20)) + ')')});
      }
      try { g.click(); } catch (e) { /* fecha, se for toggle */ }
    }
    slides.forEach((s, i) => { s.className = antes[i]; });
  }
  return out;
}"""


def _tem_par(texto):
    return 'class="fill-item"' in texto or "class='fill-item'" in texto


def falhas(paths):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('GATE 49 NAO PODE RODAR: playwright ausente. '
              'Instale com `pip install playwright && python3 -m playwright install chromium`.',
              file=sys.stderr)
        sys.exit(2)   # 2 = gate impedido de rodar. NUNCA verde por omissao.

    seletores = [[g, a] for g, a in PARES]
    out = []
    with sync_playwright() as p:
        try:
            navegador = p.chromium.launch()
        except Exception as e:
            print('GATE 49 NAO PODE RODAR: chromium nao abre (%s)' % str(e)[:120], file=sys.stderr)
            sys.exit(2)
        pagina = navegador.new_page(viewport={'width': 1440, 'height': 900})
        pagina.on('dialog', lambda d: d.dismiss())
        for f in paths:
            try:
                pagina.goto('file://' + str(pathlib.Path(f).resolve()), timeout=30000)
                pagina.evaluate("() => { try { if (typeof enterSlideMode === 'function') "
                                "enterSlideMode(1); } catch (e) {} }")
                res = pagina.evaluate(JS, seletores)
            except Exception as e:
                if 'context was destroyed' in str(e):
                    pagina = navegador.new_page(viewport={'width': 1440, 'height': 900})
                    continue
                print('  aviso: %s nao pode ser medido (%s)' % (f, str(e)[:60]))
                continue
            rel = os.path.relpath(f, RAIZ) if os.path.abspath(f).startswith(RAIZ) else f
            for r in res:
                out.append('%s: slide %s, "%s" — %s'
                           % (rel, r['slide'], r['rotulo'], r['motivo']))
        navegador.close()
    return out


QUEBRADO = """<!doctype html><html><head><style>
.fill-item .fill-answer{display:none}
.fill-item.revealed .fill-blank{display:none}
.fill-item.revealed .fill-answer{display:inline}
</style></head><body>
<div class="slide active"><div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"My name
<span class="fill-blank"><span class="fill-blank">___</span><span class="fill-answer">is</span></span> Ana."</div></div></div>
<script>function revealFill(i){i.classList.toggle('revealed');}</script>
</body></html>"""

OK_IRMAOS = """<!doctype html><html><head><style>
.fill-item .fill-answer{display:none}
.fill-item.revealed .fill-blank{display:none}
.fill-item.revealed .fill-answer{display:inline}
</style></head><body>
<div class="slide active"><div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"My name
<span class="fill-blank">___</span><span class="fill-answer">is</span> Ana."</div></div></div>
<script>function revealFill(i){i.classList.toggle('revealed');}</script>
</body></html>"""

OK_SLIDE_INATIVO = """<!doctype html><html><head><style>
.slide{display:none}.slide.active{display:block}
.fill-item .fill-answer{display:none}
.fill-item.revealed .fill-blank{display:none}
.fill-item.revealed .fill-answer{display:inline}
</style></head><body>
<div class="slide"><div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"I
<span class="fill-blank">___</span><span class="fill-answer">am</span> here."</div></div></div>
<script>function revealFill(i){i.classList.toggle('revealed');}</script>
</body></html>"""


def selftest():
    """Prova que o gate REPROVA o aninhado e ACEITA os dois certos.

    O terceiro caso e o que separa este gate de uma medicao ingenua: o slide
    nasce INATIVO (`display:none` no proprio slide), como em todo material real.
    Medir sem abrir o slide daria caixa zero para TODO mundo — 3.373 arquivos de
    falso positivo.
    """
    casos = [
        ('QUEBRADO: .fill-answer aninhado dentro do .fill-blank', QUEBRADO, True),
        ('OK: .fill-answer irmao do .fill-blank (forma do modelo)', OK_IRMAOS, False),
        ('OK: mesma forma certa, em slide que nasce inativo', OK_SLIDE_INATIVO, False),
    ]
    erros = 0
    with tempfile.TemporaryDirectory() as d:
        for nome, html, deve_falhar in casos:
            p = os.path.join(d, 'caso.html')
            open(p, 'w', encoding='utf-8').write(html)
            falhou = bool(falhas([p]))
            ok = falhou == deve_falhar
            print('  [%s] %s' % ('ok' if ok else 'ERRO', nome))
            if not ok:
                erros += 1
    if erros:
        print('SELFTEST FALHOU: o gate parou de morder.', file=sys.stderr)
        return 1
    print('SELFTEST OK — reprova o aninhado e aceita as duas formas certas.')
    return 0


def todos_do_repo():
    saida = subprocess.run(['git', 'grep', '-l', 'class="fill-item"', '--', 'public/*.html'],
                           cwd=RAIZ, capture_output=True, text=True).stdout.split()
    return [os.path.join(RAIZ, p) for p in saida]


def main(argv):
    if '--selftest' in argv:
        return selftest()
    if '--varre' in argv:
        paths = todos_do_repo()
        print('varrendo o repo inteiro: %d arquivo(s) com .fill-item' % len(paths))
    else:
        paths = [a for a in argv if not a.startswith('--')]
        if not paths:
            print('uso: check_fill_reveal.py <arquivos.html> | --selftest | --varre')
            return 0
        paths = [p for p in paths if p.endswith('.html') and os.path.exists(p)]
        # Filtro barato de quem vale abrir no navegador. Nao e criterio: so tira
        # arquivo em que a classe nem aparece no texto.
        paths = [p for p in paths
                 if _tem_par(open(p, encoding='utf-8', errors='ignore').read())]
    if not paths:
        print('GATE 49: nenhum arquivo com exercicio de completar a medir.')
        return 0
    problemas = falhas(paths)
    if problemas:
        print('GATE 49 — O CLIQUE NAO MOSTRA A RESPOSTA (%d):' % len(problemas), file=sys.stderr)
        for p in problemas[:60]:
            print('  X ' + p, file=sys.stderr)
        if len(problemas) > 60:
            print('  ... e mais %d' % (len(problemas) - 60), file=sys.stderr)
        return 1
    print('GATE 49 OK — %d arquivo(s) medido(s) no Chromium, toda resposta aparece.' % len(paths))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
