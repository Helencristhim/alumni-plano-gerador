#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ordering.py — o exercicio de ordenar frases COM O DEDO (Pre-class, Stage 2).

O QUE ESTAVA ERRADO
-------------------
Feedback do Ricardo Wertheim: "seria interessante se desse pra arrastar as frases pra
colocar em ordem, ou numerar, ao inves de ser com setinha".

Arrastar E numerar ja existiam — e o "Check Order" sempre aceitou os tres caminhos
(arrastar, numerar por clique, ou os dois). O que faltava era ARRASTAR NO CELULAR:

  |                    | desktop | celular (dedo) |
  | arrastar reordena  |   sim   |      NAO       |

Nao era bug de codigo: `draggable="true"` e a HTML5 Drag and Drop API, que nasce presa a
evento de MOUSE. Dedo nunca dispara `dragstart`. No telefone, arrastar simplesmente nao
acontecia — e o toque caia no onclick e NUMERAVA o card, que para quem estava tentando
arrastar parece defeito. Sobrava a seta, medindo 28x28 px (a REGRA 25 exige 44x44). Ou
seja: no celular so funcionava o alvo mais dificil de acertar da tela.

O CONSERTO
----------
1. POINTER EVENTS no lugar do drag do HTML5: `pointerdown/move/up` valem para mouse E
   dedo com o MESMO codigo. O `draggable` fica onde esta (nao atrapalha, e continua
   servindo o desktop se o pointer falhar).
2. ALCA (`.order-grip`) para pegar o card. Nao e enfeite: sem ela, arrastar para cima e
   para baixo com o dedo BRIGA com a rolagem da pagina — o navegador nao tem como saber
   se voce quer mover o card ou rolar a tela. A alca resolve porque so ela leva
   `touch-action:none`; o resto do card continua rolando e continua clicavel para numerar.
   E ela e o unico alvo de 44x44 que o exercicio ganha de graca.
3. SETA de 28 -> 44 px (REGRA 25). Ela FICA: e o caminho acessivel, por teclado e para
   quem nao consegue arrastar.
4. Uma linha dizendo os tres gestos. A numeracao por toque existia e NADA na tela
   contava — e ela e a unica que funciona em qualquer lugar.

