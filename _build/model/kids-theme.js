/* ============================================================================
   KIDS-THEME.JS — injetado pelo builder SOMENTE quando model==kids (analogo ao
   kids-theme.css). NUNCA entra no material adulto => caminho do adulto intocado
   (memoria nao-tocar-adulto). Contem o(s) mini-game(s) do Pre-class kids.

   DINO TAP ("Listen and tap") — REGRA 4 etapa 2 (pratica de vocabulario), ludico
   pra A1. Toca a palavra (speakText do shell = MP3 ElevenLabs, REGRA 7) e a
   crianca toca a figura certa. Score/streak/confete (padroes reaproveitados do
   word-arena, better-learn).

   PROGRESSO (REGRA 18) SEM tocar o shell: o widget tem class `think-card` — o
   updateProgress do shell ja conta think-card (done quando `.recorded`). O
   save/load de think-card e no-op aqui (nao ha `.think-question`), entao a
   persistencia fica por conta DESTE engine (localStorage proprio). Ao completar:
   adiciona `recorded completed`, persiste e chama updateProgress().
   ============================================================================ */
(function () {
  'use strict';

  // Pool de distratores: TODA palavra concreta/distinta da biblioteca kids.
  // (imagens em /assets/kids/{w}.png). O builder so coloca como ALVO as palavras
  // da aula que estao aqui; os distratores saem deste pool.
  var POOL = ['dinosaur', 'tree', 'rocket', 'star', 'moon', 'planet', 'cat', 'dog', 'run', 'green'];
  var IMG = function (w) { return '/assets/kids/' + w + '.png'; };
  var OPTIONS = 4;
  var PRAISE = ['Nice!', 'Great!', 'You got it!', 'Awesome!', 'Perfect!'];
  var TRY = ['Try again!', 'Almost!', 'Listen again!'];

  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  function sfx(ok) {
    try {
      var C = window.__kidsActx || (window.__kidsActx = new (window.AudioContext || window.webkitAudioContext)());
      var seq = ok ? [[660, 0], [880, 0.1]] : [[300, 0]];
      seq.forEach(function (s) {
        var o = C.createOscillator(), g = C.createGain(); o.type = 'sine'; o.frequency.value = s[0];
        o.connect(g); g.connect(C.destination); var t = C.currentTime + s[1];
        g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.2, t + 0.02);
        g.gain.exponentialRampToValueAtTime(0.0001, t + 0.22); o.start(t); o.stop(t + 0.24);
      });
    } catch (e) { }
  }

  function say(word) {
    // Reusa o pipeline de audio do shell (audioMap -> MP3 ElevenLabs; TTS so fallback).
    if (typeof window.speakText === 'function') window.speakText(word, null);
  }

  function persistKey(el) { return 'dinotap-' + (el.getAttribute('data-key') || 'x'); }

  function markDone(el) {
    el.classList.add('recorded', 'completed');
    try { localStorage.setItem(persistKey(el), '1'); } catch (e) { }
    if (typeof window.updateProgress === 'function') window.updateProgress();
  }

  function confetti() {
    var COL = ['#1E9E5F', '#3FD489', '#f5b301', '#e74c3c', '#3498db'];
    for (var i = 0; i < 60; i++) {
      var c = document.createElement('div'); c.className = 'dt-confetti';
      c.style.left = Math.random() * 100 + 'vw'; c.style.background = COL[i % COL.length];
      c.style.animation = 'dtFall ' + (1.6 + Math.random() * 1.4) + 's linear ' + (Math.random() * 0.5) + 's forwards';
      document.body.appendChild(c); (function (el) { setTimeout(function () { el.remove(); }, 3600); })(c);
    }
  }

  function build(el) {
    var targets;
    try { targets = JSON.parse(el.getAttribute('data-deck') || '[]'); } catch (e) { targets = []; }
    targets = targets.filter(function (w) { return POOL.indexOf(w) !== -1; });
    if (targets.length < 1) { el.style.display = 'none'; return; }
    var rounds = targets.length;

    // Estado ja concluido (voltou de outra sessao)? mostra tela de vitoria direto.
    var done = false; try { done = localStorage.getItem(persistKey(el)) === '1'; } catch (e) { }

    el.innerHTML =
      '<div class="dt-head"><div class="dt-title">Listen and tap!<small>Ouça e toque no certo</small></div>' +
      '<div class="dt-hud"><span class="dt-chip"><span class="dt-star">★</span> <b class="dt-streak">0</b></span>' +
      '<span class="dt-chip"><b class="dt-qn">1</b>/' + rounds + '</span></div></div>' +
      '<div class="dt-progress"><i></i></div>' +
      '<div class="dt-listen"><button type="button" class="dt-listen-btn" aria-label="Play the word">' +
      '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a9 9 0 0 1 0 14"/></svg> Listen</button></div>' +
      '<div class="dt-hint">Tap Listen, then choose the picture</div>' +
      '<div class="dt-grid"></div><div class="dt-feedback"></div>';

    var grid = el.querySelector('.dt-grid'), listen = el.querySelector('.dt-listen-btn'),
      fb = el.querySelector('.dt-feedback'), hint = el.querySelector('.dt-hint'),
      streakEl = el.querySelector('.dt-streak'), qnEl = el.querySelector('.dt-qn'),
      bar = el.querySelector('.dt-progress > i');
    var order = shuffle(targets.slice()), qi = 0, streak = 0, busy = false;

    function playCur() { if (order[qi]) { listen.classList.add('playing'); say(order[qi]); setTimeout(function () { listen.classList.remove('playing'); }, 1400); } }
    listen.addEventListener('click', playCur);

    function render() {
      busy = false; fb.textContent = ''; fb.className = 'dt-feedback';
      qnEl.textContent = qi + 1; bar.style.width = (qi / rounds * 100) + '%';
      var correct = order[qi];
      var distract = shuffle(POOL.filter(function (w) { return w !== correct; })).slice(0, OPTIONS - 1);
      var opts = shuffle([correct].concat(distract));
      grid.innerHTML = '';
      opts.forEach(function (w) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'dt-opt'; b.setAttribute('aria-label', w);
        b.innerHTML = '<img src="' + IMG(w) + '" alt="' + w + '">';
        b.addEventListener('click', function () { choose(b, w, correct); });
        grid.appendChild(b);
      });
      hint.style.visibility = 'visible';
      setTimeout(playCur, 350);
    }
    function choose(btn, w, correct) {
      if (busy) return;
      if (w === correct) {
        busy = true; btn.classList.add('correct'); sfx(true);
        streak++; streakEl.textContent = streak; hint.style.visibility = 'hidden';
        fb.textContent = PRAISE[Math.floor(Math.random() * PRAISE.length)]; fb.className = 'dt-feedback good';
        qi++; setTimeout(function () { qi >= rounds ? win() : render(); }, 850);
      } else {
        btn.classList.add('wrong'); sfx(false); streak = 0; streakEl.textContent = 0;
        fb.textContent = TRY[Math.floor(Math.random() * TRY.length)]; fb.className = 'dt-feedback try';
        setTimeout(function () { btn.classList.remove('wrong'); }, 400);
      }
    }
    function win() {
      bar.style.width = '100%';
      el.innerHTML = '<div class="dt-win"><img src="' + IMG(targets[0]) + '" alt="done">' +
        '<h4>You did it! &#127881;</h4><p>Você acertou as palavras!</p>' +
        '<button type="button" class="dt-again">Play again</button></div>';
      el.querySelector('.dt-again').addEventListener('click', function () { el.classList.remove('completed', 'recorded'); try { localStorage.removeItem(persistKey(el)); } catch (e) { } build(el); });
      markDone(el); confetti();
    }

    if (done) { // ja concluido: tela de vitoria calma (sem confete/som), permite jogar de novo
      el.innerHTML = '<div class="dt-win"><img src="' + IMG(targets[0]) + '" alt="done">' +
        '<h4>Completed ✓</h4><p>Toque pra jogar de novo</p><button type="button" class="dt-again">Play again</button></div>';
      el.classList.add('recorded', 'completed');
      el.querySelector('.dt-again').addEventListener('click', function () { el.classList.remove('completed', 'recorded'); try { localStorage.removeItem(persistKey(el)); } catch (e) { } build(el); });
      if (typeof window.updateProgress === 'function') window.updateProgress();
    } else {
      render();
    }
  }

  function initAll() {
    var games = document.querySelectorAll('.dino-tap-game');
    for (var i = 0; i < games.length; i++) build(games[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll);
  else initAll();
})();
