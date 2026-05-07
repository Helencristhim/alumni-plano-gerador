/* ═══════════════════════════════════════════════════════════════
   ALUMNI BY BETTER — EXERCISE COMPONENTS v2.0
   7 tipos de exercicio FAAP reutilizaveis.
   Cada funcao retorna HTML limpo. Event handlers sao anexados
   via addEventListener apos innerHTML (nao inline onclick).
   Depende apenas de design-system.css.
   ═══════════════════════════════════════════════════════════════ */

/* ── SVG Icons (Lucide-style) ── */
var ICONS = {
  check: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
  x: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
  chevronUp: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>',
  chevronDown: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
  mic: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="1" width="6" height="11" rx="3"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>',
  volume: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>',
  play: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
  refreshCw: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
  lock: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
};

var FEEDBACK_CORRECT = ['Boa!', 'Perfeito!', 'Excelente!', 'Muito bem!'];
var FEEDBACK_WRONG = ['Quase. Tente de novo.', 'Não foi dessa vez.', 'Tente mais uma vez.'];

function _randomFeedback(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function _escapeHtml(str) {
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

function _shuffleArray(arr) {
  var a = arr.slice();
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var t = a[i]; a[i] = a[j]; a[j] = t;
  }
  return a;
}

/* ── Global exercise data registry ── */
var _exData = {};

/* ── Contractions map for answer validation ── */
var _contractions = {
  "i'm":"i am","i am":"i'm","don't":"do not","do not":"don't",
  "doesn't":"does not","does not":"doesn't","didn't":"did not","did not":"didn't",
  "can't":"cannot","cannot":"can't","won't":"will not","will not":"won't",
  "i'd":"i would","i would":"i'd","i'll":"i will","i will":"i'll",
  "it's":"it is","it is":"it's","he's":"he is","he is":"he's",
  "she's":"she is","she is":"she's","we're":"we are","we are":"we're",
  "they're":"they are","they are":"they're","isn't":"is not","is not":"isn't",
  "aren't":"are not","are not":"aren't","wasn't":"was not","was not":"wasn't",
  "weren't":"were not","were not":"weren't","haven't":"have not","have not":"haven't",
  "hasn't":"has not","has not":"hasn't","couldn't":"could not","could not":"couldn't",
  "wouldn't":"would not","would not":"wouldn't","shouldn't":"should not","should not":"shouldn't"
};

/* ═══════════════════════════════════════════════════════════════
   HANDLER FUNCTIONS (called from simple onclick strings)
   ═══════════════════════════════════════════════════════════════ */

function _handleVerifyMatching(id) {
  var data = _exData[id];
  if (!data) return;
  var pairs = data.pairs;
  var allCorrect = true;
  for (var i = 0; i < pairs.length; i++) {
    var sel = document.getElementById(id + '_select_' + i);
    var icon = document.getElementById(id + '_icon_' + i);
    var fb = document.getElementById(id + '_feedback_' + i);
    var row = document.getElementById(id + '_row_' + i);
    if (!sel) continue;
    if (sel.value === pairs[i].correct) {
      sel.style.borderColor = 'var(--success)';
      sel.style.background = 'var(--success-bg)';
      icon.innerHTML = '<span style="color:var(--success)">' + ICONS.check + '</span>';
      fb.style.color = 'var(--success)';
      fb.textContent = _randomFeedback(FEEDBACK_CORRECT);
      row.style.pointerEvents = 'none';
    } else {
      allCorrect = false;
      sel.style.borderColor = 'var(--error)';
      sel.style.background = 'var(--error-bg)';
      icon.innerHTML = '<span style="color:var(--error)">' + ICONS.x + '</span>';
      fb.style.color = 'var(--error)';
      fb.textContent = _randomFeedback(FEEDBACK_WRONG);
      sel.style.animation = 'shake 200ms ease';
      (function(s, ic, f) {
        setTimeout(function() {
          s.style.animation = '';
          s.style.borderColor = ''; s.style.background = '';
          ic.innerHTML = ''; f.textContent = '';
        }, 1800);
      })(sel, icon, fb);
    }
  }
  var resultEl = document.getElementById(id + '_result');
  if (allCorrect && resultEl) {
    resultEl.innerHTML = '<span style="color:var(--success);font-weight:600;display:flex;align-items:center;gap:4px;">' + ICONS.check + ' Todas corretas!</span>';
  }
}

function _handleVerifyFill(id, index) {
  var data = _exData[id];
  if (!data) return;
  var item = data.items[index];
  var input = document.getElementById(id + '_input_' + index);
  var fb = document.getElementById(id + '_fb_' + index);
  if (!input || !fb) return;

  var v = input.value.trim().toLowerCase();
  var a = item.answer.toLowerCase();
  var alts = item.altAnswers || [];
  var match = (v === a) || (_contractions[v] === a) || (_contractions[a] === v) || alts.some(function(alt) { return v === alt.toLowerCase(); });

  if (match) {
    input.classList.remove('is-wrong');
    input.classList.add('is-correct');
    input.readOnly = true;
    fb.innerHTML = '<span style="color:var(--success);display:flex;align-items:center;gap:4px;">' + ICONS.check + ' ' + _randomFeedback(FEEDBACK_CORRECT) + '</span>';
  } else {
    input.classList.remove('is-correct');
    input.classList.add('is-wrong');
    input.style.animation = 'shake 200ms ease';
    setTimeout(function() { input.style.animation = ''; }, 250);
    fb.innerHTML = '<span style="color:var(--error);display:flex;align-items:center;gap:4px;">' + ICONS.x + ' ' + _randomFeedback(FEEDBACK_WRONG) + '</span>';
    setTimeout(function() { input.classList.remove('is-wrong'); fb.innerHTML = ''; }, 2000);
  }
}

function _handleQuizSelect(id, optIndex, correctIndex) {
  var already = document.querySelector('#' + id + ' .quiz-option-student.is-correct');
  if (already) return;
  var opts = document.querySelectorAll('#' + id + ' .quiz-option-student');
  var fb = document.getElementById(id + '_fb');

  if (optIndex === correctIndex) {
    document.getElementById(id + '_opt_' + optIndex).classList.add('is-correct');
    fb.innerHTML = '<span style="color:var(--success);display:flex;align-items:center;gap:4px;">' + ICONS.check + ' ' + _randomFeedback(FEEDBACK_CORRECT) + '</span>';
    for (var j = 0; j < opts.length; j++) { opts[j].style.pointerEvents = 'none'; }
  } else {
    var el = document.getElementById(id + '_opt_' + optIndex);
    el.classList.add('is-wrong');
    el.style.animation = 'shake 200ms ease';
    setTimeout(function() { el.style.animation = ''; }, 250);
    fb.innerHTML = '<span style="color:var(--error);display:flex;align-items:center;gap:4px;">' + ICONS.x + ' ' + _randomFeedback(FEEDBACK_WRONG) + '</span>';
    setTimeout(function() {
      document.getElementById(id + '_opt_' + correctIndex).classList.add('is-correct');
      for (var j = 0; j < opts.length; j++) { opts[j].style.pointerEvents = 'none'; }
    }, 800);
  }
}

function _handleVerifyOrder(id) {
  var data = _exData[id];
  if (!data) return;
  var list = document.getElementById(id + '_list');
  var items = list.querySelectorAll('[data-word]');
  var correct = data.correctOrder;
  var allOk = true;
  for (var i = 0; i < items.length; i++) {
    if (items[i].getAttribute('data-word') === correct[i]) {
      items[i].style.borderColor = 'var(--success)';
      items[i].style.background = 'var(--success-bg)';
    } else {
      items[i].style.borderColor = 'var(--error)';
      items[i].style.background = 'var(--error-bg)';
      items[i].style.animation = 'shake 200ms ease';
      (function(el) { setTimeout(function() { el.style.animation = ''; }, 250); })(items[i]);
      allOk = false;
    }
  }
  var fb = document.getElementById(id + '_fb');
  if (allOk) {
    fb.innerHTML = '<span style="color:var(--success);font-weight:600;display:flex;align-items:center;gap:4px;">' + ICONS.check + ' Perfeito!</span>';
  } else {
    fb.innerHTML = '<span style="color:var(--error);display:flex;align-items:center;gap:4px;">' + ICONS.x + ' Quase. Ajuste a ordem e tente de novo.</span>';
    setTimeout(function() {
      for (var j = 0; j < items.length; j++) { items[j].style.borderColor = ''; items[j].style.background = ''; }
      fb.innerHTML = '';
    }, 2200);
  }
}

function _orderMove(exId, index, direction) {
  var list = document.getElementById(exId + '_list');
  if (!list) return;
  var items = Array.from(list.children);
  var newIndex = index + direction;
  if (newIndex < 0 || newIndex >= items.length) return;
  var current = items[index];
  var target = items[newIndex];
  if (direction === -1) list.insertBefore(current, target);
  else { if (target.nextSibling) list.insertBefore(current, target.nextSibling); else list.appendChild(current); }
  var updated = Array.from(list.children);
  updated.forEach(function(el, idx) {
    var btns = el.querySelectorAll('button');
    if (btns[0]) btns[0].setAttribute('onclick', "_orderMove('" + exId + "'," + idx + ",-1)");
    if (btns[1]) btns[1].setAttribute('onclick', "_orderMove('" + exId + "'," + idx + ",1)");
  });
  current.style.transition = 'transform 200ms ease-out';
  current.style.transform = 'scale(1.03)';
  setTimeout(function() { current.style.transform = ''; }, 200);
}

function _handlePronListen(id) {
  var data = _exData[id];
  if (!data) return;
  if (data.audioSrc) {
    var a = new Audio(data.audioSrc); a.play();
  } else if (typeof speakText === 'function') {
    speakText(data.phrase);
  } else if (typeof speakWithFallback === 'function') {
    speakWithFallback(data.phrase, typeof audioMap !== 'undefined' ? audioMap : {});
  } else {
    var u = new SpeechSynthesisUtterance(data.phrase);
    u.lang = 'en-US'; u.rate = 0.85;
    speechSynthesis.speak(u);
  }
}

function _handlePronRecord(id) {
  var data = _exData[id];
  if (!data) return;
  var btn = document.getElementById(id + '_record');
  var fb = document.getElementById(id + '_fb');
  var score = document.getElementById(id + '_score');
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    fb.innerHTML = '<span style="color:var(--error)">Seu navegador nao suporta reconhecimento de voz. Use Chrome ou Edge.</span>';
    return;
  }
  var recognition = new SR();
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 3;

  btn.innerHTML = '<span style="display:inline-block;width:10px;height:10px;background:var(--error);border-radius:50%;animation:pulse 1s infinite;"></span> Gravando...';
  btn.disabled = true;
  btn.style.background = 'var(--error)';
  btn.style.borderColor = 'var(--error)';

  recognition.start();

  recognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript.toLowerCase().replace(/[^a-z0-9\s]/g, '');
    var targetWords = data.phrase.toLowerCase().replace(/[^a-z0-9\s]/g, '').split(/\s+/);
    var spokenWords = transcript.split(/\s+/);
    var matched = 0;
    for (var i = 0; i < targetWords.length; i++) {
      var el = document.getElementById(id + '_w_' + i);
      if (!el) continue;
      var found = spokenWords.indexOf(targetWords[i]) !== -1;
      if (found) {
        el.style.color = 'var(--success)'; el.style.background = 'var(--success-bg)';
        matched++;
        var idx = spokenWords.indexOf(targetWords[i]);
        spokenWords.splice(idx, 1);
      } else {
        el.style.color = 'var(--error)'; el.style.background = 'var(--error-bg)';
      }
    }
    score.innerHTML = matched + '/' + targetWords.length + ' palavras corretas';
    score.style.color = matched === targetWords.length ? 'var(--success)' : 'var(--warning, #b45309)';
    if (matched === targetWords.length) {
      fb.innerHTML = '<span style="color:var(--success);font-weight:600;display:flex;align-items:center;gap:4px;">' + ICONS.check + ' Excelente pronuncia!</span>';
    } else {
      fb.innerHTML = '<span style="color:var(--text-muted, #777)">As palavras em vermelho precisam de mais pratica.</span>';
    }
    _resetPronBtn(id);
  };
  recognition.onerror = function(e) {
    fb.innerHTML = '<span style="color:var(--error)">Erro: ' + e.error + '. Tente de novo.</span>';
    _resetPronBtn(id);
  };
  recognition.onend = function() {
    _resetPronBtn(id);
  };
}

