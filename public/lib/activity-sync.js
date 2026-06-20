/**
 * Alumni — Activity Sync v2.0 (Supabase + localStorage)
 *
 * Sincroniza o estado de exercicios do aluno (matches, blanks, quiz, speech,
 * mediaChecks, checklists, ordering) entre localStorage e Supabase.
 *
 * v2.0 melhorias:
 *   - MutationObserver detecta mudancas mesmo se wrap do saveState falhar
 *   - Auto-save periodico a cada 30s como fallback
 *   - Event listeners diretos em exercicios (click, change, input)
 *   - Coleta ordering exercises (order-item.correct-order)
 *   - beforeunload salva estado final antes de sair da pagina
 *   - Supabase load restaura MESMO sem localStorage (cross-device)
 *
 * Requer:
 *   - supabase.min.js + supabase-config.js carregados ANTES
 *   - window.STUDENT_SLUG definido no <head>
 *
 * Inclusao no HTML (DEPOIS do script principal, DEPOIS de lesson-progress.js):
 *   <script src="/lib/activity-sync.js"></script>
 */

(function() {
  var slug = window.STUDENT_SLUG;
  if (!slug) { console.warn('activity-sync.js: STUDENT_SLUG not defined'); return; }
  if (typeof sb === 'undefined') { console.warn('activity-sync.js: Supabase client not found'); return; }

  // Detectar view type pela URL
  var path = window.location.pathname;
  var viewType = path.indexOf('/aluno/') !== -1 ? 'aluno' : 'professor';

  // Chave localStorage (mesmo padrao dos materiais existentes)
  var localKey = slug + '-' + viewType;
  var timestampKey = localKey + '-ts';

  // Captura o createObjectURL NATIVO antes do interceptRecordings envolve-lo, para o
  // playback (fetch->blob) nao ser confundido com uma nova gravacao.
  var nativeCreateObjectURL = URL.createObjectURL.bind(URL);
  var sharedAudioCtx = null;     // AudioContext reutilizado p/ playback decodificado
  var activePlayback = null;     // controller da gravacao tocando agora (p/ parar a anterior)

  var saveTimer = null;
  var DEBOUNCE_MS = 2000;
  var AUTO_SAVE_MS = 30000;
  var lastSavedJSON = '';

  // knownState = melhor estado conhecido (uniao do remoto + tudo que o aluno fez nesta sessao).
  // Progresso e MONOTONICO: exercicios so sao concluidos, nunca "desfeitos" (exceto Reset explicito).
  // Por isso TODA escrita faz merge (uniao) com knownState, evitando lost-update entre os varios
  // gravadores (saveToSupabase, saveRecordingRef, beforeunload). Antes, cada um sobrescrevia a linha
  // inteira e apagava o trabalho dos outros — causando perda de progresso do Pre-class.
  var knownState = null;

  function emptyState() {
    return { matches: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: [], ordering: [], vocabListened: [], thinkRecorded: [], recordings: {}, _tombstones: {} };
  }

  // Tipos de array do estado + como extrair a CHAVE de cada item (para dedupe/tombstone)
  var ARRAY_TYPES = ['matches', 'blanks', 'quiz', 'vocabListened', 'mediaChecks', 'speech', 'thinkRecorded', 'ordering'];
  function keyOf(type, item) {
    try {
      if (type === 'matches') return String(item).split('|')[0];
      if (type === 'speech') return JSON.parse(item).p;
      if (type === 'thinkRecorded') return JSON.parse(item).q;
      if (type === 'ordering') return (item && typeof item === 'object') ? item.id : item;
    } catch (e) {}
    return String(item);
  }

  // Uniao de arrays simples (dedupe por valor)
  function unionArr(a, b) {
    var out = [], seen = {};
    (a || []).concat(b || []).forEach(function(v) {
      if (v === undefined || v === null) return;
      var k = String(v);
      if (!seen[k]) { seen[k] = true; out.push(v); }
    });
    return out;
  }

  // Combina duas entradas de speech/think da MESMA frase, mantendo o melhor de cada:
  //  - a correcao word-by-word mais COMPLETA (maior array words / melhor score)
  //  - a URL de gravacao (r) de qualquer uma que tenha
  // Resolve o caso "some a parte da correcao": antes, escolher so pela gravacao (r)
  // podia descartar a entrada que tinha a correcao word-by-word.
  function richerEntry(x, y) {
    if (!x) return y;
    if (!y) return x;
    var xw = (x.words || []).length, yw = (y.words || []).length;
    // base = a que tem mais palavras de correcao (empate: a que ja tem gravacao, senao x)
    var base, other;
    if (xw !== yw) { base = xw > yw ? x : y; other = xw > yw ? y : x; }
    else { base = x.r ? x : (y.r ? y : x); other = base === x ? y : x; }
    var out = {};
    for (var k in base) out[k] = base[k];
    if (!out.r && other.r) out.r = other.r;          // herda a gravacao
    if ((!out.words || !out.words.length) && other.words && other.words.length) out.words = other.words;
    if ((!out.s || out.s === 'Done') && other.s && other.s !== 'Done') out.s = other.s; // melhor score txt
    if ((!out.c || out.c === 'good') && other.c && base !== x) out.c = base.c || other.c;
    return out;
  }

  // Uniao de arrays de JSON-strings keyed por um campo (p=phrase, q=question).
  // Em conflito, COMBINA as entradas (correcao mais completa + gravacao).
  function unionByKey(a, b, keyField) {
    var map = {}, order = [];
    (a || []).concat(b || []).forEach(function(item) {
      var key, obj = null;
      try { obj = JSON.parse(item); key = obj[keyField]; } catch (e) { obj = null; key = String(item); }
      if (key === undefined) key = String(item);
      if (!(key in map)) { order.push(key); map[key] = obj || item; }
      else if (obj && typeof map[key] === 'object') { map[key] = richerEntry(map[key], obj); }
      else if (obj && typeof map[key] !== 'object') { map[key] = obj; }
      // se obj nao parseou, mantem o que ja tinha
    });
    return order.map(function(k) { return typeof map[k] === 'object' ? JSON.stringify(map[k]) : map[k]; });
  }

  // Uniao de ordering (keyed por container id)
  function unionOrdering(a, b) {
    var map = {}, order = [];
    (a || []).concat(b || []).forEach(function(o) {
      var id = (o && typeof o === 'object') ? o.id : o;
      if (id === undefined) return;
      if (!(id in map)) { order.push(id); map[id] = o; }
    });
    return order.map(function(k) { return map[k]; });
  }

  // Merge de dois estados — resultado nunca encolhe (uniao monotonica)
  function mergeState(base, add) {
    base = base || emptyState();
    add = add || emptyState();
    var out = emptyState();
    out.matches = unionArr(base.matches, add.matches);
    out.blanks = unionArr(base.blanks, add.blanks);
    out.quiz = unionArr(base.quiz, add.quiz);
    out.vocabListened = unionArr(base.vocabListened, add.vocabListened);
    // mediaChecks pode chegar como array (atual) ou objeto (legado) — normalizar para array de ids marcados
    out.mediaChecks = unionArr(toMediaArray(base.mediaChecks), toMediaArray(add.mediaChecks));
    out.speech = unionByKey(base.speech, add.speech, 'p');
    out.thinkRecorded = unionByKey(base.thinkRecorded, add.thinkRecorded, 'q');
    out.ordering = unionOrdering(base.ordering, add.ordering);
    out.checklists = {};
    [base.checklists, add.checklists].forEach(function(c) {
      if (c) Object.keys(c).forEach(function(k) { if (c[k]) out.checklists[k] = true; else if (!(k in out.checklists)) out.checklists[k] = c[k]; });
    });
    out.recordings = {};
    if (base.recordings) Object.assign(out.recordings, base.recordings);
    if (add.recordings) Object.assign(out.recordings, add.recordings);
    // _tombstones: marcas de "resetado" — uniao por tipo/chave. Persistem no estado para que
    // TODAS as janelas respeitem o reset (senao uma janela com o estado antigo re-adicionaria
    // via uniao). Sao limpos quando o exercicio e refeito (ver applyTombstones).
    out._tombstones = {};
    [base._tombstones, add._tombstones].forEach(function(tb) {
      if (!tb) return;
      Object.keys(tb).forEach(function(type) {
        if (!out._tombstones[type]) out._tombstones[type] = {};
        Object.keys(tb[type] || {}).forEach(function(k) { if (tb[type][k]) out._tombstones[type][k] = true; });
      });
    });
    return out;
  }

  // Remove de `state` os itens marcados como resetados (_tombstones) que NAO foram refeitos.
  // `live` = collectState() atual (DOM). Se a chave reaparece no DOM, o exercicio foi refeito:
  // limpa o tombstone e mantem o item.
  function applyTombstones(state, live) {
    var tb = state._tombstones;
    if (!tb) return state;
    live = live || emptyState();
    ARRAY_TYPES.forEach(function(type) {
      if (!tb[type]) return;
      var liveKeys = {};
      (live[type] || []).forEach(function(it) { liveKeys[keyOf(type, it)] = true; });
      state[type] = (state[type] || []).filter(function(it) {
        var k = keyOf(type, it);
        if (liveKeys[k]) { delete tb[type][k]; return true; }   // refeito -> destombstone
        if (tb[type][k]) return false;                          // resetado e nao refeito -> remove
        return true;
      });
      // chaves refeitas tambem saem do tombstone mesmo se nao estavam no state
      Object.keys(tb[type]).forEach(function(k) { if (liveKeys[k]) delete tb[type][k]; });
      if (Object.keys(tb[type]).length === 0) delete tb[type];
    });
    // checklists (objeto index->bool)
    if (tb.checklists) {
      var liveC = live.checklists || {};
      Object.keys(tb.checklists).forEach(function(k) {
        if (liveC[k]) { delete tb.checklists[k]; }
        else if (state.checklists) { delete state.checklists[k]; }
      });
      if (Object.keys(tb.checklists).length === 0) delete tb.checklists;
    }
    return state;
  }

  // Registra como tombstone tudo que existia em `before` e sumiu em `after` (= foi resetado).
  function addResetTombstones(target, before, after) {
    if (!target._tombstones) target._tombstones = {};
    var tb = target._tombstones;
    ARRAY_TYPES.forEach(function(type) {
      var afterKeys = {};
      (after[type] || []).forEach(function(it) { afterKeys[keyOf(type, it)] = true; });
      (before[type] || []).forEach(function(it) {
        var k = keyOf(type, it);
        if (!afterKeys[k]) { if (!tb[type]) tb[type] = {}; tb[type][k] = true; }
      });
    });
    var bc = before.checklists || {}, ac = after.checklists || {};
    Object.keys(bc).forEach(function(k) {
      if (bc[k] && !ac[k]) { if (!tb.checklists) tb.checklists = {}; tb.checklists[k] = true; }
    });
  }

  function toMediaArray(m) {
    if (Array.isArray(m)) return m;
    if (m && typeof m === 'object') return Object.keys(m).filter(function(k) { return m[k]; });
    return [];
  }

  // ===== PLAYBACK COM FIX DE DURACAO =====
  // Gravacoes do MediaRecorder (webm no Chrome, mp4 no Safari) frequentemente saem SEM
  // metadata de duracao (o header diz duracao ~0). No dispositivo que gravou, o browser
  // tem o audio decodificado em memoria e toca inteiro. Em OUTRO computador, ao carregar
  // o arquivo do Storage, o player le duracao ~0 e CORTA logo no inicio.
  // Solucao: ao detectar duracao invalida (0/NaN/Infinity), seek pro fim forca o browser
  // a varrer o arquivo e descobrir a duracao real; depois volta pro inicio e toca inteiro.
  function stopActivePlayback() {
    if (activePlayback) { try { activePlayback.stop(); } catch (e) {} activePlayback = null; }
  }

  // Playback PRINCIPAL: decodifica o arquivo inteiro via Web Audio API (le todos os bytes
  // e sabe a duracao EXATA) e toca o buffer. Isso ignora completamente a metadata de
  // duracao quebrada do MediaRecorder — toca a gravacao inteira em qualquer computador.
  // Retorna um controller com .stop(). onStart()/onEnd() sao callbacks de UI.
  function playRecordingFixed(url, onStart, onEnd) {
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return playViaAudioElement(url, onStart, onEnd);

    if (!sharedAudioCtx) { try { sharedAudioCtx = new AC(); } catch (e) { return playViaAudioElement(url, onStart, onEnd); } }
    var ctx = sharedAudioCtx;
    if (ctx.state === 'suspended') { try { ctx.resume(); } catch (e) {} }

    var ended = false, node = null;
    var controller = { stop: function() { if (node) { try { node.stop(); } catch (e) {} } finish(); } };
    function finish() { if (ended) return; ended = true; if (onEnd) onEnd(); }

    fetch(url, { cache: 'reload' })
      .then(function(r) { if (!r.ok) throw new Error('http ' + r.status); return r.arrayBuffer(); })
      .then(function(buf) { return ctx.decodeAudioData(buf); })
      .then(function(audioBuffer) {
        if (ended) return;
        node = ctx.createBufferSource();
        node.buffer = audioBuffer;
        node.connect(ctx.destination);
        node.onended = finish;
        node.start(0);
        if (onStart) onStart(controller);
      })
      .catch(function() {
        // Se decodeAudioData falhar, cai pro <audio>+blob com seek de duracao
        if (ended) return;
        var c = playViaAudioElement(url, onStart, onEnd);
        controller.stop = c.stop;
      });

    return controller;
  }

  // Fallback: <audio> tocando a partir do blob completo + truque de seek pra descobrir
  // a duracao. Usado quando Web Audio nao esta disponivel ou decodeAudioData falha.
  function playViaAudioElement(url, onStart, onEnd) {
    var audio = new Audio();
    audio.preload = 'auto';
    var started = false, primed = false, objUrl = null, ended = false;
    var controller = { stop: function() { try { audio.pause(); } catch (e) {} cleanup(); finish(); } };
    function cleanup() { if (objUrl) { try { URL.revokeObjectURL(objUrl); } catch (e) {} objUrl = null; } }
    function finish() { if (ended) return; ended = true; if (onEnd) onEnd(); }
    function startPlay() { if (started) return; started = true; try { audio.currentTime = 0; } catch (e) {} audio.play(); if (onStart) onStart(controller); }
    audio.addEventListener('loadedmetadata', function() {
      var d = audio.duration;
      if (isFinite(d) && d > 0) { startPlay(); return; }
      var onTU = function() {
        if (primed) return;
        if (isFinite(audio.duration) && audio.duration > 0) { primed = true; audio.removeEventListener('timeupdate', onTU); startPlay(); }
      };
      audio.addEventListener('timeupdate', onTU);
      try { audio.currentTime = 1e101; } catch (e) { startPlay(); }
    });
    audio.addEventListener('ended', function() { cleanup(); finish(); });
    audio.addEventListener('error', function() { cleanup(); finish(); });
    fetch(url, { cache: 'reload' })
      .then(function(r) { if (!r.ok) throw new Error('http ' + r.status); return r.blob(); })
      .then(function(blob) { objUrl = nativeCreateObjectURL(blob); audio.src = objUrl; })
      .catch(function() { audio.src = url; });
    setTimeout(function() { if (!started && !audio.src) audio.src = url; }, 4000);
    return controller;
  }

  // ===== TRANSCODE PRA WAV (compatibilidade cross-browser) =====
  // O Chrome grava em Opus (dentro de webm ou mp4). O Safari/Mac NAO decodifica Opus,
  // entao a gravacao toca cortada/nada em outro computador. Solucao: no proprio browser
  // que gravou (Chrome, que decodifica seu Opus), converter pra WAV — formato universal
  // que toca em qualquer navegador. A conversao roda no UPLOAD, antes de subir.
  function audioBufferToWav(buffer) {
    var numCh = buffer.numberOfChannels;
    var sampleRate = buffer.sampleRate;
    var numFrames = buffer.length;
    var bytesPerSample = 2;
    var blockAlign = numCh * bytesPerSample;
    var dataSize = numFrames * blockAlign;
    var arr = new ArrayBuffer(44 + dataSize);
    var view = new DataView(arr);
    function ws(off, s) { for (var i = 0; i < s.length; i++) view.setUint8(off + i, s.charCodeAt(i)); }
    ws(0, 'RIFF'); view.setUint32(4, 36 + dataSize, true); ws(8, 'WAVE');
    ws(12, 'fmt '); view.setUint32(16, 16, true); view.setUint16(20, 1, true);
    view.setUint16(22, numCh, true); view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * blockAlign, true); view.setUint16(32, blockAlign, true);
    view.setUint16(34, 8 * bytesPerSample, true);
    ws(36, 'data'); view.setUint32(40, dataSize, true);
    var channels = [];
    for (var c = 0; c < numCh; c++) channels.push(buffer.getChannelData(c));
    var offset = 44;
    for (var i = 0; i < numFrames; i++) {
      for (var ch = 0; ch < numCh; ch++) {
        var sample = Math.max(-1, Math.min(1, channels[ch][i]));
        view.setInt16(offset, sample < 0 ? sample * 0x8000 : sample * 0x7FFF, true);
        offset += 2;
      }
    }
    return new Blob([arr], { type: 'audio/wav' });
  }

  // Recebe um Blob de gravacao e devolve Promise<Blob WAV>. Rejeita se nao decodificar.
  function transcodeToWav(blob) {
    return new Promise(function(resolve, reject) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) { reject(new Error('no AudioContext')); return; }
      var ctx;
      try { ctx = sharedAudioCtx || (sharedAudioCtx = new AC()); } catch (e) { reject(e); return; }
      var done = false;
      var fr = new FileReader();
      fr.onload = function() {
        ctx.decodeAudioData(fr.result, function(audioBuffer) {
          if (done) return; done = true;
          try { resolve(audioBufferToWav(audioBuffer)); } catch (e) { reject(e); }
        }, function(err) { if (done) return; done = true; reject(err || new Error('decode failed')); });
      };
      fr.onerror = function() { if (done) return; done = true; reject(fr.error || new Error('read failed')); };
      fr.readAsArrayBuffer(blob);
    });
  }

  // Envolve sb.storage.from('recordings').upload para transcodar gravacoes pra WAV no
  // mesmo path (browsers tocam pelo content-type, nao pela extensao). Assim TODA gravacao
  // nova — pelo upload inline do material OU pelo interceptRecordings — sobe como WAV.
  function installStorageTranscode() {
    if (typeof sb === 'undefined' || !sb.storage || sb.storage.__transcodeWrapped) return;
    var origFrom = sb.storage.from.bind(sb.storage);
    sb.storage.from = function(bucket) {
      var ref = origFrom(bucket);
      if (bucket === 'recordings' && ref && typeof ref.upload === 'function' && !ref.__uploadWrapped) {
        var origUpload = ref.upload.bind(ref);
        ref.upload = function(path, blob, opts) {
          var t = blob && blob.type ? blob.type : '';
          var isCompressed = /audio|webm|mp4|ogg|opus/i.test(t) && t.indexOf('wav') === -1;
          if (!isCompressed || !blob || !blob.size) return origUpload(path, blob, opts);
          return transcodeToWav(blob).then(function(wav) {
            var o = {};
            if (opts) for (var k in opts) o[k] = opts[k];
            o.contentType = 'audio/wav';
            return origUpload(path, wav, o);
          }).catch(function() {
            // Se nao der pra transcodar (ex: browser nao decodifica), sobe o original
            return origUpload(path, blob, opts);
          });
        };
        ref.__uploadWrapped = true;
      }
      return ref;
    };
    sb.storage.__transcodeWrapped = true;
  }

  // Forca o MediaRecorder a gravar em webm/opus no Chrome (em vez de mp4/opus).
  // Motivo: o transcode pra WAV usa decodeAudioData, que decodifica Opus-em-WEBM de
  // forma confiavel mas NAO decodifica Opus-em-MP4 (que o Chrome tambem grava). Sem
  // isso, dependendo do formato que o Chrome escolhe, o transcode falha e sobe Opus cru
  // (que o Safari nao toca). No Safari, webm nao e suportado — mantem o default (mp4/AAC,
  // que decodifica e toca em qualquer lugar).
  function installRecorderFormatFix() {
    if (typeof window.MediaRecorder !== 'function' || window.MediaRecorder.__formatWrapped) return;
    var Orig = window.MediaRecorder;
    function preferredType() {
      try {
        if (Orig.isTypeSupported && Orig.isTypeSupported('audio/webm;codecs=opus')) return 'audio/webm;codecs=opus';
        if (Orig.isTypeSupported && Orig.isTypeSupported('audio/webm')) return 'audio/webm';
      } catch (e) {}
      return null;
    }
    function Wrapped(stream, opts) {
      opts = opts || {};
      var mt = opts.mimeType || '';
      // Se pediram mp4 (ou nada), e webm/opus existe (Chrome), troca pra webm/opus.
      if (mt.indexOf('mp4') !== -1 || !mt) {
        var pref = preferredType();
        if (pref) { var o = {}; for (var k in opts) o[k] = opts[k]; o.mimeType = pref; opts = o; }
      }
      return new Orig(stream, opts);
    }
    Wrapped.isTypeSupported = function(t) { return Orig.isTypeSupported(t); };
    Wrapped.prototype = Orig.prototype;
    Wrapped.__formatWrapped = true;
    window.MediaRecorder = Wrapped;
  }

  // ===== COLLECT STATE (replica a logica do saveState original) =====
  function collectState() {
    var s = { matches: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: [], ordering: [], vocabListened: [], thinkRecorded: [] };

    document.querySelectorAll('.media-card-wrapper').forEach(function(w) {
      var id = w.dataset.media;
      var cb = w.querySelector('input[type="checkbox"]');
      if (id && cb && cb.checked) s.mediaChecks.push(id);
    });

    document.querySelectorAll('.match-row.correct select').forEach(function(sel) {
      var word = sel.closest('.match-row').querySelector('.match-word');
      if (word) s.matches.push(word.textContent + '|' + sel.value);
    });

    document.querySelectorAll('.blank-input.correct').forEach(function(e) {
      s.blanks.push(e.dataset.answer);
    });

    document.querySelectorAll('.quiz-option.correct').forEach(function(e) {
      s.quiz.push(e.textContent.trim().substring(0, 30));
    });

    document.querySelectorAll('.speech-result.show').forEach(function(e) {
      var card = e.closest('.speech-card');
      if (card && card.dataset.phrase) {
        var cls = e.classList.contains('good') ? 'good' : e.classList.contains('try-again') ? 'try-again' : 'bad';
        var strong = e.querySelector('strong');
        var scoreTxt = strong ? strong.textContent : 'Done';
        var words = [];
        e.querySelectorAll('.word-box').forEach(function(wb) {
          words.push({ w: wb.textContent, s: wb.classList.contains('word-correct') ? 'c' : 'm' });
        });
        var recUrl = card.dataset.recordingUrl || '';
        s.speech.push(JSON.stringify({ p: card.dataset.phrase, c: cls, s: scoreTxt, words: words, r: recUrl }));
      }
    });

    document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) {
      s.checklists[i] = cb.checked;
    });

    // Vocab cards listened
    document.querySelectorAll('.vocab-card-pc.listened').forEach(function(vc) {
      var w = vc.querySelector('.vocab-card-word');
      if (w) s.vocabListened.push(w.textContent);
    });

    // Ordering exercises completados
    document.querySelectorAll('.order-container').forEach(function(oc) {
      var items = oc.querySelectorAll('.order-item');
      var correct = oc.querySelectorAll('.order-item.correct-order');
      if (items.length > 0 && items.length === correct.length) {
        var id = oc.id || '';
        var order = [];
        items.forEach(function(it) {
          var txt = it.querySelector('.order-text');
          if (txt) order.push(txt.textContent);
        });
        s.ordering.push({ id: id, order: order });
      }
    });

    // Think cards recorded
    document.querySelectorAll('.think-card.recorded').forEach(function(tc) {
      var q = tc.querySelector('.think-question');
      if (q) {
        var recUrl = tc.dataset.recordingUrl || '';
        s.thinkRecorded.push(JSON.stringify({ q: q.textContent.trim().substring(0, 40), r: recUrl }));
      }
    });

    return s;
  }

  // ===== APPLY STATE (replica a logica do loadState original) =====
  function applyState(s) {
    if (!s) return;

    if (s.matches) s.matches.forEach(function(d) {
      var parts = d.split('|');
      var word = parts[0];
      var val = parts[1];
      document.querySelectorAll('.match-row').forEach(function(row) {
        var matchWord = row.querySelector('.match-word');
        if (matchWord && matchWord.textContent === word) {
          var sel = row.querySelector('select');
          if (sel && !row.classList.contains('correct')) {
            sel.value = val;
            row.classList.add('correct');
            sel.disabled = true;
          }
        }
      });
    });

    if (s.blanks) s.blanks.forEach(function(a) {
      document.querySelectorAll('.blank-input[data-answer="' + a + '"]').forEach(function(e) {
        if (!e.classList.contains('correct')) {
          e.value = a;
          e.classList.add('correct');
        }
      });
    });

    if (s.quiz) s.quiz.forEach(function(t) {
      document.querySelectorAll('.quiz-option[data-correct="true"]').forEach(function(e) {
        if (e.textContent.trim().substring(0, 30) === t) e.classList.add('correct');
      });
    });

    if (s.speech) s.speech.forEach(function(d) {
      var phrase, cls, scoreTxt, words;
      try { var obj = JSON.parse(d); phrase = obj.p; cls = obj.c; scoreTxt = obj.s; words = obj.words || []; }
      catch(e) { if (d.indexOf('||') !== -1) { var parts = d.split('||'); phrase = parts[0]; cls = parts[1]; scoreTxt = 'Done'; words = []; } else { phrase = d; cls = 'good'; scoreTxt = 'Done'; words = []; } }
      var recUrl; try { recUrl = JSON.parse(d).r || ''; } catch(e) { recUrl = ''; }
      document.querySelectorAll('.speech-card').forEach(function(sc) {
        if (sc.dataset.phrase === phrase) {
          var rd = sc.querySelector('.speech-result');
          if (rd) {
            rd.classList.add('show', cls);
            var html = '<strong>' + scoreTxt + '</strong> — ' + (cls === 'good' ? 'Excellent!' : cls === 'try-again' ? 'Almost there!' : 'Keep practicing!');
            if (words.length > 0) {
              html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
              words.forEach(function(w) { html += '<span class="word-box word-' + (w.s === 'c' ? 'correct' : 'missing') + '">' + w.w + '</span>'; });
              html += '</div></div>';
            }
            rd.innerHTML = html;
          }
          if (recUrl) {
            sc.dataset.recordingUrl = recUrl;
            if (typeof injectPronunciationBtn === 'function') injectPronunciationBtn(sc, recUrl);
          }
        }
      });
    });

    if (s.checklists) {
      document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) {
        if (s.checklists[i]) {
          cb.checked = true;
          var li = cb.closest('li');
          if (li) li.classList.add('checked');
        }
      });
    }

    if (s.mediaChecks) {
      // Suportar tanto array (novo) quanto objeto (legado localStorage)
      if (Array.isArray(s.mediaChecks)) {
        s.mediaChecks.forEach(function(id) {
          document.querySelectorAll('.media-card-wrapper').forEach(function(w) {
            if (w.dataset.media === id) {
              var cb = w.querySelector('input[type="checkbox"]');
              if (cb) { cb.checked = true; w.classList.add('done'); }
            }
          });
        });
      } else {
        // Formato objeto legado do localStorage
        document.querySelectorAll('.media-card-wrapper').forEach(function(w) {
          var id = w.dataset.media;
          var cb = w.querySelector('input[type="checkbox"]');
          if (id && cb && s.mediaChecks[id]) { cb.checked = true; w.classList.add('done'); }
        });
      }
    }

    // Vocab cards listened
    if (s.vocabListened) {
      s.vocabListened.forEach(function(word) {
        document.querySelectorAll('.vocab-card-pc').forEach(function(vc) {
          var w = vc.querySelector('.vocab-card-word');
          if (w && w.textContent === word) vc.classList.add('listened');
        });
      });
    }

    // Ordering exercises
    if (s.ordering) {
      s.ordering.forEach(function(o) {
        var id = typeof o === 'string' ? o : o.id;
        var savedOrder = typeof o === 'object' ? o.order : null;
        var oc = id ? document.getElementById(id) : null;
        if (!oc) return;
        if (savedOrder && savedOrder.length > 0) {
          var items = Array.from(oc.querySelectorAll('.order-item'));
          savedOrder.forEach(function(txt) {
            for (var i = 0; i < items.length; i++) {
              var t = items[i].querySelector('.order-text');
              if (t && t.textContent === txt) { oc.appendChild(items[i]); break; }
            }
          });
        }
        oc.querySelectorAll('.order-item').forEach(function(it, i) {
          it.classList.add('correct-order');
          var num = it.querySelector('.order-num');
          if (num) num.textContent = i + 1;
          it.style.borderColor = 'var(--success)';
        });
      });
    }

    // Think cards recorded
    if (s.thinkRecorded) {
      s.thinkRecorded.forEach(function(d) {
        var qTxt, recUrl;
        try { var obj = JSON.parse(d); qTxt = obj.q; recUrl = obj.r || ''; }
        catch(e) { qTxt = d; recUrl = ''; }
        document.querySelectorAll('.think-card').forEach(function(tc) {
          var qEl = tc.querySelector('.think-question');
          if (qEl && qEl.textContent.trim().substring(0, 40) === qTxt) {
            tc.classList.add('recorded');
            tc.dataset.recordingUrl = recUrl;
            var rd = tc.querySelector('[id^="think-result"]');
            if (rd) {
              if (recUrl) {
                rd.innerHTML = '<audio controls src="' + recUrl + '" style="width:100%;margin-top:0.5rem;"></audio><p style="font-size:.72rem;color:#16a34a;margin-top:.3rem;">&#10003; Recording saved</p>';
              } else if (!rd.innerHTML) {
                rd.innerHTML = '<p style="font-size:.82rem;color:#16a34a;font-weight:500;">&#10003; Recording completed</p>';
              }
            }
          }
        });
      });
    }

    // Atualizar progresso visual
    if (typeof updateProgress === 'function') updateProgress();
  }

  // ===== SAVE TO SUPABASE (debounced) =====
  function saveToSupabase(force) {
    if (saveTimer) clearTimeout(saveTimer);
    var delay = force ? 0 : DEBOUNCE_MS;

    saveTimer = setTimeout(function() {
      // Merge (uniao) com o melhor estado conhecido desta janela.
      knownState = mergeState(knownState, collectState());
      var localJSON = JSON.stringify(knownState);
      if (localJSON === lastSavedJSON && !force) return;

      // READ-MODIFY-WRITE: le o estado REMOTO vivo e une com o local ANTES de gravar.
      // Sem isso, uma janela com retrato antigo sobrescreve o progresso que outra janela
      // gravou (lost-update). Como o merge e uniao (comutativo + monotonico), gravacoes
      // concorrentes convergem para a uniao — nenhuma janela consegue encolher a linha.
      sb.from('student_activity')
        .select('state')
        .eq('student_slug', slug)
        .eq('view_type', viewType)
        .single()
        .then(function(readRes) {
          var remote = (readRes && readRes.data && readRes.data.state) ? readRes.data.state : null;
          var merged = mergeState(remote, knownState);
          // Respeita resets (de qualquer janela) que ainda nao foram refeitos
          merged = applyTombstones(merged, collectState());
          knownState = merged;

          var mergedJSON = JSON.stringify(merged);
          lastSavedJSON = mergedJSON;
          var now = new Date().toISOString();
          try {
            localStorage.setItem(timestampKey, now);
            localStorage.setItem(localKey, mergedJSON);
          } catch(e) {}

          sb.from('student_activity')
            .upsert({
              student_slug: slug,
              view_type: viewType,
              state: merged,
              updated_at: now
            }, { onConflict: 'student_slug,view_type' })
            .then(function(res) {
              if (res.error) console.error('activity-sync save error:', res.error.message);
            });
        });
    }, delay);
  }

  // ===== WRAP saveState (metodo principal) =====
  if (typeof window.saveState === 'function') {
    var _originalSaveState = window.saveState;
    window.saveState = function() {
      _originalSaveState();  // localStorage (instantaneo)
      saveToSupabase();      // Supabase (debounced)
    };
  }

  // ===== WRAP updateProgress (calculo real da barra de progresso do Pre-class) =====
  if (typeof window.updateProgress === 'function') {
    var _originalUpdateProgress = window.updateProgress;
    window.updateProgress = function() {
      // Calcular progresso real por lesson card
      document.querySelectorAll('.lesson-card[id^="ex-lesson-"]').forEach(function(card) {
        var lessonNum = card.id.replace('ex-lesson-', '');
        var total = 0, done = 0;
        // Matching rows
        total += card.querySelectorAll('.match-row').length;
        done += card.querySelectorAll('.match-row.correct').length;
        // Fill-in blanks
        total += card.querySelectorAll('.blank-input').length;
        done += card.querySelectorAll('.blank-input.correct').length;
        // Quiz items (1 por quiz-item)
        var quizItems = card.querySelectorAll('.quiz-item');
        total += quizItems.length;
        quizItems.forEach(function(qi) { if (qi.querySelector('.quiz-option.correct')) done++; });
        // Speech cards
        var speechCards = card.querySelectorAll('.speech-card');
        total += speechCards.length;
        speechCards.forEach(function(sc) { if (sc.querySelector('.speech-result.good')) done++; });
        // Ordering containers (1 por container)
        card.querySelectorAll('.order-container').forEach(function(oc) {
          var items = oc.querySelectorAll('.order-item');
          total += 1;
          if (items.length > 0 && items.length === oc.querySelectorAll('.order-item.correct-order').length) done++;
        });
        // Atualizar barra visual
        var pct = total > 0 ? Math.round(done / total * 100) : 0;
        var fill = card.querySelector('.mini-bar-fill[data-lesson-progress="' + lessonNum + '"]');
        if (fill) fill.style.width = pct + '%';
        var pctEl = card.querySelector('.mini-percent[data-lesson-pct="' + lessonNum + '"]');
        if (pctEl) pctEl.textContent = pct + '%';
      });
      // Chamar original (localStorage + saveState → Supabase)
      _originalUpdateProgress();
    };
  }

  // ===== RECORDING UPLOAD (Speech cards — Listen + Record) =====
  var STORAGE_BUCKET = 'recordings';
  var uploadingRecordings = {};

  function uploadRecording(blob, phraseId) {
    if (!blob || uploadingRecordings[phraseId]) return;
    uploadingRecordings[phraseId] = true;

    // Path: {slug}/{phraseId}.webm — upsert sobreescreve a anterior
    var filePath = slug + '/' + phraseId + '.webm';

    sb.storage.from(STORAGE_BUCKET).upload(filePath, blob, {
      contentType: blob.type || 'audio/webm',
      upsert: true
    }).then(function(res) {
      uploadingRecordings[phraseId] = false;
      if (res.error) {
        console.error('recording upload error:', res.error.message);
        return;
      }

      // Salvar referencia no state
      var publicUrl = sb.storage.from(STORAGE_BUCKET).getPublicUrl(filePath).data.publicUrl;
      saveRecordingRef(phraseId, publicUrl);
    });
  }

  function saveRecordingRef(phraseId, url) {
    // Adiciona a ref da gravacao no knownState e grava pelo MESMO caminho read-modify-write
    // do saveToSupabase (le o remoto vivo, une, aplica tombstones) — assim um upload de
    // gravacao nunca sobrescreve progresso de outra janela.
    knownState = mergeState(knownState, collectState());
    if (!knownState.recordings) knownState.recordings = {};
    knownState.recordings[phraseId] = url;
    saveToSupabase(true);
    // Injetar botao "My Recording" assim que possivel
    var recs = {}; recs[phraseId] = url;
    injectMyRecordingButtons(recs);
  }

  // Interceptar URL.createObjectURL para capturar blobs de audio
  function interceptRecordings() {
    var _origCreateObjectURL = URL.createObjectURL.bind(URL);

    URL.createObjectURL = function(obj) {
      var url = _origCreateObjectURL(obj);

      // Detectar blobs de audio (gravacoes do aluno)
      if (obj instanceof Blob && obj.size > 1000 && (
        obj.type.indexOf('audio') !== -1 ||
        obj.type.indexOf('webm') !== -1 ||
        obj.type.indexOf('ogg') !== -1
      )) {
        // Delay para dar tempo do DOM atualizar (saber qual speech card gravou)
        setTimeout(function() {
          var phraseId = findRecordingPhraseId(url);
          if (phraseId) {
            uploadRecording(obj, phraseId);
          }
        }, 800);
      }

      return url;
    };
  }

  // Encontrar o ID da frase que acabou de ser gravada
  function findRecordingPhraseId(blobUrl) {
    // 1. Procurar nos _tai_audio_ do window (exercises.js salva la)
    var keys = Object.keys(window);
    for (var i = 0; i < keys.length; i++) {
      if (keys[i].indexOf('_tai_audio_') === 0 && window[keys[i]] === blobUrl) {
        return keys[i].replace('_tai_audio_', '');
      }
    }

    // 2. Procurar botao de gravar que acabou (data-recording mudou pra false)
    var btns = document.querySelectorAll('[data-recording="false"]');
    for (var j = btns.length - 1; j >= 0; j--) {
      var card = btns[j].closest('.speech-card') || btns[j].closest('[id]');
      if (card) return card.dataset.phrase || card.id || 'rec-' + Date.now();
    }

    // 3. Procurar audio element com o blobUrl
    var audios = document.querySelectorAll('audio[src="' + blobUrl + '"]');
    if (audios.length > 0) {
      var parent = audios[0].closest('.speech-card') || audios[0].closest('.think-card') || audios[0].closest('[id]');
      if (parent) return parent.dataset.phrase || parent.id || 'rec-' + Date.now();
    }

    // 4. Fallback com timestamp
    return 'recording-' + Date.now();
  }

  // ===== MY RECORDING BUTTON (injected into speech cards) =====
  var myRecCSS = false;
  function injectMyRecordingCSS() {
    if (myRecCSS) return;
    myRecCSS = true;
    var style = document.createElement('style');
    style.textContent =
      '.btn-my-rec{display:inline-flex;align-items:center;gap:5px;padding:0.55rem 1.2rem;' +
      'font:600 0.85rem/1.4 -apple-system,BlinkMacSystemFont,"Inter",sans-serif;' +
      'color:#fff;background:#16a34a;border:2px solid #16a34a;border-radius:8px;cursor:pointer;' +
      'transition:all 150ms ease;white-space:nowrap}' +
      '.btn-my-rec:hover{background:#15803d;border-color:#15803d}' +
      '.btn-my-rec svg{flex-shrink:0}';
    document.head.appendChild(style);
  }

  function injectMyRecordingButtons(recordings) {
    if (!recordings || typeof recordings !== 'object') return;
    injectMyRecordingCSS();

    var headphoneIcon = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3v5z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3v5z"/></svg>';

    document.querySelectorAll('.speech-card[data-phrase]').forEach(function(card) {
      var phrase = card.dataset.phrase;
      var audioUrl = recordings[phrase];
      if (!audioUrl) return;

      // Evitar duplicar botao
      if (card.querySelector('.btn-my-rec')) return;

      var controls = card.querySelector('.speech-controls');
      if (!controls) return;

      var btn = document.createElement('button');
      btn.className = 'btn btn-my-rec';
      btn.innerHTML = headphoneIcon + ' My Recording';
      btn.onclick = function(e) {
        e.preventDefault();
        function restore() { btn.innerHTML = headphoneIcon + ' My Recording'; btn.style.background = ''; }
        // Toggle: se esta tocando esta gravacao, para
        if (btn.dataset.playing === 'true') { stopActivePlayback(); restore(); btn.dataset.playing = 'false'; return; }
        stopActivePlayback();
        btn.innerHTML = headphoneIcon + ' Playing...';
        btn.style.background = '#15803d';
        btn.dataset.playing = 'true';
        activePlayback = playRecordingFixed(audioUrl, null, function() { restore(); btn.dataset.playing = 'false'; activePlayback = null; });
      };

      controls.appendChild(btn);
    });
  }

  // ===== OVERRIDE do botao "Your Pronunciation" (inline no HTML do aluno) =====
  // Substitui a versao inline por uma que toca com o fix de duracao, corrigindo o
  // "audio cortado em outro computador" para TODOS os alunos sem editar o material.
  function installPronunciationFix() {
    window.injectPronunciationBtn = function(card, audioUrl) {
      var old = card.querySelector('.btn-your-pronunciation');
      if (old) old.remove();
      var playBtn = document.createElement('button');
      playBtn.className = 'btn btn-your-pronunciation';
      playBtn.innerHTML = '&#9654; Your Pronunciation';
      playBtn.onclick = function(e) {
        e.preventDefault();
        if (playBtn.dataset.playing === 'true') {
          stopActivePlayback();
          playBtn.innerHTML = '&#9654; Your Pronunciation';
          playBtn.dataset.playing = 'false';
          return;
        }
        stopActivePlayback();
        playBtn.innerHTML = '&#9632; Playing...';
        playBtn.dataset.playing = 'true';
        activePlayback = playRecordingFixed(audioUrl, null, function() {
          playBtn.innerHTML = '&#9654; Your Pronunciation';
          playBtn.dataset.playing = 'false';
          activePlayback = null;
        });
      };
      var controls = card.querySelector('.speech-controls');
      if (controls) controls.appendChild(playBtn);
    };
  }

  // Carregar gravacoes salvas do Supabase e injetar botoes
  function loadSavedRecordings() {
    if (viewType !== 'aluno') return;

    sb.from('student_activity')
      .select('state')
      .eq('student_slug', slug)
      .eq('view_type', 'aluno')
      .single()
      .then(function(res) {
        if (res.error || !res.data || !res.data.state || !res.data.state.recordings) return;
        injectMyRecordingButtons(res.data.state.recordings);
      });
  }

  // ===== RESET BUTTON (per lesson, injected at bottom of each lesson-body) =====
  function injectResetButtons() {
    if (viewType !== 'aluno') return;

    var style = document.createElement('style');
    style.textContent =
      '.reset-lesson-wrap{display:flex;justify-content:center;padding:24px 0 8px;margin-top:20px;border-top:1px dashed var(--border-light,#d4d4cc)}' +
      '.btn-reset-lesson{display:inline-flex;align-items:center;gap:6px;padding:8px 20px;' +
      'font:500 0.8rem/1.4 -apple-system,BlinkMacSystemFont,"Inter",sans-serif;' +
      'color:var(--text-dim,#888);background:transparent;border:1px solid var(--border,#d4d4cc);' +
      'border-radius:8px;cursor:pointer;transition:all 150ms ease}' +
      '.btn-reset-lesson:hover{color:#dc2626;border-color:#dc2626;background:rgba(220,38,38,0.05)}' +
      '.btn-reset-lesson svg{flex-shrink:0}';
    document.head.appendChild(style);

    var trashIcon = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>';

    document.querySelectorAll('.lesson-card[id^="ex-lesson-"]').forEach(function(card) {
      var lessonBody = card.querySelector('.lesson-body');
      if (!lessonBody) return;

      // Evitar duplicar
      if (lessonBody.querySelector('.reset-lesson-wrap')) return;

      var lessonNum = card.id.replace('ex-lesson-', '');

      var wrap = document.createElement('div');
      wrap.className = 'reset-lesson-wrap';

      var btn = document.createElement('button');
      btn.className = 'btn-reset-lesson';
      btn.innerHTML = trashIcon + ' Reset Lesson ' + lessonNum;
      btn.setAttribute('data-lesson', lessonNum);
      btn.onclick = function(e) {
        e.preventDefault();
        if (!confirm('Reset all progress for Lesson ' + lessonNum + '?\n\nThis will erase exercises, recordings, and progress for this lesson.\n\nThis action cannot be undone.')) return;
        resetLesson(card, lessonNum);
      };

      wrap.appendChild(btn);
      lessonBody.appendChild(wrap);
    });
  }

  function resetLesson(lessonCard, lessonNum) {
    // Captura o estado ANTES de limpar o DOM, para saber o que sera removido (tombstones).
    var beforeReset = mergeState(knownState, collectState());

    // 1. Reset visual state de todos os exercicios DENTRO desta aula
    lessonCard.querySelectorAll('.blank-input').forEach(function(el) {
      el.value = ''; el.classList.remove('correct', 'wrong'); el.readOnly = false;
    });
    lessonCard.querySelectorAll('.quiz-option').forEach(function(el) {
      el.classList.remove('correct', 'wrong'); el.style.pointerEvents = '';
    });
    lessonCard.querySelectorAll('.match-row').forEach(function(el) {
      el.classList.remove('correct', 'wrong');
      var sel = el.querySelector('select');
      if (sel) { sel.value = ''; sel.disabled = false; }
    });
    lessonCard.querySelectorAll('.order-item').forEach(function(el) {
      el.classList.remove('correct-order', 'wrong');
      var num = el.querySelector('.order-num');
      if (num) num.textContent = '?';
    });
    lessonCard.querySelectorAll('.speech-result').forEach(function(el) {
      el.classList.remove('show', 'good', 'try-again', 'bad'); el.innerHTML = '';
    });
    lessonCard.querySelectorAll('.media-card-wrapper').forEach(function(el) {
      el.classList.remove('done');
      var cb = el.querySelector('input[type="checkbox"]');
      if (cb) cb.checked = false;
    });
    lessonCard.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb) {
      cb.checked = false;
      var li = cb.closest('li');
      if (li) li.classList.remove('checked');
    });
    // Remove My Recording buttons desta aula
    lessonCard.querySelectorAll('.btn-my-rec').forEach(function(el) { el.remove(); });
    // Remove tracker badges
    lessonCard.querySelectorAll('.tracker-badge').forEach(function(el) { el.remove(); });

    // 2. Atualizar progress bar e stamp
    if (typeof updateProgress === 'function') updateProgress();

    // 3. Salvar estado limpo no localStorage
    if (typeof saveState === 'function') saveState();

    // 4. Limpar gravacoes desta aula no Supabase Storage
    var phrasesInLesson = [];
    lessonCard.querySelectorAll('.speech-card[data-phrase]').forEach(function(card) {
      phrasesInLesson.push(card.dataset.phrase);
    });

    // 5. Atualizar Supabase: remover recordings desta aula do state
    sb.from('student_activity')
      .select('state')
      .eq('student_slug', slug)
      .eq('view_type', 'aluno')
      .single()
      .then(function(res) {
        var state = (res.data && res.data.state) || {};
        if (state.recordings && phrasesInLesson.length > 0) {
          phrasesInLesson.forEach(function(phrase) {
            delete state.recordings[phrase];
            // Deletar audio do Storage
            var filePath = slug + '/' + phrase + '.webm';
            sb.storage.from(STORAGE_BUCKET).remove([filePath]);
          });
        }

        // Recoletar estado limpo (DOM ja foi limpo para esta aula; outras aulas continuam)
        var cleanState = mergeState(emptyState(), collectState());
        cleanState.recordings = state.recordings || {};

        // Tombstones: marca o que foi removido nesta aula para que NENHUMA janela (nem o
        // proprio merge contra o remoto) re-adicione o que o reset limpou. Carrega tombstones
        // anteriores e adiciona os novos (diff entre antes e depois do reset).
        cleanState._tombstones = mergeState(emptyState(), beforeReset)._tombstones || {};
        addResetTombstones(cleanState, beforeReset, cleanState);

        // CRITICO: o knownState precisa virar o estado limpo, senao o proximo merge
        // re-infla a aula resetada a partir do knownState antigo (Reset seria desfeito).
        knownState = cleanState;

        var now = new Date().toISOString();
        var cleanJSON = JSON.stringify(cleanState);
        try { localStorage.setItem(timestampKey, now); localStorage.setItem(localKey, cleanJSON); } catch(e) {}
        lastSavedJSON = cleanJSON;

        sb.from('student_activity')
          .upsert({
            student_slug: slug,
            view_type: 'aluno',
            state: cleanState,
            updated_at: now
          }, { onConflict: 'student_slug,view_type' })
          .then(function(r) {
            if (r.error) console.error('reset save error:', r.error.message);
          });
      });

    // 6. Feedback visual
    var btn = lessonCard.querySelector('.btn-reset-lesson');
    if (btn) {
      btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg> Reset done!';
      btn.style.color = '#16a34a';
      btn.style.borderColor = '#16a34a';
      setTimeout(function() {
        btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg> Reset Lesson ' + lessonCard.id.replace('ex-lesson-', '');
        btn.style.color = '';
        btn.style.borderColor = '';
      }, 2000);
    }
  }

  // ===== FALLBACK: Event listeners diretos nos exercicios =====
  // Garante sync mesmo se o wrap do saveState nao funcionar
  function setupEventListeners() {
    // Click em quiz options, check buttons, order items
    document.addEventListener('click', function(e) {
      var target = e.target;
      if (
        target.closest('.quiz-option') ||
        target.closest('.check-btn') ||
        target.closest('.order-item') ||
        target.closest('.match-row') ||
        target.closest('[onclick*="checkBlank"]') ||
        target.closest('[onclick*="selectQuiz"]') ||
        target.closest('[onclick*="checkMatch"]') ||
        target.closest('[onclick*="checkOrder"]') ||
        target.closest('[onclick*="verifyAllMatches"]') ||
        target.closest('[onclick*="toggleMediaDone"]')
      ) {
        // Delay para dar tempo da logica do exercicio rodar
        setTimeout(function() { saveToSupabase(); }, 500);
      }
    }, true);

    // Change em selects (matching) e checkboxes (media/checklists)
    document.addEventListener('change', function(e) {
      if (
        e.target.closest('.match-row select') ||
        e.target.closest('.media-card-wrapper input[type="checkbox"]') ||
        e.target.closest('.checklist input[type="checkbox"]')
      ) {
        setTimeout(function() { saveToSupabase(); }, 500);
      }
    }, true);
  }

  // ===== FALLBACK: Auto-save periodico (30s) =====
  function startAutoSave() {
    setInterval(function() {
      var currentJSON = JSON.stringify(collectState());
      if (currentJSON !== lastSavedJSON) {
        saveToSupabase();
      }
    }, AUTO_SAVE_MS);
  }

  // ===== FALLBACK: Save antes de sair da pagina =====
  window.addEventListener('beforeunload', function() {
    // Merge antes de sair — nunca envia um estado menor que o conhecido (preserva recordings)
    knownState = mergeState(knownState, collectState());
    var state = knownState;
    var stateJSON = JSON.stringify(state);
    if (stateJSON === lastSavedJSON) return;

    var now = new Date().toISOString();
    try { localStorage.setItem(timestampKey, now); localStorage.setItem(localKey, stateJSON); } catch(e) {}

    // fetch com keepalive para garantir envio mesmo ao fechar
    try {
      var anonKey = 'sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29';
      fetch('https://xxdggcopydghbmgqqebq.supabase.co/rest/v1/student_activity', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'apikey': anonKey,
          'Authorization': 'Bearer ' + anonKey,
          'Prefer': 'resolution=merge-duplicates'
        },
        body: JSON.stringify({
          student_slug: slug,
          view_type: viewType,
          state: state,
          updated_at: now
        }),
        keepalive: true
      });
    } catch(e) {}
  });

  // ===== LOAD FROM SUPABASE (on page load) =====
  function loadFromSupabase() {
    sb.from('student_activity')
      .select('state, updated_at')
      .eq('student_slug', slug)
      .eq('view_type', viewType)
      .single()
      .then(function(res) {
        if (res.error || !res.data) return;

        var remoteState = res.data.state;

        // MERGE bidirecional: une o remoto (outro computador) com o que ja existe
        // localmente/nesta sessao. Cross-device deixa de PERDER progresso porque
        // nada e sobrescrito — so cresce. Resolve o caso "entro em outro PC e some".
        knownState = mergeState(knownState, remoteState);
        // Respeita resets propagados (de qualquer janela) antes de renderizar
        knownState = applyTombstones(knownState, collectState());
        applyState(knownState);

        var mergedJSON = JSON.stringify(knownState);
        try {
          localStorage.setItem(localKey, mergedJSON);
          localStorage.setItem(timestampKey, res.data.updated_at);
        } catch(e) {}

        // Se o merge resultou em algo MAIOR que o remoto (havia progresso local que
        // o outro PC nao tinha), empurra a uniao de volta pro Supabase.
        if (mergedJSON !== JSON.stringify(remoteState)) {
          lastSavedJSON = JSON.stringify(remoteState);
          saveToSupabase(true);
        } else {
          lastSavedJSON = mergedJSON;
        }
      });
  }

  // ===== LOAD PRECLASS VIEWER (professor pages only) =====
  function loadPreclassViewer() {
    if (viewType !== 'professor') return;
    var script = document.createElement('script');
    script.src = '/lib/preclass-viewer.js';
    document.body.appendChild(script);
  }

  // Re-injeta os botoes "Your Pronunciation" ja na tela com a versao corrigida
  // (a versao inline antiga foi usada no loadState do material, antes desta lib carregar)
  function refreshPronunciationButtons() {
    document.querySelectorAll('.speech-card[data-phrase]').forEach(function(card) {
      var url = card.dataset.recordingUrl;
      if (url && typeof window.injectPronunciationBtn === 'function') {
        window.injectPronunciationBtn(card, url);
      }
    });
  }

  // ===== INIT =====
  function init() {
    // Garantia anti-Opus em QUALQUER visao (aluno, professor, "ver como aluno"): toda
    // gravacao, de qualquer pagina, vira WAV. Forcar webm no Chrome + transcodar no upload.
    installRecorderFormatFix();
    installStorageTranscode();

    // Interceptar MediaRecorder ANTES de qualquer gravacao
    if (viewType === 'aluno') interceptRecordings();

    // Substituir o player do botao "Your Pronunciation" pela versao com fix de duracao
    installPronunciationFix();
    setTimeout(refreshPronunciationButtons, 300);

    // Capturar estado atual (ja restaurado do localStorage pelo loadState do material) como baseline
    knownState = mergeState(emptyState(), collectState());
    lastSavedJSON = JSON.stringify(knownState);

    // Carregar do Supabase e fazer merge (nunca sobrescreve — so cresce)
    setTimeout(loadFromSupabase, 200);

    // Carregar botoes "My Recording" para gravacoes salvas
    setTimeout(loadSavedRecordings, 600);

    // Injetar botoes Reset no final de cada aula
    setTimeout(injectResetButtons, 400);

    // Ativar fallbacks
    setupEventListeners();
    startAutoSave();

    // Preclass viewer desativado — quebrava layout do IN CLASS (slide-mode)
    // loadPreclassViewer();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { init(); });
  } else {
    init();
  }

})();

