/* ═══════════════════════════════════════════════════════════════
   ALUMNI BY BETTER — ACTIVITY TRACKER
   Registra todas as atividades do aluno em localStorage.
   Oferece funcionalidade de "Refazer" exercicios.
   Auto-inicializa — basta incluir o script na pagina.
   ═══════════════════════════════════════════════════════════════ */

var AlumniTracker = (function() {
  'use strict';

  // Detecta o ID do aluno a partir da URL: /aluno/maisa.html → "maisa"
  function getStudentId() {
    var path = location.pathname;
    var match = path.match(/\/(?:aluno|planos)\/([^/?#]+?)(?:\.html)?(?:[?#]|$)/);
    return match ? match[1] : 'unknown';
  }

  var STUDENT_ID = getStudentId();
  var STORAGE_KEY = 'alumni-activity-' + STUDENT_ID;

  // ── Carregar / Salvar ──
  function loadLog() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []; }
    catch(e) { return []; }
  }

  function saveLog(log) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(log)); } catch(e) {}
  }

  // ── Registrar atividade ──
  function track(exerciseId, data) {
    var log = loadLog();
    var entry = {
      id: exerciseId,
      type: data.type || 'unknown',
      label: data.label || exerciseId,
      score: data.score || null,       // ex: "5/5", "3/4", "correct", "recorded"
      result: data.result || 'done',   // "correct", "incorrect", "partial", "done"
      attempt: countAttempts(exerciseId) + 1,
      timestamp: new Date().toISOString()
    };
    log.push(entry);
    saveLog(log);
    showCompletionBadge(exerciseId, entry);
    return entry;
  }

  // ── Contar tentativas de um exercicio ──
  function countAttempts(exerciseId) {
    return loadLog().filter(function(e) { return e.id === exerciseId; }).length;
  }

  // ── Ultimo resultado de um exercicio ──
  function lastResult(exerciseId) {
    var entries = loadLog().filter(function(e) { return e.id === exerciseId; });
    return entries.length > 0 ? entries[entries.length - 1] : null;
  }

  // ── Historico completo de um exercicio ──
  function history(exerciseId) {
    return loadLog().filter(function(e) { return e.id === exerciseId; });
  }

  // ── Resumo geral ──
  function summary() {
    var log = loadLog();
    var exercises = {};
    log.forEach(function(e) {
      if (!exercises[e.id]) exercises[e.id] = { id: e.id, type: e.type, label: e.label, attempts: 0, bestResult: null, lastAt: null };
      exercises[e.id].attempts++;
      exercises[e.id].lastAt = e.timestamp;
      if (e.result === 'correct') exercises[e.id].bestResult = 'correct';
      else if (!exercises[e.id].bestResult) exercises[e.id].bestResult = e.result;
    });
    return Object.values(exercises);
  }

  // ── Badge de conclusao no exercicio ──
  function showCompletionBadge(exerciseId, entry) {
    var el = document.getElementById(exerciseId);
    if (!el) return;

    // Remove badge anterior se existir
    var old = el.querySelector('.tracker-badge');
    if (old) old.remove();

    var badge = document.createElement('div');
    badge.className = 'tracker-badge';

    var isSuccess = entry.result === 'correct' || entry.result === 'done';
    var color = isSuccess ? 'var(--success, #16803d)' : 'var(--warning, #b45309)';
    var bgColor = isSuccess ? 'var(--success-bg, rgba(22,128,61,0.06))' : 'var(--warning-bg, rgba(180,83,9,0.06))';
    var borderColor = isSuccess ? 'var(--success-border, rgba(22,128,61,0.2))' : 'var(--warning-border, rgba(180,83,9,0.2))';
    var icon = isSuccess
      ? '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>'
      : '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';

    var dateStr = new Date(entry.timestamp).toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' });
    var timeStr = new Date(entry.timestamp).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
    var attemptLabel = entry.attempt > 1 ? ' (' + entry.attempt + 'a tentativa)' : '';
    var scoreLabel = entry.score ? ' — ' + entry.score : '';

    badge.style.cssText = 'display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:12px;padding:10px 14px;background:' + bgColor + ';border:1px solid ' + borderColor + ';border-radius:8px;font:500 0.8rem/1.4 var(--font-body, -apple-system, sans-serif);color:' + color + ';flex-wrap:wrap;';

    badge.innerHTML =
      '<span style="display:flex;align-items:center;gap:6px;">' +
        icon +
        '<span>Concluído em ' + dateStr + ' as ' + timeStr + scoreLabel + attemptLabel + '</span>' +
      '</span>' +
      '<button class="tracker-redo-btn" data-exercise-id="' + exerciseId + '" style="' +
        'display:inline-flex;align-items:center;gap:5px;padding:6px 14px;' +
        'font:600 0.78rem/1.4 var(--font-body, -apple-system, sans-serif);' +
        'color:var(--alumni-navy, #003080);background:var(--bg-card, #fff);' +
        'border:1px solid var(--border, #d4d4cc);border-radius:6px;cursor:pointer;' +
        'transition:all 150ms ease;white-space:nowrap;' +
      '">' +
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>' +
        'Refazer' +
      '</button>';

    el.appendChild(badge);

    // Hover no botao
    var btn = badge.querySelector('.tracker-redo-btn');
    btn.addEventListener('mouseenter', function() {
      this.style.borderColor = 'var(--alumni-navy, #003080)';
      this.style.background = 'var(--alumni-navy-dim, rgba(0,48,128,0.08))';
    });
    btn.addEventListener('mouseleave', function() {
      this.style.borderColor = 'var(--border, #d4d4cc)';
      this.style.background = 'var(--bg-card, #fff)';
    });
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      resetExercise(exerciseId);
    });
  }

  // ── Reset exercicio para refazer ──
  function resetExercise(exerciseId) {
    var el = document.getElementById(exerciseId);
    if (!el) return;

    // Remove badge
    var badge = el.querySelector('.tracker-badge');
    if (badge) badge.remove();

    // Matching dropdown: reset selects, icons, feedback
    el.querySelectorAll('select').forEach(function(sel) {
      sel.value = '';
      sel.style.borderColor = '';
      sel.style.background = '';
      sel.disabled = false;
      var row = sel.closest('.fill-item');
      if (row) row.style.pointerEvents = '';
    });
    el.querySelectorAll('[id*="_icon_"]').forEach(function(ic) { ic.innerHTML = ''; });
    el.querySelectorAll('[id*="_feedback_"]').forEach(function(fb) { fb.textContent = ''; });
    var result = el.querySelector('[id$="_result"]');
    if (result) result.innerHTML = '';

    // Fill-in-blank: reset inputs
    el.querySelectorAll('.fill-item__input').forEach(function(input) {
      input.value = '';
      input.readOnly = false;
      input.classList.remove('is-correct', 'is-wrong');
    });
    el.querySelectorAll('[id*="_fb_"]').forEach(function(fb) { fb.innerHTML = ''; });
    // Also reset the main feedback
    var mainFb = el.querySelector('[id$="_fb"]');
    if (mainFb) mainFb.innerHTML = '';

    // Multiple choice: reset options
    el.querySelectorAll('.quiz-option-student').forEach(function(opt) {
      opt.classList.remove('is-correct', 'is-wrong');
      opt.style.pointerEvents = '';
    });

    // Ordering: reset colors
    el.querySelectorAll('[data-word]').forEach(function(item) {
      item.style.borderColor = '';
      item.style.background = '';
    });

    // Pronunciation: reset word highlights and score
    el.querySelectorAll('[id*="_w_"]').forEach(function(w) {
      w.style.color = '';
      w.style.background = '';
    });
    var score = el.querySelector('[id$="_score"]');
    if (score) score.innerHTML = '';

    // Manual HTML fallback classes
    el.querySelectorAll('.correct, .wrong, .correct-order').forEach(function(item) {
      item.classList.remove('correct', 'wrong', 'correct-order');
    });
    el.querySelectorAll('.match-row select').forEach(function(sel) {
      sel.disabled = false;
      sel.value = '';
    });
    el.querySelectorAll('.blank-input').forEach(function(input) {
      input.value = '';
      input.classList.remove('correct', 'wrong');
      input.readOnly = false;
    });
    el.querySelectorAll('.speech-result').forEach(function(r) {
      r.classList.remove('show', 'good', 'try-again', 'bad');
      r.innerHTML = '';
    });
  }

  // ── Restaurar badges ao carregar pagina ──
  function restoreBadges() {
    var log = loadLog();
    var seen = {};
    // Percorrer de tras pra frente para pegar o ultimo de cada exercicio
    for (var i = log.length - 1; i >= 0; i--) {
      if (!seen[log[i].id]) {
        seen[log[i].id] = log[i];
      }
    }
    Object.keys(seen).forEach(function(exId) {
      var el = document.getElementById(exId);
      if (el) showCompletionBadge(exId, seen[exId]);
    });
  }

  // ── Inicializar ao carregar pagina ──
  function init() {
    // Aguardar exercicios serem renderizados (eles usam DOMContentLoaded tambem)
    setTimeout(restoreBadges, 500);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // API publica
  return {
    track: track,
    countAttempts: countAttempts,
    lastResult: lastResult,
    history: history,
    summary: summary,
    resetExercise: resetExercise,
    getStudentId: getStudentId
  };
})();