function _resetPronBtn(id) {
  var btn = document.getElementById(id + '_record');
  if (btn) {
    btn.innerHTML = ICONS.mic + ' Gravar';
    btn.disabled = false;
    btn.style.background = '';
    btn.style.borderColor = '';
  }
}

function _handlePronReset(id) {
  var data = _exData[id];
  if (!data) return;
  var targetWords = data.phrase.toLowerCase().replace(/[^a-z0-9\s]/g, '').split(/\s+/);
  for (var i = 0; i < targetWords.length; i++) {
    var el = document.getElementById(id + '_w_' + i);
    if (el) { el.style.color = ''; el.style.background = ''; }
  }
  var fb = document.getElementById(id + '_fb');
  var score = document.getElementById(id + '_score');
  if (fb) fb.innerHTML = '';
  if (score) score.innerHTML = '';
}

function _handleThinkRecord(id) {
  var btn = document.getElementById(id + '_rec');
  var fb = document.getElementById(id + '_fb');
  var playBtn = document.getElementById(id + '_play');

  if (btn.dataset.recording === 'true') {
    if (window['_tai_recorder_' + id]) window['_tai_recorder_' + id].stop();
    return;
  }

  navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
    var mediaRecorder = new MediaRecorder(stream);
    window['_tai_recorder_' + id] = mediaRecorder;
    var chunks = [];
    mediaRecorder.ondataavailable = function(e) { chunks.push(e.data); };
    mediaRecorder.onstop = function() {
      stream.getTracks().forEach(function(t) { t.stop(); });
      var blob = new Blob(chunks, { type: 'audio/webm' });
      var url = URL.createObjectURL(blob);
      window['_tai_audio_' + id] = url;
      if (playBtn) playBtn.style.display = 'inline-flex';
      fb.innerHTML = '<span style="display:flex;align-items:center;gap:4px;color:var(--text-muted, #777);font-size:0.85rem;">' + ICONS.lock + ' Seu audio fica no seu dispositivo.</span>';
      btn.innerHTML = ICONS.mic + ' Gravar';
      btn.dataset.recording = 'false';
      btn.style.background = '';
      btn.style.borderColor = '';
    };
    mediaRecorder.start();
    btn.innerHTML = '<span style="display:inline-block;width:10px;height:10px;background:var(--error);border-radius:50%;animation:pulse 1s infinite;"></span> Parar';
    btn.dataset.recording = 'true';
    btn.style.background = 'var(--error)';
    btn.style.borderColor = 'var(--error)';
  }).catch(function() {
    fb.innerHTML = '<span style="color:var(--error);font-size:0.85rem;">Permita o acesso ao microfone para gravar.</span>';
  });
}

