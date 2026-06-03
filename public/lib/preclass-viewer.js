/**
 * Alumni — Pre-class Viewer (Professor View)
 *
 * Mostra o progresso Pre-class do ALUNO dentro da pagina do professor.
 * Carregado automaticamente pelo activity-sync.js quando viewType === 'professor'.
 *
 * Busca student_activity (view_type='aluno') do Supabase e exibe um painel
 * com resumo visual do que o aluno fez.
 *
 * NAO modifica nenhum arquivo HTML existente.
 */

(function() {
  var slug = window.STUDENT_SLUG;
  if (!slug) return;
  if (typeof sb === 'undefined') return;

  // Só mostrar na pagina do professor
  var path = window.location.pathname;
  if (path.indexOf('/professor/') === -1) return;

  function init() {
    sb.from('student_activity')
      .select('state, updated_at')
      .eq('student_slug', slug)
      .eq('view_type', 'aluno')
      .single()
      .then(function(res) {
        if (res.error || !res.data || !res.data.state) {
          renderPanel(null);
          return;
        }
        renderPanel(res.data);
      });
  }

  function renderPanel(data) {
    var panel = document.createElement('div');
    panel.id = 'preclass-viewer-panel';

    if (!data) {
      panel.innerHTML = buildPanelHTML(null);
    } else {
      panel.innerHTML = buildPanelHTML(data);
    }

    // Inserir antes do primeiro tab-content ou no topo do main-content
    var target = document.querySelector('.main-content') || document.querySelector('.container') || document.body;
    var firstTab = target.querySelector('.tab-content');
    if (firstTab) {
      target.insertBefore(panel, firstTab);
    } else {
      var tabNav = target.querySelector('.tab-nav');
      if (tabNav) {
        tabNav.parentElement.insertBefore(panel, tabNav.nextSibling);
      } else {
        target.prepend(panel);
      }
    }

    // Auto-refresh a cada 60s
    setInterval(function() {
      sb.from('student_activity')
        .select('state, updated_at')
        .eq('student_slug', slug)
        .eq('view_type', 'aluno')
        .single()
        .then(function(res) {
          if (res.error || !res.data) return;
          var existing = document.getElementById('preclass-viewer-panel');
          if (existing) existing.innerHTML = buildPanelHTML(res.data);
        });
    }, 60000);
  }

  function buildPanelHTML(data) {
    var accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#003080';
    var accentDim = 'rgba(0,48,128,0.06)';

    var css = '<style>' +
      '#preclass-viewer-panel{margin:16px 0 24px;font-family:var(--font-body,-apple-system,BlinkMacSystemFont,"Inter",sans-serif)}' +
      '.pcv-card{background:var(--bg-card,#fff);border:1px solid var(--border-light,#e0e0e0);border-radius:12px;padding:20px 24px;box-shadow:0 2px 8px rgba(0,0,0,0.04)}' +
      '.pcv-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:8px}' +
      '.pcv-title{font:600 1rem/1.3 var(--font-body);color:var(--text,#1a1a2e);display:flex;align-items:center;gap:8px}' +
      '.pcv-title svg{color:' + accent + '}' +
      '.pcv-time{font:400 0.78rem/1.4 var(--font-body);color:var(--text-dim,#888)}' +
      '.pcv-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px}' +
      '.pcv-stat{background:' + accentDim + ';border-radius:8px;padding:14px 16px;text-align:center}' +
      '.pcv-stat-num{font:700 1.5rem/1 var(--font-body);color:' + accent + ';margin-bottom:4px}' +
      '.pcv-stat-label{font:500 0.75rem/1.3 var(--font-body);color:var(--text-dim,#888);text-transform:uppercase;letter-spacing:0.3px}' +
      '.pcv-empty{text-align:center;padding:24px;color:var(--text-dim,#888);font:400 0.9rem/1.5 var(--font-body)}' +
      '.pcv-empty svg{margin-bottom:8px;opacity:0.4}' +
      '.pcv-details{margin-top:16px;border-top:1px solid var(--border-light,#e0e0e0);padding-top:16px}' +
      '.pcv-detail-title{font:600 0.8rem/1.4 var(--font-body);color:var(--text-mid,#555);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.3px}' +
      '.pcv-pills{display:flex;flex-wrap:wrap;gap:6px}' +
      '.pcv-pill{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:20px;font:500 0.75rem/1.4 var(--font-body);background:var(--success-bg,rgba(22,163,74,0.08));color:var(--success,#16a34a);border:1px solid var(--success-border,rgba(22,163,74,0.2))}' +
      '.pcv-pill svg{width:12px;height:12px}' +
      '.pcv-section{margin-bottom:12px}' +
      '.pcv-section:last-child{margin-bottom:0}' +
      '.pcv-audio{display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--bg-elevated,#f5f5f0);border-radius:8px;margin-bottom:8px}' +
      '.pcv-audio-label{font:500 0.8rem/1.3 var(--font-body);color:var(--text,#1a1a2e);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
      '.pcv-audio audio{height:32px;max-width:220px;flex-shrink:0}' +
      '.pcv-mic-icon{color:var(--accent,#003080);flex-shrink:0}' +
      '.pcv-live{display:inline-flex;align-items:center;gap:4px;font:600 0.7rem/1 var(--font-body);color:var(--success,#16a34a);text-transform:uppercase;letter-spacing:0.5px}' +
      '.pcv-live-dot{width:6px;height:6px;border-radius:50%;background:var(--success,#16a34a);animation:pcv-pulse 2s ease-in-out infinite}' +
      '@keyframes pcv-pulse{0%,100%{opacity:1}50%{opacity:0.3}}' +
      '@media(max-width:640px){.pcv-grid{grid-template-columns:1fr 1fr}.pcv-card{padding:16px}}' +
      '</style>';

    var checkIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>';
    var eyeIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>';
    var emptyIcon = '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="8" y1="15" x2="16" y2="15"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>';

    if (!data) {
      return css +
        '<div class="pcv-card">' +
          '<div class="pcv-header"><div class="pcv-title">' + eyeIcon + ' Progresso Pre-class do Aluno</div></div>' +
          '<div class="pcv-empty">' + emptyIcon + '<div>O aluno ainda não iniciou o Pre-class.</div><div style="font-size:0.8rem;margin-top:4px">Os dados aparecem aqui automaticamente quando o aluno começar os exercícios.</div></div>' +
        '</div>';
    }

    var s = data.state;
    var updatedAt = data.updated_at;

    // Count totals
    var blanksCount = (s.blanks && s.blanks.length) || 0;
    var quizCount = (s.quiz && s.quiz.length) || 0;
    var matchesCount = (s.matches && s.matches.length) || 0;
    var speechCount = (s.speech && s.speech.length) || 0;
    var orderingCount = (s.ordering && s.ordering.length) || 0;
    var mediaCount = 0;
    if (s.mediaChecks) {
      if (Array.isArray(s.mediaChecks)) mediaCount = s.mediaChecks.length;
      else mediaCount = Object.keys(s.mediaChecks).filter(function(k) { return s.mediaChecks[k]; }).length;
    }

    var recordingsCount = (s.recordings && typeof s.recordings === 'object') ? Object.keys(s.recordings).length : 0;
    var totalExercises = blanksCount + quizCount + matchesCount + speechCount + orderingCount;

    // Format update time
    var timeStr = '';
    if (updatedAt) {
      var d = new Date(updatedAt);
      timeStr = 'Atualizado em ' + d.toLocaleDateString('pt-BR') + ' às ' + d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
    }

    var html = css +
      '<div class="pcv-card">' +
        '<div class="pcv-header">' +
          '<div class="pcv-title">' + eyeIcon + ' Progresso Pre-class do Aluno</div>' +
          '<div style="display:flex;align-items:center;gap:12px">' +
            '<span class="pcv-live"><span class="pcv-live-dot"></span> LIVE</span>' +
            '<span class="pcv-time">' + esc(timeStr) + '</span>' +
          '</div>' +
        '</div>';

    // Stats grid
    html += '<div class="pcv-grid">';
    html += buildStat(totalExercises, 'Exercícios Feitos');
    if (blanksCount > 0) html += buildStat(blanksCount, 'Fill-in-blank');
    if (quizCount > 0) html += buildStat(quizCount, 'Quiz');
    if (matchesCount > 0) html += buildStat(matchesCount, 'Matching');
    if (speechCount > 0) html += buildStat(speechCount, 'Pronúncia');
    if (orderingCount > 0) html += buildStat(orderingCount, 'Ordering');
    if (mediaCount > 0) html += buildStat(mediaCount, 'Mídias Assistidas');
    if (recordingsCount > 0) html += buildStat(recordingsCount, 'Gravações');
    html += '</div>';

    // Recordings section — audio players for professor
    if (recordingsCount > 0) {
      var micIcon = '<svg class="pcv-mic-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="1" width="6" height="11" rx="3"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>';
      html += '<div class="pcv-details"><div class="pcv-section"><div class="pcv-detail-title">Gravações do Aluno</div>';
      Object.keys(s.recordings).forEach(function(phraseId) {
        var audioUrl = s.recordings[phraseId];
        var label = phraseId.length > 50 ? phraseId.substring(0, 50) + '...' : phraseId;
        html += '<div class="pcv-audio">' +
          micIcon +
          '<span class="pcv-audio-label" title="' + esc(phraseId) + '">' + esc(label) + '</span>' +
          '<audio controls preload="none" src="' + esc(audioUrl) + '"></audio>' +
        '</div>';
      });
      html += '</div></div>';
    }

    // Details section — show what was completed
    var hasDetails = blanksCount > 0 || matchesCount > 0 || speechCount > 0;
    if (hasDetails) {
      html += '<div class="pcv-details">';

      if (blanksCount > 0) {
        html += '<div class="pcv-section"><div class="pcv-detail-title">Vocabulário Completado</div><div class="pcv-pills">';
        s.blanks.forEach(function(word) {
          html += '<span class="pcv-pill">' + checkIcon + ' ' + esc(word) + '</span>';
        });
        html += '</div></div>';
      }

      if (matchesCount > 0) {
        html += '<div class="pcv-section"><div class="pcv-detail-title">Matching Correto</div><div class="pcv-pills">';
        s.matches.forEach(function(m) {
          var parts = m.split('|');
          html += '<span class="pcv-pill">' + checkIcon + ' ' + esc(parts[0]) + '</span>';
        });
        html += '</div></div>';
      }

      if (speechCount > 0) {
        html += '<div class="pcv-section"><div class="pcv-detail-title">Pronúncia Praticada</div><div class="pcv-pills">';
        s.speech.forEach(function(phrase) {
          html += '<span class="pcv-pill">' + checkIcon + ' ' + esc(truncate(phrase, 40)) + '</span>';
        });
        html += '</div></div>';
      }

      if (quizCount > 0) {
        html += '<div class="pcv-section"><div class="pcv-detail-title">Quiz Respondido</div><div class="pcv-pills">';
        s.quiz.forEach(function(q) {
          html += '<span class="pcv-pill">' + checkIcon + ' ' + esc(truncate(q, 30)) + '</span>';
        });
        html += '</div></div>';
      }

      html += '</div>';
    }

    html += '</div>';
    return html;
  }

  function buildStat(num, label) {
    return '<div class="pcv-stat"><div class="pcv-stat-num">' + num + '</div><div class="pcv-stat-label">' + label + '</div></div>';
  }

  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function truncate(s, n) { return s.length > n ? s.substring(0, n) + '...' : s; }

  // Init
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { setTimeout(init, 500); });
  } else {
    setTimeout(init, 500);
  }
})();
