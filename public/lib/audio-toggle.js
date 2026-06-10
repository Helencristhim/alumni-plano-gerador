/* ═══════════════════════════════════════════════════════════════
   AUDIO TOGGLE — Play/Pause para speakText()
   Sobrescreve o speakText inline com versao que faz toggle.
   Carregar DEPOIS do <script> inline que define speakText/audioMap.
   ═══════════════════════════════════════════════════════════════ */
(function() {
  // Guardar referencia ao audioMap e audioSpeed do escopo global
  var _atAudio = null;
  var _atBtn = null;
  var _atText = null;

  var _playSvg = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';
  var _pauseSvg = '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';

  function _isInlineAudio(b) {
    return b && b.classList && b.classList.contains('audio-inline');
  }

  function _resetBtn(b) {
    if (!b) return;
    if (_isInlineAudio(b)) {
      b.classList.remove('playing');
      b.innerHTML = _playSvg;
    } else if (b.style) {
      b.style.opacity = '1';
    }
  }

  function _tts(text) {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      var u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = (typeof audioSpeed !== 'undefined' ? audioSpeed : 1) * 0.85;
      u.pitch = 1;
      window.speechSynthesis.speak(u);
    }
  }

  // Sobrescrever speakText global
  window.speakText = function(text, btnEl) {
    var cleanText = text.replace(/\\'/g, "'");

    // Toggle: mesma frase + audio tocando = pausa
    if (_atAudio && !_atAudio.paused && _atText === cleanText) {
      _atAudio.pause(); _atAudio.currentTime = 0;
      _resetBtn(_atBtn);
      _atAudio = null; _atBtn = null; _atText = null;
      // Tambem limpar currentAudio global (compatibilidade)
      if (typeof currentAudio !== 'undefined') window.currentAudio = null;
      return;
    }

    // Parar audio anterior
    if (_atAudio) {
      _atAudio.pause(); _atAudio.currentTime = 0;
      _resetBtn(_atBtn);
      _atAudio = null; _atBtn = null; _atText = null;
    }
    // Tambem parar currentAudio do speakText antigo (pode estar tocando)
    if (typeof currentAudio !== 'undefined' && currentAudio) {
      currentAudio.pause(); currentAudio.currentTime = 0;
      window.currentAudio = null;
    }

    var map = (typeof audioMap !== 'undefined') ? audioMap : {};
    var file = map[cleanText] || map[cleanText.replace(/\.$/, '')] || map[cleanText + '.'];

    if (file) {
      var audio = new Audio(file);
      audio.playbackRate = (typeof audioSpeed !== 'undefined') ? audioSpeed : 1;
      _atAudio = audio;
      _atBtn = btnEl;
      _atText = cleanText;
      window.currentAudio = audio; // compatibilidade

      if (_isInlineAudio(btnEl)) {
        btnEl.classList.add('playing');
        btnEl.innerHTML = _pauseSvg;
      } else if (btnEl && btnEl.style) {
        btnEl.style.opacity = '0.5';
      }

      audio.onended = function() {
        _resetBtn(btnEl);
        _atAudio = null; _atBtn = null; _atText = null;
        window.currentAudio = null;
      };
      audio.onerror = function() {
        _resetBtn(btnEl);
        _atAudio = null; _atBtn = null; _atText = null;
        window.currentAudio = null;
        _tts(cleanText);
      };
      audio.play().catch(function() {
        _resetBtn(btnEl);
        _atAudio = null; _atBtn = null; _atText = null;
        window.currentAudio = null;
        _tts(cleanText);
      });
    } else {
      // Sem MP3 — fallback TTS (sem toggle)
      if (btnEl) { btnEl.style.opacity = '0.6'; setTimeout(function() { btnEl.style.opacity = '1'; }, 600); }
      _tts(cleanText);
    }
  };
})();