function _handleThinkPlay(id) {
  var url = window['_tai_audio_' + id];
  if (url) { new Audio(url).play(); return; }
  var dbReq = indexedDB.open('alumni_think_about_it', 1);
  dbReq.onsuccess = function(e) {
    var db = e.target.result;
    var tx = db.transaction('recordings', 'readonly');
    var req = tx.objectStore('recordings').get(id);
    req.onsuccess = function() {
      if (req.result) { var u = URL.createObjectURL(req.result); new Audio(u).play(); }
    };
  };
}


/* ═══════════════════════════════════════════════════════════════
   1. MATCHING DROPDOWN
   ═══════════════════════════════════════════════════════════════ */
function createMatchingDropdown(exerciseId, pairs) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  _exData[id] = { pairs: pairs };

  var rows = '';
  pairs.forEach(function(pair, i) {
    var shuffled = _shuffleArray(pair.options);
    var optionsHtml = '<option value="">Escolha...</option>';
    shuffled.forEach(function(opt) {
      optionsHtml += '<option value="' + _escapeHtml(opt) + '">' + _escapeHtml(opt) + '</option>';
    });
    rows += '<div class="fill-item" id="' + id + '_row_' + i + '" style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">' +
      '<span style="font-weight:600;color:var(--text-primary, #1a1a2e);min-width:120px;">' + _escapeHtml(pair.en) + '</span>' +
      '<button class="btn btn--sm" style="background:var(--alumni-navy, #003080);color:#fff;border:none;padding:4px 8px;border-radius:6px;cursor:pointer;min-height:44px;min-width:44px;display:flex;align-items:center;" onclick="if(typeof speakText===\'function\')speakText(\'' + _escapeHtml(pair.en).replace(/'/g, "\\'") + '\',this)" title="Ouvir">' + ICONS.volume + '</button>' +
      '<select class="select" id="' + id + '_select_' + i + '" style="flex:1;min-width:160px;min-height:44px;">' + optionsHtml + '</select>' +
      '<span id="' + id + '_icon_' + i + '" style="width:24px;display:flex;align-items:center;justify-content:center;"></span>' +
      '<div id="' + id + '_feedback_' + i + '" style="width:100%;font-size:0.85rem;margin-top:4px;min-height:20px;"></div>' +
    '</div>';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--vocab">MATCHING</span> Match the words</div>' +
    '<p class="microcopy">Select the correct translation for each word.</p>' +
    rows +
    '<div style="margin-top:16px;display:flex;gap:8px;align-items:center;">' +
      '<button class="btn btn--primary" onclick="_handleVerifyMatching(\'' + id + '\')">Verificar respostas</button>' +
      '<span id="' + id + '_result"></span>' +
    '</div>' +
  '</div>';
}

/* ═══════════════════════════════════════════════════════════════
   2. FILL-IN-THE-BLANK (simple)
   ═══════════════════════════════════════════════════════════════ */
function createFillBlank(exerciseId, items) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  _exData[id] = { items: items };

  var rows = '';
  items.forEach(function(item, i) {
    var parts = item.sentence.split('___');
    rows += '<div class="fill-item" id="' + id + '_item_' + i + '">' +
      '<div class="fill-item__sentence">' +
        _escapeHtml(parts[0] || '') +
        '<input type="text" class="fill-item__input" id="' + id + '_input_' + i + '" autocomplete="off" autocorrect="off" spellcheck="false" placeholder="...">' +
        _escapeHtml(parts[1] || '') +
      '</div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-top:8px;">' +
        '<button class="btn btn--secondary btn--sm" onclick="_handleVerifyFill(\'' + id + '\',' + i + ')">Verificar</button>' +
        '<span id="' + id + '_fb_' + i + '" style="font-size:0.85rem;"></span>' +
      '</div>' +
    '</div>';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--practice">FILL IN</span> Complete the sentences</div>' +
    '<p class="microcopy">Complete with the correct word.</p>' +
    rows +
  '</div>';
}

/* ═══════════════════════════════════════════════════════════════
   3. FILL-IN WITH HINT
   ═══════════════════════════════════════════════════════════════ */
function createFillBlankWithHint(exerciseId, items) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  _exData[id] = { items: items };

  var rows = '';
  items.forEach(function(item, i) {
    var parts = item.sentence.split('___');
    rows += '<div class="fill-item" id="' + id + '_item_' + i + '">' +
      '<div class="fill-item__sentence">' +
        _escapeHtml(parts[0] || '') +
        '<input type="text" class="fill-item__input" id="' + id + '_input_' + i + '" autocomplete="off" autocorrect="off" spellcheck="false" placeholder="...">' +
        _escapeHtml(parts[1] || '') +
        ' <span style="color:var(--text-dim, #777);font-size:0.85rem;font-style:italic;">(' + _escapeHtml(item.hint) + ')</span>' +
      '</div>' +
      '<div style="display:flex;align-items:center;gap:8px;margin-top:8px;">' +
        '<button class="btn btn--secondary btn--sm" onclick="_handleVerifyFill(\'' + id + '\',' + i + ')">Verificar</button>' +
        '<span id="' + id + '_fb_' + i + '" style="font-size:0.85rem;"></span>' +
      '</div>' +
    '</div>';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--practice">FILL IN</span> Complete with the correct word</div>' +
    '<p class="microcopy">Complete with the correct word. Use the hint if you need help.</p>' +
    rows +
  '</div>';
}

/* ═══════════════════════════════════════════════════════════════
   4. MULTIPLE CHOICE
   ═══════════════════════════════════════════════════════════════ */
function createMultipleChoice(exerciseId, question, options, correctIndex) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  var letters = ['A', 'B', 'C', 'D'];

  var optionsHtml = '';
  options.forEach(function(opt, i) {
    optionsHtml += '<div class="quiz-option-student" id="' + id + '_opt_' + i + '" onclick="_handleQuizSelect(\'' + id + '\',' + i + ',' + correctIndex + ')" style="cursor:pointer;">' +
      '<span class="quiz-option-student__letter">' + letters[i] + '</span>' +
      '<span>' + _escapeHtml(opt) + '</span>' +
    '</div>';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--quiz">QUIZ</span> Choose the correct answer</div>' +
    '<div class="quiz-question-student">' + _escapeHtml(question) + '</div>' +
    '<div class="quiz-options-student">' + optionsHtml + '</div>' +
    '<div id="' + id + '_fb" style="margin-top:16px;font-size:0.85rem;font-weight:600;min-height:24px;"></div>' +
  '</div>';
}

/* ═══════════════════════════════════════════════════════════════
   5. ORDERING
   ═══════════════════════════════════════════════════════════════ */
function createOrdering(exerciseId, correctOrder, shuffledOrder) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  _exData[id] = { correctOrder: correctOrder };

  var itemsHtml = '';
  shuffledOrder.forEach(function(word, i) {
    itemsHtml += '<div class="match-item" id="' + id + '_oi_' + i + '" data-word="' + _escapeHtml(word) + '" draggable="true" style="display:flex;align-items:center;gap:8px;justify-content:space-between;padding:8px 12px;cursor:grab;">' +
      '<button class="btn btn--ghost btn--sm" style="padding:6px;min-width:36px;min-height:36px;" onclick="_orderMove(\'' + id + '\',' + i + ',-1)" aria-label="Mover para cima">' + ICONS.chevronUp + '</button>' +
      '<span style="flex:1;text-align:center;font-weight:500;">' + _escapeHtml(word) + '</span>' +
      '<button class="btn btn--ghost btn--sm" style="padding:6px;min-width:36px;min-height:36px;" onclick="_orderMove(\'' + id + '\',' + i + ',1)" aria-label="Mover para baixo">' + ICONS.chevronDown + '</button>' +
    '</div>';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--practice">ORDERING</span> Put the words in order</div>' +
    '<p class="microcopy">Use the arrows to move the words into the correct order.</p>' +
    '<div id="' + id + '_list" style="display:flex;flex-direction:column;gap:4px;">' + itemsHtml + '</div>' +
    '<div style="margin-top:16px;display:flex;align-items:center;gap:8px;">' +
      '<button class="btn btn--primary" onclick="_handleVerifyOrder(\'' + id + '\')">Verificar</button>' +
      '<span id="' + id + '_fb" style="font-size:0.85rem;min-height:24px;"></span>' +
    '</div>' +
  '</div>';
}

/* ═══════════════════════════════════════════════════════════════
   6. PRONUNCIATION ASSESSMENT
   ═══════════════════════════════════════════════════════════════ */
function createPronunciation(exerciseId, targetPhrase, audioSrc) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');
  _exData[id] = { phrase: targetPhrase, audioSrc: audioSrc };

  var words = targetPhrase.split(/\s+/);
  var targetWordsHtml = '';
  words.forEach(function(w, i) {
    targetWordsHtml += '<span id="' + id + '_w_' + i + '" style="display:inline-block;padding:2px 6px;border-radius:4px;font-weight:600;font-size:1.1rem;transition:all 200ms ease-out;">' + _escapeHtml(w) + '</span> ';
  });

  return '<div class="exercise-student" id="' + id + '">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--speak">PRONUNCIATION</span> Practice pronunciation</div>' +
    '<p class="microcopy">Listen to the audio, then record yourself. We will compare word by word.</p>' +
    '<div style="font-size:1.15rem;line-height:2;margin-bottom:16px;padding:12px;background:var(--bg-subtle, #f5f5f0);border-radius:8px;" id="' + id + '_words">' + targetWordsHtml + '</div>' +
    '<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">' +
      '<button class="btn btn--secondary" id="' + id + '_listen" onclick="_handlePronListen(\'' + id + '\')">' + ICONS.volume + ' Ouvir</button>' +
      '<button class="btn btn--primary" id="' + id + '_record" onclick="_handlePronRecord(\'' + id + '\')">' + ICONS.mic + ' Gravar</button>' +
      '<button class="btn btn--ghost btn--sm" onclick="_handlePronReset(\'' + id + '\')">' + ICONS.refreshCw + ' Tentar de novo</button>' +
    '</div>' +
    '<div id="' + id + '_score" style="margin-top:12px;font-weight:600;min-height:24px;"></div>' +
    '<div id="' + id + '_fb" style="margin-top:4px;font-size:0.85rem;min-height:20px;"></div>' +
  '</div>' +
  '<style>@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}</style>';
}

/* ═══════════════════════════════════════════════════════════════
   7. THINK ABOUT IT
   ═══════════════════════════════════════════════════════════════ */
function createThinkAboutIt(exerciseId, question) {
  var id = exerciseId.replace(/[^a-zA-Z0-9_-]/g, '');

  return '<div class="exercise-student" id="' + id + '" style="border-left:4px solid #7c3aed;">' +
    '<div class="exercise-student__title"><span class="exercise-student__badge exercise-student__badge--speak">THINK ABOUT IT</span> Think and respond</div>' +
    '<p class="microcopy">There is no right or wrong answer. Use the English you have.</p>' +
    '<div style="font-weight:500;color:var(--text-primary, #1a1a2e);margin-bottom:16px;padding:12px;background:var(--bg-subtle, #f5f5f0);border-radius:8px;line-height:1.7;">' + _escapeHtml(question) + '</div>' +
    '<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">' +
      '<button class="btn btn--primary" id="' + id + '_rec" data-recording="false" onclick="_handleThinkRecord(\'' + id + '\')">' + ICONS.mic + ' Gravar</button>' +
      '<button class="btn btn--secondary" id="' + id + '_play" style="display:none;" onclick="_handleThinkPlay(\'' + id + '\')">' + ICONS.play + ' Ouvir minha resposta</button>' +
    '</div>' +
    '<div id="' + id + '_fb" style="margin-top:12px;min-height:24px;"></div>' +
  '</div>';
}


/* ═══════════════════════════════════════════════════════════════
   AUTO-INIT SYSTEM — Exercises via data-attributes
   ═══════════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('[data-exercise]').forEach(function(el) {
    var type = el.getAttribute('data-exercise');
    var id = el.getAttribute('data-id') || 'ex_' + Math.random().toString(36).substr(2, 6);
    var html = '';

    try {
      switch(type) {
        case 'matching':
          var pairs = JSON.parse(el.getAttribute('data-pairs') || '[]');
          html = createMatchingDropdown(id, pairs);
          break;
        case 'fill-blank':
          var items = JSON.parse(el.getAttribute('data-items') || '[]');
          html = createFillBlank(id, items);
          break;
        case 'fill-blank-hint':
          var itemsH = JSON.parse(el.getAttribute('data-items') || '[]');
          html = createFillBlankWithHint(id, itemsH);
          break;
        case 'multiple-choice':
          var question = el.getAttribute('data-question') || '';
          var options = JSON.parse(el.getAttribute('data-options') || '[]');
          var correct = parseInt(el.getAttribute('data-correct') || '0');
          html = createMultipleChoice(id, question, options, correct);
          break;
        case 'ordering':
          var correctOrder = JSON.parse(el.getAttribute('data-correct') || '[]');
          var shuffled = JSON.parse(el.getAttribute('data-shuffled') || '[]');
          html = createOrdering(id, correctOrder, shuffled);
          break;
        case 'pronunciation':
          var phrase = el.getAttribute('data-phrase') || '';
          var audio = el.getAttribute('data-audio') || null;
          html = createPronunciation(id, phrase, audio);
          break;
        case 'think-about-it':
          var q = el.getAttribute('data-question') || '';
          html = createThinkAboutIt(id, q);
          break;
        default:
          console.warn('[exercises.js] Unknown exercise type:', type);
          html = '<div style="color:var(--error,#dc2626);padding:1rem;border:1px solid var(--error,#dc2626);border-radius:8px;">Exercise type "' + type + '" not supported.</div>';
      }
    } catch(err) {
      console.error('[exercises.js] Error rendering exercise', id, ':', err);
      html = '<div style="color:var(--error);padding:1rem;border:1px solid var(--error);border-radius:8px;">Erro ao carregar exercicio: ' + err.message + '</div>';
    }

    if (html) {
      el.innerHTML = html;
    }
  });

  // Drag and drop for ordering exercises
  document.querySelectorAll('[id$="_list"]').forEach(function(list) {
    if (!list.querySelector('[data-word]')) return;
    var exId = list.id.replace('_list', '');
    var draggedItem = null;
    list.addEventListener('dragstart', function(e) {
      var item = e.target.closest('[data-word]');
      if (!item) return;
      draggedItem = item;
      item.style.opacity = '0.5';
      e.dataTransfer.effectAllowed = 'move';
    });
    list.addEventListener('dragend', function(e) {
      var item = e.target.closest('[data-word]');
      if (item) item.style.opacity = '1';
      list.querySelectorAll('[data-word]').forEach(function(el) { el.classList.remove('drag-over'); });
      draggedItem = null;
    });
    list.addEventListener('dragover', function(e) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      var target = e.target.closest('[data-word]');
      if (target && target !== draggedItem) {
        list.querySelectorAll('[data-word]').forEach(function(el) { el.classList.remove('drag-over'); });
        target.classList.add('drag-over');
      }
    });
    list.addEventListener('drop', function(e) {
      e.preventDefault();
      var target = e.target.closest('[data-word]');
      if (target && draggedItem && target !== draggedItem) {
        var items = Array.from(list.querySelectorAll('[data-word]'));
        if (items.indexOf(draggedItem) < items.indexOf(target)) list.insertBefore(draggedItem, target.nextSibling);
        else list.insertBefore(draggedItem, target);
        var updated = Array.from(list.children);
        updated.forEach(function(el, idx) {
          var btns = el.querySelectorAll('button');
          if (btns[0]) btns[0].setAttribute('onclick', "_orderMove('" + exId + "'," + idx + ",-1)");
          if (btns[1]) btns[1].setAttribute('onclick', "_orderMove('" + exId + "'," + idx + ",1)");
        });
      }
      list.querySelectorAll('[data-word]').forEach(function(el) { el.classList.remove('drag-over'); });
    });
  });
});


/* ═══════════════════════════════════════════════════════════════
   MANUAL HTML FALLBACK FUNCTIONS (safety net)
   ═══════════════════════════════════════════════════════════════ */

function checkBlank(btn) {
  var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
  input.classList.remove('correct', 'wrong');
  var answer = input.dataset.answer.toLowerCase().trim();
  var altAnswer = input.dataset.alt ? input.dataset.alt.toLowerCase().trim() : null;
  var value = input.value.toLowerCase().trim();
  var hintEl = item.querySelector('.blank-hint-feedback');
  if (hintEl) hintEl.classList.remove('visible');
  if (value === answer || (altAnswer && value === altAnswer)) {
    input.classList.add('correct');
    if (hintEl) hintEl.classList.remove('visible');
    if (typeof updateProgress === 'function') updateProgress();
  } else {
    input.classList.add('wrong');
    if (input.dataset.hint) {
      if (!hintEl) { hintEl = document.createElement('div'); hintEl.className = 'blank-hint-feedback'; item.appendChild(hintEl); }
      hintEl.textContent = input.dataset.hint;
      hintEl.classList.add('visible');
    }
    setTimeout(function() { input.classList.remove('wrong'); }, 1500);
  }
}

function listenBlank(btn) {
  var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
  if (input && input.dataset.phrase && typeof speakText === 'function') speakText(input.dataset.phrase, btn);
}

function selectQuiz(o) {
  var p = o.closest('.quiz-options'); if (p.querySelector('.correct')) return;
  if (o.dataset.correct === 'true') { o.classList.add('correct'); if (typeof updateProgress === 'function') updateProgress(); }
  else { o.classList.add('wrong'); setTimeout(function() { o.classList.remove('wrong'); }, 800); }
}

function verifyAllMatches(gridId) {
  var grid = document.getElementById(gridId);
  if (!grid) return;
  var rows = grid.querySelectorAll('.match-row');
  rows.forEach(function(row) {
    var select = row.querySelector('select');
    var answer = row.dataset.answer;
    row.classList.remove('correct', 'wrong');
    if (select.value === answer) row.classList.add('correct');
    else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); }, 1800); }
  });
  if (typeof updateProgress === 'function') updateProgress();
}

function checkMatch(select) {
  var row = select.closest('.match-row');
  var answer = row.dataset.answer;
  row.classList.remove('correct', 'wrong');
  if (select.value === answer) { row.classList.add('correct'); select.disabled = true; if (typeof updateProgress === 'function') updateProgress(); }
  else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); select.value = ''; }, 1000); }
}

