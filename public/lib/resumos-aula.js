/**
 * RESUMOS DAS AULAS — Alumni by Better
 * Injeta a tab "Resumos das Aulas" nos hubs professor/aluno.
 *
 * Lista as aulas ANALISADAS pelo sistema de Análise de Aulas
 * (https://alumni-dashboard-analisedeaula.vercel.app) e linka o resumo de cada uma.
 * Mesmo projeto Supabase deste repo: a tabela `analises` é lida direto com a anon key.
 *
 * POR QUE A LISTA É POR DATA, E NÃO POR NÚMERO DE AULA:
 *   A coluna `analises.lesson_number` é preenchida pelo sync do Zoom e está incorreta na
 *   maioria dos alunos (ex: 8 análises da Elaine todas marcadas como "aula 4"; as 6 aulas
 *   de julho da Carolina todas como "aula 2"). Casar a linha da aula N do Controle com
 *   esse número apontaria o resumo de OUTRA aula. A única chave confiável é a DATA da
 *   gravação — que é também a chave que o site de análise usa na URL. Por isso esta tab
 *   lista por data e não promete alinhamento com a numeração do currículo.
 *
 * Requisitos no HTML hospedeiro (já satisfeitos por controle-aulas.js, que carrega este):
 *   - window.STUDENT_SLUG definido
 *   - supabase-config.js carregado (variável sb)
 *   - switchTab() existente
 */
