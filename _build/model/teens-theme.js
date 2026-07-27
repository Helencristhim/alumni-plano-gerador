/* ============================================================================
   TEENS-THEME.JS — injetado pelo builder SOMENTE quando existe teens-theme.js e
   model==teens (analogo ao kids-theme.js). NUNCA entra no material adulto nem no
   kids => caminho do adulto intocado (memoria nao-tocar-adulto).

   WORD ARENA — arcade de vocabulario embutido na aula. O motor veio do jogo
   standalone /games/word-arena (que por sua vez veio do "Tabuada do Dino", do app
   interno better-learn). Duas mudancas OBRIGATORIAS em relacao ao standalone:

     1. ZERO EMOJI. Todo icone e SVG inline (REGRA: visual do material).
     2. AUDIO = speakText do shell (MP3 ElevenLabs, REGRA 7). O standalone usa
        speechSynthesis; aqui isso seria TTS robotico como metodo principal, que a
        REGRA 7 proibe. As palavras do deck entram no audioMap via
        lesson.extra_audio do config.

   USO no slides.html / preclass.html:
     <div class="word-arena" data-key="theo-a1"
          data-deck='[{"w":"match","def":"a game between two teams"}, ...]'></div>

   PROGRESSO (REGRA 18): igual ao dino-tap — se o container TAMBEM tiver a classe
   `think-card`, ele conta na barra do Pre-class (o updateProgress do shell ja conta
   think-card, done quando `.recorded`). No slide do IN CLASS ele NAO tem think-card:
   e atividade conduzida pela professora, e teacher-led nunca entra na barra do aluno.
   ============================================================================ */
