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

  var saveTimer = null;
  var DEBOUNCE_MS = 2000;
  var AUTO_SAVE_MS = 30000;
  var lastSavedJSON = '';

  // ===== COLLECT STATE (replica a logica do saveState original) =====
  function collectState() {
    var s = { matches: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: [], ordering: [] };

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

    document.querySelectorAll('.speech-result.good').forEach(function(e) {
      var card = e.closest('.speech-card');
      if (card && card.dataset.phrase) s.speech.push(card.dataset.phrase);
    });

    document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) {
      s.checklists[i] = cb.checked;
    });

    // Ordering exercises completados
    document.querySelectorAll('.order-container').forEach(function(oc) {
      var items = oc.querySelectorAll('.order-item');
      var correct = oc.querySelectorAll('.order-item.correct-order');
      if (items.length > 0 && items.length === correct.length) {
        var id = oc.id || oc.closest('[id]')?.id || 'order-' + s.ordering.length;
        s.ordering.push(id);
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

    // Atualizar progresso visual
    if (typeof updateProgress === 'function') updateProgress();
  }

  // ===== SAVE TO SUPABASE (debounced) =====
  function saveToSupabase(force) {
    if (saveTimer) clearTimeout(saveTimer);
    var delay = force ? 0 : DEBOUNCE_MS;

    saveTimer = setTimeout(function() {
      var state = collectState();
      var stateJSON = JSON.stringify(state);

      // Evitar saves redundantes (nada mudou)
      if (stateJSON === lastSavedJSON && !force) return;
      lastSavedJSON = stateJSON;

      var now = new Date().toISOString();

      // Salvar timestamp local para comparacao
      try { localStorage.setItem(timestampKey, now); } catch(e) {}

      sb.from('student_activity')
        .upsert({
          student_slug: slug,
          view_type: viewType,
          state: state,
          updated_at: now
        }, { onConflict: 'student_slug,view_type' })
        .then(function(res) {
          if (res.error) console.error('activity-sync save error:', res.error.message);
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
    // Ler estado atual, adicionar/atualizar recording ref, salvar
    sb.from('student_activity')
      .select('state')
      .eq('student_slug', slug)
      .eq('view_type', viewType)
      .single()
      .then(function(res) {
        var state = (res.data && res.data.state) || collectState();
        if (!state.recordings) state.recordings = {};
        state.recordings[phraseId] = url;

        var now = new Date().toISOString();
        sb.from('student_activity')
          .upsert({
            student_slug: slug,
            view_type: viewType,
            state: state,
            updated_at: now
          }, { onConflict: 'student_slug,view_type' })
          .then(function(r) {
            if (r.error) console.error('recording ref save error:', r.error.message);
            else {
              // Injetar botao "My Recording" imediatamente apos salvar
              var recs = {};
              recs[phraseId] = url;
              injectMyRecordingButtons(recs);
            }
          });
      });
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
        // Parar qualquer audio anterior
        document.querySelectorAll('.my-rec-audio-active').forEach(function(a) {
          a.pause(); a.currentTime = 0; a.remove();
        });

        var audio = new Audio(audioUrl);
        audio.className = 'my-rec-audio-active';
        audio.style.display = 'none';
        document.body.appendChild(audio);

        btn.innerHTML = headphoneIcon + ' Playing...';
        btn.style.background = '#15803d';
        audio.play();
        audio.onended = function() {
          btn.innerHTML = headphoneIcon + ' My Recording';
          btn.style.background = '';
          audio.remove();
        };
        audio.onerror = function() {
          btn.innerHTML = headphoneIcon + ' My Recording';
          btn.style.background = '';
          audio.remove();
        };
      };

      controls.appendChild(btn);
    });
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

  // Apos upload de gravacao, injetar botao imediatamente
  var _origSaveRecordingRef = null;

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
    var state = collectState();
    var stateJSON = JSON.stringify(state);
    if (stateJSON === lastSavedJSON) return;

    var now = new Date().toISOString();
    try { localStorage.setItem(timestampKey, now); } catch(e) {}

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
        var remoteTime = new Date(res.data.updated_at).getTime();

        // Comparar com timestamp local
        var localTime = 0;
        try {
          var ts = localStorage.getItem(timestampKey);
          if (ts) localTime = new Date(ts).getTime();
        } catch(e) {}

        // Se Supabase e mais recente OU se localStorage nao tem dados, aplicar
        var hasLocalData = false;
        try { hasLocalData = !!localStorage.getItem(localKey); } catch(e) {}

        if (remoteTime > localTime || !hasLocalData) {
          applyState(remoteState);
          // Atualizar localStorage com dados do Supabase
          try {
            localStorage.setItem(localKey, JSON.stringify(remoteState));
            localStorage.setItem(timestampKey, res.data.updated_at);
          } catch(e) {}
          // Guardar como baseline para evitar re-save imediato
          lastSavedJSON = JSON.stringify(remoteState);
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

  // ===== INIT =====
  function init() {
    // Interceptar MediaRecorder ANTES de qualquer gravacao
    if (viewType === 'aluno') interceptRecordings();

    // Capturar estado atual como baseline
    lastSavedJSON = JSON.stringify(collectState());

    // Carregar do Supabase (pode sobrescrever se mais recente)
    setTimeout(loadFromSupabase, 200);

    // Carregar botoes "My Recording" para gravacoes salvas
    setTimeout(loadSavedRecordings, 600);

    // Ativar fallbacks
    setupEventListeners();
    startAutoSave();

    // Carregar viewer de Pre-class nas paginas de professor
    loadPreclassViewer();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { init(); });
  } else {
    init();
  }

})();