(function() {
  'use strict';

  if (window.__RESUMOS_AULA_LOADED) return;
  window.__RESUMOS_AULA_LOADED = true;

  var ANALISE_BASE = 'https://alumni-dashboard-analisedeaula.vercel.app';

  var slug = window.STUDENT_SLUG;
  if (!slug) return;
  if (typeof sb === 'undefined') return;

  var tabsContainer = document.querySelector('.tabs');
  if (!tabsContainer) return;

  // ── Tab button ──
  var tabBtn = document.createElement('button');
  tabBtn.className = 'tab-btn';
  tabBtn.setAttribute('onclick', "switchTab('resumos')");
  tabBtn.textContent = 'Resumos das Aulas';
  tabsContainer.appendChild(tabBtn);

  // ── Tab content ──
  var tabContent = document.createElement('div');
  tabContent.className = 'tab-content';
  tabContent.id = 'tab-resumos';
  var allTabContents = document.querySelectorAll('.tab-content');
  var lastTabContent = allTabContents[allTabContents.length - 1];
  if (lastTabContent && lastTabContent.parentNode) {
    lastTabContent.parentNode.insertBefore(tabContent, lastTabContent.nextSibling);
  }

  tabContent.innerHTML = '<div style="text-align:center;padding:3rem;"><div style="width:32px;height:32px;border:3px solid #e5e5e0;border-top-color:#003080;border-radius:50%;animation:spin .7s linear infinite;margin:0 auto 1rem;"></div><p style="font:500 .9rem/1.5 \'Inter\',sans-serif;color:#777;">Carregando resumos...</p></div>';

  // ── Styles ──
  var style = document.createElement('style');
  style.textContent = [
    '.resumos-header-row { display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:1rem;margin-bottom:.5rem; }',
    '.resumos-title { font:600 1.4rem/1.3 "Cormorant Garamond",Georgia,serif;color:#1a1a2e; }',
    '.resumos-subtitle { font:400 .88rem/1.5 "Inter",sans-serif;color:#777;max-width:60ch; }',
    '.resumos-card { background:#fff;border:1px solid #d4d4cc;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 8px rgba(0,0,0,.04); }',
    '.resumo-item { display:flex;align-items:center;gap:1rem;padding:.9rem .2rem;border-bottom:1px solid #e8e8e0; }',
    '.resumo-item:last-child { border-bottom:none; }',
    '.resumo-date { display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:58px;height:58px;background:#003080;color:#fff;border-radius:10px;flex-shrink:0; }',
    '.resumo-date .rd-day { font:700 1.15rem/1 "Inter",sans-serif; }',
    '.resumo-date .rd-mon { font:600 .68rem/1.3 "Inter",sans-serif;text-transform:uppercase;letter-spacing:.5px;opacity:.85; }',
    '.resumo-info { flex:1;min-width:0; }',
    '.resumo-info .ri-main { font:600 .92rem/1.4 "Inter",sans-serif;color:#2d2d3a; }',
    '.resumo-info .ri-sub { font:400 .8rem/1.4 "Inter",sans-serif;color:#777;margin-top:2px; }',
    '.resumo-link { display:inline-flex;align-items:center;gap:6px;padding:9px 16px;min-height:44px;box-sizing:border-box;font:600 .82rem/1.4 "Inter",sans-serif;color:#fff;background:#003080;border:2px solid #003080;border-radius:8px;text-decoration:none;transition:all .2s;flex-shrink:0; }',
    '.resumo-link:hover { background:#0043b0;border-color:#0043b0; }',
    '.resumo-link:focus-visible { outline:3px solid #d70c0c;outline-offset:2px; }',
    '.resumos-empty { text-align:center;padding:3rem;color:#777;font:500 .9rem/1.6 "Inter",sans-serif; }',
    '@media (prefers-reduced-motion:reduce) { .resumo-link { transition:none; } }',
    '@media (max-width:768px) {',
    '  .resumo-item { flex-wrap:wrap; }',
    '  .resumo-link { width:100%;justify-content:center; }',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  load();

  async function load() {
    try {
      var resp = await sb.from('analises')
        .select('id,data_aula')
        .eq('student_slug', slug)
        .order('data_aula', { ascending: false });
      if (resp.error) throw new Error(resp.error.message);
      render(resp.data || []);
    } catch (err) {
      console.error('Resumos das Aulas error:', err);
      tabContent.innerHTML = '<div class="resumos-empty">Erro ao carregar os resumos: ' + escHTML(err.message) + '</div>';
    }
  }

  function render(rows) {
    var header = '<div class="resumos-header-row"><div>' +
      '<div class="resumos-title">Resumos das Aulas</div>' +
      '<div class="resumos-subtitle">Aulas gravadas e analisadas automaticamente. Cada resumo traz o conteúdo estudado, palavras novas, pronúncia e plano de estudo daquele dia.</div>' +
      '</div></div>';

    if (!rows.length) {
      tabContent.innerHTML = header +
        '<div class="resumos-card"><div class="resumos-empty">Nenhuma aula analisada ainda.<br>Os resumos aparecem aqui depois que a gravação da aula é processada.</div></div>';
      return;
    }

    var items = rows.map(function(r) {
      var d = new Date(r.data_aula);
      var dd = fmt(d, { day: '2-digit' });
      var mon = fmt(d, { month: 'short' }).replace('.', '');
      var full = fmt(d, { day: '2-digit', month: '2-digit', year: 'numeric' });
      var weekday = fmt(d, { weekday: 'long' });

      // Duração NUNCA é exibida (pedido do Dan, 14/07/2026) — nem quando `duracao_min`
      // existe. Por isso ela também não é mais buscada no select().
      return '<div class="resumo-item">' +
        '<div class="resumo-date" aria-hidden="true"><span class="rd-day">' + escHTML(dd) + '</span><span class="rd-mon">' + escHTML(mon) + '</span></div>' +
        '<div class="resumo-info">' +
          '<div class="ri-main">Aula de ' + escHTML(full) + '</div>' +
          '<div class="ri-sub">' + escHTML(cap(weekday)) + '</div>' +
        '</div>' +
        '<a class="resumo-link" href="' + escAttrHTML(resumoUrl(r, d)) + '" target="_blank" rel="noopener" ' +
          'aria-label="Ver resumo da aula de ' + escAttrHTML(full) + '">Ver resumo</a>' +
      '</div>';
    }).join('');

    tabContent.innerHTML = header + '<div class="resumos-card">' + items + '</div>';
  }

  // URL amigável do site de análise: /resumo/<slug sem hífens>-aula<DD>-<MM>
  // O ?id= manda: com ele o site resolve a análise exata, então o caminho não precisa
  // acertar o fuso nem a convenção de nome — ele é só cosmético/legível.
  function resumoUrl(row, d) {
    var path = slug.replace(/-/g, '') + '-aula' + fmt(d, { day: '2-digit' }) + '-' + fmt(d, { month: '2-digit' });
    return ANALISE_BASE + '/resumo/' + encodeURIComponent(path) + '?id=' + encodeURIComponent(row.id);
  }

  // data_aula vem em UTC; o aluno e o professor pensam no horário de Brasília.
  function fmt(d, opts) {
    opts = Object.assign({ timeZone: 'America/Sao_Paulo' }, opts);
    return d.toLocaleDateString('pt-BR', opts);
  }

  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : ''; }
  function escHTML(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }
  function escAttrHTML(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

})();
