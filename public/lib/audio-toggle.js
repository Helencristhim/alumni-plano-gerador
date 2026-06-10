/* ═══════════════════════════════════════════════════════════════
   AUDIO TOGGLE — Play/Pause APENAS para .audio-inline (dialogue)
   Nao interfere com nenhum outro uso de speakText (vocab, listening, etc.)
   Carregar DEPOIS do <script> inline que define speakText/audioMap.
   ═══════════════════════════════════════════════════════════════ */
(function() {
  var _origSpeakText = window.speakText;
  var _atAudio = null;
  var _atBtn = null;
  var _atText = null;

  var _playSvg = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';
  var _pauseSvg = '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';

  function _resetBtn(b) {
    if (b) { b.classList.remove('playing'); b.innerHTML = _playSvg; }
  }

  window.speakText = function(text, btnEl) {
    // Se NAO e audio-inline, usar speakText original sem nenhuma modificacao
    if (!btnEl || !btnEl.classList || !btnEl.classList.contains('audio-inline')) {
      if (_origSpeakText) _origSpeakText(text, btnEl);
      return;
    }

    // --- A partir daqui: APENAS audio-inline (dialogue) ---
    var cleanText = text.replace(/\\'/g, "'");

    // Toggle: mesma frase tocando = pausa
    if (_atAudio && !_atAudio.paused && _atText === cleanText) {
      _atAudio.pause(); _atAudio.currentTime = 0;
      _resetBtn(_atBtn);
      _atAudio = null; _atBtn = null; _atText = null;
      return;
    }

    // Parar audio anterior do dialogue
    if (_atAudio) {
      _atAudio.pause(); _atAudio.currentTime = 0;
      _resetBtn(_atBtn);
      _atAudio = null; _atBtn = null; _atText = null;
    }

    // Parar qualquer outro audio global
    if (typeof currentAudio !== 'undefined' && currentAudio) {
      currentAudio.pause(); currentAudio.currentTime = 0;
    }

    var map = (typeof audioMap !== 'undefined') ? audioMap : {};
    var file = map[cleanText] || map[cleanText.replace(/\.$/, '')] || map[cleanText + '.'];

    if (file) {
      var audio = new Audio(file);
      audio.playbackRate = (typeof audioSpeed !== 'undefined') ? audioSpeed : 1;
      _atAudio = audio;
      _atBtn = btnEl;
      _atText = cleanText;
      btnEl.classList.add('playing');
      btnEl.innerHTML = _pauseSvg;

      audio.onended = function() { _resetBtn(btnEl); _atAudio = null; _atBtn = null; _atText = null; };
      audio.onerror = function() { _resetBtn(btnEl); _atAudio = null; _atBtn = null; _atText = null; };
      audio.play().catch(function() { _resetBtn(btnEl); _atAudio = null; _atBtn = null; _atText = null; });
    } else {
      // Fallback: chamar original para TTS
      if (_origSpeakText) _origSpeakText(text, btnEl);
    }
  };
})();