var _orderSelection = {};
function selectOrderItem(item, containerId) {
  if (item.classList.contains('correct-order')) return;
  if (!_orderSelection[containerId]) _orderSelection[containerId] = [];
  var idx = _orderSelection[containerId].indexOf(item);
  if (idx > -1) { _orderSelection[containerId].splice(idx, 1); item.querySelector('.order-num').textContent = '?'; item.style.borderColor = ''; }
  else { _orderSelection[containerId].push(item); item.querySelector('.order-num').textContent = _orderSelection[containerId].length; item.style.borderColor = 'var(--alumni-navy, #003080)'; }
}

function checkOrder(containerId) {
  var container = document.getElementById(containerId);
  var items = container.querySelectorAll('.order-item');
  var selected = _orderSelection[containerId] || [];
  if (selected.length !== items.length) { alert('Select all items in the correct order.'); return; }
  var allCorrect = true;
  selected.forEach(function(item, idx) {
    if (parseInt(item.dataset.order) === idx + 1) { item.classList.add('correct-order'); item.querySelector('.order-num').textContent = idx + 1; }
    else { allCorrect = false; item.style.borderColor = 'var(--error, #dc2626)'; item.classList.add('wrong'); setTimeout(function() { item.classList.remove('wrong'); item.style.borderColor = ''; item.querySelector('.order-num').textContent = '?'; }, 1000); }
  });
  if (!allCorrect) _orderSelection[containerId] = [];
  else if (typeof updateProgress === 'function') updateProgress();
}

