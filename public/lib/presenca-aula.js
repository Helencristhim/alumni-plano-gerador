/**
 * PRESENÇA — Alumni by Better
 * Injeta a tab "Presença" SÓ no link do PROFESSOR, e SÓ em material IMERSIVO
 * (pedido da Helen, 28/10/2026: "só no link do professor, não aparece no link do
 * aluno, e é só para alunos imersivos por enquanto").
 *
 *   - link do professor  = página em /professor/...  (o hub em /aluno/ nunca recebe a tab)
 *   - material imersivo  = hub SEM <meta name="alumni-anatomia" content="consultivo">
 *                          (o mesmo carimbo que scripts/build_anatomias.py lê)
 *
 * Os dados vêm do sistema de Análise de Aulas (GET /api/presenca?slug=), que cruza todo dia
 * os dias em que a sala do Zoom do aluno abriu com as aulas analisadas:
 *   aula         -> tem aula analisada no dia
 *   falta        -> a sala ficou aberta 10+ min e só uma pessoa entrou, ou ninguém falou
 *   sem_registro -> a sala abriu e não ficou gravação para saber
 *
 * Carregado por controle-aulas.js, igual ao resumos-aula.js: chega em todos os hubs sem
 * editar nenhum HTML de aluno (REGRA 30 — o legado é intocável).
 */