NADA E REMOVIDO. `moveItem`, `selectOrderItem` e `checkOrder` continuam iguais (REGRA 12:
nunca remover/renomear funcao existente). O que entra e aditivo.
"""
import re
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import htmlpatch  # noqa: E402

GRIP = ('<span class="order-grip" onclick="event.stopPropagation()" aria-hidden="true">'
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">'
        '<circle cx="9" cy="6" r="1.6"/><circle cx="15" cy="6" r="1.6"/>'
        '<circle cx="9" cy="12" r="1.6"/><circle cx="15" cy="12" r="1.6"/>'
        '<circle cx="9" cy="18" r="1.6"/><circle cx="15" cy="18" r="1.6"/>'
        '</svg></span>')

HINT = ('<p class="order-hint">Drag by the handle, use the arrows, '
        'or tap the sentences in the right order.</p>')

CSS = """/* === ORDER: arrastar com o dedo (pointer events) === */
.order-grip { display:flex;align-items:center;justify-content:center;flex:0 0 44px;width:44px;height:44px;margin:-.7rem -.4rem -.7rem -.8rem;color:var(--text-dim);cursor:grab;touch-action:none;border-radius:8px; }
.order-grip:hover { color:var(--accent);background:var(--accent-dim); }
.order-grip:active { cursor:grabbing; }
.order-item.dragging { opacity:.65;border-color:var(--accent);box-shadow:0 6px 18px rgba(0,0,0,.14); }
.order-hint { font-size:.75rem;color:var(--text-dim);margin:0 0 .5rem; }
.order-item.correct-order .order-grip { opacity:.35;cursor:default; }"""

JS = """// ===== ORDERING: arrastar com MOUSE e com DEDO (pointer events) =====
// O draggable="true" do HTML5 so responde a mouse — no celular nao acontecia nada.
// Pointer events cobrem os dois com o mesmo codigo. Arrasta-se pela ALCA (.order-grip),
// que e a unica coisa com touch-action:none: assim o card continua rolando a pagina e
// continua clicavel para numerar. Ver _build/model/ordering.py.
(function () {
  var drag = null;
  function items(c) { return Array.prototype.slice.call(c.querySelectorAll('.order-item')); }
  document.addEventListener('pointerdown', function (e) {
    var grip = e.target.closest && e.target.closest('.order-grip');
    if (!grip) return;
    var item = grip.closest('.order-item');
    if (!item || item.classList.contains('correct-order')) return;
    var box = item.closest('.order-container');
    if (!box) return;
    e.preventDefault();
    drag = { item: item, box: box };
    item.classList.add('dragging');
    try { grip.setPointerCapture(e.pointerId); } catch (err) {}
  });
  document.addEventListener('pointermove', function (e) {
    if (!drag) return;
    e.preventDefault();
    // A POSICAO SAI DO PONTO MEDIO DOS VIZINHOS, nao de "trocar com quem esta embaixo
    // do dedo". Trocando de a um, o card anda UMA casa por vizinho ATRAVESSADO e fica
    // para tras do dedo (medido: dedo andou 2 posicoes, card andou 1). Aqui a posicao e
    // recalculada a cada movimento, entao o card fica exatamente onde o dedo esta.
    var outros = items(drag.box).filter(function (x) { return x !== drag.item; });
    var pos = outros.length;
    for (var i = 0; i < outros.length; i++) {
      var r = outros[i].getBoundingClientRect();
      if (e.clientY < r.top + r.height / 2) { pos = i; break; }
    }
    if (outros[pos]) drag.box.insertBefore(drag.item, outros[pos]);
    else drag.box.appendChild(drag.item);
  });
  function fim() { if (!drag) return; drag.item.classList.remove('dragging'); drag = null; }
  document.addEventListener('pointerup', fim);
  document.addEventListener('pointercancel', fim);
})();"""


def upgrade(s):
    """Aplica o conserto num hub. Idempotente. Devolve (html, nº de itens que ganharam alça)."""
    if 'order-item' not in s:
        return s, 0

    # 1) alça em cada item (antes do .order-num, que é o primeiro filho hoje)
    n = [0]

    def _grip(m):
        # A ALCA VEM DEPOIS DA TAG, entao o guarda tem de olhar para a FRENTE do match.
        # Olhar so para m.group(0) (a tag de abertura) nunca ve a alca que ja esta la, e
        # cada nova rodada empilha outra. `m.string` e o texto sendo varrido.
        if 'order-grip' in m.string[m.end():m.end() + 60]:
            return m.group(0)
        n[0] += 1
        return m.group(0) + GRIP

    s = re.sub(r'<div class="order-item"[^>]*>', _grip, s)

    # 2) a linha que conta os três gestos, antes de cada container
    def _hint(m):
        antes = m.string[max(0, m.start() - 260):m.start()]
        return m.group(0) if 'order-hint' in antes else HINT + '\n      ' + m.group(0)

    s = re.sub(r'<div class="order-container"[^>]*>', _hint, s)

    # 3) alvo da seta: 28 -> 44 px (REGRA 25). Regra existente, editada no lugar.
    s = s.replace('min-height:28px;min-width:28px', 'min-height:44px;min-width:44px')

    # 4) CSS e JS
    if '.order-grip {' not in s:
        s = s.replace('</style>', CSS + '\n</style>', 1)
    if 'ORDERING: arrastar com MOUSE' not in s:
        # NUNCA "antes do ultimo </script>": o arquivo pode terminar com <script src=...>,
        # e conteudo inline de script com src o navegador IGNORA (ver htmlpatch.py).
        s = htmlpatch.append_to_inline_script(s, JS)
    return s, n[0]