/* ============================================================================
 * PATCH: gravacao do Pre-class desacoplada do SpeechRecognition
 * ----------------------------------------------------------------------------
 * Bug antigo (inline em todos os materiais): o MediaRecorder era parado dentro
 * de finish(), chamado por SR.onend/onerror/onresult. No Chrome atual o
 * SpeechRecognition encerra sozinho em ~0.5s (onend/onerror 'no-speech'),
 * cortando a gravacao quase imediatamente e deixando mediaChunks vazio -> o
 * botao "Your Pronunciation" nunca aparecia.
 *
 * Correcao: a gravacao (MediaRecorder) roda ate o usuario clicar Stop ou um
 * timeout de seguranca de 30s. O SpeechRecognition roda EM PARALELO so para o
 * score word-by-word; quando ele encerra/erra, NAO para a gravacao (so tenta
 * reiniciar para continuar pontuando). Sem SR (Safari/Firefox/mobile) grava
 * audio-only e conta como feito — sem o antigo alert('Please use Google Chrome').
 *
 * Esta lib carrega DEPOIS do <script> inline em toda pagina (REGRA 28), entao
 * window.startRecording/stopRecording aqui sobrescrevem a versao bugada. Um
 * unico arquivo conserta todos os materiais (existentes e futuros).
 * ==========================================================================*/
