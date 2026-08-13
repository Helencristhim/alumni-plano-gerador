/* ============================================================================
   KIDS POST-CLASS — o SLOT (abrir, fechar, um percurso por vez).

   PROVENIÊNCIA: copiado do artefato "Dante Blecker Gregory · Kids A2 ·
   Professor View" (13/08/2026) — bloco "Post-class: CARGA SOB DEMANDA". O que
   mudou: o artefato prendia os cards com addEventListener('[data-post]') e as
   abas com data-tab; aqui o card chama enterPostMode(N) no onclick, que é a
   convenção do shell (enterSlideMode) e sobrevive a card emitido pelo builder.

   UM PERCURSO POR VEZ NO DOM. Os percursos compartilham ~24 ids (starCount,
   s-story, bb, ck...). Abrir um esvazia o outro: assim os ids nunca se cruzam e
   nenhuma das duas peças precisou ser reescrita. Custo declarado: trocar de
   percurso reinicia aquele percurso.

   Injetado pelo builder SÓ quando model==kids e a aula tem postclass.html.
   Adulto nunca vê este arquivo (memória nao-tocar-adulto).
   ============================================================================ */
(function () {
  'use strict';

  function parar() {
    try { if (typeof stopAllAudio === 'function') stopAllAudio(); } catch (e) {}
    try { if ('speechSynthesis' in window) { window.speechSynthesis.resume(); window.speechSynthesis.cancel(); } } catch (e) {}
  }

  var aberto = null;

  /* Abre o percurso N em tela cheia. O CSS (body.pc-mode) esconde logo-bar,
     main-content e slides-wrapper — o percurso ocupa a tela como o deck. */
  function enterPostMode(n) {
    n = String(n);
    var POSTS = window.PV_POSTS || {};
    if (!POSTS[n]) return;
    parar();
    if (aberto !== n) {
      var roots = document.querySelectorAll('.pv-post');
      for (var i = 0; i < roots.length; i++) roots[i].innerHTML = '';
      var alvo = document.getElementById('pc-root-' + n);
      if (!alvo) return;
      alvo.innerHTML = POSTS[n].html;
      /* innerHTML não executa <script>: o JS do percurso entra por um nó novo. */
      var s = document.createElement('script');
      s.textContent = POSTS[n].js;
      alvo.appendChild(s);
      var nome = document.getElementById('pv-post-nome');
      if (nome) nome.textContent = POSTS[n].titulo || '';
      aberto = n;
    }
    document.body.classList.add('pc-mode');
    window.scrollTo(0, 0);
  }

  function exitPostMode() {
    parar();
    document.body.classList.remove('pc-mode');
    window.scrollTo(0, 0);
  }

  window.enterPostMode = enterPostMode;
  window.exitPostMode = exitPostMode;

  /* MESMA REGRA DO slide-mode (REGRA 2, aba IN CLASS): trocar de aba NUNCA pode
     deixar o modo tela-cheia ligado. Sem isto, sair do percurso pela aba deixava
     o hub invisível atrás de um percurso que continuava por cima. */
  var _switchTab = window.switchTab;
  if (typeof _switchTab === 'function') {
    window.switchTab = function () {
      document.body.classList.remove('pc-mode');
      return _switchTab.apply(this, arguments);
    };
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('pc-mode')) exitPostMode();
  });

  function wire() {
    var sair = document.getElementById('pv-post-sair');
    if (sair) sair.addEventListener('click', exitPostMode);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire);
  else wire();
})();