(function() {
  'use strict';

  if (window.__PRESENCA_AULA_LOADED) return;
  window.__PRESENCA_AULA_LOADED = true;

  if (!/^\/professor\//.test(location.pathname)) return;
  if (document.querySelector('meta[name="alumni-anatomia"][content="consultivo"]')) return;

  var API = 'https://alumni-dashboard-analisedeaula.vercel.app/api/presenca';
  var ANALISE_BASE = 'https://alumni-dashboard-analisedeaula.vercel.app';

  var slug = window.STUDENT_SLUG;
  if (!slug) return;
  // Hub preservado de um cutover ({slug}-anterior) fala do mesmo aluno.
  var slugAluno = String(slug).replace(/-anterior$/, '');

  var tabsContainer = document.querySelector('.tabs');
  if (!tabsContainer || typeof window.switchTab !== 'function') return;

  // ── Tab button ──
  var tabBtn = document.createElement('button');
  tabBtn.className = 'tab-btn';
  tabBtn.setAttribute('onclick', "switchTab('presenca')");
  tabBtn.textContent = 'Presença';
  tabsContainer.appendChild(tabBtn);

  // ── Tab content ──
  var tabContent = document.createElement('div');
  tabContent.className = 'tab-content';
  tabContent.id = 'tab-presenca';
  var allTabContents = document.querySelectorAll('.tab-content');
  var lastTabContent = allTabContents[allTabContents.length - 1];
  if (lastTabContent && lastTabContent.parentNode) {
    lastTabContent.parentNode.insertBefore(tabContent, lastTabContent.nextSibling);
  }

  tabContent.innerHTML = '<div style="text-align:center;padding:3rem;"><div style="width:32px;height:32px;border:3px solid #e5e5e0;border-top-color:#003080;border-radius:50%;animation:spin .7s linear infinite;margin:0 auto 1rem;"></div><p style="font:500 .9rem/1.5 \'Inter\',sans-serif;color:#777;">Carregando presença...</p></div>';

  // ── Styles ──
  var style = document.createElement('style');
  style.textContent = [
    '.pz-header-row { display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:1rem;margin-bottom:1rem; }',
    '.pz-title { font:600 1.4rem/1.3 "Cormorant Garamond",Georgia,serif;color:#1a1a2e; }',
    '.pz-subtitle { font:400 .88rem/1.5 "Inter",sans-serif;color:#777;max-width:60ch; }',
    '.pz-seg { display:inline-flex;border:1px solid #d4d4cc;border-radius:8px;overflow:hidden; }',
    '.pz-seg button { font:600 .8rem/1 "Inter",sans-serif;border:0;background:#fff;color:#555;padding:0 14px;min-height:40px;cursor:pointer; }',
    '.pz-seg button + button { border-left:1px solid #d4d4cc; }',
    '.pz-seg button.on { background:#003080;color:#fff; }',
    '.pz-seg button:focus-visible { outline:3px solid #d70c0c;outline-offset:-3px; }',
    '.pz-stats { display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-bottom:1rem; }',
    '.pz-stat { background:#fff;border:1px solid #d4d4cc;border-radius:12px;padding:1rem 1.1rem;box-shadow:0 2px 8px rgba(0,0,0,.04); }',
    '.pz-stat .l { font:600 .68rem/1.3 "Inter",sans-serif;text-transform:uppercase;letter-spacing:.6px;color:#777; }',
    '.pz-stat .v { font:700 1.6rem/1.2 "Inter",sans-serif;color:#1a1a2e;margin-top:.3rem; }',
    '.pz-stat.aula .v { color:#2f6b2f; } .pz-stat.falta .v { color:#b3261e; }',
    '.pz-card { background:#fff;border:1px solid #d4d4cc;border-radius:12px;padding:.4rem 1.4rem;box-shadow:0 2px 8px rgba(0,0,0,.04); }',
    '.pz-item { display:flex;align-items:center;gap:1rem;padding:.8rem .2rem;border-bottom:1px solid #e8e8e0; }',
    '.pz-item:last-child { border-bottom:none; }',
    '.pz-date { display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:54px;height:54px;background:#f1f1ec;color:#1a1a2e;border-radius:10px;flex-shrink:0; }',
    '.pz-date .d { font:700 1.1rem/1 "Inter",sans-serif; }',
    '.pz-date .m { font:600 .66rem/1.3 "Inter",sans-serif;text-transform:uppercase;letter-spacing:.5px;color:#666; }',
    '.pz-info { flex:1;min-width:0;font:400 .85rem/1.4 "Inter",sans-serif;color:#555; }',
    '.pz-info b { display:block;font-weight:600;color:#2d2d3a;font-size:.92rem; }',
    '.pz-chip { font:600 .75rem/1 "Inter",sans-serif;padding:7px 11px;border-radius:20px;flex-shrink:0;white-space:nowrap; }',
    '.pz-chip.aula { background:#e6f0e3;color:#2f6b2f; }',
    '.pz-chip.falta { background:#f8e3e1;color:#b3261e; }',
    '.pz-chip.sem_registro, .pz-chip.sem_texto { background:#efefea;color:#666; }',
    '.pz-link { font:600 .78rem/1.4 "Inter",sans-serif;color:#003080;text-decoration:underline;flex-shrink:0; }',
    '.pz-link:focus-visible { outline:3px solid #d70c0c;outline-offset:2px; }',
    '.pz-note { font:400 .78rem/1.5 "Inter",sans-serif;color:#777;margin-top:.9rem; }',
    '.pz-empty { text-align:center;padding:2.5rem 1rem;color:#777;font:500 .9rem/1.6 "Inter",sans-serif; }',
    '.pz-alert { background:#f8e3e1;color:#8c1d16;border-radius:10px;padding:.8rem 1rem;font:500 .85rem/1.5 "Inter",sans-serif;margin-bottom:1rem; }',
    '@media (max-width:768px) {',
    '  .pz-stats { grid-template-columns:repeat(2,1fr); }',
    '  .pz-item { flex-wrap:wrap;column-gap:.8rem;row-gap:.5rem; }',
    '  .pz-info { flex:1 1 calc(100% - 70px); }',
    '  .pz-chip { margin-left:calc(54px + .8rem); }',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  var DADOS = null, DIAS = 30;
  var NOME = { aula: 'Aula', falta: 'Falta', sem_registro: 'Sem registro', sem_texto: 'Sem registro' };

  load();

  async function load() {
    try {
      var r = await fetch(API + '?slug=' + encodeURIComponent(slugAluno), { cache: 'no-store' });
      var j = await r.json();
      if (!j.ok) throw new Error(j.error || ('HTTP ' + r.status));
      DADOS = j;
      render();
    } catch (err) {
      console.error('Presença error:', err);
      tabContent.innerHTML = '<div class="pz-empty">Não consegui carregar a presença agora. Tente de novo mais tarde.</div>';
    }
  }

  function render() {
    var header = '<div class="pz-header-row"><div>' +
      '<div class="pz-title">Presença</div>' +
      '<div class="pz-subtitle">Dias em que a sala do Zoom deste aluno abriu e o que aconteceu em cada um. Esta aba aparece só no link do professor.</div>' +
      '</div>' +
      '<div class="pz-seg" role="group" aria-label="Período">' +
        [30, 60, 90].map(function(n) { return '<button type="button" data-d="' + n + '"' + (n === DIAS ? ' class="on" aria-pressed="true"' : ' aria-pressed="false"') + '>' + n + ' dias</button>'; }).join('') +
      '</div></div>';

    var a = DADOS.aluno;
    if (!a) {
      tabContent.innerHTML = header + '<div class="pz-card"><div class="pz-empty">Este aluno ainda não tem sala do Zoom acompanhada pelo sistema de análise de aulas.</div></div>';
      liga();
      return;
    }

    var corte = new Date(Date.parse(DADOS.ate) - (DIAS - 1) * 864e5).toISOString().slice(0, 10);
    var dias = a.dias.filter(function(x) { return x.d >= corte; }).reverse();
    var n = { aula: 0, falta: 0 };
    dias.forEach(function(x) { if (n[x.s] != null) n[x.s]++; });
    var base = n.aula + n.falta;
    var pct = base ? Math.round(100 * n.aula / base) + '%' : '—';

    var alerta = a.sala_existe === false
      ? '<div class="pz-alert">A sala do Zoom cadastrada para este aluno foi apagada. Se ele tem sala nova, avise a coordenação para atualizar o link.</div>' : '';

    var stats = '<div class="pz-stats">' +
      '<div class="pz-stat aula"><div class="l">Aulas</div><div class="v">' + n.aula + '</div></div>' +
      '<div class="pz-stat falta"><div class="l">Faltas</div><div class="v">' + n.falta + '</div></div>' +
      '<div class="pz-stat"><div class="l">Presença</div><div class="v">' + pct + '</div></div>' +
      '<div class="pz-stat"><div class="l">Última aula</div><div class="v">' + (a.ultima_aula ? escHTML(br(a.ultima_aula)) : '—') + '</div></div>' +
      '</div>';

    var lista = dias.length ? dias.map(function(x) {
      var d = new Date(x.d + 'T12:00:00Z');
      var link = x.s === 'aula' && x.id
        ? '<a class="pz-link" href="' + escAttrHTML(ANALISE_BASE + '/resumo/' + encodeURIComponent(slugAluno.replace(/-/g, '') + '-aula' + x.d.slice(8, 10) + '-' + x.d.slice(5, 7)) + '?id=' + encodeURIComponent(x.id)) + '" target="_blank" rel="noopener" aria-label="Ver resumo da aula de ' + escAttrHTML(br(x.d)) + '">Ver resumo</a>' : '';
      return '<div class="pz-item">' +
        '<div class="pz-date" aria-hidden="true"><span class="d">' + x.d.slice(8, 10) + '</span><span class="m">' + escHTML(fmt(d, { month: 'short' }).replace('.', '')) + '</span></div>' +
        '<div class="pz-info"><b>' + escHTML(cap(fmt(d, { weekday: 'long' }))) + ', ' + escHTML(br(x.d)) + '</b>' + (x.h ? 'Sala abriu às ' + escHTML(x.h) : '') + '</div>' +
        '<span class="pz-chip ' + escAttrHTML(x.s) + '">' + escHTML(NOME[x.s] || x.s) + '</span>' + link +
      '</div>';
    }).join('') : '<div class="pz-empty">Nenhuma sessão da sala nos últimos ' + DIAS + ' dias.</div>';

    var gerado = new Date(DADOS.gerado_em).toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo', day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' });
    var nota = '<div class="pz-note"><b>Falta</b>: a sala ficou aberta 10 minutos ou mais e só uma pessoa entrou (ou ninguém falou). ' +
      '<b>Sem registro</b>: a sala abriu, mas não ficou gravação para saber. Sala aberta por menos de 10 minutos não conta. ' +
      'Presença = aulas ÷ (aulas + faltas). Dados até ' + escHTML(br(DADOS.ate)) + ', atualizados em ' + escHTML(gerado) + '.</div>';

    tabContent.innerHTML = header + alerta + stats + '<div class="pz-card">' + lista + '</div>' + nota;
    liga();
  }

  function liga() {
    var seg = tabContent.querySelector('.pz-seg');
    if (!seg) return;
    seg.addEventListener('click', function(e) {
      var b = e.target.closest('button');
      if (!b) return;
      DIAS = Number(b.getAttribute('data-d'));
      render();
    });
  }

  function br(d) { return d.slice(8, 10) + '/' + d.slice(5, 7); }
  function fmt(d, opts) { return d.toLocaleDateString('pt-BR', Object.assign({ timeZone: 'America/Sao_Paulo' }, opts)); }
  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : ''; }
  function escHTML(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }
  function escAttrHTML(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

})();