(function () {
  'use strict';

  var OPTIONS = 4;
  var SVG_SOUND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a9 9 0 0 1 0 14"/></svg>';
  var SVG_FLAME = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2c1 4 4 5 4 9a4 4 0 0 1-8 0c0-2 1-3 1-5-2 1-4 3-4 6a7 7 0 0 0 14 0c0-5-4-7-7-10Z"/></svg>';
  var SVG_TARGET = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg>';

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* SFX curtos (Web Audio) — o "game feel". Silencioso se o navegador barrar. */
  function sfx(ok) {
    try {
      var C = window.__teensActx || (window.__teensActx = new (window.AudioContext || window.webkitAudioContext)());
      var seq = ok ? [[523.25, 0], [659.25, 0.09], [783.99, 0.18]] : [[220, 0], [165, 0.11]];
      seq.forEach(function (s) {
        var o = C.createOscillator(), g = C.createGain();
        o.type = ok ? 'triangle' : 'sawtooth'; o.frequency.value = s[0];
        o.connect(g); g.connect(C.destination);
        var t = C.currentTime + s[1];
        g.gain.setValueAtTime(0.0001, t);
        g.gain.exponentialRampToValueAtTime(0.18, t + 0.02);
        g.gain.exponentialRampToValueAtTime(0.0001, t + 0.2);
        o.start(t); o.stop(t + 0.22);
      });
    } catch (e) { }
  }

  /* Audio da palavra = pipeline do shell (audioMap -> MP3 ElevenLabs). */
  function say(word) {
    if (typeof window.speakText === 'function') window.speakText(word, null);
  }

  function persistKey(el) { return 'wordarena-' + (el.getAttribute('data-key') || 'x'); }

  function build(el) {
    var deck;
    try { deck = JSON.parse(el.getAttribute('data-deck') || '[]'); } catch (e) { deck = []; }
    deck = deck.filter(function (x) { return x && x.w && x.def; });
    if (deck.length < 2) { el.style.display = 'none'; return; }

    var rounds = deck.length;
    var order = shuffle(deck.slice());
    var qi = 0, streak = 0, best = 0, hits = 0, busy = false;

    el.innerHTML =
      '<div class="wa-hud"><span class="wa-tag">Word Arena</span>' +
      '<span class="wa-stats">' +
      '<span class="wa-chip">' + SVG_FLAME + '<b class="wa-streak">0</b></span>' +
      '<span class="wa-chip">' + SVG_TARGET + '<b class="wa-qn">1</b>/' + rounds + '</span>' +
      '</span></div>' +
      '<div class="wa-bar"><i></i></div>' +
      '<div class="wa-word"></div>' +
      '<div class="wa-say"><button type="button" class="wa-say-btn" aria-label="Hear the word">' +
      SVG_SOUND + ' Hear it</button></div>' +
      '<div class="wa-opts"></div>';

    var wordEl = el.querySelector('.wa-word'),
      optsEl = el.querySelector('.wa-opts'),
      sayBtn = el.querySelector('.wa-say-btn'),
      streakEl = el.querySelector('.wa-streak'),
      qnEl = el.querySelector('.wa-qn'),
      bar = el.querySelector('.wa-bar > i');

    function playCur() {
      if (!order[qi]) return;
      sayBtn.classList.add('playing');
      say(order[qi].w);
      setTimeout(function () { sayBtn.classList.remove('playing'); }, 1200);
    }
    sayBtn.addEventListener('click', playCur);

    function options(correct) {
      var pool = shuffle(deck.filter(function (x) { return x.def !== correct.def; }))
        .slice(0, OPTIONS - 1).map(function (x) { return x.def; });
      return shuffle([correct.def].concat(pool));
    }

    function render() {
      busy = false;
      var q = order[qi];
      wordEl.textContent = q.w;
      qnEl.textContent = qi + 1;
      bar.style.width = (qi / rounds * 100) + '%';
      optsEl.innerHTML = '';
      options(q).forEach(function (def) {
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'wa-opt'; b.textContent = def;
        b.addEventListener('click', function () { choose(b, def, q.def); });
        optsEl.appendChild(b);
      });
      setTimeout(playCur, 250);
    }

    function choose(btn, def, answer) {
      if (busy) return;
      busy = true;
      var all = optsEl.querySelectorAll('.wa-opt');
      for (var i = 0; i < all.length; i++) all[i].classList.add('disabled');
      if (def === answer) {
        btn.classList.add('correct'); sfx(true);
        streak++; hits++; if (streak > best) best = streak;
      } else {
        btn.classList.add('wrong'); sfx(false); streak = 0;
        for (var j = 0; j < all.length; j++) {
          if (all[j].textContent === answer) all[j].classList.add('correct');
        }
      }
      streakEl.textContent = streak;
      setTimeout(function () {
        qi++;
        if (qi >= rounds) finish(); else render();
      }, def === answer ? 800 : 1500);
    }

    function finish() {
      bar.style.width = '100%';
      var stars = hits >= rounds - 1 ? 3 : hits >= Math.ceil(rounds * 0.6) ? 2 : hits >= Math.ceil(rounds * 0.3) ? 1 : 0;
      var title = stars === 3 ? 'Flawless.' : stars === 2 ? 'Solid run.' : 'Run it back.';
      el.innerHTML =
        '<div class="wa-end"><div class="wa-stars">' +
        new Array(stars + 1).join('★') + new Array(4 - stars).join('☆') +
        '</div><h4>' + title + '</h4>' +
        '<p>' + hits + ' of ' + rounds + ' correct &middot; best streak ' + best + '</p>' +
        '<button type="button" class="wa-again">Play again</button></div>';
      el.querySelector('.wa-again').addEventListener('click', function () { replay(el); });
      markDone(el);
    }

    render();
  }

  function replay(el) {
    el.classList.remove('recorded', 'completed');
    try { localStorage.removeItem(persistKey(el)); } catch (e) { }
    build(el);
  }

  function markDone(el) {
    // So conta progresso se o container tambem for think-card (Pre-class). No slide do
    // IN CLASS a atividade e conduzida pela professora — teacher-led nao entra na barra.
    if (!el.classList.contains('think-card')) return;
    el.classList.add('recorded', 'completed');
    try { localStorage.setItem(persistKey(el), '1'); } catch (e) { }
    if (typeof window.updateProgress === 'function') window.updateProgress();
  }

  function done(el) {
    // Volta de outra sessao ja concluido: tela calma, sem som, com opcao de jogar de novo.
    el.innerHTML =
      '<div class="wa-end"><div class="wa-stars">★★★</div>' +
      '<h4>Completed</h4><p>Play it again to beat your streak.</p>' +
      '<button type="button" class="wa-again">Play again</button></div>';
    el.classList.add('recorded', 'completed');
    el.querySelector('.wa-again').addEventListener('click', function () { replay(el); });
    if (typeof window.updateProgress === 'function') window.updateProgress();
  }

  function initAll() {
    var games = document.querySelectorAll('.word-arena');
    for (var i = 0; i < games.length; i++) {
      var el = games[i], was = false;
      if (el.classList.contains('think-card')) {
        try { was = localStorage.getItem(persistKey(el)) === '1'; } catch (e) { }
      }
      if (was) done(el); else build(el);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll);
  else initAll();
})();
