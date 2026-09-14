/* ═══════════════════════════════════════════════════════════════
   GAP DRAG — gap-fill do IN CLASS com banco: arrastar, tocar ou digitar.

   É o gap-fill interativo que a professora pediu na aula 1 da Helena Andrade (PR #2614,
   11/09/2026), tirado do arquivo da aula e posto aqui para valer em toda aula que
   carregar este script. Comportamento, classes (ic-gap*) e textos são OS MESMOS daquela
   aula (REGRA 11.9: componente repetido tem de ser igual em todas as instâncias).

   A diferença é só DE ONDE vem o markup: lá ele foi escrito no HTML; aqui é montado em
   runtime a partir do que o builder emite para o bloco "gapfill":
     .ic-card > .ic-gaptext > .ic-blank[data-answer] + .ic-bank > .ic-b
   Cada .ic-blank ganha o campo, cada .ic-b vira arrastável, e o cartão ganha a dica e a
   barra Check / Reset / placar. O .ic-blank continua no .ic-gaptext (GATE de padrão).

   Não lê nem escreve em nenhuma função, classe ou estado do shell — por isso não entra
   no contador de progresso nem no saveState, igual à aula 1.

   Aula que já traz a versão embutida (define icGapInit) é deixada em paz.
   Carregar antes de </body>.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  if (window.__GAP_DRAG_LOADED || typeof window.icGapInit === 'function') return;
  window.__GAP_DRAG_LOADED = true;

  var CSS = [
    '.ic-gapslot { position: relative; display: inline-block; min-width: 9.5ch; border-bottom: 2px solid var(--accent); text-align: center; padding: 0 .3rem; transition: background .15s, border-color .15s; }',
    '.ic-gapslot .ic-n { font-size: .6rem; font-weight: 700; color: var(--text-dim); vertical-align: super; margin-right: .1rem; }',
    '.ic-gapin { width: 9.5ch; max-width: 100%; border: 0; background: transparent; font: inherit; font-weight: 700; color: var(--accent); text-align: center; padding: .05rem 0; outline: none; }',
    '.ic-gapslot.ic-over { background: var(--accent-dim); }',
    '.ic-gapslot.ic-ok { border-bottom-color: var(--success); }',
    '.ic-gapslot.ic-ok .ic-gapin { color: var(--success); }',
    '.ic-gapslot.ic-no { border-bottom-color: var(--danger); }',
    '.ic-gapslot.ic-no .ic-gapin { color: var(--danger); }',
    '.ic-bank .ic-b.ic-gapchip { cursor: grab; user-select: none; transition: opacity .15s, box-shadow .15s, transform .12s; }',
    '.ic-bank .ic-b.ic-gapchip:active { cursor: grabbing; }',
    '.ic-bank .ic-b.ic-gapchip.ic-sel { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 2px 10px rgba(0, 0, 0, .18); transform: translateY(-1px); }',
    '.ic-bank .ic-b.ic-gapchip.ic-used { opacity: .3; }',
    '.ic-gaphint { font-size: .75rem; color: var(--text-dim); margin: .7rem 0 0; }',
    '.ic-gapbar { display: flex; align-items: center; gap: .6rem; margin-top: .8rem; flex-wrap: wrap; }',
    '.ic-gapbtn { background: var(--accent); color: #fff; border: none; border-radius: 8px; padding: .45rem 1.1rem; font-size: .85rem; font-weight: 600; font-family: inherit; cursor: pointer; }',
    '.ic-gapbtn.ic-gapghost { background: transparent; color: var(--accent); border: 1.5px solid var(--accent); }',
    '.ic-gapscore { font-size: .85rem; font-weight: 700; color: var(--accent); margin-left: auto; }',
    '.slide-dark .ic-gapin, .slide-dark .ic-gapscore { color: #fff; }',
    '.ic-gapchip:focus-visible, .ic-gapbtn:focus-visible, .ic-gapin:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }',
    '@media (prefers-reduced-motion: reduce) { .ic-gapslot, .ic-bank .ic-b.ic-gapchip { transition: none; } }'
  ].join('\n');

  function icGapNorm(s) {
    return String(s == null ? '' : s).toLowerCase()
      .replace(/[‘’ʼ]/g, "'")
      .replace(/[^a-z0-9'\- ]/g, '')
      .replace(/-/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }
  function icGapCard(el) { return el.closest('.ic-card'); }
  function icGapSync(card) {
    var usadas = {};
    card.querySelectorAll('.ic-gapin').forEach(function (inp) {
      var v = icGapNorm(inp.value);
      if (v) usadas[v] = (usadas[v] || 0) + 1;
    });
    card.querySelectorAll('.ic-gapchip').forEach(function (chip) {
      var v = icGapNorm(chip.dataset.w);
      if (usadas[v] > 0) { usadas[v]--; chip.classList.add('ic-used'); }
      else chip.classList.remove('ic-used');
    });
  }
  function icGapClearSel(card) {
    card.querySelectorAll('.ic-gapchip.ic-sel').forEach(function (c) { c.classList.remove('ic-sel'); });
  }
  function icGapFit(inp) {
    /* "towage assets" nao cabe em largura fixa: o campo cresce com o que esta escrito. */
    var ch = Math.max(9.5, String(inp.value || '').length + 1.5);
    inp.style.width = ch + 'ch';
  }
  function icGapPut(slot, palavra) {
    var inp = slot.querySelector('.ic-gapin');
    if (!inp) return;
    inp.value = palavra;
    icGapFit(inp);
    slot.classList.remove('ic-ok', 'ic-no');
    icGapSync(icGapCard(slot));
  }
  function icGapCheck(btn) {
    var card = icGapCard(btn), acertos = 0, total = 0;
    card.querySelectorAll('.ic-gapslot').forEach(function (slot) {
      var inp = slot.querySelector('.ic-gapin'), v = icGapNorm(inp ? inp.value : '');
      total++;
      slot.classList.remove('ic-ok', 'ic-no');
      if (!v) return;
      if (v === icGapNorm(slot.dataset.answer)) { slot.classList.add('ic-ok'); acertos++; }
      else slot.classList.add('ic-no');
    });
    var out = card.querySelector('.ic-gapscore');
    if (out) out.textContent = acertos + ' / ' + total;
  }
  function icGapReset(btn) {
    var card = icGapCard(btn);
    card.querySelectorAll('.ic-gapslot').forEach(function (slot) {
      slot.classList.remove('ic-ok', 'ic-no');
      var inp = slot.querySelector('.ic-gapin');
      if (inp) { inp.value = ''; icGapFit(inp); }
    });
    var out = card.querySelector('.ic-gapscore');
    if (out) out.textContent = '';
    icGapClearSel(card);
    icGapSync(card);
  }

  /* Monta, a partir do markup do builder, o markup que a aula 1 traz escrito. */
  function icGapUpgrade(card) {
    var text = card.querySelector('.ic-gaptext'), bank = card.querySelector('.ic-bank');
    if (!text || !bank || card.dataset.icGapReady) return;
    var blanks = text.querySelectorAll('.ic-blank');
    if (!blanks.length) return;
    card.dataset.icGapReady = '1';
    var comGabarito = true;
    blanks.forEach(function (b) {
      var n = b.querySelector('.ic-n'), num = n ? n.textContent.trim() : '';
      if (!b.hasAttribute('data-answer')) comGabarito = false;
      b.classList.add('ic-gapslot');
      b.setAttribute('data-n', num);
      b.innerHTML = '';
      if (n) b.appendChild(n);
      var inp = document.createElement('input');
      inp.className = 'ic-gapin'; inp.type = 'text';
      inp.setAttribute('autocomplete', 'off'); inp.setAttribute('spellcheck', 'false');
      inp.setAttribute('aria-label', 'gap ' + num);
      b.appendChild(inp);
    });
    bank.querySelectorAll('.ic-b').forEach(function (chip) {
      chip.classList.add('ic-gapchip');
      chip.setAttribute('draggable', 'true');
      chip.setAttribute('tabindex', '0');
      chip.setAttribute('role', 'button');
      chip.dataset.w = chip.textContent.trim();
    });
    var hint = document.createElement('p');
    hint.className = 'ic-gaphint';
    hint.textContent = 'Drag a word into a gap, or tap a word and then a gap. You can also type the answer.';
    bank.insertAdjacentElement('afterend', hint);
    var bar = document.createElement('div');
    bar.className = 'ic-gapbar';
    /* Sem gabarito no HTML (aula antiga) nao ha o que conferir: fica so o Reset. */
    bar.innerHTML = (comGabarito ? '<button type="button" class="ic-gapbtn">Check</button>' : '') +
      '<button type="button" class="ic-gapbtn ic-gapghost">Reset</button>' +
      '<span class="ic-gapscore" aria-live="polite"></span>';
    hint.insertAdjacentElement('afterend', bar);
    bar.querySelectorAll('.ic-gapbtn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (btn.classList.contains('ic-gapghost')) icGapReset(btn); else icGapCheck(btn);
      });
    });
  }

  function icGapInit() {
    if (!document.getElementById('ic-gap-css')) {
      var st = document.createElement('style');
      st.id = 'ic-gap-css'; st.textContent = CSS;
      document.head.appendChild(st);
    }
    document.querySelectorAll('.ic-card').forEach(icGapUpgrade);
    document.querySelectorAll('.ic-gapchip').forEach(function (chip) {
      if (chip.dataset.icBound) return;
      chip.dataset.icBound = '1';
      function escolher() {
        var card = icGapCard(chip), jaEstava = chip.classList.contains('ic-sel');
        icGapClearSel(card);
        if (!jaEstava) chip.classList.add('ic-sel');
      }
      chip.addEventListener('click', escolher);
      chip.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); e.stopPropagation(); escolher(); }
      });
      chip.addEventListener('dragstart', function (e) {
        e.dataTransfer.setData('text/plain', chip.dataset.w);
        e.dataTransfer.effectAllowed = 'copy';
        icGapClearSel(icGapCard(chip));
        chip.classList.add('ic-sel');
      });
      chip.addEventListener('dragend', function () { icGapClearSel(icGapCard(chip)); });
    });
    document.querySelectorAll('.ic-gapslot').forEach(function (slot) {
      if (slot.dataset.icBound) return;
      slot.dataset.icBound = '1';
      slot.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'copy';
        slot.classList.add('ic-over');
      });
      slot.addEventListener('dragleave', function () { slot.classList.remove('ic-over'); });
      slot.addEventListener('drop', function (e) {
        e.preventDefault();
        slot.classList.remove('ic-over');
        var w = e.dataTransfer.getData('text/plain');
        if (w) icGapPut(slot, w);
        icGapClearSel(icGapCard(slot));
      });
      slot.addEventListener('click', function () {
        var card = icGapCard(slot), sel = card.querySelector('.ic-gapchip.ic-sel');
        if (sel) { icGapPut(slot, sel.dataset.w); icGapClearSel(card); }
      });
      var inp = slot.querySelector('.ic-gapin');
      if (inp) {
        inp.addEventListener('input', function () {
          slot.classList.remove('ic-ok', 'ic-no');
          icGapFit(inp);
          icGapSync(icGapCard(slot));
        });
        /* Setas e espaco digitados no campo sao texto, nao navegacao de slide. */
        inp.addEventListener('keydown', function (e) { e.stopPropagation(); });
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', icGapInit);
  else icGapInit();
})();
