/**
 * Alumni — Activity Sync (Supabase + localStorage)
 *
 * Sincroniza o estado de exercicios do aluno (matches, blanks, quiz, speech,
 * mediaChecks, checklists) entre localStorage e Supabase.
 *
 * Requer:
 *   - supabase.min.js + supabase-config.js carregados ANTES
 *   - window.STUDENT_SLUG definido no <head>
 *   - saveState() e loadState() definidos no <script> principal do material
 *
 * Como funciona:
 *   1. Ao carregar: busca estado do Supabase. Se mais recente que localStorage, aplica.
 *   2. Ao salvar (saveState): salva localStorage (instantaneo) + upsert Supabase (debounce 2s).
 *   3. Fallback: se Supabase falhar, localStorage continua funcionando normalmente.
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

  // ===== COLLECT STATE (replica a logica do saveState original) =====
  function collectState() {
    var s = { matches: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: [] };

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
  function saveToSupabase() {
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(function() {
      var state = collectState();
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
    }, DEBOUNCE_MS);
  }

  // ===== WRAP saveState =====
  if (typeof window.saveState === 'function') {
    var _originalSaveState = window.saveState;
    window.saveState = function() {
      _originalSaveState();  // localStorage (instantaneo)
      saveToSupabase();      // Supabase (debounced)
    };
  }

  // ===== LOAD FROM SUPABASE (on page load) =====
  function loadFromSupabase() {
    sb.from('student_activity')
      .select('state, updated_at')
      .eq('student_slug', slug)
      .eq('view_type', viewType)
      .single()
      .then(function(res) {
        if (res.error || !res.data) return; // Sem dados no Supabase — localStorage ja carregou

        var remoteState = res.data.state;
        var remoteTime = new Date(res.data.updated_at).getTime();

        // Comparar com timestamp local
        var localTime = 0;
        try {
          var ts = localStorage.getItem(timestampKey);
          if (ts) localTime = new Date(ts).getTime();
        } catch(e) {}

        // Se Supabase e mais recente, aplicar por cima
        if (remoteTime > localTime) {
          applyState(remoteState);
          // Atualizar localStorage com dados do Supabase
          try {
            localStorage.setItem(localKey, JSON.stringify(remoteState));
            localStorage.setItem(timestampKey, res.data.updated_at);
          } catch(e) {}
        }
      });
  }

  // ===== INIT =====
  // loadState() original ja rodou (esta no script principal).
  // Agora verificamos se Supabase tem dados mais recentes.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      setTimeout(loadFromSupabase, 200);
    });
  } else {
    setTimeout(loadFromSupabase, 200);
  }

})();
