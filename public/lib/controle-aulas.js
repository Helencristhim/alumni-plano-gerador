/**
 * CONTROLE DE AULAS — Alumni by Better
 * Injeta tab "Controle de Aulas" em materiais professor/aluno.
 * Lê currículo do Supabase, salva feedbacks via upsert.
 *
 * Requisitos no HTML hospedeiro:
 *   - window.STUDENT_SLUG definido
 *   - supabase-config.js carregado (variável sb)
 *   - switchTab() existente (genérico)
 */
(function() {
  'use strict';

  // ── Detectar tipo de página ──
  var badges = document.querySelectorAll('.prof-badge, .view-badge');
  var isProfessor = false;
  badges.forEach(function(b) {
    var txt = (b.textContent || '').toLowerCase();
    if (txt.indexOf('professor') !== -1) isProfessor = true;
  });
  var isAluno = !isProfessor;

  var slug = window.STUDENT_SLUG;
  if (!slug) return;

  // ── Injetar tab button ──
  var tabsContainer = document.querySelector('.tabs');
  if (!tabsContainer) return;

  var tabBtn = document.createElement('button');
  tabBtn.className = 'tab-btn';
  tabBtn.setAttribute('onclick', "switchTab('controle')");
  tabBtn.textContent = 'Controle de Aulas';
  tabsContainer.appendChild(tabBtn);

  // ── Criar tab content ──
  var tabContent = document.createElement('div');
  tabContent.className = 'tab-content';
  tabContent.id = 'tab-controle';

  // Inserir após o último tab-content existente dentro do main-content
  var allTabContents = document.querySelectorAll('.tab-content');
  var lastTabContent = allTabContents[allTabContents.length - 1];
  if (lastTabContent && lastTabContent.parentNode) {
    lastTabContent.parentNode.insertBefore(tabContent, lastTabContent.nextSibling);
  }

  // ── Loading state ──
  tabContent.innerHTML = '<div style="text-align:center;padding:3rem;"><div style="width:32px;height:32px;border:3px solid #e5e5e0;border-top-color:#003080;border-radius:50%;animation:spin .7s linear infinite;margin:0 auto 1rem;"></div><p style="font:500 .9rem/1.5 \'Inter\',sans-serif;color:#777;">Carregando controle de aulas...</p></div>';

  // ── Styles ──
  var style = document.createElement('style');
  style.textContent = [
    '.controle-table { width:100%;border-collapse:separate;border-spacing:0;margin-top:1rem; }',
    '.controle-table th { background:#003080;color:#fff;padding:10px 14px;font:600 .78rem/1.4 "Inter",sans-serif;text-align:left;letter-spacing:.5px;text-transform:uppercase;position:sticky;top:0;z-index:2; }',
    '.controle-table th:first-child { border-radius:8px 0 0 0; }',
    '.controle-table th:last-child { border-radius:0 8px 0 0; }',
    '.controle-table td { padding:12px 14px;font:.88rem/1.5 "Inter",sans-serif;color:#2d2d3a;border-bottom:1px solid #e8e8e0;vertical-align:top; }',
    '.controle-table tr:hover td { background:rgba(0,48,128,.02); }',
    '.controle-table .lesson-num { font-weight:700;color:#003080;text-align:center;width:40px; }',
    '.controle-table .lesson-tema { font-weight:500;min-width:180px; }',
    '.controle-table input[type="date"] { border:1px solid #d4d4cc;border-radius:6px;padding:6px 10px;font:.85rem/1.4 "Inter",sans-serif;color:#2d2d3a;background:#fafaf7;outline:none;transition:border-color .2s;width:100%;min-width:130px; }',
    '.controle-table input[type="date"]:focus { border-color:#003080;box-shadow:0 0 0 3px rgba(0,48,128,.12); }',
    '.controle-table input[type="date"]:read-only { background:#f0f0eb;color:#777;cursor:default;border-color:transparent; }',
    '.controle-table textarea { width:100%;min-height:60px;border:1px solid #d4d4cc;border-radius:6px;padding:8px 10px;font:.85rem/1.5 "Inter",sans-serif;color:#2d2d3a;background:#fafaf7;resize:vertical;outline:none;transition:border-color .2s; }',
    '.controle-table textarea:focus { border-color:#003080;box-shadow:0 0 0 3px rgba(0,48,128,.12); }',
    '.controle-table textarea::placeholder { color:#aaa;font-style:italic; }',
    '.controle-bloco-header td { background:rgba(0,48,128,.06);font:600 .82rem/1.4 "Inter",sans-serif;color:#003080;letter-spacing:.5px;text-transform:uppercase;padding:8px 14px;border-bottom:2px solid rgba(0,48,128,.15); }',
    '.controle-header-row { display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;margin-bottom:.5rem; }',
    '.controle-title { font:600 1.4rem/1.3 "Cormorant Garamond",Georgia,serif;color:#1a1a2e; }',
    '.controle-subtitle { font:400 .88rem/1.5 "Inter",sans-serif;color:#777; }',
    '.controle-save-status { font:500 .78rem/1.4 "Inter",sans-serif;color:#16a34a;opacity:0;transition:opacity .3s; }',
    '.controle-save-status.show { opacity:1; }',
    '.controle-save-status.error { color:#dc2626; }',
    '.controle-card { background:#fff;border:1px solid #d4d4cc;border-radius:12px;padding:1.5rem 1.8rem;box-shadow:0 2px 8px rgba(0,0,0,.04); }',
    '.controle-empty { text-align:center;padding:3rem;color:#777;font:500 .9rem/1.5 "Inter",sans-serif; }',
    '@media (max-width:768px) {',
    '  .controle-card { padding:1rem;overflow-x:auto; }',
    '  .controle-table td, .controle-table th { padding:8px 10px;font-size:.8rem; }',
    '  .controle-table textarea { min-height:48px; }',
    '  .controle-table { min-width:600px; }',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  // ── Carregar dados ──
  loadControle();

  async function loadControle() {
    try {
      // 1. Buscar currículo do aluno
      var perfilResp = await sb.from('perfis').select('data,num_aulas').eq('id', slug).maybeSingle();
      if (perfilResp.error) throw new Error('Erro ao carregar perfil: ' + perfilResp.error.message);
      if (!perfilResp.data) { tabContent.innerHTML = '<div class="controle-empty">Perfil não encontrado.</div>'; return; }

      var perfil = perfilResp.data;
      var curriculo = (perfil.data && perfil.data.curriculo) || [];
      var numAulas = perfil.num_aulas || curriculo.length || 0;

      // Piso: a tabela nunca mostra MENOS aulas do que o material realmente tem.
      // window.TOTAL_AULAS é setado no HTML de cada aluno e reflete a contagem real
      // de aulas geradas; se o perfil no Supabase estiver defasado (ex: num_aulas=10
      // mas o aluno já tem 20), usamos o valor real. Só aumenta, nunca diminui.
      var realTotal = (typeof window !== 'undefined' && window.TOTAL_AULAS) ? parseInt(window.TOTAL_AULAS, 10) : 0;
      if (realTotal > numAulas) numAulas = realTotal;

      if (numAulas === 0) { tabContent.innerHTML = '<div class="controle-empty">Nenhuma aula cadastrada no currículo.</div>'; return; }

      // Título do MATERIAL autorado (Pre-class / IN CLASS) tem PRIORIDADE sobre o
      // curriculo do Supabase: o curriculo é o PLANO original e frequentemente divergiu
      // do que foi de fato gerado (título errado no Controle — REGRA 29). Se a aula já
      // existe no hub, o Controle mostra o título real dela; senão, cai no plano.
      var aulas = [];
      for (var i = 1; i <= numAulas; i++) {
        var found = curriculo.find(function(c) { return c.aula === i; });
        var authored = authoredTema(i);
        aulas.push({
          num: i,
          tema: authored || (found ? found.tema : 'Aula ' + i)
        });
      }

      // 2. Buscar dados salvos do controle
      var controleResp = await sb.from('controle_aulas').select('*').eq('student_slug', slug).order('lesson_number', { ascending: true });
      var savedData = {};
      if (!controleResp.error && controleResp.data) {
        controleResp.data.forEach(function(row) {
          savedData[row.lesson_number] = row;
        });
      }

      // 3. Detectar blocos (blocosGeracoes)
      var blocos = (perfil.data && perfil.data.blocosGeracoes) || [];

      // 4. Renderizar
      renderControle(aulas, savedData, blocos);

    } catch (err) {
      console.error('Controle de Aulas error:', err);
      tabContent.innerHTML = '<div class="controle-empty">Erro ao carregar: ' + escHTML(err.message) + '</div>';
    }
  }

  // Lê o título REAL da aula a partir do material autorado no hub: primeiro o
  // Pre-class (#ex-lesson-N h3), depois o menu IN CLASS (card com enterSlideMode(N)).
  // Retorna null se a aula ainda não foi gerada no hub (aí usa-se o plano do curriculo).
  function authoredTema(n) {
    var ex = document.getElementById('ex-lesson-' + n);
    if (ex) {
      var h3 = ex.querySelector('h3');
      if (h3 && h3.textContent && h3.textContent.trim()) return h3.textContent.trim();
    }
    var cards = document.querySelectorAll('[onclick*="enterSlideMode(' + n + ')"]');
    for (var k = 0; k < cards.length; k++) {
      var t = cards[k].querySelector('div[style*="font-weight:600"]');
      if (t && t.textContent && t.textContent.trim()) return t.textContent.trim();
    }
    return null;
  }

  function renderControle(aulas, savedData, blocos) {
    var totalAulas = aulas.length;

    // Header
    var headerHTML = '<div class="controle-header-row">' +
      '<div>' +
        '<div class="controle-title">Controle de Aulas</div>' +
        '<div class="controle-subtitle">' + totalAulas + ' aulas no programa</div>' +
      '</div>' +
      '<div class="controle-save-status" id="controleSaveStatus">Salvo</div>' +
    '</div>';

    // Colunas por tipo
    var colsHTML = '<tr>';
    colsHTML += '<th style="width:40px;">#</th>';
    colsHTML += '<th>Tema</th>';
    colsHTML += '<th style="width:150px;">Data da Aula</th>';
    if (isProfessor) {
      colsHTML += '<th>Feedback do Aluno</th>';
      colsHTML += '<th>Feedback do Material</th>';
    } else {
      colsHTML += '<th>Feedback da Aula</th>';
      colsHTML += '<th>Feedback do Material</th>';
    }
    colsHTML += '</tr>';

    // Mapear blocos para saber onde inserir headers
    var blocoMap = {};
    blocos.forEach(function(b, idx) {
      if (b && b.aulaInicio) {
        blocoMap[b.aulaInicio] = b.nome || b.titulo || ('Bloco ' + (idx + 1));
      }
    });

    // Rows
    var rowsHTML = '';
    var totalCols = isProfessor ? 5 : 5;

    aulas.forEach(function(aula) {
      var n = aula.num;
      var saved = savedData[n] || {};

      // Bloco header
      if (blocoMap[n]) {
        rowsHTML += '<tr class="controle-bloco-header"><td colspan="' + totalCols + '">' + escHTML(blocoMap[n]) + '</td></tr>';
      }

      rowsHTML += '<tr data-lesson="' + n + '">';
      rowsHTML += '<td class="lesson-num">' + n + '</td>';

      // Tema — limpar sufixos longos
      var temaDisplay = aula.tema;
      var dashIdx = temaDisplay.indexOf(' — ');
      if (dashIdx > 0 && dashIdx < 60) temaDisplay = temaDisplay.substring(0, dashIdx);
      if (temaDisplay.length > 65) temaDisplay = temaDisplay.substring(0, 62) + '...';
      rowsHTML += '<td class="lesson-tema" title="' + escAttrHTML(aula.tema) + '">' + escHTML(temaDisplay) + '</td>';

      // Data
      var dateVal = saved.aula_date || '';
      if (isProfessor) {
        rowsHTML += '<td><input type="date" value="' + escAttrHTML(dateVal) + '" data-field="aula_date" data-lesson="' + n + '" onchange="window._controleChange(this)"></td>';
      } else {
        var dateDisplay = dateVal ? formatDate(dateVal) : '<span style="color:#aaa;font-style:italic;">Aguardando</span>';
        rowsHTML += '<td>' + dateDisplay + '</td>';
      }

      // Feedback fields
      if (isProfessor) {
        var fb1 = saved.prof_feedback_aluno || '';
        var fb2 = saved.prof_feedback_material || '';
        rowsHTML += '<td><textarea placeholder="Como foi o aluno nesta aula..." data-field="prof_feedback_aluno" data-lesson="' + n + '" oninput="window._controleDebounce(this)">' + escHTML(fb1) + '</textarea></td>';
        rowsHTML += '<td><textarea placeholder="Feedback sobre o material..." data-field="prof_feedback_material" data-lesson="' + n + '" oninput="window._controleDebounce(this)">' + escHTML(fb2) + '</textarea></td>';
      } else {
        var fb1a = saved.aluno_feedback_aula || '';
        var fb2a = saved.aluno_feedback_material || '';
        rowsHTML += '<td><textarea placeholder="O que você achou da aula..." data-field="aluno_feedback_aula" data-lesson="' + n + '" oninput="window._controleDebounce(this)">' + escHTML(fb1a) + '</textarea></td>';
        rowsHTML += '<td><textarea placeholder="Feedback sobre o material..." data-field="aluno_feedback_material" data-lesson="' + n + '" oninput="window._controleDebounce(this)">' + escHTML(fb2a) + '</textarea></td>';
      }

      rowsHTML += '</tr>';
    });

    tabContent.innerHTML = headerHTML +
      '<div class="controle-card">' +
        '<table class="controle-table">' +
          '<thead>' + colsHTML + '</thead>' +
          '<tbody>' + rowsHTML + '</tbody>' +
        '</table>' +
      '</div>';
  }

  // ── Save logic ──
  var saveTimers = {};

  window._controleDebounce = function(el) {
    var lesson = el.getAttribute('data-lesson');
    var field = el.getAttribute('data-field');
    var key = lesson + '-' + field;
    clearTimeout(saveTimers[key]);
    saveTimers[key] = setTimeout(function() {
      saveField(parseInt(lesson), field, el.value);
    }, 1500);
  };

  window._controleChange = function(el) {
    var lesson = parseInt(el.getAttribute('data-lesson'));
    var field = el.getAttribute('data-field');
    saveField(lesson, field, el.value);
  };

  async function saveField(lessonNumber, field, value) {
    var statusEl = document.getElementById('controleSaveStatus');
    try {
      statusEl.textContent = 'Salvando...';
      statusEl.classList.remove('error');
      statusEl.classList.add('show');

      var payload = {
        student_slug: slug,
        lesson_number: lessonNumber,
        updated_at: new Date().toISOString()
      };
      payload[field] = value;

      var resp = await sb.from('controle_aulas').upsert(payload, { onConflict: 'student_slug,lesson_number' });
      if (resp.error) throw new Error(resp.error.message);

      statusEl.textContent = 'Salvo';
      statusEl.classList.remove('error');
      setTimeout(function() { statusEl.classList.remove('show'); }, 2000);
    } catch (err) {
      console.error('Erro ao salvar controle:', err);
      statusEl.textContent = 'Erro ao salvar';
      statusEl.classList.add('error', 'show');
    }
  }

  // ── Helpers ──
  function escHTML(s) { var d = document.createElement('div'); d.textContent = s || ''; return d.innerHTML; }
  function escAttrHTML(s) { return String(s || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function formatDate(dateStr) {
    if (!dateStr) return '';
    var parts = dateStr.split('-');
    if (parts.length === 3) return parts[2] + '/' + parts[1] + '/' + parts[0];
    return dateStr;
  }

})();
