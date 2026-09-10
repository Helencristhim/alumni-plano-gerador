#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pendura no hub o JS que preenche as barrinhas de % das ABAS SUPLEMENTARES.

PARA QUE SERVE
--------------
O `insert_hub_extras.py` insere as abas novas (Extra Practice / Living in the
USA / Gospel) e nao pode inserir JS -- e proposital: um snippet que traz funcao
nova e um snippet que pode quebrar o hub. Mas a Helen pediu (10/09/2026) que as
abas novas tenham a MESMA barrinha de % do Pre-class, "para sabermos o que ele
ja fez". Barra sem JS nao anda. Este script e a outra metade: escreve UM bloco
`<script>` no fim do <body>, depois das libs, e nada mais.

O QUE ELE GARANTE
-----------------
1. UM BLOCO SO, DELIMITADO. Entra entre marcadores. Rodar de novo SUBSTITUI o
   bloco (idempotente de verdade), nunca empilha uma segunda copia.

2. NAO TOCA NO PROGRESSO DAS AULAS. O `updateProgress()` do hub segue intacto:
   este bloco so o ENVOLVE (`window.updateProgress = ...`) e, depois que ele
   roda, calcula as abas novas em atributos `data-extra-*`, que sao de uso
   exclusivo delas. Barra do pacote, stamps, mini-barras `data-lesson-progress`
   e a chave `alumni-progress-<slug>` do dashboard continuam como estavam.

3. DEPOIS DAS LIBS. `lesson-progress.js` e `activity-sync.js` tambem envolvem o
   `updateProgress`. Entrando por ultimo, o bloco fica por FORA das duas: toda
   chamada delas (inclusive o `applyState` que restaura o estado vindo do
   Supabase noutro aparelho) passa por aqui e as barras novas se atualizam.

4. NAO INVENTA PERSISTENCIA. O que o aluno faz nas abas novas ja e salvo pelo
   `saveState()` do hub (localStorage) e pelo `activity-sync.js` (Supabase):
   os dois varrem o DOCUMENTO INTEIRO por classe de exercicio, nao por aula.
   Este script so LE o DOM para desenhar a barra.

USO
    python3 _build/model/patch_extras_progress.py --hub public/aluno/<slug>.html [--dry-run]