function moveItem(btn, direction, containerId) {
  var item = btn.closest('.order-item');
  var container = document.getElementById(containerId);
  var items = Array.from(container.querySelectorAll('.order-item'));
  var idx = items.indexOf(item);
  if (direction === -1 && idx > 0) container.insertBefore(item, items[idx - 1]);
  else if (direction === 1 && idx < items.length - 1) container.insertBefore(items[idx + 1], item);
}

function speakPhrase(btn) {
  var card = btn.closest('.speech-card');
  if (card && typeof speakText === 'function') speakText(card.dataset.phrase, btn);
}

var _activeRecognition = null;
function startRecording(btn) {
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { alert('Please use Google Chrome for voice recognition.'); return; }
  var card = btn.closest('.speech-card');
  var target = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9'\s]/g, '');
  var resultDiv = card.querySelector('.speech-result');
  var stopBtn = card.querySelector('.btn-stop');
  if (btn.classList.contains('recording')) return;
  btn.classList.add('recording'); btn.style.display = 'none';
  if (stopBtn) stopBtn.style.display = 'inline-flex';
  var r = new SR();
  r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 3; r.continuous = true;
  _activeRecognition = { recognition: r, btn: btn, stopBtn: stopBtn };
  r.start();
  function resetBtns() { btn.classList.remove('recording'); btn.style.display = ''; if (stopBtn) stopBtn.style.display = 'none'; _activeRecognition = null; }
  r.onresult = function(event) {
    var best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9'\s]/g, '');
    var tw = target.split(/\s+/).filter(function(w) { return w; });
    var sw = best.split(/\s+/).filter(function(w) { return w; });
    var correct = 0, html = '';
    tw.forEach(function(w, i) {
      var match = sw[i] && (sw[i] === w || sw[i].replace(/'/g, '') === w.replace(/'/g, ''));
      if (match) correct++;
      html += '<span class="word-box word-' + (match ? 'correct' : 'missing') + '">' + w + '</span> ';
    });
    var score = correct / Math.max(tw.length, 1);
    resultDiv.classList.add('show');
    resultDiv.classList.remove('good', 'try-again', 'bad');
    if (score >= 0.8) resultDiv.classList.add('good');
    else if (score >= 0.5) resultDiv.classList.add('try-again');
    else resultDiv.classList.add('bad');
    resultDiv.innerHTML = '<strong>Score: ' + correct + '/' + tw.length + '</strong><div style="margin-top:0.5rem;">' + html + '</div>';
    resetBtns();
  };
  r.onerror = function() { resetBtns(); if (resultDiv) { resultDiv.classList.add('show', 'try-again'); resultDiv.innerHTML = 'Could not hear you. Check your microphone.'; } };
  r.onend = function() { resetBtns(); };
  setTimeout(function() { if (btn.classList.contains('recording')) { r.stop(); resetBtns(); } }, 30000);
}