(function () {
  function pslug(s) { return (s || '').toLowerCase().replace(/[^a-z0-9]/g, '_').substring(0, 50); }

  window.startRecording = function (btn) {
    var card = btn.closest('.speech-card');
    if (!card) return;
    if (btn.classList.contains('recording')) return;
    var target = (card.dataset.phrase || '').toLowerCase().replace(/[^a-z0-9' ]/g, '');
    var resultDiv = card.querySelector('.speech-result');
    var stopBtn = card.querySelector('.btn-stop');
    btn.classList.add('recording', 'hidden');
    if (stopBtn) stopBtn.classList.add('visible');

    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    var hasSR = !!SR;

    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      var mimeType = MediaRecorder.isTypeSupported('audio/mp4') ? 'audio/mp4'
        : MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : '';
      var mediaRec = mimeType ? new MediaRecorder(stream, { mimeType: mimeType }) : new MediaRecorder(stream);
      var chunks = [], stopped = false, rec = null, srRestarts = 0;

      mediaRec.ondataavailable = function (e) { if (e.data && e.data.size > 0) chunks.push(e.data); };
      mediaRec.onstop = function () {
        stream.getTracks().forEach(function (t) { t.stop(); });
        if (!chunks.length) return;
        var blob = new Blob(chunks, { type: mediaRec.mimeType || 'audio/webm' });
        var url = URL.createObjectURL(blob);
        if (typeof injectPronunciationBtn === 'function') injectPronunciationBtn(card, url);
        if (resultDiv && !resultDiv.classList.contains('show')) {
          resultDiv.classList.add('show', 'good');
          resultDiv.innerHTML = '<strong>&#10003; Recording saved</strong> — listen back with "Your Pronunciation".';
          if (typeof updateProgress === 'function') updateProgress();
        }
        var slug = window.STUDENT_SLUG || 'unknown';
        var ext = blob.type.indexOf('mp4') !== -1 ? 'mp4' : 'webm';
        var filePath = slug + '/' + pslug(card.dataset.phrase) + '.' + ext;
        if (typeof sb !== 'undefined') {
          sb.storage.from('recordings').upload(filePath, blob, { contentType: blob.type, upsert: true }).then(function (res) {
            if (!res.error) {
              card.dataset.recordingUrl = sb.storage.from('recordings').getPublicUrl(filePath).data.publicUrl;
              if (typeof saveState === 'function') saveState();
            }
          });
        }
      };

      function endAll() {
        if (stopped) return; stopped = true;
        btn.classList.remove('recording', 'hidden');
        if (stopBtn) stopBtn.classList.remove('visible');
        if (rec) { try { rec.stop(); } catch (e) {} }
        if (mediaRec.state === 'recording') { try { mediaRec.stop(); } catch (e) {} }
        window.activeRecognition = null;
      }
      window.activeRecognition = { mediaRec: mediaRec, endAll: endAll, recognition: null };

      mediaRec.start(100);

      if (hasSR) {
        rec = new SR();
        rec.lang = 'en-US'; rec.interimResults = false; rec.maxAlternatives = 3; rec.continuous = true;
        if (window.activeRecognition) window.activeRecognition.recognition = rec;
        rec.onresult = function (event) {
          if (typeof analyzeWords !== 'function' || !resultDiv) return;
          var best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9' ]/g, '');
          var analysis = analyzeWords(target, best);
          var totalWords = analysis.expected.length;
          var correctWords = analysis.expected.filter(function (w) { return w.status === 'correct'; }).length;
          resultDiv.classList.add('show'); resultDiv.classList.remove('good', 'try-again', 'bad');
          var html = '';
          if (analysis.score >= 0.8) { resultDiv.classList.add('good'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Excellent!'; if (typeof updateProgress === 'function') updateProgress(); }
          else if (analysis.score >= 0.5) { resultDiv.classList.add('try-again'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Almost there!'; }
          else { resultDiv.classList.add('bad'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Keep practicing!'; }
          html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
          analysis.expected.forEach(function (w) { html += '<span class="word-box word-' + (w.status === 'correct' ? 'correct' : 'missing') + '">' + w.word + '</span>'; });
          html += '</div></div>';
          resultDiv.innerHTML = html;
          /* NAO para a gravacao — usuario controla via Stop */
        };
        rec.onend = function () { if (!stopped && srRestarts++ < 60) { setTimeout(function () { if (!stopped) { try { rec.start(); } catch (e) {} } }, 250); } };
        rec.onerror = function () { /* ignora — gravacao continua */ };
        try { rec.start(); } catch (e) {}
      }

      setTimeout(endAll, 30000);
    }).catch(function () {
      btn.classList.remove('recording', 'hidden');
      if (stopBtn) stopBtn.classList.remove('visible');
      alert('Could not access microphone.');
    });
  };

  window.stopRecording = function (stopBtn) {
    var ar = window.activeRecognition;
    if (ar && typeof ar.endAll === 'function') { ar.endAll(); return; }
    if (ar) {
      try { if (ar.recognition) ar.recognition.stop(); } catch (e) {}
      try { if (ar.mediaRec && ar.mediaRec.state === 'recording') ar.mediaRec.stop(); } catch (e) {}
    }
  };
})();