"""
import argparse
import re
import sys

ABRE = '<!-- ===== EXTRAS PROGRESS (abas suplementares) — inicio ===== -->'
FECHA = '<!-- ===== EXTRAS PROGRESS (abas suplementares) — fim ===== -->'

BLOCO = ABRE + '''
<script>
/* Barrinha de % das abas suplementares (Extra Practice / Living in the USA /
   Gospel). Mesma conta do Pre-class, em atributos proprios `data-extra-*`.
   Ver _build/model/patch_extras_progress.py. */
(function () {
  var ABAS = [
    { tab: 'xpractice', cards: '.lesson-card[id^="xp-lesson-"]' },
    { tab: 'uslife',    cards: '.lesson-card[id^="us-lesson-"]' },
    { tab: 'gospel',    cards: '.media-card-wrapper[data-media^="gs-song-"]' },
    { tab: 'expressions', cards: '.lesson-card[id^="ae-group-"]' }
  ];

  // MESMAS unidades que o updateProgress() do hub conta numa aula do Pre-class,
  // para que 60% numa aba queira dizer o mesmo que 60% numa aula.
  function unidades(card) {
    var total = 0, done = 0;
    card.querySelectorAll('.vocab-card-pc').forEach(function (v) { total++; if (v.classList.contains('listened')) done++; });
    card.querySelectorAll('.match-row').forEach(function (r) { total++; if (r.classList.contains('correct')) done++; });
    card.querySelectorAll('.blank-input').forEach(function (b) { total++; if (b.classList.contains('correct')) done++; });
    card.querySelectorAll('.quiz-item').forEach(function (q) { total++; if (q.querySelector('.quiz-option.correct')) done++; });
    card.querySelectorAll('.speech-card').forEach(function (s) { total++; if (s.querySelector('.speech-result.show')) done++; });
    card.querySelectorAll('.order-container').forEach(function (o) {
      total++;
      var itens = o.querySelectorAll('.order-item');
      if (itens.length && itens.length === o.querySelectorAll('.order-item.correct-order').length) done++;
    });
    card.querySelectorAll('.think-card').forEach(function (t) { total++; if (t.classList.contains('recorded')) done++; });
    // No Gospel o "mark as done" da musica e uma unidade: e ele que diz que o
    // aluno trabalhou a musica, e nao so acertou as lacunas.
    var cb = card.querySelector(':scope > .media-check input[type="checkbox"]');
    if (cb) { total++; if (cb.checked) done++; }
    return { total: total, done: done };
  }

  function chave(card) { return card.id || card.getAttribute('data-media') || ''; }

  function updateExtrasProgress() {
    ABAS.forEach(function (aba) {
      var feitos = 0, totais = 0;
      document.querySelectorAll(aba.cards).forEach(function (card) {
        var u = unidades(card);
        feitos += u.done; totais += u.total;
        var pct = u.total > 0 ? Math.round(u.done / u.total * 100) : 0;
        var k = chave(card);
        var barra = document.querySelector('.mini-bar-fill[data-extra-progress="' + k + '"]');
        if (barra) barra.style.width = pct + '%';
        var rotulo = document.querySelector('.mini-percent[data-extra-pct="' + k + '"]');
        if (rotulo) rotulo.textContent = pct + '%';
      });
      var pctAba = totais > 0 ? Math.round(feitos / totais * 100) : 0;
      var f = document.querySelector('.mini-bar-fill[data-extra-tab="' + aba.tab + '"]');
      if (f) f.style.width = pctAba + '%';
      var p = document.querySelector('[data-extra-tab-pct="' + aba.tab + '"]');
      if (p) p.textContent = pctAba + '%';
      var d = document.querySelector('[data-extra-tab-done="' + aba.tab + '"]');
      if (d) d.textContent = feitos;
      var t = document.querySelector('[data-extra-tab-total="' + aba.tab + '"]');
      if (t) t.textContent = totais;
      // Chave PROPRIA. A do dashboard (alumni-progress-<slug>) nao e tocada:
      // as abas suplementares sao autoestudo e nao contam como aula dada.
      try {
        localStorage.setItem('alumni-extras-' + (window.STUDENT_SLUG || '') + '-' + aba.tab,
          JSON.stringify({ feitos: feitos, total: totais, pct: pctAba }));
      } catch (e) {}
    });
  }
  window.updateExtrasProgress = updateExtrasProgress;

  // Envolve o updateProgress QUE JA EXISTIR (hub + libs). Nunca o substitui:
  // chama o de dentro, devolve o retorno dele e so entao desenha as abas novas.
  if (typeof window.updateProgress === 'function') {
    var _orig = window.updateProgress;
    window.updateProgress = function () {
      var r = _orig.apply(this, arguments);
      try { updateExtrasProgress(); } catch (e) { console.warn('extras-progress:', e); }
      return r;
    };
  }

  // Rede de seguranca: exercicio que nao passe pelo updateProgress (um check
  // que so muda classe, o checkbox da musica) mesmo assim redesenha a barra.
  document.addEventListener('click', function (ev) {
    var alvo = ev.target && ev.target.closest ? ev.target.closest('#tab-xpractice, #tab-uslife, #tab-gospel, #tab-expressions') : null;
    if (alvo) setTimeout(updateExtrasProgress, 60);
  }, true);
  document.addEventListener('change', function (ev) {
    var alvo = ev.target && ev.target.closest ? ev.target.closest('#tab-xpractice, #tab-uslife, #tab-gospel, #tab-expressions') : null;
    if (alvo) setTimeout(updateExtrasProgress, 60);
  }, true);

  function inicia() { updateExtrasProgress(); setTimeout(updateExtrasProgress, 1200); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', inicia);
  else inicia();
})();
</script>
''' + FECHA


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hub', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    with open(args.hub, encoding='utf-8') as f:
        html = f.read()
    original = html

    # Sem as abas novas o bloco nao tem o que medir: recusa em vez de sujar o hub.
    if 'data-extra-tab=' not in html:
        sys.exit('ERRO: %s nao tem as abas suplementares com barra (data-extra-tab).' % args.hub)

    velho = re.search(re.escape(ABRE) + r'.*?' + re.escape(FECHA), html, re.S)
    if velho:
        html = html[:velho.start()] + BLOCO + html[velho.end():]
        acao = 'substituido'
    else:
        # Depois das libs, imediatamente antes de </body>: e o que garante que o
        # wrap fique por fora do lesson-progress.js e do activity-sync.js.
        if '</body>' not in html:
            sys.exit('ERRO: %s nao tem </body>.' % args.hub)
        i = html.rindex('</body>')
        html = html[:i] + BLOCO + '\n' + html[i:]
        acao = 'inserido'

    # O hub so pode crescer, e nada fora do bloco pode ter mudado.
    # O \n? no fim tira tambem a quebra que a insercao acrescenta: sem ele o
    # proprio separador acusaria "mudou fora do bloco" na primeira rodada.
    fora = re.escape(ABRE) + r'.*?' + re.escape(FECHA) + r'\n?'
    fora_antes = re.sub(fora, '', original, flags=re.S)
    fora_depois = re.sub(fora, '', html, flags=re.S)
    if fora_antes.strip() != fora_depois.strip():
        sys.exit('ERRO: o patch alterou algo FORA do bloco. Nao gravado.')

    print('%s: bloco %s (%+d bytes)' % (args.hub, acao, len(html) - len(original)))
    if args.dry_run:
        return
    with open(args.hub, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    main()