function stopRecording(stopBtn) {
  if (_activeRecognition) _activeRecognition.recognition.stop();
}

function listenAllVocab(btn) {
  var section = btn.closest('.exercise-section') || btn.closest('.lesson-body') || btn.parentElement.parentElement;
  var audioBtns = section.querySelectorAll('.vocab-card .audio-btn');
  var i = 0;
  function playNext() { if (i < audioBtns.length) { audioBtns[i].click(); i++; setTimeout(playNext, 2500); } }
  playNext();
}
var playAllVocab = listenAllVocab;

function toggleLesson(header) { header.parentElement.classList.toggle('open'); }

function toggleMediaDone(checkbox) {
  var wrapper = checkbox.closest('.media-card-wrapper');
  if (wrapper) { if (checkbox.checked) wrapper.classList.add('done'); else wrapper.classList.remove('done'); }
}

function toggleChecklist(cb) {
  var li = cb.closest('li');
  if (li) { if (cb.checked) li.classList.add('checked'); else li.classList.remove('checked'); }
}

var _freeRecorder = null, _freeChunks = [];
function startFreeRecording(btn) {
  var stopBtn = btn.parentElement.querySelector('.btn-stop');
  navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
    _freeRecorder = new MediaRecorder(stream);
    _freeChunks = [];
    _freeRecorder.ondataavailable = function(e) { if (e.data.size > 0) _freeChunks.push(e.data); };
    _freeRecorder.onstop = function() {
      var blob = new Blob(_freeChunks, { type: 'audio/webm' });
      var url = URL.createObjectURL(blob);
      var thinkCard = btn.closest('.think-card') || btn.closest('.speech-card');
      var resultDiv = thinkCard ? thinkCard.querySelector('[class*="result"], [id*="result"]') : null;
      if (resultDiv) resultDiv.innerHTML = '<audio controls src="' + url + '" style="width:100%;margin-top:0.5rem;"></audio>';
      stream.getTracks().forEach(function(t) { t.stop(); });
    };
    _freeRecorder.start();
    btn.style.display = 'none';
    if (stopBtn) stopBtn.style.display = 'inline-flex';
    setTimeout(function() { if (_freeRecorder && _freeRecorder.state === 'recording') _freeRecorder.stop(); }, 60000);
  }).catch(function() { alert('Could not access microphone.'); });
}

function stopFreeRecording(stopBtn) {
  if (_freeRecorder && _freeRecorder.state === 'recording') _freeRecorder.stop();
  var recordBtn = stopBtn.parentElement.querySelector('.btn-record');
  if (recordBtn) recordBtn.style.display = '';
  stopBtn.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
  var draggedItem = null;
  document.querySelectorAll('.order-container').forEach(function(container) {
    container.addEventListener('dragstart', function(e) { var item = e.target.closest('.order-item'); if (!item || item.classList.contains('correct-order')) return; draggedItem = item; item.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; });
    container.addEventListener('dragend', function(e) { var item = e.target.closest('.order-item'); if (item) item.classList.remove('dragging'); container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); draggedItem = null; });
    container.addEventListener('dragover', function(e) { e.preventDefault(); e.dataTransfer.dropEffect = 'move'; var target = e.target.closest('.order-item'); if (target && target !== draggedItem) { container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); target.classList.add('drag-over'); } });
    container.addEventListener('drop', function(e) { e.preventDefault(); var target = e.target.closest('.order-item'); if (target && draggedItem && target !== draggedItem) { var items = Array.from(container.querySelectorAll('.order-item')); if (items.indexOf(draggedItem) < items.indexOf(target)) container.insertBefore(draggedItem, target.nextSibling); else container.insertBefore(draggedItem, target); } container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); });
  });
});

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    createMatchingDropdown, createFillBlank, createFillBlankWithHint,
    createMultipleChoice, createOrdering, createPronunciation, createThinkAboutIt,
    ICONS, _exData
  };
}
